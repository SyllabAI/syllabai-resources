#!/usr/bin/env python3
"""P17 gap-profile lane: assemble inventories (P11-P15 shape) + overlap verification.

Reads work/p17/{resolve.json, <slug>_up.tsv}; writes work/p17/inventory/<slug>-uploads.json;
verifies 0 overlap of pool ids vs (a) the hub shipped union at hub main (all 96
course files incl. P15/P16), (b) all prior lane inventories on resources main,
(c) intra-P17. Pool set = the 21 post-classify pools of record in
Videos/scripts/p17/p17_pools.json (henry-brand + science-shorts dropped at the
register gate; Exam Essentials excluded-of-record; the P15-swept sentinel keeps
resurfaced pools disclosed).
"""
import json, os, glob, datetime

WORK = "/home/z/my-project/work/p17"
RES = "/home/z/my-project/repos/syllabai-resources"
HUB = "/tmp/hub-main-p17/apps/hub/content/video-map"
OUT = os.path.join(WORK, "inventory")
os.makedirs(OUT, exist_ok=True)

NOW = datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
pools = {p["slug"]: p for p in json.load(open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "p17_pools.json")))["pools"]}
resolve = {r["slug"]: r for r in json.load(open(os.path.join(WORK, "resolve.json"))) if r["status"] == "resolved"}


def parse_tsv(path):
    vids = []
    for l in open(path, encoding="utf-8"):
        parts = l.rstrip("\n").split("\t")
        if len(parts) >= 5:
            vid, dur, views, ts = parts[0], parts[1], parts[2], parts[3]
            title = "\t".join(parts[4:])
            vids.append({
                "id": vid,
                "title": title,
                "duration": int(dur) if dur.isdigit() else None,
                "viewCount": int(views) if views.isdigit() else None,
                "timestamp": None if ts in ("NA", "None", "") else ts,
            })
    return vids


pool_ids = {}
for slug, p in sorted(pools.items()):
    rec = resolve.get(slug)
    if not rec:
        print(f"[skip] {slug}: unresolved"); continue
    vids = parse_tsv(os.path.join(WORK, f"{slug}_up.tsv"))
    uc = rec["uc"]
    inv = {
        "channel": rec["title"],
        "channelId": uc,
        "channelUrl": f"https://www.youtube.com/channel/{uc}/videos",
        "playlistTitle": f"{rec['title']} uploads (uploads playlist)",
        "count": len(vids),
        "enumeratedUtc": NOW,
        "provenance": p.get("provenance", "new"),
        "videos": vids,
    }
    json.dump(inv, open(os.path.join(OUT, f"{slug}-uploads.json"), "w"), ensure_ascii=False, indent=1)
    pool_ids[slug] = {v["id"] for v in vids}
    print(f"[inv] {slug}: {len(vids)} uploads ({p['label']})")

# overlap law
hub_union = set()
for fp in glob.glob(HUB + "/*.json"):
    if fp.endswith("registry.json"):
        continue
    hub_union |= {v["id"] for v in json.load(open(fp)).get("videos", [])}
prior_union = set()
for fp in glob.glob(RES + "/Videos/inventory/channels/*-uploads.json"):
    d = json.load(open(fp))
    prior_union |= {v["id"] for v in d.get("videos", [])}
allp = set().union(*pool_ids.values()) if pool_ids else set()
dup_intra = len(allp) - sum(len(s) for s in pool_ids.values())
ov_hub = allp & hub_union
ov_prior = allp & prior_union
print(f"\npools: {len(pool_ids)}; uploads total {sum(len(s) for s in pool_ids.values())}; distinct {len(allp)} (intra-P17 shared ids: {dup_intra})")
print(f"hub shipped union (96 courses, main incl. P15+P16): {len(hub_union)}; overlap: {len(ov_hub)} {'PASS' if not ov_hub else 'FAIL ' + str(list(ov_hub)[:6])}")
print(f"prior lane inventories union: {len(prior_union)}; overlap: {len(ov_prior)} {'PASS' if not ov_prior else 'FAIL ' + str(list(ov_prior)[:6])}")
for s in sorted(pool_ids):
    oh, op = len(pool_ids[s] & hub_union), len(pool_ids[s] & prior_union)
    if oh or op:
        print(f"  !! {s}: hub {oh} / prior {op}")
json.dump({"poolIds": {k: len(v) for k, v in pool_ids.items()},
           "distinct": len(allp), "hubUnion": len(hub_union), "ovHub": len(ov_hub),
           "priorUnion": len(prior_union), "ovPrior": len(ov_prior), "intraShared": dup_intra,
           "enumeratedUtc": NOW},
          open(os.path.join(WORK, "filing_stats.json"), "w"), indent=1)
