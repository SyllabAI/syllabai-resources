#!/usr/bin/env python3
"""Acceptance filter for econ/business cell rebuilds.

Apply a rebuild ONLY if:
  (1) new text is contiguous-verbatim in the row's page text (normalized)
  (2) every new item is contiguous-verbatim in the page text
  (3) stored state is provably broken: stored text not contiguous-verbatim,
      or any stored item not contiguous-verbatim, or any stored item absent
      from the whole PDF (foreign block)
Everything else is left untouched (no churn on clean rows).
"""
import json, re, unicodedata
from pathlib import Path
import fitz

RES = Path('/home/z/my-project/download/syllabai-resources/Official-Specifications')

def norm(s):
    if not s: return ''
    s = unicodedata.normalize('NFKC', s)
    for a, b in (('\u2019', "'"), ('\u2018', "'"), ('\u201c', '"'), ('\u201d', '"'),
                 ('\u2013', '-'), ('\u2014', '-'), ('\u2212', '-'), ('\u00d7', 'x'),
                 ('\ufb01', 'fi'), ('\ufb02', 'fl'), ('\u2022', ' ')):
        s = s.replace(a, b)
    return re.sub(r'\s+', ' ', s).strip().lower()

accepted, rejected_verbatim, rejected_clean = {}, {}, {}
for q in ['igcse-economics', 'igcse-business']:
    rep = json.load(open(f'/home/z/my-project/scripts/t_spec_{q}_cellrepairs.json'))
    sp = json.load(open(RES / 'parsed' / q / 'spec_points.json'))
    pts = {p['id']: p for p in sp['spec_points']}
    docs = {}
    for pid, v in rep.items():
        p = pts[pid]
        pg = p['provenance']['page']
        if q not in docs:
            docs[q] = fitz.open(RES / q / sp['source']['pdf'])
        doc = docs[q]
        ptext = norm(doc[pg - 1].get_text('text'))
        alltext = norm(' '.join(doc[i].get_text('text') for i in range(len(doc))))
        new_text_ok = norm(v['text']) in ptext
        new_items_ok = all(norm(it) in ptext for it in v['sub_items'])
        stored_text_ok = norm(p['text']) in ptext
        stored_items_ok = all(norm(it) in ptext for it in p['sub_items'])
        foreign = any(norm(it) not in alltext for it in p['sub_items'])
        broken = (not stored_text_ok) or (not stored_items_ok) or foreign
        if new_text_ok and new_items_ok and broken:
            accepted[pid] = {'text': v['text'], 'sub_items': v['sub_items'], 'qual': q}
        elif not (new_text_ok and new_items_ok):
            rejected_verbatim[pid] = v
        else:
            rejected_clean[pid] = v
    print(f'{q}: accepted={len(accepted)} rejected_verbatim={len(rejected_verbatim)} '
          f'clean-no-churn={len(rejected_clean)}')

json.dump({'accepted': accepted,
           'rejected_verbatim': rejected_verbatim,
           'rejected_clean': rejected_clean},
          open('/home/z/my-project/scripts/t_spec_cellrepairs_accepted.json', 'w'),
          indent=1, ensure_ascii=False)
print('\nsample accepted:')
for pid, v in list(accepted.items())[:10]:
    print(f"  {pid} [{v['qual']}]")
    print('    text:', v['text'][:110])
    print('    items:', [i[:45] for i in v['sub_items'][:4]])
