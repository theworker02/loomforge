# SC-A0 manufacturing plan - proposed M1 pilot

## Purpose and boundary

SC-A0 is LoomForge's proposed **supply-chain and manufacturing-package baseline A0**: enough controlled structure for a receiving manufacturer to quote, plan, build, and verify a limited pilot, but not a production release. It covers the proposed 12-unit M1 manufacturer pilot for LF-P1-R02. It does not authorize fabrication, operation, certification, or customer deployment.

The receiving manufacturer remains responsible for component sourcing, substitutions, independent safety review, fabrication, assembly, calibration, physical verification, applicable compliance assessment, training, and production approval.

## M1 pilot objective

Build 12 traceable development units to establish assembly feasibility, inspectability, service access, guide/fixture repeatability, and the correlation of proposed software/simulator behavior with controlled bench evidence. The M1 pilot is not intended to establish production yield, reliability, or safety compliance.

| Phase | Gate | Evidence required | Decision |
|---|---|---|---|
| SC-A0 package freeze | `A0-R` | released BOM framework, approved RFQ package, DFM risk review | authorize supplier quotation only |
| First article | `FA-1` | one assembled non-operational mechanical unit, dimensional/fit report | resolve geometry/tool-access issues |
| Mechanism verification | `DV-M` | controlled guide/insertion tests, force calibration, inspected terminals/housings | authorize remaining M1 assembly or stop |
| M1 completion | `M1-C` | 12 completed travelers, nonconformance log, configuration audit | evaluate next engineering revision |

## Proposed unit allocation

| Units | Purpose | Allowed use |
|---|---|---|
| M1-001 to M1-002 | fixture/guide engineering first articles | setup, destructive/inspection correlation only |
| M1-003 to M1-006 | mechanism and electrical test development | supervised validation only |
| M1-007 to M1-010 | operator flow/changeover studies | supervised non-production evaluation |
| M1-011 to M1-012 | retained configuration/reference units | serviceability and regression checks |

The quantity is a planning target. It must be revisited after first-article findings; do not continue assembly merely to reach twelve units.

## Build sequence and controls

1. Confirm configuration baseline, supplier drawings, approved alternates, and incoming-inspection criteria.
2. Procure long-lead purchased parts only after responsible-engineer review; do not substitute connector, safety, or force-sensing components without a recorded change.
3. Fabricate frame/panels, machine datum-bearing parts, and prototype tray/comb items; record material and revision traceability.
4. Build M1-001 first through the controlled traveler. Perform dimensional/fit review before electrical integration.
5. Complete guard/interlock, safe-state, force-sensor, fixture-ID, and test-fixture checks before any guided insertion trial.
6. Run verification gates; record all failures, rework, substitutions, and deviations against unit serial number.
7. Build later units only with approved deviation disposition. Preserve failed/incomplete evidence.

## Required records

- M1 serial number, configuration revision, BOM revision, and software/firmware identifiers.
- Receiving inspection, material certifications where required by the receiving manufacturer, and approved substitutes.
- Traveler signoffs, torque/assembly records, calibration certificates, test results, deviations, rework, and photographs.
- DFM-risk and nonconformance closure status.

## Stop conditions

Stop the affected unit/pilot phase for uncontrolled safety function, fixture datum loss, force-sensor out-of-calibration, connector/terminal mismatch, damaged terminal/housing, unapproved substitution, or any result that cannot establish intended test status. No automatic waiver exists.
