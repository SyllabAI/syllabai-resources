#!/usr/bin/env python3
"""SIB course-library instantiator — onboards ANY course into SubjectIntelligence/.

Implements the operator directive of record (2026-10-25): "SubjectIntelligence will
host all courses not just 4ch1". One SI library per qualification, dir name
<SUBJECT>_<SPEC>, scaffolded from pipeline/templates/course/.

Usage:
    python3 pipeline/new_course.py CHEMISTRY_4BI1 \
        --subject "Biology" --qualification "International GCSE" \
        --curriculum-version 2017 [--taxonomy /path/to/SyllabAI/syllabai] [--root DIR]

Behaviour (fail-closed):
  - refuses to run if the target library directory already exists
  - refuses a library name outside ^[A-Z][A-Z0-9]*_[A-Z0-9.]+$
    (the <SUBJECT>_<SPEC> contract; SPEC is the official spec code)
  - creates the five work dirs with .gitkeep sentinels
  - writes manifest.yaml / source_manifest.yaml / curriculum_registry.yaml from the
    templates with placeholder substitution
  - with --taxonomy, imports tools.sib.taxonomy from the given SyllabAI/syllabai
    checkout and emits the full 95-row artifacts section (HIS family OPTIONAL,
    everything else REQUIRED — applicability review remains a mandatory onboarding
    step); records the taxonomy pin commit in the manifest header
  - NEVER touches canonical planes, other libraries, or the validator of record
"""
import argparse
import datetime
import re
import subprocess
import sys
from pathlib import Path

TEMPLATES = Path(__file__).resolve().parent / "templates" / "course"
NAME_RE = re.compile(r"^[A-Z][A-Z0-9]*_[A-Z0-9.]+$")
WORK_DIRS = ("artifacts", "qa-reports", "staged", "published", "chunks")


def taxonomy_pin(checkout: Path) -> str:
    try:
        return subprocess.run(
            ["git", "-C", str(checkout), "rev-parse", "HEAD"],
            check=True, capture_output=True, text=True, timeout=30,
        ).stdout.strip()
    except Exception as exc:  # pragma: no cover - defensive
        print(f"WARNING: could not resolve taxonomy pin commit: {exc}", file=sys.stderr)
        return "unresolved"


def emit_manifest_rows(taxonomy_checkout: Path) -> str:
    sys.path.insert(0, str(taxonomy_checkout))
    try:
        from tools.sib import taxonomy  # type: ignore
    finally:
        sys.path.pop(0)
    if taxonomy.TAXONOMY_SIZE != 95:
        raise SystemExit(
            f"FATAL: taxonomy of record unexpected size {taxonomy.TAXONOMY_SIZE} (expected 95); "
            "the protocol changed — re-pin and update the pipeline before onboarding."
        )
    rows = []
    for aid in taxonomy.all_artifact_ids():
        family = taxonomy.family_of(aid)
        applicability = "OPTIONAL" if family == "HIS" else "REQUIRED"
        rows.append(f"  - artifact_id: {aid}\n    applicability: {applicability}")
    return "\n".join(rows)


def main() -> int:
    ap = argparse.ArgumentParser(description="Scaffold a new SIB course library.")
    ap.add_argument("library", help="library dir name, <SUBJECT>_<SPEC> (e.g. BIOLOGY_4BI1)")
    ap.add_argument("--subject", required=True, help='e.g. "Biology"')
    ap.add_argument("--qualification", required=True, help='e.g. "International GCSE"')
    ap.add_argument("--curriculum-version", default="", help='e.g. "2017" (empty ok)')
    ap.add_argument("--taxonomy", type=Path, default=None,
                    help="path to a SyllabAI/syllabai checkout; enables the generated "
                         "95-row manifest artifacts section")
    ap.add_argument("--root", type=Path, default=Path(__file__).resolve().parent.parent,
                    help="SubjectIntelligence root (default: the repo dir this script lives in)")
    args = ap.parse_args()

    if not NAME_RE.match(args.library):
        ap.error(f"library name {args.library!r} violates the <SUBJECT>_<SPEC> contract "
                 f"(^[A-Z][A-Z0-9]*_[A-Z0-9.]+$)")
    lib = args.root / args.library
    if lib.exists():
        ap.error(f"FATAL: {lib} already exists — never overwrite a library (fail-closed)")
    if not TEMPLATES.is_dir():
        ap.error(f"FATAL: templates missing at {TEMPLATES}")

    ctx = {
        "LIBRARY": args.library,
        "SUBJECT": args.subject,
        "SPECIFICATION": args.library.split("_", 1)[1],
        "QUALIFICATION": args.qualification,
        "CURRICULUM_VERSION": args.curriculum_version,
        "YEAR": datetime.date.today().isoformat(),
    }

    lib.mkdir(parents=True)
    for d in WORK_DIRS:
        (lib / d).mkdir()
        (lib / d / ".gitkeep").write_text("")

    pin_note = ""
    if args.taxonomy:
        rows = emit_manifest_rows(args.taxonomy)
        pin = taxonomy_pin(args.taxonomy)
        pin_note = f"\n# artifacts section generated from tools/sib/taxonomy.py @ {pin}\n"
        (lib / "manifest.yaml").write_text(
            fill("manifest.template.yaml", ctx).replace(
                "artifacts:\n  # --- GENERATED SECTION (new_course.py --taxonomy) -------------------------\n"
                "  # One row per taxonomy artifact of record, emitted as:\n"
                "  #   - artifact_id: <ID>\n"
                "  #     applicability: REQUIRED\n",
                f"artifacts:{pin_note}\n{rows}\n",
            )
        )
    else:
        (lib / "manifest.yaml").write_text(fill("manifest.template.yaml", ctx))
    (lib / "source_manifest.yaml").write_text(fill("source_manifest.template.yaml", ctx))
    (lib / "curriculum_registry.yaml").write_text(fill("curriculum_registry.template.yaml", ctx))

    print(f"scaffolded {lib}")
    print("next steps (docs/COURSE_ONBOARDING.md):")
    print("  2. inventory-first sweep -> fill source_manifest.yaml (six groups + gaps)")
    print("  3. pin curriculum_registry.yaml from the course's curriculum plane of record")
    print("  4. applicability review of manifest.yaml rows (subject-specific)")
    print("  5. gate: python3 -m tools.sib.cli validate-manifest <this library>")
    return 0


def fill(template_name: str, ctx: dict) -> str:
    text = (TEMPLATES / template_name).read_text()
    for key, value in ctx.items():
        text = text.replace("{{" + key + "}}", value)
    leftover = re.findall(r"\{\{[A-Z_]+\}\}", text)
    if leftover:
        raise SystemExit(f"FATAL: unsubstituted placeholders in {template_name}: {leftover}")
    return text


if __name__ == "__main__":
    raise SystemExit(main())
