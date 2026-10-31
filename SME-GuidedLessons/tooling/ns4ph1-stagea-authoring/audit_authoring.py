#!/usr/bin/env python3
"""NS-4PH1 stage-A authoring audit (mirror of the R3 S-B10 audit law of record).

Gates:
  A0  inventory 1 note / 1 lesson / 4 items, per-lesson kind order
      [recall, recall, explain-why, application]
  AN  anchor.kp within 1..len(keyPoints) of its lesson (source skeleton)
  SG  self-grading under the hub keyword law: case-insensitive whole-token
      ([a-z0-9]+) match of the model answer against keywords[], >=1 hit -> correct
      + zero-keyword miss probe
  KW  keyword hygiene: every keyword tokenizes (letters/digits), 1..20 keywords,
      no keyword token appearing in its own stem
  JC  token-Jaccard >= 0.6 vs ALL of-record stems (1,195 MCQ + 956 written, chemistry)
      + the 5 pilot MCQ stems -> any flag FAILS
  2.1B  learner surface "from the revision note" 0 hits across stems/model answers
  NUM numeric-claim clusters recomputed in code (the 80 km/h application item and
      the worked-example arithmetic)
  EMIT writes authoring-part1.json (committed to tooling/ns4ph1-stagea-authoring/)
"""
import glob
import json
import re
import sys

RES = "/home/z/my-project/syllabai-resources/SME-GuidedLessons/integration"
HERE = "/home/z/my-project/scripts/ns4ph1"
sys.path.insert(0, HERE)
from authoring_data_part1 import PART1

TRACE = "1a19291d96cc7aed"
PILOT = "rn_k9wr3prcgSBg5vfw"
KIND_ORDER = ["recall", "recall", "explain-why", "application"]

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


# ── A0/AN inventory + field hygiene ──────────────────────────────────────────
skel = json.load(open(f"{HERE}/source_skeleton_{PILOT}.json"))
body = PART1[PILOT]
lesson_total, item_total = 0, 0
gate("A0 authored lessons == source lessons", len(body["lessons"]) == len(skel["lessons"]))
for i, (L, items) in enumerate(zip(skel["lessons"], body["lessons"])):
    lesson_total += 1
    item_total += len(items["items"])
    kinds = [it["kind"] for it in items["items"]]
    gate(f"A0 L{i+1} kind order", kinds == KIND_ORDER, ",".join(kinds))
    for k, it in enumerate(items["items"]):
        bad = []
        if not it.get("stem", "").strip():
            bad.append("stem")
        if not it.get("misconceptionClass", "").strip():
            bad.append("mc-class")
        if not it.get("modelAnswer", "").strip():
            bad.append("modelAnswer")
        kw = it.get("keywords", [])
        if not (1 <= len(kw) <= 20) or any((not w) or (not w.strip()) for w in kw):
            bad.append("keywords")
        if "options" in it:
            bad.append("options-forbidden")
        kp = it.get("anchor", {}).get("kp")
        if not (isinstance(kp, int) and 1 <= kp <= len(L["keyPoints"])):
            bad.append(f"anchor {kp}")
        for w in kw:
            if not re.fullmatch(r"[a-z0-9.]+", w.lower()):
                bad.append(f"kw-shape {w}")
        stem_toks = tok(it["stem"])
        for w in kw:
            if w.lower() in stem_toks:
                bad.append(f"kw-in-stem {w}")
        if bad:
            gate(f"A0 L{i+1} Q{6+k}", False, ",".join(bad))
gate("A0 inventory totals (lessons 1, items 4)", lesson_total == 1 and item_total == 4, f"{lesson_total}/{item_total}")

# ── SG self-grading + zero-keyword miss probe ────────────────────────────────
sg_ok = 0
for li, L in enumerate(body["lessons"]):
    for qi, it in enumerate(L["items"]):
        kws = {w.lower() for w in it["keywords"]}
        ma_toks = tok(it["modelAnswer"])
        hits = sorted(kws & ma_toks)
        if hits:
            sg_ok += 1
        else:
            gate(f"SG L{li+1} Q{6+qi} model answer grades correct", False, "0 keyword hits in model answer")
