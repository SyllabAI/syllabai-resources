#!/usr/bin/env python3
"""P15 discovery: gap profile over the 96-course video-map corpus at hub main."""
import json, glob, os

TREE = '/tmp/hub-main-p15/apps/hub/content/video-map'
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

print(f"courses: {len(rows)}; corpus totals: spec points {sum(r['total'] or 0 for r in rows)}, mapped {sum(r['mapped'] or 0 for r in rows)}")
unmapped_total = sum(r['unmapped'] or 0 for r in rows if r['unmapped'])
print(f"total unmapped spec points: {unmapped_total}")

# honest-empty / zero rows first
zero = [r for r in rows if r['rows'] == 0]
print(f"\n== courses with 0 rows ({len(zero)}):")
for r in zero:
    print(f"   {r['course']:50s} {str(r['qual'])[:28]:28s} specs {r['total']}")

# worst coverage among courses WITH rows
partial = [r for r in rows if r['rows'] > 0 and r['unmapped'] and r['unmapped'] > 0]
partial.sort(key=lambda r: -r['unmapped'])
print(f"\n== courses with rows but unmapped specs, ranked by unmapped count ({len(partial)}):")
for r in partial[:30]:
    print(f"   {r['course']:50s} {str(r['qual'])[:28]:28s} {r['mapped']}/{r['total']} ({r['unmapped']} left, {r['pct']}%) rows {r['rows']}")
