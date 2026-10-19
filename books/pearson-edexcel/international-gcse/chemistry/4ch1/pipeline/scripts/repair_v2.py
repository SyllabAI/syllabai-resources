#!/usr/bin/env python3
"""Repair pass v2: mechanical OCR fixes + breadcrumb context.
- Fixes: state-paren subscript commas (H,(g)->H2(g)), zero-for-O (H20->H2O),
  intra-word semicolons (s;owly->slowly), 10? exponents, junk line debris.
- Adds a self-contained breadcrumb line to every chunk (helps retrieval).
- Preserves original text in 'text_original'; logs per-rule change counts.
Output: edexcel_igcse_chemistry_chunks_v2.jsonl"""
import json
import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from book_structure import BOOK_TITLE, UNIT_NAMES

SRC = "/home/z/my-project/download/rag_chemistry/edexcel_igcse_chemistry_chunks.jsonl"
DST = "/home/z/my-project/download/rag_chemistry/edexcel_igcse_chemistry_chunks_v2.jsonl"

RX_STATE_COMMA = re.compile(r"(?<![A-Za-z])([A-Z][a-z]?)\s*,\s*(?=\((?:g|l|s|aq)\))")
RX_ZERO_O = re.compile(r"(?<![A-Za-z0-9])([A-Z][a-z]?\d*)0(?=\d|\b)")
RX_SEMI = re.compile(r"(?<=[A-Za-z0-9]);(?=[A-Za-z0-9])")  # subscript 3 misread
RX_TENQ = re.compile(r"\b10\?")
RX_JUNK_PREFIX = re.compile(r"^[|}\]>«»\"';:.]{1,4}\s+")
RX_JUNK_LINE = re.compile(r"^[|}\]>«»\"';:~_=+\-]{1,6}$")
RX_MOSTLY_PUNCT = re.compile(r"^(?:[^A-Za-z0-9]*[A-Za-z0-9][^A-Za-z0-9]*){1,3}$")

def repair_text(text):
    log = {"state_comma": 0, "zero_O": 0, "semi": 0, "tenq": 0,
           "junk_prefix": 0, "junk_line": 0}
    def sc(m):
        log["state_comma"] += 1
        return m.group(1) + "2"
    text = RX_STATE_COMMA.sub(sc, text)
    def zo(m):
        log["zero_O"] += 1
        return m.group(1) + "O"
    text = RX_ZERO_O.sub(zo, text)
    def sm(m):
        log["semi"] += 1
        return m.group(0).replace(";", "3")
    text = RX_SEMI.sub(sm, text)
    def tq(m):
        log["tenq"] += 1
        return "10^"
    text = RX_TENQ.sub(tq, text)
    lines = text.splitlines()
    out = []
    for ln in lines:
        if RX_JUNK_LINE.match(ln.strip()) or RX_MOSTLY_PUNCT.match(ln.strip()):
            log["junk_line"] += 1
            continue
        new = RX_JUNK_PREFIX.sub("", ln)
        if new != ln:
            log["junk_prefix"] += 1
        out.append(new)
    return "\n".join(out), log

def breadcrumb(md):
    parts = []
    if md.get("unit_name"):
        parts.append(f"Unit {md['unit_no']} - {md['unit_name']}")
    if md.get("chapter_no"):
        parts.append(f"Chapter {md['chapter_no']}: {md['chapter_title']}")
    elif md.get("chapter_title"):
        parts.append(md["chapter_title"])
    if md.get("topic"):
        parts.append(md["topic"])
    pp = f"book pp.{md['page_start']}-{md['page_end']}"
    ctx = " | ".join(parts) if parts else BOOK_TITLE
    return f"[{ctx} | {pp}]"

def main():
    n_chunks, n_changed, rule_totals = 0, 0, {}
    with open(SRC, encoding="utf-8") as src, open(DST, "w", encoding="utf-8") as dst:
        for line in src:
            c = json.loads(line)
            n_chunks += 1
            fixed, log = repair_text(c["text"])
            for k, v in log.items():
                rule_totals[k] = rule_totals.get(k, 0) + v
            changed = fixed != c["text"]
            n_changed += changed
            new = {"id": c["id"], "text": f"{breadcrumb(c['metadata'])}\n\n{fixed}",
                   "text_original": c["text"], "metadata": c["metadata"],
                   "repair_log": log, "llm_repaired": False}
            dst.write(json.dumps(new, ensure_ascii=False) + "\n")
    print(f"chunks: {n_chunks} | changed by mechanical pass: {n_changed}")
    print("rule totals:", json.dumps(rule_totals))
    print("OK ->", DST)

if __name__ == "__main__":
    main()
