#!/usr/bin/env python3
"""Build RAG chunks for IAL Chemistry SB2 (YCH12 lane, Curtis/Murgatroyd/Scott)
from Docling page JSONs (data/ych12_sb2/docling_pages/).

Pipeline (per books/README.md §5 phase 5, adapted from the validated YPH11 SB1
IAL chunker): page JSONs -> cleaned ordered blocks (LaTeX -> Unicode chemistry,
dedup, heading dedup) -> structure mapping via book_structure_ych12.py ->
segment by headings/markers -> pack (350-1600, 2400 hard max) -> JSONL +
full markdown + report.

YCH11 deltas vs the YPH11 SB1 reference:
- unit = TOPIC (11-20; Unit 4 = Topics 11-15, Unit 5 = Topics 16-20), chapter =
  the book's lettered sections (11A-20A) numbered sequentially c1-c19
- per-TOPIC THINKING BIGGER + EXAM PRACTICE banks (10 each) typed per the
  YPH11 EP precedent (`chapter_questions`, chapter_no None — serving-critical
  law is the exact-page question anchoring, not the owner granularity)
- page law: arabic book = pdf - 12, book 1 does not exist in the PDF
  (front matter roman ii-xiii = PDF 2-13, book_pages null); first arabic page
  is book 2 = PDF 14 (4-way confirmed; roman = pdf - 0)
- ID grammar: ych1_v1_u<unit|0>_c<chapter|0>_pdf<pdfpage:03d>_<block:04d>
  (ych2_v1_ per the two-book law, YPH11 D-8 — THIS lane)
- chemistry LaTeX -> Unicode: state symbols (s)/(l)/(g)/(aq), ⇌, ΔH, Aᵣ/Mᵣ (identical pass)
"""
import json, re, sys, glob, collections, os

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from book_structure_ych12 import (CHAPTERS, EXTRA_SECTIONS, TOPIC_DIVIDERS,
                                  THINKING_BIGGER, EXAM_PRACTICE, TOPIC_TITLES,
                                  UNIT_NAMES, OFFSET, N_PAGES, MARKERS,
                                  TYPE_PRIORITY, BOOK_TITLE, BOOK_AUTHOR, SHA256)

PAGES_DIR = "/home/z/my-project/data/ych12_sb2/docling_pages"
OUT_DIR = os.environ.get("YCH12_OUT_DIR", "/home/z/my-project/data/ych12_sb2/out")
# v2 fresh-parse lane (T-PARSE-YCH12-2): YCH12_VERSION=v2 re-tags ids/filenames
# (ych2_v2_). Default "v1" reproduces the r0 parse of record byte-for-byte.
# (VER interpolates DIRECTLY into the id tag and filenames — the value must
# be "v2", not "2": E-005 in books/README.md.)
VER = os.environ.get("YCH12_VERSION", "v1")
TARGET_MIN, TARGET_MAX, HARD_MAX, MERGE_MIN = 350, 1600, 2400, 250
FIRST_ARABIC_PDF = OFFSET + 2  # book 2 = PDF 14 (book 1 print-blank omitted)

SUB = str.maketrans("0123456789+-", "₀₁₂₃₄₅₆₇₈₉₊₋")
SUP = str.maketrans("0123456789+-", "⁰¹²³⁴⁵⁶⁷⁸⁹⁺⁻")
FRAC = {("1", "2"): "½", ("1", "3"): "⅓", ("2", "3"): "⅔", ("1", "4"): "¼",
        ("3", "4"): "¾", ("1", "8"): "⅛", ("3", "8"): "⅜", ("5", "8"): "⅝",
        ("7", "8"): "⅞", ("1", "6"): "⅙", ("5", "6"): "⅚"}

