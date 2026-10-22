#!/usr/bin/env python3
"""For each page with EMPTY formula items (docling 2.33 CodeFormula bug),
check whether equation content survives as plain text items (like the
physics 4PH1 base corpus did). A page is 'suspect' when empty-formula count
exceeds the number of equation-looking text items — candidates for real
content loss needing a 2.133.0 splice."""
import json, glob, re

EQ = re.compile(r"[a-zA-Z0-9\)\]]\s*[=≈×/]\s*[a-zA-Z0-9\(]|=\s*[a-zA-Z0-9]")

suspect = []
total_empty = 0
for fp in sorted(glob.glob("/home/z/my-project/data/yph11_sb1/docling_pages/page_*.json")):
    d = json.load(open(fp))
    empties = sum(1 for it in d["items"]
                  if it["label"] in ("formula", "code") and not (it.get("text") or "").strip())
    if not empties:
        continue
    total_empty += empties
    eq_texts = 0
    for it in d["items"]:
        if it["label"] in ("text", "list_item", "caption"):
            t = (it.get("text") or "").strip()
            if t and EQ.search(t) and len(t) < 120:
                eq_texts += 1
    if empties > eq_texts:
        suspect.append((d["pdf_page"], empties, eq_texts))

print(f"total empty formula items: {total_empty}")
print(f"suspect pages (empties > eq-texts): {len(suspect)}")
for pno, e, q in suspect:
    print(f"  pdf {pno:3d}: {e} empty formulas, {q} equation-ish text items")
