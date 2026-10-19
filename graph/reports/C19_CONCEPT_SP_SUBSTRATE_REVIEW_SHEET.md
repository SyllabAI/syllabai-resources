# C19 — Concept→SP Attachment Substrate OPERATOR REVIEW SHEET (the promotion gate)

**Seed:** `5fd9d4c8ce619003` (sha256_16 of the sampled row set — deterministic regeneration) · **Rows:** 117 materialized attachments · **Sampled:** 41 (100% non-CORE + 100% check-fails + ≥20% CORE per section + multi-attachment coverage) · **Multi-attached SPs:** 23.

**Rule:** this sheet is the ONLY path from SUGGESTED to HUMAN_VALIDATED for the concept→SP attachment rows. Per-class rollup: any confirmed-precision < 90% on the sampled rows → rework that class before promotion. **Anti-forgery reminder:** the tool cannot emit HUMAN_VALIDATED rows (G5/G19); only your verdicts here can.

**Method (recorded before filling):** *mechanical* — the emitted M1–M5 ledger is re-displayed per row and re-proved by re-running the tool; *semantic* — the reviewer judges whether the CONCEPT (title, aliases, definition scope) genuinely subsumes the SP's demand, using the quote(s) against the SP's official wording and the note context. The note-level mapping is already operator-validated upstream (T-C10); the new judgment is concept-level topical fidelity.

## Part A — attachment-row review

### 1. `4CH1-CON-EXP-FORMULA-DEDUCTION` PART_OF `4CH1-1.31` — mapping_id `0b548e899a089a27`
- Concept: Experimental formula deduction (mass-difference method)  (aliases: deducing formulae by experiment, formula from mass measurements) · node status: SUGGESTED
- SP official wording (R2): “understand how the formulae of simple compounds can be obtained experimentally, including metal oxides, water and salts containing water of crystallisation”
- SP applicability: papers 1C, 2C · shared with Double Award
- Role: CORE · confidence: high · section: S1 · checks: M1 True · M3 True · M4 True · M5 True
- Evidence [NOTE] `Chemistry IGCSE Revision Notes/1. Principles of Chemistry/e. Chemical Formulae, Equations, Calculations/Simple compound formulae - IGCSE Chemistry Revision Notes.md`: “The principle is to use mass measurements before and after a reaction and then convert masses into moles”
- Upstream: T-C10 HUMAN_VALIDATED 4CH1-1.31 @ Simple compound formulae + @ Investigating metal oxide formulas; 4CH1-1.36 @ Investigating metal oxide formulas (2026-09-11)
- Verdict: [ ] CONFIRM — the concept genuinely subsumes this SP's demand   [ ] REJECT — wrong concept/SP pairing   [ ] HOLD — needs better evidence (state what)
- Reviewer note:

### 2. `4CH1-CON-AVOGADRO-LAW` PART_OF `4CH1-1.35C` — mapping_id `0d4343056f261b75`
- Concept: Avogadro's Law  (aliases: ) · node status: SUGGESTED
- SP official wording (R2): “understand how to carry out calculations involving gas volumes and the molar volume of a gas (24 dm 3 and 24 000 cm 3 at room temperature and pressure (rtp))”
- SP applicability: papers 2C
- Role: ENRICHMENT · confidence: high · section: S1 · checks: M1 True · M3 True · M4 True · M5 True
- Evidence [NOTE] `Chemistry IGCSE Revision Notes/1. Principles of Chemistry/e. Chemical Formulae, Equations, Calculations/Calculate Gas Volumes - IGCSE Chemistry Revision Notes.md`: “Avogadro’s Law states that at the same conditions of temperature and pressure, equal amounts of gases occupy the same volume of space”
- Upstream: T-C10 HUMAN_VALIDATED 4CH1-1.35C @ Calculate Gas Volumes (2026-09-11)
- Verdict: [ ] CONFIRM — the concept genuinely subsumes this SP's demand   [ ] REJECT — wrong concept/SP pairing   [ ] HOLD — needs better evidence (state what)
- Reviewer note:

### 3. `4CH1-CON-METALLIC-BOND` PART_OF `4CH1-1.53C` — mapping_id `1bc93f10196ebe54`
- Concept: Metallic bonding (positive metal ions and delocalised electrons; the 2-D metallic lattice representation)  (aliases: metallic bond, metallic bonding, delocalised electrons, sea of electrons) · node status: SUGGESTED
- SP official wording (R2): “understand metallic bonding in terms of electrostatic attractions”
- SP applicability: papers 2C
- Role: CORE · confidence: high · section: S1 · checks: M1 True · M3 True · M4 True · M5 True · spec_in_r2 True
- Evidence [NOTE] `Chemistry IGCSE Revision Notes/1. Principles of Chemistry/h. Metallic Bonding/Metallic bonding - IGCSE Chemistry Revision Notes.md`: “Within the metal lattice, the atoms lose their outer electrons and become positively charged metal ions”
- Evidence [NOTE] `Chemistry IGCSE Revision Notes/1. Principles of Chemistry/h. Metallic Bonding/Metallic bonding - IGCSE Chemistry Revision Notes.md`: “The metallic bond is the strong force of attraction between the positive metal ions and the delocalised electrons”
- Evidence [SPEC] `graph/specification_points.yaml`: “metallic bonding in terms of electrostatic attractions”
- Upstream: T-C10 HUMAN_VALIDATED 4CH1-1.52C @ Metallic Bonding (2026-09-11); T-C10 HUMAN_VALIDATED 4CH1-1.53C @ Metallic Bonding (2026-09-11); specs 4CH1-1.52C + 4CH1-1.53C official wording
- Verdict: [ ] CONFIRM — the concept genuinely subsumes this SP's demand   [ ] REJECT — wrong concept/SP pairing   [ ] HOLD — needs better evidence (state what)
- Reviewer note:

### 4. `4CH1-CON-IONIC-CONDUCTION` PART_OF `4CH1-1.43` — mapping_id `226ed494ec1e237c`
- Concept: Ionic conduction (solid insulator; molten and aqueous conductor via mobile ions)  (aliases: conductivity of ionic compounds, ionic conductivity) · node status: SUGGESTED
- SP official wording (R2): “know that ionic compounds do not conduct electricity when solid, but do conduct electricity when molten and in aqueous solution”
- SP applicability: papers 1C, 2C · shared with Double Award
- Role: CORE · confidence: high · section: S1 · checks: M1 True · M3 True · M4 True · M5 True · spec_in_r2 True
- Evidence [NOTE] `Chemistry IGCSE Revision Notes/1. Principles of Chemistry/f. Ionic Bonding/Ionic bonding and lattices - IGCSE Chemistry Revision Notes.md`: “Ionic compounds are poor conductors in the solid state”
- Evidence [NOTE] `Chemistry IGCSE Revision Notes/1. Principles of Chemistry/f. Ionic Bonding/Ionic bonding and lattices - IGCSE Chemistry Revision Notes.md`: “Ionic compounds are good conductors of electricity in the molten state or in solution”
- Evidence [SPEC] `graph/specification_points.yaml`: “ionic compounds do not conduct electricity when solid”
- Upstream: T-C10 HUMAN_VALIDATED 4CH1-1.43 @ Ionic Bonding and Lattices (2026-09-11); T-C10 HUMAN_VALIDATED 4CH1-1.56C @ Electronic Conductivity (2026-09-11); specs 4CH1-1.43 + 4CH1-1.56C official wording
- Verdict: [ ] CONFIRM — the concept genuinely subsumes this SP's demand   [ ] REJECT — wrong concept/SP pairing   [ ] HOLD — needs better evidence (state what)
- Reviewer note:

