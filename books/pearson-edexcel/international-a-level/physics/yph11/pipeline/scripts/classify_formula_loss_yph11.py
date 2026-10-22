#!/usr/bin/env python3
"""Classify every EMPTY formula item in the YPH11 page JSONs:
  twin      -> a text/list/caption item vertically overlapping the formula's
               bbox already carries equation-ish content (the empty formula is
               a duplicate region) -> safe to DROP the empty item
  orphan    -> no twin -> genuinely lost content, needs manual transcription
Outputs data/yph11_sb1/formula_orphans.json = {page: [item indices]} plus a
drop plan. Also purges earlier auto-residue (untrusted VLM decodes)."""
import json, glob, re

PAGES_DIR = "/home/z/my-project/data/yph11_sb1/docling_pages"
EQ = re.compile(r"[a-zA-Z0-9\)\]]\s*[=≈×/]\s*[a-zA-Z0-9\(]|=\s*[-a-zA-Z0-9]")

orphans = {}
drop_total = twin_total = 0
for fp in sorted(glob.glob(f"{PAGES_DIR}/page_*.json")):
    d = json.load(open(fp))
    pno = d["pdf_page"]
    changed = False
    items = d["items"]
    empty_idx = [i for i, it in enumerate(items)
                 if it["label"] in ("formula", "code") and not (it.get("text") or "").strip()]
    if not empty_idx:
        continue
    # purge untrusted auto-residue from the abandoned VLM pass
    for it in items:
        if it["label"] in ("formula", "code") and it.get("text") and it.get("formula_rescued"):
            it["text"] = ""
            it.pop("latex", None)
            it.pop("formula_rescued", None)
            changed = True
        for k in ("rescue_failed", "latex_rejected"):
            it.pop(k, None)
    page_orphans = []
    for i in empty_idx:
        it = items[i]
        bb = it.get("bbox")
        if not bb:
            page_orphans.append(i)
            continue
        l, t, r, b = bb
        twin = False
        for j, o in enumerate(items):
            if j == i or o["label"] not in ("text", "list_item", "caption"):
                continue
            ot = (o.get("text") or "").strip()
            if not ot or not EQ.search(ot) or len(ot) > 160:
                continue
            ob = o.get("bbox")
            if not ob:
                continue
            ol, ot_, orr, ob_ = ob
            # vertical overlap in y-up coords
            overlap = max(0, min(t, ot_) - max(b, ob_))
            oheight = max(1e-6, ot_ - ob_)
            if overlap / oheight > 0.45:
                twin = True
                break
        if twin:
            twin_total += 1
            it["_drop_twin"] = True
            changed = True
        else:
            orphan_total = page_orphans.append(i)
    if page_orphans:
        orphans[pno] = page_orphans
    if changed:
        json.dump(d, open(fp, "w"), ensure_ascii=False)

n_orphan_items = sum(len(v) for v in orphans.values())
print(f"empty formula items: twin(droppable)={twin_total} orphan={n_orphan_items}")
print(f"pages with orphans: {len(orphans)}")
json.dump(orphans, open("/home/z/my-project/data/yph11_sb1/formula_orphans.json", "w"), indent=1)
for pno in sorted(orphans, key=int):
    print(f"  pdf {pno}: {len(orphans[pno])} orphans at item idx {orphans[pno]}")
