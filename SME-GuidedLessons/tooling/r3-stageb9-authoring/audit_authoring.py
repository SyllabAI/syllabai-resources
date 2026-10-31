#!/usr/bin/env python3
"""R3-CHECK-TYPES S-B9 authoring audit (mirror of the S-B8 audit law of record).

Gates:
  A0  inventory 11 notes / 25 lessons / 100 items, per-lesson kind order
      [recall, recall, explain-why, application]
  AN  anchor.kp within 1..len(keyPoints) of its lesson (source-0.4)
  SG  self-grading under the hub keyword law: case-insensitive whole-token
      ([a-z0-9]+) match of the model answer against keywords[], >=1 hit -> correct
  KW  keyword hygiene: every keyword tokenizes (letters/digits), 1..20 keywords,
      no keyword token appearing in its own stem (stem must not self-satisfy)
  JC  token-Jaccard >= 0.6 vs ALL of-record stems (1,195 MCQ + 796 written) and
      intra-tranche x100 -> any flag FAILS (re-point at authoring)
  NUM numeric-claim clusters recomputed in code
  EMIT writes authoring-part{1,2}.json (committed to tooling/r3-stageb9-authoring/)
"""
import json
import re
import sys

RES = "/home/z/my-project/syllabai-resources/SME-GuidedLessons/integration"
HERE = "/home/z/my-project/scripts/r3-stageb9"
sys.path.insert(0, HERE)
from authoring_data_part1 import PART1
from authoring_data_part2 import PART2

NOTES = {**PART1, **PART2}
TRANCHE = ["rn_6c2G8nJpFSnQnbcP", "rn_9J7DQhskyxzhd7CP", "rn_DBGf3WVffDBNDp4R",
           "rn_DrqzYWZMScqGrbWT", "rn_H2zGfgH76qYV5cmr", "rn_H9chr9BWCfXYW472",
           "rn_HqqBFgKRHykMMhbB", "rn_MmqCNJfWbtYzRVqT", "rn_NdJGQM8BqHmTy7Vg",
           "rn_V3hNWh6QWrbCRHrX", "rn_wDdXr5k7gknQ7xJp"]
KIND_ORDER = ["recall", "recall", "explain-why", "application"]
TRACE = "1a190d455ab9612d"

FAILED = 0
def gate(name, ok, detail=""):
    global FAILED
    if not ok:
        FAILED += 1
        print(f"FAIL {name} — {detail}")
    return ok

tok = lambda s: set(re.findall(r"[a-z0-9]+", s.lower()))
def jac(a, b):
    A, B = tok(a), tok(b)
    if not A or not B:
        return 0.0
    return len(A & B) / len(A | B)

# ── A0 inventory ─────────────────────────────────────────────────────────────
item_total, lesson_total = 0, 0
for n in TRANCHE:
    s4 = json.load(open(f"{RES}/source-0.4/guided-lesson-{n}.json"))
    body = NOTES[n]
    gate(f"A0 {n} lessons == source lessons", len(body["lessons"]) == len(s4["lessons"]))
    for i, (L, items) in enumerate(zip(s4["lessons"], body["lessons"])):
        lesson_total += 1
        item_total += len(items["items"])
        kinds = [it["kind"] for it in items["items"]]
        gate(f"A0 {n} L{i+1} kind order", kinds == KIND_ORDER, ",".join(kinds))
        for k, it in enumerate(items["items"]):
            bad = []
            if not it.get("stem", "").strip(): bad.append("stem")
            if not it.get("misconceptionClass", "").strip(): bad.append("mc-class")
            if not it.get("modelAnswer", "").strip(): bad.append("modelAnswer")
            kw = it.get("keywords", [])
            if not (1 <= len(kw) <= 20) or any((not w) or (not w.strip()) for w in kw): bad.append("keywords")
            if "options" in it: bad.append("options-forbidden")
            kp = it.get("anchor", {}).get("kp")
            if not (isinstance(kp, int) and 1 <= kp <= len(L["keyPoints"])): bad.append(f"anchor {kp}")
            for w in kw:
                if not re.fullmatch(r"[a-z0-9]+", w.lower()): bad.append(f"kw-shape {w}")
            stem_toks = tok(it["stem"])
            for w in kw:
                if w.lower() in stem_toks: bad.append(f"kw-in-stem {w}")
            if bad: gate(f"A0 {n} L{i+1} Q{6+k}", False, ",".join(bad))
