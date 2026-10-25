#!/usr/bin/env python3
"""SIB artifact generation — emit the Z.ai agent task / ingest the returned draft.

The agent of record (the Z.ai run in the operator's session) is the execution
engine; this module is the governance wrapper:
  --emit       write runs/<RUN_ID>/agent_task.md (instruction + artifact row +
               evidence-policy entry + pack index + output contract with V2
               provenance pre-pinned from the run manifest)
  --ingest F   verify the draft front matter against the run manifest (ids,
               provenance pins, no placeholders) and land it into artifacts/
               as status GENERATED, recording the artifact sha256 in the run
               record. Rejections are recorded, never silently repaired.
"""
from __future__ import annotations

import argparse
import re
import sys
from datetime import date
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

try:
    import yaml  # type: ignore
except ImportError:  # pragma: no cover
    yaml = None

V2_REQUIRED_PROV = ("source_manifest", "generation_run_id",
                    "generator_provider", "generator_model")
FORBIDDEN_PLACEHOLDERS = ("<", "none", "unknown", "tbd", "todo", "fixme")


class IngestError(SystemExit):
    def __init__(self, msg: str):
        super().__init__(f"REJECTED (ingest): {msg}")


def _require_yaml() -> None:
    if yaml is None:
        raise IngestError("PyYAML is required by the SIB generator wrapper")


def parse_front_matter(text: str) -> tuple[dict, str]:
    lines = text.replace("\r\n", "\n").split("\n")
    if not lines or lines[0].strip() != "---":
        raise IngestError("draft has no opening '---' front-matter delimiter")
    try:
        close = next(i for i in range(1, len(lines)) if lines[i].strip() == "---")
    except StopIteration:
        raise IngestError("draft has no closing '---' front-matter delimiter")
    meta = yaml.safe_load("\n".join(lines[1:close]))
    if not isinstance(meta, dict):
        raise IngestError("front matter is not a mapping")
    return meta, "\n".join(lines[close + 1:])


def emit_task(run: dict, artifact_id: str, pack: dict, library: Path,
              manifest_row: dict | None = None) -> Path:
    prov = run["manifest"]["generator"]
    pack_index = "\n".join(
        f"- {i.get('source_id')} [{i.get('role', '?')}] {i.get('path', i.get('disclosure', ''))}"
        f" (sha256 {str(i.get('sha256', ''))[:12]})"
        for i in pack["items"])
    task = f"""# SIB generation task — {artifact_id}

Run: {run['run_id']} | provider {prov.get('provider')} | model {prov.get('model')} | prompt pack {prov.get('prompt_pack')}

{chr(35)} 1. Master instruction
Execute the SIB_ZAI_PROMPTS_V1.md master generation instruction (§1) for artifact
{artifact_id} of {run['manifest']['course']}, grounded EXCLUSIVELY in the evidence
pack below. Family prompt: SIB_NOTEBOOKLM_PROMPTS_V1.md §2-§13 (incorporated by
reference), the entry matching family {pack['family']}.

{chr(35)} 2. Artifact row (manifest.yaml)
{_yaml_block(manifest_row) or '(row not supplied — read manifest.yaml of the library)'}

{chr(35)} 3. Evidence-policy restrictions (families.{pack['family']})
""" + "\n".join(f"- {r}" for r in pack["restrictions"]) + f"""

{chr(35)} 4. Evidence pack ({len(pack['items'])} items, sha256 {pack['pack_sha256'][:16]}…)
Full pack: {run['run_dir'] / 'evidence' / f'{artifact_id}.pack.json'}
{pack_index}

{chr(35)} 5. Output contract
- Canonical filename: <SUBJECT>_<SPEC>_{artifact_id}_<SLUG>.md
- Front matter: schema V2 (SIB_ARTIFACT_SCHEMA_V2.md §2), 15 required fields,
  status: GENERATED, generated_by: zai_agent, provenance EXACTLY:
    source_manifest: (the library's source manifest identifier)
    generation_run_id: "{run['run_id']}"
    generator_provider: "{prov.get('provider')}"
    generator_model: "{prov.get('model')}"
    generator_agent_version: "{prov.get('prompt_pack')}"
- Universal sections §4; stable record IDs; current/legacy separation;
  every load-bearing claim cites a pack item + locator; nothing invented.
"""
    path = run["run_dir"] / "agent_task.md"
    path.write_text(task)
    return path


