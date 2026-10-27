#!/usr/bin/env python3
"""T-IMG-1: re-extract canonical QP/MS figure images from the source PDFs.

Problem: the canonical QP/MS JSONs (produced 2026-09-11 by syllabai-parser /
opendataloader-pdf 2.5.7) reference figures as `input_images/imageFileN.png` —
parser-temp paths that were never kept. The engine + JDK toolchain that produced
them is no longer available, so the exact PNGs cannot be regenerated. What IS
kept: every source PDF, and each figure entry's page_number + bounding_box.

Fix (this script, idempotent):
  1. resolve each canonical JSON's source PDF via the recorded SHA-256
  2. for every figure entry, locate the matching image instance on the PDF page
     geometrically (both y-origin conventions tried; overlap > center-distance)
  3. extract the embedded raster via PyMuPDF (composed with its soft mask when
     present); if the entry has no raster partner or the xref is inline (0),
     fall back to rendering the entry's own bbox region from the page
  4. save to `<canonical dir>/images/imageFileN.png` (the name the entry
     declares; per-paper dirs keep the engine's global counter collision-free)
  5. rewrite the entry's `source_name` to `images/imageFileN.png` (surgical
     text edit — the gson formatting of the file is untouched otherwise) and
     stamp `provenance.figureRecovery` (surgical insert, idempotent)
  6. verify: every `images/` ref resolves; entries still on input_images are
     listed as unresolved (their JSON is left untouched)

Content fields (text, tables, bboxes, provenance history) are never modified.
Run: python3 pmt_qpms_fig_extract.py [--root <PMT resources dir>] [--verify-only]
"""
import glob
import hashlib
import io
import json
import os
import re
import sys
from collections import Counter
from datetime import datetime, timezone

import fitz  # PyMuPDF

ROOT = "/home/z/my-project/download/syllabai-resources/PMT Edexcel IGCSE Chemistry Resources"
if "--root" in sys.argv:
    ROOT = sys.argv[sys.argv.index("--root") + 1]
VERIFY_ONLY = "--verify-only" in sys.argv

PROV_STAMP = {
    "tool": "pmt_qpms_fig_extract.py (PyMuPDF %s)" % fitz.version[0],
    "method": "geometric match of figure bbox to embedded PDF image instance; "
              "fallback: bbox clip render",
    "reason": "original opendataloader input_images/ lost; source PDFs retained",
}
ENGINE_VERSION_RE = re.compile(r'("engineVersion"\s*:\s*"[^"]+")\s*,')


def sha256(path):
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(1 << 20), b""):
            h.update(chunk)
    return h.hexdigest()


def resolve_pdf(cjson_path, checksum, cache):
    parts = cjson_path.split(os.sep)
    unit, paper = parts[-5], parts[-3]
    kind = "Questions" if cjson_path.endswith("canonical-qp.json") else "Mark Schemes"
    for cand in sorted(glob.glob(os.path.join(ROOT, unit, kind, paper, "*.pdf"))):
        if cand not in cache:
            cache[cand] = sha256(cand)
        if cache[cand] == checksum:
            return cand
    return None


def inst_rect(info):
    x0, y0, x1, y1 = info["bbox"]
    return x0, y0, x1, y1


def best_partner(cands, rect):
    """Return (score, info) — overlap area positive beats center distance."""
    best, bi = -1e18, None
    rx, ry = (rect[0] + rect[2]) / 2.0, (rect[1] + rect[3]) / 2.0
    for info in cands:
        x0, y0, x1, y1 = inst_rect(info)
        ox = min(rect[2], x1) - max(rect[0], x0)
        oy = min(rect[3], y1) - max(rect[1], y0)
        if ox > 0 and oy > 0:
            score = ox * oy
        else:
            cx, cy = (x0 + x1) / 2.0, (y0 + y1) / 2.0
            score = -((rx - cx) ** 2 + (ry - cy) ** 2) ** 0.5
        if score > best:
            best, bi = score, info
    return best, bi


