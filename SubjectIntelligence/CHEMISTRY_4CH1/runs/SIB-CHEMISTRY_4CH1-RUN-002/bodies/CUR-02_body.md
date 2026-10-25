# CUR-02 — Specification Interpretation

## Purpose

This artifact is the interpretation layer of the CHEMISTRY_4CH1 curriculum-intelligence
family: it states what the specification's statements DEMAND, not merely what they say.
Where CUR-01 fixes the qualification skeleton (papers, weightings, topics, subtopics,
practicals), CUR-02 works one grain deeper — how each of the 182 specification
statements is phrased as a demand (know / understand / describe / calculate / draw /
explain / investigate / write), how those demands are classified into seven guide
classes in the validated command-kind store, how the bold/'C' convention partitions
content between Paper 1 and Paper 2, and where the interpretation layer's own coverage
has honest gaps. Every downstream family that turns curriculum wording into teaching or
assessment behavior (EXP explanations, ASM question archetypes, PRA practical guidance,
TUT tutoring moves) inherits its demand vocabulary from this artifact. It is a research
artifact grounded on the run's evidence pack; the canonical planes of SyllabAI remain
authoritative, and this pipeline treats them read-only.

## Scope

**Covers:** the demand-verb taxonomy of the 4CH1 specification statements as recorded in
the validated command-kind store (spec_command_kinds.yaml: 181 classified statements,
seven guide classes); the statement-entry law of the specification-point store
(official wording, section/subsection placement, 'C' flag, practical flag, per-paper
applicability with the Double Award sharing rule); the official presentation of the
content section in the specification PDF (topic structure, "Students should:" framing,
bold/'C' marking); and the coverage boundary of the interpretation layer itself (the
one statement absent from the command-kind store, and the one verb-count discrepancy it
explains). Temporal scope is CURRENT — AUTHORITATIVE throughout; no legacy material is
used or cited.

**Does not cover:** the concept-level graph (CUR-03/04), prerequisite structure
(CUR-05), the qualification-level skeleton (CUR-01), assessment behavior of real
sessions (ASM/MS/EXM families), or the wording of teaching guidance (PED). Where this
artifact interprets a statement's demand, it does so at the grain of the validated
store's own class assignments; it does not re-classify statements the store leaves
unclassified.

## Executive Summary

- The validated command-kind store classifies 181 of the 182 specification statements
  into seven demand classes; the single gap is 4CH1-4.15 (RUN-COMPUTED:
  census.json, command_kinds.coverage_gap_vs_spec_points).
- KNOW_TERM is the largest class (60 of 181, 33.2%), followed by UNDERSTAND_RELATION
  (45, 24.9%) and DESCRIBE_EXPERIMENT (34, 18.8%); CALCULATE (12),
  REPRESENT_DIAGRAM (18), EXPLAIN_HOW (9) and PRODUCE_EQUATION (3) complete the
  taxonomy (RUN-COMPUTED: census.json, command_kinds.guide_class_distribution).
- The 'C'-suffix law is carried per statement in machine-readable form: C-suffixed
  statements are Paper 2-only and are NOT shared with Science Double Award 4SD0
  (exemplars 1.5C, 1.7C: papers [2C], double_award_shared: false), while non-suffixed
  statements are shared and assessed in both papers (exemplar 1.1: papers [1C, 2C]).
