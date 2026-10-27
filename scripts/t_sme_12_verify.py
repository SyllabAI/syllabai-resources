#!/usr/bin/env python3
"""
T-SME-12 — live re-verification of the 8 honest no_topic_questions_on_sme
lanes against the current SME frontend (run 2026-09-20; results captured in
scripts/t_sme_12_verification_results.json).

For each lane: GET the topic-questions page, parse __NEXT_DATA__, aggregate
per-topic published-question attributes + syllabus-version flags. maths-b's
family-level past-papers page is counted to document SME's only exam material
for that course (Pearson-hosted PDFs). Re-run anytime to refresh evidence.
"""
from __future__ import annotations

import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
import sme_examq_scrape as eq  # noqa: E402

BASE = "https://www.savemyexams.com"
LANES = {
    "igcse-maths-b-16": "igcse/maths/edexcel/b/16",
    "igcse-science-double-award-modular-24-biology-unit-1": "igcse/science/edexcel/double-award-modular/24/biology-unit-1",
    "igcse-science-double-award-modular-24-biology-unit-2": "igcse/science/edexcel/double-award-modular/24/biology-unit-2",
    "igcse-science-double-award-modular-24-chemistry-unit-1": "igcse/science/edexcel/double-award-modular/24/chemistry-unit-1",
    "igcse-science-double-award-modular-24-chemistry-unit-2": "igcse/science/edexcel/double-award-modular/24/chemistry-unit-2",
    "igcse-science-double-award-modular-24-physics-unit-1": "igcse/science/edexcel/double-award-modular/24/physics-unit-1",
    "igcse-science-double-award-modular-24-physics-unit-2": "igcse/science/edexcel/double-award-modular/24/physics-unit-2",
}
ELA_P3 = "igcse/english-language/edexcel/a/16/paper-3-coursework"


def lane_record(path: str) -> dict:
    d = eq.parse_next_data(eq.http_get(f"{BASE}/{path}/topic-questions/"))
    topics = d.get("topics") or []
    sv = (d.get("syllabusVersions") or [{}])[0].get("attributes", {})
    rels = sum(
        len(((t.get("relationships") or {}).get("question_sets") or {}).get("data") or [])
        for t in topics
    )
    return {
        "topics": len(topics),
        "topics_with_questions": sum(1 for t in topics if t["attributes"].get("has_published_questions")),
        "published_questions_total": sum(t["attributes"].get("published_questions_count") or 0 for t in topics),
        "published_question_parts_total": sum(t["attributes"].get("published_question_parts_count") or 0 for t in topics),
        "question_set_relationships_total": rels,
        "syllabus_version": sv.get("name"),
        "has_published_topic_questions": sv.get("has_published_topic_questions"),
        "has_published_teacher_only_questions": sv.get("has_published_teacher_only_questions"),
        "has_published_mock_exam_papers": sv.get("has_published_mock_exam_papers"),
        "study_tool_links": [l.get("title") for l in ((d.get("studyToolLinks") or {}).get("links") or [])],
    }


def main() -> int:
    out: dict = {"verified_utc": "2026-09-20", "lanes": {}}
    ok = True
    for slug, path in LANES.items():
        rec = lane_record(path)
        out["lanes"][slug] = rec
        empty = (rec["topics_with_questions"] == 0 and rec["published_questions_total"] == 0
                 and rec["has_published_topic_questions"] is False)
        ok &= empty
        print(f"{slug}: topics={rec['topics']} with_q={rec['topics_with_questions']} "
              f"q_total={rec['published_questions_total']} sv_tq={rec['has_published_topic_questions']} "
              f"{'EMPTY-CONFIRMED' if empty else 'HAS QUESTIONS — corpus update needed'}")

    # ELA p3 module flag
    d3 = eq.parse_next_data(eq.http_get(f"{BASE}/{ELA_P3}/topic-questions/"))
    cm = (d3.get("courseModule") or {}).get("attributes", {})
    p3 = {
        "course_module": cm.get("name"),
        "has_published_topic_questions": cm.get("has_published_topic_questions"),
        "pageType": d3.get("pageType"),
        "note": "question-set payload on this URL is the sibling paper-1 session-set listing",
    }
    out["lanes"]["igcse-english-language-a-16-paper-3-coursework"] = p3
    ok &= p3["has_published_topic_questions"] is False
    print(f"ela-p3: module={p3['course_module']} sv_tq={p3['has_published_topic_questions']} "
          f"{'EMPTY-CONFIRMED' if p3['has_published_topic_questions'] is False else 'HAS QUESTIONS'}")

    # maths-b past papers (family-level URL)
    dp = eq.parse_next_data(eq.http_get(f"{BASE}/igcse/maths/edexcel/b/past-papers/"))
    pp = dp.get("pastPapers") or []
    out["lanes"]["igcse-maths-b-16"]["past_papers_entries"] = len(pp)
    print(f"maths-b past-paper entries (Pearson PDF links): {len(pp)}")

    print("RESULT:", "ALL 8 LANES CONFIRMED EMPTY ON SME" if ok else "MISMATCH — re-check")
    report = Path(__file__).with_name("t_sme_12_verification_results.json")
    if "--write" in sys.argv:
        report.write_text(json.dumps(out, indent=1) + "\n")
        print("wrote", report.name)
    return 0 if ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
