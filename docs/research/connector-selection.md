# Connector selection — provisional first family

## Compared families

| Family | Documentation / accessible test interface | Terminal handling | Locks / risks | Initial assessment |
|---|---|---|---|---|
| Molex Mini-Fit Jr (selected) | Public product specification includes insertion force; 4-circuit `44281-0001` test plug listed by Molex | 4.20 mm pitch and comparatively large terminal envelope aid guided handling | primary terminal lance; some variants use TPA. Selected `39-01-2040` configuration requires drawing confirmation on secondary-lock state | Best initial evidence and access |
| TE Micro-MaTch | Strong family/application information and premade cable availability | 1.27 mm pitch, much smaller alignment margin | contact/housing variants require exact selection; less forgiving for first gripper | Deferred: precision requirement too high |
| TE PicoMQS / Mini 0.50 | Automotive tooling ecosystem | sub-millimetre terminal scale | high process sensitivity and customer-specific standards | Excluded from v0 |

## Selected implementation envelope

- Housing: Molex Mini-Fit Jr receptacle `39-01-2040`, 4 circuit (verify exact drawing/revision before releasing fixture).
- Terminal: Molex `39-00-0038` female crimp terminal; pre-crimped only.
- Proposed supported wire: stranded copper 18, 20, 22, or 24 AWG with a supplier-qualified crimp to the exact terminal. Insulation OD envelope is **unresolved** until controlled terminal drawing/application specification review.
- Cavity convention: viewing mating face with latch up, cavities 1–2 left-to-right on top row and 3–4 left-to-right on bottom row. This is a recipe/UI convention and must be checked against the controlled housing drawing and fixture datum.
- Manufacturer source: PS-5556-002 reports a 15 N maximum terminal insertion force under its specified method. It is not a demonstrated LoomForge process force.

The terminal's primary locking lance must enter in the manufacturer-prescribed orientation. The guide's keyed terminal channel and gripper jaw datum constrain rotation. A 12 mm maximum proposed unsupported lead length from guide nose to cavity entry minimizes wire buckling; a floating guide has ±0.25 mm proposed radial compliance. Neither number is verified.

No secondary lock is modeled in this first housing. If the selected controlled drawing requires a TPA/secondary lock, recipe validation must require a separate confirmation step and the fixture must be redesigned. Retention check is **not** continuity: proposed seating signature plus fixture datum inspection, followed by manufacturer-approved retention sampling. Rework uses the manufacturer-specified extraction tool/procedure; LoomForge must not pull a terminal out with its gripper.
