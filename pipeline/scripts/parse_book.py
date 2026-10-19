#!/usr/bin/env python3
"""Main parser: OCR text -> cleaned, structure-aware RAG chunks.
Outputs: JSONL chunks + full clean markdown + parse report + loader helper."""
import json
import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from book_structure import (BOOK_TITLE, BOOK_AUTHOR, SOURCE_URL, OUT_DIR,
                            N_PAGES, CHAPTERS, EXTRA_SECTIONS, UNIT_NAMES,
                            TYPE_PRIORITY, TARGET_MIN, TARGET_MAX, HARD_MAX,
                            MERGE_MIN)
from parse_lib import (book_page, build_blocks, normalize_formulas,
                       MARKER_LINE_RES)

SENT_SPLIT = re.compile(r"(?<=[.!?])\s+")
CHUNK_ID_PREFIX = "edex-igcse-chem"

def build_sections():
    """Ordered list of section dicts covering every page exactly once."""
    secs = []
    for (no, unit, title, bp) in CHAPTERS:
        secs.append({"key": f"ch{no}", "kind": "chapter", "unit": unit,
                     "chapter_no": no, "chapter_title": title,
                     "pdf_start": bp + 9, "label": title,
                     "content_type": "body"})
    for (key, s, e, unit, label, ctype) in EXTRA_SECTIONS:
        secs.append({"key": key, "kind": "extra", "unit": unit,
                     "chapter_no": None, "chapter_title": None,
                     "pdf_start": s, "pdf_end": e, "label": label,
                     "content_type": ctype})
    # chapters end where the next section in the same unit (or any later
    # section) begins -> compute via global ordering
    secs.sort(key=lambda x: x["pdf_start"])
    ordered = []
    for i, sec in enumerate(secs):
        nxt = secs[i + 1] if i + 1 < len(secs) else None
        if sec["kind"] == "chapter":
            sec["pdf_end"] = (nxt["pdf_start"] - 1) if nxt else N_PAGES
        ordered.append(sec)
    # verify full coverage, no overlaps
    covered = []
    for sec in ordered:
        covered.extend(range(sec["pdf_start"], sec["pdf_end"] + 1))
    assert len(covered) == len(set(covered)), "overlapping sections!"
    assert set(covered) == set(range(1, N_PAGES + 1)), (
        f"coverage gap: {set(range(1, N_PAGES+1)) - set(covered)}")
    return ordered

def chunk_type(blocks):
    types = {b[1] for b in blocks if b[1]}
    for t in reversed(TYPE_PRIORITY):
        if t in types:
            return t
    return "body"

def split_long_text(text, max_len=1600):
    """Split text trying: sentences -> lines -> word-boundary slices."""
    if len(text) <= max_len:
        return [text]
    pieces = SENT_SPLIT.split(text)
    if len(pieces) == 1:                      # no sentence ends (lists/indexes)
        pieces = text.split("\n")
    out, buf, blen = [], [], 0
    for piece in pieces:
        while len(piece) > HARD_MAX:           # pathological: one huge line
            cut = piece.rfind(" ", 0, max_len)
            cut = cut if cut > max_len // 2 else max_len
            out.append(piece[:cut])
            piece = piece[cut:].lstrip()
        if buf and blen + len(piece) > max_len:
            out.append(" ".join(buf))
            buf, blen = [], 0
        buf.append(piece)
        blen += len(piece) + 1
    if buf:
        out.append(" ".join(buf))
    return out

def pack_blocks(blocks, sec):
    """Pack blocks into chunks within size targets; split oversized blocks."""
    units = []  # (topic, text, page)
    for (topic, marker, text, page) in blocks:
        text, _n, _ex = normalize_formulas(text)
        text = re.sub(r"\n{3,}", "\n\n", text).strip()
        if not text:
            continue
        if len(text) > HARD_MAX:
            for piece in split_long_text(text):
                units.append((topic, piece, page))
        else:
            units.append((topic, text, page))
    # pack units into chunks
    chunks = []
    cur, cur_pages, cur_topic = [], set(), None
    for (topic, text, page) in units:
        tlen = len(text)
        if cur and (sum(len(t) for t in cur) + tlen > TARGET_MAX
                    and sum(len(t) for t in cur) >= TARGET_MIN):
            chunks.append((cur_topic, cur, cur_pages))
            cur, cur_pages = [], set()
        cur.append(text)
        cur_pages.add(page)
        cur_topic = topic or cur_topic
    if cur:
        chunks.append((cur_topic, cur, cur_pages))
    # merge undersized chunks into neighbours
    merged = []
    for ch in chunks:
        if (merged and sum(len(t) for t in ch[1]) < MERGE_MIN
                and sum(len(t) for t in merged[-1][1]) + sum(len(t) for t in ch[1]) <= HARD_MAX):
            merged[-1] = (merged[-1][0], merged[-1][1] + ch[1],
                          merged[-1][2] | ch[2])
        else:
            merged.append(list(ch) and (ch[0], ch[1], ch[2]))
    # second pass forward-merge for remaining tiny chunks
    out = []
    skip = set()
    for i, ch in enumerate(merged):
        if i in skip:
            continue
        if sum(len(t) for t in ch[1]) < MERGE_MIN and i + 1 < len(merged):
            nxt = merged[i + 1]
            merged[i + 1] = (nxt[0] or ch[0], ch[1] + nxt[1], ch[2] | nxt[2])
            skip.add(i + 1)
        out.append(merged[i] if i not in skip else None)
    return [c for c in out if c]

