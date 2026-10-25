#!/usr/bin/env python3
"""SIB run orchestrator — preflight → evidence pack → run record → agent task.

Modes of record (SIB-GEN):
  --dry-run    preflight only: resolve the artifact's required sources (fail-closed)
               and print the resolution verdict; nothing else is written.
  default      preflight + evidence pack + run record + agent task emission.
               The Z.ai agent then executes the task; the returned draft lands via
               --ingest <draft.md> (generate_artifact.ingest_draft through here).

The orchestrator NEVER calls a model API and never writes outside the library root
(runs/, artifacts/). Canonical planes stay read-only.
"""
from __future__ import annotations

import argparse
import json
import subprocess
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

import evidence_pack as ep  # noqa: E402
import generate_artifact as ga  # noqa: E402
import run_manifest as rm  # noqa: E402
import source_resolver as sr  # noqa: E402


def git_head(repo: Path) -> str:
    try:
        return subprocess.run(["git", "-C", str(repo), "rev-parse", "HEAD"],
                              check=True, capture_output=True, text=True,
                              timeout=30).stdout.strip()
    except Exception:
        return "unresolved"


def main() -> int:
    ap = argparse.ArgumentParser(description="SIB run orchestrator (fail-closed)")
    ap.add_argument("--library", type=Path, required=True,
                    help="course library dir, e.g. SubjectIntelligence/CHEMISTRY_4CH1")
    ap.add_argument("--artifact", required=True, help="one artifact id (e.g. CUR-01)")
    ap.add_argument("--resources-repo", type=Path, required=True)
    ap.add_argument("--pastpapers-repo", type=Path, default=None)
    ap.add_argument("--core-repo", type=Path, default=None)
    ap.add_argument("--generator-model", default="",
                    help="model identifier of record for provenance.generator_model")
    ap.add_argument("--generator-provider", default="z.ai")
    ap.add_argument("--source-manifest-ref", default="",
                    help="identifier the artifact's provenance.source_manifest must carry "
                         "(defaults to '<library> source_manifest.yaml <manifest_version>')")
    ap.add_argument("--dry-run", action="store_true")
    ap.add_argument("--ingest", type=Path, default=None,
                    help="land the returned draft (run dir taken from --run-dir)")
    ap.add_argument("--run-dir", type=Path, default=None)
    ap.add_argument("--force", action="store_true",
                    help="ingest: disclose-overwrite an existing artifact file")
    args = ap.parse_args()

    library = args.library.resolve()
    if not library.is_dir():
        ap.error(f"library dir not found: {library}")
    course = library.name

    # ---- ingest path -----------------------------------------------------
    if args.ingest:
        if not args.run_dir:
            ap.error("--ingest requires --run-dir")
        manifest = rm.__dict__["yaml"].safe_load(
            (args.run_dir / "run_manifest.yaml").read_text())
        run = {"run_id": manifest["run_id"], "run_dir": args.run_dir.resolve(),
               "manifest": manifest}
        aid = manifest["artifact_ids"][0]
        ref = args.source_manifest_ref or f"{course} source_manifest.yaml"
        target = ga.ingest_draft(run, aid, args.ingest, library, ref, args.force)
        print(f"LANDED {aid} -> {target}")
        return 0

    # ---- preflight -------------------------------------------------------
    repo_roots = {"resources": args.resources_repo.resolve()}
    if args.pastpapers_repo:
        repo_roots["pastpapers"] = args.pastpapers_repo.resolve()
    if args.core_repo:
        repo_roots["core"] = args.core_repo.resolve()
    policy = ep.load_policy(library)
    fam = ep.family_of(args.artifact)
    entry = policy["families"][fam]
    wanted = list(entry.get("primary_sources") or []) + list(entry.get("optional_sources") or [])
    resolution = sr.resolve_course(library, repo_roots, wanted,
                                   fatal_ids=set(entry.get("primary_sources") or []))
    resolution["source_revisions"] = {k: git_head(v) for k, v in repo_roots.items()}
    verdict = "OK" if resolution["ok"] else "FAILED"
    print(f"preflight [{args.artifact} / {fam}]: {verdict}")
    for rec in resolution["sources"]:
        marks = ",".join(sorted({p["result"] for p in rec["paths"]}) or {"NO-PATHS"})
        checks = ",".join(sorted({c["result"] for c in rec["identity_checks"]})) or "-"
        print(f"  {rec['source_id']:<22} {marks:<40} identity: {checks}")

    # ---- pack + run record + task ----------------------------------------
    pack = ep.build_pack(library, args.artifact, resolution, policy)
    if args.dry_run:
        print(f"dry-run: pack would be {len(pack['items'])} items "
              f"(sha256 {pack['pack_sha256'][:16]}…) — nothing written")
        return 0 if resolution["ok"] else 2
    if not resolution["ok"]:
        print("FATAL: preflight failed — no run opened (fail-closed)")
        return 2
    if not args.generator_model:
        ap.error("--generator-model is required for a real run "
                 "(provenance.generator_model records the actual model; never assumed)")
    ref = args.source_manifest_ref or (
        f"{course} source_manifest.yaml v"
        f"{(sr.load_manifest(library).get('manifest_version') or '?')}")
    run = rm.open_run(library, course, [args.artifact], resolution,
                      {args.artifact: pack},
                      {"provider": args.generator_provider, "model": args.generator_model,
                       "prompt_pack": "SIB_ZAI_PROMPTS_V1"})
    rm.attach_resolution(run, resolution)
    rm.attach_pack(run, args.artifact, pack)
    manifest_row = None
    import yaml
    m = yaml.safe_load((library / "manifest.yaml").read_text())
    for row in m.get("artifacts") or []:
        if row.get("artifact_id") == args.artifact:
            manifest_row = row
            break
    task_path = ga.emit_task(run, args.artifact, pack, library, manifest_row)
    print(f"run {run['run_id']} opened; agent task -> {task_path}")
    print("next: the Z.ai agent executes the task, then: "
          f"run_build.py --ingest <draft> --run-dir {run['run_dir']} --library {library}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
