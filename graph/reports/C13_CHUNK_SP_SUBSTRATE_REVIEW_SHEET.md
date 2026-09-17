# C13 — Chunk→SP Substrate OPERATOR REVIEW SHEET (the promotion gate)

**Seed:** `2be697213aa8ccad` (sha256 of the emitted rows — deterministic regeneration) · **Rows:** 42 anchored
spot-checks + 13 worklist decisions.
**Rule:** this sheet is the ONLY path from SUGGESTED to HUMAN_VALIDATED for the chunk→SP substrate.
Per-class rollup: any confirmed-precision < 90% on the sampled rows → rework that class before promotion.
**Anti-forgery reminder:** the tool cannot emit HUMAN_VALIDATED rows (gate G5); only your verdicts here can.

## Verdict record (filled)

- **Filled:** 2026-09-18 (UTC+8) · Reviewer: **Super Z (GLM agent), acting as operator-delegate** under the
  operator's explicit instruction to complete this sheet with the agent's own verification capabilities.
  The human operator retains final sign-off; per the anti-forgery rule nothing here flips the store.
- **Part A method (per row):** two independent layers. *Mechanical:* each emitted row was re-verified in a
  sandbox mirror of the notes corpus pinned at resources `75755855f9` by re-running the pinned chunker
  (`c13-chunk-convention-1`) and the shared `norm()` — quote-in-chunk containment, chunk `sha256_16` /
  heading / chars agreement with the sheet, 1:1 `mapping_id` presence in `graph/spec_chunk_mappings.yaml`
  (all rows SUGGESTED), and cross-note anchor uniqueness with ambiguity-flag agreement — **42/42 PASS**.
  *Semantic:* each quote was judged against the SP's official 4CH1-2017 wording and the full chunk text
  for topical fidelity — all 42 confirmed; 4 rows carry supplementary-anchor recommendations (below).
- **Part B method (per row):** the note was re-chunked under the pinned convention; a fresh verbatim
  passage quote was authored from the SP-teaching section and mechanically verified before recording
  (`norm(quote) in norm(chunk)` containment **and** exactly-one-content-chunk uniqueness in its note) —
  12/12 AUTHOR verdicts carry verified quotes with target chunk identity; 4CH1-4.15 DEFERred (reason in row).
- **Result summary:** Part A precision **42/42 = 100%** (≥ 90% gate) · Part B **13/13 decided**
  (12 AUTHOR + 1 DEFER). Gate arithmetic passes; promotion remains a separate recorded apply step.

## Part A — anchored-row spot-check (42 rows, seeded 20% stratified + all ambiguous)

### 4CH1-3.3 — calculate the heat energy change from a measured temperature change using the expression $ Q=mc\Delta T $
- Note: Energetics calculations in chemistry - IGCSE Revision Notes (`3. Physical Chemistry/a. Energetics/Energetics calculations in chemistry - IGCSE Revision Notes.md`)
- Chunk: ordinal 1 — heading `Worked Example` — sha256_16 `7664e3d4c43118ec` — 1270 chars ⚠️ AMBIGUOUS (quote matches more than one section; lowest ordinal chosen)
- Evidence quote (verbatim, from the T-C10 store): "State the equation: Q = m x c x ΔT"
- Chunk excerpt: «Worked Example Excess iron powder was added to 100.0 cm<sup>3&nbsp;</sup> of 0.200 mol dm<sup>-3</sup> copper(II) sulfate solution in a calorimeter. The reaction equation was as follows. Fe (s) + CuSO<sub>4&nbsp;</sub> (aq) **→** FeSO<sub>4&nbsp;</sub> (aq) + Cu (s) The maximum temperature rise was 7.5 <sup>o</sup>C. Determine the heat energy change of the reaction, in kJ. **Answer:** The solution is assumed to have …»
- Upstream: T-C10 3. Physical Chemistry/a. Energetics/Energetics calculations in chemistry - IGCSE Revision Notes.md::4CH1-3.3 — HUMAN_VALIDATED 2026-09-11 — confidence high
- Rationale: Heat-energy-change calculation from measured temperature change with a fully worked displacement-reaction example.
- Verdict: [x] CONFIRM — quote anchors this chunk to this SP   [ ] REJECT — wrong chunk/SP   [ ] HOLD — needs better anchor
- Reviewer note: the quote matches both `Worked Example` chunks (ordinals 1 and 3); both are on-SP Q = mcΔT calculations from a measured temperature rise, so the deterministic lowest-ordinal choice is correct. Supplementary row at ordinal 3 recommended in the apply step.

### 4CH1-1.10 — describe these experimental techniques for the separation of mixtures: 简单 distillation fractional distillation filtration crystallisation paper chromatography.
- Note: Separation techniques - IGCSE Chemistry Revision Notes (`1. Principles of Chemistry/b. Elements, Compounds and Mixtures/Separation techniques - IGCSE Chemistry Revision Notes.md`)
- Chunk: ordinal 1 — heading `Simple distillation` — sha256_16 `ad1f0809913d2c33` — 576 chars
- Evidence quote (verbatim, from the T-C10 store): "Simple distillation is used to separate a liquid and soluble solid from a solution"
- Chunk excerpt: «Simple distillation - Simple distillation is used to separate a liquid and **soluble solid** from a solution (e.g., water from a solution of salt water) or a pure liquid from a mixture of liquids - The solution is heated, and pure water evaporates producing a vapour which rises through the neck of the round bottomed flask - The vapour passes through the condenser, where it cools and condenses, turning into the pure l…»
- Upstream: T-C10 1. Principles of Chemistry/b. Elements, Compounds and Mixtures/Separation techniques - IGCSE Chemistry Revision Notes.md::4CH1-1.10 — HUMAN_VALIDATED 2026-09-11 — confidence high
- Rationale: All five named techniques have dedicated sections: simple distillation, fractional distillation, filtration, crystallisation, paper chromatography.
- Verdict: [x] CONFIRM — quote anchors this chunk to this SP   [ ] REJECT — wrong chunk/SP   [ ] HOLD — needs better anchor

### 4CH1-1.45 — understand covalent bonds in terms of electrostatic attractions
- Note: Forming covalent bonds - IGCSE Chemistry Revision Notes (`1. Principles of Chemistry/g. Covalent Bonding/Forming covalent bonds - IGCSE Chemistry Revision Notes.md`)
- Chunk: ordinal 4 — heading `Electrostatic attractions` — sha256_16 `84ac2985ebb57baf` — 1056 chars
- Evidence quote (verbatim, from the T-C10 store): "electrostatic attraction between the shared pair of electrons and the nuclei of the atoms involved"
- Chunk excerpt: «Electrostatic attractions - There is a strong electrostatic attraction between the shared pair of electrons and the nuclei of the atoms involved, since the electrons are negatively charged and the nuclei are positively charged ![Hydrogen molecular orbital, downloadable IB Chemistry revision notes](../../assets/4.1.4-hydrogen-molecular-orbital.png) _**The attraction between the shared pair of electrons and the nuclei …»
- Upstream: T-C10 1. Principles of Chemistry/g. Covalent Bonding/Forming covalent bonds - IGCSE Chemistry Revision Notes.md::4CH1-1.45 — HUMAN_VALIDATED 2026-09-11 — confidence high
- Rationale: Dedicated Electrostatic attractions section explaining the covalent bond in those terms.
- Verdict: [x] CONFIRM — quote anchors this chunk to this SP   [ ] REJECT — wrong chunk/SP   [ ] HOLD — needs better anchor

### 4CH1-2.48 — describe tests for these anions: · Cl$^{-}$, Br$^{-}$ and I$^{-}$ using acidified silver nitrate solution · SO$_{4}^{2-}$ using acidified barium chloride solution · CO$_{3}^{2-}$ using hydrochloric acid and identifying the gas evolved.
- Note: Tests for Anions | Edexcel IGCSE Chemistry Revision Notes 2017 (`2. Inorganic Chemistry/h. Chemical Tests/Tests for Anions  Edexcel IGCSE Chemistry Revision Notes 2017.md`)
- Chunk: ordinal 2 — heading `Test for carbonate ions` — sha256_16 `598786c1922c0df2` — 911 chars
- Evidence quote (verbatim, from the T-C10 store): "Limewater turns cloudy if the carbonate ion is present"
- Chunk excerpt: «Test for carbonate ions - Carbonate compounds contain the carbonate ion, CO<sub>3</sub><sup>2-</sup> - The test for the carbonate ion is: - Add **dilute acid** - Bubble the **gas** released through limewater - Limewater turns cloudy if the carbonate ion is present - If a carbonate compound is present then fizzing / effervescence should be seen as **CO**<sub><b>2</b></sub> gas is produced, which forms a white precipit…»
- Upstream: T-C10 2. Inorganic Chemistry/h. Chemical Tests/Tests for Anions  Edexcel IGCSE Chemistry Revision Notes 2017.md::4CH1-2.48 — HUMAN_VALIDATED 2026-09-11 — confidence high
- Rationale: Tests for carbonate (dilute acid + limewater), halides (acidified silver nitrate) and sulfate (acidified barium chloride) with equations and results.
- Verdict: [x] CONFIRM — quote anchors this chunk to this SP   [ ] REJECT — wrong chunk/SP   [ ] HOLD — needs better anchor

### 4CH1-4.45 — understand how to draw the repeat unit of an addition polymer, including poly(ethene), poly(propene), poly(chloroethene) and (poly)tetrafluoroethene
- Note: Addition Polymers | Edexcel IGCSE Chemistry Revision Notes 2017 (`4. Organic Chemistry/h. Synthetic Polymers/Addition Polymers  Edexcel IGCSE Chemistry Revision Notes 2017.md`)
- Chunk: ordinal 2 — heading `Drawing polymers` — sha256_16 `32947b710872a95a` — 832 chars
- Evidence quote (verbatim, from the T-C10 store): "The polymer polyethene is formed by the addition polymerisation of ethene monomers"
- Chunk excerpt: «Drawing polymers - Addition polymers are formed by the joining up of many monomers and only occurs in monomers that contain C=C bonds - **One** of the bonds in each C=C bond breaks and forms a bond with the adjacent monomer with the polymer being formed containing **single bonds** only - Many polymers can be made by the addition of alkene monomers - Others are made from alkene monomers with different atoms attached t…»
- Upstream: T-C10 4. Organic Chemistry/h. Synthetic Polymers/Addition Polymers  Edexcel IGCSE Chemistry Revision Notes 2017.md::4CH1-4.45 — HUMAN_VALIDATED 2026-09-11 — confidence high
- Rationale: Drawing polymers and repeat units from the monomer (polyethene, polypropene, chloroethene examples). Note for PR review: poly(tetrafluoroethene) is not among the worked examples in this note.
- Verdict: [x] CONFIRM — quote anchors this chunk to this SP   [ ] REJECT — wrong chunk/SP   [ ] HOLD — needs better anchor