- The interpretation layer inherits two disclosed defects honestly: statement 4.15 is
  present in the specification-point store (verb "explain") but absent from the
  command-kind store, which also explains the 16-vs-15 "explain" verb delta between
  the two stores; and one official wording carries a verbatim typo ("in a aqueous
  solution" at 2.31) preserved by the store's damage-preservation law.

## Main Analysis

### CUR-001 — The seven demand classes and their law

The validated command-kind store assigns every classified statement a verb, a guide
class, and a demanded substance (the substance the statement actually requires the
learner to command) (SRC-GRAPH-4CH1, lines 259-273). The seven classes observed in the
store, with in-pack exemplars: KNOW_TERM — definitional recall demands, e.g. 1.14
("definitions of the terms atom and molecule") and 2.31 ("acids in aqueous solution as
sources of hydrogen ions and alkalis … as sources of hydroxide ions — the
solution-ionisation picture that makes a solution acidic or alkaline")
(SRC-GRAPH-4CH1, lines 279-293; SRC-GRAPH-4CH1, lines 708-722);
UNDERSTAND_RELATION — relational understanding demands, e.g. 1.1 (particle-level
description of the three states with the simple sphere model) and 1.41 (ionic bonding
as electrostatic attraction between oppositely charged ions acting in all directions)
(SRC-GRAPH-4CH1, lines 259-273; SRC-GRAPH-4CH1, lines 420-434);
DESCRIBE_EXPERIMENT — experimental description demands, e.g. 1.10 (the separation
techniques and what each separates) and 1.7C (the solubility practical: saturate,
evaporate, heat to constant mass, calculate) (SRC-GRAPH-4CH1, lines 264-278;
SRC-GRAPH-4CH1, lines 536-550); REPRESENT_DIAGRAM — e.g. 1.40 (dot-and-cross diagrams
for ionic compound formation, outer electrons only, bracketed charges)
(SRC-GRAPH-4CH1, lines 420-434); CALCULATE — e.g. 1.26 (Mr calculation procedure),
1.34C (concentration/volume calculations) and 1.35C (molar gas volumes at RTP)
(SRC-GRAPH-4CH1, lines 342-356; SRC-GRAPH-4CH1, lines 387-401); PRODUCE_EQUATION —
e.g. 1.25 (word equations and balanced symbol equations with state symbols)
(SRC-GRAPH-4CH1, lines 342-356); and EXPLAIN_HOW (class present in the store's
distribution; RUN-COMPUTED: census.json, command_kinds.guide_class_distribution).
The demanded-substance fields are themselves interpretation of record: they expand
list-shaped statements (1.10's wording ends in a colon; the demanded substance names
simple distillation, fractional distillation, filtration, crystallisation and paper
chromatography) and carry the store's own examiner tips where ratified (3.10's rate
factors are flagged "a recall demand per the note's own examiner tip")
(SRC-GRAPH-4CH1, lines 867-881; SRC-GRAPH-4CH1, lines 985-999).

### CUR-002 — KNOW_TERM is the load-bearing class

KNOW_TERM is the single largest demand class: 60 of 181 classified statements, 33.2%
(RUN-COMPUTED: census.json, command_kinds.guide_class_distribution). Its spread is
not confined to one topic: in-pack exemplars run from S1 language (1.14 atom and
molecule; 1.15 atomic structure) through S2 fact demands (2.5 halogen colours, states
and trends; 2.13 carbon dioxide as a greenhouse gas) to S3/S4 classification knowledge
(3.1 exothermic/endothermic; 4.1 the hydrocarbon definition with its "only" qualifier;
4.12 complete vs incomplete combustion products) (SRC-GRAPH-4CH1, lines 279-293;
SRC-GRAPH-4CH1, lines 831-845; SRC-GRAPH-4CH1, lines 867-881; SRC-GRAPH-4CH1,
lines 985-999; SRC-GRAPH-4CH1, lines 1000-1014). The interpretation consequence is
direct: a third of the specification's demands are definitional or factual recall
grain, which is why the terminology layer (CUR-07) and the misconception-atlas' error
grain (MIS family) matter at exactly this depth rather than deeper.

### CUR-003 — The quantitative strand: CALCULATE and PRODUCE_EQUATION

CALCULATE holds 12 statements and PRODUCE_EQUATION 3 (RUN-COMPUTED: census.json,
command_kinds.guide_class_distribution). The in-pack exemplars show where the
quantitative demand sits: formula-mass calculations (1.26), mole-based stoichiometry
(1.27 context), empirical/molecular formulae from experimental data, concentration and
gas-volume arithmetic (1.34C, 1.35C) in S1, and calorimetry arithmetic (Q = mcΔT, molar
enthalpy) in S3 (SRC-GRAPH-4CH1, lines 342-356; SRC-GRAPH-4CH1, lines 387-401;
SRC-SPEC-4CH1, page 27). Two of the exemplar calculation demands are 'C' statements,
which places the deeper quantitative work (concentration, gas volumes) in Paper 2
territory by the paper-content rule (SRC-SPEC-4CH1, page 13); the interpretation layer
therefore expects calculation-heavy extended items in Paper 2 and core-grain
arithmetic (Mr, Rf from chromatograms — 1.12 is classed CALCULATE) in Paper 1
(SRC-GRAPH-4CH1, lines 264-278; SRC-GRAPH-4CH1, lines 342-356).

### CUR-004 — Practical demand: class law and practical flag

DESCRIBE_EXPERIMENT holds 34 statements (RUN-COMPUTED: census.json,
command_kinds.guide_class_distribution), and the investigation verb leads seven
statements (RUN-COMPUTED: census.json, command_kinds.verb_distribution). The in-pack
exemplars show the class covering both named practical methods (1.7C solubility
determination; 1.60C electrolysis of aqueous solutions with product identification via
gas tests; 2.14 the iron-wool determination of oxygen in air with its ~20% expected
result) and technique descriptions (1.10 separation techniques; 1.13 the
paper-chromatography practical with pencil baseline and solvent-below-start-line
discipline) (SRC-GRAPH-4CH1, lines 264-278; SRC-GRAPH-4CH1, lines 536-550;
SRC-GRAPH-4CH1, lines 521-535; SRC-GRAPH-4CH1, lines 867-881). The statement store
additionally carries a machine-readable practical flag distinguishing statements that
ARE Core Practicals (exemplar 1.7C: practical: true) from statements that merely
demand experimental description (exemplar 1.10: practical: false) (SRC-GRAPH-4CH1,
lines 2498-2512; SRC-GRAPH-4CH1, lines 84-98). Both signals matter downstream: the
practical flag anchors PRA-family artifacts to the twelve Core Practicals, while the
DESCRIBE_EXPERIMENT class predicts the AO3 examination surface beyond the named
practicals.

### CUR-005 — The papers applicability law, carried per statement

The specification states the partition plainly: Paper 1 "assesses core content that is
not in bold and does not have a 'C' reference", Paper 2 assesses all content
(SRC-SPEC-4CH1, page 13). The statement store carries this per statement as data:
non-suffixed 1.1 carries papers [1C, 2C] with the sharing rule "non-suffixed
statements are shared with Science Double Award 4SD0 and assessed in both Paper 1C and
Paper 2C" (SRC-GRAPH-4CH1, lines 41-55), while C-suffixed 1.5C ("know what is meant by
the term solubility in the units g per 100 g of solvent") and 1.7C (the solubility
practical) carry papers [2C] and double_award_shared: false (SRC-GRAPH-4CH1,
lines 2374-2388; SRC-GRAPH-4CH1, lines 2498-2512). The same law reads off the official
topic pages: S1 statements 1.1-1.4 appear unmarked while 1.5C appears with the C
suffix in the "Students should:" list (SRC-SPEC-4CH1, page 17). Interpretation
consequence for every downstream family: a bold/'C' statement is simultaneously
(a) Paper 2 territory and (b) not part of the 4SD0 Double Award route — two different
boundaries that the single C suffix encodes, and which CUR-08 treats as boundary law.

