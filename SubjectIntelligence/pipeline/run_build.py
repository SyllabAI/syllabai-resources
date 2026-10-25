#!/usr/bin/env python3
"""SIB run builder — orchestrates the mechanical chain of a SIB-GEN wave (r0).

The chain (docs/PIPELINE.md §3, layered gates §5):

  1. preflight  — source_resolver over the library's source_manifest.yaml;
                  wave families must have their PRIMARY sources RESOLVED.
  2. pack       — evidence_pack per artifact (family law from evidence_policy.yaml;
                  extraction plan is agent-authored and committed to the run record).
  3. generate   — AGENT-AUTHORED (the generator class writes the body from the pack;
                  the human/agent loop is deliberately NOT automated here).
  4. stamp+QA   — generate_artifact.py (v2 provenance, pre-checks) then
                  tools.sib.cli qa (validator of record).
  5. record     — run_manifest.py receipts under <LIBRARY>/runs/<RUN-ID>/.

This module drives 1, 2 and 5 mechanically and hands 3/4 to the agent + validator;
its job is to make every step's evidence inspectable and fail-closed.

Usage:
  python3 run_build.py preflight --library <LIB> --run-dir <runs/RUN-001> --repo name=path ...
  python3 run_build.py pack --library <LIB> --run-dir <runs/RUN-001> --artifact-id CUR-01 \
      [--spec <pack_spec.json>]
"""
from __future__ import annotations

import argparse
import hashlib
import json
import subprocess
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent


def _fail(msg: str):
    print(f"run_build: FATAL: {msg}", file=sys.stderr)
    sys.exit(2)


def _sh(cmd: list[str]) -> int:
    print("+", " ".join(cmd))
    return subprocess.run(cmd).returncode


def _run_id_from_dir(run_dir: Path) -> str:
    rid = run_dir.name
    if not rid.startswith("SIB-"):
        _fail(f"run dir must be named <RUN-ID> (SIB-...), got {rid}")
    return rid


def cmd_preflight(args) -> int:
    library, run_dir = Path(args.library), Path(args.run_dir)
    run_id = _run_id_from_dir(run_dir)
    report = run_dir / "preflight" / "resolution_report.json"
    rc = _sh([sys.executable, str(HERE / "source_resolver.py"),
              "--library", str(library),
              "--out", str(report)]
             + [f"--repo={r}" for r in args.repo])
    if not report.exists():
        _fail("resolver produced no report")
    if rc != 0:
        # sources failed — disclosed, and the family gate below decides which
        # families are blocked. Global failure is not itself a wave abort:
        # the gate law is per-family primary coverage (PIPELINE.md §5 layer 1).
        print("run_build: some sources FAILED/PARTIAL — evaluating the per-family "
              "primary-coverage gate against the report")
    # policy gate: each requested family must have >=1 RESOLVED primary source
    import yaml  # local import; preflight already proved the env
    policy = yaml.safe_load((HERE / "evidence_policy.yaml").read_text(encoding="utf-8"))
    res = json.loads(report.read_text(encoding="utf-8"))
    ok_ids = {s["id"] for s in res["sources"] if s["status"] == "RESOLVED"}
    fams = args.family or []
    blocked = []
    for fam in fams:
        primaries = (policy.get("families", {}).get(fam, {}) or {}).get("primary", [])
        import fnmatch
        if not any(fnmatch.fnmatch(sid, p) for sid in ok_ids for p in primaries):
            blocked.append(fam)
    if blocked:
        _fail(f"families with NO resolved primary source: {', '.join(blocked)}")
    (run_dir / "preflight").mkdir(parents=True, exist_ok=True)
    failed_ids = res["summary"]["failed_ids"]
    partial_ids = res["summary"]["partial_ids"]
    (run_dir / "preflight" / "PREFLIGHT_STATE.txt").write_text(
        f"run_id: {run_id}\nfamilies: {', '.join(fams)}\n"
        f"resolved_sources: {res['summary']['resolved']}/{res['summary']['total']}\n"
        f"gate: PASS (all requested families have >=1 RESOLVED primary source)\n"
        f"disclosed_failed_sources: {', '.join(failed_ids) if failed_ids else 'none'}\n"
        f"disclosed_partial_sources: {', '.join(partial_ids) if partial_ids else 'none'}\n"
        f"law: failures outside the requested families' primary coverage are "
        f"disclosed, never silently accepted (source_gaps stay disclosed)\n",
        encoding="utf-8")
    print(f"run_build: preflight PASS for families {', '.join(fams)} "
          f"({res['summary']['resolved']}/{res['summary']['total']} sources resolved; "
          f"{len(failed_ids)} failed sources disclosed)")
    return 0


def cmd_pack(args) -> int:
    library, run_dir = Path(args.library), Path(args.run_dir)
    run_id = _run_id_from_dir(run_dir)
    family = args.family or args.artifact_id.split("-")[0]
    spec = run_dir / "evidence" / args.artifact_id / "pack_spec.json"
    out = run_dir / "evidence" / args.artifact_id / "evidence_pack.json"
    cmd = [sys.executable, str(HERE / "evidence_pack.py"),
           "--library", str(library), "--artifact-id", args.artifact_id,
           "--family", family, "--run-id", run_id,
           "--policy", str(HERE / "evidence_policy.yaml"),
           "--resolution", str(run_dir / "preflight" / "resolution_report.json"),
           "--out", str(out)]
    if spec.exists() or args.spec:
        cmd += ["--spec", str(args.spec or spec)]
    rc = _sh(cmd)
    if rc != 0:
        return rc
    digest = hashlib.sha256(out.read_bytes()).hexdigest()
    (run_dir / "evidence" / args.artifact_id / "evidence_pack.sha256").write_text(digest + "\n", encoding="utf-8")
    print(f"run_build: pack {args.artifact_id} sha256={digest}")
    return 0


def cmd_record(args) -> int:
    run_dir = Path(args.run_dir)
    mpath = run_dir / "run_manifest.json"
    if not mpath.exists():
        _fail("run_manifest.json not initialized (run run_manifest.py init first)")
    return _sh([sys.executable, str(HERE / "run_manifest.py"), "validate", str(mpath)])


def main() -> int:
    ap = argparse.ArgumentParser(description="SIB-GEN run orchestrator")
    sub = ap.add_subparsers(dest="cmd", required=True)

    p_pre = sub.add_parser("preflight")
    p_pre.add_argument("--library", required=True)
    p_pre.add_argument("--run-dir", required=True)
    p_pre.add_argument("--repo", action="append", default=[])
    p_pre.add_argument("--family", action="append", default=[])

    p_pack = sub.add_parser("pack")
    p_pack.add_argument("--library", required=True)
    p_pack.add_argument("--run-dir", required=True)
    p_pack.add_argument("--artifact-id", required=True)
    p_pack.add_argument("--family", default=None)
    p_pack.add_argument("--spec", default=None)

    p_rec = sub.add_parser("record")
    p_rec.add_argument("--run-dir", required=True)

    args = ap.parse_args()
    if args.cmd == "preflight":
        return cmd_preflight(args)
    if args.cmd == "pack":
        return cmd_pack(args)
    if args.cmd == "record":
        return cmd_record(args)
    return 0


if __name__ == "__main__":
    sys.exit(main())
