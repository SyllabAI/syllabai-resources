#!/usr/bin/env python3
"""Diff Cognito channel uploads against the P1 site inventory + merged hub map."""
import json

ch = json.load(open("/home/z/my-project/work/channels/cognito-uploads.json"))
inv = json.load(open("/home/z/my-project/repos/syllabai-resources/Videos/inventory/cognito-lessons.json"))
hub = json.load(open("/home/z/my-project/repos/syllabai-v2/apps/hub/content/video-map/igcse-biology-19.json"))

site_ids = {}  # id -> [lesson keys]
for shelf, b in inv["shelves"].items():
    for L in b["lessons"]:
        for vid in [L.get("primaryVideoId")] + list(L.get("videoIds") or []):
            if vid and len(vid) == 11:
                site_ids.setdefault(vid, []).append(f"{shelf}:{L['key']}")

hub_ids = {v["id"] for v in hub["videos"]}
chan = {v["id"]: v for v in ch["videos"]}
site = set(site_ids)

print(f"channel uploads: {len(chan)}")
print(f"site inventory distinct ids: {len(site)}")
print(f"hub igcse-biology-19 ids: {len(hub_ids)}")
print(f"hub ids missing from site inventory: {len(hub_ids - site)}")
print(f"hub ids missing from channel: {sorted(hub_ids - set(chan))}")

only = sorted(set(chan) - site)
print(f"\nchannel-only (not on any crawled site page): {len(only)}")
shorts = [v for v in only if chan[v].get("duration") is not None and chan[v]["duration"] <= 90]
print(f"  of which <=90s (likely Shorts): {len(shorts)}")

# summarize channel-only non-shorts
rows = []
for vid in only:
    v = chan[vid]
    d = v.get("duration")
    rows.append((d if d is not None else -1, vid, v.get("title"), v.get("timestamp")))
rows.sort(reverse=True)
print(f"\n--- channel-only videos, longest first (top 60) ---")
for d, vid, t, ts in rows[:60]:
    import datetime
    dt = datetime.datetime.utcfromtimestamp(ts).strftime("%Y-%m-%d") if ts else "?"
    print(f"{vid}  {str(d)+'s' if d and d>0 else '??':>7}  {dt}  {(t or '')[:80]}")

json.dump({"channelOnly": [{"id": vid, "title": chan[vid].get("title"), "duration": chan[vid].get("duration"), "timestamp": chan[vid].get("timestamp")} for vid in only]},
          open("/home/z/my-project/work/channels/cognito-channel-only.json", "w"), ensure_ascii=False, indent=1)
