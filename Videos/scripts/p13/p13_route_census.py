#!/usr/bin/env python3
"""P13 route census: bucket the 8-pool Alt Academy family (985 uploads) into subject
clusters. Buckets are keyword-based (syllabus codes + register phrases); per-channel
out-of-cluster counts become the census skip ledger. Writes work/p13 inl-*.json extracts
+ curriculum snapshots + p13_route_census.json.

Clusters (code, register phrases, spine targets — P13 pre-inherit / P13B post-inherit):
  chem9701  9701 | AS/A Level Chemistry, | Ch  -> al-chemistry-25 [P13] + as-chemistry-25 [P13B]
  econ9708  9708 | Economics/Economic          -> a-level-economics-23
  maths9709 9709 | A Level Maths/Math           -> 10 maths unit courses
  phys9702  9702 | AS/A Level Physics, | Ph     -> a-level-physics-25 [P13] + as-physics-25 [P13B]
  bio9700   9700 | AS/A Level Biology         -> a-level-biology-25 [P13] + as-biology-25 [P13B]
  acct9706  9706 | Accounting                   -> a-level-accounting-21 + as-accounting-21
  biz9609   9609 | Business (main channel only; subject channel = P12 pool, not re-inventoried)
  psych9990 9990 | Psycholog                    -> NO SPINE COURSE (honest no-target)
  olevel    O Level register                  -> out of lane scope (no O-level courses in spine)
"""
import json, os, re

WORK = "/home/z/my-project/work/p13"
HUB = "/home/z/my-project/repos/syllabai-v2-fresh/apps/hub/content"
os.makedirs(WORK, exist_ok=True)

CHANNELS = {
    "alt-academy-main": "chem-any",
    "alt-academy-chemistry": "chem9701",
    "alt-academy-economics": "econ9708",
    "alt-academy-maths": "maths9709",
    "alt-academy-physics": "phys9702",
    "alt-academy-biology": "bio9700",
    "alt-academy-psychology": "psych9990",
    "alt-academy-accounting": "acct9706",
}

RE_CODE = {
    "chem9701": re.compile(r"\b9701\b"),
    "econ9708": re.compile(r"\b9708\b"),
    "maths9709": re.compile(r"\b9709\b"),
    "phys9702": re.compile(r"\b9702\b"),
    "bio9700": re.compile(r"\b9700\b"),
    "acct9706": re.compile(r"\b9706\b"),
    "biz9609": re.compile(r"\b9609\b"),
    "psych9990": re.compile(r"\b9990\b"),
}
RE_REG = {
    "chem9701": re.compile(r"(AS\s+Level|A\s?Level)\s*\|?\s*Chemistry|Chemistry\s+9701|AS\s+Level\s+Chemistry", re.I),
    "econ9708": re.compile(r"(AS\s+Level|A\s?Level)\s*\|?\s*Econom", re.I),
    "maths9709": re.compile(r"(AS\s+Level|A\s?Level)\s*\|?\s*Math", re.I),
    "phys9702": re.compile(r"(AS\s+Level|A\s?Level)\s*\|?\s*Physics", re.I),
    "bio9700": re.compile(r"(AS\s+Level|A\s?Level)\s*\|?\s*Biology", re.I),
    "acct9706": re.compile(r"(AS\s+Level|A\s?Level)\s*\|?\s*Accounting|Accounting\s+9706", re.I),
    "biz9609": re.compile(r"(AS\s+Level|A\s?Level)\s*\|?\s*Business|Business\s+9609", re.I),
    "psych9990": re.compile(r"(AS\s+Level|A\s?Level)\s*\|?\s*Psycholog", re.I),
}
RE_OLEVEL = re.compile(r"\bO\s?-?Level\b", re.I)
RE_LEVEL = re.compile(r"\bA\s?LE?vel\b|\bAS\b|\bA2\b", re.I)
RE_SUBJ = {
    "chem9701": re.compile(r"\bchem(istry|\b)", re.I),
    "econ9708": re.compile(r"\beconom", re.I),
    "maths9709": re.compile(r"\bmath", re.I),
    "phys9702": re.compile(r"\bphysic", re.I),
    "bio9700": re.compile(r"\bbiology\b", re.I),
    "acct9706": re.compile(r"\baccount", re.I),
    "biz9609": re.compile(r"\bbusi?n[ae]ss|\bbusiness", re.I),
    "psych9990": re.compile(r"\bpsycholog", re.I),
}

def buckets(title):
    t = title
    out = set()
    if RE_OLEVEL.search(t):
        out.add("olevel")
        return out
    for code, rx in RE_CODE.items():
        if rx.search(t):
            out.add(code)
    lev = bool(RE_LEVEL.search(t))
    subj = [c for c, rx in RE_SUBJ.items() if rx.search(t)]
    if lev and subj:
        out.update(subj)
    elif lev:
        out.add("terse")
    return out

TARGETS = {
    "chem9701": ["cie-a-level-chemistry-25", "cie-as-chemistry-25"],
    "econ9708": ["cie-a-level-economics-23"],
    "maths9709": ["cie-a-level-maths-20-mechanics", "cie-as-maths-20-mechanics",
                  "cie-a-level-maths-20-probability-and-statistics-1", "cie-as-maths-20-probability-and-statistics-1",
                  "cie-a-level-maths-20-probability-and-statistics-2",
                  "cie-a-level-maths-20-pure-1", "cie-as-maths-20-pure-1",
                  "cie-a-level-maths-20-pure-2", "cie-as-maths-20-pure-2",
                  "cie-a-level-maths-20-pure-3"],
    "phys9702": ["cie-a-level-physics-25", "cie-as-physics-25"],
    "bio9700": ["cie-a-level-biology-25", "cie-as-biology-25"],
    "acct9706": ["cie-a-level-accounting-21", "cie-as-accounting-21"],
    "biz9609": ["cie-a-level-business-23", "cie-as-business-23"],
    "psych9990": [],
}

def main():
    census = {}
    for slug, home in CHANNELS.items():
        raw = slug.replace("alt-academy", "alt")
        if raw == "alt-main":
            raw = "alt-org-main"
        rows = [l.split("\t") for l in open(f"/home/z/my-project/work/p13recon/{raw}_raw.tsv", encoding="utf-8").read().splitlines() if l]
        inl, out = [], []
        for p in rows:
            vid, title = p[0], p[5]
            bs = buckets(title)
            bs.discard("olevel")
            if bs:
                inl.append({"id": vid, "title": title, "buckets": sorted(bs)})
            else:
                out.append({"id": vid, "title": title[:90]})
        census[slug] = {"home": home, "total": len(rows), "in_cluster": len(inl), "out": len(out)}
        json.dump(inl, open(os.path.join(WORK, f"inl-{slug}.json"), "w"), indent=1, ensure_ascii=False)
    for courses in TARGETS.values():
        for c in courses:
            cur = json.load(open(os.path.join(HUB, c, "curriculum.json")))
            json.dump(cur, open(os.path.join(WORK, f"curriculum-{c}.json"), "w"), indent=1)
    total_in = sum(v["in_cluster"] for v in census.values())
    total_all = sum(v["total"] for v in census.values())
    census["_totals"] = {"pool": total_all, "in_cluster": total_in, "census_skips": total_all - total_in}
    json.dump(census, open(os.path.join(WORK, "p13_route_census.json"), "w"), indent=1)
    print(json.dumps(census, indent=1))

if __name__ == "__main__":
    main()
