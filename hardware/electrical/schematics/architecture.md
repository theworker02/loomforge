# Wiring schematic intent

```text
AC mains -> certified enclosed 24 VDC PSU -> lockable DC disconnect -> fused distribution
                                                               +--> motor drivers -> XYZ actuators
                                                               +--> controller, home/limits, force ADC
                                                               +--> lighting/camera and gripper branch
                                                               +--> isolated continuity tester -> test matrix -> J2 mating plug

E-STOP CH A + door CH A -> safety relay CH A
E-STOP CH B + door CH B -> safety relay CH B -> driver-enable / safety interface
```

This is a wiring architecture, not a native KiCad schematic or release for wiring/fabrication. Pin assignment is `hardware/electrical/wiring/io-map.csv`; cable selection, conductor size, connector series, grounding/EMC, fault ratings, and schematic ERC remain unresolved design work.
