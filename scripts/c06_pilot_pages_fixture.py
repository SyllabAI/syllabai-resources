#!/usr/bin/env python3
"""Build student-book-pilot/pages/ — the 5 OCR pilot pages re-wrapped in the
exact c05_book_ocr.py output shape (CMC front matter, status: raw_ocr) so
they serve as a permanent OCR-path fixture for c06_ingest_book.py.

Source bodies: the committed pilot evidence (student-book-pilot/pilot-*.md,
Unlimited-OCR Space output, 2026-09-10). Slot = book page + 9 (1-up pdf),
chapter stamped via the shared chapter map.

Usage: python3 c06_pilot_pages_fixture.py   (idempotent, byte-stable)
"""
import os
import re
import sys
import time

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from c05_book_ocr import chapter_for

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PILOT = os.path.join(ROOT, "student-book-pilot")
OUT = os.path.join(PILOT, "pages")

PILOTS = [  # file stem -> book page
    ("pilot-book-p51-titration-formula-page", 51),
    ("pilot-book-p74-equations-state-symbols", 74),
    ("pilot-book-p75-learning-objectives-ion-charges", 75),
    ("pilot-book-p76-cmc-shaped", 76),
    ("pilot-book-p78-dot-and-cross-lattice", 78),
]


def front_matter(pdf_page: int, book_page: int) -> str:
    unit, ch_no, _, title = chapter_for(book_page)
    return f"""---
source_type: textbook
book_title: "Edexcel International GCSE (9-1) Chemistry Student Book"
authors: "Jim Clark, Steve Owen, Rachel Yu"
publisher: "Pearson Education Limited"
edition_year: 2017
source_file: edexcel-international-gcse-9-1-chemistry-student-book-pdf-free.pdf
pdf_page: {pdf_page}
book_page: {book_page}
unit: {unit}
chapter: {ch_no}
chapter_title: "{title}"
ocr:
  tool: Unlimited-OCR (baidu/Unlimited-OCR)
  mode: document parsing
  dpi: 200
  backend: space (pilot, 2026-09-10)
  date: 2026-09-10
status: raw_ocr
notes: >
  Pilot page from the committed evidence set. Treated as raw OCR: not
  reviewed, lint-owned damage, figure placeholders unresolved.
---
"""


def main():
    os.makedirs(OUT, exist_ok=True)
    for stem, book_page in PILOTS:
        src = os.path.join(PILOT, f"{stem}.md")
        body = open(src, encoding="utf-8").read()
        # drop any pilot-era headline comment lines (keep OCR body only)
        body = re.sub(r"^<!--.*?-->\s*", "", body, flags=re.S)
        slot = book_page + 9
        out_path = os.path.join(OUT, f"page-{slot:03d}.md")
        with open(out_path, "w", encoding="utf-8") as f:
            f.write(front_matter(slot, book_page) + "\n" + body.strip()
                    + "\n")
        print(f"{out_path}  (book p.{book_page}, "
              f"ch {chapter_for(book_page)[1]})")


if __name__ == "__main__":
    main()
