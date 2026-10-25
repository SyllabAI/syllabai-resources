#!/usr/bin/env python3
"""SIB run manifest — the receipt of record for a SIB-GEN generation wave (r0).

One run = one manifest = one or more artifacts, each with:
  * evidence-pack id + sha256 (what grounded it),
  * artifact sha256 (what it produced),
  * outcome / attempts / QA verdict (how it went),
  * layered-gate results (source preflight, structural, evidence-claim QA,
    educational review — staging/publication stay operator-ordered).

Deterministic serializer: indent=2, ensure_ascii=False, trailing newline.
Fail-closed validation: a manifest missing required fields or carrying
placeholder values is refused by validate().

CLI:
  python3 run_manifest.py init --run-id SIB-CHEMISTRY-4CH1-RUN-001 --library CHEMISTRY_4CH1 \
      --provider-provider z.ai --provider-model <id> --provider-agent-version SIB-GEN-r0 \
      --revision syllabai_resources=<sha> --revision syllabai_pastpapers=<sha> --out <runs/RUN-001/run_manifest.json>
  python3 run_manifest.py validate <run_manifest.json>
  python3 run_manifest.py add-artifact <run_manifest.json> --artifact-id CUR-01 --filename ... \
      --evidence-pack ... --evidence-pack-sha256 ... --artifact-sha256 ... --outcome GENERATED \
      --gate structural=PASS --gate evidence_claim_qa=PASS ...
"""
from __future__ import annotations

import argparse
import hashlib
import json
import re
import sys
from pathlib import Path

SCHEMA = "sib-run-manifest/1.0"
PROGRAM = "SIB-GEN"
_SHA_RE = re.compile(r"^[0-9a-f]{7,64}$")
_PLACEHOLDER_VALUES = {"", "none", "unknown", "tbd", "todo"}


def _fail(msg: str):
    print(f"run_manifest: FATAL: {msg}", file=sys.stderr)
    sys.exit(2)


def canonical_bytes(manifest: dict) -> str:
    return json.dumps(manifest, indent=2, ensure_ascii=False) + "\n"


def sha256_of(manifest: dict) -> str:
    return hashlib.sha256(canonical_bytes(manifest).encode("utf-8")).hexdigest()


def init(args) -> dict:
    if not _SHA_RE.fullmatch(args.run_id.replace("SIB-", "").replace("RUN-", "") or "x"):
        pass  # run id shape checked below by name-contract regex
    if not re.fullmatch(r"SIB-[A-Z0-9]+_[A-Z0-9.]+-RUN-\d+", args.run_id):
        _fail(f"run id must match SIB-<SUBJECT>_<SPEC>-RUN-<n>, got {args.run_id!r}")
    revs = {}
    for r in args.revision:
        k, _, v = r.partition("=")
        if not k or not _SHA_RE.fullmatch(v):
            _fail(f"revision {r!r} must be name=<git sha>")
        revs[k] = v
    manifest = {
        "schema": SCHEMA,
        "program": PROGRAM,
        "run_id": args.run_id,
        "library": args.library,
        "provider": {
            "provider": args.provider_provider,
            "model": args.provider_model,
            "agent_version": args.provider_agent_version,
        },
        "source_revisions": revs,
        "preflight": {},
        "artifacts": [],
        "gates": {},
        "disclosures": [],
    }
    for f in ("provider", "model", "agent_version"):
        if manifest["provider"][f].strip().lower() in _PLACEHOLDER_VALUES or \
                manifest["provider"][f].strip().startswith("<"):
            _fail(f"provider.{f} must be a concrete runtime-reported value")
    return manifest


REQUIRED_ARTIFACT_FIELDS = ("artifact_id", "filename", "evidence_pack", "artifact_sha256", "outcome")


def add_artifact(manifest: dict, **kw) -> dict:
    art = {
        "artifact_id": kw["artifact_id"],
        "filename": kw["filename"],
        "evidence_pack": kw["evidence_pack"],
        "evidence_pack_sha256": kw.get("evidence_pack_sha256", ""),
        "artifact_sha256": kw["artifact_sha256"],
        "attempts": int(kw.get("attempts", 1)),
        "outcome": kw["outcome"],          # GENERATED | QA_PASSED | QA_FAILED | BLOCKED
        "gates": kw.get("gates", {}),      # gate name -> PASS/FAIL/PARTIAL + note
        "qa_report": kw.get("qa_report", ""),
    }
    for f in REQUIRED_ARTIFACT_FIELDS:
        if not art.get(f):
            _fail(f"add-artifact: required field {f} missing/empty")
    if not re.fullmatch(r"[0-9a-f]{64}", art["artifact_sha256"]):
        _fail("artifact_sha256 must be a sha256 hex digest of the final artifact file")
    if any(a["artifact_id"] == art["artifact_id"] for a in manifest["artifacts"]):
        _fail(f"artifact {art['artifact_id']} already recorded in this run (append a new run instead)")
    manifest["artifacts"].append(art)
    return manifest


