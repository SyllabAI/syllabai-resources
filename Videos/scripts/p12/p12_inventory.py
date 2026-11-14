#!/usr/bin/env python3
"""P12: convert 11 raw TSVs -> P9-schema channel inventory JSONs in resources repo."""
import json, os

WORK = "/home/z/my-project/work/p12"
RES = "/home/z/my-project/repos/syllabai-resources/Videos/inventory/channels"
UTC = "2026-11-13T14:05:00Z"  # enumeration run time (approx of recon exec)

NAMES = {
    "cambridge-business-essentials": "Cambridge Business Essentials A-level & IGCSE",
    "bizedmadesimple": "BizEdMadeSimple",
    "alt-academy": "A Level Business | Alt Academy",
    "the-teaching-student": "The Teaching Student",
    "the-geography-academy": "The Geography Academy",
    "virtual-pathways": "Virtual Pathways",
    "polymath-institute": "Polymath Institute",
    "mini-lessons-gp": "Mini Lessons",
    "english-with-ms-irum": "English with Ms Irum",
    "ace-the-exam": "Ace The Exam Cambridge IGCSE O & A Levels",
    "miss-cutu": "Miss Cutu Bilingual Help",
}

s = json.load(open(os.path.join(WORK, "p12_summary.json")))
uc = {x["slug"]: x["uc"] for x in s}

for slug, name in NAMES.items():
    path = os.path.join(WORK, f"{slug}_raw.tsv")
    vids = []
    for line in open(path).read().splitlines():
        if not line.strip():
            continue
        p = line.split("\t")
        vid, title, dur, views, ts = (p + [""] * 5)[:5]
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
    dst = os.path.join(RES, f"{slug}-uploads.json")
    json.dump(out, open(dst, "w"), indent=1, ensure_ascii=False)
    print(f"{slug}: {len(vids)} -> {dst}")
print("done")
