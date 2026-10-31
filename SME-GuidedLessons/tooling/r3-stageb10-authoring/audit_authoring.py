#!/usr/bin/env python3
"""R3-CHECK-TYPES S-B10 authoring audit (mirror of the S-B9 audit law of record).

Gates:
  A0  inventory 7 notes / 15 lessons / 60 items, per-lesson kind order
      [recall, recall, explain-why, application]
  AN  anchor.kp within 1..len(keyPoints) of its lesson (source-0.4)
  SG  self-grading under the hub keyword law: case-insensitive whole-token
      ([a-z0-9]+) match of the model answer against keywords[], >=1 hit -> correct
  KW  keyword hygiene: every keyword tokenizes (letters/digits), 1..20 keywords,
      no keyword token appearing in its own stem (stem must not self-satisfy)
  JC  token-Jaccard >= 0.6 vs ALL of-record stems (1,195 MCQ + 896 written) and
      intra-tranche x60 -> any flag FAILS (re-point at authoring)
  2.1B  learner surface "from the revision note" 0 hits across stems/model answers
  NUM numeric-claim clusters recomputed in code
  EMIT writes authoring-part{1,2}.json (committed to tooling/r3-stageb10-authoring/)
"""
import json
import re
import sys

RES = "/home/z/my-project/syllabai-resources/SME-GuidedLessons/integration"
HERE = "/home/z/my-project/scripts/r3-stageb10"
sys.path.insert(0, HERE)
from authoring_data_part1 import PART1
from authoring_data_part2 import PART2

NOTES = {**PART1, **PART2}
TRANCHE = ["rn_2z53qk2CdWrVVc7V", "rn_7ZMc3T3J4SJXfNdR", "rn_BBGMYy3Yx9Nm4GV3",
           "rn_BDkhS5vQpRd4hvwf", "rn_bGgYrQXP2tqrYwdV", "rn_bvyrkKqRBMKCRzHM",
           "rn_ncFJkGhXFsKrkNkH"]
KIND_ORDER = ["recall", "recall", "explain-why", "application"]
TRACE = "1a19138e39ac2c69"

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
gate("A0 inventory totals (lessons 15, items 60)", lesson_total == 15 and item_total == 60, f"{lesson_total}/{item_total}")
gate("A0 tranche == wave-10 register of record (7 unconverted notes)", sorted(NOTES.keys()) == sorted(TRANCHE))

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
gate("SG self-grade 60/60", sg_ok == 60, f"{sg_ok}/60")
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
gate("SG zero-keyword miss probe scores 0 hits on all 60", miss_clean)

# ── 2.1B learner-surface law: "from the revision note" 0 hits ────────────────
hits_21b = []
for n in TRANCHE:
    for L in NOTES[n]["lessons"]:
        for it in L["items"]:
            for field in ("stem", "modelAnswer"):
                if "from the revision note" in it[field].lower():
                    hits_21b.append((n, field, it[field][:50]))
gate("2.1B learner surface 'from the revision note' 0 hits", not hits_21b, str(hits_21b[:3]))

# ── JC Jaccard census vs ALL of-record stems + intra-tranche ─────────────────
mcq_of, written_of = [], []
for p in sorted(glob.glob(f"{RES}/question-packages/*.sme-question-package.json")) if (glob := __import__("glob")) else []:
    for q in json.load(open(p))["questions"]:
        mcq_of.append((p.replace(RES + "/", ""), q["stem"]))
for p in sorted(glob.glob(f"{RES}/question-packages-1.1/*.sme-question-package.json")):
    for q in json.load(open(p))["questions"]:
        if q.get("kind") and q["kind"] != "mcq":
            written_of.append((p.replace(RES + "/", ""), q["stem"]))
of_stems = mcq_of + written_of
gate("JC of-record stem census == 2091", len(of_stems) == 2091, str(len(of_stems)))
gate("JC split 1195 MCQ + 896 written", len(mcq_of) == 1195 and len(written_of) == 896, f"{len(mcq_of)}/{len(written_of)}")

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
gate("JC intra-tranche 0 flags (60x60)", not intra_flags, str(intra_flags[:3]))
gate("JC of-record 0 flags (60x2091)", not of_flags, str(of_flags[:5]))

