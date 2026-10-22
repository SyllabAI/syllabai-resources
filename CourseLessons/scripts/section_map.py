#!/usr/bin/env python3
"""
section_map.py — L0: build the section spine for a chapter from the parse of
record (chunks_v3). Output feeds `lessonctl.py scaffold` (S0).

Fetch-first recipe (START-HERE law 1):
  1) If the parse already exists locally, point CL_PARSED at it:
       CL_PARSED=parsed/edexcel_igcse_chemistry_chunks_v3.jsonl
  2) Else fetch ONE-SHOT with an inline credentialed URL and scrub:
       curl -sH "Authorization: token $SYLLABAI_PAT" \
         "https://raw.githubusercontent.com/SyllabAI/syllabai-resources/main/parsed/edexcel_igcse_chemistry_chunks_v3.jsonl" \
         -o /tmp/chunks_v3.jsonl && rm -f /tmp/chunks_v3.jsonl   # NEVER persist
     (5.3GB repo — do NOT clone; fetch the single file or use the trees API.)

Schema note of record: the chunk field grammar is calibrated at FIRST RUN —
this tool auto-detects the id/chapter/page/type/text keys (candidates listed
below) and prints the mapping it found. If detection fails, file a finding
(type: process) with the observed keys; do not hand-edit output blindly.

  python3 scripts/section_map.py --chapter u1:c01 [--out /tmp/spine-u1-c01.json]
"""
import argparse, json, os, re, sys
from pathlib import Path

KEY_CANDIDATES = {
    "id": ["id", "chunk_id", "chunkId"],
    "chapter": ["chapter_key", "chapterKey", "chapter", "chapter_slug"],
    "page": ["page", "book_page", "bookPage", "page_number", "pageNum"],
    "type": ["type", "content_type", "contentType", "chunk_type"],
    "text": ["text", "content", "body", "markdown"],
}
SECTIONIZERS = ["learning_objectives", "body", "key_point"]  # body chunks start new sections


def pick(rec: dict, field: str):
    for k in KEY_CANDIDATES[field]:
        if k in rec:
            return rec[k]
    return None


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--chapter", required=True, help="e.g. u1:c01")
    ap.add_argument("--parsed", default=os.environ.get("CL_PARSED"))
    ap.add_argument("--out")
    args = ap.parse_args()
    if not args.parsed or not Path(args.parsed).exists():
        sys.exit("parse of record not found — see the fetch-first recipe in this file's docstring")
    unit, chap = args.chapter.split(":c")
    unit_no = int(unit[1:])
    sections, current = [], None
    mapping = {}
    with open(args.parsed, encoding="utf-8") as f:
        for line in f:
            rec = json.loads(line)
            ch = pick(rec, "chapter")
            if not mapping and ch:
                mapping = {k: pick(rec, k) for k in KEY_CANDIDATES}
            if ch is None or chap not in str(ch):
                continue
            rtype = pick(rec, "type") or "body"
            page = pick(rec, "page")
            if rtype in SECTIONIZERS and rtype != "key_point" and current:
                sections.append(current)
                current = None
            if current is None:
                current = {"id": f"{args.chapter}:s{len(sections)+1:02d}",
                           "title": None, "bookPage": page,
                           "chunkRefs": [], "specRefs": [], "status": "todo"}
            current["chunkRefs"].append(pick(rec, "id"))
    if current:
        sections.append(current)
    out = {"chapter_key": args.chapter, "source": str(args.parsed),
           "key_mapping": mapping, "sections": sections}
    text = json.dumps(out, indent=2, ensure_ascii=False)
    if args.out:
        Path(args.out).write_text(text, encoding="utf-8")
        print(f"wrote {args.out} ({len(sections)} sections)")
    else:
        print(text)


if __name__ == "__main__":
    main()