### 5. `4CH1-CON-MASS-NUMBER` PART_OF `4CH1-1.16` — mapping_id `2e375102f036b717`
- Concept: Mass number  (aliases: mass number) · node status: SUGGESTED
- SP official wording (R2): “ know what is meant by the terms atomic number, mass number, isotopes and relative atomic mass (Ar)”
- SP applicability: papers 1C, 2C · shared with Double Award
- Role: CORE · confidence: high · section: S1 · checks: M1 True · M3 True · M4 True · M5 True · spec_in_r2 True
- Evidence [NOTE] `Chemistry IGCSE Revision Notes/1. Principles of Chemistry/c. Atomic Structure/Atoms Definitions & Structure  Edexcel IGCSE Chemistry Revision Notes 2017.md`: “The number of protons and neutrons in the nucleus of an atom”
- Evidence [NOTE] `Chemistry IGCSE Revision Notes/1. Principles of Chemistry/c. Atomic Structure/Atoms Definitions & Structure  Edexcel IGCSE Chemistry Revision Notes 2017.md`: “The mass number of lithium is 7, so it has 7 - 3 = 4 neutrons”
- Evidence [NOTE] `Chemistry IGCSE Revision Notes/1. Principles of Chemistry/c. Atomic Structure/Atoms Definitions & Structure  Edexcel IGCSE Chemistry Revision Notes 2017.md`: “Think MASS = MASSIVE, as the mass number is always the bigger of the two numbers”
- Evidence [SPEC] `graph/specification_points.yaml`: “atomic number, mass number, isotopes”
- Upstream: T-C10 HUMAN_VALIDATED 4CH1-1.16 @ Atoms: Definitions & Structure (2026-09-11); spec 4CH1-1.16 official wording
- Verdict: [ ] CONFIRM — the concept genuinely subsumes this SP's demand   [ ] REJECT — wrong concept/SP pairing   [ ] HOLD — needs better evidence (state what)
- Reviewer note:

### 6. `4CH1-CON-DILUTION` PART_OF `4CH1-1.3` — mapping_id `374c5711b75c5242`
- Concept: Dilution of coloured solutions  (aliases: dilution, diluted) · node status: SUGGESTED
- SP official wording (R2): “understand how the results of experiments involving the dilution of coloured solutions and diffusion of gases can be explained”
- SP applicability: papers 1C, 2C · shared with Double Award
- Role: CORE · confidence: high · section: S1 · checks: M1 True · M3 True · M4 True · M5 True · spec_in_r2 True
- Evidence [NOTE] `Chemistry IGCSE Revision Notes/1. Principles of Chemistry/a. States of Matter/Diffusion - IGCSE Chemistry Revision Notes.md`: “Dilution is the process of adding more solvent (usually water) to a solution”
- Evidence [NOTE] `Chemistry IGCSE Revision Notes/1. Principles of Chemistry/a. States of Matter/Diffusion - IGCSE Chemistry Revision Notes.md`: “The solute particles become more spread out but are still present in the solution”
- Evidence [SPEC] `graph/specification_points.yaml`: “dilution of coloured solutions”
- Upstream: T-C10 HUMAN_VALIDATED 4CH1-1.3 @ Diffusion (2026-09-11); spec 4CH1-1.3 official wording
- Verdict: [ ] CONFIRM — the concept genuinely subsumes this SP's demand   [ ] REJECT — wrong concept/SP pairing   [ ] HOLD — needs better evidence (state what)
- Reviewer note:

