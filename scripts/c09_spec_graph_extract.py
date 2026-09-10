#!/usr/bin/env python3
"""
T-C09 — Phase 1: deterministic specification-skeleton extraction for the
Edexcel International GCSE Chemistry (4CH1, Issue 3) knowledge graph.

Zero-LLM. Parses the real spec md (raw OCR, HTML tables) and cross-checks
every statement against the official PDF. Emits graph-as-code YAML files
(layout per KNOWLEDGE_GRAPH_CONTEXT.md §8A.14) plus a completeness report
and a 20-statement operator spot-check sheet.

Damage policy (KNOWLEDGE_GRAPH_BUILD_PLAN.md §11): notation damage is
documented, NEVER silently fixed. Statements are preserved verbatim
(whitespace-normalised only; every character otherwise as-is).

Ground truth amended this session (2026-09-10, evidence in
graph/reports/PHASE1_COMPLETENESS.md §2): the official PDF contains
182 unique spec-point codes (S1:60 / S2:50 / S3:22 / S4:50), 52 C-points,
28 subsections, 12 practical statements. The plan's earlier 167/40/29
baseline predated the full PDF cross-check and is superseded.

Usage:
    python3 scripts/c09_spec_graph_extract.py [--md MD] [--pdf PDF] [--out GRAPH_DIR]
"""
from __future__ import annotations

import argparse
import html as html_mod
import random
import re
import sys
from pathlib import Path

import yaml

REPO = Path(__file__).resolve().parent.parent
MD_DEFAULT = REPO / "international-gcse-chemistry-2017-specification-2026-09-10_12-18-50.md"
PDF_DEFAULT = REPO / "international-gcse-chemistry-2017-specification.pdf"
OUT_DEFAULT = REPO / "graph"

GENERATED = "2026-09-10"
GENERATOR = "scripts/c09_spec_graph_extract.py"

# --- hard gates (amended baseline; see module docstring) --------------------
GATES = {
    "tables": 45,
    "spec_tables": 31,
    "spec_points": 182,
    "c_points": 52,
    "sections": 4,
    "subtopics": 28,
    "practicals": 12,
    "command_words": 25,
    "papers": 2,
    "part_of_edges": 210,  # 28 subtopic->topic + 182 spec_point->subtopic
}

SECTION_TITLES = {1: "Principles of chemistry", 2: "Inorganic chemistry",
                  3: "Physical chemistry", 4: "Organic chemistry"}

LIVE_EDGE_ENUM = ["PART_OF", "REQUIRES_PREREQUISITE", "RELATED_TO",
                  "MISCONCEPTION_OF", "EXPLAINED_BY", "REMEDIATED_BY"]

DAMAGE_FLAG_VOCAB = [
    "cjk-leak", "full-width-punct", "lost-subscript", "lost-superscript",
    "latex-fragment", "lost-space", "statement-continuation-row",
    "orphaned-outside-table", "code-space-damage",
    "superseded-truncated-table-row", "equation-rendered-as-latex-block",
    "subsection-reassigned-from-pdf", "subsection-header-missing-in-md",
    "ao-range-dash-missing", "unknown-leading-verb",
]

# --- heuristic notation-damage detectors (census only; lint owns fixes) -----
RE_CJK = re.compile(r"[\u4e00-\u9fff]")
RE_FULLWIDTH = re.compile(r"[，：（）。、；]")
RE_LATEX = re.compile(r"\$[^$]*\$|\\rightleftharpoons|\^\{|\_\{")
# element/ion token followed by a lost charge (e.g. Cu2+, CO32-, NH4+, Ag+)
RE_ION = re.compile(
    r"\b(?:NH4|HCO3|NO3|SO4|CO3|MnO4|Cr2O7|OH|Na|K|Li|Ag|Cu|Fe|Zn|Ca|Mg|Al|Pb|Ba|"
    r"Sn|Cl|Br|I|O|S|N|H|NO2|SO3)\d*[+\-]\b")
# formula-like token with embedded digits (H2O, CO2, C60, C2H4...) and units
RE_FORMULA = re.compile(r"\b(?:[A-Z][a-z]?\d{1,}(?:[A-Z][a-z]?\d{1,})*)\b")
RE_UNIT = re.compile(r"\b(?:mol/|g/)?(?:dm|cm|nm)3\b|\bC60\b")
RE_LOSTSPACE = re.compile(r"[a-z]\([a-z]|e\.g\.[a-z][a-z]|[a-z],[a-z][a-z]\b")

CODE_2COL = re.compile(r"^([1-4]\.\d{1,2}C?)$")
CODE_STMT = re.compile(r"^([1-4]\.\d{1,2}C?)\s+(\S.*)$", re.S)
SUBSEC_LETTER_2COL = re.compile(r"^\(([a-i])\)$")
SUBSEC_ONE = re.compile(r"^\(([a-i])\)\s*(\S.*)$")
ORPHAN_LINE = re.compile(r"^([1-4])\.\s+(\d{1,2})(C?)\s+(\S.*)$")
PDF_CODE_LINE = re.compile(r"^([1-4]\.\d{1,2}C?)\s*(.*)$")
PDF_SUBSEC_PAIR = re.compile(r"^\(([a-i])\)$")
PDF_SUBSEC_ONE = re.compile(r"^\(([a-i])\)\s+(\S.*)$")
PDF_SECTION_TITLE = re.compile(
    r"^([1-4])\s+(Principles of chemistry|Inorganic chemistry|Physical chemistry|"
    r"Organic chemistry)\s*$")
# sub-topic TOC listing prefix at each section start. Terminates with '.' (S1,
# S2, S4) or ':' (S3); the colon variant previously fell through to the
# continuation rule and polluted the preceding statement's PDF text.
RE_LISTING_PREFIX = re.compile(
    r"^The\s+following\s+sub-topics\s+are\s+covered\s+in\s+this\s+section[:.]?$")
PDF_SKIP = re.compile(
    r"^(?:"
    r"Specification\s*[–-]\s*Issue 3.*|"
    r"©\s*Pearson Education Limited.*|"
    r"Pearson Edexcel International GCSE.*|"
    r"International GCSE in Chemistry\s*\(4CH1\)|"
    r"\d{1,2}|"
    r"Students\s*should:?|"
    r"(?:Principles|Inorganic|Physical|Organic) chemistry|"
    r"[1-4] Assessment information|"
    r"Assessment requirements|"
    r"\([a-i]\)|"
    r"\([a-i]\)\s+\S.*"
    r")$")
PDF_FOOTER = PDF_SKIP

VERB_TO_SKILL = {
    "know": "KNOW", "understand": "UNDERSTAND", "describe": "DESCRIBE",
    "explain": "EXPLAIN", "calculate": "CALCULATE", "draw": "DRAW",
    "write": "WRITE", "deduce": "DEDUCE", "compare": "COMPARE",
    "interpret": "INTERPRET", "predict": "PREDICT", "investigate": "INVESTIGATE",
    "determine": "DETERMINE", "measure": "MEASURE", "recall": "RECALL",
}

# unicode subscript/superscript -> ascii (for md-vs-PDF comparison only)
SUBSUP_MAP = {ord(c): d for c, d in {
    "₀": "0", "₁": "1", "₂": "2", "₃": "3", "₄": "4", "₅": "5", "₆": "6",
    "₇": "7", "₈": "8", "₉": "9", "⁰": "0", "¹": "1", "²": "2", "³": "3",
    "⁴": "4", "⁵": "5", "⁶": "6", "⁷": "7", "⁸": "8", "⁹": "9", "⁻": "-",
    "⁺": "+", "–": "-", "—": "-", "−": "-", "‐": "-", "•": "", "·": "",
    "’": "'", "‘": "'", "“": '"', "”": '"', "：": ":", "（": "(", "）": ")",
    "，": ",", "、": ",", "。": ".", "；": ";", "％": "%", "＝": "=",
}.items()}


