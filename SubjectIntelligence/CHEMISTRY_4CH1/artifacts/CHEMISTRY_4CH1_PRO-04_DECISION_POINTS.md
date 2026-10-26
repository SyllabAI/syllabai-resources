---
sib_protocol: SIB-1.0
artifact_id: PRO-04
artifact_version: 1.0
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

status: GENERATED
generated_by: zai_agent
generated_at: 2026-10-26

provenance:
  source_manifest: "SRC-QPMS-4CH1"
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

# PRO-04 — Decision Points

## Purpose

This artifact catalogues the decision points of record in 4CH1 problem solving:
the forks the official mark schemes publish (equipment and reagent identity
alternatives, reverse-argument routes, observation ranges with tolerances,
dependency and error-carried-forward rules), the which-style item type that
forces a decision of SRC-QPMS-4CH1 and SRC-SPEC-4CH1, and the book's own decision
rules (SRC-BOOK-4CH1-SB1). Claims ride only on this artifact's own bounded pack
excerpts. Canonical planes are untouched.

## Scope

**Covers:** identity forks with ALLOW/ACCEPT alternates; reverse-argument
route forks; observation-range tolerances; dependency (DEP) and error-carried-
forward (ECF) decision structures; which-decision items; book-side phase
decision rule.

**Out of scope:** multi-step chains (PRO-03) and dead ends (PRO-05).

## Executive Summary

Decision points in 4CH1 are published with their tolerated alternatives. Where
an identity decision arises — which piece of apparatus, which reagent, which
name — the mark scheme prints the fork explicitly: pipette with burette
allowed, barium chloride with the nitrate accepted, magnesium with its symbol.
Where a route decision arises, both directions are pre-authorised (reverse
arguments accepted on the extraction-method justification). Observation
decisions come with tolerance ranges (any orange/yellow combination; pink-brown
spanning red-brown). The decision machinery also carries its own logic rules:
dependencies (a mark depends on its parent) and error-carried-forward windows
with stated validity conditions. The book's phase rule shows the same
decision-point structure on the learning side: one rule, three regions.

## Main Analysis

### PRO-021 — Identity forks published with alternates

**Claim:** identity decisions in answers carry published alternates — either
the apparatus or its acceptable substitute, either the name or the formula.
**Evidence:** the apparatus item accepts "(graduated) pipette ALLOW burette"
(SRC-QPMS-4CH1, 2020-11/4CH1-2C/questions.md lines 611-625); the element answer
is "magnesium ALLOW Mg" (SRC-QPMS-4CH1, 2020-11/4CH1-2C/questions.md lines
154-168); the sulfate test reads "add barium chloride/BaCl2 ACCEPT barium
nitrate/Ba(NO3)2" (SRC-QPMS-4CH1, 2020-11/4CH1-2C/questions.md lines 593-607).
Temporal scope: CURRENT — AUTHORITATIVE.

### PRO-022 — Route forks with reverse arguments authorised

**Claim:** method-choice decisions are pre-authorised in both directions where
the reasoning supports either orientation.
**Evidence:** the extraction-method scheme marks "Method 1/ heating the metal
oxide/lead(II) oxide with carbon" as the chosen route and prints "ACCEPT
reverse arguments" for the justification (SRC-QPMS-4CH1,
2020-11/4CH1-2C/questions.md lines 186-205). Temporal scope: CURRENT —
AUTHORITATIVE.

### PRO-023 — Observation decisions with tolerance ranges

**Claim:** observation decisions carry explicit tolerance ranges rather than a
single accepted answer.
**Evidence:** the bromine-water decision accepts "from orange to colourless
ALLOW yellow for orange or any combination of orange/yellow"
(SRC-QPMS-4CH1, 2020-11/4CH1-2C/questions.md lines 407-427); the reversible
equation decision accepts the reverse arrow while ignoring an added catalyst
symbol on either side (SRC-QPMS-4CH1, 2020-11/4CH1-2C/questions.md lines
378-383). Temporal scope: CURRENT — AUTHORITATIVE.
### PRO-024 — Dependency and error-carried-forward decision structures

**Claim:** the mark machinery encodes decision dependencies — a mark may depend
on its parent, and early errors carry forward only within stated validity
conditions.
**Evidence:** the ion-identity scheme marks the precipitate "M2 DEP M1"
(SRC-QPMS-4CH1, 2020-11/4CH1-2C/questions.md lines 601-615); the chromatography
Rf scheme allows "ECF from M1 M2 only if Rf < 1" (SRC-QPMS-4CH1,
2020-11/4CH1-2C/questions.md lines 122-136); the bond-energy scheme carries
"M3 M4 ECF from M1 and M2" (SRC-QPMS-4CH1, 2020-11/4CH1-2C/questions.md lines
433-453). Temporal scope: CURRENT — AUTHORITATIVE.

### PRO-025 — Which-decision items

**Claim:** the papers force decisions with which-style items, backed by the
command-word taxonomy's maintained definitions.
**Evidence:** a cathode-gas item asks "Which of these tests shows that the gas
formed at the cathode is hydrogen?" as a keyed multiple choice (SRC-QPMS-4CH1,
2020-11/4CH1-2C/questions.md lines 560-574); the spec's command-word appendix
pins the decision vocabulary definitions (SRC-SPEC-4CH1,
international-gcse-chemistry-2017-specification.pdf p 52). Temporal scope:
CURRENT — AUTHORITATIVE.

### PRO-026 — Book-side decision rules

**Claim:** the book teaches its own decision rules as three-region phase logic.
**Evidence:** the states section fixes the rule — "A substance is a solid at
temperatures below its melting point", liquid between melting and boiling, gas
above boiling (SRC-BOOK-4CH1-SB1, edexcel_igcse_chemistry_chunks_v3.jsonl line
33). Temporal scope: CURRENT — AUTHORITATIVE.

## Evidence / Source Basis

Primary evidence: SRC-QPMS-4CH1 (2019-06 Paper 1C mark-scheme forks with paper
identity preserved via the pack file path) and SRC-BOOK-4CH1-SB1 (decision-rule
chunk at line+chunk-id locator). Supplementary: SRC-SPEC-4CH1 command-word
appendix page. Bounded excerpts with locators preserved; caps enforced by the
pack builder.

## Limitations / Coverage Gaps

Decision forks are catalogued from this pack's excerpt windows for one paper;
other sessions' fork structures are neither enumerated nor denied. Mark-scheme
forks are cited as published decision statements only; the MS family owns the
systematic mark-layer analysis, and no mark_points plane data is consumed or
written. No examiner sentiment is synthesized from mark schemes. OCR-era
quirks are quoted as parsed or paraphrased, never repaired. No canonical planes
were written.

## Research Status

GENERATED under SIB-CHEMISTRY_4CH1-RUN-006 (BL-008 pass 6) from this artifact's
evidence pack alone; validator of record tools/sib @ 357ace0a; claim QA r3 binds
every citation to a pack excerpt. Research artifact — evidence-backed, not
canonical educational truth.
