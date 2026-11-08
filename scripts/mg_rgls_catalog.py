#!/usr/bin/env python3
"""mg_rgls_catalog.py — build the RG/FC/LS catalog of record for the three
maths lanes from the site sitemap (mode URLs per topic), cross-checked with
the GCSE mirror catalog, and save it to logs/rgls_catalog.json."""
import json
import sys

sys.path.insert(0, "/home/z/my-project/scripts/mg_rgls_work")
import mg_common as C  # noqa: E402

cat = {}
for lane, lane_dir in C.LANES.items():
    mu = C.lane_mode_urls(lane_dir)
    topics = {}
    for mode in C.MODES:
        for slug in mu[mode]:
            topics.setdefault(slug, {"title": None, "modes": set()})
            topics[slug]["modes"].add(mode)
    entry = {
        "lane": lane,
        "lane_dir": lane_dir,
        "topic_count": len(topics),
        "mode_counts": {m: len(mu[m]) for m in C.MODES},
        "topics": {s: {"modes": sorted(v["modes"])} for s, v in sorted(topics.items())},
    }
    if lane == "gcse-maths-edexcel":
        gc = C.gcse_catalog()
        entry["catalog_source"] = "SyllabAI/MathsGenie data/gcse-maths/topics-edexcel.json"
        missing_from_catalog = sorted(set(topics) - set(gc))
        extra_in_catalog = sorted(set(gc) - set(topics))
        entry["catalog_crosscheck"] = {
            "catalog_topics": len(gc),
            "sitemap_topics": len(topics),
            "in_catalog_no_sitemap_page": extra_in_catalog,
            "in_sitemap_not_in_catalog": missing_from_catalog,
        }
        for s in topics:
            if s in gc:
                entry["topics"][s]["title"] = gc[s]["title"]
                entry["topics"][s]["grade"] = gc[s]["grade"]
    cat[lane] = entry
    print(lane, "topics:", entry["topic_count"], "modes:", entry["mode_counts"])

out = f"{C.LOGS}/rgls_catalog.json"
json.dump(cat, open(out, "w"), indent=1)
print("saved", out)
