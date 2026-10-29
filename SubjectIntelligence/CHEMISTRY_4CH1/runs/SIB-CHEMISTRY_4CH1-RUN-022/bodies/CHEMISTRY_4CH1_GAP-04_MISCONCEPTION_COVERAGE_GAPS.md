---
sib_protocol: SIB-1.0
artifact_id: GAP-04
artifact_version: 1.0
subject: Chemistry
qualification: International GCSE
specification: 4CH1
curriculum_version: "2017"

research_family: gap_intelligence
applicability: REQUIRED

temporal_scope:
  current: true
  legacy: false

source_scope:
  specification: true
  textbook: true
  question_papers: false
  mark_schemes: false
  examiner_reports: true
  supplementary: true

# lifecycle: GENERATED -> QA_PASSED -> STAGED
status: PUBLISHED
generated_by: zai_agent
generated_at: 2026-10-26

provenance:
  source_manifest: "SRC-SPEC-4CH1"
  generation_run_id: "SIB-CHEMISTRY_4CH1-RUN-009"
  generator:
    provider: "z.ai"
    model: "GLM"
    agent_version: "SIB-GEN-r0"
  source_revisions:
    syllabai: "357ace0a230f5e0095ad230320af587dca6bb71f"
    syllabai_pastpapers: "2cb92fe5f56d22f1b231c129a7e0dbc27bf86007"
    syllabai_resources: "6ef8c89291a6662f11fc6dc5ada151c47b172075"
---

# GAP-04 — Misconception Coverage Gaps

## Purpose

This artifact audits misconception coverage for the Pearson Edexcel
International GCSE in Chemistry (4CH1): which misconceptions the of-record
evidence actually documents, from which sources, and for which topics — and
where the documentation stops. It cross-reads three misconception surfaces of
record — examiner-report feedback windows, the board's teaching-and-learning
guidance, and the student book's own warning apparatus — and discloses every
topic for which no misconception evidence of record exists. Gaps stay
disclosed, never filled.

## Scope

**Covers:** the examiner-report misconception windows of record (six reports,
2019–2025); the teaching-and-learning misconception guidance of record (two
topic guides); the book's common-mistake and wording-precision markers across
all four units; and the topic-level asymmetries between those surfaces.

**Out of scope:** the full 23-report examiner census (GAP-03) and tutor-facing
response patterns built on these materials (TUT family).

## Executive Summary

Misconception evidence of record is real but unevenly distributed. The
examiner reports document mark-binding misconceptions in rates of reaction,
energy language and halogen properties; the teaching-and-learning guidance
documents anthropomorphism and four forbidden statements — but only for
bonding and equilibria, the two topics for which topic guides exist of record;
and the book's own warning apparatus is the broadest surface, spanning units
from mole calculations to equilibrium wording to alkene observations. The
audit discloses the resulting asymmetry: no examiner-report misconception
window for organic chemistry enters the pack of record, and 17 of the 23
clean reports of record lie outside this artifact's pack.

## Main Analysis

### GAP-019 — Examiner-report misconception feedback of record is mark-binding and session-anchored

**Claim:** the examiner reports of record document specific, mark-binding
misconceptions — candidates losing marks for identifiable wrong models —
anchored to named papers and sessions, which makes them the strongest
misconception evidence class of record.
**Evidence:** the November 2024 Paper 1C report records that "In Q8(a), a
common misconception was that the reduction in size of the marble chips caused
the reading on the balance to decrease" and that candidates "incorrectly
referenced 'CO₂ produced' or 'given off' without clarifying that the gas had
left the flask, leading to the loss of marks" (SRC-ER-4CH1,
2024-11/4CH1-1C/er.pdf p5); the June 2025 Paper 2C report states "A few lost
the mark for just saying that energy was released. It must be heat or thermal
energy to gain the mark" (SRC-ER-4CH1, 2025-06/4CH1-2C/er.pdf p6). Temporal
scope: CURRENT — AUTHORITATIVE.

