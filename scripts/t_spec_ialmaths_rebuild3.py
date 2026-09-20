#!/usr/bin/env python3
"""ial-maths v3 rebuild — parser-native, column-sequential, band-limited.

Uses spec_parser's own page_spans/visual_lines/strip_running_text machinery so
tokenization & satellite spacing match corpus conventions exactly.

Per scoped point: row band = its code line to the next code line (same page;
if none, to the content bottom). text = content-column lines then
guidance-column lines (column-sequential, the corpus convention for two-column
tables). sub_items = bullet lines INSIDE the band only (drops runaway
assessment-info bullets harvested across pages).

Modes:
  --check   self-validation report only (no writes)
  --apply   write repair JSON for the applier
"""
import json, re, sys
from pathlib import Path
import fitz

RES = Path('/home/z/my-project/download/syllabai-resources')
sys.path.insert(0, str(RES / 'scripts'))
import spec_parser as SP

BASE = RES / 'Official-Specifications'
sp = json.load(open(BASE / 'parsed/ial-maths/spec_points.json'))
doc = fitz.open(BASE / 'ial-maths' / sp['source']['pdf'])
kill = SP.strip_running_text(doc)

CODE_L, CODE_R, CONT_L, CONT_R, GUID_L, GUID_R = 62.4, 97.4, 97.4, 267.6, 267.6, 544.0
CODE_RE = re.compile(r'^(\d{1,2})\.(\d{1,2})$')

def page_data(i):
    spans = [s for s in SP.page_spans(doc[i]) if not kill(s)]
    col = [s for s in spans if CODE_L <= s['x0'] < CODE_R]
    lines = SP.visual_lines(col, tol=3.5)
    codes = []
    for L in lines:
        m = CODE_RE.match(L['text'].strip())
        if m:
            codes.append((L['text'].strip(), L['oy']))
    return spans, codes

def row_band(pg, code, oy):
    spans, codes = page_data(pg)
    cands = [c for c in codes if c[0] == code]
    if not cands:
        return None, None, None
    cy = min(cands, key=lambda c: abs(c[1] - oy))[1]
    below = sorted([c[1] for c in codes if c[1] > cy + 2])
    y_end = below[0] - 1 if below else 770.0
    return spans, cy, y_end

def rebuild(p):
    pg = p['provenance']['page'] - 1
    spans, cy, y_end = row_band(pg, p['official_code'], p['provenance']['oy'])
    if spans is None:
        return None
    band = [s for s in spans if cy - 1 <= s['oy'] < y_end]
    cont = [s for s in band if CONT_L <= s['x0'] < CONT_R]
    guid = [s for s in band if GUID_L <= s['x0'] < GUID_R]
    c_lines = SP.visual_lines(cont, tol=7.0)
    g_lines = SP.visual_lines(guid, tol=7.0)
    items = [L['text'].lstrip('\u2022').strip()
             for L in c_lines + g_lines if L['text'].startswith('\u2022')]
    text = ' '.join([L['text'] for L in c_lines] + [L['text'] for L in g_lines])
    text = re.sub(r'\s+', ' ', text).strip()
    return {'text': text, 'sub_items': items,
            'col2': ' '.join(L['text'] for L in c_lines),
            'col3': ' '.join(L['text'] for L in g_lines)}

def norm(s):
    return re.sub(r'\s+', ' ', s or '').strip().lower()

mode = sys.argv[1] if len(sys.argv) > 1 else '--check'
single = multi = 0
changes = []
skips = []
for p in sp['spec_points']:
    if p['scope'] is None:
        continue
    rec = rebuild(p)
    if rec is None:
        skips.append(p['id'])
        continue
    n_lines_col2 = 1 if rec['col2'] else 0
    n_lines_col3 = len([x for x in rec['col3'].split(' \u2022 ')])  # approx
    text_changed = norm(rec['text']) != norm(p['text'])
    items_changed = rec['sub_items'] != p['sub_items']
    if text_changed or items_changed:
        changes.append((p, rec))
    else:
        single += 1

print(f'unchanged (byte-equal under rebuild): {single}')
print(f'changed: {len(changes)}  skips: {skips}')
print('\n=== change list (OLD -> NEW) ===')
for p, rec in changes:
    items_old, items_new = p['sub_items'], rec['sub_items']
    print(f'--- {p["id"]} (p{p["provenance"]["page"]})')
    if norm(rec['text']) != norm(p['text']):
        print('  T-OLD:', p['text'][:150])
        print('  T-NEW:', rec['text'][:150])
    if items_old != items_new:
        print(f'  I-OLD({len(items_old)}):', [i[:40] for i in items_old[:4]])
        print(f'  I-NEW({len(items_new)}):', [i[:40] for i in items_new[:4]])

if mode == '--apply':
    out = {}
    for p, rec in changes:
        out[p['id']] = {'text': rec['text'], 'sub_items': rec['sub_items']}
    Path('/home/z/my-project/scripts/t_spec_ialmaths_repairs.json').write_text(
        json.dumps(out, indent=1, ensure_ascii=False) + '\n')
    print('\nwrote repair set -> /home/z/my-project/scripts/t_spec_ialmaths_repairs.json')
