"""Machine configuration and bounded coordinate derivation for LF-P1-R02."""
from __future__ import annotations

import json
from dataclasses import dataclass
from pathlib import Path

from .models import Recipe, Wire


@dataclass(frozen=True)
class Position:
    x_mm: float
    y_mm: float
    z_mm: float

    def jsonable(self) -> dict[str, float]:
        return {"x_mm": self.x_mm, "y_mm": self.y_mm, "z_mm": self.z_mm}


class MachineConfiguration:
    """A recipe can select cavities, never arbitrary machine positions."""
    configuration_id = "LF-P1-R02"
    fixture_origin = Position(0.0, -92.0, 151.0)
    tray_origin = Position(-143.0, -174.0, 158.0)

    def __init__(self, parameters_path: str | Path | None = None):
        path = Path(parameters_path) if parameters_path else Path(__file__).parents[3] / "hardware/mechanical/source/parameters.json"
        self.parameters = json.loads(path.read_text(encoding="utf-8"))
        self.motion = self.parameters["motion"]
        self.tray_pitch = float(self.parameters["fixture"]["tray_pitch"])
        self.max_x = float(self.parameters["work_envelope"]["x"])
        self.max_y = float(self.parameters["work_envelope"]["y"])
        self.max_z = float(self.parameters["work_envelope"]["z"])

    def tray_pickup(self, wire: Wire) -> Position:
        if not 1 <= wire.tray_slot <= int(self.parameters["fixture"]["tray_slots"]):
            raise ValueError("tray slot outside physical tray")
        return Position(self.tray_origin.x_mm + (wire.tray_slot - 1) * self.tray_pitch, self.tray_origin.y_mm, self.tray_origin.z_mm)

    def cavity_approach(self, cavity: int) -> Position:
        if cavity not in {1, 2, 3, 4}:
            raise ValueError("unsupported cavity")
        # Four-circuit Mini-Fit Jr pattern: two rows, recipe convention from connector-selection.md.
        column = (cavity - 1) % 2
        row = (cavity - 1) // 2
        return Position(self.fixture_origin.x_mm + column * 4.2, self.fixture_origin.y_mm - row * 4.2, self.fixture_origin.z_mm + 18.0)

    def insertion_target(self, cavity: int) -> Position:
        approach = self.cavity_approach(cavity)
        return Position(approach.x_mm, approach.y_mm, approach.z_mm - 32.0)

    def validate_recipe_reach(self, recipe: Recipe) -> None:
        for wire in recipe.wires:
            pickup, target = self.tray_pickup(wire), self.insertion_target(wire.target_cavity)
            if abs(pickup.x_mm - self.fixture_origin.x_mm) > self.max_x or abs(target.y_mm - self.fixture_origin.y_mm) > self.max_y or abs(target.z_mm - self.fixture_origin.z_mm) > self.max_z:
                raise ValueError(f"wire {wire.identifier} is outside the released conceptual envelope")
