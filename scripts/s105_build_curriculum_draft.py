#!/usr/bin/env python3
"""s105_build_curriculum_draft.py — build the T-010 curriculum-draft.json
(schema 1.1) for one course from the parsed official spec, ready for
POST /api/v1/teacher/curriculum/drafts (TEACHER/ADMIN).

This is the layer-3 PREREQUISITE of the Smart Mark subject-#2 program: the
SME question-bank ingest resolves every package question's primaryTopicCode
against core's knowledge_nodes, and the hub join resolves the course code to
the subject root. Without this draft, a 4MA1 package ingest fails closed
("unknown KG code: …") and the hub join answers no_subject.

Tree shape (mirrors the 4CH1 precedent, e.g. node 4CH1-S1-c):

    SUBJECT 4MA1-ROOT            (created by CurriculumIngestionService)
      UNIT     4MA1-S1 .. S6    (the 6 content sections of the spec)
        TOPIC  4MA1-S1-1.1 ..   (the spec subsections, code = letter "1.1")
          SUBTOPIC 4MA1-S1-1.1A ..  (the spec points, code = official_code)

Codes are namespace-qualified by CurriculumIngestionService.namespaceOf(code)
→ "4MA1" + "-" + draft code; s104_build_question_package derives the same
strings, and s104_verify_question_package asserts the containment.

Everything lands SUGGESTED (the pipeline never self-validates); spec-point
nodes carry confidence 0.95 (8/242 parse-flagged rows remain for teacher
review), structure nodes 1.0 (deterministic table parse, gates G1-G4 green).

Usage:
    python3 scripts/s105_build_curriculum_draft.py \
        --hub-repo /path/to/syllabai-hub \
        --course igcse-maths-a-18-higher \
        --resources-sha <sha> \
        --out build/layer3/4ma1-curriculum-draft.json
"""
from __future__ import annotations

import argparse
import json
import re
import subprocess
import sys
from pathlib import Path

SPEC_CODE_RE = re.compile(r"^(\d+)\.(\d+)([A-Z]?)$")


def fail(msg: str) -> None:
    print(f"FAIL: {msg}", file=sys.stderr)
    sys.exit(1)


def git_show(resources: Path, path: str) -> str:
    r = subprocess.run(["git", "-C", str(resources), "show", f"HEAD:{path}"],
                       capture_output=True, text=True)
    if r.returncode != 0:
        fail(f"git show {path}: {r.stderr.strip()}")
    return r.stdout


