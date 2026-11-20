#!/usr/bin/env python3
"""P17 gap profile: fresh residual over the 96-course video-map corpus at hub main.

Post-P15/P16 state — the coverage blocks in the shipped files reflect the P15
(+1,899 rowsApproved) and P16 (+100 lit-21) emits, so this is the CURRENT gap
map, not the stale pre-P15 numbers quoted in the P15 receipt.
"""
import json, glob, os

TREE = '/tmp/hub-main-p17/apps/hub/content/video-map'
OUT = os.path.join(os.path.dirname(__file__), 'gap_profile_p17.json')

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
    'utc': '2026-11-20',
    'courses': len(rows),
    'specPointsTotal': sum(r['total'] or 0 for r in rows),
    'specPointsMapped': sum(r['mapped'] or 0 for r in rows),
    'specPointsUnmapped': sum(r['unmapped'] or 0 for r in rows if r['unmapped']),
    'rows': rows,
}
json.dump(summary, open(OUT, 'w'), indent=1)

print(f"courses: {summary['courses']}; spec points {summary['specPointsTotal']}, "
      f"mapped {summary['specPointsMapped']}, unmapped {summary['specPointsUnmapped']}")
zero = [r for r in rows if r['rows'] == 0]
print(f"\n== courses with 0 rows ({len(zero)}):")
for r in zero:
    print(f"   {r['course']:50s} {str(r['qual'])[:30]:30s} specs {r['total']}")
print(f"\n== residual ranked by unmapped (top 40 of {sum(1 for r in rows if (r['unmapped'] or 0) > 0)}):")
for r in rows[:40]:
    if not r['unmapped']:
        break
    print(f"   {r['course']:50s} {str(r['qual'])[:30]:30s} {r['mapped']}/{r['total']} ({r['unmapped']} left, {r['pct']}%) rows {r['rows']}")