# ---------------------------------------------------------------- formulas
def latex_to_chem(latex: str):
    """Convert CodeFormula LaTeX to compact Unicode chemistry/math. None if not clean."""
    s = latex.strip().strip("$").strip()
    s = re.sub(r"\\\s*(to|arrow|rightarrow|longrightarrow)\b", " → ", s)
    s = re.sub(r"\\([+\-=%,;])", r" \1 ", s)
    s = s.replace("\\ ", " ")
    s = re.sub(r"\\(begin|end)\s*\{\s*array\s*\}\s*(\{[^{}]*\})?", " ", s)
    s = s.replace("&", " ")
    s = s.replace("\\\\", "; ")
    s = re.sub(r"\\(?:text|mathrm|mathbf|mathit|operatorname)\s*\{\s*([^{}]*?)\s*\}", r" \1 ", s)
    s = (s.replace("\\ln", " ln ").replace("\\log", " log ")
          .replace("\\left", " ").replace("\\right", " ")
          .replace("\\,", " ").replace("\\;", " ").replace("\\:", " ").replace("\\!", "")
          .replace("\\quad", " ").replace("\\qquad", " "))
    s = (s.replace("\\rightleftharpoons", " ⇌ ").replace("\\rightarrow", " → ")
          .replace("\\leftarrow", " ← ").replace("\\times", " × ")
          .replace("\\cdot", "·").replace("\\Delta", "Δ")
          .replace("\\div", " ÷ ").replace("\\approx", " ≈ ").replace("\\pm", "±")
          .replace("\\propto", " ∝ ").replace("\\infty", "∞")
          .replace("\\lambda", "λ").replace("\\rho", "ρ")
          .replace("\\pi", "π").replace("\\theta", "θ").replace("\\Omega", "Ω")
          .replace("\\mu", "μ").replace("\\omega", "ω")
          .replace("\\epsilon", "ε").replace("\\sigma", "σ")
          .replace("\\circ", "°").replace("\\degree", "°"))
    s = re.sub(r"\\[dtc]?frac\s*\{\s*([^{}]+?)\s*\}\s*\{\s*([^{}]+?)\s*\}",
               lambda m: FRAC.get((m.group(1), m.group(2)), f"({m.group(1)})/({m.group(2)})"), s)
    s = re.sub(r"([A-Za-z\)\]])\s*_\s*\{\s*([^{}]+?)\s*\}",
               lambda m: m.group(1) + m.group(2).translate(SUB), s)
    s = re.sub(r"(\d)\s*_\s*\{\s*([^{}]+?)\s*\}", r"\1\2", s)
    s = re.sub(r"\^\s*\{\s*([^{}]+?)\s*\}", lambda m: m.group(1).translate(SUP), s)
    for _ in range(12):
        if not re.search(r"\b[a-z] [a-z]\b", s):
            break
        s = re.sub(r"\b([a-z]) ([a-z])\b", r"\1\2", s)
    s = re.sub(r"(?<=[A-Z0-9\)⁺⁻₀-₉])\s+(?=[A-Za-z0-9\(])", "", s)
    s = re.sub(r"\s*([+→⇌×÷≈=∝])\s*", r" \1 ", s)
    s = re.sub(r"(?<![A-Za-z])(?:arrow|longrightarrow|rightarrow)(?![A-Za-z])", " → ", s)
    s = re.sub(r"\(\s+([^()]*?)\s+\)", r"(\1)", s)
    s = re.sub(r"(?<=\d)(?=[a-z])", " ", s)
    s = re.sub(r"\s{2,}", " ", s).strip()
    if re.search(r"\\|\{|\}", s):
        return None
    return s

# ------------------------------------------------------------- small fixes
MERGED_HEADINGS = {
    "CHECKPOINT": "CHECKPOINT",
    "LEARNINGOBJECTIVES": "LEARNING OBJECTIVES",
    "LEARNINGTIP": "LEARNING TIP",
    "SUBJECTVOCABULARY": "SUBJECT VOCABULARY",
    "DIDYOUKNOW": "DID YOU KNOW?",
    "DIDYOUKNOW?": "DID YOU KNOW?",
    "WORKEDEXAMPLE": "WORKED EXAMPLE",
    "EXAMPRACTICE": "EXAM PRACTICE",
    "EXAMHINT": "EXAM HINT",
    "THINKINGBIGGER": "THINKING BIGGER",
    "THINKINGBIGGERTIP": "THINKING BIGGER TIP",
    "MATHSSKILLSFORTHISTOPIC": "MATHS SKILLS FOR THIS TOPIC",
    "MATHSSKILLSFORTHISCHAPTER": "MATHS SKILLS FOR THIS CHAPTER",
    "SPECIFICATIONREFERENCE": "SPECIFICATION REFERENCE",
    "SPECREFERENCE": "SPEC REFERENCE",
    "CHEMISTRYINDETAIL": "CHEMISTRY IN DETAIL",
    "SCIENCECOMMUNICATION": "SCIENCE COMMUNICATION",
    "COREPRACTICAL": "CORE PRACTICAL",
    "KEYPOINT": "KEY POINT",
    "ADDITIONALREADING": "ADDITIONAL READING",
}

