#!/usr/bin/env python3
"""P4 scale pass — inheritance map builder (T-VIDEOMAP-P4).

For each of the 35 `inherit` courses (see work/p4/matrix.json classification),
compute the child-spec -> parent-spec containment map against the course that
already carries owner-approved external rows. Only containment >= 0.55 maps;
everything below stays an honest gap (recorded in unmappedChildSpecs).

Method (identical to the §11 probe in the P4 decision matrix): IDF-weighted
title-token containment — the fraction of a child spec's informative tokens
found in the best parent spec title, IDF taken over the parent course's spec
set. Deterministic; same input -> same map.

Output: Videos/drafts/_p4/inheritance-map.json (committed reviewed artifact;
the hub builder derives inherited rows from it at build time).

Usage: python3 build-p4-inheritance.py <hubCloneRoot>
"""
import json, os, re, math, sys, datetime
from collections import defaultdict

HUB = sys.argv[1] if len(sys.argv) > 1 else "/home/z/my-project/repos/syllabai-v2-fresh"
RES = "/home/z/my-project/repos/syllabai-resources"
SPINES = os.path.join(HUB, "apps/hub/spines")
OUT = os.path.join(RES, "Videos/drafts/_p4")
os.makedirs(OUT, exist_ok=True)
THRESHOLD = 0.55

STOP = set("""a an the of and or to in on for with without by is are be been use uses using
this that these those which who what when where how why all any both each other its it their
there from into onto about between during before after above below up down out off over under
again further then once here do does did done have has had having i you he she we they them his
her its our your my me as at but if not no nor only own same so than too very can will just
should now also may might must shall should would could following given list including include
includes state states describe explain calculate recall recognise understand understandings""".split())

def norm(t):
    t = (t or "").lower()
    t = re.sub(r"[^a-z0-9\s/+\-]", " ", t)
    return re.sub(r"\s+", " ", t).strip()

def toks(t):
    return [w for w in norm(t).split() if w not in STOP and len(w) > 2]

def load_specs(course):
    s = json.load(open(f"{SPINES}/{course}.json"))
    return [(n["code"], n["title"] or "") for n in s["curriculum"]["nodes"]
            if n["family"] == "SPEC_POINT"]

TRIPLE_CIE = {"biology": "cie-igcse-biology-23", "chemistry": "cie-igcse-chemistry-23", "physics": "cie-igcse-physics-23"}
TRIPLE_EDX = {"biology": "igcse-biology-19", "chemistry": "igcse-chemistry-19", "physics": "igcse-physics-19"}
A_LEVEL_CIE = {"biology": "cie-a-level-biology-25", "chemistry": "cie-a-level-chemistry-25", "physics": "cie-a-level-physics-25"}

PARENT = {}
for sub, p in TRIPLE_CIE.items():
    PARENT[f"cie-igcse-science-co-ordinated-sciences-double-award-23-{sub}"] = p
    PARENT[f"cie-igcse-science-combined-science-23-{sub}"] = p
for sub, p in TRIPLE_EDX.items():
    PARENT[f"igcse-science-double-award-17-{sub}"] = p
    PARENT[f"igcse-science-double-award-modular-24-{sub}-unit-1"] = p
    PARENT[f"igcse-science-double-award-modular-24-{sub}-unit-2"] = p
    PARENT[f"igcse-{sub}-modular-24-unit-1"] = p
    PARENT[f"igcse-{sub}-modular-24-unit-2"] = p
for sub, p in A_LEVEL_CIE.items():
    PARENT[f"cie-as-{sub}-25"] = p
PARENT["cie-igcse-maths-25-core"] = "cie-igcse-maths-25-extended"
PARENT["cie-igcse-maths-international-maths-23-core"] = "cie-igcse-maths-25-extended"
PARENT["cie-igcse-maths-international-maths-23-extended"] = "cie-igcse-maths-25-extended"
PARENT["igcse-maths-a-18-foundation"] = "igcse-maths-a-18-higher"
for u in ("foundation-unit-1", "foundation-unit-2", "higher-unit-1", "higher-unit-2"):
    PARENT[f"igcse-maths-a-modular-24-{u}"] = "igcse-maths-a-18-higher"
