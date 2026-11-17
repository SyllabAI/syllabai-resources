#!/usr/bin/env python3
"""P14 filing step: assemble the per-pool inventory JSONs (P11-P13 shape).

Reads work/p14/<slug>_up.tsv (uploads-playlist enumeration) + resolve.json and
writes Videos/inventory/channels/<slug>-uploads.json:
  {channel, channelId, channelUrl, playlistTitle, count, enumeratedUtc,
   videos: [{id, title, duration, viewCount, timestamp}]}
Also writes scripts/p14/p14_readjudication.json (the two re-adjudication
candidate tables + evidence) from analysis.json.
"""
import json, os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from datetime import datetime, timezone

HERE = os.path.dirname(os.path.abspath(__file__))
WORK = "/home/z/my-project/work/p14"
RES = "/home/z/my-project/repos/syllabai-resources"
NOW = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")

def parse_int(s):
    if s is None or s in ("NA", "None", "", "nan"):
        return None
    try:
        return int(float(s))
    except ValueError:
        return None

def main():
    resolve = {r["slug"]: r for r in json.load(open(os.path.join(WORK, "resolve.json"))) if r["status"] == "resolved"}
    written = []
    for slug, rec in resolve.items():
        tsv = os.path.join(WORK, f"{slug}_up.tsv")
        videos = []
        with open(tsv, encoding="utf-8") as f:
            for l in f:
                parts = l.rstrip("\n").split("\t")
                if len(parts) >= 5 and parts[0]:
                    videos.append({"id": parts[0], "title": parts[4],
                                   "duration": parse_int(parts[1]),
                                   "viewCount": parse_int(parts[2]),
                                   "timestamp": None})
        out = {"channel": rec["title"], "channelId": rec["uc"],
               "channelUrl": f"https://www.youtube.com/channel/{rec['uc']}/videos",
               "playlistTitle": f"{rec['title']} uploads (uploads playlist)",
               "count": len(videos), "enumeratedUtc": NOW, "videos": videos}
        path = os.path.join(RES, "Videos/inventory/channels", f"{slug}-uploads.json")
        json.dump(out, open(path, "w"), indent=1, ensure_ascii=False)
        written.append((slug, len(videos), os.path.getsize(path)))
        print(f"[inv] {slug}: {len(videos)} videos -> {os.path.basename(path)} ({os.path.getsize(path)//1024} KiB)")
    # re-adjudication artifact
    a = json.load(open(os.path.join(WORK, "analysis.json")))
    ra = {"generatedUtc": NOW,
          "econplusdal-cie": {k: v for k, v in a["readjudication"]["econplusdal-cie"].items()},
          "allery-chemistry-cie": {k: v for k, v in a["readjudication"]["allery-chemistry-cie"].items()}}
    json.dump(ra, open(os.path.join(HERE, "p14_readjudication.json"), "w"), indent=1, ensure_ascii=False)
    print(f"[ra] econplusdal candidates {len(ra['econplusdal-cie']['cieCandidates'])} "
          f"(ib {ra['econplusdal-cie']['ibTitleCount']}, fresh {ra['econplusdal-cie']['freshVideosTabCount']}); "
          f"allery candidates {len(ra['allery-chemistry-cie']['cieCandidates'])} "
          f"(wide {ra['allery-chemistry-cie']['wideCieCount']})")
    print(f"TOTAL {sum(c for _, c, _ in written)} videos across {len(written)} inventories")

if __name__ == "__main__":
    main()
