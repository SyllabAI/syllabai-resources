#!/usr/bin/env python3
"""Marker + damage census on the parsed YCH11 SB1 Docling page JSONs.
Refines book_structure_ych11.MARKERS and quantifies damage classes before
chunking (books/README.md §5 phase 2 + L-005/L-013 production-side discipline).
Also runs the structure map boundary-coherence assert (phase 3 gate)."""
import json, re, glob, collections, sys, os

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from book_structure_ych11 import MARKERS, N_PAGES, OFFSET, boundary_coherence

PAGES = sorted(glob.glob("/home/z/my-project/data/ych11_sb1/docling_pages/page_*.json"))
print(f"pages on disk: {len(PAGES)} / {N_PAGES}")

marker_hits = collections.Counter()
merged_forms = collections.Counter()
label_counts = collections.Counter()
glue_total = glue_pages = 0
errors = []
formula_pages = 0
formula_empty_items = 0
formula_nonempty_items = 0
empty_pages = []

WORD = re.compile(r"[A-Za-z]{4,}")

def glue_ratio(text: str):
    """Fraction of words >= 12 chars (crude glue-run proxy) + long-run count."""
    words = WORD.findall(text)
    if not words:
        return 0.0, 0
    long_runs = [w for w in words if len(w) >= 14]
    return len(long_runs) / len(words), len(long_runs)

for fp in PAGES:
    d = json.load(open(fp))
    pno = d["pdf_page"]
    if d.get("error"):
        errors.append((pno, d["error"][:80]))
        continue
    page_text = []
    for it in d.get("items", []):
        label, text = it["label"], (it.get("text") or "").strip()
        label_counts[label] += 1
        if label in ("formula", "code"):
            if text:
                formula_nonempty_items += 1
                formula_pages += 1
            else:
                formula_empty_items += 1
        if not text or label == "picture":
            continue
        page_text.append(text)
        up = text.upper()
        for key, rx in MARKERS.items():
            if re.search(rx, up):
                marker_hits[key] += 1
        for tok in re.findall(r"\b[A-Z][A-Z&']{9,}\b", text):
            if not re.search(r"[AEIOU]", tok[1:]):
                continue
            merged_forms[tok] += 1
        r, n = glue_ratio(text)
        if n:
            glue_total += n
    joined = " ".join(page_text)
    if len(joined) < 20:
        empty_pages.append((pno, pno - OFFSET))
    if joined:
        _, runs = glue_ratio(joined)
        if runs >= 3:
            glue_pages += 1

print("\n--- structure map boundary coherence ---")
problems = boundary_coherence()
if problems:
    for p in problems:
        print("  PROBLEM:", p)
else:
    print("  OK: arabic map tiles book 2..316 exactly, no gaps/overlaps")

print("\n--- label census ---")
for lab, n in label_counts.most_common():
    print(f"  {lab:16s} {n}")

print("\n--- marker hits (pages containing) ---")
for k, n in marker_hits.most_common():
    print(f"  {k:22s} {n}")

print("\n--- suspected merged ALLCAPS forms (top 25) ---")
for tok, n in merged_forms.most_common(25):
    print(f"  {tok:28s} {n}")

print("\n--- damage ---")
print(f"pages with >=3 long glue runs: {glue_pages} / {len(PAGES)}")
print(f"total long runs: {glue_total}")
print(f"formula items: nonempty={formula_nonempty_items} EMPTY={formula_empty_items} (pages with nonempty formula: {formula_pages})")
if errors:
    print(f"ERROR pages: {errors}")
if empty_pages:
    print(f"near-empty pages (<20 chars, pdf,book): {empty_pages}")
