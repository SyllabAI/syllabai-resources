#!/usr/bin/env python3
"""SIB artifact generator — provider-neutral stamping + pre-validation (r0).

Division of labor (provider-neutral law):
  * the run agent AUTHORS the artifact body from the run's evidence pack alone;
  * this module assembles the final artifact deterministically: canonical
    filename, the 15-field front matter (schema v1 fields + schema v2
    generator-shape provenance stamped from the run manifest), and runs the
    structural pre-checks BEFORE the validator of record sees the file.

Fail-closed behaviors:
  * refuses to overwrite an existing artifact (regeneration = new version, new run);
  * refuses placeholder provenance values;
  * pre-checks: required front-matter fields, universal section headings,
    record-id format + family match, filename contract.

Usage:
  python3 generate_artifact.py --library <LIBRARY> --artifact-id CUR-01 \
      --subject Chemistry --qualification "International GCSE" --specification 4CH1 \
      --curriculum-version 2017 --run-manifest <runs/RUN/run_manifest.json> \
      --body body_CUR-01.md --out <LIBRARY>/artifacts/
"""
from __future__ import annotations

import argparse
import hashlib
import json
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

REQUIRED_SECTIONS = (
    "Purpose", "Scope", "Executive Summary", "Main Analysis",
    "Evidence / Source Basis", "Limitations / Coverage Gaps", "Research Status",
)
_DATE_RE = re.compile(r"^\d{4}-\d{2}-\d{2}$")


def _bool_arg(v: str) -> bool:
    return str(v).strip().lower() in ("true", "1", "yes", "y")


def _fail(msg: str):
    print(f"generate_artifact: FATAL: {msg}", file=sys.stderr)
    sys.exit(2)


def canonical_filename(subject: str, specification: str, artifact_id: str, slug: str) -> str:
    return f"{subject.upper()}_{specification}_{artifact_id}_{slug}.md"


def build_front_matter(args, manifest: dict, source_manifest_id: str) -> str:
    prov = manifest.get("provider") or {}
    revs = manifest.get("source_revisions") or {}
    rev_lines = []
    for name in sorted(revs):
        rev_lines.append(f"    {name}: \"{revs[name]}\"")
    gen_block = "\n".join(rev_lines)
    fm = f"""---
sib_protocol: SIB-1.0
artifact_id: {args.artifact_id}
artifact_version: {args.artifact_version}
subject: {args.subject}
qualification: {args.qualification}
specification: {args.specification}
curriculum_version: "{args.curriculum_version}"

research_family: {args.research_family}
applicability: {args.applicability}

temporal_scope:
  current: {str(args.temporal_current).lower()}
  legacy: {str(args.temporal_legacy).lower()}

source_scope:
  specification: {str(args.src_specification).lower()}
  textbook: {str(args.src_textbook).lower()}
  question_papers: {str(args.src_question_papers).lower()}
  mark_schemes: {str(args.src_mark_schemes).lower()}
  examiner_reports: {str(args.src_examiner_reports).lower()}
  supplementary: {str(args.src_supplementary).lower()}

status: GENERATED
generated_by: zai_agent
generated_at: {args.generated_at}

provenance:
  source_manifest: "{source_manifest_id}"
  generation_run_id: "{manifest.get('run_id', '')}"
  generator:
    provider: "{prov.get('provider', '')}"
    model: "{prov.get('model', '')}"
    agent_version: "{prov.get('agent_version', '')}"
  source_revisions:
{gen_block}
---"""
    if "<" in prov.get("model", "") or prov.get("model", "").lower() in ("", "none", "unknown", "tbd"):
        _fail("run manifest provider.model is not a concrete runtime-reported value")
    if not _DATE_RE.fullmatch(args.generated_at):
        _fail("generated_at must be YYYY-MM-DD")
    return fm


def prevalidate(final_text: str, artifact_id: str, family: str) -> list[str]:
    errs = []
    m = re.match(r"^---\n(.*?)\n---\n", final_text, re.S)
    if not m:
        return ["front matter missing or malformed"]
    fm_text = m.group(1)
    for field in ("sib_protocol", "artifact_id", "artifact_version", "subject",
                  "qualification", "specification", "curriculum_version",
                  "research_family", "applicability", "temporal_scope",
                  "source_scope", "status", "generated_by", "generated_at",
                  "provenance"):
        if not re.search(rf"^{field}:", fm_text, re.M):
            errs.append(f"required front-matter field missing: {field}")
    body = final_text[m.end():]
    for sec in REQUIRED_SECTIONS:
        if not re.search(rf"^##\s+{re.escape(sec)}\b", body, re.M):
            errs.append(f"universal section missing: {sec}")
    for rid in set(re.findall(r"^###\s+([A-Z]{2,3}-\d{3})\s+—", body, re.M)):
        if not rid.startswith(artifact_id.split("-")[0] + "-"):
            errs.append(f"record {rid} family mismatch (artifact family {family})")
    if "status: GENERATED" not in fm_text:
        errs.append("landing artifacts must declare status: GENERATED")
    return errs


def main() -> int:
    ap = argparse.ArgumentParser(description="SIB artifact stamping + pre-validation (SIB-GEN)")
    ap.add_argument("--library", required=True)
    ap.add_argument("--artifact-id", required=True)
    ap.add_argument("--artifact-version", default="1.0")
    ap.add_argument("--subject", required=True)
    ap.add_argument("--qualification", required=True)
    ap.add_argument("--specification", required=True)
    ap.add_argument("--curriculum-version", required=True)
    ap.add_argument("--research-family", required=True)
    ap.add_argument("--applicability", default="REQUIRED")
    ap.add_argument("--temporal-current", type=_bool_arg, default=True)
    ap.add_argument("--temporal-legacy", type=_bool_arg, default=False)
    ap.add_argument("--src-specification", action="store_true")
    ap.add_argument("--src-textbook", action="store_true")
    ap.add_argument("--src-question-papers", action="store_true")
    ap.add_argument("--src-mark-schemes", action="store_true")
    ap.add_argument("--src-examiner-reports", action="store_true")
    ap.add_argument("--src-supplementary", action="store_true")
    ap.add_argument("--generated-at", required=True)
    ap.add_argument("--run-manifest", required=True)
    ap.add_argument("--source-manifest-id", required=True)
    ap.add_argument("--slug", required=True)
    ap.add_argument("--body", required=True, help="authored body markdown (front matter absent)")
    ap.add_argument("--outdir", required=True)
    args = ap.parse_args()

    manifest = json.loads(Path(args.run_manifest).read_text(encoding="utf-8"))
    fm = build_front_matter(args, manifest, args.source_manifest_id)
    body = Path(args.body).read_text(encoding="utf-8").strip()
    final = fm + "\n\n" + body + "\n"

    errs = prevalidate(final, args.artifact_id, args.research_family)
    if errs:
        for e in errs:
            print(f"generate_artifact: PRECHECK FAIL: {e}", file=sys.stderr)
        return 1

    fname = canonical_filename(args.subject, args.specification, args.artifact_id, args.slug)
    out = Path(args.outdir) / fname
    if out.exists():
        _fail(f"refusing to overwrite existing artifact {out} (regenerate as a new artifact_version/run)")
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(final, encoding="utf-8")
    digest = hashlib.sha256(out.read_bytes()).hexdigest()
    print(f"generate_artifact: {fname} sha256={digest} ({len(final)} chars)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
