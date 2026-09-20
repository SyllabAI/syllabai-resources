#!/usr/bin/env python3
"""
T-SPEC-NORM-1 — independent PDF-vs-parse fidelity sweep.

For EVERY spec point in all 23 canonical bundles: extract the text of its
provenance page (PyMuPDF, independent of spec_parser's pdfplumber span-geometry
pipeline) and verify the statement text appears there, using two tiers:

  strict  — normalized statement text is a contiguous substring of the
            normalized page text (order-preserving verbatim evidence)
  tokens  — >=85% of the statement's significant tokens appear on the page
            (order-insensitive; catches column-interleave + glyph-order
            artifacts of the PDF text layer)

Every sub_item is checked the same way against the same page.
Outputs per-qual table + JSON; miss samples printed for eyeball check.
"""
import json, re, unicodedata
from pathlib import Path
import fitz  # PyMuPDF

RES = Path('/home/z/my-project/download/syllabai-resources')
BASE = RES / 'Official-Specifications'

def norm(s):
    if not s:
        return ''
    s = unicodedata.normalize('NFKC', s)
    s = s.replace('\ufb01', 'fi').replace('\ufb02', 'fl')
    for a, b in (('\u2018', "'"), ('\u2019', "'"), ('\u201c', '"'), ('\u201d', '"'),
                 ('\u2013', '-'), ('\u2014', '-'), ('\u00d7', 'x'), ('\u2212', '-'),
                 ('\u2022', ' ')):
        s = s.replace(a, b)
    s = re.sub(r'\s+', ' ', s)
    return s.strip().lower()

STOP = set('''a an the and or of to in on for with as by is are be been was were
it its this that these those which who whom whose at from into onto per e g i e
eg ie'''.split())

def toks(s):
    return [t for t in re.findall(r'[a-z0-9\u03b4\u0394]+', s) if t not in STOP and len(t) > 1]

quals = sorted([d.name for d in (BASE / 'parsed').iterdir()
                if d.is_dir() and not d.name.startswith('_')])
results = {}
miss_samples = {}
for q in quals:
    sp = json.loads((BASE / 'parsed' / q / 'spec_points.json').read_text())
    pdf_name = sp['source']['pdf']
    doc = fitz.open(BASE / q / pdf_name)
    page_cache = {}
    def page_text(pg):
        if pg not in page_cache:
            page_cache[pg] = norm(doc[pg - 1].get_text('text'))  # provenance pages are 1-based
        return page_cache[pg]
    strict = tok_ok = pts = 0
    item_strict = item_tok = item_tot = 0
    misses = []
    for p in sp['spec_points']:
        pg = p['provenance']['page']
        pt = page_text(pg)
        pts += 1
        s = norm(p['text'])
        hit = bool(s) and s in pt
        if not hit:
            tt = toks(s)
            cov = (sum(1 for t in tt if t in pt) / len(tt)) if tt else 1.0
            hit2 = cov >= 0.85
            if not hit2:
                misses.append({'id': p['id'], 'page': pg, 'cov': round(cov, 2),
                               'text': p['text'][:110]})
            tok_ok += hit2
        else:
            tok_ok += 1
        strict += hit
        for it in p.get('sub_items') or []:
            item_tot += 1
            si = norm(re.sub(r'^[\u2022\u00b7\u25cf]\s*', '', it))
            h = bool(si) and si in pt
            if not h:
                tt = toks(si)
                cov = (sum(1 for t in tt if t in pt) / len(tt)) if tt else 1.0
                h = cov >= 0.85
                if not h:
                    misses.append({'id': p['id'] + '+item', 'page': pg,
                                   'cov': round(cov, 2), 'text': it[:110]})
            item_strict += (bool(si) and si in pt)
            item_tok += h
    doc.close()
    results[q] = {
        'pdf': pdf_name, 'points': pts,
        'strict_hit': strict, 'token_hit': tok_ok,
        'sub_items_total': item_tot, 'sub_items_strict': item_strict,
        'sub_items_token': item_tok,
        'misses': misses,
    }
    miss_samples[q] = misses[:4]
    print(f"{q:40s} pts={pts:4d} strict={strict:4d} ({strict/pts*100:5.1f}%) "
          f"token>=85%={tok_ok:4d} ({tok_ok/pts*100:5.1f}%) "
          f"items={item_tot:4d} item_tok={item_tok:4d} hard_misses={len(misses)}")

out = RES / 'scripts' / 't_spec_norm_fidelity_sweep.json'
out.write_text(json.dumps({'results': results, 'miss_samples': miss_samples},
                          indent=1, ensure_ascii=False) + '\n')
print('\nwrote', out)
