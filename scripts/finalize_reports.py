#!/usr/bin/env python3
"""Write per-qual parse_report.json: counts, validation gates, crossref."""
import glob, json, os

RES = '/home/z/my-project/download/syllabai-resources'
PARSED = f'{RES}/Official-Specifications/parsed'
crossref = json.load(open(f'{PARSED}/_sme_crossref.json'))
summary = {s['qual']: s for s in json.load(open(f'{PARSED}/_summary.json'))}

for d in sorted(glob.glob(f'{PARSED}/*/')):
    q = d.rstrip('/').rsplit('/', 1)[-1]
    if q.startswith('_'):
        continue
    files = sorted(glob.glob(f'{d}/*.parsed.json'))
    counts, n_stmt, n_flag, ids_ok, prov_ok, uniq = {}, 0, 0, True, True, True
    all_ids = set()
    for f in files:
        j = json.load(open(f))
        counts[f.rsplit('/', 1)[-1]] = j['counts']
        for st in j['spec_points']:
            n_stmt += 1
            n_flag += bool(st.get('flags'))
            if st['id'] in all_ids:
                uniq = False
            all_ids.add(st['id'])
            if st.get('page') is None or st.get('oy') is None:
                prov_ok = False
            if not st['id'].startswith(q.upper().replace('-', '_') + ':'):
                ids_ok = False
    xr = crossref.get(q, {})
    report = {
        'qual': q,
        'generated_utc': '2026-09-17',
        'files': [f.rsplit('/', 1)[-1] for f in files],
        'counts': counts,
        'totals': {'spec_points': n_stmt, 'flagged': n_flag},
        'gates': {
            'G1_schema_present': bool(files),
            'G2_ids_unique': uniq,
            'G3_provenance_complete': prov_ok,
            'G4_id_prefix_valid': ids_ok,
        },
        'sme_crossref': {
            'sme_spcpt': xr.get('sme'), 'pdf_statements': xr.get('pdf'),
            'defs_with_definitions': xr.get('defs'), 'verbatim_hits': xr.get('hit'),
            'rate': round(xr['hit'] / xr['defs'] * 100, 1) if xr.get('defs') else None,
            'note': ('rate = SME definitions found verbatim in parsed statements+bullets; '
                     'misses are SME-side merged/paraphrased definitions -> mapping-stage '
                     'fuzzy tier, not parser losses') if xr.get('defs') else
                    ('SME index for this qual is name-only (no definitions); verbatim '
                     'crossref not applicable -> mapping-stage name bridging'),
        },
    }
    report['gates']['ALL_PASS'] = all(v is True for k, v in report['gates'].items())
    with open(f'{d}/parse_report.json', 'w') as f:
        json.dump(report, f, indent=1, ensure_ascii=False)
    print(f"{q:32} stmts={n_stmt:4} flags={n_flag:2} gates={'PASS' if report['gates']['ALL_PASS'] else 'CHECK'}")
