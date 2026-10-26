---
sib_protocol: SIB-1.0
artifact_id: PRA-04
artifact_version: 1.0
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

status: GENERATED
generated_by: zai_agent
generated_at: 2026-10-26

provenance:
  source_manifest: "SRC-TL-4CH1"
  generation_run_id: "SIB-CHEMISTRY_4CH1-RUN-006"
  generator:
    provider: "z.ai"
    model: "GLM"
    agent_version: "SIB-GEN-r0"
  source_revisions:
    syllabai: "357ace0a230f5e0095ad230320af587dca6bb71f"
    syllabai_pastpapers: "3b6a443d4e3643f461a1cca12c6e1ad47ab6b596"
    syllabai_resources: "8b5a64f1b18724208ff19969b002028d3ed41bed"
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

## Evidence / Source Basis

Primary evidence: SRC-BOOK-4CH1-SB1 (safety-note, error-source, evaluation and
variant chunks at line+chunk-id locators) and SRC-QPMS-4CH1 (2019-06 Paper 1C
mark-scheme classes with the paper identity preserved via the pack file path).
Supplementary: SRC-TL-4CH1 terminology guidance pages; SRC-SPEC-4CH1 held for
statement context. Bounded excerpts with locators preserved; caps enforced by
the pack builder.

## Limitations / Coverage Gaps

Safety notes are catalogued from this pack's excerpt windows; the full
safety-note inventory across all procedures is neither enumerated nor denied.
Mark-scheme classes are cited only as they appear in this pack's excerpt windows
for one paper; the MS family owns the systematic mark-point layer. No examiner
sentiment is synthesized from mark schemes, and no mark_points plane data is
consumed or written. OCR-era quirks are quoted as parsed or paraphrased, never
repaired. No canonical planes were written.

## Research Status

GENERATED under SIB-CHEMISTRY_4CH1-RUN-006 (BL-008 pass 6) from this artifact's
evidence pack alone; validator of record tools/sib @ 357ace0a; claim QA r3 binds
every citation to a pack excerpt. Research artifact — evidence-backed, not
canonical educational truth.
