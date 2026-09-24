# T-C11 §16 Batch 9 Review Sheet — Concept / Prerequisite / Misconception Graph

Slice 4CH1–4.1–4.22 minus the 4CH1-4.15 negative-control carve-out (Section 4 — Organic Chemistry, FIRST slice: a Introduction + b Crude Oil & Fuels + c Alkanes, 21 authorable SPs; no practicals own any batch-9 SP) · generated 2026-09-24 · decision record `scripts/c11_batch9_decisions.yaml` (pass 1: `c11-s16-batch-9`) · adversarial pass 2: `scripts/c11_batch9_review_pass2.yaml` · authorization: `scripts/c11_s16_authorization.yaml` (§16 authorized 2026-09-12; batch 9 = the first slice of the S4 section program commissioned by the operator's 'commission a new section' directive) · boundary ruling: `scripts/c11_batch9_boundary_ruling.yaml` (session 62, machine-checked — the FIVE sanctioned boundary edges below)

**NOTHING in this batch is authoritative.** All 15 nodes / 41 batch edges (20 authored semantic + 21 derived PART_OF) are AI_SUGGESTED (SUGGESTED). HUMAN_VALIDATED is reachable only by your promotion command via the §18 pathway (`scripts/c11_promote.py` → `scripts/c11_promotions.yaml` → regeneration). **Zero batch-9 promotions exist.** This sheet is the batch's operator gate: record verdicts in `scripts/c11_batch9_verdicts_template.yaml` (fill + rename to `c11_batch9_verdicts.yaml`); a later session encodes and applies them.

How to review: for each row check the quoted evidence actually appears in the cited file and actually says what the record claims; then rule on the relation CLASS and direction, not just existence. Machine state: the full gate suite is green at the merged 180-node / 425-edge store; every quote is machine-verified against its source file (G03/c11.4; 101 quote probes + preverify checks verified BEFORE the registry grew); the 4.15 negative control is uncovered. FIVE edges are cross-section boundary edges into the ruled targets (CON-FRACTIONAL-DISTILLATION — the batch-1 owner; CON-EMPIRICAL-FORMULA and CON-MOLECULAR-FORMULA — the pilot owners; CON-COMBUSTION-O2 — the batch-5 owner; CON-MIXTURE — the batch-1 owner; sanctioned per the session-62 cross-slice ruling; no duplicate concept was minted). The S4-a/b/c families are MS-pinned (the Crude Oil MS Q2b Reject column anchors the ONE misconception mint; the Alkanes MS Q1a(i) marking points anchor the isomer definition). NO pass-2 finding required re-authoring (FP-B9-1..4 / FN-B9-1..2 are recorded questions and resolutions).

## 1. Totals & second-pass agreement

| | nodes | authored edges | held | |
|---|---|---|---|---|
| pass-1 (extraction) | 15 | 20 (+21 derived PART_OF) | 9 |
| pass-2 verdicts | 15 CONFIRM | 20 CONFIRM · 0 HOLD · 0 REJECT | all 9 AGREE |

Raw agreement (NOT κ — single human rater, architecture §12): nodes 15/15 = 100.0%; edges — of the 20 edges pass-1 asserted (SUGGESTED), pass-2 confirmed 20 (100.0%); pass-1 quarantined 0 edges as REVIEW_REQUIRED (this batch authored NONE — every doubt was held or resolved on explicit evidence). **Zero pass-2 findings required re-authoring; zero demotions.**

Forecast calibration (C11_BATCH_FORECAST.json future_batch_records): the batch-9 record is appended by the forecast instrument at this gate (see the regenerated C11_BATCH_FORECAST.json). The S4-a/b/c slice runs in the descriptive band (nodes/SP 0.71, edges/SP 0.95), with the held adjacencies (B9-H-01..09 — the surfaces the ruling dispositioned) accounting for the gap, not thin coverage: no S1/S2/S3 identity was re-minted (the 5 existing-owner targets reached via the 5 sanctioned boundary edges); no batch-9 SP is practical-typed (the PR lane is empty).

## 2. Concept & misconception nodes (15)

| # | code | family | title | attaches to (role) | conf | evidence (anchor → quote) | pass-2 | operator |
|---|---|---|---|---|---|---|---|---|
| 1 | `4CH1-CON-HYDROCARBON` | CONCE | Hydrocarbon (a compound of hydrogen and carbon only) | 4CH1-4.1 (core) | high | NOTE: “A compound that contains **only** hydrogen and carbon atoms” | CONFIRM | ☐ |
| 2 | `4CH1-CON-ORGANIC-FORMULAE` | CONCE | Representing organic molecules (empirical, molecular, general, structural, displayed formulae) | 4CH1-4.2 (core) | high | NOTE: “Organic compounds can be represented in a number of ways:” | CONFIRM | ☐ |
| 3 | `4CH1-CON-HOMOLOGOUS-SERIES` | CONCE | Homologous series and functional groups | 4CH1-4.3 (core) | high | NOTE: “Three important terms to know in this topic are **homologous series**, **functio” | CONFIRM | ☐ |
| 4 | `4CH1-CON-IUPAC-NAMING` | CONCE | IUPAC naming of organic compounds (stems and suffixes) | 4CH1-4.4 (core) | high | NOTE: “The names of organic compounds have two parts: the prefix or stem and the end pa” | CONFIRM | ☐ |
| 5 | `4CH1-CON-ISOMERS` | CONCE | Isomers and drawing possible structures from a molecular formula | 4CH1-4.5 (core) | high | NOTE: “**Isomers** are compounds that have the same **molecular** formula but different” | CONFIRM | ☐ |
| 6 | `4CH1-CON-ORGANIC-REACTION-CLASSES` | CONCE | Classifying organic reactions (substitution, addition, combustion) | 4CH1-4.6 (core) | high | NOTE: “The reactions of organic compounds can be classified into” | CONFIRM | ☐ |
| 7 | `4CH1-CON-CRUDE-OIL` | CONCE | Crude oil as a mixture of hydrocarbons | 4CH1-4.7 (core) | high | NOTE: “Crude oil as a mixture is not a very useful substance” | CONFIRM | ☐ |
| 8 | `4CH1-CON-CRUDE-OIL-FRACTIONS` | CONCE | Fractional distillation of crude oil — the fractions, their uses and their trends | 4CH1-4.8 (core); 4CH1-4.9 (core); 4CH1-4.10 (core) | high | NOTE: “The fractions in petroleum are separated from each other in a process called **f” | CONFIRM | ☐ |
| 9 | `4CH1-CON-FUELS-COMBUSTION` | CONCE | Fuels and the products of complete and incomplete combustion | 4CH1-4.11 (core); 4CH1-4.12 (core) | high | NOTE: “A fuel is a substance that, when burned, releases heat energy (exothermic reacti” | CONFIRM | ☐ |
| 10 | `4CH1-CON-CO-POISONING` | CONCE | Why carbon monoxide is poisonous (blood oxygen transport) | 4CH1-4.13 (core) | high | NOTE: “Carbon monoxide (CO) is a highly poisonous gas produced during the incomplete co” | CONFIRM | ☐ |
| 11 | `4CH1-CON-ACID-RAIN-CAUSES` | CONCE | Nitrogen oxides and sulfur dioxide as acid-rain causes | 4CH1-4.14 (core); 4CH1-4.16 (core) | high | NOTE: “These compounds (NO and NO<sub>2</sub>) are formed when nitrogen and oxygen reac” | CONFIRM | ☐ |
| 12 | `4CH1-CON-CRACKING` | CONCE | Catalytic cracking of long-chain fractions (process and why it is necessary) | 4CH1-4.17 (core); 4CH1-4.18 (core) | high | NOTE: “Cracking is an industrial process used to break **low demand, long chain hydroca” | CONFIRM | ☐ |
| 13 | `4CH1-CON-ALKANES` | CONCE | Alkanes (general formula, saturated hydrocarbons, first five members) | 4CH1-4.19 (core); 4CH1-4.20 (core); 4CH1-4.21 (core) | high | NOTE: “of the alkanes is **C**<sub><b>n</b></sub>**H**<sub><b>2n+2</b></sub>” | CONFIRM | ☐ |
| 14 | `4CH1-CON-ALKANE-HALOGEN-SUBSTITUTION` | CONCE | Alkane substitution reactions with halogens under ultraviolet radiation | 4CH1-4.22 (core) | high | NOTE: “Alkanes undergo a substitution reaction with halogens in the presence of ultravi” | CONFIRM | ☐ |
| 15 | `4CH1-MIS-KEROSENE-DOUBLE-BONDS` | MISCO | Claiming kerosene (a crude-oil fraction) contains double bonds | — | high | MARK_SCHEME: “Reject references to double bonds in kerosene” | CONFIRM | ☐ |

Identity-policy notes (split-first; merges are operator-only, OD-1 operand rule): pass-2 flags the 4.8-4.10 one-family ruling (B9-ID-01), the 4.11-4.12 one-family ruling (B9-ID-02), the 4.14+4.16 one-family ruling (B9-ID-03), the 4.17-4.18 one-family ruling (B9-ID-04), the 4.19-4.21 one-family ruling (B9-ID-05), and the ONE single-Reject-column misconception mint (B9-ID-06). All are operator identity decisions (template §identity_decisions). No batch-9 SP attaches a practical node (none is practical-typed; the 4CH1-4.43C practical belongs to batch 11's slice).

## 3. Authored semantic edges (20)

| # | edge | conf | derivation | evidence (anchor → quote) | pass-2 | operator |
|---|---|---|---|---|---|---|
| 1 | `4CH1-CON-ORGANIC-FORMULAE REQUIRES_PREREQUISITE 4CH1-CON-HYDROCARBON` | high | EXPLICIT_TEACH_SEQUENCE | NOTE: “Organic compounds can be represented in a number of ways:” | CONFIRM | ☐ |
| 2 | `4CH1-CON-IUPAC-NAMING REQUIRES_PREREQUISITE 4CH1-CON-HOMOLOGOUS-SERIES` | high | EXPLICIT_TEACH_SEQUENCE | NOTE: “The suffix tells you what **functional group** is on the compound” | CONFIRM | ☐ |
| 3 | `4CH1-CON-ISOMERS REQUIRES_PREREQUISITE 4CH1-CON-ORGANIC-FORMULAE` | high | USED_WITHOUT_RETEACHING | NOTE: “**Isomers** are compounds that have the same **molecular** formula but different” | CONFIRM | ☐ |
| 4 | `4CH1-CON-ORGANIC-REACTION-CLASSES REQUIRES_PREREQUISITE 4CH1-CON-HOMOLOGOUS-SERIES` | high | USED_WITHOUT_RETEACHING | NOTE: “A **substitution** reaction takes place when one functional group is replaced by” | CONFIRM | ☐ |
| 5 | `4CH1-CON-CRUDE-OIL REQUIRES_PREREQUISITE 4CH1-CON-HYDROCARBON` | high | USED_WITHOUT_RETEACHING | NOTE: “However, the different hydrocarbons that make up the mixture, called fractions, ” | CONFIRM | ☐ |
| 6 | `4CH1-CON-CRUDE-OIL-FRACTIONS REQUIRES_PREREQUISITE 4CH1-CON-CRUDE-OIL` | high | EXPLICIT_TEACH_SEQUENCE | NOTE: “Crude oil as a mixture is not a very useful substance” | CONFIRM | ☐ |
| 7 | `4CH1-CON-FUELS-COMBUSTION REQUIRES_PREREQUISITE 4CH1-CON-CRUDE-OIL-FRACTIONS` | high | EXPLICIT_TEACH_SEQUENCE | NOTE: “Non-renewable fossil fuels are obtained from **crude oil** by fractional distill” | CONFIRM | ☐ |
| 8 | `4CH1-CON-CO-POISONING REQUIRES_PREREQUISITE 4CH1-CON-FUELS-COMBUSTION` | high | EXPLICIT_TEACH_SEQUENCE | NOTE: “Carbon monoxide (CO) is a highly poisonous gas produced during the incomplete co” | CONFIRM | ☐ |
| 9 | `4CH1-CON-ACID-RAIN-CAUSES REQUIRES_PREREQUISITE 4CH1-CON-FUELS-COMBUSTION` | high | USED_WITHOUT_RETEACHING | NOTE: “The sulfur dioxide produced from the combustion of fossil fuels dissolves in rai” | CONFIRM | ☐ |
| 10 | `4CH1-CON-CRACKING REQUIRES_PREREQUISITE 4CH1-CON-CRUDE-OIL-FRACTIONS` | high | EXPLICIT_TEACH_SEQUENCE | NOTE: “The demand for certain fractions outstrips the supply so **cracking** is used to” | CONFIRM | ☐ |
| 11 | `4CH1-CON-ALKANES REQUIRES_PREREQUISITE 4CH1-CON-HOMOLOGOUS-SERIES` | high | USED_WITHOUT_RETEACHING | NOTE: “of the alkanes is **C**<sub><b>n</b></sub>**H**<sub><b>2n+2</b></sub>” | CONFIRM | ☐ |
| 12 | `4CH1-CON-ALKANE-HALOGEN-SUBSTITUTION REQUIRES_PREREQUISITE 4CH1-CON-ALKANES` | high | EXPLICIT_TEACH_SEQUENCE | NOTE: “Alkanes undergo a substitution reaction with halogens in the presence of ultravi” | CONFIRM | ☐ |
| 13 | `4CH1-CON-ALKANE-HALOGEN-SUBSTITUTION REQUIRES_PREREQUISITE 4CH1-CON-ORGANIC-REACTION-CLASSES` | high | USED_WITHOUT_RETEACHING | NOTE: “In a substitution reaction, one atom is swapped with another atom” | CONFIRM | ☐ |
| 14 | `4CH1-CON-CRUDE-OIL-FRACTIONS REQUIRES_PREREQUISITE 4CH1-CON-FRACTIONAL-DISTILLATION` | high | USED_WITHOUT_RETEACHING | NOTE: “The fractions in petroleum are separated from each other in a process called **f” | CONFIRM | ☐ |
| 15 | `4CH1-CON-ORGANIC-FORMULAE REQUIRES_PREREQUISITE 4CH1-CON-EMPIRICAL-FORMULA` | high | USED_WITHOUT_RETEACHING | NOTE: “The **empirical formula** shows the **simplest possible ratio** of the atoms in ” | CONFIRM | ☐ |
| 16 | `4CH1-CON-ORGANIC-FORMULAE REQUIRES_PREREQUISITE 4CH1-CON-MOLECULAR-FORMULA` | high | USED_WITHOUT_RETEACHING | NOTE: “The **molecular formula** shows the **actual number** of atoms in a molecule” | CONFIRM | ☐ |
| 17 | `4CH1-CON-FUELS-COMBUSTION REQUIRES_PREREQUISITE 4CH1-CON-COMBUSTION-O2` | high | USED_WITHOUT_RETEACHING | NOTE: “Complete combustion occurs when there is **excess oxygen**” | CONFIRM | ☐ |
| 18 | `4CH1-CON-CRUDE-OIL REQUIRES_PREREQUISITE 4CH1-CON-MIXTURE` | high | USED_WITHOUT_RETEACHING | NOTE: “Crude oil as a mixture is not a very useful substance” | CONFIRM | ☐ |
| 19 | `4CH1-MIS-KEROSENE-DOUBLE-BONDS WRONG_ANSWER_PATTERN 4CH1-CON-CRUDE-OIL-FRACTIONS` | high | ASSESSMENT_DOCUMENTED | MARK_SCHEME: “Reject references to double bonds in kerosene” | CONFIRM | ☐ |
| 20 | `4CH1-MIS-KEROSENE-DOUBLE-BONDS REMEDIATED_BY 4CH1-CON-CRUDE-OIL-FRACTIONS` | high | ASSESSMENT_DOCUMENTED | NOTE: “Most fractions contain mainly **alkanes**, which are compounds of carbon and hyd” | CONFIRM | ☐ |

FIVE edges are CROSS-SECTION boundary edges into the ruled targets (sanctioned per the session-62 cross-slice ruling — no duplicate mint): the 4.8 industrial-distillation row (into the batch-1 CON-FRACTIONAL-DISTILLATION owner), the 4.2 representation rows (into the pilot CON-EMPIRICAL-FORMULA and CON-MOLECULAR-FORMULA owners), the 4.11/4.12 oxygen row (into the batch-5 CON-COMBUSTION-O2 owner) and the 4.7 mixture row (into the batch-1 CON-MIXTURE owner). The THIRTEEN in-slice RP edges carry the teaching sequence the notes themselves establish.

## 4. Held candidates (9) — the abstention record

| id | candidate | failure class / reason |
|---|---|---|
| B9-H-01 | REQUIRES_PREREQUISITE(CON-ISOMERS, CON-IUPAC-NAMING) | AVAILABLE-BUT-SURFACE-MINIMAL |
| B9-H-02 | REQUIRES_PREREQUISITE(CON-FUELS-COMBUSTION, CON-EXO-ENDO) | NAMING-APPLIED-AS-GIVEN (the B7-H-03 rule) |
| B9-H-03 | RELATED_TO(CON-ACID-RAIN-CAUSES, CON-CO2-GREENHOUSE) | SAME-FAMILY-ADJACENCY |
| B9-H-04 | REQUIRES_PREREQUISITE(CON-CRACKING, CON-CATALYST) | MECHANISM-APPLIED-AS-GIVEN |
| B9-H-05 | REQUIRES_PREREQUISITE(CON-CRACKING, CON-EXO-ENDO) | ENRICHMENT-NOT-LOAD-BEARING |
| B9-H-06 | REQUIRES_PREREQUISITE(CON-ALKANES, CON-COMBUSTION-O2) | BOUNDARY-TARGETS-ONCE |
| B9-H-07 | RELATED_TO(CON-ALKANE-HALOGEN-SUBSTITUTION, CON-G7-DISPLACEMENT) | SAME-REAGENT-DIFFERENT-DEMAND |
| B9-H-08 | REQUIRES_PREREQUISITE(CON-CRUDE-OIL-FRACTIONS, CON-SIMPLE-MOLECULAR) | EXPLANATION-DEEPER-THAN-DEMAND |
| B9-H-09 | REQUIRES_PREREQUISITE(CON-HYDROCARBON, CON-COMPOUND) | NAMING-APPLIED-AS-GIVEN (the B7-H-03 rule) |

Every held candidate cites its §19 failure class; the abstention record remains part of the graph provenance. A held record is a valid outcome — the abstention is the system's honest output.

## 5. Operator verdict surface

- **20 SUGGESTED edges** (B9-E-01..20) — the §18 promotion surface
- **15 nodes** (14 CONCEPT B9-N-01..14 + 1 MISCONCEPTION B9-M-01) — node authority stays SUGGESTED; nodes have no §18 pathway (node promotion is a separate identity decision, deferred)
- **6 identity decisions** (B9-ID-01..06) — MERGE/SPLIT/KEEP_AS_IS
- **9 held candidates** — acknowledge the quarantine (no reopening)
- **0 REVIEW_REQUIRED edges** — zero RR settlements needed

Pathway: fill `scripts/c11_batch9_verdicts_template.yaml` → rename to `c11_batch9_verdicts.yaml` → a later session encodes + applies via `c11_verdict_encode_batch9`-style reconciliation + `c11_promote.py` (§18) + the gated generator re-run. NOTHING is promoted at this gate.
