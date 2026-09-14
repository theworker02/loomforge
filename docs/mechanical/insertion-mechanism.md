# Guided insertion mechanism

Operator-loaded, labelled pre-crimped wires enter keyed indexed tray slots terminal-forward. A parallel gripper holds the insulation behind the terminal barrel, while a replaceable keyed guide captures the terminal body without touching its locking lance. The guide nose reaches within a **proposed** 12 mm of the cavity; 0.5 mm total radial passive compliance is proposed. Z advances under bounded force/travel monitoring, then releases and retracts. No blind repeated insertion is permitted.

| Failure | Detection | Machine response | Recovery |
|---|---|---|---|
| bent/rotated/incorrect terminal | tray datum + future vision gate | no cavity entry | replace lead; inspect guide |
| buckled wire / wrong diameter | qualification + force/travel | stop | inspect support and lead |
| partial seating / high force | signature / 15 N ceiling | stop, never pass | approved inspection/rework |
| wrong cavity | recipe-bound fixture mapping | reject command | reload recipe |
| damaged housing/fixture | datum/RFID + future vision | no motion | reseat/replace |
| missing/double tray slot | future tray sensor/vision | stop | correct presentation |
| previously inserted obstruction | envelope/force | stop | inspect sequence |

All “future” detections are requirements, not working hardware. Physical trials, microscope inspection, and sectioning must validate guide geometry and the seating signature.
