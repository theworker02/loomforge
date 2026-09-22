# Buyer evaluation â€” LoomForge

## Goal

In 15â€“45 minutes, verify the Product builds or runs as documented and that proprietary notices are present.

## Steps

1. Confirm root `LICENSE` is proprietary and `ACQUISITION.md` exists.
2. Skim `README.md` install/run claims.
3. Execute:

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

4. Run tests if present (`npm test`, `pytest`, `cargo test`, `go test ./...`, etc.).
5. Record README vs observed behavior gaps in workpapers.

## Pass criteria

- [ ] Clone succeeds
- [ ] Documented happy path works **or** failure is explained
- [ ] Minimal path needs no surprise secrets
- [ ] License notices intact

*Updated: 2026-09-22*
