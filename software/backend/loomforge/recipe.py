from __future__ import annotations

import json
from pathlib import Path

from .models import Recipe, Wire

SUPPORTED_CONNECTOR = "39-01-2040"
SUPPORTED_TERMINAL = "39-00-0038"
SUPPORTED_FIXTURE = "LF-MFJ-4C-001"
SUPPORTED_CALIBRATION = "LF-CAL-2026-001"


class RecipeError(ValueError):
    pass


def load_recipe(path: str | Path) -> Recipe:
    with open(path, encoding="utf-8") as handle:
        return parse_recipe(json.load(handle))


def parse_recipe(data: dict) -> Recipe:
    required = {"recipe_id", "revision", "connector", "fixture_id", "calibration_id", "insertion", "wires", "expected_connectivity", "source_references"}
    missing = required - data.keys()
    if missing:
        raise RecipeError(f"missing required fields: {', '.join(sorted(missing))}")
    connector, insertion = data["connector"], data["insertion"]
    if connector.get("manufacturer") != "Molex" or connector.get("housing_part_number") != SUPPORTED_CONNECTOR:
        raise RecipeError("unsupported connector; only Molex 39-01-2040 is enabled")
    if connector.get("terminal_part_number") != SUPPORTED_TERMINAL:
        raise RecipeError("incompatible terminal for enabled fixture")
    if connector.get("cavity_count") != 4:
        raise RecipeError("fixture supports exactly four cavities")
    if data["fixture_id"] != SUPPORTED_FIXTURE:
        raise RecipeError("unknown fixture")
    if data["calibration_id"] != SUPPORTED_CALIBRATION:
        raise RecipeError("expired or incompatible calibration")
    max_force = float(insertion.get("force_max_n", 0))
    if not 0 < max_force <= 15.0:
        raise RecipeError("force_max_n must be >0 and <= 15.0 N for this validated envelope")
    wires = tuple(Wire(
        identifier=str(w["identifier"]), tray_slot=int(w["tray_slot"]), target_cavity=int(w["target_cavity"]),
        gauge_awg=int(w["gauge_awg"]), color=str(w["color"]), terminal_part_number=str(w["terminal_part_number"])
    ) for w in data["wires"])
    if not wires:
        raise RecipeError("at least one wire is required")
    cavities, slots, ids = set(), set(), set()
    for wire in wires:
        if wire.identifier in ids or wire.target_cavity in cavities or wire.tray_slot in slots:
            raise RecipeError("wire identifiers, tray slots, and cavity assignments must be unique")
        if wire.target_cavity not in {1, 2, 3, 4}:
            raise RecipeError(f"invalid cavity {wire.target_cavity}")
        if wire.tray_slot not in range(1, 13):
            raise RecipeError(f"invalid tray slot {wire.tray_slot}")
        if wire.gauge_awg not in {18, 20, 22, 24}:
            raise RecipeError(f"wire {wire.identifier} gauge outside proposed supported range")
        if wire.terminal_part_number != SUPPORTED_TERMINAL:
            raise RecipeError(f"wire {wire.identifier} has incompatible terminal")
        ids.add(wire.identifier); cavities.add(wire.target_cavity); slots.add(wire.tray_slot)
    connectivity = data["expected_connectivity"]
    if set(connectivity) != ids:
        raise RecipeError("expected_connectivity must contain every wire identifier exactly once")
    return Recipe(
        recipe_id=data["recipe_id"], revision=data["revision"], connector_manufacturer="Molex",
        connector_part_number=SUPPORTED_CONNECTOR, terminal_part_number=SUPPORTED_TERMINAL,
        cavity_count=4, cavity_view=connector.get("cavity_view", "mating face, latch up: 1-2 top, 3-4 bottom"),
        fixture_id=data["fixture_id"], calibration_id=data["calibration_id"], insertion_force_max_n=max_force,
        seating_method=insertion.get("seating_method", "TPA-free visual datum plus force/travel signature; proposed"),
        expected_connectivity=connectivity, wires=wires, source_references=tuple(data["source_references"]),
    )
