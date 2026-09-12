# T-C11 §16 Batch 2 Review Sheet — Concept / Prerequisite / Misconception Graph

Slice 4CH1-1.13–1.24 (S1 remainder, second 12 SPs) + practical PR-02 · generated 2026-09-12 · decision record `scripts/c11_batch2_decisions.yaml` (pass 1: `c11-s16-batch-2`) · adversarial pass 2: `scripts/c11_batch2_review_pass2.yaml` · authorization: `scripts/c11_s16_authorization.yaml` (§16 authorized 2026-09-12; batch 2 commissioned by the operator, session 49)

**NOTHING in this batch is authoritative.** All 14 nodes / 38 batch edges are AI_SUGGESTED (SUGGESTED). HUMAN_VALIDATED is reachable only by your promotion command via the §18 pathway (`scripts/c11_promote.py` → `scripts/c11_promotions.yaml` → **Zero batch-2 promotions exist.** This sheet is the batch's operator gate: record verdicts in `scripts/c11_batch2_verdicts_template.yaml` (fill + rename to `c11_batch2_verdicts.yaml`); a later session encodes and applies them.

How to review: for each row check the quoted evidence actually appears in the cited file and actually says what the record claims; then rule on the relation CLASS and direction, not just existence. Machine state: the full gate suite is green at the merged 67-node / 156-edge store; every quote is machine-verified byte-for-byte against its source file (G03/c11.4); the 4.15 negative control is uncovered. Five edges are CROSS-BOUNDARY into earlier-record nodes (CON-AR ×2, CON-ELEMENT, CON-CHROMATOGRAPHY, CON-RF-VALUE — sanctioned per FN-B1-2; no duplicate concept was minted: the Ar term stays with the pilot's CON-AR).

## 1. Totals & second-pass agreement

| | nodes | authored edges | held | |
|---|---|---|---|
| pass-1 (extraction) | 14 | 23 (+15 derived PART_OF) | 10 |
| pass-2 verdicts | 14 CONFIRM(+note) | 23 CONFIRM(+note) · 0 HOLD · 0 REJECT | all 10 AGREE |

Raw agreement (NOT κ — single human rater, architecture §12): nodes 14/14 = 100.0%; edges — of the 23 edges pass-1 asserted (SUGGESTED), pass-2 confirmed 23 (100.0%); pass-1 quarantined 0 edges as REVIEW_REQUIRED (this batch authored NONE — every doubt was held or resolved on explicit evidence). **Zero pass-2 demotions.**

Forecast calibration (C11_BATCH_FORECAST.json future_batch_records): predicted 28.8 nodes / 33 edges / 13 held vs actual 14 / 23 / 10 — nodes −51.4%, edges −30.3%, held −23.1%. The delta is the boundary discipline, not thin coverage: the Ar TERM was NOT re-minted (the pilot's CON-AR owns it — 1.16's definition reached via the CON-ISOTOPES attachment + the boundary edge), and 1.13 attaches no batch-2 node (its concept content is the batch-1 chromatography triplet reached via the PR-02 boundary edges).

## 2. Concept & misconception nodes (14)

| # | code | family | title | attaches to (role) | conf | evidence (anchor → quote) | pass-2 | operator |
|---|---|---|---|---|---|---|---|---|
| 1 | `4CH1-CON-ATOM` | CONCE | Atom (definition and subatomic composition) | 4CH1-1.14 (core) | high | NOTE: “The smallest particle of an element that contains electrons surrounding a nucleus that contains prot” | CONFIRM | ☐ |
| 2 | `4CH1-CON-MOLECULE` | CONCE | Molecule | 4CH1-1.14 (core) | high | NOTE: “A group of two or more atoms chemically combined to form an identifiable unit which retains the prop” | CONFIRM | ☐ |
| 3 | `4CH1-CON-SUBATOMIC-PARTICLES` | CONCE | Subatomic particles (proton, neutron, electron — positions, relative masses, relative charges) | 4CH1-1.15 (core) | high | NOTE: “Each atom is made of subatomic particles called protons, neutrons, and electrons” | CONFIRM_WITH_NOTE | ☐ |
| 4 | `4CH1-CON-ATOMIC-NUMBER` | CONCE | Atomic number | 4CH1-1.16 (core) | high | NOTE: “The number of protons in the nucleus of an atom” | CONFIRM_WITH_NOTE | ☐ |
| 5 | `4CH1-CON-MASS-NUMBER` | CONCE | Mass number | 4CH1-1.16 (core) | high | NOTE: “The number of protons and neutrons in the nucleus of an atom” | CONFIRM | ☐ |
| 6 | `4CH1-CON-ISOTOPES` | CONCE | Isotopes and relative atomic mass from isotopic abundances | 4CH1-1.16 (core); 4CH1-1.17 (core) | high | NOTE: “Atoms of the same element which have the same number of protons but a different number of neutrons” | CONFIRM_WITH_NOTE | ☐ |
| 7 | `4CH1-CON-PERIODIC-TABLE` | CONCE | Periodic Table arrangement (atomic-number order, groups and periods) | 4CH1-1.18 (core) | high | NOTE: “Elements are arranged on the Periodic table in order of increasing atomic number” | CONFIRM_WITH_NOTE | ☐ |
| 8 | `4CH1-CON-ELECTRONIC-CONFIGURATION` | CONCE | Electronic configuration of the first 20 elements (shells 2, 8, 8; configuration and Periodic Table position) | 4CH1-1.19 (core); 4CH1-1.22 (core) | high | NOTE: “For the first 20 elements, once the third shell has 8 electrons, the fourth shell begins to fill” | CONFIRM | ☐ |
| 9 | `4CH1-CON-METAL-NONMETAL` | CONCE | Classifying elements as metals or non-metals (by properties and by Periodic Table position) | 4CH1-1.20 (core); 4CH1-1.21 (core) | high | NOTE: “We can use properties such as electrical conductivity and acid-base character to classify elements a” | CONFIRM_WITH_NOTE | ☐ |
| 10 | `4CH1-CON-METALLOID` | CONCE | Semi-metals (metalloids) — elements bordering the metal/non-metal divide | 4CH1-1.21 (enri) | high | NOTE: “Elements which border the line are hard to classify as they have characteristics of both sides, so t” | CONFIRM_WITH_NOTE | ☐ |
| 11 | `4CH1-CON-GROUP-SIMILARITY` | CONCE | Why elements in the same group have similar chemical properties | 4CH1-1.23 (core) | high | NOTE: “Elements in the same group in the Periodic Table will have similar chemical properties” | CONFIRM | ☐ |
| 12 | `4CH1-CON-NOBLE-GAS-INERTNESS` | CONCE | Why the noble gases (Group 0) do not readily react | 4CH1-1.24 (core) | high | NOTE: “Group 0 elements do not do this because they have full outer shells of electrons” | CONFIRM | ☐ |
| 13 | `4CH1-MIS-ISOTOPES-DIFFER-PROTONS` | MISCO | Believing isotopes of an element differ in their number of protons | — | high | MARK_SCHEME: “different number of protons”<br>remediation: “Atoms of the same element which have the same number of protons but a different ” | CONFIRM | ☐ |
| 14 | `4CH1-MIS-RAM-MASS-NUMBER` | MISCO | Calling the Periodic Table relative atomic mass the mass number | — | high | MARK_SCHEME: “Reject mass number”<br>remediation: “The relative atomic mass of every element is given on the Periodic Table. It is ” | CONFIRM | ☐ |

Identity-policy notes (split-first; merges are operator-only, OD-1 operand rule): pass-2 flags the CON-ISOTOPES/CON-AR boundary split (FP-B2-1 — 1.16's Ar term vs the pilot's CON-AR), the CON-SUBATOMIC-PARTICLES particle triple, the CON-PERIODIC-TABLE arrangement+group+period block and the CON-METAL-NONMETAL 1.20/1.21 pair. All are operator identity decisions (template §identity_decisions). 1.13 attaches NO batch-2 node (practical-only scope — the explicit gap, see §5 FP-B2-4).

## 3. Authored semantic edges (23)

Direction conventions: REQUIRES_PREREQUEREQUISITE source=dependent → target=prerequisite; EXPLAINED_BY explained → explainer; COMMONLY_CONFUSED_WITH is a symmetric term-pair relation; WRONG_ANSWER_PATTERN / REMEDIATED_BY misconception → concept.

### 3.1 REVIEW_REQUIRED (open operator decision)

**None.** This batch authored no REVIEW_REQUIRED edge: the pass-1 authoring either resolved each doubt on explicit evidence or sent the candidate to held (10 rows, §4).

### 3.2 SUGGESTED edges (23) — the §18-promotable surface after verdicts

Flagged rows (pre-triage FLAGGED in the verdict template): the relation-class choices on the two EXPLAINED_BY edges and the CON-AR→CON-ISOTOPES boundary edge, the first COMMONLY_CONFUSED_WITH deployment, the vocabulary-level Periodic-Table→CON-ELEMENT class, the MASS-NUMBER→ATOMIC-NUMBER density flag, and the two remediation-target=WAP-target rows (the batch-1 B1-E-25 pattern).

| edge | method | conf | evidence (quote) | upstream | pass-2 | operator |
|---|---|---|---|---|---|---|
| `4CH1-CON-AR` **REQUIRES_PREREQUISITE** `4CH1-CON-ISOTOPES` ⚑ | USED_WITHOUT_RETEACHING | high | “The relative atomic mass of each element is calculated from the mass number and relative abundances ” | T-C10 HUMAN_VALIDATED 4CH1-1.17 @ Relative atomic mass (2026-09-11); source node owned ... | CONFIRM_WITH_NOTE | ☐ |
| `4CH1-CON-ATOMIC-NUMBER` **COMMONLY_CONFUSED_WITH** `4CH1-CON-MASS-NUMBER` ⚑ | EXAMINER_TIP_EXPLICIT | high | “Both the atomic number and the mass number are given on the Periodic Table, but it can be easy to co” | T-C10 HUMAN_VALIDATED 4CH1-1.16 @ Atoms: Definitions & Structure (2026-09-11); assessme... | CONFIRM_WITH_NOTE | ☐ |
| `4CH1-CON-ATOMIC-NUMBER` **REQUIRES_PREREQUISITE** `4CH1-CON-SUBATOMIC-PARTICLES` | DEFINITIONAL_DEPENDENCY | high | “The number of protons in the nucleus of an atom” | T-C10 HUMAN_VALIDATED 4CH1-1.16 @ Atoms: Definitions & Structure (2026-09-11) | CONFIRM | ☐ |
| `4CH1-CON-ELECTRONIC-CONFIGURATION` **REQUIRES_PREREQUISITE** `4CH1-CON-PERIODIC-TABLE` | USED_WITHOUT_RETEACHING | high | “The number of notations in the electronic configuration tells us the number of occupied shells” | T-C10 HUMAN_VALIDATED 4CH1-1.19/1.22 @ Electronic Configurations (2026-09-11) | CONFIRM | ☐ |
| `4CH1-CON-ELECTRONIC-CONFIGURATION` **REQUIRES_PREREQUISITE** `4CH1-CON-SUBATOMIC-PARTICLES` | DEFINITIONAL_DEPENDENCY | high | “Electrons orbit the nucleus in shells (or energy levels) and each shell has a different amount of en” | T-C10 HUMAN_VALIDATED 4CH1-1.19 @ Electronic Configurations + 4CH1-1.15 @ Atoms: Defini... | CONFIRM | ☐ |
| `4CH1-CON-GROUP-SIMILARITY` **EXPLAINED_BY** `4CH1-CON-ELECTRONIC-CONFIGURATION` ⚑ | SINGLE_SOURCE_CAUSAL_TEACHING | high | “This is because they have the same number of outer electrons so will react and bond similarly” | T-C10 HUMAN_VALIDATED 4CH1-1.23 @ Electronic Configuration & Reactivity (2026-09-11) | CONFIRM_WITH_NOTE | ☐ |
| `4CH1-CON-GROUP-SIMILARITY` **REQUIRES_PREREQUISITE** `4CH1-CON-PERIODIC-TABLE` | USED_WITHOUT_RETEACHING | high | “Elements in the same group in the Periodic Table will have similar chemical properties” | T-C10 HUMAN_VALIDATED 4CH1-1.23 @ Electronic Configuration & Reactivity (2026-09-11) | CONFIRM | ☐ |
| `4CH1-CON-ISOTOPES` **REQUIRES_PREREQUISITE** `4CH1-CON-SUBATOMIC-PARTICLES` | DEFINITIONAL_DEPENDENCY | high | “Atoms of the same element which have the same number of protons but a different number of neutrons” | T-C10 HUMAN_VALIDATED 4CH1-1.16 @ Atoms: Definitions & Structure (2026-09-11) | CONFIRM | ☐ |
| `4CH1-CON-MASS-NUMBER` **REQUIRES_PREREQUISITE** `4CH1-CON-ATOMIC-NUMBER` ⚑ | USED_WITHOUT_RETEACHING | high | “The number of neutrons can thus be calculated by subtracting the atomic number from the mass number” | T-C10 HUMAN_VALIDATED 4CH1-1.16 @ Atoms: Definitions & Structure (2026-09-11) | CONFIRM_WITH_NOTE | ☐ |
| `4CH1-CON-MASS-NUMBER` **REQUIRES_PREREQUISITE** `4CH1-CON-SUBATOMIC-PARTICLES` | DEFINITIONAL_DEPENDENCY | high | “The number of protons and neutrons in the nucleus of an atom” | T-C10 HUMAN_VALIDATED 4CH1-1.16 @ Atoms: Definitions & Structure (2026-09-11) | CONFIRM | ☐ |
| `4CH1-CON-METAL-NONMETAL` **REQUIRES_PREREQUISITE** `4CH1-CON-PERIODIC-TABLE` | USED_WITHOUT_RETEACHING | high | “Metals are on the left of the Periodic Table and non-metals on the right” | T-C10 HUMAN_VALIDATED 4CH1-1.20/1.21 @ Metals & non-metals in the Periodic Table (2026-... | CONFIRM | ☐ |
| `4CH1-CON-MOLECULE` **REQUIRES_PREREQUISITE** `4CH1-CON-ATOM` | DEFINITIONAL_DEPENDENCY | high | “A group of two or more atoms chemically combined to form an identifiable unit which retains the prop” | T-C10 HUMAN_VALIDATED 4CH1-1.14 @ Atoms: Definitions & Structure (2026-09-11) | CONFIRM | ☐ |
| `4CH1-CON-NOBLE-GAS-INERTNESS` **EXPLAINED_BY** `4CH1-CON-ELECTRONIC-CONFIGURATION` ⚑ | SINGLE_SOURCE_CAUSAL_TEACHING | high | “Group 0 elements do not do this because they have full outer shells of electrons” | T-C10 HUMAN_VALIDATED 4CH1-1.24 @ Electronic Configuration & Reactivity (2026-09-11) | CONFIRM_WITH_NOTE | ☐ |
| `4CH1-CON-NOBLE-GAS-INERTNESS` **REQUIRES_PREREQUISITE** `4CH1-CON-PERIODIC-TABLE` | USED_WITHOUT_RETEACHING | high | “The elements in Group 0 of the Periodic Table are called the noble gases” | T-C10 HUMAN_VALIDATED 4CH1-1.24 @ Electronic Configuration & Reactivity (2026-09-11) | CONFIRM | ☐ |
| `4CH1-CON-PERIODIC-TABLE` **REQUIRES_PREREQUISITE** `4CH1-CON-ATOMIC-NUMBER` | DEFINITIONAL_DEPENDENCY | high | “Elements are arranged on the Periodic table in order of increasing atomic number” | T-C10 HUMAN_VALIDATED 4CH1-1.18 @ Periodic Table: Basics (2026-09-11) | CONFIRM | ☐ |
| `4CH1-CON-PERIODIC-TABLE` **REQUIRES_PREREQUISITE** `4CH1-CON-ELEMENT` ⚑ | USED_WITHOUT_RETEACHING | high | “There are over 100 chemical elements which have been isolated and identified” | T-C10 HUMAN_VALIDATED 4CH1-1.18 @ Periodic Table: Basics (2026-09-11); target node owne... | CONFIRM_WITH_NOTE | ☐ |
| `4CH1-CON-SUBATOMIC-PARTICLES` **REQUIRES_PREREQUISITE** `4CH1-CON-ATOM` | DEFINITIONAL_DEPENDENCY | high | “Each atom is made of subatomic particles called protons, neutrons, and electrons” | T-C10 HUMAN_VALIDATED 4CH1-1.15 @ Atoms: Definitions & Structure (2026-09-11) | CONFIRM | ☐ |
| `4CH1-MIS-ISOTOPES-DIFFER-PROTONS` **REMEDIATED_BY** `4CH1-CON-ISOTOPES` ⚑ | EXPLICIT_TEACH_SEQUENCE | high | “Atoms of the same element which have the same number of protons but a different number of neutrons” | T-C10 HUMAN_VALIDATED 4CH1-1.16 @ Atoms: Definitions & Structure (2026-09-11) | CONFIRM_WITH_NOTE | ☐ |
| `4CH1-MIS-ISOTOPES-DIFFER-PROTONS` **WRONG_ANSWER_PATTERN** `4CH1-CON-ISOTOPES` | ASSESSMENT_DOCUMENTED | high | “different number of protons” | PMT Unit-1 Paper-1 MS "Atomic Structure 2" Q1(b) (pinned scripts/c11_evidence/ATOM2_MS_... | CONFIRM | ☐ |
| `4CH1-MIS-RAM-MASS-NUMBER` **REMEDIATED_BY** `4CH1-CON-AR` ⚑ | EXPLICIT_TEACH_SEQUENCE | high | “The relative atomic mass of every element is given on the Periodic Table. It is the larger of the tw” | T-C10 HUMAN_VALIDATED 4CH1-1.26 @ Calculate Relative Mass (2026-09-11) | CONFIRM_WITH_NOTE | ☐ |
| `4CH1-MIS-RAM-MASS-NUMBER` **WRONG_ANSWER_PATTERN** `4CH1-CON-AR` | ASSESSMENT_DOCUMENTED | high | “Reject mass number” | PMT Unit-1 Paper-1 MS "The Periodic Table" Q1(b) (pinned scripts/c11_evidence/PT_MS_P1.... | CONFIRM | ☐ |
| `4CH1-PR-02` **REQUIRES_PREREQUISITE** `4CH1-CON-CHROMATOGRAPHY` | USED_WITHOUT_RETEACHING | high | “Investigate how paper chromatography can be used to separate and identify a mixture of food colourin” | T-C10 HUMAN_VALIDATED 4CH1-1.13 @ Paper chromatography (2026-09-11); target node owned ... | CONFIRM | ☐ |
| `4CH1-PR-02` **REQUIRES_PREREQUISITE** `4CH1-CON-RF-VALUE` | USED_WITHOUT_RETEACHING | high | “The Rf values of food colours A, B, C and D should be compared to that for the unknown sample as wel” | T-C10 HUMAN_VALIDATED 4CH1-1.13 @ Paper chromatography (2026-09-11); target node owned ... | CONFIRM | ☐ |

### 3.3 Derived PART_OF edges (15)

Derived deterministically from node attachments (concepts.yaml); each carries the attachment's evidence anchors and the node's provenance. Not re-listed here — review them via the §2 node rows. Machine-verified: the PART_OF set must exactly equal the declared attachments (c11.7).

## 4. Held / rejected candidates (10) — the abstention record

These were considered and NOT drawn. Review that each hold reason is right (pass-2 already did — column below). Overriding a hold = re-authoring the decision record, never hand-editing the graph.

| id | status | candidate | failing rule | pass-2 | operator |
|---|---|---|---|---|---|
| B2-H-01 | held | `REQUIRES_PREREQUISITE(CON-ISOTOPES, CON-ATOMIC-NUMBER)` | VOCABULARY_OPERAND_DUPLICATION | AGREE_HOLD | ☐ |
| B2-H-02 | held | `REQUIRES_PREREQUISITE(CON-MASS-NUMBER, CON-ATOM)` | TRANSITIVELY_SUBSUMED | AGREE_HOLD | ☐ |
| B2-H-03 | held | `REQUIRES_PREREQUISITE(CON-ELECTRONIC-CONFIGURATION, CON-ATOM)` | TRANSITIVELY_SUBSUMED | AGREE_HOLD | ☐ |
| B2-H-04 | held | `REQUIRES_PREREQUISITE(CON-METAL-NONMETAL, CON-ELECTRONIC-CONFIGURATION)` | OD_2_TABLE_LABEL | AGREE_HOLD | ☐ |
| B2-H-05 | held | `REQUIRES_PREREQUISITE(CON-GROUP-SIMILARITY, CON-ELECTRONIC-CONFIGURATION) — "understanding grou` | RELATION_CLASS_PAIR_CONFLICT | AGREE_HOLD | ☐ |
| B2-H-06 | held | `REQUIRES_PREREQUISITE(CON-NOBLE-GAS-INERTNESS, CON-ELECTRONIC-CONFIGURATION) — "the full-outer-` | RELATION_CLASS_PAIR_CONFLICT | AGREE_HOLD | ☐ |
| B2-H-07 | held | `REQUIRES_PREREQUISITE(CON-NOBLE-GAS-INERTNESS, CON-GROUP-SIMILARITY)` | RELATION_CLASS_AMBIGUITY_PLUS_DENSITY | AGREE_HOLD | ☐ |
| B2-H-08 | held | `REQUIRES_PREREQUISITE(PR-02, CON-SOLUTION)` | TRANSITIVELY_SUBSUMED | AGREE_HOLD | ☐ |
| B2-H-09 | held | `MISCONCEPTION node "the Periodic Table is arranged in order of (relative) atomic mass" MISCONCE` | INSUFFICIENT_EVIDENCE | AGREE_HOLD | ☐ |
| B2-H-10 | held | `MISCONCEPTION node "the solvent-level rule explained as the solvent reacting with the dyes" MIS` | EVIDENCE_CLASS_WEAK | AGREE_HOLD | ☐ |

## 5. Findings (pass-2, for the batch record)

- **FP-B2-1 (split-artifact)** — CON-ISOTOPES carries the 1.16 isotope term + the 1.17 Ar-from-abundances calculation while the Ar TERM stays with the pilot's CON-AR (boundary discipline, no duplicate mint); CON-PERIODIC-TABLE carries arrangement+group+period; CON-METAL-NONMETAL carries 1.20+1.21; CON-SUBATOMIC-PARTICLES carries the particle triple. All operator identity decisions; no defect.
- **FP-B2-2 (relation-class-choice)** — CON-AR -> CON-ISOTOPES (USED_WITHOUT_RETEACHING vs EXPLAINED_BY reading) and the GROUP-SIMILARITY / NOBLE-GAS EXPLAINED_BY edges (prereq readings held as B2-H-05/H-06) — one relation per pair forced the choices; OD-class decisions for the operator.
- **FP-B2-3 (first-class-deployment)** — The store's FIRST COMMONLY_CONFUSED_WITH edge (ATOMIC-NUMBER <-> MASS-NUMBER) on an explicit corpus confusability statement + assessed confusion family; relation_class_rationale recorded per G08. The earlier zero-CCW state was honest abstention, not a rule.
- **FP-B2-4 (boundary discipline)** — Five cross-boundary edges into earlier-record nodes (CON-AR x2, CON-ELEMENT, CON-CHROMATOGRAPHY, CON-RF-VALUE) + the practical PR-02 — all sanctioned (FN-B1-2, no boundary minting). 1.13 attaches no batch-2 concept node: its concept content is the batch-1 chromatography triplet reached via the PR-02 edges; the practical method itself is procedure, not concept — recorded so the gap is explicit, not silent (the FN-B1-3 style).
- **FN-B2-1 (false-negative-concern)** — Mark-scheme mining: 6 MS pinned for this batch (ATOM1/2/3, PT, ECM1, ECM3) — ECM1/ECM3 close the batch-1 FN-B1-1 remainder for the ECM family; the Paper-2 variants remain unpinned for both slices. Batch 3 should pin Paper-2.
- **FN-B2-2 (boundary)** — Batch 3 = S1 remainder 1.37-1.60C (12 SPs): its boundary edges to CON-ATOM / CON-SUBATOMIC-PARTICLES / CON-ELECTRONIC-CONFIGURATION and the bonding-section nodes are sanctioned (cross-batch boundary edges to EXISTING nodes; no boundary minting needed).
- **FN-B2-3 (vocabulary-coverage)** — "Monatomic" (noble gases) and "zig-zag line" (metal/non-metal divide) are taught inline without concepts — deliberate non-minting at pilot granularity; recorded so the coverage gap is explicit, not silent.

## 6. Command-kind tags (guide §8) — batch-2 SPs

| SP | verb | guide class | demanded substance | operator |
|---|---|---|---|---|
| 4CH1-1.13 | investigate | DESCRIBE_EXPERIMENT | the paper-chromatography practical using inks/food colourings (pencil baseline, small spots, solvent below the start line, distances and Rf values, comparison with known colourings) | ☐ |
| 4CH1-1.14 | know | KNOW_TERM | definitions of the terms atom and molecule | ☐ |
| 4CH1-1.15 | know | KNOW_TERM | the structure of an atom in terms of the positions, relative masses and relative charges of protons, neutrons and electrons | ☐ |
| 4CH1-1.16 | know | KNOW_TERM | definitions of the terms atomic number, mass number, isotopes and relative atomic mass | ☐ |
| 4CH1-1.17 | be | CALCULATE | calculation of the relative atomic mass of an element from isotopic abundances (percentage-weighted average of isotopic mass numbers) | ☐ |
| 4CH1-1.18 | understand | UNDERSTAND_RELATION | how elements are arranged in the Periodic Table (in order of increasing atomic number, in groups and periods) | ☐ |
| 4CH1-1.19 | understand | UNDERSTAND_RELATION | deducing the electronic configurations of the first 20 elements (shell filling 2, 8, 8 then the fourth shell) from their Periodic Table positions | ☐ |
| 4CH1-1.20 | understand | UNDERSTAND_RELATION | using electrical conductivity and the acid-base character of oxides to classify elements as metals or non-metals | ☐ |
| 4CH1-1.21 | identify | UNDERSTAND_RELATION | identifying an element as a metal or a non-metal according to its position in the Periodic Table (metals left, non-metals right of the zig-zag dividing line) | ☐ |
| 4CH1-1.22 | understand | UNDERSTAND_RELATION | relating the electronic configuration of a main group element to its Periodic Table position (period = occupied shells, group = outer electrons) | ☐ |
| 4CH1-1.23 | understand | UNDERSTAND_RELATION | why elements in the same group of the Periodic Table have similar chemical properties (same number of outer electrons) | ☐ |
| 4CH1-1.24 | understand | UNDERSTAND_RELATION | why the noble gases (Group 0) do not readily react (full outer shells of electrons) | ☐ |

## 7. Negative control (4CH1-4.15) — carried forward, still uncovered

Zero concepts, zero edges, zero coverage for 4.15 across the whole merged store (machine-tested: graph_check + negative test class 10/11 + the s16-authorization check D5). The batch adds nothing in S4 territory. Operator: acknowledge ☐

## 8. Batch-2 evidence set (pinned)

- 7 T-C10 HUMAN_VALIDATED-mapped notes (read in full at extraction): b. Paper chromatography (the 1.13 practical note) + c. Atoms: Definitions & Structure, c. Relative atomic mass + d. Periodic Table Basics, d. Electronic Configurations, d. Metals & non-metals, d. Electronic Configuration & Reactivity.
- 6 pinned mark-scheme extractions (misconception-class evidence only): ATOM1/ATOM2/ATOM3_MS_P1.txt (9b943e58cce1 / 6c60d4721ea0 / 59a666306b02) + PT_MS_P1.txt (fd6352a38077) + ECM1/ECM3_MS_P1.txt (bb33cf992b1c / 4ef3bd02ce8f) — the ECM1/ECM3 pins close the batch-1 FN-B1-1 remainder; the Paper-2 variants remain unpinned (FN-B2-1).

## 9. After review (the batch gate)

1. Fill `scripts/c11_batch2_verdicts_template.yaml` (rename to `c11_batch2_verdicts.yaml`): per-row verdicts, the identity decisions, the held acknowledgment. (This batch has NO RR settlement — no REVIEW_REQUIRED edge was authored.)
2. The next session encodes your verdicts (fail-closed) and applies them: CONFIRM edges through the §18 pathway (`c11_diff_review.py approve` → one `c11_promote.py` invocation → gated G13 re-run); REJECT rows re-authored out like HELD-13; MERGE/SPLIT as §7 re-authoring (B2-ID-01 may re-scope the Ar boundary).
3. Only after the batch-2 gate settles does batch 3 (S1 remainder 1.37–1.60C) get commissioned — the consolidated cross-slice boundary ruling comes before phase 2 (S3).

---
Machine artifacts: `graph/concepts.yaml`, `graph/concept_edges.yaml`, `graph/spec_command_kinds.yaml` (generated, gated, merged store) · `C11_BATCH2_REVIEW.json` (this sheet's machine record) · `scripts/c11_batch2_verdicts_template.yaml` (the verdict template) · contract: `C11_ARCHITECTURE.md`
