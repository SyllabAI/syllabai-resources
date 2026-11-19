#!/usr/bin/env python3
"""P14 spec-join census (the emitter's second gate, hub-side): over every
flags.videoMap course — mapping rows, spec refs, violations (unreviewed rows,
bad spec refs, dangling videos, duplicate video|specs keys). The P13 census
generalized: no work-dir dependency; the committed artifact of record is
scripts/p15/specjoin-census.json (per-course row/ref counts + violations).

Usage: python3 p15_specjoin_census.py [hubRoot]
  hubRoot defaults to the sibling clone at ../syllabai-v2-fresh.
"""
import json, os, sys

RES = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
HUB = sys.argv[1] if len(sys.argv) > 1 else os.path.join(
    os.path.dirname(RES), "syllabai-v2-fresh", "apps", "hub", "content")

fl = json.load(open(f"{HUB}/flags.json"))
courses = fl["flags"]["videoMap"]["courses"]

total_rows = total_refs = 0
violations = []
per_course = {}
for slug in courses:
    p = f"{HUB}/video-map/{slug}.json"
    if not os.path.exists(p):
        violations.append((slug, "MISSING CONTENT FILE"))
        continue
    d = json.load(open(p))
    vids = {v["id"] for v in d.get("videos", [])}
    spine = {n["code"] for n in json.load(open(f"{HUB}/{slug}/curriculum.json"))["nodes"]
             if n["family"] == "SPEC_POINT"}
    rows = d.get("mappings", [])
    refs = 0
    keys = set()
    for m in rows:
        total_refs += len(m.get("specs") or [])
        refs += len(m.get("specs") or [])
        if m.get("reviewed") is not True:
            violations.append((slug, f"unreviewed row {m.get('video')}"))
        for c in m.get("specs") or []:
            if c not in spine:
                violations.append((slug, f"bad spec ref {c} ({m.get('video')})"))
        if m.get("video") not in vids:
            violations.append((slug, f"dangling video {m.get('video')}"))
        k = m.get("video") + "|" + json.dumps(m.get("specs") or [], sort_keys=True)
        if k in keys:
            violations.append((slug, f"duplicate key {k[:60]}"))
        keys.add(k)
    total_rows += len(rows)
    per_course[slug] = {"rows": len(rows), "refs": refs, "videos": len(vids)}

print(f"census: {len(courses)} courses / {total_rows} rows / {total_refs} refs / {len(violations)} violations")
if violations:
    for v in violations[:20]:
        print("  VIOLATION:", v)
p15 = json.load(open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "p15-courses.json")))
touched = p15["pre"] + p15["post"]
print(f"\nP14-touched courses: {len(touched)}")
for slug in touched:
    r = per_course.get(slug)
    if r:
        print(f"  {slug}: {r['rows']} rows / {r['refs']} spec refs / {r['videos']} videos")

out = os.path.join(os.path.dirname(os.path.abspath(__file__)), "specjoin-census.json")
json.dump({
    "courses": len(courses), "rows": total_rows, "refs": total_refs,
    "violations": [list(v) for v in violations], "perCourse": per_course,
}, open(out, "w"), indent=1)
open(out, "a").write("\n")
print(f"wrote {out}")
