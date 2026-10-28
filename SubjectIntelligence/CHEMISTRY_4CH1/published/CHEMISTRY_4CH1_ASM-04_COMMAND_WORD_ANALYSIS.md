---
sib_protocol: SIB-1.0
artifact_id: ASM-04
artifact_version: 1.1
subject: Chemistry
qualification: International GCSE
specification: 4CH1
curriculum_version: "2017"

research_family: assessment_intelligence
applicability: REQUIRED

temporal_scope:
  current: true
  legacy: false

source_scope:
  specification: true
  textbook: false
  question_papers: true
  mark_schemes: true
  examiner_reports: false
  supplementary: true

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

# ASM-04 — Command Word Analysis

## Purpose

This artifact analyses the command words that drive the 4CH1 papers as parsed in the
official exam corpus of record (SRC-QPMS-4CH1): what State, Explain, Calculate,
Describe, Give, Complete, Draw and Suggest each demand, and how the embedded
mark-scheme text responds to each. Command-word literacy is the candidate-side key
that unlocks the archetypes catalogued in ASM-03; this artifact grounds that key in
the corpus itself. Every claim is carried on a bounded, locator-addressed excerpt from
the run's evidence pack. Research artifact; canonical planes untouched.

## Scope

**Covers:** the observable command-word inventory of the parsed papers and the
mark-scheme shape each command elicits.

**Grounding:** SRC-QPMS-4CH1 (official paper extractions with embedded mark-scheme
text — the 2019-06 2C and 1CR papers of the pack supply the anchors).

**Out of scope:** command-word frequency counts (pack spreads for that live in
ASM-05/ASM-09 ground), examiner commentary on command words (EXM family).

## Executive Summary

The parsed papers run a compact command lexicon. State elicits single facts or
observations marked against tight accepted sets; Explain dominates the reasoning load
and almost always buys a linked-point mark scheme (M1/M2 with dependency notes);
Calculate is always a working problem with step bullets; Describe demands a process
or arrangement narrative with points-based marking; Give/Name/Complete/Draw are
production commands with completeness marking; and Suggest opens controlled
speculative reasoning where the mark scheme rewards a defensible mechanism. The
command word, not the topic, predicts the mark-scheme shape — which is why command-word
drilling transfers across the whole specification.

## Main Analysis

### ASM-019 — Explain: the dominant reasoning command

**Claim:** Explain items require a causal chain, and their mark schemes are built as
linked point pairs or triples rather than single accepted answers.
**Evidence:** "Explain what is meant by the term dynamic equilibrium." is marked "An
explanation that links together the following two points" (SRC-QPMS-4CH1, 2019-06/4CH1-2C/questions.md lines 571-585); "Explain, in terms of bonds broken and
bonds made, why this reaction is exothermic." runs the same two-point law
(SRC-QPMS-4CH1, 2019-06/4CH1-2C/questions.md lines 361-375); the safety item "Explain
a safety precaution that should be taken when doing this experiment." offers
alternative linked pairs (the parsed excerpt) (SRC-QPMS-4CH1, 2019-06/4CH1-2C/questions.md lines 701-715).
**Design reading:** Explain is where marks are lost by one-legged answers; the
mark-scheme machinery (linked pairs, alternatives) shows the examiner wants
mechanism-plus-consequence, not assertion.
Temporal scope: CURRENT — AUTHORITATIVE.

### ASM-020 — State: the single-fact command

**Claim:** State items demand one fact, one observation or a short list, marked
against a closed accepted set.
**Evidence:** "State two variables the student should control to make sure her results
are valid." (SRC-QPMS-4CH1, 2019-06/4CH1-2C/questions.md lines 130-144); "State the
colour change that occurs in the potassium dichromate(VI) during this reaction." with
mark scheme "(from) orange (to) green" (SRC-QPMS-4CH1, 2019-06/4CH1-2C/questions.md lines 523-537).
**Design reading:** State rewards precise observation language — colour names,
specific variables — and the mark schemes show near-zero tolerance for vagueness.
Temporal scope: CURRENT — AUTHORITATIVE.

### ASM-021 — Calculate: the working command

**Claim:** Calculate items are quantitative, printed with Mr values or conversion
data, and marked step-wise with explicit dependency and ECF notes.
**Evidence:** "Calculate the relative atomic mass of this sample of chlorine" over the
isotope-percentage stem (SRC-QPMS-4CH1, 2019-06/4CH1-2C/questions.md lines 68-82);
"Calculate the amount, in moles, of chlorine gas produced." with "M1 60 ÷ 24 000, M2
0.0025 (mol)" (SRC-QPMS-4CH1, 2019-06/4CH1-2C/questions.md lines 721-735); the
enthalpy item adds "Include a sign in your answer." (SRC-QPMS-4CH1, 2019-06/4CH1-2C/questions.md lines 337-351).
**Design reading:** the moles item's step marks and the concentration item's "Mark
CSQ on (b)(ii)" note (SRC-QPMS-4CH1, 2019-06/4CH1-2C/questions.md lines 746-760)
show consequential marking chains that candidates can exploit by keeping working
visible.
Temporal scope: CURRENT — AUTHORITATIVE.

### ASM-022 — Describe: the narrative command

