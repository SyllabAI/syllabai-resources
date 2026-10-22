#!/usr/bin/env python3
"""Build RAG chunks for YPH11 SB1 (IAL Physics, Miles Hudson) from Docling
page JSONs (data/yph11_sb1/docling_pages/).

Pipeline (per books/README.md §5 phase 5, adapted from the audited 4PH1
physics chunker): page JSONs -> cleaned ordered blocks (CodeFormula LaTeX ->
Unicode physics, dedup, heading dedup) -> structure mapping via
book_structure_yph11.py -> segment by headings/markers -> pack (350-1600,
2400 hard max) -> JSONL + full markdown + report.

YPH11 deltas vs the 4PH1 reference:
- unit = TOPIC (1-4), chapter = the book's own A/B/C/D chapters (1-11)
- additive content types: checkpoint (CHECKPOINT self-check boxes),
  subject_vocabulary (SUBJECT VOCABULARY boxes); LEARNING TIP -> exam_hint
  family; PRACTICAL SKILLS -> practical
- page law: arabic book = pdf - 11, book 1 does not exist in the PDF
  (front matter roman i-xi = PDF 1-12, book_pages null); first arabic page
  is book 2 = PDF 13
- ID grammar: yph1_v1_u<unit|0>_c<chapter|0>_pdf<pdfpage:03d>_<block:04d>
"""
import json, re, sys, glob, collections

sys.path.insert(0, "/home/z/my-project/scripts")
from book_structure_yph11 import (CHAPTERS, EXTRA_SECTIONS, TOPIC_NAMES, OFFSET,
                                  N_PAGES, MARKERS, TYPE_PRIORITY, BOOK_TITLE,
                                  BOOK_AUTHOR, SHA256)

PAGES_DIR = "/home/z/my-project/data/yph11_sb1/docling_pages"
OUT_DIR = "/home/z/my-project/download/rag_yph11"
TARGET_MIN, TARGET_MAX, HARD_MAX, MERGE_MIN = 350, 1600, 2400, 250
FIRST_ARABIC_PDF = OFFSET + 2  # book 2 = PDF 13 (book 1 print-blank omitted)

SUB = str.maketrans("0123456789+-", "₀₁₂₃₄₅₆₇₈₉₊₋")
SUP = str.maketrans("0123456789+-", "⁰¹²³⁴⁵⁶⁷⁸⁹⁺⁻")
FRAC = {("1", "2"): "½", ("1", "3"): "⅓", ("2", "3"): "⅔", ("1", "4"): "¼",
        ("3", "4"): "¾", ("1", "8"): "⅛", ("3", "8"): "⅜", ("5", "8"): "⅝",
        ("7", "8"): "⅞", ("1", "6"): "⅙", ("5", "6"): "⅚"}

# ---------------------------------------------------------------- formulas
def latex_to_phys(latex: str):
    """Convert CodeFormula LaTeX to compact Unicode physics/math. None if not clean."""
    s = latex.strip().strip("$").strip()
    s = re.sub(r"\\\s*arrow\b", " → ", s)
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
MERGED_HEADINGS = {"KEYPOINT": "KEY POINT", "LEARNINGOBJECTIVES": "LEARNING OBJECTIVES",
                   "WORKEDEXAMPLE": "WORKED EXAMPLE", "EXAMPRACTICE": "EXAM PRACTICE",
                   "THINKINGBIGGER": "THINKING BIGGER", "THINKINGBIGGERTIP": "THINKING BIGGER TIP",
                   "DIDYOUKNOW": "DID YOU KNOW?", "SUBJECTVOCABULARY": "SUBJECT VOCABULARY",
                   "PRACTICALSKILLS": "PRACTICAL SKILLS", "CHECKPOINT": "CHECKPOINT",
                   "LEARNINGTIP": "LEARNING TIP", "MATHSSKILLSFORTHISCHAPTER": "MATHS SKILLS FOR THIS CHAPTER",
                   "SPECIFICATIONREFERENCE": "SPECIFICATION REFERENCE",
                   "PHYSICSINDETAIL": "PHYSICS IN DETAIL", "ASSESSMENTOBJECTIVE": "ASSESSMENT OBJECTIVE",
                   "COREPRACTICAL": "CORE PRACTICAL", "CHAPTERQUESTIONS": "CHAPTER QUESTIONS"}

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
    "practical_skills": "practical",
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
    if re.search(r"^PRACTICAL\s*SKILLS", up):
        return "practical"
    return None

