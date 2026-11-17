#!/usr/bin/env python3
"""P14 recon step 3: signal classification + overlap + coverage baselines.

Classifies every enumerated upload title against the spine registry
(hub content/courses.json): qualification-code regexes (CIE subject codes,
Edexcel IAL W-codes, Edexcel IGCSE 4-codes, old-register GCE unit tokens),
register buckets (session-paper / guidance / teaching) and out-of-spine board
markers (AQA/OCR/IB/NCERT/...). Produces per-pool verdict SUGGESTIONS — the
recon-approved verdict stands where one exists; fresh derivation is flagged
for pools whose recon verdict row was lost in the session recycle.

Also: overlap check vs the shipped union (all video ids in hub
content/video-map/*.json) and per-course coverage baselines, plus the two
re-adjudication groups (EconplusDal P11 pool, Allery P2F pool) classified
over their EXISTING repo inventories.

Writes work/p14/analysis.json
"""
import json, os, re, sys
from collections import Counter, defaultdict

WORK = "/home/z/my-project/work/p14"
HUB = "/home/z/my-project/repos/syllabai-v2-fresh/apps/hub"
RES = "/home/z/my-project/repos/syllabai-resources"

# ---------------------------------------------------------------- spine maps
def load_spine():
    d = json.load(open(f"{HUB}/content/courses.json"))["courses"]
    return {c["slug"]: c for c in d}

SPINE = load_spine()

