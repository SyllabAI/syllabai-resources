#!/usr/bin/env python3
"""P11: build the 14 channel inventory JSONs (P9/P10 schema) from the recon TSVs.
enumeratedUtc = TSV mtime (the time the flat enumeration actually ran)."""
import json, os, datetime

WORK = "/home/z/my-project/work/p11"
OUT = "/home/z/my-project/repos/syllabai-resources/Videos/inventory/channels"

CHANNELS = [
    ("enhancetuition", "EnhanceTuition", "UC-JtWwjn16J5aqMfvmxkceg"),
    ("econplusdal", "EconplusDal", "UCQbBh9Jn2IjcSPZOiNKJu0g"),
    ("yimakesiteasy", "Yi MakesItEasy", "UCpH_SaN8pH5dkf1TVN4Ja8w"),
    ("cambridge-study-materials", "Cambridge IGCSE, AS and A Level Study Materials", "UCyZdlkz3Oc2I4hkPimjVi8Q"),
    ("james-gan", "James Gan", "UCzH8c5HRgdxNdC8igHtXCtg"),
    ("igcse-online", "IGCSE Online", "UCQsOJB-oUEX_Q3Ie6xGBKKg"),
    ("igcse-computer-science", "IGCSE Computer Science", "UC-2VV9ZMEN-h6L6MlNiwfcw"),
    ("purple-shirt-history", "Purple Shirt History", "UCiEKSuhYV8qUb3wup6eKziQ"),
    ("mindful-maths", "Mindful Maths", "UC1QKwZGLOriJQRhngH4919A"),
    ("cambridge-accounting", "Cambridge Accounting IGCSE and A Level", "UCyXQ7oORWXppb0NBPAtpQ5A"),
    ("ar-accounting", "AR Accounting", "UCMUXpRwc-dKaNkKs8ip555A"),
    ("evm-dr-mohamed-saber", "EVM WITH DR MOHAMED SABER", "UCR6nfQLaG5iMSb5idA7tDRw"),
    ("mr-salles", "Mr Salles Teaches English", "UCEB4IwW-eVk9SxHBIGhrY3w"),
    ("the-igcse-geographer", "The iGCSE Geographer", "UCkIQLDXJlNlh3n-B_ilOYwQ"),
]

def num(x):
    if x in ("NA", "", None):
        return None
    try:
        return int(float(x))
    except ValueError:
        return None

for slug, name, uc in CHANNELS:
    ts = os.path.getmtime(f"{WORK}/{slug}_raw.tsv")
    enum_utc = datetime.datetime.fromtimestamp(ts, datetime.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
    vids = []
    seen = set()
    for line in open(f"{WORK}/{slug}_raw.tsv", encoding="utf-8"):
        p = line.rstrip("\n").split("\t")
        if len(p) < 5 or not p[0] or p[0] in seen:
            continue
        seen.add(p[0])
        vids.append({"id": p[0], "title": p[1], "duration": num(p[2]),
                     "viewCount": num(p[3]), "timestamp": None if p[4] == "NA" else p[4]})
    inv = {
        "channel": name,
        "channelId": uc,
        "channelUrl": f"https://www.youtube.com/channel/{uc}/videos",
        "playlistTitle": f"{name} uploads",
        "count": len(vids),
        "enumeratedUtc": enum_utc,
        "videos": vids,
    }
    path = f"{OUT}/{slug}-uploads.json"
    json.dump(inv, open(path, "w"), ensure_ascii=False, indent=1)
    print(f"{slug}: {len(vids)} videos @ {enum_utc}")
print("done")
