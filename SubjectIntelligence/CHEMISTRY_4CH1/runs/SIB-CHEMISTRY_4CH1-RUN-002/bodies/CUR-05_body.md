# CUR-05 — Prerequisite Knowledge Map

## Purpose

This artifact is the prerequisite map of the CHEMISTRY_4CH1 curriculum at the
specification-point grain: the complete, operator-ratified REQUIRES_PREREQUISITE store
plus its RELATED_TO complement, read as learning-order law. Where CUR-04 classified
the concept-level relationship vocabulary, CUR-05 works at the official statement
grain — which statement requires which prior statement — because that is the grain at
which teaching sequence and gap diagnosis are actually planned. It is a research
artifact grounded on the run's evidence pack; the canonical planes remain authoritative
and read-only to this pipeline.

## Scope

**Covers:** the entire point-edge store of record — 35 edges, every one
OPERATOR_RATIFIED with confidence 1.0 — comprising 30 REQUIRES_PREREQUISITE edges and
5 RELATED_TO edges across the four topics; the direction contract declared by the
store's meta block; the official wording of the anchor statements involved; and the
intra-topic boundary of the store (zero cross-topic point edges of record).
Temporal scope is CURRENT — AUTHORITATIVE; no legacy material is used or cited.

**Does not cover:** concept-grain dependencies (CUR-04/06's ground), teaching
methodology (PED), or any claim that the ratified store is exhaustive of all real
prerequisites — it is the RATIFIED subset of record, and its boundaries are stated,
not hidden.

## Executive Summary

- The point-edge store of record holds exactly 35 edges — 30 REQUIRES_PREREQUISITE
  and 5 RELATED_TO — all validated OPERATOR_RATIFIED at confidence 1.0
  (RUN-COMPUTED: census.json, point_edges.edges;
  census.json, point_edges.relation_distribution;
  census.json, point_edges.validation_distribution).
- Every REQUIRES_PREREQUISITE edge is intra-topic: S1 carries 11, S2 5, S3 5, S4 9;
  there are zero cross-topic point edges of record (RUN-COMPUTED: census.json,
  point_edges.cross_topic_point_edges).
- The store's direction contract is V2-native: `from` requires, `to` is the
  prerequisite — exemplified by p:1.19 REQUIRES_PREREQUISITE p:1.18 (electronic
  configurations require Periodic Table arrangement) (SRC-GRAPH-4CH1, lines 32-46).
- Concept-grain prerequisite edges (209 of record, CUR-04) are a denser, partially
  AI-suggested layer above this fully-ratified statement-grain spine; the two layers
  agree in direction law but differ in validation tier.

## Main Analysis

### CUR-024 — The store and its law

The point-edge store is small, ratified and contract-bound: 35 edges, each carrying
validation_status OPERATOR_RATIFIED and confidence 1.0 (RUN-COMPUTED: census.json,
point_edges.validation_distribution); every in-pack edge window shows the same
record shape (from, relation, to, kg_direction, validation_status, confidence,
version) (SRC-GRAPH-4CH1, lines 32-46; SRC-GRAPH-4CH1, lines 752-766). The meta
block declares the direction contract: "REQUIRES_PREREQUISITE rows are V2-native:
from REQUIRES to (to is the prerequisite). The kg exporter maps them to the
canonicalKG 'pre' contract by flipping: golden [to, from, 'pre']. RELATED_TO rows are
stored verbatim and exported 1:1" (SRC-GRAPH-4CH1, lines 32-46 context; store meta).
Consumers must therefore read p:A REQUIRES_PREREQUISITE p:B as "A requires B" — and
note that the canonical KG export flips the pair, so any cross-plane join must apply
the documented flip rather than raw field equality. This is the only store in the
wave where every row is operator-ratified, which makes it the dependable spine for
sequencing claims.

### CUR-025 — S1: the atomic-structure-to-bonding spine and the mole chain

S1 carries 11 of the 30 prerequisite edges (RUN-COMPUTED: census.json,
point_edges.relation_distribution) — with in-pack windows lines 32-286
(SRC-GRAPH-4CH1, lines 32-46). Three chains
structure the topic. First, the Periodic-Table spine: 1.19 (deduce electronic
configurations of the first 20 elements from Periodic Table position) requires 1.18
(how elements are arranged in the Periodic Table) (SRC-GRAPH-4CH1, lines 32-46;
SRC-GRAPH-4CH1, lines 436-450; SRC-GRAPH-4CH1, lines 481-495), and 1.22 (electronic
configuration relates to position) requires 1.19 (SRC-GRAPH-4CH1, lines 56-70;
SRC-GRAPH-4CH1, lines 654-668) — a three-step chain ending at statement 1.18. Second,
the mole chain: 1.28 (calculations involving amount of substance, Ar, Mr) requires
both 1.25 (equations) and 1.27 (the mole), and 1.29 requires 1.28
(SRC-GRAPH-4CH1, lines 80-94; SRC-GRAPH-4CH1, lines 104-118; SRC-GRAPH-4CH1,
lines 128-142; SRC-GRAPH-4CH1, lines 915-929). Third, the bonding lattice: 1.42 and
1.43 each require 1.41 (ionic bonding), 1.46 requires 1.44 (covalent bonding), 1.47
requires 1.45, with 1.39 requiring 1.37 upstream (SRC-GRAPH-4CH1, lines 152-166;
SRC-GRAPH-4CH1, lines 176-190; SRC-GRAPH-4CH1, lines 200-214; SRC-GRAPH-4CH1,
lines 224-238; SRC-GRAPH-4CH1, lines 248-262). The electrolysis pair closes the
topic: 1.58C requires 1.57C (SRC-GRAPH-4CH1, lines 272-286). The teaching-order
consequence is direct: no learner meets 1.42/1.43 profitably before 1.41, and the
entire calculation strand hangs from the 1.25/1.27 double root.

### CUR-026 — S2: reactivity and acid-base chains

S2 carries 5 prerequisite edges (in-pack windows lines 296-430). The reactivity
chain: both 2.17 (Group 7 displacement reactions) and 2.20 (oxidation-reduction in
terms of electron transfer) require 2.15 (the reactivity series context)
(SRC-GRAPH-4CH1, lines 296-310; SRC-GRAPH-4CH1, lines 320-334). The acid-base chain
runs 2.31 → 2.29, then 2.32 requires 2.31: the solution-ionisation statement (2.31,
"know that acids in aqueous solution are a source of hydrogen ions and alkalis in a
aqueous solution are a source of hydroxide ions", verbatim including the
specification's own article typo) is itself downstream of 2.29 and upstream of the
neutralisation frame (SRC-GRAPH-4CH1, lines 344-358; SRC-GRAPH-4CH1, lines 392-406;
SRC-GRAPH-4CH1, lines 3659-3673). The salt-preparation edge 2.36 → 2.35 completes
the topic (SRC-GRAPH-4CH1, lines 368-382). Downstream consequence: the acid-base
spine is a strict linear order (2.29 → 2.31 → 2.32), so diagnostic failures at 2.31
propagate to every neutralisation demand later in the course.

### CUR-027 — S3: energetics, rates and equilibria

S3 carries 5 prerequisite edges (in-pack windows lines 416-526). Energetics: 3.5C
(energy level diagrams) requires 3.1 (the exothermic/endothermic classification), and
3.7C (bond-energy calculations) requires 3.6C (bond-breaking endothermic /
bond-making exothermic) (SRC-GRAPH-4CH1, lines 416-430; SRC-GRAPH-4CH1, lines
440-454). Rates: 3.11 requires 3.9 (SRC-GRAPH-4CH1, lines 464-478). Equilibria: 3.14C
requires 3.13, and the C-suffixed pair 3.20C requires 3.19C (SRC-GRAPH-4CH1, lines
488-502; SRC-GRAPH-4CH1, lines 512-526). Note the tier pattern: both energetics
edges end in C-suffixed statements, consistent with the Paper 2 placement of deeper
energetics work recorded at CUR-02 — the prerequisite map and the paper-content
partition tell the same story from independent directions.

### CUR-028 — S4: the organic chains

S4 carries 9 prerequisite edges, the largest topic share (in-pack windows lines
536-742). The industrial pair opens it: 4.8 (fractional distillation of crude oil)
requires 4.7 (crude oil as a mixture) (SRC-GRAPH-4CH1, lines 536-550). The homologous
chains follow: 4.20 requires 4.19; 4.25 and 4.27 both require 4.23; the C-suffixed
cluster 4.31C and 4.32C each require 4.29C; 4.36C requires 4.34C; 4.40C requires
4.39C; and 4.46 requires 4.44 (SRC-GRAPH-4CH1, lines 560-574; SRC-GRAPH-4CH1,
lines 584-598; SRC-GRAPH-4CH1, lines 608-622; SRC-GRAPH-4CH1, lines 632-646;
SRC-GRAPH-4CH1, lines 656-670; SRC-GRAPH-4CH1, lines 680-694; SRC-GRAPH-4CH1,
lines 704-718; SRC-GRAPH-4CH1, lines 728-742). Six of the nine S4 edges terminate in
C-suffixed statements — the organic chemistry extension demand is structurally
stacked, which is why the official topic page order (S4 spanning printed pages
23 onward) is also a dependency order here (SRC-SPEC-4CH1, page 29).

### CUR-029 — The RELATED_TO complement and the intra-topic boundary

Five RELATED_TO edges complement the prerequisite spine: 1.59C ↔ 1.60C (electrolysis
of molten binary compounds and of aqueous solutions — the two electrolysis contexts),
2.34 ↔ 2.37 (metals + acids with salt preparations), 3.22C ↔ 3.21C, 4.8 ↔ 4.9
(fractional distillation with the fractions and their uses), 4.27 ↔ 4.28
(SRC-GRAPH-4CH1, lines 752-766; SRC-GRAPH-4CH1, lines 776-790; SRC-GRAPH-4CH1,
lines 800-814; SRC-GRAPH-4CH1, lines 824-838; SRC-GRAPH-4CH1, lines 848-862).
RELATED_TO rows are stored verbatim and exported 1:1 per the direction contract —
they are associations, not orderings, and must never be compiled into teaching
sequence (store meta law; SRC-GRAPH-4CH1, lines 32-46). The boundary finding of
record: zero of the 35 point edges cross topic boundaries (RUN-COMPUTED: census.json,
point_edges.cross_topic_point_edges) — at the official statement grain, the ratified
dependency structure of 4CH1 is entirely intra-topic. Cross-topic connectivity that
DOES exist of record lives at the concept grain (24 genuine cross-topic concept
edges; RUN-COMPUTED: census.json, concept_edges.genuine_cross_topic_edges.count) and
is synthesized in CUR-06.

### CUR-030 — Consumption contract for downstream families

Three rules govern any consumer of this map. First, direction: sequence must flow
from prerequisite to dependent — teaching order within S1's bonding subtopic is 1.41
before 1.42/1.43, within S2's acids subtopic 2.29 before 2.31 before 2.32, and the
canonical-KG export's flipped pairs must be un-flipped before use
(SRC-GRAPH-4CH1, lines 32-46; SRC-GRAPH-4CH1, lines 176-190; SRC-GRAPH-4CH1,
lines 392-406). Second, tier discipline: the 35 point edges are all
OPERATOR_RATIFIED and are the dependable spine; concept-grain REQUIRES_PREREQUISITE
edges (CUR-04, 209 of record at mixed validation tiers) may enrich but not override
the ratified spine (RUN-COMPUTED: census.json, point_edges.validation_distribution;
census.json, concept_edges.validation_distribution). Third, gap honesty: the store is
the RATIFIED subset, not the full prerequisite truth of the subject — an unlisted
statement pair is undiagnosed, not diagnosed-as-independent, and remediation
planning (TUT/MIS families) must treat missing edges as open questions rather than
proofs of independence.

## Evidence / Source Basis

- **CURRENT — AUTHORITATIVE:** SRC-GRAPH-4CH1 — validated curriculum graph:
  point_edges.yaml (the complete 35-edge ratified store, meta direction contract),
  specification_points.yaml (anchor statement wording), verified at run preflight.
  Read-only plane for this pipeline.
- **CURRENT — AUTHORITATIVE:** SRC-SPEC-4CH1 — official specification PDF, Issue 3
  (page 15, topic structure context; page 29 for S4's printed position), sha1 of
  record 3ad641b7c60b314fa3b10680feda30bf56280a53, verified at run preflight.
- **CURRENT — AUTHORITATIVE / SUPPLEMENTARY:** SRC-TL-4CH1 — Getting Started Guide
  (page 3) as identity/context row.
- **CURRENT — ASSESSMENT EVIDENCE (specimen):** SRC-SAMS-4CH1 — page 1 identity-only
  row.
- **RUN-COMPUTED:** census.json — deterministic counts over the graph stores of
  record; verified by the run's evidence-claim QA.

## Limitations / Coverage Gaps

- The map is the RATIFIED subset of record (35 edges); it is not claimed to be the
  complete prerequisite truth of 4CH1, and unlisted pairs are undiagnosed, not
  disproven.
- The store's meta block documents a canonical-KG export flip ([to, from, 'pre']);
  any cross-plane consumer must apply it — a consumer reading raw pairs against the
  golden export will invert every dependency.
- Anchor statement wording quoted here is verbatim from the specification-point
  store, including the preserved typo at 2.31; the wording authority remains the
  official PDF (sha1 3ad641b7…).
- Cross-topic prerequisite structure is absent at this grain by the store's own
  content (zero rows); the concept-grain cross-topic edges (CUR-06) are a different
  store with a different validation tier, and the two must not be conflated.
- The RELATED_TO edges are associations by contract; any sequencing use of them is a
  violation of the store's declared law.

## Research Status

status: GENERATED (research artifact; not educational truth, not canonical curriculum
truth). Generated by the SIB-GEN batch run SIB-CHEMISTRY_4CH1-RUN-002 under the
provider-neutral pipeline (BL-008 wave 1, protocol §4 pass 2), grounded exclusively on
the run's CUR-05 evidence pack (pack sha256 of record in the run manifest) plus the
run's deterministic census annex. Current/legacy separation: fully CURRENT; no legacy
claims. Determinism: content fingerprint of this artifact is recorded in the run
manifest; regeneration produces a new artifact_version.
