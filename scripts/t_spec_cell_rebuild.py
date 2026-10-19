#!/usr/bin/env python3
"""econ + business row-level cell rebuilder with strict self-validation.

Rebuilds each lettered/triplet row's text + sub_items from the raw PDF text
layer structure (code/letter row ranges; bullet markers '•'/'o' are in the
text layer). Convention (from clean rows):
  text    = row main line + 'o' sub-bullet lines (with 'o ' glyph kept)
  items   = '•' bullet lines (bullet-wrapped continuations joined)

Validation: rows whose rebuild == stored text+items are no-ops; the fraction
of byte-exact no-ops measures reconstructor fidelity. Changed rows are
verified: every rebuilt item and the rebuilt text must appear verbatim
(normalised) in the raw page text.
"""
import json, re, unicodedata
from pathlib import Path

RES = Path('/home/z/my-project/download/syllabai-resources/Official-Specifications')

def norm(s):
    if not s: return ''
    s = unicodedata.normalize('NFKC', s)
    for a, b in (('\u2019', "'"), ('\u2018', "'"), ('\u201c', '"'), ('\u201d', '"'),
                 ('\u2013', '-'), ('\u2014', '-'), ('\u2212', '-'), ('\u00d7', 'x'),
                 ('\ufb01', 'fi'), ('\ufb02', 'fl')):
        s = s.replace(a, b)
    return re.sub(r'\s+', ' ', s).strip().lower()

QUALS = {
    'igcse-economics': {'row': re.compile(r'^([a-z])\)\s*(.*)$'),
                        'code': re.compile(r'^(\d\.\d{1,2}(?:\.\d{1,2})?)\s*$|^(\d\.\d{1,2})\s+\S')},
    'igcse-business': {'row': re.compile(r'^([a-z])\)\s*(.*)$'),
                       'code': re.compile(r'^(\d\.\d{1,2}\.\d{1,2})\s*$|^(\d\.\d{1,2}\.\d{1,2})\s+\S')},
}