def save_png(doc, entry, page, out_path):
    """Return method used or None. rect choices: parser-top vs parser-bottom origin."""
    bb = entry["bounding_box"]
    x, y, w, h = float(bb["x"]), float(bb["y"]), float(bb["width"]), float(bb["height"])
    ph = page.rect.height
    rects = [fitz.Rect(x, y, x + w, y + h),
             fitz.Rect(x, ph - y - h, x + w, ph - y)]
    cands = page.get_image_info(xrefs=True)
    top_score, top_info = best_partner(cands, rects[0])
    bot_score, bot_info = best_partner(cands, rects[1])
    # prefer an interpretation with real overlap; else the smaller distance
    if (top_score > 0) >= (bot_score > 0):
        score, info, rect = (top_score, top_info, rects[0]) if top_score >= bot_score \
            else (bot_score, bot_info, rects[1])
    else:
        score, info, rect = bot_score, bot_info, rects[1]
    accepted = score > 0 or -score <= 2.0  # overlap, or partner within 2 pt
    if accepted and info and info.get("xref"):
        try:
            raw = doc.extract_image(info["xref"])
            img = _compose(doc, raw)
            img.save(out_path, "PNG")
            return "embedded"
        except Exception:
            pass  # fall through to clip render
    if rect.is_empty or rect.width <= 0 or rect.height <= 0:
        rect = fitz.Rect(x - 1, min(y, ph - y - h) - 1, x + w + 1,
                         max(y + h, ph - y) + 1)
        rect &= page.rect
    zoom = 2.0 if max(w, h) < 2 else 1.0
    pix = page.get_pixmap(matrix=fitz.Matrix(zoom, zoom), clip=rect, alpha=False)
    pix.save(out_path)
    return "clip-render"


def _compose(doc, raw):
    from PIL import Image
    img = Image.open(io.BytesIO(raw["image"]))
    if raw.get("smask"):
        try:
            m = doc.extract_image(raw["smask"])
            mask = Image.open(io.BytesIO(m["image"])).convert("L")
            mask = mask.resize(img.size)
            if img.mode in ("P", "CMYK"):
                img = img.convert("RGB")
            img = img.convert("RGBA")
            img.putalpha(mask)
        except Exception:
            pass
    if img.mode == "CMYK":
        img = img.convert("RGB")
    elif img.mode == "P":
        img = img.convert("RGBA" if "transparency" in img.info else "RGB")
    return img


def process(cjson_path, cache, report, owned=None):
    with open(cjson_path, encoding="utf-8") as f:
        text = f.read()
    d = json.loads(text)
    figs = d.get("figures") or []
    if not figs:
        return
    # per-document imageFile counters collide when QP and MS share one dir:
    # the first file (sorted order) keeps the plain name, later claimants of
    # the same name get a kind-suffixed file so no two entries share pixels
    kind = "qp" if cjson_path.endswith("canonical-qp.json") else "ms"
    dirkey = os.path.dirname(cjson_path)
    pdf = resolve_pdf(cjson_path, d["source"]["checksum"], cache)
    if not pdf:
        report["unresolvedPdf"].append(cjson_path)
        return
    outdir = os.path.join(os.path.dirname(cjson_path), "images")
    os.makedirs(outdir, exist_ok=True)
    doc = fitz.open(pdf)
    counts = Counter()
    changed = 0
    try:
        for entry in figs:
            src = str(entry.get("source_name") or "")
            m = re.fullmatch(r"(?:input_)?images/(imageFile\d+\.png)", src)
            if not m:
                if src.startswith("images/"):
                    counts["already-done"] += 1
                else:
                    counts["nonstandard-name"] += 1
                continue
            fname = m.group(1)
            if owned is not None:
                if (dirkey, fname) in owned and owned[(dirkey, fname)] != kind:
                    fname = re.sub(r"\.png$", "-%s.png" % kind, fname)
                else:
                    owned[(dirkey, fname)] = kind
            out_path = os.path.join(outdir, fname)
            pno = int(entry["page_number"])
            if not (1 <= pno <= doc.page_count):
                counts["bad-page"] += 1
                report["entries"].append({"file": cjson_path, "id": entry.get("element_id"),
                                          "status": "bad-page", "page": pno})
                continue
            if not os.path.exists(out_path):
                method = save_png(doc, entry, doc[pno - 1], out_path)
                counts[method or "failed"] += 1
                if not method:
                    report["entries"].append({"file": cjson_path, "id": entry.get("element_id"),
                                              "status": "failed", "declared": src})
                    continue
            else:
                counts["kept-existing"] += 1
            for old in ('"input_images/%s"' % re.sub(r"-\w+\.png$", ".png", fname),
                        '"images/%s"' % re.sub(r"-\w+\.png$", ".png", fname),
                        '"images/%s"' % fname):
                if old != '"images/%s"' % fname and text.count(old) == 1:
                    text = text.replace(old, '"images/%s"' % fname)
                    changed += 1
                    break
            else:
                if '"images/%s"' % fname not in text:
                    counts["ambiguous-ref"] += 1
    finally:
        doc.close()
    if changed:
        if "figureRecovery" not in text:
            stamp = json.dumps(PROV_STAMP, ensure_ascii=False)
            stamp = stamp[1:-1]  # strip braces for inline insert
            m = ENGINE_VERSION_RE.search(text)
            if m:
                text = text[:m.end()] + '\n    "figureRecovery" : { %s },' % stamp + text[m.end():]
        with open(cjson_path, "w", encoding="utf-8") as f:
            f.write(text)
    report["summary"][cjson_path] = dict(counts)
    report["totals"].update(counts)


