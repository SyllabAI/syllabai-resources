---
sib_protocol: SIB-1.0
artifact_id: PRO-05
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

# PRO-05 — Dead Ends and Failed Approaches

## Purpose

This artifact catalogues the dead ends and failed approaches of record in 4CH1:
the wrong-answer rationales published inside the official mark schemes' multiple
choice keys, the named fatal dead ends that score zero, the IGNORE/REJECT
fences around near-miss wording, the credited failure analyses of practical
work, the Rf dead end the book disarms in advance, and the teaching-side dead
end the publisher's own topic guide dismantles of SRC-QPMS-4CH1, SRC-BOOK-4CH1-SB1 and SRC-TL-4CH1. Claims ride only on this artifact's own bounded pack excerpts.
Canonical planes are untouched.

## Scope

**Covers:** distractor rationales as published dead ends; zero-score traps;
IGNORE/REJECT wording fences; credited practical failure analyses; the
insoluble-dye dead end; the principle-first equilibrium critique.

**Out of scope:** misconception taxonomy (MIS family) and diagnostic teaching
(PED-09).

## Executive Summary

Dead ends in 4CH1 are not left for learners to discover: the mark schemes
publish them. Every multiple-choice key explains why each wrong option is wrong
("A is not correct as the crystal does not condense"), turning the distractor
set into a catalogue of failed approaches. Some dead ends are named as fatal —
mentioning bond-breaking where intermolecular forces are demanded scores zero.
Near-miss wording is fenced with IGNORE and REJECT classes so the boundary
between almost-right and wrong is explicit. Practical failure modes are
credited analysis targets: gas escaping before the bung is replaced, impure
magnesium with an oxide coating. The book disarms one dead end in advance — a
dye that never leaves the pencil line was never soluble in that solvent — and
the publisher's equilibrium guide names the field's own failed approach
(principle-first teaching) and replaces it with rule application.

## Main Analysis

### PRO-027 — Distractor rationales as published dead ends

**Claim:** the official keys explain every wrong option, publishing the dead
end behind each distractor.
**Evidence:** the dissolving key rules out each option in turn — "A is not
correct as the crystal does not condense", with evaporation and melting ruled
out the same way (SRC-QPMS-4CH1, 2019-06/4CH1-1C/questions.md lines 22-36); the
helium key dismisses colour, solubility and smell as "irrelevant" to the
property that matters (SRC-QPMS-4CH1, 2019-06/4CH1-1C/questions.md lines
343-357). Temporal scope: CURRENT — AUTHORITATIVE.

### PRO-028 — The named fatal dead end

**Claim:** one reasoning dead end is named as fatal: invoking bond-breaking
where intermolecular forces are the demand scores zero.
**Evidence:** the melting-point explanation scheme warns "Any mention of
covalent bonds/ionic bonds/metallic bonds breaking scores 0 out of 2" while
crediting the intermolecular-forces route (SRC-QPMS-4CH1,
2019-06/4CH1-1C/questions.md lines 726-740). Temporal scope: CURRENT —
AUTHORITATIVE.

### PRO-029 — IGNORE and REJECT fences around near-miss wording

**Claim:** near-miss wording is fenced explicitly — tolerated irrelevances are
IGNOREd, named wrong answers are REJECTed.
**Evidence:** the alkene-test scheme requires decolourised, marks "IGNORE
clear", and REJECTs a named wrong observation (SRC-QPMS-4CH1,
2019-06/4CH1-1C/questions.md lines 611-625); the displacement scheme IGNOREs
references to the magnesium disappearing and to heat (SRC-QPMS-4CH1,
2019-06/4CH1-1C/questions.md lines 464-481); the conductivity scheme IGNOREs
the "sea of electrons" phrasing while crediting delocalised electrons able to
flow (SRC-QPMS-4CH1, 2019-06/4CH1-1C/questions.md lines 521-537). Temporal
scope: CURRENT — AUTHORITATIVE.
### PRO-030 — Practical failure modes as credited analysis

**Claim:** failed practical approaches are examined as credited analysis: the
mark scheme names the classic failure modes of a gas-volume investigation.
**Evidence:** the rate-investigation scheme credits "M1 some gas escapes before
the bung is" replaced and "M2 the magnesium is impure/ the magnesium ribbon has
an oxide coating" (SRC-QPMS-4CH1, 2019-06/4CH1-1C/questions.md lines
1076-1093). Temporal scope: CURRENT — AUTHORITATIVE.

### PRO-031 — The Rf dead end disarmed in advance

**Claim:** the book pre-empts the chromatography dead end — a stationary dye
spot — by stating its cause directly.
**Evidence:** the chromatography KEY POINT states "If the dye does not move
from the pencil line during an experiment, then the dye is not at all soluble in
the solvent you are using" (SRC-BOOK-4CH1-SB1,
edexcel_igcse_chemistry_chunks_v3.jsonl line 77); the Rf caution adds the
solvent-and-paper dependence that invalidates cross-experiment comparison
(SRC-BOOK-4CH1-SB1, edexcel_igcse_chemistry_chunks_v3.jsonl line 82).
Temporal scope: CURRENT — AUTHORITATIVE.

