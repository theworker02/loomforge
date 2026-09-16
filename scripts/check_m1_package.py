"""Check document presence and 12-unit arithmetic for the SC-A0 M1 handoff.

This is intentionally not a substitute for supplier, CAD, safety, or physical
verification; it only prevents a basic package-consistency error.
"""

from __future__ import annotations

import csv
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
REQUIRED_DOCS = (
    "docs/manufacturing/sc-a0-manufacturing-plan.md",
    "docs/manufacturing/supplier-rfq-package.md",
    "docs/manufacturing/design-verification-plan.md",
    "docs/manufacturing/m1-pilot-traveler.md",
    "docs/manufacturing/dfm-risk-register.md",
    "docs/manufacturing/m1-manufacturer-pilot-package.md",
    "docs/manufacturing/configuration-management-plan.md",
    "docs/manufacturing/quality-control-plan.md",
    "docs/manufacturing/first-article-inspection-template.md",
    "docs/manufacturing/nonconformance-and-capa.md",
    "docs/manufacturing/m1-pilot-execution-plan.md",
    "docs/manufacturing/interface-control-register.md",
    "docs/manufacturing/supplier-evaluation-framework.md",
    "docs/manufacturing/m1-cost-and-capacity-framework.md",
    "docs/manufacturing/pilot-work-instructions.md",
    "docs/manufacturing/calibration-and-test-records.md",
    "docs/manufacturing/supplier-data-package-requirements.md",
    "docs/manufacturing/m1-release-review-checklist.md",
    "hardware/bom/m1-rfq-line-items.csv",
)


def main() -> int:
    missing = [path for path in REQUIRED_DOCS if not (ROOT / path).is_file()]
    if missing:
        raise SystemExit(f"missing required M1 package files: {', '.join(missing)}")
    with (ROOT / "hardware/bom/m1-bom-framework.csv").open(newline="", encoding="utf-8") as source:
        rows = list(csv.DictReader(source))
    numbers = [row["part_number"] for row in rows]
    if not rows or len(numbers) != len(set(numbers)):
        raise SystemExit("M1 BOM framework is empty or has duplicate part numbers")
    for row in rows:
        if int(row["pilot_build_qty_12"]) != int(row["per_unit_qty"]) * 12:
            raise SystemExit(f"12-unit arithmetic error at {row['part_number']}")
    print(f"SC-A0 M1 package check passed ({len(rows)} BOM lines).")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