# §11.1 decision lane: IAL sciences take CIE A-level topical rows (boardMismatch:true)
PARENT["ial-biology-18"] = "cie-a-level-biology-25"
PARENT["ial-chemistry-17"] = "cie-a-level-chemistry-25"
PARENT["ial-physics-19"] = "cie-a-level-physics-25"

parent_cache = {}
def get_parent(course):
    if course not in parent_cache:
        specs = load_specs(course)
        tset = {c: set(toks(t)) for c, t in specs}
        df = defaultdict(int)
        for s in tset.values():
            for w in s:
                df[w] += 1
        parent_cache[course] = (specs, tset, df)
    return parent_cache[course]

def best(child_title, parent_course):
    _, tset, df = get_parent(parent_course)
    ctoks = set(toks(child_title))
    if not ctoks:
        return 0.0, None
    tot = sum(1.0 / math.log(2 + df.get(t, 0)) for t in ctoks)
    if not tot:
        return 0.0, None
    best_s, bcode = 0.0, None
    for code, ptoks in tset.items():
        inter = sum(1.0 / math.log(2 + df.get(t, 0)) for t in ctoks if t in ptoks)
        sc = inter / tot
        if sc > best_s:
            best_s, bcode = sc, code
    return best_s, bcode

spec_cache = {}
def specs_of(course):
    if course not in spec_cache:
        spec_cache[course] = load_specs(course)
    return spec_cache[course]

now = datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
parents_out, stats = {}, {}
for child in sorted(PARENT):
    par = PARENT[child]
    spec_map, unmapped = {}, []
    child_specs = specs_of(child)
    for code, title in child_specs:
        # guard: trivially short spec titles (<=2 informative tokens) always
        # produce degenerate 1.0 containments — keep them honestly unmapped
        if len(set(toks(title))) < 3:
            unmapped.append(code)
            continue
        s, pc = best(title, par)
        if s >= THRESHOLD and pc:
            spec_map[code] = {"parentSpec": pc, "containment": round(s, 3)}
        else:
            unmapped.append(code)
    parents_out[child] = {"parent": par, "specMap": spec_map, "unmappedChildSpecs": unmapped}
    stats[child] = {"specs": len(child_specs), "mapped": len(spec_map), "unmapped": len(unmapped)}
    print(f"{child:64s} -> {par:34s} n={len(child_specs):4d} mapped={len(spec_map):4d}")

out = {
    "schema": "syllabai.p4-inheritance-map/1",
    "task": "T-VIDEOMAP-P4 (inheritance lane)",
    "threshold": THRESHOLD,
    "method": ("idf-weighted title-token containment of each child spec title against the parent "
               "course's spec titles (identical to the P4 decision-matrix probe); containment >= 0.55 "
               "maps the child spec to its best parent spec; below-threshold specs stay honestly "
               "unmapped and are listed in unmappedChildSpecs. Deterministic — same spines, same map."),
    "parentRowBasis": ("only owner-approved rows (reviewed:true) of the parent course's external "
                       "lanes (video-map.draft.external.json + video-map.draft.external-p2e.json "
                       "where present) are eligible for inheritance"),
    "generatedUtc": now,
    "parents": parents_out,
}
path = os.path.join(OUT, "inheritance-map.json")
json.dump(out, open(path, "w"), indent=1)
print(f"\nwrote {path}")
tot_c = sum(s["specs"] for s in stats.values())
tot_m = sum(s["mapped"] for s in stats.values())
print(f"TOTAL child specs {tot_c}, mapped>= {THRESHOLD}: {tot_m} ({100.0*tot_m/tot_c:.1f}%)")