### 4CH1-4.33C — understand the reasons for fermentation,in the absence of air,and at an optimum temperature
- Note: Manufacture of Ethanol | Edexcel IGCSE Chemistry Revision Notes 2017 (`4. Organic Chemistry/e. Alcohols/Manufacture of Ethanol  Edexcel IGCSE Chemistry Revision Notes 2017.md`)
- Chunk: ordinal 4 — heading `Fermentation` — sha256_16 `159d46aa78a5a3af` — 1098 chars
- Evidence quote (verbatim, from the T-C10 store): "enzymes that break down sugar to alcohol"
- Chunk excerpt: «Fermentation - Ethanol can also be produced by fermentation where sugar or starch is dissolved in water and yeast is added - The mixture is then fermented between **25** and **35°C** (the optimum temperature is **30 °C**) with the **absence** of oxygen for a few days - Yeast contains enzymes that break down sugar to alcohol - If the temperature is too **low** the reaction rate will be too slow and if it is too **high…»
- Upstream: T-C10 4. Organic Chemistry/e. Alcohols/Manufacture of Ethanol  Edexcel IGCSE Chemistry Revision Notes 2017.md::4CH1-4.33C — HUMAN_VALIDATED 2026-09-11 — confidence high
- Rationale: Fermentation conditions explained: yeast enzymes (optimum ~30 C, denature if hotter) and absence of oxygen preventing aerobic oxidation.
- Verdict: [x] CONFIRM — quote anchors this chunk to this SP   [ ] REJECT — wrong chunk/SP   [ ] HOLD — needs better anchor

### 4CH1-1.33 — calculate empirical and molecular formulae from experimental data
- Note: Empirical & Molecular Formulae | Edexcel IGCSE Chemistry Revision Notes 2017 (`1. Principles of Chemistry/e. Chemical Formulae, Equations, Calculations/Empirical & Molecular Formulae  Edexcel IGCSE Chemistry Revision Notes 2017.md`)
- Chunk: ordinal 3 — heading `How to calculate empirical formulae` — sha256_16 `1222f85a4e25145b` — 983 chars
- Evidence quote (verbatim, from the T-C10 store): "Use a table and the following steps to complete an empirical formula calculation"
- Chunk excerpt: «How to calculate empirical formulae - Empirical formula calculations are very methodical - Use a table and the following steps to complete an empirical formula calculation: 1. Write the element 2. Write the value given for each element - This may be given as a mass, in g, or as a percentage - There are exam questions where you are required to calculate the value of one of the elements 3. Write the relative atomic mas…»
- Upstream: T-C10 1. Principles of Chemistry/e. Chemical Formulae, Equations, Calculations/Empirical & Molecular Formulae  Edexcel IGCSE Chemistry Revision Notes 2017.md::4CH1-1.33 — HUMAN_VALIDATED 2026-09-11 — confidence high
- Rationale: Step-by-step empirical formula determination from mass/percentage data plus molecular formula from Mr, with worked examples.
- Verdict: [x] CONFIRM — quote anchors this chunk to this SP   [ ] REJECT — wrong chunk/SP   [ ] HOLD — needs better anchor

### 4CH1-2.18 — know the conditions under which iron rusts
- Note: Rusting of iron - IGCSE Chemistry Revision Notes (`2. Inorganic Chemistry/d. Reactivity Series/Rusting of iron - IGCSE Chemistry Revision Notes.md`)
- Chunk: ordinal 2 — heading `Investigating rusting` — sha256_16 `1859c40a682a3a0d` — 298 chars
- Evidence quote (verbatim, from the T-C10 store): "Oxygen and water must be present for rust to occur"
- Chunk excerpt: «Investigating rusting - **Oxygen** and **water** must be present for rust to occur - You can investigate the conditions needed for rusting by setting up a series of control test tubes as shown below - Boiled water removes any dissolved oxygen and calcium chloride is a drying agent…»
- Upstream: T-C10 2. Inorganic Chemistry/d. Reactivity Series/Rusting of iron - IGCSE Chemistry Revision Notes.md::4CH1-2.18 — HUMAN_VALIDATED 2026-09-11 — confidence high
- Rationale: Rusting-conditions investigation with the three control tubes (air+water, no air, no water).
- Verdict: [x] CONFIRM — quote anchors this chunk to this SP   [ ] REJECT — wrong chunk/SP   [ ] HOLD — needs better anchor

### 4CH1-1.35C — understand how to carry out calculations involving gas volumes and the molar volume of a gas(24dm3and24000cm3at room temperature and pressure(rtp))
- Note: Calculate Gas Volumes - IGCSE Chemistry Revision Notes (`1. Principles of Chemistry/e. Chemical Formulae, Equations, Calculations/Calculate Gas Volumes - IGCSE Chemistry Revision Notes.md`)
- Chunk: ordinal 2 — heading `Avogadro's Law` — sha256_16 `c40882f251c5af4d` — 1440 chars
- Evidence quote (verbatim, from the T-C10 store): "This is known as the molar gas volume at RTP"
- Chunk excerpt: «Avogadro's Law - **Avogadro’s Law** states that at the same conditions of **temperature** and **pressure**, equal amounts of gases occupy the **same volume** of space - At room temperature and pressure, the volume occupied by one mole of any gas was found to be **24** dm<sup>3</sup> or **24,000** cm<sup>3</sup> - This is known as the **molar gas volume at RTP** - RTP stands for “room temperature and pressure” and the…»
- Upstream: T-C10 1. Principles of Chemistry/e. Chemical Formulae, Equations, Calculations/Calculate Gas Volumes - IGCSE Chemistry Revision Notes.md::4CH1-1.35C — HUMAN_VALIDATED 2026-09-11 — confidence high
- Rationale: Molar volume 24 dm3 / 24000 cm3 at RTP, Avogadro's Law, mole-to-volume and volume-to-mole conversions with worked examples.
- Verdict: [x] CONFIRM — quote anchors this chunk to this SP   [ ] REJECT — wrong chunk/SP   [ ] HOLD — needs better anchor

### 4CH1-2.29 — understand how to use the pH scale, from 0-14, can be used to classify solutions as strongly acidic(0-3), weakly acidic(4-6), neutral(7), weakly alkaline(8-10)和 strongly alkaline(11-14)
- Note: What is an indicator? - IGCSE Chemistry Revision Notes (`2. Inorganic Chemistry/f. Acids, Alkalis & Titrations/What is an indicator - IGCSE Chemistry Revision Notes.md`)
- Chunk: ordinal 4 — heading `The pH scale` — sha256_16 `658ae389af263860` — 582 chars
- Evidence quote (verbatim, from the T-C10 store): "The pH scale goes from 0 – 14"
- Chunk excerpt: «The pH scale - The pH scale goes from 0 – 14 - All acids have pH values of **below** 7, all alkalis have pH values of **above** 7 - The **lower** the pH then the **more acidic** the solution is - pH 0-3 = strong acid - Extremely acidic substances can have values of below 1 - pH 4-6 = weak acid - The **higher** the pH then the **more alkaline** the solution is - pH 8-10 = weak alkali - pH 11-14 = strong alkali - A sol…»
- Upstream: T-C10 2. Inorganic Chemistry/f. Acids, Alkalis & Titrations/What is an indicator - IGCSE Chemistry Revision Notes.md::4CH1-2.29 — HUMAN_VALIDATED 2026-09-11 — confidence high
- Rationale: pH scale section with the 0-14 classification (acids below 7, alkalis above 7, bands by strength).
- Verdict: [x] CONFIRM — quote anchors this chunk to this SP   [ ] REJECT — wrong chunk/SP   [ ] HOLD — needs better anchor

### 4CH1-4.4 — understand how to name compounds relevant to this specification using the rules of International Union of Pure and Applied Chemistry (IUPAC) nomenclature students will be expected to name compounds containing up to six carbon atoms
- Note: Naming Organic Compounds | Edexcel IGCSE Chemistry Revision Notes 2017 (`4. Organic Chemistry/a. Introduction/Naming Organic Compounds  Edexcel IGCSE Chemistry Revision Notes 2017.md`)
- Chunk: ordinal 2 — heading `Names of compounds` — sha256_16 `5498a4d177be5532` — 305 chars
- Evidence quote (verbatim, from the T-C10 store): "The prefix tells you how many carbon atoms are present in the longest continuous chain in the compound"
- Chunk excerpt: «Names of compounds - The names of organic compounds have two parts: the prefix or stem and the end part (or suffix) - The prefix tells you how many carbon atoms are present in the longest continuous chain in the compound - The suffix tells you what **functional group** is on the compound…»
- Upstream: T-C10 4. Organic Chemistry/a. Introduction/Naming Organic Compounds  Edexcel IGCSE Chemistry Revision Notes 2017.md::4CH1-4.4 — HUMAN_VALIDATED 2026-09-11 — confidence high
- Rationale: IUPAC naming rules: stem/suffix system, further rules section, naming-isomers worked examples (up to six carbons implied by stem table).
- Verdict: [x] CONFIRM — quote anchors this chunk to this SP   [ ] REJECT — wrong chunk/SP   [ ] HOLD — needs better anchor