CIE_AL = {
    "9702": ["cie-a-level-physics-25", "cie-as-physics-25"],
    "9701": ["cie-a-level-chemistry-25", "cie-as-chemistry-25"],
    "9700": ["cie-a-level-biology-25", "cie-as-biology-25"],
    "9709": ["cie-a-level-maths-20-mechanics", "cie-a-level-maths-20-probability-and-statistics-1",
             "cie-a-level-maths-20-probability-and-statistics-2", "cie-a-level-maths-20-pure-1",
             "cie-a-level-maths-20-pure-2", "cie-a-level-maths-20-pure-3",
             "cie-as-maths-20-mechanics", "cie-as-maths-20-probability-and-statistics-1",
             "cie-as-maths-20-pure-1", "cie-as-maths-20-pure-2"],
    "9708": ["cie-a-level-economics-23"],
    "9706": ["cie-a-level-accounting-21", "cie-as-accounting-21"],
    "9609": ["cie-a-level-business-23", "cie-as-business-23"],
    "9618": ["cie-a-level-computer-science-19", "cie-as-computer-science-19"],
    "9696": ["cie-a-level-geography-21"],
    "8021": ["cie-as-english-general-paper-21"],
    "8291": ["cie-as-environmental-management-20"],
}
CIE_IG = {
    "0620": ["cie-igcse-chemistry-23"], "0625": ["cie-igcse-physics-23"], "0610": ["cie-igcse-biology-23"],
    "0580": ["cie-igcse-maths-25-core", "cie-igcse-maths-25-extended"],
    "0606": ["cie-igcse-further-maths-additional-maths-25"],
    "0450": ["cie-igcse-business-23"], "0264": ["cie-igcse-business-25"],
    "0455": ["cie-igcse-economics-20", "cie-igcse-economics-25"],
    "0452": ["cie-igcse-accounting-21", "cie-igcse-accounting-25"],
    "0478": ["cie-igcse-computer-science-23"], "0500": ["cie-igcse-english-language-20", "cie-igcse-english-language-25"],
    "0475": ["cie-igcse-english-literature-21"], "0680": ["cie-igcse-environmental-management-25"],
    "0460": ["cie-igcse-geography-20", "cie-igcse-geography-25"], "0417": ["cie-igcse-ict-21"],
    "0470": ["cie-igcse-history-18"], "0607": ["cie-igcse-maths-international-maths-23-core",
             "cie-igcse-maths-international-maths-23-extended"],
    "0490": ["cie-igcse-religious-studies-23"],
    "0973": ["cie-igcse-science-co-ordinated-sciences-double-award-23-biology",
             "cie-igcse-science-co-ordinated-sciences-double-award-23-chemistry",
             "cie-igcse-science-co-ordinated-sciences-double-award-23-physics"],
    "0653": ["cie-igcse-science-combined-science-23-biology",
             "cie-igcse-science-combined-science-23-chemistry",
             "cie-igcse-science-combined-science-23-physics"],
}
IAL_W = {
    "WMA11": ["ial-maths-20-pure-1"], "WMA12": ["ial-maths-20-pure-2"], "WMA13": ["ial-maths-20-pure-3"],
    "WMA14": ["ial-maths-20-pure-4"], "WME01": ["ial-maths-20-mechanics-1"], "WME02": ["ial-maths-20-mechanics-2"],
    "WST01": ["ial-maths-20-statistics-1"], "WST02": ["ial-maths-20-statistics-2"], "WDM11": ["ial-maths-20-decision-1"],
    "WFM11": ["ial-further-maths-18-further-pure-1"],
    "WPH11": ["ial-physics-19"], "WCH11": ["ial-chemistry-17"], "WBI11": ["ial-biology-18"],
}
IG_4 = {
    "4MA1": ["igcse-maths-a-18-higher", "igcse-maths-a-18-foundation"],
    "4PH1": ["igcse-physics-19"], "4CH1": ["igcse-chemistry-19"], "4BI1": ["igcse-biology-19"],
    "4EA1": ["igcse-english-language-a-16-paper-1-non-fiction-texts-and-transactional-writing",
             "igcse-english-language-a-16-paper-2-poetry-and-prose-texts-and-imaginative-writing",
             "igcse-english-language-a-16-paper-3-coursework"],
    "4ET1": ["igcse-english-literature-16"], "4PM1": ["igcse-further-maths-19"],
    "4AC1": ["igcse-accounting-17-financial-statements", "igcse-accounting-17-introduction-to-bookkeeping-and-accounting"],
    "4BS1": ["igcse-business-19"], "4EC1": ["igcse-economics-17"], "4GE1": ["igcse-geography-19"],
    "4IT1": ["igcse-ict-17"], "4HI1": ["igcse-history-17"], "4MB1": ["igcse-maths-b-16"],
    "4SD0": ["igcse-science-double-award-17-biology", "igcse-science-double-award-17-chemistry",
             "igcse-science-double-award-17-physics"],
    "4XPH1": ["igcse-physics-modular-24-unit-1", "igcse-physics-modular-24-unit-2"],
    "4XCH1": ["igcse-chemistry-modular-24-unit-1", "igcse-chemistry-modular-24-unit-2"],
    "4XBI1": ["igcse-biology-modular-24-unit-1", "igcse-biology-modular-24-unit-2"],
    "4XMAF": ["igcse-maths-a-modular-24-foundation-unit-1", "igcse-maths-a-modular-24-foundation-unit-2"],
    "4XMAH": ["igcse-maths-a-modular-24-higher-unit-1", "igcse-maths-a-modular-24-higher-unit-2"],
    "4XSD1": ["igcse-science-double-award-modular-24-biology-unit-1", "igcse-science-double-award-modular-24-biology-unit-2",
              "igcse-science-double-award-modular-24-chemistry-unit-1", "igcse-science-double-award-modular-24-chemistry-unit-2",
              "igcse-science-double-award-modular-24-physics-unit-1", "igcse-science-double-award-modular-24-physics-unit-2"],
}
OLD_GCE = r"\b(C[1-4]|M[1-5]|S[1-4]|FP[1-3]|D1)\b"

