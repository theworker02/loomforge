# Local simulation operator guide

1. Validate a recipe using the CLI simulation command; validation rejects unsupported parts, duplicate cavities, invalid tray slots, unknown fixture/calibration IDs, and force values above 15 N.
2. Run `success` for the simulated acceptance path. Run `incorrect_connection` to demonstrate a deliberate assembly fault detected by the simulated mating test.
3. Review the SQLite-backed job history in the local UI. Every result has `SIMULATED` mode and generated synthetic traces.
4. Faulted/interrupted simulated jobs remain stored; they are never converted to pass. A future physical machine must require manual recovery/homing after E-stop, power loss, or communication loss.

The present application has no physical controller adapter and cannot control machinery.
