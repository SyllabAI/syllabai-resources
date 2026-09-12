# T-C11 §16 Batch 3 Review Sheet — Concept / Prerequisite / Misconception Graph

Slice 4CH1-1.37–1.60C (the FULL S1 remainder: ionic + covalent + metallic bonding + electrolysis, 24 SPs) + practical PR-04 · generated 2026-09-12 · decision record `scripts/c11_batch3_decisions.yaml` (pass 1: `c11-s16-batch-3`) · adversarial pass 2: `scripts/c11_batch3_review_pass2.yaml` · authorization: `scripts/c11_s16_authorization.yaml` (§16 authorized 2026-09-12; batch 3 commissioned by the operator's session-51 move-forward directive — the whole S1 remainder in one batch; FN-B2-1 closed: the Paper-2 topic MS set is pinned)

**NOTHING in this batch is authoritative.** All 24 nodes / 64 batch edges are AI_SUGGESTED (SUGGESTED). HUMAN_VALIDATED is reachable only by your promotion command via the §18 pathway (`scripts/c11_promote.py` → `scripts/c11_promotions.yaml` → **Zero batch-3 promotions exist.** This sheet is the batch's operator gate: record verdicts in `scripts/c11_batch3_verdicts_template.yaml` (fill + rename to `c11_batch3_verdicts.yaml`); a later session encodes and applies them.)

How to review: for each row check the quoted evidence actually appears in the cited file and actually says what the record claims; then rule on the relation CLASS and direction, not just existence. Machine state: the full gate suite is green at the merged 91-node / 220-edge store; every quote is machine-verified byte-for-byte against its source file (G03/c11.4); the 4.15 negative control is uncovered. Six edges are CROSS-BOUNDARY into batch-2 nodes (CON-ATOM ×2, CON-ELECTRONIC-CONFIGURATION ×2, CON-MOLECULE ×2 — sanctioned per FN-B1-2/FN-B2-2; no duplicate concept was minted). One mark-scheme quote preserves the pinned artifact's line wrap ("atoms/molecul es/electrons" — FP-B3-5, layout-verified against the PDF).

## 1. Totals & second-pass agreement

| | nodes | authored edges | held | |
|---|---|---|---|
| pass-1 (extraction) | 24 | 39 (+25 derived PART_OF) | 14 |
| pass-2 verdicts | 24 CONFIRM(+note) | 39 CONFIRM(+note) · 0 HOLD · 0 REJECT | all 14 AGREE |

Raw agreement (NOT κ — single human rater, architecture §12): nodes 24/24 = 100.0%; edges — of the 39 edges pass-1 asserted (SUGGESTED), pass-2 confirmed 39 (100.0%); pass-1 quarantined 0 edges as REVIEW_REQUIRED (this batch authored NONE — every doubt was held or resolved on explicit evidence). **Zero pass-2 demotions.**

Forecast calibration (C11_BATCH_FORECAST.json future_batch_records): predicted 57.6 nodes / 66 edges / 24 held vs actual 24 / 39 / 14 — nodes −58.3%, edges −40.9%, held −41.7%. The delta is the boundary discipline + bond-family granularity, not thin coverage: no batch-2 identity was re-minted (ION/CBOND/DCC/SM reach ATOM/ELECTRONIC-CONFIGURATION/MOLECULE via 6 sanctioned boundary edges); the spec's own know/understand pairs were merged as dual attachments (1.43+1.56C, 1.44+1.45, 1.51+1.55C, 1.52C+1.53C); and 1.60C attaches no concept node (the practical owns it — the 1.13 precedent).

## 2. Concept & misconception nodes (24)

| # | code | family | title | attaches to (role) | conf | evidence (anchor → quote) | pass-2 | operator |
|---|---|---|---|---|---|---|---|---|
| 1 | `4CH1-CON-ION` | CONCE | Ion (formation by electron loss or gain) | 4CH1-1.37 (core) | high | NOTE: “An ion is an electrically charged atom or group of atoms formed by the loss or gain of electrons” | CONFIRM | ☐ |
| 2 | `4CH1-CON-ION-CHARGE-RULES` | CONCE | Common ion charges (group-based and named-ion table, with the deduction rule) | 4CH1-1.38 (core) | high | NOTE: “Find the number of electrons in the outer electron shell” | CONFIRM_WITH_NOTE | ☐ |
| 3 | `4CH1-CON-IONIC-FORMULA` | CONCE | Writing formulae for ionic compounds (charge cancellation and swap-and-drop) | 4CH1-1.39 (core) | high | NOTE: “Ionic compounds typically have no overall charge” | CONFIRM | ☐ |
| 4 | `4CH1-CON-DOT-CROSS-IONIC` | CONCE | Dot-and-cross diagrams for ionic compounds (electron transfer) | 4CH1-1.40 (core) | high | NOTE: “Ionic bonds can be represented diagrammatically using dot-and-cross diagrams” | CONFIRM | ☐ |
| 5 | `4CH1-CON-IONIC-BOND` | CONCE | Ionic bonding (electrostatic attraction between oppositely charged ions) | 4CH1-1.41 (core) | high | NOTE: “Between positive and negative ions are strong electrostatic forces of attraction which act in all di” | CONFIRM | ☐ |
| 6 | `4CH1-CON-IONIC-LATTICE` | CONCE | Giant ionic lattice and why ionic compounds have high melting and boiling points | 4CH1-1.42 (core) | high | NOTE: “Thousands of positive and negative ions in an ionic compound form a giant lattice structure” | CONFIRM | ☐ |
| 7 | `4CH1-CON-IONIC-CONDUCTION` | CONCE | Ionic conduction (solid insulator; molten and aqueous conductor via mobile ions) | 4CH1-1.43 (core); 4CH1-1.56C (core) | high | NOTE: “Ionic compounds are poor conductors in the solid state” | CONFIRM_WITH_NOTE | ☐ |
| 8 | `4CH1-CON-COVALENT-BOND` | CONCE | Covalent bond (shared pair of electrons; electrostatic attraction between the shared pair and the nuclei) | 4CH1-1.44 (core); 4CH1-1.45 (core) | high | NOTE: “Non-metal atoms can share electrons with other non-metal atoms to obtain a full outer shell of elect” | CONFIRM_WITH_NOTE | ☐ |
| 9 | `4CH1-CON-DOT-CROSS-COVALENT` | CONCE | Dot-and-cross diagrams for covalent substances (diatomic, inorganic and organic molecules) | 4CH1-1.46 (core) | high | NOTE: “Small covalent molecules can be represented by dot and cross diagrams” | CONFIRM | ☐ |
| 10 | `4CH1-CON-SIMPLE-MOLECULAR` | CONCE | Simple molecular structures (weak intermolecular forces; low melting and boiling points; the relative-molecular-mass trend) | 4CH1-1.47 (core); 4CH1-1.48 (core) | high | NOTE: “Simple molecular structures have covalent bonds joining the atoms together, but intermolecular force” | CONFIRM_WITH_NOTE | ☐ |
| 11 | `4CH1-CON-GIANT-COVALENT` | CONCE | Giant covalent structures (solids with high melting and boiling points) | 4CH1-1.49 (core) | high | NOTE: “Giant covalent structures are solids with high melting points” | CONFIRM | ☐ |
| 12 | `4CH1-CON-DIAMOND-GRAPHITE` | CONCE | Structures and properties of diamond, graphite and C60 fullerene (allotropes of carbon) | 4CH1-1.50 (core) | high | NOTE: “Diamond and graphite are allotropes of carbon” | CONFIRM_WITH_NOTE | ☐ |
| 13 | `4CH1-CON-COVALENT-CONDUCTION` | CONCE | Covalent compounds do not conduct electricity (no freely moving charged particles) | 4CH1-1.51 (core); 4CH1-1.55C (core) | high | NOTE: “Simple molecular structures are poor conductors of electricity (even when molten)” | CONFIRM_WITH_NOTE | ☐ |
| 14 | `4CH1-CON-METALLIC-BOND` | CONCE | Metallic bonding (positive metal ions and delocalised electrons; the 2-D metallic lattice representation) | 4CH1-1.52C (core); 4CH1-1.53C (core) | high | NOTE: “Metals consist of giant structures of atoms arranged in a regular pattern” | CONFIRM_WITH_NOTE | ☐ |
| 15 | `4CH1-CON-METAL-PROPERTIES` | CONCE | Typical physical properties of metals (electrical conductivity and malleability) and their explanations | 4CH1-1.54C (core) | high | NOTE: “Metals conduct electricity” | CONFIRM | ☐ |
| 16 | `4CH1-CON-ANODE-CATHODE` | CONCE | Anions and cations (negative and positive ions) and their migration to cathode and anode | 4CH1-1.57C (core) | high | NOTE: “Anions are negatively charged ions” | CONFIRM_WITH_NOTE | ☐ |
| 17 | `4CH1-CON-ELECTROLYSIS` | CONCE | Electrolysis (decomposition by direct current: molten binary compounds and their element products, using inert electrodes) | 4CH1-1.58C (core) | high | NOTE: “These compounds undergo electrolysis and always produce their corresponding element” | CONFIRM | ☐ |
| 18 | `4CH1-CON-AQUEOUS-DISCHARGE` | CONCE | Selective discharge in aqueous electrolysis (halide preference at the anode; hydrogen vs metal at the cathode) | 4CH1-1.58C (core) | high | NOTE: “Which ions get discharged and at which electrode depends on the relative reactivity of the elements ” | CONFIRM_WITH_NOTE | ☐ |
| 19 | `4CH1-CON-ELECTRODE-HALF-EQUATIONS` | CONCE | Ionic half-equations for the electrode reactions during electrolysis | 4CH1-1.59C (core) | high | NOTE: “This can be illustrated using half equations which describe the movement of electrons at each electr” | CONFIRM | ☐ |
| 20 | `4CH1-CON-REDOX-ELECTRONS` | CONCE | Oxidation and reduction in terms of electron loss and gain | 4CH1-1.59C (core) | high | NOTE: “Oxidation is when a substance loses electrons” | CONFIRM | ☐ |
| 21 | `4CH1-MIS-IONIC-CONDUCTION-ELECTRONS` | MISCO | Believing ionic compounds conduct electricity because electrons move and carry the charge | — | high | NOTE: “A common mistake students make in exams is to say that ionic compounds conduct electricity because '”<br>remediation: “When the ionic compound is melted or dissolved in water, the ions are able to mo” | CONFIRM | ☐ |
| 22 | `4CH1-MIS-IONIC-BOND-ATOMS` | MISCO | Describing ionic bonding as attraction between atoms or molecules (or as intermolecular forces) | — | high | MARK_SCHEME: “intermolecular forces”<br>remediation: “Between positive and negative ions are strong electrostatic forces of attraction” | CONFIRM_WITH_NOTE | ☐ |
| 23 | `4CH1-MIS-COVALENT-BONDS-BROKEN` | MISCO | Saying covalent bonds are broken when simple molecular substances melt or boil (instead of weak intermolecular forces) | — | high | MARK_SCHEME: “Any reference to bonds between molecules”<br>remediation: “Remember: When explaining the low melting and boiling point of simple molecular ” | CONFIRM | ☐ |
| 24 | `4CH1-MIS-GRAPHITE-LAYER-BONDS` | MISCO | Saying graphite layers are held together by bonds (instead of weak forces of attraction between the layers) | — | high | MARK_SCHEME: “Any reference to bonds between layers / molecules”<br>remediation: “The layers are free to slide over each other because there are only weak forces ” | CONFIRM_WITH_NOTE | ☐ |

Identity-policy notes (split-first; merges are operator-only, OD-1 operand rule): pass-2 flags the four know/understand dual-attachment pairs (FP-B3-1 — 1.43+1.56C, 1.44+1.45, 1.51+1.55C, 1.52C+1.53C), the CON-SIMPLE-MOLECULAR structure-vs-IMF split question, the CON-DIAMOND-GRAPHITE three-allotrope block, the CON-METALLIC-BOND representation-vs-mechanism pair and the 1.58C dual node attachment. All are operator identity decisions (template §identity_decisions, B3-ID-01..07). 1.60C attaches NO batch-3 concept node (the practical PR-04 owns it — the 1.13 precedent; the explicit gap is §5 FN-B3-3).

## 3. Authored semantic edges (39)

Direction conventions: REQUIRES_PREREQUISITE source=dependent → target=prerequisite; EXPLAINED_BY explained → explainer; RELATED_TO is a residual concept-to-concept association; COMMONLY_CONFUSED_WITH is a symmetric term-pair relation stored one-directionally; WRONG_ANSWER_PATTERN / REMEDIATED_BY / MISCONCEPTION_OF misconception → concept.

### 3.1 REVIEW_REQUIRED (open operator decision)

**None.** This batch authored no REVIEW_REQUIRED edge: the pass-1 authoring either resolved each doubt on explicit evidence or sent the candidate to held (14 rows, §4).

### 3.2 SUGGESTED edges (39) — the §18-promotable surface after verdicts

Flagged rows (pre-triage FLAGGED in the verdict template): the relation-class choice on the EXPLAINED_BY edge, the density flag on ELECTROLYSIS→IONIC-BOND, the FIRST RELATED_TO deployment, the SECOND COMMONLY_CONFUSED_WITH deployment, the vocabulary-level SIMPLE-MOLECULAR→MOLECULE class, and the four remediation-target=misconception-target rows (the batch-1 B1-E-25 pattern) + the MIS-GRAPHITE-LAYER-BONDS family-overlap rows.

| edge | method | conf | evidence (quote) | upstream | pass-2 | operator |
|---|---|---|---|---|---|---|
| `4CH1-CON-ANODE-CATHODE` **REQUIRES_PREREQUISITE** `4CH1-CON-ION` | DEFINITIONAL_DEPENDENCY | high | “Anions are negatively charged ions” | T-C10 HUMAN_VALIDATED 4CH1-1.57C @ Electronic Conductivity (2026-09-11) | CONFIRM | ☐ |
| `4CH1-CON-AQUEOUS-DISCHARGE` **REQUIRES_PREREQUISITE** `4CH1-CON-ELECTROLYSIS` | USED_WITHOUT_RETEACHING | high | “We now have an electrolyte that contains ions from the compound plus ions from the water” | T-C10 HUMAN_VALIDATED 4CH1-1.58C @ Electrolysis Diagram (2026-09-11) | CONFIRM | ☐ |
| `4CH1-CON-COVALENT-BOND` **REQUIRES_PREREQUISITE** `4CH1-CON-ATOM` | DEFINITIONAL_DEPENDENCY | high | “When atoms share pairs of electrons, they form covalent bonds” | T-C10 HUMAN_VALIDATED 4CH1-1.44 @ Forming Covalent Bonds (2026-09-11); target node owne... | CONFIRM | ☐ |
| `4CH1-CON-COVALENT-BOND` **REQUIRES_PREREQUISITE** `4CH1-CON-ELECTRONIC-CONFIGURATION` | DEFINITIONAL_DEPENDENCY | high | “Non-metal atoms can share electrons with other non-metal atoms to obtain a full outer shell of elect” | T-C10 HUMAN_VALIDATED 4CH1-1.44 @ Forming Covalent Bonds (2026-09-11); target node owne... | CONFIRM | ☐ |
| `4CH1-CON-COVALENT-CONDUCTION` **REQUIRES_PREREQUISITE** `4CH1-CON-SIMPLE-MOLECULAR` | USED_WITHOUT_RETEACHING | high | “Simple molecular structures are poor conductors of electricity (even when molten)”<br>“There are no free ions or electrons to move and carry the charge” | T-C10 HUMAN_VALIDATED 4CH1-1.51 @ Simple Molecular Structures (2026-09-11); T-C10 HUMAN... | CONFIRM | ☐ |
| `4CH1-CON-DIAMOND-GRAPHITE` **RELATED_TO** `4CH1-CON-SIMPLE-MOLECULAR` ⚑ | RELATED_RESIDUAL | medium | “C60 is a simple molecular structure” | T-C10 HUMAN_VALIDATED 4CH1-1.50 @ Simple Molecular Structures (2026-09-11) | CONFIRM_WITH_NOTE | ☐ |
| `4CH1-CON-DIAMOND-GRAPHITE` **REQUIRES_PREREQUISITE** `4CH1-CON-GIANT-COVALENT` | USED_WITHOUT_RETEACHING | high | “Examples include diamond and graphite” | T-C10 HUMAN_VALIDATED 4CH1-1.49/1.50 @ Giant Covalent Structures (2026-09-11) | CONFIRM | ☐ |
| `4CH1-CON-DOT-CROSS-COVALENT` **REQUIRES_PREREQUISITE** `4CH1-CON-COVALENT-BOND` | USED_WITHOUT_RETEACHING | high | “Each covalent bond represents one shared pair of electrons” | T-C10 HUMAN_VALIDATED 4CH1-1.46 @ Covalent Bonds: Dot & Cross Diagrams (2026-09-11) | CONFIRM | ☐ |
| `4CH1-CON-DOT-CROSS-COVALENT` **REQUIRES_PREREQUISITE** `4CH1-CON-MOLECULE` | DEFINITIONAL_DEPENDENCY | high | “Dot & cross representation of a molecule of hydrogen” | T-C10 HUMAN_VALIDATED 4CH1-1.46 @ Covalent Bonds: Dot & Cross Diagrams (2026-09-11); ta... | CONFIRM | ☐ |
| `4CH1-CON-DOT-CROSS-IONIC` **REQUIRES_PREREQUISITE** `4CH1-CON-ION` | USED_WITHOUT_RETEACHING | high | “A chlorine atom will gain an electron to form a negatively charged chloride ion with a charge of 1-” | T-C10 HUMAN_VALIDATED 4CH1-1.37/1.40 @ Ionic Bonding Diagrams (2026-09-11) | CONFIRM | ☐ |
| `4CH1-CON-ELECTRODE-HALF-EQUATIONS` **REQUIRES_PREREQUISITE** `4CH1-CON-ELECTROLYSIS` | USED_WITHOUT_RETEACHING | high | “As the ions come into contact with the electrode, electrons are either lost or gained and they form ” | T-C10 HUMAN_VALIDATED 4CH1-1.59C @ Half Equations (2026-09-11) | CONFIRM | ☐ |
| `4CH1-CON-ELECTRODE-HALF-EQUATIONS` **REQUIRES_PREREQUISITE** `4CH1-CON-REDOX-ELECTRONS` | DEFINITIONAL_DEPENDENCY | high | “hence the definitions of oxidation and reduction are applied in terms of electron loss or gain rathe” | T-C10 HUMAN_VALIDATED 4CH1-1.59C @ Half Equations (2026-09-11) | CONFIRM | ☐ |
| `4CH1-CON-ELECTROLYSIS` **REQUIRES_PREREQUISITE** `4CH1-CON-ANODE-CATHODE` | USED_WITHOUT_RETEACHING | high | “The positive ion will migrate towards the cathode and the negative ion will migrate towards the anod” | T-C10 HUMAN_VALIDATED 4CH1-1.58C @ Electrolysis Diagram (2026-09-11) | CONFIRM | ☐ |
| `4CH1-CON-ELECTROLYSIS` **REQUIRES_PREREQUISITE** `4CH1-CON-IONIC-BOND` ⚑ | USED_WITHOUT_RETEACHING | high | “Binary ionic compound are compounds consisting of just two elements joined together by ionic bonding” | T-C10 HUMAN_VALIDATED 4CH1-1.58C @ Electrolysis Diagram (2026-09-11) | CONFIRM_WITH_NOTE | ☐ |
| `4CH1-CON-ELECTROLYSIS` **REQUIRES_PREREQUISITE** `4CH1-CON-IONIC-CONDUCTION` | USED_WITHOUT_RETEACHING | high | “When these compounds are heated beyond their melting point, they become molten and can conduct elect” | T-C10 HUMAN_VALIDATED 4CH1-1.58C @ Electrolysis Diagram (2026-09-11) | CONFIRM | ☐ |
| `4CH1-CON-GIANT-COVALENT` **REQUIRES_PREREQUISITE** `4CH1-CON-COVALENT-BOND` | DEFINITIONAL_DEPENDENCY | high | “They have a huge number of non-metal atoms bonded to other non-metal atoms via strong covalent bonds” | T-C10 HUMAN_VALIDATED 4CH1-1.49 @ Giant Covalent Structures (2026-09-11) | CONFIRM | ☐ |
| `4CH1-CON-ION` **REQUIRES_PREREQUISITE** `4CH1-CON-ATOM` | DEFINITIONAL_DEPENDENCY | high | “An ion is an electrically charged atom or group of atoms formed by the loss or gain of electrons” | T-C10 HUMAN_VALIDATED 4CH1-1.37 @ Formation of Ions (2026-09-11); target node owned by ... | CONFIRM | ☐ |
| `4CH1-CON-ION` **REQUIRES_PREREQUISITE** `4CH1-CON-ELECTRONIC-CONFIGURATION` | DEFINITIONAL_DEPENDENCY | high | “This loss or gain of electrons takes place to obtain a full outer shell of electrons” | T-C10 HUMAN_VALIDATED 4CH1-1.37 @ Formation of Ions (2026-09-11); target node owned by ... | CONFIRM | ☐ |
| `4CH1-CON-ION-CHARGE-RULES` **REQUIRES_PREREQUISITE** `4CH1-CON-ION` | USED_WITHOUT_RETEACHING | high | “Atoms that gain electrons become negative ions and atoms that donate electron forms positive ion” | T-C10 HUMAN_VALIDATED 4CH1-1.37/1.38 @ Common Ions (2026-09-11) | CONFIRM | ☐ |
| `4CH1-CON-IONIC-BOND` **COMMONLY_CONFUSED_WITH** `4CH1-CON-COVALENT-BOND` ⚑ | EXAMINER_TIP_EXPLICIT | high | “A key difference between covalent bonds and ionic bonds is that in covalent bonds the electrons are ” | T-C10 HUMAN_VALIDATED 4CH1-1.44 @ Forming Covalent Bonds (2026-09-11); assessment conte... | CONFIRM_WITH_NOTE | ☐ |
| `4CH1-CON-IONIC-BOND` **REQUIRES_PREREQUISITE** `4CH1-CON-ION` | DEFINITIONAL_DEPENDENCY | high | “Between positive and negative ions are strong electrostatic forces of attraction which act in all di” | T-C10 HUMAN_VALIDATED 4CH1-1.41 @ Ionic Bonding and Lattices (2026-09-11) | CONFIRM | ☐ |
| `4CH1-CON-IONIC-CONDUCTION` **REQUIRES_PREREQUISITE** `4CH1-CON-ION` | DEFINITIONAL_DEPENDENCY | high | “When the ionic compound is melted or dissolved in water, the ions are able to move and carry a charg” | T-C10 HUMAN_VALIDATED 4CH1-1.43 @ Ionic Bonding and Lattices (2026-09-11) | CONFIRM | ☐ |
| `4CH1-CON-IONIC-CONDUCTION` **REQUIRES_PREREQUISITE** `4CH1-CON-IONIC-LATTICE` | DEFINITIONAL_DEPENDENCY | high | “The ions are in fixed positions in the lattice” | T-C10 HUMAN_VALIDATED 4CH1-1.43 @ Ionic Bonding and Lattices (2026-09-11) | CONFIRM | ☐ |
| `4CH1-CON-IONIC-FORMULA` **REQUIRES_PREREQUISITE** `4CH1-CON-ION-CHARGE-RULES` | DEFINITIONAL_DEPENDENCY | high | “The formulae of simple ionic compounds can be determined if you know the charge on the ions” | T-C10 HUMAN_VALIDATED 4CH1-1.39 @ Formula of Ionic Compounds (2026-09-11) | CONFIRM | ☐ |
| `4CH1-CON-IONIC-LATTICE` **REQUIRES_PREREQUISITE** `4CH1-CON-IONIC-BOND` | DEFINITIONAL_DEPENDENCY | high | “There are strong electrostatic forces of attraction between oppositely charged ions in all direction” | T-C10 HUMAN_VALIDATED 4CH1-1.41/1.42 @ Ionic Bonding and Lattices (2026-09-11) | CONFIRM | ☐ |
| `4CH1-CON-METAL-PROPERTIES` **EXPLAINED_BY** `4CH1-CON-METALLIC-BOND` ⚑ | SINGLE_SOURCE_CAUSAL_TEACHING | high | “This is because the atoms/ions are arranged in layers which can slide over each other when a force i”<br>“There are delocalised electrons available to move and carry charge”<br>“There are strong electrostatic forces of attraction between the positive metal ions and the negative” | T-C10 HUMAN_VALIDATED 4CH1-1.54C @ Metallic Bonding (2026-09-11) | CONFIRM_WITH_NOTE | ☐ |
| `4CH1-CON-METALLIC-BOND` **REQUIRES_PREREQUISITE** `4CH1-CON-ION` | DEFINITIONAL_DEPENDENCY | high | “Within the metal lattice, the atoms lose their outer electrons and become positively charged metal i” | T-C10 HUMAN_VALIDATED 4CH1-1.53C @ Metallic Bonding (2026-09-11) | CONFIRM | ☐ |
| `4CH1-CON-SIMPLE-MOLECULAR` **REQUIRES_PREREQUISITE** `4CH1-CON-COVALENT-BOND` | DEFINITIONAL_DEPENDENCY | high | “Simple molecular structures have covalent bonds joining the atoms together, but intermolecular force” | T-C10 HUMAN_VALIDATED 4CH1-1.47 @ Simple Molecular Structures (2026-09-11) | CONFIRM | ☐ |
| `4CH1-CON-SIMPLE-MOLECULAR` **REQUIRES_PREREQUISITE** `4CH1-CON-MOLECULE` ⚑ | DEFINITIONAL_DEPENDENCY | high | “intermolecular forces that act between neighbouring molecules are weak” | T-C10 HUMAN_VALIDATED 4CH1-1.47 @ Simple Molecular Structures (2026-09-11); target node... | CONFIRM_WITH_NOTE | ☐ |
| `4CH1-MIS-COVALENT-BONDS-BROKEN` **REMEDIATED_BY** `4CH1-CON-SIMPLE-MOLECULAR` ⚑ | ASSESSMENT_DOCUMENTED | high | “it is not the covalent bonds between the atoms which are broken, but the weak intermolecular forces” | T-C10 HUMAN_VALIDATED 4CH1-1.47 @ Simple Molecular Structures (2026-09-11) | CONFIRM_WITH_NOTE | ☐ |
| `4CH1-MIS-COVALENT-BONDS-BROKEN` **WRONG_ANSWER_PATTERN** `4CH1-CON-SIMPLE-MOLECULAR` | ASSESSMENT_DOCUMENTED | high | “Any reference to bonds between molecules” | PMT Unit-1 Paper-2 MS "Covalent Bonding" Q1(d) (pinned scripts/c11_evidence/COVALENT_MS... | CONFIRM | ☐ |
| `4CH1-MIS-GRAPHITE-LAYER-BONDS` **REMEDIATED_BY** `4CH1-CON-DIAMOND-GRAPHITE` ⚑ | ASSESSMENT_DOCUMENTED | high | “The layers are free to slide over each other because there are only weak forces between the layers, ” | T-C10 HUMAN_VALIDATED 4CH1-1.50 @ Giant Covalent Structures (2026-09-11) | CONFIRM_WITH_NOTE | ☐ |
| `4CH1-MIS-GRAPHITE-LAYER-BONDS` **WRONG_ANSWER_PATTERN** `4CH1-CON-DIAMOND-GRAPHITE` ⚑ | ASSESSMENT_DOCUMENTED | high | “Any reference to bonds between layers / molecules” | PMT Unit-1 Paper-2 MS "Covalent Bonding" Q1(b) (pinned scripts/c11_evidence/COVALENT_MS... | CONFIRM_WITH_NOTE | ☐ |
| `4CH1-MIS-IONIC-BOND-ATOMS` **REMEDIATED_BY** `4CH1-CON-IONIC-BOND` ⚑ | ASSESSMENT_DOCUMENTED | high | “Between positive and negative ions are strong electrostatic forces of attraction which act in all di” | T-C10 HUMAN_VALIDATED 4CH1-1.41 @ Ionic Bonding and Lattices (2026-09-11) | CONFIRM_WITH_NOTE | ☐ |
| `4CH1-MIS-IONIC-BOND-ATOMS` **WRONG_ANSWER_PATTERN** `4CH1-CON-IONIC-BOND` | ASSESSMENT_DOCUMENTED | high | “If any reference to attraction between atoms/molecul es/electrons scores 0/3” | PMT Unit-1 Paper-2 MS "Ionic Bonding" Q1(a)/Q2(a)(iii) (pinned scripts/c11_evidence/ION... | CONFIRM | ☐ |
| `4CH1-MIS-IONIC-CONDUCTION-ELECTRONS` **MISCONCEPTION_OF** `4CH1-CON-IONIC-CONDUCTION` | EXAMINER_TIP_EXPLICIT | high | “A common mistake students make in exams is to say that ionic compounds conduct electricity because '” | T-C10 HUMAN_VALIDATED 4CH1-1.43 @ Ionic Bonding and Lattices (2026-09-11) | CONFIRM | ☐ |
| `4CH1-MIS-IONIC-CONDUCTION-ELECTRONS` **REMEDIATED_BY** `4CH1-CON-IONIC-CONDUCTION` ⚑ | EXAMINER_TIP_EXPLICIT | high | “When the ionic compound is melted or dissolved in water, the ions are able to move and carry a charg” | T-C10 HUMAN_VALIDATED 4CH1-1.43 @ Ionic Bonding and Lattices (2026-09-11) | CONFIRM_WITH_NOTE | ☐ |
| `4CH1-PR-04` **REQUIRES_PREREQUISITE** `4CH1-CON-AQUEOUS-DISCHARGE` | USED_WITHOUT_RETEACHING | high | “Sodium chloride solutions produces hydrogen at the cathode and chlorine at the anode” | T-C10 HUMAN_VALIDATED 4CH1-1.58C/1.60C @ Practical: Investigate the Electrolysis of Aqu... | CONFIRM | ☐ |
| `4CH1-PR-04` **REQUIRES_PREREQUISITE** `4CH1-CON-ELECTROLYSIS` | USED_WITHOUT_RETEACHING | high | “To electrolyse aqueous solutions of sodium chloride, sulfuric acid and copper(II)sulfate, and to col” | T-C10 HUMAN_VALIDATED 4CH1-1.58C/1.60C @ Practical: Investigate the Electrolysis of Aqu... | CONFIRM | ☐ |

### 3.3 Derived PART_OF edges (25)

Derived deterministically from node attachments (concepts.yaml); each carries the attachment's evidence anchors and the node's provenance. Not re-listed here — review them via the §2 node rows. Machine-verified: the PART_OF set must exactly equal the declared attachments (c11.7).

## 4. Held / rejected candidates (14) — the abstention record

These were considered and NOT drawn. Review that each hold reason is right (pass-2 already did — column below). Overriding a hold = re-authoring the decision record, never hand-editing the graph.

| id | status | candidate | failing rule | pass-2 | operator |
|---|---|---|---|---|---|
| B3-H-01 | held | `REQUIRES_PREREQUISITE(CON-ION, CON-SUBATOMIC-PARTICLES)` | TRANSITIVELY_SUBSUMED | AGREE_HOLD | ☐ |
| B3-H-02 | held | `REQUIRES_PREREQUISITE(CON-DOT-CROSS-IONIC, CON-ELECTRONIC-CONFIGURATION)` | TRANSITIVELY_SUBSUMED | AGREE_HOLD | ☐ |
| B3-H-03 | held | `REQUIRES_PREREQUISITE(CON-IONIC-FORMULA, CON-COMPOUND)` | VOCABULARY_OPERAND_DUPLICATION | AGREE_HOLD | ☐ |
| B3-H-04 | held | `REQUIRES_PREREQUISITE(CON-ION-CHARGE-RULES, CON-PERIODIC-TABLE)` | OD_2_TABLE_LABEL | AGREE_HOLD | ☐ |
| B3-H-05 | held | `REQUIRES_PREREQUISITE(CON-METALLIC-BOND, CON-ELECTRONIC-CONFIGURATION)` | TRANSITIVELY_SUBSUMED | AGREE_HOLD | ☐ |
| B3-H-06 | held | `REQUIRES_PREREQUISITE(CON-COVALENT-CONDUCTION, CON-COVALENT-BOND)` | TRANSITIVELY_SUBSUMED | AGREE_HOLD | ☐ |
| B3-H-07 | held | `REQUIRES_PREREQUISITE(CON-DOT-CROSS-COVALENT, CON-SIMPLE-MOLECULAR)` | RELATION_CLASS_AMBIGUITY_PLUS_DENSITY | AGREE_HOLD | ☐ |
| B3-H-08 | held | `REQUIRES_PREREQUISITE(CON-REDOX-ELECTRONS, CON-SUBATOMIC-PARTICLES)` | VOCABULARY_OPERAND_DUPLICATION | AGREE_HOLD | ☐ |
| B3-H-09 | held | `REQUIRES_PREREQUISITE(PR-04, CON-ION)` | TRANSITIVELY_SUBSUMED | AGREE_HOLD | ☐ |
| B3-H-10 | held | `REQUIRES_PREREQUISITE(PR-04, CON-ELECTRODE-HALF-EQUATIONS)` | INSUFFICIENT_EVIDENCE | AGREE_HOLD | ☐ |
| B3-H-11 | held | `MISCONCEPTION node "expecting the metal at the cathode of aqueous NaCl electrolysis (e.g. sodiu` | INSUFFICIENT_EVIDENCE | AGREE_HOLD | ☐ |
| B3-H-12 | held | `MISCONCEPTION node "metallic bonding described as intermolecular forces / attraction between at` | EVIDENCE_CLASS_WEAK | AGREE_HOLD | ☐ |
| B3-H-13 | held | `COMMONLY_CONFUSED_WITH(CON-IONIC-CONDUCTION, CON-COVALENT-CONDUCTION)` | INSUFFICIENT_EVIDENCE_FOR_CLASS | AGREE_HOLD | ☐ |
| B3-H-14 | held | `MISCONCEPTION node "hydroxide ions are discharged at the anode in acidic solutions (water molec` | INSUFFICIENT_EVIDENCE | AGREE_HOLD | ☐ |

## 5. Findings (pass-2, for the batch record)

- **FP-B3-1 (split-artifact)** — Know/understand dual attachments: CON-IONIC-CONDUCTION (1.43+1.56C), CON-COVALENT-CONDUCTION (1.51+1.55C), CON-COVALENT-BOND (1.44+1.45), CON-METALLIC-BOND (1.52C+1.53C); dual node attachments on 1.58C (CON-ELECTROLYSIS + CON-AQUEOUS-DISCHARGE) and 1.59C (equations + redox). All operator identity decisions (B3-ID-01..05); no defect — the mirrors of the ratified 1.19/1.20 precedents.
- **FP-B3-2 (relation-class-choice)** — CON-METAL-PROPERTIES EXPLAINED_BY CON-METALLIC-BOND (explicit causal sentences; the prereq reading equally real) and CON-ELECTROLYSIS REQUIRES_PREREQUISITE CON-IONIC-BOND (reachable-ne-redundant density flag) — one relation per pair forced the choices; OD-class decisions for the operator.
- **FP-B3-3 (first-class-deployment)** — The store's FIRST RELATED_TO edge (DIAMOND-GRAPHITE -> SIMPLE-MOLECULAR, the C60 cross-class fact) on the note's explicit "C60 is a simple molecular structure" statement; relation_class_rationale recorded per G08. The alternative (attaching 1.50 to CON-SIMPLE-MOLECULAR) is B3-ID-07. The earlier zero-RL state was honest abstention, not a rule.
- **FP-B3-4 (second-class-deployment)** — The SECOND COMMONLY_CONFUSED_WITH edge (IONIC-BOND -> COVALENT-BOND) on the corpus's explicit share-vs-transfer difference tip; one-directional storage per the batch-2 convention; the MS cross-REJECTs are assessment context only (G07 inadmissible).
- **FP-B3-5 (evidence-artifact)** — One mark-scheme quote preserves the pinned artifact's line wrap ("atoms/molecul es/electrons" — pdftotext wrapped "molecules" across lines; the byte-verification norm collapses newlines to single spaces, so the quote is verbatim against the pinned file). Layout-verified against the PDF with pdftotext -layout before pinning; the artifact is noted in the node's derivation_notes. No action needed — recorded so the artifact is explicit, not silent.
- **FN-B3-1 (false-negative-concern)** — Mark-scheme mining: 3 Paper-2 pins (IONIC/COVALENT/CFEC — FN-B2-1 closed). Coverage fact: PMT Unit 1 publishes NO metallic-bonding or electrolysis MS, so 1.52C-1.60C misconception mining has note evidence only (B3-H-11/H-12 record the refused candidates). Deeper electrolysis MS mining would need the pastpapers corpus or PMT Unit-2+ sets — a future evidence pass, not this batch.
- **FN-B3-2 (boundary)** — S1 is now FULLY covered (pilot + batches 1-3: 60 SPs, all mapped). The next batch (S3 Physical, per the §16 phase order) will mint the first cross-section boundary edges; the consolidated cross-slice boundary-concept ruling is still pending before phase 2 (S3) — the §16 authorization's standing condition.
- **FN-B3-3 (vocabulary-coverage)** — "Electrolyte" and "inert electrode" are taught inline without dedicated concept nodes (CON-ELECTROLYSIS carries "electrolyte" as an alias; the inert-electrode fact is in the 1.58C evidence) — deliberate non-minting at pilot granularity; recorded so the gap is explicit, not silent (the FN-B2-3 style).

## 6. Command-kind tags (guide §8) — batch-3 SPs

| SP | verb | guide class | demanded substance | operator |
|---|---|---|---|---|
| 4CH1-1.37 | understand | UNDERSTAND_RELATION | how ions are formed by electron loss or gain (the full-outer-shell motive; metals lose electrons to become cations, non-metals gain electrons to become anions) | ☐ |
| 4CH1-1.38 | know | KNOW_TERM | the charges of the listed ions (Group 1/2/3 metals, Group 5/6/7 non-metals, Ag+, Cu2+, Fe2+, Fe3+, Pb2+, Zn2+, H+, OH-, NH4+, CO3 2-, NO3-, SO4 2-) and the charge-deduction rule from outer electrons | ☐ |
| 4CH1-1.39 | write | PRODUCE_EQUATION | writing formulae for compounds formed between the listed ions (charge cancellation, direct comparison and swap-and-drop, brackets around compound ions) | ☐ |
| 4CH1-1.40 | draw | REPRESENT_DIAGRAM | dot-and-cross diagrams showing the formation of ionic compounds by electron transfer (Group 1/2/3 with Group 5/6/7 combinations, outer electrons only, bracketed charges) | ☐ |
| 4CH1-1.41 | understand | UNDERSTAND_RELATION | ionic bonding in terms of electrostatic attraction between oppositely charged ions acting in all directions | ☐ |
| 4CH1-1.42 | understand | UNDERSTAND_RELATION | why compounds with giant ionic lattices have high melting and boiling points (strong electrostatic forces between oppositely charged ions, large amounts of thermal energy, charge-magnitude effect) | ☐ |
| 4CH1-1.43 | know | KNOW_TERM | that ionic compounds do not conduct electricity when solid but do conduct when molten and in aqueous solution | ☐ |
| 4CH1-1.44 | know | KNOW_TERM | that a covalent bond is formed between atoms by the sharing of a pair of electrons | ☐ |
| 4CH1-1.45 | understand | UNDERSTAND_RELATION | covalent bonds in terms of electrostatic attraction between the shared pair of electrons and the nuclei of the atoms involved | ☐ |
| 4CH1-1.46 | understand | REPRESENT_DIAGRAM | using dot-and-cross diagrams to represent covalent bonds in diatomic molecules (H2, O2, N2, halogens, hydrogen halides), inorganic molecules (H2O, NH3, CO2) and organic molecules (CH4, C2H6, C2H4) | ☐ |
| 4CH1-1.47 | explain | UNDERSTAND_RELATION | why substances with simple molecular structures are gases or liquids, or solids with low melting and boiling points (weak intermolecular forces between molecules) | ☐ |
| 4CH1-1.48 | explain | UNDERSTAND_RELATION | why the melting and boiling points of simple molecular substances generally increase with increasing relative molecular mass (more electrons, stronger intermolecular forces) | ☐ |
| 4CH1-1.49 | explain | UNDERSTAND_RELATION | why substances with giant covalent structures are solids with high melting and boiling points (huge numbers of strong covalent bonds requiring lots of energy) | ☐ |
| 4CH1-1.50 | explain | UNDERSTAND_RELATION | how the structures of diamond, graphite and C60 fullerene influence their physical properties, including electrical conductivity and hardness | ☐ |
| 4CH1-1.51 | know | KNOW_TERM | that covalent compounds do not usually conduct electricity | ☐ |
| 4CH1-1.52C | know | REPRESENT_DIAGRAM | representing a metallic lattice by a 2-D diagram (regular pattern of positive metal ions with delocalised electrons) | ☐ |
| 4CH1-1.53C | understand | UNDERSTAND_RELATION | metallic bonding in terms of electrostatic attraction between positive metal ions and delocalised electrons | ☐ |
| 4CH1-1.54C | explain | UNDERSTAND_RELATION | typical physical properties of metals (electrical conductivity, malleability) explained by metallic bonding and the layer structure | ☐ |
| 4CH1-1.55C | understand | UNDERSTAND_RELATION | why covalent compounds do not conduct electricity (no freely moving charged particles in solid, liquid or gas) | ☐ |
| 4CH1-1.56C | understand | UNDERSTAND_RELATION | why ionic compounds conduct electricity only when molten or in aqueous solution (ions fixed in the solid lattice, free to move when molten or dissolved) | ☐ |
| 4CH1-1.57C | know | KNOW_TERM | that anion and cation are the terms for negative and positive ions respectively (and their migration to anode/cathode during electrolysis) | ☐ |
| 4CH1-1.58C | describe | DESCRIBE_EXPERIMENT | experiments to investigate electrolysis with inert electrodes, of molten compounds (including lead(II) bromide) and aqueous solutions (including sodium chloride, dilute sulfuric acid and copper(II) sulfate), with prediction of the products | ☐ |
| 4CH1-1.59C | write | PRODUCE_EQUATION | ionic half-equations representing the reactions at the electrodes during electrolysis and why these reactions are classified as oxidation or reduction | ☐ |
| 4CH1-1.60C | investigate | DESCRIBE_EXPERIMENT | the electrolysis-of-aqueous-solutions practical (electrolysis cell, collection and identification of the products at each electrode via gas tests) | ☐ |

## 7. Negative control (4CH1-4.15) — carried forward, still uncovered

Zero concepts, zero edges, zero coverage for 4.15 across the whole merged store (machine-tested: graph_check + negative test class 10/11 + the s16-authorization check D5). The batch adds nothing in S4 territory. Operator: acknowledge ☐

## 8. Batch-3 evidence set (pinned)

- 14 T-C10 HUMAN_VALIDATED-mapped notes (read in full at extraction): f. Ionic Bonding ×5 (Common Ions, Formation of ions, Formula of ionic compounds, Ionic bonding and lattices, Ionic bonding diagrams) + g. Covalent Bonding ×4 (Dot & Cross Diagrams, Forming covalent bonds, Giant covalent structures, Simple molecular structures) + h. Metallic Bonding ×1 (Metallic bonding) + i. Electrolysis ×4 (Electrolysis diagram, Electronic conductivity, Half equations, the 1.60C practical note).
- 3 pinned Paper-2 mark-scheme extractions (misconception-class evidence only; FN-B2-1 closed): IONIC_MS_P2.txt (4ccfc377514a) + COVALENT_MS_P2.txt (ed012522d306) + CFEC_MS_P2.txt (84d641c55208). Coverage fact: PMT Unit 1 publishes NO metallic-bonding or electrolysis MS, so 1.52C–1.60C misconception mining has note evidence only (B3-H-11/H-12 record the refused candidates — the gap is explicit, not silent).

## 9. After review (the batch gate)

1. Fill `scripts/c11_batch3_verdicts_template.yaml` (rename to `c11_batch3_verdicts.yaml`): per-row verdicts, the identity decisions, the held acknowledgment. (This batch has NO RR settlement — no REVIEW_REQUIRED edge was authored.)
2. The next session encodes your verdicts (fail-closed) and applies them: CONFIRM edges through the §18 pathway (`c11_diff_review.py approve` → one `c11_promote.py` invocation → gated G13 re-run); REJECT rows re-authored out like HELD-13; MERGE/SPLIT as §7 re-authoring (B3-ID-01..07 may re-scope the dual-attachment pairs).
3. This batch COMPLETES Section 1 coverage (pilot + batches 1–3 = all 60 S1 SPs). Per the §16 phase order, the next slice is S3 Physical (batch 4); the consolidated cross-slice boundary-concept ruling comes before phase 2 (S3).

---
Machine artifacts: `graph/concepts.yaml`, `graph/concept_edges.yaml`, `graph/spec_command_kinds.yaml` (generated, gated, merged store) · `C11_BATCH3_REVIEW.json` (this sheet's machine record) · `scripts/c11_batch3_verdicts_template.yaml` (the verdict template) · contract: `C11_ARCHITECTURE.md`