### GAP-020 — The of-record misconception windows concentrate on rates, energy and halogens — no organic-chemistry misconception window enters the pack

**Claim:** the six examiner-report windows of record document misconceptions
in rates of reaction (marble chips, concentration, collisions), activation
energy, halogen physical properties and limewater testing — all mapping to
Topics 1 and 3 of the specification's four-topic map — and no window in this
pack documents an organic-chemistry (Topic 4) misconception, a topic-level
coverage gap this audit discloses rather than fills.
**Evidence:** the June 2019 Paper 2C report records "The most common
misapprehensions were stating bromine as a gas at room temperature and even
more thought solid iodine was purple or brown" (SRC-ER-4CH1,
2019-06/4CH1-2C/er.pdf p6); the June 2024 Paper 2CR report records that
candidates "focused on the reactants being solids and the need to melt them
rather than on the high activation energy associated with the chemical
reaction" (SRC-ER-4CH1, 2024-06/4CH1-2CR/er.pdf p5); the June 2022 Paper 2C
report records limewater-test wording — "Make sure you describe how to perform
the test, by adding the carbon dioxide to the limewater in some way"
(SRC-ER-4CH1, 2022-06/4CH1-2C/er.pdf p6); the specification's topic map fixes
where those topics sit — "(a) Energetics (b) Rates of reaction (c) Reversible
reactions and equilibria" under Topic 3 (SRC-SPEC-4CH1,
international-gcse-chemistry-2017-specification.pdf p27). Temporal scope:
CURRENT — AUTHORITATIVE.

### GAP-021 — Board-level misconception guidance exists only for the two topics that have topic guides of record

**Claim:** the teaching-and-learning corpus of record supplies
misconception guidance only through its two topic guides — chemical bonding
and chemical equilibria — whose pages document anthropomorphism, four
statements candidates should avoid, and the pressure/volume equilibrium
distinction; for the remaining topics no board-level misconception guidance is
resolved of record, and that absence is disclosed.
**Evidence:** the bonding guide's page documents that "Statements such as 'The
sodium atom wants to lose one electron' are very common" and lists "Four
statements candidates should avoid making" — "1. The noble gases are unreactive
because their atoms have stable electronic configurations / have a full outer
shell / have eight electrons in their outer shell." among them (SRC-TL-4CH1,
Chemical-bonding---FINAL.pdf p4); the equilibria guide's page works the
van't Hoff volume rule — "'An increase in volume, at constant temperature,
will shift the equilibrium to the side where there are more moles of gas'"
(SRC-TL-4CH1, Chemical-equilibrium---FINAL.pdf p4); both pages carry the
guides' own tutoring framing of record (SRC-TL-4CH1,
Chemical-bonding---FINAL.pdf p4). Temporal scope: CURRENT — AUTHORITATIVE.

### GAP-022 — The book's warning apparatus is the broadest misconception surface of record, spanning all four units

**Claim:** the student book's own hint apparatus documents common mistakes in
every unit — mole calculations, half-equations, displacement wording,
equilibrium language and alkene observations — making it the only misconception
surface of record with all-unit coverage, though its statements are book-native
guidance rather than examiner sentiment.
**Evidence:** the book warns "A common mistake is to multiply the number of
moles by the mass of 2Fe (112 g)" (SRC-BOOK-4CH1-SB1,
parsed/edexcel_igcse_chemistry_chunks_v3.jsonl line 214) and "A common mistake
is to put the electrons on the wrong side of the halfequation" (SRC-BOOK-4CH1-SB1,
parsed/edexcel_igcse_chemistry_chunks_v3.jsonl line 368) in Unit 1; it warns
"In the exam you must write 'chlorine displaces bromine' not 'chlorine
displaces bromide'" (SRC-BOOK-4CH1-SB1,
parsed/edexcel_igcse_chemistry_chunks_v3.jsonl line 446) in Unit 2; that "the
concentrations of the reactants and products at equilibrium are constant, they
are not equal" (SRC-BOOK-4CH1-SB1,
parsed/edexcel_igcse_chemistry_chunks_v3.jsonl line 833) in Unit 3; and "the
final mixture is colourless and not clear. Do not use the word clear"
(SRC-BOOK-4CH1-SB1, parsed/edexcel_igcse_chemistry_chunks_v3.jsonl line 965)
in Unit 4. Temporal scope: CURRENT — AUTHORITATIVE.