**Claim:** Describe items demand an arrangement, process or method narrative, marked
on the points the narrative must contain.
**Evidence:** "Describe the arrangement and the movement of particles in a solid." is
marked "A description that refers to three of the following points" (SRC-QPMS-4CH1, 2019-06/4CH1-1CR/questions.md lines 44-58); the copper(II) sulfate water test in the
same family asks candidates to describe reagent-then-result
.
**Design reading:** Describe differs from Explain in what buys the mark — sufficient
correct features, not causal linking; the "three of the following" form also shows
choice built into the tariff.
Temporal scope: CURRENT — AUTHORITATIVE.

### ASM-023 — Give/Complete/Draw: the production commands

**Claim:** production commands (Give, Complete, Draw, Name) ask candidates to
manufacture an answer artifact — a value, a formula, a balanced equation, a diagram —
and their mark schemes mark completeness and dependency.
**Evidence:** "Give the mass number of this atom." marked "> 13" ; the parsed excerpt with "M1 for both products correct, M2 for correctly
balanced" ; "Draw an
energy level diagram for the reaction between N2H4 and H2O2" (SRC-QPMS-4CH1, 2019-06/4CH1-2C/questions.md lines 378-392).
**Design reading:** balanced-equation items split content (M1) from balancing (M2) —
a candidate who writes correct products but wrong coefficients banks half.
Temporal scope: CURRENT — AUTHORITATIVE.

### ASM-024 — Suggest: the controlled-speculation command

**Claim:** Suggest items license plausible reasoning beyond strict recall, and the
mark schemes reward a defensible mechanism rather than a canonical fact.
**Evidence:** "Suggest why the new equilibrium mixture is actually darker" — where the
candidate must reconcile the shifted equilibrium with the observation (SRC-QPMS-4CH1, 2019-06/4CH1-2C/questions.md lines 637-651).
**Design reading:** Suggest signals that several defensible answers exist; candidates
trained only for closed recall lose confidence here, so targeted practice on
mechanism-first speculation pays.
Temporal scope: CURRENT — AUTHORITATIVE.

### ASM-070 — Suggest examined as a bounded numeric range

**Claim:** the Suggest command operates over a printed acceptance interval: a suggested pH earns the mark for any value or range inside eleven-to-fourteen, so the command's speculative demand is bounded by a numeric window rather than a single answer. The scheme prints the boundary as the whole mark scheme.
**Evidence:** the scheme answers "Suggest a value for the pH of the solution." with "any value or range between 11 and 14" (SRC-QPMS-4CH1, 2019-06/4CH1-1CR/questions.md lines 102-116).
Temporal scope: CURRENT — AUTHORITATIVE.

### ASM-071 — Describe examined as a pool of points with packed alternates

**Claim:** the Describe command over particle arrangements is marked as a pool — any three of the printed points — and each point carries its own allowances: close together tolerates tightly packed or touching, regularly arranged tolerates a lattice. The command's narrative demand is therefore operationalised as selectable points with per-point synonym sets.
**Evidence:** the scheme prints "A description that refers to three of" "the following points" with "M1 (particles) close together ALLOW tightly" "packed/ touching" and "M2 (particles) regularly arranged ALLOW" "arranged in a" "lattice" (SRC-QPMS-4CH1, 2019-06/4CH1-1CR/questions.md lines 44-58).
Temporal scope: CURRENT — AUTHORITATIVE.

### ASM-072 — The describe-or-draw hybrid with a conditional scoring rule

**Claim:** the method-description item permits a diagram and then conditions the scoring on the diagram's content: if the drawn solvent level sits above the pencil line, two of the points can still be scored. The hybrid command therefore has a printed failure branch that preserves partial credit inside a flawed diagram.
**Evidence:** the item prints "Describe how the student should set up and carry out her experiment. You may draw a diagram to help with your answer." and the scheme carries the conditional "If diagram shows" "solvent above pencil" "line only M1 and M2" "can be scored" (SRC-QPMS-4CH1, 2019-06/4CH1-1CR/questions.md lines 146-160).
Temporal scope: CURRENT — AUTHORITATIVE.


## Evidence / Source Basis

Primary evidence: SRC-QPMS-4CH1 — the run's pack carries the 2019-06 2C and 1CR
papers (plus interleaved sessions) as bounded line-window excerpts with line locators
preserved; every command-word anchor above is quoted from those excerpts and
locator-addressed. The mark-scheme responses cited ride inside the same parsed files
(the corpus embeds mark-scheme text per item). No ER evidence is used (EXM ground);
no specimen material is cited.

## Limitations / Coverage Gaps

The command inventory is observational over the pack's sessions, not a claimed census
of every command on every paper; rare commands outside the query net are possible and
unassessed here. Frequency statistics belong to ASM-05/ASM-09. Deduce/Justify/Compare
were included in the pack's query plan; where the pack's excerpts show no instance,
this artifact makes no claim about them rather than inferring from outside the pack.
No canonical planes were written.

## Research Status

GENERATED under SIB-CHEMISTRY_4CH1-RUN-005 (BL-008 pass 5) from the run's evidence
pack alone; validator of record tools/sib @ 357ace0a; claim QA r3 bound all citations
to pack excerpts. Deepened under SIB-CHEMISTRY_4CH1-RUN-019 (D3 tranche 3): +3 records (ASM-070..072), zero-append mining of the carried pack of record; every quote self-bound to raw excerpt text before the official gate; claim QA re-bound all citations. Research artifact — evidence-backed, not canonical educational
truth.
