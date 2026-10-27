---
sib_protocol: SIB-1.0
artifact_id: MS-07
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

# MS-07 — Examiner/Marking Language

## Purpose

This artifact catalogues the marking language of the 4CH1 mark schemes as parsed in
the official exam corpus of record (SRC-QPMS-4CH1): the annotation lexicon (IGNORE,
ALLOW, ACCEPT, OWTTE, CSQ, DO NOT ALLOW) and the semantics each marker term carries.
The lexicon is read strictly off the parsed text — it is the board's own operating
language for examiners, preserved verbatim in the corpus. Every claim is carried on a
bounded, locator-addressed excerpt from the run's evidence pack. Research artifact;
canonical planes untouched.

## Scope

**Covers:** the six-term annotation lexicon and its per-term semantics as printed on
the mark points.

**Grounding:** SRC-QPMS-4CH1 (the 2019-06 1C and 1CR papers of the pack).

**Out of scope:** examiner-report language (EXM family — examiner sentiment
synthesised from mark schemes is a forbidden substitution), alternatives breadth
(MS-04).

## Executive Summary

The mark schemes speak in a compact, consistent marking language. IGNORE marks
content that neither earns nor loses credit (clear for colourless); ALLOW admits
format latitude on the same point (red-brown/orange-brown for brown); ACCEPT admits
chemically equivalent formulations (a reversible arrow; HO- for OH-); OWTTE waives
wording while holding the chemistry; CSQ chains a point's credit onto an earlier
answer; and DO NOT WITHHOLDS credit for a named error. Reading the lexicon is
reading the examiner's operating manual — and because it is preserved in the parsed
corpus, revision materials can quote the board's own terms rather than paraphrasing
them.

## Main Analysis

### MS-037 — The six-term annotation lexicon

**Claim:** the parsed mark schemes use a stable annotation lexicon — IGNORE, ALLOW,
ACCEPT, OWTTE, CSQ and DO NOT ALLOW — attached directly to mark points.
**Evidence:** the displacement-observation scheme runs ALLOW, IGNORE and the point
lines together — "M1 brown/pink/pink-brown solid forms ALLOW red-brown /orange-brown
IGNORE red or orange alone ... M2 solution turns colourless ALLOW solution becomes
paler IGNORE clear" (SRC-QPMS-4CH1, 2019-06/4CH1-1C/questions.md lines 457-471).
Temporal scope: CURRENT — AUTHORITATIVE.

### MS-038 — IGNORE: non-scoring, non-penalised

**Claim:** IGNORE voids named content without penalising the candidate.
**Evidence:** "IGNORE Fe if added to both sides of the equation" on the ammonia
equation (SRC-QPMS-4CH1, 2019-06/4CH1-1C/questions.md lines 378-392); the stacked
IGNORE notes on the displacement observation point — the parsed excerpt (SRC-QPMS-4CH1, 2019-06/4CH1-1C/questions.md lines 463-477).
Temporal scope: CURRENT — AUTHORITATIVE.

### MS-039 — ALLOW: format latitude on the required chemistry

**Claim:** ALLOW admits variant renderings of the same chemical fact.
**Evidence:** "M1 brown/pink/pink-brown solid forms ALLOW red-brown /orange-brown
... ALLOW precipitate for solid" and "M2 solution turns colourless ALLOW solution
becomes paler" (SRC-QPMS-4CH1, 2019-06/4CH1-1C/questions.md lines 457-471).
Temporal scope: CURRENT — AUTHORITATIVE.

### MS-040 — ACCEPT: chemically equivalent formulations

**Claim:** ACCEPT admits alternative chemical notations and formulations of equal
standing.
**Evidence:** "N2 + 3H2 → 2NH3 ACCEPT reversible arrow" (SRC-QPMS-4CH1, 2019-06/4CH1-1C/questions.md lines 378-392); "OH- ACCEPT HO-" (SRC-QPMS-4CH1, 2019-06/4CH1-1CR/questions.md lines 119-133).
Temporal scope: CURRENT — AUTHORITATIVE.

### MS-041 — Boundary enforcement: DO NOT ALLOW

**Claim:** where a named error must void the mark, the scheme prints DO NOT ALLOW on
the point.
**Evidence:** the chromatography method scheme's guard "place the paper in the
beaker so DO NOT ALLOW M3 if" alongside its point lines (SRC-QPMS-4CH1, 2019-06/4CH1-1CR/questions.md lines 171-185).
Temporal scope: CURRENT — AUTHORITATIVE.

### MS-042 — Consequential marking: CSQ and OWTTE

**Claim:** CSQ chains credit onto earlier answers and OWTTE waives wording; both
ride on the point lines.
**Evidence:** "lithium bromide / LiBr Mark CSQ on (a) and" (SRC-QPMS-4CH1, 2019-06/4CH1-1C/questions.md lines 184-198); the parsed excerpt
(SRC-QPMS-4CH1, 2019-06/4CH1-1CR/questions.md lines 171-185).
Temporal scope: CURRENT — AUTHORITATIVE.

## Evidence / Source Basis

Primary evidence: SRC-QPMS-4CH1 — the 2019-06 1C and 1CR official extractions (82
bounded line-window excerpts across the two files, locators preserved; marking
language cited verbatim). No examiner reports were consumed for this artifact; the
examiner-sentiment substitution is forbidden and was not made. No specimen material
was cited.

## Limitations / Coverage Gaps

The lexicon covers the annotation terms visible in the pack's excerpt windows of two
2019-06 papers; the corpus's later sessions share the declared extraction schema but
lexicon drift is not audited here. Term frequency is not measured. No canonical
planes were written.

## Research Status

GENERATED under SIB-CHEMISTRY_4CH1-RUN-005 (BL-008 pass 5) from the run's evidence
pack alone; validator of record tools/sib @ 357ace0a; claim QA r3 bound all citations
to pack excerpts. Research artifact — evidence-backed, not canonical educational
truth.
