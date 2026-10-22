#!/usr/bin/env python3
"""Manual-transcription workflow helper for orphan formulas.
Usage:
  python3 scripts/manual_formula_ws_yph11.py ws P1 P2 ...   # render + worksheets
  python3 scripts/manual_formula_ws_yph11.py apply          # apply sidecars
Sidecars: append JSON lines to data/yph11_sb1/manual_formulas.jsonl:
  {"pdf_page": 132, "items": {"14": "y = mx + c", "16": "..."}}
'apply' writes each equation into the page JSON item text and flags
formula_rescued=true, rescue="manual-transcription".
"""
import os, sys, json, glob

os.environ.setdefault("HF_HUB_OFFLINE", "1")

sys.path.insert(0, "/home/z/my-project/scripts")
import fitz

PDF = "/home/z/my-project/data/yph11_sb1.pdf"
PAGES_DIR = "/home/z/my-project/data/yph11_sb1/docling_pages"
OUT_PNG = "/home/z/my-project/data/yph11_sb1/probe_png"
ORPHANS = json.load(open("/home/z/my-project/data/yph11_sb1/formula_orphans.json"))
SIDECARS = "/home/z/my-project/data/yph11_sb1/manual_formulas.jsonl"

def worksheets(pnos):
    doc = fitz.open(PDF)
    for pno in pnos:
        pno = int(pno)
        idxs = ORPHANS.get(str(pno), [])
        page = doc[pno - 1]
        pix = page.get_pixmap(matrix=fitz.Matrix(1.3, 1.3))
        pix.save(f"{OUT_PNG}/p{pno:03d}.png")
        d = json.load(open(f"{PAGES_DIR}/page_{pno:03d}.json"))
        items = d["items"]
        print(f"=== pdf {pno} (png p{pno:03d}.png) {len(idxs)} orphans ===")
        for i in idxs:
            it = items[i]
            bb = it.get("bbox") or [0, 0, 0, 0]
            # context: nearest preceding + following non-empty text item
            prev_ctx = nxt_ctx = ""
            for j in range(i - 1, -1, -1):
                t = (items[j].get("text") or "").strip()
                if t and items[j]["label"] in ("text", "list_item", "section_header", "caption"):
                    prev_ctx = t[-55:]
                    break
            for j in range(i + 1, len(items)):
                t = (items[j].get("text") or "").strip()
                if t and items[j]["label"] in ("text", "list_item", "section_header", "caption"):
                    nxt_ctx = t[:55]
                    break
            print(f"  item {i:3d} x=[{bb[0]:5.1f},{bb[2]:6.1f}] y={bb[1]:6.1f} "
                  f"prev=...{prev_ctx!r} next={nxt_ctx!r}...")
    doc.close()

def apply():
    n = 0
    for line in open(SIDECARS):
        line = line.strip()
        if not line or line.startswith("#"):
            continue
        rec = json.loads(line)
        pno = rec["pdf_page"]
        fp = f"{PAGES_DIR}/page_{pno:03d}.json"
        d = json.load(open(fp))
        for idx_s, eq in rec["items"].items():
            i = int(idx_s)
            assert d["items"][i]["label"] in ("formula", "code"), (pno, i)
            cur = (d["items"][i].get("text") or "").strip()
            if cur == eq.strip():
                continue  # idempotent re-apply
            assert not cur, (pno, i, "conflicting text already present", cur[:60])
            d["items"][i]["text"] = eq
            d["items"][i]["formula_rescued"] = True
            d["items"][i]["rescue"] = "manual-transcription"
            n += 1
        json.dump(d, open(fp, "w"), ensure_ascii=False)
    print(f"[apply] patched {n} orphan formulas")

if __name__ == "__main__":
    if sys.argv[1] == "apply":
        apply()
    else:
        worksheets(sys.argv[2:])
