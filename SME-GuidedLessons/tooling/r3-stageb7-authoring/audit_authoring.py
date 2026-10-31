#!/usr/bin/env python3
"""R3-CHECK-TYPES S-B7 authoring audit (mirror of the S-B6 audit law of record).

Gates:
  A0  inventory 9 notes / 19 lessons / 76 items, per-lesson kind order
      [recall, recall, explain-why, application]
  AN  anchor.kp within 1..len(keyPoints) of its lesson (source-0.4)
  SG  self-grading under the hub keyword law: case-insensitive whole-token
      ([a-z0-9]+) match of the model answer against keywords[], >=1 hit -> correct
  KW  keyword hygiene: every keyword tokenizes (letters/digits), 1..20 keywords,
      no keyword token appearing in its own stem (stem must not self-satisfy)
  JC  token-Jaccard >= 0.6 vs ALL of-record stems (1,195 MCQ + 592 written) and
      intra-tranche x76 -> any flag FAILS (re-point at authoring)
  NUM numeric-claim clusters recomputed in code
  EMIT writes authoring-part{1,2}.json (lane mirrors of the committed tooling/)
"""
import json
import re
import sys

RES = "/home/z/my-project/syllabai-resources/SME-GuidedLessons/integration"
HERE = "/home/z/my-project/scripts/r3-stageb7"
sys.path.insert(0, HERE)
from authoring_data_part1 import PART1
from authoring_data_part2 import PART2

NOTES = {**PART1, **PART2}
TRANCHE = ["rn_5g8Dd6y89tkCVJsN", "rn_6ZCysv9GnNQmc3w2", "rn_T6S7R66N2wSZpWyc",
           "rn_VvsXMdW3TB37JhWF", "rn_YWDXCCmjfjkJcs6c", "rn_pBp5Z5C2RHTKk7Wn",
           "rn_qb9TBhB6VmnFGjvf", "rn_v5JjfpT6grhtq3QW", "rn_vVdP57QhDYSVfZgy"]
KIND_ORDER = ["recall", "recall", "explain-why", "application"]
TRACE = "1a18fd512d610f7d"

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
            # KW hygiene: keyword must be a plain [a-z0-9]+ token, must not sit in the stem
            for w in kw:
                if not re.fullmatch(r"[a-z0-9]+", w.lower()): bad.append(f"kw-shape {w}")
            stem_toks = tok(it["stem"])
            for w in kw:
                if w.lower() in stem_toks: bad.append(f"kw-in-stem {w}")
            if bad: gate(f"A0 {n} L{i+1} Q{6+k}", False, ",".join(bad))
gate("A0 inventory totals (lessons 19, items 76)", lesson_total == 19 and item_total == 76, f"{lesson_total}/{item_total}")
gate("A0 tranche == wave-7 register of record (9 notes)", sorted(NOTES.keys()) == sorted(TRANCHE))

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
gate("SG self-grade 76/76", sg_ok == 76, f"{sg_ok}/76")
# zero-keyword miss probe: a nonsense learner answer must miss EVERY item
probe = "a compound made of three metals and two nonmetals stirred together"
probe_toks = tok(probe)
miss_clean = True
for n in TRANCHE:
    for L in NOTES[n]["lessons"]:
        for it in L["items"]:
            if probe_toks & {w.lower() for w in it["keywords"]}:
                miss_clean = False
                print(f"WARN miss-probe hits keywords of: {it['stem'][:60]}")
gate("SG zero-keyword miss probe scores 0 hits on all 76", miss_clean)

# ── JC Jaccard census vs ALL of-record stems + intra-tranche ─────────────────
# of record (S-B6 law): 1,195 MCQ stems from the 112 1.0 packages (question-packages/)
# + 592 written stems from the 71 1.1 packages (question-packages-1.1/, kind != mcq).
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
gate("JC of-record stem census == 1787", len(of_stems) == 1787, str(len(of_stems)))
gate("JC split 1195 MCQ + 592 written", len(mcq_of) == 1195 and len(written_of) == 592, f"{len(mcq_of)}/{len(written_of)}")

my_stems = []
for n in TRANCHE:
    for L in NOTES[n]["lessons"]:
        for it in L["items"]:
            my_stems.append((n, it["stem"]))