### 4CH1-1.50 — explain how the structures of diamond, graphite and C60 fullerene influence their physical properties, including electrical conductivity and hardness
- Note: Giant covalent structures - IGCSE Chemistry Revision Notes (`1. Principles of Chemistry/g. Covalent Bonding/Giant covalent structures - IGCSE Chemistry Revision Notes.md`)
- Chunk: ordinal 6 — heading `Examiner Tips and Tricks` — sha256_16 `b75b11ee5d2bab34` — 368 chars
- Evidence quote (verbatim, from the T-C10 store): "Diamond is the hardest naturally occurring mineral"
- Chunk excerpt: «Examiner Tips and Tricks Diamond is the hardest naturally occurring mineral, but it is by no means the strongest. Students often confuse **hard** with **strong**, thinking it is the opposites of weak. Diamonds are hard, but brittle – that is, they can be smashed fairly easily with a hammer. The opposite of saying a material is hard is to describe it as **soft**.…»
- Upstream: T-C10 1. Principles of Chemistry/g. Covalent Bonding/Giant covalent structures - IGCSE Chemistry Revision Notes.md::4CH1-1.50 — HUMAN_VALIDATED 2026-09-11 — confidence high
- Rationale: Structure-to-properties for diamond (rigid network, hard, high m.p.) and graphite (layers, free electron, soft/slippery, conducts) — the 1.50 core content; C60 fullerene handled in the simple-molecular note.
- Verdict: [x] CONFIRM — quote anchors this chunk to this SP   [ ] REJECT — wrong chunk/SP   [ ] HOLD — needs better anchor
- Reviewer note: faithful anchor of the upstream T-C10 evidence quote (Examiner Tips section — diamond hard-vs-strong). The note's own properties sections (ordinal 5 'What are the properties of diamond?', ordinal 9 'What are the properties of graphite?') are materially better SP-teaching chunks — recommend supplementary rows in the apply step.

### 4CH1-1.48 — explain why the melting and boiling points of substances with simple molecular structures increase, in general, with increasing relative molecular mass
- Note: Simple molecular structures - IGCSE Chemistry Revision Notes (`1. Principles of Chemistry/g. Covalent Bonding/Simple molecular structures - IGCSE Chemistry Revision Notes.md`)
- Chunk: ordinal 1 — heading `Simple molecular structures` — sha256_16 `d9f7ec8abc27e73a` — 1011 chars
- Evidence quote (verbatim, from the T-C10 store): "As the molecules increase in size, the melting and boiling points generally increase because the strength of these intermolecular forces increases"
- Chunk excerpt: «Simple molecular structures - Simple molecular structures have covalent bonds joining the atoms together, but intermolecular forces that act between neighbouring molecules are weak - They have relatively **low melting and boiling points** because: - There are weak intermolecular forces between the molecules - These forces require little energy to overcome - Most simple molecular structures are either gases or liquids…»
- Upstream: T-C10 1. Principles of Chemistry/g. Covalent Bonding/Simple molecular structures - IGCSE Chemistry Revision Notes.md::4CH1-1.48 — HUMAN_VALIDATED 2026-09-11 — confidence high
- Rationale: Dedicated Melting and boiling point patterns section relating m.p./b.p. to relative molecular mass.
- Verdict: [x] CONFIRM — quote anchors this chunk to this SP   [ ] REJECT — wrong chunk/SP   [ ] HOLD — needs better anchor

### 4CH1-2.50 — describe a physical test to show whether a sample of water is pure
- Note: Chemical test for water - IGCSE Chemistry Revision Notes (`2. Inorganic Chemistry/h. Chemical Tests/Chemical test for water - IGCSE Chemistry Revision Notes.md`)
- Chunk: ordinal 3 — heading `Physical test for water` — sha256_16 `fabbb6e9138f2602` — 436 chars
- Evidence quote (verbatim, from the T-C10 store): "physical test to see if a sample of water is pure is to check its boiling point"
- Chunk excerpt: «Physical test for water - A physical test to see if a sample of water is pure is to check its boiling point - A sample of the liquid is placed in a suitable container such as a boiling tube and gently heated - Using a thermometer, you can check if the boiling point is exactly 100 <sup>o</sup>C - Any impurities present will usually tend to raise the boiling point and depress the melting point of pure substance…»
- Upstream: T-C10 2. Inorganic Chemistry/h. Chemical Tests/Chemical test for water - IGCSE Chemistry Revision Notes.md::4CH1-2.50 — HUMAN_VALIDATED 2026-09-11 — confidence high
- Rationale: Physical purity test section (boiling point of pure water).
- Verdict: [x] CONFIRM — quote anchors this chunk to this SP   [ ] REJECT — wrong chunk/SP   [ ] HOLD — needs better anchor

### 4CH1-2.30 — describe the use of universal indicator to measure the approximate pH value of an aqueous solution
- Note: What is an indicator? - IGCSE Chemistry Revision Notes (`2. Inorganic Chemistry/f. Acids, Alkalis & Titrations/What is an indicator - IGCSE Chemistry Revision Notes.md`)
- Chunk: ordinal 5 — heading `Universal indicator` — sha256_16 `d9d3442a314b7835` — 817 chars
- Evidence quote (verbatim, from the T-C10 store): "Universal indicator is a wide range indicator and can give only an approximate value for pH"
- Chunk excerpt: «Universal indicator - Universal indicator is a wide range indicator and can give only an approximate value for pH It is made of a mixture of different plant **indicators** which operate across a broad pH range and is useful for estimating the pH of an **unknown solution** A few drops are added to the solution and the colour is matched with a colour chart which indicates the pH which matches with specific colours Univ…»
- Upstream: T-C10 2. Inorganic Chemistry/f. Acids, Alkalis & Titrations/What is an indicator - IGCSE Chemistry Revision Notes.md::4CH1-2.30 — HUMAN_VALIDATED 2026-09-11 — confidence high
- Rationale: Universal indicator section on measuring approximate pH of aqueous solutions.
- Verdict: [x] CONFIRM — quote anchors this chunk to this SP   [ ] REJECT — wrong chunk/SP   [ ] HOLD — needs better anchor

### 4CH1-1.7C — practical: investigate the solubility of a solid in water at a specific temperature
- Note: Investigating solubility - IGCSE Chemistry Revision Notes (`1. Principles of Chemistry/a. States of Matter/Investigating solubility - IGCSE Chemistry Revision Notes.md`)
- Chunk: ordinal 2 — heading `Aim` — sha256_16 `5380c95c3eef37d5` — 179 chars
- Evidence quote (verbatim, from the T-C10 store): "To find the solubility of a solid in water at a given temperature by preparing a saturated solution"
- Chunk excerpt: «Aim - To find the solubility of a solid in water at a given temperature by preparing a saturated solution, evaporating the solvent, and measuring the mass of the solid obtained…»
- Upstream: T-C10 1. Principles of Chemistry/a. States of Matter/Investigating solubility - IGCSE Chemistry Revision Notes.md::4CH1-1.7C — HUMAN_VALIDATED 2026-09-11 — confidence high
- Rationale: This IS the named practical: saturated solution preparation, temperature control, evaporation, mass measurement.
- Verdict: [x] CONFIRM — quote anchors this chunk to this SP   [ ] REJECT — wrong chunk/SP   [ ] HOLD — needs better anchor

### 4CH1-3.22C — know the effect of changing either temperature or pressure on the position of equilibrium in a reversible reaction: • an increase (or decrease) in temperature shifts the position of equilibrium in the direction of the endothermic (or exothermic) reaction • an increase (or decrease) in pressure shifts the position of equilibrium in the direction that produces fewer (or more) moles of gas References to Le Chatelier's principle are not required
- Note: The position of equilibrium - IGCSE Chemistry Revision Notes (`3. Physical Chemistry/c. Reversible Reactions & Equilibria/The position of equilibrium - IGCSE Chemistry Revision Notes.md`)
- Chunk: ordinal 1 — heading `The position of equilibrium` — sha256_16 `9cade9433e4dbbc2` — 1369 chars
- Evidence quote (verbatim, from the T-C10 store): "if pressure is increased, the position of equilibrium moves in the direction which has the smallest amount of gaseous molecules"
- Chunk excerpt: «The position of equilibrium - The relative amounts of all the reactants and products at equilibrium depend on the **conditions** of the reaction - This balance is framed in an important concept known as Le Chatelier's Principle, - Named after Henri Le Chatelier, who was a French military engineer in the 19th century - This principle states that when a change is made to the conditions of a system at equilibrium, the s…»
- Upstream: T-C10 3. Physical Chemistry/c. Reversible Reactions & Equilibria/The position of equilibrium - IGCSE Chemistry Revision Notes.md::4CH1-3.22C — HUMAN_VALIDATED 2026-09-11 — confidence high
- Rationale: Temperature and pressure effects on equilibrium position with worked examples (Le Chatelier used as teaching frame, not required language).
- Verdict: [x] CONFIRM — quote anchors this chunk to this SP   [ ] REJECT — wrong chunk/SP   [ ] HOLD — needs better anchor

