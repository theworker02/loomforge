# LF-P1-R02 mechanisms and wire cycle

## Moving assemblies

| Assembly | Function / range | proposed drive / guidance | references, limits, service / calibration |
|---|---|---|---|
| X carriage | tray-to-fixture positioning, 210 mm | belt/linear rail; rear spine | home switch + hard buffers; drag chain over spine; fixture artifact calibration |
| Y cross slide | row/slot/cavity alignment, 110 mm | compact linear stage | home/limit sensors; cable loop; camera-to-fixture calibration |
| Z insertion | approach/guide/retract, 72 mm with 32 mm controlled insertion | ballscrew or captive actuator on linear guides | home/upper/lower limits; load cell inline; force zero and travel datum |
| gripper | closes on insulated conductor only | low-force miniature parallel actuator | open sensor; replaceable pads; pinch limits unresolved |
| split guide | terminal support/orientation then release | passive spring split jaws, 0.5 mm total radial compliance | guide datum; replaceable wear part; geometry unverified |
| tray index | operator keyed placement; no automatic carousel in P1 | manually indexed fixed tray | RFID/visual slot check proposed; service-front access |

## Full wire-handling cycle

1. Operator opens the interlocked upward guard, places a labelled pre-crimped lead terminal-forward into one keyed tray channel, and routes slack through a passive comb. The opposite end stays in a labelled breakout/test position.
2. Operator verifies the slot and closes the guard. Software enters validation, not automatic motion.
3. X/Y head approaches the selected slot. Soft gripper pads close on insulation behind the terminal barrel; terminal/lance are not gripped.
4. The terminal is slid into the keyed split guide. The guide supports it to a maximum **proposed** 12 mm from cavity entry, constraining rotational orientation.
5. Head moves to recipe-bound cavity coordinate; fixture nest/dowels establish cavity datum. Z advances under force/travel limit.
6. Proposed seating signature is evaluated. It is not proof of retention.
7. Z retracts slightly, split guide jaws cam open around the inserted wire, gripper opens, and head retreats. The wire remains in a prescribed rear/upward slack corridor held by combs.
8. Recipe sequence is initially ordered to avoid crossing prior wires; any obstruction/force anomaly stops for intervention. Completed assembly is removed by the operator after test and guard opening.

Minimum bend radius is unresolved because it depends on the final wire construction. Tray channels must be revised after a supplier-approved wire selection. No step is claimed physically demonstrated.
