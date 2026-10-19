#!/usr/bin/env python3
"""Build RAG chunks v3 from Docling page JSONs (data/docling_pages/).

Pipeline: page JSONs -> cleaned ordered blocks (LaTeX formulas -> Unicode,
dedup sidebar double-OCR, heading dedup) -> structure mapping via
book_structure.py -> segment by headings/markers -> pack into chunks
(350-1600 target, 2400 hard max) -> JSONL + full markdown + report.
"""
import json, re, sys, glob, collections

sys.path.insert(0, "/home/z/my-project/scripts")
from book_structure import (CHAPTERS, EXTRA_SECTIONS, UNIT_NAMES, OFFSET,
                            N_PAGES, MARKERS, TYPE_PRIORITY, BOOK_TITLE, BOOK_AUTHOR)

PAGES_DIR = "/home/z/my-project/data/docling_pages"
OUT_DIR = "/home/z/my-project/download/rag_chemistry"
TARGET_MIN, TARGET_MAX, HARD_MAX, MERGE_MIN = 350, 1600, 2400, 250

SUB = str.maketrans("0123456789+-", "₀₁₂₃₄₅₆₇₈₉₊₋")
SUP = str.maketrans("0123456789+-", "⁰¹²³⁴⁵⁶⁷⁸⁹⁺⁻")
FRAC = {("1", "2"): "½", ("1", "3"): "⅓", ("2", "3"): "⅔", ("1", "4"): "¼",
        ("3", "4"): "¾", ("1", "8"): "⅛", ("3", "8"): "⅜", ("5", "8"): "⅝",
        ("7", "8"): "⅞", ("1", "6"): "⅙", ("5", "6"): "⅚"}

# ---------------------------------------------------------------- formulas
def latex_to_chem(latex: str):
    """Convert CodeFormula LaTeX to compact Unicode chemistry/math. None if not clean."""
    s = latex.strip().strip("$").strip()
    # salvage literal junk the VLM emits: \ arrow, \ +, \%, \,
    s = re.sub(r"\\\s*arrow\b", " → ", s)
    s = re.sub(r"\\([+\-=%,;])", r" \1 ", s)
    s = s.replace("\\ ", " ")
    # strip array/matrix scaffolding and alignment
    s = re.sub(r"\\(begin|end)\s*\{\s*array\s*\}\s*(\{[^{}]*\})?", " ", s)
    s = s.replace("&", " ")
    s = s.replace("\\\\", "; ")
    # text-like commands -> verbatim content
    s = re.sub(r"\\(?:text|mathrm|mathbf|mathit|operatorname)\s*\{\s*([^{}]*?)\s*\}", r" \1 ", s)
    # functions and spacing/fence commands
    s = (s.replace("\\ln", " ln ").replace("\\log", " log ")
          .replace("\\left", " ").replace("\\right", " ")
          .replace("\\,", " ").replace("\\;", " ").replace("\\:", " ").replace("\\!", "")
          .replace("\\quad", " ").replace("\\qquad", " "))
    # VLM zero-vs-O confusion after a coefficient: "7 0 _ { 2 }" -> 7 O2
    s = re.sub(r"(?<=\d)\s+0\s*_\s*\{", " O _ {", s)
    # state symbols: ( 1 ) is really (l); ( a q ) -> (aq)
    s = re.sub(r"\(\s*1\s*\)", "(l)", s)
    for st in ("s", "l", "g", "aq"):
        s = re.sub(r"\(\s*" + st + r"\s*\)", f"({st})", s)
    # arrows / operators
    s = (s.replace("\\rightleftharpoons", " ⇌ ").replace("\\rightarrow", " → ")
          .replace("\\leftarrow", " ← ").replace("\\times", " × ")
          .replace("\\cdot", "·").replace("\\Delta", "Δ")
          .replace("\\div", " ÷ ").replace("\\approx", " ≈ ").replace("\\pm", "±"))
    # fractions (all common variants)
    s = re.sub(r"\\[dtc]?frac\s*\{\s*([^{}]+?)\s*\}\s*\{\s*([^{}]+?)\s*\}",
               lambda m: FRAC.get((m.group(1), m.group(2)), f"({m.group(1)})/({m.group(2)})"), s)
    # letter subscripts: O _ { 2 } -> O2(sub)
    s = re.sub(r"([A-Za-z\)\]])\s*_\s*\{\s*([^{}]+?)\s*\}",
               lambda m: m.group(1) + m.group(2).translate(SUB), s)
    # mixed-number coefficient left after fraction conversion: 3 _ { ½ } -> 3½
    s = re.sub(r"(\d)\s*_\s*\{\s*([^{}]+?)\s*\}", r"\1\2", s)
    # superscripts: ^ { 2 + } -> ²⁺  (also ^{ 12 }C -> ¹²C)
    s = re.sub(r"\^\s*\{\s*([^{}]+?)\s*\}", lambda m: m.group(1).translate(SUP), s)
    # rejoin char-spaced lowercase words: "s o l u b i l i t y" -> "solubility"
    for _ in range(12):
        if not re.search(r"\b[a-z] [a-z]\b", s):
            break
        s = re.sub(r"\b([a-z]) ([a-z])\b", r"\1\2", s)
    # compact: join atoms split by spaces (F e -> Fe, C O2 -> CO2), keep (aq) glue;
    # lowercase->lowercase boundaries keep their space (don't glue words)
    s = re.sub(r"(?<=[A-Z0-9\)⁺⁻₀-₉])\s+(?=[A-Za-z0-9\(])", "", s)
    s = re.sub(r"\s*([+→⇌×÷≈=])\s*", r" \1 ", s)
    # catch-all: any leftover arrow word -> arrow glyph
    s = re.sub(r"(?<![A-Za-z])(?:arrow|longrightarrow|rightarrow)(?![A-Za-z])", " → ", s)
    # tidy inner-paren spacing: ( aq ) -> (aq)
    s = re.sub(r"\(\s+([^()]*?)\s+\)", r"(\1)", s)
    # space between number and following unit letter (13.84g -> 13.84 g)
    s = re.sub(r"(?<=\d)(?=[a-z])", " ", s)
    s = re.sub(r"\s{2,}", " ", s).strip()
    if re.search(r"\\|\{|\}", s):  # ANY residual LaTeX scaffolding -> reject
        return None
    return s

