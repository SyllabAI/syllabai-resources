#!/usr/bin/env python3
"""Mine page-level structure markers from YCH12 SB2 docling pages (phase 3 probe).

Prints one line per pdf page: the TOPIC banner, chapter-banner candidates
(\\d{1,2}[A-E] + CAPS title), and marker-family hits (LEARNING OBJECTIVES,
EXAM PRACTICE, THINKING BIGGER, MATHS SKILLS FOR THIS TOPIC, CHECKPOINT...).
Output feeds the book_structure_ych12.py map (chapters / dividers / TB / EP).
"""
import json, re, glob, sys

PAGES = "/home/z/my-project/data/ych12_sb2/docling_pages"

TOPIC_PAT = re.compile(r"TOPIC\s*(1[1-9]|20)\b\s*([A-Z][A-Z &,\-()']*)?")
CHAP_PAT = re.compile(r"^\s*(1[1-9]|20)\s*([A-E])\s*[.:—-]?\s*([A-Z][A-Za-z0-9 &,'()\-]{3,60})\s*$")
BANNER_PAT = re.compile(r"^\s*([A-E])\s+([A-Z][A-Z &,\-()']{3,60})\s*$")  # "A FURTHER KINETICS" banner form
MARKERS = {
    "LO": re.compile(r"LEARNING\s*\.?\s*OBJECTIVES|LEARNINGOBJECTIVES", re.I),
    "EP": re.compile(r"EXAM\s*PRACTICE", re.I),
    "TB": re.compile(r"THINKING\s*BIGGER", re.I),
    "MS": re.compile(r"MATHS\s*SKILLS\s*FOR\s*THIS\s*TOPIC", re.I),
    "CP": re.compile(r"CHECKPOINT", re.I),
    "WK": re.compile(r"WORKED\s*EXAMPLE", re.I),
}

def page_text(rec):
    out = []
    for it in rec["items"]:
        t = (it.get("text") or "").strip()
        if t:
            out.append((it.get("label") or "", t))
    return out

def main():
    lo_page = {}
    for f in sorted(glob.glob(f"{PAGES}/page_*.json")):
        rec = json.load(open(f))
        pdf = rec["pdf_page"]
        items = page_text(rec)
        flags = set()
        topic = None
        chap = None
        banner = None
        for label, t in items:
            joined = t.replace("\n", " ")
            m = TOPIC_PAT.search(joined.upper())
            if m and len(joined) < 80:
                topic = (m.group(1), m.group(2).strip() if m.group(2) else "")
            m2 = CHAP_PAT.match(joined)
            if m2:
                chap = (m2.group(1) + m2.group(2), m2.group(3)[:45])
            m3 = BANNER_PAT.match(joined)
            if m3 and m3.group(1) in ("A", "B", "C", "D", "E") and label in ("section_header", "title", "chapter_header", "subtitle", "heading"):
                banner = (m3.group(1), m3.group(2)[:45])
            for k, pat in MARKERS.items():
                if pat.search(joined):
                    flags.add(k)
                    if k == "LO" and pdf >= 14:
                        lo_page.setdefault(pdf, True)
        if topic or chap or banner or flags:
            print(f"pdf{pdf:03d} book{pdf-12:03d} | topic={topic} chap={chap} banner={banner} | {' '.join(sorted(flags))}")

if __name__ == "__main__":
    main()