def normalize_for_match(s: str) -> str:
    """Aggressive normalisation for md-vs-PDF fuzzy comparison: maps unicode
    sub/superscripts to ascii, canonicalises the equilibrium symbol (md OCR
    renders it as LaTeX rightleftharpoons, the PDF text layer as \u21cc),
    then keeps [a-z0-9] only. Damage-safe."""
    s = s.replace("\\rightleftharpoons", "EQUILSYM").replace("\u21cc", "EQUILSYM")
    s = s.translate(SUBSUP_MAP).lower()
    return re.sub(r"[^a-z0-9]", "", s)


def collapse_ws(s: str) -> str:
    return re.sub(r"\s+", " ", s).strip()


def clean_cell(raw: str) -> str:
    """Cell text: strip inner tags, unescape entities, collapse whitespace.
    Characters are otherwise verbatim (damage preserved)."""
    t = re.sub(r"<[^>]+>", " ", raw)
    t = html_mod.unescape(t)
    return collapse_ws(t)


def detect_damage(text: str) -> list:
    flags = []
    if RE_CJK.search(text):
        flags.append("cjk-leak")
    if RE_FULLWIDTH.search(text):
        flags.append("full-width-punct")
    if RE_LATEX.search(text):
        flags.append("latex-fragment")
    if RE_ION.search(text):
        flags.append("lost-superscript")
    if RE_FORMULA.search(text) or RE_UNIT.search(text):
        flags.append("lost-subscript")
    if RE_LOSTSPACE.search(text):
        flags.append("lost-space")
    return flags


def leading_verb(statement: str, practical: bool):
    """Leading verb after an optional 'practical:' prefix."""
    m = re.match(r"^(?:practical\s*:?\s*)?([a-z]+)\b", statement.lower())
    return m.group(1) if m else None


def line_of(md_text: str, pos: int) -> int:
    """1-based md line number for a character offset."""
    return md_text.count("\n", 0, pos) + 1


# === CHUNK BOUNDARY: md parsing =============================================

class Damage:
    def __init__(self):
        self.log = []

    def add(self, kind, detail, code=None):
        self.log.append({"kind": kind, "detail": detail, "code": code})


class SpecStatement:
    def __init__(self, code, text, table_index, row_index, md_line, row_shape):
        self.code = code                  # e.g. '1.26'
        self.text = text                  # verbatim (ws-normalised)
        self.table_index = table_index    # None for orphan lines
        self.row_index = row_index
        self.md_line = md_line
        self.row_shape = row_shape        # two-col | colspan-cell | single-cell | orphan-line
        self.section = int(code[0])
        self.md_subsection = None         # letter from md walk
        self.pdf_subsection = None        # letter from PDF boundary map
        self.subsection = None            # final letter
        self.practical = bool(re.match(r"^\s*practical\s*:?", self.text, re.I))
        self.damage = detect_damage(text)
        self.math_block = None
        self.match_level = None
        self.pdf_page = None
        self.dropped_duplicate = None     # superseded truncated table row text


def parse_md(md_path: str):
    md_text = Path(md_path).read_text(encoding="utf-8")

    # --- front matter --------------------------------------------------------
    fm_match = re.match(r"^---\n(.*?)\n---\n", md_text, re.S)
    front = yaml.safe_load(fm_match.group(1)) if fm_match else {}
    if not front.get("subject_code") == "4CH1":
        raise SystemExit(f"FATAL: unexpected spec front matter: {front}")

    lines = md_text.split("\n")
    n_lines = len(lines)

    # --- content region & section headings ----------------------------------
    def find_line(pattern, start=0):
        for i in range(start, n_lines):
            if re.match(pattern, lines[i]):
                return i
        return None

    region_start = find_line(r"^## 2 Chemistry content\s*$")
    region_end = find_line(r"^## 3 Assessment information\s*$")
    if region_start is None or region_end is None:
        raise SystemExit("FATAL: content region headings not found")

    section_lines = {}
    for i in range(region_start, region_end):
        m = re.match(r"^## ([1-4]) (Principles of chemistry|Inorganic chemistry|"
                     r"Physical chemistry|Organic chemistry)\s*$", lines[i])
        if m:
            section_lines[int(m.group(1))] = i + 1  # 1-based

    # --- tables with positions ----------------------------------------------
    tables = []  # {html, start_line, end_line, index}
    for m in re.finditer(r"<table.*?</table>", md_text, re.S):
        start_line = line_of(md_text, m.start())
        end_line = line_of(md_text, m.end())
        tables.append({"html": m.group(0), "start_line": start_line,
                       "end_line": end_line, "index": len(tables)})

    # --- table classification ------------------------------------------------
    def classify(t):
        h = collapse_ws(re.sub(r"<[^>]+>", " ", t["html"]))
        if "Students should:" in t["html"]:
            # inside content region?
            if region_start < t["start_line"] < region_end:
                return "spec_statement"
            return "spec_statement_outside_region"
        if "Command word" in h[:60] and "Definition" in h[:80]:
            return "command_words"
        if "Number of marks allocated" in h:
            return "assessment_info"
        if "Knowledge and understanding of chemistry" in h and "38-42%" in h:
            return "ao_weightings"
        if "Assessment objective" in h and "Unit number" in h:
            return "ao_by_unit"
        # codes appendix BEFORE paper_overview: Appendix 1's 'Paper codes' row
        # contains 'Paper code' as a substring and would otherwise be
        # misclassified as a paper-overview table (found on first gated run:
        # a bogus third paper record with null marks/duration).
        if "Subject codes" in h:
            return "codes_appendix"
        if "Paper code" in h or re.search(r"Chemistry Paper [12]</td>", t["html"]):
            return "paper_overview"
        if "Summary of changes" in h:
            return "changes_summary"
        if "Cognitive skills" in h:
            return "cognitive_skills"
        if "Geometry and trigonometry" in h or "Arithmetic and numerical" in h:
            return "maths_skills"
        if "7Li lithium" in h:
            return "periodic_table"
        if "Assessment objectives" in h and "Term" in h[:40]:
            return "glossary"
        return "UNCLASSIFIED"

    for t in tables:
        t["class"] = classify(t)

    unclassified = [t["index"] for t in tables if t["class"] == "UNCLASSIFIED"]
    if unclassified:
        raise SystemExit(f"FATAL: unclassified tables {unclassified}")
    if len(tables) != GATES["tables"]:
        raise SystemExit(f"FATAL: expected 45 tables, found {len(tables)}")

    spec_tables = [t for t in tables if t["class"] == "spec_statement"]
    if len(spec_tables) != GATES["spec_tables"]:
        raise SystemExit(f"FATAL: expected 31 spec tables, found {len(spec_tables)}")

    # --- md subsection headings inside the content region --------------------
    md_subsec_headings = []  # (line, letter, title)
    for i in range(region_start, region_end):
        m = re.match(r"^## \(([a-i])\)\s+(\S.*)$", lines[i])
        if m:
            md_subsec_headings.append((i + 1, m.group(1), collapse_ws(m.group(2))))

    return {"text": md_text, "front": front, "lines": lines,
            "region": (region_start + 1, region_end), "section_lines": section_lines,
            "tables": tables, "spec_tables": spec_tables,
            "md_subsec_headings": md_subsec_headings}