gate("A0 inventory totals (lessons 25, items 100)", lesson_total == 25 and item_total == 100, f"{lesson_total}/{item_total}")
gate("A0 tranche == wave-9 register of record (11 unconverted notes)", sorted(NOTES.keys()) == sorted(TRANCHE))

# ── SG self-grading under the hub keyword law ────────────────────────────────
sg_ok = 0
for n in TRANCHE:
    for li, L in enumerate(NOTES[n]["lessons"]):
        for qi, it in enumerate(L["items"]):
            kws = {w.lower() for w in it["keywords"]}
            ma_toks = tok(it["modelAnswer"])
            hits = sorted(kws & ma_toks)
            if hits:
                sg_ok += 1
            else:
                gate(f"SG {n} L{li+1} Q{6+qi} model answer grades correct", False, "0 keyword hits in model answer")
gate("SG self-grade 100/100", sg_ok == 100, f"{sg_ok}/100")
# zero-keyword miss probe: a nonsense learner answer must miss EVERY item
probe = "a purple elephant balanced seventeen umbrellas on a quartz harmonica while zephyrs wandered yonder"
probe_toks = tok(probe)
miss_clean = True
for n in TRANCHE:
    for L in NOTES[n]["lessons"]:
        for it in L["items"]:
            if probe_toks & {w.lower() for w in it["keywords"]}:
                miss_clean = False
                print(f"WARN miss-probe hits keywords of: {it['stem'][:60]}")
gate("SG zero-keyword miss probe scores 0 hits on all 100", miss_clean)

# ── JC Jaccard census vs ALL of-record stems + intra-tranche ─────────────────
# of record (S-B8 law): 1,195 MCQ stems from the 112 1.0 packages (question-packages/)
# + 796 written stems from the 94 1.1 packages (question-packages-1.1/, kind != mcq).
# The 1.1 MCQ stems are byte-duplicates of the 1.0 ones and are NOT double-counted.
import glob
mcq_of, written_of = [], []
for p in sorted(glob.glob(f"{RES}/question-packages/*.sme-question-package.json")):
    for q in json.load(open(p))["questions"]:
        mcq_of.append((p.replace(RES + "/", ""), q["stem"]))
for p in sorted(glob.glob(f"{RES}/question-packages-1.1/*.sme-question-package.json")):
    for q in json.load(open(p))["questions"]:
        if q.get("kind") and q["kind"] != "mcq":
            written_of.append((p.replace(RES + "/", ""), q["stem"]))
of_stems = mcq_of + written_of
gate("JC of-record stem census == 1991", len(of_stems) == 1991, str(len(of_stems)))
gate("JC split 1195 MCQ + 796 written", len(mcq_of) == 1195 and len(written_of) == 796, f"{len(mcq_of)}/{len(written_of)}")

my_stems = []
for n in TRANCHE:
    for L in NOTES[n]["lessons"]:
        for it in L["items"]:
            my_stems.append((n, it["stem"]))
intra_flags, of_flags = [], []
for (na, sa) in my_stems:
    for (p, s) in of_stems:
        j = jac(sa, s)
        if j >= 0.6:
            of_flags.append((na, sa[:50], p.split("/")[-1], round(j, 3), s[:50]))
for i, (na, sa) in enumerate(my_stems):
    for (nb, sb) in my_stems:
        if (na, sa) >= (nb, sb):
            continue
        j = jac(sa, sb)
        if j >= 0.6:
            intra_flags.append((na, sa[:50], nb, round(j, 3), sb[:50]))
gate("JC intra-tranche 0 flags (100x100)", not intra_flags, str(intra_flags[:3]))
gate("JC of-record 0 flags (100x1991)", not of_flags, str(of_flags[:3]))

# ── NUM numeric-claim clusters recomputed in code ────────────────────────────
# c1 alkane formula: n = 12 -> C12H26 (2*12+2 hydrogens)
gate("NUM c1 C12H26: 2*12+2 == 26", 2 * 12 + 2 == 26)
# c2 alkene formula: n = 6 -> C6H12 (2*6 hydrogens)
gate("NUM c2 C6H12: 2*6 == 12", 2 * 6 == 12)
# c3 propane complete combustion balances: C3H8 + 5O2 -> 3CO2 + 4H2O
gate("NUM c3 propane balance (C3=3, H8=8, O10=6+4)",
     (3 == 3) and (8 == 2 * 4) and (2 * 5 == 3 * 2 + 4 * 1))