### GAP-023 — Wording-precision is the one misconception class all three surfaces document, at different scopes

**Claim:** wording-precision misconceptions — answers marked wrong for the
wrong word, not the wrong idea — are the only misconception class documented
by all three of-record surfaces: the examiner reports ("It must be heat or
thermal energy to gain the mark"), the book's wording warnings, and the
board's anthropomorphism guidance — which marks it as the highest-confidence
misconception class of record.
**Evidence:** the June 2025 Paper 2C report requires "heat or thermal energy
to gain the mark" (SRC-ER-4CH1, 2025-06/4CH1-2C/er.pdf p6); the book insists
"the final mixture is colourless and not clear. Do not use the word clear"
(SRC-BOOK-4CH1-SB1, parsed/edexcel_igcse_chemistry_chunks_v3.jsonl line 965)
and "You have to be careful with the words you use here" before the
displacement wording rule (SRC-BOOK-4CH1-SB1,
parsed/edexcel_igcse_chemistry_chunks_v3.jsonl line 446); the bonding guide
categorizes anthropomorphic answers — "This example of anthropomorphism (i.e.
giving inanimate objects human characteristics) is not justified" (SRC-TL-4CH1,
Chemical-bonding---FINAL.pdf p4). Temporal scope: CURRENT — AUTHORITATIVE.

### GAP-024 — The coverage boundary: six windows of a 23-report census, and two topic guides against a four-topic specification

**Claim:** this audit's misconception coverage is bounded by its pack — six
examiner-report windows of the 23 clean reports enumerated of record, and two
topic guides against the specification's four topics — so 17 reports and all
non-bonding, non-equilibria board guidance are outside the pack and stay
disclosed as unaudited rather than treated as absent misconceptions.
**Evidence:** the pack's six windows of record are the feedback pages
cited in GAP-019–GAP-022, including the June 2019 Paper 2C halogen window
(SRC-ER-4CH1, 2019-06/4CH1-2C/er.pdf p6); the specification's topic pages
frame the asymmetry — Topic 3 opens "The following sub-topics are covered in
this section: (a) Energetics (b) Rates of reaction (c) Reversible reactions
and equilibria" (SRC-SPEC-4CH1,
international-gcse-chemistry-2017-specification.pdf p27); the two guides'
misconception pages of record are the bonding guide's "Four statements
candidates should avoid making" page and the equilibria guide's van't Hoff
page (SRC-TL-4CH1, Chemical-bonding---FINAL.pdf p4;
Chemical-equilibrium---FINAL.pdf p4). Temporal scope: CURRENT —
AUTHORITATIVE.

### GAP-058 — The book's own answer key is a misconception surface: it documents the coefficient-vs-whole-entity multiplication errors inline

**Claim:** The end-of-book answer pages document two calculation misconceptions in the students' own expected terms — forgetting to multiply the whole water-of-crystallisation molecule by the leading coefficient, and multiplying by the mass of 2FeBr3 instead of FeBr3 — a coefficient-vs-whole-entity error class documented nowhere else in this artifact's windows; the answer key therefore acts as a misconception register, not just a score surface, and extends the book's warning apparatus beyond the hint-chunks cited at GAP-022.
**Evidence:** the Chapter 5 answer warns "The common mistake would be not to multiply the whole water molecule by 10. So the mass of the 10H2O is 180. Students will commonly and wrongly come up with 36 for this by multiplying the H2 by 10 but not the O as well." (SRC-BOOK-4CH1-SB1, parsed/edexcel_igcse_chemistry_chunks_v3.jsonl line 1143); the later answer repeats the class — "A common mistake here is to multiply the number of moles of FeBr3 by the mass of 2FeBr3." (SRC-BOOK-4CH1-SB1, parsed/edexcel_igcse_chemistry_chunks_v3.jsonl line 1154).
Temporal scope: CURRENT — AUTHORITATIVE.

