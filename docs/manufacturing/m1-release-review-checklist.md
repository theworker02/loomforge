# M1 gate and release-review checklist

**Document:** LF-REV-001 · **Revision:** A0 (proposed)

This checklist controls decisions, not hardware. Completion means the stated evidence is reviewed; it does not confer production, safety, or regulatory approval.

| Gate | Required decision evidence | Outcome options |
|---|---|---|
| A0-R: quote baseline | BOM line ownership, RFQ scope, interface register, DFM risk review, document revisions | quote / revise / stop |
| FA-1: first article | FAI, assembly-access findings, fabrication deviations, updated DFM risks | build one more / revise / stop |
| DV-M: mechanism | force calibration, guide/fixture observations, damage/seating evidence, sensor/overload behavior | limited next-wave test / redesign / stop |
| DV-E: electrical/control | reference fixture results, fault matrix, state/protocol test evidence, preserved failure records | supervised workflow tests / revise / stop |
| M1-C: pilot closeout | all travelers, as-built audit, NCR/CAPA status, lessons learned, retained-unit records | define next development revision / repeat study / stop |

### Required reviewer roles

- Responsible mechanical/fixture engineer
- Electrical/controls engineer
- Test/metrology owner
- Manufacturing/quality owner
- Manufacturer-appointed machinery safety authority for any energized or safeguarded operation

Any reviewer may place a gate on hold. A hold requires written evidence-based disposition; schedule pressure is not a disposition.
