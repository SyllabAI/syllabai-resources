#!/usr/bin/env python3
"""Extract unmapped igcse-biology-19 spec statements + classify Cognito channel-only videos."""
import json, re

hub = json.load(open("/home/z/my-project/repos/syllabai-v2/apps/hub/content/video-map/igcse-biology-19.json"))
spine = json.load(open("/home/z/my-project/repos/syllabai-v2/apps/hub/spines/igcse-biology-19.json"))
ch = json.load(open("/home/z/my-project/work/channels/cognito-uploads.json"))

mapped = set()
for m in hub["mappings"]:
    if m.get("reviewed") and not str(m.get("specs", [""])[0]).startswith("REJ"):
        for s in m["specs"]:
            mapped.add(s)
# rejects do not count as mapped
for r in hub.get("review", {}).get("rejects", []):
    pass

pts = [n for n in spine["curriculum"]["nodes"] if n.get("family") == "SPEC_POINT"]
unmapped = [p for p in pts if p["code"] not in mapped]
print(f"mapped specs: {len(mapped)}  unmapped: {len(unmapped)}")

out = []
for p in unmapped:
    out.append({"code": p["code"], "title": p["title"], "parents": p.get("parents")})
json.dump(out, open("/home/z/my-project/work/channels/unmapped-specs.json", "w"), ensure_ascii=False, indent=1)
for p in out:
    print(f"  {p['code']:>6}  {p['title'][:110]}")

# classify channel-only videos by subject prefix
co = json.load(open("/home/z/my-project/work/channels/cognito-channel-only.json"))["channelOnly"]
def subject(t):
    if not t: return "unknown"
    for pre, lab in [
        ("GCSE Biology", "gcse-bio"), ("A-Level Biology", "alevel-bio"), ("KS3 Biology", "ks3-bio"),
        ("GCSE Chemistry", "gcse-chem"), ("A-Level Chemistry", "alevel-chem"), ("KS3 Chemistry", "ks3-chem"),
        ("GCSE Physics", "gcse-phys"), ("A-Level Physics", "alevel-phys"), ("KS3 Physics", "ks3-phys"),
        ("GCSE Maths", "gcse-maths"), ("A-Level Maths", "alevel-maths"), ("KS3 Maths", "ks3-maths"),
        ("GCSE", "gcse-other"), ("A-Level", "alevel-other"), ("KS3", "ks3-other"), ("Psychology", "psych"),
    ]:
        if t.startswith(pre): return lab
    return "other"
import collections
c = collections.Counter(subject(v["title"]) for v in co)
print("\nchannel-only by subject:", dict(c.most_common()))
gb = [v for v in co if subject(v["title"]) == "gcse-bio"]
print(f"\nGCSE Biology channel-only ({len(gb)}):")
for v in sorted(gb, key=lambda x: x["title"] or ""):
    d = v.get("duration")
    print(f"  {v['id']}  {str(int(d))+'s' if d else '??':>6}  {v['title'][:95]}")
json.dump(gb, open("/home/z/my-project/work/channels/cognito-only-gcse-bio.json", "w"), ensure_ascii=False, indent=1)
