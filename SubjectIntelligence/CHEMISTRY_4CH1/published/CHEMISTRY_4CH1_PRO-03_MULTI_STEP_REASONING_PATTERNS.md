---
sib_protocol: SIB-1.0
artifact_id: PRO-03
artifact_version: 1.1
subject: Chemistry
qualification: International GCSE
specification: 4CH1
curriculum_version: "2017"

research_family: problem_solving_intelligence
applicability: REQUIRED

temporal_scope:
  current: true
  legacy: false

source_scope:
  specification: true
  textbook: true
  question_papers: true
  mark_schemes: true
  examiner_reports: false
  supplementary: false

# lifecycle: GENERATED -> QA_PASSED -> STAGED
status: PUBLISHED
generated_by: zai_agent
generated_at: 2026-10-29

provenance:
  source_manifest: "SRC-QPMS-4CH1"
  generation_run_id: "SIB-CHEMISTRY_4CH1-RUN-019"
  generator:
    provider: "z.ai"
    model: "GLM"
    agent_version: "SIB-GEN-r0"
  source_revisions:
    syllabai: "357ace0a230f5e0095ad230320af587dca6bb71f"
    syllabai_pastpapers: "e4c1960be234beb0406b9218f4fbb2a95b1e3f28"
    syllabai_resources: "e3d648a195a13e3713b4b14a3095518e4a0d24e5"
---

# PRO-03 — Multi-Step Reasoning Patterns

## Purpose

This artifact catalogues the multi-step reasoning patterns of record in 4CH1:
part-chained questions that feed answers forward, show-that verify steps that
anchor later calculation, sign-chained data through a problem family, linked
two-point explanation marking, explicit inference chains in the book prose, and
the examiner's own precision feedback on reasoning — for sources SRC-QPMS-4CH1,
SRC-BOOK-4CH1-SB1, SRC-TL-4CH1 and SRC-SPEC-4CH1. Claims ride only on this
artifact's own bounded pack excerpts. Canonical planes are untouched.

## Scope

**Covers:** use-your-answer chaining; show-that anchoring; data chaining across
a question family; linked-points explanation patterns; book-side inference
chains; precision rules for carried figures; exemplar commentary on reasoning
quality.

**Out of scope:** the type-to-method mapping (PRO-02) and decision points
(PRO-04).

## Executive Summary

Multi-step reasoning is engineered into the papers: a calorimetry item asks
candidates to "show that" the heat change is about 2400 J and then to "use your
answer to part (b)" for the enthalpy change — a verify-then-chain design in
which the published skeleton carries the steps (moles, divide Q by n, convert J
to kJ, sign and precision). A question family chains its data three deep — mass
produced, mass of water, then x from the mole ratio — each part's answer
feeding the next. The mark schemes name the pattern explicitly: explanations
that "link" two points, with each link marked. The book teaches the same
inference chains in prose (moles counted, therefore twice as many atoms) and
polices precision across the chain (carried figures to matching significant
figures). The exemplars booklet adds the examiner's own diagnosis of reasoning
precision — ions, not molecules, in dilute solution.

## Main Analysis

### PRO-015 — Show-that anchoring

**Claim:** show-that items anchor a later calculation by verifying an
intermediate result first — the reasoning chain is built into the question
design.
**Evidence:** the calorimetry item demands "Show that the heat energy change,
Q, is about 2400 J" with the mass and c values printed (SRC-QPMS-4CH1,
2019-06/4CH1-1C/questions.md lines 935-949); the copper-sulfate item demands
"Show that the maximum possible mass of CuSO4.5H2O crystals tha"t can form,
feeding the later yield part (SRC-QPMS-4CH1,
2019-06/4CH1-1C/questions.md lines 1269-1283). Temporal scope: CURRENT —
AUTHORITATIVE.

### PRO-016 — Use-your-answer chaining

**Claim:** the papers chain parts explicitly: a later part consumes an earlier
part's answer as its input.
**Evidence:** the enthalpy item instructs "Use your answer to part (b) to
calculate the enthalpy change, ∆H, in kilojoules per mole of ammonium nitrate"
(SRC-QPMS-4CH1, 2019-06/4CH1-1C/questions.md lines 967-981); its published
skeleton then carries the chained steps — the moles of ammonium nitrate, the
division of Q by n, the conversion of joules to kilojoules, and the required
sign and significant figures — as one scored route. Temporal scope: CURRENT —
AUTHORITATIVE.

### PRO-017 — Verify-then-use chaining inside one question

**Claim:** the chaining design compounds within a single question: the verified
intermediate becomes the named input of the next part, so reasoning accumulates
rather than restarting.
**Evidence:** the calorimetry chain verifies Q first (SRC-QPMS-4CH1,
2019-06/4CH1-1C/questions.md lines 935-949) and the next part opens with the
instruction to use that answer for the molar enthalpy change
(SRC-QPMS-4CH1, 2019-06/4CH1-1C/questions.md lines 967-981). Temporal scope:
CURRENT — AUTHORITATIVE.

### PRO-018 — Linked-points explanation marking

**Claim:** the mark schemes publish the reasoning pattern itself: explanations
must link the named points, and each link carries its own mark.
**Evidence:** the rates explanation skeleton opens "An explanation that links
the following points:" with the concentration fall as the first linked point and
the collision consequence as the second (SRC-QPMS-4CH1,
2019-06/4CH1-1C/questions.md lines 1117-1130). Temporal scope: CURRENT —
AUTHORITATIVE.
### PRO-019 — Inference chains in the book prose

