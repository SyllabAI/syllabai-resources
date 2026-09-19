#!/usr/bin/env python3
"""T-SME-11: add the 10 new course entries to SME-ExamQuestion/manifest.json
(registry), reading scrape totals from the per-course manifests. Idempotent.
"""
from __future__ import annotations

import json
import time
from pathlib import Path

CORPUS = Path("/home/z/my-project/download/syllabai-resources/SME-ExamQuestion")

NEW = {
    "igcse-english-language-a-16-paper-1-non-fiction-texts-and-transactional-writing": {
        "level": "igcse", "subject": "english-language",
        "mid": "a/16/paper-1-non-fiction-texts-and-transactional-writing",
        "path": "igcse/english-language/edexcel/a/16/paper-1-non-fiction-texts-and-transactional-writing"},
    "igcse-english-language-a-16-paper-2-poetry-and-prose-texts-and-imaginative-writing": {
        "level": "igcse", "subject": "english-language",
        "mid": "a/16/paper-2-poetry-and-prose-texts-and-imaginative-writing",
        "path": "igcse/english-language/edexcel/a/16/paper-2-poetry-and-prose-texts-and-imaginative-writing"},
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


def main() -> int:
    reg_path = CORPUS / "manifest.json"
    reg = json.loads(reg_path.read_text())
    have = {c["slug"] for c in reg["courses"]}
    added = 0
    for slug, m in NEW.items():
        if slug in have:
            print(f"[skip] {slug}")
            continue
        mf = CORPUS / slug / "manifest.json"
        man = json.loads(mf.read_text())
        idx_path = CORPUS / slug / "spec_point_index.json"
        entry = {
            "slug": slug, "level": m["level"], "subject": m["subject"],
            "mid": m["mid"],
            "landing_url": f"https://www.savemyexams.com/{m['path']}/topic-questions/",
            "page_count": man["course"]["leaf_types"].get("exam-questions", 0)
            or sum(len(t.get("sets_completed") or []) for t in man.get("topics", [])),
            "leaf_types": man["course"].get("leaf_types") or {},
            "sections": len({t["section_slug"] for t in man.get("topics", [])}),
            "status": ("scraped" if man.get("topics")
                       else "no_topic_questions_on_sme"),
            "totals": man["totals"],
        }
        if idx_path.exists():
            idx = json.loads(idx_path.read_text())
            cov = idx["coverage"]
            entry["spec_index"] = {
                "schema": idx["schema"],
                "source_pages": idx.get("source_pages"),
                "spec_points": len(idx["spec_points"]),
                "part_ids": cov["question_part_ids_total"],
                "covered": cov["covered_by_index"],
                "missing": len(cov["missing_from_index"]),
            }
        if man.get("status_note"):
            entry["status_note"] = man["status_note"]
        reg["courses"].append(entry)
        added += 1
        print(f"[added] {slug} status={entry['status']}")
    reg["courses"].sort(key=lambda c: c["slug"])
    reg["generated_utc"] = time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime())
    reg["course_count"] = len(reg["courses"])
    reg["scraped_courses"] = sum(1 for c in reg["courses"]
                                 if c.get("status") == "scraped")
    reg["spec_index_courses"] = sum(1 for c in reg["courses"]
                                    if c.get("spec_index"))
    reg_path.write_text(json.dumps(reg, indent=1, ensure_ascii=False),
                        encoding="utf-8")
    print(f"registry: {reg['course_count']} courses "
          f"({reg['scraped_courses']} scraped, "
          f"{reg['spec_index_courses']} with spec index)")
    return 0


if __name__ == "__main__":
    import sys
    sys.exit(main())
