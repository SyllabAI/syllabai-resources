---
sib_protocol: SIB-1.0
artifact_id: PRA-04
artifact_version: 1.1
subject: Chemistry
qualification: International GCSE
specification: 4CH1
curriculum_version: "2017"

research_family: practical_procedural_intelligence
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
  source_manifest: "SRC-TL-4CH1"
  generation_run_id: "SIB-CHEMISTRY_4CH1-RUN-020"
  generator:
    provider: "z.ai"
    model: "GLM"
    agent_version: "SIB-GEN-r0"
  source_revisions:
    syllabai: "357ace0a230f5e0095ad230320af587dca6bb71f"
    syllabai_pastpapers: "f39fc0fde3ee12f97efa5c031e16c17c25243fd5"
    syllabai_resources: "923232c73d9ac7dca748b29ccca1c8067ba741aa"
---

# PRA-04 — Procedure Errors and Failure Modes

## Purpose

This artifact catalogues the procedure-error and failure-mode intelligence of
record for 4CH1 practical work: the hazard-specific safety-note system embedded
in procedures (SRC-BOOK-4CH1-SB1), named error sources with physical causes, the
calorimetry evaluation section, version-dependence disclosures, the terminology
guide's failure-prevention vocabulary (SRC-TL-4CH1), and the exam-side failure
modes encoded in the official mark schemes as IGNORE/ALLOW/REJECT classes
(SRC-QPMS-4CH1). Claims ride only on this artifact's own bounded pack excerpts.
Canonical planes are untouched.

## Scope

**Covers:** hazard-specific safety notes; demonstration-only hazard gating;
named error sources and approximations; evaluation sections; variant-tolerance
disclosures; mark-scheme failure-mode classes (IGNORE clear, REJECT, ALLOW
ranges).

**Out of scope:** mark-point taxonomy breadth (MS family) and misconception
diagnosis (MIS/PED-09).

## Executive Summary

Failure modes are handled on two sides. Before the lab, the book's safety-note
system attaches the specific hazard to the specific step — spitting hot solids,
chlorine with asthma, spirit burners near flames — and gates the most dangerous
reactions as teacher-only demonstrations or names them as impossible in school
(rubidium and caesium explode; fluorine is never in a school lab). After the
measurement, named error sources with physical causes (heat loss to air and
vessel in calorimetry; the volume-change approximation behind solubility work)
are written into the procedure itself, and one procedure discloses its own
variant tolerance. The official mark schemes then encode the exam-side failure
modes as classes — IGNORE clear (echoing the colourless-not-clear rule), REJECT
for a named wrong observation, ALLOW ranges for acceptable colour variants — so
the failure taxonomy of the lab and the mark scheme face the same way.
The deepened records extend the failure-mode claim into the data plane: the book's own question procedures carry the processing law (best-fit lines, anomaly identification with corrected readings, and comparability of conditions across results), the approximation disclosures that name where a calculation stops being exact and offer the instrument upgrade (a pH meter over indicator, a solubility experiment over a volume-assuming calculation), and the exam's own pricing of method improvement as linked explanation pairs with error-attribution classes.

## Main Analysis

### PRA-021 — Hazard-specific safety notes embedded in procedures

**Claim:** each procedure carries the safety note for its own hazard class, from
generic eye protection to substance-specific and condition-specific warnings.
**Evidence:** the solubility note pairs eye protection with gentle heating
against "burns from hot solid 'spitting' out of the basin"
(SRC-BOOK-4CH1-SB1, edexcel_igcse_chemistry_chunks_v3.jsonl line 45); the
chlorine note adds the asthma-specific "Do not smell the chlorine, especially if
you have asthma" with the switch-off rule (SRC-BOOK-4CH1-SB1,
edexcel_igcse_chemistry_chunks_v3.jsonl line 371); the ester preparation demands
goggles, a fume cupboard, and immediate washing of skin contact
(SRC-BOOK-4CH1-SB1, edexcel_igcse_chemistry_chunks_v3.jsonl line 1021); the
spirit-burner note bans carrying a lit burner or refilling near a naked flame
(SRC-BOOK-4CH1-SB1, edexcel_igcse_chemistry_chunks_v3.jsonl line 727).
Temporal scope: CURRENT — AUTHORITATIVE.

### PRA-022 — Hazard gating: demonstrations and impossibility statements

