#!/usr/bin/env python3
"""T-C05 companion: extract the PUBLISHER-EMBEDDED TEXT LAYER of the 2-up
Student Book PDF (`edexcel-chemistry-igcse-book.pdf`, 192 spread pages) into
the SAME CMC-shaped per-page layout as c05_book_ocr.py output, so the two
substrates join page-for-page (identical page keys = 1-up pdf page numbers).

Verified linear mapping (probed at 2-up pdf 10/20/60/100/150/191/192 on
2026-10-24):
  2-up pdf page N, LEFT  half = 1-up pdf slot 2N-1 = book page 2N-10
  2-up pdf page N, RIGHT half = 1-up pdf slot 2N   = book page 2N-9
  book_page = 1-up pdf page - 9 (same OFFSET as the 1-up scan)
  slots 1..9 (2-up pdf 1L..5L) are front matter (book_page <= 0)

Output (CMC v1.0 aligned, status: text_layer):
  student-book-textlayer/manifest.json   slot -> {book_page, chapter, status, sha}
  student-book-textlayer/pages/page-NNN.md   front matter + raw text-layer body

Provenance honesty: this is the publisher's own embedded OCR layer. It is
FAST and FULL-COVERAGE but noisier than Unlimited-OCR (figure-caption
ghosting, occasional glyph garbage like `PIHi&`, `httpsJ/`). Status is
`text_layer` everywhere so the ingest lint can treat it as UNREVIEWED and
the later Unlimited-OCR run (Path A/B, GPU-hosted) supersedes it per page.

Usage:
  python3 c05_book_textlayer.py                 # full book
  python3 c05_book_textlayer.py --range 39-40   # 1-up slot range subset
"""
import argparse
import hashlib
import json
import os
import subprocess
import sys
import time

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from c05_book_ocr import CHAPTERS, chapter_for, PDF_DEFAULT, OFFSET_DEFAULT

PDF_2UP_DEFAULT = "edexcel-chemistry-igcse-book.pdf"
OUT_DEFAULT = "student-book-textlayer"
PAGE_W, PAGE_H = 841.68, 525.6     # 2-up spread size in pt (pdfinfo)
MID = PAGE_W / 2                   # gutter

FRONT_SLOTS = 9                    # slots 1..9 = front matter (book_page <= 0)


def half_text(pdf: str, page: int, left: bool) -> str:
    x, w = (0, int(MID) + 1) if left else (int(MID) + 1, int(MID) + 1)
    r = subprocess.run(
        ["pdftotext", "-f", str(page), "-l", str(page),
         "-x", str(x), "-y", "0", "-W", str(w), "-H", str(int(PAGE_H) + 2),
         pdf, "-"],
        capture_output=True, text=True, check=True)
    return r.stdout.strip()


def front_matter(slot: int, book_page: int, backend_note: str) -> str:
    if book_page < 1:
        unit, ch_no, _, title = "front", 0, 0, "Front matter"
    else:
        unit, ch_no, _, title = chapter_for(book_page)
    return f"""---
source_type: textbook
book_title: "Edexcel International GCSE (9-1) Chemistry Student Book"
authors: "Jim Clark, Steve Owen, Rachel Yu"
publisher: "Pearson Education Limited"
edition_year: 2017
source_file: {PDF_2UP_DEFAULT}
pdf_page: {slot}
book_page: {book_page if book_page >= 1 else 'null'}
unit: {unit}
chapter: {ch_no}
chapter_title: "{title}"
ocr:
  tool: pdftotext (poppler) over the publisher-embedded text layer
  mode: 2-up spread split (left/right crop boxes)
  backend: {backend_note}
  date: {time.strftime("%Y-%m-%d")}
status: text_layer
notes: >
  Publisher-embedded OCR layer, NOT reviewed or validated. Noisier than the
  Unlimited-OCR substrate: figure-caption ghosting, glyph garbage in image
  regions, no LaTeX (unicode sub/superscripts only), no figure placeholders.
  Tables arrive as plain text lines. This page is a STOPGAP substrate for
  retrieval/joining; the Unlimited-OCR run (c05_book_ocr.py, GPU host)
  supersedes it per page when it lands. No hand-fixing — the ingestion lint
  owns damage flagging with page provenance intact.
---
"""


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--pdf", default=PDF_2UP_DEFAULT)
    ap.add_argument("--out", default=OUT_DEFAULT)
    ap.add_argument("--range", dest="slot_range", default="1-383",
                    help="1-up slot range (= pdf page), e.g. 39-40")
    args = ap.parse_args()

    lo, hi = (int(x) for x in args.slot_range.split("-"))
    md_dir = os.path.join(args.out, "pages")
    os.makedirs(md_dir, exist_ok=True)

    manifest_path = os.path.join(args.out, "manifest.json")
    manifest = {}
    if os.path.exists(manifest_path):
        manifest = json.load(open(manifest_path, encoding="utf-8"))
        print(f"manifest: {sum(1 for v in manifest.values() if v['status'] == 'ok')} "
              f"pages already done — resuming")

    total_slots = 192 * 2
    done = failed = blank = 0
    for n in range(1, 193):
        for left in (True, False):
            slot = 2 * n - (1 if left else 0)
            if slot < lo or slot > hi:
                continue
            key = f"page-{slot:03d}"
            if manifest.get(key, {}).get("status") == "ok":
                done += 1
                continue
            book_page = slot - OFFSET_DEFAULT
            try:
                text = half_text(args.pdf, n, left)
            except subprocess.CalledProcessError as e:
                print(f"[{key}] pdftotext failed: {e.stderr}", file=sys.stderr)
                manifest[key] = {"pdf_page": slot, "book_page": book_page,
                                 "status": "failed"}
                failed += 1
                continue
            if len(text) < 20:
                manifest[key] = {"pdf_page": slot, "book_page": book_page,
                                 "source_2up_page": n,
                                 "half": "left" if left else "right",
                                 "status": "blank"}
                blank += 1
                continue
            backend_note = (f"2-up pdf page {n} "
                            f"({'left' if left else 'right'} half)")
            md = (front_matter(slot, book_page, backend_note)
                  + "\n" + text + "\n")
            with open(os.path.join(md_dir, f"{key}.md"), "w",
                      encoding="utf-8") as f:
                f.write(md)
            manifest[key] = {
                "pdf_page": slot, "book_page": book_page,
                "source_2up_page": n, "half": "left" if left else "right",
                "chapter": chapter_for(max(book_page, 1))[1],
                "status": "ok", "chars": len(text),
                "sha256": hashlib.sha256(text.encode()).hexdigest()[:16],
            }
            done += 1
    if done and not (lo == 1 and hi == total_slots):
        pass  # partial run; manifest still records per-slot state

    json.dump(manifest, open(manifest_path, "w", encoding="utf-8"),
              indent=1)
    print(f"\nDONE {done} ok, {blank} blank, {failed} failed "
          f"-> {manifest_path}")


if __name__ == "__main__":
    main()
