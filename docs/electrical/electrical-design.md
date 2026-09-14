# Electrical architecture (preliminary)

Certified external 24 VDC >=8 A proposed supply -> fused distribution -> controller/drivers/motors, sensors, gripper, camera/light, and protected low-energy tester. E-stop and dual-channel door interlock feed a safety relay controlling motor enable independent of host/browser/network. Protective-earth/chassis design, shielding, and local codes require review.

```text
host USB/Ethernet -> bounded controller protocol -> motion/force/limits
E-stop + door -> safety relay -> motor-enable / energy-safe interface
isolated <=5 V, <=2 mA continuity excitation -> switch matrix -> mating plug + far-end breakout
```

Both ends are accessible: the mating test plug connects the assembled connector and each opposite wire end lands in a known breakout. Fixture ID plus short/open/reference-loop self-test gates each job. Opens, mapping errors, and cross-shorts are detected; unavailable test cannot pass. This is not precision contact-resistance measurement: contacts, switches, and leads dominate without Kelvin hardware. External-voltage protection needs characterized current limiting and clamps before release.
