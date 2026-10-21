#!/usr/bin/env python3
"""
official_examq_extract.py — ADR-037 prototype converter
========================================================
Converts ONE official past paper (QP+MS) into the serving schema
`syllabai.official-paper-questions/0.1` using VERBATIM extraction
(no generation), then runs fail-closed gates G0–G6 plus negative controls.

The one-sentence rule (ADR-037 §2): the converter extracts; it never authors.
Every character of problem_md / solution_md / choices[].text_md is copied
from the source layer; the only generated fields are labels (command_word,
spec seeds) and links (answer linkage, asset stubs) — and labels are
registry-validated or flagged for human review.

Run:  python3 official_examq_extract.py --series 2020-11   (baseline; also 2019-06, 2020-01, 2021-06, 2022-06, 2024-06)
"""
import hashlib
import json
import os
import re
import sys
from datetime import datetime, timezone
from pathlib import Path

import fitz  # PyMuPDF — page-anchored provenance
import yaml

# --- pipeline roots (LEDGER F15: derived from this file's location so the kit
# --- runs from any clean checkout; env vars override for exotic staging) ---
SCRIPTS_DIR = Path(__file__).resolve().parent            # .../syllabai-resources/scripts
RES_DIR     = SCRIPTS_DIR.parent                         # the checkout root
UPLOAD = Path(os.environ.get("EXAMQ_UPLOAD_DIR", "/home/z/my-project/upload"))
OUTROOT = RES_DIR / "Official-ExamQuestion" / "igcse-chemistry-19"   # ALWAYS inside the checkout
# spec-point registry: canonical copy lives in this repo (SME-ExamQuestion/...);
# staged spc-resolution.json is a legacy fallback for pre-F15 staging areas.
_SPEC_REPO = RES_DIR / "SME-ExamQuestion" / "igcse-chemistry-19" / "spec_point_resolution.json"
if os.environ.get("EXAMQ_SPEC_RESOLUTION"):
    SPEC_RESOLUTION = Path(os.environ["EXAMQ_SPEC_RESOLUTION"])
elif _SPEC_REPO.exists():
    SPEC_RESOLUTION = _SPEC_REPO
else:
    SPEC_RESOLUTION = UPLOAD / "spc-resolution.json"

SCHEMA = "syllabai.official-paper-questions/0.1"
CONVERTER_VERSION = "0.6"   # see Official-ExamQuestion/CHANGELOG.md + LEDGER.md
PAPER_TOTAL = 110          # registry expectation for 4CH1/1C — constant across series
# printed question counts verified per series (footers vary 9..15 across the 4CH1 era);
# counts cross-checked against per-question footer marks summing to 110
EXPECT_QUESTIONS = {"2020-11": 10, "2020-01": 10, "2021-06": 10, "2022-06": 10, "2024-06": 10,
                    "2019-06": 15, "2021-01": 11, "2021-11": 11, "2022-01": 11, "2023-01": 12,
                    "2023-06": 10, "2023-11": 10, "2024-11": 11, "2025-06": 10, "2025-11": 10,
                    "2026-06": 9}
# per-series demo seeds (labels only; registry-validated in G6). Other series -> pending-llm.
SEEDS = {
    "2020-11": {
        "1(b)(i)": "4CH1-1.20", "4(c)(ii)": "4CH1-1.25",
        "9(c)(ii)": "4CH1-1.28", "10(b)": "4CH1-1.31",
        "8(c)(ii)": "4CH1-3.9", "7": "4CH1-3.15C",   # 7* deliberately incl. registry-gap demo
    },
}


def paths_for(series: str) -> dict:
    return {
        "qp_pdf": UPLOAD / f"official-4CH1-1C-{series}-qp.pdf",
        "ms_pdf": UPLOAD / f"official-4CH1-1C-{series}-ms.pdf",
        "qp_txt": UPLOAD / f"official-{series}-qp.txt",
        "ms_txt": UPLOAD / f"official-{series}-ms.txt",
        "manifest": UPLOAD / f"manifest-{series}-1C.yaml",
        "out": OUTROOT / series / "4CH1-1C",
    }

# ---------------------------------------------------------------- utilities
def sha256(p: Path) -> str:
    h = hashlib.sha256()
    with open(p, "rb") as f:
        for chunk in iter(lambda: f.read(65536), b""):
            h.update(chunk)
    return h.hexdigest()


def norm(s: str) -> str:
    return re.sub(r"\s+", " ", s).strip().lower()


DOTRUN_RE = re.compile(r"(?:\s*\.\s*){4,}")   # printed answer lines "= . . . . . g"


def strip_dotrun(s: str) -> str:
    return DOTRUN_RE.sub(" ", s).strip()


def ngrams(text: str, n: int = 5):
    toks = norm(text).split()
    return set(tuple(toks[i:i + n]) for i in range(len(toks) - n + 1))


def now_iso():
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


# ---------------------------------------------------------------- stage 1: QP cleaning
FURNITURE_SUBS = [
    (re.compile(r"\*P\d{5}[A-Z]\w*\*"), " "),       # page identity marker (P62045A*, P58561A*, ...)
    (re.compile(r"\bTurn over\b"), " "),
    (re.compile(r"DO NOT WRITE IN THIS (?:AREA|MARGIN|SPACE)\s*"), " "),   # often 3x on one line
]
FURNITURE_LINE = [
    re.compile(r"^\s*PMT\s*$"),                     # archive watermark
    re.compile(r"^\s*BLANK PAGE\s*$"),
    re.compile(r"^\s*DO NOT WRITE IN THIS (AREA|MARGIN|SPACE)\s*$"),
    re.compile(r"^\s*\d{1,2}\s*$"),                 # bare page number (1..36)
    re.compile(r"^[\s.]*\.[\s.]*$"),                # dotted answer lines
    re.compile(r"^\s*$"),
]


def clean_lines(raw: str):
    out = []
    for ln in raw.splitlines():
        for rx, rep in FURNITURE_SUBS:
            ln = rx.sub(rep, ln)
        if any(rx.match(ln) for rx in FURNITURE_LINE):
            continue
        out.append(ln.rstrip())
    return out


# ---------------------------------------------------------------- stage 2: segmentation
FOOTER_RE = re.compile(r"\(Total for Question (\d{1,2}) = (\d{1,2}) marks\)")
QSTART_RE = re.compile(r"^\s*(\d{1,2})\s+([A-Za-z(].*)$")   # remainder must start alpha/'(' (indent-tolerant)
L1_RE = re.compile(r"^\s*\(([a-h])\s*\)\s*(.*)$")
L2_RE = re.compile(r"^\s*\((i{1,3}|iv|v|vi{1,3})\s*\)\s+(.*)$")   # romans i..viii
L2_INLINE_RE = re.compile(r"^\((i{1,3}|iv|v|vi{1,3})\s*\)\s+(.*)$")
MARK_RE = re.compile(r"^\s*\((\d{1,2})\)\s*$")
OPT_RE = re.compile(r"^\s*([A-E])\s+(\S.*?)\s*$")
ROMAN = ["i", "ii", "iii", "iv", "v", "vi", "vii", "viii"]

COMMAND_WORDS = ["identify", "explain", "state", "describe", "calculate", "draw",
                 "write", "give", "suggest", "name", "complete", "plot", "show",
                 "use", "define", "deduce", "place", "what", "which", "how", "why",
                 "complete the", "add", "order"]


def strip_leading_command(text):
    m = re.match(r"^(identify|explain|state|describe|calculate|draw|write|give|"
                 r"suggest|name|complete|plot|show|use|define|deduce|place)\b",
                 norm(text))
    return m.group(1) if m else None


def parse_mcq_block(lines):
    """Return (choices, consumed_idx_set) for a consecutive A,B,C,... option run."""
    choices, consumed = [], set()
    expect = 0  # index into A,B,C,D,E
    for i, ln in enumerate(lines):
        m = OPT_RE.match(ln)
        if m and ord(m.group(1)) - 65 == expect:
            choices.append({"label": m.group(1), "text_md": m.group(2).strip()})
            consumed.add(i)
            expect += 1
        elif choices:
            break
    return (choices if len(choices) >= 3 else []), consumed


def segment_question(qnum, region_lines):
    """Split a question region into stem + parts (two levels) + option lists."""
    q = {"number": qnum, "stem_lines": [], "groups": {}}
    order = []
    cur_group, cur_part = None, None

    # question-start line
    start_idx = 0
    m = QSTART_RE.match(region_lines[0]) if region_lines else None
    inline_rest = None
    if m and int(m.group(1)) == qnum:
        inline_rest = m.group(2).strip()
        start_idx = 1
    else:
        # line 0 is NOT the question-start (damaged/trimmed region): let the
        # loop classify it — it may itself be a part marker (e.g. a question
        # whose stem page was rasterized, leaving only "(c) ..." fragments)
        start_idx = 0

    # inline "(a) ..." or "(a) (i) ..." on the question-number line
    if inline_rest:
        g = L1_RE.match(inline_rest)
        if g:
            cur_group = g.group(1)
            q["groups"][cur_group] = {"stem_lines": [], "parts": {}, "order": []}
            order.append(cur_group)
            rest = g.group(2).strip()
            r2 = L2_INLINE_RE.match(rest)
            if r2:
                cur_part = r2.group(1)
                q["groups"][cur_group]["parts"][cur_part] = {"lines": [r2.group(2)]}
                q["groups"][cur_group]["order"].append(cur_part)
            elif rest:
                q["groups"][cur_group]["stem_lines"].append(rest)
        else:
            q["stem_lines"].append(inline_rest)

    for ln in region_lines[start_idx:]:
        g = L1_RE.match(ln)
        r = L2_RE.match(ln)
        if g and not r:
            cur_group, cur_part = g.group(1), None
            q["groups"].setdefault(cur_group, {"stem_lines": [], "parts": {}, "order": []})
            if cur_group not in order:
                order.append(cur_group)
            rest = g.group(2).strip()
            r2 = L2_INLINE_RE.match(rest)
            if r2:
                cur_part = r2.group(1)
                q["groups"][cur_group]["parts"][cur_part] = {"lines": [r2.group(2)]}
                q["groups"][cur_group]["order"].append(cur_part)
            elif rest:
                q["groups"][cur_group]["stem_lines"].append(rest)
        elif r:
            if cur_group is None:  # roman without letter — attach to virtual group
                cur_group = "_"
                q["groups"].setdefault(cur_group, {"stem_lines": [], "parts": {}, "order": []})
                order.append(cur_group)
            cur_part = r.group(1)
            q["groups"][cur_group]["parts"][cur_part] = {"lines": [r.group(2)]}
            q["groups"][cur_group]["order"].append(cur_part)
        else:
            if cur_part is not None:
                q["groups"][cur_group]["parts"][cur_part]["lines"].append(ln)
            elif cur_group is not None:
                q["groups"][cur_group]["stem_lines"].append(ln)
            else:
                q["stem_lines"].append(ln)
    q["group_order"] = order
    return q


