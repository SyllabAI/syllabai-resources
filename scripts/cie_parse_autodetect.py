#!/usr/bin/env python3
"""T-SPECS-CIE-PARSE-1: family auto-detect across the 33 CIE syllabuses.
Print-only signals + reference dumps to scripts/cie_samples/<slug>.txt."""
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

P_RX = [
    ('NMK',      re.compile(r'^\s*\d{1,2}\.\d{1,2}\.\d{1,2}[a-z]?(?=\s)', re.M)),
    ('NM',       re.compile(r'^\s*\d{1,2}\.\d{1,2}\s+(?=[A-Za-z])', re.M)),
    ('CE',       re.compile(r'^\s*[CE]\d{1,2}\.\d{1,2}(?=\s)', re.M)),
    ('CAND',     re.compile(r'Candidates should be able to', re.I)),
    ('ASSESS',   re.compile(r'Candidates will be assessed on', re.I)),
    ('LEARN',    re.compile(r'Learning outcomes', re.I)),
    ('CORECOL',  re.compile(r'^\s*Core\s*$', re.M)),
    ('SUPPCOL',  re.compile(r'^\s*Supplement\s*$', re.M)),
    ('EXTCOL',   re.compile(r'^\s*Extended\s*$', re.M)),
    ('FOCUS',    re.compile(r'^\s*(Focus points|Specified content|Detailed content)\s*$', re.M)),
]

print(f"{'slug':<58} {'cp':>3} {'pgs':>3}  " + ' '.join(f"{k:>7}" for k, _ in P_RX))
for q in cie:
    pdf = os.path.join(OSDIR, q['slug'], q['pdf'])
    n = q['pages']
    full = ptext(pdf, 1, n)
    pages = full.split('\f')
    # content region: pages whose running header mentions 'Subject content'/'Syllabus content'
    cp = next((i + 1 for i, p in enumerate(pages) if re.search(r'(Subject|Syllabus) content', p)), None)
    region = '\f'.join(pages[cp - 1:]) if cp else full
    sig = {k: len(rx.findall(region)) for k, rx in P_RX}
    # reference dump: content start + 2 pages
    dump = ptext(pdf, cp, min(cp + 2, n)) if cp else ''
    with open(os.path.join(SAMP, q['slug'] + '.txt'), 'w') as f:
        f.write(f"{q['slug']} p{cp} of {n}\n" + dump)
    print(f"{q['slug']:<58} {str(cp):>3} {n:>3}  " + ' '.join(f"{sig[k]:>7}" for k, _ in P_RX))
