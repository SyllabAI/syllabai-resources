#!/usr/bin/env python3
"""Parsing library: page loading, OCR cleaning, block segmentation.
Used by parse_book.py. Prints only stats, never book text."""
import os
import re
from book_structure import OCR_DIR, UNIT_NAME_CAPS, MARKERS, ELEMENTS

LIGATURES = {"\ufb00": "ff", "\ufb01": "fi", "\ufb02": "fl", "\ufb03": "ffi",
             "\ufb04": "ffl", "\u2018": "'", "\u2019": "'", "\u201c": '"',
             "\u201d": '"', "\u2013": "-", "\u2014": "-", "\u00a0": " "}

ROMAN_JUNK = re.compile(r"\s+[ivxlcdm]{1,7}\s*[i=\[\-|]*\s*$")
PAGE_NUM_ONLY = re.compile(r"^\d{1,3}$")
HEADER_WITH_PAGE = re.compile(r"^\d{1,3}\s+[A-Z][A-Za-z ,'-]{2,60}$")
FOOTER_A = re.compile(r"^\d{1,3}\s+[A-Z]{3,30}$")
FOOTER_B = re.compile(r"^[A-Z]{3,30}\s+\d{1,3}$")
NO_ALNUM = re.compile(r"^[^A-Za-z0-9]*$")
ALL_CAPS = re.compile(r"^[A-Z][A-Z0-9 ,'()&?/-]{3,70}$")
CAPTION_LABEL = re.compile(
    r"^(FIGURE|FIG|TABLE|EXAMPLE|STEP|ANSWER|QUESTION|PHOTO|SOURCE|PART)\b", re.I)
MARKER_RES = {k: re.compile(v, re.I | re.M) for k, v in MARKERS.items()}
MARKER_LINE_RES = {k: re.compile(v, re.I) for k, v in MARKERS.items()}

def book_page(pdf_no: int) -> int:
    return pdf_no - 9

def load_page_lines(pdf_no: int):
    """Read OCR text of one PDF page, clean it, return (lines, dropped_header)."""
    path = os.path.join(OCR_DIR, f"page_{pdf_no:03d}.txt")
    with open(path, encoding="utf-8") as f:
        raw = f.read()
    for k, v in LIGATURES.items():
        raw = raw.replace(k, v)
    lines = [re.sub(r"\s{2,}", " ", ln).strip() for ln in raw.splitlines()]
    lines = [ln for ln in lines if ln and not NO_ALNUM.match(ln)]
    dropped = None
    # --- running header (first line) ---
    if lines:
        first = lines[0]
        is_header = False
        if pdf_no >= 11:
            if any(u in first for u in UNIT_NAME_CAPS) and len(first) < 72:
                is_header = True
            elif HEADER_WITH_PAGE.match(first) and len(first) < 72:
                is_header = True
            elif PAGE_NUM_ONLY.match(first):
                is_header = True
        else:
            # front matter: only drop obvious running heads
            if re.match(r"^ABOUT THIS BOO[K]?\b", first) and len(first) < 40:
                is_header = True
        if is_header:
            dropped = first
            lines = lines[1:]
    # strip trailing roman-numeral junk from remaining lines (TOC pages)
    lines = [ROMAN_JUNK.sub("", ln) for ln in lines]
    # --- running footer (last two lines) ---
    for _ in range(2):
        if lines and (PAGE_NUM_ONLY.match(lines[-1]) or FOOTER_A.match(lines[-1])
                      or FOOTER_B.match(lines[-1]) and len(lines[-1]) < 30):
            lines = lines[:-1]
    # de-hyphenate across line breaks
    merged = []
    i = 0
    while i < len(lines):
        cur = lines[i]
        while (cur.endswith("-") and i + 1 < len(lines)
               and lines[i + 1][:1].islower()):
            nxt = lines[i + 1]
            cur = cur[:-1] + nxt
            i += 1
        merged.append(cur)
        i += 1
    return merged, dropped

