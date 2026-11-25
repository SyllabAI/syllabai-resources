#!/usr/bin/env python3
"""P19 register gate: adjudicate the 43 enumerated candidates into filed/drops.

Filed = International-spine register density machine-checked over the enumerated
titles (the P15-P18 classify families); drops are register-level with reasons of
record (the P15-P18 drop shape). Tiers per the P17/P18 convention: T1
judgment-ready (dense or targeting a top residual), T2 small-or-thin (the
pinnacle/dr-sarah/click-ict + indigo/scinova precedent — small pools file, the
judgment reads them honestly).
"""
import json, os

HERE = os.path.dirname(os.path.abspath(__file__))
WORK = "/home/z/my-project/work/p19"
OUT = os.path.join(HERE, "register_gate.json")

cl = json.load(open(os.path.join(WORK, "classify.json")))

def up(slug):
    return cl[slug]["uploads"]

def fam(slug, k):
    return cl[slug]["families"].get(k, 0)

T1 = [
    ("igbiocomplete", "0610 x272 + 0620 x194 + 0625 x48 of 514 \u2014 the CIE sciences trio content class; targets 0610/0620/0625 tails (61/54 left + combined/co-ordinated units)"),
    ("maths-with-mohaiminul", "4MB1 x46/58 (79%) \u2014 targets maths-B 44 left"),
    ("mr-khan-ict-solutions", "0417 x72/74 (97%) \u2014 targets ict-21 30 left"),
    ("miss-tech-teacher", "0417 x73/73 (100%) \u2014 targets ict-21 30 left"),
    ("ict-with-tatchen", "0417 x48/55 (87%) + 4IT1 x1 \u2014 dual ICT register; targets ict-21 30 + ict-17 109 left"),
    ("rapid-revision-with-shayan", "0452 x127 + 0455 x31 of 275 \u2014 the accounting CONTENT class; targets accounting-25 74 + econ-25 75 left"),
    ("the-visible-hand", "9708 x78 + 0455 x59 of 156 \u2014 the econ theory class; targets a-level-econ-23 40 + econ-25 75 + econ-20 52 left"),
    ("muzammil-ameer-acma", "9609 x59 + 0452 x10 + 0450 x9 of 140 \u2014 the CIE business/accounting multi; targets a-level-business-23 44 left"),
    ("saifullah-ajaz", "9609 x33 + 0450 x28 of 149 \u2014 dual CIE business register; targets business-23 44 + business-25 27 left"),
    ("bookkeepers-journal", "0452 x49/68 (72%) \u2014 targets accounting-25 74 left"),
    ("your-igcse-tutors", "0455 x34 + 0606 x14 + 0452 x5 of 64 \u2014 multi International; targets econ-20 52 + further-25 19 left"),
    ("igcse-study-buddy", "0620 x43 + 0610 x35 + 0625 x11 of 92 (97% International) \u2014 sciences trio; targets chem-19 61 + bio tails"),
    ("ginger-mathematician", "4MA1 x159 + 0607 x52 of 665 \u2014 resurfaced p15-swept WITH disclosure; targets 4MA1-H 100 + 4MA1-F 95 + 0607 43 left"),
    ("sciencewithchun", "0654 x14/16 (88%) \u2014 the co-ordinated class; targets co-ordinated-23 64 + combined 54 left"),
    ("the-physics-examiner", "WPH x10/11 (91%) \u2014 IAL physics content; targets ial-phys 102 left"),
    ("education-for-success", "0680 x64 + 4MA1 x14 of 1783 \u2014 the 0680 CONTENT class (64 absolute); targets EM-25 91 left"),
    ("edubbey", "0417 x81 + 0625 x45 + 0455 x37 of 636 \u2014 the multi International class; targets ict-21 30 + physics/econ tails"),
]
T2 = [
    ("precool-skillz", "0417 x31 + 0625 x26 + 0620 x25 + 0455 x11 of 195 (multi 47%) \u2014 dual ICT + sciences + econ"),
    ("save-my-exams", "4MA1 x57 + 0625 x29 + 0620 x26 + 0610 x20 + 0475 x15 of 786 (mixed-board, NT x122 dominant \u2014 disclosed)"),
    ("accounting-celebrity", "0452 x44/635 (44 absolute; 7% ratio disclosed) \u2014 targets accounting-25 74 left"),
    ("revwise", "Ed-IGCSE sciences x15 + 0620 x9 + 0610 x8 of 134 (mixed NT x34 \u2014 disclosed)"),
    ("benzakademi", "8291 x13/44 (30%) \u2014 targets EM-20 64 left; language/register read stays with the judgment"),
    ("academic-plus", "4BS1 x10 + 9609 x1 of 467 (thin-multi disclosed; the indigo T2 precedent)"),
    ("easy-edu", "4MB1 x4/5 \u2014 micro (the P17 mr-quakers precedent)"),
    ("the-revision-notebook", "9609 x3/3 \u2014 micro 100% (the P17 mr-quakers precedent)"),
]
DROPS = [
    ("1st-class-maths", "0 International-spine tokens across 333 uploads (session x28 + NT x32 generic) \u2014 re-drop consistent with the P18 gate; priorDrop carried in the pool provenance"),
    ("the-gcse-maths-tutor", "0 International families across 518 uploads \u2014 UK GCSE 1MA1 register (the corbettmaths exclusion class)"),
    ("science-shorts", "NT x122 dominant, International topics x2 of 415 \u2014 re-drop consistent with the P17 gate (AQA register)"),
    ("henry-brand", "0 International families across 232 uploads \u2014 re-drop consistent with the P17 gate (0 geography tokens)"),
    ("the-a-level-english-guide", "0 8291 tokens across 134 uploads (0500 x1 thin) \u2014 re-drop consistent with the P18 gate (register-suspect confirmed)"),
    ("internet-geography", "0 0460/4GE1 tokens across 285 uploads \u2014 UK geography register despite the name (register-suspect confirmed)"),
    ("ict-computer-tution-class", "0417+4IT1 x2 of 628 (session x72 generic) \u2014 the name promises Edexcel, the titles do not carry it (register-suspect confirmed)"),
    ("ammar-samana", "0 International families across 794 uploads (session x269 generic walkthrough tokens) \u2014 code-less titles cannot bind at judgment (the P18 0580 law)"),
    ("jensenmath", "0 International families across 501 uploads \u2014 Canadian curriculum register"),
    ("justin-sung", "0 register density across 897 uploads (4PM0 x1 noise) \u2014 study-skills channel"),
    ("peekaboo-kidz", "0 register density across 1133 uploads \u2014 kids' science content"),
    ("grade-solution", "0 register density across 247 uploads (session x3)"),
    ("caitlin-jessica", "0 families across 39 uploads \u2014 the lit-21 unseen sweep hits were noise"),
    ("raiexclusive", "0 register density across 79 uploads (session x1)"),
    ("the-geography-guy", "0 families across 14 uploads \u2014 sweep noise"),
    ("mathematics-gurukul-goln", "0 International density across 321 uploads (session x8 generic)"),
    ("geographer-online", "0 0460/4GE1 tokens across 88 uploads (NT x4) \u2014 the geography sweep hits were noise"),
    ("the-organic-chemistry-tutor", "0 International families across 2916 uploads (session x11 + NT x9 generic) \u2014 the wide-audience US register; the sweep hits were noise"),
    ("accounting-lecture-legacy", None),  # placeholder removed below
]

