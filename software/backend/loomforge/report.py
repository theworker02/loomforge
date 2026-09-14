from __future__ import annotations

import json
from pathlib import Path

from .repository import JobRepository


def export_report(repository: JobRepository, job_id: str, destination: str | Path) -> Path:
    """Export a traceable JSON record without changing its simulated/physical designation."""
    record = repository.get(job_id)
    if record is None:
        raise KeyError(f"unknown job {job_id}")
    target = Path(destination)
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(json.dumps({"report_version": "1", "scope_of_supply": "LoomForge supplies engineering plans, digital design files, software, and supporting documentation only. No physical machine or assembled equipment is supplied. The receiving manufacturer or its appointed machine builder must procure or fabricate the parts, assemble the equipment, and perform the necessary engineering review, safety assessment, calibration, testing, and application-specific validation before use. The current package is a development design and is not represented as production-ready or certified.", "evidence_notice": "SIMULATION results are synthetic, not physical verification." if record["mode"] == "SIMULATED" else "PHYSICAL run designation requires independent evidence review.", "job": record}, indent=2), encoding="utf-8")
    return target