# ------------------------------------------------------------- small fixes
MERGED_HEADINGS = {"KEYPOINT": "KEY POINT", "EXTENSIONWORK": "EXTENSION WORK",
                   "CHEMISTRYONLY": "CHEMISTRY ONLY", "DIDYOUKNOW": "DID YOU KNOW?",
                   "UNITQUESTIONS": "UNIT QUESTIONS", "CHAPTERQUESTIONS": "CHAPTER QUESTIONS"}

def clean_heading(t: str) -> str:
    t = " ".join(t.split())
    if t.upper() in MERGED_HEADINGS:
        return MERGED_HEADINGS[t.upper()]
    words = t.split()
    # collapse doubled headings: "KEY POINT KEY POINT"
    if len(words) % 2 == 0 and len(words) >= 2:
        h = len(words) // 2
        if [w.lower() for w in words[:h]] == [w.lower() for w in words[h:]]:
            t = " ".join(words[:h])
    return t

BRACE_SUB = [
    re.compile(r"([A-Za-z\)])_\{\s*([^{}]{1,6})\s*\}"),   # NO_{3-}
    re.compile(r"([A-Za-z])\{([0-9]{1,2})\}"),            # R{f}
    re.compile(r"([A-Za-z])\{(\d+)"),                     # Cl{2  (unclosed)
]

def clean_braces(t: str) -> str:
    for rx in BRACE_SUB:
        t = rx.sub(lambda m: m.group(1) + m.group(2).translate(SUB), t)
    return t.replace("{", "").replace("}", "")

