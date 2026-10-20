#!/usr/bin/env python3
"""Build RAG chunks for the 4BI1 BIOLOGY book from text-layer half-page JSONs
(data/biology/text_pages/ — extract_text_4bi1.py).

TEXT-LAYER LANE (first in the playbook): PyMuPDF native extraction instead of
Docling OCR — the source is a Word-2016 print-replica, not a scan.

Pipeline: half-page JSONs -> cleaned ordered lines (icon-junk strip, dash-rule
drop, whitespace normalize) -> structure mapping via book_structure_biology.py
(per-HALF context: 2-up spreads carry two book pages) -> segment by
headings/inline markers/context -> pack (350-1600 target, 2400 hard max) ->
15-key JSONL + full markdown + parse report.

Chunk ID: bio_v1_u<unit|0>_c<chapter|0>_pdf<spread:03d>_<seq:04d>
pdf_pages = [start_spread, end_spread] (viewer numbering of the 2-up PDF)
book_pages = [first, last] numbered book pages covered (null for front/back
matter) — PARSE_STANDARD point 1 dual numbering.
Adapted from the audited physics pipeline (parse_docling_physics.py).
"""
import json, re, sys, glob, collections

sys.path.insert(0, "/home/z/my-project/syllabai-resources/books/pearson-edexcel/"
                   "international-gcse/biology/4bi1/pipeline/scripts")
from book_structure_biology import (
    CHAPTERS, QUESTION_RANGES, EXTRA_SECTIONS, UNIT_NAMES,
    N_SPREADS, MARKERS, TYPE_PRIORITY, BOOK_TITLE, BOOK_AUTHOR, SHA256,
    PAGES_DIR, OUT_DIR, TARGET_MIN, TARGET_MAX, HARD_MAX, MERGE_MIN,
    book_page_of, spread_side_of, FRONT_MATTER_SPREADS, BACK_COVER_HALVES,
)

SUB = str.maketrans("0123456789+-", "₀₁₂₃₄₅₆₇₈₉₊₋")   # reserved (not applied
SUP = str.maketrans("0123456789+-", "⁰¹²³⁴⁵⁶⁷⁸⁹⁺⁻")   # in v1; see report)

# ------------------------------------------------------------ line cleanup
# DECISION (PM-4 discipline): the first cleaner draft token-dropped anything
# without 3+ consecutive letters — that silently ate two-letter words
# ("composed of" -> "composed", "with or without" -> "with without"),
# corpus-destroying. The surviving cleaner is SURGICAL:
#   1. salvage skill words merged with icon junk ("mDANAlYSIS" -> "ANALYSIS",
#      "~REASONING" -> "REASONING")
#   2. drop dash-rule lines (decorative rules rendered as text)
#   3. everything else verbatim — residual icon glyphs ("mD", "11>", ~150
#      tokens book-wide) are left for the LLM fidelity polish phase.
SKILL_RX = re.compile(r"CRITICAL\s*THINKING|ANALYSIS|REASONING|INTERPRETATION|"
                      r"DECISION\s*MAKING|PROBLEM\s*SOLVING|EXECUTIVE\s*FUNCTION|"
                      r"MATHEMATICS|PRACTICAL\s*SKILLS?", re.I)
ROMAN_OK = None  # retired (was part of the destructive draft cleaner)
LO_ITEM_RX = re.compile(r"^(?:[\u2022e_]|[0-9]{1,2})\s+"
                        r"(Understand|Know|Describe|Explain|Recall|Investigate|"
                        r"Be\s+able|Demonstrate|Apply|Carry\s+out|Use)\b", re.I)
DASH_RUN = re.compile(r"^[-_=~.\u2014\u2013\u00b7]{6,}$")
MULTISPACE = re.compile(r"[ \t]{2,}")

def clean_line(text: str) -> str:
    """Salvage skill words from icon-merged tokens; keep all else verbatim."""
    tokens = text.split()
    keep = []
    for tok in tokens:
        has_junk = re.search(r"[\W_}\]>{(!:=~]", tok) is not None
        m = SKILL_RX.findall(tok)
        if m and has_junk:
            # icon glyph merged with skill word (or pure skill token with
            # trailing punctuation) — keep only the skill words
            keep.extend(m)
            continue
        keep.append(tok)
    return MULTISPACE.sub(" ", " ".join(keep)).strip()

