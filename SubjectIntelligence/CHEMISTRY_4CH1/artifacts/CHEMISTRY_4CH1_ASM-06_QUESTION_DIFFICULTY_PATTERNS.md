---
sib_protocol: SIB-1.0
artifact_id: ASM-06
artifact_version: 1.0
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

status: GENERATED
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

# ASM-06 — Question Difficulty Patterns

## Purpose

This artifact analyses the observable difficulty machinery of the 4CH1 papers as
parsed in the official exam corpus of record (SRC-QPMS-4CH1): how tariff, command
word, mark-scheme tolerance and dependency notes combine into the papers' difficulty
gradient. It deliberately grounds difficulty in what the parsed papers themselves
show — tariffs, accepted-answer breadth, dependency chains — and refuses to
synthesise examiner sentiment from mark schemes (the ASM/MIS/EXM boundary law). Every
claim is carried on a bounded, locator-addressed excerpt from the run's evidence
pack. Research artifact; canonical planes untouched.

## Scope

**Covers:** the within-question difficulty gradient; mark-scheme tolerance
(ALLOW/ACCEPT breadth) as an observable difficulty signal; dependency-based
difficulty; quantitative complexity; and the honest boundary of what mark schemes can
and cannot show about difficulty.

**Grounding:** SRC-QPMS-4CH1 (the 2019-06 2C and 2CR papers plus the interleaved
2020-01 2C paper of the pack).

**Out of scope:** empirical difficulty (facility values) — that is examiner-report
ground (EXM family); cross-session drift statistics (ASM-09).

## Executive Summary

Difficulty on the observed papers is built in layers. Each question opens with
1-mark identify/name parts whose mark schemes are tight but forgiving of format
(ALLOW Ar and He), then climbs through 2-3 mark linked explanations whose mark
schemes harden into point chains, to multi-step calculations where partial credit is
governed by dependency notes and no-working penalties. Mark-scheme tolerance narrows
as tariff rises: format alternatives abound at 1 mark, while 3+ mark items demand
specific steps in order. The corpus shows the machinery of difficulty but not its
empirical measure — facility data belongs to the examiner-report plane.

## Main Analysis

### ASM-031 — The within-question difficulty gradient opens at 1 mark

**Claim:** questions open with a run of 1-mark identification parts before climbing
in tariff.
**Evidence:** the 2CR opening question runs four consecutive 1-mark parts — "### 1(a)
(i) [1]" through "### 1(a)(iv) [1]" with stems "Identify the gas that is a
compound.", "Identify the most abundant gas in the atmosphere." and "Identify the
greenhouse gas." (SRC-QPMS-4CH1, 2019-06/4CH1-2CR/questions.md lines 14-28); the 2020-01 2C paper repeats the pattern with "Identify the compound."
and "Identify the mixture." (SRC-QPMS-4CH1, 2020-01/4CH1-2C/questions.md lines 25-39).
Temporal scope: CURRENT — AUTHORITATIVE.

### ASM-032 — Mark-scheme tolerance is the low-tariff cushion

**Claim:** 1-mark parts show the widest accepted-answer breadth — alternative names,
formulae and visual renderings are pre-allowed.
**Evidence:** "argon and helium ALLOW Ar and He" (SRC-QPMS-4CH1, 2019-06/4CH1-2CR/questions.md lines 14-28); the parsed excerpt (SRC-QPMS-4CH1, 2019-06/4CH1-2CR/questions.md lines 25-39); the colour-observation mark scheme allows "ALLOW any combination of
grey and black eg grey-black" (SRC-QPMS-4CH1, 2019-06/4CH1-2C/questions.md lines 58-72).
**Design reading:** at 1 mark the papers reward knowing the substance, not the
notation; drills should not over-invest in format at this tier.
Temporal scope: CURRENT — AUTHORITATIVE.

### ASM-033 — Dependency notes harden the higher tiers

**Claim:** as tariff rises, mark schemes impose ordering and dependency — steps must
be shown in sequence, and later marks can hang on earlier ones.
**Evidence:** the mean-evaporation calculation grants the answer without working a
capped value — "62/62.3 with no working scores 2" with the alternative "ALLOW
69/69.25/69.3 for 1 mark" (SRC-QPMS-4CH1, 2019-06/4CH1-2C/questions.md lines 166-180); the moles calculation's "0.0025 with no working scores" note truncates
unearned credit (SRC-QPMS-4CH1, 2019-06/4CH1-2C/questions.md lines 724-738); and the
concentration calculation chains on the previous part — "Mark CSQ on (b)(ii)"
(SRC-QPMS-4CH1, 2019-06/4CH1-2C/questions.md lines 749-763).
Temporal scope: CURRENT — AUTHORITATIVE.

### ASM-034 — Quantitative complexity is tariff-stamped

**Claim:** multi-step quantitative work is stamped with its complexity in the tariff —
the isotope-mixture relative-atomic-mass calculation carries [3].
**Evidence:** "### 2(b) [3]" heads the chlorine-isotope RAM item "Calculate the
relative atomic mass of this sample of chlorine" over the 77.78%/22.22% mixture stem
(SRC-QPMS-4CH1, 2019-06/4CH1-2C/questions.md lines 58-72); the same question's
table-completion parts sit at [2] (SRC-QPMS-4CH1, 2019-06/4CH1-2C/questions.md lines 37-51).
Temporal scope: CURRENT — AUTHORITATIVE.

### ASM-035 — Three-point links mark the reasoning ceiling within a question

**Claim:** the hardest reasoning parts in ordinary questions are three-point linked
explanations.
**Evidence:** "Explain why magnalium is harder than aluminium." is marked "An
explanation that links together the following three points" (SRC-QPMS-4CH1, 2019-06/4CH1-2C/questions.md lines 278-292); the same paper's equilibrium item uses
the two-point form at [2] (SRC-QPMS-4CH1, 2019-06/4CH1-2C/questions.md lines 574-588).
Temporal scope: CURRENT — AUTHORITATIVE.

### ASM-036 — The difficulty boundary: what mark schemes cannot show

**Claim:** the parsed papers show the machinery of difficulty (tariff, tolerance,
dependency) but not its empirical measure; candidate-level facility belongs to the
examiner-report plane and is out of this family's ground.
**Evidence:** the mark schemes cited above expose marking rules — the parsed excerpt (SRC-QPMS-4CH1, 2019-06/4CH1-2C/questions.md lines 14-28) — but no
attempt-rate or facility data exists anywhere in the parsed QP/MS text; this artifact
therefore makes no facility claim, and the examiner-sentiment substitution is
forbidden by the family law.
Temporal scope: CURRENT — AUTHORITATIVE.

## Evidence / Source Basis

Primary evidence: SRC-QPMS-4CH1 — the 2019-06 2C, 2019-06 2CR and 2020-01 2C official
extractions (bounded line-window excerpts, locators preserved, embedded mark-scheme
text cited verbatim). No examiner reports were consumed here; no specimen material
was cited; supplementary pack sources were not consumed for claims.

## Limitations / Coverage Gaps

Difficulty here means the papers' own difficulty machinery; it is not a facility
ranking, and no such ranking is derivable from this pack by law. The anchors come
from three paper files; the pattern claims are asserted only where the pack shows
them. Cross-session difficulty drift is unmeasured here. No canonical planes were
written.

## Research Status

GENERATED under SIB-CHEMISTRY_4CH1-RUN-005 (BL-008 pass 5) from the run's evidence
pack alone; validator of record tools/sib @ 357ace0a; claim QA r3 bound all citations
to pack excerpts. Research artifact — evidence-backed, not canonical educational
truth.
