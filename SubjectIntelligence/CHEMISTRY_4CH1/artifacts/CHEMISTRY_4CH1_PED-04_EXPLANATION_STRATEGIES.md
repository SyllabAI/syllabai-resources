---
sib_protocol: SIB-1.0
artifact_id: PED-04
artifact_version: 1.0
subject: Chemistry
qualification: International GCSE
specification: 4CH1
curriculum_version: "2017"

research_family: learning_pedagogy_intelligence
applicability: REQUIRED

temporal_scope:
  current: true
  legacy: false

source_scope:
  specification: false
  textbook: true
  question_papers: false
  mark_schemes: false
  examiner_reports: true
  supplementary: true

status: GENERATED
generated_by: zai_agent
generated_at: 2026-10-26

provenance:
  source_manifest: "SRC-BOOK-4CH1-SB1"
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

# PED-04 — Explanation Strategies

## Purpose

This artifact catalogues the explanation strategies the 4CH1 evidence of record
actually deploys: imagination- and model-based explanation in the student book
(SRC-BOOK-4CH1-SB1), research-informed strategy guides for the hard topics
(SRC-TL-4CH1), examiner-verified explanation routes (SRC-ER-4CH1), and
spec-point-bound strategy notes (SRC-SME-NOTES-4CH1). Claims ride only on this
artifact's own bounded pack excerpts. Canonical planes are untouched.

## Scope

**Covers:** imagine-style cognitive anchoring; models with stated limits;
worked-example ladders; alternative-route hints; diagram-first explanations;
examiner-observed multiple valid routes; note-level explanation scaffolds.

**Out of scope:** when to teach what (PED-01) and error diagnosis (PED-09).

## Executive Summary

The dominant explanation strategy in the book is cognitive anchoring: abstract
amounts and probabilities are explained by inviting the reader to imagine
countable, concrete scenarios (a mole of carbon-12, sixty-four blue squares
changing colour, a world without fossil fuels). Models are explained with their
limits attached — the probability model is followed by a technical caution about
smooth curves — and calculations are explained through worked-example ladders
that interpret equations in moles. Hints offer a second route to the same result
rather than a different result. The examiner report confirms the reward
structure behind this: full credit is given for different valid approaches to
the same calculation, and named difficulties (drawing branched polymer
structures) confirm where explanation effort pays. Topic guides supply the
strategy layer for the two hardest explanatory jumps in the course — bonding and
equilibrium — from published education research.

## Main Analysis

### PED-021 — Imagination-based cognitive anchoring

**Claim:** the book's core explanation strategy is to anchor abstractions in
imagine-style concrete scenarios the reader can count or picture.
**Evidence:** the mole is introduced as "Imagine you had 1 mole of" carbon-12
with its 12 g mass and enormous atom count worked through
(SRC-BOOK-4CH1-SB1, edexcel_igcse_chemistry_chunks_v3.jsonl line 165); the
probability treatment of rate asks the reader to "Imagine you started with 64
blue squares" with a one-in-four chance of changing colour each second
(SRC-BOOK-4CH1-SB1, edexcel_igcse_chemistry_chunks_v3.jsonl line 831); a
crude-oil counterfactual opens with "Imagine a world in which fossil fuels" had
never formed (SRC-BOOK-4CH1-SB1, edexcel_igcse_chemistry_chunks_v3.jsonl line
938). Temporal scope: CURRENT — AUTHORITATIVE.

### PED-022 — Models taught with their limits attached

**Claim:** explanatory models are taught together with their correctness limits,
so the model is not mistaken for the mechanism.
**Evidence:** immediately after the blue-squares probability picture, the book
cautions that smooth plots can be "technically wrong" because a smooth curve
should only be used for a continuous indicator (SRC-BOOK-4CH1-SB1,
edexcel_igcse_chemistry_chunks_v3.jsonl line 739); the enthalpy hint attaches
its own convention caveat, that energy given out is shown with a negative sign
(SRC-BOOK-4CH1-SB1, edexcel_igcse_chemistry_chunks_v3.jsonl line 765).
Temporal scope: CURRENT — AUTHORITATIVE.

### PED-023 — Worked-example ladders that interpret equations in moles