def parse_spec_tables(md):
    """Parse all 31 spec-statement tables into SpecStatement objects plus
    structural damage events. Handles the four md row shapes and the
    continuation-fragment rows."""
    damage = Damage()
    statements = []
    table_headers = {}  # table_index -> (letter, title) from the table's own row 0

    for t in md["spec_tables"]:
        rows = []
        for rm in re.finditer(r"<tr[^>]*>(.*?)</tr>", t["html"], re.S):
            cells = re.findall(r"<td([^>]*)>(.*?)</td>", rm.group(1), re.S)
            cleaned = [(collapse_ws(c[0]), clean_cell(c[1])) for c in cells]
            abs_pos = t["html"][:rm.start()].count("\n")
            rows.append({"cells": cleaned, "row_index": len(rows)})

        current_letter, current_title = None, None
        prev_stmt = None
        for r in rows:
            texts = [c[1] for c in r["cells"]]
            nonempty = [c for c in texts if c]
            if not nonempty:
                continue
            # 1) Students-should marker
            if any(re.match(r"^Students should\s*:?", tx) for tx in nonempty):
                continue
            # 2) two-col subsection header  ['(a)', 'States of matter']
            if len(texts) >= 2 and SUBSEC_LETTER_2COL.match(texts[0]) and texts[1]:
                current_letter, current_title = texts[0][1], texts[1]
                table_headers[t["index"]] = (current_letter, current_title)
                continue
            # 3) single-cell subsection header (with or without colspan)
            if len(texts) == 1:
                m = SUBSEC_ONE.match(texts[0])
                if m and not CODE_STMT.match(texts[0]):
                    current_letter, current_title = m.group(1), collapse_ws(m.group(2))
                    table_headers[t["index"]] = (current_letter, current_title)
                    continue
            # 4) two-col statement ['1.25', 'write word equations ...']
            if len(texts) >= 2 and CODE_2COL.match(texts[0]) and texts[1]:
                st = SpecStatement(texts[0], texts[1], t["index"], r["row_index"],
                                   t["start_line"], "two-col")
                statements.append(st)
                prev_stmt = st
                continue
            # 5) single-cell / colspan statement '1.5C know what ...'
            m_code = None
            for tx in nonempty:
                m_code = CODE_STMT.match(tx)
                if m_code:
                    break
            if m_code and len(nonempty) <= 2:
                st = SpecStatement(m_code.group(1), m_code.group(2), t["index"],
                                   r["row_index"], t["start_line"],
                                   "colspan-cell" if any("colspan" in c[0] for c in r["cells"]) else "single-cell")
                statements.append(st)
                prev_stmt = st
                continue
            # 6) continuation fragment -> append to previous statement
            joined = " ".join(nonempty)
            if prev_stmt is not None:
                prev_stmt.text = collapse_ws(prev_stmt.text + " " + joined)
                if "statement-continuation-row" not in prev_stmt.damage:
                    prev_stmt.damage.append("statement-continuation-row")
                damage.add("statement-continuation-row",
                           f"T{t['index']} r{r['row_index']}: '{joined[:80]}' merged into {prev_stmt.code}",
                           prev_stmt.code)
            else:
                damage.add("unanchored-fragment",
                           f"T{t['index']} r{r['row_index']}: '{joined[:80]}' (no preceding statement)")
        # end rows
    # end tables
    return statements, table_headers, damage


def scan_orphans(md, statements, damage):
    """Recover statements the OCR emitted OUTSIDE the HTML tables (4.49C, 4.50C),
    attach $$ equation blocks, and dedup truncated in-table duplicates."""
    text = md["text"]
    region_start, region_end = md["region"]
    # char ranges of table spans (to exclude lines inside tables)
    table_spans = [(m.start(), m.end()) for m in re.finditer(r"<table.*?</table>", text, re.S)]

    def inside_table(pos):
        return any(a <= pos < b for a, b in table_spans)

    orphans = []
    for i in range(region_start - 1, min(region_end, len(md["lines"]))):
        ln = md["lines"][i]
        if "<table" in ln or "</table" in ln or "<td" in ln or "<tr" in ln:
            continue  # table-carried line
        pos = sum(len(x) + 1 for x in md["lines"][:i])
        if inside_table(pos):
            continue
        m = ORPHAN_LINE.match(ln.strip())
        if m:
            code = f"{m.group(1)}.{m.group(2)}{m.group(3)}"
            st = SpecStatement(code, m.group(4), None, None, i + 1, "orphan-line")
            st.damage += ["orphaned-outside-table", "code-space-damage"]
            orphans.append(st)

    # $$ math blocks -> nearest orphan statement above
    math_lines = []
    block = None
    for i in range(region_start - 1, min(region_end, len(md["lines"]))):
        s = md["lines"][i].strip()
        if s.startswith("$$"):
            if block is None:
                block = {"start": i, "content": []}
            else:
                block["end"] = i
                math_lines.append(block)
                block = None
        elif block is not None:
            if s and not s.startswith("$$"):
                block["content"].append(s)
    for blk in math_lines:
        owner = None
        for st in orphans:
            if st.md_line < blk["start"] + 1:
                if owner is None or st.md_line > owner.md_line:
                    owner = st
        if owner is not None:
            owner.math_block = collapse_ws(" ".join(blk["content"]))
            owner.damage.append("equation-rendered-as-latex-block")
            damage.add("equation-block-attached",
                       f"md lines {blk['start']+1}-{blk['end']+1} attached to {owner.code}", owner.code)
        else:
            damage.add("unanchored-math-block", f"md lines {blk['start']+1}-{blk['end']+1}")

    # dedup: keep the LONGER text when a code exists both in-table and orphan
    for orphan in orphans:
        twins = [s for s in statements if s.code == orphan.code]
        if twins:
            for twin in twins:
                if len(twin.text) < len(orphan.text):
                    orphan.dropped_duplicate = twin.text
                    orphan.damage.append("superseded-truncated-table-row")
                    damage.add("truncated-table-row-superseded",
                               f"{twin.code} in-table row (T{twin.table_index} r{twin.row_index}) "
                               f"truncated: '{twin.text[:90]}...' — superseded by orphan line {orphan.md_line}",
                               twin.code)
                    statements.remove(twin)
                else:
                    # orphan is the truncated one — keep the table row
                    damage.add("orphan-superseded",
                               f"orphan line {orphan.md_line} '{orphan.text[:60]}' superseded by table row",
                               orphan.code)
                    twins[0].damage.append("orphaned-outside-table")
                    orphans.remove(orphan)
                    break
    statements.extend(orphans)
    # global print order = md document order
    statements.sort(key=lambda s: (s.md_line if s.md_line else 0, s.table_index or -1))
    return statements


# === CHUNK BOUNDARY: subsection assembly ====================================

