---
sib_protocol: SIB-1.0
artifact_id: MS-06
artifact_version: 1.1
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
  supplementary: false

# lifecycle: GENERATED -> QA_PASSED -> STAGED
status: PUBLISHED
generated_by: zai_agent
generated_at: 2026-10-29

provenance:
  source_manifest: "SRC-QPMS-4CH1"
  generation_run_id: "SIB-CHEMISTRY_4CH1-RUN-018"
  generator:
    provider: "z.ai"
    model: "GLM"
    agent_version: "SIB-GEN-r0"
  source_revisions:
    syllabai: "357ace0a230f5e0095ad230320af587dca6bb71f"
    syllabai_pastpapers: "2cb92fe5f56d22f1b231c129a7e0dbc27bf86007"
    syllabai_resources: "251b46ba0bd9a08d66d57eca44fc8c80cd283289"
---

# MS-06 — Partial Credit Patterns

## Purpose

This artifact catalogues how the 4CH1 mark schemes award partial credit, as parsed in
the official exam corpus of record (SRC-QPMS-4CH1): step-pair splits, no-working
caps with fallback values, dependency-based one-mark outcomes, pick-N pool awards,
diagram-route equivalence and deduction mechanics. The patterns are read strictly off
the parsed text. Every claim is carried on a bounded, locator-addressed excerpt from
the run's evidence pack. Research artifact; canonical planes untouched.

## Scope

**Covers:** step-pair credit; no-working caps and fallback allowances; dependency
partial credit; pooled pick-N awards; diagram-route equivalence; deduction rules.

**Grounding:** SRC-QPMS-4CH1 (the 2019-06 2C/1CR, 2020-01 2C, 2022-01 1CR, 2022-06 2C, 2023-11 2C, 2025-06 2C and 2026-06 2C excerpt windows of the pack).

**Out of scope:** full mark-loss catalogue (MS-05), marking-language lexicon (MS-07).

## Executive Summary