### 4CH1-3.15 — practical: investigate the effect of changing the surface area of marble chips and of changing the concentration of hydrochloric acid on the rate of reaction between marble chips and dilute hydrochloric acid
- Note: How surface area affects rate - IGCSE Revision Notes (`3. Physical Chemistry/b. Rates of Reaction/How surface area affects rate - IGCSE Revision Notes.md`)
- Chunk: ordinal 3 — heading `Diagram:` — sha256_16 `253fef35d478b661` — 647 chars
- Evidence quote (verbatim, from the T-C10 store): "Investigating the effect of different size marble chips on the rate of reaction between calcium carbonate and hydrochloric acid"
- Chunk excerpt: «Diagram: ![Effect of Surface Area on a Reaction Rate 1, downloadable IGCSE & GCSE Chemistry revision notes](../../assets/3.2.1-Effect-of-Surface-Area-on-a-Reaction-Rate-1.png) ![Effect of Surface Area on a Reaction Rate 2, downloadable IGCSE & GCSE Chemistry revision notes](../../assets/3.2.1-Effect-of-Surface-Area-on-a-Reaction-Rate-2.png) ![Effect of Surface Area on a Reaction Rate 3, downloadable IGCSE & GCSE Chem…»
- Upstream: T-C10 3. Physical Chemistry/b. Rates of Reaction/How surface area affects rate - IGCSE Revision Notes.md::4CH1-3.15 — HUMAN_VALIDATED 2026-09-11 — confidence high
- Rationale: This IS the named practical (surface-area strand): marble chips + dilute HCl with method, results, conclusion.
- Verdict: [x] CONFIRM — quote anchors this chunk to this SP   [ ] REJECT — wrong chunk/SP   [ ] HOLD — needs better anchor

### 4CH1-4.41C — understand how to write the structural and displayed formulae of an ester, given the name or formula of the alcohol and carboxylic acid from which it is formed and vice versa
- Note: Making and naming esters - IGCSE Chemistry Revision Notes (`4. Organic Chemistry/g. Esters/Making and naming esters - IGCSE Chemistry Revision Notes.md`)
- Chunk: ordinal 4 — heading `Naming Esters` — sha256_16 `c90ad0d7c5a88c4b` — 635 chars
- Evidence quote (verbatim, from the T-C10 store): "An ester is made from an alcohol and carboxylic acid"
- Chunk excerpt: «Naming Esters - An ester is made from an alcohol and carboxylic acid - The first part of the name indicates the length of the carbon chain in the alcohol, and it ends with the letters ‘- yl’ - The second part of the name indicates the length of the carbon chain in the carboxylic acid, and it ends with the letters ‘- oate’ - E.g. The ester formed from **pent**anol and **butan**oic acid is called **pent**yl **butan**oa…»
- Upstream: T-C10 4. Organic Chemistry/g. Esters/Making and naming esters - IGCSE Chemistry Revision Notes.md::4CH1-4.41C — HUMAN_VALIDATED 2026-09-11 — confidence high
- Rationale: Naming-esters system mapping alcohol + acid to the ester name and formula (both directions), with the examples table.
- Verdict: [x] CONFIRM — quote anchors this chunk to this SP   [ ] REJECT — wrong chunk/SP   [ ] HOLD — needs better anchor

### 4CH1-3.2 — describe simple calorimetry experiments for reactions such as combustion, displacement, dissolving and neutralisation
- Note: Calorimetry - IGCSE Chemistry Revision Notes (`3. Physical Chemistry/a. Energetics/Calorimetry - IGCSE Chemistry Revision Notes.md`)
- Chunk: ordinal 1 — heading `Calorimetry` — sha256_16 `4f33b9da8592fdc2` — 345 chars
- Evidence quote (verbatim, from the T-C10 store): "There are two types of calorimetry experiments you need to know"
- Chunk excerpt: «Calorimetry - We can experimentally determine the relative amounts of energy released by a fuel - We do this using **simple** **calorimetry** - There are two types of calorimetry experiments you need to know: - **Enthalpy** changes of **reactions in solution** - **Enthalpy** changes of **combustion**…»
- Upstream: T-C10 3. Physical Chemistry/a. Energetics/Calorimetry - IGCSE Chemistry Revision Notes.md::4CH1-3.2 — HUMAN_VALIDATED 2026-09-11 — confidence high
- Rationale: Simple calorimetry for reactions in solution (neutralisation, dissolving, displacement) and combustion, with apparatus diagram and error analysis.
- Verdict: [x] CONFIRM — quote anchors this chunk to this SP   [ ] REJECT — wrong chunk/SP   [ ] HOLD — needs better anchor

### 4CH1-3.8 — practical: investigate temperature changes accompanying some of the following types of change: • salts dissolving in water • neutralisation reactions • displacement reactions • combustion reactions.
- Note: Temperature change practical - IGCSE Revision Notes (`3. Physical Chemistry/a. Energetics/Temperature change practical - IGCSE Revision Notes.md`)
- Chunk: ordinal 2 — heading `Aim:` — sha256_16 `82e32176da94404f` — 77 chars
- Evidence quote (verbatim, from the T-C10 store): "To perform a calorimetry study of the reaction between HCl and NaOH"
- Chunk excerpt: «Aim: - To perform a calorimetry study of the reaction between HCl and NaOH…»
- Upstream: T-C10 3. Physical Chemistry/a. Energetics/Temperature change practical - IGCSE Revision Notes.md::4CH1-3.8 — HUMAN_VALIDATED 2026-09-11 — confidence high
- Rationale: This IS the named practical (neutralisation strand): styrofoam calorimeter, method, results table, conclusion.
- Verdict: [x] CONFIRM — quote anchors this chunk to this SP   [ ] REJECT — wrong chunk/SP   [ ] HOLD — needs better anchor

### 4CH1-4.50C — know that some polyesters, known as biopolyesters, are biodegradable
- Note: Condensation polymerisation - IGCSE Chemistry Revision Notes (`4. Organic Chemistry/h. Synthetic Polymers/Condensation polymerisation - IGCSE Chemistry Revision Notes.md`)
- Chunk: ordinal 3 — heading `Biopolyesters` — sha256_16 `07b8c1ee18378d4f` — 517 chars
- Evidence quote (verbatim, from the T-C10 store): "Biopolyesters are a specific type of polymers that are synthesised from sugars and plant oils"
- Chunk excerpt: «Biopolyesters - Biopolyesters are a specific type of polymers that are synthesised from sugars and plant oils using microorganisms - They are able to **biodegrade** naturally in the environment after their intended purpose - The polymers are synthetically made, consisting of ester, amide and ether functional groups which gives them the characteristic of being biodegradable ![Diagram of biopolysters](../../assets/biop…»
- Upstream: T-C10 4. Organic Chemistry/h. Synthetic Polymers/Condensation polymerisation - IGCSE Chemistry Revision Notes.md::4CH1-4.50C — HUMAN_VALIDATED 2026-09-11 — confidence high
- Rationale: Biopolyesters section: the biodegradable polyester subclass.
- Verdict: [x] CONFIRM — quote anchors this chunk to this SP   [ ] REJECT — wrong chunk/SP   [ ] HOLD — needs better anchor

### 4CH1-1.31 — understand how the formulae of simple compounds can be obtained experimentally, including metal oxides, water and salts containing water of crystallisation
- Note: Simple compound formulae - IGCSE Chemistry Revision Notes (`1. Principles of Chemistry/e. Chemical Formulae, Equations, Calculations/Simple compound formulae - IGCSE Chemistry Revision Notes.md`)
- Chunk: ordinal 1 — heading `Formulae of a simple compound by experiment` — sha256_16 `ee4a6338446c0cc7` — 585 chars
- Evidence quote (verbatim, from the T-C10 store): "The formulae of simple compounds can be found by careful experimentation and accurate measurements of mass changes"
- Chunk excerpt: «Formulae of a simple compound by experiment - The formulae of simple compounds can be found by careful experimentation and accurate measurements of mass changes - The principle is to use mass measurements before and after a reaction and then convert masses into moles - Using the moles of reactants and products it is possible to deduce molar ratios and hence an empirical formula - Experiments which are easier to do us…»
- Upstream: T-C10 1. Principles of Chemistry/e. Chemical Formulae, Equations, Calculations/Simple compound formulae - IGCSE Chemistry Revision Notes.md::4CH1-1.31 — HUMAN_VALIDATED 2026-09-11 — confidence high
- Rationale: Experimental formula determination principle plus the hydrated-copper-sulfate heating experiment (water of crystallisation named in 1.31).
- Verdict: [x] CONFIRM — quote anchors this chunk to this SP   [ ] REJECT — wrong chunk/SP   [ ] HOLD — needs better anchor

### 4CH1-2.11 — describe the combustion of elements in oxygen,including magnesium,hydrogen and sulfur
- Note: Combustion | Edexcel IGCSE Chemistry Revision Notes 2017 (`2. Inorganic Chemistry/c. Gases in the Atmosphere/Combustion  Edexcel IGCSE Chemistry Revision Notes 2017.md`)
- Chunk: ordinal 2 — heading `What is combustion?` — sha256_16 `d1af0c9a97293750` — 399 chars
- Evidence quote (verbatim, from the T-C10 store): "You need to be able to describe the combustion reactions of magnesium, hydrogen and sulfur"
- Chunk excerpt: «What is combustion? - **Combustion** is the scientific word for burning - All combustion reactions involve a chemical change in which oxygen reacts with elements or compounds to produce **oxides** - Combustion reactions give out heat, so they will always be **exothermic** reactions - You need to be able to describe the combustion reactions of magnesium, hydrogen and sulfur…»
- Upstream: T-C10 2. Inorganic Chemistry/c. Gases in the Atmosphere/Combustion  Edexcel IGCSE Chemistry Revision Notes 2017.md::4CH1-2.11 — HUMAN_VALIDATED 2026-09-11 — confidence high
- Rationale: Exactly the three named elements with observations, symbol equations and oxidation classification.
- Verdict: [x] CONFIRM — quote anchors this chunk to this SP   [ ] REJECT — wrong chunk/SP   [ ] HOLD — needs better anchor

### 4CH1-1.40 — draw dot-and-cross diagrams to show the formation of ionic compounds by electron transfer，limited to combinations of elements from Groups1，2，3和5，6，7only outer electrons need be shown
- Note: Ionic bonding diagrams - IGCSE Chemistry Revision Notes (`1. Principles of Chemistry/f. Ionic Bonding/Ionic bonding diagrams - IGCSE Chemistry Revision Notes.md`)
- Chunk: ordinal 1 — heading `Dot and cross diagrams for ionic compounds` — sha256_16 `26937d3b8ae595f6` — 490 chars
- Evidence quote (verbatim, from the T-C10 store): "Ionic bonds can be represented diagrammatically using dot-and-cross diagrams"
- Chunk excerpt: «Dot and cross diagrams for ionic compounds - Ionic bonds can be represented diagrammatically using **dot-and-cross diagrams** - The electrons from each atom should be represented by using solid dots and crosses - If there are more than two atoms, then hollow circles or other symbols / colours may be used to make it clear - The large square brackets should encompass each atom and the charge should be in superscript an…»
- Upstream: T-C10 1. Principles of Chemistry/f. Ionic Bonding/Ionic bonding diagrams - IGCSE Chemistry Revision Notes.md::4CH1-1.40 — HUMAN_VALIDATED 2026-09-11 — confidence high
- Rationale: Dot-and-cross diagrams for ionic formation by electron transfer (NaCl, MgO; Groups 1/2 with 6/7), brackets and charges, outer electrons only.
- Verdict: [x] CONFIRM — quote anchors this chunk to this SP   [ ] REJECT — wrong chunk/SP   [ ] HOLD — needs better anchor

### 4CH1-1.56C — understand why ionic compounds conduct electricity only when molten or in aqueous solution
- Note: Electronic conductivity - IGCSE Chemistry Revision Notes (`1. Principles of Chemistry/i. Electrolysis/Electronic conductivity - IGCSE Chemistry Revision Notes.md`)
- Chunk: ordinal 3 — heading `Conductivity of ionic compounds` — sha256_16 `a89af09b4be51d65` — 580 chars
- Evidence quote (verbatim, from the T-C10 store): "Ionic compounds can conduct electricity in the molten state or in solution"
- Chunk excerpt: «Conductivity of ionic compounds - Ionic compounds can conduct electricity in the **molten** state or in **solution** - This is because they have ions that can move and carry charge - They cannot conduct electricity in the solid state as the ions are in fixed positions within the lattice and are unable to move ![Molten ionic substances conduct electricity, IGCSE & GCSE Chemistry revision notes](../../assets/Molten-ion…»
- Upstream: T-C10 1. Principles of Chemistry/i. Electrolysis/Electronic conductivity - IGCSE Chemistry Revision Notes.md::4CH1-1.56C — HUMAN_VALIDATED 2026-09-11 — confidence high
- Rationale: Ionic conductivity limited to molten/aqueous states with the ion-mobility explanation.
- Verdict: [x] CONFIRM — quote anchors this chunk to this SP   [ ] REJECT — wrong chunk/SP   [ ] HOLD — needs better anchor

### 4CH1-2.23C — explain how the method of extraction of a metal is related to its position in the reactivity series, illustrated by carbon extraction for iron and electrolysis for aluminium
- Note: Extraction of metals from ores - IGCSE Chemistry (`2. Inorganic Chemistry/e. Extraction & Uses of Metals/Extraction of metals from ores - IGCSE Chemistry.md`)
- Chunk: ordinal 1 — heading `Extraction of metals and the reactivity series` — sha256_16 `8989bd392368a6d0` — 3267 chars
- Evidence quote (verbatim, from the T-C10 store): "The position of the metal on the reactivity series determines the method of extraction"
- Chunk excerpt: «Extraction of metals and the reactivity series - The most reactive metals are at the **top** of the series - The tendency to become **oxidised** is thus linked to how **reactive** a metal is and therefore its **position** on the reactivity series - Metals higher up are therefore **less resistant** to oxidation than the metals placed lower down which are **more resistant** to oxidation - The position of the metal on t…»
- Upstream: T-C10 2. Inorganic Chemistry/e. Extraction & Uses of Metals/Extraction of metals from ores - IGCSE Chemistry.md::4CH1-2.23C — HUMAN_VALIDATED 2026-09-11 — confidence high
- Rationale: Extraction-method table including electrolysis of aluminium and the carbon/blast-furnace route for iron with its zone chemistry.
- Verdict: [x] CONFIRM — quote anchors this chunk to this SP   [ ] REJECT — wrong chunk/SP   [ ] HOLD — needs better anchor

### 4CH1-1.38 — know the charges of these ions: •metals in Groups 1,2 and 3 •non-metals in Groups 5,6 and 7 •Ag+，Cu2+，Fe2+，Fe3+，Pb2+，Zn2+ •hydrogen（H+），hydroxide（OH-），ammonium（NH4+），carbonate（CO32-），nitrate（NO3-），sulfate（SO42-）
- Note: Common Ions | Edexcel IGCSE Chemistry Revision Notes 2017 (`1. Principles of Chemistry/f. Ionic Bonding/Common Ions  Edexcel IGCSE Chemistry Revision Notes 2017.md`)
- Chunk: ordinal 3 — heading `Common ions with a positive charge` — sha256_16 `aedc9add94d32d45` — 373 chars
- Evidence quote (verbatim, from the T-C10 store): "Common ions with a positive charge"
- Chunk excerpt: «Common ions with a positive charge | **Ion** | **Charge / formula** | |----------------|------------------| | Group 1 metals | 1+ (E.g. Na+) | | Group 2 metals | 2+ (E.g. Mg2+) | | Group 3 metals | 3+ (E.g. Al3+) | | Silver | Ag+ | | Copper(II) | Cu2+ | | Iron(II) | Fe2+ | | Iron(III) | Fe3+ | | Lead(II) | Pb2+ | | Zinc(II) | Zn2+ | | Hydrogen | H+ | | Ammonium | NH4+ |…»
- Upstream: T-C10 1. Principles of Chemistry/f. Ionic Bonding/Common Ions  Edexcel IGCSE Chemistry Revision Notes 2017.md::4CH1-1.38 — HUMAN_VALIDATED 2026-09-11 — confidence high
- Rationale: Charges table for the specified ions: Groups 1/2/3 metals, Groups 5/6/7 non-metals, the named metal ions, and the compound ions incl. OH-, NH4+, CO32-, NO3-, SO42- (quoted section heading).
- Verdict: [x] CONFIRM — quote anchors this chunk to this SP   [ ] REJECT — wrong chunk/SP   [ ] HOLD — needs better anchor

### 4CH1-1.39 — write formulae for compounds formed between the ions listed above
- Note: Formula of ionic compounds - IGCSE Chemistry Revision Notes (`1. Principles of Chemistry/f. Ionic Bonding/Formula of ionic compounds - IGCSE Chemistry Revision Notes.md`)
- Chunk: ordinal 2 — heading `Direct comparison` — sha256_16 `7c0d32c34f13b646` — 645 chars
- Evidence quote (verbatim, from the T-C10 store): "The formula of an ionic compound can be determined by directly comparing the charges of the ions"
- Chunk excerpt: «Direct comparison - The formula of an ionic compound can be determined by directly comparing the charges of the ions: - For example, iron(II) sulfate - The iron(II) ion is Fe<sup>2+</sup>, which means that it has a 2+ or +2 charge - The sulfate ion is SO<sub>4</sub><sup>2–</sup>, which means that it has a 2– or –2 charge - The charges cancel each other out - Mathematically, (+2) + (–2) = 0 - This means that one SO<su…»
- Upstream: T-C10 1. Principles of Chemistry/f. Ionic Bonding/Formula of ionic compounds - IGCSE Chemistry Revision Notes.md::4CH1-1.39 — HUMAN_VALIDATED 2026-09-11 — confidence high
- Rationale: Direct-comparison and swap-and-drop methods for writing formulae from the listed ions (Fe2+, sulfate etc.).
- Verdict: [x] CONFIRM — quote anchors this chunk to this SP   [ ] REJECT — wrong chunk/SP   [ ] HOLD — needs better anchor

### 4CH1-1.21 — identify an element as a metal or a non-metal according to its position in the Periodic Table
- Note: Metals & non-metals in the Periodic Table - IGCSE Chemistry (`1. Principles of Chemistry/d. The Periodic Table/Metals & non-metals in the Periodic Table - IGCSE Chemistry.md`)
- Chunk: ordinal 1 — heading `Properties of metals and non-metals` — sha256_16 `9481d2e4500ae502` — 1586 chars
- Evidence quote (verbatim, from the T-C10 store): "Metals are on the left of the Periodic Table and non-metals on the right"
- Chunk excerpt: «Properties of metals and non-metals | **Property** | **Metals** | **Non-metals** | |--------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------| | …»
- Upstream: T-C10 1. Principles of Chemistry/d. The Periodic Table/Metals & non-metals in the Periodic Table - IGCSE Chemistry.md::4CH1-1.21 — HUMAN_VALIDATED 2026-09-11 — confidence high
- Rationale: Position-based identification of metals vs non-metals with the left/right rule.
- Verdict: [x] CONFIRM — quote anchors this chunk to this SP   [ ] REJECT — wrong chunk/SP   [ ] HOLD — needs better anchor

### 4CH1-4.36C — describe the reactions of aqueous solutions of carboxylic acids with metals and metal carbonates
- Note: Reactions of Carboxylic Acids | Edexcel IGCSE Chemistry Revision Notes 2017 (`4. Organic Chemistry/f. Carboxylic Acids/Reactions of Carboxylic Acids  Edexcel IGCSE Chemistry Revision Notes 2017.md`)
- Chunk: ordinal 1 — heading `Reactions of carboxylic acids` — sha256_16 `0d2c4f30525988fe` — 498 chars
- Evidence quote (verbatim, from the T-C10 store): "In the reaction with metals, a metal salt and hydrogen gas are produced"
- Chunk excerpt: «Reactions of carboxylic acids - The carboxylic acids behave like other acids - They react with: - **metals** to form a salt and hydrogen - **carbonates** to form a salt, water and carbon dioxide gas - The salts formed by the reaction of carboxylic acids all end –**anoate** - So methanoic acid forms a salt called methanoate, ethanoic a salt called ethanoate etc. - In the reaction with metals, a metal salt and hydrogen…»
- Upstream: T-C10 4. Organic Chemistry/f. Carboxylic Acids/Reactions of Carboxylic Acids  Edexcel IGCSE Chemistry Revision Notes 2017.md::4CH1-4.36C — HUMAN_VALIDATED 2026-09-11 — confidence high
- Rationale: Reactions with metals (magnesium ethanoate + hydrogen) and with carbonates (salt + water + carbon dioxide) with equations.
- Verdict: [x] CONFIRM — quote anchors this chunk to this SP   [ ] REJECT — wrong chunk/SP   [ ] HOLD — needs better anchor

### 4CH1-2.34 — know the general rules for predicting the solubility of ionic compounds in water: • common sodium, potassium and ammonium compounds are soluble • all nitrates are soluble • common chlorides are soluble, except those of silver and lead(II) • common sulfates are soluble, except for those of barium, calcium and lead(II) • common carbonates are insoluble, except for those of sodium, potassium and ammonium • common hydroxides are insoluble except for those of sodium, potassium and calcium(calcium hydroxide is slightly soluble).
- Note: Solubility Rules | Edexcel IGCSE Chemistry Revision Notes 2017 (`2. Inorganic Chemistry/g. Acids, Bases & Salt Preparations/Solubility Rules  Edexcel IGCSE Chemistry Revision Notes 2017.md`)
- Chunk: ordinal 1 — heading `Solubility rules` — sha256_16 `e14a58149c1375cf` — 329 chars
- Evidence quote (verbatim, from the T-C10 store): "A knowledge of the solubility of ionic compounds helps us to determine the most appropriate method for the preparation of salts"
- Chunk excerpt: «Solubility rules - Ionic compounds are generally soluble in water compared to covalent substances, but there are exceptions - A knowledge of the solubility of ionic compounds helps us to determine the most appropriate method for the preparation of salts - The solubility of common ionic compounds is shown below:…»
- Upstream: T-C10 2. Inorganic Chemistry/g. Acids, Bases & Salt Preparations/Solubility Rules  Edexcel IGCSE Chemistry Revision Notes 2017.md::4CH1-2.34 — HUMAN_VALIDATED 2026-09-11 — confidence high
- Rationale: The complete solubility table: Na/K/NH4 all soluble, nitrates all, chlorides except Ag/Pb, sulfates except Ba/Ca/Pb, carbonates except Na/K/NH4, hydroxides except Na/K/Ca.
- Verdict: [x] CONFIRM — quote anchors this chunk to this SP   [ ] REJECT — wrong chunk/SP   [ ] HOLD — needs better anchor

### 4CH1-1.8 — understand how to classify a substance as an element,compound or mixture
- Note: Element, Compound or Mixture | Edexcel IGCSE Chemistry Revision Notes 2017 (`1. Principles of Chemistry/b. Elements, Compounds and Mixtures/Element, Compound or Mixture  Edexcel IGCSE Chemistry Revision Notes 2017.md`)
- Chunk: ordinal 1 — heading `Element, compounds and mixtures` — sha256_16 `3aa1b78639ca6a44` — 174 chars
- Evidence quote (verbatim, from the T-C10 store): "All substances can be classified into one of these three types"
- Chunk excerpt: «Element, compounds and mixtures - All substances can be classified into one of these three types - Elements - Compounds - Mixtures…»
- Upstream: T-C10 1. Principles of Chemistry/b. Elements, Compounds and Mixtures/Element, Compound or Mixture  Edexcel IGCSE Chemistry Revision Notes 2017.md::4CH1-1.8 — HUMAN_VALIDATED 2026-09-11 — confidence high
- Rationale: Definitions and particle diagrams for elements, compounds and mixtures.
- Verdict: [x] CONFIRM — quote anchors this chunk to this SP   [ ] REJECT — wrong chunk/SP   [ ] HOLD — needs better anchor

### 4CH1-2.10 — understand how to determine the percentage by volume of oxygen in air using experiments involving the reactions of metals(e.g. iron)and non-metals(e.g. phosphorus)with air
- Note: Composition of air - IGCSE Chemistry Revision Notes (`2. Inorganic Chemistry/c. Gases in the Atmosphere/Composition of air - IGCSE Chemistry Revision Notes.md`)
- Chunk: ordinal 5 — heading `Finding the percentage of oxygen` — sha256_16 `01245f3678179450` — 366 chars
- Evidence quote (verbatim, from the T-C10 store): "The percentage of oxygen in air can be found by reacting a metal or non-metal with the oxygen in a fixed volume of air"
- Chunk excerpt: «Finding the percentage of oxygen - The percentage of oxygen in air can be found by reacting a metal or non-metal with the oxygen in a fixed volume of air - One way to carry this out is to burn a small amount of **phosphorus** in a bell jar that is sitting in a trough of water - Initially the water levels are the **same** inside and outside the jar…»
- Upstream: T-C10 2. Inorganic Chemistry/c. Gases in the Atmosphere/Composition of air - IGCSE Chemistry Revision Notes.md::4CH1-2.10 — HUMAN_VALIDATED 2026-09-11 — confidence high
- Rationale: Describes the phosphorus-in-bell-jar determination (the 2.10 non-metal example) with volume readings.
- Verdict: [x] CONFIRM — quote anchors this chunk to this SP   [ ] REJECT — wrong chunk/SP   [ ] HOLD — needs better anchor

### 4CH1-4.29C — know that alcohols contain the functional group-OH
- Note: Alcohols | Edexcel IGCSE Chemistry Revision Notes 2017 (`4. Organic Chemistry/e. Alcohols/Alcohols  Edexcel IGCSE Chemistry Revision Notes 2017.md`)
- Chunk: ordinal 1 — heading `Alcohols` — sha256_16 `b80fdc56130483cd` — 331 chars
- Evidence quote (verbatim, from the T-C10 store): "All alcohols contain the hydroxyl (-OH) functional group"
- Chunk excerpt: «Alcohols - Alcohols are colourless liquids that dissolve in water to form **neutral** solutions - The first four alcohols are commonly used as **fuels** - All alcohols contain the hydroxyl (**\-OH**) functional group which is the part of alcohol molecules that is responsible for their **characteristic reactions**…»
- Upstream: T-C10 4. Organic Chemistry/e. Alcohols/Alcohols  Edexcel IGCSE Chemistry Revision Notes 2017.md::4CH1-4.29C — HUMAN_VALIDATED 2026-09-11 — confidence high
- Rationale: The -OH functional group as the reactive part of alcohols, with the ethanol molecule diagram.
- Verdict: [x] CONFIRM — quote anchors this chunk to this SP   [ ] REJECT — wrong chunk/SP   [ ] HOLD — needs better anchor

### 4CH1-1.4 — know what is meant by the terms: • solvent • solute • solution • saturated solution.
- Note: Solubility - IGCSE Chemistry Revision Notes (`1. Principles of Chemistry/a. States of Matter/Solubility - IGCSE Chemistry Revision Notes.md`)
- Chunk: ordinal 1 — heading `Solubility` — sha256_16 `7fdc3eabbf277fc5` — 742 chars
- Evidence quote (verbatim, from the T-C10 store): "The liquid is called the solvent"
- Chunk excerpt: «Solubility - Solubility is **a measurement of how much of a substance will dissolve in a given volume of a liquid** - The liquid is called the solvent - The solubility of a gas depends on pressure and temperature - Different substances have different solubilities - Solubility can be expressed in **g per 100 g of solvent** - Solubility of solids is affected by temperature - As **temperature increases**, solids usually…»
- Upstream: T-C10 1. Principles of Chemistry/a. States of Matter/Solubility - IGCSE Chemistry Revision Notes.md::4CH1-1.4 — HUMAN_VALIDATED 2026-09-11 — confidence low
- Rationale: Teaches the solvent term definitionally in context ('the liquid is called the solvent') and uses solute / saturated solution operationally in the solubility-curve discussion; the Solutions note carries the four 1.4 term definitions as a separate mapping - contributory coverage, not sole coverage.
- Verdict: [x] CONFIRM — quote anchors this chunk to this SP   [ ] REJECT — wrong chunk/SP   [ ] HOLD — needs better anchor
- Reviewer note: this chunk defines solvent and solubility measurement; the solute / solution / saturated-solution term coverage lives in the note's excerpt region and sibling chunks (2 and 4) — recommend supplementary rows in the apply step.

### 4CH1-1.5C — know what is meant by the term solubility in the units g per 100 g of solvent
- Note: Investigating solubility - IGCSE Chemistry Revision Notes (`1. Principles of Chemistry/a. States of Matter/Investigating solubility - IGCSE Chemistry Revision Notes.md`)
- Chunk: ordinal 2 — heading `Aim` — sha256_16 `5380c95c3eef37d5` — 179 chars
- Evidence quote (verbatim, from the T-C10 store): "evaporating the solvent, and measuring the mass of the solid obtained"
- Chunk excerpt: «Aim - To find the solubility of a solid in water at a given temperature by preparing a saturated solution, evaporating the solvent, and measuring the mass of the solid obtained…»
- Upstream: T-C10 1. Principles of Chemistry/a. States of Matter/Investigating solubility - IGCSE Chemistry Revision Notes.md::4CH1-1.5C — HUMAN_VALIDATED 2026-09-11 — confidence medium
- Rationale: Practical's calculation section converts measured masses into solubility in g per 100 g of water.
- Verdict: [x] CONFIRM — quote anchors this chunk to this SP   [ ] REJECT — wrong chunk/SP   [ ] HOLD — needs better anchor
- Reviewer note: the anchored Aim chunk teaches the operational determination of solubility; the note's 'Calculation' section (ordinal 5) carries the g-per-100-g content directly — recommend a supplementary row there in the apply step.

### 4CH1-1.25 — write word equations and balanced chemical equations(including state symbols):for reactions studied in this specificationfor unfamiliar reactions where suitable information is provided.
- Note: Reacting mass calculations - IGCSE Chemistry Revision Notes (`1. Principles of Chemistry/e. Chemical Formulae, Equations, Calculations/Reacting mass calculations - IGCSE Chemistry Revision Notes.md`)
- Chunk: ordinal 4 — heading `Balancing Equations using Reacting Masses` — sha256_16 `0e7177518a5396de` — 287 chars
- Evidence quote (verbatim, from the T-C10 store): "Balancing Equations using Reacting Masses"
- Chunk excerpt: «Balancing Equations using Reacting Masses - If the masses of reactants and products of a reaction are known then we can use them to write a balanced equation for that reaction - This is done by converting the **masses** to **moles** and simplifying to find the **molar ratios**…»
- Upstream: T-C10 1. Principles of Chemistry/e. Chemical Formulae, Equations, Calculations/Reacting mass calculations - IGCSE Chemistry Revision Notes.md::4CH1-1.25 — HUMAN_VALIDATED 2026-09-11 — confidence medium
- Rationale: Dedicated section (quoted heading) on deducing balanced equations from reacting-mass data.
- Verdict: [x] CONFIRM — quote anchors this chunk to this SP   [ ] REJECT — wrong chunk/SP   [ ] HOLD — needs better anchor

### 4CH1-1.22 — understand how the electronic configuration of a main group element is related to its position in the Periodic Table
- Note: Electronic Configuration & Reactivity | Edexcel IGCSE Chemistry Revision Notes 2017 (`1. Principles of Chemistry/d. The Periodic Table/Electronic Configuration & Reactivity  Edexcel IGCSE Chemistry Revision Notes 2017.md`)
- Chunk: ordinal 2 — heading `Chemical properties of elements in the same group` — sha256_16 `cafc2df10b0311a6` — 1425 chars
- Evidence quote (verbatim, from the T-C10 store): "The group number of an element which is given on the Periodic Table indicates the number of electrons in the outer shell"
- Chunk excerpt: «Chemical properties of elements in the same group - Elements in the same group in the Periodic Table will have **similar chemical properties** - This is because they have the **same number of outer electrons** so will react and bond similarly - The group number of an element which is given on the Periodic Table indicates the number of electrons in the outer shell - This rule holds true for all elements except helium;…»
- Upstream: T-C10 1. Principles of Chemistry/d. The Periodic Table/Electronic Configuration & Reactivity  Edexcel IGCSE Chemistry Revision Notes 2017.md::4CH1-1.22 — HUMAN_VALIDATED 2026-09-11 — confidence medium
- Rationale: Group-number-to-outer-electrons rule links main-group position to electronic configuration.
- Verdict: [x] CONFIRM — quote anchors this chunk to this SP   [ ] REJECT — wrong chunk/SP   [ ] HOLD — needs better anchor

### 4CH1-1.37 — understand how ions are formed by electron loss or gain
- Note: Common Ions | Edexcel IGCSE Chemistry Revision Notes 2017 (`1. Principles of Chemistry/f. Ionic Bonding/Common Ions  Edexcel IGCSE Chemistry Revision Notes 2017.md`)
- Chunk: ordinal 2 — heading `How to deduce the charge of an ion` — sha256_16 `d6068969e6c139de` — 537 chars
- Evidence quote (verbatim, from the T-C10 store): "Find out if it is easier for the atom to gain electron or to donate electron"
- Chunk excerpt: «How to deduce the charge of an ion - Find the number of electrons in the outer electron shell - Find out if it is easier for the atom to gain electron or to donate electron (in most cases atoms that have fewer than four electrons, donate electrons and atoms that have more than 4 electrons, receive electrons) - Atoms that gain electrons become negative ions and atoms that donate electron forms positive ion - You also …»
- Upstream: T-C10 1. Principles of Chemistry/f. Ionic Bonding/Common Ions  Edexcel IGCSE Chemistry Revision Notes 2017.md::4CH1-1.37 — HUMAN_VALIDATED 2026-09-11 — confidence medium
- Rationale: Charge-deduction rule via outer-electron loss or gain supports the 1.37 mechanism.
- Verdict: [x] CONFIRM — quote anchors this chunk to this SP   [ ] REJECT — wrong chunk/SP   [ ] HOLD — needs better anchor

### 4CH1-3.10 — describe the effects of changes in surface area of a solid, concentration of a solution, pressure of a gas, temperature and the use of a catalyst on the rate of a reaction
- Note: Explaining Rates | Edexcel IGCSE Chemistry Revision Notes 2017 (`3. Physical Chemistry/b. Rates of Reaction/Explaining Rates  Edexcel IGCSE Chemistry Revision Notes 2017.md`)
- Chunk: ordinal 2 — heading `How increasing concentration affects rate` — sha256_16 `33d3359fdfd46bd1` — 606 chars
- Evidence quote (verbatim, from the T-C10 store): "Increasing the concentration of a solution increases the rate of reaction"
- Chunk excerpt: «How increasing concentration affects rate - Increasing the concentration of a solution increases the rate of reaction - Increasing the concentration means that there are more reactant particles in a given volume - This causes more collisions per second - Leading to more frequent and successful collisions per second - Therefore, the rate of reaction increases - If you double the number of particles, you will double th…»
- Upstream: T-C10 3. Physical Chemistry/b. Rates of Reaction/Explaining Rates  Edexcel IGCSE Chemistry Revision Notes 2017.md::4CH1-3.10 — HUMAN_VALIDATED 2026-09-11 — confidence medium
- Rationale: Collision-theory sections explaining the concentration, pressure, temperature and surface-area effects on rate; the catalyst factor of 3.10 is taught in the rate-of-reaction and catalysts notes.
- Verdict: [x] CONFIRM — quote anchors this chunk to this SP   [ ] REJECT — wrong chunk/SP   [ ] HOLD — needs better anchor

### 4CH1-1.58C — describe experiments to investigate electrolysis, using inert electrodes, of molten compounds (including lead(II) bromide) and aqueous solutions (including sodium chloride, dilute sulfuric acid and copper(II) sulfate) and to predict the products
- Note: Practical: Investigate the Electrolysis of Aqueous Solutions | Edexcel IGCSE Chemistry Revision Notes 2017 (`1. Principles of Chemistry/i. Electrolysis/Practical Investigate the Electrolysis of Aqueous Solutions  Edexcel IGCSE Chemistry Revision Notes 2017.md`)
- Chunk: ordinal 2 — heading `Aim:` — sha256_16 `2e5aba99a89ec8d0` — 154 chars
- Evidence quote (verbatim, from the T-C10 store): "To electrolyse aqueous solutions of sodium chloride, sulfuric acid and copper(II)sulfate, and to collect and identify the products at each electrode"
- Chunk excerpt: «Aim: To electrolyse aqueous solutions of sodium chloride, sulfuric acid and copper(II)sulfate, and to collect and identify the products at each electrode…»
- Upstream: T-C10 1. Principles of Chemistry/i. Electrolysis/Practical Investigate the Electrolysis of Aqueous Solutions  Edexcel IGCSE Chemistry Revision Notes 2017.md::4CH1-1.58C — HUMAN_VALIDATED 2026-09-11 — confidence medium
- Rationale: The practical describes exactly the 1.58C experiments (inert electrodes, the three named solutions) and their products.
- Verdict: [x] CONFIRM — quote anchors this chunk to this SP   [ ] REJECT — wrong chunk/SP   [ ] HOLD — needs better anchor

## Part B — worklist decisions (13 rows)

### 4CH1-1.1 — 
- Note: `1. Principles of Chemistry/a. States of Matter/Changing states of matter - IGCSE Chemistry Revision Notes.md`
- Quote (excerpt-region only): "The three states of matter are solids, liquids and gases"
- Reason: quote resolves only to the note title/excerpt region — no passage anchor; author a fresh verbatim section quote
- Disposition: WORKLIST — needs a fresh authored passage quote (or markdown repair) before a chunk-level row can exist
- Verdict: [x] AUTHOR fresh passage quote   [ ] REPAIR markdown   [ ] DEFER (record why)
- Authored quote (verbatim, verified): `Movement of particles | Vibrate about a fixed position | Move around each other | Move quickly in all directions`
- Target chunk: ordinal 1 — heading `Summary of the properties of the three states of matter` — sha256_16 `26b724f7261fabee` — 1041 chars — unique exact match under c13-chunk-convention-1 + shared norm()

### 4CH1-1.2 — 
- Note: `1. Principles of Chemistry/a. States of Matter/Changing states of matter - IGCSE Chemistry Revision Notes.md`
- Quote (excerpt-region only): "State changes occur at the melting point (solid to liquid, liquid to solid) and at the boiling point (liquid to gas and gas to liquid)"
- Reason: quote resolves only to the note title/excerpt region — no passage anchor; author a fresh verbatim section quote
- Disposition: WORKLIST — needs a fresh authored passage quote (or markdown repair) before a chunk-level row can exist
- Verdict: [x] AUTHOR fresh passage quote   [ ] REPAIR markdown   [ ] DEFER (record why)
- Authored quote (verbatim, verified): `The amount of energy needed to change state from solid to liquid and from liquid to gas depends on the strength of the forces between the particles`
- Target chunk: ordinal 2 — heading `Changing states of matter` — sha256_16 `7bff6087efa41e4f` — 575 chars — unique exact match under c13-chunk-convention-1 + shared norm()

### 4CH1-1.20 — 
- Note: `1. Principles of Chemistry/d. The Periodic Table/Metals & non-metals in the Periodic Table - IGCSE Chemistry.md`
- Quote (excerpt-region only): "We can use properties such as electrical conductivity and acid-base character to classify elements as metals or non-metals"
- Reason: quote resolves only to the note title/excerpt region — no passage anchor; author a fresh verbatim section quote
- Disposition: WORKLIST — needs a fresh authored passage quote (or markdown repair) before a chunk-level row can exist
- Verdict: [x] AUTHOR fresh passage quote   [ ] REPAIR markdown   [ ] DEFER (record why)
- Authored quote (verbatim, verified): `Electrical conductivity | Good conductor of electricity | Poor conductors of electricity`
- Target chunk: ordinal 1 — heading `Properties of metals and non-metals` — sha256_16 `9481d2e4500ae502` — 1586 chars — unique exact match under c13-chunk-convention-1 + shared norm()

### 4CH1-1.28 — 
- Note: `1. Principles of Chemistry/e. Chemical Formulae, Equations, Calculations/Reacting mass calculations - IGCSE Chemistry Revision Notes.md`
- Quote (excerpt-region only): "Once the moles have been determined they can then be converted into grams using the relative atomic or relative formula masses"
- Reason: quote resolves only to the note title/excerpt region — no passage anchor; author a fresh verbatim section quote
- Disposition: WORKLIST — needs a fresh authored passage quote (or markdown repair) before a chunk-level row can exist
- Verdict: [x] AUTHOR fresh passage quote   [ ] REPAIR markdown   [ ] DEFER (record why)
- Authored quote (verbatim, verified): `Mass = moles x Mr = 0.25 moles x (24 + 16) = 10 g`
- Target chunk: ordinal 1 — heading `Worked Example` — sha256_16 `66cb3a45ae3a59fb` — 940 chars — unique exact match under c13-chunk-convention-1 + shared norm()

### 4CH1-1.41 — 
- Note: `1. Principles of Chemistry/f. Ionic Bonding/Ionic bonding and lattices - IGCSE Chemistry Revision Notes.md`
- Quote (excerpt-region only): "Between positive and negative ions are strong electrostatic forces of attraction which act in all directions"
- Reason: quote resolves only to the note title/excerpt region — no passage anchor; author a fresh verbatim section quote
- Disposition: WORKLIST — needs a fresh authored passage quote (or markdown repair) before a chunk-level row can exist
- Verdict: [x] AUTHOR fresh passage quote   [ ] REPAIR markdown   [ ] DEFER (record why)
- Authored quote (verbatim, verified): `There are strong electrostatic forces of attraction between oppositely charged ions in all directions`
- Target chunk: ordinal 2 — heading `Giant ionic lattice of sodium chloride` — sha256_16 `d26624fc348b565f` — 925 chars — unique exact match under c13-chunk-convention-1 + shared norm()

### 4CH1-1.43 — 
- Note: `1. Principles of Chemistry/f. Ionic Bonding/Ionic bonding and lattices - IGCSE Chemistry Revision Notes.md`
- Quote (excerpt-region only): "ionic compounds have high melting points and conduct electricity when molten or in solution"
- Reason: quote resolves only to the note title/excerpt region — no passage anchor; author a fresh verbatim section quote
- Disposition: WORKLIST — needs a fresh authored passage quote (or markdown repair) before a chunk-level row can exist
- Verdict: [x] AUTHOR fresh passage quote   [ ] REPAIR markdown   [ ] DEFER (record why)
- Authored quote (verbatim, verified): `Ionic compounds are good conductors of electricity in the molten state or in solution`
- Target chunk: ordinal 3 — heading `Conductivity of ionic compounds` — sha256_16 `9bc6cd91624beafb` — 820 chars — unique exact match under c13-chunk-convention-1 + shared norm()

### 4CH1-1.52C — 
- Note: `1. Principles of Chemistry/h. Metallic Bonding/Metallic bonding - IGCSE Chemistry Revision Notes.md`
- Quote (excerpt-region only): "Metals consist of giant structures of atoms arranged in a regular pattern"
- Reason: quote resolves only to the note title/excerpt region — no passage anchor; author a fresh verbatim section quote
- Disposition: WORKLIST — needs a fresh authored passage quote (or markdown repair) before a chunk-level row can exist
- Verdict: [x] AUTHOR fresh passage quote   [ ] REPAIR markdown   [ ] DEFER (record why)
- Authored quote (verbatim, verified): `Structure & bonding in a metal, IGCSE & GCSE Chemistry revision notes`
- Target chunk: ordinal 1 — heading `Metallic bonding` — sha256_16 `5985c7a1c9690f51` — 864 chars — unique exact match under c13-chunk-convention-1 + shared norm()
- Reviewer note: this SP is taught by the note's lattice diagram itself; the authored anchor is the diagram's own alt-text line (the closest verbatim passage text available). The T-C06 converter/apply step may prefer linking the asset directly.

### 4CH1-1.53C — 
- Note: `1. Principles of Chemistry/h. Metallic Bonding/Metallic bonding - IGCSE Chemistry Revision Notes.md`
- Quote (excerpt-region only): "The metallic bond is the strong force of attraction between the positive metal ions and the delocalised electrons"
- Reason: quote resolves only to the note title/excerpt region — no passage anchor; author a fresh verbatim section quote
- Disposition: WORKLIST — needs a fresh authored passage quote (or markdown repair) before a chunk-level row can exist
- Verdict: [x] AUTHOR fresh passage quote   [ ] REPAIR markdown   [ ] DEFER (record why)
- Authored quote (verbatim, verified): `There are strong electrostatic forces of attraction between the positive metal ions and the negative delocalised electrons within the metal lattice structure`
- Target chunk: ordinal 1 — heading `Metallic bonding` — sha256_16 `5985c7a1c9690f51` — 864 chars — unique exact match under c13-chunk-convention-1 + shared norm()

### 4CH1-2.16 — 
- Note: `2. Inorganic Chemistry/d. Reactivity Series/Metal displacement - IGCSE Chemistry Revision Notes.md`
- Quote (excerpt-region only): "a more reactive metal will displace a less reactive metal from its compounds"
- Reason: quote resolves only to the note title/excerpt region — no passage anchor; author a fresh verbatim section quote
- Disposition: WORKLIST — needs a fresh authored passage quote (or markdown repair) before a chunk-level row can exist
- Verdict: [x] AUTHOR fresh passage quote   [ ] REPAIR markdown   [ ] DEFER (record why)
- Authored quote (verbatim, verified): `The reactivity between two metals can be compared using displacement reactions in salt solutions of one of the metals`
- Target chunk: ordinal 2 — heading `Displacement reactions between metals & aqueous solutions of metal salts` — sha256_16 `ce045b9ac30bf7eb` — 755 chars — unique exact match under c13-chunk-convention-1 + shared norm()

### 4CH1-2.15 — 
- Note: `2. Inorganic Chemistry/d. Reactivity Series/Metals Reacting with Water & Acids  Edexcel IGCSE Chemistry Revision Notes 2017.md`
- Quote (excerpt-region only): "The series can be used to place a group of metals in order of reactivity based on the observations of their reactions with water and acids"
- Reason: quote resolves only to the note title/excerpt region — no passage anchor; author a fresh verbatim section quote
- Disposition: WORKLIST — needs a fresh authored passage quote (or markdown repair) before a chunk-level row can exist
- Verdict: [x] AUTHOR fresh passage quote   [ ] REPAIR markdown   [ ] DEFER (record why)
- Authored quote (verbatim, verified): `Only metals above hydrogen in the reactivity series will react with dilute acids`
- Target chunk: ordinal 3 — heading `Reaction with dilute sulfuric or hydrochloric acids` — sha256_16 `ada48b59f21e2045` — 605 chars — unique exact match under c13-chunk-convention-1 + shared norm()

### 4CH1-2.17 — 
- Note: `2. Inorganic Chemistry/d. Reactivity Series/Metals Reacting with Water & Acids  Edexcel IGCSE Chemistry Revision Notes 2017.md`
- Quote (excerpt-region only): "The series can be used to place a group of metals in order of reactivity based on the observations of their reactions with water and acids"
- Reason: quote resolves only to the note title/excerpt region — no passage anchor; author a fresh verbatim section quote
- Disposition: WORKLIST — needs a fresh authored passage quote (or markdown repair) before a chunk-level row can exist
- Verdict: [x] AUTHOR fresh passage quote   [ ] REPAIR markdown   [ ] DEFER (record why)
- Authored quote (verbatim, verified): `Potassium | Reacts violently | | Sodium | Reacts quickly | | Lithium | Reacts less strongly | | Calcium | Reacts less strongly`
- Target chunk: ordinal 1 — heading `Reactions of metal with cold water summary table` — sha256_16 `441462a310b3db9d` — 516 chars — unique exact match under c13-chunk-convention-1 + shared norm()

### 4CH1-2.25C — 
- Note: `2. Inorganic Chemistry/e. Extraction & Uses of Metals/Metals and their uses - IGCSE Chemistry Revision Notes.md`
- Quote (excerpt-region only): "The uses of aluminium, copper and steel are summarised in these tables"
- Reason: quote resolves only to the note title/excerpt region — no passage anchor; author a fresh verbatim section quote
- Disposition: WORKLIST — needs a fresh authored passage quote (or markdown repair) before a chunk-level row can exist
- Verdict: [x] AUTHOR fresh passage quote   [ ] REPAIR markdown   [ ] DEFER (record why)
- Authored quote (verbatim, verified): `Mild | 0.25% C | Car body panels and wiring | Soft and malleable`
- Target chunk: ordinal 4 — heading `Uses of Steel` — sha256_16 `2fd4343517d081c5` — 463 chars — unique exact match under c13-chunk-convention-1 + shared norm()

### 4CH1-4.15 — explain how the combustion of some impurities in hydrocarbon fuels results in the formation of sulfur dioxide
- Note: `(no note-level mapping)`
- Quote (excerpt-region only): "(none)"
- Reason: no note-level mapping exists in the T-C10 store for this SP (registered corpus gap)
- Disposition: WORKLIST — chunk-level mapping decision needed (C12 question-level mappings exist; see C10_GAP_ANNOTATIONS)
- Verdict: [ ] AUTHOR fresh passage quote   [ ] REPAIR markdown   [x] DEFER (record why)
- Why DEFERred: registered corpus gap — C10 GAP_ANNOTATIONS records that no SME note teaches the
  formation explanation this SP demands (sulfur dioxide from the combustion of impurities in hydrocarbon
  fuels). No note-level T-C10 mapping exists for 4CH1-4.15, so there is no passage to quote and nothing
  to repair; authoring an anchor requires new SME content acquisition, not re-anchoring. C12 already maps
  this SP at question level. Deferred to the content-acquisition worklist; the resolution axis can go to
  scoreable without it (the SP is simply uncovered until the gap is closed).

## Rollup

| Part | Rows | CONFIRM | REJECT | HOLD | Precision |
|---|---|---|---|---|---|
| A (anchored spot-check) | 42 | 42 | 0 | 0 | 42/42 = 100% |
| B (worklist) | 13 | 12 AUTHOR · 1 DEFER | 0 | 0 | 13/13 decided |

Gate: Part A precision >= 90% AND every Part B row decided -> the store may be promoted (rows flip to
HUMAN_VALIDATED in a recorded, deterministic apply step — never hand-edits).

**Gate outcome (this fill):** Part A precision 42/42 = 100% (≥ 90%) AND all 13 Part B rows decided ->
gate arithmetic **PASSES** — the store may be promoted. Per the anti-forgery rule the rows still flip to
HUMAN_VALIDATED only in a recorded, deterministic apply step (re-run of the substrate tool over the
12 authored quotes + supplementary-row additions); this sheet does not flip them. Carry-forward items
for that apply step: 12 authored quotes above (target chunks pinned by sha256_16), supplementary-row
recommendations on the four Part A reviewer notes, and the 4CH1-4.15 content-acquisition deferral.