### PRO-032 — The teaching-side dead end: principle-first equilibrium

**Claim:** the publisher's own topic guide names a field-level failed approach —
teaching equilibrium through Le Chatelier's principle first — and replaces it
with rule application on worked cases.
**Evidence:** the guide opens from the Allsop and George argument that use of
the principle was "counterproductive to the understanding of chemical
equilibrium" (SRC-TL-4CH1, Chemical-equilibrium---FINAL.pdf p 2); its recovery
route works the rules on stated cases such as the methanol-manufacture
equilibrium (SRC-TL-4CH1, Chemical-equilibrium---FINAL.pdf p 3). Temporal
scope: CURRENT — AUTHORITATIVE.

### PRO-057 — The octet-stability misconception named and quantified

**Claim:** the publisher's bonding guide names the octet-stability belief as a misconception and quantifies its reach: a large majority of tested students held that an ion is more stable than the parent atom, and the guide states flatly that this is not so — energy must be supplied to form either ion, so both sit at higher energy. The dead end is therefore documented with its own evidence base, not merely asserted.
**Evidence:** the guide states the belief "species with full outer shells or outer shell octet" configurations are "more energetically stable than species with other electronic configurations" and answers "This is very far from the truth"; it reports "One study showed that over 97% of the 15-16 year olds tested believed that a Na+ ion was more stable than a sodium atom" (SRC-TL-4CH1, igcse-chemistry/teaching-and-learning-materials/Chemical-bonding---FINAL.pdf p2).
Temporal scope: CURRENT — AUTHORITATIVE.

### PRO-058 — The octet-teleology fence and its Period-2 scope

**Claim:** the guide fences a second, subtler dead end — purpose language: students must not leave with the impression that atoms bond in order to acquire an octet, because that is not why bonding happens. The same guide bounds the octet rule's own scope to four Period-2 elements and names the Group 2 exceptions, so both the teleology and the over-generalisation are fenced in one place.
**Evidence:** the guide prints that students should not gain the impression that atoms bond "in order to acquire an octet of electrons in the outer shell of their atoms" because "This is not the reason for bonding taking place", and that the octet rule "applies only to these four elements in Period 2" (SRC-TL-4CH1, igcse-chemistry/teaching-and-learning-materials/Chemical-bonding---FINAL.pdf p8).
Temporal scope: CURRENT — AUTHORITATIVE.

### PRO-059 — The ignored-observation stack on one mark point

**Claim:** a single observation point can carry a stack of named irrelevances: the magnesium and silver-nitrate observation scheme prints the credited observation with its colour alternates, then ignores clear, incorrect initial colour, references to the metal disappearing, and references to heat — four distinct wrong observations, each named and dismissed on the same point. The stack shows the dead ends are inventoried at the granularity of the individual point.
**Evidence:** the scheme prints "M1 brown/pink/pink-brown solid forms ALLOW red-brown /orange-brown" with "IGNORE red or orange alone" and "ALLOW precipitate for solid", and "M2 solution turns colourless ALLOW solution becomes paler" with "IGNORE clear", "IGNORE incorrect initial colour of solution" and "IGNORE references to magnesium disappearing" (SRC-QPMS-4CH1, 2019-06/4CH1-1C/questions.md lines 457-471).
Temporal scope: CURRENT — AUTHORITATIVE.


## Evidence / Source Basis

Primary evidence: SRC-QPMS-4CH1 (2019-06 Paper 1C key rationales, fences, and
failure-mode marks with paper identity preserved via the pack file path) and
SRC-BOOK-4CH1-SB1 (chromatography dead-end chunks at line+chunk-id locators).
Supplementary: SRC-TL-4CH1 equilibrium topic guide. Bounded excerpts with
locators preserved; caps enforced by the pack builder.

## Limitations / Coverage Gaps

Dead ends are catalogued from this pack's excerpt windows; the full fence
inventory across sessions is neither enumerated nor denied. Mark-scheme
rationales are cited as published key statements only; the MS family owns the
systematic mark-layer analysis, and no mark_points plane data is consumed or
written. No examiner sentiment is synthesized from mark schemes. OCR-era quirks
are quoted as parsed or paraphrased, never repaired. No canonical planes were
written.

## Research Status

GENERATED under SIB-CHEMISTRY_4CH1-RUN-006 (BL-008 pass 6) from this artifact's
evidence pack alone; validator of record tools/sib @ 357ace0a; claim QA r3 binds
every citation to a pack excerpt. Deepened under SIB-CHEMISTRY_4CH1-RUN-019 (D3 tranche 3): +3 records (PRO-057..059), zero-append mining of the carried pack of record; every quote self-bound to raw excerpt text before the official gate; claim QA re-bound all citations. Research artifact — evidence-backed, not
canonical educational truth.
