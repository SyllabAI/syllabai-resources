#!/usr/bin/env python3
"""P13 spec-join census (the emitter's second gate, hub-side): over every flags.videoMap
course — mapping rows, spec refs, violations (unreviewed rows, bad spec refs, dangling
videos, duplicate video|specs keys)."""
import json, os, glob

HUB = "/home/z/my-project/repos/syllabai-v2-fresh/apps/hub/content"
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
    spine = {n["code"] for n in json.load(open(f"{HUB}/{slug}/curriculum.json"))["nodes"] if n["family"] == "SPEC_POINT"}
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
    per_course[slug] = (len(rows), refs, len(vids))

print(f"census: {len(courses)} courses / {total_rows} rows / {total_refs} refs / {len(violations)} violations")
if violations:
    for v in violations[:20]:
        print("  VIOLATION:", v)
bad = {k: v for k, v in per_course.items() if "p13" in json.load(open(f'{HUB}/video-map/{k}.json')).get("source", {}).get("provider", "") + str(json.load(open(f'{HUB}/video-map/{k}.json')).get("inputs", {}))}
print(f"\nP13-touched courses: {len(json.load(open('/home/z/my-project/work/p13/p13-courses.json'))['pre'] + json.load(open('/home/z/my-project/work/p13/p13-courses.json'))['post'])}")
json.dump(per_course, open("/home/z/my-project/work/p13/specjoin-census.json", "w"), indent=1)
