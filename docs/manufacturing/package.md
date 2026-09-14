# Prototype manufacturing package

> **Scope of supply** — LoomForge supplies engineering plans, digital design files, software, and supporting documentation only. No physical machine or assembled equipment is supplied. The receiving manufacturer or its appointed machine builder must procure or fabricate the parts, assemble the equipment, and perform the necessary engineering review, safety assessment, calibration, testing, and application-specific validation before use. The current package is a development design and is not represented as production-ready or certified.

## Assembly and make/buy

Assembly hierarchy: `LF-000` workstation -> `LF-100` base/feet, `LF-110` gantry, `LF-200` motion head, `LF-300` fixture interface, `LF-400` tray, `LF-500` guard, `LF-600` electrical enclosure. The preliminary BOM is `hardware/bom/prototype-bom.csv`; it is not a supplier quotation and contains no prices.

Prototype approach: 3D-print tray pockets, guide-body test pieces, and fixture soft jaws in PETG/nylon; machine base/fixture datum plates in aluminum; buy certified supply, safety hardware, rails, sensors, and connector components. Small-batch approach: replace printed guide/fixture load surfaces with machined/anodized aluminum or qualified engineering polymer because creep, wear, and datum stability can alter insertion alignment.

## Fabrication / assembly controls

- Locator strategy: two dowel pins plus clamp fastener on cartridge; define fixture datum in controlled drawing.
- Datum/fit/tolerance note: no released tolerance may be inferred from conceptual CAD. Set after tolerance stack and sample component measurement.
- Use threadlocker only after fastener/joint validation and document material compatibility; no adhesive is presently specified.
- Route motor/force wiring separately from camera/test wiring; strain-relieve all moving cables and shield terminate per released grounding plan.
- Incoming inspection: housing/terminal part number, packaging condition, wire gauge, visible crimp condition, fixture ID, and connector sample fit.
- Calibration: home axes, verify fixture artifact coordinates, zero force sensor with guide unloaded, run electrical fixture self-test, record IDs/time/operator.
- Maintenance: inspect guide nose, gripper pads, cable chain, interlock/ESTOP function, force calibration, and test-fixture contacts at an interval established by physical use data.

No PCB is released: a custom board would require native KiCad schematic/layout, ERC/DRC, electrical review, and functional test before fabrication.
