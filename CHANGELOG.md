# Changelog

All notable changes are recorded here. This project is a development design package; entries do not indicate physical validation or production release.

## [3.5] - 2026-09-15

### Added

- SC-A0 / M1 manufacturer handoff expansion: configuration management, process control, first-article template, nonconformance/CAPA procedure, supplier-evaluation framework, cost/capacity framework, interface-control register, and staged pilot execution plan.
- A proposed serialized 12-unit M1 traveler, DFM risk register, RFQ line-item index, and machine-readable 12-unit BOM consistency check.
- Pilot work instructions, calibration/test record forms, supplier data requirements, and an evidence-based gate-review checklist.

### Changed

- The manufacturer pilot package now explicitly gates later build waves on first-article and controlled verification evidence rather than treating a 12-unit count as a pass.

## [3.4] - 2026-09-14

### Added

- GitHub Pages static engineering-package site and deployment workflow.
- Repository funding configuration placeholder, contribution/security/governance documents.
- MIT License for the repository, attributed to theworker02 and Magnexis, plus trademark/no-endorsement guidance.
- Bounded controller-protocol contract that rejects raw motion and invalid state/unit messages.
- LF-P1-R02 coordinate derivation shared by recipe reach checks and synthetic simulator telemetry.
- `loomforge validate` and `loomforge scenarios` CLI workflows.
- LF-P1-R02 design package, OpenSCAD export, technical views, motion demonstration, and design-review PDF.

### Changed

- Established plans-only supply and manufacturer-led validation boundaries throughout the package.
