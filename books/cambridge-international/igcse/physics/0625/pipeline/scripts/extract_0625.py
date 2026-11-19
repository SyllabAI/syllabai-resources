#!/usr/bin/env python3
"""extract_0625.py — column-aware PyMuPDF span-pool extraction for the CIE 0625
book (text-layer lane, no OCR).

Column law (probed on raw span geometry; evidence cache/w-f9/probe*.json):
FIXED gutter x=307 (the render has an irregular two-band grid — per-page votes are unreliable); both-bands >= 6-spans sanity; crossing spans stay in the left band; col 0 emitted fully before col 1
Sub/superscript rebuild from span geometry: spans < 8.5pt attach to the nearest
body line (|dy| < 14pt) and translate to Unicode sub/superscripts.
Per-page JSON checkpoints (skip-if-exists, resume-safe, golden rule 7).

Paths are workspace-era dependent (this era: repo at
/home/z/my-project/cache/syllabai-resources, data at /home/z/my-project/cache/w-f9/).
"""
import fitz, json, os, re, sys, glob, statistics

PDF = "/home/z/my-project/cache/w-f9/pdfs/0625.pdf"
OUT_DIR = "/home/z/my-project/cache/w-f9/text_pages/0625"
SMALL = 8.5          # small-span (sub/sup) threshold, pt
FIXED_GUTTER = 307     # None = per-page vote law

SUB = str.maketrans("0123456789-−+()n", "₀₁₂₃₄₅₆₇₈₉₋₋₊₍₎ₙ")
SUP = str.maketrans("0123456789-−+()n", "⁰¹²³⁴⁵⁶⁷⁸⁹⁻⁻⁺⁽⁾ⁿ")
def collect(p, small_thresh):
    d = p.get_text("dict")
    raw = []
    for b in d["blocks"]:
        if b.get("type") != 0:
            continue
        for l in b.get("lines", []):
            for s in l["spans"]:
                if not s["text"].strip():
                    continue
                raw.append({"x0": s["bbox"][0], "x1": s["bbox"][2],
                            "ym": (s["bbox"][1] + s["bbox"][3]) / 2,
                            "size": s["size"], "text": s["text"],
                            "sup": bool(s["flags"] & 1),
                            "bold": bool(s["flags"] & 16)})
    return raw


def gutter_of(raw, small_thresh):
    """v3: page-level gutter vote.

    Per y-band line, candidate gaps: consecutive span gap >= 14pt with both
    sides >= 25pt wide. Largest vote cluster (within 24pt) with >= 4 votes wins;
    both bands must hold >= 6 body spans. Returns gutter x or None.
    """
    body = [r for r in raw if r["size"] >= small_thresh and r["text"].strip()]
    body.sort(key=lambda r: (r["ym"], r["x0"]))
    lines = []
    for r in body:
        if lines and abs(r["ym"] - lines[-1][0]["ym"]) < 3.0:
            lines[-1].append(r)
        else:
            lines.append([r])
    votes = []
    for ln in lines:
        spans = sorted(ln, key=lambda s: s["x0"])
        for a, b in zip(spans, spans[1:]):
            gap = b["x0"] - a["x1"]
            if gap >= 14 and (a["x1"] - a["x0"]) >= 25 and (b["x1"] - b["x0"]) >= 25:
                votes.append((gap / 2) + a["x1"])
    if len(votes) < 4:
        return None
    votes.sort()
    best_cluster, cur = [], []
    for v in votes:
        if cur and v - cur[0] > 24:
            if len(cur) > len(best_cluster):
                best_cluster = cur
            cur = []
        cur.append(v)
    if len(cur) > len(best_cluster):
        best_cluster = cur
    if len(best_cluster) < 4:
        return None
    g = statistics.median(best_cluster)
    left = [r for r in body if (r["x0"] + r["x1"]) / 2 < g]
    right = [r for r in body if (r["x0"] + r["x1"]) / 2 >= g]
    if len(left) < 6 or len(right) < 6:
        return None
    return g


