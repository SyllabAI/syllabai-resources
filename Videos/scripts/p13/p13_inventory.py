#!/usr/bin/env python3
"""P13 inventory: 8 Alt Academy family raw TSVs -> P9-schema channel inventory JSONs.
The business subject channel is EXCLUDED (it IS the P12 pool alt-academy-uploads.json,
75 uploads, already shipped). Slugs carry the alt-academy- family prefix."""
import json, os

WORK = "/home/z/my-project/work/p13recon"
RES = "/home/z/my-project/repos/syllabai-resources/Videos/inventory/channels"
UTC = "2026-11-14T14:55:00Z"  # enumeration run time (recon exec)

NAMES = {
    "alt-org-main": ("alt-academy-main", "Alt Academy (CAIE multi-subject hub: topic lectures + past-paper solutions)"),
    "alt-chemistry": ("alt-academy-chemistry", "A Level Chemistry | Alt Academy"),
    "alt-economics": ("alt-academy-economics", "A Level Economics | Alt Academy"),
    "alt-maths": ("alt-academy-maths", "A Level Maths | Alt Academy"),
    "alt-physics": ("alt-academy-physics", "A Level Physics | Alt Academy"),
    "alt-biology": ("alt-academy-biology", "A Level Biology | Alt Academy"),
    "alt-psychology": ("alt-academy-psychology", "A Level Psychology | Alt Academy"),
    "alt-accounting": ("alt-academy-accounting", "A Level Accounting | Alt Academy"),
}

s = json.load(open(os.path.join(WORK, "p13_summary.json")))
uc = {k: v["expected_uc"] for k, v in s.items()}

tot = 0
for slug, (out_slug, name) in NAMES.items():
    path = os.path.join(WORK, f"{slug}_raw.tsv")
    vids = []
    for line in open(path, encoding="utf-8").read().splitlines():
        if not line.strip():
            continue
        p = line.split("\t")
        # P13 recon TSV columns: id, duration, view_count, timestamp, channel_id, title
        vid, dur, views, ts, _cid, title = (p + [""] * 6)[:6]
        def num(x):
            x = (x or "").strip()
            if x and x != "NA":
                try:
                    return int(float(x))
                except ValueError:
                    return None
            return None
        vids.append({"id": vid, "title": title, "duration": num(dur),
                     "viewCount": num(views), "timestamp": None if (not ts or ts == "NA") else ts})
    out = {
        "channel": name,
        "channelId": uc[slug],
        "channelUrl": f"https://www.youtube.com/channel/{uc[slug]}/videos",
        "playlistTitle": f"{name} uploads",
        "count": len(vids),
        "enumeratedUtc": UTC,
        "videos": vids,
    }
    dst = os.path.join(RES, f"{out_slug}-uploads.json")
    json.dump(out, open(dst, "w"), indent=1, ensure_ascii=False)
    tot += len(vids)
    print(f"{slug} -> {out_slug}: {len(vids)}")
print("total inventoried:", tot)
