# LoomForge

> **Scope of supply** — LoomForge supplies engineering plans, digital design files, software, and supporting documentation only. No physical machine or assembled equipment is supplied. The receiving manufacturer or its appointed machine builder must procure or fabricate the parts, assemble the equipment, and perform the necessary engineering review, safety assessment, calibration, testing, and application-specific validation before use. The current package is a development design and is not represented as production-ready or certified.

> **Manufacturer-led implementation** — We provide the plans and digital package. The receiving manufacturer or its appointed machine builder is responsible for procurement, fabrication, assembly, safeguarding, commissioning, calibration, operator training, maintenance, and application-specific validation.

LoomForge is an early engineering prototype for a modular benchtop workstation that inserts **pre-crimped** wires into one supported connector family and verifies the completed connector through a mating electrical test interface.

## Intended Applications and Target Organizations

LoomForge is being developed for engineering and manufacturing teams working on small-batch wiring assemblies, including applications relevant to aerospace, robotics, automotive development, industrial automation, and electronics manufacturing. Named organizations are prospective application targets identified through public research. No affiliation, endorsement, customer relationship, or purchasing interest is implied.

The package is for review, engineering-package export, compatibility evaluation, fabrication/procurement planning, manufacturer-led assembly/commissioning, and manufacturer-led validation. It does not offer checkout, shipping, installation, or certification services.

## Status

This repository contains a functioning **local simulation** and engineering design package. Nothing here is evidence of physical performance, machinery safety compliance, production readiness, or aerospace qualification. Simulation reports and the UI are deliberately marked `SIMULATED`.

The initial proposed differentiator is faster, mechanically keyed fixture/recipe changeover for small-batch work—not broad novelty in automated harness assembly.

## First selected system (provisional but sourced)

Molex Mini-Fit Jr. 4-circuit receptacle housing `39-01-2040`, with `39-00-0038` female crimp terminals on 18–24 AWG stranded wire. See [connector selection](docs/research/connector-selection.md). The system is selected because Molex publishes an insertion-force requirement (15 N maximum) and a practical test plug exists (`44281-0001`). Exact housing drawing dimensions and the final wire/terminal supplier availability must be confirmed against controlled manufacturer documents before fabrication.

## Run the simulated acceptance demonstration

Requires only Python 3.11+.

```powershell
python -m unittest discover -s tests -v
python -m software.backend.loomforge.cli run recipes/examples/mini_fit_4c.json --scenario success --database reports/loomforge.sqlite
python -m software.backend.loomforge.cli run recipes/examples/mini_fit_4c.json --scenario incorrect_connection --database reports/loomforge.sqlite
python -m software.backend.loomforge.cli export JOB_ID reports/JOB_ID.json --database reports/loomforge.sqlite
python -m software.backend.loomforge.cli serve --database reports/loomforge.sqlite
```

Open `http://127.0.0.1:8787`. The server is local-only and simulation-only. It will not fall back to a simulated adapter if a future physical adapter disconnects.

## Regenerate CAD

Install OpenSCAD, then run:

```powershell
openscad -o hardware/mechanical/exports/loomforge-assembly.stl hardware/mechanical/source/loomforge.scad
```

The model is a parametric, conceptual envelope assembly—not a released fabrication model. See [CAD README](hardware/mechanical/source/README.md).

## Evidence boundaries

- **Sourced:** manufacturer specifications and links in `docs/research/sources.md`.
- **Calculated:** reproducible values in `calculations/preliminary_sizing.py`.
- **Simulated:** job outcomes, synthetic force curves, and test results produced by the simulator.
- **Physical verification:** not performed. The first experiment is specified in `docs/validation/physical-validation-plan.md`.

## Repository guide

- `software/backend/loomforge`: typed-domain Python simulation, persistence, protocol boundary, and local API
- `recipes`: declarative recipe examples and rejected examples
- `hardware`: parametric CAD source, electrical/wiring artifacts, fixture definition, and BOM
- `docs`: research, architecture, safety, manufacturing, validation, and operator material
- `calculations`: executable preliminary engineering calculations

## License and marks

Repository material is available under the [MIT License](LICENSE). See [TRADEMARKS.md](TRADEMARKS.md) for name/mark use and no-endorsement boundaries.