def assemble_band(spans, small_thresh):
    """span-pool -> lines for one band (the extract_9701 algorithm)."""
    body = [r for r in spans if r["size"] >= small_thresh and r["text"].strip()]
    small = [r for r in spans if r["size"] < small_thresh and r["text"].strip()]
    body.sort(key=lambda r: (r["ym"], r["x0"]))
    lines = []
    for r in body:
        if lines and abs(r["ym"] - lines[-1]["ym"]) < 3.0:
            lines[-1]["spans"].append(r)
            n = len(lines[-1]["spans"])
            lines[-1]["ym"] = (lines[-1]["ym"] * (n - 1) + r["ym"]) / n
        else:
            lines.append({"ym": r["ym"], "spans": [r]})
    for s in small:
        best, best_dy = None, 99.0
        for ln in lines:
            lx0 = min(sp["x0"] for sp in ln["spans"])
            lx1 = max(sp["x1"] for sp in ln["spans"])
            if not (lx0 - 6 <= (s["x0"] + s["x1"]) / 2 <= lx1 + 40):
                continue
            dy = s["ym"] - ln["ym"]
            if abs(dy) < 14 and abs(dy) < abs(best_dy):
                best, best_dy = ln, dy
        if best is not None:
            s["__dy"] = best_dy
            best["spans"].append(s)
    blocks = []
    for ln in sorted(lines, key=lambda l: l["ym"]):
        spans2 = sorted(ln["spans"], key=lambda r: (r["x0"], 0 if r.get("__dy", 0) < 0 else 1))
        txt, prev_x1 = "", None
        for r in spans2:
            t = r["text"]
            if r["size"] < small_thresh:
                dy = r.get("__dy", 0)
                t = t.translate(SUP if (dy < 0 or r["sup"]) else SUB)
                txt += t
            else:
                if prev_x1 is not None and r["x0"] - prev_x1 > 1.0 and txt and not txt[-1].isspace() and not t[0].isspace():
                    txt += " "
                txt += t
            prev_x1 = r["x1"]
        txt = txt.replace("\u00ad", "").strip()
        if not txt:
            continue
        txt = re.sub(r"\u2003+", "  ", txt)
        maxsize = max(r["size"] for r in ln["spans"])
        bold = any(r["bold"] for r in ln["spans"] if r["size"] >= small_thresh)
        blocks.append((round(ln["ym"], 1), round(min(sp["x0"] for sp in ln["spans"]), 1),
                       txt, round(maxsize, 2), bold))
    return blocks


def page_blocks(p, small_thresh, fixed_gutter=None):
    raw = collect(p, small_thresh)
    g = fixed_gutter if fixed_gutter else gutter_of(raw, small_thresh)
    out = []
    if g is not None:
        body_count = sum(1 for r in raw if r["size"] >= small_thresh and r["text"].strip())
        left_n = sum(1 for r in raw if (r["x0"] + r["x1"]) / 2 < g)
        right_n = body_count - left_n
        if left_n >= 6 and right_n >= 6:
            left = [r for r in raw if (r["x0"] + r["x1"]) / 2 < g]
            right = [r for r in raw if (r["x0"] + r["x1"]) / 2 >= g]
            for col, band in ((0, left), (1, right)):
                for (y, x, t, sz, bo) in assemble_band(band, small_thresh):
                    out.append({"y": y, "x": x, "text": t, "size": sz, "bold": bo, "col": col})
            return out, 2
    for (y, x, t, sz, bo) in assemble_band(raw, small_thresh):
        out.append({"y": y, "x": x, "text": t, "size": sz, "bold": bo, "col": 0})
    return out, 0


def main():
    which = sys.argv[1:] or list(BOOKS)
    for code in which:
        cfg = BOOKS[code]
        outdir = os.path.join(OUT, code)
        os.makedirs(outdir, exist_ok=True)
        # v2: wipe stale v1 pages (layout law changed)
        import glob
        for f in glob.glob(os.path.join(outdir, "page_*.json")):
            os.remove(f)
        doc = fitz.open(os.path.join(PDFS, f"{code}.pdf"))
        n_new = 0
        n_col = 0
        for i, p in enumerate(doc):
            out = os.path.join(outdir, f"page_{i+1:03d}.json")
            blocks, nb = page_blocks(p, cfg["small"], cfg.get("fixed_gutter"))
            n_col += nb
            data = {"pdf": i + 1, "w": round(p.rect.width), "h": round(p.rect.height),
                    "col_mode": nb, "blocks": blocks}
            with open(out, "w", encoding="utf-8") as f:
                json.dump(data, f, ensure_ascii=False)
            n_new += 1
            if n_new % 250 == 0:
                print(f"{code}: {i+1}/{doc.page_count}")
        print(f"{code}: DONE pages={doc.page_count} col_mode2_pages={n_col}")


if __name__ == "__main__":
    main()

def main():
    os.makedirs(OUT_DIR, exist_ok=True)
    doc = fitz.open(PDF)
    n_new = 0
    n_col = 0
    for i, p in enumerate(doc):
        out = os.path.join(OUT_DIR, f"page_{i+1:03d}.json")
        blocks, nb = page_blocks(p, SMALL, FIXED_GUTTER)
        n_col += nb
        data = {"pdf": i + 1, "w": round(p.rect.width), "h": round(p.rect.height),
                "col_mode": nb, "blocks": blocks}
        with open(out, "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False)
        n_new += 1
        if n_new % 250 == 0:
            print(f"{i+1}/{doc.page_count}")
    print(f"DONE pages={doc.page_count} col_mode2_pages={n_col}")


if __name__ == "__main__":
    main()