### CUR-006 — Wording authority and damage preservation

The specification-point store is the wording authority of record: its official_wording
fields are verbatim from the official PDF (canonical PDF-direct parse,
whitespace-normalised only), and its lineage block retires the earlier markdown-lineage
extraction in favor of the definitive wording authority
(SRC-GRAPH-4CH1, lines 41-55). Damage preservation is observable in-pack: 2.31's
official wording reads "alkalis in a aqueous solution" — the specification's own
article typo, preserved verbatim and never silently repaired (SRC-GRAPH-4CH1,
lines 3659-3673). List-shaped statements keep their colon-and-list presentation
(1.10's wording ends with a colon), with the demanded substance carrying the expanded
content (SRC-GRAPH-4CH1, lines 84-98; SRC-GRAPH-4CH1, lines 264-278). Downstream
families quoting specification wording MUST quote through this store's verbatim fields
or the PDF itself — paraphrase presented as quotation is the failure mode this law
exists to prevent.

### CUR-007 — The 181/182 coverage gap is one statement, and it explains the verb delta

The command-kind store classifies 181 statements; the specification-point store holds
182 (RUN-COMPUTED: census.json, command_kinds.entries;
census.json, specification_points.total). The gap is exactly 4CH1-4.15 — "explain how
the combustion of some impurities in hydrocarbon fuels results in the formation of
sulfur dioxide" (S4-b, papers [1C]) — present in the statement store with leading verb
"explain" but absent from the command-kind store (SRC-GRAPH-4CH1, lines 5982-5996;
RUN-COMPUTED: census.json, command_kinds.coverage_gap_vs_spec_points). This single gap
also accounts for the two stores' explain-verb counts differing by one (16 in the
statement store's leading verbs vs 15 in the command-kind store; RUN-COMPUTED:
census.json, command_kinds.explain_verb_delta_vs_spec_points). By the verb census the
absent statement belongs to the EXPLAIN_HOW class by construction, which would take
that class from 9 to 10 were the gap closed — a repair decision for the graph plane's
own operators, not something this pipeline does (canonical planes are read-only here).
Until then, any downstream family touching 4.15's demand grain works from the
statement store's wording and verb, and discloses the absence of a ratified
demanded-substance interpretation.