def main():
    os.makedirs(OUT_DIR, exist_ok=True)
    sections = build_sections()
    print(f"sections: {len(sections)} (29 chapters + back/front matter)")
    all_chunks, report = [], {
        "book_title": BOOK_TITLE, "source_url": SOURCE_URL,
        "n_pdf_pages": N_PAGES, "sections": len(sections),
        "per_unit": {}, "per_content_type": {}, "formula_fixes": 0,
        "empty_sections": [], "pages_skipped": []}
    md = [f"# {BOOK_TITLE}", f"*{BOOK_AUTHOR} - Pearson, 2017 edition*", "",
          f"Source: {SOURCE_URL}", ""]
    last_unit_header = None
    cid = 0
    for sec in sections:
        blocks = build_blocks(sec["pdf_start"], sec["pdf_end"])
        if not blocks:
            report["empty_sections"].append(sec["key"])
            continue
        packed = pack_blocks(blocks, sec)
        unit = sec.get("unit")
        unit_name = UNIT_NAMES.get(unit) if unit else None
        if unit_name and unit_name != last_unit_header and sec["kind"] in ("chapter", "extra"):
            if sec["kind"] == "chapter" or "questions" in sec["content_type"]:
                md += [f"## Unit {unit}: {unit_name}", ""]
                last_unit_header = unit_name
        if sec["kind"] == "chapter":
            md += [f"### Chapter {sec['chapter_no']}: {sec['chapter_title']}", ""]
        else:
            md += [f"### {sec['label']}", ""]
        for (topic, texts, pages) in packed:
            cid += 1
            text = "\n\n".join(t for t in texts if t.strip())
            pstart, pend = min(pages), max(pages)
            ctype = sec["content_type"]
            if ctype == "body":
                ctype = _block_level_type(blocks_for_pages(blocks, pages))
            chunk = {
                "id": f"{CHUNK_ID_PREFIX}-{cid:04d}",
                "text": text,
                "metadata": {
                    "book_title": BOOK_TITLE,
                    "unit_no": unit,
                    "unit_name": unit_name,
                    "chapter_no": sec.get("chapter_no"),
                    "chapter_title": sec.get("chapter_title") or sec["label"]
                                     if sec["kind"] == "extra" else sec.get("chapter_title"),
                    "topic": topic,
                    "content_type": ctype,
                    "pdf_page_start": pstart,
                    "pdf_page_end": pend,
                    "page_start": book_page(pstart),
                    "page_end": book_page(pend),
                    "source_url": SOURCE_URL,
                    "char_count": len(text),
                },
            }
            all_chunks.append(chunk)
            md += [f"*[book pp.{book_page(pstart)}-{book_page(pend)} | {ctype}]*", "",
                   text.replace("\n", "  \n"), ""]
            ukey = f"unit{unit}" if unit else "back_front_matter"
            report["per_unit"].setdefault(ukey, {"chunks": 0, "chars": 0})
            report["per_unit"][ukey]["chunks"] += 1
            report["per_unit"][ukey]["chars"] += len(text)
            report["per_content_type"][ctype] = report["per_content_type"].get(ctype, 0) + 1

    jsonl_path = os.path.join(OUT_DIR, "edexcel_igcse_chemistry_chunks.jsonl")
    with open(jsonl_path, "w", encoding="utf-8") as f:
        for c in all_chunks:
            f.write(json.dumps(c, ensure_ascii=False) + "\n")
    md_path = os.path.join(OUT_DIR, "full_book_clean.md")
    with open(md_path, "w", encoding="utf-8") as f:
        f.write("\n".join(md))
    report["total_chunks"] = len(all_chunks)
    report["total_chars"] = sum(c["metadata"]["char_count"] for c in all_chunks)
    sizes = [c["metadata"]["char_count"] for c in all_chunks]
    report["chunk_size"] = {"min": min(sizes), "max": max(sizes),
                            "avg": sum(sizes) // len(sizes)}
    with open(os.path.join(OUT_DIR, "parse_report.json"), "w") as f:
        json.dump(report, f, indent=2)
    print(json.dumps({k: report[k] for k in
                      ("total_chunks", "total_chars", "chunk_size",
                       "per_content_type", "empty_sections")}, indent=1))
    print("per_unit:", json.dumps(report["per_unit"]))
    print("OK ->", jsonl_path)

def blocks_for_pages(blocks, pages):
    return [b for b in blocks if b[3] in pages]

def _block_level_type(blocks):
    types = {b[1] for b in blocks if b[1]}
    for t in reversed(TYPE_PRIORITY):
        if t in types:
            return t
    return "body"

if __name__ == "__main__":
    main()
