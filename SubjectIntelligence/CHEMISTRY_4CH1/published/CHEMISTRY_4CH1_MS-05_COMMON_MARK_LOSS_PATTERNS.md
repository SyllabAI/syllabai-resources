---
sib_protocol: SIB-1.0
artifact_id: MS-05
artifact_version: 1.0
subject: Chemistry
qualification: International GCSE
specification: 4CH1
curriculum_version: "2017"

research_family: mark_scheme_intelligence
applicability: REQUIRED

temporal_scope:
  current: true
  legacy: false

source_scope:
  specification: false
  textbook: false
  question_papers: true
  mark_schemes: true
  examiner_reports: false
  supplementary: true

# lifecycle: GENERATED -> QA_PASSED -> STAGED
status: PUBLISHED
generated_by: zai_agent
generated_at: 2026-10-26

provenance:
  source_manifest: "SRC-QPMS-4CH1"
  generation_run_id: "SIB-CHEMISTRY_4CH1-RUN-005"
  generator:
    provider: "z.ai"
    model: "GLM"
    agent_version: "SIB-GEN-r0"
  source_revisions:
    syllabai: "357ace0a230f5e0095ad230320af587dca6bb71f"
    syllabai_pastpapers: "f61a5bafe6cacdf538e5e06d86f818e7737cbfe3"
    syllabai_resources: "367b5d61cd5f1ab115f9947ba2981f08389540ee"
---

# MS-05 — Common Mark-Loss Patterns

## Purpose

This artifact catalogues where and why candidates lose marks according to the 4CH1
mark schemes themselves, as parsed in the official exam corpus of record
(SRC-QPMS-4CH1): the distractor rationales that map MCQ traps, the IGNORE notes that
void non-scoring answers, the conceptual traps the schemes explicitly anticipate, and
the both-must-hold style credit conditions. The patterns are read strictly off the
parsed text. Every claim is carried on a bounded, locator-addressed excerpt from the
run's evidence pack. Research artifact; canonical planes untouched.

## Scope

**Covers:** MCQ distractor rationales; IGNORE-voided answers; anticipated conceptual
traps; selection-task credit rules; allowed-versus-ignored phrasing contrasts.

**Grounding:** SRC-QPMS-4CH1 (the 2019-06 1C/2C, 2020-01 1C and the interleaved
2020-2024 session files of the pack).

**Out of scope:** partial-credit mechanics (MS-06), examiner-reported causes of loss
(EXM family — forbidden substitution from mark schemes).

## Executive Summary

The mark schemes expose the standard loss routes: for MCQs, each distractor carries
its own rejection rationale naming the misconception behind it; for open answers,
IGNORE notes void specific irrelevant content while ALLOW notes keep valid
alternatives alive; for anticipated traps, the scheme states why the tempting answer
is wrong (a halogen cannot displace itself); and for selection tasks, credit rules
cap what any two picks can earn. The schemes also contrast allowed and ignored
phrasings on the same point — corrosion language earns, inertness language does not
— which is precisely the discrimination candidates must learn.

## Main Analysis

### MS-025 — Distractor rationales map the MCQ loss routes

**Claim:** every rejected MCQ option carries a printed rationale naming why it fails.
**Evidence:** "A is not correct as the crystal does not condense / C is not correct
as the crystal does not evaporate / D is not correct as the crystal does not melt"
(SRC-QPMS-4CH1, 2019-06/4CH1-1C/questions.md lines 22-36); the appearance item's
rationales run the same form (SRC-QPMS-4CH1, 2019-06/4CH1-1C/questions.md lines 41-55).
Temporal scope: CURRENT — AUTHORITATIVE.

### MS-026 — IGNORE notes void specific non-scoring content

**Claim:** mark points print IGNORE notes for content that does not score, however
true it may be.
**Evidence:** the saucepan-properties scheme runs "M2 does not react with
food/affect flavour of food IGNORE non-toxic", "M4 high melting point IGNORE
references to recycling" and "M5 low density/lightweight/strong IGNO..." (SRC-QPMS-4CH1, 2019-06/4CH1-2C/questions.md lines 249-263).
Temporal scope: CURRENT — AUTHORITATIVE.

### MS-027 — Anticipated conceptual traps are stated, not implied

**Claim:** the schemes name the trap explicitly where candidates predictably err.
**Evidence:** the halogen item's full rejection logic — the parsed excerpt (SRC-QPMS-4CH1, 2020-01/4CH1-1C/questions.md lines 726-740).
Temporal scope: CURRENT — AUTHORITATIVE.

### MS-028 — Selection tasks cap credit by rule

**Claim:** pick-N tasks print the pool and the per-pick rule, so wrong picks simply
forfeit their mark.
**Evidence:** "Any two from the following: M1 good conductor of heat/thermal energy
M2 does not react with food..." (SRC-QPMS-4CH1, 2019-06/4CH1-2C/questions.md lines 249-263).
Temporal scope: CURRENT — AUTHORITATIVE.

### MS-029 — Allowed and ignored phrasings contrast on the same point

**Claim:** the same point can accept one formulation and explicitly void a
neighbouring one.
**Evidence:** "M3 resistant to corrosion ALLOW does not corrode/rust IGNORE
unreactive/inert" (SRC-QPMS-4CH1, 2019-06/4CH1-2C/questions.md lines 249-263).
Temporal scope: CURRENT — AUTHORITATIVE.

### MS-030 — The schemes state why wrong answers are wrong

**Claim:** beyond voiding answers, the rejection rationales teach the correct
distinction — the loss pattern and the learning point are the same text.
**Evidence:** the process-discrimination rationales "A is not correct as condensation
describes the process of a gas changing into a liquid / B is not correct as
crystallisation describes the process of a soluble solid forming from a solution"
(SRC-QPMS-4CH1, 2019-06/4CH1-1C/questions.md lines 62-76).
Temporal scope: CURRENT — AUTHORITATIVE.

## Evidence / Source Basis

Primary evidence: SRC-QPMS-4CH1 — the run's pack of official extractions (bounded
line-window excerpts across the 2019-2024 sessions listed, locators preserved;
mark-scheme text cited verbatim). No examiner reports were consumed for this
artifact — examiner-reported causes of mark loss belong to the EXM family, and
drawing them from mark schemes is the forbidden substitution. No specimen material
was cited.

## Limitations / Coverage Gaps

The pattern catalogue covers the loss machinery visible in the pack's excerpts;
session files with few excerpts (e.g. the 2021-01 2C and 2023-06 2C windows) are
thinly sampled and contribute anchors only where shown. Facility or frequency of
these losses is not measurable from mark schemes and is not claimed. No canonical
planes were written.

## Research Status

GENERATED under SIB-CHEMISTRY_4CH1-RUN-005 (BL-008 pass 5) from the run's evidence
pack alone; validator of record tools/sib @ 357ace0a; claim QA r3 bound all citations
to pack excerpts. Research artifact — evidence-backed, not canonical educational
truth.
