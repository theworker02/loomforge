from __future__ import annotations

import csv
from pathlib import Path
import unittest


ROOT = Path(__file__).resolve().parents[1]


class M1PackageTests(unittest.TestCase):
    def test_m1_bom_is_a_twelve_unit_framework(self) -> None:
        with (ROOT / "hardware/bom/m1-bom-framework.csv").open(newline="", encoding="utf-8") as source:
            rows = list(csv.DictReader(source))
        self.assertGreaterEqual(len(rows), 10)
        self.assertEqual(len({row["part_number"] for row in rows}), len(rows))
        for row in rows:
            self.assertEqual(int(row["pilot_build_qty_12"]), int(row["per_unit_qty"]) * 12)

    def test_m1_control_documents_exist(self) -> None:
        for path in (
            "docs/manufacturing/sc-a0-manufacturing-plan.md",
            "docs/manufacturing/supplier-rfq-package.md",
            "docs/manufacturing/design-verification-plan.md",
            "docs/manufacturing/m1-pilot-traveler.md",
            "docs/manufacturing/dfm-risk-register.md",
            "docs/manufacturing/configuration-management-plan.md",
            "docs/manufacturing/quality-control-plan.md",
            "docs/manufacturing/first-article-inspection-template.md",
            "docs/manufacturing/nonconformance-and-capa.md",
            "docs/manufacturing/m1-pilot-execution-plan.md",
            "docs/manufacturing/interface-control-register.md",
            "docs/manufacturing/pilot-work-instructions.md",
            "docs/manufacturing/calibration-and-test-records.md",
            "docs/manufacturing/supplier-data-package-requirements.md",
            "docs/manufacturing/m1-release-review-checklist.md",
        ):
            self.assertTrue((ROOT / path).is_file(), path)
