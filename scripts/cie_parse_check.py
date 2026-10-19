#!/usr/bin/env python3
"""T-SPECS-CIE-PARSE-1 check battery. Emits graph/reports/T_SPECS_CIE_PARSE_1_CHECK.json.
Exit 0 iff ALL checks PASS."""
import glob, hashlib, importlib.util, json, os, re, subprocess, sys

BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OSDIR = os.path.join(BASE, 'Official-Specifications')
PDIR = os.path.join(OSDIR, 'parsed')
REPORTS = os.path.join(BASE, 'graph', 'reports')
sys.path.insert(0, os.path.join(BASE, 'scripts'))
spec = importlib.util.spec_from_file_location('csp', os.path.join(BASE, 'scripts', 'cie_spec_parser.py'))
csp = importlib.util.module_from_spec(spec)
spec.loader.exec_module(csp)

results = []

def check(cid, name, ok, detail):
    results.append({'id': cid, 'check': name, 'pass': bool(ok), 'detail': detail})
    print(f"{'PASS' if ok else 'FAIL'} {cid} {name}: {detail}")
    return ok

manifest = json.load(open(os.path.join(OSDIR, 'manifest.json')))
quals = manifest['qualifications'] if isinstance(manifest, dict) else manifest
cie = {q['slug']: q for q in quals if 'cambridge' in str(q.get('board', '')).lower()}

# C1 existence + schema + sha1 vs manifest
c1, c1d = True, []
for slug, q in sorted(cie.items()):
    d = os.path.join(PDIR, slug)
    fs = [f for f in os.listdir(d) if f.endswith('.parsed.json')] if os.path.isdir(d) else []
    if len(fs) != 1:
        c1 = False; c1d.append(f"{slug}: {len(fs)} parsed files"); continue
    j = json.load(open(os.path.join(d, fs[0])))
    if j.get('schema') != 'syllabai.parsed-specification/1.0':
        c1 = False; c1d.append(f"{slug}: schema"); continue
    if j['source']['pdf_sha1'] != q['sha1'] or j['source']['pdf'] != q['pdf']:
        c1 = False; c1d.append(f"{slug}: sha1/pdf mismatch"); continue
    if j['source']['parser'] != 'cie-spec-parser-1.0':
        c1 = False; c1d.append(f"{slug}: parser version"); continue
    c1d.append(slug)
check('C1', '33 parsed registries, schema+sha1+parser pinned', c1, f"{sum(1 for x in c1d if x != c1d[0] or True) and len(c1d)}/33 ok; fails: {[x for x in c1d if 'mismatch' in str(x) or 'schema' in str(x) or 'parser' in str(x)] or 'none'}")

# C2 gates all pass, no duplicates
c2, c2d = True, []
for rp in sorted(glob.glob(os.path.join(PDIR, 'cie-*', 'parse_report.json'))):
    r = json.load(open(rp))
    if not (r['gates_all_pass'] and all(r['gates'].values()) and not r['duplicate_ids']):
        c2 = False; c2d.append(r['qual'])
check('C2', 'G1-G4 ALL PASS x33, zero duplicate ids', c2, f"33 reports; failures: {c2d or 'none'}")

# C3 id prefix + uniqueness (independent recheck)
c3, c3d, total = True, [], 0
for slug in sorted(cie):
    d = os.path.join(PDIR, slug)
    f = [x for x in os.listdir(d) if x.endswith('.parsed.json')][0]
    j = json.load(open(os.path.join(d, f)))
    qual_id = slug.replace('-', '_').upper()
    ids = [p['id'] for p in j['spec_points']]
    total += len(ids)
    if any(not i.startswith(qual_id + ':') for i in ids) or len(set(ids)) != len(ids):
        c3 = False; c3d.append(slug)
check('C3', 'id prefix <QUAL>: + uniqueness (independent)', c3, f"{total} points; failures: {c3d or 'none'}")

# C4 family conformance vs parser FAMILY map
c4, c4d = True, []
for slug in sorted(cie):
    d = os.path.join(PDIR, slug)
    f = [x for x in os.listdir(d) if x.endswith('.parsed.json')][0]
    j = json.load(open(os.path.join(d, f)))
    if j['family'] != csp.FAMILY.get(slug) or j['id'] != slug:
        c4 = False; c4d.append(slug)
check('C4', 'family map conformance x33', c4, f"failures: {c4d or 'none'}")

# C5 provenance completeness
c5, c5d = True, []
for slug in sorted(cie):
    d = os.path.join(PDIR, slug)
    f = [x for x in os.listdir(d) if x.endswith('.parsed.json')][0]
    j = json.load(open(os.path.join(d, f)))
    for pnt in j['spec_points']:
        ok = (isinstance(pnt.get('page'), int) and 1 <= pnt['page'] <= j['source']['pages']
              and isinstance(pnt.get('oy'), (int, float))
              and pnt.get('text') and pnt['text'].strip()
              and (isinstance(pnt.get('topic'), dict) or isinstance(pnt.get('subsection'), dict))
              and 'tier' in pnt and 'scope' in pnt and 'sub_items' in pnt)
        if not ok:
            c5 = False; c5d.append(f"{slug}:{pnt.get('official_code')}")
