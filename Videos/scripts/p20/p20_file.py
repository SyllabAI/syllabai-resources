#!/usr/bin/env python3
"""P20 filing: build inventories x35 (filed pools only) + the overlap law + filing_stats.

The 21 register-gate drops are NOT inventoried — they are documented in
register_gate.json (re-sweepable next lane, nothing silently dropped: the drop
is register-level, not overlap-level).
"""
import json, os, glob

WORK = "/home/z/my-project/work/p20"
RES = "/home/z/my-project/repos/syllabai-resources"
HERE = os.path.join(RES, "Videos", "scripts", "p20")
OUT = os.path.join(RES, "Videos", "inventory", "channels")
HUB = "/tmp/hub-main-p20/apps/hub/content/video-map"
NOW = "2026-11-26T08:45:00Z"

pools_all = json.load(open(os.path.join(HERE, "p20_pools.json")))["pools"]
gate = json.load(open(os.path.join(HERE, "register_gate.json")))
filed_slugs = gate["filed"]
pools = {p["slug"]: p for p in pools_all if p["slug"] in filed_slugs}
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
    print(f"[inv] {slug}: {len(vids)} uploads")

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
# exclude the files this script just wrote (they are IN the inventory dir now)
for slug in pool_ids:
    fp = os.path.join(OUT, f"{slug}-uploads.json")
    d = json.load(open(fp))
    prior_union -= {v["id"] for v in d.get("videos", [])}
allp = set().union(*pool_ids.values()) if pool_ids else set()
dup_intra = sum(len(s) for s in pool_ids.values()) - len(allp)
ov_hub = allp & hub_union
ov_prior = allp & prior_union
print(f"\npools: {len(pool_ids)}; uploads total {sum(len(s) for s in pool_ids.values())}; distinct {len(allp)} (intra-P20 shared ids: {dup_intra})")
print(f"hub shipped union (96 courses, main 1389bf21 incl. P19): {len(hub_union)}; overlap: {len(ov_hub)} {'PASS' if not ov_hub else 'FAIL ' + str(list(ov_hub)[:6])}")
print(f"prior lane inventories union (incl. P14..P19): {len(prior_union)}; overlap: {len(ov_prior)} {'PASS' if not ov_prior else 'FAIL ' + str(list(ov_prior)[:6])}")
for s in sorted(pool_ids):
    oh, op = len(pool_ids[s] & hub_union), len(pool_ids[s] & prior_union)
    if oh or op:
        print(f"  !! {s}: hub {oh} / prior {op}")
json.dump({"poolIds": {k: len(v) for k, v in pool_ids.items()},
           "distinct": len(allp), "hubUnion": len(hub_union), "ovHub": len(ov_hub),
           "priorUnion": len(prior_union), "ovPrior": len(ov_prior), "intraShared": dup_intra,
           "enumeratedUtc": NOW},
          open(os.path.join(HERE, "filing_stats.json"), "w"), indent=1)
open(os.path.join(HERE, "filing_stats.json"), "a").write("\n")
print("wrote filing_stats.json")
