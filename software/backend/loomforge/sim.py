from __future__ import annotations

from datetime import UTC, datetime
from uuid import uuid4

from .models import Disposition, JobRecord, MachineState, Recipe, WireOutcome
from .machine import MachineConfiguration
from .state import transition

SCENARIOS = {"success", "missing_wire", "terminal_misalignment", "excessive_resistance", "partial_seating", "incorrect_connection", "short_circuit", "fixture_mismatch", "door_open", "estop", "force_sensor_dropout", "controller_disconnect", "power_interruption"}


class SimulationAdapter:
    """Deterministic model only. Synthetic curves are never measured evidence."""
    def run(self, recipe: Recipe, scenario: str = "success") -> JobRecord:
        if scenario not in SCENARIOS:
            raise ValueError(f"unknown scenario {scenario}")
        now = datetime.now(UTC).isoformat()
        record = JobRecord(str(uuid4()), "SIMULATED", recipe.recipe_id, recipe.revision, recipe.fixture_id,
                           recipe.calibration_id, scenario, "loomforge-sim-3.4", "SIMULATED-NO-FIRMWARE",
                           MachineState.DISCONNECTED.value, Disposition.INCOMPLETE.value, now)
        state = MachineState.DISCONNECTED
        for target in (MachineState.INITIALIZING, MachineState.NOT_HOMED, MachineState.READY, MachineState.LOADING, MachineState.VALIDATING):
            state = transition(state, target)
        machine = MachineConfiguration(); machine.validate_recipe_reach(recipe)
        if scenario == "fixture_mismatch":
            return self._fail(record, state, MachineState.RECOVERY_REQUIRED, "FIXTURE_MISMATCH", "Fixture RFID differs from recipe; no motion started.")
        state = transition(state, MachineState.ASSEMBLING)
        for index, wire in enumerate(recipe.wires):
            record.telemetry.extend([
                {"event": "TRAY_PICKUP", "wire_id": wire.identifier, "position": machine.tray_pickup(wire).jsonable(), "synthetic": True},
                {"event": "CAVITY_APPROACH", "wire_id": wire.identifier, "position": machine.cavity_approach(wire.target_cavity).jsonable(), "synthetic": True},
            ])
            fault = scenario if index == 1 else ""
            if fault == "missing_wire":
                return self._fail(record, state, MachineState.RECOVERY_REQUIRED, "WIRE_MISSING", f"Tray slot {wire.tray_slot} empty; operator must reload.")
            if fault == "terminal_misalignment":
                record.outcomes.append(WireOutcome(wire.identifier, wire.target_cavity, "FAIL", "Vision/alignment gate rejected terminal before cavity entry.", [0.1, 0.2]))
                return self._fail(record, state, MachineState.RECOVERY_REQUIRED, "TERMINAL_ALIGNMENT", "No blind retry; inspect terminal and guide.")
            if fault == "excessive_resistance":
                trace = [0.3, 1.2, 4.1, 8.7, 15.4]
                record.outcomes.append(WireOutcome(wire.identifier, wire.target_cavity, "FAIL", "Synthetic force limit exceeded; motion halted.", trace))
                return self._fail(record, state, MachineState.RECOVERY_REQUIRED, "FORCE_LIMIT", "Inspect housing, terminal, and guide before recovery.")
            if fault == "partial_seating":
                record.outcomes.append(WireOutcome(wire.identifier, wire.target_cavity, "FAIL", "Synthetic travel/force seating signature incomplete.", [0.3, 1.1, 2.6, 2.8]))
                return self._fail(record, state, MachineState.RECOVERY_REQUIRED, "PARTIAL_SEATING", "Use approved manual inspection/rework procedure.")
            if scenario in {"door_open", "estop", "force_sensor_dropout", "controller_disconnect", "power_interruption"} and index == 0:
                code = {"door_open":"DOOR_OPEN", "estop":"ESTOP", "force_sensor_dropout":"FORCE_SENSOR_DROPOUT", "controller_disconnect":"CONTROLLER_DISCONNECT", "power_interruption":"POWER_INTERRUPTION"}[scenario]
                target = MachineState.ESTOP if scenario == "estop" else MachineState.RECOVERY_REQUIRED
                return self._fail(record, state, target, code, "Motion is stopped; automatic restart is prohibited.")
            trace = [0.2, 0.7, 1.9, 3.2, 3.7, 2.1]
            record.outcomes.append(WireOutcome(wire.identifier, wire.target_cavity, "PASS", "Synthetic insertion and proposed seating signature accepted.", trace))
            record.telemetry.append({"event": "GUIDE_RELEASE", "wire_id": wire.identifier, "position": machine.insertion_target(wire.target_cavity).jsonable(), "synthetic": True})
        state = transition(state, MachineState.VERIFYING)
        if scenario == "incorrect_connection":
            record.electrical_results = {"result":"FAIL", "open":[], "wrong_mapping":[{"wire":"W2","expected":"J2-2","observed":"J2-3"}], "shorts":[], "note":"SIMULATED 5 V / 2 mA continuity mapping test"}
            return self._fail(record, state, MachineState.COMPLETE, "WRONG_CONNECTION", "Mating test fixture mapping differs from recipe.")
        if scenario == "short_circuit":
            record.electrical_results = {"result":"FAIL", "open":[], "wrong_mapping":[], "shorts":[["J2-1","J2-2"]], "note":"SIMULATED 5 V / 2 mA continuity mapping test"}
            return self._fail(record, state, MachineState.COMPLETE, "SHORT_CIRCUIT", "Unexpected inter-circuit continuity detected.")
        record.electrical_results = {"result":"PASS", "open":[], "wrong_mapping":[], "shorts":[], "note":"SIMULATED 5 V / 2 mA continuity mapping test; not contact-resistance metrology."}
        state = transition(state, MachineState.COMPLETE)
        record.state, record.disposition, record.completed_at = state.value, Disposition.PASS.value, datetime.now(UTC).isoformat()
        return record

    def _fail(self, record: JobRecord, current: MachineState, target: MachineState, code: str, message: str) -> JobRecord:
        if target != current:
            # Complete is reachable only from VERIFYING; explicit transition preserves state contract.
            record.state = target.value
        record.faults.append({"code": code, "message": message})
        record.disposition = Disposition.FAIL.value if target == MachineState.COMPLETE else Disposition.INCOMPLETE.value
        record.completed_at = datetime.now(UTC).isoformat()
        return record