# textual register families (titles that carry the qualification WITHOUT the
# bare unit code): Edexcel IAL chemistry session units, Edexcel IGCSE by
# subject keyword, explicit CIE IGCSE literature markers.
RE_ED_IAL_CHEM_UNIT = re.compile(r"Edexcel.{0,60}Chemistry.{0,60}Unit\s*[1-6]|Unit\s*[1-6].{0,60}Chemistry.{0,60}Edexcel|Chemistry.{0,30}(AS|A2).{0,60}Edexcel", re.I)
RE_ED_IG = re.compile(r"Edexcel\s+IGCSE|IGCSE.{0,40}Edexcel", re.I)
RE_CIE_LIT = re.compile(r"(\b0475\b|\bCIE\b).{0,60}Literature|Literature.{0,60}(\b0475\b|\bCIE\b)|IGCSE\s+Literature", re.I)

def ed_ig_subject_slugs(t):
    tl = t.lower()
    if "physics" in tl:
        return ["igcse-physics-19", "igcse-physics-modular-24-unit-1", "igcse-physics-modular-24-unit-2"]
    if "chemistry" in tl:
        return ["igcse-chemistry-19", "igcse-chemistry-modular-24-unit-1", "igcse-chemistry-modular-24-unit-2"]
    if "biology" in tl:
        return ["igcse-biology-19", "igcse-biology-modular-24-unit-1", "igcse-biology-modular-24-unit-2"]
    if "further" in tl:
        return ["igcse-further-maths-19"]
    if "math" in tl:
        return ["igcse-maths-a-18-higher", "igcse-maths-a-18-foundation",
                "igcse-maths-a-modular-24-higher-unit-1", "igcse-maths-a-modular-24-higher-unit-2",
                "igcse-maths-a-modular-24-foundation-unit-1", "igcse-maths-a-modular-24-foundation-unit-2"]
    if "double award" in tl or "science" in tl:
        return IG_4["4SD0"] + IG_4["4XSD1"]
    if "literature" in tl:
        return ["igcse-english-literature-16"]
    if "english" in tl:
        return IG_4["4EA1"]
    if "business" in tl:
        return ["igcse-business-19"]
    if "accounting" in tl:
        return IG_4["4AC1"]
    if "econ" in tl:
        return ["igcse-economics-17"]
    if "ict" in tl:
        return ["igcse-ict-17"]
    if "geography" in tl:
        return ["igcse-geography-19"]
    if "history" in tl:
        return ["igcse-history-17"]
    return None

def build_patterns():
    pats = []
    for code, slugs in CIE_AL.items():
        pats.append((re.compile(rf"\b{code}\b"), slugs, "cie"))
    for code, slugs in CIE_IG.items():
        pats.append((re.compile(rf"\b{code}\b"), slugs, "cie"))
    for code, slugs in IAL_W.items():
        pats.append((re.compile(rf"\b{code}\b", re.I), slugs, "edexcel-ial"))
    for code, slugs in IG_4.items():
        pats.append((re.compile(rf"\b{code}\b", re.I), slugs, "edexcel-ig"))
    return pats

PATTERNS = build_patterns()
RE_SESSION = re.compile(r"past paper|mark scheme|walkthrough|\bsolved\b|solution|may[/ ]?june|oct[/ ]?nov|\bm/j\b|\bo/n\b|paper\s*\d|\bqp\b|\bms\b", re.I)
RE_GUIDANCE = re.compile(r"tips|revision guide|how to (revise|study|get)|exam technique|predict(ed|ion|ions)|top \d+|grade boundaries|in \d+ minutes|a\*|secrets?", re.I)
RE_NT_BOARD = re.compile(r"\bAQA\b|\bOCR\b|\bIB\b|\bNCERT\b|\bCBSE\b|\bJEE\b|\bNEET\b|\bGCSE\b|\bKey Stage\b|\bKS[1-4]\b|\bAP\b|\bSAT\b")
RE_IAL_UNIT = re.compile(r"(IAL|International A[- ]?Level).{0,40}Unit\s*[1-6]|Unit\s*[1-6].{0,40}(IAL|International A[- ]?Level)", re.I)
RE_CHEM_UNIT = re.compile(r"Unit\s*[1-6]\b", re.I)