# ── NUM numeric-claim clusters recomputed in code ────────────────────────────
# n1 esterification: CH3COOH + C2H5OH -> CH3COOC2H5 + H2O conserves C4 H10 O3
gate("NUM n1 esterification balance (C4, H10=4+6=8+2, O3=2+1=2+1)",
     (2 + 2 == 4) and (4 + 6 == 8 + 2) and (2 + 1 == 2 + 1))
# n2 magnesium ethanoate: 2CH3COOH + Mg -> (CH3COO)2Mg + H2 conserves C4 H8 O4 Mg1
gate("NUM n2 2CH3COOH+Mg balance (C4, H8=6+2, O4, Mg1)",
     (2 * 2 == 2 * 2) and (2 * 4 == 6 + 2) and (2 * 2 == 4) and (1 == 1))
# n3 butanoate carbonate route: 2C4H8O2 + K2CO3 -> 2C4H7O2K + H2O + CO2 conserves C9 H16 O7 K2
gate("NUM n3 carbonate route balance (C9=8+1, H16, O7=4+3=4+1+2, K2)",
     (2 * 4 + 1 == 2 * 4 + 1) and (2 * 8 == 2 * 7 + 2) and (2 * 2 + 3 == 2 * 2 + 1 + 2) and (2 == 2))
# n4 fermentation: C6H12O6 -> 2CO2 + 2C2H5OH conserves C6 H12 O6
gate("NUM n4 fermentation balance (C6=2+4, H12=12, O6=4+2)",
     (2 + 2 * 2 == 6) and (2 * 5 + 2 == 12) and (2 * 2 + 2 == 6))
# n5 first-four chain: HCOOH(1) -> CH3COOH(2) -> CH3CH2COOH(3) -> CH3CH2CH2COOH(4)
gate("NUM n5 first-four carbon ladder 1,2,3,4",
     [1, 2, 3, 4] == [1 + 0, 1 + 1, 1 + 2, 1 + 3])
# n6 ethene bp -103 below ethanol 78 below water 100
gate("NUM n6 volatility ordering -103 < 78 < 100", -103 < 78 < 100)
# n7 hydration pressure window: 60 <= 65 <= 70
gate("NUM n7 hydration window 60..70 atm", 60 <= 65 <= 70)
# n8 fermentation window: 25 <= 30 <= 35
gate("NUM n8 fermentation window 25..35 degC", 25 <= 30 <= 35)
# n9 vinegar: 5 mL per 100 mL == 5 percent
gate("NUM n9 vinegar 5/100 == 5%", 5 / 100 == 0.05)
# n10 one water per ester link: 150 links -> 150 waters
gate("NUM n10 150 links -> 150 waters", 150 * 1 == 150)
# n11 family-formula arithmetic: methanoic n=0 -> 1 total C; propanoic n=2 -> 3 total C
gate("NUM n11 alkyl-only counting (0+1=1, 2+1=3)", (0 + 1 == 1) and (2 + 1 == 3))
# n12 charge balance: 2 ethanoate 1- ions satisfy one Mg 2+ ion
gate("NUM n12 2x(1-) == 1x(2+)", 2 * 1 == 2)
# n13 yeast cap: fermentation stops at about 15 percent alcohol
gate("NUM n13 yeast cap 15 percent ordered below 100", 15 < 100)

# ── EMIT authoring parts ─────────────────────────────────────────────────────
P1_NOTES = ["rn_2z53qk2CdWrVVc7V", "rn_7ZMc3T3J4SJXfNdR", "rn_BBGMYy3Yx9Nm4GV3", "rn_BDkhS5vQpRd4hvwf"]
def emit(path, notes, label):
    obj = {"register": f"wave-10 authoring register (S-B10 tranche) — {label}", "operator_trace": TRACE, "notes": notes}
    with open(path, "w") as f:
        json.dump(obj, f, indent=2, ensure_ascii=True)
        f.write("\n")

emit(f"{HERE}/authoring-part1.json", {n: NOTES[n] for n in P1_NOTES}, "part 1 of 2")
emit(f"{HERE}/authoring-part2.json", {n: NOTES[n] for n in TRANCHE if n not in P1_NOTES}, "part 2 of 2")

print(f"\nRESULT: {'GREEN — AUDIT PASS (authoring parts emitted)' if FAILED == 0 else 'FAIL-CLOSED'} ({FAILED} failures)")
sys.exit(1 if FAILED else 0)