def clean_heading(t: str) -> str:
    t = " ".join(t.split())
    if t.upper() in MERGED_HEADINGS:
        return MERGED_HEADINGS[t.upper()]
    words = t.split()
    if len(words) % 2 == 0 and len(words) >= 2:
        h = len(words) // 2
        if [w.lower() for w in words[:h]] == [w.lower() for w in words[h:]]:
            t = " ".join(words[:h])
    return t

BRACE_SUB = [
    re.compile(r"([A-Za-z\)])_\{\s*([^{}]{1,6})\s*\}"),
    re.compile(r"([A-Za-z])\{([0-9]{1,2})\}"),
    re.compile(r"([A-Za-z])\{(\d+)"),
]

def clean_braces(t: str) -> str:
    for rx in BRACE_SUB:
        t = rx.sub(lambda m: m.group(1) + m.group(2).translate(SUB), t)
    return t.replace("{", "").replace("}", "")

def fix_text(t: str) -> str:
    t = clean_braces(t)
    t = re.sub(r"[ \t]{2,}", " ", t)
    return t.strip()

# feature markers (merged-OCR aware) -> content types
CT_MAP = {
    "learning_objectives": "learning_objectives",
    "worked_example": "worked_example",
    "exam_hint": "exam_hint",
    "thinking_bigger": "thinking_bigger",
    "exam_practice": "chapter_questions",
    "maths_skills": "skills",
    "spec_reference": "learning_objectives",
    "key_point": "key_point",
    "did_you_know": "did_you_know",
    "core_practical": "practical",
    "checkpoint": "checkpoint",
    "subject_vocabulary": "subject_vocabulary",
    "learning_tip": "exam_hint",
    "activity": "activity",
}

def detect_marker(text: str):
    up = text.upper()
    for key, rx in MARKERS.items():
        if re.search(rx, up):
            return CT_MAP.get(key)
    # merged-OCR forms the census caught (not in structure MARKERS)
    if re.search(r"^CHECKPOINT\b", up):
        return "checkpoint"
    if re.search(r"^SUBJECT\s*VOCABULARY", up):
        return "subject_vocabulary"
    if re.search(r"^LEARNING\s*TIP", up):
        return "exam_hint"
    if re.search(r"^CORE\s*PRACTICAL", up):
        return "practical"
    if re.search(r"^ACTIVITY\b", up):
        return "activity"
    return None

# ------------------------------------------------------------ page context
def build_page_context():
    """pdf_page -> {unit_no, unit_name, chapter_no, chapter_title, base}."""
    ctx = {p: {"unit_no": None, "unit_name": None, "chapter_no": None,
               "chapter_title": None, "base": "front_matter"} for p in range(1, N_PAGES + 1)}
    # chapter bodies (book pages are explicit ranges from the structure map)
    for i, (unit, label, title, b, e) in enumerate(CHAPTERS):
        start, end = b + OFFSET, e + OFFSET
        for p in range(start, end + 1):
            ctx[p] = {"unit_no": unit, "unit_name": UNIT_NAMES[unit], "chapter_no": i + 1,
                      "chapter_title": f"{label} {title}", "base": "body"}
    # topic dividers
    for t, (b, e) in TOPIC_DIVIDERS.items():
        for p in range(b + OFFSET, e + OFFSET + 1):
            ctx[p] = {"unit_no": t, "unit_name": UNIT_NAMES[t], "chapter_no": None,
                      "chapter_title": TOPIC_TITLES[t], "base": "topic_divider"}
    # per-topic THINKING BIGGER pages
    for t, (b, e) in THINKING_BIGGER.items():
        for p in range(b + OFFSET, e + OFFSET + 1):
            ctx[p] = {"unit_no": t, "unit_name": UNIT_NAMES[t], "chapter_no": None,
                      "chapter_title": TOPIC_TITLES[t], "base": "thinking_bigger"}
    # per-topic EXAM PRACTICE banks -> chapter_questions per the YPH11 EP precedent
    for t, (b, e) in EXAM_PRACTICE.items():
        for p in range(b + OFFSET, e + OFFSET + 1):
            ctx[p] = {"unit_no": t, "unit_name": UNIT_NAMES[t], "chapter_no": None,
                      "chapter_title": TOPIC_TITLES[t], "base": "chapter_questions"}
    # back matter
    for kind, s, e, label in EXTRA_SECTIONS:
        t = 20 if s >= 282 else None
        for p in range(s + OFFSET, e + OFFSET + 1):
            ctx[p] = {"unit_no": t, "unit_name": UNIT_NAMES.get(t),
                      "chapter_no": None, "chapter_title": label, "base": kind}
    return ctx

