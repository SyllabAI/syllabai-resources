#!/usr/bin/env python3
"""Layout-based cut-item detector for bullet-item quals (econ, business, ict).

For each sub_item: locate its LAST line in the row's cell region; if the next
visual line within the same cell starts at the bullet-text indent x (not a
bullet marker x) and is not already part of the item -> the item was cut at
the line boundary; report the continuation.
"""
import json, re, sys
from pathlib import Path
import fitz

RES = Path('/home/z/my-project/download/syllabai-resources/Official-Specifications')

def norm(s):
    if not s: return ''
    s = unicodedata.normalize('NFKC', s)
    for a, b in (('\u2019', "'"), ('\u2018', "'"), ('\u2013', '-'), ('\u2014', '-'),
                 ('\u2022', ' ')):
        s = s.replace(a, b)
    return re.sub(r'\s+', ' ', s).strip().lower()

import unicodedata

for q in ['igcse-economics', 'igcse-business', 'igcse-ict']:
    sp = json.load(open(RES / 'parsed' / q / 'spec_points.json'))
    doc = fitz.open(RES / q / sp['source']['pdf'])
    # cache page words grouped into visual lines
    page_lines = {}
    for i in range(len(doc)):
        ws = doc[i].get_text('words')
        lines = {}
        for w in ws:
            lines.setdefault(round(w[1] / 4), []).append(w)
        seq = []
        for k in sorted(lines):
            g = sorted(lines[k], key=lambda w: w[0])
            seq.append({'y': g[0][1], 'text': ' '.join(w[4] for w in g),
                        'x0': g[0][0], 'x1': g[-1][2], 'words': g})
        page_lines[i] = seq
    cuts = 0
    checked = 0
    for p in sp['spec_points']:
        pg = p['provenance']['page'] - 1
        seq = page_lines[pg]
        flat = [(j, L) for j, L in enumerate(seq)]
        for it in p.get('sub_items') or []:
            checked += 1
            inw = norm(it).split()
            if not inw:
                continue
            # find the line containing the item's LAST 3 words
            tail = ' '.join(inw[-3:])
            hit = None
            for j, L in flat:
                if tail and tail in norm(L['text']):
                    hit = (j, L)
            if hit is None:
                continue
            j, L = hit
            # next line within the page
            if j + 1 >= len(seq):
                continue
            N = seq[j + 1]
            nt = norm(N['text'])
            # continuation heuristics: next line starts lowercase (not a bullet
            # marker, not a new code/letter row) AND item doesn't end with
            # sentence punctuation
            if re.search(r'[.:;]$', it.strip()):
                continue
            first = N['text'].strip().lstrip('\u2022o ')
            if not first:
                continue
            if N['text'].strip().startswith(('\u2022', 'o ')):
                continue  # new bullet
            if re.match(r'^[a-z]', first) and first[0] not in 'oi':
                cuts += 1
                print(f"{q} [{p['id']}] CUT? item={it[-60:]!r}")
                print(f"    next line: {N['text'][:90]!r}")
    print(f'== {q}: items checked={checked}, suspected cuts={cuts}\n')