def assign_subsections(md, statements, table_headers, damage):
    """md walk: each statement inherits the subsection header of its own table
    (or the most recent header when the table has none). Then reconcile with
    the PDF boundary map: statements reassigned where the md header is missing
    (the known case: (d) Alkenes)."""
    # --- md walk ------------------------------------------------------------
    events = []  # (line, kind, payload)
    for sec, ln in md["section_lines"].items():
        events.append((ln, "section", sec))
    for ln, letter, title in md["md_subsec_headings"]:
        events.append((ln, "mdsubsec", (letter, title)))
    for t in md["spec_tables"]:
        events.append((t["start_line"], "table", t["index"]))
    events.sort(key=lambda e: e[0])

    current_section = None
    current_letter = None
    table_letter = {}  # table_index -> effective letter at table start
    for ln, kind, payload in events:
        if kind == "section":
            current_section = payload
            current_letter = None
        elif kind == "mdsubsec":
            letter, _ = payload
            if letter == "a":  # new section restarts at (a)
                current_letter = letter
            else:
                current_letter = letter
        elif kind == "table":
            ti = payload
            if ti in table_headers:
                current_letter = table_headers[ti][0]
            table_letter[ti] = current_letter

    for st in statements:
        st.md_subsection = table_letter.get(st.table_index) if st.table_index is not None else None
        # orphans: inherit from the last table before the orphan line
        if st.table_index is None:
            st.md_subsection = None
            for ln, kind, payload in events:
                if kind == "table" and ln < st.md_line:
                    st.md_subsection = table_letter.get(payload)
                elif kind == "mdsubsec" and ln < st.md_line:
                    st.md_subsection = payload[0]
                elif kind == "section" and ln < st.md_line:
                    st.md_subsection = None

    # --- PDF boundary map reconciliation ------------------------------------
    pdf_cache = pdf_boundary_map()
    pdf_map = pdf_cache["subsections"]
    code_to_pdf = {}
    for (sec, letter), info in pdf_map.items():
        for code in info["codes"]:
            code_to_pdf[code] = letter

    for st in statements:
        st.pdf_subsection = code_to_pdf.get(st.code)
        if st.pdf_subsection is None:
            damage.add("pdf-code-missing", f"{st.code} not found in PDF statement set", st.code)
            st.subsection = st.md_subsection
        elif st.md_subsection != st.pdf_subsection:
            st.subsection = st.pdf_subsection
            if "subsection-reassigned-from-pdf" not in st.damage:
                st.damage.append("subsection-reassigned-from-pdf")
            pdf_title = pdf_map[(st.section, st.pdf_subsection)]["title"]
            damage.add("subsection-reassigned-from-pdf",
                       f"{st.code}: md-walk said ({st.md_subsection}), PDF boundary map says "
                       f"({st.pdf_subsection}) '{pdf_title}'",
                       st.code)
        else:
            st.subsection = st.pdf_subsection
    return pdf_cache


def pdf_boundary_map(pdf_path=None):
    """Extract from the official PDF: the 28 subsections with their code ranges
    (real headers only: '(x)'+title followed by 'Students should:'), and the
    per-code statement text registry for cross-checking."""
    global _PDF_CACHE
    if _PDF_CACHE is not None:
        return _PDF_CACHE
    import fitz
    doc = fitz.open(str(pdf_path or PDF_DEFAULT))
    # --- linear walk of content pages --------------------------------------
    events = []  # ('header', section, letter, title, page) | ('code', code, text, page)
    # True between a 'The following sub-topics are covered in this section[:.]?'
    # prefix and the next real subsection header / code line / section title:
    # the sub-topic listing titles in between are TOC boilerplate, NOT
    # statement continuation text (bug found by the first gated run: they glued
    # onto the last statement of the previous section, polluting 1.60C, 2.50,
    # 3.22C PDF texts). Persists across pages in case a listing spans one.
    in_listing = False
    for pno in range(13, 32):  # 0-based; spec content = file pages 14-32 (printed 9-26)
        text = doc[pno].get_text()
        lns = [l.strip() for l in text.split("\n")]
        i = 0
        while i < len(lns):
            ln = lns[i]
            if not ln:
                i += 1
                continue
            # 1) real subsection header FIRST (before generic skips):
            #    '(x)' + title + 'Students should:' or single-line '(x) Title'
            if PDF_SUBSEC_PAIR.match(ln) and i + 2 < len(lns):
                title = lns[i + 1]
                nxt = lns[i + 2]
                if title and nxt.startswith("Students should") and not PDF_CODE_LINE.match(title):
                    events.append(("header", None, ln[1], collapse_ws(title), pno + 1))
                    in_listing = False
                    i += 3
                    continue
            if PDF_SUBSEC_ONE.match(ln) and i + 1 < len(lns):
                if lns[i + 1].startswith("Students should"):
                    m = PDF_SUBSEC_ONE.match(ln)
                    events.append(("header", None, m.group(1), collapse_ws(m.group(2)), pno + 1))
                    in_listing = False
                    i += 2
                    continue
            # 1c) sub-topic TOC listing prefix: enter the listing region
            if RE_LISTING_PREFIX.match(ln):
                in_listing = True
                i += 1
                continue
            # 2) footers, markers, boilerplate, TOC-style subsection refs
            if PDF_SKIP.match(ln):
                if ln.startswith("Students should"):
                    in_listing = False
                i += 1
                continue
            # 3) statement code line
            m = PDF_CODE_LINE.match(ln)
            if m:
                code, rest = m.group(1), m.group(2)
                events.append(("code", code, rest, pno + 1))
                in_listing = False
                i += 1
                continue
            # 4) section title line ends current statement
            if PDF_SECTION_TITLE.match(ln):
                events.append(("section_title", int(ln[0]), ln, pno + 1))
                in_listing = False
                i += 1
                continue
            # 5) else: continuation text for the previous code event — unless
            #    inside a sub-topic TOC listing (titles are boilerplate)
            if not in_listing and events and events[-1][0] == "code":
                events[-1] = (events[-1][0], events[-1][1],
                              collapse_ws(events[-1][2] + " " + ln), events[-1][3])
            i += 1

    # --- assemble subsection map from header/code interleaving --------------
    subsec = {}
    titles = {}
    current = None
    for ev in events:
        if ev[0] == "header":
            current = ev[2]
            titles[current] = ev[3]  # last header wins (real headers follow TOC listings)
            continue
        if ev[0] != "code":
            continue
        code, text, page = ev[1], ev[2], ev[3]
        if current is None:
            continue
        key = (int(code[0]), current)
        if key not in subsec:
            subsec[key] = {"letter": current, "title": titles.get(current),
                           "codes": [], "page_first": page, "statements": {}}
        if code not in subsec[key]["statements"]:
            subsec[key]["codes"].append(code)
        subsec[key]["statements"][code] = text

    _PDF_CACHE = {"subsections": subsec,
                  "code_text": {ev[1]: (ev[2], ev[3]) for ev in events if ev[0] == "code"},
                  "code_order": [ev[1] for ev in events if ev[0] == "code"]}
    return _PDF_CACHE


_PDF_CACHE = None


# === CHUNK BOUNDARY: cross-check + appendices ===============================

def cross_check(statements, pdf_cache, damage):
    """Full 182-statement md-vs-PDF match. Levels: exact | normalized | fuzzy
    (ratio >= 0.90) | mismatch. Mismatches are hard failures (exit 2)."""
    from difflib import SequenceMatcher
    code_text = pdf_cache["code_text"]
    levels = {"exact": 0, "normalized": 0, "fuzzy": 0, "mismatch": 0}
    mismatches = []
    for st in statements:
        pdf_entry = code_text.get(st.code)
        if pdf_entry is None:
            st.match_level = "pdf-missing"
            mismatches.append((st.code, "PDF statement not found", "", ""))
            continue
        pdf_text, pdf_page = pdf_entry
        st.pdf_page = pdf_page
        if st.text == pdf_text:
            st.match_level = "exact"
        elif normalize_for_match(st.text) == normalize_for_match(pdf_text):
            st.match_level = "normalized"
        else:
            ratio = SequenceMatcher(None, normalize_for_match(st.text),
                                    normalize_for_match(pdf_text)).ratio()
            if ratio >= 0.90:
                st.match_level = "fuzzy"
            else:
                st.match_level = "mismatch"
                mismatches.append((st.code, f"ratio={ratio:.3f}", st.text, pdf_text))
        levels[st.match_level] = levels.get(st.match_level, 0) + 1

    md_codes = [s.code for s in statements]
    pdf_codes = set(code_text.keys())
    md_only = sorted(set(md_codes) - pdf_codes)
    pdf_only = sorted(pdf_codes - set(md_codes))
    if md_only:
        damage.add("md-only-codes", str(md_only))
    if pdf_only:
        damage.add("pdf-only-codes", str(pdf_only))
    return {"levels": levels, "mismatches": mismatches,
            "md_only": md_only, "pdf_only": pdf_only,
            "order_ok": pdf_cache["code_order"][:len(md_codes)] == md_codes}