# ----------------------------------------------------------------- markers
CT_MAP = {
    "learning_objectives": "learning_objectives",
    "chapter_questions": "chapter_questions",
    "unit_questions": "unit_questions",
    "activity": "activity",
    "practical": "practical",
    "extension_work": "extension_work",
    "key_point": "key_point",
    "did_you_know": "did_you_know",
    "exam_hint": "exam_hint",
    "biology_only": "biology_only",
    "safety": "safety",
}
PRIO = {t: i for i, t in enumerate(TYPE_PRIORITY)}

def detect_marker(text: str):
    up = text.strip()
    if len(up) > 60:
        return None
    for key, rx in MARKERS.items():
        if key == "safety":
            if re.search(rx, text):
                return CT_MAP[key]
            continue
        if re.search(rx, up, re.I if key in ("did_you_know", "exam_hint") else 0):
            return CT_MAP[key]
    return None

# ------------------------------------------------------------ page context
def build_page_context():
    """ctx[(spread, side)] = dict(unit_no, unit_name, chapter_no,
    chapter_title, base). Later overrides earlier."""
    ctx = {}
    for sp in range(1, N_SPREADS + 1):
        for side in ("L", "R"):
            ctx[(sp, side)] = {"unit_no": None, "unit_name": None,
                               "chapter_no": None, "chapter_title": None,
                               "base": "body"}
    # chapters (body ranges = full range; question ranges override below)
    for i, (cno, unit, title, start) in enumerate(CHAPTERS):
        nxt = CHAPTERS[i + 1][3] if i + 1 < len(CHAPTERS) else 350
        end = nxt - 1
        for bp in range(start, end + 1):
            sp, side = spread_side_of(bp)
            ctx[(sp, side)] = {"unit_no": unit, "unit_name": UNIT_NAMES[unit],
                               "chapter_no": cno, "chapter_title": title,
                               "base": "body", "is_opener": bp == start}
    # chapter end-of-chapter question sections (serving-critical)
    for cno, bp0, bp1 in QUESTION_RANGES:
        unit, title = next((u, t) for c, u, t, _s in CHAPTERS if c == cno)
        for bp in range(bp0, bp1 + 1):
            sp, side = spread_side_of(bp)
            ctx[(sp, side)] = {"unit_no": unit, "unit_name": UNIT_NAMES[unit],
                               "chapter_no": cno, "chapter_title": title,
                               "base": "chapter_questions"}
    # extra sections
    for key, bp0, bp1, unit, label, ctype in EXTRA_SECTIONS:
        for bp in range(bp0, bp1 + 1):
            sp, side = spread_side_of(bp)
            ctx[(sp, side)] = {"unit_no": unit, "unit_name": UNIT_NAMES.get(unit),
                               "chapter_no": None, "chapter_title": label,
                               "base": ctype}
    # front matter: spreads 1-5, all halves EXCEPT (5,R)=skills handled by
    # EXTRA_SECTIONS above (skills bp1 -> spread 5 R). Override remaining.
    for sp in range(FRONT_MATTER_SPREADS[0], FRONT_MATTER_SPREADS[1] + 1):
        for side in ("L", "R"):
            if (sp, side) == spread_side_of(1):   # book page 1 = skills
                continue
            ctx[(sp, side)] = {"unit_no": None, "unit_name": None,
                               "chapter_no": None,
                               "chapter_title": "Front matter (cover, contents, course structure, about this book, assessment overview)",
                               "base": "front_matter"}
    # back cover (blank, image-only)
    bsp, bside = BACK_COVER_HALVES
    ctx[(bsp, bside)] = {"unit_no": None, "unit_name": None, "chapter_no": None,
                         "chapter_title": "Back cover", "base": "back_cover"}
    return ctx

