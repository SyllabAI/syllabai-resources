#!/usr/bin/env python3
"""Probe #2: parse TOC from contents pages + find heading rendering patterns.
Prints only titles / counts / short structural lines."""
import os, re, json
from collections import Counter

OCR_DIR = "/home/z/my-project/data/ocr_pages"

def read_page(p):
    with open(os.path.join(OCR_DIR, f"page_{p:03d}.txt"), encoding="utf-8") as f:
        return f.read()

# --- 1. TOC entries on contents pages (pages 4-6): lines ending with a page number ---
print("== TOC entries (contents pages 4-6) ==")
toc = []
for p in (4, 5, 6):
    for ln in read_page(p).splitlines():
        m = re.match(r"^\s*(.{3,70}?)\s+(\d{1,3})\s*$", ln)
        if m and not re.match(r"^\d+\s", ln):
            title = m.group(1).strip(" .")
            if len(title.split()) >= 2 or title.isupper():
                toc.append({"p": p, "title": title, "book_page": int(m.group(2))})
for t in toc:
    print(t)

# --- 2. Phrase frequency across all pages ---
print("\n== Phrase occurrences (page count containing phrase) ==")
phrases = [
    (r"TEST\s*YOURSELF", "TEST YOURSELF"),
    (r"EXAM[- ]?STYLE", "EXAM-STYLE"),
    (r"SUMMARY\s+QUESTION", "SUMMARY QUESTIONS"),
    (r"\bCHAPTER\s+\d+", "CHAPTER n"),
    (r"^\s*UNIT\s*\d+\s*$", "UNIT n (alone)"),
    (r"\bSECTION\s+\d", "SECTION n"),
    (r"MATHS\s+SKILLS", "MATHS SKILLS"),
    (r"EXAM\s+TECHNIQUE|EXAM\s+TIP|EXAM\s+HINT", "EXAM TIP/HINT"),
    (r"PROGRESS\s+CHECK|CHECKPOINT", "PROGRESS CHECK"),
    (r"PRACTICAL", "PRACTICAL"),
    (r"END\s+OF\s+UNIT", "END OF UNIT"),
    (r"GLOSSARY|INDEX", "GLOSSARY/INDEX"),
    (r"COMMAND\s+WORD", "COMMAND WORD"),
    (r"WORKED\s+EXAMPLE", "WORKED EXAMPLE"),
]
for pat, name in phrases:
    cnt = 0
    pages_with = []
    for p in range(1, 384):
        if re.search(pat, read_page(p), re.I | re.M):
            cnt += 1
            pages_with.append(p)
    print(f"{name:28s} pages={cnt:4d}  first5={pages_with[:5]}")

# --- 3. ALL-CAPS short lines sample from a few body pages (heading style probe) ---
print("\n== ALL-CAPS short lines on pages 20, 60, 120, 200, 300 (heading style) ==")
for p in (20, 60, 120, 200, 300):
    caps = [ln.strip() for ln in read_page(p).splitlines()
            if re.match(r"^[A-Z][A-Z0-9 ,'()&?/-]{4,45}$", ln.strip())]
    print(f"p{p:3d}: {caps[:8]}")

# --- 4. First 6 non-empty lines of pages 20,60,200 (layout probe: how titles sit) ---
print("\n== First 6 non-empty lines of a few pages (layout style, truncated) ==")
for p in (20, 60, 200):
    lines = [ln for ln in read_page(p).splitlines() if ln.strip()][:6]
    print(f"--- p{p} ---")
    for ln in lines:
        print("   ", ln.strip()[:70])
