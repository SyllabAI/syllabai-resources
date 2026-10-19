#!/usr/bin/env python3
"""Probe #3: chapter boundaries + running header transitions.
Prints structural metadata only (headers, chapter numbers/titles)."""
import os, re

OCR_DIR = "/home/z/my-project/data/ocr_pages"

def read_page(p):
    with open(os.path.join(OCR_DIR, f"page_{p:03d}.txt"), encoding="utf-8") as f:
        return f.read()

# --- 1. Running header (first non-empty line) transitions ---
print("== Running-header transitions ==")
prev = None
headers = {}
for p in range(1, 384):
    lines = [ln.strip() for ln in read_page(p).splitlines() if ln.strip()]
    h = lines[0] if lines else ""
    headers[p] = h
    if h != prev:
        print(f"p{p:3d}: {h[:60]}")
        prev = h

# --- 2. Chapter markers: pages containing 'CHAPTER <n>' + nearby LEARNING OBJECTIVES ---
print("\n== CHAPTER n occurrences (page: chapter numbers) ==")
chap_pages = {}
for p in range(1, 384):
    nums = re.findall(r"CHAPTER\s+(\d{1,2})\b", read_page(p), re.I)
    if nums:
        chap_pages[p] = sorted(set(int(n) for n in nums))
print(json.dumps(chap_pages))

# --- 3. LEARNING OBJECTIVES pages: what's the chapter title? (all-caps lines before it) ---
print("\n== LEARNING OBJECTIVES pages (chapter start candidates) ==")
for p in range(1, 384):
    txt = read_page(p)
    if re.search(r"LEARNING\s+OBJECTIVES", txt, re.I):
        caps = [ln.strip() for ln in txt.splitlines()
                if re.match(r"^[A-Z][A-Z0-9 ,'()&?/-]{4,55}$", ln.strip())]
        print(f"p{p:3d}: caps={caps[:5]}")

# --- 4. Verify page offset: print tiny structure of page 11 (unit divider?) ---
print("\n== Page 11 all-caps lines ==")
txt11 = read_page(11)
print([ln.strip() for ln in txt11.splitlines()
       if re.match(r"^[A-Z][A-Z0-9 ,'()&?/-]{2,55}$", ln.strip())][:8])
print("page11 chars:", len(txt11))
