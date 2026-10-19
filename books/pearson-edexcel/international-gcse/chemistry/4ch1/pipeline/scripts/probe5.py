#!/usr/bin/env python3
"""Probe #5: parse unit-divider pages for authoritative chapter titles + book pages."""
import os, re

OCR_DIR = "/home/z/my-project/data/ocr_pages"

def read_page(p):
    with open(os.path.join(OCR_DIR, f"page_{p:03d}.txt"), encoding="utf-8") as f:
        return f.read()

DIVIDERS = {"UNIT 1 (pdf 11 / book 2)": 11, "UNIT 2 (pdf 131 / book 122)": 131,
            "UNIT 3 (pdf 215 / book 206)": 215, "UNIT 4 (pdf 263 / book 254)": 263}

for label, p in DIVIDERS.items():
    print(f"== {label} ==")
    txt = read_page(p)
    # entries look like: 'TITLE 123' possibly joined with '|' or newlines
    flat = re.sub(r"\s+", " ", txt.replace("|", "\n"))
    entries = re.findall(r"([A-Z][A-Z0-9 ,'()&/-]{4,60}?)\s+(\d{1,3})(?=\s|$)", flat)
    for t, n in entries:
        t = t.strip(" ,")
        # filter noise: keep entries whose title has >= 2 words or is known topic-like
        if len(t.split()) >= 2:
            print(f"   book p.{int(n):>3}  {t}")
    print()
