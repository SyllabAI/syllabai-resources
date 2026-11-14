#!/usr/bin/env python3
"""P12 route census: bucket 11-channel pool against the five uncovered CIE targets.
Buckets are keyword-based (syllabus codes + register phrases); per-channel out-of-scope
counts become the honest-skip ledger. Reads work/p12 TSVs + hub curriculum targets.
"""
import json, os, re, glob

WORK = "/home/z/my-project/work/p12"
HUB = "/home/z/my-project/repos/syllabai-v2-fresh/apps/hub/content"

TARGETS = {
    "business9609": ["cie-as-business-23", "cie-a-level-business-23"],
    "geo9696": ["cie-a-level-geography-21"],
    "em8291": ["cie-as-environmental-management-20"],
    "gp8021": ["cie-as-english-general-paper-21"],
}
CHANNEL_CLUSTER = {
    "cambridge-business-essentials": "business9609",
    "bizedmadesimple": "business9609",
    "alt-academy": "business9609",
    "the-teaching-student": "business9609",
    "the-geography-academy": "geo9696",
    "virtual-pathways": "em8291",
    "polymath-institute": "em8291",
    "mini-lessons-gp": "gp8021",
    "english-with-ms-irum": "gp8021",
    "ace-the-exam": "gp8021",
    "miss-cutu": "gp8021",
}

RE_9609 = re.compile(r"\b9609\b", re.I)
RE_BUSINESS_CIE = re.compile(r"(as|a[- ]?level|a2|igcse|o[- ]?level)\s+(level\s+)?business|business\s+(9609|studies)", re.I)
RE_9696 = re.compile(r"\b9696\b", re.I)
RE_GEO = re.compile(r"geograph", re.I)
RE_8291 = re.compile(r"\b8291\b", re.I)
RE_EM = re.compile(r"environmental\s+management", re.I)
RE_8021 = re.compile(r"\b8021\b", re.I)
RE_GP = re.compile(r"general\s+paper", re.I)

def buckets(title):
    t = title
    out = set()
    if RE_9609.search(t) or RE_BUSINESS_CIE.search(t):
        out.add("business9609")
    if RE_9696.search(t) or (RE_GEO.search(t) and re.search(r"cambridge|caie|\ba[- ]?level|as\s", t, re.I)):
        out.add("geo9696")
    if RE_8291.search(t) or (RE_EM.search(t) and re.search(r"\bas\b|cambridge|caie|8291", t, re.I)):
        out.add("em8291")
    if RE_8021.search(t) or RE_GP.search(t):
        out.add("gp8021")
    return out

def main():
    s = json.load(open(os.path.join(WORK, "p12_summary.json")))
    census = {}
    for x in s:
        slug = x["slug"]
        rows = [l.split("\t") for l in open(os.path.join(WORK, f"{slug}_raw.tsv")).read().splitlines() if l]
        inl, out = [], []
        for p in rows:
            vid, title = p[0], p[1]
            bs = buckets(title)
            home = CHANNEL_CLUSTER[slug]
            if home in bs:
                inl.append({"id": vid, "title": title, "buckets": sorted(bs)})
            else:
                out.append({"id": vid, "title": title[:90]})
        census[slug] = {"cluster": home, "total": len(rows), "in_cluster": len(inl), "out": len(out)}
        json.dump(inl, open(os.path.join(WORK, f"inl-{slug}.json"), "w"), indent=1)
    # target course unit snapshots for the judgment pass
    for courses in TARGETS.values():
        for c in courses:
            cur = json.load(open(os.path.join(HUB, c, "curriculum.json")))
            json.dump(cur, open(os.path.join(WORK, f"curriculum-{c}.json"), "w"), indent=1)
    total_in = sum(v["in_cluster"] for v in census.values())
    total_all = sum(v["total"] for v in census.values())
    census["_totals"] = {"pool": total_all, "in_cluster": total_in, "skips": total_all - total_in}
    json.dump(census, open(os.path.join(WORK, "p12_route_census.json"), "w"), indent=1)
    print(json.dumps(census, indent=1))

if __name__ == "__main__":
    main()