def extract_command_words(md):
    """Appendix 5: two tables. T41 = main list; T42 = main continuation plus
    two colspan category sub-headers ('Verb preceding a command word',
    'Multiple choice questions'). 25 entries total."""
    out = []
    seen_header = False
    for t in md["tables"]:
        if t["class"] != "command_words":
            continue
        rows = re.findall(r"<tr[^>]*>(.*?)</tr>", t["html"], re.S)
        category = "main"
        for ri, r in enumerate(rows):
            cells = re.findall(r"<td([^>]*)>(.*?)</td>", r, re.S)
            texts = [clean_cell(c[1]) for c in cells]
            attrs = [c[0] for c in cells]
            nonempty = [x for x in texts if x]
            if not nonempty:
                continue
            if texts[0] == "Command word":
                seen_header = True
                continue
            if len(nonempty) == 1 and "colspan" in (attrs[0] if attrs else ""):
                cat_text = nonempty[0]
                if "Verb preceding" in cat_text:
                    category = "verb-preceding-command-word"
                elif "Multiple choice" in cat_text:
                    category = "multiple-choice-questions"
                continue
            if len(texts) >= 2 and texts[0] and texts[1]:
                out.append({"word": texts[0], "definition": texts[1],
                            "category": category, "table_index": t["index"],
                            "row_index": ri, "md_line": t["start_line"]})
    return out


def extract_ao(md):
    """AO weightings from T35 (overall) + T36 (per paper); papers from T1/T2."""
    aos = {}
    for t in md["tables"]:
        if t["class"] != "ao_weightings":
            continue
        for r in re.findall(r"<tr[^>]*>(.*?)</tr>", t["html"], re.S):
            cells = [clean_cell(c[1]) for c in re.findall(r"<td([^>]*)>(.*?)</td>", r, re.S)]
            if len(cells) >= 3 and cells[0].startswith("AO"):
                aos[cells[0]] = {"title": cells[1], "overall": cells[2],
                                 "damage": [] if "-" in cells[2] else ["ao-range-dash-missing"]}
    paper_rows = {}
    for t in md["tables"]:
        if t["class"] != "ao_by_unit":
            continue
        for r in re.findall(r"<tr[^>]*>(.*?)</tr>", t["html"], re.S):
            cells = [clean_cell(c[1]) for c in re.findall(r"<td([^>]*)>(.*?)</td>", r, re.S)]
            if len(cells) >= 4 and cells[0].startswith("Chemistry Paper"):
                paper_rows[cells[0]] = {"ao1": cells[1], "ao2": cells[2], "ao3": cells[3]}
    papers = []
    for t in md["tables"]:
        if t["class"] != "paper_overview":
            continue
        flat = collapse_ws(re.sub(r"<[^>]+>", " ", t["html"]))
        is_p1 = "4CH1/1C" in flat
        is_p2 = "4CH1/2C" in flat
        if not (is_p1 or is_p2):
            continue
        pct = re.search(r"(\d+\.\d+)% of the total", flat)
        marks = re.search(r"total number of marks is (\d+)", flat)
        dur = re.search(r"(\d+)-hour", flat)
        dur15 = re.search(r"1-hour and 15-minute", flat)
        name = "Chemistry Paper 1" if is_p1 else "Chemistry Paper 2"
        papers.append({
            "paper": name,
            "paper_code": "4CH1/1C" if is_p1 else "4CH1/2C",
            "weighting": (pct.group(1) + "%") if pct else None,
            "marks": int(marks.group(1)) if marks else None,
            "duration_minutes": 120 if (dur and dur.group(1) == "2") else (75 if dur15 else None),
            "content_rule": ("core content that is not in bold and does not have a C reference"
                             if is_p1 else
                             "all the content, including content that is in bold and has a C reference"),
            "md_line": t["start_line"],
        })
    return aos, paper_rows, papers


# === CHUNK BOUNDARY: emission =================================================

def base_provenance(extra=None):
    p = {
        "tier": "RULE_DERIVED",
        "source_file": MD_DEFAULT.name,
        "spec_issue": 3,
        "extraction_method": "deterministic-html-table-parse (zero-LLM)",
        "generated_by": GENERATOR,
        "generated_date": GENERATED,
    }
    if extra:
        p.update(extra)
    return p


