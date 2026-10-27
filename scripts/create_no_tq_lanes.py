#!/usr/bin/env python3
"""T-SME-11: create the 8 lane folders for courses where SME publishes NO
topic questions (ELA paper-3, maths-b, SDA (Modular) x6). Each lane gets a
v1.1 manifest with zero totals and an explicit status_note — honest gap,
never synthesized. The spec-point harvest then writes its notes-only
spec_point_index.json alongside.
"""
from __future__ import annotations

import json
import time
from pathlib import Path

OUT = Path("/home/z/my-project/download/syllabai-resources/SME-ExamQuestion")
LICENSE = ("operator-authorized; see repo LICENSE-DATA.md (SME attestation "
           "2026-09-17)")

LANES = {
    "igcse-english-language-a-16-paper-3-coursework": {
        "level": "igcse", "subject": "english-language",
        "mid": "a/16/paper-3-coursework",
        "path": "igcse/english-language/edexcel/a/16/paper-3-coursework"},
    "igcse-maths-b-16": {
        "level": "igcse", "subject": "maths", "mid": "b/16",
        "path": "igcse/maths/edexcel/b/16"},
    "igcse-science-double-award-modular-24-biology-unit-1": {
        "level": "igcse", "subject": "science",
        "mid": "double-award-modular/24/biology-unit-1",
        "path": "igcse/science/edexcel/double-award-modular/24/biology-unit-1"},
    "igcse-science-double-award-modular-24-biology-unit-2": {
        "level": "igcse", "subject": "science",
        "mid": "double-award-modular/24/biology-unit-2",
        "path": "igcse/science/edexcel/double-award-modular/24/biology-unit-2"},
    "igcse-science-double-award-modular-24-chemistry-unit-1": {
        "level": "igcse", "subject": "science",
        "mid": "double-award-modular/24/chemistry-unit-1",
        "path": "igcse/science/edexcel/double-award-modular/24/chemistry-unit-1"},
    "igcse-science-double-award-modular-24-chemistry-unit-2": {
        "level": "igcse", "subject": "science",
        "mid": "double-award-modular/24/chemistry-unit-2",
        "path": "igcse/science/edexcel/double-award-modular/24/chemistry-unit-2"},
    "igcse-science-double-award-modular-24-physics-unit-1": {
        "level": "igcse", "subject": "science",
        "mid": "double-award-modular/24/physics-unit-1",
        "path": "igcse/science/edexcel/double-award-modular/24/physics-unit-1"},
    "igcse-science-double-award-modular-24-physics-unit-2": {
        "level": "igcse", "subject": "science",
        "mid": "double-award-modular/24/physics-unit-2",
        "path": "igcse/science/edexcel/double-award-modular/24/physics-unit-2"},
}

NOTE = ("no topic questions published on SME for this course "
        "(topic-questions page carries zero published question sets; "
        "census 2026-09-19). Lane kept for its notes/flashcard resources "
        "and spec-point index; no questions synthesized.")


def main() -> int:
    now = time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime())
    for slug, m in LANES.items():
        lane = OUT / slug
        mf = lane / "manifest.json"
        if mf.exists():
            print(f"[skip] {slug}")
            continue
        lane.mkdir(parents=True, exist_ok=True)
        doc = {
            "schema": "syllabai.sme-exam-questions/1.1",
            "course_slug": slug,
            "generated_utc": now,
            "source": {"provider": "Save My Exams",
                       "landing_url": f"https://www.savemyexams.com/{m['path']}/topic-questions/",
                       "registry": "scripts/sme_examq_courses.py",
                       "license": LICENSE},
            "course": {"slug": slug, "level": m["level"],
                       "subject": m["subject"], "mid": m["mid"],
                       "leaf_types": {}},
            "totals": {"topics": 0, "questions": 0, "parts": 0, "marks": 0,
                       "assets": 0, "asset_failures": 0,
                       "missing_questions": 0, "equations": 0},
            "topics": [],
            "status_note": NOTE,
        }
        mf.write_text(json.dumps(doc, indent=1, ensure_ascii=False),
                      encoding="utf-8")
        print(f"[created] {slug}")
    return 0


if __name__ == "__main__":
    import sys
    sys.exit(main())