### 7. `4CH1-CON-AVOGADRO-CONST` PART_OF `4CH1-1.27` — mapping_id `3f8e517e7aff502b`
- Concept: Avogadro constant  (aliases: Avogadro's constant) · node status: SUGGESTED
- SP official wording (R2): “know that the mole (mol) is the unit for the amount of a substance”
- SP applicability: papers 1C, 2C · shared with Double Award
- Role: ENRICHMENT · confidence: high · section: S1 · checks: M1 True · M3 True · M4 True · M5 True
- Evidence [NOTE] `Chemistry IGCSE Revision Notes/1. Principles of Chemistry/e. Chemical Formulae, Equations, Calculations/Calculating moles and mass - IGCSE Chemistry Revision Notes.md`: “The number of atoms, molecules or ions in a mole (1 mol) of a given substance is the Avogadro constant.”
- Upstream: T-C10 HUMAN_VALIDATED 4CH1-1.27 @ Calculating moles and mass (2026-09-11)
- Verdict: [ ] CONFIRM — the concept genuinely subsumes this SP's demand   [ ] REJECT — wrong concept/SP pairing   [ ] HOLD — needs better evidence (state what)
- Reviewer note:

### 8. `4CH1-CON-STATES-THREE` PART_OF `4CH1-1.1` — mapping_id `457f73c1391a16ae`
- Concept: The three states of matter (solid, liquid, gas)  (aliases: states of matter, three states of matter) · node status: SUGGESTED
- SP official wording (R2): “understand the three states of matter in terms of the arrangement, movement and energy of the particles”
- SP applicability: papers 1C, 2C · shared with Double Award
- Role: CORE · confidence: high · section: S1 · checks: M1 True · M3 True · M4 True · M5 True · spec_in_r2 True
- Evidence [NOTE] `Chemistry IGCSE Revision Notes/1. Principles of Chemistry/a. States of Matter/Changing states of matter - IGCSE Chemistry Revision Notes.md`: “The three states of matter are solids, liquids and gases”
- Evidence [SPEC] `graph/specification_points.yaml`: “understand the three states of matter”
- Upstream: T-C10 HUMAN_VALIDATED 4CH1-1.1 @ Changing states of matter (2026-09-11); spec 4CH1-1.1 official wording
- Verdict: [ ] CONFIRM — the concept genuinely subsumes this SP's demand   [ ] REJECT — wrong concept/SP pairing   [ ] HOLD — needs better evidence (state what)
- Reviewer note:

### 9. `4CH1-CON-MOLE-MASS-CONV` PART_OF `4CH1-1.28` — mapping_id `45cf6f1e8ad614bd`
- Concept: Mole-mass conversion  (aliases: converting between moles and grams, moles and mass calculations) · node status: SUGGESTED
- SP official wording (R2): “ understand how to carry out calculations involving amount of substance, relative atomic mass (Ar) and relative formula mass (Mr)”
- SP applicability: papers 1C, 2C · shared with Double Award
- Role: CORE · confidence: high · section: S1 · checks: M1 True · M3 True · M4 True · M5 True
- Evidence [NOTE] `Chemistry IGCSE Revision Notes/1. Principles of Chemistry/e. Chemical Formulae, Equations, Calculations/Calculating moles and mass - IGCSE Chemistry Revision Notes.md`: “Therefore we have to be able to convert between moles and grams”
- Evidence [NOTE] `Chemistry IGCSE Revision Notes/1. Principles of Chemistry/e. Chemical Formulae, Equations, Calculations/Reacting mass calculations - IGCSE Chemistry Revision Notes.md`: “Once the moles have been determined they can then be converted into grams using the relative atomic or relative formula masses”
- Upstream: T-C10 HUMAN_VALIDATED 4CH1-1.28 @ Calculating moles and mass + @ Reacting mass calculations (2026-09-11)
- Verdict: [ ] CONFIRM — the concept genuinely subsumes this SP's demand   [ ] REJECT — wrong concept/SP pairing   [ ] HOLD — needs better evidence (state what)
- Reviewer note:

### 10. `4CH1-CON-METALLOID` PART_OF `4CH1-1.21` — mapping_id `46da34b8122712d9`
- Concept: Semi-metals (metalloids) — elements bordering the metal/non-metal divide  (aliases: semi-metal, metalloid) · node status: SUGGESTED
- SP official wording (R2): “identify an element as a metal or a non-metal according to its position in the Periodic Table”
- SP applicability: papers 1C, 2C · shared with Double Award
- Role: ENRICHMENT · confidence: high · section: S1 · checks: M1 True · M3 True · M4 True · M5 True
- Evidence [NOTE] `Chemistry IGCSE Revision Notes/1. Principles of Chemistry/d. The Periodic Table/Metals & non-metals in the Periodic Table - IGCSE Chemistry.md`: “Elements which border the line are hard to classify as they have characteristics of both sides, so the term semi-metal or metalloid is used”
- Upstream: T-C10 HUMAN_VALIDATED 4CH1-1.21 @ Metals & non-metals in the Periodic Table (2026-09-11)
- Verdict: [ ] CONFIRM — the concept genuinely subsumes this SP's demand   [ ] REJECT — wrong concept/SP pairing   [ ] HOLD — needs better evidence (state what)
- Reviewer note:

### 11. `4CH1-CON-YIELD-FACTORS` PART_OF `4CH1-1.30` — mapping_id `4aeb1144e29ebeb8`
- Concept: Factors reducing yield  (aliases: reasons for less than 100 percent yield, yield losses) · node status: SUGGESTED
- SP official wording (R2): “calculate percentage yield”
- SP applicability: papers 1C, 2C · shared with Double Award
- Role: ENRICHMENT · confidence: high · section: S1 · checks: M1 True · M3 True · M4 True · M5 True
- Evidence [NOTE] `Chemistry IGCSE Revision Notes/1. Principles of Chemistry/e. Chemical Formulae, Equations, Calculations/Calculate percentage yield - IGCSE Chemistry Revision Notes.md`: “In practice, you never get 100% yield in a chemical process for several reasons”
- Upstream: T-C10 HUMAN_VALIDATED 4CH1-1.30 @ Calculate percentage yield (2026-09-11)
- Verdict: [ ] CONFIRM — the concept genuinely subsumes this SP's demand   [ ] REJECT — wrong concept/SP pairing   [ ] HOLD — needs better evidence (state what)
- Reviewer note:

### 12. `4CH1-CON-MIXTURE` PART_OF `4CH1-1.8` — mapping_id `5f0e6b93dde3ccbc`
- Concept: Mixture  (aliases: mixtures) · node status: SUGGESTED
- SP official wording (R2): “understand how to classify a substance as an element, compound or mixture”
- SP applicability: papers 1C, 2C · shared with Double Award
- Role: CORE · confidence: high · section: S1 · checks: M1 True · M3 True · M4 True · M5 True · spec_in_r2 True
- Evidence [NOTE] `Chemistry IGCSE Revision Notes/1. Principles of Chemistry/b. Elements, Compounds and Mixtures/Element, Compound or Mixture  Edexcel IGCSE Chemistry Revision Notes 2017.md`: “A combination of two or more substances (elements and/or compounds) that are not chemically combined”
- Evidence [SPEC] `graph/specification_points.yaml`: “or mixture”
- Upstream: T-C10 HUMAN_VALIDATED 4CH1-1.8 @ Element, Compound or Mixture (2026-09-11); spec 4CH1-1.8 official wording
- Verdict: [ ] CONFIRM — the concept genuinely subsumes this SP's demand   [ ] REJECT — wrong concept/SP pairing   [ ] HOLD — needs better evidence (state what)
- Reviewer note:

### 13. `4CH1-CON-ELECTROLYSIS` PART_OF `4CH1-1.58C` — mapping_id `5f27be59ad021821`
- Concept: Electrolysis (decomposition by direct current: molten binary compounds and their element products, using inert electrodes)  (aliases: electrolysis, electrolyte, electrolysis of molten compounds) · node status: SUGGESTED
- SP official wording (R2): “describe experiments to investigate electrolysis, using inert electrodes, of molten compounds (including lead(II) bromide) and aqueous solutions (including sodium chloride, dilute sulfuric acid and copper(II) sulfate) and to predict the products”
- SP applicability: papers 2C
- Role: CORE · confidence: high · section: S1 · checks: M1 True · M3 True · M4 True · M5 True · spec_in_r2 True
- Evidence [NOTE] `Chemistry IGCSE Revision Notes/1. Principles of Chemistry/i. Electrolysis/Electrolysis diagram - IGCSE Chemistry Revision Notes.md`: “These compounds undergo electrolysis and always produce their corresponding element”
- Evidence [NOTE] `Chemistry IGCSE Revision Notes/1. Principles of Chemistry/i. Electrolysis/Electrolysis diagram - IGCSE Chemistry Revision Notes.md`: “The positive ion will migrate towards the cathode and the negative ion will migrate towards the anode”
- Evidence [NOTE] `Chemistry IGCSE Revision Notes/1. Principles of Chemistry/i. Electrolysis/Electrolysis diagram - IGCSE Chemistry Revision Notes.md`: “Add lead(II) bromide into a crucible and heat so it will turn molten, allowing ions to be free to move and conduct an electric charge”
- Evidence [SPEC] `graph/specification_points.yaml`: “describe experiments to investigate electrolysis, using inert electrodes”
- Upstream: T-C10 HUMAN_VALIDATED 4CH1-1.58C @ Electrolysis Diagram (2026-09-11); spec 4CH1-1.58C official wording
- Verdict: [ ] CONFIRM — the concept genuinely subsumes this SP's demand   [ ] REJECT — wrong concept/SP pairing   [ ] HOLD — needs better evidence (state what)
- Reviewer note:

### 14. `4CH1-CON-STATE-PARTICLE-MODEL` PART_OF `4CH1-1.3` — mapping_id `6b63cb7ee8206660`
- Concept: Particle arrangement, movement and energy in the three states  (aliases: kinetic theory of matter) · node status: SUGGESTED
- SP official wording (R2): “understand how the results of experiments involving the dilution of coloured solutions and diffusion of gases can be explained”
- SP applicability: papers 1C, 2C · shared with Double Award
- Role: SUPPORTING · confidence: high · section: S1 · checks: M1 True · M3 True · M4 True · M5 True
- Evidence [NOTE] `Chemistry IGCSE Revision Notes/1. Principles of Chemistry/a. States of Matter/Diffusion - IGCSE Chemistry Revision Notes.md`: “Diffusion and dilution experiments support a theory that all matter (solids, liquids and gases) is made up of tiny, moving particles”
- Upstream: T-C10 HUMAN_VALIDATED 4CH1-1.1 @ Changing states of matter + 4CH1-1.3 @ Diffusion (2026-09-11); spec 4CH1-1.1 official wording
- Verdict: [ ] CONFIRM — the concept genuinely subsumes this SP's demand   [ ] REJECT — wrong concept/SP pairing   [ ] HOLD — needs better evidence (state what)
- Reviewer note:

### 15. `4CH1-CON-REACTING-MASS` PART_OF `4CH1-1.29` — mapping_id `6c975732a8dd5cc7`
- Concept: Reacting mass calculation  (aliases: calculating reacting masses, mass calculations from equations) · node status: SUGGESTED
- SP official wording (R2): “calculate reacting masses using experimental data and chemical equations”
- SP applicability: papers 1C, 2C · shared with Double Award
- Role: CORE · confidence: high · section: S1 · checks: M1 True · M3 True · M4 True · M5 True · spec_in_r2 True
- Evidence [SPEC] `graph/specification_points.yaml`: “calculate reacting masses using experimental data and chemical equations”
- Evidence [NOTE] `Chemistry IGCSE Revision Notes/1. Principles of Chemistry/e. Chemical Formulae, Equations, Calculations/Reacting mass calculations - IGCSE Chemistry Revision Notes.md`: “Information from the question is used to find the amount in moles of the substances being considered”
- Upstream: T-C10 HUMAN_VALIDATED 4CH1-1.29 @ Reacting mass calculations (2026-09-11); spec 4CH1-1.29 official wording
- Verdict: [ ] CONFIRM — the concept genuinely subsumes this SP's demand   [ ] REJECT — wrong concept/SP pairing   [ ] HOLD — needs better evidence (state what)
- Reviewer note:

### 16. `4CH1-CON-DOT-CROSS-IONIC` PART_OF `4CH1-1.40` — mapping_id `778c100988b3e127`
- Concept: Dot-and-cross diagrams for ionic compounds (electron transfer)  (aliases: dot and cross diagram, dot-and-cross diagrams, ionic bonding diagrams) · node status: SUGGESTED
- SP official wording (R2): “draw dot-and-cross diagrams to show the formation of ionic compounds by electron transfer, limited to combinations of elements from Groups 1, 2, 3 and 5, 6, 7 only outer electrons need be shown”
- SP applicability: papers 1C, 2C · shared with Double Award
- Role: CORE · confidence: high · section: S1 · checks: M1 True · M3 True · M4 True · M5 True · spec_in_r2 True
- Evidence [NOTE] `Chemistry IGCSE Revision Notes/1. Principles of Chemistry/f. Ionic Bonding/Ionic bonding diagrams - IGCSE Chemistry Revision Notes.md`: “Ionic bonds can be represented diagrammatically using dot-and-cross diagrams”
- Evidence [NOTE] `Chemistry IGCSE Revision Notes/1. Principles of Chemistry/f. Ionic Bonding/Ionic bonding diagrams - IGCSE Chemistry Revision Notes.md`: “One electron will be transferred from the outer shell of the sodium atom to the outer shell of the chlorine atom”
- Evidence [NOTE] `Chemistry IGCSE Revision Notes/1. Principles of Chemistry/f. Ionic Bonding/Ionic bonding diagrams - IGCSE Chemistry Revision Notes.md`: “For exam purposes you need only show the outer electrons in dot & cross diagrams”
- Evidence [SPEC] `graph/specification_points.yaml`: “dot-and-cross diagrams to show the formation of ionic compounds by electron transfer”
- Upstream: T-C10 HUMAN_VALIDATED 4CH1-1.40 @ Ionic Bonding Diagrams (2026-09-11); spec 4CH1-1.40 official wording
- Verdict: [ ] CONFIRM — the concept genuinely subsumes this SP's demand   [ ] REJECT — wrong concept/SP pairing   [ ] HOLD — needs better evidence (state what)
- Reviewer note:

### 17. `4CH1-CON-ELECTRODE-HALF-EQUATIONS` PART_OF `4CH1-1.59C` — mapping_id `7f81df7683fc74ca`
- Concept: Ionic half-equations for the electrode reactions during electrolysis  (aliases: half equation, half equations, electrode reactions) · node status: SUGGESTED
- SP official wording (R2): “write ionic half-equations representing the reactions at the electrodes during electrolysis and understand why these reactions are classified as oxidation or reduction”
- SP applicability: papers 2C
- Role: CORE · confidence: high · section: S1 · checks: M1 True · M3 True · M4 True · M5 True · spec_in_r2 True
- Evidence [NOTE] `Chemistry IGCSE Revision Notes/1. Principles of Chemistry/i. Electrolysis/Half equations - IGCSE Chemistry Revision Notes.md`: “This can be illustrated using half equations which describe the movement of electrons at each electrode”
- Evidence [NOTE] `Chemistry IGCSE Revision Notes/1. Principles of Chemistry/i. Electrolysis/Half equations - IGCSE Chemistry Revision Notes.md`: “At the anode, negatively charged ions lose electrons and are thus oxidised”
- Evidence [NOTE] `Chemistry IGCSE Revision Notes/1. Principles of Chemistry/i. Electrolysis/Half equations - IGCSE Chemistry Revision Notes.md`: “In electrode half equations the charges on each side of the equation should always balance”
- Evidence [SPEC] `graph/specification_points.yaml`: “write ionic half-equations representing the reactions at the electrodes during electrolysis”
- Upstream: T-C10 HUMAN_VALIDATED 4CH1-1.59C @ Half Equations (2026-09-11); spec 4CH1-1.59C official wording
- Verdict: [ ] CONFIRM — the concept genuinely subsumes this SP's demand   [ ] REJECT — wrong concept/SP pairing   [ ] HOLD — needs better evidence (state what)
- Reviewer note:

### 18. `4CH1-CON-REACTION-PROFILE` PART_OF `4CH1-3.14C` — mapping_id `7f8e2c4af06fbdf1`
- Concept: Reaction profile diagrams (showing ΔH and activation energy)  (aliases: reaction profile, reaction profiles, reaction profile diagram, energy profile) · node status: SUGGESTED
- SP official wording (R2): “draw and explain reaction profile diagrams showing Δ H and activation energy”
- SP applicability: papers 2C
- Role: CORE · confidence: high · section: S3 · checks: M1 True · M3 True · M4 True · M5 True · spec_in_r2 True
- Evidence [NOTE] `Chemistry IGCSE Revision Notes/3. Physical Chemistry/b. Rates of Reaction/What is activation energy- IGCSE Revision Notes.md`: “Reaction profiles are similar to energy level diagrams seen in a previous topic”
- Evidence [NOTE] `Chemistry IGCSE Revision Notes/3. Physical Chemistry/b. Rates of Reaction/What is activation energy- IGCSE Revision Notes.md`: “The initial increase in energy, from the reactants to the peak of the curve, represents the activation energy”
- Evidence [SPEC] `graph/specification_points.yaml`: “draw and explain reaction profile diagrams showing”
- Upstream: T-C10 HUMAN_VALIDATED 4CH1-3.14C @ What is Activation Energy (2026-09-11); spec 4CH1-3.14C official wording
- Verdict: [ ] CONFIRM — the concept genuinely subsumes this SP's demand   [ ] REJECT — wrong concept/SP pairing   [ ] HOLD — needs better evidence (state what)
- Reviewer note:

### 19. `4CH1-CON-ISOTOPES` PART_OF `4CH1-1.16` — mapping_id `809939b0b9b6bf59`
- Concept: Isotopes and relative atomic mass from isotopic abundances  (aliases: isotope, isotopes) · node status: SUGGESTED
- SP official wording (R2): “ know what is meant by the terms atomic number, mass number, isotopes and relative atomic mass (Ar)”
- SP applicability: papers 1C, 2C · shared with Double Award
- Role: CORE · confidence: high · section: S1 · checks: M1 True · M3 True · M4 True · M5 True · spec_in_r2 True
- Evidence [NOTE] `Chemistry IGCSE Revision Notes/1. Principles of Chemistry/c. Atomic Structure/Atoms Definitions & Structure  Edexcel IGCSE Chemistry Revision Notes 2017.md`: “Atoms of the same element which have the same number of protons but a different number of neutrons”
- Evidence [SPEC] `graph/specification_points.yaml`: “atomic number, mass number, isotopes”
- Upstream: T-C10 HUMAN_VALIDATED 4CH1-1.16/1.17 @ Atoms: Definitions & Structure + Relative atomic mass (2026-09-11); spec 4CH1-1.16/1.17 official wording
- Verdict: [ ] CONFIRM — the concept genuinely subsumes this SP's demand   [ ] REJECT — wrong concept/SP pairing   [ ] HOLD — needs better evidence (state what)
- Reviewer note:

### 20. `4CH1-CON-THEOR-YIELD` PART_OF `4CH1-1.30` — mapping_id `8b5d4f6d6ce1bfb1`
- Concept: Theoretical yield  (aliases: ) · node status: SUGGESTED
- SP official wording (R2): “calculate percentage yield”
- SP applicability: papers 1C, 2C · shared with Double Award
- Role: CORE · confidence: high · section: S1 · checks: M1 True · M3 True · M4 True · M5 True
- Evidence [NOTE] `Chemistry IGCSE Revision Notes/1. Principles of Chemistry/e. Chemical Formulae, Equations, Calculations/Calculate percentage yield - IGCSE Chemistry Revision Notes.md`: “The theoretical yield is the amount of product that would be obtained under perfect practical and chemical conditions”
- Upstream: T-C10 HUMAN_VALIDATED 4CH1-1.30 @ Calculate percentage yield (2026-09-11)
- Verdict: [ ] CONFIRM — the concept genuinely subsumes this SP's demand   [ ] REJECT — wrong concept/SP pairing   [ ] HOLD — needs better evidence (state what)
- Reviewer note:

### 21. `4CH1-CON-EVAPORATION-BOILING` PART_OF `4CH1-1.2` — mapping_id `8bf7660c71661003`
- Concept: Evaporation and its distinction from boiling  (aliases: evaporation, boiling, evaporating) · node status: SUGGESTED
- SP official wording (R2): “understand the interconversions between the three states of matter in terms of:”
- SP applicability: papers 1C, 2C · shared with Double Award
- Role: ENRICHMENT · confidence: high · section: S1 · checks: M1 True · M3 True · M4 True · M5 True
- Evidence [NOTE] `Chemistry IGCSE Revision Notes/1. Principles of Chemistry/a. States of Matter/Changing states of matter - IGCSE Chemistry Revision Notes.md`: “Evaporation occurs over a range of temperatures”
- Evidence [NOTE] `Chemistry IGCSE Revision Notes/1. Principles of Chemistry/a. States of Matter/Changing states of matter - IGCSE Chemistry Revision Notes.md`: “It can happen at temperatures below the boiling point of the liquid”
- Upstream: T-C10 HUMAN_VALIDATED 4CH1-1.2 @ Changing states of matter (2026-09-11)
- Verdict: [ ] CONFIRM — the concept genuinely subsumes this SP's demand   [ ] REJECT — wrong concept/SP pairing   [ ] HOLD — needs better evidence (state what)
- Reviewer note:

### 22. `4CH1-CON-SATURATED-SOLUTION` PART_OF `4CH1-1.10` — mapping_id `8d45c1b98aaa2cf9`
- Concept: Saturated solution  (aliases: saturated, saturation) · node status: SUGGESTED
- SP official wording (R2): “describe these experimental techniques for the separation of mixtures:”
- SP applicability: papers 1C, 2C · shared with Double Award
- Role: SUPPORTING · confidence: high · section: S1 · checks: M1 True · M3 True · M4 True · M5 True
- Evidence [NOTE] `Chemistry IGCSE Revision Notes/1. Principles of Chemistry/b. Elements, Compounds and Mixtures/Separation techniques - IGCSE Chemistry Revision Notes.md`: “The solution is heated, allowing the solvent to evaporate, leaving a saturated solution behind”
- Upstream: T-C10 HUMAN_VALIDATED 4CH1-1.4 @ Solutions + 4CH1-1.10 @ Separation techniques (2026-09-11); spec 4CH1-1.4 official wording
- Verdict: [ ] CONFIRM — the concept genuinely subsumes this SP's demand   [ ] REJECT — wrong concept/SP pairing   [ ] HOLD — needs better evidence (state what)
- Reviewer note:

### 23. `4CH1-CON-NOBLE-GAS-INERTNESS` PART_OF `4CH1-1.24` — mapping_id `8dae8d3250c528f6`
- Concept: Why the noble gases (Group 0) do not readily react  (aliases: noble gases, Group 0, inert gases) · node status: SUGGESTED
- SP official wording (R2): “understand why the noble gases (Group 0) do not readily react”
- SP applicability: papers 1C, 2C · shared with Double Award
- Role: CORE · confidence: high · section: S1 · checks: M1 True · M3 True · M4 True · M5 True · spec_in_r2 True
- Evidence [NOTE] `Chemistry IGCSE Revision Notes/1. Principles of Chemistry/d. The Periodic Table/Electronic Configuration & Reactivity  Edexcel IGCSE Chemistry Revision Notes 2017.md`: “Group 0 elements do not do this because they have full outer shells of electrons”
- Evidence [NOTE] `Chemistry IGCSE Revision Notes/1. Principles of Chemistry/d. The Periodic Table/Electronic Configuration & Reactivity  Edexcel IGCSE Chemistry Revision Notes 2017.md`: “They are therefore unreactive (inert) and do not form molecules easily”
- Evidence [NOTE] `Chemistry IGCSE Revision Notes/1. Principles of Chemistry/d. The Periodic Table/Electronic Configuration & Reactivity  Edexcel IGCSE Chemistry Revision Notes 2017.md`: “Most noble gases have 8 electrons in their outer shell, except helium which has 2”
- Evidence [SPEC] `graph/specification_points.yaml`: “the noble gases”
- Upstream: T-C10 HUMAN_VALIDATED 4CH1-1.24 @ Electronic Configuration & Reactivity (2026-09-11); spec 4CH1-1.24 official wording
- Verdict: [ ] CONFIRM — the concept genuinely subsumes this SP's demand   [ ] REJECT — wrong concept/SP pairing   [ ] HOLD — needs better evidence (state what)
- Reviewer note:

### 24. `4CH1-CON-MOLECULE` PART_OF `4CH1-1.14` — mapping_id `98bd3c9bb76696db`
- Concept: Molecule  (aliases: molecule, molecules) · node status: SUGGESTED
- SP official wording (R2): “know what is meant by the terms atom and molecule”
- SP applicability: papers 1C, 2C · shared with Double Award
- Role: CORE · confidence: high · section: S1 · checks: M1 True · M3 True · M4 True · M5 True · spec_in_r2 True
- Evidence [NOTE] `Chemistry IGCSE Revision Notes/1. Principles of Chemistry/c. Atomic Structure/Atoms Definitions & Structure  Edexcel IGCSE Chemistry Revision Notes 2017.md`: “A group of two or more atoms chemically combined to form an identifiable unit which retains the properties and composition of the substance”
- Evidence [SPEC] `graph/specification_points.yaml`: “the terms atom and molecule”
- Upstream: T-C10 HUMAN_VALIDATED 4CH1-1.14 @ Atoms: Definitions & Structure (2026-09-11); spec 4CH1-1.14 official wording
- Verdict: [ ] CONFIRM — the concept genuinely subsumes this SP's demand   [ ] REJECT — wrong concept/SP pairing   [ ] HOLD — needs better evidence (state what)
- Reviewer note:

### 25. `4CH1-CON-EMPIRICAL-FORMULA` PART_OF `4CH1-1.33` — mapping_id `a0f6c86c63ab100c`
- Concept: Empirical formula  (aliases: simplest whole number ratio formula) · node status: SUGGESTED
- SP official wording (R2): “calculate empirical and molecular formulae from experimental data”
- SP applicability: papers 1C, 2C · shared with Double Award
- Role: CORE · confidence: high · section: S1 · checks: M1 True · M3 True · M4 True · M5 True · spec_in_r2 True
- Evidence [SPEC] `graph/specification_points.yaml`: “calculate empirical and molecular formulae from experimental data”
- Upstream: T-C10 HUMAN_VALIDATED 4CH1-1.32 + 4CH1-1.33 @ Empirical & Molecular Formulae (2026-09-11); spec wordings
- Verdict: [ ] CONFIRM — the concept genuinely subsumes this SP's demand   [ ] REJECT — wrong concept/SP pairing   [ ] HOLD — needs better evidence (state what)
- Reviewer note:

### 26. `4CH1-CON-MOLECULAR-FORMULA` PART_OF `4CH1-1.32` — mapping_id `aa9cfece0996f6ef`
- Concept: Molecular formula  (aliases: ) · node status: SUGGESTED
- SP official wording (R2): “know what is meant by the terms empirical formula and molecular formula”
- SP applicability: papers 1C, 2C · shared with Double Award
- Role: CORE · confidence: high · section: S1 · checks: M1 True · M3 True · M4 True · M5 True
- Evidence [NOTE] `Chemistry IGCSE Revision Notes/1. Principles of Chemistry/e. Chemical Formulae, Equations, Calculations/Empirical & Molecular Formulae  Edexcel IGCSE Chemistry Revision Notes 2017.md`: “The molecular formula is the formula that shows the number and type of each atom in a molecule”
- Upstream: T-C10 HUMAN_VALIDATED 4CH1-1.32 + 4CH1-1.33 @ Empirical & Molecular Formulae (2026-09-11); spec wordings
- Verdict: [ ] CONFIRM — the concept genuinely subsumes this SP's demand   [ ] REJECT — wrong concept/SP pairing   [ ] HOLD — needs better evidence (state what)
- Reviewer note:

### 27. `4CH1-CON-CONSERVATION-MASS` PART_OF `4CH1-1.26` — mapping_id `af846a5f28c7ecd1`
- Concept: Law of Conservation of Mass  (aliases: conservation of mass) · node status: SUGGESTED
- SP official wording (R2): “ calculate relative formula masses (including relative molecular masses) (Mr) from relative atomic masses (Ar)”
- SP applicability: papers 1C, 2C · shared with Double Award
- Role: SUPPORTING · confidence: high · section: S1 · checks: M1 True · M3 True · M4 True · M5 True
- Evidence [NOTE] `Chemistry IGCSE Revision Notes/1. Principles of Chemistry/e. Chemical Formulae, Equations, Calculations/Calculate Relative Mass  Edexcel IGCSE Chemistry Revision Notes 2017.md`: “In accordance with the Law of Conservation of Mass, the sum of the relative formula masses of the reactants will be the same as the sum of the relative formula masses of the products”
- Upstream: T-C10 HUMAN_VALIDATED 4CH1-1.25 @ Writing chemical equations; 4CH1-1.26 @ Calculate Relative Mass (2026-09-11)
- Verdict: [ ] CONFIRM — the concept genuinely subsumes this SP's demand   [ ] REJECT — wrong concept/SP pairing   [ ] HOLD — needs better evidence (state what)
- Reviewer note:

### 28. `4CH1-CON-BOND-BREAKING-MAKING` PART_OF `4CH1-3.6C` — mapping_id `b56662765f0f0b39`
- Concept: Bond-breaking endothermic, bond-making exothermic  (aliases: bond breaking, bond making, bond-breaking, bond-making…) · node status: SUGGESTED
- SP official wording (R2): “know that bond-breaking is an endothermic process and that bond-making is an exothermic process”
- SP applicability: papers 2C
- Role: CORE · confidence: high · section: S3 · checks: M1 True · M3 True · M4 True · M5 True · spec_in_r2 True
- Evidence [NOTE] `Chemistry IGCSE Revision Notes/3. Physical Chemistry/a. Energetics/What is bond energy - IGCSE Chemistry Revision Notes.md`: “During a chemical reaction energy must be taken in to break bonds”
- Evidence [NOTE] `Chemistry IGCSE Revision Notes/3. Physical Chemistry/a. Energetics/What is bond energy - IGCSE Chemistry Revision Notes.md`: “During a chemical reaction, energy is released when new bonds are formed”
- Evidence [SPEC] `graph/specification_points.yaml`: “bond-breaking is an endothermic process and that bond-making is an exothermic process”
- Upstream: T-C10 HUMAN_VALIDATED 4CH1-3.6C @ What is Bond Energy (2026-09-11); spec 4CH1-3.6C official wording
- Verdict: [ ] CONFIRM — the concept genuinely subsumes this SP's demand   [ ] REJECT — wrong concept/SP pairing   [ ] HOLD — needs better evidence (state what)
- Reviewer note:

### 29. `4CH1-CON-MOLE` PART_OF `4CH1-1.27` — mapping_id `b7b41e8b67b4688d`
- Concept: The mole (unit of amount of substance)  (aliases: amount of substance, chemical amount, mol) · node status: SUGGESTED
- SP official wording (R2): “know that the mole (mol) is the unit for the amount of a substance”
- SP applicability: papers 1C, 2C · shared with Double Award
- Role: CORE · confidence: high · section: S1 · checks: M1 True · M3 True · M4 True · M5 True · spec_in_r2 True
- Evidence [SPEC] `graph/specification_points.yaml`: “know that the mole (mol) is the unit for the amount of a substance”
- Evidence [NOTE] `Chemistry IGCSE Revision Notes/1. Principles of Chemistry/e. Chemical Formulae, Equations, Calculations/Calculating moles and mass - IGCSE Chemistry Revision Notes.md`: “Chemical amounts are measured in moles”
- Upstream: T-C10 HUMAN_VALIDATED 4CH1-1.27 @ Calculating moles and mass (2026-09-11); spec 4CH1-1.27 official wording
- Verdict: [ ] CONFIRM — the concept genuinely subsumes this SP's demand   [ ] REJECT — wrong concept/SP pairing   [ ] HOLD — needs better evidence (state what)
- Reviewer note:

### 30. `4CH1-CON-EQ-POSITION` PART_OF `4CH1-3.22C` — mapping_id `bf6658212cdd8a2c`
- Concept: Position of equilibrium (temperature and pressure effects; catalyst does not affect it)  (aliases: position of equilibrium, equilibrium position, shifts to the right, shifts to the left…) · node status: SUGGESTED
- SP official wording (R2): “know the effect of changing either temperature or pressure on the position of equilibrium in a reversible reaction:”
- SP applicability: papers 2C
- Role: CORE · confidence: high · section: S3 · checks: M1 True · M3 True · M4 True · M5 True · spec_in_r2 True
- Evidence [NOTE] `Chemistry IGCSE Revision Notes/3. Physical Chemistry/c. Reversible Reactions & Equilibria/The position of equilibrium - IGCSE Chemistry Revision Notes.md`: “To make this prediction it is necessary to know whether the reaction is exothermic or endothermic”
- Evidence [SPEC] `graph/specification_points.yaml`: “know the effect of changing either temperature or pressure on the position of equilibrium in a reversible reaction”
- Upstream: T-C10 HUMAN_VALIDATED 4CH1-3.21C @ The Position of Equilibrium (2026-09-11); T-C10 HUMAN_VALIDATED 4CH1-3.22C @ The Position of Equilibrium (2026-09-11); spec 4CH1-3.21C/3.22C official wording
- Verdict: [ ] CONFIRM — the concept genuinely subsumes this SP's demand   [ ] REJECT — wrong concept/SP pairing   [ ] HOLD — needs better evidence (state what)
- Reviewer note:

### 31. `4CH1-CON-EXP-FORMULA-DEDUCTION` PART_OF `4CH1-1.36` — mapping_id `c686a2582d4e9925`
- Concept: Experimental formula deduction (mass-difference method)  (aliases: deducing formulae by experiment, formula from mass measurements) · node status: SUGGESTED
- SP official wording (R2): “practical: know how to determine the formula of a metal oxide by combustion (e.g. magnesium oxide) or by reduction (e.g. copper(II) oxide)”
- SP applicability: papers 1C, 2C · shared with Double Award
- Role: CORE · confidence: high · section: S1 · checks: M1 True · M3 True · M4 True · M5 True
- Evidence [NOTE] `Chemistry IGCSE Revision Notes/1. Principles of Chemistry/e. Chemical Formulae, Equations, Calculations/Investigating metal oxide formulas - IGCSE Revision Notes.md`: “To determine the empirical formula of magnesium oxide by combustion of magnesium”
- Upstream: T-C10 HUMAN_VALIDATED 4CH1-1.31 @ Simple compound formulae + @ Investigating metal oxide formulas; 4CH1-1.36 @ Investigating metal oxide formulas (2026-09-11)
- Verdict: [ ] CONFIRM — the concept genuinely subsumes this SP's demand   [ ] REJECT — wrong concept/SP pairing   [ ] HOLD — needs better evidence (state what)
- Reviewer note:

### 32. `4CH1-CON-WATER-CRYST` PART_OF `4CH1-1.31` — mapping_id `cc16e1b347581dc3`
- Concept: Water of crystallisation and hydrated salts  (aliases: hydrated salt, water of crystallisation) · node status: SUGGESTED
- SP official wording (R2): “understand how the formulae of simple compounds can be obtained experimentally, including metal oxides, water and salts containing water of crystallisation”
- SP applicability: papers 1C, 2C · shared with Double Award
- Role: CORE · confidence: high · section: S1 · checks: M1 True · M3 True · M4 True · M5 True · spec_in_r2 True
- Evidence [SPEC] `graph/specification_points.yaml`: “salts containing water of crystallisation”
- Evidence [NOTE] `Chemistry IGCSE Revision Notes/1. Principles of Chemistry/e. Chemical Formulae, Equations, Calculations/Empirical & Molecular Formulae  Edexcel IGCSE Chemistry Revision Notes 2017.md`: “A hydrated salt is a crystallised salt that contains water molecules as part of its structure”
- Upstream: T-C10 HUMAN_VALIDATED 4CH1-1.31 @ Empirical & Molecular Formulae + @ Simple compound formulae (2026-09-11); spec 4CH1-1.31 wording
- Verdict: [ ] CONFIRM — the concept genuinely subsumes this SP's demand   [ ] REJECT — wrong concept/SP pairing   [ ] HOLD — needs better evidence (state what)
- Reviewer note:

### 33. `4CH1-CON-HEATING-CONSTANT-MASS` PART_OF `4CH1-1.7C` — mapping_id `d04783dbcfc34795`
- Concept: Heating to constant mass  (aliases: heating to constant mass, constant mass) · node status: SUGGESTED
- SP official wording (R2): “practical: investigate the solubility of a solid in water at a specific temperature”
- SP applicability: papers 2C
- Role: ENRICHMENT · confidence: high · section: S1 · checks: M1 True · M3 True · M4 True · M5 True
- Evidence [NOTE] `Chemistry IGCSE Revision Notes/1. Principles of Chemistry/a. States of Matter/Investigating solubility - IGCSE Chemistry Revision Notes.md`: “Repeat this process until the mass remains constant”
- Evidence [NOTE] `Chemistry IGCSE Revision Notes/1. Principles of Chemistry/a. States of Matter/Investigating solubility - IGCSE Chemistry Revision Notes.md`: “This is called heating to constant mass and confirms that all water has been removed”
- Upstream: T-C10 HUMAN_VALIDATED 4CH1-1.7C @ Investigating solubility (2026-09-11)
- Verdict: [ ] CONFIRM — the concept genuinely subsumes this SP's demand   [ ] REJECT — wrong concept/SP pairing   [ ] HOLD — needs better evidence (state what)
- Reviewer note:

### 34. `4CH1-CON-EXO-ENDO` PART_OF `4CH1-3.1` — mapping_id `d25cf56d69ac43ab`
- Concept: Exothermic and endothermic reactions (heat energy given out or taken in)  (aliases: exothermic, endothermic, exothermic reaction, endothermic reaction…) · node status: SUGGESTED
- SP official wording (R2): “know that chemical reactions in which heat energy is given out are described as exothermic, and those in which heat energy is taken in are described as endothermic”
- SP applicability: papers 1C, 2C · shared with Double Award
- Role: CORE · confidence: high · section: S3 · checks: M1 True · M3 True · M4 True · M5 True · spec_in_r2 True
- Evidence [NOTE] `Chemistry IGCSE Revision Notes/3. Physical Chemistry/a. Energetics/Exothermic and endothermic - IGCSE Chemistry Revision Notes.md`: “An exothermic reaction releases heat energy into the surroundings”
- Evidence [NOTE] `Chemistry IGCSE Revision Notes/3. Physical Chemistry/a. Energetics/Exothermic and endothermic - IGCSE Chemistry Revision Notes.md`: “An endothermic reaction takes heat energy in from the surroundings”
- Evidence [SPEC] `graph/specification_points.yaml`: “heat energy is given out are described as exothermic”
- Upstream: T-C10 HUMAN_VALIDATED 4CH1-3.1 @ Exothermic and Endothermic (2026-09-11); spec 4CH1-3.1 official wording
- Verdict: [ ] CONFIRM — the concept genuinely subsumes this SP's demand   [ ] REJECT — wrong concept/SP pairing   [ ] HOLD — needs better evidence (state what)
- Reviewer note:

### 35. `4CH1-CON-YIELD` PART_OF `4CH1-1.30` — mapping_id `d8c603cf8ff3c5ba`
- Concept: Yield (actual yield)  (aliases: actual yield, yield of a reaction) · node status: SUGGESTED
- SP official wording (R2): “calculate percentage yield”
- SP applicability: papers 1C, 2C · shared with Double Award
- Role: CORE · confidence: high · section: S1 · checks: M1 True · M3 True · M4 True · M5 True
- Evidence [NOTE] `Chemistry IGCSE Revision Notes/1. Principles of Chemistry/e. Chemical Formulae, Equations, Calculations/Calculate percentage yield - IGCSE Chemistry Revision Notes.md`: “The actual yield is the recorded amount of product obtained”
- Upstream: T-C10 HUMAN_VALIDATED 4CH1-1.30 @ Calculate percentage yield (2026-09-11)
- Verdict: [ ] CONFIRM — the concept genuinely subsumes this SP's demand   [ ] REJECT — wrong concept/SP pairing   [ ] HOLD — needs better evidence (state what)
- Reviewer note:

### 36. `4CH1-CON-RATE-EXPERIMENTS` PART_OF `4CH1-3.9` — mapping_id `e00cea1f8cc2f3d7`
- Concept: Rate-of-reaction experiments (gas collection, disappearing cross, timing methods)  (aliases: rate experiments, measuring rates of reaction, investigating rate of reaction, downward displacement…) · node status: SUGGESTED
- SP official wording (R2): “describe experiments to investigate the effects of changes in surface area of a solid, concentration of a solution, temperature and the use of a catalyst on the rate of a reaction”
- SP applicability: papers 1C, 2C · shared with Double Award
- Role: CORE · confidence: high · section: S3 · checks: M1 True · M3 True · M4 True · M5 True · spec_in_r2 True
- Evidence [NOTE] `Chemistry IGCSE Revision Notes/3. Physical Chemistry/b. Rates of Reaction/Rate of reaction - IGCSE Chemistry Revision Notes.md`: “You should be able to describe experiments to investigate the effect of surface area, concentration, temperature and a catalyst on a rate of reaction”
- Evidence [NOTE] `Chemistry IGCSE Revision Notes/3. Physical Chemistry/b. Rates of Reaction/How surface area affects rate - IGCSE Revision Notes.md`: “Investigating the effect of different size marble chips on the rate of reaction between calcium carbonate and hydrochloric acid”
- Evidence [NOTE] `Chemistry IGCSE Revision Notes/3. Physical Chemistry/b. Rates of Reaction/Investigating catalysts - IGCSE Chemistry Revision Notes.md`: “To investigate the effect of different solids on the catalytic decomposition of hydrogen peroxide”
- Evidence [SPEC] `graph/specification_points.yaml`: “describe experiments to investigate the effects of changes in surface area of a solid, concentration of a solution, temperature and the use of a catalyst on the rate of a reaction”
- Upstream: T-C10 HUMAN_VALIDATED 4CH1-3.9 @ Rate of Reaction (2026-09-11); T-C10 HUMAN_VALIDATED 4CH1-3.9 @ How Surface Area Affects Rate (2026-09-11); T-C10 HUMAN_VALIDATED 4CH1-3.9 @ Investigating Catalysts (2026-09-11); spec 4CH1-3.9 official wording
- Verdict: [ ] CONFIRM — the concept genuinely subsumes this SP's demand   [ ] REJECT — wrong concept/SP pairing   [ ] HOLD — needs better evidence (state what)
- Reviewer note:

### 37. `4CH1-CON-VOL-CONVERSION` PART_OF `4CH1-1.34C` — mapping_id `e0b1a0a719d12de0`
- Concept: Volume unit conversion (cm3/dm3)  (aliases: converting cm3 to dm3) · node status: SUGGESTED
- SP official wording (R2): “ understand how to carry out calculations involving amount of substance, volume and concentration (in mol/dm3) of solution”
- SP applicability: papers 2C
- Role: CORE · confidence: high · section: S1 · checks: M1 True · M3 True · M4 True · M5 True
- Evidence [NOTE] `Chemistry IGCSE Revision Notes/1. Principles of Chemistry/e. Chemical Formulae, Equations, Calculations/Solution concentration - IGCSE Chemistry Revision Notes.md`: “To convert cm3 to dm3, divide by 1000”
- Upstream: T-C10 HUMAN_VALIDATED 4CH1-1.34C @ Solution concentration (2026-09-11)
- Verdict: [ ] CONFIRM — the concept genuinely subsumes this SP's demand   [ ] REJECT — wrong concept/SP pairing   [ ] HOLD — needs better evidence (state what)
- Reviewer note:

### 38. `4CH1-CON-CONSERVATION-MASS` PART_OF `4CH1-1.25` — mapping_id `e0b30d5cb28f50c1`
- Concept: Law of Conservation of Mass  (aliases: conservation of mass) · node status: SUGGESTED
- SP official wording (R2): “write word equations and balanced chemical equations (including state symbols):”
- SP applicability: papers 1C, 2C · shared with Double Award
- Role: CORE · confidence: high · section: S1 · checks: M1 True · M3 True · M4 True · M5 True
- Evidence [NOTE] `Chemistry IGCSE Revision Notes/1. Principles of Chemistry/e. Chemical Formulae, Equations, Calculations/Writing chemical equations - IGCSE Chemistry Revision Notes.md`: “Atoms cannot be created or destroyed, so if they exist in the reactants then they absolutely must be in the products!”
- Upstream: T-C10 HUMAN_VALIDATED 4CH1-1.25 @ Writing chemical equations; 4CH1-1.26 @ Calculate Relative Mass (2026-09-11)
- Verdict: [ ] CONFIRM — the concept genuinely subsumes this SP's demand   [ ] REJECT — wrong concept/SP pairing   [ ] HOLD — needs better evidence (state what)
- Reviewer note:

### 39. `4CH1-CON-MOLAR-GAS-VOL` PART_OF `4CH1-1.35C` — mapping_id `e4039d5ce4821524`
- Concept: Molar gas volume at RTP (24 dm3)  (aliases: molar volume, molar gas volume) · node status: SUGGESTED
- SP official wording (R2): “understand how to carry out calculations involving gas volumes and the molar volume of a gas (24 dm 3 and 24 000 cm 3 at room temperature and pressure (rtp))”
- SP applicability: papers 2C
- Role: CORE · confidence: high · section: S1 · checks: M1 True · M3 True · M4 True · M5 True · spec_in_r2 True
- Evidence [SPEC] `graph/specification_points.yaml`: “gas volumes and the molar volume of a gas (24 dm 3 and 24 000 cm 3 at room temperature and pressure (rtp))”
- Evidence [NOTE] `Chemistry IGCSE Revision Notes/1. Principles of Chemistry/e. Chemical Formulae, Equations, Calculations/Calculate Gas Volumes - IGCSE Chemistry Revision Notes.md`: “At room temperature and pressure, the volume occupied by one mole of any gas was found to be 24 dm3 or 24,000 cm3”
- Upstream: T-C10 HUMAN_VALIDATED 4CH1-1.35C @ Calculate Gas Volumes (2026-09-11); spec 4CH1-1.35C official wording
- Verdict: [ ] CONFIRM — the concept genuinely subsumes this SP's demand   [ ] REJECT — wrong concept/SP pairing   [ ] HOLD — needs better evidence (state what)
- Reviewer note:

### 40. `4CH1-CON-STATE-CHANGES` PART_OF `4CH1-1.2` — mapping_id `efcbe29df6f82c2f`
- Concept: Interconversions between the three states (melting, freezing, boiling, condensation, sublimation)  (aliases: changes of state, interconversion, melting, freezing…) · node status: SUGGESTED
- SP official wording (R2): “understand the interconversions between the three states of matter in terms of:”
- SP applicability: papers 1C, 2C · shared with Double Award
- Role: CORE · confidence: high · section: S1 · checks: M1 True · M3 True · M4 True · M5 True · spec_in_r2 True
- Evidence [NOTE] `Chemistry IGCSE Revision Notes/1. Principles of Chemistry/a. States of Matter/Changing states of matter - IGCSE Chemistry Revision Notes.md`: “State changes occur at the melting point (solid to liquid, liquid to solid) and at the boiling point (liquid to gas and gas to liquid)”
- Evidence [SPEC] `graph/specification_points.yaml`: “interconversions between the three states of matter”
- Upstream: T-C10 HUMAN_VALIDATED 4CH1-1.2 @ Changing states of matter (2026-09-11); spec 4CH1-1.2 official wording
- Verdict: [ ] CONFIRM — the concept genuinely subsumes this SP's demand   [ ] REJECT — wrong concept/SP pairing   [ ] HOLD — needs better evidence (state what)
- Reviewer note:

### 41. `4CH1-CON-SOLUTION` PART_OF `4CH1-1.4` — mapping_id `fb9ffd5706778ea7`
- Concept: Solution, solute and solvent  (aliases: solution, solute, solvent) · node status: SUGGESTED
- SP official wording (R2): “know what is meant by the terms:”
- SP applicability: papers 1C, 2C · shared with Double Award
- Role: CORE · confidence: high · section: S1 · checks: M1 True · M3 True · M4 True · M5 True · spec_in_r2 False
- Evidence [NOTE] `Chemistry IGCSE Revision Notes/1. Principles of Chemistry/a. States of Matter/Solutions - IGCSE Chemistry Revision Notes.md`: “The liquid in which a solute dissolves”
- Evidence [NOTE] `Chemistry IGCSE Revision Notes/1. Principles of Chemistry/a. States of Matter/Solutions - IGCSE Chemistry Revision Notes.md`: “The mixture formed when a solute is dissolved in a solvent”
- Evidence [SPEC] `graph/specification_points.yaml`: “solvent”
- Upstream: T-C10 HUMAN_VALIDATED 4CH1-1.4 @ Solutions (2026-09-11); spec 4CH1-1.4 official wording
- Verdict: [ ] CONFIRM — the concept genuinely subsumes this SP's demand   [ ] REJECT — wrong concept/SP pairing   [ ] HOLD — needs better evidence (state what)
- Reviewer note:

## Part B — in-scope gap register (no authoring in this lane)

In-scope SPs carrying no attachment row: 5 (4CH1-1.13, 4CH1-1.60C, 4CH1-3.15, 4CH1-3.16, 4CH1-3.8).
Verdict vocabulary here is DEFER-only: T-C19 validates what exists; new concepts/attachments are T-C11 expansion-round authoring (batch 5 per the §16 order), not this lane.

### 4CH1-1.13
- Status: no attachment row in the store (r2 wording: “practical: investigate paper chromatography using inks/food colourings”)
- Verdict: [x] DEFER → T-C11 expansion round
- Reviewer note:

### 4CH1-1.60C
- Status: no attachment row in the store (r2 wording: “practical: investigate the electrolysis of aqueous solutions”)
- Verdict: [x] DEFER → T-C11 expansion round
- Reviewer note:

### 4CH1-3.15
- Status: no attachment row in the store (r2 wording: “practical: investigate the effect of changing the surface area of marble chips and of changing the concentration of hydrochloric acid on the rate of reaction between marble chips and dilute hydrochloric acid”)
- Verdict: [x] DEFER → T-C11 expansion round
- Reviewer note:

### 4CH1-3.16
- Status: no attachment row in the store (r2 wording: “practical: investigate the effect of different solids on the catalytic decomposition of hydrogen peroxide solution”)
- Verdict: [x] DEFER → T-C11 expansion round
- Reviewer note:

### 4CH1-3.8
- Status: no attachment row in the store (r2 wording: “practical: investigate temperature changes accompanying some of the following types of change:”)
- Verdict: [x] DEFER → T-C11 expansion round
- Reviewer note:

## Rollup (filled at gate time)

| Class (role|section) | stratum rows | sampled | CONFIRM | REJECT | HOLD | precision |
|---|---:|---:|---:|---:|---:|---:|
| CORE|S1 | 88 | 27 | — | — | — | — |
| CORE|S3 | 20 | 5 | — | — | — | — |
| ENRICHMENT|S1 | 6 | 6 | — | — | — | — |
| SUPPORTING|S1 | 3 | 3 | — | — | — | — |

gate arithmetic **PENDING** (filler computes; c19_promote.py re-computes and asserts)