def finalize_part(lines):
    """Extract marks, MCQ choices, clean problem text from a part's raw lines."""
    lines = [l for l in lines if l.strip()]
    marks = None
    kept = []
    for ln in lines:
        mm = MARK_RE.match(ln)
        if mm and marks is None:
            marks = int(mm.group(1))
        else:
            kept.append(ln)
    source_norm = norm(" ".join(kept))   # verbatim ground truth BEFORE choice strip
    if marks is None:  # fallback: trailing "(n)"
        for ln in reversed(kept):
            tm = re.search(r"\((\d{1,2})\)\s*$", ln)
            if tm and not ln.strip().startswith(("A ", "B ", "C ", "D ")):
                marks = int(tm.group(1))
                kept[kept.index(ln)] = re.sub(r"\((\d{1,2})\)\s*$", "", ln).rstrip()
                break

    choices, consumed = parse_mcq_block(kept)
    if choices:
        kept = [ln for i, ln in enumerate(kept) if i not in consumed]
    source_norm = norm(strip_dotrun(" ".join(kept)))   # final ground truth (marks + options removed)

    text = strip_dotrun(re.sub(r"\s{2,}", " ", " ".join(kept))).strip()
    return {"marks": marks, "choices": choices, "problem_md": text, "source_norm": source_norm}


# ---------------------------------------------------------------- stage 3: MS linkage
MS_ROW_RE = re.compile(
    r"^ {0,20}(?:(\d{1,2})\s+)?(?:\(([a-h])\s*\)\s*)?(?:\((i{1,3}|iv|v|vi{1,3})\s*\)\s*)?(\S.*)$")
MS_MARKER_ONLY_RE = re.compile(
    r"^\s*(?:(\d{1,2})\s+)?(?:\(([a-h])\s*\))?\s*(?:\((i{1,3}|iv|v|vi{1,3})\s*\))?\s*$")
# some series (2019-06) print sub-letters bare without parentheses: "    b      they have..."
MS_BARE_LETTER_RE = re.compile(
    r"^ {0,20}(?:(\d{1,2})\s+)?([a-h])(?=\s{2,})\s*(.*)$")


def parse_ms(ms_lines):
    """Link MS rows positionally: rows carry qnum / letter / roman in any
    combination; absent components inherit from the previous row. Marker-only
    rows (e.g. a bare '(ii)' line) open an entry whose content starts on the
    next line. Returns key -> list of raw lines (per-line structure matters
    for MCQ keying: answer rows vs 'X is incorrect' note rows)."""
    entries = {}
    cur_q, cur_letter = None, None
    cur = None
    TOTAL_RE = re.compile(r"^\s*Total\s+\d+\s*$")
    for ln in ms_lines:
        if TOTAL_RE.match(ln):
            continue
        mo = MS_MARKER_ONLY_RE.match(ln)
        m = MS_ROW_RE.match(ln)
        mb = MS_BARE_LETTER_RE.match(ln)
        if mo and any(mo.groups()[:3]):
            qn, letter, roman = mo.group(1), mo.group(2), mo.group(3)
            if qn:
                cur_q = int(qn)
            if letter:
                cur_letter = letter
            cur = (cur_q, cur_letter, roman if roman else None)
            entries.setdefault(cur, [])
        elif mb:
            # bare-letter rows must win over MS_ROW_RE (whose groups are all
            # optional and therefore match almost any line)
            qn, letter, rest = mb.groups()
            if qn:
                cur_q = int(qn)
            cur_letter = letter
            roman = None
            r2 = L2_INLINE_RE.match(rest.strip())
            if r2:
                roman, rest = r2.group(1), r2.group(2)
            cur = (cur_q, cur_letter, roman)
            entries.setdefault(cur, [rest.strip()] if rest.strip() else [])
        elif m:
            qn, letter, roman, rest = m.groups()
            if any([qn, letter, roman]):
                if qn:
                    cur_q = int(qn)
                if letter:
                    cur_letter = letter
                cur = (cur_q, cur_letter, roman if roman else None)
                entries.setdefault(cur, [rest])
            elif cur is not None:
                entries[cur].append(ln)
        elif cur is not None:
            entries[cur].append(ln)
    return entries


# ---------------------------------------------------------------- v0.5: solution emission
# The reveal + Smart Mark layer: per-part solution_md (verbatim MS answer block)
# and mark_points[] (awardable points whose marks always sum to the part marks).
SOL_TAIL_MARKS_RE = re.compile(r"\s{2,}(\d{1,2})\s*$")   # marks-column digit, far right
TOTAL_ROW_RE = re.compile(r"^Total \d+$")
NOTES_COL_INDENT = 45   # answer-column content sits left of this in every observed table;
                        # the Notes column (ALLOW/ACCEPT/... + its M1/M2 cross-references)
                        # starts at col ~60+ — never confuse its M-rows for points


def build_solution(p, ms_lines, series):
    """v0.5: derive solution_md + mark_points[] from the linked MS entry.

    Verbatim doctrine: solution_md is every content line of the entry block,
    whitespace-normalized, with the marker row's trailing marks-column digit
    removed (it is layout, not answer). Nothing is added or reworded.

    mark_points[]: points are split ONLY on explicit ascending M1..Mn rows
    printed in the answer column (indent < NOTES_COL_INDENT), each worth 1,
    accepted only when n == the part's marks. Every other entry becomes ONE
    point carrying the whole block (marks = part marks). MCQ parts emit a
    single label-style point referencing the keyed choice. Fail-closed: the
    splitter can only under-split, never invent; unlinked parts emit nothing.
    Returns (solution_md, mark_points, ms_marks_digit_or_None)."""
    marks = p["marks"]
    lines = []                      # (raw indent, normalized text)
    ms_marks = None
    for ln in ms_lines:
        raw = ln.rstrip()
        if not raw.strip():
            continue
        tail = SOL_TAIL_MARKS_RE.search(raw)
        if tail and raw[:tail.start()].strip():
            if ms_marks is None:
                ms_marks = int(tail.group(1))
            raw = raw[:tail.start()].rstrip()
        text = re.sub(r"\s{2,}", " ", raw).strip()
        if not text or TOTAL_ROW_RE.match(text):
            continue
        lines.append((len(raw) - len(raw.lstrip()), text))
    if not lines:
        return None, None, None
    solution_md = "\n".join(t for _, t in lines)
    base = f"{series}-{p['part_number'].replace('(', '-').replace(')', '')}"
    pts = None
    if p["question_type"] == "multiple_choice":
        keyed = next((c for c in p.get("choices") or [] if c.get("is_correct")), None)
        if marks is not None:
            pts = [{"id": f"{base}-MP1", "marks": marks,
                    "text_md": (f"Answer {keyed['label']}: {keyed['text_md']}"
                                if keyed else solution_md)}]
    elif marks is not None:
        m_rows = [(k, m) for k, (ind, t) in enumerate(lines)
                  if ind < NOTES_COL_INDENT and (m := re.match(r"^M([1-9])\s+(\S.*)$", t))]
        nums = [int(m.group(1)) for _, m in m_rows]
        if m_rows and nums == list(range(1, len(nums) + 1)) and len(nums) == marks:
            pts = []
            for j, (k, m) in enumerate(m_rows):
                end = m_rows[j + 1][0] if j + 1 < len(m_rows) else len(lines)
                seg = [m.group(2)]
                seg += [t for ind, t in lines[k + 1:end]
                        if ind < NOTES_COL_INDENT and not re.match(r"^M[1-9]\s", t)]
                pts.append({"id": f"{base}-MP{j + 1}", "marks": 1,
                            "text_md": "\n".join(seg)})
        if pts is None:
            pts = [{"id": f"{base}-MP1", "marks": marks, "text_md": solution_md}]
    return solution_md, pts, ms_marks


# ---------------------------------------------------------------- v0.5: figure crop pass
# Turns the page-anchored crop-required stubs into real PNG crops rendered from
# the QP PDF. Detection is deterministic (vector-drawing + raster-image clusters);
# anything not provably a figure stays a stub and keeps its review-queue entry.
CROP_MIN_W, CROP_MIN_H = 40, 25          # figure-sized regions (pt)
CROP_PAD, CROP_DPI = 9.0, 150
FULL_PAGE_FRAC = 0.80                    # page-border frames cover ~100% -> rejected
ANSWER_STRIP_W, ANSWER_STRIP_H = 320, 55  # full-width ruled answer boxes are furniture
FOOTER_BAND = 80                         # pt: page-bottom band (barcode / Turn over) F18