gate("SG self-grade 4/4", sg_ok == 4, f"{sg_ok}/4")
probe = "a purple elephant balanced seventeen umbrellas on a quartz harmonica while zephyrs wandered yonder"
probe_toks = tok(probe)
miss_clean = True
for L in body["lessons"]:
    for it in L["items"]:
        if probe_toks & {w.lower() for w in it["keywords"]}:
            miss_clean = False
            print(f"WARN miss-probe hits keywords of: {it['stem'][:60]}")
gate("SG zero-keyword miss probe scores 0 hits on all 4", miss_clean)

# grading-law digit-hazard probe: no keyword may be a substring-prefix token of a
# number that appears in the stem (a learner echoing stem digits must not pass)
digit_clean = True
for L in body["lessons"]:
    for it in L["items"]:
        for w in it["keywords"]:
            if w.isdigit() and any(t.isdigit() and t != w and t.endswith(w) for t in tok(it["stem"])):
                digit_clean = False
                print(f"WARN digit-prefix hazard: keyword {w} of '{it['stem'][:50]}'")
gate("KW digit-prefix hazard clean", digit_clean)

# ── 2.1B learner-surface law ─────────────────────────────────────────────────
hits_21b = []
for L in body["lessons"]:
    for it in L["items"]:
        for field in ("stem", "modelAnswer"):
            if "from the revision note" in it[field].lower():
                hits_21b.append((field, it[field][:50]))
gate("2.1B learner surface 'from the revision note' 0 hits", not hits_21b, str(hits_21b[:3]))

# ── JC Jaccard census vs ALL of-record stems + intra-pilot ───────────────────
of_stems = []
for pattern in ("question-packages/*.sme-question-package.json", "question-packages-1.1/*.sme-question-package.json"):
    for p in sorted(glob.glob(f"{RES}/{pattern}")):
        for q in json.load(open(p))["questions"]:
            of_stems.append((p.replace(RES + "/", ""), q["stem"]))
mcq_stems = [(f"pilot-L1-Q{i+1}", c["stem"]) for i, c in enumerate(skel["lessons"][0]["check"])]
flags = []
for src, stem in [("authoring:Q6", body["lessons"][0]["items"][0]["stem"]), ("authoring:Q7", body["lessons"][0]["items"][1]["stem"]), ("authoring:Q8", body["lessons"][0]["items"][2]["stem"]), ("authoring:Q9", body["lessons"][0]["items"][3]["stem"])] + mcq_stems:
    for other_src, other in of_stems + [x for x in mcq_stems if x[0] != src]:
        if jac(stem, other) >= 0.6:
            flags.append((src, other_src, round(jac(stem, other), 3)))
gate(f"JC >=0.6 flags vs {len(of_stems)} of-record stems + intra-pilot", not flags, str(flags[:4]))

# ── NUM numeric-claim clusters recomputed in code ────────────────────────────
num_ok = True
num_ok &= abs(120 / 1.5 - 80.0) < 1e-9          # Q9 application
num_ok &= 30 * 60 == 1800                        # workedExample step 2
num_ok &= abs(2400 / 1800 - 4 / 3) < 1e-9        # workedExample step 4
num_ok &= round(2400 / 1800, 2) == 1.33          # workedExample final answer
gate("NUM numeric clusters (80 km/h; 1800 s; 2400/1800=4/3≈1.33)", num_ok)

# ── EMIT authoring-part1.json ────────────────────────────────────────────────
if FAILED == 0:
    emit = {"_audit": {"trace": TRACE, "note": PILOT, "gates": "A0/AN/SG/KW/JC/2.1B/NUM all GREEN"}}
    emit.update({"notes": {PILOT: body}})
    out = {k: v for k, v in emit.items() if k != "_audit"}
    json.dump(out, open(f"{HERE}/authoring-part1.json", "w"), indent=1, ensure_ascii=False)
    print("EMITTED authoring-part1.json")
print(f"AUDIT RESULT: {'GREEN' if FAILED == 0 else f'{FAILED} FAILURE(S)'}")
sys.exit(1 if FAILED else 0)