def _yaml_block(row: dict | None) -> str:
    if not row:
        return ""
    return yaml.safe_dump(row, sort_keys=False, allow_unicode=True).strip()


def ingest_draft(run: dict, artifact_id: str, draft_path: Path, library: Path,
                 expected_manifest_ref: str, force: bool = False) -> Path:
    _require_yaml()
    text = draft_path.read_text()
    meta, _body = parse_front_matter(text)
    if str(meta.get("artifact_id")) != artifact_id:
        raise IngestError(f"artifact_id {meta.get('artifact_id')!r} != run artifact {artifact_id!r}")
    if str(meta.get("sib_protocol")) != "SIB-1.0":
        raise IngestError("sib_protocol must be SIB-1.0")
    if str(meta.get("status")) != "GENERATED":
        raise IngestError(f"landing artifacts may declare only GENERATED (got {meta.get('status')!r})")
    if str(meta.get("generated_by")) != "zai_agent":
        raise IngestError(f"generated_by must be zai_agent (got {meta.get('generated_by')!r})")
    prov = meta.get("provenance") or {}
    if not isinstance(prov, dict):
        raise IngestError("provenance must be a mapping")
    gen = run["manifest"]["generator"]
    expected = {
        "generation_run_id": run["run_id"],
        "generator_provider": gen.get("provider"),
        "generator_model": gen.get("model"),
        "generator_agent_version": gen.get("prompt_pack"),
        "source_manifest": expected_manifest_ref,
    }
    for key, want in expected.items():
        got = str(prov.get(key, "")).strip()
        if not got or got.lower() in FORBIDDEN_PLACEHOLDERS:
            raise IngestError(f"provenance.{key} missing/placeholder")
        if key != "source_manifest" and got != str(want):
            raise IngestError(f"provenance.{key} {got!r} does not match run record {want!r}")
    for key in V2_REQUIRED_PROV:
        if key not in prov:
            raise IngestError(f"provenance.{key} missing (schema V2)")

    from run_manifest import record_outcome, sha256_file  # local import: sibling module
    target = library / "artifacts" / draft_path.name
    if target.exists() and not force:
        raise IngestError(f"refusing to overwrite existing artifact: {target} (--force to disclose)")
    library.joinpath("artifacts").mkdir(exist_ok=True)
    target.write_text(text)
    record_outcome(run, artifact_id, "LANDED",
                   artifact_file=str(target.relative_to(library)),
                   artifact_sha256=sha256_file(target))
    return target


def main() -> int:  # pragma: no cover - used via run_build.py
    ap = argparse.ArgumentParser(description="SIB artifact emit/ingest wrapper")
    ap.add_argument("mode", choices=["emit", "ingest"])
    ap.add_argument("--run-dir", type=Path, required=True)
    ap.add_argument("--library", type=Path, required=True)
    ap.add_argument("--artifact", required=True)
    ap.add_argument("--draft", type=Path, default=None)
    ap.add_argument("--source-manifest-ref", default="")
    ap.add_argument("--force", action="store_true")
    args = ap.parse_args()
    _require_yaml()
    manifest = yaml.safe_load((args.run_dir / "run_manifest.yaml").read_text())
    run = {"run_id": manifest["run_id"], "run_dir": args.run_dir, "manifest": manifest}
    if args.mode == "ingest":
        if not args.draft or not args.source_manifest_ref:
            ap.error("--draft and --source-manifest-ref are required for ingest")
        target = ingest_draft(run, args.artifact, args.draft, args.library,
                              args.source_manifest_ref, args.force)
        print(f"landed: {target}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
