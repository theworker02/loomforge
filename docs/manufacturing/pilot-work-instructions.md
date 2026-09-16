# M1 pilot work instructions — LF-P1-R02

**Document:** LF-WI-001 · **Revision:** A0 (proposed)
**Applies to:** supervised development builds only. Follow the unit traveler and manufacturer safety procedures in addition to these instructions.

> LoomForge provides plans and documentation only. The receiving manufacturer must authorize the work area, personnel, tooling, safeguarding, and energized testing before use.

## WI-01 — Prepare the build cell

1. Open a traveler for the assigned serialized unit and identify the controlled configuration.
2. Confirm the unit is not an uncontrolled rework item and that required components have passed receiving inspection.
3. Establish an ESD, clean-work, and sample-retention area appropriate to the selected connector and terminal supplier guidance.
4. Stage only the tools named in the assembly instructions, with current calibration where a measurement or torque record is required.
5. Record any missing controlled drawing, tool, calibration, or material as a hold. Do not continue on memory or an informal substitute.

## WI-02 — Mechanical assembly and access review

1. Assemble base, spine, and side supports to the released drawing datums; record applicable torque values from controlled assembly documentation.
2. Install the fixture plate, cartridge, tray, guide, gripper, force-sensor mount, and cable routing in the stated assembly order.
3. Without applying motion power, manually review tool access, fixture removal, tray loading, guard closure, and service-panel removal.
4. Perform the FAI on M1-001 and M1-002 before electrical integration.
5. If a fastener, connector, cable, or panel obstructs a required operation, create an NCR. Do not bend, file, enlarge, or relocate a datum-bearing feature without disposition.

## WI-03 — Dry motion and cable routing

1. Install actual proposed cables/service loops, not only representative strings.
2. With energy isolated and the manufacturer-approved safe method, traverse each axis through home and documented extremes.
3. Confirm cable bend radius, no pinch between moving/fixed assemblies, no pull on connectors, and no contact with the guard/fixture/tray.
4. Repeat with fixture installed and with one representative wire path; illustrative CAD wires are not proof of flexible-wire clearance.
5. Record observed clearance concerns in the traveler and DFM register.

## WI-04 — Electrical integration and protective-function checkout

1. Build wiring from the controlled cable schedule; label both ends and record any approved substitute.
2. Have qualified personnel inspect grounding, branch protection, disconnect, E-stop, interlock, stored-energy behavior, and controller watchdog design before energized checkout.
3. Execute the receiving manufacturer’s protective-function test procedure. Verify that guard opening, E-stop, controller reset, and power restoration do not create automatic restart.
4. If any protective-function test is incomplete or ambiguous, mark the unit **do not use** for powered work.

## WI-05 — Calibration and controlled insertion study

1. Complete the calibration checklist before a controlled run. Link calibration record IDs in the traveler.
2. Validate the declarative recipe and fixture ID. The host interface must not issue raw motion coordinates.
3. Begin with a supervised, bounded trial using the specified connector, terminal, and wire only.
4. Preserve the force trace, fixture ID, recipe revision, calibration IDs, terminal/housing samples, and visual inspection result.
5. Stop on force limit, incomplete seating evidence, damaged material, sensor dropout, door event, electrical ambiguity, or controller fault. Do not make repeated blind insertion attempts.

## WI-06 — Close and archive

1. Reconcile the traveler with the as-built BOM, deviations, NCRs, calibration records, photos, and job records.
2. Assign only the disposition permitted by the traveler. “Complete” means the development step is recorded—not production approval.
3. Retain M1-011 and M1-012 with their as-built configuration and environmental/storage conditions documented for later regression comparison.
