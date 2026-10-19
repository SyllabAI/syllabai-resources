#!/usr/bin/env python3
"""Probe #6: dump contents-pages (PDF 4-6) raw lines to resolve full chapter list."""
import os

OCR_DIR = "/home/z/my-project/data/ocr_pages"

for p in (4, 5, 6):
    print(f"===== PDF page {p} =====")
    with open(os.path.join(OCR_DIR, f"page_{p:03d}.txt"), encoding="utf-8") as f:
        for ln in f.read().splitlines():
            if ln.strip():
                print("  ", ln.strip()[:75])
