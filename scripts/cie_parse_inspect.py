#!/usr/bin/env python3
"""Locate the syllabus-content region per CIE PDF and dump representative pages."""
import json, os, re, subprocess, sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OSDIR = os.path.join(ROOT, 'Official-Specifications')
manifest = json.load(open(os.path.join(OSDIR, 'manifest.json')))
quals = manifest['qualifications'] if isinstance(manifest, dict) else manifest
cie = {q['spec_codes'][0] if q.get('spec_codes') else q['slug']: q for q in quals if 'cambridge' in str(q.get('board', '')).lower()}

def ptext(pdf, first, last):
    r = subprocess.run(['pdftotext', '-f', str(first), '-l', str(last), '-layout', pdf, '-'],
                       capture_output=True, text=True)
    return r.stdout

def find_content_page(pdf, npages):
    """scan pages for a header line naming the syllabus content section"""
    for n in range(1, min(npages, 99) + 1):
        t = ptext(pdf, n, n)
        if re.search(r'Syllabus content', t):
            return n
    return None

samples = sys.argv[1:] or ['0620', '0478', '9708', '0580', '0475']
for code in samples:
    q = cie.get(code)
    if not q:
        print(f"!! code {code} not found"); continue
    pdf = os.path.join(OSDIR, q['slug'], q['pdf'])
    cp = find_content_page(pdf, q['pages'])
    print("=" * 100)
    print(f"{code} {q['slug']}  pdf={q['pdf']}  pages={q['pages']}  content-section-starts-p{cp}")
    if cp:
        body = ptext(pdf, cp, min(cp + 1, q['pages']))
        lines = body.splitlines()
        print(f"--- first 55 lines of p{cp}(-{cp+1}):")
        for ln in lines[:55]:
            print("   |" + ln[:150])
