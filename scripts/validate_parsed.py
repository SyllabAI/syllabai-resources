#!/usr/bin/env python3
"""Validator v2: parsed spec JSONs vs SME spec_point_index.
- haystack = statement text + sub_items (bullets)
- strips '(physics only)'-style qualifiers from both sides
- modular courses mapped to modular quals
- name-only SME indexes (IAL, maths, econ, ...) -> count-parity report only
"""
import glob, json, os, re, unicodedata

RES = '/home/z/my-project/download/syllabai-resources'
PARSED = f'{RES}/Official-Specifications/parsed'
SME = f'{RES}/SME-ExamQuestion'

def qual_of(course):
    if course.startswith('igcse-science-double-award'):
        return 'igcse-science-double-award'
    if 'modular' in course:
        m = re.match(r'(igcse-[a-z-]+)-modular', course)
        return m.group(1) + '-modular'
    if course.startswith('ial-'):
        m = re.match(r'(ial-[a-z-]+)-\d{2}', course)
        if m and m.group(1) in ('ial-maths',):
            return 'ial-maths'
        if course.startswith('ial-further-maths'):
            return 'ial-maths'
        return m.group(1)
    m = re.match(r'(igcse-[a-z-]+)-\d{2}', course)
    q = m.group(1)
    for tail in ('-foundation', '-higher', '-financial-statements',
                 '-introduction-to-bookkeeping-and-accounting'):
        if q.endswith(tail):
            q = q[:-len(tail)]
    return q

QUALIFIER = re.compile(r'\s*\((?:physics|chemistry|biology|chemistry \(single award\)|'
                       r'biology \(single award\)|physics \(single award\)|double award) only\)', re.I)

def norm(s):
    if not s:
        return ''
    s = unicodedata.normalize('NFKC', s)
    s = s.replace('\ufb01', 'fi').replace('\ufb02', 'fl')
    for a, b in (('\u2018', "'"), ('\u2019', "'"), ('\u201c', '"'), ('\u201d', '"'),
                 ('\u2013', '-'), ('\u2014', '-'), ('\u00d7', 'x'), ('\u2212', '-')):
        s = s.replace(a, b)
    s = re.sub(r'[\s]+', ' ', s)
    return s.strip().lower()

def mnorm(s):
    """match-normalization: drop bullet glyphs, sentence periods, core-practical
    prefixes, and collapse notation runs split by sub/sup satellites
    (R f -> rf, δ h -> δh, m c δ t -> mcδt, dm 3 -> dm3)."""
    s = norm(s)
    s = re.sub(r'^(?:core\s+)?practical\s*\d*\s*:\s*', '', s)
    s = s.replace('\u2022', ' ').replace('.', ' ')
    s = re.sub(r'[\s]+', ' ', s)
    prev = None
    while prev != s:
        prev = s
        s = re.sub(r'\b([a-z\u03b4\u0394]) ([a-z0-9\u03b4\u0394])\b', r'\1\2', s)
    return s.strip()

# load parsed per qual: haystack = joined text + sub_items
parsed = {}
for d in sorted(glob.glob(f'{PARSED}/*/')):
    q = d.rstrip('/').rsplit('/', 1)[-1]
    if q.startswith('_'):
        continue
    stmts = []
    for f in glob.glob(f'{d}/*.parsed.json'):
        stmts.extend(json.load(open(f))['spec_points'])
    parsed[q] = stmts

rows = []
report = {}
for course in sorted(os.listdir(SME)):
    p = f'{SME}/{course}/spec_point_index.json'
    if not os.path.exists(p):
        continue
    q = qual_of(course)
    idx = json.load(open(p))
    sps = list(idx['spec_points'].values())
    stmts = parsed.get(q, [])
    # per-statement haystack so misses can point at statements
    hays = []
    for s in stmts:
        parts = [s['text']] + list(s.get('sub_items') or [])
        hays.append(mnorm(QUALIFIER.sub('', ' '.join(parts))))
    joined = ' || '.join(hays)
    defs = []
    for sp in sps:
        dtext = mnorm(QUALIFIER.sub('', sp.get('definition') or ''))
        if dtext:
            defs.append(dtext)
    hit = sum(1 for d in defs if d in joined)
    report.setdefault(q, {'courses': [], 'sme': 0, 'defs': 0, 'hit': 0,
                          'pdf': len(stmts)})
    report[q]['courses'].append({'course': course, 'sme': len(sps),
                                 'defs': len(defs), 'hit': hit})
    report[q]['sme'] += len(sps)
    report[q]['defs'] += len(defs)
    report[q]['hit'] += hit

print(f"{'qual':32} {'SME':>5} {'PDF':>5} {'defs':>5} {'hit':>5} {'rate':>7}")
for q in sorted(report):
    r = report[q]
    rate = r['hit'] / r['defs'] * 100 if r['defs'] else float('nan')
    print(f"{q:32} {r['sme']:5} {r['pdf']:5} {r['defs']:5} {r['hit']:5} "
          f"{(f'{rate:6.1f}%' if r['defs'] else '    n/a'):>7}")

json.dump(report, open(f'{PARSED}/_sme_crossref.json', 'w'), indent=1, ensure_ascii=False)

# miss samples for def-ful quals below 85%
print('\nmiss samples:')
for q in sorted(report):
    r = report[q]
    if not r['defs'] or r['hit'] / r['defs'] >= 0.85:
        continue
    print(f'--- {q} ({r["hit"]}/{r["defs"]})')
    shown = 0
    for course in r['courses']:
        idx = json.load(open(f'{SME}/{course["course"]}/spec_point_index.json'))
        for sp in list(idx['spec_points'].values()):
            dtext = mnorm(QUALIFIER.sub('', sp.get('definition') or ''))
            if not dtext:
                continue
            stmts = parsed.get(q, [])
            hays = [mnorm(QUALIFIER.sub('', ' '.join([s['text']] + list(s.get('sub_items') or []))))
                    for s in stmts]
            if dtext not in ' || '.join(hays) and shown < 3:
                print('   MISS:', dtext[:95])
                shown += 1
        if shown >= 3:
            break
