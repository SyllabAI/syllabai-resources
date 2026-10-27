#!/usr/bin/env python3
"""T-SPECS-CIE-PARSE-1 pre-work survey: text-layer + numbering-family reconnaissance
over the 33 CIE syllabus PDFs. Print-only, deterministic. No repo writes."""
import json, os, re, subprocess, sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OSDIR = os.path.join(ROOT, 'Official-Specifications')
manifest = json.load(open(os.path.join(OSDIR, 'manifest.json')))
quals = manifest['qualifications'] if isinstance(manifest, dict) else manifest
cie = [q for q in quals if 'cambridge' in str(q.get('board', '')).lower()]
print(f"CIE quals in manifest: {len(cie)}")

# extract first N pages text via pdftotext (fast, layout-aware)
def pages_text(pdf, first, last):
    r = subprocess.run(['pdftotext', '-f', str(first), '-l', str(last), '-layout', pdf, '-'],
                       capture_output=True, text=True)
    return r.stdout if r.returncode == 0 else ''

def page_text(pdf, n):
    return pages_text(pdf, n, n)

rows = []
for q in cie:
    pdf = os.path.join(OSDIR, q['slug'], q['pdf'])
    if not os.path.exists(pdf):
        rows.append((q['slug'], 'MISSING', 0, 0, 0))
        continue
    npages = q.get('pages', 0)
    # full text scan for structure signals (cheap: single pass per doc)
    txt = subprocess.run(['pdftotext', '-layout', pdf, '-'], capture_output=True, text=True).stdout
    chars = len(txt)
    if chars < 1000:
        rows.append((q['slug'], 'NO_TEXT_LAYER', npages, 0, 0))
        continue
    # numbering family signals in the content region
    # N.M.K deep outcomes (e.g. "3.2.1")
    deep = len(re.findall(r'^\s*\d+\.\d+\.\d+[a-z]?\s', txt, re.M))
    # N.M topic heads (e.g. "3.2 " at line start)
    topics = len(re.findall(r'^\s*\d+\.\d+\s+\S', txt, re.M))
    # Core/Supplement/Extended tier signals
    core = len(re.findall(r'\bCore\b', txt))
    supp = len(re.findall(r'\bSupplement\b', txt))
    ext = len(re.findall(r'\bExtended\b', txt))
    # syllabus content section marker
    m = re.search(r'^\s*\d+\.?\s+Syllabus content\s*$', txt, re.M)
    marker = bool(m)
    rows.append((q['slug'], f"deep={deep} top={topics} core={core} supp={supp} ext={ext} content_marker={marker}", npages, chars, q['spec_codes']))

print()
print(f"{'slug':<58} {'pages':>5} {'chars':>8}  signals")
for slug, sig, np_, chars, codes in rows:
    print(f"{slug:<58} {np_:>5} {chars:>8}  {sig}  {codes}")