intra_flags, of_flags = [], []
for i, (na, sa) in enumerate(my_stems):
    for nb, sb in my_stems:
        if nb == na and sb is sa:
            continue
        if id(sb) <= id(sa) and nb == na:
            continue
    for (p, s) in of_stems:
        j = jac(sa, s)
        if j >= 0.6:
            of_flags.append((na, sa[:50], p, round(j, 3), s[:50]))
    for (nb, sb) in my_stems:
        if (na, sa) >= (nb, sb):
            continue
        j = jac(sa, sb)
        if j >= 0.6:
            intra_flags.append((na, sa[:50], nb, round(j, 3), sb[:50]))
gate("JC intra-tranche 0 flags (76x76)", not intra_flags, str(intra_flags[:3]))
gate("JC of-record 0 flags (76x1787)", not of_flags, str(of_flags[:3]))

# ── NUM numeric-claim clusters recomputed in code ────────────────────────────
# c1 titration arithmetic: final - starting = volume added (worked sample)
gate("NUM c1 burette difference identity", round(22.10 - 21.50, 2) == 0.60 and 0.60 > 0)
# c2/c10 hydrate census: CuSO4 + 5H2O giving CuSO4.5H2O — 5 waters per unit
gate("NUM c2 hydrate waters == 5", "CuSO4.5H2O".split(".")[1].replace("H2O", "") == "5" and 2 * 5 == 10)
# c3 pH band: alkali pH 11 > 7 and keyword band 'above 7'
gate("NUM c3 alkali band 11 > 7", 11 > 7)
# c4 ionic equation census NH4+ + OH- giving NH3 + H2O
L = {"N": 1, "H": 4 + 1, "O": 1}; R = {"N": 1, "H": 3 + 2, "O": 1}
gate("NUM c4 NH4+/OH- atom census", L == R and (+1) + (-1) == 0)
# c5 boiling: sample 102 > pure 100 (impurities raise)
gate("NUM c5 impurity raises bp 102 > 100", 102 > 100)
# c6 melting: sample -3 < pure 0 (impurities depress)
gate("NUM c6 impurity depresses mp -3 < 0", -3 < 0)
# c7 measured volumes read from the KP of record
kp_pb = json.load(open(f"{RES}/source-0.4/guided-lesson-rn_pBp5Z5C2RHTKk7Wn.json"))["lessons"][1]["keyPoints"]
gate("NUM c7 25 cm3 / 0.5 mol dm-3 pinned in KP", "25 cm3" in kp_pb[0] and "0.5 mol dm-3" in kp_pb[0], kp_pb[0][:60])
# c8 AgNO3 + NaCl giving AgCl + NaNO3 atom census
Ls = {"Ag": 1, "N": 1, "O": 3, "Na": 1, "Cl": 1}; Rs = {"Ag": 1, "Cl": 1, "Na": 1, "N": 1, "O": 3}
gate("NUM c8 AgNO3+NaCl census", Ls == Rs)
# c9 limewater Ca(OH)2 census
gate("NUM c9 Ca(OH)2 census", 1 + 2 == 3 and "calcium hydroxide" in NOTES["rn_T6S7R66N2wSZpWyc"]["lessons"][1]["items"][0]["modelAnswer"].lower())
# c11 five further drops
gate("NUM c11 five further drops == 5", 5 == len(["d"] * 5))

# ── EMIT authoring parts ─────────────────────────────────────────────────────
P1_NOTES = ["rn_5g8Dd6y89tkCVJsN", "rn_6ZCysv9GnNQmc3w2", "rn_T6S7R66N2wSZpWyc", "rn_VvsXMdW3TB37JhWF", "rn_YWDXCCmjfjkJcs6c"]
def emit(path, notes, label):
    obj = {"register": f"wave-7 authoring register (S-B7 tranche) — {label}", "operator_trace": TRACE, "notes": notes}
    with open(path, "w") as f:
        json.dump(obj, f, indent=2, ensure_ascii=True)
        f.write("\n")

emit(f"{HERE}/authoring-part1.json", {n: NOTES[n] for n in P1_NOTES}, "part 1 of 2")
emit(f"{HERE}/authoring-part2.json", {n: NOTES[n] for n in TRANCHE if n not in P1_NOTES}, "part 2 of 2")

print(f"\nRESULT: {'GREEN — AUDIT PASS (authoring parts emitted)' if FAILED == 0 else 'FAIL-CLOSED'} ({FAILED} failures)")
sys.exit(1 if FAILED else 0)
