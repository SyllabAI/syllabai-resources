#!/usr/bin/env python3
"""
T-SPEC-NORM-1 — cross-qual normalization audit of the canonical 7-file
specification bundles (23 quals) + derived Layer-A graph YAMLs.

Checks per qual:
  C1  all 7 bundle files present + JSON-parseable
  C2  spec_points.json: uniform point field set, id prefix == QUAL,
      ids unique, provenance complete (pdf/sha1/page/oy), counts block
      matches actual, applicability/leading_verb present
  C3  topics.json / practicals.json / equations.json /
      assessment_objectives.json / command_words.json: top-level key sets
  C4  parse_report.json: gates all pass, canonical counts consistent
  C5  v1.0 parsed.json spec_points count == canonical count
  C6  _derived/graph/<qual>/ 4 YAMLs present (loader contract)
Prints a per-qual matrix + global field-set variants.
"""
import json, sys, collections, re
from pathlib import Path

BASE = Path('/home/z/my-project/download/syllabai-resources/Official-Specifications/parsed')
BUNDLE = ['spec_points.json', 'topics.json', 'practicals.json', 'equations.json',
          'assessment_objectives.json', 'command_words.json', 'parse_report.json']
quals = sorted([d.name for d in BASE.iterdir() if d.is_dir() and not d.name.startswith('_')])

def jload(p):
    return json.loads(p.read_text())

problems = []
fieldsets = collections.Counter()
topkeys = {f.replace('.json', ''): collections.Counter() for f in BUNDLE if f != 'parse_report.json'}
idshapes = collections.defaultdict(set)
rows = []

def shape(tail):
    if re.fullmatch(r'S\d+\.\d+', tail): return 'S<sec>.<nnn>'
    if re.fullmatch(r'[A-Za-z0-9]+-\d+\.\d+[A-C]?', tail): return '<scope>-<N.M>'
    if re.fullmatch(r'M\d+-\d+\.\d+', tail): return 'M<unit>-<N.M>'
    if re.fullmatch(r'\d+\.\d+[A-C]?', tail): return '<N.M>[suffix]'
    if re.fullmatch(r'\d+\.\d+\.\d+[a-e]?', tail): return '<N.M.K>[letter]'
    if re.fullmatch(r'\d+', tail): return '<int>'
    return 'OTHER:' + tail

for q in quals:
    r = {'qual': q}
    missing = [f for f in BUNDLE if not (BASE/q/f).exists()]
    r['missing_files'] = missing
    if missing:
        problems.append(f'{q}: missing bundle files {missing}')
        rows.append(r); continue
    try:
        sp = jload(BASE/q/'spec_points.json')
        tp = jload(BASE/q/'topics.json')
        pr = jload(BASE/q/'practicals.json')
        eq = jload(BASE/q/'equations.json')
        ao = jload(BASE/q/'assessment_objectives.json')
        cw = jload(BASE/q/'command_words.json')
        rp = jload(BASE/q/'parse_report.json')
        v1 = jload(next((BASE/q).glob('*.parsed.json')))
    except Exception as e:
        problems.append(f'{q}: JSON parse error {e!r}'); rows.append(r); continue

    for name, obj in [('spec_points', sp), ('topics', tp), ('practicals', pr),
                      ('equations', eq), ('assessment_objectives', ao),
                      ('command_words', cw)]:
        topkeys[name][tuple(sorted(obj.keys()))] += 1

    pts = sp['spec_points']
    qual_prefix = q.upper().replace('-', '_')
    fs = collections.Counter(tuple(sorted(p.keys())) for p in pts)
    if len(fs) > 1:
        problems.append(f'{q}: {len(fs)} distinct spec_point field sets')
    ids = [p['id'] for p in pts]
    if len(set(ids)) != len(ids):
        problems.append(f'{q}: duplicate ids')
    badpre = [i for i in ids if not i.startswith(qual_prefix + ':')]
    if badpre:
        problems.append(f'{q}: {len(badpre)} ids without {qual_prefix}: e.g. {badpre[:3]}')
    nopro = [p['id'] for p in pts if not (p.get('provenance') or {}).get('page')
             or (p.get('provenance') or {}).get('oy') is None
             or not (p.get('provenance') or {}).get('pdf')
             or not (p.get('provenance') or {}).get('pdf_sha1')]
    if nopro:
        problems.append(f'{q}: {len(nopro)} points missing provenance, e.g. {nopro[:3]}')
    noapp = [p['id'] for p in pts if 'applicability' not in p]
    if noapp:
        problems.append(f'{q}: {len(noapp)} points missing applicability, e.g. {noapp[:3]}')
    nov = [p['id'] for p in pts if 'leading_verb' not in p]
    if nov:
        problems.append(f'{q}: {len(nov)} points missing leading_verb, e.g. {nov[:3]}')
    cnt = sp.get('counts', {})
    if cnt.get('spec_points') != len(pts):
        problems.append(f"{q}: counts.spec_points={cnt.get('spec_points')} != actual {len(pts)}")
    r['points'] = len(pts)
    r['practical_flag'] = sum(1 for p in pts if p.get('practical'))
    r['flags'] = sum(1 for p in pts if p.get('flags'))
    r['fields'] = list(fs.keys())[0] if len(fs) == 1 else 'VARIABLE'

    for i in ids:
        idshapes[q].add(shape(i.split(':', 1)[1]))
    r['id_shapes'] = sorted(idshapes[q])

    gates = rp.get('gates') or {}
    gp = all(bool(v) for v in gates.values()) and bool(gates)
    r['gates_all_pass'] = gp
    if gp is not True:
        problems.append(f'{q}: gates not ALL_PASS: {r.get("gates")}')
    cb = rp.get('canonical_bundle') or {}
    if cb.get('spec_points') not in (None, len(pts)):
        problems.append(f'{q}: parse_report.canonical_bundle.spec_points={cb.get("spec_points")} != {len(pts)}')

    v1n = len(v1.get('spec_points', []))
    if v1n != len(pts):
        problems.append(f'{q}: v1 parsed {v1n} points != canonical {len(pts)}')

    der = BASE/'_derived'/'graph'/q
    r['derived'] = sorted(p.name for p in der.glob('*.yaml')) if der.exists() else []
    if len(r['derived']) != 4:
        problems.append(f'{q}: derived graph YAMLs missing ({len(r["derived"])}/4)')
    rows.append(r)

print('=' * 108)
for r in rows:
    print(f"{r['qual']:42s} pts={r.get('points','-'):>4} prac={r.get('practical_flag','-'):>3} "
          f"flagged={r.get('flags','-'):>3} shapes={','.join(r.get('id_shapes',[])) or '-':30s} "
          f"derived={len(r.get('derived',[]))}/4")
print('=' * 108)
print('spec_point field-set variants across quals:')
variants = collections.Counter()
for (q, ks), n in fieldsets.items():
    variants[ks] += 1
for ks, nq in variants.items():
    print(f'  {nq:2d} quals: {list(ks)}')
print('top-level key-set variants per file:')
for name, c in topkeys.items():
    uniq = set(c.keys())
    print(f'  {name}: {len(uniq)} variant(s)')
    if len(uniq) > 1:
        for u in uniq: print('     *', list(u))
print('id-shape classes per qual:')
for q in sorted(idshapes): print(f'  {q:42s} {sorted(idshapes[q])}')
print()
if problems:
    print(f'PROBLEMS ({len(problems)}):')
    for p in problems: print('  -', p)
else:
    print('NO PROBLEMS FOUND')