def subsection_key(code: str) -> tuple[int, int]:
    m = SPEC_CODE_RE.match(code)
    return (int(m.group(1)), int(m.group(2))) if m else (999, 999)


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("--hub-repo", required=True, type=Path)
    ap.add_argument("--course", required=True, help="e.g. igcse-maths-a-18-higher")
    ap.add_argument("--resources", type=Path, default=None,
                    help="syllabai-resources clone (default: <hub-repo>/../syllabai-resources)")
    ap.add_argument("--resources-sha", default=None)
    ap.add_argument("--board", default="Pearson Edexcel")
    ap.add_argument("--qualification", default="International GCSE")
    ap.add_argument("--out", required=True, type=Path)
    args = ap.parse_args()

    resources = args.resources or (args.hub_repo.parent / "syllabai-resources")
    spec_dir = f"Official-Specifications/parsed/{args.course.replace('-18-higher', '').replace('-19', '').replace('-17', '')}"
    # the parsed dir drops the year suffix (igcse-maths-a-18-higher -> igcse-maths-a)
    topics = json.loads(git_show(resources, f"{spec_dir}/topics.json"))
    spec = json.loads(git_show(resources, f"{spec_dir}/spec_points.json"))
    parse_report = json.loads(git_show(resources, f"{spec_dir}/parse_report.json"))

    courses = json.loads((args.hub_repo / "content" / "courses.json").read_text())["courses"]
    course = next((c for c in courses if c["slug"] == args.course), None)
    if course is None:
        fail(f"course {args.course} not in content/courses.json")
    code = course["code"]

    # subsection titles: the hub KG carries operator-approved display titles
    hub_cur = json.loads((args.hub_repo / "content" / args.course / "curriculum.json").read_text())
    sub_titles: dict[str, str] = {}
    for n in hub_cur["nodes"]:
        if n.get("family") == "SUBTOPIC" and ":SUB" in n["code"]:
            letter = n["code"].split(":SUB", 1)[1]
            sub_titles.setdefault(letter, n.get("title") or "")

    if not parse_report.get("gates", {}).get("ALL_PASS"):
        fail("spec parse gates are not ALL_PASS — do not seed the KG from this parse")

    # the higher-tier content rows of the parsed topic table (dedup by number)
    section_titles: dict[str, str] = {}
    for t in topics["topics"]:
        num = str(t.get("number"))
        if num.isdigit():
            section_titles.setdefault(num, t["title"])
    sections = sorted(section_titles, key=int)
    if not sections:
        fail("parsed topics carry no numbered content sections")

    # spec points grouped by (section, subsection); the parse carries BOTH
    # tiers (242 rows / 188 distinct official_codes) — dedupe by official_code
    points: dict[str, list[dict]] = {}
    subsections: dict[str, dict] = {}
    seen_codes: set[str] = set()
    for p in spec["spec_points"]:
        m = SPEC_CODE_RE.match(p["official_code"])
        if not m:
            fail(f"official_code does not parse: {p['official_code']!r}")
        if p["official_code"] in seen_codes:
            continue
        seen_codes.add(p["official_code"])
        sec, sub = m.group(1), m.group(2)
        letter = f"{sec}.{sub}"
        subsections.setdefault(letter, {"section": sec, "letter": letter})
        points.setdefault(letter, []).append(p)
    for letter in subsections:
        if letter not in sub_titles:
            print(f"note: subsection {letter} has no hub KG title — falling back to section title")

    sha = args.resources_sha or subprocess.run(
        ["git", "-C", str(resources), "rev-parse", "--short", "HEAD"],
        capture_output=True, text=True).stdout.strip()
    pdf_sha1 = spec["spec_points"][0]["provenance"]["pdf_sha1"]

    units = []
    n_topics = n_subtopics = 0
    for sec in sections:
        sec_letters = sorted((l for l, s in subsections.items() if s["section"] == sec),
                             key=subsection_key)
        topic_list = []
        for letter in sec_letters:
            subs = []
            for p in sorted(points[letter], key=lambda x: x["official_code"]):
                subs.append({
                    "code": p["official_code"],
                    "title": (p.get("text") or "")[:200] or p["official_code"],
                    "confidence": 0.95,
                })
            topic_list.append({
                "code": letter,
                "title": sub_titles.get(letter) or section_titles[sec] + f" ({letter})",
                "subtopics": subs,
                "confidence": 1.0,
            })
            n_subtopics += len(subs)
        units.append({
            "code": f"S{sec}",
            "title": section_titles[sec],
            "topics": topic_list,
            "confidence": 1.0,
        })
        n_topics += len(topic_list)

    draft = {
        "schemaVersion": "1.1",
        "board": args.board,
        "qualification": args.qualification,
        "code": code,
        "title": f"{args.board} {args.qualification} Maths A ({code}) — Higher tier",
        "subject": {"code": code, "name": "Maths A"},
        "units": units,
        "provenance": {
            "sourceDocumentId": "pearson-international-gcse-in-mathematics-spec-a",
            "sourceChecksum": f"sha1:{pdf_sha1}",
            "engine": "syllabai-resources Official-Specifications parser",
            "engineVersion": "canonical-builder-2.0",
            "extractionMethod": (f"official-spec-parse/1.0 (gates G1-G4 ALL_PASS, "
                                 f"syllabai-resources@{sha})"),
            "validationStatus": "SUGGESTED",
        },
    }

    # self-checks: uniqueness + node-code shape the package builder will derive
    seen: set[str] = set()
    for u in draft["units"]:
        for key in (f"4MA1-{u['code']}",):
            if key in seen:
                fail(f"duplicate node code {key}")
            seen.add(key)
        for t in u["topics"]:
            for key in (f"4MA1-{u['code']}-{t['code']}",):
                if key in seen:
                    fail(f"duplicate node code {key}")
                seen.add(key)
            for s in t["subtopics"]:
                key = f"4MA1-{u['code']}-{s['code']}"
                if key in seen:
                    fail(f"duplicate node code {key}")
                seen.add(key)

    counts = {"units": len(units), "topics": n_topics, "subtopics": n_subtopics,
              "nodeCodes": len(seen) + 1, "specPointsParsed": len(spec["spec_points"])}
    args.out.parent.mkdir(parents=True, exist_ok=True)
    args.out.write_text(json.dumps(draft, ensure_ascii=False, indent=1) + "\n")
    print(json.dumps(counts, indent=1))
    print(f"draft: {args.out}")
    print("note: POST this to /api/v1/teacher/curriculum/drafts (TEACHER/ADMIN) "
          "BEFORE the question-bank ingest; everything lands SUGGESTED.")


if __name__ == "__main__":
    main()
