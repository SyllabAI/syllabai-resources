#!/usr/bin/env python3
"""P20 gap profile: fresh residual over the 96-course video-map corpus at hub main.

Post-P19 state — the coverage blocks in the shipped files reflect the P19 emit
(+1,091 rowsApproved direct + the P4-inherit cascade), so this is the CURRENT gap
map, not the stale P19-filing numbers (2,932 unmapped) quoted in the P19 receipt.
"""
import json, glob, os

TREE = '/tmp/hub-main-p20/apps/hub/content/video-map'
OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'gap_profile_p20.json')

rows = []
for p in sorted(glob.glob(TREE + '/*.json')):
    if p.endswith('registry.json'):
        continue
    d = json.load(open(p))
    cov = d.get('coverage') or {}
    tot = cov.get('specPointsTotal') or 0
    mapped = cov.get('specPointsMapped') or 0
    unmapped = cov.get('specPointsUnmapped') or (tot - mapped if tot else None)
    appr = (d.get('review') or {}).get('rowsApproved') or 0
    rows.append({
        'course': d.get('course'),
        'qual': d.get('qual'),
        'total': tot,
        'mapped': mapped,
        'unmapped': unmapped,
        'rows': appr,
        'pct': round(100 * mapped / tot) if tot else None,
    })

rows.sort(key=lambda r: -(r['unmapped'] or 0))
summary = {
    'utc': '2026-11-26',
    'lane': 'p20-gap-profile',
    'baseHub': '1389bf21',
    'courses': len(rows),
    'specPointsTotal': sum(r['total'] or 0 for r in rows),
    'specPointsMapped': sum(r['mapped'] or 0 for r in rows),
    'specPointsUnmapped': sum(r['unmapped'] or 0 for r in rows if r['unmapped']),
    'rows': rows,
}
json.dump(summary, open(OUT, 'w'), indent=1)
open(OUT, 'a').write('\n')

print(f"courses: {summary['courses']}; spec points {summary['specPointsTotal']}, "
      f"mapped {summary['specPointsMapped']}, unmapped {summary['specPointsUnmapped']}")
zero = [r for r in rows if r['rows'] == 0]
print(f"\n== courses with 0 rows ({len(zero)}):")
for r in zero:
    print(f"   {r['course']:50s} {str(r['qual'])[:30]:30s} specs {r['total']}")
res = [r for r in rows if (r['unmapped'] or 0) > 0]
print(f"\n== residual ranked by unmapped (top 50 of {len(res)}):")
for r in res[:50]:
    print(f"   {r['course']:50s} {str(r['qual'])[:30]:30s} {r['mapped']}/{r['total']} ({r['unmapped']} left, {r['pct']}%) rows {r['rows']}")
