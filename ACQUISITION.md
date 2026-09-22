# Acquisition Brief â€” LoomForge

**Date:** 2026-09-22  
**Repository:** https://github.com/theworker02/loomforge  
**Default branch:** `main`  
**Primary language:** Python  
**Status:** Diligence briefing only. **No acquisition has occurred** by virtue of this file.  
**License:** Proprietary â€” sale, written commercial license, or completed asset transfer required (see root `LICENSE`).  
**Valuation:** Not stated.  
**Contact:** GitHub [@theworker02](https://github.com/theworker02) Â· [thanks.dev/u/gh/theworker02](https://thanks.dev/u/gh/theworker02)

> Cloning or forking this repository does **not** grant production, redistribution, SaaS, OEM, or commercial rights.

---

## 1. Executive thesis

This project is **proprietary**. Production use, redistribution, and commercial deployment require a written commercial license or completed acquisition. See [LICENSE](./LICENSE) and [ACQUISITION.md](./ACQUISITION.md). Contact [@theworker02](https://github.com/theworker02). > **Scope of supply** Ã¢â‚¬â€ LoomForge supplies engineering plans, digital design files, software, and supporting documentation only. No physical machine or assembled equipment is supplied. The receiving manufacturer or its appointed machine builder must procure or fabricate the parts, assemble the equipment, and perform the necessary engineering review, safety assessment, calibration, testing, and application-specific validation before use. The current package is a development design and is not represented as production-ready or certified. > **Manufacturer-led implementation** Ã¢â‚¬â€ We provide the plans and digital package. The receiving manufacturer or its appointed machine builder is responsible for procurement, fabrication, assembly, safeguarding, commissioning, calibration, operator training, maintenance, and application-specific validation.

**Why a buyer cares:** LoomForge packages transferable product IP â€” source, docs, in-repo brand assets, and a diligence room under `docs/acquisition/` â€” under a clear proprietary posture so diligence can proceed without mistaking the repo for open source.

---

## 2. Product snapshot

| Item | Detail |
|------|--------|
| Product | LoomForge |
| Repo | `theworker02/loomforge` |
| Language | Python |
| Open source? | **No** â€” proprietary |
| Rightsholder | theworker02 |
| Diligence pack | `docs/acquisition/` |

### Capability highlights (from current materials)

- **Sourced:** manufacturer specifications and links in `docs/research/sources.md`.
- **Calculated:** reproducible values in `calculations/preliminary_sizing.py`.
- **Simulated:** job outcomes, synthetic force curves, and test results produced by the simulator.
- **Physical verification:** not performed. The first experiment is specified in `docs/validation/physical-validation-plan.md`.
- `software/backend/loomforge`: typed-domain Python simulation, persistence, protocol boundary, and local API
- `recipes`: declarative recipe examples and rejected examples
- `hardware`: parametric CAD source, electrical/wiring artifacts, fixture definition, and BOM
- `docs`: research, architecture, safety, manufacturing, validation, and operator material
- `calculations`: executable preliminary engineering calculations

---

## 3. Problem / opportunity

Teams evaluating LoomForge typically need either (a) a commercial right to run or embed it, or (b) outright ownership of the Product IP for strategic build-out. Public GitHub visibility without a proprietary license creates false assumptions about free production use. This brief and the linked data room make the commercial path explicit.

---

## 4. What ships today

Honest maturity: treat repository contents, README claims, tests, and release tags as the source of truth. Do not assume production customers, ARR, filed patents, or SLAs unless separately evidenced in diligence.

Typical transferable surfaces:

- Source tree and build/test scripts present in-repo
- Documentation and design notes
- Acquisition / diligence markdown under `docs/acquisition/`
- Branding assets committed to the repository (if any)

---

## 5. Demo / evaluation path (buyer)

Minimal path (no secrets required unless README says otherwise):

```
```powershell
python -m unittest discover -s tests -v
python -m software.backend.loomforge.cli run recipes/examples/mini_fit_4c.json --scenario success --database reports/loomforge.sqlite
python -m software.backend.loomforge.cli run recipes/examples/mini_fit_4c.json --scenario incorrect_connection --database reports/loomforge.sqlite
python -m software.backend.loomforge.cli export JOB_ID reports/JOB_ID.json --database reports/loomforge.sqlite
python -m software.backend.loomforge.cli serve --database reports/loomforge.sqlite
```
```powershell
openscad -o hardware/mechanical/exports/loomforge-assembly.stl hardware/mechanical/source/loomforge.scad
```
```

Extended evaluation: `docs/acquisition/BUYER_EVALUATION.md`. Written NDA / evaluation grants may be required for private materials.

---

## 6. What a transaction typically includes

Subject to definitive schedules:

| Included (typical) | Excluded (typical) |
|--------------------|--------------------|
| Repo materials + asserted original IP | Seller personal accounts / unrelated repos |
| Docs + diligence room at closing | Third-party dependency source under separate licenses |
| In-repo brand marks as assigned | Secrets without rotation plan |
| Know-how captured in docs | Fabricated revenue, user, or adoption metrics |

---

## 7. Suggested deal structures

| Structure | When it fits |
|-----------|--------------|
| Non-exclusive commercial license | Deploy/run under seat or environment terms |
| Exclusive field-of-use license | Buyer wants exclusivity; seller may retain entity |
| Asset / IP assignment | Buyer wants ownership of Materials outright |
| OEM / redistribution | Separate agreement â€” not implied here |

Commercial terms (price, earnouts, escrow) are negotiated under NDA with counsel.

---

## 8. Buyer diligence checklist

- [ ] Confirm Rightsholder identity and authority to sell/license
- [ ] Inventory Materials (`docs/acquisition/ASSET_INVENTORY.md`)
- [ ] Review IP posture (`IP_PROVENANCE.md`) and dependencies (`DEPENDENCY_INVENTORY.md`)
- [ ] Run evaluation script (`BUYER_EVALUATION.md`)
- [ ] Review risks (`RISK_REGISTER.md`)
- [ ] Agree transfer scope (`TRANSFER_MANIFEST.md`) and handoff (`HANDOFF_CHECKLIST.md`)
- [ ] Supersede root `LICENSE` at closing via definitive agreement

---

## 9. Related documents

| Document | Purpose |
|----------|---------|
| `LICENSE` | Proprietary â€” no default grant |
| `docs/acquisition/README.md` | Data-room index |
| `docs/acquisition/EXECUTIVE_SUMMARY.md` | One-page thesis |
| `README.md` | Product overview |
| `SECURITY.md` | Vulnerability reporting |
| `COMMERCIAL.md` | Licensing contact path |
| `.github/FUNDING.yml` | Sponsors / thanks.dev |

---

## 10. Disclaimer

This package is informational and **does not** create a binding offer, grant of rights, or investment advice. Engage counsel for any transaction.

---

*Document version: 2.0.0 / 2026-09-22 Â· Classification: acquisition briefing*
