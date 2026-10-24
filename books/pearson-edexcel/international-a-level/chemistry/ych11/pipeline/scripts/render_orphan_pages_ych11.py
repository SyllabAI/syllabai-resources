#!/usr/bin/env python3
"""Render the formula-orphan pages of YCH11 SB1 at 150 dpi for the
verbatim manual-transcription pass (L-020 remedy of record).
PNGs go to data/ych11_sb1/formula_png/ (workspace scratch)."""
import json, os, sys, fitz

ORPHANS = "/home/z/my-project/gh_repos/syllabai-resources/books/pearson-edexcel/international-a-level/chemistry/ych11/pipeline/evidence/formula_orphans.json"
PDF = "/home/z/my-project/scratch/ych11/ych11_sb1_taleem360.pdf"
OUT = "/home/z/my-project/data/ych11_sb1/formula_png"
os.makedirs(OUT, exist_ok=True)

pages = sorted({o["pdf_page"] for o in json.load(open(ORPHANS))["orphans"]})
if len(sys.argv) > 1:
    want = {int(x) for x in sys.argv[1:]}
    pages = [p for p in pages if p in want]

doc = fitz.open(PDF)
for pno in pages:
    fp = f"{OUT}/p{pno:03d}.png"
    if os.path.exists(fp):
        continue
    pix = doc[pno - 1].get_pixmap(dpi=150)
    pix.save(fp)
    print(f"rendered {fp}")
doc.close()
print(f"{len(pages)} pages rendered to {OUT}")