def verify(report):
    bad = []
    total = resolved = 0
    for cjson_path in sorted(glob.glob(os.path.join(ROOT, "Unit */Canonical (JSON)/Paper */*/canonical-*.json"))):
        d = json.load(open(cjson_path, encoding="utf-8"))
        for entry in d.get("figures") or []:
            total += 1
            src = str(entry.get("source_name") or "")
            if src.startswith("images/"):
                if os.path.exists(os.path.join(os.path.dirname(cjson_path), src)):
                    resolved += 1
                else:
                    bad.append((cjson_path, src, "missing file"))
            elif src:
                bad.append((cjson_path, src, "still on input_images"))
    report["verify"] = {"entries": total, "resolved": resolved, "problems": bad}
    return total, resolved, bad


def main():
    report = {"generatedAt": datetime.now(timezone.utc).isoformat(timespec="seconds"),
              "tool": PROV_STAMP["tool"], "summary": {}, "totals": Counter(),
              "unresolvedPdf": [], "entries": []}
    if VERIFY_ONLY:
        total, resolved, bad = verify(report)
        print(json.dumps({"entries": total, "resolved": resolved,
                          "problems": len(bad)}, indent=2))
        for b in bad[:20]:
            print("  ", b)
        sys.exit(0 if not bad else 1)
    files = sorted(glob.glob(os.path.join(ROOT, "Unit */Canonical (JSON)/Paper */*/canonical-*.json")))
    cache = {}
    owned = {}
    for i, f in enumerate(files, 1):
        n0 = len(report["entries"])
        process(f, cache, report, owned)
        n = len(report["entries"])
        if n > n0:
            print("  !! %s: %d problem entries" % (os.path.relpath(f, ROOT), n - n0))
        if i % 20 == 0:
            print("[%d/%d] totals so far: %s" % (i, len(files), dict(report["totals"])))
    total, resolved, bad = verify(report)
    report["verify"] = {"entries": total, "resolved": resolved, "problems": bad}
    out = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                       "pmt_qpms_fig_extract_report.json")
    with open(out, "w", encoding="utf-8") as f:
        json.dump(report, f, indent=2, ensure_ascii=False, default=dict)
    print(json.dumps({"files": len(files), "entries": total, "resolved": resolved,
                      "problems": len(bad), "totals": dict(report["totals"]),
                      "unresolvedPdf": report["unresolvedPdf"], "report": out}, indent=2))
    sys.exit(0 if not bad and not report["unresolvedPdf"] else 1)


if __name__ == "__main__":
    main()
