# Safety concept — not a compliance claim

This is a preliminary risk assessment using the risk-reduction approach of ISO 12100 and OSHA guarding guidance. A qualified machinery-safety professional must review the final machine, electrical design, local regulations, and validation before operation.

| Hazard | Design control | Safe response / recovery |
|---|---|---|
| pinch/crush at head and fixture | physical guard, interlocked door, limited speeds | safety relay disables motion torque; inspect before recovery |
| unexpected host command | controller state preconditions and bounded recipes | reject command; no raw host motion |
| door opened | independent monitored interlock | controlled/energy-safe stop; `RECOVERY_REQUIRED` |
| sharp terminals / jam clearing | tool-only service, power isolation procedure | lockout; no automatic retry |
| wire entanglement | indexed tray, cable retention, supervised operation | pause/stop and inspect |
| electrical fault | certified 24 V supply, fusing, grounding, protected test ports | de-energize branch; diagnose |
| lost communication/controller reset/power restoration | watchdog and persistent incomplete jobs | remain stopped; home and revalidate |
| E-stop | latching physical actuator into safety chain | no restart until manual reset, inspection, controller recovery |

Safe state is proposed as: Z braking/controlled stop where feasible, motor torque disabled by safety relay, gripper in mechanically non-crushing released/low-force condition, test excitation off, status red, and no restart after E-stop/power loss. Gravity and stored spring energy must be physically characterized.