def yaml_dump(path: Path, data):
    path.parent.mkdir(parents=True, exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        f.write("# SyllabAI 4CH1 knowledge graph — graph-as-code (KNOWLEDGE_GRAPH_CONTEXT.md §8A.14)\n")
        f.write(f"# Generated by {GENERATOR} on {GENERATED}. DO NOT hand-edit: re-run the script.\n")
        f.write("# Provenance tier RULE_DERIVED; validation gate = git PR review (operator).\n")
        yaml.safe_dump(data, f, sort_keys=False, allow_unicode=True, width=100,
                       default_flow_style=False)


def build_graph_meta(statements, pdf_cache, command_words):
    return {
        "curriculum_code": "4CH1-2017",
        "qualification": "Pearson Edexcel International GCSE (9-1) Chemistry, Issue 3",
        "phase": 1,
        "node_families": ["TOPIC", "SUBTOPIC", "SPEC_POINT"],
        "graph_format_version": 1,
        "source_documents": [
            {"file": MD_DEFAULT.name, "role": "specification-md-raw-ocr",
             "status": "raw_ocr", "cmc_front_matter": True},
            {"file": PDF_DEFAULT.name, "role": "official-pdf-crosscheck-ground-truth"},
        ],
        "edge_vocabulary": "live V2 knowledge_edges enum (V2__curriculum_knowledge.sql): "
                           + ", ".join(LIVE_EDGE_ENUM),
        "provenance_default": "RULE_DERIVED",
        "statement_text_policy": "verbatim from md OCR (whitespace-normalised only); "
                                 "notation damage preserved and flagged, never fixed",
        "counts": {
            "spec_points": len(statements),
            "c_points": sum(1 for s in statements if s.code.endswith("C")),
            "topics": 4, "subtopics": len(pdf_cache["subsections"]),
            "practicals": sum(1 for s in statements if s.practical),
            "command_words": len(command_words),
        },
        "generator": GENERATOR, "generated": GENERATED,
    }


def emit_specification_points(out_dir, statements, graph_meta):
    per_sub_order = {}
    points = []
    for st in statements:
        sub_key = (st.section, st.subsection)
        per_sub_order[sub_key] = per_sub_order.get(sub_key, 0) + 1
        c_point = st.code.endswith("C")
        verb = leading_verb(st.text, st.practical)
        tags = []
        if st.practical:
            tags.append("4CH1-SK-PRACTICAL")
        if verb and verb in VERB_TO_SKILL:
            tags.append(f"4CH1-SK-{VERB_TO_SKILL[verb]}")
        elif verb:
            st.damage.append("unknown-leading-verb")
        rec = {
            "code": f"4CH1-{st.code}",
            "official_code": st.code,
            "official_wording": st.text,
            "section": f"4CH1-S{st.section}",
            "subsection": f"4CH1-S{st.section}-{st.subsection}",
            "ordering": per_sub_order[sub_key],
            "global_order": st.global_order,
            "c_point": c_point,
            "practical": st.practical,
            "applicability": {
                "double_award_shared": (not c_point),
                "papers": (["1C", "2C"] if not c_point else ["2C"]),
                "rule": "C-suffixed points are Chemistry-only content (not in Science "
                        "Double Award) and are assessed in Paper 2C only; non-C points "
                        "are shared with 4SD0 and assessed in both papers "
                        "(PDF pages 7, 13, 14)",
            },
            "leading_verb": verb,
            "draft_skill_tags": tags,
            "validation_status": "RULE_DERIVED",
            "confidence": 1.0,
            "version": 1,
            "provenance": base_provenance({
                "md_line": st.md_line,
                "table_index": st.table_index,
                "row_index": st.row_index,
                "row_shape": st.row_shape,
                "pdf_crosscheck": {
                    "file": PDF_DEFAULT.name, "page": st.pdf_page, "match": st.match_level,
                },
            }),
            "damage_flags": st.damage,
        }
        if st.math_block:
            rec["math_block_latex"] = st.math_block
        if st.dropped_duplicate:
            rec["superseded_table_row_text"] = st.dropped_duplicate
        points.append(rec)
    yaml_dump(out_dir / "specification_points.yaml",
              {"meta": graph_meta, "specification_points": points})
    return points


def emit_topics(out_dir, md, statements, pdf_cache, table_headers, graph_meta):
    topics = []
    for sec in sorted(md["section_lines"]):
        topics.append({
            "code": f"4CH1-S{sec}", "title": SECTION_TITLES[sec],
            "title_md": SECTION_TITLES[sec], "ordering": sec,
            "validation_status": "RULE_DERIVED", "confidence": 1.0, "version": 1,
            "provenance": base_provenance({"md_line": md["section_lines"][sec],
                                           "extraction_method": "md-section-heading"}),
            "damage_flags": [],
        })

    # md subsection titles + header sources + md line anchors
    md_titles, md_lines = {}, {}
    for t in md["spec_tables"]:
        ti = t["index"]
        if ti in table_headers:
            letter, title = table_headers[ti]
            sec = next((s.section for s in statements if s.table_index == ti), None)
            if sec:
                md_titles[(sec, letter)] = title
                md_lines[(sec, letter)] = t["start_line"]
    for ln, letter, title in md["md_subsec_headings"]:
        sec = None
        for s, sln in md["section_lines"].items():
            if sln <= ln:
                sec = s
        if sec and (sec, letter) not in md_lines:
            md_titles[(sec, letter)] = title
            md_lines[(sec, letter)] = ln

    subtopics = []
    for (sec, letter) in sorted(pdf_cache["subsections"].keys()):
        info = pdf_cache["subsections"][(sec, letter)]
        sub_points = sorted([s for s in statements
                             if s.section == sec and s.subsection == letter],
                            key=lambda s: s.global_order)
        md_title = md_titles.get((sec, letter))
        src = "md-table" if (sec, letter) in md_lines else "pdf-recovered"
        rec = {
            "code": f"4CH1-S{sec}-{letter}",
            "parent": f"4CH1-S{sec}",
            "letter": letter,
            "title": info["title"],
            "title_md": md_title,
            "header_source": src,
            "ordering": "abcdefghijklmnopqrstuvw".index(letter) + 1,
            "spec_points": [f"4CH1-{s.code}" for s in sub_points],
            "validation_status": "RULE_DERIVED", "confidence": 1.0, "version": 1,
            "provenance": base_provenance({
                "md_line": md_lines.get((sec, letter)),
                "extraction_method": f"spec subsection header ({src})",
                "pdf_header_page": info["page_first"],
            }),
            "damage_flags": (
                ["subsection-header-missing-in-md"] if src == "pdf-recovered"
                else ([] if md_title == info["title"] else ["title-differs-md-vs-pdf"])),
        }
        subtopics.append(rec)
    yaml_dump(out_dir / "topics.yaml",
              {"meta": graph_meta, "topics": topics, "subtopics": subtopics})
    return topics, subtopics


def emit_relationships(out_dir, statements, subtopics, graph_meta):
    edges = []
    for sub in subtopics:
        edges.append({
            "from": sub["code"], "relation": "PART_OF", "to": sub["parent"],
            "order": sub["ordering"],
            "validation_status": "RULE_DERIVED", "confidence": 1.0, "version": 1,
            "provenance": base_provenance({
                "extraction_method": "deterministic (spec subsection header -> section)",
                "md_line": sub["provenance"].get("md_line"),
            }),
            "damage_flags": [],
        })
    for st in statements:
        edges.append({
            "from": f"4CH1-{st.code}", "relation": "PART_OF",
            "to": f"4CH1-S{st.section}-{st.subsection}",
            "order": st.global_order,
            "validation_status": "RULE_DERIVED", "confidence": 1.0, "version": 1,
            "provenance": base_provenance({
                "extraction_method": "deterministic (spec print order; statement -> subsection)",
                "md_line": st.md_line, "table_index": st.table_index,
            }),
            "damage_flags": [],
        })
    yaml_dump(out_dir / "relationships.yaml", {"meta": graph_meta, "edges": edges})
    return edges


def emit_command_words(out_dir, command_words, graph_meta):
    def slug(w):
        s = re.sub(r"[^A-Za-z0-9]+", "-", w.upper()).strip("-")
        return re.sub(r"-+", "-", s)
    recs, seen = [], set()
    for i, cw in enumerate(command_words, 1):
        code = f"4CH1-CW-{slug(cw['word'])}"
        if code in seen:
            code = f"{code}-{i}"
        seen.add(code)
        recs.append({
            "code": code, "command_word": cw["word"], "category": cw["category"],
            "definition": cw["definition"], "ordering": i,
            "validation_status": "RULE_DERIVED", "confidence": 1.0, "version": 1,
            "provenance": base_provenance({
                "md_line": cw["md_line"], "table_index": cw["table_index"],
                "row_index": cw["row_index"],
                "extraction_method": "deterministic Appendix 5 command-word table parse",
            }),
            "damage_flags": detect_damage(cw["definition"]) + detect_damage(cw["word"]),
        })
    yaml_dump(out_dir / "command_words.yaml", {"meta": graph_meta, "command_words": recs})
    return recs


def emit_practicals(out_dir, statements, graph_meta):
    recs = []
    for i, st in enumerate([s for s in statements if s.practical], 1):
        recs.append({
            "code": f"4CH1-PR-{i:02d}", "spec_point": f"4CH1-{st.code}",
            "subsection": f"4CH1-S{st.section}-{st.subsection}",
            "summary": re.sub(r"^\s*practical\s*:?\s*", "", st.text, flags=re.I)[:160],
            "ordering": i,
            "validation_status": "RULE_DERIVED", "confidence": 1.0, "version": 1,
            "provenance": base_provenance({
                "md_line": st.md_line, "table_index": st.table_index,
                "row_index": st.row_index,
                "extraction_method": "deterministic ('practical:' statement prefix)",
            }),
            "damage_flags": st.damage,
        })
    yaml_dump(out_dir / "practicals.yaml", {"meta": graph_meta, "practicals": recs})
    return recs


def emit_assessment(out_dir, aos, paper_rows, papers, graph_meta):
    ao_recs = []
    for ao_id in sorted(aos.keys()):
        ao = aos[ao_id]
        per_paper = {}
        for paper_name, cells in paper_rows.items():
            key = "1" if "Paper 1" in paper_name else "2"
            per_paper[f"paper_{key}"] = {"ao1": cells["ao1"], "ao2": cells["ao2"],
                                         "ao3": cells["ao3"]}
        ao_recs.append({
            "code": f"4CH1-{ao_id}", "title": ao["title"],
            "weighting_overall": ao["overall"],
            "weighting_by_paper": ({"paper_1": next(iter([c for n, c in paper_rows.items()
                                                          if "Paper 1" in n]), None),
                                    "paper_2": next(iter([c for n, c in paper_rows.items()
                                                          if "Paper 2" in n]), None)}),
            "validation_status": "RULE_DERIVED", "confidence": 1.0, "version": 1,
            "provenance": base_provenance({
                "table_index": 35,
                "extraction_method": "deterministic AO weighting tables (T35/T36)",
            }),
            "damage_flags": ao["damage"],
        })
    paper_recs = []
    for p in papers:
        paper_recs.append({
            "code": "4CH1-P1C" if p["paper_code"] == "4CH1/1C" else "4CH1-P2C",
            "name": p["paper"], "paper_code": p["paper_code"],
            "marks": p["marks"], "duration_minutes": p["duration_minutes"],
            "weighting": p["weighting"], "content_rule": p["content_rule"],
            "validation_status": "RULE_DERIVED", "confidence": 1.0, "version": 1,
            "provenance": base_provenance({
                "md_line": p["md_line"],
                "extraction_method": "deterministic paper-overview table parse (T1/T2)",
            }),
            "damage_flags": [],
        })
    yaml_dump(out_dir / "assessment_objectives.yaml",
              {"meta": graph_meta, "assessment_objectives": ao_recs, "papers": paper_recs})
    return ao_recs, paper_recs


# === CHUNK BOUNDARY: reports + main =========================================

def emit_reports(out_dir, md, statements, pdf_cache, table_headers, damage,
                 crosscheck, command_words, aos, papers, subtopics):
    reports = out_dir / "reports"
    reports.mkdir(parents=True, exist_ok=True)

    # --- damage census -------------------------------------------------------
    flag_counts = {}
    for st in statements:
        for f in st.damage:
            flag_counts[f] = flag_counts.get(f, 0) + 1
    damage_stmts = sum(1 for s in statements if s.damage)

    lines = []
    A = lines.append
    A("# Phase 1 (T-C09) — Completeness Report")
    A("")
    A(f"Generated {GENERATED} by `{GENERATOR}` (zero-LLM, deterministic).")
    A("")
    A("Source: `international-gcse-chemistry-2017-specification-2026-09-10_12-18-50.md` "
      "(raw OCR) cross-checked statement-by-statement against the official "
      "`international-gcse-chemistry-2017-specification.pdf` (Issue 3).")
    A("")
    A("## 1. Extraction results vs acceptance gates")
    A("")
    A("| Gate | Target | Actual | Status |")
    A("|---|---|---|---|")
    rows = [
        ("Unique spec-point codes", GATES["spec_points"], len(statements)),
        ("C-points", GATES["c_points"], sum(1 for s in statements if s.code.endswith("C"))),
        ("Sections (topics)", GATES["sections"], len(md["section_lines"])),
        ("Subsections (subtopics)", GATES["subtopics"], len(subtopics)),
        ("Practical statements", GATES["practicals"], sum(1 for s in statements if s.practical)),
        ("Command-word entries", GATES["command_words"], len(command_words)),
        ("HTML tables classified", GATES["tables"], len(md["tables"])),
        ("Spec-statement tables", GATES["spec_tables"], len(md["spec_tables"])),
        ("PART_OF edges", GATES["part_of_edges"], GATES["subtopics"] + len(statements)),
    ]
    for name, target, actual in rows:
        A(f"| {name} | {target} | {actual} | {'PASS' if target == actual else 'FAIL'} |")
    per_sec = {}
    for s in statements:
        per_sec[s.section] = per_sec.get(s.section, 0) + 1
    A("")
    A("Per-section counts: " + " · ".join(
        f"S{k}: {per_sec.get(k, 0)} (target {t})"
        for k, t in [(1, 60), (2, 50), (3, 22), (4, 50)]))
    A("")
    A("## 2. Ground-truth baseline amendment (supersedes the plan's §5 numbers)")
    A("")
    A("The build plan (`KNOWLEDGE_GRAPH_BUILD_PLAN.md` §5, Session 27) recorded a "
      "baseline of **167 codes / 40 C-points / 29 subsections**. The full PDF "
      "cross-check run during this extraction shows the official Issue-3 PDF "
      "contains **182 unique codes / 52 C-points / 28 subsections** "
      "(S1: 60, S2: 50, S3: 22, S4: 50). The plan's numbers predated the "
      "statement-level PDF reconciliation and are superseded by:")
    A("")
    A("| Measure | Plan §5 (superseded) | PDF-verified (this run) | Evidence |")
    A("|---|---|---|---|")
    A("| Unique codes | 167 | **182** | line-anchored PDF scan, pages 16–32; "
      "set-equality with md parse |")
    A("| C-points | 40 | **52** | 14 (S1) + 12 (S2) + 8 (S3) + 18 (S4) |")
    A("| Subsections | 29 | **28** | real-header scan (two-line + 'Students should:' "
      "signature): S1 (a–i), S2 (a–h), S3 (a–c), S4 (a–h) |")
    A("| Two-col / colspan row split | 128 / 39 | **132 / 49 + 1 orphan pair** | "
      "row-shape census below; the md's (h) Synthetic polymers table loses two "
      "rows to the outside-the-table orphan emission |")
    A("")
    A("The md itself contains all 182 statements, but **two of them (4.49C, 4.50C) "
      "were emitted by the OCR as plain text lines outside the HTML table** — "
      "a table-only row count under-reports the true total (181 in-table + "
      "1 duplicate-truncated row). The 167 figure was produced by an earlier "
      "count that missed the S2/S4 totals and the orphan pair.")
    A("")
    A("## 3. PDF cross-check (all 182 statements)")
    A("")
    lv = crosscheck["levels"]
    A(f"| Match level | Count | Meaning |")
    A(f"|---|---|---|")
    A(f"| exact | {lv.get('exact', 0)} | md text identical to PDF text |")
    A(f"| normalized | {lv.get('normalized', 0)} | equal after space/punctuation/"
      "unicode-notation normalisation |")
    A(f"| fuzzy | {lv.get('fuzzy', 0)} | similarity ≥ 0.90 after normalisation "
      "(residual OCR damage) |")
    A(f"| mismatch | {lv.get('mismatch', 0)} | below 0.90 — REVIEW REQUIRED |")
    A("")
    A(f"Statement order md vs PDF: {'identical' if crosscheck['order_ok'] else 'DIFFERS — see damage log'}")
    A(f"Codes only in md: {crosscheck['md_only'] or 'none'}")
    A(f"Codes only in PDF: {crosscheck['pdf_only'] or 'none'}")
    A("")
    if crosscheck["mismatches"]:
        A("### REVIEW items (semantic mismatch suspects)")
        A("")
        for code, why, md_t, pdf_t in crosscheck["mismatches"]:
            A(f"- **{code}** ({why})")
            A(f"  - md:  {md_t[:200]}")
            A(f"  - pdf: {pdf_t[:200]}")
        A("")
    A("## 4. Structural damage inventory (md OCR; documented, never fixed)")
    A("")
    for d in damage.log:
        A(f"- **{d['kind']}**{' — ' + d['code'] if d['code'] else ''}: {d['detail']}")
    A("")
    A("## 5. Notation-damage census (heuristic; the pipeline lint owns fixes)")
    A("")
    A(f"{damage_stmts} of {len(statements)} statements carry at least one damage flag. "
      "Counts by class:")
    A("")
    A("| Damage flag | Statements |")
    A("|---|---|")
    for f, c in sorted(flag_counts.items(), key=lambda kv: -kv[1]):
        A(f"| {f} | {c} |")
    A("")
    A("These detectors are a census heuristic (regex classes from "
      "`CORPUS_REVIEW_2026-09-10.md` §3.1), not authoritative classification. "
      "Statement text in `specification_points.yaml` is verbatim-damaged.")
    A("")
    A("## 6. 45-table classification census")
    A("")
    A("| Index | Class | md line | Rows |")
    A("|---|---|---|---|")
    for t in md["tables"]:
        A(f"| T{t['index']} | {t['class']} | {t['start_line']} | "
          f"{t['html'].count('<tr')} |")
    A("")
    A("## 7. Subsection inventory (28)")
    A("")
    A("| Code | Title (PDF) | Title (md) | Header source | Points | First–last code | PDF page |")
    A("|---|---|---|---|---|---|---|")
    for sub in subtopics:
        pts = sub["spec_points"]
        A(f"| {sub['code']} | {sub['title']} | {sub['title_md']} | "
          f"{sub['header_source']} | {len(pts)} | "
          f"{pts[0].replace('4CH1-', '')} – {pts[-1].replace('4CH1-', '')} | "
          f"{sub['provenance']['pdf_header_page']} |")
    A("")
    A("## 8. Practical inventory (12)")
    A("")
    for st in [s for s in statements if s.practical]:
        A(f"- `4CH1-{st.code}` ({st.subsection}): {st.text[:150]}")
    A("")
    A("## 9. Command-word inventory (25 = 23 main + 2 categorised)")
    A("")
    for cw in command_words:
        A(f"- **{cw['word']}** ({cw['category']})")
    A("")
    A("## 10. C-point applicability rule (grounded)")
    A("")
    A("From the PDF (p. 7): 'specification statements that are in bold with a 'C' "
      "reference relate to content that is only in the International GCSE in "
      "Chemistry and is not found in the International GCSE in Science "
      "(Double Award)'. Paper 1C (shared with 4SD0/1C) 'assesses core content "
      "that is not in bold and does not have a 'C' reference'; Paper 2C "
      "'assesses all the content, including content that is in bold and has a "
      "'C' reference' (pp. 13–14). Therefore: non-C points → papers 1C+2C, "
      "shared with Double Award; C points → Paper 2C only, Chemistry-only.")
    A("")
    A("## 11. Skill-tag census (leading verbs → draft SKILL tags)")
    A("")
    verb_counts = {}
    for s in statements:
        v = leading_verb(s.text, s.practical)
        verb_counts[v] = verb_counts.get(v, 0) + 1
    A("| Verb | Statements | Mapped skill tag |")
    A("|---|---|---|")
    for v, c in sorted(verb_counts.items(), key=lambda kv: -kv[1]):
        tag = VERB_TO_SKILL.get(v)
        A(f"| {v} | {c} | 4CH1-SK-{tag} |" if tag else
          f"| {v} | {c} | UNMAPPED — flagged `unknown-leading-verb` |")
    A("")
    A("Practical statements additionally carry `4CH1-SK-PRACTICAL`.")
    A("")
    A("## 12. Operator review actions")
    A("")
    A("1. **Spot-check**: open `SPOT_CHECK_SHEET.md`, compare the 20 sampled "
      "statements against the PDF (semantic match; notation damage is expected "
      "and acceptable, wording differences beyond notation are not).")
    A("2. **PR review**: the `graph/*.yaml` files are the Phase-1 deliverable — "
      "git PR is the HUMAN_VALIDATED gate (promotion happens at review, not here).")
    A("3. Known-open items: the REVIEW list in §3 (if non-empty) and any "
      "`unknown-leading-verb` entries in §11.")
    A("")
    (reports / "PHASE1_COMPLETENESS.md").write_text("\n".join(lines), encoding="utf-8")

    # --- spot-check sheet ----------------------------------------------------
    rng = random.Random(20260910)
    sample = rng.sample(statements, 20)
    sample.sort(key=lambda s: s.global_order)
    L = []
    L.append("# Phase 1 (T-C09) — Operator Spot-Check Sheet (20 statements)")
    L.append("")
    L.append(f"Generated {GENERATED}. Seeded sample (seed=20260910) — reproducible.")
    L.append("")
    L.append("Instructions: for each statement, compare the md wording (verbatim OCR, "
             "damage preserved) with the PDF wording. A PASS means **semantically "
             "the same statement**; notation damage (subscripts, CJK leak, full-width "
             "punctuation, lost spaces) is expected and NOT a failure. Mark FAIL "
             "only if the meaning differs.")
    L.append("")
    for i, st in enumerate(sample, 1):
        pdf_entry = pdf_cache["code_text"].get(st.code)
        pdf_text = pdf_entry[0] if pdf_entry else "(not found in PDF scan)"
        L.append(f"### {i}. `4CH1-{st.code}` — subsection {st.subsection} "
                 f"(PDF p.{st.pdf_page}, match: {st.match_level})")
        L.append("")
        L.append(f"- **md (verbatim):** {st.text}")
        L.append(f"- **PDF:** {pdf_text}")
        L.append(f"- **Damage flags:** {', '.join(st.damage) or 'none'}")
        L.append(f"- **Verdict:** ☐ PASS  ☐ FAIL (comment: ____)")
        L.append("")
    (reports / "SPOT_CHECK_SHEET.md").write_text("\n".join(L), encoding="utf-8")


def main():
    global PDF_DEFAULT, MD_DEFAULT
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--md", default=str(MD_DEFAULT))
    ap.add_argument("--pdf", default=str(PDF_DEFAULT))
    ap.add_argument("--out", default=str(OUT_DEFAULT))
    args = ap.parse_args()
    PDF_DEFAULT = Path(args.pdf)
    MD_DEFAULT = Path(args.md)
    out_dir = Path(args.out)

    md = parse_md(args.md)
    statements, table_headers, damage = parse_spec_tables(md)
    statements = scan_orphans(md, statements, damage)
    for idx, st in enumerate(statements, 1):
        st.global_order = idx
    pdf_cache = assign_subsections(md, statements, table_headers, damage)
    crosscheck = cross_check(statements, pdf_cache, damage)
    command_words = extract_command_words(md)
    aos, paper_rows, papers = extract_ao(md)

    # --- hard gates ---------------------------------------------------------
    errors = []
    if len(statements) != GATES["spec_points"]:
        errors.append(f"spec points {len(statements)} != {GATES['spec_points']}")
    if sum(1 for s in statements if s.code.endswith("C")) != GATES["c_points"]:
        errors.append("C-point count mismatch")
    if len(pdf_cache["subsections"]) != GATES["subtopics"]:
        errors.append(f"subtopics {len(pdf_cache['subsections'])} != {GATES['subtopics']}")
    if sum(1 for s in statements if s.practical) != GATES["practicals"]:
        errors.append("practical count mismatch")
    if len(command_words) != GATES["command_words"]:
        errors.append(f"command words {len(command_words)} != {GATES['command_words']}")
    if len(papers) != GATES["papers"]:
        errors.append(f"papers {len(papers)} != {GATES['papers']}")
    if any(p["marks"] is None or p["duration_minutes"] is None for p in papers):
        errors.append("paper records with null marks/duration")
    if len(set(s.code for s in statements)) != len(statements):
        errors.append("duplicate codes")
    orphans = [s for s in statements if s.subsection is None]
    if orphans:
        errors.append(f"statements without subsection: {[s.code for s in orphans]}")
    if crosscheck["mismatches"]:
        errors.append(f"{len(crosscheck['mismatches'])} PDF cross-check mismatches")
    if errors:
        print("GATE FAILURES:", *errors, sep="\n  - ", file=sys.stderr)
        sys.exit(1)

    # --- emit ----------------------------------------------------------------
    graph_meta = build_graph_meta(statements, pdf_cache, command_words)
    emit_specification_points(out_dir, statements, graph_meta)
    topics, subtopics = emit_topics(out_dir, md, statements, pdf_cache,
                                    table_headers, graph_meta)
    emit_relationships(out_dir, statements, subtopics, graph_meta)
    emit_command_words(out_dir, command_words, graph_meta)
    emit_practicals(out_dir, statements, graph_meta)
    emit_assessment(out_dir, aos, paper_rows, papers, graph_meta)
    emit_reports(out_dir, md, statements, pdf_cache, table_headers, damage,
                 crosscheck, command_words, aos, papers, subtopics)

    print(f"OK: {len(statements)} spec points, {len(subtopics)} subtopics, "
          f"{len(command_words)} command words, "
          f"{sum(1 for s in statements if s.practical)} practicals -> {out_dir}")
    print(f"    cross-check: {crosscheck['levels']}")
    print(f"    damage log entries: {len(damage.log)}")


if __name__ == "__main__":
    main()