# ------------------------------------------------------------------ blocks
def load_blocks():
    """Yield (spread, side, kind, text) in natural book order (spread-major,
    L then R; natural content-stream order within each half)."""
    n_lines = n_dropped = 0
    for sp in range(1, N_SPREADS + 1):
        fp = f"{PAGES_DIR}/page_{sp:03d}.json"
        d = json.load(open(fp))
        for side in ("L", "R"):
            for row in d["body_lines"][side]:
                y0, x0, x1, raw, size, bold, italic = row
                text = raw.strip()
                if not text or DASH_RUN.match(text):
                    n_dropped += 1
                    continue
                text = clean_line(text)
                if not text:
                    n_dropped += 1
                    continue
                n_lines += 1
                # kind: heading if large or caps-ish short line, else para
                letters = [c for c in text if c.isalpha()]
                caps = sum(1 for c in letters if c.isupper()) / max(1, len(letters))
                if size >= 10.0 or (size >= 7.6 and caps >= 0.72 and len(text) <= 70):
                    kind = "heading"
                else:
                    kind = "para"
                yield (sp, side, kind, text, size)
    print(f"[blocks] lines kept={n_lines} dropped={n_dropped}", file=sys.stderr)

# ------------------------------------------------------------------ chunks
def split_long(text: str, max_len: int = 1900):
    """Split an oversized block: sentences first, then lines (index/glossary
    entries have no periods), then hard word-splits as last resort (L-009)."""
    parts, cur = [], ""
    sents = re.split(r"(?<=[.!?;]) +", text)
    if len(sents) == 1 and len(text) > max_len:
        sents = [ln for ln in text.splitlines() if ln.strip()] or [text]
    for s in sents:
        while len(s) > max_len:
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
        cur, cur_size, out = [], 0, []
        for kind, text in blocks:
            if cur_size >= TARGET_MIN and cur_size + len(text) > TARGET_MAX:
                out.append(cur)
                cur, cur_size = [], 0
            elif cur_size and cur_size + len(text) + 2 > HARD_MAX:
                # strict HARD_MAX: break BEFORE appending (a piece must never
                # exceed 2400 even when cur_size < TARGET_MIN)
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
            if size < 20:
                continue
            self.idx += 1
            sp0, side0 = seg["start"]
            sp1, side1 = seg["end"]
            bp0 = book_page_of(sp0, side0)
            bp1 = book_page_of(sp1, side1)
            book_pages = [bp0, bp1] if (bp0 is not None and bp1 is not None) else None
            cid = (f"bio_v1_u{seg['unit_no'] or 0}_c{seg['chapter_no'] or 0}"
                   f"_pdf{sp0:03d}_{self.idx:04d}")
            self.chunks.append({
                "id": cid,
                "book_title": BOOK_TITLE,
                "author": BOOK_AUTHOR,
                "unit_no": seg["unit_no"], "unit_name": seg["unit_name"],
                "chapter_no": seg["chapter_no"], "chapter_title": seg["chapter_title"],
                "section": seg["section"],
                "content_type": seg["ctype"],
                "book_pages": book_pages,
                "pdf_pages": [sp0, sp1],
                "text": "\n\n".join(t for _, t in piece),
                # char_count MUST be computed from the final text (a first
                # draft computed it from tuple lengths — bug caught in review)
                "char_count": len("\n\n".join(t for _, t in piece)),
            })

    def run(self, blocks, ctx):
        seg = None

        def new_seg(sp, side, section, ctype):
            c = ctx[(sp, side)]
            return {"blocks": [], "section": section, "ctype": ctype,
                    "start": (sp, side), "end": (sp, side),
                    "unit_no": c["unit_no"], "unit_name": c["unit_name"],
                    "chapter_no": c["chapter_no"], "chapter_title": c["chapter_title"]}

        cur_key = None
        for sp, side, kind, text, size in blocks:
            c = ctx[(sp, side)]
            key = (c["unit_no"], c["chapter_no"], c["base"])
            if key != cur_key:
                if seg:
                    self.flush(seg)
                seg = new_seg(sp, side, None, c["base"])
                cur_key = key
            # guarded context types: question banks and answers keep their
            # type regardless of inline markers (PARSE_STANDARD point 3)
            GUARDED = {"chapter_questions", "unit_questions", "answers",
                       "glossary", "index", "appendix", "front_matter",
                       "divider", "skills", "back_cover"}
            marker = detect_marker(text)
            if kind == "heading":
                if seg and seg["blocks"]:
                    self.flush(seg)
                if c["base"] in GUARDED:
                    ctype = c["base"]
                else:
                    ctype = marker or c["base"]
                seg = new_seg(sp, side, text, ctype)
                seg["blocks"].append(("heading", text))
            elif marker and c["base"] not in GUARDED:
                # inline box heading (DID YOU KNOW? / KEY POINT / ACTIVITY n /
                # Safety Note: / BIOLOGY ONLY ...): split only if it outranks
                cur_type = seg["ctype"] if seg else "body"
                if PRIO.get(marker, 0) > PRIO.get(cur_type, 0):
                    if seg and seg["blocks"]:
                        self.flush(seg)
                    seg = new_seg(sp, side, None, marker)
                seg["blocks"].append((kind, text))
                seg["end"] = (sp, side)
            else:
                if seg is None:
                    seg = new_seg(sp, side, None, c["base"])
                # opener fallback: chapters whose LEARNING OBJECTIVES heading
                # is CMap-garbled (probe: 7/22) still carry the bullet list;
                # a verb-bullet line on an opener half starts the LO segment
                if (c.get("is_opener") and c["base"] == "body"
                        and LO_ITEM_RX.match(text)
                        and (seg["ctype"] == "body" or not seg["blocks"])):
                    if seg and seg["blocks"]:
                        self.flush(seg)
                    seg = new_seg(sp, side, None, "learning_objectives")
                seg["blocks"].append((kind, text))
                seg["end"] = (sp, side)
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
                and ((merged[-1]["book_pages"] and c["book_pages"]
                      and merged[-1]["book_pages"][1] >= c["book_pages"][0] - 1)
                     or (merged[-1]["book_pages"] is None
                         and c["book_pages"] is None))):
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

    import os
    os.makedirs(OUT_DIR, exist_ok=True)
    out_jsonl = f"{OUT_DIR}/edexcel_igcse_biology_chunks_v1.jsonl"
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
                md.append(f"\n## Unit {c['unit_no']}: {c['unit_name']}")
            md.append(f"\n### {c['chapter_title']}\n")
            last = key
        if c["section"] and c["text"].split("\n\n")[0] != c["section"]:
            md.append(f"\n#### {c['section']}")
        md.append(c["text"])
    with open(f"{OUT_DIR}/full_book_textlayer.md", "w", encoding="utf-8") as f:
        f.write("\n".join(md))

    types = collections.Counter(c["content_type"] for c in chunks)
    sizes = sorted(c["char_count"] for c in chunks)
    report = {
        "n_chunks": len(chunks), "content_types": dict(types),
        "size_min": sizes[0], "size_max": sizes[-1],
        "size_avg": round(sum(sizes) / len(sizes)),
        "n_chunks_over_hardmax": sum(1 for s in sizes if s > HARD_MAX),
        "source_pdf_sha256": SHA256,
        "parser": ("PyMuPDF 1.26.7 native text layer (2-up spreads split at "
                   "x-midpoint; natural content-stream order; icon-junk strip; "
                   "no OCR) — text-layer lane, first in playbook"),
        "n_llm_polished": 0,
        "known_limitations": [
            "chemical formulas keep plain digits (CO2 not CO2 subscript) — "
            "span-size sub/sup conversion rejected: garbled display-font "
            "bullets ('11') mimic small spans; candidate for additive v2",
            "broken-CMap display/italic font garbles (e.g. chapler/U1e/KEV) "
            "left as-is in v1; LLM fidelity polish phase handles them",
        ],
    }
    json.dump(report, open(f"{OUT_DIR}/parse_report_v1.json", "w"), indent=2)
    print(json.dumps(report, indent=2), file=sys.stderr)


if __name__ == "__main__":
    main()
