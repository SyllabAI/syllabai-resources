#!/usr/bin/env python3
"""T-SME-CAMBRIDGE — Cambridge (CAIE) extension of the SME corpora.

Operator directive 2026-10-17 (zai-web, gateway trace 1a1472e1880cc011):
"similarly download Cambridge ones as well. Push it in the repo" — i.e.
extend the attested SME corpora (SME-RevisionNotes / SME-ExamQuestion /
SME-Flashcards) with the Cambridge International lanes on savemyexams.com,
mirroring the Edexcel IAL + IGCSE coverage. Authorization: LICENSE-DATA.md
"Amendment 2026-09-17 — Save My Exams authorization (operator attestation)"
(SME Ltd is the rights holder); acquisition channel = SME's own public
site/sitemaps ONLY (no aggregators, no Pearson DAM, no access-control
circumvention — the Task-7 closure basis is untouched).

Scope (44 lanes), from the sitemap census 2026-10-17
(.cache/sme_cambridge_sitemap_census.json):
- a-level/cie: 12 lanes — SME's Cambridge A Level trees carry the FULL
  A Level (AS + A2; verified: a-level/chemistry/cie/25 has 38 note sections
  = AS 1-22 + A2 23-37), so they mirror the Edexcel full-course IAL lanes.
  a-level maths 20 splits into 5 unit lanes (pure-1/pure-3/mechanics/PS1/
  PS2) exactly mirroring the Edexcel ial-maths-20 unit lanes.
- as/cie: 2 lanes ONLY where a-level has no counterpart (english general
  paper, environmental management) — the other AS trees are subset views of
  the a-level lanes and would duplicate content.
- igcse/cie: 30 lanes, incl. syllabus-version and tier/strand variants that
  mirror the Edexcel lane model: maths 25 core/extended, international
  maths 23 core/extended, additional maths 25, co-ordinated (double award)
  23 biology/chemistry/physics, combined science 23 biology/chemistry/
  physics (the Edexcel science-double-award-17-{science} pattern).
- o-level/cie: 15 courses EXCLUDED — no O Level equivalent exists in the
  Edexcel corpus (IAL + IGCSE only); recorded here so the scope decision is
  visible and reversible by a later directive.

URL shape note (the sitemap census caught this): 7 courses carry an EXTRA
path segment between the course id and the resource trees
(e.g. .../cie/combined-science/23/biology/revision-notes/...) — the
variant lanes below carry the FULL sme_path so all three scrapers work
unchanged. mid is therefore everything after the board segment (mechanical
"20/pure-1", "23/biology", "general-paper/21"), and slugs are mechanical:
cie-{a-level|as|igcse}-{subject}-{mid-with-/-as--}.
"""
from __future__ import annotations

import json
import sys
from pathlib import Path

CACHE = Path("/home/z/my-project/.cache")
CENSUS = CACHE / "sme_cambridge_sitemap_census.json"

# (level, subject, mid) per lane; mid may span variant segments.
A_LEVEL = [("accounting", "21"), ("biology", "25"), ("business", "23"),
           ("chemistry", "25"), ("computer-science", "19"),
           ("economics", "23"),
           ("maths", "20/mechanics"), ("maths", "20/pure-1"),
           ("maths", "20/pure-3"),
           ("maths", "20/probability-and-statistics-1"),
           ("maths", "20/probability-and-statistics-2"),
           ("physics", "25")]
AS_ONLY = [("english", "general-paper/21"),
           ("environmental-management", "20")]
IGCSE = [("accounting", "21"), ("accounting", "25"), ("biology", "23"),
         ("business", "23"), ("business", "25"), ("chemistry", "23"),
         ("computer-science", "23"), ("economics", "20"),
         ("economics", "25"), ("english-language", "20"),
         ("english-language", "25"), ("english-literature", "21"),
         ("environmental-management", "25"),
         ("further-maths", "additional-maths/25"),
         ("geography", "20"), ("geography", "25"), ("history", "18"),
         ("ict", "21"),
         ("maths", "25/core"), ("maths", "25/extended"),
         ("maths", "international-maths/23/core"),
         ("maths", "international-maths/23/extended"),
         ("physics", "23"), ("religious-studies", "23"),
         ("science", "co-ordinated-sciences-double-award/23/biology"),
         ("science", "co-ordinated-sciences-double-award/23/chemistry"),
         ("science", "co-ordinated-sciences-double-award/23/physics"),
         ("science", "combined-science/23/biology"),
         ("science", "combined-science/23/chemistry"),
         ("science", "combined-science/23/physics")]