### CUR-008 — Per-topic demand profile

The class-by-topic census shows the demand mix is not uniform across the four topics
(RUN-COMPUTED: census.json, command_kinds.class_distribution_by_topic). S1 (Principles
of chemistry) carries the largest share of every hands-on class — its subtopic list
runs from states of matter through electrolysis, and its statement grain includes the
separation techniques, the atom/molecule definitions, the equation-writing demands and
the ionic/covalent diagram demands read off the official topic page (SRC-SPEC-4CH1,
page 17) (SRC-GRAPH-4CH1, lines 259-273) (SRC-GRAPH-4CH1, lines 420-434). S2's
in-pack exemplars skew KNOW_TERM plus DESCRIBE_EXPERIMENT (halogen facts, greenhouse
role of CO2, the oxygen-in-air determination) (SRC-GRAPH-4CH1, lines 831-845;
SRC-GRAPH-4CH1, lines 867-881). S3 mixes KNOW_TERM classification (3.1) with
CALCULATE calorimetry and the C-suffixed energy-level diagram work (3.5C-3.7C on the
official page) (SRC-SPEC-4CH1, page 27) (SRC-GRAPH-4CH1, lines 867-881). S4's exemplars
are KNOW_TERM-heavy with DESCRIBE_EXPERIMENT industrial chemistry (4.8 fractional
distillation of crude oil) (SRC-GRAPH-4CH1, lines 985-999; SRC-GRAPH-4CH1,
lines 1237-1251). The four topic headings and their printed page starts (11/16/21/23)
are the official structure this profile hangs from (SRC-SPEC-4CH1, page 15).

### CUR-009 — The verb taxonomy itself

