#!/usr/bin/env python3
"""Phase-4 extraction for the 4BI1 Biology student book — TEXT-LAYER route.

This is the first text-layer lane in the playbook (playbook §5 phase 1 says:
"If a future book HAS a text layer, stop and re-plan" — re-plan approved by
intake T-INTAKE-4BI1-1: native Word-2016 print-replica, OCR route NOT
required). IBM Docling + RapidOCR are NOT used; PyMuPDF extracts the native
text with coordinates.

Form: 179 landscape 2-up spreads. Each spread carries two book pages:
  book_page(left half)  = 2*spread - 10   (even, verso)
  book_page(right half) = 2*spread - 9    (odd,  recto)
Three-way confirmed 2026-10-21 (probe_4bi1_structure.py):
  1. running-header digits: R-top 93 hits follow 2s-9 across spreads 72-178;
     L-top hits (s7-s11) follow 2s-10
  2. course-structure digits: ch1 p3 -> spread 6 R, ch2 25 -> 17 R,
     ch3 39 -> 24 R, ch4 52 -> 31 L ... ch22 289 -> 149 R
  3. LEARNING OBJECTIVES opener hits land on the computed opener half-pages
     (15/22 direct; 7 openers have CMap-garbled headings, verified by eye)

Per-half-page JSON checkpoints (skip-if-exists, resumable). Line text is the
NATURAL span concatenation (PyMuPDF already reconstructs kerning splits like
"Th|is" -> "This"); NO space inserted between spans.

Line record: [y0, x0, x1, text, size, bold, italic]
  size = max span size; bold/italic from span flags (may be absent on this
  print-replica: fonts report as base-14 Helvetica/Times, flags still set).
"""
import fitz, json, os, re, sys

PDF = "/home/z/my-project/data/biology/student-book.pdf"
OUT_DIR = "/home/z/my-project/data/biology/text_pages"
N_SPREADS = 179
HEADER_Y = 30.0  # running headers sit at y=13-14 (probe: n=90, min 13 max 14)

os.makedirs(OUT_DIR, exist_ok=True)
doc = fitz.open(PDF)
mid = doc[0].rect.width / 2

def half_of_block(bbox):
    x0, y0, x1, y1 = bbox
    return "L" if (x0 + x1) / 2 < mid else "R"

done = 0
for p in range(len(doc)):
    out_path = f"{OUT_DIR}/page_{p+1:03d}.json"
    if os.path.exists(out_path):
        done += 1
        continue
    page = doc[p]
    halves = {"L": [], "R": []}
    d = page.get_text("dict")
    n_imgs = len(page.get_images(full=True))
    for b in d["blocks"]:
        if b.get("type") != 0:
            continue
        side = half_of_block(b["bbox"])
        for ln in b.get("lines", []):
            spans = [s for s in ln.get("spans", []) if s["text"].strip()]
            if not spans:
                continue
            text = "".join(s["text"] for s in ln.get("spans", []))
            text = text.strip()
            if not text:
                continue
            size = max(s["size"] for s in spans)
            bold = any(s["flags"] & 16 for s in spans)
            italic = any(s["flags"] & 2 for s in spans)
            halves[side].append([
                round(ln["bbox"][1], 1), round(ln["bbox"][0], 1),
                round(ln["bbox"][2], 1), text, round(size, 1), bold, italic,
            ])
    # NOTE: keep NATURAL content-stream order (Word print-replica exports
    # blocks in authored reading order; y-sorting was tested and INTERLEAVES
    # sidebar boxes into main text — see probe 2026-10-21, METHOD doc D-4).
    rec = {
        "pdf_page": p + 1,
        "book_pages": {"L": 2 * (p + 1) - 10, "R": 2 * (p + 1) - 9},
        "n_images": n_imgs,
        "lines": halves,
        "header_lines": {
            s: [r for r in halves[s] if r[0] < HEADER_Y] for s in ("L", "R")
        },
        "body_lines": {
            s: [r for r in halves[s] if r[0] >= HEADER_Y] for s in ("L", "R")
        },
    }
    with open(out_path, "w") as f:
        json.dump(rec, f, ensure_ascii=False)
    done += 1
    if done % 20 == 0:
        print(f"[extract] {done}/{N_SPREADS}", flush=True)

print(f"[extract] complete: {done}/{N_SPREADS} spreads -> {OUT_DIR}")
