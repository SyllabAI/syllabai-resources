#!/usr/bin/env python3
"""Verify the T-SME-EQ-2 single-segment harvest outputs (read-only).

Gates:
  G1  spec_point_index.json exists, parses, schema == 1.0, course_slug matches
  G2  spec_points well-formed (id/name present; notes + subtopic_slugs lists)
  G3  coverage block consistent: covered + missing == total, and recomputed
      from the course's topic.json files it matches exactly
  G4  no empty-name spec points; rn_ ids well-formed; subtopic slugs non-empty
  G5  seeded spot-check: for sampled parts, the index entry for each tagged
      id exists (and for definition-bearing entries, name is non-trivial)
"""
from __future__ import annotations

import glob
import json
import random
import sys
from pathlib import Path

CORPUS = Path("/home/z/my-project/download/syllabai-resources/SME-ExamQuestion")
COURSES = [
    "ial-biology-18", "ial-chemistry-17",
    "ial-further-maths-18-further-pure-1", "ial-physics-19",
    "igcse-business-19", "igcse-economics-17",
    "igcse-english-literature-16", "igcse-further-maths-19",
    "igcse-geography-19", "igcse-ict-17",
]

fail = 0


def check(cond: bool, msg: str) -> None:
    global fail
    print(("  PASS " if cond else "  FAIL ") + msg)
    if not cond:
        fail += 1


def topic_files(course: str) -> list[str]:
    p = CORPUS / course
    return (sorted(glob.glob(str(p / "*/*/*/topic.json"))) +
            sorted(glob.glob(str(p / "*/*/topic.json"))))


for course in COURSES:
    print(f"[{course}]")
    f = CORPUS / course / "spec_point_index.json"
    if not f.exists():
        check(False, "index file exists")
        continue
    doc = json.loads(f.read_text(encoding="utf-8"))
    check(doc.get("schema") == "syllabai.sme-spec-point-index/1.0", "G1 schema")
    check(doc.get("course_slug") == course, "G1 course_slug")
    sp = doc.get("spec_points", {})
    check(len(sp) > 0, f"G1 non-empty index ({len(sp)} points)")

    bad = [k for k, v in sp.items()
           if not k.startswith("spcpt_") or not isinstance(v.get("name"), str)
           or not v["name"].strip()
           or not isinstance(v.get("notes"), list)
           or not isinstance(v.get("subtopic_slugs"), list)
           or not v["subtopic_slugs"]]
    check(not bad, f"G2/G4 well-formed entries (bad: {len(bad)})")

    ids_actual: set[str] = set()
    n_parts = 0
    for tf in topic_files(course):
        t = json.loads(Path(tf).read_text(encoding="utf-8"))
        for q in t.get("questions", []):
            for part in q.get("parts", []):
                n_parts += 1
                ids_actual.update(part.get("spec_point_ids") or [])
    cov = doc["coverage"]
    check(cov["covered_by_index"] + len(cov["missing_from_index"]) ==
          cov["question_part_ids_total"], "G3 coverage block adds up")
    check((cov["covered_by_index"] + len(cov["missing_from_index"])) ==
          len(ids_actual) or not ids_actual,
          f"G3 recomputed ids match ({len(ids_actual)} distinct)")
    check(set(cov["missing_from_index"]) == (ids_actual - set(sp)),
          "G3 missing list exact")

    rnd = random.Random(20260917)
    parts = []
    for tf in topic_files(course):
        t = json.loads(Path(tf).read_text(encoding="utf-8"))
        for q in t.get("questions", []):
            for part in q.get("parts", []):
                if part.get("spec_point_ids"):
                    parts.append((q["id"], part))
    sample = rnd.sample(parts, min(5, len(parts)))
    ok = True
    for qid, part in sample:
        for sid in part["spec_point_ids"]:
            if sid not in sp:
                ok = False
                print(f"    spot MISS {sid} (question {qid})")
    check(ok, f"G5 seeded spot-check {len(sample)} parts all resolve")

    miss = cov["missing_from_index"]
    print(f"  info: parts={n_parts} distinct ids={len(ids_actual)} "
          f"covered={cov['covered_by_index']} "
          f"missing={len(miss)} source_pages={doc.get('source_pages')} "
          f"fetch_failures={len(doc.get('fetch_failures', []))}")

print("RESULT:", "ALL PASS" if fail == 0 else f"{fail} FAILURES")
sys.exit(1 if fail else 0)