# ------------------------------------------------------------------- load
def load_blocks():
    """Yield (page, kind, text) blocks in reading order, cleaned."""
    formulas_ok = formulas_fail = dropped_dupes = 0
    for fp in sorted(glob.glob(f"{PAGES_DIR}/page_*.json")):
        d = json.load(open(fp))
        pno = d["pdf_page"]
        if d.get("error"):
            print(f"[blocks] WARNING error page {pno} skipped", file=sys.stderr)
            continue
        prev = None
        for it in d.get("items", []):
            label, text = it["label"], (it.get("text") or "").strip()
            if label in ("picture", "checkbox_unselected", "checkbox_selected"):
                continue
            if label in ("formula", "code"):
                if not text or len(text) > 600:
                    continue
                if "\\" in text or "{" in text or "frac" in text:
                    conv = latex_to_chem(text)
                else:
                    conv = " ".join(text.split())  # already Unicode (rescue pass)
                if conv and len(conv) >= 4:
                    formulas_ok += 1
                    blk = ("formula", conv)
                else:
                    formulas_fail += 1
                    continue
            elif label == "table":
                if len(text) < 30:
                    continue
                blk = ("table", clean_braces(text))
            elif label in ("text", "section_header", "list_item", "caption", "footnote"):
                if not text:
                    continue
                if label == "text" and re.fullmatch(r"\d{1,3}", text) and \
                   int(text) in (pno, pno - OFFSET):
                    continue  # running header/footer page digits
                if label == "section_header":
                    blk = ("heading", clean_heading(fix_text(text)))
                elif label == "list_item":
                    blk = ("list", fix_text(text))
                else:
                    blk = ("para", fix_text(text))
            else:
                continue
            if prev == blk[1] and blk[0] in ("para", "heading", "formula"):
                dropped_dupes += 1
                continue
            yield (pno, blk[0], blk[1])
            prev = blk[1]
    print(f"[blocks] formulas converted={formulas_ok} failed={formulas_fail} dupes dropped={dropped_dupes}",
          file=sys.stderr)

