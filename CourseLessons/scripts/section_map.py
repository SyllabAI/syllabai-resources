#!/usr/bin/env python3
"""
section_map.py — L0: build the section spine for a chapter from the parse of
record (chunks_v3). Output feeds `lessonctl.py scaffold` (S0).

CALIBRATED 2026-10-22 against parsed/edexcel_igcse_chemistry_chunks_v3.jsonl
(1,234 chunks) — closes finding f-0001. Confirmed chunk grammar:
  id: "chem_v3_u<unit>_c<chap>_pdf<N>_<M>"
  unit_no / unit_name / chapter_no / chapter_title   (ints/strings; null on front matter)
  section: printed section heading (uppercase); boilerplate set excluded from
           section-boundary detection (HINT, KEY POINT(S), REMINDER, PRACTICAL:*,
           CHEMISTRY ONLY, EXTENSION WORK, LEARNING OBJECTIVES, …)
  content_type: body | key_point | exam_hint | table_data | learning_objectives |
           safety | chapter_questions | … (17-type census, PLAN-4CH1 §2.2)
  book_pages: [start, end] | null      pdf_pages: [start, end]
  text: chunk text

Fetch-first recipe (START-HERE law 1) — NEVER persist the token:
  curl -sL -H "Authorization: token $SYLLABAI_PAT" \
    "https://raw.githubusercontent.com/SyllabAI/syllabai-resources/main/parsed/<parse>.jsonl" \
    -o /tmp/chunks_v3.jsonl

  python3 scripts/section_map.py --parsed /tmp/chunks_v3.jsonl --chapter u1:c01
"""
import argparse, json, sys
from pathlib import Path

BOILER_TOKENS = {"HINT", "KEY", "POINT", "POINTS", "KEYPOINT", "REMINDER",
                 "LEARNING", "OBJECTIVES", "CHEMISTRY", "ONLY", "EXTENSION",
                 "WORK", "DID", "YOU", "KNOW?", "KNOW", "MATHS", "SKILLS",
                 "PRACTICAL", "ACTIVITIES", "CHAPTER", "QUESTIONS"}
BOILER_PREFIXES = ("PRACTICAL:", "PRACTICAL ")
NEW_SECTION_TYPES = {"body", "learning_objectives"}
MINOR_WORDS = {"of", "the", "a", "an", "and", "or", "to", "in", "for", "at",
               "on", "by", "with", "as", "into", "from", "between"}


def smart_title(heading: str) -> str:
    """Strip chapter-opener page furniture ('1 STATES OF MATTER 1' ->
    'States of matter') and title-case with minor words lowercased."""
    words = heading.strip().split()
    while words and (words[0].isdigit() or words[-1].isdigit()):
        words = ([w for w in words[1:] if w] if words[0].isdigit() else words) if words[0].isdigit() else words[:-1]
        if words and not (words[0].isdigit() or words[-1].isdigit()):
            break
    words = [w for w in words if not w.isdigit()]
    if not words:
        return heading.title()
    out = []
    for i, w in enumerate(words):
        lw = w.lower()
        out.append(lw if (lw in MINOR_WORDS and 0 < i < len(words) - 1) else lw.capitalize())
    return " ".join(out)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--chapter", required=True, help="e.g. u1:c01")
    ap.add_argument("--parsed", required=True)
    ap.add_argument("--out")
    args = ap.parse_args()
    unit_s, chap_s = args.chapter.split(":c")
    unit_no, chap_no = int(unit_s[1:]), int(chap_s)

    recs, picked = [], {"schema": "chunks_v3 calibrated 2026-10-22 (f-0001 closed)"}
    with open(args.parsed, encoding="utf-8") as f:
        for line in f:
            r = json.loads(line)
            recs.append(r)
    picked["total_chunks"] = len(recs)
    matched = [r for r in recs
               if r.get("unit_no") == unit_no and r.get("chapter_no") == chap_no]
    if not matched:
        sys.exit(f"no chunks for {args.chapter} (unit_no={unit_no} chapter_no={chap_no})")
    picked["chapter_chunks"] = len(matched)
    picked["chapter_title"] = matched[0].get("chapter_title")

    sections, current = [], None
    for r in matched:
        heading = (r.get("section") or "").strip()
        tokens = {t.strip(".,:;?") for t in heading.upper().split()}
        boiler = (not heading or tokens <= BOILER_TOKENS
                  or any(heading.upper().startswith(p) for p in BOILER_PREFIXES))
        starts_new = (r.get("content_type") in NEW_SECTION_TYPES
                      and not boiler and heading != (current or {}).get("_heading"))
        if starts_new:
            if current:
                sections.append(current)
            pages = r.get("book_pages") or [None, None]
            current = {"id": f"{args.chapter}:s{len(sections)+1:02d}",
                       "title": smart_title(heading), "_heading": heading,
                       "bookPage": pages[0],
                       "chunkRefs": [r["id"]], "specRefs": [], "status": "todo"}
        else:
            if current is None:
                pages = r.get("book_pages") or [None, None]
                current = {"id": f"{args.chapter}:s01", "title": "Introduction",
                           "_heading": None, "bookPage": pages[0],
                           "chunkRefs": [], "specRefs": [], "status": "todo"}
            current["chunkRefs"].append(r["id"])
    if current:
        sections.append(current)
    for s in sections:
        s.pop("_heading", None)   # internal; bookPage stays (lesson.yaml needs it)
    out = {"chapter_key": args.chapter, "key_mapping": picked,
           "book_page_range": [min(s["bookPage"] for s in sections if s["bookPage"]),
                               max(s["bookPage"] for s in sections if s["bookPage"])],
           "sections": sections}
    text = json.dumps(out, indent=2, ensure_ascii=False)
    if args.out:
        Path(args.out).write_text(text, encoding="utf-8")
        print(f"wrote {args.out} — {len(sections)} sections, pages {out['book_page_range']}")
    else:
        print(text)


if __name__ == "__main__":
    main()
