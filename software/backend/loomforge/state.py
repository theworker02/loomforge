from __future__ import annotations

from .models import MachineState

ALLOWED: dict[MachineState, set[MachineState]] = {
    MachineState.DISCONNECTED: {MachineState.INITIALIZING},
    MachineState.INITIALIZING: {MachineState.NOT_HOMED, MachineState.FAULT, MachineState.ESTOP},
    MachineState.NOT_HOMED: {MachineState.READY, MachineState.FAULT, MachineState.ESTOP},
    MachineState.READY: {MachineState.LOADING, MachineState.FAULT, MachineState.ESTOP},
    MachineState.LOADING: {MachineState.VALIDATING, MachineState.PAUSED, MachineState.FAULT, MachineState.ESTOP},
    MachineState.VALIDATING: {MachineState.ASSEMBLING, MachineState.FAULT, MachineState.RECOVERY_REQUIRED, MachineState.ESTOP},
    MachineState.ASSEMBLING: {MachineState.VERIFYING, MachineState.PAUSED, MachineState.FAULT, MachineState.RECOVERY_REQUIRED, MachineState.ESTOP},
    MachineState.VERIFYING: {MachineState.COMPLETE, MachineState.FAULT, MachineState.RECOVERY_REQUIRED, MachineState.ESTOP},
    MachineState.COMPLETE: {MachineState.READY},
    MachineState.PAUSED: {MachineState.RECOVERY_REQUIRED, MachineState.ESTOP},
    MachineState.FAULT: {MachineState.RECOVERY_REQUIRED, MachineState.ESTOP},
    MachineState.ESTOP: {MachineState.RECOVERY_REQUIRED},
    MachineState.RECOVERY_REQUIRED: {MachineState.NOT_HOMED},
}


class StateError(RuntimeError):
    pass


def transition(current: MachineState, target: MachineState) -> MachineState:
    if target not in ALLOWED[current]:
        raise StateError(f"rejected transition {current.value} -> {target.value}")
    return target