**Claim:** the book models multi-step inference explicitly in prose — count the
moles, therefore the atom ratio, therefore the formula.
**Evidence:** the formula-determination section reasons "From calculating the
number of moles of Cu and O we can see that there are twice as many moles of Cu
and therefore there must be twice as many Cu atom"s in the formula
(SRC-BOOK-4CH1-SB1, edexcel_igcse_chemistry_chunks_v3.jsonl line 171); the same
chain polices precision across steps — carried figures kept to the original two
significant figures (SRC-BOOK-4CH1-SB1,
edexcel_igcse_chemistry_chunks_v3.jsonl line 180). Temporal scope: CURRENT —
AUTHORITATIVE.

### PRO-020 — Examiner precision on reasoning language

**Claim:** the exemplar commentary diagnoses reasoning precision at the
chemistry-language level — what exists in solution changes what the reasoning
may claim.
**Evidence:** the examiner comment on the acid part states that "In dilute
solution HCl exists as ions, not molecules" and that the answer must also state
what the ions are (SRC-TL-4CH1,
international-gcse-chemistry-exemplars-commentary.pdf p 8); the booklet pairs
student responses A and B so the reasoning difference is visible
(SRC-TL-4CH1, international-gcse-chemistry-exemplars-commentary.pdf p 9).
Temporal scope: CURRENT — AUTHORITATIVE.

### PRO-051 — The three-stage computation scaffold inside show-that items

**Claim:** the show-that item publishes its own internal scaffold as bullet steps — the temperature change, the substitution into the printed equation, and the evaluation — before any arithmetic appears, and the worked example then shows the sign-reversed substitution being carried through the chain. The scaffold makes the reasoning order inspectable: each stage is nameable before it is performed.
**Evidence:** the scheme lists "calculation of temperature change", "substitution into Q = mcΔT" and "evaluation" before the worked lines "M1 14.2 – 20.0 = (-)5.8" and "M2 Q = 100 × 4.18 × (‒)5.8" (SRC-QPMS-4CH1, 2019-06/4CH1-1C/questions.md lines 935-949).
Temporal scope: CURRENT — AUTHORITATIVE.

### PRO-052 — The fail-closed reagent gate in test-method chains

**Claim:** the two-step ion-test method carries a fail-closed gate on its first step: the reagent must be the named one (with its own alternates), and any incorrect reagent voids the method mark outright — the observation point cannot rescue a wrong reagent. The chain's epistemics are therefore ordered: reagent identity gates the method, and the observation earns only inside a valid method.
**Evidence:** the scheme prints "M1 add sodium hydroxide (to the copper(II) sulfate ALLOW potassium" "solution) hydroxide or aqueous ammonia" with the gate "No M1 if any incorrect" "reagent added", and "M2 blue precipitate (forms)" with "IGNORE qualifiers e.g." (SRC-QPMS-4CH1, 2023-06/4CH1-2C/questions.md lines 491-505).
Temporal scope: CURRENT — AUTHORITATIVE.

### PRO-053 — Cross-point crediting inside one linked chain

**Claim:** a linked chain can carry a spanning formulation that earns two points at once: the collision-rate explanation prints a consolidated clause whose wording covers both the frequency point and the next point, and the scheme says so explicitly. The chain is therefore not strictly additive at the sentence level — one well-formed statement can discharge two chain points, and the scheme names the overlap.
**Evidence:** the scheme opens "An explanation that links the following points:" and prints "M2 therefore there are fewer (successful) collisions" with the spanning note "collision rate scores" "M2 and M3" (SRC-QPMS-4CH1, 2019-06/4CH1-1C/questions.md lines 1116-1130).
Temporal scope: CURRENT — AUTHORITATIVE.


## Evidence / Source Basis

Primary evidence: SRC-QPMS-4CH1 (2019-06 Paper 1C chained items and skeletons
with paper identity preserved via the pack file path) and SRC-BOOK-4CH1-SB1
(inference-chain chunks at line+chunk-id locators). Supplementary: SRC-TL-4CH1
exemplars-commentary pages; SRC-SPEC-4CH1 command-word page for the show-that
definition. Bounded excerpts with locators preserved; caps enforced by the pack
builder.

## Limitations / Coverage Gaps

The patterns catalogued are those in this pack's excerpt windows for one paper
plus the book chunks captured; other sessions' chaining designs are neither
enumerated nor denied. Mark-scheme skeletons are cited as published pattern
statements only; no mark_points plane data is consumed or written. No examiner
sentiment is synthesized from mark schemes (the exemplar commentary is official
examiner text consumed as ER-class evidence from the TL corpus). OCR-era quirks
are quoted as parsed or paraphrased, never repaired. No canonical planes were
written.

## Research Status

GENERATED under SIB-CHEMISTRY_4CH1-RUN-006 (BL-008 pass 6) from this artifact's
evidence pack alone; validator of record tools/sib @ 357ace0a; claim QA r3 binds
every citation to a pack excerpt. Deepened under SIB-CHEMISTRY_4CH1-RUN-019 (D3 tranche 3): +3 records (PRO-051..053), zero-append mining of the carried pack of record; every quote self-bound to raw excerpt text before the official gate; claim QA re-bound all citations. Research artifact — evidence-backed, not
canonical educational truth.