**Claim:** quantitative topics are explained through worked-example ladders that
progress from a direct application to interpreting a full equation in moles.
**Evidence:** the relative-atomic-mass ladder starts at "EXAMPLE1" with a boron
isotope abundance calculation (SRC-BOOK-4CH1-SB1,
edexcel_igcse_chemistry_chunks_v3.jsonl line 101); a later rung poses a heating
calcium-carbonate problem (SRC-BOOK-4CH1-SB1,
edexcel_igcse_chemistry_chunks_v3.jsonl line 211); the percentage-yield rung
instructs the learner to "Interpret the equation in terms of moles" and trace the
substance through (SRC-BOOK-4CH1-SB1,
edexcel_igcse_chemistry_chunks_v3.jsonl line 221); solution calculations are
explained on the everyday limescale context (SRC-BOOK-4CH1-SB1,
edexcel_igcse_chemistry_chunks_v3.jsonl line 253). Temporal scope: CURRENT —
AUTHORITATIVE.

### PED-024 — Alternative-route hints

**Claim:** explanation hints offer a second route to the same result rather than
introducing a different claim.
**Evidence:** a mole-ratio step is re-explained as "Another way of thinking about
this" — divide by three, then multiply by two (SRC-BOOK-4CH1-SB1,
edexcel_igcse_chemistry_chunks_v3.jsonl line 244). Temporal scope: CURRENT —
AUTHORITATIVE.

### PED-025 — Diagram-first explanations for structure and process

**Claim:** structural and process topics lead with diagrams — energy level
diagrams for enthalpy changes, figure-led deduce-the-polymerisation procedures —
with the prose wrapped around the visual.
**Evidence:** endothermic change is explained on an energy level diagram where
"the products have more energy than the reactants" (SRC-BOOK-4CH1-SB1,
edexcel_igcse_chemistry_chunks_v3.jsonl line 724); polymerisation is taught
through a figure-led "HOW TO DEDUCE THE POLYMERISATION REACTION FOR ANY ALKENE"
procedure (SRC-BOOK-4CH1-SB1, edexcel_igcse_chemistry_chunks_v3.jsonl line
1036). Temporal scope: CURRENT — AUTHORITATIVE.

### PED-026 — Examiner-verified explanation routes

**Claim:** the examiner's own commentary verifies that multiple explanation
routes are rewarded, and names where explanation effort concentrates.
**Evidence:** the 2023-06 report states "Candidates have different ways of
approaching calculations" and that full credit was given for mole-based and
other valid routes alike (SRC-ER-4CH1, er.pdf p 34); the same report names
poly(propene) as the structure candidates find hardest to draw because of the
side chain (SRC-ER-4CH1, er.pdf p 17); it also flags the paired water tests as a
standing confusion point (SRC-ER-4CH1, er.pdf p 46). Temporal scope: CURRENT —
AUTHORITATIVE.

### PED-027 — Spec-point-bound strategy notes

**Claim:** the notes corpus packages the same strategies at note grain, bound to
spec points and closed with exam-hint cautions.
**Evidence:** the separation-techniques note binds each technique section to its
spec point with typed ids, from simple distillation onward
(SRC-SME-NOTES-4CH1, 2-3-separation-techniques.md lines 11-25); its exam hint
instructs that condenser water "goes in at the bottom" near the collecting beaker
(SRC-SME-NOTES-4CH1, 2-3-separation-techniques.md lines 32-46). Temporal scope:
CURRENT — AUTHORITATIVE.

## Evidence / Source Basis

Primary evidence: SRC-BOOK-4CH1-SB1 (imagine-anchored, model-limited,
worked-example, hint, and diagram chunks at line+chunk-id locators) and
SRC-TL-4CH1 (bonding/equilibrium strategy guides; Getting Started Guide pages;
identity-pinned scheme-of-work entry). Supplementary: SRC-ER-4CH1 (2023-06
Paper 1C examiner-report pages with session identity preserved via the pack file
path); SRC-SME-NOTES-4CH1 spec-point-bound notes; SRC-SPEC-4CH1 held for
context pages. Bounded excerpts with locators preserved; caps enforced by the
pack builder.

## Limitations / Coverage Gaps

The strategy devices catalogued are those visible in this pack's query windows
only; further imagine-style passages outside the window are neither enumerated
nor denied. The equilibrium guide's internal sequence is cited at the level its
excerpted pages show. The legacy examiner-report entry is present for identity
only; no legacy claim is made. No canonical planes were written.

## Research Status

GENERATED under SIB-CHEMISTRY_4CH1-RUN-006 (BL-008 pass 6) from this artifact's
evidence pack alone; validator of record tools/sib @ 357ace0a; claim QA r3 binds
every citation to a pack excerpt. Research artifact — evidence-backed, not
canonical educational truth.