def fix_text(t: str) -> str:
    t = re.sub(r"\(([AM])\s*,\s*\)", r"(\1ᵣ)", t)          # (A,) (M,) -> Ar Mr
    t = re.sub(r"\b([a-z]{4,})\(ll\)", r"\1(II)", t)        # iron(ll) -> iron(II)
    t = re.sub(r"\(([A-Z][A-Za-z]?\d*)\+\)", r"(\1⁺)", t)   # (H+) (Cu2+) style
    t = re.sub(r"\(([A-Z][A-Za-z]?\d*)\-\)", r"(\1⁻)", t)
    t = re.sub(r"\bH\+(?=[\s,)])", "H⁺", t)
    t = clean_braces(t)
    t = re.sub(r"[ \t]{2,}", " ", t)
    return t.strip()

EXTRA_MARKERS = {
    "alternative_method": r"ALTERNATIVE\s+METHOD",
    "problem_solving":    r"PROBLEM\s+SOLVING",
    "chemistry_only_box": r"CHEMISTRY\s+ONLY",
    "stat":               r"^STAT\s*$",
    "skills_box":         r"^SKILLS\s*$",
}
CT_MAP = {  # marker key -> content_type
    "learning_objectives": "learning_objectives", "chapter_questions": "chapter_questions",
    "activity": "activity", "practical": "practical", "did_you_know": "did_you_know",
    "key_point": "key_point", "worked_example": "worked_example", "exam_hint": "exam_hint",
    "safety": "safety", "alternative_method": "exam_hint", "problem_solving": "activity",
    "chemistry_only_box": "learning_objectives", "stat": "did_you_know", "skills_box": "exam_hint",
}

def detect_marker(text: str):
    up = text.upper()
    for key, rx in list(MARKERS.items()) + list(EXTRA_MARKERS.items()):
        if key == "safety":
            if re.search(rx, text):
                return CT_MAP[key]
            continue
        if re.search(rx, up):
            return CT_MAP[key]
    return None

# ------------------------------------------------------------ page context
def build_page_context():
    ctx = {p: {"unit_no": None, "unit_name": None, "chapter_no": None,
               "chapter_title": None, "base": "front_matter"} for p in range(1, N_PAGES + 1)}
    for i, (cno, unit, title, bpage) in enumerate(CHAPTERS):
        start = bpage + OFFSET
        end = (CHAPTERS[i + 1][3] + OFFSET - 1) if i + 1 < len(CHAPTERS) else N_PAGES
        for p in range(start, end + 1):
            ctx[p] = {"unit_no": unit, "unit_name": UNIT_NAMES[unit], "chapter_no": cno,
                      "chapter_title": title, "base": "body"}
    for key, s, e, unit, label, ctype in EXTRA_SECTIONS:
        for p in range(s, e + 1):
            ctx[p] = {"unit_no": unit, "unit_name": UNIT_NAMES.get(unit),
                      "chapter_no": None, "chapter_title": label, "base": ctype}
    return ctx

# ------------------------------------------------------------------- load
def load_blocks():
    """Yield (page, kind, text) blocks in reading order, cleaned."""
    formulas_ok = formulas_fail = dropped_dupes = 0
    for fp in sorted(glob.glob(f"{PAGES_DIR}/page_*.json")):
        d = json.load(open(fp))
        pno = d["pdf_page"]
        prev = None
        for it in d.get("items", []):
            label, text = it["label"], (it.get("text") or "").strip()
            if label == "picture":
                continue
            if label in ("formula", "code"):
                if not text or len(text) > 600:  # real equations are short; long = hallucination
                    continue
                conv = latex_to_chem(text)
                if conv and len(conv) >= 4:
                    formulas_ok += 1
                    blk = ("formula", conv)
                else:
                    formulas_fail += 1
                    continue  # keep junk out of the corpus
            elif label == "table":
                if len(text) < 30:
                    continue
                blk = ("table", clean_braces(text))
            elif label in ("text", "section_header", "list_item", "caption"):
                if not text:
                    continue
                # page-number artifacts
                if label == "text" and re.fullmatch(r"\d{1,3}", text) and \
                   int(text) in (pno, pno - OFFSET):
                    continue
                if label == "section_header":
                    blk = ("heading", clean_heading(fix_text(text)))
                elif label == "list_item":
                    blk = ("list", fix_text(text))
                else:
                    blk = ("para", fix_text(text))
            else:
                continue
            if prev == blk[1] and blk[0] in ("para", "heading", "formula"):
                dropped_dupes += 1  # sidebar double-OCR artifact
                continue
            yield (pno, blk[0], blk[1])
            prev = blk[1]
    print(f"[blocks] formulas converted={formulas_ok} failed={formulas_fail} dupes dropped={dropped_dupes}",
          file=sys.stderr)

