# M1 process control and inspection plan

**Document:** LF-QA-001 · **Revision:** A0 (proposed) · **Status:** proposed engineering controls, not a certified quality system

| Step | Characteristic / failure prevented | Method & equipment | Frequency | Record | Reaction plan |
|---|---|---|---|---|---|
| Receiving: connector system | correct housing, terminal, test plug; revision/lot condition | part-number, label, packaging and visible-condition inspection | every lot | receiving log | quarantine lot; connector/fixture review |
| Receiving: motion/sensor | correct travel/load/rating; damage | PO/datasheet and visual interface check | every item/lot | receiving log | hold substitution/damage |
| Fabrication: datum parts | hole pattern, datum faces, burrs, material | drawing-based inspection with suitable metrology | first article + defined sample | FAI record | stop lot; NCR / rework route |
| Fabrication: sheet parts | bend geometry, access, edge condition | fabricator first article against datum scheme | first article | panel FAI | correct flat pattern or bracket design |
| Assembly: structure | accessible joints, stable feet, guard fit | traveler visual/torque/access check | every unit | traveler | hold/rework |
| Assembly: motion | guide alignment, cable clearance, hard stops | dry motion at documented extremes | every unit | traveler/calibration record | stop integration; correct alignment/routing |
| Assembly: protective functions | E-stop/interlock/no restart | manufacturer-qualified functional procedure | every configuration change and unit | safety-test record | no powered use; investigate |
| Calibration | force zero/known load, coordinate datum, camera/test fixture | controlled calibration procedure | before controlled trials; after relevant change | calibration record | mark unavailable; do not pass jobs |
| Insertion study | terminal/housing damage, traceability, seating correlation | force trace + approved inspection method | per defined DV sample | job and inspection record | preserve sample; NCR; no blind retry |
| Electrical verification | open, mis-map, short detection and fixture health | self-test/reference + fault coupons | before run / per DV plan | test report | reject inconclusive result; service fixture |
| Final configuration | known as-built unit and outstanding issues | traveler/document audit | every unit | configuration audit | restricted use or hold |

## Measurement-system boundary

No measurement result may be represented as traceable, accurate, or capability-qualified without the receiving manufacturer defining the instrument, resolution, calibration status, method uncertainty, environmental conditions, and operator training. The electrical test is a connection-mapping check; it is not precision contact-resistance metrology.
