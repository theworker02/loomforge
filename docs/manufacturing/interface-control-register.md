# Critical interface-control register — LF-P1-R02

This register identifies interfaces that must be defined from released drawings and manufacturer data before fabrication. It deliberately avoids invented dimensions.

| Interface ID | From → to | Controlled characteristics | Verification | Change sensitivity |
|---|---|---|---|---|
| ICD-01 | Connector housing → fixture cartridge | housing datums, cavity orientation, retention, mating access | supplier drawing review + fixture FAI | critical |
| ICD-02 | Fixture cartridge → base plate | location, clamp/load path, repeatable removal | datum survey / removal cycles | critical |
| ICD-03 | Guide/gripper → terminal/wire | terminal envelope, lance clearance, insulation contact, release path | controlled insertion and damage study | critical |
| ICD-04 | Force sensor → insertion carriage | load axis, preload, overload stop, stiffness | calibration / overload functional check | critical |
| ICD-05 | Motion system → enclosure | travel, hard/soft limits, cable-service zone | dry travel at extremes | critical |
| ICD-06 | Guard/door → protective circuit | closure position, interlock actuation, restart prevention | qualified functional test | critical |
| ICD-07 | Camera/lighting → work envelope | FOV, working distance, glare control, electrical separation | documented image set | high |
| ICD-08 | Test plug → far-end harness fixture | mating geometry, pin map, reference/self-test path | electrical fault coupons | critical |
| ICD-09 | Host software → controller | version, bounded commands, state preconditions, watchdog behavior | automated protocol tests | critical |

Any critical-interface change requires impact review against the DFM register, traveler, BOM, relevant drawing, and verification plan.