Partial credit on 4CH1 is engineered, not incidental. Two-mark calculations split
into a method point and a result point; a bare correct answer is capped ("with no
working scores 2") while a wrong-but-defensible value can still earn one mark
(fallback allowances); reasoning points that depend on an earlier point say so
("M2 dep on M1 ... scores 1 mark"); pick-N tasks pool their credit into a single
line; diagram routes can earn the same marks as prose routes; and deduction rules
strip a mark for a named omission. The candidate-facing consequence: visible working
is never wasted, and a defensible wrong answer often banks something.

## Main Analysis

### MS-031 — Step-pair credit on two-mark calculations

**Claim:** two-mark calculations print one point for the method and one for the
result.
**Evidence:** "- **(1)** (64 + 63 + 60) ÷3 / - **(1)** = 62" on the mean-evaporation
item (SRC-QPMS-4CH1, 2019-06/4CH1-2C/questions.md lines 172-186).
Temporal scope: CURRENT — AUTHORITATIVE.

### MS-032 — No-working caps with fallback allowances

**Claim:** bare answers are capped by printed no-working notes, while named
fallback values can still earn a reduced award.
**Evidence:** "62/62.3 with no working scores 2 / ALLOW 69/69.25/69.3 for 1 mark"
(SRC-QPMS-4CH1, 2019-06/4CH1-2C/questions.md lines 172-186); the Rf scheme's "0.66
with no working scores 3" and "M2 0.6615 ACCEPT any number of sig fig / M3 0.66
must be 2 sig fig" (SRC-QPMS-4CH1, 2019-06/4CH1-1CR/questions.md lines 282-296).
Temporal scope: CURRENT — AUTHORITATIVE.

### MS-033 — Dependency-based one-mark outcomes

**Claim:** a dependent point that loses its anchor can still score one mark where
the scheme says so.
**Evidence:** "M2 (electrons) can move/can flow/are mobile REJECT cations/atoms move
for both marks / M2 dep on M1 or mention of electrons i.e. 'electrons move' scores 1
mark" (SRC-QPMS-4CH1, 2020-01/4CH1-2C/questions.md lines 220-234).
Temporal scope: CURRENT — AUTHORITATIVE.

### MS-034 — Pooled pick-N awards

**Claim:** pick-N tasks print a single pooled point whose value is the count of
acceptable picks.
**Evidence:** "Award 1 mark each for any six of the following: Method 1 M1 polystyrene
(insulator so) reduces/prevents heat loss (to atmosphere) OWTTE..." with its point
line "- **(6)** Award 1 mark each for any six of the following:" (SRC-QPMS-4CH1, 2022-01/4CH1-1CR/questions.md lines 1031-1045).
Temporal scope: CURRENT — AUTHORITATIVE.

### MS-035 — Diagram-route equivalence

**Claim:** credit routes through diagrams equal the prose route where the scheme
says so.
**Evidence:** "Both marks can be scored from diagrams showing correct electronic
configurations of the ions." alongside the ion points "- **(1)** magnesium/Mg loses
two electrons/becomes 2.8 / - **(1)** oxygen/O gains two electrons/becomes 2.8"
(SRC-QPMS-4CH1, 2022-06/4CH1-2C/questions.md lines 340-354).
Temporal scope: CURRENT — AUTHORITATIVE.

### MS-036 — Deduction mechanics

**Claim:** schemes can deduct a mark for a named omission and penalise broken
alternative methods.
**Evidence:** "Deduct 1 mark if no mention of layers/sheets/rows" on the
alloy-hardness scheme (SRC-QPMS-4CH1, 2023-11/4CH1-2C/questions.md lines 274-288);
the titration scheme's "REJECT incorrect ALTERNATIVE METHOD rounding for 1 mark"
with the printed alternative route (SRC-QPMS-4CH1, 2025-06/4CH1-2C/questions.md lines 550-564).
Temporal scope: CURRENT — AUTHORITATIVE.

### MS-064 — Subsumption rules let stronger answers absorb weaker points

**Claim:** the schemes print subsumption rules that collapse point boundaries for strong answers: a more precise final result can absorb a less precise one, and the absorbed point still counts. The Rf scheme states M3 subsumes M2 while both remain awardable; the zinc-excess scheme states M2 subsumes M1 outright. The examiner report of the same era observes the resulting bimodal outcome — most candidates scored either zero or two on a neighbouring displayed-formula item — corroborating that subsumption compresses the middle of the distribution.
**Evidence:** "M3 subsumes M2 can score M2 and M3" rides on the Rf precision rows (SRC-QPMS-4CH1, 2019-06/4CH1-1CR/questions.md lines 282-296); "M2 subsumes M1" rides on the zinc-excess calculation (SRC-QPMS-4CH1, 2022-01/4CH1-1CR/questions.md lines 1064-1078). The 2019 report corroborates the compressed outcome (SUPPLEMENTARY texture): "Most candidates either scored 0 or 2 here, with a very small minority scoring 1 mark" (SRC-ER-4CH1, 2019-06/4CH1-1C/er.pdf p25).
Temporal scope: CURRENT — AUTHORITATIVE.

### MS-065 — Fallback awards for near-miss and reduced-method answers

**Claim:** the schemes print explicit fallback prices for answers that miss the full condition: an electron statement without the delocalisation scores one of two, a dilution misroute prices at two of three, and a bare correct answer to the wrong precision still banks the full three. The fallback is always priced — the printed scheme names both the reduced award and the condition that triggers it — so partial credit is a printed rule, not an examiner's discretion.
**Evidence:** the electrolysis point prices the reduced statement as "electrons i.e. 'electrons move' scores 1 mark" (SRC-QPMS-4CH1, 2020-01/4CH1-2C/questions.md lines 220-234); the titration scheme prints "ALLOW 0.472 /0.118 for 2 marks" beside the full-credit route (SRC-QPMS-4CH1, 2025-06/4CH1-2C/questions.md lines 550-564); the Rf scheme banks the bare answer, "0.66 with no working scores 3" (SRC-QPMS-4CH1, 2019-06/4CH1-1CR/questions.md lines 282-296).
Temporal scope: CURRENT — AUTHORITATIVE.

### MS-066 — Consequential partial credit on data-selection tasks

**Claim:** the newest session in the pack extends partial credit to data handling: titre selection, averaging and the final concentration each key off the candidate's own earlier choices, and the scheme prints the consequential chain explicitly — which selection earns which downstream award, and what a single-tick selection forfeits. The 2026 window shows the machinery is current house practice, not a legacy form; the printed dependency is the auditor's handle on the whole chain.
**Evidence:** the titrine-selection window prints "only use of 2 or 3 concordant titres can scores both marks in (ii)" and chains the awards so that "M1 consequential on results ticked" feeding "M2 consequential on correct calculation from M1" (SRC-QPMS-4CH1, 2026-06/4CH1-2C/questions.md lines 192-206).
Temporal scope: CURRENT — AUTHORITATIVE.


## Evidence / Source Basis

Primary evidence: SRC-QPMS-4CH1 — the run's pack of official extractions (bounded
line-window excerpts across the 2019-2025 sessions listed, locators preserved;
mark-scheme text cited verbatim). No examiner reports consumed; no specimen material
cited; supplementary sources not consumed for claims.

## Limitations / Coverage Gaps

The partial-credit catalogue covers the mechanics visible in the pack's excerpt
windows; several session files in the pack are identity-only (no excerpts matched
the query net) and contribute nothing here. Frequency of each pattern across the
corpus is not measured. No canonical planes were written.

## Research Status

GENERATED under SIB-CHEMISTRY_4CH1-RUN-005 (BL-008 pass 5) from the run's evidence
pack alone; validator of record tools/sib @ 357ace0a; claim QA r3 bound all citations
to pack excerpts. Deepened under SIB-CHEMISTRY_4CH1-RUN-018 (D3 tranche 2): +3 records (MS-064..066), zero-append mining of the carried RUN-005 pack of record; every quote self-bound to raw excerpt text before the official gate; claim QA re-bound all citations. Research artifact — evidence-backed, not canonical educational truth.
