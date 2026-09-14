from __future__ import annotations

import argparse
import json
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer

from .recipe import load_recipe
from .repository import JobRepository
from .sim import SCENARIOS, SimulationAdapter


def main() -> None:
    parser = argparse.ArgumentParser(description="LoomForge local simulation")
    sub = parser.add_subparsers(dest="command", required=True)
    run = sub.add_parser("run"); run.add_argument("recipe"); run.add_argument("--scenario", choices=sorted(SCENARIOS), default="success"); run.add_argument("--database", default="reports/loomforge.sqlite")
    validate = sub.add_parser("validate"); validate.add_argument("recipe")
    sub.add_parser("scenarios")
    export = sub.add_parser("export"); export.add_argument("job_id"); export.add_argument("destination"); export.add_argument("--database", default="reports/loomforge.sqlite")
    serve = sub.add_parser("serve"); serve.add_argument("--database", default="reports/loomforge.sqlite"); serve.add_argument("--port", type=int, default=8787)
    args = parser.parse_args()
    if args.command == "run":
        record = SimulationAdapter().run(load_recipe(args.recipe), args.scenario); JobRepository(args.database).save(record); print(json.dumps(record.jsonable(), indent=2)); return
    if args.command == "validate":
        recipe = load_recipe(args.recipe)
        from .machine import MachineConfiguration
        MachineConfiguration().validate_recipe_reach(recipe)
        print(json.dumps({"valid": True, "recipe_id": recipe.recipe_id, "configuration": "LF-P1-R02"}, indent=2)); return
    if args.command == "scenarios":
        print("\n".join(sorted(SCENARIOS))); return
    if args.command == "export":
        from .report import export_report
        print(export_report(JobRepository(args.database), args.job_id, args.destination)); return
    repo = JobRepository(args.database)
    class Handler(BaseHTTPRequestHandler):
        def do_GET(self):
            if self.path == "/api/jobs": body, ctype = json.dumps(repo.list()).encode(), "application/json"
            elif self.path == "/assets/front-elevation.svg":
                body, ctype = open("hardware/mechanical/renders/front-elevation.svg", "rb").read(), "image/svg+xml"
            else: body, ctype = b"<html><body style='font-family:system-ui;max-width:1000px;margin:30px;background:#eef1ef;color:#162328'><header style='display:flex;justify-content:space-between'><h1>LoomForge</h1><b style='color:#087e80'>SIMULATION ONLY</b></header><p><b>Engineering view:</b> LF-P1-R02 silhouette, not a live physical machine. Physical controls are separate from visualization controls.</p><img style='max-width:100%;border:1px solid #aab5b5;background:white' src='/assets/front-elevation.svg' alt='CAD-derived LoomForge front elevation'><section style='display:flex;gap:24px'><div><h2>Machine state</h2><p>SIMULATED / no physical controller connected</p><p>Door: simulated closed | Fixture: LF-MFJ-4C-001 | Tray: 12 indexed slots</p><p>Axis display and force traces are stored per job record below.</p></div><div><h2>Operator view</h2><p>Open guard, load labelled slot, route comb, close/validate, supervise. The local UI cannot command motion.</p></div></section><h2>Assembly history</h2><pre id='jobs'>Loading...</pre><details><summary>About / Scope of supply</summary><p>LoomForge supplies engineering plans, digital design files, software, and supporting documentation only. No physical machine or assembled equipment is supplied. The receiving manufacturer or its appointed machine builder must procure or fabricate the parts, assemble the equipment, and perform the necessary engineering review, safety assessment, calibration, testing, and application-specific validation before use. The current package is a development design and is not represented as production-ready or certified.</p></details><script>fetch('/api/jobs').then(x=>x.json()).then(x=>jobs.textContent=JSON.stringify(x,null,2))</script></body></html>", "text/html; charset=utf-8"
            self.send_response(200); self.send_header("Content-Type", ctype); self.end_headers(); self.wfile.write(body)
        def log_message(self, *_): pass
    print(f"LoomForge simulation UI: http://127.0.0.1:{args.port}")
    ThreadingHTTPServer(("127.0.0.1", args.port), Handler).serve_forever()

if __name__ == "__main__": main()
