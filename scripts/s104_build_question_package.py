#!/usr/bin/env python3
"""s104_build_question_package.py — build the ADR-026 sme-question-package/1.0
ZIP for one course's SME exam-question corpus, ready for the core admin ingest
(POST /api/v1/admin/question-bank/ingest).

Layer-3 (syllabai-core question bank) of the Smart Mark subject-#2 program.
The package carries IDs, marks and content md ONLY — exactly what
SmeQuestionIngestService validates and stores; no learner data crosses here.

Content source of truth: the syllabai-hub content bundle
(content/<course>/questions.json) — the parity-certified transform of the
upstream SME-ExamQuestion corpus (see scripts/verify_4ma1_corpus_parity.py
and download/verify_4ma1_corpus_parity_report.json for the 4MA1 certificate).
The hub bundle md references corpus images by their canonical
raw.githubusercontent URLs (the hub serving plane's convention), so the
package ships NO assets/* and the ingest leaves the core asset store
untouched (ADR-026 amendment).

Ref derivation (must equal the hub join in
src/app/api/core/questions/route.ts):

    sme-eq-<corpusTopicSlug>-q<order>

Known (topicSlug, order) collisions (percentages q34, algebra-toolkit q28 for
4MA1 Higher) are EXCLUDED from the package — first occurrence in corpus order
wins, exactly like the hub join's claimedRefs guard. The hub questions whose
ref collides then degrade to honest local-only practice (expected skipped=2).

Mixed questions (option-bearing parts inside a STRUCTURED question) are
emitted through the Part.options amendment: the ingest emits the production
-pN/-s multi-row family shape that QuestionFamilyAssembler reassembles.

Usage:
    python3 scripts/s104_build_question_package.py \
        --hub-repo /path/to/syllabai-hub \
        --course igcse-maths-a-18-higher \
        --out build/layer3 \
        [--resources-sha <syllabai-resources sha for corpusVersion>]

Outputs: <out>/<course>.question-package.zip (+ .package.json + build report).
"""
from __future__ import annotations

import argparse
import hashlib
import json
import re
import sys
import zipfile
from datetime import datetime, timezone
from pathlib import Path

SUPPORTED_PACKAGE_VERSION = "1.0"
# V30 convention extended for the SME 4-tier corpus (easy/medium/hard/very_hard);
# the 1-5 core scale keeps its SME categorical mapping
DIFFICULTY_MAP = {"easy": 2, "medium": 3, "hard": 4, "very_hard": 5}
EXPECTED_TIME_FLOOR_S = 60
EXPECTED_TIME_PER_MARK_S = 75  # ≈ 4MA1 exam pace (~71 s/mark), documented rule
SPEC_CODE_RE = re.compile(r"^(\d+)\.(\d+)([A-Z]?)$")
MCQ_TYPE = "multiple_choice"


def fail(msg: str) -> None:
    print(f"FAIL: {msg}", file=sys.stderr)
    sys.exit(1)


def part_label(order: int) -> str:
    if order >= 26:
        fail("question has more than 26 parts — label scheme exhausted")
    return chr(ord("a") + order)


def node_codes_for(code: str, section: str | None) -> tuple[str, list[str]]:
    """(primaryTopicCode, secondaryTopicCodes) — the KG node codes this
    question attaches to. Spec codes look like '1.6E' (official spec point
    codes); the node scheme mirrors the 4CH1 precedent
    (<subject>-S<section>-<subsection>) seeded by s105_build_curriculum_draft.
    """
    if not code:
        return "", []
    subs: list[str] = []
    for c in code:
        m = SPEC_CODE_RE.match(c)
        if not m:
            fail(f"spec point code does not parse: {c!r}")
        subs.append(f"{m.group(1)}.{m.group(2)}")
    primary_sub = subs[0]
    primary = f"4MA1-S{primary_sub.split('.')[0]}-{primary_sub}"
    secondaries: list[str] = []
    for s in subs[1:]:
        if s != primary_sub and s not in secondaries:
            secondaries.append(s)
    secondaries = [f"4MA1-S{s.split('.')[0]}-{s}" for s in secondaries]
    return primary, secondaries


