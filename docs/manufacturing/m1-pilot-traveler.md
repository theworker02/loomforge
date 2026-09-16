# M1 pilot build traveler — LF-P1-R02

**Document:** LF-MFG-TRV-001
**Revision:** A0 (proposed)
**Applies to:** a single serialized unit in the proposed 12-unit M1 manufacturer pilot
**Disposition:** engineering-development record; not a production traveler or conformity certificate

> **Plans-only scope of supply.** LoomForge supplies engineering plans, digital design files, software, and supporting documentation only. No physical machine or assembled equipment is supplied. The receiving manufacturer or its appointed machine builder must procure or fabricate the parts, assemble the equipment, and complete the necessary engineering review, safety assessment, calibration, testing, and application-specific validation before use.

Print or copy this traveler once for every unit (`M1-001` through `M1-012`). Attach objective evidence by reference; do not replace an incomplete step with a verbal sign-off.

## 1. Unit identity and configuration

| Field | Record |
|---|---|
| Unit serial | `M1-___` |
| Traveler copy | `___ of ___` |
| Build start / completion (UTC) |  |
| Builder / reviewer |  |
| Mechanical CAD configuration | LF-P1-R02 / `____________` |
| Software / firmware identifiers | `____________` |
| Fixture cartridge ID | `____________` |
| Calibration record IDs | `____________` |
| BOM framework revision | `m1-bom-framework.csv / A0` |
| Deviation record IDs | `____________` |

**Hold point:** no build begins without a unique serial, released-for-pilot drawing register, and an approved deviation route for every unresolved interface.

## 2. Receiving and kitting

| Check | Acceptance record | Builder / date | Reviewer / date |
|---|---|---|---|
| Purchased parts match approved manufacturer / part number or recorded substitute | Receiving log / C of C if available |  |  |
| Motion components visually undamaged; travel and mounting interfaces inspected | Receiving inspection record |  |  |
| Safety-rated components selected by manufacturer and traceable | Part / lot record |  |  |
| Connector housing, terminal, and mating test interface are the specified parts | Incoming part record |  |  |
| Printed/prototype parts identified as prototype-only where applicable | Part labels / material record |  |  |
| Missing, substituted, or damaged items segregated | NCR or deviation ID |  |  |

**Stop condition:** an unreviewed safety, motion, fixture, connector, or force-sensing substitution blocks the affected build step.

## 3. Structure, enclosure, and access assembly

| Check | Acceptance record | Builder / date | Reviewer / date |
|---|---|---|---|
| Base, rear spine, and side supports assembled with accessible fasteners | Torque / assembly record |  |  |
| Adjustable feet set; unit does not rock on intended bench surface | Inspection result |  |  |
| Front loading deck, tray access, and fixture extraction clearance confirmed | Access check |  |  |
| Guard panel, hinges, retention, handle, and opening limit installed | Guard assembly check |  |  |
| Door interlock mounting is mechanically protected and repeatable | Interlock mounting check |  |  |
| Service panel can be removed without disturbing motion alignment | Service-access check |  |  |

## 4. Motion, insertion head, and wire-handling assembly

| Check | Acceptance record | Builder / date | Reviewer / date |
|---|---|---|---|
| X/Y guides and insertion axis installed to drawing datums | Alignment measurement |  |  |
| Cable chain/service loops clear all stated axis extremes | Manual dry-motion record |  |  |
| Force sensor mount and overload stop fitted; no bypass path observed | Assembly photo / inspection |  |  |
| Gripper jaws, terminal guide halves, and release clearance assembled | Functional dry-cycle record |  |  |
| Connector cartridge locates repeatably and its identifier is readable | Fixture repeatability record |  |  |
| Tray slots, terminal orientation features, and wire slack combs installed | Loading check |  |  |
| Representative illustrative wire path does not foul head, guard, or fixture during dry motion | Observation record |  |  |

**Hold point:** do not introduce terminals or energized motion until dry motion passes at all documented axis extremes and the guard behavior is verified.

## 5. Electrical build and protective functions

| Check | Acceptance record | Builder / date | Reviewer / date |
|---|---|---|---|
| External low-voltage supply, branch protection, disconnect, and grounding installed as reviewed | Wiring inspection |  |  |
| Motor, sensor, camera, lighting, and test-interface cables labelled at both ends | Cable schedule check |  |  |
| Wiring is strain-relieved and separated from moving mechanism as designed | Visual / motion check |  |  |
| Protective circuit / safety controller behavior reviewed by qualified manufacturer personnel | Review record |  |  |
| E-stop, door interlock, and controller watchdog reach documented safe state | Functional test record |  |  |
| No automatic restart occurs after E-stop, door event, controller reset, or power restoration | Functional test record |  |  |
| Work, vision, and status lighting are independently controllable; vision condition is documented | Lighting check |  |  |

## 6. Calibration and no-load commissioning

| Check | Acceptance record | Builder / date | Reviewer / date |
|---|---|---|---|
| Homing references and soft limits configured from reviewed machine limits | Configuration export |  |  |
| Coordinate datum from fixture to cavity map recorded | Calibration record |  |  |
| Tray pickup locations recorded | Calibration record |  |  |
| Force sensor zero and known-load check completed with traceable equipment | Calibration record |  |  |
| Camera focus, field of view, and illumination condition recorded | Calibration record |  |  |
| Test fixture self-test/reference path completed | Test-fixture record |  |  |

**Stop condition:** expired, missing, incompatible, or failed calibration blocks any claimed pass disposition.

## 7. Controlled insertion study and electrical verification

Use only the supported connector / terminal combination and approved engineering recipe. Each result is a **physical test result**, not evidence inferred from simulation.

| Check | Acceptance record | Builder / date | Reviewer / date |
|---|---|---|---|
| Recipe validation rejects duplicate cavity, incompatible part, unknown fixture, and calibration issues | Software evidence |  |  |
| Representative guided insertion performed with force trace retained | Job / trace IDs |  |  |
| Seating method is performed per manufacturer guidance; result and limitations recorded | Inspection record |  |  |
| Gripper and guide release without damaging wire/terminal in observed samples | Inspection record |  |  |
| Mating electrical fixture checks open, wrong-map, and short scenarios | Test report |  |  |
| A failed or interrupted job remains preserved in history | Job record |  |  |
| A protective event requires explicit recovery; stale UI cannot resume motion | Test record |  |  |

## 8. Disposition

| Disposition | Conditions | Authorization |
|---|---|---|
| **Development complete for this build step** | Required evidence exists; outstanding issues are logged | Engineering reviewer |
| **Restricted engineering use** | Known limits are communicated; only approved trials allowed | Manufacturer engineering authority |
| **Hold / rework** | Any safety, motion, force, seating, electrical, or traceability check is unresolved | Manufacturer engineering authority |
| **Do not use** | Damage, uncontrolled substitution, failed protective function, or unknown configuration | Manufacturer engineering authority |

Final disposition: `____________________`
Authorizing name / signature / date: `________________________________`

## 9. Evidence attachment index

| Attachment ID | Type | Description | Storage location / checksum |
|---|---|---|---|
|  | Photo |  |  |
|  | Calibration |  |  |
|  | Force trace |  |  |
|  | Electrical test |  |  |
|  | Deviation / NCR |  |  |

## Deviation rules

A deviation must state the affected part/interface, reason, risk, temporary controls, verification required, approver, and expiration. A pilot deviation does not update the design baseline until it has been reviewed and incorporated into the controlled package.