**Claim:** procedures that cannot run safely at student level are gated as
teacher demonstrations with extra equipment, or declared impossible in school.
**Evidence:** demonstration notes require face shields and safety screens with
pupils kept back (SRC-BOOK-4CH1-SB1, edexcel_igcse_chemistry_chunks_v3.jsonl
line 181); the alkali-metals chapter states the rubidium and caesium reactions
"would be too hazardous to attempt in school as they would explode"
(SRC-BOOK-4CH1-SB1, edexcel_igcse_chemistry_chunks_v3.jsonl line 421); the
halogens chapter states fluorine is "so dangerously reactive that you would
never expect to find it in a school lab" (SRC-BOOK-4CH1-SB1,
edexcel_igcse_chemistry_chunks_v3.jsonl line 441). Temporal scope: CURRENT —
AUTHORITATIVE.

### PRA-023 — Named error sources with physical causes

**Claim:** the procedures name their own dominant error sources and attach the
physical cause, rather than leaving error as a vague category.
**Evidence:** the combustion calorimetry evaluation states "There are many
sources of error in this experiment, in particular large amounts of heat loss"
with heat lost to air and vessel enumerated (SRC-BOOK-4CH1-SB1,
edexcel_igcse_chemistry_chunks_v3.jsonl line 738); the solubility calculation
carries its own approximation disclosure — the result "gives only an approximate
value" because dissolved substance changes the volume (SRC-BOOK-4CH1-SB1,
edexcel_igcse_chemistry_chunks_v3.jsonl line 400); the evaluation section fixes
the specific heat capacity value used, c = 4.18 J/g/°C (SRC-BOOK-4CH1-SB1,
edexcel_igcse_chemistry_chunks_v3.jsonl line 737). Temporal scope: CURRENT —
AUTHORITATIVE.

### PRA-024 — Version tolerance disclosed at the procedure

**Claim:** the book discloses that a procedure has acceptable variants —
different temperature-rise targets or fixed heating times — so learners do not
treat one recipe as the only valid method.
**Evidence:** the calorimetry KEY POINT states "You may see other versions of
this experiment recommending a different temperature rise" or fixed-duration
heating (SRC-BOOK-4CH1-SB1, edexcel_igcse_chemistry_chunks_v3.jsonl line 731).
Temporal scope: CURRENT — AUTHORITATIVE.

### PRA-025 — The exam-side failure-mode classes

**Claim:** the official mark schemes encode practical failure modes as explicit
classes — IGNORE for irrelevant wording, REJECT for a named wrong observation,
ALLOW ranges for acceptable variants — including the clear-versus-colourless
trap.
**Evidence:** the displacement scheme allows the colour range "brown/pink/
pink-brown solid forms ALLOW red-brown /orange-brown" and ignores wrong
initial-colour references (SRC-QPMS-4CH1, 2019-06/4CH1-1C/questions.md lines
457-481); the same scheme ignores the word clear where the required observation
is "solution turns colourless ALLOW solution becomes paler"
(SRC-QPMS-4CH1, 2019-06/4CH1-1C/questions.md lines 463-481); the alkene scheme
accepts decolourised while marking "IGNORE clear" and REJECTing a named wrong
observation (SRC-QPMS-4CH1, 2019-06/4CH1-1C/questions.md lines 611-625).
Temporal scope: CURRENT — AUTHORITATIVE.

### PRA-026 — The vocabulary fix for failure prevention

**Claim:** the terminology guidance exists because inconsistent definitions are
themselves a failure mode, and its planning band starts failure prevention at
variable control.
**Evidence:** the guide's introduction names the problem — "Definitions of terms
can vary between" sources (SRC-TL-4CH1,
practical-terminology-in-int-gcse-science.pdf p 3); its planning section makes
variable consideration the first step of an investigation (SRC-TL-4CH1,
practical-terminology-in-int-gcse-science.pdf p 4). Temporal scope: CURRENT —
AUTHORITATIVE.

### PRA-042 — The book's question procedures carry an in-procedure data-processing law

