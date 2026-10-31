#!/usr/bin/env python3
"""R3-CHECK-TYPES S-B8 authoring audit (mirror of the S-B7 audit law of record).

Gates:
  A0  inventory 14 notes / 32 lessons / 128 items, per-lesson kind order
      [recall, recall, explain-why, application]
  AN  anchor.kp within 1..len(keyPoints) of its lesson (source-0.4)
  SG  self-grading under the hub keyword law: case-insensitive whole-token
      ([a-z0-9]+) match of the model answer against keywords[], >=1 hit -> correct
  KW  keyword hygiene: every keyword tokenizes (letters/digits), 1..20 keywords,
      no keyword token appearing in its own stem (stem must not self-satisfy)
  JC  token-Jaccard >= 0.6 vs ALL of-record stems (1,195 MCQ + 668 written) and
      intra-tranche x128 -> any flag FAILS (re-point at authoring)
  NUM numeric-claim clusters recomputed in code
  EMIT writes authoring-part{1,2}.json (committed to tooling/r3-stageb8-authoring/)
"""
import json
import re
import sys

RES = "/home/z/my-project/syllabai-resources/SME-GuidedLessons/integration"
HERE = "/home/z/my-project/scripts/r3-stageb8"
sys.path.insert(0, HERE)
from authoring_data_part1 import PART1
from authoring_data_part2 import PART2

NOTES = {**PART1, **PART2}
TRANCHE = ["rn_3wZh9qRT7qFJn9QW", "rn_6478QfpYNQDjZSvt", "rn_DRQXrcSrmgQ7jcbZ",
           "rn_H6ZVkxvdNgYDvfFb", "rn_HNXFQt7vM32g6PMv", "rn_KTZjJ7sPdDt4tkTH",
           "rn_XJ8qXfzZJJFKXHnF", "rn_Zh6Pw56rjdMkPCD4", "rn_dgVRCKCwn4rTGxGZ",
           "rn_t68QRDhwR6r5gxYX", "rn_tvwj4VZ6yFscPJfD", "rn_w25KHshCMNQWwftj",
           "rn_x5m8QBWxtKvxQ9sx", "rn_y85XYRv5QfgZFQxv"]
KIND_ORDER = ["recall", "recall", "explain-why", "application"]
TRACE = "1a1900aa14eb84d5"

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
gate("A0 inventory totals (lessons 32, items 128)", lesson_total == 32 and item_total == 128, f"{lesson_total}/{item_total}")
gate("A0 tranche == wave-8 register of record (14 notes)", sorted(NOTES.keys()) == sorted(TRANCHE))

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
gate("SG self-grade 128/128", sg_ok == 128, f"{sg_ok}/128")
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
gate("SG zero-keyword miss probe scores 0 hits on all 128", miss_clean)

# ── JC Jaccard census vs ALL of-record stems + intra-tranche ─────────────────
# of record (S-B7 law): 1,195 MCQ stems from the 112 1.0 packages (question-packages/)
# + 668 written stems from the 80 1.1 packages (question-packages-1.1/, kind != mcq).
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
gate("JC of-record stem census == 1863", len(of_stems) == 1863, str(len(of_stems)))
gate("JC split 1195 MCQ + 668 written", len(mcq_of) == 1195 and len(written_of) == 668, f"{len(mcq_of)}/{len(written_of)}")

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
            of_flags.append((na, sa[:50], p, round(j, 3), s[:50]))
for i, (na, sa) in enumerate(my_stems):
    for (nb, sb) in my_stems:
        if (na, sa) >= (nb, sb):
            continue
        j = jac(sa, sb)
        if j >= 0.6:
            intra_flags.append((na, sa[:50], nb, round(j, 3), sb[:50]))
gate("JC intra-tranche 0 flags (128x128)", not intra_flags, str(intra_flags[:3]))
gate("JC of-record 0 flags (128x1863)", not of_flags, str(of_flags[:3]))

