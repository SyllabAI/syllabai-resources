#!/usr/bin/env python3
"""extract_9701.py — PyMuPDF dict-mode text extraction for 9701 (clean regenerated PDF).

Per-page output JSON: {"pdf": N, "lines": [str], "headings": [(line_idx, size)], ...}
Key features (probed):
- watermark strip: 3 CJK ad lines on pdf 31/66 (is_watermark_line, structure module)
- sub/superscript rebuild from span geometry: size<8pt spans offset vs line body
  baseline -> Unicode ₀-₉/⁰-⁹/⁻/⁺ (chemistry-grade formulas, docling-class result)
- line assembly in x order within y-banded lines; blocks y-sorted (single-column render)
- de-hyphenation: EOL '-' joins (0.2% of lines) handled at parse stage, not here
"""
import fitz, json, os, sys, re, unicodedata

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from book_structure_9701 import is_watermark_line

PDF = "/home/z/my-project/syllabai-resources/books/cambridge-international/ial/chemistry/9701/source/student-book.pdf"
OUT_DIR = "/home/z/my-project/data/9701/text_pages"

SUB = str.maketrans("0123456789-−+()n", "₀₁₂₃₄₅₆₇₈₉₋₋₊₍₎ₙ")
SUP = str.maketrans("0123456789-−+()n", "⁰¹²³⁴⁵⁶⁷⁸⁹⁻⁻⁺⁽⁾ⁿ")


def page_lines(p):
    """Page-level span pool assembly.

    Body spans (size>=8) cluster into lines by y. Small spans (size<8: sub/sup)
    attach to the nearest body line whose x-window brackets them (|dy|<14);
    x-order emission; same-x-cluster ties emit superscript before subscript
    (isotope law: nucleon number top, proton number bottom).
    """
    d = p.get_text("dict")
    raw = []
    for b in d["blocks"]:
        if b.get("type") != 0:
            continue
        for l in b.get("lines", []):
            for s in l["spans"]:
                if not s["text"]:
                    continue
                raw.append({"x0": s["bbox"][0], "x1": s["bbox"][2],
                            "ym": (s["bbox"][1] + s["bbox"][3]) / 2,
                            "size": s["size"], "text": s["text"],
                            "sup": bool(s["flags"] & 1),
                            "bold": bool(s["flags"] & 16)})
    body = [r for r in raw if r["size"] >= 8.0 and r["text"].strip()]
    small = [r for r in raw if r["size"] < 8.0 and r["text"].strip()]
    # cluster body spans into lines by y-mid
    body.sort(key=lambda r: (r["ym"], r["x0"]))
    lines = []
    for r in body:
        if lines and abs(r["ym"] - lines[-1]["ym"]) < 3.0:
            lines[-1]["spans"].append(r)
            n = len(lines[-1]["spans"])
            lines[-1]["ym"] = (lines[-1]["ym"] * (n - 1) + r["ym"]) / n
        else:
            lines.append({"ym": r["ym"], "spans": [r]})
    # attach small spans
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
        # else: orphan small span (page number-less footer etc.) -> drop
    # emit lines
    blocks = []
    for ln in sorted(lines, key=lambda l: l["ym"]):
        spans = sorted(ln["spans"], key=lambda r: (r["x0"], 0 if r.get("__dy", 0) < 0 else 1))
        txt, prev_x1 = "", None
        for r in spans:
            t = r["text"]
            if r["size"] < 8.0:
                dy = r.get("__dy", 0)
                t = t.translate(SUP if (dy < 0 or r["sup"]) else SUB)
                txt += t
            else:
                if prev_x1 is not None and r["x0"] - prev_x1 > 1.0 and txt and not txt[-1].isspace() and not t[0].isspace():
                    txt += " "
                txt += t
            prev_x1 = r["x1"]
        txt = txt.replace("\u00ad", "").strip()
        if not txt or is_watermark_line(txt):
            continue
        # normalize em/multi spaces
        txt = re.sub(r"\u2003+", "  ", txt)
        maxsize = max(r["size"] for r in ln["spans"])
        bold = any(r["bold"] for r in ln["spans"] if r["size"] >= 8.0)
        blocks.append((round(ln["ym"], 1), round(min(sp["x0"] for sp in ln["spans"]), 1),
                       txt, round(maxsize, 2), bold))
    return blocks


def main():
    os.makedirs(OUT_DIR, exist_ok=True)
    doc = fitz.open(PDF)
    n = 0
    for i, p in enumerate(doc):
        out = os.path.join(OUT_DIR, f"page_{i+1:03d}.json")
        if os.path.exists(out):
            continue
        blocks = page_lines(p)
        data = {
            "pdf": i + 1,
            "w": round(p.rect.width),
            "h": round(p.rect.height),
            "blocks": [{"y": y, "x": x, "text": t, "size": sz, "bold": bo}
                       for (y, x, t, sz, bo) in blocks],
        }
        with open(out, "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False)
        n += 1
        if n % 200 == 0:
            print(f"extracted {i+1}/{doc.page_count}")
    print(f"DONE pages={doc.page_count} written={n}")


if __name__ == "__main__":
    main()