def detect_figure_clusters(page):
    """Figure-sized regions on a QP page: vector-drawing rects (lines, curves,
    fills — apparatus diagrams, graphs, tables) plus embedded raster bboxes,
    union-merged with padding to fixpoint. Page furniture is removed BEFORE
    merging (printed page-border frames, margin decoration strips, full-height
    stripe images, full-page scans) because a frame at 79% page area survives
    any post-hoc area filter, margin stripe images sit close enough to merge
    with it, and a full-height 'DO NOT WRITE' stripe image bridges the border
    rules + answer rules + tables into one page-sized mega-cluster (F18: the
    2019-06 defect that left table pages with zero clusters). Horizontal
    ruling lines are zero-height rects — they ARE table strokes, so only
    truly zero-size artifacts are dropped here; answer-rule stacks that do
    merge are removed by the answer-strip filter. Post-merge filters: footer
    band (F18), figure minimum size, full-width ruled answer strips.
    Deterministic order."""
    pw, ph = page.rect.width, page.rect.height

    def furniture(r):
        if r.width >= 0.45 * pw and r.height >= 0.45 * ph:
            return True                      # page-border frame / full-page scan
        if r.height >= 0.5 * ph and r.width <= 60:
            return True                      # full-height margin stripe image (F18)
        if r.x1 <= 45 or r.x0 >= pw - 45 or r.y1 <= 30 or r.y0 >= ph - 30:
            return True                      # margin decorations / edge stripes
        return False

    seeds = []
    for d in page.get_drawings():
        r = fitz.Rect(d["rect"])
        if max(r.width, r.height) < 3 or furniture(r):
            continue
        seeds.append(r)
    for info in page.get_image_info():
        r = fitz.Rect(info["bbox"])
        if max(r.width, r.height) < 5 or furniture(r):
            continue
        seeds.append(r)
    if not seeds:
        return []
    page_area = abs(page.rect)
    boxes = [fitz.Rect(r.x0 - CROP_PAD, r.y0 - CROP_PAD, r.x1 + CROP_PAD, r.y1 + CROP_PAD)
             for r in seeds]
    merged = []
    for b in sorted(boxes, key=lambda r: (round(r.y0, 1), round(r.x0, 1))):
        hit_i = next((i for i, m in enumerate(merged) if m.intersects(b)), None)
        if hit_i is None:
            merged.append(fitz.Rect(b))
        else:
            merged[hit_i] = merged[hit_i] | b   # NOTE: Rect has no __ior__ — must rebind into the list
    for _ in range(10):                    # absorb merge chains to a fixpoint
        out, changed = [], False
        for b in merged:
            hit_i = next((i for i, m in enumerate(out) if m.intersects(b)), None)
            if hit_i is None:
                out.append(fitz.Rect(b))
            else:
                if not out[hit_i].contains(b):
                    out[hit_i] = out[hit_i] | b
                    changed = True
        merged = out
        if not changed:
            break
    # labelled fragments of one figure sit in a vertical stack (an 'eye' label
    # above the apparatus drawing) — merge pairs with strong x-overlap, a small
    # y-gap and real figure heights; answer-rule stacks (h <= 20) never qualify
    for _ in range(6):
        pairs = []
        for i in range(len(merged)):
            for j in range(i + 1, len(merged)):
                a_, b_ = merged[i], merged[j]
                if a_.height < 40 or b_.height < 40:
                    continue
                xov = min(a_.x1, b_.x1) - max(a_.x0, b_.x0)
                if xov < 0.4 * min(a_.width, b_.width):
                    continue
                gap = max(a_.y0, b_.y0) - min(a_.y1, b_.y1)
                if 0 <= gap <= 24:
                    pairs.append((i, j))
        if not pairs:
            break
        killed = set()
        for i, j in pairs:
            if i in killed or j in killed:
                continue
            merged[i] = merged[i] | merged[j]
            killed.add(j)
        merged = [m for k, m in enumerate(merged) if k not in killed]

    figs = []
    for m in merged:
        if abs(m) > FULL_PAGE_FRAC * page_area:
            continue
        if m.y0 >= ph - FOOTER_BAND:
            continue                         # footer band: barcode / Turn over / page number (F18)
        if m.width >= ANSWER_STRIP_W and m.height <= ANSWER_STRIP_H:
            continue
        if m.width < CROP_MIN_W or m.height < CROP_MIN_H:
            continue
        figs.append(m)
    return sorted(figs, key=lambda r: (round(r.y0), round(r.x0)))


def figure_anchor_y(page, problem_md):
    """Y position of the part's own text on the page (figures sit below it).
    Tries progressively shorter word prefixes because pdftotext and PyMuPDF
    disagree about spacing/punctuation. None = unanchorable -> review flag."""
    frag = re.sub(r"\s+", " ", problem_md).strip()
    words = frag.split()
    for n in (8, 6, 4, 3, 2):
        k = min(n, len(words))
        if k < 2:
            break
        hits = page.search_for(" ".join(words[:k]))
        if hits:
            return hits[0].y0
    return None


REF_PREPS = {"on", "from", "in", "of", "at", "than", "against"}


def noun_anchor_y(page, problem_md, noun):
    """F20/F22/F24: anchor candidates at EVERY figure-noun phrase of the part
    text, each with a direction. 'Complete the table' / 'The diagram shows'
    instruct -> the figure sits BELOW; 'on the diagram' / 'in apparatus X'
    refer -> the figure sits ABOVE. Returns [(y, below?), ...] in document
    order of the phrases. None when the noun is absent from the page text."""
    frag = re.sub(r"\s+", " ", problem_md).strip()
    occ = list(re.finditer(rf"\b{noun}s?\b", frag, re.I))
    if not occ:
        return None
    out = []
    for m in occ:
        ws = frag[:m.end()].split()[-6:]
        # direction: a sentence that OPENS with a prepositional phrase
        # ('On the grid, add ...') refers to a figure printed ABOVE; an
        # instruction sentence ('Plot the results on the grid.', 'Complete
        # the table ...') points at a figure printed BELOW (F24)
        sentence_start = max(frag.rfind(".", 0, m.start()), frag.rfind("!", 0, m.start())) + 1
        head = frag[sentence_start:m.start()].strip()
        below = True
        if head:
            hw = head.split()
            if len(hw) <= 2 and hw[0].lower() in REF_PREPS:
                below = False
        for n in (len(ws), 4, 3):
            if n < 2:
                break
            hits = page.search_for(" ".join(ws[-n:]))
            if hits:
                out.append((hits[-1].y1 if below else hits[-1].y0, below))
                break
    return out or None


PART_MARKER_RE = re.compile(r"^\(?[a-z]+\)?\s+\([ivx]+\)|^\([ivx]+\)|^\([a-z]+\)\s", re.I)
MARK_TAG_RE = re.compile(r"^\(\d+\)$")


def expand_with_labels(page, rect, exclude_frags=()):
    """Union the cluster with nearby text blocks that overlap a fixed +16pt
    ring around it — graph axis labels and chart annotations are TEXT sitting
    just outside the vector strokes, and belong to the figure. Only blocks
    overlapping the ring are absorbed (distant paragraph text is not).
    F22: blocks that sit ENTIRELY outside the pre-expansion rect and carry
    foreign text — the part's own question line, a neighbouring part's marker
    line, a bare mark tag — must never be absorbed: they are layout, not
    labels (the 2025-11 4(c)(i) defect where the crop swallowed '(i) Explain
    the mistake in the student's diagram.'). Axis labels under a graph don't
    match any exclusion and stay inside the crop."""
    ring = fitz.Rect(rect.x0 - 16, rect.y0 - 16, rect.x1 + 16, rect.y1 + 16) & page.rect
    inner = fitz.Rect(rect.x0 + 2, rect.y0 + 2, rect.x1 - 2, rect.y1 - 2)
    contain = fitz.Rect(rect.x0 - 66, rect.y0 - 66, rect.x1 + 66, rect.y1 + 66) & page.rect
    out = fitz.Rect(rect)
    frags = [norm(f)[:40] for f in exclude_frags if f]
    for b in page.get_text("blocks"):
        tb = fitz.Rect(b[:4])
        if tb.is_empty or not ring.intersects(tb):
            continue
        if not contain.contains(tb):
            continue             # a block reaching far beyond the figure is page
                                 # text, not a label (F22: whole-page text blocks)
        if inner.intersects(tb):
            out |= tb
            continue
        txt = norm(b[4] if len(b) > 4 else "")[:80]
        foreign = (MARK_TAG_RE.match(txt) or PART_MARKER_RE.match(txt)
                   or re.search(r"total for (question|paper)", txt)
                   or DOTRUN_RE.search(txt)          # printed answer-line dots
                   or any(f and f in txt for f in frags))
        if not foreign:
            out |= tb
    return out


def text_coverage(page, rect):
    """Fraction of the rect's area overlapped by text blocks — high values mean
    the region is mostly text (mis-detected cluster) and the crop needs eyes."""
    tot = 0.0
    for b in page.get_text("blocks"):
        inter = fitz.Rect(b[:4]) & rect
        if not inter.is_empty:
            tot += abs(inter)
    return round(min(1.0, tot / max(abs(rect), 1.0)), 3)


# ---------------------------------------------------- v0.6: mention semantics (F19)
# A figure noun in the part text is only a figure REFERENCE when at least one
# occurrence is not itself part of a non-figural phrase. "Periodic Table",
# "Draw a dot-and-cross diagram", "Sketch a labelled diagram", "use a diagram",
# "a piece of apparatus" and "set up the apparatus" describe tasks or common
# nouns, never a printed figure. Verbatim problem_md is untouched — this only
# gates asset creation, so spurious crop-required stubs never enter the queue.
MENTION_SUPPRESS_RE = {
    "table": [re.compile(r"periodic\s+table$", re.I)],
    "diagram": [re.compile(r"(?:use|draw|sketch)\s+(?:a\s+)?(?:labelled\s+)?(?:dot(?:-| )and( |-)cross\s+)?diagram$", re.I)],
    "apparatus": [re.compile(r"(?:piece\s+of|set\s+up\s+the)\s+apparatus$", re.I)],
}
MENTION_NOUNS = ("table", "diagram", "grid", "graph", "apparatus", "boxes")