Across the classified statements the store records 13 distinct leading verbs; the
statement store's leading-verb census differs only in the explain count (the 4.15 gap)
(RUN-COMPUTED: census.json, command_kinds.verb_distribution;
census.json, specification_points.leading_verb_distribution). The heavy verbs are
know (56), understand (54) and describe (27); the rest are explain (15), investigate
(7), calculate (6), write (3), draw (3), use (3), prepare (3), identify (1), determine
(1) and be (2) (RUN-COMPUTED: census.json, command_kinds.verb_distribution). The
in-pack exemplars calibrate the big three: know → definitional/factual recall (1.14,
2.5, 4.1); understand → relational explanation (1.1, 1.41, 4.13's carbon-monoxide
poisoning mechanism); describe → experimental or process narration (1.10, 4.8)
(SRC-GRAPH-4CH1, lines 279-293; SRC-GRAPH-4CH1, lines 831-845; SRC-GRAPH-4CH1,
lines 1000-1014; SRC-GRAPH-4CH1, lines 1237-1251). The rare verbs concentrate in
specific grades of demand (equations, diagrams, preparations) and are the natural
seeds for the assessment-family archetypes (ASM) — but that mapping is those families'
work, not this artifact's.

## Evidence / Source Basis

- **CURRENT — AUTHORITATIVE:** SRC-SPEC-4CH1 — official specification PDF, Issue 3
  (pages 13, 15, 16, 17, 22, 27, 29 as paginated in the evidence pack), sha1 of record
  3ad641b7c60b314fa3b10680feda30bf56280a53, verified at run preflight.
- **CURRENT — AUTHORITATIVE:** SRC-GRAPH-4CH1 — validated curriculum graph:
  spec_command_kinds.yaml (181 command-kind entries with guide classes and demanded
  substances), specification_points.yaml (182 statement entries, verbatim wording,
  applicability law), both verified at run preflight. Read-only plane for this
  pipeline.
- **CURRENT — AUTHORITATIVE / SUPPLEMENTARY:** SRC-TL-4CH1 — official
  teaching-and-learning corpus: Getting Started Guide (pages 3-4) as course-shape
  context; the command-words document carried as an identity-only row (DOCX text not
  extracted in this run).
- **CURRENT — ASSESSMENT EVIDENCE (specimen):** SRC-SAMS-4CH1 — SAMs booklet page 1 as
  identity-only row; specimen material is never cited as session evidence.
- **RUN-COMPUTED:** census.json — deterministic counts over the graph stores of
  record, inputs pinned by sha256 in the annex; verified by the run's evidence-claim
  QA.

## Limitations / Coverage Gaps

- One specification statement (4CH1-4.15) has no ratified command-kind interpretation;
  records here treat its demand class as inferred-from-verb, and label it as such.
- The pack carries 15 of the store's 181 command-kind entries and 9 of 182 statement
  entries as bounded excerpts; per-topic class profiles beyond the in-pack exemplars
  rest on the RUN-COMPUTED census, whose inputs are pinned but which is a
  run-computed view, not a store-published census.
- The command-kind store's class assignments are the validated overlay of record;
  where a class assignment embeds examiner tips from teaching notes, this artifact
  inherits the store's verdict rather than re-deriving it.
- The DOCX members of the teaching corpus (scheme of work, command words) are
  identity-only rows in this pack: no claim here grounds on their internal text.
- Book (SRC-BOOK-4CH1-SB1) is present as an identity-only supplementary row; no
  textbook-grain claim is made in this artifact.

## Research Status

status: GENERATED (research artifact; not educational truth, not canonical curriculum
truth). Generated by the SIB-GEN batch run SIB-CHEMISTRY_4CH1-RUN-002 under the
provider-neutral pipeline (BL-008 wave 1, protocol §4 pass 2), grounded exclusively on
the run's CUR-02 evidence pack (pack sha256 of record in the run manifest) plus the
run's deterministic census annex. Current/legacy separation: fully CURRENT; no legacy
claims. Determinism: content fingerprint of this artifact is recorded in the run
manifest; regeneration produces a new artifact_version.
