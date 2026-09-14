import tempfile
import unittest
from pathlib import Path

from software.backend.loomforge.recipe import RecipeError, load_recipe
from software.backend.loomforge.repository import JobRepository
from software.backend.loomforge.sim import SimulationAdapter
from software.backend.loomforge.state import StateError, transition
from software.backend.loomforge.models import MachineState
from software.backend.loomforge.report import export_report
from software.backend.loomforge.machine import MachineConfiguration
from software.backend.loomforge.protocol import ControllerCommand, ProtocolError
from uuid import uuid4

ROOT = Path(__file__).parents[1]

class LoomForgeTests(unittest.TestCase):
    def setUp(self): self.recipe = load_recipe(ROOT / "recipes/examples/mini_fit_4c.json")
    def test_valid_recipe(self): self.assertEqual(self.recipe.cavity_count, 4)
    def test_duplicate_cavity_is_rejected(self):
        with self.assertRaises(RecipeError): load_recipe(ROOT / "recipes/invalid/duplicate_cavity.json")
    def test_unsafe_transition_is_rejected(self):
        with self.assertRaises(StateError): transition(MachineState.READY, MachineState.ASSEMBLING)
    def test_successful_simulated_job_persists(self):
        job = SimulationAdapter().run(self.recipe)
        self.assertEqual(job.disposition, "PASS")
        with tempfile.TemporaryDirectory() as d:
            repo = JobRepository(Path(d) / "jobs.sqlite"); repo.save(job)
            self.assertEqual(repo.get(job.job_id)["mode"], "SIMULATED")
    def test_wrong_connection_fails(self):
        job = SimulationAdapter().run(self.recipe, "incorrect_connection")
        self.assertEqual(job.disposition, "FAIL")
        self.assertEqual(job.electrical_results["wrong_mapping"][0]["wire"], "W2")
    def test_estop_requires_recovery(self):
        job = SimulationAdapter().run(self.recipe, "estop")
        self.assertEqual(job.state, "ESTOP")
        self.assertEqual(job.disposition, "INCOMPLETE")
    def test_all_declared_faults_preserve_nonpass_disposition(self):
        for scenario in ("missing_wire", "terminal_misalignment", "excessive_resistance", "partial_seating", "short_circuit", "fixture_mismatch", "door_open", "force_sensor_dropout", "controller_disconnect", "power_interruption"):
            self.assertNotEqual(SimulationAdapter().run(self.recipe, scenario).disposition, "PASS", scenario)
    def test_export_preserves_simulation_notice(self):
        with tempfile.TemporaryDirectory() as d:
            repo = JobRepository(Path(d) / "jobs.sqlite"); job = SimulationAdapter().run(self.recipe); repo.save(job)
            output = export_report(repo, job.job_id, Path(d) / "job-report.json")
            self.assertIn("SIMULATION", output.read_text())
    def test_machine_coordinates_are_recipe_bound(self):
        machine = MachineConfiguration()
        machine.validate_recipe_reach(self.recipe)
        self.assertEqual(machine.cavity_approach(4).x_mm, 4.2)
        self.assertEqual(machine.tray_pickup(self.recipe.wires[1]).x_mm, -117.0)
    def test_protocol_rejects_raw_motion(self):
        message = {"command_id":str(uuid4()), "protocol_version":"1.0", "command":"START_JOB", "expected_state":"READY", "units":{"distance":"mm","speed":"mm/s","force":"N","time":"ms"}, "payload":{"coordinates":[1,2,3]}}
        with self.assertRaises(ProtocolError): ControllerCommand.parse(message)
    def test_protocol_accepts_bounded_start(self):
        command = ControllerCommand.parse({"command_id":str(uuid4()), "protocol_version":"1.0", "command":"START_JOB", "expected_state":"READY", "units":{"distance":"mm","speed":"mm/s","force":"N","time":"ms"}, "payload":{"recipe_digest":"abc", "operator_confirmation":True}})
        self.assertEqual(command.command.value, "START_JOB")

if __name__ == "__main__": unittest.main()