# drop the placeholder (defensive; not in classify)
DROPS = [(s, r) for s, r in DROPS if r and s in cl]
# every classified pool must be adjudicated exactly once
filed = [s for s, _ in T1] + [s for s, _ in T2]
dropped = [s for s, _ in DROPS]
assert sorted(filed + dropped) == sorted(cl.keys()), (
    f"adjudication mismatch: missing={set(cl) - set(filed + dropped)}, extra={set(filed + dropped) - set(cl)}")

gate = {
    "schema": "syllabai.p19-register-gate/1",
    "utc": "2026-11-25",
    "resolved": f"43/43 identity gate (externalId + og:title agree)",
    "enumerated": 43,
    "filed": filed,
    "tiers": {
        "T1-judgment-ready": [f"{s} ({n})" for s, n in T1],
        "T2-small-or-thin": [f"{s} ({n})" for s, n in T2],
    },
    "drops": [{"slug": s, "reason": r} for s, r in DROPS],
    "dropPolicy": "re-sweepable next lane; the drops are register-level, not overlap-level; nothing silently dropped",
}
json.dump(gate, open(OUT, "w"), indent=1)
open(OUT, "a").write("\n")
print(f"gate: {len(filed)} filed ({len(T1)} T1 + {len(T2)} T2) + {len(dropped)} drops of {len(cl)} classified")