LEVELS = (("a-level", A_LEVEL), ("as", AS_ONLY), ("igcse", IGCSE))
PREFIX = {"a-level": "cie-a-level", "as": "cie-as", "igcse": "cie-igcse"}


def course_slug(level: str, subject: str, mid: str) -> str:
    return f"{PREFIX[level]}-{subject}-{mid.replace('/', '-')}"


def courses() -> list[dict]:
    """The 44 lanes with URL census counts attached (variant-aware)."""
    census = json.loads(CENSUS.read_text(encoding="utf-8"))
    urls = census["cambridge_urls"]
    out = []
    for level, items in LEVELS:
        for subject, mid in items:
            sme_path = f"{level}/{subject}/cie/{mid}"
            base = f"https://www.savemyexams.com/{sme_path}"
            census_v = {
                "revision_notes": sum(1 for u in urls if u.startswith(base)
                                      and "/revision-notes/" in u),
                "topic_questions": sum(1 for u in urls if u.startswith(base)
                                       and "/topic-questions/" in u),
                "flashcards": sum(1 for u in urls if u.startswith(base)
                                  and "/flashcards/" in u),
            }
            out.append({
                "slug": course_slug(level, subject, mid),
                "level": level, "subject": subject, "mid": mid,
                "sme_path": sme_path,
                "notes_base": f"{base}/revision-notes/",
                "census": census_v,
            })
    return out


def build_notes_cache() -> Path:
    """Write the discover cache in sme_notes_discover.py's format, scoped to
    the Cambridge lanes, so scripts/sme_notes_scrape.py runs unmodified.

    Leaf selection inside the scraper: URLs starting with notes_base whose
    remainder has >= 2 segments — note leaves are
    /revision-notes/{section}/{topic}/{leaf}/ (depth 3), so depth-1/2
    landing URLs are excluded exactly as for Edexcel.
    """
    census = json.loads(CENSUS.read_text(encoding="utf-8"))
    notes_urls = [u for u in census["cambridge_urls"]
                  if "/revision-notes/" in u and "/cie/" in u]
    courses_out = {}
    for c in courses():
        base = c["notes_base"]
        direct = [u for u in notes_urls if u.startswith(base)]
        courses_out[c["slug"]] = {
            "notes_base": base,
            "direct_pages": len(direct),
            "alt_variant_prefixes": [c["mid"]],
            "kind": ("single-segment" if "/" not in c["mid"]
                     else "extra-segment"),
        }
    out = CACHE / "sme_notes_urls.json"
    out.write_text(json.dumps({
        "notes_urls_total": len(notes_urls),
        "notes_urls": sorted(notes_urls),
        "courses": courses_out,
    }, indent=1), encoding="utf-8")
    print(f"notes cache: {out} "
          f"({len(notes_urls)} urls, {len(courses_out)} courses)")
    return out


def flashcards_registry_entries() -> dict:
    """Cambridge entries for sme_flashcards_scrape.py REGISTRY."""
    entries = {}
    for c in courses():
        fc = c["census"]["flashcards"]
        if fc > 0:
            entries[c["slug"]] = {"path": c["sme_path"],
                                  "expected_decks": fc - 1}
        else:
            entries[c["slug"]] = {
                "status": "missing_on_sme",
                "reason": "no flashcard decks on SME "
                          "(Cambridge census 2026-10-17)"}
    return entries


if __name__ == "__main__":
    if "--notes-cache" in sys.argv:
        build_notes_cache()
    elif "--fc-registry" in sys.argv:
        print(json.dumps(flashcards_registry_entries(), indent=1))
    else:
        n = t = f = 0
        for c in courses():
            v = c["census"]
            d = max(0, v["flashcards"] - 1) if v["flashcards"] else 0
            n += v["revision_notes"]
            t += v["topic_questions"]
            f += d
            print(f"{c['slug']:64s} notes={v['revision_notes']:4d} "
                  f"tq={v['topic_questions']:4d} decks={d:4d}")
        print(f"total lanes: {len(courses())} | notes pages {n} "
              f"| tq leaf pages {t} | decks {f}")