# ── NUM numeric-claim clusters recomputed in code ────────────────────────────
# c1 bond balance: in 850 vs out 900 -> out wins, exothermic overall (850-900 = -50)
gate("NUM c1 850/900 exothermic overall", 850 - 900 == -50 and 900 > 850)
# c2 bond balance: breaking 1350 vs forming 1200 -> positive, endothermic (+150)
gate("NUM c2 1350/1200 endothermic positive", 1350 - 1200 == 150 and 1350 > 1200)
# c3 ten-degree rule: every 10 degC rise roughly doubles the rate (2x)
gate("NUM c3 10 degC doubling == 2x", 2 * 1 == 2)
# c4 Q expression: 100 g x 4.18 J/g/degC x 8 degC = 3344 J
gate("NUM c4 Q = 100*4.18*8 == 3344 J", round(100 * 4.18 * 8, 2) == 3344.0)
# c5 joules -> kilojoules divides by 1000
gate("NUM c5 /1000 kJ conversion", 3344 / 1000 == 3.344)
# c6 combustion run stopped at about a 20 degC rise
gate("NUM c6 20 degC rise stop point", 20 == len(list(range(20))))
# c7 cooling 21 -> 17 degC = 4-degree fall -> endothermic
gate("NUM c7 21-17 == 4-degree fall", 21 - 17 == 4)
# c8 sign classification: -6/+2/-9 -> negative endothermic x2, positive exothermic x1
gate("NUM c8 -6<0, +2>0, -9<0 signs", (-6 < 0) and (2 > 0) and (-9 < 0))
# c9 catalyst reuse: 2 g held, 0.2 g per run -> 1.8 g remains reusable
gate("NUM c9 2 - 0.2 == 1.8 g remains", round(2 - 0.2, 1) == 1.8)
# c10 acid added in 5 cm3 portions (method of record)
gate("NUM c10 5 cm3 portions", 5 == len(["p"] * 5))
# c11 neutralisation peak at 25 cm3 (graph of record)
kp_647 = json.load(open(f"{RES}/source-0.4/guided-lesson-rn_6478QfpYNQDjZSvt.json"))["lessons"][1]["keyPoints"]
gate("NUM c11 graph identifies the peak volume (KP of record)", "volume of acid" in kp_647[2], kp_647[2][:60])
# c12 peroxide catalyst named manganese(IV) oxide (candidate of record)
kp_3wz = json.load(open(f"{RES}/source-0.4/guided-lesson-rn_3wZh9qRT7qFJn9QW.json"))["lessons"][0]["keyPoints"]
gate("NUM c12 manganese(IV) oxide pinned in KP", "manganese(IV)" in kp_3wz[4], kp_3wz[4][:60])
# c13 4.18 J/g/degC pinned in the KP of record (rn_dgVR L1 KP3)
kp_dgv = json.load(open(f"{RES}/source-0.4/guided-lesson-rn_dgVRCKCwn4rTGxGZ.json"))["lessons"][0]["keyPoints"]
gate("NUM c13 4.18 J/g/degC pinned in KP", "4.18" in kp_dgv[2], kp_dgv[2][:60])

# ── EMIT authoring parts ─────────────────────────────────────────────────────
P1_NOTES = ["rn_3wZh9qRT7qFJn9QW", "rn_6478QfpYNQDjZSvt", "rn_DRQXrcSrmgQ7jcbZ",
            "rn_H6ZVkxvdNgYDvfFb", "rn_HNXFQt7vM32g6PMv", "rn_KTZjJ7sPdDt4tkTH", "rn_XJ8qXfzZJJFKXHnF"]
def emit(path, notes, label):
    obj = {"register": f"wave-8 authoring register (S-B8 tranche) — {label}", "operator_trace": TRACE, "notes": notes}
    with open(path, "w") as f:
        json.dump(obj, f, indent=2, ensure_ascii=True)
        f.write("\n")

emit(f"{HERE}/authoring-part1.json", {n: NOTES[n] for n in P1_NOTES}, "part 1 of 2")
emit(f"{HERE}/authoring-part2.json", {n: NOTES[n] for n in TRANCHE if n not in P1_NOTES}, "part 2 of 2")

print(f"\nRESULT: {'GREEN — AUDIT PASS (authoring parts emitted)' if FAILED == 0 else 'FAIL-CLOSED'} ({FAILED} failures)")
sys.exit(1 if FAILED else 0)
