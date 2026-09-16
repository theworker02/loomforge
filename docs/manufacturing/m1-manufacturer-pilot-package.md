# SC-A0 manufacturer package and proposed 12-unit M1 pilot

**Package status:** engineering-development handoff
**Configuration:** LF-P1-R02 / SC-A0
**Pilot:** proposed 12-unit M1 manufacturer build; not authorized procurement, production release, or certification

> **Plans-only scope of supply.** LoomForge supplies engineering plans, digital design files, software, and supporting documentation only. No physical machine or assembled equipment is supplied. The receiving manufacturer or its appointed machine builder must procure or fabricate the parts, assemble the equipment, and complete the necessary engineering review, safety assessment, calibration, testing, and application-specific validation before use.

## Package map

| Review need | Controlled source | Maturity / use |
|---|---|---|
| Supply-chain build plan and quality gates | [SC-A0 manufacturing plan](sc-a0-manufacturing-plan.md) | Proposed M1 planning baseline |
| Structured make/buy and sourcing starting point | [M1 BOM framework](../../hardware/bom/m1-bom-framework.csv) | Framework only; pricing and supplier selections pending |
| Supplier quote request scopes | [Supplier RFQ package](supplier-rfq-package.md) and [RFQ line index](../../hardware/bom/m1-rfq-line-items.csv) | Quote-ready context after supplier-specific drawing release |
| Prototype assembly order | [Assembly and commissioning](assembly-and-commissioning.md), [R02 assembly order](assembly-order-r02.md) | Engineering guidance; first-article review required |
| Serialized build evidence | [M1 pilot traveler](m1-pilot-traveler.md) | Use one controlled copy per M1 unit |
| Verification gates | [Design verification plan](design-verification-plan.md) | Proposed targets; physical results pending |
| Fabrication and assembly risks | [DFM risk register](dfm-risk-register.md) | Active / must be updated during pilot |
| Configuration and deviations | [Configuration-management plan](configuration-management-plan.md), [NCR/CAPA procedure](nonconformance-and-capa.md) | Required for as-built traceability |
| Process and first-article control | [Quality control plan](quality-control-plan.md), [FAI template](first-article-inspection-template.md) | Proposed M1 inspection method |
| Pilot sequencing and interfaces | [M1 execution plan](m1-pilot-execution-plan.md), [interface-control register](interface-control-register.md) | Build only in staged waves |
| Supplier selection and cost evidence | [Supplier evaluation framework](supplier-evaluation-framework.md), [cost/capacity framework](m1-cost-and-capacity-framework.md) | Manufacturer-owned quotation and estimate process |
| Build execution and records | [Pilot work instructions](pilot-work-instructions.md), [calibration/test record set](calibration-and-test-records.md) | Controlled supervised pilot work only |
| Supplier deliverables and gate decisions | [Supplier data requirements](supplier-data-package-requirements.md), [M1 release-review checklist](m1-release-review-checklist.md) | Evidence-based quote/build decisions |
| Overall implementation boundaries | [Scope of supply](scope-of-supply.md), [manufacturer responsibilities](manufacturer-responsibilities.md), [unresolved design items](unresolved-design-items.md) | Mandatory review before build |

## Proposed M1 evidence set

Before a unit is assigned anything more than restricted engineering use, the receiving manufacturer should retain:

1. Approved supplier substitutions and incoming inspection records.
2. As-built BOM, drawing/CAD configuration, software/firmware versions, fixture ID, and calibration references.
3. Traveler signatures, photos, torque/alignment records, and all deviations.
4. Protective-function tests for the manufacturer-selected E-stop/interlock architecture.
5. Insertion traces, seating/damage inspections, and electrical-fixture self-test results.
6. Results—pass, fail, interrupted, and inconclusive—from the pilot plan. Failed records must be retained.

## Explicit non-release statement

SC-A0 is a coherent starting package for supplier review and a controlled prototype pilot. It is **not** a blanket “ready to manufacture” release. Release of any fabrication drawing, supplier purchase order, safety architecture, substituted component, or use authorization belongs to the receiving manufacturer’s controlled engineering process.
