#!/usr/bin/env python3
"""Probe #4 (fixed): chapter marker pages, LEARNING OBJECTIVES pages, page-11 layout."""
import os, re, sys, json, traceback

OCR_DIR = "/home/z/my-project/data/ocr_pages"

def read_page(p):
    with open(os.path.join(OCR_DIR, f"page_{p:03d}.txt"), encoding="utf-8") as f:
        return f.read()

try:
    print("== CHAPTER n occurrences (page: chapter numbers) ==")
    chap_pages = {}
    for p in range(1, 384):
        nums = re.findall(r"CHAPTER\s+(\d{1,2})\b", read_page(p), re.I)
        if nums:
            chap_pages[p] = sorted(set(int(n) for n in nums))
    print(json.dumps(chap_pages))

    print("\n== LEARNING OBJECTIVES pages (chapter start candidates) ==")
    for p in range(1, 384):
        txt = read_page(p)
        if re.search(r"LEARNING\s+OBJECTIVES", txt, re.I):
            caps = [ln.strip() for ln in txt.splitlines()
                    if re.match(r"^[A-Z][A-Z0-9 ,'()&?/-]{4,55}$", ln.strip())]
            print(f"p{p:3d}: {caps[:4]}")

    print("\n== Page 11 all-caps lines ==")
    txt11 = read_page(11)
    print([ln.strip() for ln in txt11.splitlines()
           if re.match(r"^[A-Z][A-Z0-9 ,'()&?/-]{2,55}$", ln.strip())][:10])
    print("page11 chars:", len(txt11))
except Exception:
    traceback.print_exc()
    sys.exit(1)