# ------------------------------------------------------------------ chunks
def split_long(text: str, max_len: int = 1900):
    """Split an oversized block at sentence boundaries."""
    sents = re.split(r"(?<=[.!?;]) +", text)
    parts, cur = [], ""
    for s in sents:
        if cur and len(cur) + len(s) + 1 > max_len:
            parts.append(cur)
            cur = s
        else:
            cur = (cur + " " + s).strip() if cur else s
    if cur:
        parts.append(cur)
    return parts


class Chunker:
    def __init__(self):
        self.chunks = []
        self.idx = 0

    def flush(self, seg):
        if not seg["blocks"]:
            return
        blocks = []
        for kind, text in seg["blocks"]:
            if len(text) > HARD_MAX:
                blocks.extend((kind, p) for p in split_long(text))
            else:
                blocks.append((kind, text))
        paras, cur, cur_size = blocks, [], 0
        out = []
        for kind, text in paras:
            if cur_size >= TARGET_MIN and cur_size + len(text) > TARGET_MAX:
                out.append(cur)
                cur, cur_size = [], 0
            cur.append((kind, text))
            cur_size += len(text) + 2
        if cur:
            out.append(cur)
        # merge tiny trailing piece
        if len(out) >= 2 and sum(len(t) for _, t in out[-1]) < MERGE_MIN:
            last, prev = out.pop(), out.pop()
            out.append(prev + last)
        for piece in out:
            size = sum(len(t) for _, t in piece)
            if size < 40:  # drop nano-fragments
                continue
            parts = []
            for kind, text in piece:
                if kind == "list":
                    parts.append("• " + text)
                else:
                    parts.append(text)
            self.idx += 1
            bp0 = seg["start_page"] - OFFSET
            bp1 = seg["end_page"] - OFFSET
            has_book_page = seg["start_page"] >= OFFSET + 2  # book page 1 = PDF 10+
            book_pages = [bp0, bp1] if has_book_page else None
            cid = (f"chem_v3_u{seg['unit_no'] or 0}_c{seg['chapter_no'] or 0}"
                   f"_pdf{seg['start_page']:03d}_{self.idx:04d}")
            self.chunks.append({
                "id": cid,
                "book_title": BOOK_TITLE,
                "author": BOOK_AUTHOR,
                "unit_no": seg["unit_no"], "unit_name": seg["unit_name"],
                "chapter_no": seg["chapter_no"], "chapter_title": seg["chapter_title"],
                "section": seg["section"],
                "content_type": seg["ctype"],
                "book_pages": book_pages,
                "pdf_pages": [seg["start_page"], seg["end_page"]],
                "char_count": sum(len(p) for p in parts) + 2 * max(0, len(parts) - 1),
                "text": "\n\n".join(parts),
            })

    def run(self, blocks, ctx):
        seg = None

        def new_seg(pno, section, ctype):
            c = ctx[pno]
            return {"blocks": [], "section": section, "ctype": ctype,
                    "start_page": pno, "end_page": pno,
                    "unit_no": c["unit_no"], "unit_name": c["unit_name"],
                    "chapter_no": c["chapter_no"], "chapter_title": c["chapter_title"]}

        cur_ctx_key = None
        for pno, kind, text in blocks:
            c = ctx[pno]
            key = (c["unit_no"], c["chapter_no"], c["base"])
            if key != cur_ctx_key:  # structural boundary (chapter/section change)
                if seg:
                    self.flush(seg)
                seg = new_seg(pno, None, c["base"])
                cur_ctx_key = key
            if kind == "heading":
                if seg and seg["blocks"]:
                    self.flush(seg)
                seg = new_seg(pno, text, detect_marker(text) or c["base"])
                seg["blocks"].append(("heading", text))  # keep heading as first line
                seg["end_page"] = pno
            elif kind == "table":
                if seg is None:
                    seg = new_seg(pno, None, c["base"])
                if seg["blocks"]:
                    sect, ctype = seg["section"], seg["ctype"]
                    self.flush(seg)
                    seg = new_seg(pno, sect, ctype)  # fresh segment; stale one must not re-flush
                tseg = new_seg(pno, seg["section"], "table_data")
                tseg["blocks"].append(("table", text))
                self.flush(tseg)
            else:
                if seg is None:
                    seg = new_seg(pno, None, c["base"])
                if kind == "para" and text.startswith("Safety Note:"):
                    if seg["blocks"]:
                        self.flush(seg)
                    seg = new_seg(pno, seg["section"], "safety")
                seg["blocks"].append((kind, text))
                seg["end_page"] = pno
        if seg and seg["blocks"]:
            self.flush(seg)