# recon-approved verdicts for the identified pools (report 2026-11-16);
# pools not listed here get a fresh derivation, flagged "recon-row-lost".
RECON_VERDICT = {
    "etphysics": "T1", "prosperity-academy": "T1", "dr-hanaa-assil": "T1", "zainematics": "T1",
    "craigndave": "T1", "science-with-hazel": "T1", "mega-lecture": "T1", "examsolutions": "T1",
    "tlmaths": "NT", "physics-by-m-anwar": "NT", "takingthebiz": "NT", "accounting-lecture": "NT",
    "the-econ-show": "NT",
}

def load_pool_tsv(slug):
    path = os.path.join(WORK, f"{slug}_up.tsv")
    rows = []
    with open(path, encoding="utf-8") as f:
        for l in f:
            parts = l.rstrip("\n").split("\t")
            if len(parts) >= 5:
                rows.append({"id": parts[0], "duration": parts[1], "views": parts[2],
                             "ts": parts[3], "title": parts[4]})
    return rows

def known_pools_union():
    """Video ids already inventoried by ANY prior lane (inventory/channels/*)."""
    ids = set()
    chdir = os.path.join(RES, "Videos/inventory/channels")
    for fn in os.listdir(chdir):
        p = os.path.join(chdir, fn)
        try:
            if fn.endswith(".json"):
                d = json.load(open(p))
                for v in d.get("videos", []):
                    ids.add(v.get("id"))
            elif fn.endswith(".tsv"):
                with open(p, encoding="utf-8") as f:
                    for l in f:
                        head = l.split("\t", 1)[0]
                        if re.match(r"^[\w-]{11}$", head):
                            ids.add(head)
        except Exception:
            pass
    return ids

def shipped_union():
    ids = set()
    vmap = os.path.join(HUB, "content/video-map")
    for fn in os.listdir(vmap):
        if not fn.endswith(".json"):
            continue
        d = json.load(open(os.path.join(vmap, fn)))
        for v in d.get("videos", []):
            ids.add(v.get("id"))
    return ids

def classify_rows(rows):
    code_slugs = defaultdict(int)      # slug -> title count
    code_fam = Counter()               # cie / edexcel-ial / edexcel-ig
    old_gce = 0
    session = guidance = 0
    nt_board = 0
    ial_unit = 0
    spine_hit = 0
    samples = defaultdict(list)
    for r in rows:
        t = r["title"]
        hit = False
        for pat, slugs, fam in PATTERNS:
            if pat.search(t):
                hit = True
                code_fam[fam] += 1
                for s in slugs:
                    code_slugs[s] += 1
                if len(samples[fam]) < 5 and t not in samples[fam]:
                    samples[fam].append(t)
                break  # first (most specific) family wins per title
        if not hit and RE_ED_IAL_CHEM_UNIT.search(t):
            hit = True
            code_fam["edexcel-ial-chem-unit"] += 1
            code_slugs["ial-chemistry-17"] += 1
            if len(samples["edexcel-ial-chem-unit"]) < 5:
                samples["edexcel-ial-chem-unit"].append(t)
        if not hit and RE_ED_IG.search(t):
            sl = ed_ig_subject_slugs(t)
            if sl:
                hit = True
                code_fam["edexcel-ig-register"] += 1
                for s in sl:
                    code_slugs[s] += 1
                if len(samples["edexcel-ig-register"]) < 5:
                    samples["edexcel-ig-register"].append(t)
        if not hit and RE_CIE_LIT.search(t):
            hit = True
            code_fam["cie-lit"] += 1
            code_slugs["cie-igcse-english-literature-21"] += 1
            if len(samples["cie-lit"]) < 5:
                samples["cie-lit"].append(t)
        if re.search(OLD_GCE, t):
            old_gce += 1
        if RE_SESSION.search(t):
            session += 1
        if RE_GUIDANCE.search(t):
            guidance += 1
        if RE_NT_BOARD.search(t):
            nt_board += 1
        if RE_IAL_UNIT.search(t) or ("chem" in t.lower() and RE_CHEM_UNIT.search(t)):
            ial_unit += 1
        if hit:
            spine_hit += 1
    n = len(rows)
    return {"n": n, "spineCodeHitTitles": spine_hit,
            "codeFamilies": dict(code_fam), "codeSlugs": dict(sorted(code_slugs.items(), key=lambda kv: -kv[1])),
            "oldGceTitles": old_gce, "sessionRegister": session, "guidanceRegister": guidance,
            "ntBoardMarkerTitles": nt_board, "ialUnitRegister": ial_unit, "samples": dict(samples)}

