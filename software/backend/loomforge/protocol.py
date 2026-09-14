"""Versioned, bounded physical-controller protocol contract; no hardware transport included."""
from __future__ import annotations

from dataclasses import dataclass
from enum import Enum
from typing import Any
from uuid import UUID

from .models import MachineState

PROTOCOL_VERSION = "1.0"


class ProtocolError(ValueError):
    pass


class Command(str, Enum):
    GET_STATUS = "GET_STATUS"
    HOME = "HOME"
    VALIDATE_JOB = "VALIDATE_JOB"
    START_JOB = "START_JOB"
    PAUSE = "PAUSE"
    ACK_FAULT = "ACK_FAULT"
    ENTER_RECOVERY = "ENTER_RECOVERY"


PRECONDITIONS = {
    Command.GET_STATUS: set(MachineState),
    Command.HOME: {MachineState.NOT_HOMED, MachineState.RECOVERY_REQUIRED},
    Command.VALIDATE_JOB: {MachineState.LOADING},
    Command.START_JOB: {MachineState.READY},
    Command.PAUSE: {MachineState.ASSEMBLING},
    Command.ACK_FAULT: {MachineState.FAULT, MachineState.ESTOP, MachineState.RECOVERY_REQUIRED},
    Command.ENTER_RECOVERY: {MachineState.FAULT, MachineState.ESTOP, MachineState.PAUSED},
}


@dataclass(frozen=True)
class ControllerCommand:
    command_id: str
    protocol_version: str
    command: Command
    expected_state: MachineState
    units: dict[str, str]
    payload: dict[str, Any]

    @classmethod
    def parse(cls, message: dict[str, Any]) -> "ControllerCommand":
        required = {"command_id", "protocol_version", "command", "expected_state", "units", "payload"}
        missing = required - message.keys()
        if missing:
            raise ProtocolError(f"missing protocol fields: {sorted(missing)}")
        try:
            UUID(str(message["command_id"]))
        except ValueError as exc:
            raise ProtocolError("command_id must be a UUID") from exc
        if message["protocol_version"] != PROTOCOL_VERSION:
            raise ProtocolError("PROTOCOL_INCOMPATIBLE")
        command, state = Command(message["command"]), MachineState(message["expected_state"])
        if state not in PRECONDITIONS[command]:
            raise ProtocolError(f"STATE_PRECONDITION_REJECTED: {command.value} cannot run in {state.value}")
        units = message["units"]
        if units != {"distance": "mm", "speed": "mm/s", "force": "N", "time": "ms"}:
            raise ProtocolError("UNIT_SET_REJECTED")
        forbidden = {"gcode", "shell", "raw_axis_motion", "coordinates"} & set(message["payload"])
        if forbidden:
            raise ProtocolError("RAW_MOTION_REJECTED")
        return cls(str(message["command_id"]), message["protocol_version"], command, state, units, message["payload"])
