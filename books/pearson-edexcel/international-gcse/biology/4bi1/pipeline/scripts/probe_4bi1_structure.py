#!/usr/bin/env python3
"""Phase-2 structure probe for the 4BI1 Biology student book (text-layer lane).

Book form (from intake T-INTAKE-4BI1-1): 179 landscape 2-up spreads, each PDF
page carries two book pages. This probe pins down, with printed evidence:

  1. spread -> book-page mapping (three ways: running header/footer digits,
     TOC digits, chapter-opener LEARNING OBJECTIVES pages)
  2. front-matter extent (which spreads are unnumbered)
  3. marker census (LEARNING OBJECTIVES / KEY POINTS / chapter & unit
     questions / ANSWERS / PRACTICAL / DID YOU KNOW ...)
  4. layout sanity: blocks crossing the spread midline, header/footer bands

Outputs human-readable evidence to data/biology/probe_out/ + a summary JSON.
Foreground script; no network. Resumable by design (deterministic re-run).
"""
import json, re, sys, collections
import fitz  # PyMuPDF

PDF = "/home/z/my-project/data/biology/student-book.pdf"
OUT_DIR = "/home/z/my-project/data/biology/probe_out"
N_SPREADS = 179

doc = fitz.open(PDF)
W = doc[0].rect.width   # ~841.9
H = doc[0].rect.height  # ~525.7
MID = W / 2.0
print(f"pages={len(doc)}  size={W:.1f}x{H:.1f}  mid={MID:.1f}")

HALF = {"L": (0.0, MID), "R": (MID, W)}

def half_blocks(page):
    """Return (side, list-of-block-dicts) with bboxes, split by block center x."""
    out = []
    d = page.get_text("dict")
    for b in d["blocks"]:
        if b.get("type") != 0:
            continue
        x0, y0, x1, y1 = b["bbox"]
        cx = (x0 + x1) / 2.0
        side = "L" if cx < MID else "R"
        spans = []
        for ln in b.get("lines", []):
            txt = "".join(s["text"] for s in ln.get("spans", []))
            if txt.strip():
                spans.append((ln["bbox"][1], txt, ln["bbox"][0]))
        spans.sort(key=lambda t: (t[0], t[2]))
        if spans:
            out.append((side, {"bbox": b["bbox"], "lines": spans}))
    return out

# ---------------------------------------------------------------- pass 1
# header/footer band census + block-midline violations
band_rows = []       # (spread, side, band, text)
crossers = []        # blocks whose bbox spans the midline
for p in range(len(doc)):
    page = doc[p]
    for side, blk in half_blocks(page):
        x0, y0, x1, y1 = blk["bbox"]
        if (x0 < MID - 2 and x1 > MID + 2):
            crossers.append((p + 1, side, round(x0, 1), round(x1, 1),
                             " ".join(t for _, t, _ in blk["lines"])[:60]))
        for _, txt, _lx in blk["lines"]:
            ty = _  # unused
        for yy, txt, lx in blk["lines"]:
            if yy < 42:
                band_rows.append((p + 1, side, "top", txt.strip()))
            elif yy > H - 45:
                band_rows.append((p + 1, side, "bot", txt.strip()))

with open(f"{OUT_DIR}/bands.txt", "w") as f:
    for row in band_rows:
        f.write(repr(row) + "\n")
print(f"band lines: {len(band_rows)}  midline crossers: {len(crossers)}")
with open(f"{OUT_DIR}/crossers.txt", "w") as f:
    for row in crossers:
        f.write(repr(row) + "\n")

# digits found in bands per (spread, side) -> candidate page numbers
digit_rows = []
for sp, side, band, txt in band_rows:
    m = re.fullmatch(r"\D*(\d{1,3})\D*", txt)
    if m and not re.search(r"[A-Za-z]{3}", txt):
        digit_rows.append((sp, side, band, int(m.group(1))))
print("band digits (first 40):")
for r in digit_rows[:40]:
    print("   ", r)

# ---------------------------------------------------------------- pass 2
# TOC / LEARNING OBJECTIVES / ANSWERS / marker census
MARKERS = {
    "learning_objectives": re.compile(r"LEARNING[.\s]*OBJECTIVES", re.I),
    "chapter_questions":   re.compile(r"CHAPTER\s+QUESTIONS", re.I),
    "unit_questions":      re.compile(r"UNIT\s+QUESTIONS", re.I),
    "answers":             re.compile(r"\bANSWERS\b"),
    "key_points":          re.compile(r"KEY\s+POINTS?\b", re.I),
    "did_you_know":        re.compile(r"DID\s+YOU\s+KNOW", re.I),
    "practical":           re.compile(r"\bPRACTICAL\b", re.I),
    "activity":            re.compile(r"\bACTIVITY\s*\d*", re.I),
    "exam_preparation":    re.compile(r"EXAM\s+(PREPARATION|PRACTICE)", re.I),
    "hint":                re.compile(r"\bHINTS?\b"),
    "link":                re.compile(r"\bLINK\b"),
    "maths_skills":        re.compile(r"MATHS\s+SKILLS", re.I),
    "contents":            re.compile(r"\bCONTENTS\b"),
    "glossary":            re.compile(r"\bGLOSSARY\b", re.I),
    "index":               re.compile(r"\bINDEX\b"),
}
marker_hits = collections.defaultdict(list)   # marker -> [(spread, side)]
page_texts = {}                               # (spread, side) -> text
for p in range(len(doc)):
    halves = {"L": [], "R": []}
    for side, blk in half_blocks(doc[p]):
        halves[side].append(blk)
    for side in ("L", "R"):
        txt = "\n".join(" ".join(t for _, t, _ in b["lines"]) for b in sorted(
            halves[side], key=lambda b: b["bbox"][1]))
        page_texts[(p + 1, side)] = txt
        for key, rx in MARKERS.items():
            if rx.search(txt):
                marker_hits[key].append((p + 1, side))

with open(f"{OUT_DIR}/page_texts.json", "w") as f:
    json.dump({f"{s}-{d}": t for (s, d), t in page_texts.items()}, f)

print("\nmarker census (spread,side hits):")
for key in MARKERS:
    hits = marker_hits[key]
    print(f"  {key:22s} {len(hits):4d}  e.g. {hits[:8]}")

# ---------------------------------------------------------------- pass 3
# dump TOC spreads and the first LEARNING OBJECTIVES opener per chapter start
with open(f"{OUT_DIR}/toc_candidates.txt", "w") as f:
    for (s, d), txt in page_texts.items():
        if MARKERS["contents"].search(txt) and len(txt) > 200:
            f.write(f"===== spread {s} side {d} =====\n{txt}\n\n")
print("\nTOC candidates written; LEARNING OBJECTIVES half-pages:",
      len(marker_hits["learning_objectives"]))

summary = {
    "n_spreads": len(doc),
    "page_size": [W, H],
    "midline_crossers": len(crossers),
    "band_digit_rows": digit_rows,
    "marker_hits": {k: v for k, v in marker_hits.items()},
}
json.dump(summary, open(f"{OUT_DIR}/probe_summary.json", "w"), indent=1)
print("\nprobe complete ->", OUT_DIR)
