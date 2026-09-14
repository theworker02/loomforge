# System architecture

## Chosen architecture: moving insertion head (B)

Architecture A moves the fixture: lower head mass and potentially fixed optics, but pulls inserted wires and complicates retention of partially assembled harnesses. Architecture B moves a compact X/Y/Z insertion head over a fixed, front-access fixture: easier service, a stable mating-test station, and less wire drag. Its disadvantages are moving cable mass and camera coordination; these are mitigated with a short Z carriage, drag chain, and fixed overhead camera. B is selected provisionally.

```text
operator -> indexed tray -> keyed gripper/guide on X/Y/Z -> fixed fixture -> connector
                                                |                 |
                                          force sensor          mating test plug
```

```text
24 V certified PSU -> fuses -> motion controller -> drivers / motors / sensors
                              -> hardwired safety relay <- E-stop, door interlock
host (local API/UI) -- versioned bounded protocol --> controller
host -> SQLite jobs/reports        controller -> timestamped telemetry
```

The hardwired safety path must stop hazardous motion independent of the host, browser, AI, or network. Simulation adapter and future physical adapter are mutually exclusive explicit selections.

Coordinate frames: `M` base datum; `F` fixture cartridge locating dowels; `C` cavity plane; `H` guide nose. X moves across tray/cavities, Y provides row selection, Z is insertion direction. Calibration establishes `M→F`, then a fixture artifact establishes `F→C`; no recipe may supply arbitrary raw machine coordinates.

See [machine states](../controls/protocol.md) and [safety concept](../safety/hazard-analysis.md).