# ------------------------------------------------------------------ chunks
def split_long(text: str, max_len: int = 1900):
    """Split an oversized block: sentences first, then lines (index/glossary
    entries have no periods — L-009), then hard word-splits as last resort."""
    parts, cur = [], ""
    sents = re.split(r"(?<=[.!?;]) +", text)
    if len(sents) == 1 and len(text) > max_len:
        sents = [ln for ln in text.splitlines() if ln.strip()] or [text]
    for s in sents:
        while len(s) > max_len:  # single huge line: hard-split on words
            cut = s.rfind(" ", 0, max_len)
            cut = cut if cut > max_len // 2 else max_len
            parts.append(s[:cut].strip())
            s = s[cut:].strip()
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
        if len(out) >= 2 and sum(len(t) for _, t in out[-1]) < MERGE_MIN:
            last, prev = out.pop(), out.pop()
            out.append(prev + last)
        for piece in out:
            size = sum(len(t) for _, t in piece)
            if size < 40:
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
            has_book_page = seg["start_page"] >= FIRST_ARABIC_PDF
            book_pages = [bp0, bp1] if has_book_page else None
            cid = (f"ych2_{VER}_u{seg['unit_no'] or 0}_c{seg['chapter_no'] or 0}"
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
            if key != cur_ctx_key:
                if seg:
                    self.flush(seg)
                seg = new_seg(pno, None, c["base"])
                cur_ctx_key = key
            if kind == "heading":
                if seg and seg["blocks"]:
                    self.flush(seg)
                # front-matter pages keep their base type even when a feature
                # heading (e.g. 'EXAM PRACTICE' box in About this book) matches (D-9 law)
                # divider/thinking_bigger/question/back-matter pages keep their
                # base type too — the page-role typing is serving-critical
                if c["base"] in ("front_matter", "topic_divider", "thinking_bigger",
                                 "chapter_questions", "maths_skills", "preparing_for_exams",
                                 "command_words", "glossary", "periodic_table", "index",
                                 "graph_paper"):
                    ctype = c["base"]
                else:
                    ctype = detect_marker(text) or c["base"]
                seg = new_seg(pno, text, ctype)
                seg["blocks"].append(("heading", text))
                seg["end_page"] = pno
            elif kind == "table":
                if seg is None:
                    seg = new_seg(pno, None, c["base"])
                if seg["blocks"]:
                    sect, ctype = seg["section"], seg["ctype"]
                    self.flush(seg)
                    seg = new_seg(pno, sect, ctype)
                tseg = new_seg(pno, seg["section"], "table_data")
                tseg["blocks"].append(("table", text))
                self.flush(tseg)
            else:
                if seg is None:
                    seg = new_seg(pno, None, c["base"])
                seg["blocks"].append((kind, text))
                seg["end_page"] = pno
        if seg and seg["blocks"]:
            self.flush(seg)


def main():
    os.makedirs(OUT_DIR, exist_ok=True)
    ctx = build_page_context()
    blocks = list(load_blocks())
    print(f"[blocks] total={len(blocks)}", file=sys.stderr)
    ch = Chunker()
    ch.run(blocks, ctx)
    chunks = ch.chunks
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
    out_jsonl = f"{OUT_DIR}/edexcel_ial_chemistry_ych12_sb2_chunks_{VER}.jsonl"
    with open(out_jsonl, "w", encoding="utf-8") as f:
        for c in chunks:
            f.write(json.dumps(c, ensure_ascii=False) + "\n")
    print(f"[chunks] {len(chunks)} -> {out_jsonl}", file=sys.stderr)

    md = [f"# {BOOK_TITLE} — {BOOK_AUTHOR}", ""]
    last = None
    for c in chunks:
        key = (c["unit_no"], c["chapter_no"], c["content_type"])
        if key != last:
            if c["unit_no"]:
                md.append(f"\n## Topic {c['unit_no']}: {c['unit_name']}")
            if c["chapter_title"]:
                md.append(f"\n### {c['chapter_title']}\n")
            last = key
        if c["section"] and c["text"].split("\n\n")[0] != c["section"]:
            md.append(f"\n#### {c['section']}")
        md.append(c["text"])
    with open(f"{OUT_DIR}/full_book_docling.md", "w", encoding="utf-8") as f:
        f.write("\n".join(md))

    types = collections.Counter(c["content_type"] for c in chunks)
    sizes = sorted(c["char_count"] for c in chunks)
    report = {
        "n_chunks": len(chunks), "content_types": dict(types),
        "size_min": sizes[0], "size_max": sizes[-1],
        "size_avg": round(sum(sizes) / len(sizes)),
        "n_chunks_over_hardmax": sum(1 for s in sizes if s > HARD_MAX),
        "source_pdf_sha256": SHA256,
        "parser": "docling 2.33.0 + rapidocr-onnxruntime 1.4.4 (formula enrichment OFF "
                  "base corpus — 2.33 CodeFormula integration emits empty formula text "
                  "either way, YCH11 D-7/L-020; page-level JSON checkpoints; book = pdf-12 "
                  "page law, front matter roman ii-xiii; transformers 4.52.4 + "
                  "torch 2.14.1+cpu/torchvision 0.29.1+cpu rebuilt environment)",
        "formula_rescue": "see pipeline/evidence/formula_orphans.json + manual_formulas_ych12.jsonl "
                  "(verbatim manual transcription pass, applied to page JSONs before chunking)",
        "by_design_gaps": [
            {"pdf_page": 310, "book_page": 298, "kind": "periodic_table",
             "reason": "image-only page: OCR yields only the 'Group Period' axis labels "
                       "(below the 40-char chunk floor) — recorded here, not chunked"},
            {"pdf_page": 317, "book_page": 305, "kind": "graph_paper",
             "reason": "image-only end leaf (blank practice graph grid, printed '305'), "
                       "zero extractable text — recorded here, not chunked"},
            {"pdf_page": 318, "book_page": 306, "kind": "graph_paper",
             "reason": "image-only end leaf (blank practice graph grid, printed '306'), "
                       "zero extractable text — recorded here, not chunked"},
            {"pdf_page": 319, "book_page": 307, "kind": "graph_paper",
             "reason": "image-only end leaf (blank practice graph grid, printed '307'), "
                       "zero extractable text — recorded here, not chunked"},
            {"pdf_page": 320, "book_page": 308, "kind": "graph_paper",
             "reason": "image-only end leaf (blank practice graph grid, printed '308'), "
                       "zero extractable text — recorded here, not chunked"},
        ],
        "n_llm_polished": 0,
    }
    json.dump(report, open(f"{OUT_DIR}/parse_report_{VER}.json", "w"), indent=2)
    print(json.dumps(report, indent=2), file=sys.stderr)


if __name__ == "__main__":
    main()
