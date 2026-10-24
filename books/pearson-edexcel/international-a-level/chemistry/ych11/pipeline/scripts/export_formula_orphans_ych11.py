#!/usr/bin/env python3
"""Export empty-formula-region orphans from the YCH11 SB1 page JSONs.

The docling 2.33.0 blank-formula bug (YPH11 METHOD D-7, books/README.md L-020)
blanks formula-region text: layout model classifies regions, CodeFormula text
emission is empty. Every empty formula/code item is an orphan carrying a
display equation that OCR text items do NOT contain.

Exports evidence/formula_orphans.json: per orphan {pdf_page, item_index, bbox,
prev_text, next_text} for the verbatim manual-transcription pass
(manual_formula_ws_ych11.py applies transcriptions back onto the page JSONs).
"""
import json, glob, os, collections

PAGES_DIR = "/home/z/my-project/data/ych11_sb1/docling_pages"
OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "evidence", "formula_orphans.json")

orphans = []
pages_with = collections.Counter()
for fp in sorted(glob.glob(f"{PAGES_DIR}/page_*.json")):
    d = json.load(open(fp))
    if d.get("error"):
        continue
    items = d.get("items", [])
    for i, it in enumerate(items):
        if it["label"] in ("formula", "code") and not (it.get("text") or "").strip():
            prev_t = next((x.get("text", "") for x in reversed(items[:i])
                           if (x.get("text") or "").strip()), "")
            next_t = next((x.get("text", "") for x in items[i + 1:]
                           if (x.get("text") or "").strip()), "")
            orphans.append({
                "pdf_page": d["pdf_page"],
                "book_page": d["book_page"],
                "item_index": i,
                "bbox": it.get("bbox"),
                "prev_text": (prev_t or "")[:120],
                "next_text": (next_t or "")[:120],
            })
            pages_with[d["pdf_page"]] += 1

os.makedirs(os.path.dirname(OUT), exist_ok=True)
json.dump({"n_orphans": len(orphans), "n_pages": len(pages_with),
           "pages": dict(pages_with), "orphans": orphans},
          open(OUT, "w"), indent=1)
print(f"orphans: {len(orphans)} on {len(pages_with)} pages -> {OUT}")
print("pages:", ",".join(str(p) for p in sorted(pages_with)))