def figure_mentions(problem_md):
    """Nouns of problem_md that refer to a printed figure (F19). A noun is
    suppressed only when EVERY occurrence sits inside a non-figural phrase.
    Scaffold exception: 'Draw a dot-and-cross diagram' with printed element
    tokens after it ('H C Cl H H', 'N N') refers to a real printed scaffold —
    the mention (and its stub) stays."""
    scaffold_re = re.compile(r"(?:\b(?:[HCNOF]|Cl|Br)\b[\s,]*){2,}")
    out = []
    for noun in MENTION_NOUNS:
        occ = list(re.finditer(rf"\b{noun}\b", problem_md, re.I))
        if not occ:
            continue
        ok = False
        for m in occ:
            head = problem_md[:m.end()]
            if any(p.search(head) for p in MENTION_SUPPRESS_RE.get(norm(noun), [])):
                continue
            ok = True
            break
        if not ok and noun == "diagram" and any(scaffold_re.search(problem_md[m.end():]) for m in occ):
            ok = True
        if ok:
            out.append(noun)
    return sorted(set(out))


# ---------------------------------------------------- v0.6: figure anaphora (F20)
# Backward references must RESOLVE to an already-rendered figure, never
# re-anchor to whatever drawing happens to sit below the sentence.
BACKREF_RE = re.compile(r"in part \(([a-z])\)", re.I)
NUMBERED_NOUN_RE = re.compile(r"\b(?:grid|table)\s+\d+", re.I)
# forward-introducing verbs: the figure the noun refers to is printed BELOW
# this sentence (the part's own page region) — own-page anchoring is correct.
FORWARD_RE = re.compile(r"^\s*(?:\(?[a-z]+\))?\s*(?:plot|draw|complete|add|label|sketch)\b", re.I)
# an in-text introduction ('The diagram shows ...', 'uses this apparatus')
# means the part itself introduces the figure — own-page anchoring, even
# though the sentence opens with a noun, not a verb (F20: 2019-06 9(b)).
INTRO_RE = re.compile(
    r"\b(?:the\s+|this\s+)?(?:table|diagram|grid|graph|apparatus|boxes)s?\s*\d?\s*"
    r"(?:shows?|gives?|represents?|lists?|displays?|is)\b"
    r"|\buses?\s+this\s+(?:table|diagram|grid|graph|apparatus|boxes)\b", re.I)


def resolve_first(problem_md, noun=None):
    """True when the part must RESOLVE an existing figure before any own-page
    anchoring: an explicit 'in part (x)' back-ref, a numbered figure
    ('grid 1', 'table 2'), or a backward reference ('Use the graph to...')
    with no introduction phrase. Forward-introducing verbs AND in-text
    introductions ('The diagram shows ...') keep the own-page-below anchor."""
    md = problem_md or ""
    if BACKREF_RE.search(md) or NUMBERED_NOUN_RE.search(md):
        return True
    if FORWARD_RE.match(md):
        return False
    if noun and INTRO_RE.search(md):
        return False
    return True


