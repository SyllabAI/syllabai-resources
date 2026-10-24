#!/usr/bin/env python3
"""Apply the verbatim manual-transcription rescue to the YCH12 SB2 page JSONs.

Reads the merged sidecar (data/ych12_sb2/manual_formulas_ych12.jsonl, built
from manual_batch_*.jsonl) and patches each targeted formula/code item's text
in data/ych12_sb2/docling_pages/page_NNN.json. Idempotent: re-running skips
items already carrying the same text. Position-verified: bbox in the sidecar
(if present) must match the item bbox within tolerance; item_index is exact.
Empty-text records are ADJUDICATED slivers/duplicates — left empty, marked.
"""
import json, glob, os, sys

SIDECAR = "/home/z/my-project/data/ych12_sb2/manual_formulas_ych12.jsonl"
PAGES_DIR = "/home/z/my-project/data/ych12_sb2/docling_pages"
TOL = 6.0  # bbox tolerance in pt

def bbox_close(a, b, tol=TOL):
    if not a or not b or len(a) != 4 or len(b) != 4:
        return True  # nothing to compare
    return all(abs(float(x) - float(y)) <= tol for x, y in zip(a, b))

recs = [json.loads(l) for l in open(SIDECAR) if l.strip()]
by_page = {}
for r in recs:
    by_page.setdefault(r["pdf_page"], []).append(r)

applied = adjudicated = already = mismatch = 0
for fp in sorted(glob.glob(f"{PAGES_DIR}/page_*.json")):
    d = json.load(open(fp))
    pno = d["pdf_page"]
    if pno not in by_page:
        continue
    changed = False
    items = d.get("items", [])
    for r in by_page[pno]:
        idx = r["item_index"]
        if idx >= len(items):
            print(f"page {pno} item {idx}: OUT OF RANGE")
            mismatch += 1
            continue
        it = items[idx]
        if it["label"] not in ("formula", "code"):
            print(f"page {pno} item {idx}: label {it['label']!r} not formula/code — SKIPPED")
            mismatch += 1
            continue
        cur = (it.get("text") or "").strip()
        want = (r.get("text") or "").strip()
        if not bbox_close(r.get("bbox"), it.get("bbox")):
            print(f"page {pno} item {idx}: BBOX MISMATCH sidecar={r.get('bbox')} item={it.get('bbox')}")
            mismatch += 1
            continue
        if not want:
            if not it.get("rescue_adjudicated"):
                it["rescue_adjudicated"] = "sliver_or_duplicate"
                adjudicated += 1
                changed = True
            else:
                already += 1
            continue
        if cur == want:
            already += 1
            continue
        it["text"] = want
        it["rescued"] = True
        if cur:
            it["rescued_replaced_mangled"] = True
        applied += 1
        changed = True
    if changed:
        json.dump(d, open(fp, "w"), ensure_ascii=False)

print(f"applied={applied} adjudicated_empty={adjudicated} already_ok={already} mismatch={mismatch}")
if mismatch:
    sys.exit(1)