# ------------------------------------------------------------ page context
def build_page_context():
    ctx = {p: {"unit_no": None, "unit_name": None, "chapter_no": None,
               "chapter_title": None, "base": "front_matter"} for p in range(1, N_PAGES + 1)}
    for i, (cno, unit, title, bpage) in enumerate(CHAPTERS):
        start = bpage + OFFSET
        end = (CHAPTERS[i + 1][3] + OFFSET - 1) if i + 1 < len(CHAPTERS) else N_PAGES
        # chapter_questions EXTRA_SECTIONS override the tail of each chapter
        ch_end = end
        for key, s, e, u, label, ctype in EXTRA_SECTIONS:
            if ctype == "chapter_questions" and s >= start and e <= end:
                ch_end = s - 1
        for p in range(start, ch_end + 1):
            ctx[p] = {"unit_no": unit, "unit_name": TOPIC_NAMES[unit], "chapter_no": cno,
                      "chapter_title": title, "base": "body"}
    for key, s, e, unit, label, ctype in EXTRA_SECTIONS:
        for p in range(s, e + 1):
            ctx[p] = {"unit_no": unit, "unit_name": TOPIC_NAMES.get(unit),
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
            if label == "picture" or label == "checkbox_unselected":
                continue
            if label in ("formula", "code"):
                if not text or len(text) > 600:
                    continue
                if "\\" in text or "{" in text or "frac" in text:
                    conv = latex_to_phys(text)
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
            cid = (f"yph1_v1_u{seg['unit_no'] or 0}_c{seg['chapter_no'] or 0}"
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
                # heading (e.g. 'EXAM PRACTICE' box in About this book) matches
                ctype = c["base"] if c["base"] == "front_matter" else (detect_marker(text) or c["base"])
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
    out_jsonl = f"{OUT_DIR}/edexcel_ial_physics_yph11_sb1_chunks_v1.jsonl"
    with open(out_jsonl, "w", encoding="utf-8") as f:
        for c in chunks:
            f.write(json.dumps(c, ensure_ascii=False) + "\n")
    print(f"[chunks] {len(chunks)} -> {out_jsonl}", file=sys.stderr)

    md = [f"# {BOOK_TITLE} — {BOOK_AUTHOR}", ""]
    last = None
    for c in chunks:
        key = (c["unit_no"], c["chapter_no"])
        if key != last:
            if c["unit_no"]:
                md.append(f"\n## Topic {c['unit_no']}: {c['unit_name']}")
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
        "parser": "docling 2.33.0 + rapidocr-onnxruntime 1.4.4 + CodeFormula v1 "
                  "(formula enrichment ON; no-formula retry ladder; page-level "
                  "JSON checkpoints; book = pdf-11 page law, front matter roman)",
        "formula_rescue": "docling 2.33.0 blanks formula-region text (§4.3 bug): "
                  "267/272 formula items empty after base parse; regions manually "
                  "transcribed from rendered pages (verbatim, transcription-only; "
                  "evidence data/yph11_sb1/manual_formulas.jsonl + probe_png/); "
                  "5 items were parse-native; 5 empty regions adjudicated "
                  "decorative/region-split slivers (no content loss)",
        "n_llm_polished": 0,
    }
    json.dump(report, open(f"{OUT_DIR}/parse_report_v1.json", "w"), indent=2)
    print(json.dumps(report, indent=2), file=sys.stderr)


if __name__ == "__main__":
    main()
