#!/usr/bin/env python3
"""T-SME-CAMBRIDGE — append the Cambridge course entries to the
SME-ExamQuestion registry (manifest.json) + extend the README.

Additive only: existing Edexcel entries are never rewritten; Cambridge
entries are appended (or refreshed in place on re-run). spec_index is
omitted for Cambridge lanes until the spcpt harvest lane covers them —
recorded honestly, never fabricated.
"""
from __future__ import annotations

import json
import sys
import time
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
import sme_cambridge_courses as cc  # noqa: E402

BASE = "https://www.savemyexams.com"
REPO = Path("/home/z/my-project/download/syllabai-resources")
CORPUS = REPO / "SME-ExamQuestion"


def course_entry(course: dict) -> dict:
    slug = course["slug"]
    mf_path = CORPUS / slug / "manifest.json"
    if not mf_path.exists():
        raise SystemExit(f"{slug}: no course manifest — run the scrape first")
    m = json.loads(mf_path.read_text(encoding="utf-8"))
    lt = m.get("course", {}).get("leaf_types") or {}
    topics = m.get("topics") or []
    sections = len({t.get("section_slug") for t in topics if t.get("section_slug")})
    entry = {
        "slug": slug,
        "level": course["level"],
        "subject": course["subject"],
        "mid": course["mid"],
        "landing_url": f"{BASE}/{course['sme_path']}/topic-questions/",
        "page_count": sum(lt.values()),
        "leaf_types": lt,
        "sections": sections,
        "status": m.get("status", "scraped"),
        "totals": {k: (m.get("totals") or {}).get(k, 0) for k in
                   ("topics", "questions", "parts", "marks", "assets",
                    "asset_failures", "missing_questions", "equations")},
    }
    return entry


def main() -> int:
    reg = json.loads((CORPUS / "manifest.json").read_text(encoding="utf-8"))
    existing = {c["slug"]: i for i, c in enumerate(reg["courses"])}
    added, updated = 0, 0
    for course in cc.courses():
        e = course_entry(course)
        if e["slug"] in existing:
            reg["courses"][existing[e["slug"]]] = e
            updated += 1
        else:
            reg["courses"].append(e)
            added += 1
    reg["generated_utc"] = time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime())
    reg["course_count"] = len(reg["courses"])
    reg["scraped_courses"] = sum(1 for c in reg["courses"]
                                 if c.get("status") == "scraped")
    reg["spec_index_courses"] = sum(1 for c in reg["courses"]
                                    if "spec_index" in c)
    reg["source"]["cambridge_extension"] = {
        "date": "2026-10-17",
        "directive": "operator trace 1a1472e1880cc011 — 'similarly download "
                     "Cambridge ones as well. Push it in the repo'",
        "registry_builder": "scripts/sme_cambridge_courses.py",
        "scraper": "scripts/sme_cambridge_examq_scrape.py",
        "lanes": 34,
    }
    (CORPUS / "manifest.json").write_text(
        json.dumps(reg, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")

    # README: extend header + append the Cambridge section
    readme = CORPUS / "README.md"
    txt = readme.read_text(encoding="utf-8")
    txt = txt.replace(
        "# SME Exam Questions — multi-course corpus (Edexcel)",
        "# SME Exam Questions — multi-course corpus (Edexcel + Cambridge/CAIE)",
        1)
    cam_block = ["", "## Cambridge (CAIE) extension — T-SME-CAMBRIDGE "
                 "(2026-10-17)", "",
                 "Added by operator directive (trace 1a1472e1880cc011): the "
                 "attested SME corpora extended to the Cambridge lanes on "
                 "savemyexams.com — 8 `a-level/cie` full-course lanes (AS+A2), "
                 "2 `as/cie` lanes where a-level has no counterpart, 24 "
                 "`igcse/cie` lanes; O Level out of scope (no Edexcel "
                 "equivalent). Scraper: `scripts/sme_cambridge_examq_scrape.py` "
                 "(compiled set-page model, corpus schema 1.1, curriculum "
                 "page-sourced). Same authorization — LICENSE-DATA.md SME "
                 "attestation. spcpt/spec-index harvest not yet run for these "
                 "lanes (no `spec_index` blocks yet — honestly absent).", "",
                 "| course | status | topics | questions | assets |",
                 "|---|---|---|---|---|"]
    for course in cc.courses():
        e = course_entry(course)
        t = e["totals"]
        cam_block.append(f"| {e['slug']} | {e['status']} | {t['topics']} | "
                         f"{t['questions']} | {t['assets']} |")
    if "## Cambridge (CAIE) extension" not in txt:
        txt = txt.rstrip("\n") + "\n" + "\n".join(cam_block) + "\n"
    readme.write_text(txt, encoding="utf-8")
    print(f"registry: +{added} appended, {updated} refreshed; "
          f"courses={reg['course_count']} scraped={reg['scraped_courses']}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