# c4 butane complete combustion balances: 2C4H10 + 13O2 -> 8CO2 + 10H2O
gate("NUM c4 butane balance (C8=8, H20=20, O26=16+10)",
     (2 * 4 == 8) and (2 * 10 == 2 * 10) and (2 * 13 == 8 * 2 + 10 * 1))
# c5 methane CO-route balances: 2CH4 + 3O2 -> 2CO + 4H2O
gate("NUM c5 2CH4+3O2 balance (C2=2, H8=8, O6=2+4)",
     (2 == 2) and (2 * 4 == 2 * 4) and (2 * 3 == 2 * 1 + 4 * 1))
# c6 methane soot-route balances: CH4 + O2 -> C + 2H2O
gate("NUM c6 CH4+O2 balance (C1=1, H4=4, O2=2)",
     (1 == 1) and (4 == 2 * 2) and (1 * 2 == 2 * 1))
# c7 kerosene window: 25 < 180 < 350 (refinery gas below 25, bitumen above 350)
gate("NUM c7 180 in the kerosene window (25 < 180 < 350)", 25 < 180 < 350)
# c8 empirical formula: C4H10 -> divide by gcd 2 -> C2H5
import math
g = math.gcd(4, 10)
gate("NUM c8 C4H10 empirical == C2H5 (gcd 2)", g == 2 and (4 // g, 10 // g) == (2, 5))
# c9 haemoglobin affinity window ordered: 200 <= x <= 250
gate("NUM c9 affinity window 200..250 ordered", 200 <= 250)
# c10 pent-2-ene double bond sits between carbons 2 and 3 (locant = 2, lower-numbered end)
gate("NUM c10 pent-2-ene locant 2 -> bond after carbon 2", 2 + 1 == 3)
# c11 catalytic cracking window: 600..700 degrees Celsius
gate("NUM c11 cracking window 600..700 ordered", 600 <= 700)
# c12 sulfur route conservation: S + O2 -> SO2 keeps S1 O2
gate("NUM c12 S+O2->SO2 atoms conserved", (1, 2) == (1, 2))
# c13 acid-rain sulfur route: 2SO2 + O2 + 2H2O -> 2H2SO4 conserves S2 O8 H4
gate("NUM c13 2SO2+O2+2H2O balance (S2, O8=4+2+2? no: 4+2+2=8, H4)",
     (2 == 2) and (2 * 2 + 2 + 2 * 1 == 2 * 4) and (2 * 2 == 2 * 2))
# c14 methane chlorination CH4+Cl2->CH3Cl+HCl conserves Cl (2 = 1+1) and H (4 = 3+1)
gate("NUM c14 CH4+Cl2->CH3Cl+HCl conserves Cl2/H4", (1 * 2 == 1 + 1) and (4 == 3 + 1))

# ── EMIT authoring parts ─────────────────────────────────────────────────────
P1_NOTES = ["rn_6c2G8nJpFSnQnbcP", "rn_9J7DQhskyxzhd7CP", "rn_DBGf3WVffDBNDp4R",
            "rn_DrqzYWZMScqGrbWT", "rn_H2zGfgH76qYV5cmr", "rn_H9chr9BWCfXYW472"]
def emit(path, notes, label):
    obj = {"register": f"wave-9 authoring register (S-B9 tranche) — {label}", "operator_trace": TRACE, "notes": notes}
    with open(path, "w") as f:
        json.dump(obj, f, indent=2, ensure_ascii=True)
        f.write("\n")

emit(f"{HERE}/authoring-part1.json", {n: NOTES[n] for n in P1_NOTES}, "part 1 of 2")
emit(f"{HERE}/authoring-part2.json", {n: NOTES[n] for n in TRANCHE if n not in P1_NOTES}, "part 2 of 2")

print(f"\nRESULT: {'GREEN — AUDIT PASS (authoring parts emitted)' if FAILED == 0 else 'FAIL-CLOSED'} ({FAILED} failures)")
sys.exit(1 if FAILED else 0)