**Claim:** procedure intelligence extends past bench work into the data plane: the book's question procedures demand best-fit plotting, anomaly identification with corrected readings, and comparability of conditions across results.
**Evidence:** the plotting demand is stated directly — "Plot these results on a piece of graph paper and draw a straight line of best fit." — and the anomaly demand couples detection with repair: "Identify the anomalous point and suggest the volume of gas that should have been obtained for that time." (SRC-BOOK-4CH1-SB1, edexcel_igcse_chemistry_chunks_v3.jsonl line 708); comparability is priced as a choice — "Calculate the volume of water the student should have used for the result to be comparable with the other four" — and the anomaly hunt recurs with named candidate causes on the rate graph (SRC-BOOK-4CH1-SB1, edexcel_igcse_chemistry_chunks_v3.jsonl line 858).
Temporal scope: CURRENT — AUTHORITATIVE.
### PRA-043 — The book discloses its own approximations and offers the instrument upgrade

**Claim:** where a procedure's arithmetic is only approximate, the book says so in the procedure and routes the student to a more accurate experiment or instrument — approximation is disclosed, never hidden.
**Evidence:** the solubility calculation is flagged in the question itself — "The calculation used in d gives only an approximate value for the solubility because the volume changes when a substance is dissolved in water." — and the upgrade is a full experimental redesign: "Describe an experiment that the student could carry out to determine a more accurate value for how much strontium hydroxide dissolves in 100g of water at this temperature." (SRC-BOOK-4CH1-SB1, edexcel_igcse_chemistry_chunks_v3.jsonl line 400); the instrument upgrade is stated as a hint: "You can measure pH much more accurately using a pH meter." (SRC-BOOK-4CH1-SB1, edexcel_igcse_chemistry_chunks_v3.jsonl line 572).
Temporal scope: CURRENT — AUTHORITATIVE.
### PRA-044 — The exam prices method improvement as linked explanation pairs with error-attribution classes

**Claim:** the official mark schemes examine method improvement as linked pairs — an apparatus or indicator change plus its precision consequence — and attribute lost accuracy to named procedural error classes.
**Evidence:** the demand is explicit, "Explain two improvements to the student’s method so that more accurate results are obtained.", and the grammar is fixed: "An explanation that links two of the following pairs" (SRC-QPMS-4CH1, 2022-06/4CH1-2CR/questions.md lines 537-551); the priced pairs run pipette-precision against cylinder — "a pipette is more precise/a measuring cylinder is" — and a sharp end-point against indicator spread, methyl orange/phenolphthalein/litmus replacing universal indicator (SRC-QPMS-4CH1, 2022-06/4CH1-2CR/questions.md lines 548-562); the error-attribution class list admits any one of the procedural causes — "some gas escapes before the bung is" replaced or connected, "the magnesium is impure/ the magnesium" ribbon oxidised, and "ALLOW some gas dissolves in" the acid (SRC-QPMS-4CH1, 2019-06/4CH1-1C/questions.md lines 1076-1090).
Temporal scope: CURRENT — AUTHORITATIVE.

## Evidence / Source Basis

Primary evidence: SRC-BOOK-4CH1-SB1 (safety-note, error-source, evaluation and
variant chunks at line+chunk-id locators) and SRC-QPMS-4CH1 (2019-06 Paper 1C
mark-scheme classes with the paper identity preserved via the pack file path).
Supplementary: SRC-TL-4CH1 terminology guidance pages; SRC-SPEC-4CH1 held for
statement context. Bounded excerpts with locators preserved; caps enforced by
the pack builder.

## Limitations / Coverage Gaps

This artifact catalogues the failure modes and error classes visible in its pack's excerpt windows; classes outside the captured pages/lines are neither enumerated nor denied. The RUN-020 deepening added records only from the held pack surface (zero-append tranche): no windows were appended, so error-class detail outside the captured surface is neither quoted nor denied. Mark-scheme text is quoted as parsed — the source markdown hard-wraps scheme columns, so quoted fragments are read across the wrap and OCR quirks (the '(ε)' mark token) are preserved, never repaired. No examiner sentiment is synthesized from mark schemes. No canonical planes were written.

## Research Status

GENERATED under SIB-CHEMISTRY_4CH1-RUN-006 (BL-008 pass 6) from this artifact's evidence pack alone; deepened under SIB-CHEMISTRY_4CH1-RUN-020 (D3 REQUIRED-core depth pass, tranche 4 — PRA+PED, zero-append) with +3 records (PRA-042..044) authored only from the held pack excerpts, quotes pre-bound under the markup-transparent self-check; validator of record tools/sib @ 357ace0a; claim QA r3 binds every citation to a pack excerpt. Research artifact — evidence-backed, not canonical educational truth.
