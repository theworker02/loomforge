from __future__ import annotations

from dataclasses import asdict, dataclass, field
from enum import Enum
from typing import Any


class MachineState(str, Enum):
    DISCONNECTED = "DISCONNECTED"
    INITIALIZING = "INITIALIZING"
    NOT_HOMED = "NOT_HOMED"
    READY = "READY"
    LOADING = "LOADING"
    VALIDATING = "VALIDATING"
    ASSEMBLING = "ASSEMBLING"
    VERIFYING = "VERIFYING"
    COMPLETE = "COMPLETE"
    PAUSED = "PAUSED"
    FAULT = "FAULT"
    ESTOP = "ESTOP"
    RECOVERY_REQUIRED = "RECOVERY_REQUIRED"


class Disposition(str, Enum):
    PASS = "PASS"
    FAIL = "FAIL"
    INCOMPLETE = "INCOMPLETE"


@dataclass(frozen=True)
class Wire:
    identifier: str
    tray_slot: int
    target_cavity: int
    gauge_awg: int
    color: str
    terminal_part_number: str


@dataclass(frozen=True)
class Recipe:
    recipe_id: str
    revision: str
    connector_manufacturer: str
    connector_part_number: str
    terminal_part_number: str
    cavity_count: int
    cavity_view: str
    fixture_id: str
    calibration_id: str
    insertion_force_max_n: float
    seating_method: str
    expected_connectivity: dict[str, str]
    wires: tuple[Wire, ...]
    source_references: tuple[str, ...]


@dataclass
class WireOutcome:
    wire_id: str
    cavity: int
    status: str
    message: str
    force_trace_n: list[float] = field(default_factory=list)


@dataclass
class JobRecord:
    job_id: str
    mode: str
    recipe_id: str
    recipe_revision: str
    fixture_id: str
    calibration_id: str
    scenario: str
    software_id: str
    firmware_id: str
    state: str
    disposition: str
    started_at: str
    completed_at: str | None = None
    outcomes: list[WireOutcome] = field(default_factory=list)
    electrical_results: dict[str, Any] = field(default_factory=dict)
    faults: list[dict[str, str]] = field(default_factory=list)
    interventions: list[str] = field(default_factory=list)

    def jsonable(self) -> dict[str, Any]:
        return asdict(self)
