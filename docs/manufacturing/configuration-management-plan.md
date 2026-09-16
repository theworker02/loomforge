# Configuration management plan — SC-A0 / M1

**Document:** LF-CFG-001 · **Revision:** A0 (proposed) · **Scope:** LF-P1-R02 proposed 12-unit M1 pilot

This is a development configuration-control plan, not a product lifecycle-management system or manufacturing release authority.

## Configuration item hierarchy

| Level | Controlled item | Identifier / baseline | Change authority before use |
|---|---|---|---|
| System | LoomForge workstation | LF-P1-R02 / SC-A0 | Receiving manufacturer’s responsible engineer |
| Assembly | plinth, spine, guard, motion, head, fixture, tray, electrical/test | BOM assembly field + drawing register | Mechanical/electrical owner as applicable |
| Part | make part or purchased component | `LF-xxx` or manufacturer P/N | Responsible owner plus safety/connector review where applicable |
| Software | backend, simulator, UI, protocol | Git commit + package version | Software owner; protocol regression evidence |
| Recipe | connector/wire assembly data | identity + revision + checksum | Applications/fixture owner |
| Calibration | datum, force, camera, test fixture | calibration record ID + expiry | Metrology/test owner |

## Baseline rule

Every traveler must name the CAD/drawing revision, BOM revision, software commit/version, recipe revision, fixture ID, and calibration references actually used. If any item is unknown, disposition is **hold**; it is not inferred from the latest files in a shared folder.

## Change classes

| Class | Example | Required action |
|---|---|---|
| Editorial | typo with no technical meaning | Record revision; peer review |
| Minor build | panel finish or non-datum label change | Impact review; update traveler/BOM if affected |
| Functional | guide profile, fixture datum, cable routing, gripper material | Engineering impact review, DFM update, affected verification rerun |
| Critical | guard/interlock, motion limits, force protection, connector/terminal, test method | Stop affected pilot units; cross-functional manufacturer approval and explicit re-verification |

## Deviation and waiver discipline

A deviation is time-limited permission to build/test a stated departure. It must contain baseline, unit(s), reason, risk, temporary controls, affected verification, approvers, and expiry. A waiver does not silently alter a released part. Repeated deviations are a design-change trigger.

## End-of-pilot audit

Before M1 completion, compare every traveler to the SC-A0 baseline, list all deviations/NCRs, identify the as-built configuration of retained units, and prevent an M2 claim until unresolved critical items have a documented disposition.