def section_number(section_slug: str) -> str:
    m = re.match(r"^(\d+)-", section_slug or "")
    if not m:
        fail(f"sectionSlug does not start with a number: {section_slug!r}")
    return m.group(1)


def build_question(topic: dict, q: dict, course_ns: str) -> tuple[dict | None, str | None]:
    """One hub question -> one package Question (or None + exclusion reason)."""
    order = q["order"]
    ref = f"sme-eq-{topic['topicSlug']}-q{order}"
    parts = q["parts"]
    total_marks = q["totalMarks"]
    if sum(p["marks"] for p in parts) != total_marks:
        fail(f"{ref}: part marks sum {sum(p['marks'] for p in parts)} != totalMarks {total_marks}")
    difficulty = DIFFICULTY_MAP.get(q.get("difficulty"))
    if difficulty is None:
        fail(f"{ref}: unknown difficulty {q.get('difficulty')!r}")

    spec_codes: list[str] = []
    for p in parts:
        for c in p.get("specPointCodes") or []:
            if c not in spec_codes:
                spec_codes.append(c)
    section = section_number(topic.get("sectionSlug") or "")
    if spec_codes:
        primary, secondaries = node_codes_for(spec_codes, section)
    else:
        # 9 corpus questions carry no spec codes — attach to the section UNIT
        # node (exists in the draft tree, under the subject root, honest)
        primary, secondaries = f"4MA1-S{section}", []

    mcq_parts = [p for p in parts if p.get("questionType") == MCQ_TYPE]
    plain_parts = [p for p in parts if p.get("questionType") != MCQ_TYPE]

    if len(mcq_parts) == 1 and not plain_parts:
        # pure single-MCQ question → the original MCQ_SINGLE row shape
        p = mcq_parts[0]
        choices = p.get("choices") or []
        if len(choices) < 2 or sum(1 for c in choices if c.get("isCorrect")) != 1:
            fail(f"{ref}: MCQ part needs >=2 choices and exactly one correct")
        return {
            "externalRef": ref,
            "questionType": "MCQ_SINGLE",
            "stem": p.get("problemMd") or "",
            "marks": p["marks"],
            "difficulty": difficulty,
            "difficultySource": "SME",
            "expectedTimeSeconds": max(EXPECTED_TIME_FLOOR_S, p["marks"] * EXPECTED_TIME_PER_MARK_S),
            "commandWord": p.get("commandWord"),
            "primaryTopicCode": primary,
            "secondaryTopicCodes": secondaries,
            "smeSet": topic.get("setName"),
            "smeDifficulty": q.get("difficulty"),
            "options": [
                {"label": c["label"], "text": c.get("textMd") or "", "isCorrect": bool(c.get("isCorrect"))}
                for c in choices
            ],
            "solutionMd": p.get("solutionMd"),
            "parts": [],
        }, None

    if len(mcq_parts) > 1 and not plain_parts:
        fail(f"{ref}: multi-part pure-MCQ question cannot be expressed (needs "
             f"question-level option sets); no such question exists in this corpus")

    package_parts = []
    for i, p in enumerate(sorted(parts, key=lambda x: x["order"])):
        entry = {
            "label": part_label(i),
            "prompt": p.get("problemMd") or "",
            "marks": p["marks"],
            "commandWord": p.get("commandWord"),
            "solutionMd": p.get("solutionMd"),
        }
        if p.get("questionType") == MCQ_TYPE:
            choices = p.get("choices") or []
            if len(choices) < 2 or sum(1 for c in choices if c.get("isCorrect")) != 1:
                fail(f"{ref} part {i}: MCQ part needs >=2 choices and exactly one correct")
            entry["options"] = [
                {"label": c["label"], "text": c.get("textMd") or "", "isCorrect": bool(c.get("isCorrect"))}
                for c in choices
            ]
        if p.get("sourcePaper"):
            entry["sourcePaper"] = p["sourcePaper"]  # additive; core ignores
        package_parts.append(entry)

    return {
        "externalRef": ref,
        "questionType": "STRUCTURED",
        "stem": "",
        "marks": total_marks,
        "difficulty": difficulty,
        "difficultySource": "SME",
        "expectedTimeSeconds": max(EXPECTED_TIME_FLOOR_S, total_marks * EXPECTED_TIME_PER_MARK_S),
        "commandWord": next((p.get("commandWord") for p in parts if p.get("commandWord")), None),
        "primaryTopicCode": primary,
        "secondaryTopicCodes": secondaries,
        "smeSet": topic.get("setName"),
        "smeDifficulty": q.get("difficulty"),
        "options": [],
        "solutionMd": None,
        "parts": package_parts,
    }, None


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("--hub-repo", required=True, type=Path)
    ap.add_argument("--course", required=True)
    ap.add_argument("--out", required=True, type=Path)
    ap.add_argument("--resources-sha", default=None,
                    help="syllabai-resources HEAD sha pinned into corpusVersion")
    ap.add_argument("--zip", action="store_true", help="also write the ingest ZIP")
    args = ap.parse_args()

    course_dir = args.hub_repo / "content" / args.course
    questions_path = course_dir / "questions.json"
    if not questions_path.is_file():
        fail(f"missing {questions_path}")
    topics = json.loads(questions_path.read_text())

    courses = json.loads((args.hub_repo / "content" / "courses.json").read_text())["courses"]
    course = next((c for c in courses if c["slug"] == args.course), None)
    if course is None:
        fail(f"course {args.course} not in content/courses.json")
    code = course.get("code")
    if not code:
        fail(f"course {args.course} has no registry code")

    # upstream drift guard: the hub bundle must still match the resources
    # manifest totals (the parity certificate's universe) before emitting
    manifest_raw = None
    sha = args.resources_sha
    try:
        import subprocess
        if sha is None:
            sha = subprocess.run(
                ["git", "-C", str(args.hub_repo.parent / "syllabai-resources"),
                 "rev-parse", "--short", "HEAD"],
                capture_output=True, text=True).stdout.strip() or "unknown"
        manifest_raw = subprocess.run(
            ["git", "-C", str(args.hub_repo.parent / "syllabai-resources"),
             "show", f"HEAD:SME-ExamQuestion/{args.course}/manifest.json"],
            capture_output=True, text=True).stdout
    except Exception:  # noqa: BLE001 — resources repo is an optional drift guard
        pass
    if manifest_raw:
        man = json.loads(manifest_raw)
        hub_q = sum(len(t["questions"]) for t in topics)
        hub_p = sum(len(q["parts"]) for t in topics for q in t["questions"])
        if man["totals"]["questions"] != hub_q or man["totals"]["parts"] != hub_p:
            fail(f"hub bundle ({hub_q}q/{hub_p}p) drifted from upstream manifest "
                 f"({man['totals']['questions']}q/{man['totals']['parts']}p) — "
                 f"re-run scripts/verify_4ma1_corpus_parity.py first")

    package_questions: list[dict] = []
    excluded: list[dict] = []
    seen_refs: dict[str, dict] = {}
    n_mcq = n_structured = n_parts = n_options = n_mark_points = 0
    n_mixed = n_option_parts = 0
    no_code_questions = 0

    for topic in topics:
        if not topic.get("topicSlug"):
            fail(f"topic {topic.get('slug')} has no topicSlug — join cannot derive refs")
        for q in topic["questions"]:
            ref = f"sme-eq-{topic['topicSlug']}-q{q['order']}"
            if ref in seen_refs:
                excluded.append({
                    "topicSlug": topic["topicSlug"], "order": q["order"],
                    "id": q["id"], "ref": ref,
                    "keptId": seen_refs[ref]["id"],
                    "reason": "duplicate (topicSlug, order) — known corpus "
                              "collision; first occurrence wins (hub guard parity)",
                })
                continue
            pq, reason = build_question(topic, q, code)
            if pq is None:
                excluded.append({"topicSlug": topic["topicSlug"], "order": q["order"],
                                 "id": q["id"], "ref": ref, "reason": reason})
                continue
            seen_refs[ref] = q
            if not any(p.get("specPointCodes") for p in q["parts"]):
                no_code_questions += 1
            if pq["questionType"] == "MCQ_SINGLE":
                n_mcq += 1
                n_options += len(pq.get("options") or [])
                n_mark_points += 1   # the MCQ row's single mark point
            else:
                n_structured += 1
                option_parts = [pp for pp in pq["parts"] if pp.get("options")]
                plain = [pp for pp in pq["parts"] if not pp.get("options")]
                if option_parts:
                    n_mixed += 1
                    n_option_parts += len(option_parts)
                    n_options += sum(len(pp["options"]) for pp in option_parts)
                    n_mark_points += len(option_parts)  # one -pK row each
                if plain or not option_parts:
                    n_parts += len(pq["parts"]) if not option_parts else len(plain)
                    n_mark_points += len(plain) if option_parts else len(pq["parts"])
            package_questions.append(pq)

    counts = {
        "questions": len(package_questions),
        "mcq": n_mcq,
        "structured": n_structured,
        "mixed": n_mixed,
        # IngestSummary semantics: plain structured part rows (option-bearing
        # parts become -pK MCQ rows, not part rows)
        "parts": n_parts,
        "options": n_options,
        "markPoints": n_mark_points,
        "excluded": len(excluded),
        "hubQuestions": sum(len(t["questions"]) for t in topics),
        "noSpecCodeQuestions": no_code_questions,
    }
    package = {
        "packageVersion": SUPPORTED_PACKAGE_VERSION,
        "corpusVersion": f"{args.course}@{sha or 'unknown'}",
        "generatedAt": datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
        "source": f"sme-eq-{args.course}",
        "counts": counts,
        "questions": package_questions,
    }

    args.out.mkdir(parents=True, exist_ok=True)
    pkg_json = args.out / f"{args.course}.package.json"
    pkg_json.write_text(json.dumps(package, ensure_ascii=False, indent=1) + "\n")

    if args.zip:
        zip_path = args.out / f"{args.course}.question-package.zip"
        with zipfile.ZipFile(zip_path, "w", zipfile.ZIP_DEFLATED) as zf:
            info = zipfile.ZipInfo("package.json", date_time=(2026, 1, 1, 0, 0, 0))
            data = pkg_json.read_bytes()
            zf.writestr(info, data, compress_type=zipfile.ZIP_DEFLATED)
        zip_sha = hashlib.sha256(zip_path.read_bytes()).hexdigest()
    else:
        zip_path, zip_sha = None, None

    report = {
        "course": args.course,
        "code": code,
        "corpusVersion": package["corpusVersion"],
        "counts": counts,
        "excluded": excluded,
        "packageJson": str(pkg_json),
        "zip": str(zip_path) if zip_path else None,
        "zipSha256": zip_sha,
    }
    report_path = args.out / f"{args.course}.build-report.json"
    report_path.write_text(json.dumps(report, ensure_ascii=False, indent=1) + "\n")

    print(json.dumps(counts, indent=1))
    print(f"package.json : {pkg_json}")
    if zip_path:
        print(f"zip          : {zip_path} (sha256 {zip_sha[:16]}…)")
    print(f"report       : {report_path}")


if __name__ == "__main__":
    main()
