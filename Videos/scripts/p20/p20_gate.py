#!/usr/bin/env python3
"""P20 register gate: adjudicate the 56 enumerated candidates into filed/drops.

Filed = International-spine register density machine-checked over the enumerated
titles (the P15-P19 classify families + the P20 amendments: the 9700/9701/9706/
9709/9618/0606-4037 register families and the CIE/CAIE board-token family);
drops are register-level with reasons of record (the P15-P19 drop shape). Tiers
per the P17/P18/P19 convention: T1 judgment-ready (dense or targeting a top
residual), T2 small-or-thin (the pinnacle/mr-quakers/indigo/accounting-celebrity
precedent — small pools file, the judgment reads them honestly).
"""
import json, os

HERE = os.path.dirname(os.path.abspath(__file__))
WORK = "/home/z/my-project/work/p20"
OUT = os.path.join(HERE, "register_gate.json")

cl = json.load(open(os.path.join(WORK, "classify.json")))

T1 = [
    ("otterbiotutor", "9700 x246/276 (89%) — the CIE A-level biology lesson-series class ('Cambridge AS A Level Biology, 9700'); targets a-level-bio-25 31 left"),
    ("ptet-chemistry", "9701 x265 + 0620 x179 + 0653 x160 of 929 — the multi CIE chemistry + combined-science find (the 0653 corrected-code cluster, p19-swept-uninventoried disclosure); NT x150 disclosed; targets combined-23 49+42+24, chem-19 61, chem-25 29 left"),
    ("study-with-prashna", "9706 x337/404 (83%) — explicit 9706 session walkthroughs ('A Level Accounting May June 2026 Paper 12 9706/12'); targets accounting-21 17 left"),
    ("adam-viceroy", "9706 x208 + 0452 x67 of 381 — dual CIE accounting register ('O level Accounting 7707 & 0452' — the disclosed 7707 dual exempt per the P14 precedence law); targets accounting-25 71 + accounting-21 17 left"),
    ("miss-natalie-chemistry", "WCH x79 + 0620 x54 + Ed-IGCSE sciences x54 of 147 — the WCH unit-content find ('10B Halogenoalkanes - Edexcel IAS Chemistry (Unit 2)'); targets ial-chem 164 + chem-19 61 left (p15-swept-uninventoried disclosure)"),
    ("mathlete-by-saad", "0606 x117 + 9709 x30 of 1,059 — the add-maths register find ('IGCSE ADDMATHS - Vectors ... Relative Velocity'); the 4MA1 x78 family read re-adjudicated as the generic IGCSE/O-Level 0580 class per the ginger law (disclosed false density); targets further-25 19 + pure-2 left"),
    ("cswithmrg", "9618 x64 + the '0478/0984 iGCSE Computer Science Unit 7 Pseudocode' series of 143 — dual CIE CS register; targets CS-19 20 left (the 0478 course of the spine is fully mapped — the 0478 subset rides honestly)"),
    ("haguin-school", "9618 x114/120 (95%) — the 9618 paper-walkthrough class; targets CS-19 20 left"),
    ("mr-lee-business-econ", "0455 x72/158 — the IGCSE economics chapter class ('IGCSE Economics Chapter 4.1 ... Updated for 2027 specification'); NT x26 disclosed; targets econ-20 28 left (p15-swept-uninventoried disclosure)"),
    ("mr-mathew", "0680 x41 + 0610 x33 + 0460 x33 of 172 — the multi EM/bio/geo past-paper class; targets geo-25 48 + geo-20 37 + EM-25 28 left (p15-swept-uninventoried disclosure)"),
    ("pla-academy-igcse-and-a-level-buddy", "0625 x55 + Ed-IGCSE x16 + WPH x9 of 138 — Edexcel physics unit content ('2.1 Fluids: Unit 1 mechanics and materials: Edexcel IAL Physics', 'Edexcel IGCSE Physics (9-1) Unit 6 (4PH1)'); targets physics-19 18 + DA-17-phys 19 + WPH 102 left (p15-swept-uninventoried x20 disclosure)"),
    ("refactor-lab", "0606 x71 + 9709 x22 of 196 (36%) — explicit 'CIE | Add Math | 0606 | 4037' session walkthroughs (the disclosed 4024 O-Level dual); targets further-25 19 left"),
    ("mathprep-with-ahmad-bilal", "9709 x223/856 (26%) — the CAIE 9709 session-solution class; targets pure-2 32 combined left (P1-dominant disclosed)"),
    ("salihath-syed-basheer", "0450 x44 + 9609 x24 of 93 (73% International) — dual CIE business register ('CAMBRIDGE AS BUSINESS HUMAN RESOURCE MANAGEMENT #9609'); targets business-25 22 + business-23 29 left"),
    ("edex-world", "9706 x40/102 (39%) — the 'CIE Past Paper Discussion (9706 - ...)' class; the 'Accounting for IGCSE - Video N' remainder carries no 0452 code (the ammar-samana law, disclosed); targets accounting-21 17 left (p17-swept-uninventoried disclosure)"),
    ("biochemlogy", "9700 x92/122 (75%) — the A2 9700 chapter class; targets a-level-bio-25 31 left"),
]
T2 = [
    ("umara-ratnayake", "4IT1 x15 + 0417 x14 of 180 — dual ICT practical register ('EDEXCEL IGCSE ICT 9-1 - 2021 DATABASE'); targets ict-17 109 left"),
    ("aslaug-eggertsdottir", "0417 x9 + 4IT1 x2 of 30 — the Edexcel ICT practical-exam class ('Practical Edexcel IGCSE ICT Access Database Exam'); targets ict-17 109 left"),
    ("s-q", "0417 x16/40 (40%) — the iGCSE ICT spreadsheet-task class; targets ict-21 19 + ict-17 109 left"),
    ("the-lightup-hub", "0475 lit x18 (unseen poetry x10) of 1,120 (1.6% thin — UK GCSE 'GRADE 9' branding disclosed) — the unseen-poetry craft class; targets lit-21 unseen 96 left"),
    ("e-geo", "0460 x6/73 (8%) — the 0460 case-study class ('CASE STUDY_CAUSES OF A VOLCANIC ERUPTION_IGCSE GEOGRAPHY_0460'); targets geo-25 48 + geo-20 37 left (the accounting-celebrity thin precedent)"),
    ("ilm-online-academy", "0580 x25 (explicit 'Cambridge IGCSE Maths 0580') + 0620 x22 + 0625 x14 of 94 — multi CIE; targets maths-25-ext 24 + maths-25-core 16 + chem-19 61 left (the 4MA1 x25 family read as the 0580 register per the ginger law, disclosed)"),
    ("y-mx-c", "0606 x86/873 (10%) — the relative-velocity vectors series ('IGCSE ADDMATHS - Vectors related with velocity'); targets further-25 19 left (86 absolute, thin ratio disclosed)"),
    ("miss-estruch-biology", "CIE token x18 + 9700-bio x7 of 1,539, NT x185 dominant disclosed — the 'ENTIRE Topic 12-19 for CIE A-level 2027' series (63 CIE-mention titles per title-grep, the revwise mixed-NT precedent); targets a-level-bio-25 31 left"),
    ("wimzee-cambridge-academy", "0620 x10 + 0610 x8 of 44 — micro multi CIE (the mr-quakers precedent)"),
    ("mysecondteacher", "the numbered Cambridge A-Level lesson series (0625 x51 + 0610 x17 + 0620 x17 of 126) — multi CIE structured lessons; targets physics/chem/bio tails"),
    ("the-future-professionals", "9706 x14 + 0610 x7 + 9609 x6 of 124 — thin-multi (the indigo precedent)"),
    ("chembase-school-of-chemistry", "WCH x8 + 9701 x3 of 64 — thin WCH/A-level chemistry class"),
    ("sayo-enoch-aluko", "0606 x22 + NT x48 dominant of 107 — mixed-board disclosed (the revwise precedent); targets further-25 19 left"),
    ("hendrik-academy", "9709 x34/338 (10%) with the explicit 9709/21-22 'Paper 2 Pure Mathematics 2' subset; IBDP-dominant disclosed — targets pure-2 32 combined left"),
    ("walter-maths-tutoring", "9709 x21 + the 9231 further-maths solved-paper series of 121 — targets pure-2 (P1-dominant disclosed)"),
    ("maths-camp", "9709 x15/217 — the 9709 P1 everything-guides"),
    ("ishan", "9708 x6/7 micro (the mr-quakers precedent) — targets a-level-econ-23 40 left"),
    ("biology-box", "the 'International GCSE Biology (Edexcel) Lesson N' series x7/73 — micro Edexcel International bio; targets DA-17-bio 34 + bio-mod-24-u2 41 left"),
    ("the-cs-classroom", "9618 x14 + NT x27 dominant of 145 — mixed register disclosed; targets CS-19 20 left"),
]
DROPS = [
    ("henry-brand", "0 geography/International tokens across 232 uploads (session x37 paper-advice noise) — re-drop consistent with the p17/p19 gates (priorDrop carried in provenance); the 4GE1 sweep hits were advice content"),
    ("keducate", "NT x86/131 dominant (AQA GCSE geography) — re-drop; the 4GE1 sweep hits were the AQA register despite the geo cluster"),
    ("adora-yin", "0 register density across 46 uploads (NT x5 noise) — the study-tips register; the lit-unseen sweep hits were noise (the caitlin-jessica class)"),
    ("brendan-ng", "0 honest tokens across 151 uploads — the bulk is the Singapore O-Level Sec 3/4 '#olevel' hashtag register; the 'CAMBRIDGE UNI GRADUATE' A-level explainers carry no spine code (register-suspect confirmed, the ammar-samana law)"),
    ("minity-maths", "0 register tokens across 538 uploads (session x15 generic) — code-less generic maths (the ammar-samana law)"),
    ("onmaths", "0 International families across 2,030 uploads — the UK GCSE 1MA1 predicted-paper register (the corbettmaths class)"),
    ("ukmathsteacher", "4PM0 x75 (no spine course) + NT x140 dominant across 1,132 — mixed decision-maths A-level register; the 4MA1 x14 is thin (1.2%)"),
    ("infinity-math-center-myanmar", "4PM0 x34/71 — the further-pure register without a spine course (the 4PM0 class); NT x9"),
    ("accounting-stuff", "0 register tokens across 400 uploads — the generic accounting guide (the OCT wide-audience class)"),
    ("moomoomath-and-science", "0 register density across 3,670 uploads — the US wide-audience register (the OCT class)"),
    ("fuseschool-global-education", "0 register density across 986 uploads — generic GCSE mixed (the corbettmaths class)"),
    ("explainitychannel", "0 register density across 85 uploads — the German explainer register"),
    ("ace-tutors", "0 register tokens across 46 uploads — generic probability explainers"),
    ("accounting-basics", "0 register tokens across 64 uploads — generic accounting basics"),
    ("science-workshop", "0 register tokens across 111 uploads — generic GCSE chemistry"),
    ("simple-geography", "0 register tokens across 17 uploads — generic tectonics explainer"),
    ("eduelfie", "0 register tokens across 258 uploads — code-less '16A - Matrices' series"),
    ("counttuts", "0 register density across 299 uploads (session x7 generic)"),
    ("intelletics-institute", "0680 x2/168 — the Indian CET-11 admission register (the Anna-university GE8291 false-density class)"),
    ("commerce-lecturer-online", "0452 x7/231 (3%) — below the thin bar (the accounting-celebrity 7% precedent); the CIE-token x25 titles carry no 0452 code"),
    ("mohammad-umar-memon-md", "9700 x10/176 (5.7%) — below the thin bar; the topical-past-paper subset is sparse"),
]

# every classified pool must be adjudicated exactly once
filed = [s for s, _ in T1] + [s for s, _ in T2]
dropped = [s for s, _ in DROPS]
assert sorted(filed + dropped) == sorted(cl.keys()), (
    f"adjudication mismatch: missing={set(cl) - set(filed + dropped)}, extra={set(filed + dropped) - set(cl)}")

gate = {
    "schema": "syllabai.p20-register-gate/1",
    "utc": "2026-11-26",
    "resolved": "56/56 identity gate (externalId + og:title agree)",
    "enumerated": 56,
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
