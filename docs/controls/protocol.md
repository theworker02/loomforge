# Controller protocol and state safety contract

The physical controller is a documented boundary, not implemented hardware firmware. It owns homing, limits, bounded motion, force-limit response, watchdog, and safe faults. The host never sends raw text, G-code, or unbounded axis commands.

Protocol v1 messages are JSON with `protocol_version`, UUID `command_id`, `timestamp_utc`, `command`, `units`, `payload`, and `expected_state`. Acknowledgements echo `command_id`, outcome, controller timestamp, and structured error code. A repeated `command_id` is idempotent; a changed payload with an existing ID is rejected. All distance units are mm, speed mm/s, force N, and time ms. Compatibility mismatch is a connection failure.

Commands: `GET_STATUS`, `HOME`, `VALIDATE_JOB`, `START_JOB`, `PAUSE`, `ACK_FAULT`, `ENTER_RECOVERY`. `START_JOB` requires `READY`, an approved signed/validated recipe digest, valid calibration, door closed, and an explicit current operator confirmation. It contains no arbitrary coordinate data. Controller watchdog timeout transitions to safe fault. A stale browser cannot start a job: it lacks a current controller session nonce and operator confirmation.

```text
DISCONNECTED -> INITIALIZING -> NOT_HOMED -> READY -> LOADING -> VALIDATING -> ASSEMBLING -> VERIFYING -> COMPLETE -> READY
                                    \-> FAULT/ESTOP/RECOVERY_REQUIRED -> NOT_HOMED
```

`PAUSED`, `FAULT`, `ESTOP`, and power restoration enter `RECOVERY_REQUIRED`; no automatic restart is allowed. State enforcement is tested in `tests/test_loomforge.py`.
