#!/usr/bin/env python3
"""P10 recon (re-run): flat-enumerate MrArnoldsMaths + Maths Deity pools,
dedupe by video id, emit raw TSV + inventory JSON (schema identical to
mrhassansmaths-uploads.json). Identities verified separately via page-HTML
externalId grep."""
import json, subprocess, datetime, os

RES = "/home/z/my-project/repos/syllabai-resources"
WORK = "/home/z/my-project/work"
CHANNELS = [
    {"name": "MrArnoldsMaths", "channelId": "UCwa84m5RqSJEkP9pYdeDYnw",
     "url": "https://www.youtube.com/@MrArnoldsMaths/videos",
     "inv": "mrarnoldsmaths-uploads.json", "tsv": "p10_mrarnolds_raw.tsv"},
    {"name": "Maths Deity", "channelId": "UCODyYjai6abd1N5KGc1KacQ",
     "url": "https://www.youtube.com/@MathsDeity/videos",
     "inv": "mathsdeity-uploads.json", "tsv": "p10_mathsdeity_raw.tsv"},
]
FMT = "%(id)s\t%(title)s\t%(duration)s\t%(view_count)s\t%(timestamp)s\t%(channel_id)s"

for ch in CHANNELS:
    print(f"== {ch['name']} ({ch['channelId']})", flush=True)
    r = subprocess.run(["yt-dlp", "--flat-playlist", "--playlist-items", "1-4000",
                        "--print", FMT, ch["url"]], capture_output=True, text=True)
    if r.returncode != 0:
        print("STDERR tail:", r.stderr[-300:])
    rows, seen, dup = [], set(), 0
    for l in r.stdout.splitlines():
        p = (l.split("\t") + [""] * 6)[:6]
        vid, title, dur, views, ts, cid = p
        if not vid or vid in ("NA", "None") or vid in seen:
            if vid in seen: dup += 1
            continue
        seen.add(vid)
        def num(x):
            try: return int(float(x))
            except Exception: return None
        rows.append({"id": vid, "title": title, "duration": num(dur),
                     "viewCount": num(views),
                     "timestamp": num(ts) if ts not in ("NA", "None", "") else None})
    with open(os.path.join(WORK, ch["tsv"]), "w") as f:
        for v in rows:
            f.write("\t".join(str(v[k]) for k in ("id", "title", "duration", "viewCount", "timestamp")) + "\n")
    inv = {"channel": ch["name"], "channelId": ch["channelId"], "channelUrl": ch["url"],
           "playlistTitle": f"{ch['name']} uploads", "count": len(rows),
           "enumeratedUtc": datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
           "videos": rows}
    with open(os.path.join(RES, "Videos/inventory/channels", ch["inv"]), "w") as f:
        json.dump(inv, f, ensure_ascii=False, indent=1)
    print(f"rows={len(rows)} dupes={dup}")
print("DONE")