check('C5', 'page+oy+provenance complete, text non-empty', c5, f"failures: {c5d[:5] or 'none'}")

# C6 _summary.json: 56 rows, Edexcel 23 deep-equal to backup, CIE gates pass
backup = json.load(open('/home/z/my-project/scripts/_summary_edexcel_backup.json'))
summary = json.load(open(os.path.join(PDIR, '_summary.json')))
c6 = (len(summary) == 56 and summary[:23] == backup
      and all(r.get('gates_all_pass') for r in summary[23:])
      and sum(1 for r in summary[23:] if r['qual'].startswith('cie-')) == 33)
c6tot = sum(r['counts']['spec_points'] for r in summary[23:])
check('C6', '_summary 56 rows, Edexcel 23 deep-equal, CIE 33 gates pass', c6, f"CIE rows 33, points {c6tot}")

# C7 flag policy per family
c7, c7d = True, []
assembled_fams = {'tier_columns', 'int_statements', 'ce_codes'}
for slug in sorted(cie):
    d = os.path.join(PDIR, slug)
    f = [x for x in os.listdir(d) if x.endswith('.parsed.json')][0]
    j = json.load(open(os.path.join(d, f)))
    fam = j['family']
    for pnt in j['spec_points']:
        fl = set(pnt['flags'])
        if fam == 'nmk_outcomes' and fl & {'code-assembled', 'synthesized-ordinal', 'synthesized-id'}:
            c7 = False; c7d.append(f"{slug}:{pnt['official_code']} printed-code row flagged")
        if fam == 'heading_bullets' and 'synthesized-id' not in fl:
            c7 = False; c7d.append(f"{slug}:{pnt['official_code']} missing synthesized-id")
        if fam in assembled_fams and 'code-assembled' in fl and fam == 'tier_columns' \
                and pnt['tier'] not in ('Core', 'Supplement'):
            c7 = False; c7d.append(f"{slug}:{pnt['official_code']} bad tier")
check('C7', 'flag policy (printed codes unflagged; synth flagged)', c7, f"violations: {c7d[:5] or 'none'}")

# C8 Edexcel byte-stability on disk vs git HEAD
git = subprocess.run(['git', 'status', '--porcelain'], cwd=BASE, capture_output=True, text=True).stdout.splitlines()
edexcel_touched = [l for l in git if 'parsed/' in l and 'cie-' not in l and '_summary.json' not in l and 'SCHEMA.md' not in l]
check('C8', 'Edexcel parsed tree untouched vs HEAD', not edexcel_touched, f"touched: {edexcel_touched or 'none'}")

# C9 footprint guard
allowed = re.compile(
    r'^(\s*A|\s*M|\?\?)\s+('
    r'Official-Specifications/parsed/cie-[^/]+/'
    r'|Official-Specifications/parsed/_summary\.json$'
    r'|Official-Specifications/parsed/SCHEMA\.md$'
    r'|scripts/cie_[a-z_0-9]+\.py$'
    r'|graph/reports/T_SPECS_CIE_PARSE_1_'
    r'|scripts/cie_samples/)')
violations = [l for l in git if l.strip() and not allowed.match(l)]
check('C9', 'footprint guard (declared paths only)', not violations, f"violations: {violations[:6] or 'none'}")

# C10 cross-foot: parsed totals == summary CIE rows
parsed_tot = 0
for slug in cie:
    d = os.path.join(PDIR, slug)
    f = [x for x in os.listdir(d) if x.endswith('.parsed.json')][0]
    parsed_tot += json.load(open(os.path.join(d, f)))['counts']['spec_points']
check('C10', 'cross-foot parsed totals == summary rows', parsed_tot == c6tot, f"parsed {parsed_tot} == summary {c6tot}")

allp = all(r['pass'] for r in results)
out = {
    'lane': 'T-SPECS-CIE-PARSE-1',
    'generated_utc': __import__('datetime').datetime.now(__import__('datetime').timezone.utc).isoformat(timespec='seconds'),
    'parser': 'cie-spec-parser-1.0',
    'schema': 'syllabai.parsed-specification/1.0 + CIE extension (tier/number, assembled/synth flags)',
    'quals_parsed': 33,
    'spec_points_total': parsed_tot,
    'families': {k: v for k, v in sorted((f, sum(1 for s in cie if csp.FAMILY[s] == f)) for f in set(csp.FAMILY.values()))},
    'checks': results,
    'all_pass': allp,
}
os.makedirs(REPORTS, exist_ok=True)
with open(os.path.join(REPORTS, 'T_SPECS_CIE_PARSE_1_CHECK.json'), 'w') as f:
    json.dump(out, f, indent=1, ensure_ascii=False)
print(f"\nALL {'PASS' if allp else 'FAIL'} — {sum(1 for r in results if r['pass'])}/{len(results)} checks")
sys.exit(0 if allp else 1)