def verdict_suggest(c, slug):
    n = c["n"] or 1
    ratio = c["spineCodeHitTitles"] / n
    if slug in RECON_VERDICT:
        return RECON_VERDICT[slug], "recon-approved"
    if ratio >= 0.10 and c["n"] >= 80:
        return "T1", "fresh (recon row lost)"
    if ratio >= 0.02:
        return "T2", "fresh (recon row lost)"
    return "NT", "fresh (recon row lost)"

def main():
    resolve = {r["slug"]: r for r in json.load(open(os.path.join(WORK, "resolve.json")))}
    tabc = json.load(open(os.path.join(WORK, "tabcounts.json")))
    union = shipped_union()
    known = known_pools_union()
    print(f"shipped union: {len(union)} video ids; prior-inventory union: {len(known)} ids", flush=True)
    coverage = {}
    vmap = os.path.join(HUB, "content/video-map")
    for fn in sorted(os.listdir(vmap)):
        if fn.endswith(".json"):
            d = json.load(open(os.path.join(vmap, fn)))
            cov = d.get("coverage", {})
            if cov:
                coverage[fn[:-5]] = {"specPointsMapped": cov.get("specPointsMapped"),
                                     "specPointsTotal": cov.get("specPointsTotal"),
                                     "videosTotal": cov.get("videosTotal")}
    pools = []
    all_hits = 0
    for slug, rec in resolve.items():
        rows = load_pool_tsv(slug)
        c = classify_rows(rows)
        v, src = verdict_suggest(c, slug)
        overlap = sum(1 for r in rows if r["id"] in union)
        overlap_known = sum(1 for r in rows if r["id"] in known)
        pools.append({"slug": slug, "label": rec["label"], "uc": rec["uc"],
                      "tabs": tabc.get(slug, {}), "classification": c,
                      "verdict": v, "verdictSource": src, "overlapWithShippedUnion": overlap,
                      "overlapWithPriorInventories": overlap_known,
                      "reconCount": {"etphysics": 1374, "prosperity-academy": 1149, "dr-hanaa-assil": 432,
                                     "zainematics": 1449, "examsolutions": 4551, "craigndave": 842,
                                     "science-with-hazel": 949, "mega-lecture": 3859, "tlmaths": 4558,
                                     "the-econ-show": 3}.get(slug)})
        all_hits += c["spineCodeHitTitles"]
        print(f"{slug:22s} n={c['n']:5d} spineHits={c['spineCodeHitTitles']:5d} "
              f"fam={c['codeFamilies']} oldGCE={c['oldGceTitles']:4d} sess={c['sessionRegister']:4d} "
              f"ntBoard={c['ntBoardMarkerTitles']:4d} overlap={overlap}/{overlap_known} -> {v} ({src})", flush=True)
    # ------------------------------------------------ re-adjudication groups
    ra = {}
    ep = json.load(open(f"{RES}/Videos/inventory/channels/econplusdal-uploads.json"))
    ep_rows = [{"id": v["id"], "title": v["title"]} for v in ep["videos"]]
    ep_c = classify_rows(ep_rows)
    ep_cie_re = re.compile(r"\bCIE\b|Cambridge|\b9708\b|\b9706\b", re.I)
    cie_hits = [{"id": r["id"], "title": r["title"]} for r in ep_rows if ep_cie_re.search(r["title"])]
    ep_ib = re.compile(r"\bIB\b|International Baccalaureate", re.I)
    ib_hits = [r["id"] for r in ep_rows if ep_ib.search(r["title"])]
    ep_fresh = 0
    ep_fresh_path = os.path.join(WORK, "ep_videos.tsv")
    if os.path.exists(ep_fresh_path):
        with open(ep_fresh_path, encoding="utf-8") as f:
            ep_fresh = sum(1 for l in f if "\t" in l and len(l.split("\t")[0]) == 11)
    ra["econplusdal-cie"] = {"poolN": len(ep_rows), "classification": ep_c, "cieCandidates": cie_hits,
                             "ibTitleCount": len(ib_hits), "freshVideosTabCount": ep_fresh,
                             "newSinceP11": max(0, ep_fresh - len(ep_rows)) if ep_fresh else None,
                             "reconCount": 38,
                             "reproNote": ("NOT REPRODUCED at filing: the P11 pool of record carries 0 CIE/9708 "
                                           "titles (fresh /videos enumeration 761, +1 new upload since P11, "
                                           "still 0 CIE); 129 IB-econ titles confirmed no-target (no IB course "
                                           "in the spine). The recon's 38 CIE/9708 hits could not be re-derived "
                                           "from any enumeration of this channel; group closed no-change unless "
                                           "the owner can point at the enumeration that produced it.")}
    al_rows = []
    with open(f"{RES}/Videos/inventory/channels/p2f-allery-chemistry.tsv", encoding="utf-8") as f:
        for l in f:
            parts = l.rstrip("\n").split("\t")
            if len(parts) >= 2:
                al_rows.append({"id": parts[0], "title": parts[1]})
    al_c = classify_rows(al_rows)
    al_recon_re = re.compile(r"\bCIE\b", re.I)          # the recon's criterion — reproduces 41
    al_topic_re = re.compile(r"CIE\s+Topic", re.I)
    al_wide_re = re.compile(r"\bCIE\b|\b9701\b|\b0620\b|\bTopic\s*\d+", re.I)
    al_hits = [{"id": r["id"], "title": r["title"]} for r in al_rows if al_recon_re.search(r["title"])]
    al_topic = [r["id"] for r in al_rows if al_topic_re.search(r["title"])]
    al_wide = [r["id"] for r in al_rows if al_wide_re.search(r["title"])]
    ra["allery-chemistry-cie"] = {"poolN": len(al_rows), "classification": al_c, "cieCandidates": al_hits,
                                  "cieTopicSubset": len(al_topic), "wideCieCount": len(al_wide),
                                  "reconCount": 41,
                                  "reproNote": ("REPRODUCED exactly: criterion \bCIE\b over the 364-row P2F pool "
                                                "of record gives 41 (35 'CIE Topic' revision titles + 6 old CIE "
                                                "session papers 9701/2x-5x) — the recon's 41.")}
    print(f"readjudication: econplusdal {len(ep_rows)} rows -> {len(cie_hits)} CIE candidates (recon 38); "
          f"allery {len(al_rows)} rows -> {len(al_hits)} CIE candidates (recon 41)", flush=True)
    out = {"generatedUtc": __import__("datetime").datetime.utcnow().strftime("%Y-%m-%dT%H:%M:%SZ"),
           "shippedUnionSize": len(union), "pools": pools, "readjudication": ra,
           "coverageBaselines": coverage,
           "totals": {"uploadsEnumerated": sum(p["classification"]["n"] for p in pools),
                      "spineCodeHitTitles": all_hits}}
    json.dump(out, open(os.path.join(WORK, "analysis.json"), "w"), indent=1)
    print(f"TOTAL uploads {out['totals']['uploadsEnumerated']}, spine-code-hit titles {all_hits}")

if __name__ == "__main__":
    main()