### GAP-059 — The specification prints its own scope fences in-line on the organic page: a six-carbon naming ceiling and an explicit mechanisms-not-required rule

**Claim:** The Topic 4 page carries two boundary notes inside the statement list itself — students will be expected to name compounds containing up to six carbon atoms, and knowledge of reaction mechanisms is not required — so the specification walls off mechanism-level explanations by print; over-reaching beyond the fence is effort outside the assessed surface rather than a misconception to unlearn, and the fences are documented at their own statement coordinates rather than in a separate guidance document.
**Evidence:** the Topic 4 page prints the ceiling under statement 4.4 — "students will be expected to name compounds containing up to six carbon atoms" — and the fence under statement 4.6 — "knowledge of reaction mechanisms is not required" (SRC-SPEC-4CH1, international-gcse-chemistry-2017-specification.pdf p29).
Temporal scope: CURRENT — AUTHORITATIVE.

### GAP-060 — Presentation-format demands — diagram conventions and answer layout — form a documented class adjacent to misconceptions: right content, wrong form

**Claim:** The book's covalent-bonding page polices diagram form in exam terms — inner electrons may be omitted only when the question says so, and a bond-lines sketch is explicitly not a dot-and-cross diagram — while the examiner-report window of record coaches answer layout — bullet points or a numbered list to show a method clearly — so both surfaces document format demands that cost marks independently of chemical content; the class sits adjacent to the wording-precision class of GAP-023 but is distinct: the idea is right and the form is marked.
**Evidence:** the book warns "In an exam, only leave out the inner electrons if the question tells you to." and "the diagram shown in Figure 8.6 is not a dot-and-cross diagram" (SRC-BOOK-4CH1-SB1, parsed/edexcel_igcse_chemistry_chunks_v3.jsonl line 311); the examiner-report window advises "Consider using bullet points or a numbered list to show a method clearly" (SRC-ER-4CH1, 2022-06/4CH1-1C/er.pdf p6).
Temporal scope: CURRENT — AUTHORITATIVE.
## Evidence / Source Basis

Primary evidence: SRC-ER-4CH1 (six examiner-report feedback windows, 2019-2025)
and SRC-SPEC-4CH1 (the four topic pages framing where the documented topics
sit). Supplementary: SRC-BOOK-4CH1-SB1 (the book's warning apparatus across
all four units) and SRC-TL-4CH1 (the two topic guides' misconception pages)
are consumed as cited texture; SRC-ROOT-BOOK-COPIES-4CH1 and SRC-SAMS-4CH1
ride as one-page identity-presence entries consumed for no claim. All
excerpts are bounded with locators preserved; caps enforced by the pack
builder.

## Limitations / Coverage Gaps

Seventeen of the 23 clean examiner reports of record are outside this pack —
the misconception census is a six-window sample and is labeled as such. No
organic-chemistry examiner-report window enters the pack; the Topic 4
misconception gap is disclosed, not diagnosed. The book's warning apparatus is
sampled at five chunks; the remaining warning chunks are unsampled.

## Research Status

GENERATED under SIB-CHEMISTRY_4CH1-RUN-009 (BL-009 pass 9) from this artifact's
evidence pack alone; validator of record tools/sib @ 357ace0a; claim QA binds
every citation to a pack excerpt. Research artifact — evidence-backed, not
canonical educational truth. Deepened under SIB-CHEMISTRY_4CH1-RUN-022 (D3 REQUIRED-core depth pass, tranche 6: GAP): +3 records (GAP-058..GAP-060), zero-append mining of the carried pack of record (origin RUN-009) — unmined-window authoring for seven artifacts and held-window authoring with fresh claims for GAP-03, whose unmined surface was exhausted (1/29 excerpts unmined pre-run); every quote self-bound to raw excerpt text before the official gate; claim QA re-bound all citations.