def main():
    ctx = build_page_context()
    blocks = list(load_blocks())
    print(f"[blocks] total={len(blocks)}", file=sys.stderr)
    ch = Chunker()
    ch.run(blocks, ctx)
    chunks = ch.chunks
    # merge undersized chunks into their predecessor when same context & type
    merged = []
    for c in chunks:
        if (merged and c["char_count"] < MERGE_MIN
                and merged[-1]["char_count"] + c["char_count"] + 4 <= HARD_MAX
                and merged[-1]["unit_no"] == c["unit_no"]
                and merged[-1]["chapter_no"] == c["chapter_no"]
                and merged[-1]["content_type"] == c["content_type"]
                and (merged[-1]["book_pages"] and c["book_pages"]
                     and merged[-1]["book_pages"][1] >= c["book_pages"][0] - 1
                     or (merged[-1]["book_pages"] is None and c["book_pages"] is None))):
            m = merged[-1]
            m["text"] = m["text"] + "\n\n" + c["text"]
            m["char_count"] = len(m["text"])
            if m["book_pages"] and c["book_pages"]:
                m["book_pages"][1] = max(m["book_pages"][1], c["book_pages"][1])
            m["pdf_pages"][1] = max(m["pdf_pages"][1], c["pdf_pages"][1])
            m["section"] = m["section"] or c["section"]
        else:
            merged.append(c)
    chunks = merged
    # list items: docling labels list_item -> we stored kind 'list_item'; convert to bullet
    for c in chunks:
        pass
    out_jsonl = f"{OUT_DIR}/edexcel_igcse_chemistry_chunks_v3.jsonl"
    with open(out_jsonl, "w", encoding="utf-8") as f:
        for c in chunks:
            f.write(json.dumps(c, ensure_ascii=False) + "\n")
    print(f"[chunks] {len(chunks)} -> {out_jsonl}", file=sys.stderr)

    # full markdown
    md = [f"# {BOOK_TITLE} — Jim Clark", ""]
    last = None
    for c in chunks:
        key = (c["unit_no"], c["chapter_no"])
        if key != last:
            if c["unit_no"]:
                md.append(f"\n## Unit {c['unit_no']}: {c['unit_name']}")
            md.append(f"\n### {c['chapter_title']}\n")
            last = key
        if c["section"] and c["text"].split("\n\n")[0] != c["section"]:
            md.append(f"\n#### {c['section']}")
        md.append(c["text"])
    with open(f"{OUT_DIR}/full_book_docling.md", "w", encoding="utf-8") as f:
        f.write("\n".join(md))

    # report
    types = collections.Counter(c["content_type"] for c in chunks)
    sizes = sorted(c["char_count"] for c in chunks)
    report = {
        "n_chunks": len(chunks), "content_types": dict(types),
        "size_min": sizes[0], "size_max": sizes[-1],
        "size_avg": round(sum(sizes) / len(sizes)),
        "n_chunks_over_hardmax": sum(1 for s in sizes if s > HARD_MAX),
    }
    json.dump(report, open(f"{OUT_DIR}/parse_report_v3.json", "w"), indent=2)
    print(json.dumps(report, indent=2), file=sys.stderr)


if __name__ == "__main__":
    main()