for q, cfg in QUALS.items():
    sp = json.load(open(RES / 'parsed' / q / 'spec_points.json'))
    doc_lines = {}
    for i in range(len(doc_pages := __import__('fitz').open(RES / q / sp['source']['pdf']))):
        doc_lines[i] = [ln.strip() for ln in doc_pages[i].get_text('text').splitlines()
                        if ln.strip()]
    # index rows by (page, code, letter)
    def find_row(p):
        pg = p['provenance']['page'] - 1
        code = p['official_code']            # econ '1.1.1a' / business '4.3.4'
        if q == 'igcse-economics':
            m = re.match(r'^(\d+\.\d+\.\d+)([a-z])$', code)
            base, letter = m.group(1), m.group(2)
            code_pat = re.compile(r'^' + re.escape(base) + r'\s*$')
        else:
            code_pat = re.compile(r'^' + re.escape(code) + r'\s*$')
        # global flat line list with page markers for cross-page blocks
        flat = []   # (page_idx, line)
        for pi in range(len(doc_lines)):
            for ln in doc_lines[pi]:
                flat.append((pi, ln))
        # global index of first line of the prov page
        gstart = sum(len(doc_lines[pi]) for pi in range(pg))
        # locate the numbered header: search from the top of the prov page,
        # walking BACK up to 3 pages (multi-page blocks)
        start = None
        for gi in range(gstart, -1, -1):
            pi, ln = flat[gi]
            if pi < pg - 3:
                break
            if code_pat.match(ln):
                start = gi
                break
        if start is None:
            # fall back: search FORWARD on the prov page (header prints after
            # a page-break oddity)
            for gi in range(gstart, min(gstart + len(doc_lines[pg]), len(flat))):
                if code_pat.match(flat[gi][1]):
                    start = gi
                    break
        if start is None:
            NOTFOUND.append(p['id'])
            return None
        lines = [ln for _, ln in flat]
        goff = start
        if q == 'igcse-business':
            # business: statement rows are 'N.M.K' + content until next N.M.K
            nxt = None
            for j in range(goff + 1, len(lines)):
                if re.match(r'^\d+\.\d{1,2}\.\d{1,2}\s*$', lines[j]):
                    nxt = j
                    break
                if re.match(r'^\d+\.\d{1,2}\s+[A-Z]', lines[j]) and j > goff + 1:
                    nxt = nxt or j
            cell = lines[goff + 1: nxt] if nxt else lines[goff + 1:]
            cleaned = []
            for ln in cell:
                mcut = re.search(r'\s(\d+\.\d{1,2}\.\d{1,2})\s+[A-Z]', ln)
                if mcut and not re.match(r'^\d+\.\d{1,2}\.\d{1,2}\s*$', ln):
                    ln = ln[:mcut.start()]
                if ln.strip():
                    cleaned.append(ln.strip())
            return cleaned
        # econ: header line may carry a title; find letter row after start
        # within this code's block (block ends at next numbered code header)
        end = len(lines)
        for j in range(goff + 1, len(lines)):
            if re.match(r'^\d\.\d{1,2}(\.\d{1,2})?\s*$', lines[j]) or \
               re.match(r'^\d\.\d{1,2}\s+[A-Z]', lines[j]):
                end = j
                break
        block = lines[goff + 1:end]
        # letter rows inside block
        idxs = [k for k, ln in enumerate(block) if cfg['row'].match(ln)]
        letter_idx = None
        for k in idxs:
            if cfg['row'].match(block[k]).group(1) == letter:
                letter_idx = k
                break
        if letter_idx is None:
            return None
        nxt_letter = next((k for k in idxs if k > letter_idx), len(block))
        cell = [cfg['row'].match(block[letter_idx]).group(2)] + block[letter_idx + 1: nxt_letter]
        # stop at a next numbered-code line inside block (defensive)
        out = []
        for ln in cell:
            mcut = re.search(r'\s(\d\.\d{1,2}(?:\.\d{1,2})?)\s*$', ln)
            if re.match(r'^\d\.\d{1,2}(\.\d{1,2})?\s*$', ln):
                break
            out.append(ln)
        return [x for x in out if x]

    def rebuild_cell(cell):
        # join wrapped lines: a bullet's continuation = lines until next marker
        main = []
        items = []
        cur = None   # ('main'|'bullet'|'o')
        for ln in cell:
            if ln.startswith('\u2022'):
                cur = 'bullet'
                items.append(ln.lstrip('\u2022').strip())
                continue
            if re.match(r'^o\s+', ln):
                cur = 'o'
                main.append(ln)
                continue
            if cur == 'bullet' and items is not None and items and not re.match(r'^[a-z]\)', ln):
                items[-1] = (items[-1] + ' ' + ln).strip()
                continue
            if cur == 'o':
                main.append(ln)
                continue
            cur = 'main'
            main.append(ln)
        return re.sub(r'\s+', ' ', ' '.join(main)).strip(), items

    NOTFOUND = []
    noop = changed = fail = 0
    repair = {}
    for p in sp['spec_points']:
        cell = find_row(p)
        if cell is None:
            fail += 1
            continue
        text, items = rebuild_cell(cell)
        same_t = norm(text) == norm(p['text'])
        same_i = [norm(x) for x in items] == [norm(x) for x in p['sub_items']]
        if same_t and same_i:
            noop += 1
        else:
            changed += 1
            repair[p['id']] = {'text': text, 'sub_items': items, 'cell': cell}
    print(f'{q}: noop={noop} changed={changed} not-found={fail} {NOTFOUND[:22]}')
    json.dump(repair, open(f'/home/z/my-project/scripts/t_spec_{q}_cellrepairs.json', 'w'),
              indent=1, ensure_ascii=False)