def is_all_caps_heading(line: str) -> bool:
    """True if line looks like a genuine in-page sub-heading."""
    if not ALL_CAPS.match(line):
        return False
    if CAPTION_LABEL.match(line):
        return False
    for pat in MARKER_LINE_RES.values():  # markers are handled separately
        if pat.match(line):
            return False
    words = line.split()
    if len(words) < 2:
        return False
    # reject lines that are mostly single letters/numbers (equations, labels)
    alpha = sum(c.isalpha() for c in line)
    if alpha < 0.6 * len(line.replace(" ", "")):
        return False
    return True

def marker_of(line: str):
    for key, pat in MARKER_LINE_RES.items():
        if pat.match(line):
            return key
    return None

def build_blocks(pdf_start: int, pdf_end: int):
    """Segment a page range into blocks: (topic, marker, text, pdf_page).
    topic=None until a sub-heading appears; text joined per cleaned lines."""
    blocks = []
    cur_topic, cur_marker, cur_lines, cur_page = None, None, [], None

    def flush():
        nonlocal cur_topic, cur_marker, cur_lines, cur_page
        if cur_lines and any(ln for ln in cur_lines):
            blocks.append((cur_topic, cur_marker,
                           "\n".join(ln for ln in cur_lines if ln), cur_page))
        cur_topic, cur_marker, cur_lines, cur_page = None, None, [], None

    for p in range(pdf_start, pdf_end + 1):
        lines, _hdr = load_page_lines(p)
        i = 0
        while i < len(lines):
            ln = lines[i]
            mk = marker_of(ln)
            if mk:
                flush()
                cur_topic, cur_marker, cur_lines, cur_page = (
                    None, mk, [ln], p)
                i += 1
                continue
            if is_all_caps_heading(ln):
                # join wrapped all-caps heading (up to 2 continuation lines)
                heading = ln
                while (i + 1 < len(lines) and is_all_caps_heading(lines[i + 1])
                       and not heading.endswith((".", ":", ";"))):
                    i += 1
                    heading += " " + lines[i]
                flush()
                cur_topic = heading.title()
                cur_marker, cur_lines, cur_page = None, [], p
                i += 1
                continue
            if cur_page is None:
                cur_page, cur_topic = p, cur_topic
            cur_lines.append(ln)
            i += 1
    flush()
    return blocks

def normalize_formulas(text: str):
    """Conservative chemical-formula rejoining; returns (text, n_changes, examples)."""
    changes = 0
    examples = []
    def sub_element_digit(m):
        nonlocal changes
        tok, num = m.group(1), m.group(2)
        changes += 1
        if len(examples) < 12:
            examples.append(f"{tok} {num} -> {tok}{num}")
        return tok + num
    # element symbol + standalone number  (CO 2 -> CO2, H 2 -> H2)
    pattern = re.compile(r"\b([A-Z][a-z]?)\s+(\d{1,3})\b")
    out, pos = [], 0
    for m in pattern.finditer(text):
        out.append(text[pos:m.start()])
        tok, num = m.group(1), m.group(2)
        if tok in ELEMENTS and num.isdigit():
            out.append(tok + num)
            changes += 1
            if len(examples) < 12:
                examples.append(f"{tok} {num} -> {tok}{num}")
        else:
            out.append(m.group(0))
        pos = m.end()
    out.append(text[pos:])
    text = "".join(out)
    # ion charges: Mg 2+ -> Mg2+,  Na + -> Na+
    charge = re.compile(r"\b([A-Z][a-z]?)\s+(\d?)\s*([+])\b")
    text, n1 = charge.subn(lambda m: m.group(1) + m.group(2) + "+", text)
    charge2 = re.compile(r"\b([A-Z][a-z]?)\s+(\d?)\s*([-−])\b")
    text, n2 = charge2.subn(lambda m: m.group(1) + m.group(2) + "-", text)
    changes += n1 + n2
    return text, changes, examples
