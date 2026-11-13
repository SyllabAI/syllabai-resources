#!/usr/bin/env python3
"""P11 recon census: route 14 candidate pools against the 38 uncovered courses'
subject clusters, with overlap check vs the shipped union (hub video-map rows +
resources channel inventories). Coarse keyword buckets — recon only, not lane
judgment.
"""
import glob, json, os, re, unicodedata

P11 = "/home/z/my-project/work/p11"
HUB = "/home/z/my-project/repos/syllabai-v2-fresh/apps/hub/content"
RES = "/home/z/my-project/repos/syllabai-resources/Videos/inventory/channels"

CH_ORDER = ["enhancetuition","econplusdal","yimakesiteasy","cambridge-study-materials",
            "james-gan","igcse-online","igcse-computer-science","purple-shirt-history",
            "mindful-maths","cambridge-accounting","ar-accounting",
            "evm-dr-mohamed-saber","mr-salles","the-igcse-geographer"]

BUCKETS = {
    "econ":       [r"9708", r"9707", r"economi"],
    "business":   [r"\b0450\b", r"\b9609\b", r"business", r"enterprise"],
    "accounting": [r"\b0452\b", r"\b9706\b", r"account", r"ledger", r"balance sheet",
                   r"depreciation", r"trial balance"],
    "cs":         [r"\b0478\b", r"\b9618\b", r"2210", r"computer science",
                   r"pseudocode", r"binary search", r"flowchart"],
    "ict":        [r"\b0417\b", r"\bICT\b", r"spreadsheet", r"database"],
    "english":    [r"4EA1", r"4ET1", r"\benglish\b", r"Macbeth", r"Jekyll", r"poetry",
                   r"Inspector", r"language paper", r"imaginative writing"],
    "geography":  [r"\b0460\b", r"\b9696\b", r"geograph", r"population",
                   r"rivers", r"tectonic"],
    "history":    [r"\b0470\b", r"history", r"Versailles", r"League of Nations",
                   r"depth study", r"cold war"],
    "em":         [r"\b0680\b", r"environmental"],
    "rs":         [r"religious"],
    "d1":         [r"\bD1\b", r"\bdecision\b", r"simplex", r"critical path",
                   r"bin[- ]?packing", r"sorting", r"algorithm", r"Kruskal",
                   r"Prim", r"route inspection", r"linear programming"],
}

def shipped_union():
    ids = set()
    for f in glob.glob(f"{HUB}/video-map/*.json"):
        txt = open(f, encoding="utf-8", errors="ignore").read()
        for m in re.finditer(r'"(?:externalId|videoId|youtubeId|id)"\s*:\s*"([A-Za-z0-9_-]{11})"', txt):
            ids.add(m.group(1))
    inv_ids = set()
    for f in glob.glob(f"{RES}/*-uploads.json"):
        try:
            d = json.load(open(f, encoding="utf-8"))
            for v in d.get("videos", []):
                vid = v.get("id")
                if vid and re.fullmatch(r"[A-Za-z0-9_-]{11}", vid):
                    inv_ids.add(vid)
        except Exception:
            pass
    return ids, inv_ids

def bucket_for(title):
    t = title.lower()
    hits = []
    for b, pats in BUCKETS.items():
        for p in pats:
            if re.search(p, t, re.I if p.lower() == p else 0):
                hits.append(b); break
    return hits

def main():
    hub_ids, inv_ids = shipped_union()
    union = hub_ids | inv_ids
    print(f"shipped union: hub video-map ids={len(hub_ids)}  inventory ids={len(inv_ids)}  union={len(union)}")

    per = {}
    cluster_tot = {}
    overlap_rows = []
    for slug in CH_ORDER:
        f = f"{P11}/{slug}_raw.tsv"
        rows = []
        with open(f, encoding="utf-8") as fh:
            for line in fh:
                parts = line.rstrip("\n").split("\t")
                if len(parts) >= 2:
                    rows.append((parts[0], parts[1]))
        counts = {b: 0 for b in BUCKETS}
        no_target = 0
        ov = 0
        for vid, title in rows:
            hits = bucket_for(title)
            if hits:
                for b in set(hits):
                    counts[b] += 1
            else:
                no_target += 1
            if vid in union:
                ov += 1
                overlap_rows.append((slug, vid, title[:60]))
        per[slug] = {"n": len(rows), "buckets": counts, "noTarget": no_target, "overlap": ov}
        for b, c in counts.items():
            if c: cluster_tot[b] = cluster_tot.get(b, 0) + c

    hdr = f"{'channel':26s} {'n':>5s} " + " ".join(f"{b[:6]:>7s}" for b in BUCKETS) + "  noTgt  ovl"
    print("\n" + hdr)
    for slug in CH_ORDER:
        d = per[slug]
        print(f"{slug:26s} {d['n']:5d} " + " ".join(f"{d['buckets'][b]:7d}" for b in BUCKETS)
              + f"  {d['noTarget']:5d}  {d['overlap']:3d}")
    print("\ncluster totals:", {k: v for k, v in sorted(cluster_tot.items(), key=lambda x: -x[1])})
    print("total overlap vs shipped union:", len(overlap_rows))
    if overlap_rows:
        for s, v, t in overlap_rows[:15]:
            print(f"  OVL {s} {v} {t}")
    json.dump({"shippedUnion": len(union), "per": per, "clusterTotals": cluster_tot,
               "overlap": overlap_rows},
              open(f"{P11}/p11_route_census.json", "w"), indent=2)

if __name__ == "__main__":
    main()