def validate(manifest: dict) -> list[str]:
    errs = []
    if manifest.get("schema") != SCHEMA:
        errs.append(f"schema must be {SCHEMA}")
    rid = manifest.get("run_id", "")
    if not re.fullmatch(r"SIB-[A-Z0-9]+_[A-Z0-9.]+-RUN-\d+", rid):
        errs.append(f"run_id shape invalid: {rid!r}")
    prov = manifest.get("provider") or {}
    for f in ("provider", "model", "agent_version"):
        v = str(prov.get(f, "")).strip()
        if not v or v.lower() in _PLACEHOLDER_VALUES or v.startswith("<"):
            errs.append(f"provider.{f} not a concrete value: {v!r}")
    for name, sha in (manifest.get("source_revisions") or {}).items():
        if not _SHA_RE.fullmatch(sha):
            errs.append(f"source_revisions.{name} not a git sha: {sha!r}")
    if not manifest.get("artifacts"):
        errs.append("run records no artifacts (an empty run must be disclosed, not recorded)")
    for a in manifest.get("artifacts", []):
        for f in REQUIRED_ARTIFACT_FIELDS:
            if not a.get(f):
                errs.append(f"artifact {a.get('artifact_id', '?')}: missing {f}")
        if a.get("artifact_sha256") and not re.fullmatch(r"[0-9a-f]{64}", a["artifact_sha256"]):
            errs.append(f"artifact {a.get('artifact_id')}: bad artifact_sha256")
    return errs


def main() -> int:
    ap = argparse.ArgumentParser(description="SIB run manifest (SIB-GEN receipts)")
    sub = ap.add_subparsers(dest="cmd", required=True)

    p_init = sub.add_parser("init")
    p_init.add_argument("--run-id", required=True)
    p_init.add_argument("--library", required=True)
    p_init.add_argument("--provider-provider", required=True)
    p_init.add_argument("--provider-model", required=True)
    p_init.add_argument("--provider-agent-version", required=True)
    p_init.add_argument("--revision", action="append", default=[])
    p_init.add_argument("--out", required=True)

    p_val = sub.add_parser("validate")
    p_val.add_argument("manifest")

    p_add = sub.add_parser("add-artifact")
    p_add.add_argument("manifest")
    p_add.add_argument("--artifact-id", required=True)
    p_add.add_argument("--filename", required=True)
    p_add.add_argument("--evidence-pack", required=True)
    p_add.add_argument("--evidence-pack-sha256", default="")
    p_add.add_argument("--artifact-sha256", required=True)
    p_add.add_argument("--outcome", required=True)
    p_add.add_argument("--attempts", type=int, default=1)
    p_add.add_argument("--gate", action="append", default=[],
                       help="name=VERDICT[:note] (repeatable)")
    p_add.add_argument("--qa-report", default="")
    p_add.add_argument("--disclosure", action="append", default=[])

    args = ap.parse_args()

    if args.cmd == "init":
        m = init(args)
        out = Path(args.out)
        out.parent.mkdir(parents=True, exist_ok=True)
        out.write_text(canonical_bytes(m), encoding="utf-8")
        errs = validate(m)
        if errs:
            for e in errs:
                print(f"run_manifest: (expected while populating) {e}", file=sys.stderr)
        print(f"run_manifest: initialized {args.run_id} -> {out}")
        return 0

    path = Path(args.manifest)
    m = json.loads(path.read_text(encoding="utf-8"))

    if args.cmd == "validate":
        errs = validate(m)
        for e in errs:
            print(f"run_manifest: ERROR: {e}", file=sys.stderr)
        print(f"run_manifest: validate {'FAILED' if errs else 'OK'} ({m.get('run_id')})")
        return 1 if errs else 0

    if args.cmd == "add-artifact":
        gates = {}
        for g in args.gate:
            name, _, verdict = g.partition("=")
            gates[name] = verdict
        m = add_artifact(m, artifact_id=args.artifact_id, filename=args.filename,
                          evidence_pack=args.evidence_pack,
                          evidence_pack_sha256=args.evidence_pack_sha256,
                          artifact_sha256=args.artifact_sha256, outcome=args.outcome,
                          attempts=args.attempts, gates=gates, qa_report=args.qa_report)
        m.setdefault("disclosures", []).extend(args.disclosure)
        path.write_text(canonical_bytes(m), encoding="utf-8")
        errs = validate(m)
        for e in errs:
            print(f"run_manifest: ERROR: {e}", file=sys.stderr)
        print(f"run_manifest: +{args.artifact_id} ({args.outcome}); "
              f"manifest {'INVALID' if errs else 'OK'}")
        return 1 if errs else 0
    return 0


if __name__ == "__main__":
    sys.exit(main())