# ---------------------------------------------------------------- main
def main():
    import argparse, copy
    ap = argparse.ArgumentParser(description="ADR-037 official-paper question extractor")
    ap.add_argument("--series", default="2020-11",
                    help="paper series folder, e.g. 2020-11 (baseline), 2019-06, 2020-01, 2021-06, 2022-06, 2024-06")
    args = ap.parse_args()
    series = args.series
    P = paths_for(series)
    global QP_PDF, MS_PDF, QP_TXT, MS_TXT, MANIFEST, OUT
    QP_PDF, MS_PDF = P["qp_pdf"], P["ms_pdf"]
    QP_TXT, MS_TXT = P["qp_txt"], P["ms_txt"]
    MANIFEST, OUT = P["manifest"], P["out"]
    expect_q = EXPECT_QUESTIONS.get(series)

    report = {"schema": "syllabai.official-paper-questions.validation/0.1",
              "generated_utc": now_iso(), "series": series, "gates": [],
              "negative_controls": [], "review_queue": []}

    # ---- G0 identity -------------------------------------------------------
    manifest = yaml.safe_load(MANIFEST.read_text())
    qp_sha, ms_sha = sha256(QP_PDF), sha256(MS_PDF)
    mat = {m["type"]: m for m in manifest["materials"]}
    sha_ok = (qp_sha == mat["question-paper"]["sha256"] and
              ms_sha == mat["mark-scheme"]["sha256"])
    paper_id = manifest["paper_id"]
    report["gates"].append({
        "gate": "G0-identity", "status": "PASS" if sha_ok else "FAIL",
        "summary": f"paper_id={paper_id}; series={manifest['series']['normalized']}; "
                   f"printed={manifest['series'].get('printed', 'n/a (manifest schema v2 omits it)')!r}; sha256 qp/ms match manifest: {sha_ok}",
        "details": {"qp_sha256": qp_sha, "ms_sha256": ms_sha,
                    "registry_paper_id": paper_id}})
    if not sha_ok:
        print("G0 FAIL — aborting (fail-closed)"); json.dump(report, sys.stdout, indent=1); return 1

    qp_lines = clean_lines(QP_TXT.read_text(errors="replace"))
    footers = [(i, int(m.group(1)), int(m.group(2)))
               for i, ln in enumerate(qp_lines) if (m := FOOTER_RE.search(ln))]

    # ---- extraction --------------------------------------------------------
    # footer census: printed totals must exist for 1..N; a missing footer (seen in
    # 2019-06 Q7 — absent from the PDF text layer itself) splits the following
    # region into a footer-less question (marks inferred from parts -> REVIEW)
    footer_qnums = {q for _, q, _ in footers}
    max_q = max(footer_qnums)
    missing = [n for n in range(1, max_q + 1) if n not in footer_qnums]

    def emit_question(qnum, printed_total, region):
        seg = segment_question(qnum, [l for l in region if l.strip()])
        stem_md = re.sub(r"\s{2,}", " ", " ".join(seg["stem_lines"])).strip()
        questions_parts = []
        for gletter in seg["group_order"]:
            grp = seg["groups"][gletter]
            grp_stem = strip_dotrun(re.sub(r"\s{2,}", " ", " ".join(grp["stem_lines"])).strip())
            grp_choices, consumed = parse_mcq_block(
                [l for l in grp["stem_lines"]]) if not grp["parts"] else ([], set())
            option_list = [c["text_md"] for c in grp_choices] or None
            if not grp["order"]:
                # letter-group with no roman sub-parts: the group IS a part (e.g. 2(a), 7(d))
                p = finalize_part(grp["stem_lines"])
                questions_parts.append({
                    "part_number": f"{qnum}({gletter})",
                    "group": gletter, "roman": None,
                    "group_stem_md": None, "option_list": None,
                    "marks": p["marks"],
                    "question_type": "multiple_choice" if p["choices"] else "structured",
                    "problem_md": p["problem_md"], "choices": p["choices"],
                    "source_norm": p["source_norm"],
                })
                continue
            for roman in grp["order"]:
                p = finalize_part(grp["parts"][roman]["lines"])
                part_number = f"{qnum}({gletter})({roman})" if gletter != "_" else f"{qnum}({roman})"
                questions_parts.append({
                    "part_number": part_number,
                    "group": gletter, "roman": roman,
                    "group_stem_md": grp_stem or None, "option_list": option_list,
                    "marks": p["marks"], "question_type": "multiple_choice" if p["choices"] else "structured",
                    "problem_md": p["problem_md"], "choices": p["choices"],
                    "source_norm": p["source_norm"],
                })
        doc_questions.append({"question_number": qnum, "printed_total": printed_total,
                              "stem_md": stem_md, "parts": questions_parts,
                              "region_norm": norm(" ".join(region))})

    doc_questions = []
    prev = 0
    for fi, (idx, qnum, qtotal) in enumerate(footers):
        region = qp_lines[prev + 1 if fi else 0:idx]
        prev = idx
        # start lines for this question and for any missing questions whose body
        # lives inside this region (their footer was dropped by the archive PDF)
        pieces = []
        for m in missing:
            ms_ = [i for i, ln in enumerate(region)
                   if QSTART_RE.match(ln) and int(QSTART_RE.match(ln).group(1)) == m]
            if ms_:
                pieces.append((m, ms_[-1], None))
        cur = [i for i, ln in enumerate(region)
               if QSTART_RE.match(ln) and int(QSTART_RE.match(ln).group(1)) == qnum]
        pieces.append((qnum, cur[-1] if cur else 0, qtotal))
        pieces.sort(key=lambda t: t[1])
        for k, (qn, st, pt) in enumerate(pieces):
            end = pieces[k + 1][1] if k + 1 < len(pieces) else len(region)
            emit_question(qn, pt, region[st:end])
    doc_questions.sort(key=lambda q: q["question_number"])

    # ---- MS linkage + MCQ keys ---------------------------------------------
    ms_entries = parse_ms(clean_lines(MS_TXT.read_text(errors="replace")))
    for q in doc_questions:
        for p in q["parts"]:
            key = (q["question_number"], p["group"], p["roman"])
            lines = ms_entries.get(key, [])
            raw = re.sub(r"\s{2,}", " ", " ".join(lines)).strip()
            p["answer_status"] = "linked" if raw else "unmatched"
            p["answer_raw"] = raw
            if p["question_type"] == "multiple_choice" and raw:
                labels = {c["label"] for c in p["choices"]}
                # candidate answer rows: "<Letter> <text>" lines that are NOT
                # "X is incorrect ..." note rows (Edexcel MS layout drifts its
                # marker column one row early in some series, so notes leak in;
                # key only when the entry shows exactly ONE distinct candidate)
                ans, positives, rebut, ansrow = [], [], {}, {}
                for ln in lines:
                    s = re.sub(r"^\s*\d{1,2}\s+(?=[A-E]\b)", "", ln)   # glued marks digit
                    m = re.match(r"^\s*([A-E])\s+\S", s)
                    g = re.match(r"^\s*([A-E])(?=[0-9(])", s)   # glued answer cell: 'B4', 'D(NH4+)'
                    pos = re.search(r"(?<![A-Za-z])([A-E])\s+is\s+(?:the\s+)?correct\b", s)
                    if pos and pos.group(1) in labels:
                        positives.append(pos.group(1))
                    hit = m or g
                    if hit and hit.group(1) in labels:
                        # rebuttal row: an option letter followed by negative text
                        # ('A is incorrect ...', 'B is not the formula ...',
                        #  'C the charges are incorrect', 'B is X incorrect ...')
                        if re.search(r"\bis\s+not\b|\bare\s+not\b|\b(?:is|are)\s+(?:\w+\s+)?incorrect\b", s):
                            rebut[hit.group(1)] = rebut.get(hit.group(1), 0) + 1
                        else:
                            ans.append(hit.group(1))
                            ansrow[hit.group(1)] = ansrow.get(hit.group(1), 0) + 1
                    elif s.strip() in labels:
                        ans.append(s.strip())
                        ansrow[s.strip()] = ansrow.get(s.strip(), 0) + 1
                # a printed '<L> is the correct answer ...' statement is
                # authoritative: key it even if stray note-drift letters leaked in
                lab = (positives[0] if len(set(positives)) == 1 else
                       (ans[0] if len(set(ans)) == 1 else None))
                # elimination keying (F14): entries whose MS prints an explicit
                # rebuttal for every option except the correct one — key the sole
                # un-rebutted option ONLY when corroborated by exactly one answer
                # row; anything else stays unkeyed for human review
                if lab is None:
                    clean = [L for L in sorted(labels) if L not in rebut]
                    if len(clean) == 1 and clean[0] in ansrow and len(ansrow) == 1:
                        lab = clean[0]
                if lab is None and not re.search(r"\bis\s+(?:not\s+(?:the\s+)?)?correct\b|\bis\s+incorrect\b", raw):
                    # letters fallback ONLY on note-free entries (a greedy note-strip
                    # can swallow an adjacent answer row and yield a wrong key)
                    letters = set(re.findall(r"(?<![A-Za-z])([A-D])(?![A-Za-z])", raw))
                    if len(letters) == 1:
                        lab = letters.pop()
                if lab:
                    for c in p["choices"]:
                        c["is_correct"] = (c["label"] == lab)
            # v0.5 solution emission (reveal + Smart Mark): verbatim MS block +
            # awardable points; unlinked parts emit nothing (fields stay None)
            p["solution_md"], p["mark_points"], p["_ms_marks"] = build_solution(p, lines, series)

    # ---- page anchoring + assets -------------------------------------------
    pdf = fitz.open(QP_PDF)
    page_norm = [norm(pg.get_text()) for pg in pdf]
    # source-defect census: rasterized pages carry no text layer (seen in 2019-06:
    # 8 image-only pages; Q7 lost entirely, Q1/Q11/Q12/Q13/Q15 partly)
    IMG_ONLY_CHARS = 40
    image_only_pages = [i + 1 for i, pg in enumerate(pdf) if len(pg.get_text().strip()) < IMG_ONLY_CHARS]
    footer_page = {}
    for i, pg in enumerate(pdf):
        t = pg.get_text()
        for m in FOOTER_RE.finditer(t):
            footer_page.setdefault(int(m.group(1)), i + 1)
    # only content pages matter for defect attribution (covers are routinely rasterized);
    # allow up to 3 pages before the first footer (a question's first page precedes its footer)
    first_q_page = min(footer_page.values()) if footer_page else 1
    content_img_pages = [p for p in image_only_pages if p >= max(3, first_q_page - 3)]
    MENTION_RE = re.compile(r"\b(table|diagram|grid|graph|apparatus|boxes)\b", re.I)
    for q in doc_questions:
        for p in q["parts"]:
            # progressive-length anchoring: a 38-char fragment can collide with
            # an identical sibling wording (2019-06 Q9(b) 'The diagram shows the
            # displayed formula ...' also opens Q8(c) — the collision anchored
            # Q9(b) to page 13 and its figure on page 14 was never found). The
            # shortest fragment that matches EXACTLY ONE page wins (F18b).
            frag = norm(re.sub(r"^[()a-ziv ]+", "", p["problem_md"]))[:110]
            src_page = None
            for n in (38, 60, 90, 110):
                probe = frag[:n]
                if not probe:
                    break
                pages = [i + 1 for i, t in enumerate(page_norm) if probe in t]
                if len(pages) == 1:
                    src_page = pages[0]
                    break
                if pages and src_page is None:
                    src_page = pages[0]
                if len(probe) < n:        # fragment exhausted (short problem_md)
                    break
            p["source_page"] = src_page
            mentions = figure_mentions(p["problem_md"])       # F19-suppressed
            p["assets"] = [{"id": f"asset_{p['part_number'].replace('(', '_').replace(')', '')}_{k}",
                            "kind": "crop-required", "mention": k,
                            "source": "qp.pdf", "page": p["source_page"], "review": True}
                           for k in mentions]

    # ---- v0.6 figure crop pass ----------------------------------------------
    # Resolution order per mention (fail-closed; anything unresolved stays a
    # crop-required stub in the review queue):
    #   1. explicit back-ref 'on the grid in part (a)'  -> shared ref (F20)
    #   2. backward reference ('Use the graph to...', no intro phrase) resolves
    #      a figure introduced earlier BEFORE any own-page anchoring — the
    #      2021-01 10(a)(iii) defect class (a wrong nearest-below crop):
    #      2a. stem / group-stem figure intro 'The graph shows ...' -> one lazy
    #          stem crop shared by every referencing part (F21)
    #      2b. sibling part crop for the same figure class -> shared ref (F20)
    #      2c. adjacent page anchored on the group stem -> crop, review (F23)
    #   3. forward introduction ('Plot ... on the grid', 'The diagram shows ...')
    #      -> own-page cluster below the part's text (v0.5 behaviour, now with
    #      F18 furniture filters and F22 foreign-text exclusion)
    #   4. forward with no own-page cluster -> adjacent page (F23)
    #   5. unresolved -> crop-required stub (honest, review queue)
    ASSETS_DIR = OUT / "assets"
    ASSETS_DIR.mkdir(parents=True, exist_ok=True)
    page_clusters, page_rasters = {}, {}
    claimed = {}                       # page -> {cluster_index: question_number} (F24)
    crop_stats = {"crops": 0, "pending": 0, "shared": 0}
    stem_assets = {}                     # (qnum, group, noun) -> asset (F21 lazy)

    FIG_CLASS = {"graph": "plot", "grid": "plot", "table": "table",
                 "diagram": "figure", "apparatus": "figure", "boxes": "figure"}
    CLASS_NOUN_RE = {c: re.compile(rf"\b({'|'.join(sorted(n for n, k in FIG_CLASS.items() if k == c))})s?\b", re.I)
                     for c in set(FIG_CLASS.values())}

    # group stems live on the parts during extraction (q['groups'] is attached
    # to the serialized topic only) — build the per-question view now so the
    # stem-figure / adjacent-page lookups can see them
    for q in doc_questions:
        q["groups"] = {}
        for p in q["parts"]:
            if p.get("group_stem_md"):
                q["groups"].setdefault(p["group"], {})["group_stem_md"] = p["group_stem_md"]

    def clusters_for(pg):
        if pg not in page_clusters:
            page = pdf[pg - 1]
            page_clusters[pg] = detect_figure_clusters(page)
            page_rasters[pg] = [fitz.Rect(i["bbox"]) for i in page.get_image_info()
                                if i["bbox"][2] - i["bbox"][0] >= 5
                                and i["bbox"][3] - i["bbox"][1] >= 5]
        return page_clusters[pg]

    def render_crop(pg, cluster, a, ay):
        page = pdf[pg - 1]
        c = expand_with_labels(page, cluster, exclude_frags=a.get("_src_text") or [])
        clip = fitz.Rect(c.x0 - 3, c.y0 - 3, c.x1 + 3, c.y1 + 3) & page.rect
        pix = page.get_pixmap(clip=clip, dpi=CROP_DPI)
        rel = f"assets/{a['id']}.png"
        pix.save(str(OUT / rel))
        cov = text_coverage(page, c)
        a["kind"] = "crop"
        a["path"] = rel
        a["page"] = pg
        a["render"] = ("raster" if any(rb.contains(c) for rb in page_rasters[pg])
                       else "vector")
        a["text_coverage"] = cov
        a["review"] = bool(ay is None or cov > 0.55)
        crop_stats["crops"] += 1

    def page_of_text(text):
        frag = norm(re.sub(r"\s+", " ", text))[:110]
        probes, seen = [], set()
        for n in (60, 38, 110):
            probe = frag[:n]
            if len(probe) < 20 or probe in seen:
                continue
            seen.add(probe)
            pages = [i + 1 for i, t in enumerate(page_norm) if probe in t]
            if pages:
                return pages[0]
        return None

    def group_letter(p):
        m = re.match(r"\d+\(([a-z])\)", p["part_number"])
        return m.group(1) if m else None

    def stem_figure(q, p, noun):
        """F21: crop the figure a question/group stem introduces ('The graph
        shows ...', 'uses this apparatus', 'Grid 2 shows ...'), once per
        (question, group, noun). Returns the asset dict or None."""
        group = group_letter(p)
        key = (q["question_number"], group, noun)
        if key in stem_assets:
            return stem_assets[key]
        cls = FIG_CLASS[noun]
        stems = []
        g = (q.get("groups") or {}).get(group) if group else None
        if g and g.get("group_stem_md"):
            stems.append(g["group_stem_md"])
        for letter, gg in sorted((q.get("groups") or {}).items()):
            if letter != group and gg.get("group_stem_md"):
                stems.append(gg["group_stem_md"])
        if q.get("stem_md"):
            stems.append(q["stem_md"])
        # intro sentences often glue into the first part's problem_md when the
        # group stays inline — earlier siblings are legitimate introductions
        for pp in q["parts"]:
            if pp is p:
                break
            if pp.get("problem_md"):
                stems.append(pp["problem_md"])
        a = None
        cnre = CLASS_NOUN_RE[FIG_CLASS[noun]]
        for st in stems:
            sent = next((s for s in re.split(r"(?<=[.!?])\s+", st)
                         if cnre.search(s)), None)
            if not sent:
                continue
            pg = page_of_text(sent)
            if pg is None:
                continue
            page = pdf[pg - 1]
            ay = figure_anchor_y(page, sent)
            used = claimed.setdefault(pg, {})
            cand = [(i, c) for i, c in enumerate(clusters_for(pg))
                    if used.get(i) in (None, q["question_number"])]
            pick = None
            if ay is not None:
                below = sorted(((abs(c.y0 - ay), i, c) for i, c in cand
                                if c.y0 >= ay - 36), key=lambda t: (t[0], t[1]))
                pick = below[0] if below else None
            if pick is None:
                continue
            _, i, c = pick
            used[i] = q["question_number"]
            aid = f"asset_{q['question_number']}_{group or 'q'}_{noun}_stem"
            a = {"id": aid, "kind": "crop-required", "mention": noun,
                 "source": "qp.pdf", "page": pg, "review": True,
                 "_src_text": [sent, p.get("problem_md") or ""]}
            render_crop(pg, c, a, ay)
            a["review"] = True          # stem-anchored: verify target choice
            break
        stem_assets[key] = a
        return a

    def sibling_crop(q, p, noun):
        """F20: nearest preceding sibling part owning a REAL crop of the same
        figure class ('graph'/'grid' both resolve to a plotting surface)."""
        cls = FIG_CLASS[noun]
        best = None
        for pp in q["parts"]:
            if pp is p:
                break
            for aa in pp.get("assets") or []:
                if (aa.get("kind") == "crop" and aa.get("mention") in FIG_CLASS
                        and FIG_CLASS[aa["mention"]] == cls and not aa.get("ref_part")):
                    best = aa
        return best

    def adjacent_crop(q, p, a):
        """F23: the figure lives on a neighbouring page (a part continued from
        its group's previous page). Anchor on the group stem, else the question
        stem, and claim the nearest cluster below it. Always review-flagged."""
        group = group_letter(p)
        stems = []
        g = (q.get("groups") or {}).get(group) if group else None
        if g and g.get("group_stem_md"):
            stems.append(g["group_stem_md"])
        if q.get("stem_md"):
            stems.append(q["stem_md"])
        pg = p.get("source_page")
        for pg2 in (pg - 1, pg + 1) if pg else ():
            if not (1 <= pg2 <= len(pdf)) or pg2 in content_img_pages:
                continue
            page = pdf[pg2 - 1]
            ay = None
            cnre2 = CLASS_NOUN_RE[FIG_CLASS[a["mention"]]]
            for st in stems:
                sent = next((s for s in re.split(r"(?<=[.!?])\s+", st)
                             if cnre2.search(s)), st)
                ay = figure_anchor_y(page, sent)
                if ay is not None:
                    break
            used = claimed.setdefault(pg2, {})
            cand = [(i, c) for i, c in enumerate(clusters_for(pg2))
                    if used.get(i) in (None, q["question_number"])]
            if not cand:
                continue
            if ay is not None:
                below = sorted(((abs(c.y0 - ay), i, c) for i, c in cand
                                if c.y0 >= ay - 36), key=lambda t: (t[0], t[1]))
            else:
                # no stem anchor on this page: take the single unambiguous
                # figure only — never guess between several (F23)
                below = [(0,) + cand[0]] if len(cand) == 1 else []
            if not below:
                continue
            _, i, c = pick = below[0]
            used[i] = q["question_number"]
            render_crop(pg2, c, a, ay)
            a["review"] = True
            return True
        return False

    def share_ref(a, target, how):
        a["kind"] = "crop"
        a["path"] = target["path"]
        a["page"] = target.get("page")
        a["render"] = target.get("render")
        a["text_coverage"] = target.get("text_coverage")
        a["shared"] = True
        a["ref_part"] = target.get("_owner") or target.get("id")
        a["review"] = False
        crop_stats["shared"] += 1

    def own_page_pick(q, p, a, force_review, allow_single=True):
        """Own-page resolution shared by forward introductions and the
        backward-rescue path. Anchors at EVERY noun phrase with its direction
        (instructions point DOWN at the figure, references point UP), tries
        them last-first, then part-start, then — forward only — the
        unambiguous single cluster. Clusters claimed by the SAME question may
        be reused (shared=true); clusters claimed by another question are
        never taken (F24: the 2025-06/2021-01 page-mate theft)."""
        noun = a["mention"]
        pg = p.get("source_page")
        if pg is None:
            return False
        page = pdf[pg - 1]
        used = claimed.setdefault(pg, {})
        cand = [(i, c) for i, c in enumerate(clusters_for(pg))
                if used.get(i) in (None, q["question_number"])]
        if not cand:
            return False
        anchors = noun_anchor_y(page, p["problem_md"], noun) or []
        start_ay = figure_anchor_y(page, p["problem_md"])
        if start_ay is not None:
            anchors.append((start_ay, True))
        for ay, below in anchors:
            if below:
                scored = sorted(((min(abs(c.y0 - ay), abs((c.y0 + c.y1) / 2 - ay)), i, c)
                                 for i, c in cand if c.y0 >= ay - 36),
                                key=lambda t: (t[0], t[1]))
            else:
                scored = sorted(((min(abs(c.y1 - ay), abs((c.y0 + c.y1) / 2 - ay)), i, c)
                                 for i, c in cand if c.y1 <= ay + 36),
                                key=lambda t: (t[0], t[1]))
            if scored:
                _, i, c = scored[0]
                shared = used.get(i) == q["question_number"]
                used[i] = q["question_number"]
                p["_owner"] = p["part_number"]
                render_crop(pg, c, a, ay if below else None)
                a["shared"] = shared
                if shared or force_review:
                    a["review"] = True
                else:
                    a["_owner"] = p["part_number"]
                return True
        if len(cand) == 1 and not force_review and allow_single:
            # forward introduction on a page with exactly one figure: unambiguous
            i, c = cand[0]
            shared = used.get(i) == q["question_number"]
            used[i] = q["question_number"]
            p["_owner"] = p["part_number"]
            render_crop(pg, c, a, None)
            a["shared"] = shared
            a["review"] = True          # no anchor evidence -> verify
            return True
        return False

    for q in doc_questions:
        for p in q["parts"]:
            p["_owner"] = None
            pmd = p["problem_md"] or ""
            for a in p.get("assets") or []:
                a["_src_text"] = [pmd]
                noun = a["mention"]
                pg = p.get("source_page")
                # 0. dot-and-cross draw prompts: the printed scaffold is
                # text-only, so no vector region exists — honest stub (F19b)
                if (noun == "diagram" and re.search(r"dot.{0,3}and.{0,3}cross", pmd, re.I)
                        and not INTRO_RE.search(pmd)):
                    crop_stats["pending"] += 1
                    continue
                # 1. explicit 'in part (x)' back-reference
                bm = BACKREF_RE.search(pmd)
                if bm:
                    letter = bm.group(1)
                    tgt = next((pp for pp in q["parts"]
                                if pp["part_number"].startswith(f"{q['question_number']}({letter})")
                                and pp is not p), None)
                    if tgt:
                        resolved = next((aa for aa in (tgt.get("assets") or [])
                                         if aa.get("kind") == "crop"
                                         and FIG_CLASS.get(aa.get("mention")) == FIG_CLASS[noun]), None)
                        if resolved:
                            share_ref(a, resolved, "backref")
                            continue
                backward = resolve_first(pmd, noun) and not BACKREF_RE.search(pmd)
                if backward:
                    # 2a. stem / group-stem figure
                    sa = stem_figure(q, p, noun)
                    if sa:
                        share_ref(a, sa, "stem")
                        continue
                    # 2b. sibling crop
                    sc = sibling_crop(q, p, noun)
                    if sc:
                        share_ref(a, sc, "sibling")
                        continue
                    # 2c. adjacent page (a stem-anchored neighbour figure is
                    # more trustworthy than an own-page guess)
                    if adjacent_crop(q, p, a):
                        continue
                    # 2d. own-page rescue (review-flagged: a backward reference
                    # that found nothing earlier may still sit above its figure
                    # — the 10(a)(iii) trap — so the pick is always verified)
                    if own_page_pick(q, p, a, force_review=True):
                        continue
                    crop_stats["pending"] += 1
                    continue
                # 3. forward introduction: own-page cluster below the part text
                if own_page_pick(q, p, a, force_review=False, allow_single=False):
                    continue
                # 3b. the page's figure was already claimed by a sibling part
                # (two parts share one grid) -> shared reference
                sc = sibling_crop(q, p, noun)
                if sc:
                    share_ref(a, sc, "sibling")
                    continue
                # 3c. unambiguous single figure on the page (no anchor hit)
                if own_page_pick(q, p, a, force_review=False, allow_single=True):
                    continue
                # 4. forward with no own-page cluster: adjacent page
                if adjacent_crop(q, p, a):
                    continue
                # 5. honest stub
                crop_stats["pending"] += 1
        # mark owners of real crops for share_ref bookkeeping (stem crops are
        # question-level figures — they keep their own id as the ref target)
        for p in q["parts"]:
            for a in p.get("assets") or []:
                if (a.get("kind") == "crop" and not a.get("ref_part")
                        and not a["id"].endswith("_stem") and not a.get("_owner")):
                    a["_owner"] = p["part_number"]

    # ---- spec seeds (labels only; registry-validated) -----------------------
    seeds = SEEDS.get(series, {})
    reg = json.loads(SPEC_RESOLUTION.read_text())["resolved"]
    registry = set()
    for r in reg:
        if r.get("resolved_code"):
            registry.add(r["resolved_code"])
    for q in doc_questions:
        for p in q["parts"]:
            code = seeds.get(p["part_number"])
            if code:
                p["spec_point_codes"] = [code]
                p["tagging"] = "seed-demo"
                if code not in registry:
                    p["tagging"] = "registry-gap-review"
                    report["review_queue"].append({"part": p["part_number"], "reason": f"spec code {code} not in registry (gap or invalid) — human decision"})
            else:
                p["spec_point_codes"] = []
                p["tagging"] = "pending-llm"
    # ---- gates ---------------------------------------------------------------
    def gate(name, ok, summary, details=None):
        report["gates"].append({"gate": name, "status": "PASS" if ok else "FAIL",
                                "summary": summary, "details": details or {}})
        return ok

    # G1 structure: marks invariant (fail-closed; source defects -> REVIEW, parser bugs -> FAIL)
    # attribution: a mismatch/missing question is a SOURCE defect when an image-only
    # page (no text layer) sits inside or immediately before the question's pages.
    footer_gaps = []
    defective = set()
    emitted_qnums = {q["question_number"] for q in doc_questions}
    for m in missing:
        if m in emitted_qnums:
            continue                      # split succeeded; inferred total handled below
        prev_p = max((footer_page[q] for q in footer_page if q < m), default=0)
        next_p = min((footer_page[q] for q in footer_page if q > m), default=10**6)
        lost_pages = [p for p in content_img_pages if prev_p < p < next_p]
        footer_gaps.append({"question": m,
                            "reason": (f"footer absent in source PDF; question not extractable — "
                                       f"image-only page(s) {lost_pages} in archive PDF (content lost at scan)"
                                       if lost_pages else
                                       "footer absent in source PDF and no start line found — needs human split"),
                            "attributed": bool(lost_pages)})
        if lost_pages:
            defective.add(m)

    g1_bad = []
    inferred_totals = {}
    for q in doc_questions:
        ssum = sum(p["marks"] or 0 for p in q["parts"])
        if q["printed_total"] is None:
            inferred_totals[q["question_number"]] = ssum
        elif ssum != q["printed_total"]:
            g1_bad.append({"question": q["question_number"], "parts_sum": ssum, "printed": q["printed_total"]})
    # attribute mismatches to image-only pages within [min_part_page-2, max_part_page]
    for mrec in g1_bad:
        q = next(x for x in doc_questions if x["question_number"] == mrec["question"])
        pages = [p["source_page"] for p in q["parts"] if p.get("source_page")]
        if pages:
            lost = [p for p in content_img_pages if min(pages) - 2 <= p <= max(pages)]
        else:   # no anchored parts (heavily damaged question) — use neighbour footer window
            prev_p = max((footer_page[qq] for qq in footer_page if qq < mrec["question"]), default=0)
            next_p = min((footer_page[qq] for qq in footer_page if qq > mrec["question"]), default=10**6)
            lost = [p for p in content_img_pages if prev_p <= p <= next_p]
        if lost:
            mrec["attributed_to_image_only_pages"] = lost
            defective.add(mrec["question"])
    unattributed_bad = [m for m in g1_bad if "attributed_to_image_only_pages" not in m]
    total = sum(q["printed_total"] if q["printed_total"] is not None
                else inferred_totals[q["question_number"]] for q in doc_questions)
    count_ok = (expect_q is None) or (len(doc_questions) == expect_q)
    for g in footer_gaps:
        report["review_queue"].append({"part": f"Q{g['question']}", "reason": g["reason"]})
    g1_ok = not g1_bad and not footer_gaps and total == PAPER_TOTAL and count_ok
    g1_review = (not g1_ok) and not unattributed_bad and all(g["attributed"] for g in footer_gaps)
    report["gates"].append({
        "gate": "G1-structure", "status": "PASS" if g1_ok else ("REVIEW" if g1_review else "FAIL"),
        "summary": (f"{len(doc_questions)} questions; Σ question totals={total}/{PAPER_TOTAL}; "
                    f"parts-sum == printed total for all questions: {not g1_bad}"
                    if not footer_gaps and not inferred_totals else
                    f"{len(doc_questions)} questions extracted; Σ known totals={total}/{PAPER_TOTAL}; "
                    f"source defects: missing Q{sorted(defective)} (image-only pages "
                    f"{content_img_pages} in archive PDF) — lost content needs human/OCR re-ingest"),
        "details": {"mismatches": g1_bad, "unattributed": unattributed_bad,
                    "inferred_totals": inferred_totals, "footer_gaps": footer_gaps,
                    "image_only_pages": content_img_pages, "count_expected": expect_q}})
    if defective or content_img_pages:
        report["source_defects"] = {"image_only_pages": content_img_pages,
                                    "affected_questions": sorted(defective)}

    # G2 verbatim — emitted text vs the source lines it claims to be copied from
    g2_bad, g2_ratios = [], {}
    for q in doc_questions:
        for p in q["parts"]:
            grams = ngrams(p["problem_md"])
            if not grams:
                continue
            src_grams = ngrams(p["source_norm"])
            ratio = sum(1 for g in grams if g in src_grams) / len(grams)
            g2_ratios[p["part_number"]] = round(ratio, 4)
            if ratio < 0.95:
                g2_bad.append({"part": p["part_number"], "ratio": round(ratio, 4)})
    gate("G2-verbatim", not g2_bad,
         f"5-gram overlap vs source region ≥0.95 for all {len(g2_ratios)} parts: {not g2_bad}",
         {"violations": g2_bad, "min_ratio": min(g2_ratios.values()) if g2_ratios else None})

    # G3 MCQ integrity
    mcq = [p for q in doc_questions for p in q["parts"] if p["question_type"] == "multiple_choice"]
    g3_issues = []
    for p in mcq:
        labels = [c["label"] for c in p["choices"]]
        if labels != ["A", "B", "C", "D"]:
            g3_issues.append({"part": p["part_number"], "issue": f"labels={labels}"})
        if not any(c.get("is_correct") for c in p["choices"]):
            g3_issues.append({"part": p["part_number"], "issue": "no keyed correct choice"})
            report["review_queue"].append({"part": p["part_number"], "reason": "MCQ key unresolved from MS"})
    gate("G3-mcq-integrity", not g3_issues,
         f"{len(mcq)} MCQ parts; all have printed A–D and MS-keyed answer: {not g3_issues}",
         {"issues": g3_issues})

    # G4 figure resolution
    dangling = [{"part": p["part_number"]} for q in doc_questions for p in q["parts"]
                if figure_mentions(p["problem_md"]) and not p["assets"]]
    n_assets = sum(len(p["assets"]) for q in doc_questions for p in q["parts"])
    n_unanchored = sum(1 for q in doc_questions for p in q["parts"] if p["source_page"] is None)
    gate("G4-figure-resolution", not dangling,
         f"{n_assets} asset records cover every table/diagram/grid/apparatus mention: "
         f"{crop_stats['crops']} cropped to assets/*.png ({CROP_DPI} dpi), "
         f"{crop_stats['pending']} remain crop-required; "
         f"{n_unanchored} parts without page anchor",
         {"dangling": dangling, "pages_unanchored": n_unanchored, "crop_stats": crop_stats})
    for q in doc_questions:
        for p in q["parts"]:
            for a in p.get("assets") or []:
                if a.get("kind") == "crop":
                    if a.get("review"):
                        report["review_queue"].append(
                            {"part": p["part_number"],
                             "reason": f"figure crop emitted — human verify ({a['path']})"})
                else:
                    report["review_queue"].append(
                        {"part": p["part_number"],
                         "reason": f"figure crop required ({a['mention']}, page {a.get('page')})"})

    # G5 answer linkage
    parts_all = [p for q in doc_questions for p in q["parts"]]
    linked = sum(1 for p in parts_all if p["answer_status"] == "linked")
    cov = linked / len(parts_all)
    status = "PASS" if cov >= 0.8 else ("REVIEW" if cov >= 0.5 else "FAIL")
    unmatched = [p["part_number"] for p in parts_all if p["answer_status"] != "linked"]
    report["gates"].append({"gate": "G5-answer-linkage", "status": status,
                            "summary": f"MS linkage {linked}/{len(parts_all)} ({cov:.0%})",
                            "details": {"unmatched": unmatched}})
    report["review_queue"].extend([{"part": pn, "reason": "answer not auto-linked to MS"} for pn in unmatched])

    # G6 registry codes — documented registry gaps go to REVIEW; unknown codes FAIL
    ALLOWED_GAPS = {"4CH1-3.15C"}   # chemistry-only rates practical; SME notes corpus lacks it
    g6_bad = []
    for q in doc_questions:
        for p in q["parts"]:
            for c in p["spec_point_codes"]:
                if c not in registry and c not in ALLOWED_GAPS:
                    g6_bad.append({"part": p["part_number"], "code": c})
    n_pending = sum(1 for p in parts_all if p["tagging"] == "pending-llm")
    gate("G6-registry-codes", not g6_bad,
         f"all emitted codes ∈ spec_point_resolution registry ({len(registry)} codes) "
         f"or documented gaps→review; {n_pending} parts pending-llm tagging",
         {"violations": g6_bad, "allowed_gaps": sorted(ALLOWED_GAPS)})

    # G7 solution emission (v0.5): every linked part carries the verbatim MS
    # block, and every mark_points split sums exactly to the part's marks.
    sol_parts = [p for p in parts_all if p.get("answer_status") == "linked"]
    no_sol = [p["part_number"] for p in sol_parts if not p.get("solution_md")]
    sum_bad = []
    for p in parts_all:
        mp = p.get("mark_points")
        if mp and p.get("marks") is not None and sum(x["marks"] for x in mp) != p["marks"]:
            sum_bad.append({"part": p["part_number"],
                            "points_sum": sum(x["marks"] for x in mp), "marks": p["marks"]})
    ms_seen = sum(1 for p in parts_all
                  if p.get("_ms_marks") is not None and p.get("marks") is not None)
    ms_agree = sum(1 for p in parts_all
                   if p.get("_ms_marks") is not None and p.get("marks") is not None
                   and p["_ms_marks"] == p["marks"])
    ms_disagree = [f"{p['part_number']} (ms={p['_ms_marks']} qp={p['marks']})"
                   for p in parts_all
                   if p.get("_ms_marks") is not None and p.get("marks") is not None
                   and p["_ms_marks"] != p["marks"]]
    gate("G7-solution-emission", not no_sol and not sum_bad,
         f"solution_md on {len(sol_parts) - len(no_sol)}/{len(sol_parts)} linked parts; "
         f"mark_points sum == part marks everywhere: {not sum_bad}; "
         f"MS marks-column digit read for {ms_seen} parts, agrees with QP marks on {ms_agree}",
         {"missing_solution": no_sol, "sum_mismatches": sum_bad,
          "ms_marks_seen": ms_seen, "ms_marks_agree": ms_agree,
          "ms_marks_disagree": ms_disagree})

    # ---- assemble document (before popping internal fields) ------------------
    topic = {
        "schema": SCHEMA, "generated_utc": now_iso(),
        "generator": f"official_examq_extract.py v{CONVERTER_VERSION} (ADR-037) series={series}",
        "paper_id": paper_id,
        "source": {"qp_sha256": qp_sha, "ms_sha256": ms_sha,
                   "series": manifest["series"]["normalized"],
                   "printed": manifest["series"].get("printed"),
                   "archive": [m["source"]["archive"] for m in manifest["materials"]]},
        "paper_info": {"code": manifest["paper"]["official_reference"],
                       "session": manifest["series"]["normalized"],
                       "total_marks": total,
                       "course_id": "igcse-chemistry-19"},
        "questions": [{
            "id": f"{manifest['paper']['official_reference'].replace('/', '-')}-{q['question_number']:02d}",
            "question_number": q["question_number"],
            "total_marks": q["printed_total"] if q["printed_total"] is not None else inferred_totals[q["question_number"]],
            "total_marks_source": "printed-footer" if q["printed_total"] is not None else "inferred-parts-footer-missing",
            "stem_md": q["stem_md"],
            "parts": [{k: v for k, v in p.items()
                       if k not in ("group_stem_md", "option_list", "group", "roman", "answer_raw", "source_norm", "_ms_marks", "_owner") and v is not None}
                      for p in q["parts"]],
        } for q in doc_questions],
    }
    # attach group stems/option lists that carry content
    for q, dq in zip(topic["questions"], doc_questions):
        extras = {}
        for p in dq["parts"]:
            if p.get("group_stem_md") and p["group_stem_md"] not in extras:
                extras[p["group"]] = {"group_stem_md": p["group_stem_md"]}
            if p.get("option_list"):
                extras.setdefault(p["group"], {})["option_list"] = p["option_list"]
        q["groups"] = {g: v for g, v in extras.items() if v}

    # strip private crop-pass bookkeeping ("_" keys) from serialized assets
    for q in topic["questions"]:
        for p in q["parts"]:
            for a in p.get("assets") or []:
                for k in [k for k in a if k.startswith("_")]:
                    a.pop(k, None)

    # strip internal linkage fields from working copy
    for q in doc_questions:
        for p in q["parts"]:
            p.pop("group", None); p.pop("roman", None); p.pop("answer_raw", None)

    # ---- negative controls ---------------------------------------------------
    nc_results = []
    flat_parts = [p for q in topic["questions"] for p in q["parts"]]
    # N1: bump one mark on the last part of the question with the most parts
    if flat_parts:
        nc = copy.deepcopy(topic)
        tgt = max(nc["questions"], key=lambda q: len(q["parts"]))["parts"][-1]
        tgt["marks"] = (tgt["marks"] or 0) + 1
        g1_nc = _g1_recheck(nc, PAPER_TOTAL)
        nc_results.append({"id": "N1-mark-bump", "expected_gate": "G1", "detected": g1_nc})

    # N2: one-word substitution in a mid-length part (mimics paraphrase drift)
    nc2 = copy.deepcopy(topic)
    cands = [(qn, p) for qn, q in enumerate(nc2["questions"]) for p in q["parts"]
             if p.get("problem_md") and 15 <= len(p["problem_md"].split()) <= 90]
    nc2_target = None
    if cands:
        _, p_t = max(cands, key=lambda t: len(t[1]["problem_md"].split()))
        toks = p_t["problem_md"].split()
        i = next((j for j in range(len(toks) // 3, len(toks))
                  if len(toks[j]) > 3 and toks[j].isalpha()), None)
        if i is not None:
            toks[i] = "qxqqx"
            p_t["problem_md"] = " ".join(toks)
            nc2_target = p_t["part_number"]
    g2_nc = False
    if nc2_target:
        src = next(p for q in topic["questions"] for p in q["parts"] if p["part_number"] == nc2_target)
        mod = next(p for q in nc2["questions"] for p in q["parts"] if p["part_number"] == nc2_target)
        grams = ngrams(mod["problem_md"])
        r = sum(1 for g in grams if g in ngrams(src["problem_md"])) / len(grams) if grams else 1.0
        g2_nc = r < 0.95
    nc_results.append({"id": "N2-paraphrase", "expected_gate": "G2", "detected": g2_nc,
                       "target": nc2_target})

    # N3: fake spec code injected into the first part (skipped if no parts extracted)
    if flat_parts:
        nc3 = copy.deepcopy(topic)
        next(p for q in nc3["questions"] for p in q["parts"])["spec_point_codes"] = ["4CH1-9.99"]
        g6_nc = any(c not in registry for q in nc3["questions"] for p in q["parts"] for c in p["spec_point_codes"])
        nc_results.append({"id": "N3-fake-spec-code", "expected_gate": "G6", "detected": g6_nc})
    report["negative_controls"] = nc_results

    # ---- write outputs -------------------------------------------------------
    OUT.mkdir(parents=True, exist_ok=True)
    (OUT / "topic.json").write_text(json.dumps(topic, indent=1, ensure_ascii=False))
    (OUT / "validation-report.json").write_text(json.dumps(report, indent=1, ensure_ascii=False))
    write_questions_md(topic, OUT / "questions.md")

    print(f"paper: {paper_id}  (series arg: {series})")
    for g in report["gates"]:
        print(f"  {g['gate']:22} {g['status']:6} {g['summary']}")
    for nc in nc_results:
        print(f"  NC {nc['id']:18} {'DETECTED' if nc['detected'] else 'MISSED'} (expected {nc['expected_gate']})")
    print(f"  review queue: {len(report['review_queue'])} items")
    print(f"  outputs -> {OUT}")
    return 0


def _g1_recheck(doc, paper_total):
    """Negative-control recheck: any per-question parts/total mismatch or paper-total drift."""
    per_q = any(sum(p["marks"] or 0 for p in q["parts"]) != q["total_marks"] for q in doc["questions"])
    return per_q or sum(q["total_marks"] for q in doc["questions"]) != paper_total


def write_questions_md(topic, path):
    out = [f"# {topic['paper_info']['code']} — {topic['source']['series']} (official extraction)",
           "", f"> schema `{topic['schema']}` · paper_id `{topic['paper_id']}` · "
               f"qp sha256 `{topic['source']['qp_sha256'][:16]}…` · extracted verbatim, never regenerated (ADR-037)", ""]
    for q in topic["questions"]:
        out.append(f"## Question {q['question_number']} ({q['total_marks']} marks)")
        if q["stem_md"]:
            out += ["", q["stem_md"], ""]
        for g, gv in (q.get("groups") or {}).items():
            if gv.get("group_stem_md"):
                out += [f"**({g})** {gv['group_stem_md']}", ""]
            if gv.get("option_list"):
                out += [f"- {lab}" for lab in gv["option_list"]] + [""]
        for p in q["parts"]:
            marks = f"[{p['marks']}]" if p["marks"] is not None else "[?]"
            out.append(f"### {p['part_number']} {marks}")
            out += ["", p["problem_md"], ""]
            if p.get("choices"):
                out += [f"- **({c['label']})** {c['text_md']}" + ("  ✔" if c.get("is_correct") else "")
                        for c in p["choices"]] + [""]
            for a in p.get("assets") or []:
                if a.get("kind") == "crop" and a.get("path"):
                    cap = f"{a['mention']} — official paper figure (qp.pdf p.{a['page']})"
                    if a.get("shared"):
                        cap += f" — shared with {a.get('ref_part', '?')}"
                    out += [f"![{cap}]({a['path']})", ""]
                else:
                    out += [f"> 🖼 crop required: {a['mention']} (qp.pdf p.{a['page']})", ""]
            if p.get("solution_md"):
                out += ["", "**Mark scheme answer**", ""]
                out += ["> " + ln for ln in p["solution_md"].splitlines()]
                out += [""]
                for pt in p.get("mark_points") or []:
                    out += [f"- **({pt['marks']})** {pt['text_md'].splitlines()[0]}"]
                out += [""]
        out.append("")
    path.write_text("\n".join(out))


if __name__ == "__main__":
    sys.exit(main())
