#!/usr/bin/env python3
"""T-SPECS-CIE-PARSE-1: content-aware reference dumps (first real content pages)."""
import json, os, re, subprocess

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OSDIR = os.path.join(ROOT, 'Official-Specifications')
SAMP = os.path.join(ROOT, 'scripts', 'cie_samples')
os.makedirs(SAMP, exist_ok=True)

manifest = json.load(open(os.path.join(OSDIR, 'manifest.json')))
quals = manifest['qualifications'] if isinstance(manifest, dict) else manifest
cie = sorted((q for q in quals if 'cambridge' in str(q.get('board', '')).lower()), key=lambda q: q['slug'])

def ptext(pdf, first, last):
    r = subprocess.run(['pdftotext', '-f', str(first), '-l', str(last), '-layout', pdf, '-'],
                       capture_output=True, text=True)
    return r.stdout

NM2 = re.compile(r'^\s*(?:[CE]?\d{1,2}\.\d{1,2}(?!\.)\s+[A-Za-z(]|\d{1,2}\.\d{1,2}\.\d{1,2}\s)', re.M)

targets = None
if len(__import__('sys').argv) > 1:
    targets = set(__import__('sys').argv[1:])
for q in cie:
    if targets and not any(t in q['slug'] for t in targets):
        continue
    pdf = os.path.join(OSDIR, q['slug'], q['pdf'])
    n = q['pages']
    pages = ptext(pdf, 1, n).split('\f')
    first = None
    for i, p in enumerate(pages):
        if len(NM2.findall(p)) >= 2:
            first = i + 1
            break
    dump = ptext(pdf, first, min(first + 2, n)) if first else '(no content page found)'
    with open(os.path.join(SAMP, q['slug'] + '.txt'), 'w') as f:
        f.write(f"{q['slug']} FIRST-CONTENT-PAGE p{first} of {n}\n" + dump)
    print(f"{q['slug']:<62} first-content p{first}")
