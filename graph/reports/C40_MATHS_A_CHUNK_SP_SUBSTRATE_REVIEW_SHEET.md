# C40 — maths-a Chunk→SP Substrate OPERATOR REVIEW SHEET (the promotion gate)

**Seed:** `1f03f59be0a5f22e` (sha256 of the emitted rows — deterministic regeneration) ·
**Rows:** 468 anchored spot-checks + 79 worklist decisions.
**Rule:** this sheet is the ONLY path from SUGGESTED to HUMAN_VALIDATED for the
chunk→SP substrate. Per-class rollup: any confirmed-precision < 90% on the sampled
rows → rework that class before promotion.
**Sampling:** all ambiguous rows (the span-marker construction has none by design)
+ seeded stratified anchored sample — low-assurance strata (join score <1.0 or
absent) at 100%, score == 1.0 at ceil(20%) — + every worklist row.
**Anti-forgery reminder:** the tool cannot emit HUMAN_VALIDATED rows (gate G5);
only the verdicts recorded here — applied in a recorded deterministic apply step —
can. The upstream join is AI_VALIDATED (operator-delegated chain); the tier
difference to chemistry's T-C10-backed substrate is intentional and recorded.

## Part A — anchored-row spot-check (468 rows)

### 4MA1-3.3F — calculate the gradient of a straight line given the coordinates of two points
- Note: Drawing Straight Line Graphs (`notes/3-sequences-functions-and-graphs/linear-graphs-y-equals-mx-plus-c/drawing-straight-line-graphs.json`)
- Chunk: ordinal 1 — heading `How do I draw a straight line from a table of values?` — sha256_16 `e651a6d268713c4f` — 502 chars
- Evidence quote (verbatim self-slice, markdown-safe): "How do I draw a straight line from a table of values?
- You may be given a** table of values** with **no** equation
- Use the *x *and *y* values to form a point with **coordinates **(*x*, *y*)

  - Then** plot** these points
  - Use a ruler"
- Chunk excerpt: «How do I draw a straight line from a table of values? - You may be given a** table of values** with **no** equation - Use the *x *and *y* values to form a point with **coordinates **(*x*, *y*) - Then** plot** these points - Use a ruler to draw a **straight line** through them - All points should lie on the line - For example - The points below are (-3, 0), (-2, 2), ... etc | $x$ | -3 | -2 | -1 | 0 | 1 | 2 | 3 | |---|»
- Upstream: T-C32 join notes/3-sequences-functions-and-graphs/linear-graphs-y-equals-mx-plus-c/drawing-straight-line-graphs.json::spcpt_h8QyRmzX5mCJb3X9 — tier P1_name_fragment_join — score 1.0 — wording EXACT — validation tier AI_VALIDATED (operator-delegated chain)
- Rationale: SME span 'Drawing Linear Graphs' on note 'Drawing Straight Line Graphs' is anchored by the corpus spec_point block spcpt_h8QyRmzX5mCJb3X9 and joined to 4MA1-3.3F via operator-verdict name-fragment join (T-SPEC-7; PMT excluded as source); this section chunk sits inside that span.
- Verdict: [ ] CONFIRM — this chunk belongs to this SP   [ ] REJECT — wrong chunk/SP   [ ] HOLD — needs rework

### 4MA1-1.8B — round to a given number of significant figures or decimal places
- Note: Rounding & Estimation (`notes/1-numbers-and-the-number-system/rounding-estimation-and-bounds/rounding-and-estimation.json`)
- Chunk: ordinal 1 — heading `How do I round a number to a given place value?` — sha256_16 `4deee5e6c4e703c0` — 476 chars
- Evidence quote (verbatim self-slice, markdown-safe): "How do I round a number to a given place value?
- Identify the **digit** in the **required place value**
- **Circle the number to the right** of the required place value

  - If the circled number is **5 or more** then you round to the **bi"
- Chunk excerpt: «How do I round a number to a given place value? - Identify the **digit** in the **required place value** - **Circle the number to the right** of the required place value - If the circled number is **5 or more** then you round to the **bigger number** - If the circled number is **less than 5** then you round to the **smaller number** - Put a **zero** in any** following place values before the decimal point** - E.g. 15»
- Upstream: T-C32 join notes/1-numbers-and-the-number-system/rounding-estimation-and-bounds/rounding-and-estimation.json::spcpt_p8zkdCF8QVvDZyVX — tier P2_page_context_join — score 1.0 — wording EXACT — validation tier AI_VALIDATED (operator-delegated chain)
- Rationale: SME span 'Rounding & Estimation' on note 'Rounding & Estimation' is anchored by the corpus spec_point block spcpt_p8zkdCF8QVvDZyVX and joined to 4MA1-1.8B via operator-verdict page-context join (T-SPEC-7; PMT excluded as source); this section chunk sits inside that span.
- Verdict: [ ] CONFIRM — this chunk belongs to this SP   [ ] REJECT — wrong chunk/SP   [ ] HOLD — needs rework

### 4MA1-4.8B — understand and use angles of elevation and depression
- Note: SOHCAHTOA (`notes/4-geometry-and-trigonometry/right-angled-triangles---pythagoras-and-trigonometry/right-angled-trigonometry.json`)
- Chunk: ordinal 6 — heading `How do I find the shortest distance from a point to a line?` — sha256_16 `ba9e0bd780034c7f` — 2151 chars
- Evidence quote (verbatim self-slice, markdown-safe): "How do I find the shortest distance from a point to a line?
- The shortest distance from any point to a line will always be the **perpendicular** distance
- Form a right-angled triangle and then use SOHCAHTOA to find the relevant distance
E"
- Chunk excerpt: «How do I find the shortest distance from a point to a line? - The shortest distance from any point to a line will always be the **perpendicular** distance - Form a right-angled triangle and then use SOHCAHTOA to find the relevant distance Exam Hint: SOHCAHTOA (like Pythagoras) can only be used in **right-angled triangles.** Exam Hint: Ensure your calculator is set to measure angles in **degrees.** You should see the »
- Upstream: T-C32 join notes/4-geometry-and-trigonometry/right-angled-triangles---pythagoras-and-trigonometry/right-angled-trigonometry.json::spcpt_h2SHkwgcS67NJYVP — tier P1_name_fragment_join — score 1.0 — wording EXACT — validation tier AI_VALIDATED (operator-delegated chain)
- Rationale: SME span 'SOHCAHTOA' on note 'SOHCAHTOA' is anchored by the corpus spec_point block spcpt_h2SHkwgcS67NJYVP and joined to 4MA1-4.8B via operator-verdict name-fragment join (T-SPEC-7; PMT excluded as source); this section chunk sits inside that span.
- Verdict: [ ] CONFIRM — this chunk belongs to this SP   [ ] REJECT — wrong chunk/SP   [ ] HOLD — needs rework

### 4MA1-4.9C — find the area of simple shapes using the formulae for the areas of triangles and rectangles
- Note: Adding & Subtracting Areas (`notes/4-geometry-and-trigonometry/area-and-perimeter/adding-and-subtracting-areas.json`)
- Chunk: ordinal 0 — heading `Adding & subtracting areas` — sha256_16 `c7045d0c3968f8df` — 26 chars
- Evidence quote (verbatim self-slice, markdown-safe): "Adding & subtracting areas"
- Chunk excerpt: «Adding & subtracting areas»
- Upstream: T-C32 join notes/4-geometry-and-trigonometry/area-and-perimeter/adding-and-subtracting-areas.json::spcpt_2NQRqtzTGgzNksfC — tier P2_page_context_join — score 1.0 — wording EXACT — validation tier AI_VALIDATED (operator-delegated chain)
- Rationale: SME span 'Adding & Subtracting Areas' on note 'Adding & Subtracting Areas' is anchored by the corpus spec_point block spcpt_2NQRqtzTGgzNksfC and joined to 4MA1-4.9C via operator-verdict page-context join (T-SPEC-7; PMT excluded as source); this section chunk sits inside that span.
- Verdict: [ ] CONFIRM — this chunk belongs to this SP   [ ] REJECT — wrong chunk/SP   [ ] HOLD — needs rework

### 4MA1-4.5C — solve problems using scale drawings
- Note: Using a Calculator (`notes/1-numbers-and-the-number-system/using-a-calculator/using-a-calculator.json`)
- Chunk: ordinal 2 — heading `How do I make sure that I have the correct settings on the calculator?` — sha256_16 `c4a6efdb624f42b9` — 935 chars
- Evidence quote (verbatim self-slice, markdown-safe): "How do I make sure that I have the correct settings on the calculator?
- Check you know how change the **mode** of your calculator

  - There is usually a button marked 'MODE'
  - Most calculators default to 'MATH' mode with the word MATH w"
- Chunk excerpt: «How do I make sure that I have the correct settings on the calculator? - Check you know how change the **mode** of your calculator - There is usually a button marked 'MODE' - Most calculators default to 'MATH' mode with the word MATH written across the top of the display or using a symbol - The '**Angle Unit'** needs to be **degrees** - There is usually a button marked 'SETUP' where you can find the angle unit option»
- Upstream: T-C32 join notes/1-numbers-and-the-number-system/using-a-calculator/using-a-calculator.json::spcpt_xf7Y5cxcQG3T6g65 — tier P1_name_fragment_join — score 1.0 — wording EXACT — validation tier AI_VALIDATED (operator-delegated chain)
- Rationale: SME span 'Using a Calculator' on note 'Using a Calculator' is anchored by the corpus spec_point block spcpt_xf7Y5cxcQG3T6g65 and joined to 4MA1-4.5C via operator-verdict name-fragment join (T-SPEC-7; PMT excluded as source); this section chunk sits inside that span.
- Verdict: [ ] CONFIRM — this chunk belongs to this SP   [ ] REJECT — wrong chunk/SP   [ ] HOLD — needs rework

### 4MA1-1.5E — use Venn diagrams to represent sets
- Note: Probabilities from Venn Diagrams (`notes/6-statistics-and-probability/probability-diagrams---venn-and-tree-diagrams/probability-and-venn-diagrams.json`)
- Chunk: ordinal 0 — heading `Probability & Venn diagrams` — sha256_16 `cb9e97a823d5772b` — 27 chars
- Evidence quote (verbatim self-slice, markdown-safe): "Probability & Venn diagrams"
- Chunk excerpt: «Probability & Venn diagrams»
- Upstream: T-C32 join notes/6-statistics-and-probability/probability-diagrams---venn-and-tree-diagrams/probability-and-venn-diagrams.json::spcpt_Rv3DcsGBkxSkb8Ms — tier P1_name_fragment_join — score 1.0 — wording EXACT — validation tier AI_VALIDATED (operator-delegated chain)
- Rationale: SME span 'Probability & Venn Diagrams' on note 'Probabilities from Venn Diagrams' is anchored by the corpus spec_point block spcpt_Rv3DcsGBkxSkb8Ms and joined to 4MA1-1.5E via operator-verdict name-fragment join (T-SPEC-7; PMT excluded as source); this section chunk sits inside that span.
- Verdict: [ ] CONFIRM — this chunk belongs to this SP   [ ] REJECT — wrong chunk/SP   [ ] HOLD — needs rework

### 4MA1-1.6E — solve simple percentage problems, including percentage increase and decrease
- Note: Percentage Increases & Decreases (`notes/1-numbers-and-the-number-system/percentages/percentage-increases-and-decreases.json`)
- Chunk: ordinal 2 — heading `How do I decrease by a percentage?` — sha256_16 `eee0501d480e76bd` — 1262 chars
- Evidence quote (verbatim self-slice, markdown-safe): "How do I decrease by a percentage?
- A percentage **decrease **makes an amount **smaller** by **subtracting** that percentage from itself
- **With a calculator** you can use **multipliers**

  - When **decreasing **by a percentage, we are f"
- Chunk excerpt: «How do I decrease by a percentage? - A percentage **decrease **makes an amount **smaller** by **subtracting** that percentage from itself - **With a calculator** you can use **multipliers** - When **decreasing **by a percentage, we are finding a percentage **smaller than 100%** - To decrease 80 by 15% - We are finding **85%** of 80, so the multiplier is **0.85** - Because 100% - 15% = 85% - 0.85 × 80 = 68 - You can a»
- Upstream: T-C32 join notes/1-numbers-and-the-number-system/percentages/percentage-increases-and-decreases.json::spcpt_d6jcrzdmQw9SvSPr — tier P1_name_fragment_join — score 1.0 — wording EXACT — validation tier AI_VALIDATED (operator-delegated chain)
- Rationale: SME span 'Percentage Increases & Decreases' on note 'Percentage Increases & Decreases' is anchored by the corpus spec_point block spcpt_d6jcrzdmQw9SvSPr and joined to 4MA1-1.6E via operator-verdict name-fragment join (T-SPEC-7; PMT excluded as source); this section chunk sits inside that span.
- Verdict: [ ] CONFIRM — this chunk belongs to this SP   [ ] REJECT — wrong chunk/SP   [ ] HOLD — needs rework

### 4MA1-4.6C — understand and use angle properties of the circle including: (i) angle subtended by an arc at the centre of a circle is twice the angle subtended at any point on the remaining part of the circumference (ii) angle subtended at the circumference by a diameter is a right angle (iii) angles in the same segment are equal (iv) the sum of the opposite angles of a cyclic quadrilateral is180° (v) the alternate segment theorem
- Note: Angle in a Semicircle (`notes/4-geometry-and-trigonometry/circle-theorems/angle-in-a-semicircle.json`)
- Chunk: ordinal 0 — heading `Angle in a semicircle` — sha256_16 `82decf783c64d0da` — 21 chars
- Evidence quote (verbatim self-slice, markdown-safe): "Angle in a semicircle"
- Chunk excerpt: «Angle in a semicircle»
- Upstream: T-C32 join notes/4-geometry-and-trigonometry/circle-theorems/angle-in-a-semicircle.json::spcpt_vGfjmcJJ9yzSFbzs — tier P1_name_fragment_join — score 1.0 — wording EXACT — validation tier AI_VALIDATED (operator-delegated chain)
- Rationale: SME span 'Angle in a Semicircle' on note 'Angle in a Semicircle' is anchored by the corpus spec_point block spcpt_vGfjmcJJ9yzSFbzs and joined to 4MA1-4.6C via operator-verdict name-fragment join (T-SPEC-7; PMT excluded as source); this section chunk sits inside that span.
- Verdict: [ ] CONFIRM — this chunk belongs to this SP   [ ] REJECT — wrong chunk/SP   [ ] HOLD — needs rework

### 4MA1-3.3F — calculate the gradient of a straight line given the coordinates of two points
- Note: Distance-Time Graphs (`notes/3-sequences-functions-and-graphs/real-life-graphs/distance-time-graphs.json`)
- Chunk: ordinal 2 — heading `How do I work out the overall average speed?` — sha256_16 `c2805326cadd0686` — 2122 chars
- Evidence quote (verbatim self-slice, markdown-safe): "How do I work out the overall average speed?
- For journeys with **multiple parts**

  - the **overall average speed** for the **whole** journey is $\frac{\mathrm{total} \mathrm{distance} \mathrm{travelled}}{\mathrm{total} \mathrm{time}}$
 "
- Chunk excerpt: «How do I work out the overall average speed? - For journeys with **multiple parts** - the **overall average speed** for the **whole** journey is $\frac{\mathrm{total} \mathrm{distance} \mathrm{travelled}}{\mathrm{total} \mathrm{time}}$ - The total time **includes** any rests Exam Hint: These questions often have a lot of parts that depend on each other, so always double check each answer before continuing. Worked Exa»
- Upstream: T-C32 join notes/3-sequences-functions-and-graphs/real-life-graphs/distance-time-graphs.json::spcpt_MTZDMgNSvV3FdVVR — tier P1_name_fragment_join — score 1.0 — wording EXACT — validation tier AI_VALIDATED (operator-delegated chain)
- Rationale: SME span 'Distance-Time Graphs' on note 'Distance-Time Graphs' is anchored by the corpus spec_point block spcpt_MTZDMgNSvV3FdVVR and joined to 4MA1-3.3F via operator-verdict name-fragment join (T-SPEC-7; PMT excluded as source); this section chunk sits inside that span.
- Verdict: [ ] CONFIRM — this chunk belongs to this SP   [ ] REJECT — wrong chunk/SP   [ ] HOLD — needs rework

### 4MA1-1.2I — multiply and divide fractions and mixed numbers
- Note: Multiplying & Dividing Fractions (`notes/1-numbers-and-the-number-system/fractions/multiplying-and-dividing.json`)
- Chunk: ordinal 3 — heading `Dividing fractions` — sha256_16 `f7a0a5e272998ca2` — 18 chars
- Evidence quote (verbatim self-slice, markdown-safe): "Dividing fractions"
- Chunk excerpt: «Dividing fractions»
- Upstream: T-C32 join notes/1-numbers-and-the-number-system/fractions/multiplying-and-dividing.json::spcpt_Fbm5V3ByzktDQbh5 — tier P1_name_fragment_join — score 1.0 — wording EXACT — validation tier AI_VALIDATED (operator-delegated chain)
- Rationale: SME span 'Dividing Fractions' on note 'Multiplying & Dividing Fractions' is anchored by the corpus spec_point block spcpt_Fbm5V3ByzktDQbh5 and joined to 4MA1-1.2I via operator-verdict name-fragment join (T-SPEC-7; PMT excluded as source); this section chunk sits inside that span.
- Verdict: [ ] CONFIRM — this chunk belongs to this SP   [ ] REJECT — wrong chunk/SP   [ ] HOLD — needs rework

### 4MA1-1.10B — carry out calculations using standard units of mass, length, area, volume and capacity
- Note: Squared & Cubic Units (`notes/4-geometry-and-trigonometry/standard-and-compound-units/squared-and-cubic-units.json`)
- Chunk: ordinal 1 — heading `How do I convert between squared units (areas)?` — sha256_16 `bf7c0f4b4536fc32` — 774 chars
- Evidence quote (verbatim self-slice, markdown-safe): "How do I convert between squared units (areas)?
- You need to **square** the **unit conversion** rates

  - E.g., 1 cm<sup>2</sup> = 10<sup>2</sup> mm<sup>2</sup> = 100 mm<sup>2</sup>
  - This is because area is 2D
  - The fact the units ha"
- Chunk excerpt: «How do I convert between squared units (areas)? - You need to **square** the **unit conversion** rates - E.g., 1 cm<sup>2</sup> = 10<sup>2</sup> mm<sup>2</sup> = 100 mm<sup>2</sup> - This is because area is 2D - The fact the units have a 'squared' on them will help you remember - It can help to **imagine a square** - E.g. 1 m<sup>2</sup> is a square measuring 1 m × 1 m - In cm this would be 100 cm × 100 cm - So 1 m<s»
- Upstream: T-C32 join notes/4-geometry-and-trigonometry/standard-and-compound-units/squared-and-cubic-units.json::spcpt_trxtpbq9c342p3qw — tier P2_page_context_join — score 1.0 — wording EXACT — validation tier AI_VALIDATED (operator-delegated chain)
- Rationale: SME span 'Squared & Cubic Units' on note 'Squared & Cubic Units' is anchored by the corpus spec_point block spcpt_trxtpbq9c342p3qw and joined to 4MA1-1.10B via operator-verdict page-context join (T-SPEC-7; PMT excluded as source); this section chunk sits inside that span.
- Verdict: [ ] CONFIRM — this chunk belongs to this SP   [ ] REJECT — wrong chunk/SP   [ ] HOLD — needs rework

### 4MA1-1.4A — understand the meaning of surds
- Note: Powers & Roots (`notes/1-numbers-and-the-number-system/powers-roots-and-standard-form/powers-and-roots.json`)
- Chunk: ordinal 0 — heading `Powers & roots` — sha256_16 `af4edb16b7c23eff` — 14 chars
- Evidence quote (verbatim self-slice, markdown-safe): "Powers & roots"
- Chunk excerpt: «Powers & roots»
- Upstream: T-C32 join notes/1-numbers-and-the-number-system/powers-roots-and-standard-form/powers-and-roots.json::spcpt_cDnTk2242hfSCjVh — tier P2_page_context_join — score 1.0 — wording EXACT — validation tier AI_VALIDATED (operator-delegated chain)
- Rationale: SME span 'Powers & Roots' on note 'Powers & Roots' is anchored by the corpus spec_point block spcpt_cDnTk2242hfSCjVh and joined to 4MA1-1.4A via operator-verdict page-context join (T-SPEC-7; PMT excluded as source); this section chunk sits inside that span.
- Verdict: [ ] CONFIRM — this chunk belongs to this SP   [ ] REJECT — wrong chunk/SP   [ ] HOLD — needs rework

### 4MA1-4.2B — understand and use the term ‘quadrilateral’ and the angle sum property of quadrilaterals
- Note: Angles in Cyclic Quadrilaterals (`notes/4-geometry-and-trigonometry/circle-theorems/cyclic-quadrilaterals.json`)
- Chunk: ordinal 0 — heading `Cyclic quadrilaterals` — sha256_16 `42281519c2f042b7` — 21 chars
- Evidence quote (verbatim self-slice, markdown-safe): "Cyclic quadrilaterals"
- Chunk excerpt: «Cyclic quadrilaterals»
- Upstream: T-C32 join notes/4-geometry-and-trigonometry/circle-theorems/cyclic-quadrilaterals.json::spcpt_rq6jFXGjg6FVSnKc — tier P1_name_fragment_join — score 1.0 — wording EXACT — validation tier AI_VALIDATED (operator-delegated chain)
- Rationale: SME span 'Cyclic Quadrilaterals' on note 'Angles in Cyclic Quadrilaterals' is anchored by the corpus spec_point block spcpt_rq6jFXGjg6FVSnKc and joined to 4MA1-4.2B via operator-verdict name-fragment join (T-SPEC-7; PMT excluded as source); this section chunk sits inside that span.
- Verdict: [ ] CONFIRM — this chunk belongs to this SP   [ ] REJECT — wrong chunk/SP   [ ] HOLD — needs rework

### 4MA1-4.6A — understand and use the internal and external intersecting chord properties
- Note: Angles in the Same Segment (`notes/4-geometry-and-trigonometry/circle-theorems/segment-theorems.json`)
- Chunk: ordinal 1 — heading `Circle Theorem: Angles in the same segment are equal` — sha256_16 `79a1a0808d36bb5f` — 2572 chars
- Evidence quote (verbatim self-slice, markdown-safe): "Circle Theorem: Angles in the same segment are equal
- **Any** **two angles** on the **circumference** of a circle that are formed from the **same two points** on the circumference are **equal**

  - These two angles are in the **same segme"
- Chunk excerpt: «Circle Theorem: Angles in the same segment are equal - **Any** **two angles** on the **circumference** of a circle that are formed from the **same two points** on the circumference are **equal** - These two angles are in the **same segment** of the circle - To see this, add the chord *PQ* below to split the circle into two segments A circle with points P and Q and the arc between them highlighted. Two chords from eac»
- Upstream: T-C32 join notes/4-geometry-and-trigonometry/circle-theorems/segment-theorems.json::spcpt_fMWRd3TnmcQ3c92k — tier P2_page_context_join — score 1.0 — wording EXACT — validation tier AI_VALIDATED (operator-delegated chain)
- Rationale: SME span 'Circles & Segments' on note 'Angles in the Same Segment' is anchored by the corpus spec_point block spcpt_fMWRd3TnmcQ3c92k and joined to 4MA1-4.6A via operator-verdict page-context join (T-SPEC-7; PMT excluded as source); this section chunk sits inside that span.
- Verdict: [ ] CONFIRM — this chunk belongs to this SP   [ ] REJECT — wrong chunk/SP   [ ] HOLD — needs rework

### 4MA1-4.6C — understand and use angle properties of the circle including: (i) angle subtended by an arc at the centre of a circle is twice the angle subtended at any point on the remaining part of the circumference (ii) angle subtended at the circumference by a diameter is a right angle (iii) angles in the same segment are equal (iv) the sum of the opposite angles of a cyclic quadrilateral is180° (v) the alternate segment theorem
- Note: The Alternate Segment Theorem (`notes/4-geometry-and-trigonometry/circle-theorems/the-alternate-segment-theorem.json`)
- Chunk: ordinal 0 — heading `Alternate segment theorem` — sha256_16 `b0c8d4ce60fb1acb` — 25 chars
- Evidence quote (verbatim self-slice, markdown-safe): "Alternate segment theorem"
- Chunk excerpt: «Alternate segment theorem»
- Upstream: T-C32 join notes/4-geometry-and-trigonometry/circle-theorems/the-alternate-segment-theorem.json::spcpt_TXCfYj93S7vCV9nq — tier P1_name_fragment_join — score 1.0 — wording EXACT — validation tier AI_VALIDATED (operator-delegated chain)
- Rationale: SME span 'Alternate Segment Theorem' on note 'The Alternate Segment Theorem' is anchored by the corpus spec_point block spcpt_TXCfYj93S7vCV9nq and joined to 4MA1-4.6C via operator-verdict name-fragment join (T-SPEC-7; PMT excluded as source); this section chunk sits inside that span.
- Verdict: [ ] CONFIRM — this chunk belongs to this SP   [ ] REJECT — wrong chunk/SP   [ ] HOLD — needs rework

### 4MA1-1.10B — carry out calculations using standard units of mass, length, area, volume and capacity
- Note: Upper & Lower Bounds (`notes/1-numbers-and-the-number-system/rounding-estimation-and-bounds/bounds.json`)
- Chunk: ordinal 6 — heading `How can bounds help with calculations?` — sha256_16 `8cd67c195c6525fd` — 2368 chars
- Evidence quote (verbatim self-slice, markdown-safe): "How can bounds help with calculations?
- You can use bounds to determine the **level of accuracy** of a calculation

  - E.g. If a value has a lower bound of 8.33217... and upper bound of s 8.33198...
  
    - The true value is between 8.33"
- Chunk excerpt: «How can bounds help with calculations? - You can use bounds to determine the **level of accuracy** of a calculation - E.g. If a value has a lower bound of 8.33217... and upper bound of s 8.33198... - The true value is between 8.33217... and 8.33198... - Find the level of accuracy for which **both bounds** round to the **same number** - This happens at 4 sf (rounding to 8.332) - To 5 sf they are different (lower is 8.»
- Upstream: T-C32 join notes/1-numbers-and-the-number-system/rounding-estimation-and-bounds/bounds.json::spcpt_M5rhN2mwnR2yddc6 — tier P1_name_fragment_join — score 1.0 — wording EXACT — validation tier AI_VALIDATED (operator-delegated chain)
- Rationale: SME span 'Calculations using Bounds' on note 'Upper & Lower Bounds' is anchored by the corpus spec_point block spcpt_M5rhN2mwnR2yddc6 and joined to 4MA1-1.10B via operator-verdict name-fragment join (T-SPEC-7; PMT excluded as source); this section chunk sits inside that span.
- Verdict: [ ] CONFIRM — this chunk belongs to this SP   [ ] REJECT — wrong chunk/SP   [ ] HOLD — needs rework

### 4MA1-4.6B — recognise the term ‘cyclic quadrilateral’
- Note: Theorems with Chords & Tangents (`notes/4-geometry-and-trigonometry/circle-theorems/chords-and-tangents.json`)
- Chunk: ordinal 4 — heading `What is a tangent?` — sha256_16 `e9a5fe50414d2c43` — 147 chars
- Evidence quote (verbatim self-slice, markdown-safe): "What is a tangent?
- A tangent to a circle is a straight line **outside of the circle** that touches its **circumference** at exactly **one point**"
- Chunk excerpt: «What is a tangent? - A tangent to a circle is a straight line **outside of the circle** that touches its **circumference** at exactly **one point**»
- Upstream: T-C32 join notes/4-geometry-and-trigonometry/circle-theorems/chords-and-tangents.json::spcpt_pNBVGz3x9h4NS45m — tier P1_name_fragment_join — score 1.0 — wording EXACT — validation tier AI_VALIDATED (operator-delegated chain)
- Rationale: SME span 'Circles & Tangents' on note 'Theorems with Chords & Tangents' is anchored by the corpus spec_point block spcpt_pNBVGz3x9h4NS45m and joined to 4MA1-4.6B via operator-verdict name-fragment join (T-SPEC-7; PMT excluded as source); this section chunk sits inside that span.
- Verdict: [ ] CONFIRM — this chunk belongs to this SP   [ ] REJECT — wrong chunk/SP   [ ] HOLD — needs rework

### 4MA1-6.1C — use cumulative frequency diagrams
- Note: Representing Vectors as Diagrams (`notes/5-vectors-and-transformation-geometry/vectors/representing-vectors-as-diagrams.json`)
- Chunk: ordinal 1 — heading `How can I represent a vector visually?` — sha256_16 `b192f825e3da6f2f` — 898 chars
- Evidence quote (verbatim self-slice, markdown-safe): "How can I represent a vector visually?
- A **vector** has **both a size (magnitude) and a direction**

  - You need to draw a **line** to show the **size of the vector**
  - You also need to draw an **arrow** to show the **direction of the "
- Chunk excerpt: «How can I represent a vector visually? - A **vector** has **both a size (magnitude) and a direction** - You need to draw a **line** to show the **size of the vector** - You also need to draw an **arrow** to show the **direction of the vector** Magnitude and direction of a vector - Vectors are written in** bold** when typed to **show** that they are a vector and not a scalar - When writing a vector in an exam you shou»
- Upstream: T-C32 join notes/5-vectors-and-transformation-geometry/vectors/representing-vectors-as-diagrams.json::spcpt_wt9snSTkmXqhMvXn — tier P1_name_fragment_join — score 1.0 — wording EXACT — validation tier AI_VALIDATED (operator-delegated chain)
- Rationale: SME span 'Vector Diagrams' on note 'Representing Vectors as Diagrams' is anchored by the corpus spec_point block spcpt_wt9snSTkmXqhMvXn and joined to 4MA1-6.1C via operator-verdict name-fragment join (T-SPEC-7; PMT excluded as source); this section chunk sits inside that span.
- Verdict: [ ] CONFIRM — this chunk belongs to this SP   [ ] REJECT — wrong chunk/SP   [ ] HOLD — needs rework

### 4MA1-1.4A — understand the meaning of surds
- Note: Negative Numbers (`notes/1-numbers-and-the-number-system/number-toolkit/negative-numbers.json`)
- Chunk: ordinal 2 — heading `Where are negative numbers used in real-life?` — sha256_16 `9da5c1d724c3d56a` — 2242 chars
- Evidence quote (verbatim self-slice, markdown-safe): "Where are negative numbers used in real-life?
- **Temperature** is a common context for negative numbers

  - If the temperature is 3°C, and it cools by 5°C, the new temperature will be -2°C
  
    - This is equivalent to 3 - 5 = - 2
  - If"
- Chunk excerpt: «Where are negative numbers used in real-life? - **Temperature** is a common context for negative numbers - If the temperature is 3°C, and it cools by 5°C, the new temperature will be -2°C - This is equivalent to 3 - 5 = - 2 - If the temperature is -4°C, and it warms up by 6°C, the new temperature will be 2°C - This is equivalent to (-4) + 6 = 2 - To explain why (-5) - (-6) = 1, you could think of it as follows: - A r»
- Upstream: T-C32 join notes/1-numbers-and-the-number-system/number-toolkit/negative-numbers.json::spcpt_3n2jHMX7vMBh95jq — tier P1_name_fragment_join — score 1.0 — wording EXACT — validation tier AI_VALIDATED (operator-delegated chain)
- Rationale: SME span 'Negative Numbers' on note 'Negative Numbers' is anchored by the corpus spec_point block spcpt_3n2jHMX7vMBh95jq and joined to 4MA1-1.4A via operator-verdict name-fragment join (T-SPEC-7; PMT excluded as source); this section chunk sits inside that span.
- Verdict: [ ] CONFIRM — this chunk belongs to this SP   [ ] REJECT — wrong chunk/SP   [ ] HOLD — needs rework

### 4MA1-4.11A — understand that areas of similar figures are in the ratio of the square of corresponding sides
- Note: Similarity (`notes/4-geometry-and-trigonometry/congruence-similarity-and-geometrical-proof/similarity.json`)
- Chunk: ordinal 1 — heading `What are similar shapes?` — sha256_16 `bf694cbf7c0e7aba` — 310 chars
- Evidence quote (verbatim self-slice, markdown-safe): "What are similar shapes?
- Two shapes are **similar **if they have the same **shape **and their** corresponding sides **are in **proportion**

  - One shape is an **enlargement **of the other
- **Similarity** does not imply ***congruence***"
- Chunk excerpt: «What are similar shapes? - Two shapes are **similar **if they have the same **shape **and their** corresponding sides **are in **proportion** - One shape is an **enlargement **of the other - **Similarity** does not imply ***congruence*** - Two similar shapes could be different enlargements of each other»
- Upstream: T-C32 join notes/4-geometry-and-trigonometry/congruence-similarity-and-geometrical-proof/similarity.json::spcpt_HcBpSfpzpdZqCFXk — tier P1_name_fragment_join — score 1.0 — wording EXACT — validation tier AI_VALIDATED (operator-delegated chain)
- Rationale: SME span 'Similarity' on note 'Similarity' is anchored by the corpus spec_point block spcpt_HcBpSfpzpdZqCFXk and joined to 4MA1-4.11A via operator-verdict name-fragment join (T-SPEC-7; PMT excluded as source); this section chunk sits inside that span.
- Verdict: [ ] CONFIRM — this chunk belongs to this SP   [ ] REJECT — wrong chunk/SP   [ ] HOLD — needs rework

### 4MA1-1.2I — multiply and divide fractions and mixed numbers
- Note: Basic Fractions (`notes/1-numbers-and-the-number-system/fractions/basic-fractions.json`)
- Chunk: ordinal 6 — heading `How do I simplify fractions?` — sha256_16 `c919599addfcd59f` — 461 chars
- Evidence quote (verbatim self-slice, markdown-safe): "How do I simplify fractions?
- To simplify the fraction,** divide the top and bottom **by the common factor
- $\frac{12}{18}=\frac{12\div6}{18\div6}=\frac{2}{3}$
- $\frac{25}{45}=\frac{25\div5}{45\div5}=\frac{5}{9}$
Exam Hint: Make use of y"
- Chunk excerpt: «How do I simplify fractions? - To simplify the fraction,** divide the top and bottom **by the common factor - $\frac{12}{18}=\frac{12\div6}{18\div6}=\frac{2}{3}$ - $\frac{25}{45}=\frac{25\div5}{45\div5}=\frac{5}{9}$ Exam Hint: Make use of your calculator in your exam: - Typing any fraction into it and pressing equals will automatically simplify the fraction for you. - If the question asks you to show your working, yo»
- Upstream: T-C32 join notes/1-numbers-and-the-number-system/fractions/basic-fractions.json::spcpt_339DNssRW9x2NPKk — tier P1_name_fragment_join — score 1.0 — wording EXACT — validation tier AI_VALIDATED (operator-delegated chain)
- Rationale: SME span 'Basic Fractions' on note 'Basic Fractions' is anchored by the corpus spec_point block spcpt_339DNssRW9x2NPKk and joined to 4MA1-1.2I via operator-verdict name-fragment join (T-SPEC-7; PMT excluded as source); this section chunk sits inside that span.
- Verdict: [ ] CONFIRM — this chunk belongs to this SP   [ ] REJECT — wrong chunk/SP   [ ] HOLD — needs rework

### 4MA1-1.9A — solve problems involving standard form
- Note: Operations with Standard Form (`notes/1-numbers-and-the-number-system/powers-roots-and-standard-form/operations-with-standard-form.json`)
- Chunk: ordinal 3 — heading `Multiplication` — sha256_16 `9e7c1b12b6c2cc36` — 728 chars
- Evidence quote (verbatim self-slice, markdown-safe): "Multiplication
- Consider the example `open parentheses 3 cross times 10 to the power of 112 close parentheses space cross times space open parentheses 4 cross times 10 to the power of 235 close parentheses`
- **STEP 1**
**Multiply **the **"
- Chunk excerpt: «Multiplication - Consider the example `open parentheses 3 cross times 10 to the power of 112 close parentheses space cross times space open parentheses 4 cross times 10 to the power of 235 close parentheses` - **STEP 1** **Multiply **the **ordinary **numbers - e.g. $3\times4=12$ - **STEP 2** **Multiply **the **powers **of 10 by **adding **the indices - e.g. $10^{112}\times10^{235}=10^{112+235}=10^{347}$ - **STEP 3** »
- Upstream: T-C32 join notes/1-numbers-and-the-number-system/powers-roots-and-standard-form/operations-with-standard-form.json::spcpt_rV2Crq8sHcCywRhW — tier P2_page_context_join — score 1.0 — wording EXACT — validation tier AI_VALIDATED (operator-delegated chain)
- Rationale: SME span 'Operations with Standard Form' on note 'Operations with Standard Form' is anchored by the corpus spec_point block spcpt_rV2Crq8sHcCywRhW and joined to 4MA1-1.9A via operator-verdict page-context join (T-SPEC-7; PMT excluded as source); this section chunk sits inside that span.
- Verdict: [ ] CONFIRM — this chunk belongs to this SP   [ ] REJECT — wrong chunk/SP   [ ] HOLD — needs rework

### 4MA1-3.2C — understand the terms ‘domain’ and ‘range’ and which values may need to be excluded from a domain
- Note: Domain & Range (`notes/3-sequences-functions-and-graphs/functions/domain-and-range.json`)
- Chunk: ordinal 6 — heading `How can I use graphs to find ranges?` — sha256_16 `3fc157ae90e05714` — 2322 chars
- Evidence quote (verbatim self-slice, markdown-safe): "How can I use graphs to find ranges?
- Ranges are easier if you know the** shapes** of different** types of graphs**

  - For example, the shapes of $y=\frac{1}{x}$, $y=x^{2}$, $y=x^{3}$, **trig graphs**, etc
  - They may also involve **gra"
- Chunk excerpt: «How can I use graphs to find ranges? - Ranges are easier if you know the** shapes** of different** types of graphs** - For example, the shapes of $y=\frac{1}{x}$, $y=x^{2}$, $y=x^{3}$, **trig graphs**, etc - They may also involve **graph transformations** Example of sketching the graph of a restricted function. Example of an exam question on domain and range. Exam Hint: - Sketching a function in an exam can help to "»
- Upstream: T-C32 join notes/3-sequences-functions-and-graphs/functions/domain-and-range.json::spcpt_2w6yB8pYShK9mGRb — tier P1_name_fragment_join — score 1.0 — wording EXACT — validation tier AI_VALIDATED (operator-delegated chain)
- Rationale: SME span 'Domain & Range' on note 'Domain & Range' is anchored by the corpus spec_point block spcpt_2w6yB8pYShK9mGRb and joined to 4MA1-3.2C via operator-verdict name-fragment join (T-SPEC-7; PMT excluded as source); this section chunk sits inside that span.
- Verdict: [ ] CONFIRM — this chunk belongs to this SP   [ ] REJECT — wrong chunk/SP   [ ] HOLD — needs rework

### 4MA1-1.10A — use and apply number in everyday personal, domestic or community life
- Note: Best Buys (`notes/1-numbers-and-the-number-system/exchange-rates-and-best-buys/best-buys.json`)
- Chunk: ordinal 0 — heading `Best buys` — sha256_16 `8bb92f0e25864986` — 9 chars
- Evidence quote (verbatim self-slice, markdown-safe): "Best buys"
- Chunk excerpt: «Best buys»
- Upstream: T-C32 join notes/1-numbers-and-the-number-system/exchange-rates-and-best-buys/best-buys.json::spcpt_qRytkYVHXTQBJdSq — tier P2_page_context_join — score 1.0 — wording EXACT — validation tier AI_VALIDATED (operator-delegated chain)
- Rationale: SME span 'Best Buys' on note 'Best Buys' is anchored by the corpus spec_point block spcpt_qRytkYVHXTQBJdSq and joined to 4MA1-1.10A via operator-verdict page-context join (T-SPEC-7; PMT excluded as source); this section chunk sits inside that span.
- Verdict: [ ] CONFIRM — this chunk belongs to this SP   [ ] REJECT — wrong chunk/SP   [ ] HOLD — needs rework

### 4MA1-1.4C — use index laws to simplify and evaluate numerical expressions involving integer, fractional and negative powers
- Note: Laws of Indices (`notes/1-numbers-and-the-number-system/powers-roots-and-standard-form/laws-of-indices.json`)
- Chunk: ordinal 2 — heading `How do I deal with different bases?` — sha256_16 `90c2d78bf4581264` — 3431 chars
- Evidence quote (verbatim self-slice, markdown-safe): "How do I deal with different bases?
- Index laws only work with terms that have the **same base**

  - $2^{3}\times5^{2}$ cannot be simplified using index laws
- Sometimes expressions involve different base values, but **one is related to t"
- Chunk excerpt: «How do I deal with different bases? - Index laws only work with terms that have the **same base** - $2^{3}\times5^{2}$ cannot be simplified using index laws - Sometimes expressions involve different base values, but **one is related to the other by a power** - e.g. $2^{5}\times4^{3}$ - You can use powers to **rewrite one of the bases** - `2 to the power of 5 cross times bold 4 cubed equals 2 to the power of 5 cross t»
- Upstream: T-C32 join notes/1-numbers-and-the-number-system/powers-roots-and-standard-form/laws-of-indices.json::spcpt_W6x4XqqqZWnY5SZc — tier P1_name_fragment_join — score 1.0 — wording EXACT — validation tier AI_VALIDATED (operator-delegated chain)
- Rationale: SME span 'Laws of Indices' on note 'Laws of Indices' is anchored by the corpus spec_point block spcpt_W6x4XqqqZWnY5SZc and joined to 4MA1-1.4C via operator-verdict name-fragment join (T-SPEC-7; PMT excluded as source); this section chunk sits inside that span.
- Verdict: [ ] CONFIRM — this chunk belongs to this SP   [ ] REJECT — wrong chunk/SP   [ ] HOLD — needs rework

### 4MA1-2.1A — use index notation involving fractional, negative and zero powers
- Note: Algebraic Vocabulary (`notes/2-equations-formulae-and-identities/algebra-toolkit/algebraic-vocabulary.json`)
- Chunk: ordinal 1 — heading `What is a term?` — sha256_16 `8d81d759c3e9359b` — 608 chars
- Evidence quote (verbatim self-slice, markdown-safe): "What is a term?
- A **term** is either:

  - a letter (**variable**) on its own, or a variable raised to a power
  
    - For example, *x  *or* x*<sup>2</sup>
  - a number on its own
  
    - For example, 20
    - These are also called **co"
- Chunk excerpt: «What is a term? - A **term** is either: - a letter (**variable**) on its own, or a variable raised to a power - For example, *x *or* x*<sup>2</sup> - a number on its own - For example, 20 - These are also called **constants **as they can't change value - or a number **multiplied** by a letter - For example, 5*x* - The number in front of a letter is called a **coefficient** - The coefficient of *x* in 6*x* is 6 - The »
- Upstream: T-C32 join notes/2-equations-formulae-and-identities/algebra-toolkit/algebraic-vocabulary.json::spcpt_jTrpYhtMdhpPhwxb — tier P1_name_fragment_join — score 1.0 — wording EXACT — validation tier AI_VALIDATED (operator-delegated chain)
- Rationale: SME span 'Algebraic Vocabulary' on note 'Algebraic Vocabulary' is anchored by the corpus spec_point block spcpt_jTrpYhtMdhpPhwxb and joined to 4MA1-2.1A via operator-verdict name-fragment join (T-SPEC-7; PMT excluded as source); this section chunk sits inside that span.
- Verdict: [ ] CONFIRM — this chunk belongs to this SP   [ ] REJECT — wrong chunk/SP   [ ] HOLD — needs rework

### 4MA1-2.8D — represent simple linear inequalities on rectangular Cartesian graphs
- Note: Solving Linear Inequalities (`notes/2-equations-formulae-and-identities/solving-inequalities/solving-linear-inequalities.json`)
- Chunk: ordinal 3 — heading `How do I represent an inequality on a number line?` — sha256_16 `f52470c842cba88c` — 1398 chars
- Evidence quote (verbatim self-slice, markdown-safe): "How do I represent an inequality on a number line?
- The inequality -3"
- Chunk excerpt: «How do I represent an inequality on a number line? - The inequality -3 < *x* ≤ 4 is shown on a **number line** below A number line representing an inequality - Draw** circles** above the** end points **and connect them with a **horizontal line** - Leave an **open circle** for end points with **strict** inequalities, **< or >** - These end points **are not** included - Fill in a **solid circle** for end points with **»
- Upstream: T-C32 join notes/2-equations-formulae-and-identities/solving-inequalities/solving-linear-inequalities.json::spcpt_X8CSxK2dhn5rX34f — tier P1_name_fragment_join — score 1.0 — wording EXACT — validation tier AI_VALIDATED (operator-delegated chain)
- Rationale: SME span 'Solving Linear Inequalities' on note 'Solving Linear Inequalities' is anchored by the corpus spec_point block spcpt_X8CSxK2dhn5rX34f and joined to 4MA1-2.8D via operator-verdict name-fragment join (T-SPEC-7; PMT excluded as source); this section chunk sits inside that span.
- Verdict: [ ] CONFIRM — this chunk belongs to this SP   [ ] REJECT — wrong chunk/SP   [ ] HOLD — needs rework

### 4MA1-5.1D — add and subtract vectors
- Note: Introduction to Column Vectors (`notes/5-vectors-and-transformation-geometry/vectors/introduction-to-vectors.json`)
- Chunk: ordinal 1 — heading `What are column vectors?` — sha256_16 `e8948c244b0c40c2` — 304 chars
- Evidence quote (verbatim self-slice, markdown-safe): "What are column vectors?
- A **column vector** can be used to **describe** how to get **from one point to another point**

  - This is also called a **translation vector**
  - `open parentheses table row 6 row 3 end table close parentheses`"
- Chunk excerpt: «What are column vectors? - A **column vector** can be used to **describe** how to get **from one point to another point** - This is also called a **translation vector** - `open parentheses table row 6 row 3 end table close parentheses` means **6 units to the right** and **3 units up** Column vector»
- Upstream: T-C32 join notes/5-vectors-and-transformation-geometry/vectors/introduction-to-vectors.json::spcpt_v6tP4DSVShVJMJhk — tier P1_name_fragment_join — score 1.0 — wording EXACT — validation tier AI_VALIDATED (operator-delegated chain)
- Rationale: SME span 'Basic Vectors' on note 'Introduction to Column Vectors' is anchored by the corpus spec_point block spcpt_v6tP4DSVShVJMJhk and joined to 4MA1-5.1D via operator-verdict name-fragment join (T-SPEC-7; PMT excluded as source); this section chunk sits inside that span.
- Verdict: [ ] CONFIRM — this chunk belongs to this SP   [ ] REJECT — wrong chunk/SP   [ ] HOLD — needs rework

### 4MA1-2.3F — change the subject of a formula where the subject appears once
- Note: Formulas where Subject Appears Twice (`notes/2-equations-formulae-and-identities/rearranging-formulae/formulas-where-subject-appears-twice.json`)
- Chunk: ordinal 2 — heading `How do I factorise powers of a subject?` — sha256_16 `68ea783162c30225` — 3035 chars
- Evidence quote (verbatim self-slice, markdown-safe): "How do I factorise powers of a subject?
- If the **subject appears twice**, and **both have the same power**, you will need to **collect these terms together** before applying their inverse

  - E.g. When making $x$the subject of $x^{2}=-px"
- Chunk excerpt: «How do I factorise powers of a subject? - If the **subject appears twice**, and **both have the same power**, you will need to **collect these terms together** before applying their inverse - E.g. When making $x$the subject of $x^{2}=-px^{2}+r$ - Add $px^{2}$ to both sides first to form $x^{2}+px^{2}=r$ - $x^{2}$ can then be factorised out `x squared open parentheses 1 plus p close parentheses equals r` to give $x^{2»
- Upstream: T-C32 join notes/2-equations-formulae-and-identities/rearranging-formulae/formulas-where-subject-appears-twice.json::spcpt_m8WdtZKSWCKNFKrY — tier P1_name_fragment_join — score 1.0 — wording EXACT — validation tier AI_VALIDATED (operator-delegated chain)
- Rationale: SME span 'Subject Appears Twice' on note 'Formulas where Subject Appears Twice' is anchored by the corpus spec_point block spcpt_m8WdtZKSWCKNFKrY and joined to 4MA1-2.3F via operator-verdict name-fragment join (T-SPEC-7; PMT excluded as source); this section chunk sits inside that span.
- Verdict: [ ] CONFIRM — this chunk belongs to this SP   [ ] REJECT — wrong chunk/SP   [ ] HOLD — needs rework

### 4MA1-3.3F — calculate the gradient of a straight line given the coordinates of two points
- Note: Trigonometric Graphs (`notes/3-sequences-functions-and-graphs/graphs-of-functions/trig-graphs.json`)
- Chunk: ordinal 4 — heading `What is the shape of the graph of y = tan x?` — sha256_16 `16b483ad7f2aba68` — 666 chars
- Evidence quote (verbatim self-slice, markdown-safe): "What is the shape of the graph of y = tan x?
- The graph of $y=\mathrm{tan}x$ is **not a wave** but consists of** branches** that** repeat every 180° **(its **period** is 180°)

  - This is** half the period **of** **$\mathrm{sin}x$ and $\m"
- Chunk excerpt: «What is the shape of the graph of y = tan x? - The graph of $y=\mathrm{tan}x$ is **not a wave** but consists of** branches** that** repeat every 180° **(its **period** is 180°) - This is** half the period **of** **$\mathrm{sin}x$ and $\mathrm{cos}x$ - There are **dotted vertical lines** that separate the branches called **asymptotes** - These are every 180° at $x=90^{\circ}$, $x=270^{\circ}$, ... - The curve cannot t»
- Upstream: T-C32 join notes/3-sequences-functions-and-graphs/graphs-of-functions/trig-graphs.json::spcpt_6bYjJ8kxTNBbcSjX — tier P1_name_fragment_join — score 1.0 — wording EXACT — validation tier AI_VALIDATED (operator-delegated chain)
- Rationale: SME span 'Drawing Trig Graphs' on note 'Trigonometric Graphs' is anchored by the corpus spec_point block spcpt_6bYjJ8kxTNBbcSjX and joined to 4MA1-3.3F via operator-verdict name-fragment join (T-SPEC-7; PMT excluded as source); this section chunk sits inside that span.
- Verdict: [ ] CONFIRM — this chunk belongs to this SP   [ ] REJECT — wrong chunk/SP   [ ] HOLD — needs rework

### 4MA1-1.2I — multiply and divide fractions and mixed numbers
- Note: Multiplying & Dividing Fractions (`notes/1-numbers-and-the-number-system/fractions/multiplying-and-dividing.json`)
- Chunk: ordinal 2 — heading `How do I multiply two fractions if one is a mixed number?` — sha256_16 `ed1a75d07f2f4b38` — 1130 chars
- Evidence quote (verbatim self-slice, markdown-safe): "How do I multiply two fractions if one is a mixed number?
- Always convert **mixed numbers** into ***improper fractions*** before multiplying

  - **Convert **improper fractions **back** into mixed numbers at the end if required
Exam Hint: "
- Chunk excerpt: «How do I multiply two fractions if one is a mixed number? - Always convert **mixed numbers** into ***improper fractions*** before multiplying - **Convert **improper fractions **back** into mixed numbers at the end if required Exam Hint: In most questions, you can just use your calculator to multiply fractions. However, sometimes you get asked to show your working without using a calculator. Worked Example: Show that »
- Upstream: T-C32 join notes/1-numbers-and-the-number-system/fractions/multiplying-and-dividing.json::spcpt_3sptc2fDMgGnNYqg — tier P1_name_fragment_join — score 1.0 — wording EXACT — validation tier AI_VALIDATED (operator-delegated chain)
- Rationale: SME span 'Multiplying Fractions' on note 'Multiplying & Dividing Fractions' is anchored by the corpus spec_point block spcpt_3sptc2fDMgGnNYqg and joined to 4MA1-1.2I via operator-verdict name-fragment join (T-SPEC-7; PMT excluded as source); this section chunk sits inside that span.
- Verdict: [ ] CONFIRM — this chunk belongs to this SP   [ ] REJECT — wrong chunk/SP   [ ] HOLD — needs rework

### 4MA1-3.3I — recognise, generate points and plot graphs of linear and quadratic functions
- Note: Drawing Graphs from Tables (`notes/3-sequences-functions-and-graphs/graphs-of-functions/drawing-graphs-from-tables.json`)
- Chunk: ordinal 0 — heading `Drawing graphs using a table` — sha256_16 `2db0f3cf897b41f1` — 28 chars
- Evidence quote (verbatim self-slice, markdown-safe): "Drawing graphs using a table"
- Chunk excerpt: «Drawing graphs using a table»
- Upstream: T-C32 join notes/3-sequences-functions-and-graphs/graphs-of-functions/drawing-graphs-from-tables.json::spcpt_SwbJdpQTQxGXry8M — tier P2_page_context_join — score 1.0 — wording EXACT — validation tier AI_VALIDATED (operator-delegated chain)
- Rationale: SME span 'Drawing Graphs Using a Table' on note 'Drawing Graphs from Tables' is anchored by the corpus spec_point block spcpt_SwbJdpQTQxGXry8M and joined to 4MA1-3.3I via operator-verdict page-context join (T-SPEC-7; PMT excluded as source); this section chunk sits inside that span.
- Verdict: [ ] CONFIRM — this chunk belongs to this SP   [ ] REJECT — wrong chunk/SP   [ ] HOLD — needs rework

### 4MA1-1.2I — multiply and divide fractions and mixed numbers
- Note: Multiplying & Dividing Fractions (`notes/1-numbers-and-the-number-system/fractions/multiplying-and-dividing.json`)
- Chunk: ordinal 0 — heading `Multiplying fractions` — sha256_16 `b897d49aa0b01e22` — 21 chars
- Evidence quote (verbatim self-slice, markdown-safe): "Multiplying fractions"
- Chunk excerpt: «Multiplying fractions»
- Upstream: T-C32 join notes/1-numbers-and-the-number-system/fractions/multiplying-and-dividing.json::spcpt_3sptc2fDMgGnNYqg — tier P1_name_fragment_join — score 1.0 — wording EXACT — validation tier AI_VALIDATED (operator-delegated chain)
- Rationale: SME span 'Multiplying Fractions' on note 'Multiplying & Dividing Fractions' is anchored by the corpus spec_point block spcpt_3sptc2fDMgGnNYqg and joined to 4MA1-1.2I via operator-verdict name-fragment join (T-SPEC-7; PMT excluded as source); this section chunk sits inside that span.
- Verdict: [ ] CONFIRM — this chunk belongs to this SP   [ ] REJECT — wrong chunk/SP   [ ] HOLD — needs rework

### 4MA1-2.4B — set up simple linear equations from given data
- Note: Forming Equations from Shapes (`notes/2-equations-formulae-and-identities/forming-and-solving-equations/forming-equations-from-shapes.json`)
- Chunk: ordinal 0 — heading `Forming equations from shapes` — sha256_16 `1712b1840a99c980` — 29 chars
- Evidence quote (verbatim self-slice, markdown-safe): "Forming equations from shapes"
- Chunk excerpt: «Forming equations from shapes»
- Upstream: T-C32 join notes/2-equations-formulae-and-identities/forming-and-solving-equations/forming-equations-from-shapes.json::spcpt_F2BG7bHjbM3fZkrR — tier P2_page_context_join — score 1.0 — wording EXACT — validation tier AI_VALIDATED (operator-delegated chain)
- Rationale: SME span 'Forming Equations from Shapes' on note 'Forming Equations from Shapes' is anchored by the corpus spec_point block spcpt_F2BG7bHjbM3fZkrR and joined to 4MA1-2.4B via operator-verdict page-context join (T-SPEC-7; PMT excluded as source); this section chunk sits inside that span.
- Verdict: [ ] CONFIRM — this chunk belongs to this SP   [ ] REJECT — wrong chunk/SP   [ ] HOLD — needs rework

### 4MA1-4.8D — use Pythagoras’ theorem in three dimensions
- Note: 3D Pythagoras & Trigonometry (`notes/4-geometry-and-trigonometry/3d-pythagoras-and-trigonometry/3d-pythagoras-and-trigonometry.json`)
- Chunk: ordinal 2 — heading `Is there a 3D version of the Pythagoras' theorem formula?` — sha256_16 `7a288e0e86edba81` — 813 chars
- Evidence quote (verbatim self-slice, markdown-safe): "Is there a 3D version of the Pythagoras' theorem formula?
- There is a **3D version** of Pythagoras’ theorem: $d^{2}=x^{2}+y^{2}+z^{2}$

  - $d$ is the distance between two points
  - $x,y$ and $z$ are the distances in the **three different"
- Chunk excerpt: «Is there a 3D version of the Pythagoras' theorem formula? - There is a **3D version** of Pythagoras’ theorem: $d^{2}=x^{2}+y^{2}+z^{2}$ - $d$ is the distance between two points - $x,y$ and $z$ are the distances in the **three different perpendicular directions** between the two points Example showing Pythagoras' theorem to find the diagonal in a cuboid (3D formula). - However, all 3D situations can be broken into **t»
- Upstream: T-C32 join notes/4-geometry-and-trigonometry/3d-pythagoras-and-trigonometry/3d-pythagoras-and-trigonometry.json::spcpt_kX4655D8M3Q3TRzW — tier P1_name_fragment_join — score 1.0 — wording EXACT — validation tier AI_VALIDATED (operator-delegated chain)
- Rationale: SME span '3D Pythagoras & Trigonometry' on note '3D Pythagoras & Trigonometry' is anchored by the corpus spec_point block spcpt_kX4655D8M3Q3TRzW and joined to 4MA1-4.8D via operator-verdict name-fragment join (T-SPEC-7; PMT excluded as source); this section chunk sits inside that span.
- Verdict: [ ] CONFIRM — this chunk belongs to this SP   [ ] REJECT — wrong chunk/SP   [ ] HOLD — needs rework

### 4MA1-4.5C — solve problems using scale drawings
- Note: Using a Calculator (`notes/1-numbers-and-the-number-system/using-a-calculator/using-a-calculator.json`)
- Chunk: ordinal 6 — heading `Which buttons are useful for standard form and calculations involving π?` — sha256_16 `8e049e4a3afb179f` — 467 chars
- Evidence quote (verbatim self-slice, markdown-safe): "Which buttons are useful for standard form and calculations involving π?
- To write a number in **standard form** on the calculator, use the **×10**<sup>***x***</sup>

  - Modern calculators display standard form in the way it is written, e"
- Chunk excerpt: «Which buttons are useful for standard form and calculations involving π? - To write a number in **standard form** on the calculator, use the **×10**<sup>***x***</sup> - Modern calculators display standard form in the way it is written, e.g., 2 x 10<sup>5</sup> - Older models may use a small capital letter** 'E'** in place of ×10<sup>*x*</sup>, e.g., 2E5 - $π$ is often near the standard form button - You may need to u»
- Upstream: T-C32 join notes/1-numbers-and-the-number-system/using-a-calculator/using-a-calculator.json::spcpt_xf7Y5cxcQG3T6g65 — tier P1_name_fragment_join — score 1.0 — wording EXACT — validation tier AI_VALIDATED (operator-delegated chain)
- Rationale: SME span 'Using a Calculator' on note 'Using a Calculator' is anchored by the corpus spec_point block spcpt_xf7Y5cxcQG3T6g65 and joined to 4MA1-4.5C via operator-verdict name-fragment join (T-SPEC-7; PMT excluded as source); this section chunk sits inside that span.
- Verdict: [ ] CONFIRM — this chunk belongs to this SP   [ ] REJECT — wrong chunk/SP   [ ] HOLD — needs rework

### 4MA1-4.11C — use areas and volumes of similar figures in solving problems
- Note: Problem Solving with Areas (`notes/4-geometry-and-trigonometry/area-and-perimeter/problem-solving-with-areas.json`)
- Chunk: ordinal 3 — heading `How do I solve problems that involve area?` — sha256_16 `6c9715a41e702807` — 3691 chars
- Evidence quote (verbatim self-slice, markdown-safe): "How do I solve problems that involve area?
- There is often a **lot of text** in a problem-solving question, which can make it seem harder than it is

  - Avoid focusing **only** on what the question asks you, think about what you can do wi"
- Chunk excerpt: «How do I solve problems that involve area? - There is often a **lot of text** in a problem-solving question, which can make it seem harder than it is - Avoid focusing **only** on what the question asks you, think about what you can do with the **information given** - This may lead you to think of **something else** you can do - Eventually you may be able to see your way to answering the **original question** - Think »
- Upstream: T-C32 join notes/4-geometry-and-trigonometry/area-and-perimeter/problem-solving-with-areas.json::spcpt_3fMGfNtg3hXMg6gC — tier P1_name_fragment_join — score 1.0 — wording EXACT — validation tier AI_VALIDATED (operator-delegated chain)
- Rationale: SME span 'Problem Solving with Areas' on note 'Problem Solving with Areas' is anchored by the corpus spec_point block spcpt_3fMGfNtg3hXMg6gC and joined to 4MA1-4.11C via operator-verdict name-fragment join (T-SPEC-7; PMT excluded as source); this section chunk sits inside that span.
- Verdict: [ ] CONFIRM — this chunk belongs to this SP   [ ] REJECT — wrong chunk/SP   [ ] HOLD — needs rework

### 4MA1-1.4D — express integers as a product of powers of prime factors
- Note: Prime Factor Decomposition (`notes/1-numbers-and-the-number-system/prime-factors-hcf-and-lcm/prime-factor-decomposition.json`)
- Chunk: ordinal 1 — heading `What are prime factors?` — sha256_16 `5ce413527fa4baa2` — 564 chars
- Evidence quote (verbatim self-slice, markdown-safe): "What are prime factors?
- A **factor **of a given number is a value that divides the given number exactly, with no remainder

  - e.g. 6 is a factor of 18
- A **prime** number is a number which has exactly two **factors;** itself and 1

  -"
- Chunk excerpt: «What are prime factors? - A **factor **of a given number is a value that divides the given number exactly, with no remainder - e.g. 6 is a factor of 18 - A **prime** number is a number which has exactly two **factors;** itself and 1 - e.g. 5 is a prime number, as its only factors are 5 and 1 - You should remember the first few prime numbers: - 2, 3, 5, 7, 11, 13, 17, 19, … - The **prime factors** of a number are ther»
- Upstream: T-C32 join notes/1-numbers-and-the-number-system/prime-factors-hcf-and-lcm/prime-factor-decomposition.json::spcpt_SgzMz9GCcsdMwJcx — tier P1_name_fragment_join — score 1.0 — wording EXACT — validation tier AI_VALIDATED (operator-delegated chain)
- Rationale: SME span 'Prime Factor Decomposition' on note 'Prime Factor Decomposition' is anchored by the corpus spec_point block spcpt_SgzMz9GCcsdMwJcx and joined to 4MA1-1.4D via operator-verdict name-fragment join (T-SPEC-7; PMT excluded as source); this section chunk sits inside that span.
- Verdict: [ ] CONFIRM — this chunk belongs to this SP   [ ] REJECT — wrong chunk/SP   [ ] HOLD — needs rework

### 4MA1-1.6F — use reverse percentages
- Note: Basic Percentages (`notes/1-numbers-and-the-number-system/percentages/basic-percentages.json`)
- Chunk: ordinal 2 — heading `How do I find a percentage of an amount with a calculator?` — sha256_16 `f87576d350dfe434` — 558 chars
- Evidence quote (verbatim self-slice, markdown-safe): "How do I find a percentage of an amount with a calculator?
- Percentages can be found using **multipliers**
- A multiplier is the **decimal equivalent** of a percentage
- E.g. To find **12% of 650**

  - Write 12% as a decimal multiplier
  "
- Chunk excerpt: «How do I find a percentage of an amount with a calculator? - Percentages can be found using **multipliers** - A multiplier is the **decimal equivalent** of a percentage - E.g. To find **12% of 650** - Write 12% as a decimal multiplier - 12% is equivalent to 0.12 - Find the product of the amount and the multiplier, using your calculator - 0.12 × 650 = **78** - So 12% of 650 is 78 - When finding a percentage **larger t»
- Upstream: T-C32 join notes/1-numbers-and-the-number-system/percentages/basic-percentages.json::spcpt_FHRjdMc6tvRR553q — tier P1_name_fragment_join — score 1.0 — wording EXACT — validation tier AI_VALIDATED (operator-delegated chain)
- Rationale: SME span 'Basic Percentages' on note 'Basic Percentages' is anchored by the corpus spec_point block spcpt_FHRjdMc6tvRR553q and joined to 4MA1-1.6F via operator-verdict name-fragment join (T-SPEC-7; PMT excluded as source); this section chunk sits inside that span.
- Verdict: [ ] CONFIRM — this chunk belongs to this SP   [ ] REJECT — wrong chunk/SP   [ ] HOLD — needs rework

### 4MA1-1.9A — solve problems involving standard form
- Note: Operations with Standard Form (`notes/1-numbers-and-the-number-system/powers-roots-and-standard-form/operations-with-standard-form.json`)
- Chunk: ordinal 4 — heading `Division` — sha256_16 `f6384cfc32d36a32` — 1095 chars
- Evidence quote (verbatim self-slice, markdown-safe): "Division
- Consider the example `open parentheses 2 cross times 10 to the power of negative 150 end exponent close parentheses space divided by space open parentheses 8 cross times 10 to the power of negative 131 end exponent close parenthe"
- Chunk excerpt: «Division - Consider the example `open parentheses 2 cross times 10 to the power of negative 150 end exponent close parentheses space divided by space open parentheses 8 cross times 10 to the power of negative 131 end exponent close parentheses` - **STEP 1** **Divide **the **first ordinary **number by the **second ordinary** number - e.g. $2\div8=0.25$ - **STEP 2** **Divide **the **first power **of 10 by the **second »
- Upstream: T-C32 join notes/1-numbers-and-the-number-system/powers-roots-and-standard-form/operations-with-standard-form.json::spcpt_rV2Crq8sHcCywRhW — tier P2_page_context_join — score 1.0 — wording EXACT — validation tier AI_VALIDATED (operator-delegated chain)
- Rationale: SME span 'Operations with Standard Form' on note 'Operations with Standard Form' is anchored by the corpus spec_point block spcpt_rV2Crq8sHcCywRhW and joined to 4MA1-1.9A via operator-verdict page-context join (T-SPEC-7; PMT excluded as source); this section chunk sits inside that span.
- Verdict: [ ] CONFIRM — this chunk belongs to this SP   [ ] REJECT — wrong chunk/SP   [ ] HOLD — needs rework

### 4MA1-2.6B — interpret the equations as lines and the common solution as the point of intersection
- Note: Solving Equations from Graphs (`notes/3-sequences-functions-and-graphs/graphs-of-functions/graphical-solutions.json`)
- Chunk: ordinal 3 — heading `How do I use graphs to solve equations?` — sha256_16 `7b8bc4f5240bfc70` — 3560 chars
- Evidence quote (verbatim self-slice, markdown-safe): "How do I use graphs to solve equations?
- This is easiest explained through an example
- You can use the** graph** of $y=x^{2}-4x-2$ to **solve** the following **equations**

  - $x^{2}-4x-2=0$
  
    - The **solutions** are the two** *****"
- Chunk excerpt: «How do I use graphs to solve equations? - This is easiest explained through an example - You can use the** graph** of $y=x^{2}-4x-2$ to **solve** the following **equations** - $x^{2}-4x-2=0$ - The **solutions** are the two** *****x*****-intercepts** - This is where the curve cuts the *x*-axis (also called **roots**) - $x^{2}-4x-2=5$ - The **solutions **are the two** *****x*****-coordinates** where the curve** interse»
- Upstream: T-C32 join notes/3-sequences-functions-and-graphs/graphs-of-functions/graphical-solutions.json::spcpt_sHCB9WZbDMyTFqCP — tier P1_name_fragment_join — score 1.0 — wording EXACT — validation tier AI_VALIDATED (operator-delegated chain)
- Rationale: SME span 'Solving Equations Using Graphs' on note 'Solving Equations from Graphs' is anchored by the corpus spec_point block spcpt_sHCB9WZbDMyTFqCP and joined to 4MA1-2.6B via operator-verdict name-fragment join (T-SPEC-7; PMT excluded as source); this section chunk sits inside that span.
- Verdict: [ ] CONFIRM — this chunk belongs to this SP   [ ] REJECT — wrong chunk/SP   [ ] HOLD — needs rework

### 4MA1-1.3A — convert recurring decimals into fractions
- Note: Algebraic Notation (`notes/2-equations-formulae-and-identities/algebra-toolkit/algebraic-notation.json`)
- Chunk: ordinal 1 — heading `What is algebra?` — sha256_16 `aa732da46345d544` — 276 chars
- Evidence quote (verbatim self-slice, markdown-safe): "What is algebra?
- **Algebra **is a topic in mathematics that uses **letters **to** **represent **general** (or **unknown**) **numbers**

  - *x*  and *y*  are two unknown numbers
  
    - More information is needed to find their values
- L"
- Chunk excerpt: «What is algebra? - **Algebra **is a topic in mathematics that uses **letters **to** **represent **general** (or **unknown**) **numbers** - *x* and *y* are two unknown numbers - More information is needed to find their values - Letters are also called** variables**»
- Upstream: T-C32 join notes/2-equations-formulae-and-identities/algebra-toolkit/algebraic-notation.json::spcpt_gzQvnKpxPvTqzzBp — tier P1_name_fragment_join — score 1.0 — wording EXACT — validation tier AI_VALIDATED (operator-delegated chain)
- Rationale: SME span 'Algebraic Notation' on note 'Algebraic Notation' is anchored by the corpus spec_point block spcpt_gzQvnKpxPvTqzzBp and joined to 4MA1-1.3A via operator-verdict name-fragment join (T-SPEC-7; PMT excluded as source); this section chunk sits inside that span.
- Verdict: [ ] CONFIRM — this chunk belongs to this SP   [ ] REJECT — wrong chunk/SP   [ ] HOLD — needs rework

### 4MA1-1.2G — convert a fraction to a decimal or a percentage
- Note: Converting Fractions, Decimals & Percentages (`notes/1-numbers-and-the-number-system/fractions-decimals-and-percentages/converting-between-fdp.json`)
- Chunk: ordinal 4 — heading `How do I convert from a percentage to a fraction?` — sha256_16 `ffbf515b721f1d2d` — 114 chars
- Evidence quote (verbatim self-slice, markdown-safe): "How do I convert from a percentage to a fraction?
- Write the **percentage over 100**

  - 37% is $\frac{37}{100}$"
- Chunk excerpt: «How do I convert from a percentage to a fraction? - Write the **percentage over 100** - 37% is $\frac{37}{100}$»
- Upstream: T-C32 join notes/1-numbers-and-the-number-system/fractions-decimals-and-percentages/converting-between-fdp.json::spcpt_8MpvS5pnYkf9QswF — tier P2_page_context_join — score 1.0 — wording EXACT — validation tier AI_VALIDATED (operator-delegated chain)
- Rationale: SME span 'FDP Conversions' on note 'Converting Fractions, Decimals & Percentages' is anchored by the corpus spec_point block spcpt_8MpvS5pnYkf9QswF and joined to 4MA1-1.2G via operator-verdict page-context join (T-SPEC-7; PMT excluded as source); this section chunk sits inside that span.
- Verdict: [ ] CONFIRM — this chunk belongs to this SP   [ ] REJECT — wrong chunk/SP   [ ] HOLD — needs rework

### 4MA1-1.6E — solve simple percentage problems, including percentage increase and decrease
- Note: Percentage Increases & Decreases (`notes/1-numbers-and-the-number-system/percentages/percentage-increases-and-decreases.json`)
- Chunk: ordinal 1 — heading `How do I increase by a percentage?` — sha256_16 `8b0b86697a35160d` — 801 chars
- Evidence quote (verbatim self-slice, markdown-safe): "How do I increase by a percentage?
- A percentage **increase** makes an amount **bigger** by **adding** that percentage on to itself
- **With a calculator** you can use **multipliers**

  - A multiplier is the **decimal equivalent** of a pe"
- Chunk excerpt: «How do I increase by a percentage? - A percentage **increase** makes an amount **bigger** by **adding** that percentage on to itself - **With a calculator** you can use **multipliers** - A multiplier is the **decimal equivalent** of a percentage - A **percentage **can be converted** to a decimal **by **dividing by 100** - When **increasing** by a percentage, we are finding a percentage **greater than 100%** - To incr»
- Upstream: T-C32 join notes/1-numbers-and-the-number-system/percentages/percentage-increases-and-decreases.json::spcpt_d6jcrzdmQw9SvSPr — tier P1_name_fragment_join — score 1.0 — wording EXACT — validation tier AI_VALIDATED (operator-delegated chain)
- Rationale: SME span 'Percentage Increases & Decreases' on note 'Percentage Increases & Decreases' is anchored by the corpus spec_point block spcpt_d6jcrzdmQw9SvSPr and joined to 4MA1-1.6E via operator-verdict name-fragment join (T-SPEC-7; PMT excluded as source); this section chunk sits inside that span.
- Verdict: [ ] CONFIRM — this chunk belongs to this SP   [ ] REJECT — wrong chunk/SP   [ ] HOLD — needs rework

### 4MA1-2.1A — use index notation involving fractional, negative and zero powers
- Note: Algebraic Vocabulary (`notes/2-equations-formulae-and-identities/algebra-toolkit/algebraic-vocabulary.json`)
- Chunk: ordinal 3 — heading `What is an expression?` — sha256_16 `501ed805513b1d6e` — 421 chars
- Evidence quote (verbatim self-slice, markdown-safe): "What is an expression?
- An **expression **is an algebraic statement that does **not **have an **equals sign**

  - There is nothing to solve
- An expression is made by adding, subtracting, multiplying or dividing **terms**

  - 2*x* + 5*y*"
- Chunk excerpt: «What is an expression? - An **expression **is an algebraic statement that does **not **have an **equals sign** - There is nothing to solve - An expression is made by adding, subtracting, multiplying or dividing **terms** - 2*x* + 5*y* - *b*<sup>2</sup> – 2*cd* - $\frac{6y}{5t}$ - A single term is still an expression - Expressions can be **simplified** (made easier) - *x* + *x* + *x* simplifies to 3*x*»
- Upstream: T-C32 join notes/2-equations-formulae-and-identities/algebra-toolkit/algebraic-vocabulary.json::spcpt_jTrpYhtMdhpPhwxb — tier P1_name_fragment_join — score 1.0 — wording EXACT — validation tier AI_VALIDATED (operator-delegated chain)
- Rationale: SME span 'Algebraic Vocabulary' on note 'Algebraic Vocabulary' is anchored by the corpus spec_point block spcpt_jTrpYhtMdhpPhwxb and joined to 4MA1-2.1A via operator-verdict name-fragment join (T-SPEC-7; PMT excluded as source); this section chunk sits inside that span.
- Verdict: [ ] CONFIRM — this chunk belongs to this SP   [ ] REJECT — wrong chunk/SP   [ ] HOLD — needs rework

### 4MA1-6.1A — construct and interpret histograms
- Note: Pie Charts (`notes/6-statistics-and-probability/statistics-toolkit/pie-charts.json`)
- Chunk: ordinal 1 — heading `What is a pie chart?` — sha256_16 `9fdb17e9261a565c` — 289 chars
- Evidence quote (verbatim self-slice, markdown-safe): "What is a pie chart?
- A** pie chart** is a circle divided into sectors which is used to **present data**
- The **sectors** represent different **categories**

  - They show the relative **proportions** of the categories
  - They do** not**"
- Chunk excerpt: «What is a pie chart? - A** pie chart** is a circle divided into sectors which is used to **present data** - The **sectors** represent different **categories** - They show the relative **proportions** of the categories - They do** not** show the actual **frequencies **of each category»
- Upstream: T-C32 join notes/6-statistics-and-probability/statistics-toolkit/pie-charts.json::spcpt_rxmWrBrc2s2q45wF — tier P1_name_fragment_join — score 1.0 — wording EXACT — validation tier AI_VALIDATED (operator-delegated chain)
- Rationale: SME span 'Pie Charts' on note 'Pie Charts' is anchored by the corpus spec_point block spcpt_rxmWrBrc2s2q45wF and joined to 4MA1-6.1A via operator-verdict name-fragment join (T-SPEC-7; PMT excluded as source); this section chunk sits inside that span.
- Verdict: [ ] CONFIRM — this chunk belongs to this SP   [ ] REJECT — wrong chunk/SP   [ ] HOLD — needs rework

### 4MA1-1.4C — use index laws to simplify and evaluate numerical expressions involving integer, fractional and negative powers
- Note: Algebraic Roots & Indices (`notes/2-equations-formulae-and-identities/algebraic-roots-and-indices/algebraic-roots-and-indices.json`)
- Chunk: ordinal 0 — heading `Algebraic roots & indices` — sha256_16 `8184f7fc8262b8d0` — 25 chars
- Evidence quote (verbatim self-slice, markdown-safe): "Algebraic roots & indices"
- Chunk excerpt: «Algebraic roots & indices»
- Upstream: T-C32 join notes/2-equations-formulae-and-identities/algebraic-roots-and-indices/algebraic-roots-and-indices.json::spcpt_s2x4ZG4rWQhHJrTh — tier P2_page_context_join — score 1.0 — wording EXACT — validation tier AI_VALIDATED (operator-delegated chain)
- Rationale: SME span 'Algebraic Roots & Indices' on note 'Algebraic Roots & Indices' is anchored by the corpus spec_point block spcpt_s2x4ZG4rWQhHJrTh and joined to 4MA1-1.4C via operator-verdict page-context join (T-SPEC-7; PMT excluded as source); this section chunk sits inside that span.
- Verdict: [ ] CONFIRM — this chunk belongs to this SP   [ ] REJECT — wrong chunk/SP   [ ] HOLD — needs rework

### 4MA1-1.4A — understand the meaning of surds
- Note: Powers & Roots (`notes/1-numbers-and-the-number-system/powers-roots-and-standard-form/powers-and-roots.json`)
- Chunk: ordinal 3 — heading `What are cube roots?` — sha256_16 `b94e52b570ba887a` — 405 chars
- Evidence quote (verbatim self-slice, markdown-safe): "What are cube roots?
- A **cube root** of 125 is a number that when **cubed **equals 125

  - The cube root of 125 is 5
  
    - 5<sup>3</sup> = 125
  - Unlike square roots, each number only has** one cube root**
  - Every **positive** and "
- Chunk excerpt: «What are cube roots? - A **cube root** of 125 is a number that when **cubed **equals 125 - The cube root of 125 is 5 - 5<sup>3</sup> = 125 - Unlike square roots, each number only has** one cube root** - Every **positive** and **negative** **number** has** one real cube root** - The notation `cube root of blank` refers to the **cube root** of a number - `cube root of 125 equals 5`»
- Upstream: T-C32 join notes/1-numbers-and-the-number-system/powers-roots-and-standard-form/powers-and-roots.json::spcpt_cDnTk2242hfSCjVh — tier P2_page_context_join — score 1.0 — wording EXACT — validation tier AI_VALIDATED (operator-delegated chain)
- Rationale: SME span 'Powers & Roots' on note 'Powers & Roots' is anchored by the corpus spec_point block spcpt_cDnTk2242hfSCjVh and joined to 4MA1-1.4A via operator-verdict page-context join (T-SPEC-7; PMT excluded as source); this section chunk sits inside that span.
- Verdict: [ ] CONFIRM — this chunk belongs to this SP   [ ] REJECT — wrong chunk/SP   [ ] HOLD — needs rework

### 4MA1-4.11A — understand that areas of similar figures are in the ratio of the square of corresponding sides
- Note: Similarity (`notes/4-geometry-and-trigonometry/congruence-similarity-and-geometrical-proof/similarity.json`)
- Chunk: ordinal 2 — heading `How do we prove that two triangles are similar?` — sha256_16 `5010b1837d8e6167` — 649 chars
- Evidence quote (verbatim self-slice, markdown-safe): "How do we prove that two triangles are similar?
- To show that two **triangles** are **similar** you need to show that their **angles are the same**

  - If the angles are the same then **corresponding lengths** of a triangle will automatic"
- Chunk excerpt: «How do we prove that two triangles are similar? - To show that two **triangles** are **similar** you need to show that their **angles are the same** - If the angles are the same then **corresponding lengths** of a triangle will automatically be **in proportion** - You can use angle properties to **identify equal angles** - Look out for for **isosceles triangles**, **vertically opposite angles** and **angles on parall»
- Upstream: T-C32 join notes/4-geometry-and-trigonometry/congruence-similarity-and-geometrical-proof/similarity.json::spcpt_HcBpSfpzpdZqCFXk — tier P1_name_fragment_join — score 1.0 — wording EXACT — validation tier AI_VALIDATED (operator-delegated chain)
- Rationale: SME span 'Similarity' on note 'Similarity' is anchored by the corpus spec_point block spcpt_HcBpSfpzpdZqCFXk and joined to 4MA1-4.11A via operator-verdict name-fragment join (T-SPEC-7; PMT excluded as source); this section chunk sits inside that span.
- Verdict: [ ] CONFIRM — this chunk belongs to this SP   [ ] REJECT — wrong chunk/SP   [ ] HOLD — needs rework

### 4MA1-2.2F — understand the concept of a quadratic expression and be able to factorise such expressions (limited tox + bx + c)
- Note: Factorising Simple Quadratics (`notes/2-equations-formulae-and-identities/factorising/factorising-quadratics.json`)
- Chunk: ordinal 2 — heading `How do I factorise quadratics by inspection?` — sha256_16 `74ef8bf1ff1e78e4` — 544 chars
- Evidence quote (verbatim self-slice, markdown-safe): "How do I factorise quadratics by inspection?
- This is shown most easily through an example: factorising $x^{2}-2x-8$
- We need a **pair of numbers** that for $x^{2}+bx+c$

  - **multiply** to give *c*
  
    - which in this case is -8
  - "
- Chunk excerpt: «How do I factorise quadratics by inspection? - This is shown most easily through an example: factorising $x^{2}-2x-8$ - We need a **pair of numbers** that for $x^{2}+bx+c$ - **multiply** to give *c* - which in this case is -8 - and **add** to give *b* - which in this case is -2 - +2 and -4 satisfy these conditions - 2 × (-4) = -8 and 2 + (-4) = -2 - **Write** these numbers in a **pair of brackets** like this: - `open»
- Upstream: T-C32 join notes/2-equations-formulae-and-identities/factorising/factorising-quadratics.json::spcpt_7pTpRYh7tsCnGspT — tier P1_name_fragment_join — score 1.0 — wording EXACT — validation tier AI_VALIDATED (operator-delegated chain)
- Rationale: SME span 'Factorising Simple Quadratics' on note 'Factorising Simple Quadratics' is anchored by the corpus spec_point block spcpt_7pTpRYh7tsCnGspT and joined to 4MA1-2.2F via operator-verdict name-fragment join (T-SPEC-7; PMT excluded as source); this section chunk sits inside that span.
- Verdict: [ ] CONFIRM — this chunk belongs to this SP   [ ] REJECT — wrong chunk/SP   [ ] HOLD — needs rework

### 4MA1-4.1B — use angle properties of intersecting lines, parallel lines and angles on a straight line
- Note: Basic Angle Properties (`notes/4-geometry-and-trigonometry/angles-in-polygons-and-parallel-lines/basic-angle-properties.json`)
- Chunk: ordinal 4 — heading `What are the angle properties of quadrilaterals?` — sha256_16 `d5e9d999ac9cea54` — 1399 chars
- Evidence quote (verbatim self-slice, markdown-safe): "What are the angle properties of quadrilaterals?
- The **four** interior angles inside any quadrilateral **add up to 360°**
- If the quadrilateral is a **square** or a **rectangle** then all the angles are equal to **90°**
- You can use any"
- Chunk excerpt: «What are the angle properties of quadrilaterals? - The **four** interior angles inside any quadrilateral **add up to 360°** - If the quadrilateral is a **square** or a **rectangle** then all the angles are equal to **90°** - You can use any **symmetries** of the quadrilateral to identify other equal angles - For a **parallelogram** (or** **rhombus), **opposite angles** are **equal** - For a **kite,** **one pair** of »
- Upstream: T-C32 join notes/4-geometry-and-trigonometry/angles-in-polygons-and-parallel-lines/basic-angle-properties.json::spcpt_5FMXZMjqSZ3GK53q — tier P1_name_fragment_join — score 1.0 — wording EXACT — validation tier AI_VALIDATED (operator-delegated chain)
- Rationale: SME span 'Basic Angle Properties' on note 'Basic Angle Properties' is anchored by the corpus spec_point block spcpt_5FMXZMjqSZ3GK53q and joined to 4MA1-4.1B via operator-verdict name-fragment join (T-SPEC-7; PMT excluded as source); this section chunk sits inside that span.
- Verdict: [ ] CONFIRM — this chunk belongs to this SP   [ ] REJECT — wrong chunk/SP   [ ] HOLD — needs rework

### 4MA1-6.2C — find the interquartile range from a discrete data set
- Note: Averages from Grouped Data (`notes/6-statistics-and-probability/statistics-toolkit/averages-from-grouped-data.json`)
- Chunk: ordinal 0 — heading `Averages from grouped data` — sha256_16 `cb79eda53b597cf9` — 26 chars
- Evidence quote (verbatim self-slice, markdown-safe): "Averages from grouped data"
- Chunk excerpt: «Averages from grouped data»
- Upstream: T-C32 join notes/6-statistics-and-probability/statistics-toolkit/averages-from-grouped-data.json::spcpt_Nd47QSGCxH96FDk3 — tier P1_name_fragment_join — score 1.0 — wording EXACT — validation tier AI_VALIDATED (operator-delegated chain)
- Rationale: SME span 'Averages from Grouped Data' on note 'Averages from Grouped Data' is anchored by the corpus spec_point block spcpt_Nd47QSGCxH96FDk3 and joined to 4MA1-6.2C via operator-verdict name-fragment join (T-SPEC-7; PMT excluded as source); this section chunk sits inside that span.
- Verdict: [ ] CONFIRM — this chunk belongs to this SP   [ ] REJECT — wrong chunk/SP   [ ] HOLD — needs rework

### 4MA1-2.2A — expand the product of two or more linear expressions
- Note: Substitution (`notes/2-equations-formulae-and-identities/algebra-toolkit/substitution.json`)
- Chunk: ordinal 1 — heading `What is substitution?` — sha256_16 `d28933f09bd35e1d` — 117 chars
- Evidence quote (verbatim self-slice, markdown-safe): "What is substitution?
- **Substitution** means **replacing** a letter (variable) in a formula with a given **number**"
- Chunk excerpt: «What is substitution? - **Substitution** means **replacing** a letter (variable) in a formula with a given **number**»
- Upstream: T-C32 join notes/2-equations-formulae-and-identities/algebra-toolkit/substitution.json::spcpt_6tmCTQJYPsTdKKZ6 — tier P1_name_fragment_join — score 1.0 — wording EXACT — validation tier AI_VALIDATED (operator-delegated chain)
- Rationale: SME span 'Substitution' on note 'Substitution' is anchored by the corpus spec_point block spcpt_6tmCTQJYPsTdKKZ6 and joined to 4MA1-2.2A via operator-verdict name-fragment join (T-SPEC-7; PMT excluded as source); this section chunk sits inside that span.
- Verdict: [ ] CONFIRM — this chunk belongs to this SP   [ ] REJECT — wrong chunk/SP   [ ] HOLD — needs rework

### 4MA1-4.9E — find circumferences and areas of circles using relevant formulae; find perimeters and areas of semicircles
- Note: Area & Circumference of Circles (`notes/4-geometry-and-trigonometry/circles-arcs-and-sectors/area-and-circumference-of-circles.json`)
- Chunk: ordinal 3 — heading `How do I find the circumference of a circle?` — sha256_16 `4937c2b55569cebb` — 166 chars
- Evidence quote (verbatim self-slice, markdown-safe): "How do I find the circumference of a circle?
- Identify the **diameter**

  - This is **double **the length of the **radius**
- **Multiply** the **diameter** by **π**"
- Chunk excerpt: «How do I find the circumference of a circle? - Identify the **diameter** - This is **double **the length of the **radius** - **Multiply** the **diameter** by **π**»
- Upstream: T-C32 join notes/4-geometry-and-trigonometry/circles-arcs-and-sectors/area-and-circumference-of-circles.json::spcpt_Mq2w9qKSCyF5mvvs — tier P1_name_fragment_join — score 1.0 — wording EXACT — validation tier AI_VALIDATED (operator-delegated chain)
- Rationale: SME span 'Area & Circumference' on note 'Area & Circumference of Circles' is anchored by the corpus spec_point block spcpt_Mq2w9qKSCyF5mvvs and joined to 4MA1-4.9E via operator-verdict name-fragment join (T-SPEC-7; PMT excluded as source); this section chunk sits inside that span.
- Verdict: [ ] CONFIRM — this chunk belongs to this SP   [ ] REJECT — wrong chunk/SP   [ ] HOLD — needs rework

### 4MA1-1.9A — solve problems involving standard form
- Note: Operations with Standard Form (`notes/1-numbers-and-the-number-system/powers-roots-and-standard-form/operations-with-standard-form.json`)
- Chunk: ordinal 0 — heading `Operations with standard form` — sha256_16 `0f11f672b32c1930` — 29 chars
- Evidence quote (verbatim self-slice, markdown-safe): "Operations with standard form"
- Chunk excerpt: «Operations with standard form»
- Upstream: T-C32 join notes/1-numbers-and-the-number-system/powers-roots-and-standard-form/operations-with-standard-form.json::spcpt_rV2Crq8sHcCywRhW — tier P2_page_context_join — score 1.0 — wording EXACT — validation tier AI_VALIDATED (operator-delegated chain)
- Rationale: SME span 'Operations with Standard Form' on note 'Operations with Standard Form' is anchored by the corpus spec_point block spcpt_rV2Crq8sHcCywRhW and joined to 4MA1-1.9A via operator-verdict page-context join (T-SPEC-7; PMT excluded as source); this section chunk sits inside that span.
- Verdict: [ ] CONFIRM — this chunk belongs to this SP   [ ] REJECT — wrong chunk/SP   [ ] HOLD — needs rework

### 4MA1-1.1F — use brackets and the hierarchy of operations
- Note: Order of Operations (BIDMAS/BODMAS) (`notes/1-numbers-and-the-number-system/number-toolkit/order-of-operations-bidmas-bodmas.json`)
- Chunk: ordinal 3 — heading `How do I use a calculator for BIDMAS/BODMAS questions?` — sha256_16 `12fdf04dc6e4bca3` — 768 chars
- Evidence quote (verbatim self-slice, markdown-safe): "How do I use a calculator for BIDMAS/BODMAS questions?
- Ensure that you enter a long or complicated calculation carefully

  - For most modern calculators, the calculation can be typed in exactly as it is written on paper
  - You may need "
- Chunk excerpt: «How do I use a calculator for BIDMAS/BODMAS questions? - Ensure that you enter a long or complicated calculation carefully - For most modern calculators, the calculation can be typed in exactly as it is written on paper - You may need to use additional brackets on older calculators Exam Hint: Make sure that you always check that your answer seems sensible! Worked Example: Work out $(5--3)+2\times7^{2}$. **Answer:** >»
- Upstream: T-C32 join notes/1-numbers-and-the-number-system/number-toolkit/order-of-operations-bidmas-bodmas.json::spcpt_c25SPBnps9dhX2Dk — tier P1_name_fragment_join — score 1.0 — wording EXACT — validation tier AI_VALIDATED (operator-delegated chain)
- Rationale: SME span 'Order of Operations (BIDMAS/BODMAS)' on note 'Order of Operations (BIDMAS/BODMAS)' is anchored by the corpus spec_point block spcpt_c25SPBnps9dhX2Dk and joined to 4MA1-1.1F via operator-verdict name-fragment join (T-SPEC-7; PMT excluded as source); this section chunk sits inside that span.
- Verdict: [ ] CONFIRM — this chunk belongs to this SP   [ ] REJECT — wrong chunk/SP   [ ] HOLD — needs rework

### 4MA1-1.6E — solve simple percentage problems, including percentage increase and decrease
- Note: Percentage Increases & Decreases (`notes/1-numbers-and-the-number-system/percentages/percentage-increases-and-decreases.json`)
- Chunk: ordinal 0 — heading `Percentage increases & decreases` — sha256_16 `78305f00506b78a7` — 32 chars
- Evidence quote (verbatim self-slice, markdown-safe): "Percentage increases & decreases"
- Chunk excerpt: «Percentage increases & decreases»
- Upstream: T-C32 join notes/1-numbers-and-the-number-system/percentages/percentage-increases-and-decreases.json::spcpt_d6jcrzdmQw9SvSPr — tier P1_name_fragment_join — score 1.0 — wording EXACT — validation tier AI_VALIDATED (operator-delegated chain)
- Rationale: SME span 'Percentage Increases & Decreases' on note 'Percentage Increases & Decreases' is anchored by the corpus spec_point block spcpt_d6jcrzdmQw9SvSPr and joined to 4MA1-1.6E via operator-verdict name-fragment join (T-SPEC-7; PMT excluded as source); this section chunk sits inside that span.
- Verdict: [ ] CONFIRM — this chunk belongs to this SP   [ ] REJECT — wrong chunk/SP   [ ] HOLD — needs rework

### 4MA1-3.3F — calculate the gradient of a straight line given the coordinates of two points
- Note: Distance-Time Graphs (`notes/3-sequences-functions-and-graphs/real-life-graphs/distance-time-graphs.json`)
- Chunk: ordinal 0 — heading `Distance-time graphs` — sha256_16 `6c4e98cb3efc3421` — 20 chars
- Evidence quote (verbatim self-slice, markdown-safe): "Distance-time graphs"
- Chunk excerpt: «Distance-time graphs»
- Upstream: T-C32 join notes/3-sequences-functions-and-graphs/real-life-graphs/distance-time-graphs.json::spcpt_MTZDMgNSvV3FdVVR — tier P1_name_fragment_join — score 1.0 — wording EXACT — validation tier AI_VALIDATED (operator-delegated chain)
- Rationale: SME span 'Distance-Time Graphs' on note 'Distance-Time Graphs' is anchored by the corpus spec_point block spcpt_MTZDMgNSvV3FdVVR and joined to 4MA1-3.3F via operator-verdict name-fragment join (T-SPEC-7; PMT excluded as source); this section chunk sits inside that span.
- Verdict: [ ] CONFIRM — this chunk belongs to this SP   [ ] REJECT — wrong chunk/SP   [ ] HOLD — needs rework

### 4MA1-4.10A — find the surface area and volume of a sphere and a right circular cone using relevant formulae
- Note: 3D Shapes (`notes/4-geometry-and-trigonometry/volume-and-surface-area/properties-of-3d-shapes.json`)
- Chunk: ordinal 1 — heading `What common 3D shapes do I need to know about?` — sha256_16 `e5bd6abedeada7b8` — 1352 chars
- Evidence quote (verbatim self-slice, markdown-safe): "What common 3D shapes do I need to know about?
- There are a number of **common 3D shapes **

  - You should know their **names **
  - and their **key properties**
- A **prism **is a 3D shape with the same **cross-section **throughout"
- Chunk excerpt: «What common 3D shapes do I need to know about? - There are a number of **common 3D shapes ** - You should know their **names ** - and their **key properties** - A **prism **is a 3D shape with the same **cross-section **throughout ![Volume of a prism](assets/59870ec0db61-55534-properties-of-3d-shapes.png) - The cross-section of a **cube** is a **square** - The cross-section of a **cuboid** is a **rectangle** - There a»
- Upstream: T-C32 join notes/4-geometry-and-trigonometry/volume-and-surface-area/properties-of-3d-shapes.json::spcpt_Xqkq2qz7NzMcVZHQ — tier P2_page_context_join — score 1.0 — wording EXACT — validation tier AI_VALIDATED (operator-delegated chain)
- Rationale: SME span 'Properties of 3D Shapes' on note '3D Shapes' is anchored by the corpus spec_point block spcpt_Xqkq2qz7NzMcVZHQ and joined to 4MA1-4.10A via operator-verdict page-context join (T-SPEC-7; PMT excluded as source); this section chunk sits inside that span.
- Verdict: [ ] CONFIRM — this chunk belongs to this SP   [ ] REJECT — wrong chunk/SP   [ ] HOLD — needs rework

### 4MA1-2.7A — solve quadratic equations by factorisation
- Note: Solving Quadratics by Factorising (`notes/2-equations-formulae-and-identities/solving-quadratic-equations/solving-quadratic-equations.json`)
- Chunk: ordinal 2 — heading `What if there are numbers in front of the x's in the brackets?` — sha256_16 `c2d49dc19bd1675e` — 689 chars
- Evidence quote (verbatim self-slice, markdown-safe): "What if there are numbers in front of the x's in the brackets?
- The process is **the same**

  - There's a bit more work to find the solutions
  - You can't just write down the answers by changing the signs
- To solve `open parentheses 2 x"
- Chunk excerpt: «What if there are numbers in front of the x's in the brackets? - The process is **the same** - There's a bit more work to find the solutions - You can't just write down the answers by changing the signs - To solve `open parentheses 2 x minus 3 close parentheses open parentheses 3 x plus 5 close parentheses equals 0` - …solve **first bracket = 0** - 2*x* – 3 = 0 - add 3 to both sides: 2*x* = 3 - divide both sides by 2»
- Upstream: T-C32 join notes/2-equations-formulae-and-identities/solving-quadratic-equations/solving-quadratic-equations.json::spcpt_dxtWxKmTWPrYkWt3 — tier P1_name_fragment_join — score 1.0 — wording EXACT — validation tier AI_VALIDATED (operator-delegated chain)
- Rationale: SME span 'Solving Quadratics by Factorising' on note 'Solving Quadratics by Factorising' is anchored by the corpus spec_point block spcpt_dxtWxKmTWPrYkWt3 and joined to 4MA1-2.7A via operator-verdict name-fragment join (T-SPEC-7; PMT excluded as source); this section chunk sits inside that span.
- Verdict: [ ] CONFIRM — this chunk belongs to this SP   [ ] REJECT — wrong chunk/SP   [ ] HOLD — needs rework

### 4MA1-4.2C — understand and use the properties of the parallelogram, rectangle, square, rhombus, trapezium and kite
- Note: 2D Shapes (`notes/4-geometry-and-trigonometry/angles-in-polygons-and-parallel-lines/properties-of-2d-shapes.json`)
- Chunk: ordinal 1 — heading `What are the names of common 2D shapes?` — sha256_16 `2dc70747717040a3` — 525 chars
- Evidence quote (verbatim self-slice, markdown-safe): "What are the names of common 2D shapes?
- You should know the general names of all the 2D **polygons**

  - A **triangle** has 3 sides
  - A **quadrilateral** has 4 sides
  - A **pentagon** has 5 sides
  - A **hexagon** has 6 sides
  - A **"
- Chunk excerpt: «What are the names of common 2D shapes? - You should know the general names of all the 2D **polygons** - A **triangle** has 3 sides - A **quadrilateral** has 4 sides - A **pentagon** has 5 sides - A **hexagon** has 6 sides - A **heptagon** has 7 sides - An **octagon **has 8 sides - A **nonagon** has 9 sides - A **decagon **has 10 sides - A **polygon **is a flat (plane) shape with *n* straight sides - A **regular **po»
- Upstream: T-C32 join notes/4-geometry-and-trigonometry/angles-in-polygons-and-parallel-lines/properties-of-2d-shapes.json::spcpt_SVXT7VrWxFMXkD7D — tier P2_page_context_join — score 1.0 — wording EXACT — validation tier AI_VALIDATED (operator-delegated chain)
- Rationale: SME span 'Properties of 2D Shapes' on note '2D Shapes' is anchored by the corpus spec_point block spcpt_SVXT7VrWxFMXkD7D and joined to 4MA1-4.2C via operator-verdict page-context join (T-SPEC-7; PMT excluded as source); this section chunk sits inside that span.
- Verdict: [ ] CONFIRM — this chunk belongs to this SP   [ ] REJECT — wrong chunk/SP   [ ] HOLD — needs rework

### 4MA1-4.5B — construct triangles and other two-dimensional shapes using a combination of a ruler, a protractor and compasses
- Note: Constructing Triangles (`notes/4-geometry-and-trigonometry/bearings-scale-drawing-and-constructions/constructing-triangles.json`)
- Chunk: ordinal 2 — heading `How do I construct an SSS triangle?` — sha256_16 `9504aa9daea79dae` — 2191 chars
- Evidence quote (verbatim self-slice, markdown-safe): "How do I construct an SSS triangle?
- **STEP 1**
Use a **ruler** to draw the **longest **side as the **horizontal **base near the bottom of the space you have been given

  - This needs to be **accurate**
  - Write its length (with units) j"
- Chunk excerpt: «How do I construct an SSS triangle? - **STEP 1** Use a **ruler** to draw the **longest **side as the **horizontal **base near the bottom of the space you have been given - This needs to be **accurate** - Write its length (with units) just underneath - **STEP 2** Open your **compasses **so that the **length** from the **compass point to the tip of your pencil** is **exactly the length** of one of the **remaining sides»
- Upstream: T-C32 join notes/4-geometry-and-trigonometry/bearings-scale-drawing-and-constructions/constructing-triangles.json::spcpt_RXP6GyfJydf7Kggr — tier P1_name_fragment_join — score 1.0 — wording EXACT — validation tier AI_VALIDATED (operator-delegated chain)
- Rationale: SME span 'Constructing Triangles' on note 'Constructing Triangles' is anchored by the corpus spec_point block spcpt_RXP6GyfJydf7Kggr and joined to 4MA1-4.5B via operator-verdict name-fragment join (T-SPEC-7; PMT excluded as source); this section chunk sits inside that span.
- Verdict: [ ] CONFIRM — this chunk belongs to this SP   [ ] REJECT — wrong chunk/SP   [ ] HOLD — needs rework

### 4MA1-1.2I — multiply and divide fractions and mixed numbers
- Note: Multiplying & Dividing Fractions (`notes/1-numbers-and-the-number-system/fractions/multiplying-and-dividing.json`)
- Chunk: ordinal 5 — heading `How do I divide two fractions when one of them is a mixed number?` — sha256_16 `64fb48805278d5e3` — 1162 chars
- Evidence quote (verbatim self-slice, markdown-safe): "How do I divide two fractions when one of them is a mixed number?
- Always convert **mixed numbers** into ***improper fractions***** **before dividing

  - **Convert** improper fractions **back** into mixed numbers at the end if required
Ex"
- Chunk excerpt: «How do I divide two fractions when one of them is a mixed number? - Always convert **mixed numbers** into ***improper fractions***** **before dividing - **Convert** improper fractions **back** into mixed numbers at the end if required Exam Hint: Remember “flip’n’times": When dividing fractions you are multiplying by the reciprocal. Worked Example: Show that $3\frac{1}{4}\div\frac{3}{8}=8\frac{2}{3}$. **Answer:** > *R»
- Upstream: T-C32 join notes/1-numbers-and-the-number-system/fractions/multiplying-and-dividing.json::spcpt_Fbm5V3ByzktDQbh5 — tier P1_name_fragment_join — score 1.0 — wording EXACT — validation tier AI_VALIDATED (operator-delegated chain)
- Rationale: SME span 'Dividing Fractions' on note 'Multiplying & Dividing Fractions' is anchored by the corpus spec_point block spcpt_Fbm5V3ByzktDQbh5 and joined to 4MA1-1.2I via operator-verdict name-fragment join (T-SPEC-7; PMT excluded as source); this section chunk sits inside that span.
- Verdict: [ ] CONFIRM — this chunk belongs to this SP   [ ] REJECT — wrong chunk/SP   [ ] HOLD — needs rework

### 4MA1-5.1G — apply vector methods for simple geometrical proofs
- Note: Geometrical Proof (`notes/4-geometry-and-trigonometry/congruence-similarity-and-geometrical-proof/geometrical-proof.json`)
- Chunk: ordinal 0 — heading `Geometrical proof` — sha256_16 `b3464f8cbcba1dd4` — 17 chars
- Evidence quote (verbatim self-slice, markdown-safe): "Geometrical proof"
- Chunk excerpt: «Geometrical proof»
- Upstream: T-C32 join notes/4-geometry-and-trigonometry/congruence-similarity-and-geometrical-proof/geometrical-proof.json::spcpt_hK2H8q4Y8NYv833v — tier P1_name_fragment_join — score 1.0 — wording EXACT — validation tier AI_VALIDATED (operator-delegated chain)
- Rationale: SME span 'Geometrical Proof' on note 'Geometrical Proof' is anchored by the corpus spec_point block spcpt_hK2H8q4Y8NYv833v and joined to 4MA1-5.1G via operator-verdict name-fragment join (T-SPEC-7; PMT excluded as source); this section chunk sits inside that span.
- Verdict: [ ] CONFIRM — this chunk belongs to this SP   [ ] REJECT — wrong chunk/SP   [ ] HOLD — needs rework

### 4MA1-3.3G — find the equation of a straight line parallel to a given line; find the equation of a straight line perpendicular to a given line
- Note: Length of a Line (`notes/3-sequences-functions-and-graphs/coordinate-geometry/length-of-a-line.json`)
- Chunk: ordinal 1 — heading `How do I calculate the length of a line?` — sha256_16 `1ee0326acffc2430` — 2198 chars
- Evidence quote (verbatim self-slice, markdown-safe): "How do I calculate the length of a line?
- The **distance between two points** with coordinates `open parentheses x subscript 1 space comma space y subscript 1 close parentheses` and `open parentheses x subscript 2 space comma space y subsc"
- Chunk excerpt: «How do I calculate the length of a line? - The **distance between two points** with coordinates `open parentheses x subscript 1 space comma space y subscript 1 close parentheses` and `open parentheses x subscript 2 space comma space y subscript 2 close parentheses` can be found using the formula `d equals square root of open parentheses x subscript 1 minus x subscript 2 close parentheses squared plus open parentheses»
- Upstream: T-C32 join notes/3-sequences-functions-and-graphs/coordinate-geometry/length-of-a-line.json::spcpt_hMqjBRzQQfvsc9f8 — tier P1_name_fragment_join — score 1.0 — wording EXACT — validation tier AI_VALIDATED (operator-delegated chain)
- Rationale: SME span 'Length of a Line' on note 'Length of a Line' is anchored by the corpus spec_point block spcpt_hMqjBRzQQfvsc9f8 and joined to 4MA1-3.3G via operator-verdict name-fragment join (T-SPEC-7; PMT excluded as source); this section chunk sits inside that span.
- Verdict: [ ] CONFIRM — this chunk belongs to this SP   [ ] REJECT — wrong chunk/SP   [ ] HOLD — needs rework

### 4MA1-3.2A — understand the concept that a function is a mapping between elements of two sets
- Note: Introduction to Functions (`notes/3-sequences-functions-and-graphs/functions/functions-toolkit.json`)
- Chunk: ordinal 4 — heading `What is a mapping diagram?` — sha256_16 `1cc68490d8c4aea7` — 3230 chars
- Evidence quote (verbatim self-slice, markdown-safe): "What is a mapping diagram?
- A **mapping diagram** shows a **set of different inputs** going into the function to become a **set of different outputs**

  - Transforming inputs into outputs is called **mapping**
- For example, a mapping dia"
- Chunk excerpt: «What is a mapping diagram? - A **mapping diagram** shows a **set of different inputs** going into the function to become a **set of different outputs** - Transforming inputs into outputs is called **mapping** - For example, a mapping diagram for the function `straight f open parentheses x close parentheses equals x plus 3` where $x\geq3$ could be shown as: Diagram showing a set of input numbers being mapped over to a»
- Upstream: T-C32 join notes/3-sequences-functions-and-graphs/functions/functions-toolkit.json::spcpt_KSnrgNbPQV7FtyF5 — tier P1_name_fragment_join — score 1.0 — wording EXACT — validation tier AI_VALIDATED (operator-delegated chain)
- Rationale: SME span 'Introduction to Functions' on note 'Introduction to Functions' is anchored by the corpus spec_point block spcpt_KSnrgNbPQV7FtyF5 and joined to 4MA1-3.2A via operator-verdict name-fragment join (T-SPEC-7; PMT excluded as source); this section chunk sits inside that span.
- Verdict: [ ] CONFIRM — this chunk belongs to this SP   [ ] REJECT — wrong chunk/SP   [ ] HOLD — needs rework

### 4MA1-3.3F — calculate the gradient of a straight line given the coordinates of two points
- Note: Distance-Time Graphs (`notes/3-sequences-functions-and-graphs/real-life-graphs/distance-time-graphs.json`)
- Chunk: ordinal 1 — heading `How do I use a distance-time graph?` — sha256_16 `ae3b37586239a091` — 700 chars
- Evidence quote (verbatim self-slice, markdown-safe): "How do I use a distance-time graph?
- **Distance-time** **graphs** show the distance travelled at different times

  - **Distance** is on the **vertical** axis
  - **Time** is on the **horizontal** axis
- The **gradient** of the graph is th"
- Chunk excerpt: «How do I use a distance-time graph? - **Distance-time** **graphs** show the distance travelled at different times - **Distance** is on the **vertical** axis - **Time** is on the **horizontal** axis - The **gradient** of the graph is the **speed** - $\mathrm{speed}=\frac{\mathrm{distance}}{\mathrm{time}}=\frac{\mathrm{rise}}{\mathrm{run}}$ - The **steeper** the line the **faster **the object is moving - Lines with **p»
- Upstream: T-C32 join notes/3-sequences-functions-and-graphs/real-life-graphs/distance-time-graphs.json::spcpt_MTZDMgNSvV3FdVVR — tier P1_name_fragment_join — score 1.0 — wording EXACT — validation tier AI_VALIDATED (operator-delegated chain)
- Rationale: SME span 'Distance-Time Graphs' on note 'Distance-Time Graphs' is anchored by the corpus spec_point block spcpt_MTZDMgNSvV3FdVVR and joined to 4MA1-3.3F via operator-verdict name-fragment join (T-SPEC-7; PMT excluded as source); this section chunk sits inside that span.
- Verdict: [ ] CONFIRM — this chunk belongs to this SP   [ ] REJECT — wrong chunk/SP   [ ] HOLD — needs rework

### 4MA1-1.7C — use the process of proportionality to evaluate unknown quantities
- Note: Working with Proportion (`notes/1-numbers-and-the-number-system/ratio-toolkit/working-with-proportion.json`)
- Chunk: ordinal 1 — heading `What is direct proportion?` — sha256_16 `1e7ca0db884655c8` — 401 chars
- Evidence quote (verbatim self-slice, markdown-safe): "What is direct proportion?
- **Direct** proportion

  - As one quantity **increases/decreases** by a certain rate (factor)
  - The other quantity will **increase/decrease** by the same rate
- The **ratio** of the two quantities is **constan"
- Chunk excerpt: «What is direct proportion? - **Direct** proportion - As one quantity **increases/decreases** by a certain rate (factor) - The other quantity will **increase/decrease** by the same rate - The **ratio** of the two quantities is **constant** - E.g. 2 boxes of cereal is 800 g of cornflakes - **Doubling **the number of boxes of cereal (4 boxes) will **double** the amount of cornflakes (1600 g)»
- Upstream: T-C32 join notes/1-numbers-and-the-number-system/ratio-toolkit/working-with-proportion.json::spcpt_gqGskPX2FDtwyRh2 — tier P2_page_context_join — score 1.0 — wording EXACT — validation tier AI_VALIDATED (operator-delegated chain)
- Rationale: SME span 'Working with Proportion' on note 'Working with Proportion' is anchored by the corpus spec_point block spcpt_gqGskPX2FDtwyRh2 and joined to 4MA1-1.7C via operator-verdict page-context join (T-SPEC-7; PMT excluded as source); this section chunk sits inside that span.
- Verdict: [ ] CONFIRM — this chunk belongs to this SP   [ ] REJECT — wrong chunk/SP   [ ] HOLD — needs rework

### 4MA1-1.7B — divide a quantity in a given ratio or ratios
- Note: Multiple Ratios (`notes/1-numbers-and-the-number-system/ratio-problem-solving/multiple-ratios.json`)
- Chunk: ordinal 1 — heading `How do I combine two ratios to make a three-part ratio?` — sha256_16 `10a2401e0a8bf374` — 2011 chars
- Evidence quote (verbatim self-slice, markdown-safe): "How do I combine two ratios to make a three-part ratio?
- **Identify** the **link** between the two different ratios
- **Find equivalent ratios **for both original ratios, where the **value** of the **link** is the **same**
- **Join** the t"
- Chunk excerpt: «How do I combine two ratios to make a three-part ratio? - **Identify** the **link** between the two different ratios - **Find equivalent ratios **for both original ratios, where the **value** of the **link** is the **same** - **Join** the two, two-part ratios into a** three-part ratio** - Suppose that on a farm with 85 animals - The ratio of cows to sheep is 2:3 - The ratio of sheep to pigs is 6:7 - We want to find t»
- Upstream: T-C32 join notes/1-numbers-and-the-number-system/ratio-problem-solving/multiple-ratios.json::spcpt_qgWTSJ5pQ2dx6rDf — tier P1_name_fragment_join — score 1.0 — wording EXACT — validation tier AI_VALIDATED (operator-delegated chain)
- Rationale: SME span 'Multiple Ratios' on note 'Multiple Ratios' is anchored by the corpus spec_point block spcpt_qgWTSJ5pQ2dx6rDf and joined to 4MA1-1.7B via operator-verdict name-fragment join (T-SPEC-7; PMT excluded as source); this section chunk sits inside that span.
- Verdict: [ ] CONFIRM — this chunk belongs to this SP   [ ] REJECT — wrong chunk/SP   [ ] HOLD — needs rework

### 4MA1-3.3F — calculate the gradient of a straight line given the coordinates of two points
- Note: Drawing Straight Line Graphs (`notes/3-sequences-functions-and-graphs/linear-graphs-y-equals-mx-plus-c/drawing-straight-line-graphs.json`)
- Chunk: ordinal 3 — heading `How do I draw a straight line without using a table of values?` — sha256_16 `b4a6825850cd2e39` — 683 chars
- Evidence quote (verbatim self-slice, markdown-safe): "How do I draw a straight line without using a table of values?
- Assuming the equation is in the form ***y***** = *****mx***** + *****c***
- **Start** at the ***y*****-intercept**, *c*
- Then, for every **1 unit** to the **right**, go up **"
- Chunk excerpt: «How do I draw a straight line without using a table of values? - Assuming the equation is in the form ***y***** = *****mx***** + *****c*** - **Start** at the ***y*****-intercept**, *c* - Then, for every **1 unit** to the **right**, go up ***m *****units** - *m* is the gradient - If *m* is **negative**, go **down** - If *m* is a **fraction**, remember that gradient is change in *y* divided by change in *x* - A gradien»
- Upstream: T-C32 join notes/3-sequences-functions-and-graphs/linear-graphs-y-equals-mx-plus-c/drawing-straight-line-graphs.json::spcpt_h8QyRmzX5mCJb3X9 — tier P1_name_fragment_join — score 1.0 — wording EXACT — validation tier AI_VALIDATED (operator-delegated chain)
- Rationale: SME span 'Drawing Linear Graphs' on note 'Drawing Straight Line Graphs' is anchored by the corpus spec_point block spcpt_h8QyRmzX5mCJb3X9 and joined to 4MA1-3.3F via operator-verdict name-fragment join (T-SPEC-7; PMT excluded as source); this section chunk sits inside that span.
- Verdict: [ ] CONFIRM — this chunk belongs to this SP   [ ] REJECT — wrong chunk/SP   [ ] HOLD — needs rework

### 4MA1-1.7E — solve word problems about ratio and proportion
- Note: Sharing in a Ratio (`notes/1-numbers-and-the-number-system/ratio-toolkit/sharing-in-a-ratio.json`)
- Chunk: ordinal 3 — heading `How do I solve a ratio problem when given the difference between two parts?` — sha256_16 `7bac0a5461c405a1` — 530 chars
- Evidence quote (verbatim self-slice, markdown-safe): "How do I solve a ratio problem when given the difference between two parts?
- **Find** the **difference in the number of parts** between the two quantities in the ratio
- **Compare** the difference in the **number of parts** with the differ"
- Chunk excerpt: «How do I solve a ratio problem when given the difference between two parts? - **Find** the **difference in the number of parts** between the two quantities in the ratio - **Compare** the difference in the **number of parts** with the difference between the **actual numbers** - **Simplify** to find out the **value of one part** - **Multiply** the **value of one part **by the **number of parts** for each quantity in th»
- Upstream: T-C32 join notes/1-numbers-and-the-number-system/ratio-toolkit/sharing-in-a-ratio.json::spcpt_t6XtWBrsT7FH93JY — tier P1_name_fragment_join — score 1.0 — wording EXACT — validation tier AI_VALIDATED (operator-delegated chain)
- Rationale: SME span 'Working with Ratios' on note 'Sharing in a Ratio' is anchored by the corpus spec_point block spcpt_t6XtWBrsT7FH93JY and joined to 4MA1-1.7E via operator-verdict name-fragment join (T-SPEC-7; PMT excluded as source); this section chunk sits inside that span.
- Verdict: [ ] CONFIRM — this chunk belongs to this SP   [ ] REJECT — wrong chunk/SP   [ ] HOLD — needs rework

### 4MA1-2.2F — understand the concept of a quadratic expression and be able to factorise such expressions (limited tox + bx + c)
- Note: Difference Of Two Squares (`notes/2-equations-formulae-and-identities/factorising/difference-of-two-squares.json`)
- Chunk: ordinal 3 — heading `How can the difference of two squares be made harder?` — sha256_16 `97572a2f4a21a19b` — 1250 chars
- Evidence quote (verbatim self-slice, markdown-safe): "How can the difference of two squares be made harder?
- You may find it used with **numbers**

  - 7<sup>2</sup> - 3<sup>2</sup> = (7+3) (7-3) = (10) (4) = 40
- You can use a combination of **square numbers** and **squared variables**

  - "
- Chunk excerpt: «How can the difference of two squares be made harder? - You may find it used with **numbers** - 7<sup>2</sup> - 3<sup>2</sup> = (7+3) (7-3) = (10) (4) = 40 - You can use a combination of **square numbers** and **squared variables** - 4*m*<sup>2</sup> - 9*n*<sup>2</sup> = (2*m*)<sup>2</sup> - (3*n*)<sup>2</sup> = (2*m* + 3*n*)(2*m* - 3*n*) - You can use **other powers** which can be written as a **difference of two sq»
- Upstream: T-C32 join notes/2-equations-formulae-and-identities/factorising/difference-of-two-squares.json::spcpt_RJbgRvXq2VrGpP5g — tier P2_page_context_join — score 1.0 — wording EXACT — validation tier AI_VALIDATED (operator-delegated chain)
- Rationale: SME span 'Difference Of Two Squares' on note 'Difference Of Two Squares' is anchored by the corpus spec_point block spcpt_RJbgRvXq2VrGpP5g and joined to 4MA1-2.2F via operator-verdict page-context join (T-SPEC-7; PMT excluded as source); this section chunk sits inside that span.
- Verdict: [ ] CONFIRM — this chunk belongs to this SP   [ ] REJECT — wrong chunk/SP   [ ] HOLD — needs rework

### 4MA1-4.9E — find circumferences and areas of circles using relevant formulae; find perimeters and areas of semicircles
- Note: Area & Circumference of Circles (`notes/4-geometry-and-trigonometry/circles-arcs-and-sectors/area-and-circumference-of-circles.json`)
- Chunk: ordinal 1 — heading `What are the properties of a circle?` — sha256_16 `b93497942916bc32` — 543 chars
- Evidence quote (verbatim self-slice, markdown-safe): "What are the properties of a circle?
- A **circle** is a shape that is made up of all the points on a 2D plane that are **equidistant **from a single point

  - Equidistant means the same distance
- The **circumference** of a circle is its "
- Chunk excerpt: «What are the properties of a circle? - A **circle** is a shape that is made up of all the points on a 2D plane that are **equidistant **from a single point - Equidistant means the same distance - The **circumference** of a circle is its **perimeter** - The **diameter**, ***d***, of a circle is** twice** its** radius**, ***r*** - $π$** (pi)** is the number (3.14159 …) that is the ratio between a circle’s **diameter** »
- Upstream: T-C32 join notes/4-geometry-and-trigonometry/circles-arcs-and-sectors/area-and-circumference-of-circles.json::spcpt_Mq2w9qKSCyF5mvvs — tier P1_name_fragment_join — score 1.0 — wording EXACT — validation tier AI_VALIDATED (operator-delegated chain)
- Rationale: SME span 'Area & Circumference' on note 'Area & Circumference of Circles' is anchored by the corpus spec_point block spcpt_Mq2w9qKSCyF5mvvs and joined to 4MA1-4.9E via operator-verdict name-fragment join (T-SPEC-7; PMT excluded as source); this section chunk sits inside that span.
- Verdict: [ ] CONFIRM — this chunk belongs to this SP   [ ] REJECT — wrong chunk/SP   [ ] HOLD — needs rework

### 4MA1-2.7D — solve simultaneous equations in two unknowns, one equation being linear and the other being quadratic
- Note: Deciding the Quadratic Method (`notes/2-equations-formulae-and-identities/solving-quadratic-equations/quadratic-equation-methods.json`)
- Chunk: ordinal 3 — heading `When should I solve by completing the square?` — sha256_16 `b562de04cc4e58fa` — 4227 chars
- Evidence quote (verbatim self-slice, markdown-safe): "When should I solve by completing the square?
- Use completing the square when part (a) of a question says to **complete the square** and part (b) says to use part (a) to solve the equation
- Use completing the square when making *x* the **"
- Chunk excerpt: «When should I solve by completing the square? - Use completing the square when part (a) of a question says to **complete the square** and part (b) says to use part (a) to solve the equation - Use completing the square when making *x* the **subject of harder formulae** containing both *x*<sup>2</sup> and *x* terms - For example, make *x* the subject of the formula *x*<sup>2</sup> + 6*x* = *y* - Complete the square: (*»
- Upstream: T-C32 join notes/2-equations-formulae-and-identities/solving-quadratic-equations/quadratic-equation-methods.json::spcpt_7YTSNFdbGCTSMHJX — tier P1_name_fragment_join — score 1.0 — wording EXACT — validation tier AI_VALIDATED (operator-delegated chain)
- Rationale: SME span 'Quadratic Equation Methods' on note 'Deciding the Quadratic Method' is anchored by the corpus spec_point block spcpt_7YTSNFdbGCTSMHJX and joined to 4MA1-2.7D via operator-verdict name-fragment join (T-SPEC-7; PMT excluded as source); this section chunk sits inside that span.
- Verdict: [ ] CONFIRM — this chunk belongs to this SP   [ ] REJECT — wrong chunk/SP   [ ] HOLD — needs rework

### 4MA1-1.5C — use the notationn(A)for the number of elements in the setA
- Note: Mathematical Symbols (`notes/1-numbers-and-the-number-system/number-toolkit/mathematical-operations.json`)
- Chunk: ordinal 0 — heading `Mathematical symbols` — sha256_16 `c4363f5505339bcb` — 20 chars
- Evidence quote (verbatim self-slice, markdown-safe): "Mathematical symbols"
- Chunk excerpt: «Mathematical symbols»
- Upstream: T-C32 join notes/1-numbers-and-the-number-system/number-toolkit/mathematical-operations.json::spcpt_8Wtthy9gt8B5xsVW — tier P1_name_fragment_join — score 1.0 — wording EXACT — validation tier AI_VALIDATED (operator-delegated chain)
- Rationale: SME span 'Mathematical Symbols' on note 'Mathematical Symbols' is anchored by the corpus spec_point block spcpt_8Wtthy9gt8B5xsVW and joined to 4MA1-1.5C via operator-verdict name-fragment join (T-SPEC-7; PMT excluded as source); this section chunk sits inside that span.
- Verdict: [ ] CONFIRM — this chunk belongs to this SP   [ ] REJECT — wrong chunk/SP   [ ] HOLD — needs rework

### 4MA1-3.3H — recognise that equations of the form y = mx + care straight line graphs with gradientmand intercept on the y-axis at the point(0,c)
- Note: Equations of Straight Lines (y = mx + c) (`notes/3-sequences-functions-and-graphs/linear-graphs-y-equals-mx-plus-c/straight-line-graphs-y-equals-mx-plus-c.json`)
- Chunk: ordinal 2 — heading `How do I find the equation of a straight line from a graph?` — sha256_16 `32af1aed0db3601d` — 391 chars
- Evidence quote (verbatim self-slice, markdown-safe): "How do I find the equation of a straight line from a graph?
- Find** **the **gradient** by drawing a triangle and using

  - $\mathrm{gradient}=\frac{\mathrm{rise}}{\mathrm{run}}$
  
    - **Positive **for** **uphill** **lines, **negative *"
- Chunk excerpt: «How do I find the equation of a straight line from a graph? - Find** **the **gradient** by drawing a triangle and using - $\mathrm{gradient}=\frac{\mathrm{rise}}{\mathrm{run}}$ - **Positive **for** **uphill** **lines, **negative **for downhill - Read off the ***y*****-intercept** from the graph - Where it cuts the *y*-axis - **Substitute **these values into *y* = *mx *+* c*»
- Upstream: T-C32 join notes/3-sequences-functions-and-graphs/linear-graphs-y-equals-mx-plus-c/straight-line-graphs-y-equals-mx-plus-c.json::spcpt_2D9sp6d4f6jCmRMx — tier P1_name_fragment_join — score 1.0 — wording EXACT — validation tier AI_VALIDATED (operator-delegated chain)
- Rationale: SME span 'Finding Equations of Straight Lines' on note 'Equations of Straight Lines (y = mx + c)' is anchored by the corpus spec_point block spcpt_2D9sp6d4f6jCmRMx and joined to 4MA1-3.3H via operator-verdict name-fragment join (T-SPEC-7; PMT excluded as source); this section chunk sits inside that span.
- Verdict: [ ] CONFIRM — this chunk belongs to this SP   [ ] REJECT — wrong chunk/SP   [ ] HOLD — needs rework

### 4MA1-4.1B — use angle properties of intersecting lines, parallel lines and angles on a straight line
- Note: Basic Angle Properties (`notes/4-geometry-and-trigonometry/angles-in-polygons-and-parallel-lines/basic-angle-properties.json`)
- Chunk: ordinal 2 — heading `What are the basic angle properties?` — sha256_16 `4933ae6e3d6d2025` — 1042 chars
- Evidence quote (verbatim self-slice, markdown-safe): "What are the basic angle properties?
- Angles around a **point** add up to **360°**
- Angles that form a **straight line** add up to **180°**
- **Vertically opposite** angles are **equal**

  - Vertically opposite angles occur when **two li"
- Chunk excerpt: «What are the basic angle properties? - Angles around a **point** add up to **360°** - Angles that form a **straight line** add up to **180°** - **Vertically opposite** angles are **equal** - Vertically opposite angles occur when **two lines intersect**, as in the diagram below Vertically opposite angles Worked Example: The diagram below shows three straight lines intersecting at a point. ![Basic angle properties work»
- Upstream: T-C32 join notes/4-geometry-and-trigonometry/angles-in-polygons-and-parallel-lines/basic-angle-properties.json::spcpt_5FMXZMjqSZ3GK53q — tier P1_name_fragment_join — score 1.0 — wording EXACT — validation tier AI_VALIDATED (operator-delegated chain)
- Rationale: SME span 'Basic Angle Properties' on note 'Basic Angle Properties' is anchored by the corpus spec_point block spcpt_5FMXZMjqSZ3GK53q and joined to 4MA1-4.1B via operator-verdict name-fragment join (T-SPEC-7; PMT excluded as source); this section chunk sits inside that span.
- Verdict: [ ] CONFIRM — this chunk belongs to this SP   [ ] REJECT — wrong chunk/SP   [ ] HOLD — needs rework

### 4MA1-1.2G — convert a fraction to a decimal or a percentage
- Note: Converting Fractions, Decimals & Percentages (`notes/1-numbers-and-the-number-system/fractions-decimals-and-percentages/converting-between-fdp.json`)
- Chunk: ordinal 1 — heading `How do I convert from a percentage to a decimal?` — sha256_16 `bc049744e7c94158` — 268 chars
- Evidence quote (verbatim self-slice, markdown-safe): "How do I convert from a percentage to a decimal?
- **Divide by 100** (move digits two places to the right)

  - 6% as a decimal is 6 ÷ 100 = 0.06
  - 40% as a decimal is 40 ÷ 100 = 0.4
  - 350% as a decimal is 350 ÷ 100 = 3.5
  - 0.2% as a "
- Chunk excerpt: «How do I convert from a percentage to a decimal? - **Divide by 100** (move digits two places to the right) - 6% as a decimal is 6 ÷ 100 = 0.06 - 40% as a decimal is 40 ÷ 100 = 0.4 - 350% as a decimal is 350 ÷ 100 = 3.5 - 0.2% as a decimal is 0.2 ÷ 100 = 0.002»
- Upstream: T-C32 join notes/1-numbers-and-the-number-system/fractions-decimals-and-percentages/converting-between-fdp.json::spcpt_8MpvS5pnYkf9QswF — tier P2_page_context_join — score 1.0 — wording EXACT — validation tier AI_VALIDATED (operator-delegated chain)
- Rationale: SME span 'FDP Conversions' on note 'Converting Fractions, Decimals & Percentages' is anchored by the corpus spec_point block spcpt_8MpvS5pnYkf9QswF and joined to 4MA1-1.2G via operator-verdict page-context join (T-SPEC-7; PMT excluded as source); this section chunk sits inside that span.
- Verdict: [ ] CONFIRM — this chunk belongs to this SP   [ ] REJECT — wrong chunk/SP   [ ] HOLD — needs rework

### 4MA1-6.2B — understand the concept of a measure of spread
- Note: Averages from Tables (`notes/6-statistics-and-probability/statistics-toolkit/averages-from-tables.json`)
- Chunk: ordinal 5 — heading `How do I find the range from frequency tables?` — sha256_16 `3cd35146b8d708ec` — 265 chars
- Evidence quote (verbatim self-slice, markdown-safe): "How do I find the range from frequency tables?
- The **range** is the **difference **between the** **largest and smallest **data values**

  - The range above is 4 - 0 = 4
  
    - The range is **not** the difference between the largest and"
- Chunk excerpt: «How do I find the range from frequency tables? - The **range** is the **difference **between the** **largest and smallest **data values** - The range above is 4 - 0 = 4 - The range is **not** the difference between the largest and smallest** **frequencies»
- Upstream: T-C32 join notes/6-statistics-and-probability/statistics-toolkit/averages-from-tables.json::spcpt_QkZ2S7CKb8GrYdYx — tier P2_page_context_join — score 1.0 — wording EXACT — validation tier AI_VALIDATED (operator-delegated chain)
- Rationale: SME span 'Averages from Tables & Charts' on note 'Averages from Tables' is anchored by the corpus spec_point block spcpt_QkZ2S7CKb8GrYdYx and joined to 4MA1-6.2B via operator-verdict page-context join (T-SPEC-7; PMT excluded as source); this section chunk sits inside that span.
- Verdict: [ ] CONFIRM — this chunk belongs to this SP   [ ] REJECT — wrong chunk/SP   [ ] HOLD — needs rework

### 4MA1-4.8A — understand and use sine, cosine and tangent of obtuse angles
- Note: Pythagoras Theorem (`notes/4-geometry-and-trigonometry/right-angled-triangles---pythagoras-and-trigonometry/pythagoras-theorem.json`)
- Chunk: ordinal 1 — heading `Who is Pythagoras?` — sha256_16 `78bc7bd63488f9af` — 212 chars
- Evidence quote (verbatim self-slice, markdown-safe): "Who is Pythagoras?
- **Pythagoras** was a **Greek mathematician** who lived over 2500 years ago
- He is most famous for **Pythagoras’ theorem**, which includes the important formula for **right-angled triangles**"
- Chunk excerpt: «Who is Pythagoras? - **Pythagoras** was a **Greek mathematician** who lived over 2500 years ago - He is most famous for **Pythagoras’ theorem**, which includes the important formula for **right-angled triangles**»
- Upstream: T-C32 join notes/4-geometry-and-trigonometry/right-angled-triangles---pythagoras-and-trigonometry/pythagoras-theorem.json::spcpt_XWwgtKhQDRhyY5m4 — tier P1_name_fragment_join — score 1.0 — wording EXACT — validation tier AI_VALIDATED (operator-delegated chain)
- Rationale: SME span 'Pythagoras Theorem' on note 'Pythagoras Theorem' is anchored by the corpus spec_point block spcpt_XWwgtKhQDRhyY5m4 and joined to 4MA1-4.8A via operator-verdict name-fragment join (T-SPEC-7; PMT excluded as source); this section chunk sits inside that span.
- Verdict: [ ] CONFIRM — this chunk belongs to this SP   [ ] REJECT — wrong chunk/SP   [ ] HOLD — needs rework

### 4MA1-1.1F — use brackets and the hierarchy of operations
- Note: Order of Operations (BIDMAS/BODMAS) (`notes/1-numbers-and-the-number-system/number-toolkit/order-of-operations-bidmas-bodmas.json`)
- Chunk: ordinal 2 — heading `In what order should fractions and roots be dealt with?` — sha256_16 `bc6126ac5fbac321` — 769 chars
- Evidence quote (verbatim self-slice, markdown-safe): "In what order should fractions and roots be dealt with?
- **Fractions** mean **division** in calculations (BI**D**MAS/BO**D**MAS)
- There may be "invisible brackets" around the numerator and around the denominator

  - e.g.  $\frac{2+5}{7-2"
- Chunk excerpt: «In what order should fractions and roots be dealt with? - **Fractions** mean **division** in calculations (BI**D**MAS/BO**D**MAS) - There may be "invisible brackets" around the numerator and around the denominator - e.g. $\frac{2+5}{7-2}$ means `open parentheses 2 plus 5 close parentheses divided by open parentheses 7 minus 2 close parentheses` - Instead of brackets we extend the fraction line to show exactly what is»
- Upstream: T-C32 join notes/1-numbers-and-the-number-system/number-toolkit/order-of-operations-bidmas-bodmas.json::spcpt_c25SPBnps9dhX2Dk — tier P1_name_fragment_join — score 1.0 — wording EXACT — validation tier AI_VALIDATED (operator-delegated chain)
- Rationale: SME span 'Order of Operations (BIDMAS/BODMAS)' on note 'Order of Operations (BIDMAS/BODMAS)' is anchored by the corpus spec_point block spcpt_c25SPBnps9dhX2Dk and joined to 4MA1-1.1F via operator-verdict name-fragment join (T-SPEC-7; PMT excluded as source); this section chunk sits inside that span.
- Verdict: [ ] CONFIRM — this chunk belongs to this SP   [ ] REJECT — wrong chunk/SP   [ ] HOLD — needs rework

### 4MA1-3.3I — recognise, generate points and plot graphs of linear and quadratic functions
- Note: Inverse Functions (`notes/3-sequences-functions-and-graphs/functions/inverse-functions.json`)
- Chunk: ordinal 2 — heading `What notation is used for inverse functions?` — sha256_16 `f3e473804803a731` — 1043 chars
- Evidence quote (verbatim self-slice, markdown-safe): "What notation is used for inverse functions?
- The inverse function of `straight f open parentheses x close parentheses` is written as $f^{-1}(x)=\dots$ or  `straight f to the power of negative 1 end exponent colon space x rightwards arrow "
- Chunk excerpt: «What notation is used for inverse functions? - The inverse function of `straight f open parentheses x close parentheses` is written as $f^{-1}(x)=\dots$ or `straight f to the power of negative 1 end exponent colon space x rightwards arrow from bar horizontal ellipsis` - For example, if $f(x)=2x+1$ - The inverse function is $f^{-1}(x)=\frac{x-1}{2}$ or `straight f to the power of negative 1 end exponent colon space x »
- Upstream: T-C32 join notes/3-sequences-functions-and-graphs/functions/inverse-functions.json::spcpt_TZkZ5ZK4bRYdjnGY — tier P1_name_fragment_join — score 1.0 — wording EXACT — validation tier AI_VALIDATED (operator-delegated chain)
- Rationale: SME span 'Inverse Functions' on note 'Inverse Functions' is anchored by the corpus spec_point block spcpt_TZkZ5ZK4bRYdjnGY and joined to 4MA1-3.3I via operator-verdict name-fragment join (T-SPEC-7; PMT excluded as source); this section chunk sits inside that span.
- Verdict: [ ] CONFIRM — this chunk belongs to this SP   [ ] REJECT — wrong chunk/SP   [ ] HOLD — needs rework

### 4MA1-6.2B — understand the concept of a measure of spread
- Note: Averages from Tables (`notes/6-statistics-and-probability/statistics-toolkit/averages-from-tables.json`)
- Chunk: ordinal 2 — heading `How do I find the mode from a frequency table?` — sha256_16 `41e11fbc51314392` — 269 chars
- Evidence quote (verbatim self-slice, markdown-safe): "How do I find the mode from a frequency table?
- The **mode** is the **data value** with the **highest frequency**

  - The mode for the example above is 1 pet per house
  
    - The mode is **not** the frequency, 7, this is the number of h"
- Chunk excerpt: «How do I find the mode from a frequency table? - The **mode** is the **data value** with the **highest frequency** - The mode for the example above is 1 pet per house - The mode is **not** the frequency, 7, this is the number of houses that have exactly 1 pet»
- Upstream: T-C32 join notes/6-statistics-and-probability/statistics-toolkit/averages-from-tables.json::spcpt_QkZ2S7CKb8GrYdYx — tier P2_page_context_join — score 1.0 — wording EXACT — validation tier AI_VALIDATED (operator-delegated chain)
- Rationale: SME span 'Averages from Tables & Charts' on note 'Averages from Tables' is anchored by the corpus spec_point block spcpt_QkZ2S7CKb8GrYdYx and joined to 4MA1-6.2B via operator-verdict page-context join (T-SPEC-7; PMT excluded as source); this section chunk sits inside that span.
- Verdict: [ ] CONFIRM — this chunk belongs to this SP   [ ] REJECT — wrong chunk/SP   [ ] HOLD — needs rework

### 4MA1-2.2E — use algebra to support and construct proofs
- Note: Expanding Double Brackets (`notes/2-equations-formulae-and-identities/expanding-brackets/expanding-double-brackets.json`)
- Chunk: ordinal 1 — heading `How do I expand two brackets?` — sha256_16 `e9635ccc331451e3` — 310 chars
- Evidence quote (verbatim self-slice, markdown-safe): "How do I expand two brackets?
- **Every term** in the** first** bracket must be multiplied by **every term** in the **second** bracket

  - Expanding (*x * + 1)(*x*  + 3) requires 4 multiplications in total
  
    - *x*(*x*  + 1) + 3(*x * +"
- Chunk excerpt: «How do I expand two brackets? - **Every term** in the** first** bracket must be multiplied by **every term** in the **second** bracket - Expanding (*x * + 1)(*x* + 3) requires 4 multiplications in total - *x*(*x* + 1) + 3(*x * + 1) - *x*×*x *+ 1*x* + 3*x* + 3 - *x*<sup>2</sup> + 4*x* + 3»
- Upstream: T-C32 join notes/2-equations-formulae-and-identities/expanding-brackets/expanding-double-brackets.json::spcpt_S2dfVTzRhCh7pRzW — tier P1_name_fragment_join — score 1.0 — wording EXACT — validation tier AI_VALIDATED (operator-delegated chain)
- Rationale: SME span 'Expanding Two Brackets' on note 'Expanding Double Brackets' is anchored by the corpus spec_point block spcpt_S2dfVTzRhCh7pRzW and joined to 4MA1-2.2E via operator-verdict name-fragment join (T-SPEC-7; PMT excluded as source); this section chunk sits inside that span.
- Verdict: [ ] CONFIRM — this chunk belongs to this SP   [ ] REJECT — wrong chunk/SP   [ ] HOLD — needs rework

### 4MA1-4.2C — understand and use the properties of the parallelogram, rectangle, square, rhombus, trapezium and kite
- Note: 2D Shapes (`notes/4-geometry-and-trigonometry/angles-in-polygons-and-parallel-lines/properties-of-2d-shapes.json`)
- Chunk: ordinal 5 — heading `What are the properties of parallelograms and rhombuses?` — sha256_16 `b15c438bec995bb1` — 880 chars
- Evidence quote (verbatim self-slice, markdown-safe): "What are the properties of parallelograms and rhombuses?
- A **rhombus **is a **parallelogram **where all the **sides **have the **same length**
- The table below shows the **properties **of a parallelogram and rhombus
Parallelogram
|   | P"
- Chunk excerpt: «What are the properties of parallelograms and rhombuses? - A **rhombus **is a **parallelogram **where all the **sides **have the **same length** - The table below shows the **properties **of a parallelogram and rhombus Parallelogram | | Parallelogram | Rhombus | |---|---|---| | Sides | - Two pairs of equal, opposite sides<br>- Two pairs of parallel sides | - All sides have the same length<br>- Two pairs of parallel s»
- Upstream: T-C32 join notes/4-geometry-and-trigonometry/angles-in-polygons-and-parallel-lines/properties-of-2d-shapes.json::spcpt_SVXT7VrWxFMXkD7D — tier P2_page_context_join — score 1.0 — wording EXACT — validation tier AI_VALIDATED (operator-delegated chain)
- Rationale: SME span 'Properties of 2D Shapes' on note '2D Shapes' is anchored by the corpus spec_point block spcpt_SVXT7VrWxFMXkD7D and joined to 4MA1-4.2C via operator-verdict page-context join (T-SPEC-7; PMT excluded as source); this section chunk sits inside that span.
- Verdict: [ ] CONFIRM — this chunk belongs to this SP   [ ] REJECT — wrong chunk/SP   [ ] HOLD — needs rework

### 4MA1-6.1C — use cumulative frequency diagrams
- Note: Representing Vectors as Diagrams (`notes/5-vectors-and-transformation-geometry/vectors/representing-vectors-as-diagrams.json`)
- Chunk: ordinal 2 — heading `What happens when a vector is multiplied by a scalar?` — sha256_16 `a126c472b6b52a82` — 484 chars
- Evidence quote (verbatim self-slice, markdown-safe): "What happens when a vector is multiplied by a scalar?
- When you **multiply** a vector by a** positive scalar**:

  - The **direction** stays the **same**
  - The **length** of the vector is **multiplied by the scalar**
Multiplying vectors "
- Chunk excerpt: «What happens when a vector is multiplied by a scalar? - When you **multiply** a vector by a** positive scalar**: - The **direction** stays the **same** - The **length** of the vector is **multiplied by the scalar** Multiplying vectors by a scalar - When you **multiply** a vector by a **negative scalar**: - The **direction** is **reversed** - The** length** of the vector is **multiplied** by the **number after the neg»
- Upstream: T-C32 join notes/5-vectors-and-transformation-geometry/vectors/representing-vectors-as-diagrams.json::spcpt_wt9snSTkmXqhMvXn — tier P1_name_fragment_join — score 1.0 — wording EXACT — validation tier AI_VALIDATED (operator-delegated chain)
- Rationale: SME span 'Vector Diagrams' on note 'Representing Vectors as Diagrams' is anchored by the corpus spec_point block spcpt_wt9snSTkmXqhMvXn and joined to 4MA1-6.1C via operator-verdict name-fragment join (T-SPEC-7; PMT excluded as source); this section chunk sits inside that span.
- Verdict: [ ] CONFIRM — this chunk belongs to this SP   [ ] REJECT — wrong chunk/SP   [ ] HOLD — needs rework

### 4MA1-4.8D — use Pythagoras’ theorem in three dimensions
- Note: 3D Pythagoras & Trigonometry (`notes/4-geometry-and-trigonometry/3d-pythagoras-and-trigonometry/3d-pythagoras-and-trigonometry.json`)
- Chunk: ordinal 5 — heading `How do I apply 3D Pythagoras and trigonometry to more complicated problems?` — sha256_16 `05839cfac86290ed` — 4356 chars
- Evidence quote (verbatim self-slice, markdown-safe): "How do I apply 3D Pythagoras and trigonometry to more complicated problems?
- Always split up a complicated problem into **2D right-angled triangles**

  - Some questions may require more than one 2D right-angled triangle
- Some 2D triangle"
- Chunk excerpt: «How do I apply 3D Pythagoras and trigonometry to more complicated problems? - Always split up a complicated problem into **2D right-angled triangles** - Some questions may require more than one 2D right-angled triangle - Some 2D triangles on the diagram are still drawn in 3D - It helps to** redraw **these 2D triangles **flat on the page** (not at angles) - You can then spot any uses of Pythagoras' theorem and SOHCAHT»
- Upstream: T-C32 join notes/4-geometry-and-trigonometry/3d-pythagoras-and-trigonometry/3d-pythagoras-and-trigonometry.json::spcpt_kX4655D8M3Q3TRzW — tier P1_name_fragment_join — score 1.0 — wording EXACT — validation tier AI_VALIDATED (operator-delegated chain)
- Rationale: SME span '3D Pythagoras & Trigonometry' on note '3D Pythagoras & Trigonometry' is anchored by the corpus spec_point block spcpt_kX4655D8M3Q3TRzW and joined to 4MA1-4.8D via operator-verdict name-fragment join (T-SPEC-7; PMT excluded as source); this section chunk sits inside that span.
- Verdict: [ ] CONFIRM — this chunk belongs to this SP   [ ] REJECT — wrong chunk/SP   [ ] HOLD — needs rework

### 4MA1-3.4C — determine gradients, rates of change, stationary points, turning points (maxima and minima) by differentiation and relate these to graphs
- Note: Finding Gradients of Tangents (`notes/3-sequences-functions-and-graphs/estimating-gradients/finding-gradients-of-tangents.json`)
- Chunk: ordinal 1 — heading `How are the gradients of graphs and tangents related?` — sha256_16 `e35752457fa0fbfe` — 476 chars
- Evidence quote (verbatim self-slice, markdown-safe): "How are the gradients of graphs and tangents related?
- The **gradient of a graph at a point** is **equal** to the **gradient of the tangent** to the curve **at that point**

  - A tangent is a line that touches a curve, but does not cross "
- Chunk excerpt: «How are the gradients of graphs and tangents related? - The **gradient of a graph at a point** is **equal** to the **gradient of the tangent** to the curve **at that point** - A tangent is a line that touches a curve, but does not cross it A quadratic with two tangents drawn on it. The gradient of the curve at the point x=1 will be equal to the gradient of the purple tangent. The gradient of the curve at th epoint x=»
- Upstream: T-C32 join notes/3-sequences-functions-and-graphs/estimating-gradients/finding-gradients-of-tangents.json::spcpt_zrrC3yxSp579jY7k — tier P2_page_context_join — score 1.0 — wording EXACT — validation tier AI_VALIDATED (operator-delegated chain)
- Rationale: SME span 'Finding Gradients of Tangents' on note 'Finding Gradients of Tangents' is anchored by the corpus spec_point block spcpt_zrrC3yxSp579jY7k and joined to 4MA1-3.4C via operator-verdict page-context join (T-SPEC-7; PMT excluded as source); this section chunk sits inside that span.
- Verdict: [ ] CONFIRM — this chunk belongs to this SP   [ ] REJECT — wrong chunk/SP   [ ] HOLD — needs rework

### 4MA1-4.5D — use straight edge and compasses to: (i) construct the perpendicular bisector of a line segment (ii) construct the bisector of an angle
- Note: Constructions (`notes/4-geometry-and-trigonometry/bearings-scale-drawing-and-constructions/constructions.json`)
- Chunk: ordinal 2 — heading `How do I construct the perpendicular bisector of a line?` — sha256_16 `35d0ca4a6d2bf68a` — 691 chars
- Evidence quote (verbatim self-slice, markdown-safe): "How do I construct the perpendicular bisector of a line?
- **STEP 1**
Set the **distance** between the point of the **compasses** and the pencil to be **more than half the length** of the line
- **STEP 2**
Place the point of the compasses *"
- Chunk excerpt: «How do I construct the perpendicular bisector of a line? - **STEP 1** Set the **distance** between the point of the **compasses** and the pencil to be **more than half the length** of the line - **STEP 2** Place the point of the compasses **on one end** of the line and sketch an **arc **above and below the line - **STEP 3** Keeping your compasses **set to the same distance**, place the point of the compasses on **the»
- Upstream: T-C32 join notes/4-geometry-and-trigonometry/bearings-scale-drawing-and-constructions/constructions.json::spcpt_yDbZQ6WS99WPCvvR — tier P1_name_fragment_join — score 1.0 — wording EXACT — validation tier AI_VALIDATED (operator-delegated chain)
- Rationale: SME span 'Constructions' on note 'Constructions' is anchored by the corpus spec_point block spcpt_yDbZQ6WS99WPCvvR and joined to 4MA1-4.5D via operator-verdict name-fragment join (T-SPEC-7; PMT excluded as source); this section chunk sits inside that span.
- Verdict: [ ] CONFIRM — this chunk belongs to this SP   [ ] REJECT — wrong chunk/SP   [ ] HOLD — needs rework

### 4MA1-1.2G — convert a fraction to a decimal or a percentage
- Note: Converting Fractions, Decimals & Percentages (`notes/1-numbers-and-the-number-system/fractions-decimals-and-percentages/converting-between-fdp.json`)
- Chunk: ordinal 6 — heading `How do I convert from a fraction to a percentage?` — sha256_16 `553774dff1c2a4e2` — 349 chars
- Evidence quote (verbatim self-slice, markdown-safe): "How do I convert from a fraction to a percentage?
- Change fractions into **decimals** then **multiply by 100**

  - $\frac{4}{5}=\frac{8}{10}$ which is 0.8 as a decimal, which is 0.8 × 100 = 80%
Exam Hint: A calculator can be used to check"
- Chunk excerpt: «How do I convert from a fraction to a percentage? - Change fractions into **decimals** then **multiply by 100** - $\frac{4}{5}=\frac{8}{10}$ which is 0.8 as a decimal, which is 0.8 × 100 = 80% Exam Hint: A calculator can be used to check conversions between fractions and decimals (even if the question says to show working without a calculator).»
- Upstream: T-C32 join notes/1-numbers-and-the-number-system/fractions-decimals-and-percentages/converting-between-fdp.json::spcpt_8MpvS5pnYkf9QswF — tier P2_page_context_join — score 1.0 — wording EXACT — validation tier AI_VALIDATED (operator-delegated chain)
- Rationale: SME span 'FDP Conversions' on note 'Converting Fractions, Decimals & Percentages' is anchored by the corpus spec_point block spcpt_8MpvS5pnYkf9QswF and joined to 4MA1-1.2G via operator-verdict page-context join (T-SPEC-7; PMT excluded as source); this section chunk sits inside that span.
- Verdict: [ ] CONFIRM — this chunk belongs to this SP   [ ] REJECT — wrong chunk/SP   [ ] HOLD — needs rework

### 4MA1-4.5B — construct triangles and other two-dimensional shapes using a combination of a ruler, a protractor and compasses
- Note: Constructing Triangles (`notes/4-geometry-and-trigonometry/bearings-scale-drawing-and-constructions/constructing-triangles.json`)
- Chunk: ordinal 0 — heading `Constructing triangles` — sha256_16 `c7c06c2050dc56e0` — 22 chars
- Evidence quote (verbatim self-slice, markdown-safe): "Constructing triangles"
- Chunk excerpt: «Constructing triangles»
- Upstream: T-C32 join notes/4-geometry-and-trigonometry/bearings-scale-drawing-and-constructions/constructing-triangles.json::spcpt_RXP6GyfJydf7Kggr — tier P1_name_fragment_join — score 1.0 — wording EXACT — validation tier AI_VALIDATED (operator-delegated chain)
- Rationale: SME span 'Constructing Triangles' on note 'Constructing Triangles' is anchored by the corpus spec_point block spcpt_RXP6GyfJydf7Kggr and joined to 4MA1-4.5B via operator-verdict name-fragment join (T-SPEC-7; PMT excluded as source); this section chunk sits inside that span.
- Verdict: [ ] CONFIRM — this chunk belongs to this SP   [ ] REJECT — wrong chunk/SP   [ ] HOLD — needs rework

### 4MA1-4.5B — construct triangles and other two-dimensional shapes using a combination of a ruler, a protractor and compasses
- Note: Constructing Triangles (`notes/4-geometry-and-trigonometry/bearings-scale-drawing-and-constructions/constructing-triangles.json`)
- Chunk: ordinal 1 — heading `What are triangle constructions?` — sha256_16 `e7f4d69b686d36e3` — 740 chars
- Evidence quote (verbatim self-slice, markdown-safe): "What are triangle constructions?
- A **triangle construction **is an accurate drawing that usually uses:

  - a sharp **pencil**
  - a **ruler**
  - a **protractor**
  - and/or a pair of **compasses**
- You will be given information about t"
- Chunk excerpt: «What are triangle constructions? - A **triangle construction **is an accurate drawing that usually uses: - a sharp **pencil** - a **ruler** - a **protractor** - and/or a pair of **compasses** - You will be given information about the size of some of the **angles** and/or **sides** of a triangle - Depending on the type of triangle, you will need to follow a specific method and you may need different equipment - The ty»
- Upstream: T-C32 join notes/4-geometry-and-trigonometry/bearings-scale-drawing-and-constructions/constructing-triangles.json::spcpt_RXP6GyfJydf7Kggr — tier P1_name_fragment_join — score 1.0 — wording EXACT — validation tier AI_VALIDATED (operator-delegated chain)
- Rationale: SME span 'Constructing Triangles' on note 'Constructing Triangles' is anchored by the corpus spec_point block spcpt_RXP6GyfJydf7Kggr and joined to 4MA1-4.5B via operator-verdict name-fragment join (T-SPEC-7; PMT excluded as source); this section chunk sits inside that span.
- Verdict: [ ] CONFIRM — this chunk belongs to this SP   [ ] REJECT — wrong chunk/SP   [ ] HOLD — needs rework

### 4MA1-4.11C — use areas and volumes of similar figures in solving problems
- Note: Problem Solving with Areas (`notes/4-geometry-and-trigonometry/area-and-perimeter/problem-solving-with-areas.json`)
- Chunk: ordinal 0 — heading `Problem-solving with areas` — sha256_16 `91e4696b0d58b260` — 26 chars
- Evidence quote (verbatim self-slice, markdown-safe): "Problem-solving with areas"
- Chunk excerpt: «Problem-solving with areas»
- Upstream: T-C32 join notes/4-geometry-and-trigonometry/area-and-perimeter/problem-solving-with-areas.json::spcpt_3fMGfNtg3hXMg6gC — tier P1_name_fragment_join — score 1.0 — wording EXACT — validation tier AI_VALIDATED (operator-delegated chain)
- Rationale: SME span 'Problem Solving with Areas' on note 'Problem Solving with Areas' is anchored by the corpus spec_point block spcpt_3fMGfNtg3hXMg6gC and joined to 4MA1-4.11C via operator-verdict name-fragment join (T-SPEC-7; PMT excluded as source); this section chunk sits inside that span.
- Verdict: [ ] CONFIRM — this chunk belongs to this SP   [ ] REJECT — wrong chunk/SP   [ ] HOLD — needs rework

### 4MA1-1.4C — use index laws to simplify and evaluate numerical expressions involving integer, fractional and negative powers
- Note: Laws of Indices (`notes/1-numbers-and-the-number-system/powers-roots-and-standard-form/laws-of-indices.json`)
- Chunk: ordinal 1 — heading `What are the laws of indices?` — sha256_16 `4560e2cc278905a0` — 4523 chars
- Evidence quote (verbatim self-slice, markdown-safe): "What are the laws of indices?
- **Index laws **are** rules** you can use when doing **operations** with **powers**

  - They work with both **numbers **and **algebra**
| **Law** | **Description** | **How it works** |
|---|---|---|
| $a^{1}="
- Chunk excerpt: «What are the laws of indices? - **Index laws **are** rules** you can use when doing **operations** with **powers** - They work with both **numbers **and **algebra** | **Law** | **Description** | **How it works** | |---|---|---| | $a^{1}=a$ | Anything to the power of 1 is itself | $6^{1}=6$ | | $a^{0}=1$ | Anything to the power of 0 is 1 | $8^{0}=1$ | | $a^{m}\timesa^{n}=a^{m+n}$ | To multiply indices with the same ba»
- Upstream: T-C32 join notes/1-numbers-and-the-number-system/powers-roots-and-standard-form/laws-of-indices.json::spcpt_W6x4XqqqZWnY5SZc — tier P1_name_fragment_join — score 1.0 — wording EXACT — validation tier AI_VALIDATED (operator-delegated chain)
- Rationale: SME span 'Laws of Indices' on note 'Laws of Indices' is anchored by the corpus spec_point block spcpt_W6x4XqqqZWnY5SZc and joined to 4MA1-1.4C via operator-verdict name-fragment join (T-SPEC-7; PMT excluded as source); this section chunk sits inside that span.
- Verdict: [ ] CONFIRM — this chunk belongs to this SP   [ ] REJECT — wrong chunk/SP   [ ] HOLD — needs rework

### 4MA1-2.2F — understand the concept of a quadratic expression and be able to factorise such expressions (limited tox + bx + c)
- Note: Factorising Simple Quadratics (`notes/2-equations-formulae-and-identities/factorising/factorising-quadratics.json`)
- Chunk: ordinal 3 — heading `How do I factorise quadratics by grouping?` — sha256_16 `583b4e0396682bf6` — 965 chars
- Evidence quote (verbatim self-slice, markdown-safe): "How do I factorise quadratics by grouping?
- This is shown most easily through an example: factorising $x^{2}-2x-8$
- We need a **pair of numbers** that for $x^{2}+bx+c$

  - **multiply** to give *c*
  
    - which in this case is -8
  - an"
- Chunk excerpt: «How do I factorise quadratics by grouping? - This is shown most easily through an example: factorising $x^{2}-2x-8$ - We need a **pair of numbers** that for $x^{2}+bx+c$ - **multiply** to give *c* - which in this case is -8 - and **add** to give* b* - which in this case is -2 - +2 and -4 satisfy these conditions - 2 × (-4) = -8 and 2 + (-4) = -2 - **Rewrite** the middle term by using +2*x* and -4*x* - $x^{2}+2x-4x-8$»
- Upstream: T-C32 join notes/2-equations-formulae-and-identities/factorising/factorising-quadratics.json::spcpt_7pTpRYh7tsCnGspT — tier P1_name_fragment_join — score 1.0 — wording EXACT — validation tier AI_VALIDATED (operator-delegated chain)
- Rationale: SME span 'Factorising Simple Quadratics' on note 'Factorising Simple Quadratics' is anchored by the corpus spec_point block spcpt_7pTpRYh7tsCnGspT and joined to 4MA1-2.2F via operator-verdict name-fragment join (T-SPEC-7; PMT excluded as source); this section chunk sits inside that span.
- Verdict: [ ] CONFIRM — this chunk belongs to this SP   [ ] REJECT — wrong chunk/SP   [ ] HOLD — needs rework

### 4MA1-4.6C — understand and use angle properties of the circle including: (i) angle subtended by an arc at the centre of a circle is twice the angle subtended at any point on the remaining part of the circumference (ii) angle subtended at the circumference by a diameter is a right angle (iii) angles in the same segment are equal (iv) the sum of the opposite angles of a cyclic quadrilateral is180° (v) the alternate segment theorem
- Note: Angles at Centre & Circumference (`notes/4-geometry-and-trigonometry/circle-theorems/angles-at-centre-and-semicircles.json`)
- Chunk: ordinal 0 — heading `Angles at centre & circumference` — sha256_16 `75f724a5fc202a45` — 32 chars
- Evidence quote (verbatim self-slice, markdown-safe): "Angles at centre & circumference"
- Chunk excerpt: «Angles at centre & circumference»
- Upstream: T-C32 join notes/4-geometry-and-trigonometry/circle-theorems/angles-at-centre-and-semicircles.json::spcpt_wPBshqzwKBKyYHBV — tier P1_name_fragment_join — score 1.0 — wording EXACT — validation tier AI_VALIDATED (operator-delegated chain)
- Rationale: SME span 'Angles at Centre & Circumference' on note 'Angles at Centre & Circumference' is anchored by the corpus spec_point block spcpt_wPBshqzwKBKyYHBV and joined to 4MA1-4.6C via operator-verdict name-fragment join (T-SPEC-7; PMT excluded as source); this section chunk sits inside that span.
- Verdict: [ ] CONFIRM — this chunk belongs to this SP   [ ] REJECT — wrong chunk/SP   [ ] HOLD — needs rework

### 4MA1-3.1A — understand and use common difference (d)and first term(a)in an arithmetic sequence
- Note: Introduction to Sequences (`notes/3-sequences-functions-and-graphs/sequences/introduction-to-sequences.json`)
- Chunk: ordinal 2 — heading `How do I write out a sequence using a term-to-term rule?` — sha256_16 `2aaaac5f768baad8` — 501 chars
- Evidence quote (verbatim self-slice, markdown-safe): "How do I write out a sequence using a term-to-term rule?
- **Term-to-term** **rules** tell you how to get the **next term** from the term you are on

  - It is what you do **each time**
  - For example, starting on 4, add 10 each time
  
  "
- Chunk excerpt: «How do I write out a sequence using a term-to-term rule? - **Term-to-term** **rules** tell you how to get the **next term** from the term you are on - It is what you do **each time** - For example, starting on 4, add 10 each time - 4, 14, 24, 34, ... - The common term-to-term rules are: - **adding or subtracting** a number - 3, 7, 11, 15, ... the rule is add 4 each time - **multiplying or dividing** by a number - 2, »
- Upstream: T-C32 join notes/3-sequences-functions-and-graphs/sequences/introduction-to-sequences.json::spcpt_NNhjQfXtS7sNJyHD — tier P1_name_fragment_join — score 1.0 — wording EXACT — validation tier AI_VALIDATED (operator-delegated chain)
- Rationale: SME span 'Introduction to Sequences' on note 'Introduction to Sequences' is anchored by the corpus spec_point block spcpt_NNhjQfXtS7sNJyHD and joined to 4MA1-3.1A via operator-verdict name-fragment join (T-SPEC-7; PMT excluded as source); this section chunk sits inside that span.
- Verdict: [ ] CONFIRM — this chunk belongs to this SP   [ ] REJECT — wrong chunk/SP   [ ] HOLD — needs rework

### 4MA1-3.4C — determine gradients, rates of change, stationary points, turning points (maxima and minima) by differentiation and relate these to graphs
- Note: Exchange Rates (`notes/1-numbers-and-the-number-system/exchange-rates-and-best-buys/exchange-rates.json`)
- Chunk: ordinal 1 — heading `How do I convert between currencies?` — sha256_16 `bd8160d5916d360b` — 1557 chars
- Evidence quote (verbatim self-slice, markdown-safe): "How do I convert between currencies?
- Start by writing the **exchange rate**

  - £1.00 (GBP) = €1.17 (EUR)
- To convert **from GBP to EUR**, **multiply **by 1.17

  - Because 1.00 × 1.17 = 1.17
- To convert **from EUR to GBP**, **divide *"
- Chunk excerpt: «How do I convert between currencies? - Start by writing the **exchange rate** - £1.00 (GBP) = €1.17 (EUR) - To convert **from GBP to EUR**, **multiply **by 1.17 - Because 1.00 × 1.17 = 1.17 - To convert **from EUR to GBP**, **divide **by 1.17 - Because 1.17 ÷ 1.17 = 1.00 - To find £28 in Euros - 28 × 1.17 = €32.76 - To find €75 in Pounds - 75 ÷ 1.17 = £64.10 (to the nearest penny) Exam Hint: If you can't work out whe»
- Upstream: T-C32 join notes/1-numbers-and-the-number-system/exchange-rates-and-best-buys/exchange-rates.json::spcpt_XC6PSG6CcXnNDb3Q — tier P1_name_fragment_join — score 1.0 — wording EXACT — validation tier AI_VALIDATED (operator-delegated chain)
- Rationale: SME span 'Exchange Rates' on note 'Exchange Rates' is anchored by the corpus spec_point block spcpt_XC6PSG6CcXnNDb3Q and joined to 4MA1-3.4C via operator-verdict name-fragment join (T-SPEC-7; PMT excluded as source); this section chunk sits inside that span.
- Verdict: [ ] CONFIRM — this chunk belongs to this SP   [ ] REJECT — wrong chunk/SP   [ ] HOLD — needs rework

### 4MA1-3.3B — apply to the graph ofy = f(x)the transformations y = f(x) + a, y = f(ax), y = f(x + a), y = af(x) for linear, quadratic, sine and cosine functions
- Note: Stretches of Graphs (`notes/3-sequences-functions-and-graphs/transformations-of-graphs/stretches-of-graphs.json`)
- Chunk: ordinal 3 — heading `Vertical stretches: y=af(x)` — sha256_16 `23c02caa8372ad36` — 642 chars
- Evidence quote (verbatim self-slice, markdown-safe): "Vertical stretches: y=af(x)
- `y equals a straight f open parentheses x close parentheses` is a **vertical stretch **(in the $y$-direction) of **scale factor **$a$

  - The $x$-coordinates stay the same but the $y$ coordinates are multiplie"
- Chunk excerpt: «Vertical stretches: y=af(x) - `y equals a straight f open parentheses x close parentheses` is a **vertical stretch **(in the $y$-direction) of **scale factor **$a$ - The $x$-coordinates stay the same but the $y$ coordinates are multiplied by $a$ - Points appear to move **parallel to the **$y$**-axis** - either stretching vertically away from the $x$-axis if $a>1$ - or squashing vertically towards the $x$-axis if $0<a»
- Upstream: T-C32 join notes/3-sequences-functions-and-graphs/transformations-of-graphs/stretches-of-graphs.json::spcpt_YcMPxJgtrjtBzMkV — tier P2_operator_content_join — score n/a — wording EXACT — validation tier AI_VALIDATED (operator-delegated chain)
- Rationale: SME span 'Stretches of Graphs' on note 'Stretches of Graphs' is anchored by the corpus spec_point block spcpt_YcMPxJgtrjtBzMkV and joined to 4MA1-3.3B via T-SPEC-9 operator verdict (no upstream; PMT excluded as source); this section chunk sits inside that span.
- Verdict: [ ] CONFIRM — this chunk belongs to this SP   [ ] REJECT — wrong chunk/SP   [ ] HOLD — needs rework

### 4MA1-6.3A — draw and use tree diagrams
- Note: Combined Probability (`notes/6-statistics-and-probability/combined-and-conditional-probability/combined-probability.json`)
- Chunk: ordinal 2 — heading `What does independent mean?` — sha256_16 `9e459240211f4fd6` — 1573 chars
- Evidence quote (verbatim self-slice, markdown-safe): "What does independent mean?
- **Independent events **are events that **do not affect** each other

  - e.g. the probability of rolling a 6 on a fair dice and the probability of getting a head when flipping a coin
- Be careful: questions 'wi"
- Chunk excerpt: «What does independent mean? - **Independent events **are events that **do not affect** each other - e.g. the probability of rolling a 6 on a fair dice and the probability of getting a head when flipping a coin - Be careful: questions 'without replacement' are **not** independent - e.g. the probability of taking a red card out of a pack, not replacing it, then finding the probability of taking a second red card out of»
- Upstream: T-C32 join notes/6-statistics-and-probability/combined-and-conditional-probability/combined-probability.json::spcpt_RJtRSrxJtXZPyDHz — tier R1_parse_repair_statement_join — score n/a — wording EXACT — validation tier AI_VALIDATED (operator-delegated chain)
- Rationale: SME span 'Combined Probability' on note 'Combined Probability' is anchored by the corpus spec_point block spcpt_RJtRSrxJtXZPyDHz and joined to 4MA1-6.3A via operator-verdict statement join after T-SPEC-8 parse repair (PMT excluded as source); this section chunk sits inside that span.
- Verdict: [ ] CONFIRM — this chunk belongs to this SP   [ ] REJECT — wrong chunk/SP   [ ] HOLD — needs rework

### 4MA1-3.3B — apply to the graph ofy = f(x)the transformations y = f(x) + a, y = f(ax), y = f(x + a), y = af(x) for linear, quadratic, sine and cosine functions
- Note: Translations of Graphs (`notes/3-sequences-functions-and-graphs/transformations-of-graphs/translations-of-graphs.json`)
- Chunk: ordinal 3 — heading `Vertical translations: y=f(x) + a` — sha256_16 `edd6d4a6a3af6730` — 353 chars
- Evidence quote (verbatim self-slice, markdown-safe): "Vertical translations: y=f(x) + a
- $y=f(x)+a$ is a **vertical translation** by the vector `open parentheses table row 0 row a end table close parentheses`

  - The graph moves** up for positive** values of $a$* *
  - The graph moves **down"
- Chunk excerpt: «Vertical translations: y=f(x) + a - $y=f(x)+a$ is a **vertical translation** by the vector `open parentheses table row 0 row a end table close parentheses` - The graph moves** up for positive** values of $a$* * - The graph moves **down for negative** values of $a$ - The ***x*****-coordinates** stay the** same** Example of a vertical translation»
- Upstream: T-C32 join notes/3-sequences-functions-and-graphs/transformations-of-graphs/translations-of-graphs.json::spcpt_wt53CcTmwpZ3sjm3 — tier P2_operator_content_join — score n/a — wording EXACT — validation tier AI_VALIDATED (operator-delegated chain)
- Rationale: SME span 'Translations of Graphs' on note 'Translations of Graphs' is anchored by the corpus spec_point block spcpt_wt53CcTmwpZ3sjm3 and joined to 4MA1-3.3B via T-SPEC-9 operator verdict (no upstream; PMT excluded as source); this section chunk sits inside that span.
- Verdict: [ ] CONFIRM — this chunk belongs to this SP   [ ] REJECT — wrong chunk/SP   [ ] HOLD — needs rework

### 4MA1-1.6G — use compound interest and depreciation
- Note: Compound Interest (`notes/1-numbers-and-the-number-system/compound-interest-and-depreciation/compound-interest.json`)
- Chunk: ordinal 2 — heading `How do I calculate compound interest?` — sha256_16 `119724469a9ddb87` — 1051 chars
- Evidence quote (verbatim self-slice, markdown-safe): "How do I calculate compound interest?
- Compound interest **increases an amount by a percentage **and then **increases the new amount by the same percentage**

  - This process repeats each time period (yearly or monthly etc)
- We can use a"
- Chunk excerpt: «How do I calculate compound interest? - Compound interest **increases an amount by a percentage **and then **increases the new amount by the same percentage** - This process repeats each time period (yearly or monthly etc) - We can use a **multiplier **to carry out the percentage increase multiple times - To increase **\$300** by **5%** **once**, we would find **300×1.05** - To increase **\$300** by **5%**, each year»
- Upstream: T-C32 join notes/1-numbers-and-the-number-system/compound-interest-and-depreciation/compound-interest.json::spcpt_vyd4VnJDqBJWvTNc — tier P1_name_fragment_join — score n/a — wording EXACT — validation tier AI_VALIDATED (operator-delegated chain)
- Rationale: SME span 'Compound Interest' on note 'Compound Interest' is anchored by the corpus spec_point block spcpt_vyd4VnJDqBJWvTNc and joined to 4MA1-1.6G via operator-verdict name-fragment join (T-SPEC-7; PMT excluded as source); this section chunk sits inside that span.
- Verdict: [ ] CONFIRM — this chunk belongs to this SP   [ ] REJECT — wrong chunk/SP   [ ] HOLD — needs rework

### 4MA1-4.8C — understand and use the sine and cosine rules for any triangle
- Note: The Sine Rule (`notes/4-geometry-and-trigonometry/sine-cosine-rule-and-area-of-triangles/the-sine-rule.json`)
- Chunk: ordinal 1 — heading `What is the sine rule?` — sha256_16 `08f6a48cede68ae3` — 527 chars
- Evidence quote (verbatim self-slice, markdown-safe): "What is the sine rule?
- The **sine rule** is used in **non** **right-angled triangles**

  - It allows us to find missing side lengths or angles
- It states that for any triangle with angles *A, B* and *C*
$\frac{a}{\mathrm{sin}A}=\frac{b}"
- Chunk excerpt: «What is the sine rule? - The **sine rule** is used in **non** **right-angled triangles** - It allows us to find missing side lengths or angles - It states that for any triangle with angles *A, B* and *C* $\frac{a}{\mathrm{sin}A}=\frac{b}{\mathrm{sin}B}=\frac{c}{\mathrm{sin}C}$ - Where - $a$* *is the side **opposite** angle *A* - $b$* *is the side **opposite** angle *B* - $c$* *is the side **opposite** angle *C* Non R»
- Upstream: T-C32 join notes/4-geometry-and-trigonometry/sine-cosine-rule-and-area-of-triangles/the-sine-rule.json::spcpt_QJNVgG7qqP279jnN — tier R1_parse_repair_statement_join — score n/a — wording EXACT — validation tier AI_VALIDATED (operator-delegated chain)
- Rationale: SME span 'Sine Rule' on note 'The Sine Rule' is anchored by the corpus spec_point block spcpt_QJNVgG7qqP279jnN and joined to 4MA1-4.8C via operator-verdict statement join after T-SPEC-8 parse repair (PMT excluded as source); this section chunk sits inside that span.
- Verdict: [ ] CONFIRM — this chunk belongs to this SP   [ ] REJECT — wrong chunk/SP   [ ] HOLD — needs rework

### 4MA1-2.2E — use algebra to support and construct proofs
- Note: Algebraic Proof (`notes/2-equations-formulae-and-identities/algebraic-proof/algebraic-proof.json`)
- Chunk: ordinal 2 — heading `How do I prove results about integers?` — sha256_16 `815e372486d76129` — 1239 chars
- Evidence quote (verbatim self-slice, markdown-safe): "How do I prove results about integers?
- To prove results about** integers** (whole numbers), you need to first represent the integers as algebraic **letters** or **terms**

  - The following table shows the most commonly used algebraic ter"
- Chunk excerpt: «How do I prove results about integers? - To prove results about** integers** (whole numbers), you need to first represent the integers as algebraic **letters** or **terms** - The following table shows the most commonly used algebraic terms | Type of integer | Term | Comment | |---|---|---| | Any integer | $n$ | | | **Consecutive** integers | $n,n+1$ | This means one after the other. Could also use $n-1,n$ | | Any two»
- Upstream: T-C32 join notes/2-equations-formulae-and-identities/algebraic-proof/algebraic-proof.json::spcpt_dgG8VyxX4bgSvRz7 — tier R1_parse_repair_statement_join — score n/a — wording EXACT — validation tier AI_VALIDATED (operator-delegated chain)
- Rationale: SME span 'Algebraic Proof' on note 'Algebraic Proof' is anchored by the corpus spec_point block spcpt_dgG8VyxX4bgSvRz7 and joined to 4MA1-2.2E via operator-verdict statement join after T-SPEC-8 parse repair (PMT excluded as source); this section chunk sits inside that span.
- Verdict: [ ] CONFIRM — this chunk belongs to this SP   [ ] REJECT — wrong chunk/SP   [ ] HOLD — needs rework

### 4MA1-4.9A — find perimeters and areas of sectors of circles
- Note: Arc Lengths & Sector Areas (`notes/4-geometry-and-trigonometry/circles-arcs-and-sectors/arcs-and-sectors.json`)
- Chunk: ordinal 3 — heading `What formulae do I need to know?` — sha256_16 `cac58c0adfb772e0` — 863 chars
- Evidence quote (verbatim self-slice, markdown-safe): "What formulae do I need to know?
- You need to be able to calculate the **length of an arc** and the **area of a sector**
- The **angle** formed in a sector by the two radii is often labelled ***θ*** (the Greek letter “theta”)
- You can cal"
- Chunk excerpt: «What formulae do I need to know? - You need to be able to calculate the **length of an arc** and the **area of a sector** - The **angle** formed in a sector by the two radii is often labelled ***θ*** (the Greek letter “theta”) - You can calculate the **area of a sector** or the **length of an arc** by adapting the formulae for the area or circumference of a circle - A full circle is equal to 360° so the fraction will»
- Upstream: T-C32 join notes/4-geometry-and-trigonometry/circles-arcs-and-sectors/arcs-and-sectors.json::spcpt_dvX7WnB2FSdky4jW — tier R1_parse_repair_statement_join — score n/a — wording EXACT — validation tier AI_VALIDATED (operator-delegated chain)
- Rationale: SME span 'Arc Lengths & Sector Areas' on note 'Arc Lengths & Sector Areas' is anchored by the corpus spec_point block spcpt_dvX7WnB2FSdky4jW and joined to 4MA1-4.9A via operator-verdict statement join after T-SPEC-8 parse repair (PMT excluded as source); this section chunk sits inside that span.
- Verdict: [ ] CONFIRM — this chunk belongs to this SP   [ ] REJECT — wrong chunk/SP   [ ] HOLD — needs rework

### 4MA1-6.3A — draw and use tree diagrams
- Note: Combined Probability (`notes/6-statistics-and-probability/combined-and-conditional-probability/combined-probability.json`)
- Chunk: ordinal 0 — heading `Combined probability` — sha256_16 `296b980dbbc08473` — 20 chars
- Evidence quote (verbatim self-slice, markdown-safe): "Combined probability"
- Chunk excerpt: «Combined probability»
- Upstream: T-C32 join notes/6-statistics-and-probability/combined-and-conditional-probability/combined-probability.json::spcpt_RJtRSrxJtXZPyDHz — tier R1_parse_repair_statement_join — score n/a — wording EXACT — validation tier AI_VALIDATED (operator-delegated chain)
- Rationale: SME span 'Combined Probability' on note 'Combined Probability' is anchored by the corpus spec_point block spcpt_RJtRSrxJtXZPyDHz and joined to 4MA1-6.3A via operator-verdict statement join after T-SPEC-8 parse repair (PMT excluded as source); this section chunk sits inside that span.
- Verdict: [ ] CONFIRM — this chunk belongs to this SP   [ ] REJECT — wrong chunk/SP   [ ] HOLD — needs rework

### 4MA1-3.3B — apply to the graph ofy = f(x)the transformations y = f(x) + a, y = f(ax), y = f(x + a), y = af(x) for linear, quadratic, sine and cosine functions
- Note: Reflections of Graphs (`notes/3-sequences-functions-and-graphs/transformations-of-graphs/reflections-of-graphs.json`)
- Chunk: ordinal 4 — heading `Horizontal reflections: y=f(-x)` — sha256_16 `5d548d4c51aa78ea` — 257 chars
- Evidence quote (verbatim self-slice, markdown-safe): "Horizontal reflections: y=f(-x)
- `y equals straight f open parentheses negative x close parentheses` is a reflection in the** **$y$**-axis**

  - The $x$ coordinates change sign
  
    - The $y$ coordinates are unaffected
Example of a hori"
- Chunk excerpt: «Horizontal reflections: y=f(-x) - `y equals straight f open parentheses negative x close parentheses` is a reflection in the** **$y$**-axis** - The $x$ coordinates change sign - The $y$ coordinates are unaffected Example of a horizontal reflection»
- Upstream: T-C32 join notes/3-sequences-functions-and-graphs/transformations-of-graphs/reflections-of-graphs.json::spcpt_qNDqnmZtzYttZDnz — tier P2_operator_content_join — score n/a — wording EXACT — validation tier AI_VALIDATED (operator-delegated chain)
- Rationale: SME span 'Reflections of Graphs' on note 'Reflections of Graphs' is anchored by the corpus spec_point block spcpt_qNDqnmZtzYttZDnz and joined to 4MA1-3.3B via T-SPEC-9 operator verdict (no upstream; PMT excluded as source); this section chunk sits inside that span.
- Verdict: [ ] CONFIRM — this chunk belongs to this SP   [ ] REJECT — wrong chunk/SP   [ ] HOLD — needs rework

### 4MA1-1.3A — convert recurring decimals into fractions
- Note: Recurring Decimals (`notes/1-numbers-and-the-number-system/fractions-decimals-and-percentages/recurring-decimals.json`)
- Chunk: ordinal 0 — heading `Recurring decimals` — sha256_16 `6c3d5e56a3115e70` — 18 chars
- Evidence quote (verbatim self-slice, markdown-safe): "Recurring decimals"
- Chunk excerpt: «Recurring decimals»
- Upstream: T-C32 join notes/1-numbers-and-the-number-system/fractions-decimals-and-percentages/recurring-decimals.json::spcpt_BVf2GTX8FCvzJjJN — tier R1_parse_repair_statement_join — score n/a — wording EXACT — validation tier AI_VALIDATED (operator-delegated chain)
- Rationale: SME span 'Recurring Decimals' on note 'Recurring Decimals' is anchored by the corpus spec_point block spcpt_BVf2GTX8FCvzJjJN and joined to 4MA1-1.3A via operator-verdict statement join after T-SPEC-8 parse repair (PMT excluded as source); this section chunk sits inside that span.
- Verdict: [ ] CONFIRM — this chunk belongs to this SP   [ ] REJECT — wrong chunk/SP   [ ] HOLD — needs rework

### 4MA1-4.6A — understand and use the internal and external intersecting chord properties
- Note: Intersecting Chord Theorem (`notes/4-geometry-and-trigonometry/circle-theorems/intersecting-chord-theorem.json`)
- Chunk: ordinal 3 — heading `What if the lengths are algebraic?` — sha256_16 `c1f9bcba58f246a5` — 2020 chars
- Evidence quote (verbatim self-slice, markdown-safe): "What if the lengths are algebraic?
- If any of the lengths are algebraic expressions, use the fact that **AP × PB = CP × PD **to form an equation and then solve it
algebraic solution using intersecting chord theorem
Worked Example: The diag"
- Chunk excerpt: «What if the lengths are algebraic? - If any of the lengths are algebraic expressions, use the fact that **AP × PB = CP × PD **to form an equation and then solve it algebraic solution using intersecting chord theorem Worked Example: The diagram below shows a circle with centre *O* and two chords, *PQ* and *RS*. ![Diagram of intersecting chord theorem for worked example](assets/f3cdcb6305b3-12227-diagram-of-intersectin»
- Upstream: T-C32 join notes/4-geometry-and-trigonometry/circle-theorems/intersecting-chord-theorem.json::spcpt_znWXTZjqCR7PspTc — tier R1_parse_repair_statement_join — score n/a — wording EXACT — validation tier AI_VALIDATED (operator-delegated chain)
- Rationale: SME span 'Intersecting Chord Theorem' on note 'Intersecting Chord Theorem' is anchored by the corpus spec_point block spcpt_znWXTZjqCR7PspTc and joined to 4MA1-4.6A via operator-verdict statement join after T-SPEC-8 parse repair (PMT excluded as source); this section chunk sits inside that span.
- Verdict: [ ] CONFIRM — this chunk belongs to this SP   [ ] REJECT — wrong chunk/SP   [ ] HOLD — needs rework

### 4MA1-4.8C — understand and use the sine and cosine rules for any triangle
- Note: The Sine Rule (`notes/4-geometry-and-trigonometry/sine-cosine-rule-and-area-of-triangles/the-sine-rule.json`)
- Chunk: ordinal 3 — heading `How do I use the sine rule to find missing angles?` — sha256_16 `732f319406f32cfc` — 816 chars
- Evidence quote (verbatim self-slice, markdown-safe): "How do I use the sine rule to find missing angles?
- To find a** missing angle**, it is easier to **rearrange **the formula first by flipping each part $\frac{\mathrm{sin}A}{a}=\frac{\mathrm{sin}B}{b}=\frac{\mathrm{sin}C}{c}$

  - The angle"
- Chunk excerpt: «How do I use the sine rule to find missing angles? - To find a** missing angle**, it is easier to **rearrange **the formula first by flipping each part $\frac{\mathrm{sin}A}{a}=\frac{\mathrm{sin}B}{b}=\frac{\mathrm{sin}C}{c}$ - The angles are now in the numerators of the fractions - Substitute the values you have into the formula and solve - You will need to use** inverse sine** in your calculation, `sin to the power»
- Upstream: T-C32 join notes/4-geometry-and-trigonometry/sine-cosine-rule-and-area-of-triangles/the-sine-rule.json::spcpt_QJNVgG7qqP279jnN — tier R1_parse_repair_statement_join — score n/a — wording EXACT — validation tier AI_VALIDATED (operator-delegated chain)
- Rationale: SME span 'Sine Rule' on note 'The Sine Rule' is anchored by the corpus spec_point block spcpt_QJNVgG7qqP279jnN and joined to 4MA1-4.8C via operator-verdict statement join after T-SPEC-8 parse repair (PMT excluded as source); this section chunk sits inside that span.
- Verdict: [ ] CONFIRM — this chunk belongs to this SP   [ ] REJECT — wrong chunk/SP   [ ] HOLD — needs rework

### 4MA1-3.3B — apply to the graph ofy = f(x)the transformations y = f(x) + a, y = f(ax), y = f(x + a), y = af(x) for linear, quadratic, sine and cosine functions
- Note: Translations of Graphs (`notes/3-sequences-functions-and-graphs/transformations-of-graphs/translations-of-graphs.json`)
- Chunk: ordinal 6 — heading `How does a translation affect the equation of the graph?` — sha256_16 `8d6d08740d98b9da` — 1613 chars
- Evidence quote (verbatim self-slice, markdown-safe): "How does a translation affect the equation of the graph?
- For a **horizontal translation** `y equals straight f open parentheses x minus a close parentheses` of the graph `y equals straight f open parentheses x close parentheses`

  - $a$*"
- Chunk excerpt: «How does a translation affect the equation of the graph? - For a **horizontal translation** `y equals straight f open parentheses x minus a close parentheses` of the graph `y equals straight f open parentheses x close parentheses` - $a$** is subtracted from **$x$** **throughout the equation - Every instance of $x$ in the equation is replaced with `open parentheses x minus a close parentheses` - E.g. the graph $y=x^{2»
- Upstream: T-C32 join notes/3-sequences-functions-and-graphs/transformations-of-graphs/translations-of-graphs.json::spcpt_wt53CcTmwpZ3sjm3 — tier P2_operator_content_join — score n/a — wording EXACT — validation tier AI_VALIDATED (operator-delegated chain)
- Rationale: SME span 'Translations of Graphs' on note 'Translations of Graphs' is anchored by the corpus spec_point block spcpt_wt53CcTmwpZ3sjm3 and joined to 4MA1-3.3B via T-SPEC-9 operator verdict (no upstream; PMT excluded as source); this section chunk sits inside that span.
- Verdict: [ ] CONFIRM — this chunk belongs to this SP   [ ] REJECT — wrong chunk/SP   [ ] HOLD — needs rework

### 4MA1-6.1B — construct cumulative frequency diagrams from tabulated data
- Note: Interpreting Cumulative Frequency Diagrams (`notes/6-statistics-and-probability/cumulative-frequency-diagrams/interpreting-cumulative-frequency-diagrams.json`)
- Chunk: ordinal 1 — heading `How do I use and interpret a cumulative frequency diagram?` — sha256_16 `7c22963302d04f5c` — 520 chars
- Evidence quote (verbatim self-slice, markdown-safe): "How do I use and interpret a cumulative frequency diagram?
- A cumulative frequency diagram provides a way to **estimate** key facts about the data

  - **median**
  - **lower** and **upper quartiles**  (and **interquartile range**)
  - **p"
- Chunk excerpt: «How do I use and interpret a cumulative frequency diagram? - A cumulative frequency diagram provides a way to **estimate** key facts about the data - **median** - **lower** and **upper quartiles** (and **interquartile range**) - **percentiles** - These values will be **estimates** as the original raw data is unknown - Cumulative frequency diagrams are used with **grouped** data - Points are joined by a smooth curve -»
- Upstream: T-C32 join notes/6-statistics-and-probability/cumulative-frequency-diagrams/interpreting-cumulative-frequency-diagrams.json::spcpt_8sCVwmD5VVBv6xWg — tier R1_parse_repair_statement_join — score n/a — wording EXACT — validation tier AI_VALIDATED (operator-delegated chain)
- Rationale: SME span 'Interpreting Cumulative Frequency Diagrams' on note 'Interpreting Cumulative Frequency Diagrams' is anchored by the corpus spec_point block spcpt_8sCVwmD5VVBv6xWg and joined to 4MA1-6.1B via operator-verdict statement join after T-SPEC-8 parse repair (PMT excluded as source); this section chunk sits inside that span.
- Verdict: [ ] CONFIRM — this chunk belongs to this SP   [ ] REJECT — wrong chunk/SP   [ ] HOLD — needs rework

### 4MA1-6.3A — draw and use tree diagrams
- Note: Combined Conditional Probabilities (`notes/6-statistics-and-probability/combined-and-conditional-probability/combined-conditional-probabilities.json`)
- Chunk: ordinal 2 — heading `How do I calculate combined conditional probabilities?` — sha256_16 `51e1cb8c351589c6` — 689 chars
- Evidence quote (verbatim self-slice, markdown-safe): "How do I calculate combined conditional probabilities?
- You need to** adjust **the number of outcomes as you go along

  - For example, selecting two cards from a pack of 52 playing cards **without replacing **the first card:
  
    - P(re"
- Chunk excerpt: «How do I calculate combined conditional probabilities? - You need to** adjust **the number of outcomes as you go along - For example, selecting two cards from a pack of 52 playing cards **without replacing **the first card: - P(red 1<sup>st</sup> card) is 26 reds out of 52 cards - If the 1<sup>st</sup> card is not replaced, there are only 25 reds left out the remaining 51 cards - P(red 2<sup>nd </sup>card) is 25 reds»
- Upstream: T-C32 join notes/6-statistics-and-probability/combined-and-conditional-probability/combined-conditional-probabilities.json::spcpt_9cJGVGKRhP9JYgjF — tier R1_parse_repair_statement_join — score n/a — wording EXACT — validation tier AI_VALIDATED (operator-delegated chain)
- Rationale: SME span 'Combined Conditional Probabilities' on note 'Combined Conditional Probabilities' is anchored by the corpus spec_point block spcpt_9cJGVGKRhP9JYgjF and joined to 4MA1-6.3A via operator-verdict statement join after T-SPEC-8 parse repair (PMT excluded as source); this section chunk sits inside that span.
- Verdict: [ ] CONFIRM — this chunk belongs to this SP   [ ] REJECT — wrong chunk/SP   [ ] HOLD — needs rework

### 4MA1-6.1A — construct and interpret histograms
- Note: Drawing Histograms (`notes/6-statistics-and-probability/histograms/drawing-histograms.json`)
- Chunk: ordinal 0 — heading `Drawing histograms` — sha256_16 `5f7c9c3516f30cd8` — 18 chars
- Evidence quote (verbatim self-slice, markdown-safe): "Drawing histograms"
- Chunk excerpt: «Drawing histograms»
- Upstream: T-C32 join notes/6-statistics-and-probability/histograms/drawing-histograms.json::spcpt_nJCDx3cDGTVz3MBk — tier R1_parse_repair_statement_join — score n/a — wording EXACT — validation tier AI_VALIDATED (operator-delegated chain)
- Rationale: SME span 'Drawing Histograms' on note 'Drawing Histograms' is anchored by the corpus spec_point block spcpt_nJCDx3cDGTVz3MBk and joined to 4MA1-6.1A via operator-verdict statement join after T-SPEC-8 parse repair (PMT excluded as source); this section chunk sits inside that span.
- Verdict: [ ] CONFIRM — this chunk belongs to this SP   [ ] REJECT — wrong chunk/SP   [ ] HOLD — needs rework

### 4MA1-2.2B — understand the concept of a quadratic expression and be able to factorise such expressions
- Note: Factorising Harder Quadratics (`notes/2-equations-formulae-and-identities/factorising/factorising-harder-quadratics.json`)
- Chunk: ordinal 3 — heading `Method 2: Factorising using a grid` — sha256_16 `5ff67e63903ce9e0` — 3283 chars
- Evidence quote (verbatim self-slice, markdown-safe): "Method 2: Factorising using a grid
- Use the same example: factorising $4x^{2}-25x-21$
- We need a **pair of numbers** that for $ax^{2}+bx+c$

  - **multiply **to give *ac*
  
    - *ac* in this case is 4 × -21 = -84
  - and **add **to give"
- Chunk excerpt: «Method 2: Factorising using a grid - Use the same example: factorising $4x^{2}-25x-21$ - We need a **pair of numbers** that for $ax^{2}+bx+c$ - **multiply **to give *ac* - *ac* in this case is 4 × -21 = -84 - and **add **to give *b* - *b* in this case is -25 - -28 and +3 satisfy these conditions - Write the quadratic expression in a **grid ** - (as if you had used a grid to expand the brackets) - splitting the middle»
- Upstream: T-C32 join notes/2-equations-formulae-and-identities/factorising/factorising-harder-quadratics.json::spcpt_rt6wRVmbK5ZVkF3d — tier R1_parse_repair_statement_join — score n/a — wording EXACT — validation tier AI_VALIDATED (operator-delegated chain)
- Rationale: SME span 'Factorising Harder Quadratics' on note 'Factorising Harder Quadratics' is anchored by the corpus spec_point block spcpt_rt6wRVmbK5ZVkF3d and joined to 4MA1-2.2B via operator-verdict statement join after T-SPEC-8 parse repair (PMT excluded as source); this section chunk sits inside that span.
- Verdict: [ ] CONFIRM — this chunk belongs to this SP   [ ] REJECT — wrong chunk/SP   [ ] HOLD — needs rework

### 4MA1-1.4B — manipulate surds, including rationalising a denominator
- Note: Rationalising Denominators (`notes/1-numbers-and-the-number-system/surds/rationalising-denominators.json`)
- Chunk: ordinal 3 — heading `How do I rationalise harder denominators?` — sha256_16 `0d7fd84103aff832` — 3261 chars
- Evidence quote (verbatim self-slice, markdown-safe): "How do I rationalise harder denominators?
- If the **denominator **is an **expression containing a surd:**

  - For example $\frac{2}{3+\sqrt{5}}$
  - Multiply **the top and bottom of the fraction** by the **expression on the denominator**,"
- Chunk excerpt: «How do I rationalise harder denominators? - If the **denominator **is an **expression containing a surd:** - For example $\frac{2}{3+\sqrt{5}}$ - Multiply **the top and bottom of the fraction** by the **expression on the denominator**, but **with the sign changed** - $\frac{2}{3+\sqrt{5}}=\frac{2}{3+\sqrt{5}}\times\frac{3-\sqrt{5}}{3-\sqrt{5}}$ - This is equivalent to multiplying by 1, so does not change the value of»
- Upstream: T-C32 join notes/1-numbers-and-the-number-system/surds/rationalising-denominators.json::spcpt_wMN58K4jZ54z8bXC — tier R1_parse_repair_statement_join — score n/a — wording EXACT — validation tier AI_VALIDATED (operator-delegated chain)
- Rationale: SME span 'Rationalising Denominators' on note 'Rationalising Denominators' is anchored by the corpus spec_point block spcpt_wMN58K4jZ54z8bXC and joined to 4MA1-1.4B via operator-verdict statement join after T-SPEC-8 parse repair (PMT excluded as source); this section chunk sits inside that span.
- Verdict: [ ] CONFIRM — this chunk belongs to this SP   [ ] REJECT — wrong chunk/SP   [ ] HOLD — needs rework

### 4MA1-4.8C — understand and use the sine and cosine rules for any triangle
- Note: The Sine Rule (`notes/4-geometry-and-trigonometry/sine-cosine-rule-and-area-of-triangles/the-sine-rule.json`)
- Chunk: ordinal 4 — heading `What is the ambiguous case of the sine rule?` — sha256_16 `1ec0ea841466898a` — 3023 chars
- Evidence quote (verbatim self-slice, markdown-safe): "What is the ambiguous case of the sine rule?
- Given information about a triangle, there may be **two different ways** to draw it
- In the diagram below, the lengths of two sides are given,  *a* and *b*

  - A base angle is also given, $θ$,"
- Chunk excerpt: «What is the ambiguous case of the sine rule? - Given information about a triangle, there may be **two different ways** to draw it - In the diagram below, the lengths of two sides are given, *a* and *b* - A base angle is also given, $θ$, but no angle near *b *is given - It turns out that there are **two possible ways** to arrange *b to *complete the triangle! - Both triangles have the correct values of *a*, *b* and $θ»
- Upstream: T-C32 join notes/4-geometry-and-trigonometry/sine-cosine-rule-and-area-of-triangles/the-sine-rule.json::spcpt_QJNVgG7qqP279jnN — tier R1_parse_repair_statement_join — score n/a — wording EXACT — validation tier AI_VALIDATED (operator-delegated chain)
- Rationale: SME span 'Sine Rule' on note 'The Sine Rule' is anchored by the corpus spec_point block spcpt_QJNVgG7qqP279jnN and joined to 4MA1-4.8C via operator-verdict statement join after T-SPEC-8 parse repair (PMT excluded as source); this section chunk sits inside that span.
- Verdict: [ ] CONFIRM — this chunk belongs to this SP   [ ] REJECT — wrong chunk/SP   [ ] HOLD — needs rework

### 4MA1-1.4B — manipulate surds, including rationalising a denominator
- Note: Rationalising Denominators (`notes/1-numbers-and-the-number-system/surds/rationalising-denominators.json`)
- Chunk: ordinal 1 — heading `What does rationalising the denominator mean?` — sha256_16 `8456bb796a96de56` — 450 chars
- Evidence quote (verbatim self-slice, markdown-safe): "What does rationalising the denominator mean?
- If a fraction has a denominator containing a *surd* then it has an **irrational** denominator

  - E.g. $\frac{4}{\sqrt{5}}$ or $\sqrt{\frac{2}{3}}=\frac{\sqrt{2}}{\sqrt{3}}$
- The  fraction c"
- Chunk excerpt: «What does rationalising the denominator mean? - If a fraction has a denominator containing a *surd* then it has an **irrational** denominator - E.g. $\frac{4}{\sqrt{5}}$ or $\sqrt{\frac{2}{3}}=\frac{\sqrt{2}}{\sqrt{3}}$ - The fraction can be rewritten as an equivalent fraction, but with a **rational** denominator - E.g. $\frac{4\sqrt{5}}{5}$ or $\frac{\sqrt{6}}{3}$ - The numerator may contain a surd, but the denomina»
- Upstream: T-C32 join notes/1-numbers-and-the-number-system/surds/rationalising-denominators.json::spcpt_wMN58K4jZ54z8bXC — tier R1_parse_repair_statement_join — score n/a — wording EXACT — validation tier AI_VALIDATED (operator-delegated chain)
- Rationale: SME span 'Rationalising Denominators' on note 'Rationalising Denominators' is anchored by the corpus spec_point block spcpt_wMN58K4jZ54z8bXC and joined to 4MA1-1.4B via operator-verdict statement join after T-SPEC-8 parse repair (PMT excluded as source); this section chunk sits inside that span.
- Verdict: [ ] CONFIRM — this chunk belongs to this SP   [ ] REJECT — wrong chunk/SP   [ ] HOLD — needs rework

### 4MA1-6.3B — determine the probability that two or more independent events will occur
- Note: Conditional Probability (`notes/6-statistics-and-probability/combined-and-conditional-probability/conditional-probability.json`)
- Chunk: ordinal 1 — heading `What is a conditional probability?` — sha256_16 `6e00cc7011367f25` — 175 chars
- Evidence quote (verbatim self-slice, markdown-safe): "What is a conditional probability?
- A **conditional probability** is the probability of something happening (*A*) **given that **something else has **already happened** (*B*)"
- Chunk excerpt: «What is a conditional probability? - A **conditional probability** is the probability of something happening (*A*) **given that **something else has **already happened** (*B*)»
- Upstream: T-C32 join notes/6-statistics-and-probability/combined-and-conditional-probability/conditional-probability.json::spcpt_DkBXXfmWk2hGVF6Y — tier P1_name_fragment_join — score n/a — wording EXACT — validation tier AI_VALIDATED (operator-delegated chain)
- Rationale: SME span 'Conditional Probability' on note 'Conditional Probability' is anchored by the corpus spec_point block spcpt_DkBXXfmWk2hGVF6Y and joined to 4MA1-6.3B via operator-verdict name-fragment join (T-SPEC-7; PMT excluded as source); this section chunk sits inside that span.
- Verdict: [ ] CONFIRM — this chunk belongs to this SP   [ ] REJECT — wrong chunk/SP   [ ] HOLD — needs rework

### 4MA1-6.2B — understand the concept of a measure of spread
- Note: Comparing Data Sets (`notes/6-statistics-and-probability/statistics-toolkit/comparing-distributions.json`)
- Chunk: ordinal 0 — heading `Comparing distributions` — sha256_16 `c4855f3ab497d9b4` — 23 chars
- Evidence quote (verbatim self-slice, markdown-safe): "Comparing distributions"
- Chunk excerpt: «Comparing distributions»
- Upstream: T-C32 join notes/6-statistics-and-probability/statistics-toolkit/comparing-distributions.json::spcpt_vDScwbWGWfmFC3TT — tier P2_operator_content_join — score n/a — wording EXACT — validation tier AI_VALIDATED (operator-delegated chain)
- Rationale: SME span 'Comparing Distributions' on note 'Comparing Data Sets' is anchored by the corpus spec_point block spcpt_vDScwbWGWfmFC3TT and joined to 4MA1-6.2B via T-SPEC-9 operator verdict (no upstream; PMT excluded as source); this section chunk sits inside that span.
- Verdict: [ ] CONFIRM — this chunk belongs to this SP   [ ] REJECT — wrong chunk/SP   [ ] HOLD — needs rework

### 4MA1-6.2B — understand the concept of a measure of spread
- Note: Comparing Data Sets (`notes/6-statistics-and-probability/statistics-toolkit/comparing-distributions.json`)
- Chunk: ordinal 3 — heading `What restrictions are there when drawing conclusions?` — sha256_16 `23d54d33b7e9d069` — 547 chars
- Evidence quote (verbatim self-slice, markdown-safe): "What restrictions are there when drawing conclusions?
- The data set may be **too small **to be truly representative

  - Measuring the heights of only 5 pupils in a whole school is not enough to talk about averages and spreads
- The data s"
- Chunk excerpt: «What restrictions are there when drawing conclusions? - The data set may be **too small **to be truly representative - Measuring the heights of only 5 pupils in a whole school is not enough to talk about averages and spreads - The data set may be **biased** - Measuring the heights of just the older year groups in a school will make the average appear too high - The conclusions might be influenced by **who **is presen»
- Upstream: T-C32 join notes/6-statistics-and-probability/statistics-toolkit/comparing-distributions.json::spcpt_vDScwbWGWfmFC3TT — tier P2_operator_content_join — score n/a — wording EXACT — validation tier AI_VALIDATED (operator-delegated chain)
- Rationale: SME span 'Comparing Distributions' on note 'Comparing Data Sets' is anchored by the corpus spec_point block spcpt_vDScwbWGWfmFC3TT and joined to 4MA1-6.2B via T-SPEC-9 operator verdict (no upstream; PMT excluded as source); this section chunk sits inside that span.
- Verdict: [ ] CONFIRM — this chunk belongs to this SP   [ ] REJECT — wrong chunk/SP   [ ] HOLD — needs rework

### 4MA1-1.4A — understand the meaning of surds
- Note: Simplifying Surds (`notes/1-numbers-and-the-number-system/surds/simplifying-surds.json`)
- Chunk: ordinal 3 — heading `Simplifying surds` — sha256_16 `b77515f34b26a7cc` — 17 chars
- Evidence quote (verbatim self-slice, markdown-safe): "Simplifying surds"
- Chunk excerpt: «Simplifying surds»
- Upstream: T-C32 join notes/1-numbers-and-the-number-system/surds/simplifying-surds.json::spcpt_stqdXPTn5YvgKtvm — tier R1_parse_repair_statement_join — score n/a — wording EXACT — validation tier AI_VALIDATED (operator-delegated chain)
- Rationale: SME span 'Simplifying Surds' on note 'Simplifying Surds' is anchored by the corpus spec_point block spcpt_stqdXPTn5YvgKtvm and joined to 4MA1-1.4A via operator-verdict statement join after T-SPEC-8 parse repair (PMT excluded as source); this section chunk sits inside that span.
- Verdict: [ ] CONFIRM — this chunk belongs to this SP   [ ] REJECT — wrong chunk/SP   [ ] HOLD — needs rework

### 4MA1-4.8C — understand and use the sine and cosine rules for any triangle
- Note: The Cosine Rule (`notes/4-geometry-and-trigonometry/sine-cosine-rule-and-area-of-triangles/the-cosine-rule.json`)
- Chunk: ordinal 2 — heading `How do I use the cosine rule to find a missing length?` — sha256_16 `eb7ad511b78d0f0b` — 503 chars
- Evidence quote (verbatim self-slice, markdown-safe): "How do I use the cosine rule to find a missing length?
- Use the **cosine rule** for lengths

  - when you have **two sides and the angle between them**
  - and you want to find the **opposite side**, *a*
- **Start by labelling your triangl"
- Chunk excerpt: «How do I use the cosine rule to find a missing length? - Use the **cosine rule** for lengths - when you have **two sides and the angle between them** - and you want to find the **opposite side**, *a* - **Start by labelling your triangle** with the angles and sides - Angles have upper case letters - Sides **opposite** the angles have the equivalent lower case letter - **Substitute** values into $a^{2}=b^{2}+c^{2}-2bc\»
- Upstream: T-C32 join notes/4-geometry-and-trigonometry/sine-cosine-rule-and-area-of-triangles/the-cosine-rule.json::spcpt_HnxHKwwfTxKcvCN7 — tier R1_parse_repair_statement_join — score n/a — wording EXACT — validation tier AI_VALIDATED (operator-delegated chain)
- Rationale: SME span 'Cosine Rule' on note 'The Cosine Rule' is anchored by the corpus spec_point block spcpt_HnxHKwwfTxKcvCN7 and joined to 4MA1-4.8C via operator-verdict statement join after T-SPEC-8 parse repair (PMT excluded as source); this section chunk sits inside that span.
- Verdict: [ ] CONFIRM — this chunk belongs to this SP   [ ] REJECT — wrong chunk/SP   [ ] HOLD — needs rework

### 4MA1-6.1A — construct and interpret histograms
- Note: Frequency Density (`notes/6-statistics-and-probability/histograms/frequency-density.json`)
- Chunk: ordinal 1 — heading `What is frequency density?` — sha256_16 `d6e64da6f8eda2d4` — 467 chars
- Evidence quote (verbatim self-slice, markdown-safe): "What is frequency density?
- **Frequency density** is given by the formula

  - $\mathrm{frequency} \mathrm{density}=\frac{\mathrm{frequency}}{\mathrm{class} \mathrm{width}}$
- Frequency density is used with **grouped data** (i.e. data grou"
- Chunk excerpt: «What is frequency density? - **Frequency density** is given by the formula - $\mathrm{frequency} \mathrm{density}=\frac{\mathrm{frequency}}{\mathrm{class} \mathrm{width}}$ - Frequency density is used with **grouped data** (i.e. data grouped by **class intervals**) - It is useful when the class intervals are of **unequal** **width** - It provides a measure of how **dense** data is within its **class interval** - relat»
- Upstream: T-C32 join notes/6-statistics-and-probability/histograms/frequency-density.json::spcpt_Sq9YjYQDkzwdnKT3 — tier R1_parse_repair_statement_join — score n/a — wording EXACT — validation tier AI_VALIDATED (operator-delegated chain)
- Rationale: SME span 'Frequency Density' on note 'Frequency Density' is anchored by the corpus spec_point block spcpt_Sq9YjYQDkzwdnKT3 and joined to 4MA1-6.1A via operator-verdict statement join after T-SPEC-8 parse repair (PMT excluded as source); this section chunk sits inside that span.
- Verdict: [ ] CONFIRM — this chunk belongs to this SP   [ ] REJECT — wrong chunk/SP   [ ] HOLD — needs rework

### 4MA1-6.1A — construct and interpret histograms
- Note: Frequency Density (`notes/6-statistics-and-probability/histograms/frequency-density.json`)
- Chunk: ordinal 0 — heading `Frequency density` — sha256_16 `c09f1b631c9b0424` — 17 chars
- Evidence quote (verbatim self-slice, markdown-safe): "Frequency density"
- Chunk excerpt: «Frequency density»
- Upstream: T-C32 join notes/6-statistics-and-probability/histograms/frequency-density.json::spcpt_Sq9YjYQDkzwdnKT3 — tier R1_parse_repair_statement_join — score n/a — wording EXACT — validation tier AI_VALIDATED (operator-delegated chain)
- Rationale: SME span 'Frequency Density' on note 'Frequency Density' is anchored by the corpus spec_point block spcpt_Sq9YjYQDkzwdnKT3 and joined to 4MA1-6.1A via operator-verdict statement join after T-SPEC-8 parse repair (PMT excluded as source); this section chunk sits inside that span.
- Verdict: [ ] CONFIRM — this chunk belongs to this SP   [ ] REJECT — wrong chunk/SP   [ ] HOLD — needs rework

### 4MA1-6.1B — construct cumulative frequency diagrams from tabulated data
- Note: Drawing Cumulative Frequency Diagrams (`notes/6-statistics-and-probability/cumulative-frequency-diagrams/drawing-cumulative-frequency-diagrams.json`)
- Chunk: ordinal 1 — heading `What is a cumulative frequency diagram?` — sha256_16 `64f0f1735fba5905` — 285 chars
- Evidence quote (verbatim self-slice, markdown-safe): "What is a cumulative frequency diagram?
- A **cumulative frequency diagram** is a way of representing **grouped continuous data**
- A cumulative frequency diagram can be used to **estimate** other **statistical values**

  - For example the"
- Chunk excerpt: «What is a cumulative frequency diagram? - A **cumulative frequency diagram** is a way of representing **grouped continuous data** - A cumulative frequency diagram can be used to **estimate** other **statistical values** - For example the **median**, **quartiles** or **percentiles**»
- Upstream: T-C32 join notes/6-statistics-and-probability/cumulative-frequency-diagrams/drawing-cumulative-frequency-diagrams.json::spcpt_kwGrBDCwB6YtVVBQ — tier R1_parse_repair_statement_join — score n/a — wording EXACT — validation tier AI_VALIDATED (operator-delegated chain)
- Rationale: SME span 'Drawing Cumulative Frequency Diagrams' on note 'Drawing Cumulative Frequency Diagrams' is anchored by the corpus spec_point block spcpt_kwGrBDCwB6YtVVBQ and joined to 4MA1-6.1B via operator-verdict statement join after T-SPEC-8 parse repair (PMT excluded as source); this section chunk sits inside that span.
- Verdict: [ ] CONFIRM — this chunk belongs to this SP   [ ] REJECT — wrong chunk/SP   [ ] HOLD — needs rework

### 4MA1-2.2E — use algebra to support and construct proofs
- Note: Algebraic Proof (`notes/2-equations-formulae-and-identities/algebraic-proof/algebraic-proof.json`)
- Chunk: ordinal 3 — heading `How do I show that a result is odd or even?` — sha256_16 `19eaccab9c375f00` — 861 chars
- Evidence quote (verbatim self-slice, markdown-safe): "How do I show that a result is odd or even?
- To prove an expression is **even**, show that it can be written as `Error converting from MathML to accessible text.`

  - For example, `2 open parentheses n squared minus 3 n close parentheses`"
- Chunk excerpt: «How do I show that a result is odd or even? - To prove an expression is **even**, show that it can be written as `Error converting from MathML to accessible text.` - For example, `2 open parentheses n squared minus 3 n close parentheses` is even - This may require **factorising out a 2** - To prove something is **odd,** show that it can be written as `Error converting from MathML to accessible text.` - For example, `»
- Upstream: T-C32 join notes/2-equations-formulae-and-identities/algebraic-proof/algebraic-proof.json::spcpt_dgG8VyxX4bgSvRz7 — tier R1_parse_repair_statement_join — score n/a — wording EXACT — validation tier AI_VALIDATED (operator-delegated chain)
- Rationale: SME span 'Algebraic Proof' on note 'Algebraic Proof' is anchored by the corpus spec_point block spcpt_dgG8VyxX4bgSvRz7 and joined to 4MA1-2.2E via operator-verdict statement join after T-SPEC-8 parse repair (PMT excluded as source); this section chunk sits inside that span.
- Verdict: [ ] CONFIRM — this chunk belongs to this SP   [ ] REJECT — wrong chunk/SP   [ ] HOLD — needs rework

### 4MA1-6.1A — construct and interpret histograms
- Note: Interpreting Histograms (`notes/6-statistics-and-probability/histograms/interpreting-histograms.json`)
- Chunk: ordinal 0 — heading `Interpreting histograms` — sha256_16 `c6dca04fe66948ed` — 23 chars
- Evidence quote (verbatim self-slice, markdown-safe): "Interpreting histograms"
- Chunk excerpt: «Interpreting histograms»
- Upstream: T-C32 join notes/6-statistics-and-probability/histograms/interpreting-histograms.json::spcpt_zNgS9BtJ7493zsyx — tier R1_parse_repair_statement_join — score n/a — wording EXACT — validation tier AI_VALIDATED (operator-delegated chain)
- Rationale: SME span 'Interpreting Histograms' on note 'Interpreting Histograms' is anchored by the corpus spec_point block spcpt_zNgS9BtJ7493zsyx and joined to 4MA1-6.1A via operator-verdict statement join after T-SPEC-8 parse repair (PMT excluded as source); this section chunk sits inside that span.
- Verdict: [ ] CONFIRM — this chunk belongs to this SP   [ ] REJECT — wrong chunk/SP   [ ] HOLD — needs rework

### 4MA1-4.6A — understand and use the internal and external intersecting chord properties
- Note: Intersecting Chord Theorem (`notes/4-geometry-and-trigonometry/circle-theorems/intersecting-chord-theorem.json`)
- Chunk: ordinal 1 — heading `What is the intersecting chord theorem?` — sha256_16 `d04eafedb803fe94` — 467 chars
- Evidence quote (verbatim self-slice, markdown-safe): "What is the intersecting chord theorem?
- For two chords, **AB** and **CD** that meet at point P

  - **AP : PD ≡ CP : PB**
  - **Ratio** of **longer** lengths (of chords) ≡ **Ratio** of **shorter** lengths (of chords)
  - This can also be "
- Chunk excerpt: «What is the intersecting chord theorem? - For two chords, **AB** and **CD** that meet at point P - **AP : PD ≡ CP : PB** - **Ratio** of **longer** lengths (of chords) ≡ **Ratio** of **shorter** lengths (of chords) - This can also be written as **AP × PB = CP × PD** - You do not need to know the proof of this theorem - This theorem is closely related to **similar shapes** Chords AB and CD intersect at point P inside a»
- Upstream: T-C32 join notes/4-geometry-and-trigonometry/circle-theorems/intersecting-chord-theorem.json::spcpt_znWXTZjqCR7PspTc — tier R1_parse_repair_statement_join — score n/a — wording EXACT — validation tier AI_VALIDATED (operator-delegated chain)
- Rationale: SME span 'Intersecting Chord Theorem' on note 'Intersecting Chord Theorem' is anchored by the corpus spec_point block spcpt_znWXTZjqCR7PspTc and joined to 4MA1-4.6A via operator-verdict statement join after T-SPEC-8 parse repair (PMT excluded as source); this section chunk sits inside that span.
- Verdict: [ ] CONFIRM — this chunk belongs to this SP   [ ] REJECT — wrong chunk/SP   [ ] HOLD — needs rework

### 4MA1-6.1B — construct cumulative frequency diagrams from tabulated data
- Note: Cumulative Frequency (`notes/6-statistics-and-probability/cumulative-frequency-diagrams/cumulative-frequency-diagrams.json`)
- Chunk: ordinal 0 — heading `Cumulative frequency` — sha256_16 `3086c4638a92975d` — 20 chars
- Evidence quote (verbatim self-slice, markdown-safe): "Cumulative frequency"
- Chunk excerpt: «Cumulative frequency»
- Upstream: T-C32 join notes/6-statistics-and-probability/cumulative-frequency-diagrams/cumulative-frequency-diagrams.json::spcpt_gdR9ykyG92GK4hGr — tier R1_parse_repair_statement_join — score n/a — wording EXACT — validation tier AI_VALIDATED (operator-delegated chain)
- Rationale: SME span 'Cumulative Frequency' on note 'Cumulative Frequency' is anchored by the corpus spec_point block spcpt_gdR9ykyG92GK4hGr and joined to 4MA1-6.1B via operator-verdict statement join after T-SPEC-8 parse repair (PMT excluded as source); this section chunk sits inside that span.
- Verdict: [ ] CONFIRM — this chunk belongs to this SP   [ ] REJECT — wrong chunk/SP   [ ] HOLD — needs rework

### 4MA1-2.8A — solve quadratic inequalities in one unknown and represent the solution set on a number line
- Note: Solving Quadratic Inequalities (`notes/2-equations-formulae-and-identities/solving-inequalities/solving-quadratic-inequalities.json`)
- Chunk: ordinal 4 — heading `How can quadratic inequalities be made harder?` — sha256_16 `4a2e10f3e809ef0d` — 2045 chars
- Evidence quote (verbatim self-slice, markdown-safe): "How can quadratic inequalities be made harder?
- You may need to **bring all the terms to one side **first

  - For example"
- Chunk excerpt: «How can quadratic inequalities be made harder? - You may need to **bring all the terms to one side **first - For example $x^{2}-x<6$ becomes $x^{2}-x-6<0$ - It is easier to pick the side with a positive $x^{2}$ - You may have to **factorise **the quadratic inequality first - This may involve factorising - $ax^{2}+bx+c$ into **double brackets** - `a squared x squared minus b squared equals open parentheses a x plus b »
- Upstream: T-C32 join notes/2-equations-formulae-and-identities/solving-inequalities/solving-quadratic-inequalities.json::spcpt_dnkHMPkqhhdDxPkZ — tier R1_parse_repair_statement_join — score n/a — wording EXACT — validation tier AI_VALIDATED (operator-delegated chain)
- Rationale: SME span 'Solving Quadratic Inequalities' on note 'Solving Quadratic Inequalities' is anchored by the corpus spec_point block spcpt_dnkHMPkqhhdDxPkZ and joined to 4MA1-2.8A via operator-verdict statement join after T-SPEC-8 parse repair (PMT excluded as source); this section chunk sits inside that span.
- Verdict: [ ] CONFIRM — this chunk belongs to this SP   [ ] REJECT — wrong chunk/SP   [ ] HOLD — needs rework

### 4MA1-3.3B — apply to the graph ofy = f(x)the transformations y = f(x) + a, y = f(ax), y = f(x + a), y = af(x) for linear, quadratic, sine and cosine functions
- Note: Stretches of Graphs (`notes/3-sequences-functions-and-graphs/transformations-of-graphs/stretches-of-graphs.json`)
- Chunk: ordinal 0 — heading `Stretches of graphs` — sha256_16 `662b319afe6d628b` — 19 chars
- Evidence quote (verbatim self-slice, markdown-safe): "Stretches of graphs"
- Chunk excerpt: «Stretches of graphs»
- Upstream: T-C32 join notes/3-sequences-functions-and-graphs/transformations-of-graphs/stretches-of-graphs.json::spcpt_YcMPxJgtrjtBzMkV — tier P2_operator_content_join — score n/a — wording EXACT — validation tier AI_VALIDATED (operator-delegated chain)
- Rationale: SME span 'Stretches of Graphs' on note 'Stretches of Graphs' is anchored by the corpus spec_point block spcpt_YcMPxJgtrjtBzMkV and joined to 4MA1-3.3B via T-SPEC-9 operator verdict (no upstream; PMT excluded as source); this section chunk sits inside that span.
- Verdict: [ ] CONFIRM — this chunk belongs to this SP   [ ] REJECT — wrong chunk/SP   [ ] HOLD — needs rework

### 4MA1-6.2B — understand the concept of a measure of spread
- Note: Comparing Data Sets (`notes/6-statistics-and-probability/statistics-toolkit/comparing-distributions.json`)
- Chunk: ordinal 2 — heading `How do I write a conclusion when comparing two data sets?` — sha256_16 `f537001d0f8315b9` — 853 chars
- Evidence quote (verbatim self-slice, markdown-safe): "How do I write a conclusion when comparing two data sets?
- When comparing **averages **and** spreads**, you need to

  - compare **numbers**
  - **describe** what this means in **real life **
- **Copy **the **exact** wording from the quest"
- Chunk excerpt: «How do I write a conclusion when comparing two data sets? - When comparing **averages **and** spreads**, you need to - compare **numbers** - **describe** what this means in **real life ** - **Copy **the **exact** wording from the question in your answer - There should be **four** parts to your conclusion - For example: - "The **median** score of class A (45) is **higher** than the median score of class B (32)." - "Th»
- Upstream: T-C32 join notes/6-statistics-and-probability/statistics-toolkit/comparing-distributions.json::spcpt_vDScwbWGWfmFC3TT — tier P2_operator_content_join — score n/a — wording EXACT — validation tier AI_VALIDATED (operator-delegated chain)
- Rationale: SME span 'Comparing Distributions' on note 'Comparing Data Sets' is anchored by the corpus spec_point block spcpt_vDScwbWGWfmFC3TT and joined to 4MA1-6.2B via T-SPEC-9 operator verdict (no upstream; PMT excluded as source); this section chunk sits inside that span.
- Verdict: [ ] CONFIRM — this chunk belongs to this SP   [ ] REJECT — wrong chunk/SP   [ ] HOLD — needs rework

### 4MA1-2.2E — use algebra to support and construct proofs
- Note: Algebraic Proof (`notes/2-equations-formulae-and-identities/algebraic-proof/algebraic-proof.json`)
- Chunk: ordinal 1 — heading `What is algebraic proof?` — sha256_16 `aaaef540c7960e3f` — 375 chars
- Evidence quote (verbatim self-slice, markdown-safe): "What is algebraic proof?
- **Algebraic proof **means **proving a result **using **algebra**

  - This is different to proving a result by individually testing all possible values
- The proofs may require** algebraic skills** such as

  - ex"
- Chunk excerpt: «What is algebraic proof? - **Algebraic proof **means **proving a result **using **algebra** - This is different to proving a result by individually testing all possible values - The proofs may require** algebraic skills** such as - expanding brackets - factorising - collecting like terms - The** difference of two squares** factorisation can also be helpful»
- Upstream: T-C32 join notes/2-equations-formulae-and-identities/algebraic-proof/algebraic-proof.json::spcpt_dgG8VyxX4bgSvRz7 — tier R1_parse_repair_statement_join — score n/a — wording EXACT — validation tier AI_VALIDATED (operator-delegated chain)
- Rationale: SME span 'Algebraic Proof' on note 'Algebraic Proof' is anchored by the corpus spec_point block spcpt_dgG8VyxX4bgSvRz7 and joined to 4MA1-2.2E via operator-verdict statement join after T-SPEC-8 parse repair (PMT excluded as source); this section chunk sits inside that span.
- Verdict: [ ] CONFIRM — this chunk belongs to this SP   [ ] REJECT — wrong chunk/SP   [ ] HOLD — needs rework

### 4MA1-4.9A — find perimeters and areas of sectors of circles
- Note: Arc Lengths & Sector Areas (`notes/4-geometry-and-trigonometry/circles-arcs-and-sectors/arcs-and-sectors.json`)
- Chunk: ordinal 1 — heading `What is an arc?` — sha256_16 `1d228417b8433204` — 257 chars
- Evidence quote (verbatim self-slice, markdown-safe): "What is an arc?
- An **arc** is a **part **of the **circumference** of a circle
- Two points on a circumference of a circle will create **two arcs **

  - The **smaller** arc is known as the **minor arc**
  - The **bigger** arc is known as "
- Chunk excerpt: «What is an arc? - An **arc** is a **part **of the **circumference** of a circle - Two points on a circumference of a circle will create **two arcs ** - The **smaller** arc is known as the **minor arc** - The **bigger** arc is known as the **major arc**»
- Upstream: T-C32 join notes/4-geometry-and-trigonometry/circles-arcs-and-sectors/arcs-and-sectors.json::spcpt_dvX7WnB2FSdky4jW — tier R1_parse_repair_statement_join — score n/a — wording EXACT — validation tier AI_VALIDATED (operator-delegated chain)
- Rationale: SME span 'Arc Lengths & Sector Areas' on note 'Arc Lengths & Sector Areas' is anchored by the corpus spec_point block spcpt_dvX7WnB2FSdky4jW and joined to 4MA1-4.9A via operator-verdict statement join after T-SPEC-8 parse repair (PMT excluded as source); this section chunk sits inside that span.
- Verdict: [ ] CONFIRM — this chunk belongs to this SP   [ ] REJECT — wrong chunk/SP   [ ] HOLD — needs rework

### 4MA1-6.1B — construct cumulative frequency diagrams from tabulated data
- Note: Interpreting Cumulative Frequency Diagrams (`notes/6-statistics-and-probability/cumulative-frequency-diagrams/interpreting-cumulative-frequency-diagrams.json`)
- Chunk: ordinal 3 — heading `How do I find a percentile from a cumulative frequency diagram?` — sha256_16 `24e18a5cef80ae08` — 3726 chars
- Evidence quote (verbatim self-slice, markdown-safe): "How do I find a percentile from a cumulative frequency diagram?
- **Percentiles** split the data into 100 parts

  - The **50**<sup>**th**</sup>** percentile** is another way of describing the **median**
  - The **25**<sup>**th**</sup> and "
- Chunk excerpt: «How do I find a percentile from a cumulative frequency diagram? - **Percentiles** split the data into 100 parts - The **50**<sup>**th**</sup>** percentile** is another way of describing the **median** - The **25**<sup>**th**</sup> and **75**<sup>**th**</sup>** percentiles** are the same as the **lower** and **upper quartiles** (respectively) - To find the** *****p***<sup>**th**</sup>** **<sup>** **</sup>**percentile*»
- Upstream: T-C32 join notes/6-statistics-and-probability/cumulative-frequency-diagrams/interpreting-cumulative-frequency-diagrams.json::spcpt_8sCVwmD5VVBv6xWg — tier R1_parse_repair_statement_join — score n/a — wording EXACT — validation tier AI_VALIDATED (operator-delegated chain)
- Rationale: SME span 'Interpreting Cumulative Frequency Diagrams' on note 'Interpreting Cumulative Frequency Diagrams' is anchored by the corpus spec_point block spcpt_8sCVwmD5VVBv6xWg and joined to 4MA1-6.1B via operator-verdict statement join after T-SPEC-8 parse repair (PMT excluded as source); this section chunk sits inside that span.
- Verdict: [ ] CONFIRM — this chunk belongs to this SP   [ ] REJECT — wrong chunk/SP   [ ] HOLD — needs rework

### 4MA1-4.8B — understand and use angles of elevation and depression
- Note: Angles of Elevation & Depression (`notes/4-geometry-and-trigonometry/right-angled-triangles---pythagoras-and-trigonometry/angles-of-elevation-and-depression.json`)
- Chunk: ordinal 1 — heading `What are angles of elevation and depression?` — sha256_16 `4b0e802f9695fad9` — 3332 chars
- Evidence quote (verbatim self-slice, markdown-safe): "What are angles of elevation and depression?
- An **angle of elevation **or** depression** is the angle measured between the **horizontal** and the **line of sight**

  - Looking **up** at an object creates an angle of **elevation**
  - Loo"
- Chunk excerpt: «What are angles of elevation and depression? - An **angle of elevation **or** depression** is the angle measured between the **horizontal** and the **line of sight** - Looking **up** at an object creates an angle of **elevation** - Looking **down** at an object creates an angle of** depression** - **Right-angled trigonometry **can be used to find - an **angle** of elevation or depression - or a missing **distance** -»
- Upstream: T-C32 join notes/4-geometry-and-trigonometry/right-angled-triangles---pythagoras-and-trigonometry/angles-of-elevation-and-depression.json::spcpt_9JzR7VMzsQqT4KHq — tier R1_parse_repair_statement_join — score n/a — wording EXACT — validation tier AI_VALIDATED (operator-delegated chain)
- Rationale: SME span 'Elevation & Depression' on note 'Angles of Elevation & Depression' is anchored by the corpus spec_point block spcpt_9JzR7VMzsQqT4KHq and joined to 4MA1-4.8B via operator-verdict statement join after T-SPEC-8 parse repair (PMT excluded as source); this section chunk sits inside that span.
- Verdict: [ ] CONFIRM — this chunk belongs to this SP   [ ] REJECT — wrong chunk/SP   [ ] HOLD — needs rework

### 4MA1-6.1B — construct cumulative frequency diagrams from tabulated data
- Note: Cumulative Frequency (`notes/6-statistics-and-probability/cumulative-frequency-diagrams/cumulative-frequency-diagrams.json`)
- Chunk: ordinal 1 — heading `What is cumulative frequency?` — sha256_16 `4def4dcbdcf6e4c8` — 1517 chars
- Evidence quote (verbatim self-slice, markdown-safe): "What is cumulative frequency?
- **Cumulative** refers to a “running total" or "adding up as you go along”
- So in a table of **grouped data**

  - **cumulative frequency** means all of the frequencies for the different groups totalled up to"
- Chunk excerpt: «What is cumulative frequency? - **Cumulative** refers to a “running total" or "adding up as you go along” - So in a table of **grouped data** - **cumulative frequency** means all of the frequencies for the different groups totalled up to the **end** of the group in a given row - When working out cumulative frequencies you may see **tables** presented in two ways - A regular grouped data table with an extra column for»
- Upstream: T-C32 join notes/6-statistics-and-probability/cumulative-frequency-diagrams/cumulative-frequency-diagrams.json::spcpt_gdR9ykyG92GK4hGr — tier R1_parse_repair_statement_join — score n/a — wording EXACT — validation tier AI_VALIDATED (operator-delegated chain)
- Rationale: SME span 'Cumulative Frequency' on note 'Cumulative Frequency' is anchored by the corpus spec_point block spcpt_gdR9ykyG92GK4hGr and joined to 4MA1-6.1B via operator-verdict statement join after T-SPEC-8 parse repair (PMT excluded as source); this section chunk sits inside that span.
- Verdict: [ ] CONFIRM — this chunk belongs to this SP   [ ] REJECT — wrong chunk/SP   [ ] HOLD — needs rework

### 4MA1-1.4A — understand the meaning of surds
- Note: Simplifying Surds (`notes/1-numbers-and-the-number-system/surds/simplifying-surds.json`)
- Chunk: ordinal 1 — heading `What is a surd?` — sha256_16 `164dceba7cdf99e7` — 202 chars
- Evidence quote (verbatim self-slice, markdown-safe): "What is a surd?
- A surd is the square root of a non-square integer
- Using surds lets you leave answers in exact form

  - e.g. $5\sqrt{2}$  rather than $7.071067812...$
Examples of surds and not-surds"
- Chunk excerpt: «What is a surd? - A surd is the square root of a non-square integer - Using surds lets you leave answers in exact form - e.g. $5\sqrt{2}$ rather than $7.071067812...$ Examples of surds and not-surds»
- Upstream: T-C32 join notes/1-numbers-and-the-number-system/surds/simplifying-surds.json::spcpt_4QRwffMSmK66nXtp — tier R1_parse_repair_statement_join — score n/a — wording EXACT — validation tier AI_VALIDATED (operator-delegated chain)
- Rationale: SME span 'Surds & Exact Values' on note 'Simplifying Surds' is anchored by the corpus spec_point block spcpt_4QRwffMSmK66nXtp and joined to 4MA1-1.4A via operator-verdict statement join after T-SPEC-8 parse repair (PMT excluded as source); this section chunk sits inside that span.
- Verdict: [ ] CONFIRM — this chunk belongs to this SP   [ ] REJECT — wrong chunk/SP   [ ] HOLD — needs rework

### 4MA1-4.6A — understand and use the internal and external intersecting chord properties
- Note: Intersecting Chord Theorem (`notes/4-geometry-and-trigonometry/circle-theorems/intersecting-chord-theorem.json`)
- Chunk: ordinal 7 — heading `What if one of the lines is a tangent?` — sha256_16 `c1ea05d1815d0ab7` — 1849 chars
- Evidence quote (verbatim self-slice, markdown-safe): "What if one of the lines is a tangent?
- A special case of the intersecting secant theorem is when one of the lines is a **tangent**, rather than a secant

  - A tangent **touches the circumference of the circle once**, rather than intersec"
- Chunk excerpt: «What if one of the lines is a tangent? - A special case of the intersecting secant theorem is when one of the lines is a **tangent**, rather than a secant - A tangent **touches the circumference of the circle once**, rather than intersecting it - In this case,** one of the lengths becomes zero** - **BP(AB + BP) = DP(0 + DP) ** - **BP(AB + BP) = DP**<sup>**2**</sup> A diagram illustrating the intersecting chord theore»
- Upstream: T-C32 join notes/4-geometry-and-trigonometry/circle-theorems/intersecting-chord-theorem.json::spcpt_syhVK6wH6NDDfgdB — tier R1_parse_repair_statement_join — score n/a — wording EXACT — validation tier AI_VALIDATED (operator-delegated chain)
- Rationale: SME span 'Intersecting Chord Theorem (External)' on note 'Intersecting Chord Theorem' is anchored by the corpus spec_point block spcpt_syhVK6wH6NDDfgdB and joined to 4MA1-4.6A via operator-verdict statement join after T-SPEC-8 parse repair (PMT excluded as source); this section chunk sits inside that span.
- Verdict: [ ] CONFIRM — this chunk belongs to this SP   [ ] REJECT — wrong chunk/SP   [ ] HOLD — needs rework

### 4MA1-1.4A — understand the meaning of surds
- Note: Simplifying Surds (`notes/1-numbers-and-the-number-system/surds/simplifying-surds.json`)
- Chunk: ordinal 0 — heading `Surds & exact values` — sha256_16 `07779fca1803f122` — 20 chars
- Evidence quote (verbatim self-slice, markdown-safe): "Surds & exact values"
- Chunk excerpt: «Surds & exact values»
- Upstream: T-C32 join notes/1-numbers-and-the-number-system/surds/simplifying-surds.json::spcpt_4QRwffMSmK66nXtp — tier R1_parse_repair_statement_join — score n/a — wording EXACT — validation tier AI_VALIDATED (operator-delegated chain)
- Rationale: SME span 'Surds & Exact Values' on note 'Simplifying Surds' is anchored by the corpus spec_point block spcpt_4QRwffMSmK66nXtp and joined to 4MA1-1.4A via operator-verdict statement join after T-SPEC-8 parse repair (PMT excluded as source); this section chunk sits inside that span.
- Verdict: [ ] CONFIRM — this chunk belongs to this SP   [ ] REJECT — wrong chunk/SP   [ ] HOLD — needs rework

### 4MA1-2.8A — solve quadratic inequalities in one unknown and represent the solution set on a number line
- Note: Solving Quadratic Inequalities (`notes/2-equations-formulae-and-identities/solving-inequalities/solving-quadratic-inequalities.json`)
- Chunk: ordinal 0 — heading `Solving quadratic inequalities` — sha256_16 `30ddd8f8a5cfe2ea` — 30 chars
- Evidence quote (verbatim self-slice, markdown-safe): "Solving quadratic inequalities"
- Chunk excerpt: «Solving quadratic inequalities»
- Upstream: T-C32 join notes/2-equations-formulae-and-identities/solving-inequalities/solving-quadratic-inequalities.json::spcpt_dnkHMPkqhhdDxPkZ — tier R1_parse_repair_statement_join — score n/a — wording EXACT — validation tier AI_VALIDATED (operator-delegated chain)
- Rationale: SME span 'Solving Quadratic Inequalities' on note 'Solving Quadratic Inequalities' is anchored by the corpus spec_point block spcpt_dnkHMPkqhhdDxPkZ and joined to 4MA1-2.8A via operator-verdict statement join after T-SPEC-8 parse repair (PMT excluded as source); this section chunk sits inside that span.
- Verdict: [ ] CONFIRM — this chunk belongs to this SP   [ ] REJECT — wrong chunk/SP   [ ] HOLD — needs rework

### 4MA1-1.4A — understand the meaning of surds
- Note: Simplifying Surds (`notes/1-numbers-and-the-number-system/surds/simplifying-surds.json`)
- Chunk: ordinal 4 — heading `How do I simplify surds?` — sha256_16 `bc2b0fc20745a0eb` — 1895 chars
- Evidence quote (verbatim self-slice, markdown-safe): "How do I simplify surds?
- To **simplify a surd**, factorise the number using a square number, if possible

  - If multiple square numbers are a factor, use the largest
- Use the fact that $\sqrt{ab}=\sqrt{a}\times\sqrt{b}$ and then work ou"
- Chunk excerpt: «How do I simplify surds? - To **simplify a surd**, factorise the number using a square number, if possible - If multiple square numbers are a factor, use the largest - Use the fact that $\sqrt{ab}=\sqrt{a}\times\sqrt{b}$ and then work out any square roots of square numbers - E.g. $\sqrt{48}=\sqrt{16\times3}=\sqrt{16}\times\sqrt{3}=4\times\sqrt{3}=4\sqrt{3}$ Simplifying root 8 to 2 root 2 and root 720 to 12 root 5 - W»
- Upstream: T-C32 join notes/1-numbers-and-the-number-system/surds/simplifying-surds.json::spcpt_stqdXPTn5YvgKtvm — tier R1_parse_repair_statement_join — score n/a — wording EXACT — validation tier AI_VALIDATED (operator-delegated chain)
- Rationale: SME span 'Simplifying Surds' on note 'Simplifying Surds' is anchored by the corpus spec_point block spcpt_stqdXPTn5YvgKtvm and joined to 4MA1-1.4A via operator-verdict statement join after T-SPEC-8 parse repair (PMT excluded as source); this section chunk sits inside that span.
- Verdict: [ ] CONFIRM — this chunk belongs to this SP   [ ] REJECT — wrong chunk/SP   [ ] HOLD — needs rework

### 4MA1-4.6A — understand and use the internal and external intersecting chord properties
- Note: Intersecting Chord Theorem (`notes/4-geometry-and-trigonometry/circle-theorems/intersecting-chord-theorem.json`)
- Chunk: ordinal 6 — heading `How do I use the intersecting secant theorem to solve problems?` — sha256_16 `aa910cc9f10b9209` — 1407 chars
- Evidence quote (verbatim self-slice, markdown-safe): "How do I use the intersecting secant theorem to solve problems?
- If two chords intersect **outside **of a circle, you can find a missing length using the intersecting secant theorem

  - Substitute the values into the multiplication formul"
- Chunk excerpt: «How do I use the intersecting secant theorem to solve problems? - If two chords intersect **outside **of a circle, you can find a missing length using the intersecting secant theorem - Substitute the values into the multiplication formula - **BP(AB + BP) = DP(CD + DP)** - If any of the lengths are **algebraic **expressions, an **equation **will be formed which can then be solved Worked Example: In the diagram below, »
- Upstream: T-C32 join notes/4-geometry-and-trigonometry/circle-theorems/intersecting-chord-theorem.json::spcpt_syhVK6wH6NDDfgdB — tier R1_parse_repair_statement_join — score n/a — wording EXACT — validation tier AI_VALIDATED (operator-delegated chain)
- Rationale: SME span 'Intersecting Chord Theorem (External)' on note 'Intersecting Chord Theorem' is anchored by the corpus spec_point block spcpt_syhVK6wH6NDDfgdB and joined to 4MA1-4.6A via operator-verdict statement join after T-SPEC-8 parse repair (PMT excluded as source); this section chunk sits inside that span.
- Verdict: [ ] CONFIRM — this chunk belongs to this SP   [ ] REJECT — wrong chunk/SP   [ ] HOLD — needs rework

### 4MA1-6.3A — draw and use tree diagrams
- Note: Combined Conditional Probabilities (`notes/6-statistics-and-probability/combined-and-conditional-probability/combined-conditional-probabilities.json`)
- Chunk: ordinal 0 — heading `Combined conditional probabilities` — sha256_16 `6df52b67b02b94da` — 34 chars
- Evidence quote (verbatim self-slice, markdown-safe): "Combined conditional probabilities"
- Chunk excerpt: «Combined conditional probabilities»
- Upstream: T-C32 join notes/6-statistics-and-probability/combined-and-conditional-probability/combined-conditional-probabilities.json::spcpt_9cJGVGKRhP9JYgjF — tier R1_parse_repair_statement_join — score n/a — wording EXACT — validation tier AI_VALIDATED (operator-delegated chain)
- Rationale: SME span 'Combined Conditional Probabilities' on note 'Combined Conditional Probabilities' is anchored by the corpus spec_point block spcpt_9cJGVGKRhP9JYgjF and joined to 4MA1-6.3A via operator-verdict statement join after T-SPEC-8 parse repair (PMT excluded as source); this section chunk sits inside that span.
- Verdict: [ ] CONFIRM — this chunk belongs to this SP   [ ] REJECT — wrong chunk/SP   [ ] HOLD — needs rework

### 4MA1-3.3B — apply to the graph ofy = f(x)the transformations y = f(x) + a, y = f(ax), y = f(x + a), y = af(x) for linear, quadratic, sine and cosine functions
- Note: Reflections of Graphs (`notes/3-sequences-functions-and-graphs/transformations-of-graphs/reflections-of-graphs.json`)
- Chunk: ordinal 7 — heading `How do I apply a combined reflection?` — sha256_16 `d3bfeda4aa02605d` — 1078 chars
- Evidence quote (verbatim self-slice, markdown-safe): "How do I apply a combined reflection?
- The graph of `y equals negative straight f open parentheses negative x close parentheses` is a **combined reflection** in both the $x$ and $y$ axes

  - It **does not matter which order **you apply th"
- Chunk excerpt: «How do I apply a combined reflection? - The graph of `y equals negative straight f open parentheses negative x close parentheses` is a **combined reflection** in both the $x$ and $y$ axes - It **does not matter which order **you apply these in - For example, reflect about the $y$-axis then about the $x$-axis Worked Example: The diagram below shows the graph of `y equals straight f open parentheses x close parentheses»
- Upstream: T-C32 join notes/3-sequences-functions-and-graphs/transformations-of-graphs/reflections-of-graphs.json::spcpt_qNDqnmZtzYttZDnz — tier P2_operator_content_join — score n/a — wording EXACT — validation tier AI_VALIDATED (operator-delegated chain)
- Rationale: SME span 'Reflections of Graphs' on note 'Reflections of Graphs' is anchored by the corpus spec_point block spcpt_qNDqnmZtzYttZDnz and joined to 4MA1-3.3B via T-SPEC-9 operator verdict (no upstream; PMT excluded as source); this section chunk sits inside that span.
- Verdict: [ ] CONFIRM — this chunk belongs to this SP   [ ] REJECT — wrong chunk/SP   [ ] HOLD — needs rework

### 4MA1-4.8C — understand and use the sine and cosine rules for any triangle
- Note: The Cosine Rule (`notes/4-geometry-and-trigonometry/sine-cosine-rule-and-area-of-triangles/the-cosine-rule.json`)
- Chunk: ordinal 0 — heading `Cosine rule` — sha256_16 `7da2e3a359b9c306` — 11 chars
- Evidence quote (verbatim self-slice, markdown-safe): "Cosine rule"
- Chunk excerpt: «Cosine rule»
- Upstream: T-C32 join notes/4-geometry-and-trigonometry/sine-cosine-rule-and-area-of-triangles/the-cosine-rule.json::spcpt_HnxHKwwfTxKcvCN7 — tier R1_parse_repair_statement_join — score n/a — wording EXACT — validation tier AI_VALIDATED (operator-delegated chain)
- Rationale: SME span 'Cosine Rule' on note 'The Cosine Rule' is anchored by the corpus spec_point block spcpt_HnxHKwwfTxKcvCN7 and joined to 4MA1-4.8C via operator-verdict statement join after T-SPEC-8 parse repair (PMT excluded as source); this section chunk sits inside that span.
- Verdict: [ ] CONFIRM — this chunk belongs to this SP   [ ] REJECT — wrong chunk/SP   [ ] HOLD — needs rework

### 4MA1-2.8A — solve quadratic inequalities in one unknown and represent the solution set on a number line
- Note: Solving Quadratic Inequalities (`notes/2-equations-formulae-and-identities/solving-inequalities/solving-quadratic-inequalities.json`)
- Chunk: ordinal 2 — heading `How do I solve a quadratic inequality?` — sha256_16 `68d0962590784150` — 1289 chars
- Evidence quote (verbatim self-slice, markdown-safe): "How do I solve a quadratic inequality?
- Quadratic inequalities are** solved **by **sketching a graph**

  - The solutions then appears along the $x$-axis
- For example, to solve `open parentheses x minus 2 close parentheses open parenthese"
- Chunk excerpt: «How do I solve a quadratic inequality? - Quadratic inequalities are** solved **by **sketching a graph** - The solutions then appears along the $x$-axis - For example, to solve `open parentheses x minus 2 close parentheses open parentheses x minus 5 close parentheses greater or equal than 0` - Sketch the graph of `y equals open parentheses x minus 2 close parentheses open parentheses x minus 5 close parentheses` - Sho»
- Upstream: T-C32 join notes/2-equations-formulae-and-identities/solving-inequalities/solving-quadratic-inequalities.json::spcpt_dnkHMPkqhhdDxPkZ — tier R1_parse_repair_statement_join — score n/a — wording EXACT — validation tier AI_VALIDATED (operator-delegated chain)
- Rationale: SME span 'Solving Quadratic Inequalities' on note 'Solving Quadratic Inequalities' is anchored by the corpus spec_point block spcpt_dnkHMPkqhhdDxPkZ and joined to 4MA1-2.8A via operator-verdict statement join after T-SPEC-8 parse repair (PMT excluded as source); this section chunk sits inside that span.
- Verdict: [ ] CONFIRM — this chunk belongs to this SP   [ ] REJECT — wrong chunk/SP   [ ] HOLD — needs rework

### 4MA1-6.1B — construct cumulative frequency diagrams from tabulated data
- Note: Interpreting Cumulative Frequency Diagrams (`notes/6-statistics-and-probability/cumulative-frequency-diagrams/interpreting-cumulative-frequency-diagrams.json`)
- Chunk: ordinal 2 — heading `How do I find the median, lower quartile and upper quartile from a cumulative frequency diagram?` — sha256_16 `b095dc8f29b31bd1` — 2227 chars
- Evidence quote (verbatim self-slice, markdown-safe): "How do I find the median, lower quartile and upper quartile from a cumulative frequency diagram?
- This is all about understanding **how many data values** are represented by the cumulative frequency diagram

  - This may be **stated** in w"
- Chunk excerpt: «How do I find the median, lower quartile and upper quartile from a cumulative frequency diagram? - This is all about understanding **how many data values** are represented by the cumulative frequency diagram - This may be **stated** in words within the question - If not, it will be the **highest value** on the frequency (*y*-) axis that the curve on the diagram reaches - This should be "top right" of the curve on a c»
- Upstream: T-C32 join notes/6-statistics-and-probability/cumulative-frequency-diagrams/interpreting-cumulative-frequency-diagrams.json::spcpt_8sCVwmD5VVBv6xWg — tier R1_parse_repair_statement_join — score n/a — wording EXACT — validation tier AI_VALIDATED (operator-delegated chain)
- Rationale: SME span 'Interpreting Cumulative Frequency Diagrams' on note 'Interpreting Cumulative Frequency Diagrams' is anchored by the corpus spec_point block spcpt_8sCVwmD5VVBv6xWg and joined to 4MA1-6.1B via operator-verdict statement join after T-SPEC-8 parse repair (PMT excluded as source); this section chunk sits inside that span.
- Verdict: [ ] CONFIRM — this chunk belongs to this SP   [ ] REJECT — wrong chunk/SP   [ ] HOLD — needs rework

### 4MA1-2.2C — manipulate algebraic fractions where the numerator and/or the denominator can be numeric, linear or quadratic
- Note: Multiplying & Dividing Algebraic Fractions (`notes/2-equations-formulae-and-identities/algebraic-fractions/multiplying-and-dividing-algebraic-fractions.json`)
- Chunk: ordinal 1 — heading `How do I multiply algebraic fractions?` — sha256_16 `59570ab8fe238541` — 4805 chars
- Evidence quote (verbatim self-slice, markdown-safe): "How do I multiply algebraic fractions?
- **STEP 1** **Simplify** both fractions first by** fully factorising**

  - E.g. `fraction numerator x over denominator 3 x plus 6 end fraction cross times fraction numerator 2 x plus 4 over denominat"
- Chunk excerpt: «How do I multiply algebraic fractions? - **STEP 1** **Simplify** both fractions first by** fully factorising** - E.g. `fraction numerator x over denominator 3 x plus 6 end fraction cross times fraction numerator 2 x plus 4 over denominator x plus 7 end fraction equals fraction numerator x over denominator 3 open parentheses x plus 2 close parentheses end fraction cross times fraction numerator 2 open parentheses x pl»
- Upstream: T-C32 join notes/2-equations-formulae-and-identities/algebraic-fractions/multiplying-and-dividing-algebraic-fractions.json::spcpt_j2YgCQ3HvtrTXdG4 — tier R1_parse_repair_statement_join — score n/a — wording EXACT — validation tier AI_VALIDATED (operator-delegated chain)
- Rationale: SME span 'Multiplying & Dividing Algebraic Fractions' on note 'Multiplying & Dividing Algebraic Fractions' is anchored by the corpus spec_point block spcpt_j2YgCQ3HvtrTXdG4 and joined to 4MA1-2.2C via operator-verdict statement join after T-SPEC-8 parse repair (PMT excluded as source); this section chunk sits inside that span.
- Verdict: [ ] CONFIRM — this chunk belongs to this SP   [ ] REJECT — wrong chunk/SP   [ ] HOLD — needs rework

### 4MA1-2.2B — understand the concept of a quadratic expression and be able to factorise such expressions
- Note: Factorising Harder Quadratics (`notes/2-equations-formulae-and-identities/factorising/factorising-harder-quadratics.json`)
- Chunk: ordinal 2 — heading `Method 1: Factorising by grouping` — sha256_16 `f24a8401431584d8` — 1006 chars
- Evidence quote (verbatim self-slice, markdown-safe): "Method 1: Factorising by grouping
- This is shown most easily through an example: factorising $4x^{2}-25x-21$
- We need a **pair of numbers** that, for $ax^{2}+bx+c$

  - both **multiply **to give *ac*
  
    - *ac* in this case is 4 × -21 "
- Chunk excerpt: «Method 1: Factorising by grouping - This is shown most easily through an example: factorising $4x^{2}-25x-21$ - We need a **pair of numbers** that, for $ax^{2}+bx+c$ - both **multiply **to give *ac* - *ac* in this case is 4 × -21 = -84 - and both **add **to give *b* - *b* in this case is -25 - -28 and +3 satisfy these conditions - **Rewrite **the middle term using -28*x* and +3*x* - $4x^{2}-28x+3x-21$ - **Group **and»
- Upstream: T-C32 join notes/2-equations-formulae-and-identities/factorising/factorising-harder-quadratics.json::spcpt_rt6wRVmbK5ZVkF3d — tier R1_parse_repair_statement_join — score n/a — wording EXACT — validation tier AI_VALIDATED (operator-delegated chain)
- Rationale: SME span 'Factorising Harder Quadratics' on note 'Factorising Harder Quadratics' is anchored by the corpus spec_point block spcpt_rt6wRVmbK5ZVkF3d and joined to 4MA1-2.2B via operator-verdict statement join after T-SPEC-8 parse repair (PMT excluded as source); this section chunk sits inside that span.
- Verdict: [ ] CONFIRM — this chunk belongs to this SP   [ ] REJECT — wrong chunk/SP   [ ] HOLD — needs rework

### 4MA1-3.3B — apply to the graph ofy = f(x)the transformations y = f(x) + a, y = f(ax), y = f(x + a), y = af(x) for linear, quadratic, sine and cosine functions
- Note: Translations of Graphs (`notes/3-sequences-functions-and-graphs/transformations-of-graphs/translations-of-graphs.json`)
- Chunk: ordinal 5 — heading `What happens to asymptotes when a graph is translated?` — sha256_16 `1be5281d860f0c9d` — 238 chars
- Evidence quote (verbatim self-slice, markdown-safe): "What happens to asymptotes when a graph is translated?
- Any ***asymptotes*** of **f(*****x*****)** are also translated

  - An asymptote **parallel** to the **direction of translation** will **not **be affected
Translations of asymptotes"
- Chunk excerpt: «What happens to asymptotes when a graph is translated? - Any ***asymptotes*** of **f(*****x*****)** are also translated - An asymptote **parallel** to the **direction of translation** will **not **be affected Translations of asymptotes»
- Upstream: T-C32 join notes/3-sequences-functions-and-graphs/transformations-of-graphs/translations-of-graphs.json::spcpt_wt53CcTmwpZ3sjm3 — tier P2_operator_content_join — score n/a — wording EXACT — validation tier AI_VALIDATED (operator-delegated chain)
- Rationale: SME span 'Translations of Graphs' on note 'Translations of Graphs' is anchored by the corpus spec_point block spcpt_wt53CcTmwpZ3sjm3 and joined to 4MA1-3.3B via T-SPEC-9 operator verdict (no upstream; PMT excluded as source); this section chunk sits inside that span.
- Verdict: [ ] CONFIRM — this chunk belongs to this SP   [ ] REJECT — wrong chunk/SP   [ ] HOLD — needs rework

### 4MA1-4.6A — understand and use the internal and external intersecting chord properties
- Note: Intersecting Chord Theorem (`notes/4-geometry-and-trigonometry/circle-theorems/intersecting-chord-theorem.json`)
- Chunk: ordinal 5 — heading `What is the external case of the intersecting chord theorem?` — sha256_16 `066143f808c48872` — 885 chars
- Evidence quote (verbatim self-slice, markdown-safe): "What is the external case of the intersecting chord theorem?
- The **intersecting secant theorem **is the mathematical name given to the **external case of the intersecting chord theorem**

  - A **secant **is a line which **extends through"
- Chunk excerpt: «What is the external case of the intersecting chord theorem? - The **intersecting secant theorem **is the mathematical name given to the **external case of the intersecting chord theorem** - A **secant **is a line which **extends through **a circle cutting the circumference at two points - It occurs when two chords **intersect outside of the circle** - For two chords, **AB** and **CD** that extend and meet at point *»
- Upstream: T-C32 join notes/4-geometry-and-trigonometry/circle-theorems/intersecting-chord-theorem.json::spcpt_syhVK6wH6NDDfgdB — tier R1_parse_repair_statement_join — score n/a — wording EXACT — validation tier AI_VALIDATED (operator-delegated chain)
- Rationale: SME span 'Intersecting Chord Theorem (External)' on note 'Intersecting Chord Theorem' is anchored by the corpus spec_point block spcpt_syhVK6wH6NDDfgdB and joined to 4MA1-4.6A via operator-verdict statement join after T-SPEC-8 parse repair (PMT excluded as source); this section chunk sits inside that span.
- Verdict: [ ] CONFIRM — this chunk belongs to this SP   [ ] REJECT — wrong chunk/SP   [ ] HOLD — needs rework

### 4MA1-3.3B — apply to the graph ofy = f(x)the transformations y = f(x) + a, y = f(ax), y = f(x + a), y = af(x) for linear, quadratic, sine and cosine functions
- Note: Stretches of Graphs (`notes/3-sequences-functions-and-graphs/transformations-of-graphs/stretches-of-graphs.json`)
- Chunk: ordinal 1 — heading `What are stretches of graphs?` — sha256_16 `8e847b315a13e136` — 295 chars
- Evidence quote (verbatim self-slice, markdown-safe): "What are stretches of graphs?
- **Stretches **of graphs are a type of **transformation** that pushes points away from, or towards, the $x$-axis or $y$-axis

  - Graphs look like they have been **stretched** or **squashed**
  
    - either *"
- Chunk excerpt: «What are stretches of graphs? - **Stretches **of graphs are a type of **transformation** that pushes points away from, or towards, the $x$-axis or $y$-axis - Graphs look like they have been **stretched** or **squashed** - either **horizontally** or **vertically** Examples of stretches»
- Upstream: T-C32 join notes/3-sequences-functions-and-graphs/transformations-of-graphs/stretches-of-graphs.json::spcpt_YcMPxJgtrjtBzMkV — tier P2_operator_content_join — score n/a — wording EXACT — validation tier AI_VALIDATED (operator-delegated chain)
- Rationale: SME span 'Stretches of Graphs' on note 'Stretches of Graphs' is anchored by the corpus spec_point block spcpt_YcMPxJgtrjtBzMkV and joined to 4MA1-3.3B via T-SPEC-9 operator verdict (no upstream; PMT excluded as source); this section chunk sits inside that span.
- Verdict: [ ] CONFIRM — this chunk belongs to this SP   [ ] REJECT — wrong chunk/SP   [ ] HOLD — needs rework

### 4MA1-3.3B — apply to the graph ofy = f(x)the transformations y = f(x) + a, y = f(ax), y = f(x + a), y = af(x) for linear, quadratic, sine and cosine functions
- Note: Translations of Graphs (`notes/3-sequences-functions-and-graphs/transformations-of-graphs/translations-of-graphs.json`)
- Chunk: ordinal 1 — heading `What are translations of graphs?` — sha256_16 `f0920615955b7795` — 514 chars
- Evidence quote (verbatim self-slice, markdown-safe): "What are translations of graphs?
- The **equation** of a graph can be changed in certain ways

  - This has an effect on the **graph**
  
    - How a graph changes is called a **graph transformation**
- A **translation** is a type of graph "
- Chunk excerpt: «What are translations of graphs? - The **equation** of a graph can be changed in certain ways - This has an effect on the **graph** - How a graph changes is called a **graph transformation** - A **translation** is a type of graph transformation that **shifts (moves)** a graph (up or down, left or right) in the *xy* plane - The shape, size, and orientation of the graph remain unchanged Examples of translations - A par»
- Upstream: T-C32 join notes/3-sequences-functions-and-graphs/transformations-of-graphs/translations-of-graphs.json::spcpt_wt53CcTmwpZ3sjm3 — tier P2_operator_content_join — score n/a — wording EXACT — validation tier AI_VALIDATED (operator-delegated chain)
- Rationale: SME span 'Translations of Graphs' on note 'Translations of Graphs' is anchored by the corpus spec_point block spcpt_wt53CcTmwpZ3sjm3 and joined to 4MA1-3.3B via T-SPEC-9 operator verdict (no upstream; PMT excluded as source); this section chunk sits inside that span.
- Verdict: [ ] CONFIRM — this chunk belongs to this SP   [ ] REJECT — wrong chunk/SP   [ ] HOLD — needs rework

### 4MA1-6.1B — construct cumulative frequency diagrams from tabulated data
- Note: Drawing Cumulative Frequency Diagrams (`notes/6-statistics-and-probability/cumulative-frequency-diagrams/drawing-cumulative-frequency-diagrams.json`)
- Chunk: ordinal 2 — heading `How do I draw a cumulative frequency diagram?` — sha256_16 `49810306f00ffc79` — 2135 chars
- Evidence quote (verbatim self-slice, markdown-safe): "How do I draw a cumulative frequency diagram?
- This is best explained with an example

  - The times taken to complete a short general knowledge quiz taken by 50 students are shown in the table below: | **Time taken (**$s$** seconds)** | *"
- Chunk excerpt: «How do I draw a cumulative frequency diagram? - This is best explained with an example - The times taken to complete a short general knowledge quiz taken by 50 students are shown in the table below: | **Time taken (**$s$** seconds)** | **Frequency** | |---|---| | $25\leqs<30$ | 3 | | $30\leqs<35$ | 8 | | $35\leqs<40$ | 17 | | $40\leqs<45$ | 12 | | $45\leqs<50$ | 7 | | $50\leqs<55$ | 3 | | **Total** | **50** | - Then »
- Upstream: T-C32 join notes/6-statistics-and-probability/cumulative-frequency-diagrams/drawing-cumulative-frequency-diagrams.json::spcpt_kwGrBDCwB6YtVVBQ — tier R1_parse_repair_statement_join — score n/a — wording EXACT — validation tier AI_VALIDATED (operator-delegated chain)
- Rationale: SME span 'Drawing Cumulative Frequency Diagrams' on note 'Drawing Cumulative Frequency Diagrams' is anchored by the corpus spec_point block spcpt_kwGrBDCwB6YtVVBQ and joined to 4MA1-6.1B via operator-verdict statement join after T-SPEC-8 parse repair (PMT excluded as source); this section chunk sits inside that span.
- Verdict: [ ] CONFIRM — this chunk belongs to this SP   [ ] REJECT — wrong chunk/SP   [ ] HOLD — needs rework

### 4MA1-6.3A — draw and use tree diagrams
- Note: Combined Conditional Probabilities (`notes/6-statistics-and-probability/combined-and-conditional-probability/combined-conditional-probabilities.json`)
- Chunk: ordinal 3 — heading `Can I draw a tree diagram for combined conditional probabilities?` — sha256_16 `f696c26d90c6efe7` — 317 chars
- Evidence quote (verbatim self-slice, markdown-safe): "Can I draw a tree diagram for combined conditional probabilities?
- Yes, a **tree diagram** is a useful way to show combined conditional probabilities

  - For example, two counters are drawn at random from a bag of 3 blue and 8 red counter"
- Chunk excerpt: «Can I draw a tree diagram for combined conditional probabilities? - Yes, a **tree diagram** is a useful way to show combined conditional probabilities - For example, two counters are drawn at random from a bag of 3 blue and 8 red counters without replacement - The probabilities are shown below Tree Diagram»
- Upstream: T-C32 join notes/6-statistics-and-probability/combined-and-conditional-probability/combined-conditional-probabilities.json::spcpt_9cJGVGKRhP9JYgjF — tier R1_parse_repair_statement_join — score n/a — wording EXACT — validation tier AI_VALIDATED (operator-delegated chain)
- Rationale: SME span 'Combined Conditional Probabilities' on note 'Combined Conditional Probabilities' is anchored by the corpus spec_point block spcpt_9cJGVGKRhP9JYgjF and joined to 4MA1-6.3A via operator-verdict statement join after T-SPEC-8 parse repair (PMT excluded as source); this section chunk sits inside that span.
- Verdict: [ ] CONFIRM — this chunk belongs to this SP   [ ] REJECT — wrong chunk/SP   [ ] HOLD — needs rework

### 4MA1-4.8C — understand and use the sine and cosine rules for any triangle
- Note: The Cosine Rule (`notes/4-geometry-and-trigonometry/sine-cosine-rule-and-area-of-triangles/the-cosine-rule.json`)
- Chunk: ordinal 1 — heading `What is the cosine rule?` — sha256_16 `4e9e5be4f926832a` — 509 chars
- Evidence quote (verbatim self-slice, markdown-safe): "What is the cosine rule?
- The **cosine rule** is used in **non** **right-angled triangles**

  - It allows us to find missing side lengths or angles
- It states that for any triangle
$a^{2}=b^{2}+c^{2}-2bc\mathrm{cos}A$
- Where

  - $a$* *"
- Chunk excerpt: «What is the cosine rule? - The **cosine rule** is used in **non** **right-angled triangles** - It allows us to find missing side lengths or angles - It states that for any triangle $a^{2}=b^{2}+c^{2}-2bc\mathrm{cos}A$ - Where - $a$* *is the side **opposite** angle *A* - $b$* *and $c$* *are the other two sides - $b$* *and $c$ are either side of angle *A* - *A *is the angle between them Non Right-Angled Triangle labell»
- Upstream: T-C32 join notes/4-geometry-and-trigonometry/sine-cosine-rule-and-area-of-triangles/the-cosine-rule.json::spcpt_HnxHKwwfTxKcvCN7 — tier R1_parse_repair_statement_join — score n/a — wording EXACT — validation tier AI_VALIDATED (operator-delegated chain)
- Rationale: SME span 'Cosine Rule' on note 'The Cosine Rule' is anchored by the corpus spec_point block spcpt_HnxHKwwfTxKcvCN7 and joined to 4MA1-4.8C via operator-verdict statement join after T-SPEC-8 parse repair (PMT excluded as source); this section chunk sits inside that span.
- Verdict: [ ] CONFIRM — this chunk belongs to this SP   [ ] REJECT — wrong chunk/SP   [ ] HOLD — needs rework

### 4MA1-4.6A — understand and use the internal and external intersecting chord properties
- Note: Intersecting Chord Theorem (`notes/4-geometry-and-trigonometry/circle-theorems/intersecting-chord-theorem.json`)
- Chunk: ordinal 0 — heading `Intersecting chord theorem` — sha256_16 `bc8273275b1fe707` — 26 chars
- Evidence quote (verbatim self-slice, markdown-safe): "Intersecting chord theorem"
- Chunk excerpt: «Intersecting chord theorem»
- Upstream: T-C32 join notes/4-geometry-and-trigonometry/circle-theorems/intersecting-chord-theorem.json::spcpt_znWXTZjqCR7PspTc — tier R1_parse_repair_statement_join — score n/a — wording EXACT — validation tier AI_VALIDATED (operator-delegated chain)
- Rationale: SME span 'Intersecting Chord Theorem' on note 'Intersecting Chord Theorem' is anchored by the corpus spec_point block spcpt_znWXTZjqCR7PspTc and joined to 4MA1-4.6A via operator-verdict statement join after T-SPEC-8 parse repair (PMT excluded as source); this section chunk sits inside that span.
- Verdict: [ ] CONFIRM — this chunk belongs to this SP   [ ] REJECT — wrong chunk/SP   [ ] HOLD — needs rework

### 4MA1-6.3B — determine the probability that two or more independent events will occur
- Note: Conditional Probability (`notes/6-statistics-and-probability/combined-and-conditional-probability/conditional-probability.json`)
- Chunk: ordinal 2 — heading `How do I calculate conditional probabilities?` — sha256_16 `dbdc34be889dd08b` — 1762 chars
- Evidence quote (verbatim self-slice, markdown-safe): "How do I calculate conditional probabilities?
- Conditional probabilities must be out of a **smaller restricted set** of outcomes (not out of all possible events)

  - For example, if a computer randomly selects a digit from 1, 2, 3, 4, 5, "
- Chunk excerpt: «How do I calculate conditional probabilities? - Conditional probabilities must be out of a **smaller restricted set** of outcomes (not out of all possible events) - For example, if a computer randomly selects a digit from 1, 2, 3, 4, 5, 6, 7, 8, 9 - P(it select a multiple of three) = $\frac{3}{9}$ - This is **not **a conditional probability - There are 3 possibilities (3, 6, 9) out of **all **9 possibilities - Howeve»
- Upstream: T-C32 join notes/6-statistics-and-probability/combined-and-conditional-probability/conditional-probability.json::spcpt_DkBXXfmWk2hGVF6Y — tier P1_name_fragment_join — score n/a — wording EXACT — validation tier AI_VALIDATED (operator-delegated chain)
- Rationale: SME span 'Conditional Probability' on note 'Conditional Probability' is anchored by the corpus spec_point block spcpt_DkBXXfmWk2hGVF6Y and joined to 4MA1-6.3B via operator-verdict name-fragment join (T-SPEC-7; PMT excluded as source); this section chunk sits inside that span.
- Verdict: [ ] CONFIRM — this chunk belongs to this SP   [ ] REJECT — wrong chunk/SP   [ ] HOLD — needs rework

### 4MA1-6.3B — determine the probability that two or more independent events will occur
- Note: Conditional Probability (`notes/6-statistics-and-probability/combined-and-conditional-probability/conditional-probability.json`)
- Chunk: ordinal 0 — heading `Conditional probability` — sha256_16 `807b61c4f757813b` — 23 chars
- Evidence quote (verbatim self-slice, markdown-safe): "Conditional probability"
- Chunk excerpt: «Conditional probability»
- Upstream: T-C32 join notes/6-statistics-and-probability/combined-and-conditional-probability/conditional-probability.json::spcpt_DkBXXfmWk2hGVF6Y — tier P1_name_fragment_join — score n/a — wording EXACT — validation tier AI_VALIDATED (operator-delegated chain)
- Rationale: SME span 'Conditional Probability' on note 'Conditional Probability' is anchored by the corpus spec_point block spcpt_DkBXXfmWk2hGVF6Y and joined to 4MA1-6.3B via operator-verdict name-fragment join (T-SPEC-7; PMT excluded as source); this section chunk sits inside that span.
- Verdict: [ ] CONFIRM — this chunk belongs to this SP   [ ] REJECT — wrong chunk/SP   [ ] HOLD — needs rework

### 4MA1-6.1A — construct and interpret histograms
- Note: Interpreting Histograms (`notes/6-statistics-and-probability/histograms/interpreting-histograms.json`)
- Chunk: ordinal 1 — heading `How do I interpret a histogram?` — sha256_16 `0b195f580922e0e0` — 3979 chars
- Evidence quote (verbatim self-slice, markdown-safe): "How do I interpret a histogram?
- It is important to remember that the frequency density (*y-*) axis does not tell us frequency

  - The** area of the bar **is equal to the** frequency**
  
    - `table row frequency equals cell frequency s"
- Chunk excerpt: «How do I interpret a histogram? - It is important to remember that the frequency density (*y-*) axis does not tell us frequency - The** area of the bar **is equal to the** frequency** - `table row frequency equals cell frequency space density cross times class space width end cell end table` - Note that a very **simple** histogram may have **equal class widths** - In this case the *y-*axis may be labelled 'frequency'»
- Upstream: T-C32 join notes/6-statistics-and-probability/histograms/interpreting-histograms.json::spcpt_zNgS9BtJ7493zsyx — tier R1_parse_repair_statement_join — score n/a — wording EXACT — validation tier AI_VALIDATED (operator-delegated chain)
- Rationale: SME span 'Interpreting Histograms' on note 'Interpreting Histograms' is anchored by the corpus spec_point block spcpt_zNgS9BtJ7493zsyx and joined to 4MA1-6.1A via operator-verdict statement join after T-SPEC-8 parse repair (PMT excluded as source); this section chunk sits inside that span.
- Verdict: [ ] CONFIRM — this chunk belongs to this SP   [ ] REJECT — wrong chunk/SP   [ ] HOLD — needs rework

### 4MA1-1.3A — convert recurring decimals into fractions
- Note: Recurring Decimals (`notes/1-numbers-and-the-number-system/fractions-decimals-and-percentages/recurring-decimals.json`)
- Chunk: ordinal 1 — heading `What are recurring decimals?` — sha256_16 `ff87965a2dd99c16` — 790 chars
- Evidence quote (verbatim self-slice, markdown-safe): "What are recurring decimals?
- When writing a ***rational number***** **as a decimal, it will either be:

  - A decimal that stops, called a "**terminating**" decimal
  
    - $\frac{1}{4}=0.25$
  - Or a decimal that repeats with a pattern,"
- Chunk excerpt: «What are recurring decimals? - When writing a ***rational number***** **as a decimal, it will either be: - A decimal that stops, called a "**terminating**" decimal - $\frac{1}{4}=0.25$ - Or a decimal that repeats with a pattern, called a "**recurring**" decimal - $\frac{32}{99}=0.32323232...$ - The recurring part can be written with a **dot above the digit that repeats** - If multiple digits repeat, dots are used on »
- Upstream: T-C32 join notes/1-numbers-and-the-number-system/fractions-decimals-and-percentages/recurring-decimals.json::spcpt_BVf2GTX8FCvzJjJN — tier R1_parse_repair_statement_join — score n/a — wording EXACT — validation tier AI_VALIDATED (operator-delegated chain)
- Rationale: SME span 'Recurring Decimals' on note 'Recurring Decimals' is anchored by the corpus spec_point block spcpt_BVf2GTX8FCvzJjJN and joined to 4MA1-1.3A via operator-verdict statement join after T-SPEC-8 parse repair (PMT excluded as source); this section chunk sits inside that span.
- Verdict: [ ] CONFIRM — this chunk belongs to this SP   [ ] REJECT — wrong chunk/SP   [ ] HOLD — needs rework

### 4MA1-3.3B — apply to the graph ofy = f(x)the transformations y = f(x) + a, y = f(ax), y = f(x + a), y = af(x) for linear, quadratic, sine and cosine functions
- Note: Translations of Graphs (`notes/3-sequences-functions-and-graphs/transformations-of-graphs/translations-of-graphs.json`)
- Chunk: ordinal 7 — heading `How do I apply a combined translation?` — sha256_16 `9bcabca79f3d66ad` — 1817 chars
- Evidence quote (verbatim self-slice, markdown-safe): "How do I apply a combined translation?
- For a **horizontal translation** of $p$ units and **vertical translation** of $q$units **combined**

  - `y equals straight f open parentheses x close parentheses` becomes `y equals straight f open p"
- Chunk excerpt: «How do I apply a combined translation? - For a **horizontal translation** of $p$ units and **vertical translation** of $q$units **combined** - `y equals straight f open parentheses x close parentheses` becomes `y equals straight f open parentheses x minus p close parentheses plus q` - E.g. the graph $y=3x^{2}$ undergoes a **translation** of **2 units up **and **1 unit **to the** left** - `y equals straight f open par»
- Upstream: T-C32 join notes/3-sequences-functions-and-graphs/transformations-of-graphs/translations-of-graphs.json::spcpt_wt53CcTmwpZ3sjm3 — tier P2_operator_content_join — score n/a — wording EXACT — validation tier AI_VALIDATED (operator-delegated chain)
- Rationale: SME span 'Translations of Graphs' on note 'Translations of Graphs' is anchored by the corpus spec_point block spcpt_wt53CcTmwpZ3sjm3 and joined to 4MA1-3.3B via T-SPEC-9 operator verdict (no upstream; PMT excluded as source); this section chunk sits inside that span.
- Verdict: [ ] CONFIRM — this chunk belongs to this SP   [ ] REJECT — wrong chunk/SP   [ ] HOLD — needs rework

### 4MA1-6.1A — construct and interpret histograms
- Note: Drawing Histograms (`notes/6-statistics-and-probability/histograms/drawing-histograms.json`)
- Chunk: ordinal 2 — heading `How do I draw a histogram?` — sha256_16 `77eddb175e2e73d6` — 2073 chars
- Evidence quote (verbatim self-slice, markdown-safe): "How do I draw a histogram?
- **Drawing** a histogram first requires the calculation of the **frequency densities** for each class interval (group)

  - Use  `table row cell frequency space density end cell equals cell fraction numerator fre"
- Chunk excerpt: «How do I draw a histogram? - **Drawing** a histogram first requires the calculation of the **frequency densities** for each class interval (group) - Use `table row cell frequency space density end cell equals cell fraction numerator frequency over denominator class space width end fraction end cell end table` - Exam questions often ask you to **finish** an incomplete histogram, rather than start with a blank graph - »
- Upstream: T-C32 join notes/6-statistics-and-probability/histograms/drawing-histograms.json::spcpt_nJCDx3cDGTVz3MBk — tier R1_parse_repair_statement_join — score n/a — wording EXACT — validation tier AI_VALIDATED (operator-delegated chain)
- Rationale: SME span 'Drawing Histograms' on note 'Drawing Histograms' is anchored by the corpus spec_point block spcpt_nJCDx3cDGTVz3MBk and joined to 4MA1-6.1A via operator-verdict statement join after T-SPEC-8 parse repair (PMT excluded as source); this section chunk sits inside that span.
- Verdict: [ ] CONFIRM — this chunk belongs to this SP   [ ] REJECT — wrong chunk/SP   [ ] HOLD — needs rework

### 4MA1-3.3B — apply to the graph ofy = f(x)the transformations y = f(x) + a, y = f(ax), y = f(x + a), y = af(x) for linear, quadratic, sine and cosine functions
- Note: Reflections of Graphs (`notes/3-sequences-functions-and-graphs/transformations-of-graphs/reflections-of-graphs.json`)
- Chunk: ordinal 5 — heading `What happens to asymptotes when a graph is reflected?` — sha256_16 `f1738e4be0b9bdec` — 337 chars
- Evidence quote (verbatim self-slice, markdown-safe): "What happens to asymptotes when a graph is reflected?
- Any ***asymptotes*** of `straight f open parentheses x close parentheses` are also reflected
When a graph is reflected, any asymptotes are reflected too
Exam Hint: When reflecting grap"
- Chunk excerpt: «What happens to asymptotes when a graph is reflected? - Any ***asymptotes*** of `straight f open parentheses x close parentheses` are also reflected When a graph is reflected, any asymptotes are reflected too Exam Hint: When reflecting graphs in the exam, reflect any key points on the graph first, then join them up with a smooth curve.»
- Upstream: T-C32 join notes/3-sequences-functions-and-graphs/transformations-of-graphs/reflections-of-graphs.json::spcpt_qNDqnmZtzYttZDnz — tier P2_operator_content_join — score n/a — wording EXACT — validation tier AI_VALIDATED (operator-delegated chain)
- Rationale: SME span 'Reflections of Graphs' on note 'Reflections of Graphs' is anchored by the corpus spec_point block spcpt_qNDqnmZtzYttZDnz and joined to 4MA1-3.3B via T-SPEC-9 operator verdict (no upstream; PMT excluded as source); this section chunk sits inside that span.
- Verdict: [ ] CONFIRM — this chunk belongs to this SP   [ ] REJECT — wrong chunk/SP   [ ] HOLD — needs rework

### 4MA1-2.2E — use algebra to support and construct proofs
- Note: Algebraic Proof (`notes/2-equations-formulae-and-identities/algebraic-proof/algebraic-proof.json`)
- Chunk: ordinal 0 — heading `Algebraic proof` — sha256_16 `a3447a460a6bf982` — 15 chars
- Evidence quote (verbatim self-slice, markdown-safe): "Algebraic proof"
- Chunk excerpt: «Algebraic proof»
- Upstream: T-C32 join notes/2-equations-formulae-and-identities/algebraic-proof/algebraic-proof.json::spcpt_dgG8VyxX4bgSvRz7 — tier R1_parse_repair_statement_join — score n/a — wording EXACT — validation tier AI_VALIDATED (operator-delegated chain)
- Rationale: SME span 'Algebraic Proof' on note 'Algebraic Proof' is anchored by the corpus spec_point block spcpt_dgG8VyxX4bgSvRz7 and joined to 4MA1-2.2E via operator-verdict statement join after T-SPEC-8 parse repair (PMT excluded as source); this section chunk sits inside that span.
- Verdict: [ ] CONFIRM — this chunk belongs to this SP   [ ] REJECT — wrong chunk/SP   [ ] HOLD — needs rework

### 4MA1-2.2E — use algebra to support and construct proofs
- Note: Algebraic Proof (`notes/2-equations-formulae-and-identities/algebraic-proof/algebraic-proof.json`)
- Chunk: ordinal 4 — heading `How do I prove results with prime numbers?` — sha256_16 `f298e9f2afb33942` — 3007 chars
- Evidence quote (verbatim self-slice, markdown-safe): "How do I prove results with prime numbers?
- When proving results with** prime numbers**, remember that primes** only have two factors**: 1 and themselves

  - If *p* is prime then 1 × *p* or *p* × 1 are the only ways to write it as a produ"
- Chunk excerpt: «How do I prove results with prime numbers? - When proving results with** prime numbers**, remember that primes** only have two factors**: 1 and themselves - If *p* is prime then 1 × *p* or *p* × 1 are the only ways to write it as a product of two integers Exam Hint: - At the end of an algebraic proof, you need to write a** conclusion **in full sentences - A good trick is to copy word-for-word the phrases used in the »
- Upstream: T-C32 join notes/2-equations-formulae-and-identities/algebraic-proof/algebraic-proof.json::spcpt_dgG8VyxX4bgSvRz7 — tier R1_parse_repair_statement_join — score n/a — wording EXACT — validation tier AI_VALIDATED (operator-delegated chain)
- Rationale: SME span 'Algebraic Proof' on note 'Algebraic Proof' is anchored by the corpus spec_point block spcpt_dgG8VyxX4bgSvRz7 and joined to 4MA1-2.2E via operator-verdict statement join after T-SPEC-8 parse repair (PMT excluded as source); this section chunk sits inside that span.
- Verdict: [ ] CONFIRM — this chunk belongs to this SP   [ ] REJECT — wrong chunk/SP   [ ] HOLD — needs rework

### 4MA1-3.3B — apply to the graph ofy = f(x)the transformations y = f(x) + a, y = f(ax), y = f(x + a), y = af(x) for linear, quadratic, sine and cosine functions
- Note: Translations of Graphs (`notes/3-sequences-functions-and-graphs/transformations-of-graphs/translations-of-graphs.json`)
- Chunk: ordinal 0 — heading `Translations of graphs` — sha256_16 `f67c484c04e9c168` — 22 chars
- Evidence quote (verbatim self-slice, markdown-safe): "Translations of graphs"
- Chunk excerpt: «Translations of graphs»
- Upstream: T-C32 join notes/3-sequences-functions-and-graphs/transformations-of-graphs/translations-of-graphs.json::spcpt_wt53CcTmwpZ3sjm3 — tier P2_operator_content_join — score n/a — wording EXACT — validation tier AI_VALIDATED (operator-delegated chain)
- Rationale: SME span 'Translations of Graphs' on note 'Translations of Graphs' is anchored by the corpus spec_point block spcpt_wt53CcTmwpZ3sjm3 and joined to 4MA1-3.3B via T-SPEC-9 operator verdict (no upstream; PMT excluded as source); this section chunk sits inside that span.
- Verdict: [ ] CONFIRM — this chunk belongs to this SP   [ ] REJECT — wrong chunk/SP   [ ] HOLD — needs rework

### 4MA1-2.2C — manipulate algebraic fractions where the numerator and/or the denominator can be numeric, linear or quadratic
- Note: Multiplying & Dividing Algebraic Fractions (`notes/2-equations-formulae-and-identities/algebraic-fractions/multiplying-and-dividing-algebraic-fractions.json`)
- Chunk: ordinal 2 — heading `How do I divide algebraic fractions?` — sha256_16 `1d5abfd5927281ce` — 1855 chars
- Evidence quote (verbatim self-slice, markdown-safe): "How do I divide algebraic fractions?
- **Flip** (find the reciprocal of) the **second **fraction and replace ÷ with ×

  - So $\div\frac{a}{b}$ becomes $\times\frac{b}{a}$
  - E.g. $\frac{3x-12}{x}\div\frac{2x+8}{x+3}=\frac{3x-12}{x}\times\"
- Chunk excerpt: «How do I divide algebraic fractions? - **Flip** (find the reciprocal of) the **second **fraction and replace ÷ with × - So $\div\frac{a}{b}$ becomes $\times\frac{b}{a}$ - E.g. $\frac{3x-12}{x}\div\frac{2x+8}{x+3}=\frac{3x-12}{x}\times\frac{x+3}{2x+8}$ - Then follow the same rules for **multiplying** two fractions Worked Example: Divide $\frac{x+3}{x-4}$ by $\frac{2x+6}{x^{2}-16}$, giving your answer as a simplified f»
- Upstream: T-C32 join notes/2-equations-formulae-and-identities/algebraic-fractions/multiplying-and-dividing-algebraic-fractions.json::spcpt_j2YgCQ3HvtrTXdG4 — tier R1_parse_repair_statement_join — score n/a — wording EXACT — validation tier AI_VALIDATED (operator-delegated chain)
- Rationale: SME span 'Multiplying & Dividing Algebraic Fractions' on note 'Multiplying & Dividing Algebraic Fractions' is anchored by the corpus spec_point block spcpt_j2YgCQ3HvtrTXdG4 and joined to 4MA1-2.2C via operator-verdict statement join after T-SPEC-8 parse repair (PMT excluded as source); this section chunk sits inside that span.
- Verdict: [ ] CONFIRM — this chunk belongs to this SP   [ ] REJECT — wrong chunk/SP   [ ] HOLD — needs rework

### 4MA1-1.6G — use compound interest and depreciation
- Note: Compound Interest (`notes/1-numbers-and-the-number-system/compound-interest-and-depreciation/compound-interest.json`)
- Chunk: ordinal 1 — heading `What is compound interest?` — sha256_16 `12db3b5b18bae002` — 527 chars
- Evidence quote (verbatim self-slice, markdown-safe): "What is compound interest?
- **Compound interest** is where interest is calculated on the **running total**, not just the starting amount
- E.g. **\$100** earns **10% interest** each year, for 3 years

  - At the end of year 1, **10% of \$1"
- Chunk excerpt: «What is compound interest? - **Compound interest** is where interest is calculated on the **running total**, not just the starting amount - E.g. **\$100** earns **10% interest** each year, for 3 years - At the end of year 1, **10% of \$100 is earned** - The total balance will now be 100+10 = **\$110** - At the end of year 2, **10% of \$110 is earned** - The balance will now be 110+11 = **\$121** - At the end of year »
- Upstream: T-C32 join notes/1-numbers-and-the-number-system/compound-interest-and-depreciation/compound-interest.json::spcpt_vyd4VnJDqBJWvTNc — tier P1_name_fragment_join — score n/a — wording EXACT — validation tier AI_VALIDATED (operator-delegated chain)
- Rationale: SME span 'Compound Interest' on note 'Compound Interest' is anchored by the corpus spec_point block spcpt_vyd4VnJDqBJWvTNc and joined to 4MA1-1.6G via operator-verdict name-fragment join (T-SPEC-7; PMT excluded as source); this section chunk sits inside that span.
- Verdict: [ ] CONFIRM — this chunk belongs to this SP   [ ] REJECT — wrong chunk/SP   [ ] HOLD — needs rework

### 4MA1-6.1C — use cumulative frequency diagrams
- Note: Probability Tree Diagrams (`notes/6-statistics-and-probability/probability-diagrams---venn-and-tree-diagrams/tree-diagrams.json`)
- Chunk: ordinal 0 — heading `Tree diagrams` — sha256_16 `10616856bc49cbf6` — 13 chars
- Evidence quote (verbatim self-slice, markdown-safe): "Tree diagrams"
- Chunk excerpt: «Tree diagrams»
- Upstream: T-C32 join notes/6-statistics-and-probability/probability-diagrams---venn-and-tree-diagrams/tree-diagrams.json::spcpt_hTsm2dz7xmwM4jwW — tier P1_name_fragment_join — score n/a — wording EXACT — validation tier AI_VALIDATED (operator-delegated chain)
- Rationale: SME span 'Tree Diagrams' on note 'Probability Tree Diagrams' is anchored by the corpus spec_point block spcpt_hTsm2dz7xmwM4jwW and joined to 4MA1-6.1C via operator-verdict name-fragment join (T-SPEC-7; PMT excluded as source); this section chunk sits inside that span.
- Verdict: [ ] CONFIRM — this chunk belongs to this SP   [ ] REJECT — wrong chunk/SP   [ ] HOLD — needs rework

### 4MA1-2.2C — manipulate algebraic fractions where the numerator and/or the denominator can be numeric, linear or quadratic
- Note: Solving Equations with Algebraic Fractions (`notes/2-equations-formulae-and-identities/algebraic-fractions/solving-algebraic-fractions.json`)
- Chunk: ordinal 0 — heading `Solving algebraic fractions` — sha256_16 `2fb431d1c6f4497d` — 27 chars
- Evidence quote (verbatim self-slice, markdown-safe): "Solving algebraic fractions"
- Chunk excerpt: «Solving algebraic fractions»
- Upstream: T-C32 join notes/2-equations-formulae-and-identities/algebraic-fractions/solving-algebraic-fractions.json::spcpt_xwx7PVk7fQ5QpdMk — tier R1_parse_repair_statement_join — score n/a — wording EXACT — validation tier AI_VALIDATED (operator-delegated chain)
- Rationale: SME span 'Solving Algebraic Fractions' on note 'Solving Equations with Algebraic Fractions' is anchored by the corpus spec_point block spcpt_xwx7PVk7fQ5QpdMk and joined to 4MA1-2.2C via operator-verdict statement join after T-SPEC-8 parse repair (PMT excluded as source); this section chunk sits inside that span.
- Verdict: [ ] CONFIRM — this chunk belongs to this SP   [ ] REJECT — wrong chunk/SP   [ ] HOLD — needs rework

### 4MA1-6.3A — draw and use tree diagrams
- Note: Combined Conditional Probabilities (`notes/6-statistics-and-probability/combined-and-conditional-probability/combined-conditional-probabilities.json`)
- Chunk: ordinal 1 — heading `What is a combined conditional probability?` — sha256_16 `be36e013aa0fd0cf` — 199 chars
- Evidence quote (verbatim self-slice, markdown-safe): "What is a combined conditional probability?
- This is when you have two (or more) **successive events**, one after the other, and the **second** event **depends on** (is conditional on) the **first**"
- Chunk excerpt: «What is a combined conditional probability? - This is when you have two (or more) **successive events**, one after the other, and the **second** event **depends on** (is conditional on) the **first**»
- Upstream: T-C32 join notes/6-statistics-and-probability/combined-and-conditional-probability/combined-conditional-probabilities.json::spcpt_9cJGVGKRhP9JYgjF — tier R1_parse_repair_statement_join — score n/a — wording EXACT — validation tier AI_VALIDATED (operator-delegated chain)
- Rationale: SME span 'Combined Conditional Probabilities' on note 'Combined Conditional Probabilities' is anchored by the corpus spec_point block spcpt_9cJGVGKRhP9JYgjF and joined to 4MA1-6.3A via operator-verdict statement join after T-SPEC-8 parse repair (PMT excluded as source); this section chunk sits inside that span.
- Verdict: [ ] CONFIRM — this chunk belongs to this SP   [ ] REJECT — wrong chunk/SP   [ ] HOLD — needs rework

### 4MA1-3.1C — find the sum of the firstnterms of an arithmetic series(Sn)
- Note: Sum of an Arithmetic Series (`notes/3-sequences-functions-and-graphs/sequences/sum-of-an-arithmetic-series.json`)
- Chunk: ordinal 0 — heading `Sum of an arithmetic series` — sha256_16 `00b1cd097c7c3b95` — 27 chars
- Evidence quote (verbatim self-slice, markdown-safe): "Sum of an arithmetic series"
- Chunk excerpt: «Sum of an arithmetic series»
- Upstream: T-C32 join notes/3-sequences-functions-and-graphs/sequences/sum-of-an-arithmetic-series.json::spcpt_wCB5h8vpTr4WVkNd — tier R1_parse_repair_statement_join — score n/a — wording EXACT — validation tier AI_VALIDATED (operator-delegated chain)
- Rationale: SME span 'Sum of an Arithmetic Series' on note 'Sum of an Arithmetic Series' is anchored by the corpus spec_point block spcpt_wCB5h8vpTr4WVkNd and joined to 4MA1-3.1C via operator-verdict statement join after T-SPEC-8 parse repair (PMT excluded as source); this section chunk sits inside that span.
- Verdict: [ ] CONFIRM — this chunk belongs to this SP   [ ] REJECT — wrong chunk/SP   [ ] HOLD — needs rework

### 4MA1-6.1A — construct and interpret histograms
- Note: Drawing Histograms (`notes/6-statistics-and-probability/histograms/drawing-histograms.json`)
- Chunk: ordinal 1 — heading `What is a histogram?` — sha256_16 `c09f7df8f90a5f63` — 735 chars
- Evidence quote (verbatim self-slice, markdown-safe): "What is a histogram?
- A **histogram** looks similar to a bar chart, but there are important **differences**
- **Bar charts** are used for **discrete** (and sometimes **non-numerical**) data

  - In a bar chart, the **height** (or **length*"
- Chunk excerpt: «What is a histogram? - A **histogram** looks similar to a bar chart, but there are important **differences** - **Bar charts** are used for **discrete** (and sometimes **non-numerical**) data - In a bar chart, the **height** (or **length**) of a bar determines the frequency - There are usually **gaps** between the bars - **Histograms** are used with **continuous data,** grouped into **class intervals **(usually of **u»
- Upstream: T-C32 join notes/6-statistics-and-probability/histograms/drawing-histograms.json::spcpt_nJCDx3cDGTVz3MBk — tier R1_parse_repair_statement_join — score n/a — wording EXACT — validation tier AI_VALIDATED (operator-delegated chain)
- Rationale: SME span 'Drawing Histograms' on note 'Drawing Histograms' is anchored by the corpus spec_point block spcpt_nJCDx3cDGTVz3MBk and joined to 4MA1-6.1A via operator-verdict statement join after T-SPEC-8 parse repair (PMT excluded as source); this section chunk sits inside that span.
- Verdict: [ ] CONFIRM — this chunk belongs to this SP   [ ] REJECT — wrong chunk/SP   [ ] HOLD — needs rework

### 4MA1-4.8C — understand and use the sine and cosine rules for any triangle
- Note: The Cosine Rule (`notes/4-geometry-and-trigonometry/sine-cosine-rule-and-area-of-triangles/the-cosine-rule.json`)
- Chunk: ordinal 3 — heading `How do I use the cosine rule to find a missing angle?` — sha256_16 `371f73acd92c1a3d` — 2740 chars
- Evidence quote (verbatim self-slice, markdown-safe): "How do I use the cosine rule to find a missing angle?
- Use the **cosine rule** for angles

  - when you have **all three sides**
  - and you want to find an angle
- It helps to** rearrange** the formula as follows, by adding $2bc\mathrm{co"
- Chunk excerpt: «How do I use the cosine rule to find a missing angle? - Use the **cosine rule** for angles - when you have **all three sides** - and you want to find an angle - It helps to** rearrange** the formula as follows, by adding $2bc\mathrm{cos}A$ to both sides then making $\mathrm{cos}A$ the subject `table row cell a squared end cell equals cell b squared plus c squared minus 2 b c space cos space A end cell row cell a squa»
- Upstream: T-C32 join notes/4-geometry-and-trigonometry/sine-cosine-rule-and-area-of-triangles/the-cosine-rule.json::spcpt_HnxHKwwfTxKcvCN7 — tier R1_parse_repair_statement_join — score n/a — wording EXACT — validation tier AI_VALIDATED (operator-delegated chain)
- Rationale: SME span 'Cosine Rule' on note 'The Cosine Rule' is anchored by the corpus spec_point block spcpt_HnxHKwwfTxKcvCN7 and joined to 4MA1-4.8C via operator-verdict statement join after T-SPEC-8 parse repair (PMT excluded as source); this section chunk sits inside that span.
- Verdict: [ ] CONFIRM — this chunk belongs to this SP   [ ] REJECT — wrong chunk/SP   [ ] HOLD — needs rework

### 4MA1-2.2C — manipulate algebraic fractions where the numerator and/or the denominator can be numeric, linear or quadratic
- Note: Multiplying & Dividing Algebraic Fractions (`notes/2-equations-formulae-and-identities/algebraic-fractions/multiplying-and-dividing-algebraic-fractions.json`)
- Chunk: ordinal 0 — heading `Multiplying & dividing algebraic fractions` — sha256_16 `6a7b58aaf095aa3c` — 42 chars
- Evidence quote (verbatim self-slice, markdown-safe): "Multiplying & dividing algebraic fractions"
- Chunk excerpt: «Multiplying & dividing algebraic fractions»
- Upstream: T-C32 join notes/2-equations-formulae-and-identities/algebraic-fractions/multiplying-and-dividing-algebraic-fractions.json::spcpt_j2YgCQ3HvtrTXdG4 — tier R1_parse_repair_statement_join — score n/a — wording EXACT — validation tier AI_VALIDATED (operator-delegated chain)
- Rationale: SME span 'Multiplying & Dividing Algebraic Fractions' on note 'Multiplying & Dividing Algebraic Fractions' is anchored by the corpus spec_point block spcpt_j2YgCQ3HvtrTXdG4 and joined to 4MA1-2.2C via operator-verdict statement join after T-SPEC-8 parse repair (PMT excluded as source); this section chunk sits inside that span.
- Verdict: [ ] CONFIRM — this chunk belongs to this SP   [ ] REJECT — wrong chunk/SP   [ ] HOLD — needs rework

### 4MA1-2.2B — understand the concept of a quadratic expression and be able to factorise such expressions
- Note: Factorising Harder Quadratics (`notes/2-equations-formulae-and-identities/factorising/factorising-harder-quadratics.json`)
- Chunk: ordinal 1 — heading `How do I factorise a quadratic expression where  a ≠ 1  in ax<sup>2</sup> + bx + c?` — sha256_16 `94545df07401fcb2` — 83 chars
- Evidence quote (verbatim self-slice, markdown-safe): "How do I factorise a quadratic expression where  a ≠ 1  in ax<sup>2</sup> + bx + c?"
- Chunk excerpt: «How do I factorise a quadratic expression where a ≠ 1 in ax<sup>2</sup> + bx + c?»
- Upstream: T-C32 join notes/2-equations-formulae-and-identities/factorising/factorising-harder-quadratics.json::spcpt_rt6wRVmbK5ZVkF3d — tier R1_parse_repair_statement_join — score n/a — wording EXACT — validation tier AI_VALIDATED (operator-delegated chain)
- Rationale: SME span 'Factorising Harder Quadratics' on note 'Factorising Harder Quadratics' is anchored by the corpus spec_point block spcpt_rt6wRVmbK5ZVkF3d and joined to 4MA1-2.2B via operator-verdict statement join after T-SPEC-8 parse repair (PMT excluded as source); this section chunk sits inside that span.
- Verdict: [ ] CONFIRM — this chunk belongs to this SP   [ ] REJECT — wrong chunk/SP   [ ] HOLD — needs rework

### 4MA1-4.8C — understand and use the sine and cosine rules for any triangle
- Note: The Sine Rule (`notes/4-geometry-and-trigonometry/sine-cosine-rule-and-area-of-triangles/the-sine-rule.json`)
- Chunk: ordinal 0 — heading `Sine rule` — sha256_16 `9445d5ec909b1009` — 9 chars
- Evidence quote (verbatim self-slice, markdown-safe): "Sine rule"
- Chunk excerpt: «Sine rule»
- Upstream: T-C32 join notes/4-geometry-and-trigonometry/sine-cosine-rule-and-area-of-triangles/the-sine-rule.json::spcpt_QJNVgG7qqP279jnN — tier R1_parse_repair_statement_join — score n/a — wording EXACT — validation tier AI_VALIDATED (operator-delegated chain)
- Rationale: SME span 'Sine Rule' on note 'The Sine Rule' is anchored by the corpus spec_point block spcpt_QJNVgG7qqP279jnN and joined to 4MA1-4.8C via operator-verdict statement join after T-SPEC-8 parse repair (PMT excluded as source); this section chunk sits inside that span.
- Verdict: [ ] CONFIRM — this chunk belongs to this SP   [ ] REJECT — wrong chunk/SP   [ ] HOLD — needs rework

### 4MA1-3.1C — find the sum of the firstnterms of an arithmetic series(Sn)
- Note: Sum of an Arithmetic Series (`notes/3-sequences-functions-and-graphs/sequences/sum-of-an-arithmetic-series.json`)
- Chunk: ordinal 2 — heading `What is the formula for the sum of an arithmetic sequence?` — sha256_16 `dbbe6471b46be98f` — 452 chars
- Evidence quote (verbatim self-slice, markdown-safe): "What is the formula for the sum of an arithmetic sequence?
- The** formula **for the** sum of the first **$n$** terms **in an arithmetic sequence is `S subscript n equals n over 2 open square brackets 2 a plus open parentheses n minus 1 clo"
- Chunk excerpt: «What is the formula for the sum of an arithmetic sequence? - The** formula **for the** sum of the first **$n$** terms **in an arithmetic sequence is `S subscript n equals n over 2 open square brackets 2 a plus open parentheses n minus 1 close parentheses d close square brackets` - $a$ is the **first term** - $d$ is the **common difference** - $n$ is the **number of terms** being added - $S_{n}$ is the** sum **of the »
- Upstream: T-C32 join notes/3-sequences-functions-and-graphs/sequences/sum-of-an-arithmetic-series.json::spcpt_wCB5h8vpTr4WVkNd — tier R1_parse_repair_statement_join — score n/a — wording EXACT — validation tier AI_VALIDATED (operator-delegated chain)
- Rationale: SME span 'Sum of an Arithmetic Series' on note 'Sum of an Arithmetic Series' is anchored by the corpus spec_point block spcpt_wCB5h8vpTr4WVkNd and joined to 4MA1-3.1C via operator-verdict statement join after T-SPEC-8 parse repair (PMT excluded as source); this section chunk sits inside that span.
- Verdict: [ ] CONFIRM — this chunk belongs to this SP   [ ] REJECT — wrong chunk/SP   [ ] HOLD — needs rework

### 4MA1-6.1A — construct and interpret histograms
- Note: Frequency Density (`notes/6-statistics-and-probability/histograms/frequency-density.json`)
- Chunk: ordinal 2 — heading `How do I calculate frequency density?` — sha256_16 `bf9935cc0ebb3991` — 1288 chars
- Evidence quote (verbatim self-slice, markdown-safe): "How do I calculate frequency density?
- In questions it is usual to be presented with grouped data in a **table**
- **Add two extra columns** to the table

  - one to work out and write down the **class width** of each interval
  - the seco"
- Chunk excerpt: «How do I calculate frequency density? - In questions it is usual to be presented with grouped data in a **table** - **Add two extra columns** to the table - one to work out and write down the **class width** of each interval - the second to then work out the **frequency density** for each group (row) Worked Example: The table below shows information regarding the average speeds travelled by trains in a region of the »
- Upstream: T-C32 join notes/6-statistics-and-probability/histograms/frequency-density.json::spcpt_Sq9YjYQDkzwdnKT3 — tier R1_parse_repair_statement_join — score n/a — wording EXACT — validation tier AI_VALIDATED (operator-delegated chain)
- Rationale: SME span 'Frequency Density' on note 'Frequency Density' is anchored by the corpus spec_point block spcpt_Sq9YjYQDkzwdnKT3 and joined to 4MA1-6.1A via operator-verdict statement join after T-SPEC-8 parse repair (PMT excluded as source); this section chunk sits inside that span.
- Verdict: [ ] CONFIRM — this chunk belongs to this SP   [ ] REJECT — wrong chunk/SP   [ ] HOLD — needs rework

### 4MA1-6.1B — construct cumulative frequency diagrams from tabulated data
- Note: Drawing Cumulative Frequency Diagrams (`notes/6-statistics-and-probability/cumulative-frequency-diagrams/drawing-cumulative-frequency-diagrams.json`)
- Chunk: ordinal 0 — heading `Drawing cumulative frequency diagrams` — sha256_16 `6d2893021bfe23c6` — 37 chars
- Evidence quote (verbatim self-slice, markdown-safe): "Drawing cumulative frequency diagrams"
- Chunk excerpt: «Drawing cumulative frequency diagrams»
- Upstream: T-C32 join notes/6-statistics-and-probability/cumulative-frequency-diagrams/drawing-cumulative-frequency-diagrams.json::spcpt_kwGrBDCwB6YtVVBQ — tier R1_parse_repair_statement_join — score n/a — wording EXACT — validation tier AI_VALIDATED (operator-delegated chain)
- Rationale: SME span 'Drawing Cumulative Frequency Diagrams' on note 'Drawing Cumulative Frequency Diagrams' is anchored by the corpus spec_point block spcpt_kwGrBDCwB6YtVVBQ and joined to 4MA1-6.1B via operator-verdict statement join after T-SPEC-8 parse repair (PMT excluded as source); this section chunk sits inside that span.
- Verdict: [ ] CONFIRM — this chunk belongs to this SP   [ ] REJECT — wrong chunk/SP   [ ] HOLD — needs rework

### 4MA1-2.2C — manipulate algebraic fractions where the numerator and/or the denominator can be numeric, linear or quadratic
- Note: Adding & Subtracting Algebraic Fractions (`notes/2-equations-formulae-and-identities/algebraic-fractions/adding-and-subtracting-algebraic-fractions.json`)
- Chunk: ordinal 1 — heading `How do I add (or subtract) two algebraic fractions?` — sha256_16 `1764a07bff6ff439` — 7837 chars
- Evidence quote (verbatim self-slice, markdown-safe): "How do I add (or subtract) two algebraic fractions?
- The **rules** for adding and subtracting **algebraic fractions** are the **same** as they are for **fractions with numbers**
- **STEP 1 **
Find the** lowest common denominator** (LCD)

 "
- Chunk excerpt: «How do I add (or subtract) two algebraic fractions? - The **rules** for adding and subtracting **algebraic fractions** are the **same** as they are for **fractions with numbers** - **STEP 1 ** Find the** lowest common denominator** (LCD) - Sometimes the LCD can be found by **multiplying** the denominators together - E.g. The LCD for the fractions $\frac{1}{x+2}$ and $\frac{1}{x+5}$ is `open parentheses x plus 2 close»
- Upstream: T-C32 join notes/2-equations-formulae-and-identities/algebraic-fractions/adding-and-subtracting-algebraic-fractions.json::spcpt_wF3J5MKvx273VH3h — tier R1_parse_repair_statement_join — score n/a — wording EXACT — validation tier AI_VALIDATED (operator-delegated chain)
- Rationale: SME span 'Adding & Subtracting Algebraic Fractions' on note 'Adding & Subtracting Algebraic Fractions' is anchored by the corpus spec_point block spcpt_wF3J5MKvx273VH3h and joined to 4MA1-2.2C via operator-verdict statement join after T-SPEC-8 parse repair (PMT excluded as source); this section chunk sits inside that span.
- Verdict: [ ] CONFIRM — this chunk belongs to this SP   [ ] REJECT — wrong chunk/SP   [ ] HOLD — needs rework

### 4MA1-4.9A — find perimeters and areas of sectors of circles
- Note: Arc Lengths & Sector Areas (`notes/4-geometry-and-trigonometry/circles-arcs-and-sectors/arcs-and-sectors.json`)
- Chunk: ordinal 4 — heading `How do I find the length of an arc?` — sha256_16 `ed0be43862576381` — 301 chars
- Evidence quote (verbatim self-slice, markdown-safe): "How do I find the length of an arc?
- **STEP 1**
**Divide** the **angle** by **360** to form a fraction

  - $\frac{θ}{360}$
- **STEP 2**
Calculate the **circumference** of the **full circle**

  - $2πr$
- **STEP 3**
**Multiply** the **frac"
- Chunk excerpt: «How do I find the length of an arc? - **STEP 1** **Divide** the **angle** by **360** to form a fraction - $\frac{θ}{360}$ - **STEP 2** Calculate the **circumference** of the **full circle** - $2πr$ - **STEP 3** **Multiply** the **fraction** by the **circumference** - $\frac{θ}{360}\times2πr$»
- Upstream: T-C32 join notes/4-geometry-and-trigonometry/circles-arcs-and-sectors/arcs-and-sectors.json::spcpt_dvX7WnB2FSdky4jW — tier R1_parse_repair_statement_join — score n/a — wording EXACT — validation tier AI_VALIDATED (operator-delegated chain)
- Rationale: SME span 'Arc Lengths & Sector Areas' on note 'Arc Lengths & Sector Areas' is anchored by the corpus spec_point block spcpt_dvX7WnB2FSdky4jW and joined to 4MA1-4.9A via operator-verdict statement join after T-SPEC-8 parse repair (PMT excluded as source); this section chunk sits inside that span.
- Verdict: [ ] CONFIRM — this chunk belongs to this SP   [ ] REJECT — wrong chunk/SP   [ ] HOLD — needs rework

### 4MA1-6.1C — use cumulative frequency diagrams
- Note: Probability Tree Diagrams (`notes/6-statistics-and-probability/probability-diagrams---venn-and-tree-diagrams/tree-diagrams.json`)
- Chunk: ordinal 3 — heading `How do I use tree diagrams with conditional probability?` — sha256_16 `ad9a3cb0bf5709ce` — 6529 chars
- Evidence quote (verbatim self-slice, markdown-safe): "How do I use tree diagrams with conditional probability?
- Probabilities that depend on a particular thing having happened first in a tree diagram are called **conditional probabilities**
- For example, the probability that a team wins a ga"
- Chunk excerpt: «How do I use tree diagrams with conditional probability? - Probabilities that depend on a particular thing having happened first in a tree diagram are called **conditional probabilities** - For example, the probability that a team wins a game may** depend** on whether they won or lost the previous game - The **probabilities** for 'win' on the first set of branches may be **different** to those for 'win' on the second»
- Upstream: T-C32 join notes/6-statistics-and-probability/probability-diagrams---venn-and-tree-diagrams/tree-diagrams.json::spcpt_hTsm2dz7xmwM4jwW — tier P1_name_fragment_join — score n/a — wording EXACT — validation tier AI_VALIDATED (operator-delegated chain)
- Rationale: SME span 'Tree Diagrams' on note 'Probability Tree Diagrams' is anchored by the corpus spec_point block spcpt_hTsm2dz7xmwM4jwW and joined to 4MA1-6.1C via operator-verdict name-fragment join (T-SPEC-7; PMT excluded as source); this section chunk sits inside that span.
- Verdict: [ ] CONFIRM — this chunk belongs to this SP   [ ] REJECT — wrong chunk/SP   [ ] HOLD — needs rework

### 4MA1-3.3B — apply to the graph ofy = f(x)the transformations y = f(x) + a, y = f(ax), y = f(x + a), y = af(x) for linear, quadratic, sine and cosine functions
- Note: Translations of Graphs (`notes/3-sequences-functions-and-graphs/transformations-of-graphs/translations-of-graphs.json`)
- Chunk: ordinal 4 — heading `Horizontal translations: y=f(x + a)` — sha256_16 `20ae562fc0f9cb89` — 457 chars
- Evidence quote (verbatim self-slice, markdown-safe): "Horizontal translations: y=f(x + a)
- $y=f(x+a)$ is a **horizontal translation **by the vector `open parentheses table row cell negative a end cell row 0 end table close parentheses`

  - The graph moves** left for positive** values of $a$
"
- Chunk excerpt: «Horizontal translations: y=f(x + a) - $y=f(x+a)$ is a **horizontal translation **by the vector `open parentheses table row cell negative a end cell row 0 end table close parentheses` - The graph moves** left for positive** values of $a$ - This is often the opposite direction to which people expect - The graph moves* ***right for negative** values of $a$ - The** *****y*****-coordinates **stay the **same** Example of a»
- Upstream: T-C32 join notes/3-sequences-functions-and-graphs/transformations-of-graphs/translations-of-graphs.json::spcpt_wt53CcTmwpZ3sjm3 — tier P2_operator_content_join — score n/a — wording EXACT — validation tier AI_VALIDATED (operator-delegated chain)
- Rationale: SME span 'Translations of Graphs' on note 'Translations of Graphs' is anchored by the corpus spec_point block spcpt_wt53CcTmwpZ3sjm3 and joined to 4MA1-3.3B via T-SPEC-9 operator verdict (no upstream; PMT excluded as source); this section chunk sits inside that span.
- Verdict: [ ] CONFIRM — this chunk belongs to this SP   [ ] REJECT — wrong chunk/SP   [ ] HOLD — needs rework

### 4MA1-3.3B — apply to the graph ofy = f(x)the transformations y = f(x) + a, y = f(ax), y = f(x + a), y = af(x) for linear, quadratic, sine and cosine functions
- Note: Stretches of Graphs (`notes/3-sequences-functions-and-graphs/transformations-of-graphs/stretches-of-graphs.json`)
- Chunk: ordinal 5 — heading `What happens to asymptotes when a graph is stretched?` — sha256_16 `1fa85874271e7734` — 309 chars
- Evidence quote (verbatim self-slice, markdown-safe): "What happens to asymptotes when a graph is stretched?
- Any ***asymptotes*** of `straight f open parentheses x close parentheses` are also stretched
A diagram shows transformations of the function y = f(x). It illustrates vertical and horiz"
- Chunk excerpt: «What happens to asymptotes when a graph is stretched? - Any ***asymptotes*** of `straight f open parentheses x close parentheses` are also stretched A diagram shows transformations of the function y = f(x). It illustrates vertical and horizontal stretches, their effects on asymptotes, and coordinate changes.»
- Upstream: T-C32 join notes/3-sequences-functions-and-graphs/transformations-of-graphs/stretches-of-graphs.json::spcpt_YcMPxJgtrjtBzMkV — tier P2_operator_content_join — score n/a — wording EXACT — validation tier AI_VALIDATED (operator-delegated chain)
- Rationale: SME span 'Stretches of Graphs' on note 'Stretches of Graphs' is anchored by the corpus spec_point block spcpt_YcMPxJgtrjtBzMkV and joined to 4MA1-3.3B via T-SPEC-9 operator verdict (no upstream; PMT excluded as source); this section chunk sits inside that span.
- Verdict: [ ] CONFIRM — this chunk belongs to this SP   [ ] REJECT — wrong chunk/SP   [ ] HOLD — needs rework

### 4MA1-6.3A — draw and use tree diagrams
- Note: Combined Conditional Probabilities (`notes/6-statistics-and-probability/combined-and-conditional-probability/combined-conditional-probabilities.json`)
- Chunk: ordinal 4 — heading `What if there are multiple possibilities within one question?` — sha256_16 `f725fb798877303a` — 5359 chars
- Evidence quote (verbatim self-slice, markdown-safe): "What if there are multiple possibilities within one question?
- You may need a **listing strategy** (e.g.* AAB*, *ABA*, *BAA*)
- You will need the **or** rule for multiple possibilities

  - P(*AB* **or** *BA* **or*** AA ***or***...*) = P(*"
- Chunk excerpt: «What if there are multiple possibilities within one question? - You may need a **listing strategy** (e.g.* AAB*, *ABA*, *BAA*) - You will need the **or** rule for multiple possibilities - P(*AB* **or** *BA* **or*** AA ***or***...*) = P(*AB*) + P(*BA*) + P(*AA*) +... - **Add** the cases together - Remember that *AB* and *BA* are **not the same** - *AB* means *A* happened first, then *B* - *BA* means *B* happened first»
- Upstream: T-C32 join notes/6-statistics-and-probability/combined-and-conditional-probability/combined-conditional-probabilities.json::spcpt_9cJGVGKRhP9JYgjF — tier R1_parse_repair_statement_join — score n/a — wording EXACT — validation tier AI_VALIDATED (operator-delegated chain)
- Rationale: SME span 'Combined Conditional Probabilities' on note 'Combined Conditional Probabilities' is anchored by the corpus spec_point block spcpt_9cJGVGKRhP9JYgjF and joined to 4MA1-6.3A via operator-verdict statement join after T-SPEC-8 parse repair (PMT excluded as source); this section chunk sits inside that span.
- Verdict: [ ] CONFIRM — this chunk belongs to this SP   [ ] REJECT — wrong chunk/SP   [ ] HOLD — needs rework

### 4MA1-2.2B — understand the concept of a quadratic expression and be able to factorise such expressions
- Note: Factorising Harder Quadratics (`notes/2-equations-formulae-and-identities/factorising/factorising-harder-quadratics.json`)
- Chunk: ordinal 0 — heading `Factorising harder quadratics` — sha256_16 `519b8c9a0b515246` — 29 chars
- Evidence quote (verbatim self-slice, markdown-safe): "Factorising harder quadratics"
- Chunk excerpt: «Factorising harder quadratics»
- Upstream: T-C32 join notes/2-equations-formulae-and-identities/factorising/factorising-harder-quadratics.json::spcpt_rt6wRVmbK5ZVkF3d — tier R1_parse_repair_statement_join — score n/a — wording EXACT — validation tier AI_VALIDATED (operator-delegated chain)
- Rationale: SME span 'Factorising Harder Quadratics' on note 'Factorising Harder Quadratics' is anchored by the corpus spec_point block spcpt_rt6wRVmbK5ZVkF3d and joined to 4MA1-2.2B via operator-verdict statement join after T-SPEC-8 parse repair (PMT excluded as source); this section chunk sits inside that span.
- Verdict: [ ] CONFIRM — this chunk belongs to this SP   [ ] REJECT — wrong chunk/SP   [ ] HOLD — needs rework

### 4MA1-3.3B — apply to the graph ofy = f(x)the transformations y = f(x) + a, y = f(ax), y = f(x + a), y = af(x) for linear, quadratic, sine and cosine functions
- Note: Translations of Graphs (`notes/3-sequences-functions-and-graphs/transformations-of-graphs/translations-of-graphs.json`)
- Chunk: ordinal 2 — heading `How do I translate graphs?` — sha256_16 `1064a82dc1c0a02e` — 137 chars
- Evidence quote (verbatim self-slice, markdown-safe): "How do I translate graphs?
- Let `y equals straight f open parentheses x close parentheses` be the **equation** of the **original graph**"
- Chunk excerpt: «How do I translate graphs? - Let `y equals straight f open parentheses x close parentheses` be the **equation** of the **original graph**»
- Upstream: T-C32 join notes/3-sequences-functions-and-graphs/transformations-of-graphs/translations-of-graphs.json::spcpt_wt53CcTmwpZ3sjm3 — tier P2_operator_content_join — score n/a — wording EXACT — validation tier AI_VALIDATED (operator-delegated chain)
- Rationale: SME span 'Translations of Graphs' on note 'Translations of Graphs' is anchored by the corpus spec_point block spcpt_wt53CcTmwpZ3sjm3 and joined to 4MA1-3.3B via T-SPEC-9 operator verdict (no upstream; PMT excluded as source); this section chunk sits inside that span.
- Verdict: [ ] CONFIRM — this chunk belongs to this SP   [ ] REJECT — wrong chunk/SP   [ ] HOLD — needs rework

### 4MA1-2.2C — manipulate algebraic fractions where the numerator and/or the denominator can be numeric, linear or quadratic
- Note: Adding & Subtracting Algebraic Fractions (`notes/2-equations-formulae-and-identities/algebraic-fractions/adding-and-subtracting-algebraic-fractions.json`)
- Chunk: ordinal 0 — heading `Adding & subtracting algebraic fractions` — sha256_16 `f1102bb87cd52c09` — 40 chars
- Evidence quote (verbatim self-slice, markdown-safe): "Adding & subtracting algebraic fractions"
- Chunk excerpt: «Adding & subtracting algebraic fractions»
- Upstream: T-C32 join notes/2-equations-formulae-and-identities/algebraic-fractions/adding-and-subtracting-algebraic-fractions.json::spcpt_wF3J5MKvx273VH3h — tier R1_parse_repair_statement_join — score n/a — wording EXACT — validation tier AI_VALIDATED (operator-delegated chain)
- Rationale: SME span 'Adding & Subtracting Algebraic Fractions' on note 'Adding & Subtracting Algebraic Fractions' is anchored by the corpus spec_point block spcpt_wF3J5MKvx273VH3h and joined to 4MA1-2.2C via operator-verdict statement join after T-SPEC-8 parse repair (PMT excluded as source); this section chunk sits inside that span.
- Verdict: [ ] CONFIRM — this chunk belongs to this SP   [ ] REJECT — wrong chunk/SP   [ ] HOLD — needs rework

### 4MA1-3.3B — apply to the graph ofy = f(x)the transformations y = f(x) + a, y = f(ax), y = f(x + a), y = af(x) for linear, quadratic, sine and cosine functions
- Note: Reflections of Graphs (`notes/3-sequences-functions-and-graphs/transformations-of-graphs/reflections-of-graphs.json`)
- Chunk: ordinal 3 — heading `Vertical reflections: y=-f(x)` — sha256_16 `57c506cdd840739a` — 253 chars
- Evidence quote (verbatim self-slice, markdown-safe): "Vertical reflections: y=-f(x)
- `y equals negative straight f open parentheses x close parentheses` is a reflection in the** **$x$**-axis**

  - The $y$ coordinates change sign
  
    - The $x$ coordinates are unaffected
Example of a vertic"
- Chunk excerpt: «Vertical reflections: y=-f(x) - `y equals negative straight f open parentheses x close parentheses` is a reflection in the** **$x$**-axis** - The $y$ coordinates change sign - The $x$ coordinates are unaffected Example of a vertical reflection»
- Upstream: T-C32 join notes/3-sequences-functions-and-graphs/transformations-of-graphs/reflections-of-graphs.json::spcpt_qNDqnmZtzYttZDnz — tier P2_operator_content_join — score n/a — wording EXACT — validation tier AI_VALIDATED (operator-delegated chain)
- Rationale: SME span 'Reflections of Graphs' on note 'Reflections of Graphs' is anchored by the corpus spec_point block spcpt_qNDqnmZtzYttZDnz and joined to 4MA1-3.3B via T-SPEC-9 operator verdict (no upstream; PMT excluded as source); this section chunk sits inside that span.
- Verdict: [ ] CONFIRM — this chunk belongs to this SP   [ ] REJECT — wrong chunk/SP   [ ] HOLD — needs rework

### 4MA1-1.4A — understand the meaning of surds
- Note: Simplifying Surds (`notes/1-numbers-and-the-number-system/surds/simplifying-surds.json`)
- Chunk: ordinal 2 — heading `How do I do calculations with surds?` — sha256_16 `6b0fe66e4268f601` — 1106 chars
- Evidence quote (verbatim self-slice, markdown-safe): "How do I do calculations with surds?
- ** Multiplying surds**

  - You can multiply numbers under square roots together
  - $\sqrt{3}\times\sqrt{5}=\sqrt{3\times5}=\sqrt{15}$
- **Dividing surds**

  - You can divide numbers under square roo"
- Chunk excerpt: «How do I do calculations with surds? - ** Multiplying surds** - You can multiply numbers under square roots together - $\sqrt{3}\times\sqrt{5}=\sqrt{3\times5}=\sqrt{15}$ - **Dividing surds** - You can divide numbers under square roots - $\frac{\sqrt{21}}{\sqrt{7}}=\sqrt{21}\div\sqrt{7}=\sqrt{21\div7}=\sqrt{3}$ - **Factorising surds** - You can factorise numbers under square roots - $\sqrt{35}=\sqrt{5\times7}=\sqrt{5}»
- Upstream: T-C32 join notes/1-numbers-and-the-number-system/surds/simplifying-surds.json::spcpt_4QRwffMSmK66nXtp — tier R1_parse_repair_statement_join — score n/a — wording EXACT — validation tier AI_VALIDATED (operator-delegated chain)
- Rationale: SME span 'Surds & Exact Values' on note 'Simplifying Surds' is anchored by the corpus spec_point block spcpt_4QRwffMSmK66nXtp and joined to 4MA1-1.4A via operator-verdict statement join after T-SPEC-8 parse repair (PMT excluded as source); this section chunk sits inside that span.
- Verdict: [ ] CONFIRM — this chunk belongs to this SP   [ ] REJECT — wrong chunk/SP   [ ] HOLD — needs rework

### 4MA1-4.8C — understand and use the sine and cosine rules for any triangle
- Note: The Sine Rule (`notes/4-geometry-and-trigonometry/sine-cosine-rule-and-area-of-triangles/the-sine-rule.json`)
- Chunk: ordinal 2 — heading `How do I use the sine rule to find missing lengths?` — sha256_16 `5e075550c5fd13ff` — 637 chars
- Evidence quote (verbatim self-slice, markdown-safe): "How do I use the sine rule to find missing lengths?
- Use the **sine rule **

  - when you have **opposite pairs** of sides and angles in the question
  
    - *a* and *A*, or *b* and *B*, or *c* and *C*
- **Start by labelling your triangle"
- Chunk excerpt: «How do I use the sine rule to find missing lengths? - Use the **sine rule ** - when you have **opposite pairs** of sides and angles in the question - *a* and *A*, or *b* and *B*, or *c* and *C* - **Start by labelling your triangle** with the angles and sides - Angles have upper case letters - Sides **opposite** the angles have the equivalent lower case letter - To find a **missing length**, substitute numbers into th»
- Upstream: T-C32 join notes/4-geometry-and-trigonometry/sine-cosine-rule-and-area-of-triangles/the-sine-rule.json::spcpt_QJNVgG7qqP279jnN — tier R1_parse_repair_statement_join — score n/a — wording EXACT — validation tier AI_VALIDATED (operator-delegated chain)
- Rationale: SME span 'Sine Rule' on note 'The Sine Rule' is anchored by the corpus spec_point block spcpt_QJNVgG7qqP279jnN and joined to 4MA1-4.8C via operator-verdict statement join after T-SPEC-8 parse repair (PMT excluded as source); this section chunk sits inside that span.
- Verdict: [ ] CONFIRM — this chunk belongs to this SP   [ ] REJECT — wrong chunk/SP   [ ] HOLD — needs rework

### 4MA1-1.6G — use compound interest and depreciation
- Note: Compound Interest (`notes/1-numbers-and-the-number-system/compound-interest-and-depreciation/compound-interest.json`)
- Chunk: ordinal 3 — heading `Compound interest formula` — sha256_16 `1f6add8cb8df57eb` — 492 chars
- Evidence quote (verbatim self-slice, markdown-safe): "Compound interest formula
- An **alternative method** is to use the **following formula** to calculate the final balance

  - Final balance = `P open parentheses 1 plus r over 100 close parentheses to the power of n space end exponent` wher"
- Chunk excerpt: «Compound interest formula - An **alternative method** is to use the **following formula** to calculate the final balance - Final balance = `P open parentheses 1 plus r over 100 close parentheses to the power of n space end exponent` where - *P* is the original amount, - *r* is the % increase, - and *n* is the number of years - Note that $1+\frac{r}{100}$ is the same value as the multiplier - e.g. 1.15 for 15% interes»
- Upstream: T-C32 join notes/1-numbers-and-the-number-system/compound-interest-and-depreciation/compound-interest.json::spcpt_vyd4VnJDqBJWvTNc — tier P1_name_fragment_join — score n/a — wording EXACT — validation tier AI_VALIDATED (operator-delegated chain)
- Rationale: SME span 'Compound Interest' on note 'Compound Interest' is anchored by the corpus spec_point block spcpt_vyd4VnJDqBJWvTNc and joined to 4MA1-1.6G via operator-verdict name-fragment join (T-SPEC-7; PMT excluded as source); this section chunk sits inside that span.
- Verdict: [ ] CONFIRM — this chunk belongs to this SP   [ ] REJECT — wrong chunk/SP   [ ] HOLD — needs rework

### 4MA1-1.6G — use compound interest and depreciation
- Note: Compound Interest (`notes/1-numbers-and-the-number-system/compound-interest-and-depreciation/compound-interest.json`)
- Chunk: ordinal 0 — heading `Compound interest` — sha256_16 `bb96b3917d6eb2d1` — 17 chars
- Evidence quote (verbatim self-slice, markdown-safe): "Compound interest"
- Chunk excerpt: «Compound interest»
- Upstream: T-C32 join notes/1-numbers-and-the-number-system/compound-interest-and-depreciation/compound-interest.json::spcpt_vyd4VnJDqBJWvTNc — tier P1_name_fragment_join — score n/a — wording EXACT — validation tier AI_VALIDATED (operator-delegated chain)
- Rationale: SME span 'Compound Interest' on note 'Compound Interest' is anchored by the corpus spec_point block spcpt_vyd4VnJDqBJWvTNc and joined to 4MA1-1.6G via operator-verdict name-fragment join (T-SPEC-7; PMT excluded as source); this section chunk sits inside that span.
- Verdict: [ ] CONFIRM — this chunk belongs to this SP   [ ] REJECT — wrong chunk/SP   [ ] HOLD — needs rework

### 4MA1-6.1C — use cumulative frequency diagrams
- Note: Probability Tree Diagrams (`notes/6-statistics-and-probability/probability-diagrams---venn-and-tree-diagrams/tree-diagrams.json`)
- Chunk: ordinal 2 — heading `How do I find probabilities from tree diagrams?` — sha256_16 `87c8a007ba40cc33` — 566 chars
- Evidence quote (verbatim self-slice, markdown-safe): "How do I find probabilities from tree diagrams?
- Write the **probabilities** on each branch

  - Remember that P(**not **A) = 1 - P(A)
  
    - Probabilities on each **pair** of branches **add to 1**
- **Multiply** along the branches from*"
- Chunk excerpt: «How do I find probabilities from tree diagrams? - Write the **probabilities** on each branch - Remember that P(**not **A) = 1 - P(A) - Probabilities on each **pair** of branches **add to 1** - **Multiply** along the branches from** left to right** - This gives P(1st outcome **and** 2nd outcome) - **Add** between the **separate cases** - For example - P(AA **or **BB) = P(AA) + P(BB) - The probabilities of **all** poss»
- Upstream: T-C32 join notes/6-statistics-and-probability/probability-diagrams---venn-and-tree-diagrams/tree-diagrams.json::spcpt_hTsm2dz7xmwM4jwW — tier P1_name_fragment_join — score n/a — wording EXACT — validation tier AI_VALIDATED (operator-delegated chain)
- Rationale: SME span 'Tree Diagrams' on note 'Probability Tree Diagrams' is anchored by the corpus spec_point block spcpt_hTsm2dz7xmwM4jwW and joined to 4MA1-6.1C via operator-verdict name-fragment join (T-SPEC-7; PMT excluded as source); this section chunk sits inside that span.
- Verdict: [ ] CONFIRM — this chunk belongs to this SP   [ ] REJECT — wrong chunk/SP   [ ] HOLD — needs rework

### 4MA1-2.8A — solve quadratic inequalities in one unknown and represent the solution set on a number line
- Note: Solving Quadratic Inequalities (`notes/2-equations-formulae-and-identities/solving-inequalities/solving-quadratic-inequalities.json`)
- Chunk: ordinal 1 — heading `What are quadratic inequalities?` — sha256_16 `88d9ea9fea0a740b` — 452 chars
- Evidence quote (verbatim self-slice, markdown-safe): "What are quadratic inequalities?
- A **quadratic inequality **has the form $ax^{2}+bx+c\geq0$

  - There is an $x^{2}$ term and any **inequality sign**, $\geq,\leq,>,<$
  - They can usually be **factorised**
  
    - For example, `open pare"
- Chunk excerpt: «What are quadratic inequalities? - A **quadratic inequality **has the form $ax^{2}+bx+c\geq0$ - There is an $x^{2}$ term and any **inequality sign**, $\geq,\leq,>,<$ - They can usually be **factorised** - For example, `open parentheses x minus 2 close parentheses open parentheses x minus 5 close parentheses greater or equal than 0` - **Solutions** to quadratic inequalities are **ranges of **$x$** values** - For examp»
- Upstream: T-C32 join notes/2-equations-formulae-and-identities/solving-inequalities/solving-quadratic-inequalities.json::spcpt_dnkHMPkqhhdDxPkZ — tier R1_parse_repair_statement_join — score n/a — wording EXACT — validation tier AI_VALIDATED (operator-delegated chain)
- Rationale: SME span 'Solving Quadratic Inequalities' on note 'Solving Quadratic Inequalities' is anchored by the corpus spec_point block spcpt_dnkHMPkqhhdDxPkZ and joined to 4MA1-2.8A via operator-verdict statement join after T-SPEC-8 parse repair (PMT excluded as source); this section chunk sits inside that span.
- Verdict: [ ] CONFIRM — this chunk belongs to this SP   [ ] REJECT — wrong chunk/SP   [ ] HOLD — needs rework

### 4MA1-3.1C — find the sum of the firstnterms of an arithmetic series(Sn)
- Note: Sum of an Arithmetic Series (`notes/3-sequences-functions-and-graphs/sequences/sum-of-an-arithmetic-series.json`)
- Chunk: ordinal 1 — heading `What is the sum of an arithmetic sequence?` — sha256_16 `6d777d2906cc1ac6` — 278 chars
- Evidence quote (verbatim self-slice, markdown-safe): "What is the sum of an arithmetic sequence?
- The **sum of an arithmetic sequence (a series) **means the terms in an arithmetic sequence are added together

  - For example, the sum of the first 5 terms in the sequence 2, 4, 6, 8, 10, 12, .."
- Chunk excerpt: «What is the sum of an arithmetic sequence? - The **sum of an arithmetic sequence (a series) **means the terms in an arithmetic sequence are added together - For example, the sum of the first 5 terms in the sequence 2, 4, 6, 8, 10, 12, ... is - 2 + 4 + 6 + 8 + 10 = 30»
- Upstream: T-C32 join notes/3-sequences-functions-and-graphs/sequences/sum-of-an-arithmetic-series.json::spcpt_wCB5h8vpTr4WVkNd — tier R1_parse_repair_statement_join — score n/a — wording EXACT — validation tier AI_VALIDATED (operator-delegated chain)
- Rationale: SME span 'Sum of an Arithmetic Series' on note 'Sum of an Arithmetic Series' is anchored by the corpus spec_point block spcpt_wCB5h8vpTr4WVkNd and joined to 4MA1-3.1C via operator-verdict statement join after T-SPEC-8 parse repair (PMT excluded as source); this section chunk sits inside that span.
- Verdict: [ ] CONFIRM — this chunk belongs to this SP   [ ] REJECT — wrong chunk/SP   [ ] HOLD — needs rework

### 4MA1-3.1C — find the sum of the firstnterms of an arithmetic series(Sn)
- Note: Sum of an Arithmetic Series (`notes/3-sequences-functions-and-graphs/sequences/sum-of-an-arithmetic-series.json`)
- Chunk: ordinal 3 — heading `How do I use the formula for the sum of an arithmetic sequence?` — sha256_16 `8e0c1b9c8adf4d22` — 3904 chars
- Evidence quote (verbatim self-slice, markdown-safe): "How do I use the formula for the sum of an arithmetic sequence?
- You may have to **substitute** values into the formula to find $S_{n}$

  - For example, if $a=2$ and $d=5$ then the sum of the first ten terms is $S_{10}$
  
    - Substitut"
- Chunk excerpt: «How do I use the formula for the sum of an arithmetic sequence? - You may have to **substitute** values into the formula to find $S_{n}$ - For example, if $a=2$ and $d=5$ then the sum of the first ten terms is $S_{10}$ - Substitute $a=2$, $d=5$ and $n=10$ into the formula - You may have to **form equations** in terms of $a$ and $d$ when given information about the sum of the first $n$ terms - This may lead to **simul»
- Upstream: T-C32 join notes/3-sequences-functions-and-graphs/sequences/sum-of-an-arithmetic-series.json::spcpt_wCB5h8vpTr4WVkNd — tier R1_parse_repair_statement_join — score n/a — wording EXACT — validation tier AI_VALIDATED (operator-delegated chain)
- Rationale: SME span 'Sum of an Arithmetic Series' on note 'Sum of an Arithmetic Series' is anchored by the corpus spec_point block spcpt_wCB5h8vpTr4WVkNd and joined to 4MA1-3.1C via operator-verdict statement join after T-SPEC-8 parse repair (PMT excluded as source); this section chunk sits inside that span.
- Verdict: [ ] CONFIRM — this chunk belongs to this SP   [ ] REJECT — wrong chunk/SP   [ ] HOLD — needs rework

### 4MA1-1.4B — manipulate surds, including rationalising a denominator
- Note: Rationalising Denominators (`notes/1-numbers-and-the-number-system/surds/rationalising-denominators.json`)
- Chunk: ordinal 0 — heading `Rationalising denominators` — sha256_16 `8be9d37338e903b2` — 26 chars
- Evidence quote (verbatim self-slice, markdown-safe): "Rationalising denominators"
- Chunk excerpt: «Rationalising denominators»
- Upstream: T-C32 join notes/1-numbers-and-the-number-system/surds/rationalising-denominators.json::spcpt_wMN58K4jZ54z8bXC — tier R1_parse_repair_statement_join — score n/a — wording EXACT — validation tier AI_VALIDATED (operator-delegated chain)
- Rationale: SME span 'Rationalising Denominators' on note 'Rationalising Denominators' is anchored by the corpus spec_point block spcpt_wMN58K4jZ54z8bXC and joined to 4MA1-1.4B via operator-verdict statement join after T-SPEC-8 parse repair (PMT excluded as source); this section chunk sits inside that span.
- Verdict: [ ] CONFIRM — this chunk belongs to this SP   [ ] REJECT — wrong chunk/SP   [ ] HOLD — needs rework

### 4MA1-1.4B — manipulate surds, including rationalising a denominator
- Note: Rationalising Denominators (`notes/1-numbers-and-the-number-system/surds/rationalising-denominators.json`)
- Chunk: ordinal 2 — heading `How do I rationalise simple denominators?` — sha256_16 `8a3bb0edbf78da00` — 515 chars
- Evidence quote (verbatim self-slice, markdown-safe): "How do I rationalise simple denominators?
- If the **denominator **is a** surd**:

  - Multiply **the top and bottom of the fraction** by the **surd on the denominator**
  
    - $\frac{a}{\sqrt{b}}=\frac{a}{\sqrt{b}}\times\frac{\sqrt{b}}{\"
- Chunk excerpt: «How do I rationalise simple denominators? - If the **denominator **is a** surd**: - Multiply **the top and bottom of the fraction** by the **surd on the denominator** - $\frac{a}{\sqrt{b}}=\frac{a}{\sqrt{b}}\times\frac{\sqrt{b}}{\sqrt{b}}$ - This is equivalent to multiplying by 1, so does not change the value of the fraction - $\sqrt{b}\times\sqrt{b}=b$ so the denominator is no longer a surd - Multiply the fractions »
- Upstream: T-C32 join notes/1-numbers-and-the-number-system/surds/rationalising-denominators.json::spcpt_wMN58K4jZ54z8bXC — tier R1_parse_repair_statement_join — score n/a — wording EXACT — validation tier AI_VALIDATED (operator-delegated chain)
- Rationale: SME span 'Rationalising Denominators' on note 'Rationalising Denominators' is anchored by the corpus spec_point block spcpt_wMN58K4jZ54z8bXC and joined to 4MA1-1.4B via operator-verdict statement join after T-SPEC-8 parse repair (PMT excluded as source); this section chunk sits inside that span.
- Verdict: [ ] CONFIRM — this chunk belongs to this SP   [ ] REJECT — wrong chunk/SP   [ ] HOLD — needs rework

### 4MA1-6.3A — draw and use tree diagrams
- Note: Combined Probability (`notes/6-statistics-and-probability/combined-and-conditional-probability/combined-probability.json`)
- Chunk: ordinal 1 — heading `How do I calculate combined probabilities?` — sha256_16 `e25f447b8dd17739` — 632 chars
- Evidence quote (verbatim self-slice, markdown-safe): "How do I calculate combined probabilities?
- You can calculate probabilities of **one event after another** without needing tree diagrams

  - These are called **combined** (or successive) probabilities
- There are two **rules **to learn

 "
- Chunk excerpt: «How do I calculate combined probabilities? - You can calculate probabilities of **one event after another** without needing tree diagrams - These are called **combined** (or successive) probabilities - There are two **rules **to learn - **And** means **multiply** and **or **means **add** - P(A **and** B) = P(A) x P(B) - P(AA **or** BB) = P(AA) + P(BB) - Try to **rephrase **each question using and / or - For example, »
- Upstream: T-C32 join notes/6-statistics-and-probability/combined-and-conditional-probability/combined-probability.json::spcpt_RJtRSrxJtXZPyDHz — tier R1_parse_repair_statement_join — score n/a — wording EXACT — validation tier AI_VALIDATED (operator-delegated chain)
- Rationale: SME span 'Combined Probability' on note 'Combined Probability' is anchored by the corpus spec_point block spcpt_RJtRSrxJtXZPyDHz and joined to 4MA1-6.3A via operator-verdict statement join after T-SPEC-8 parse repair (PMT excluded as source); this section chunk sits inside that span.
- Verdict: [ ] CONFIRM — this chunk belongs to this SP   [ ] REJECT — wrong chunk/SP   [ ] HOLD — needs rework

### 4MA1-2.8A — solve quadratic inequalities in one unknown and represent the solution set on a number line
- Note: Solving Quadratic Inequalities (`notes/2-equations-formulae-and-identities/solving-inequalities/solving-quadratic-inequalities.json`)
- Chunk: ordinal 3 — heading `What do I do if the sign of the inequality changes?` — sha256_16 `c8072d3531b1c56d` — 1244 chars
- Evidence quote (verbatim self-slice, markdown-safe): "What do I do if the sign of the inequality changes?
- If the quadratic inequality is $ax^{2}+bx+c\geq0$ where $a$ is positive

  - then shade the parts of the curve** above** the $x$-axis
- If the quadratic inequality is $ax^{2}+bx+c\leq0$ "
- Chunk excerpt: «What do I do if the sign of the inequality changes? - If the quadratic inequality is $ax^{2}+bx+c\geq0$ where $a$ is positive - then shade the parts of the curve** above** the $x$-axis - If the quadratic inequality is $ax^{2}+bx+c\leq0$ where $a$ is positive - then shade the part of the curve** below **the $x$-axis - For example, to solve `open parentheses x minus 2 close parentheses open parentheses x minus 5 close »
- Upstream: T-C32 join notes/2-equations-formulae-and-identities/solving-inequalities/solving-quadratic-inequalities.json::spcpt_dnkHMPkqhhdDxPkZ — tier R1_parse_repair_statement_join — score n/a — wording EXACT — validation tier AI_VALIDATED (operator-delegated chain)
- Rationale: SME span 'Solving Quadratic Inequalities' on note 'Solving Quadratic Inequalities' is anchored by the corpus spec_point block spcpt_dnkHMPkqhhdDxPkZ and joined to 4MA1-2.8A via operator-verdict statement join after T-SPEC-8 parse repair (PMT excluded as source); this section chunk sits inside that span.
- Verdict: [ ] CONFIRM — this chunk belongs to this SP   [ ] REJECT — wrong chunk/SP   [ ] HOLD — needs rework

### 4MA1-1.3C — order decimals
- Note: Ordering Fractions, Decimals & Percentages (`notes/1-numbers-and-the-number-system/fractions-decimals-and-percentages/ordering-fdp.json`)
- Chunk: ordinal 3 — heading `Which symbols can I use?` — sha256_16 `b0d530fae1bcc8c5` — 2432 chars
- Evidence quote (verbatim self-slice, markdown-safe): "Which symbols can I use?
- Rather than just listing values in order, symbols can be used to compare them

  - For example, $\frac{1}{4}<\frac{1}{3}<\frac{1}{2}$
- Recall that $>$ means **greater than** and $\geq$ means greater than **or equ"
- Chunk excerpt: «Which symbols can I use? - Rather than just listing values in order, symbols can be used to compare them - For example, $\frac{1}{4}<\frac{1}{3}<\frac{1}{2}$ - Recall that $>$ means **greater than** and $\geq$ means greater than **or equal to** - Similarly, $<$ means **less **than and $\leq$ means less than or equal to - You may also see $=$and $\neq$ (which means "**not **equal to") Exam Hint: A calculator can be us»
- Upstream: T-C32 join notes/1-numbers-and-the-number-system/fractions-decimals-and-percentages/ordering-fdp.json::spcpt_KNXbNby67zKvX8SX — tier P2_operator_content_join — score n/a — wording EXACT — validation tier AI_VALIDATED (operator-delegated chain)
- Rationale: SME span 'Ordering FDP' on note 'Ordering Fractions, Decimals & Percentages' is anchored by the corpus spec_point block spcpt_KNXbNby67zKvX8SX and joined to 4MA1-1.3C via T-SPEC-9 operator verdict (no upstream; PMT excluded as source); this section chunk sits inside that span.
- Verdict: [ ] CONFIRM — this chunk belongs to this SP   [ ] REJECT — wrong chunk/SP   [ ] HOLD — needs rework

### 4MA1-1.3C — order decimals
- Note: Ordering Fractions, Decimals & Percentages (`notes/1-numbers-and-the-number-system/fractions-decimals-and-percentages/ordering-fdp.json`)
- Chunk: ordinal 1 — heading `How do I put fractions in order of size?` — sha256_16 `543455368ac60f74` — 668 chars
- Evidence quote (verbatim self-slice, markdown-safe): "How do I put fractions in order of size?
- When comparing **only fractions**, write them over a **lowest common denominator**

  - For $\frac{3}{5},\frac{1}{2},\frac{13}{20},\frac{7}{12}$, the lowest common denominator is **60**
  - So chan"
- Chunk excerpt: «How do I put fractions in order of size? - When comparing **only fractions**, write them over a **lowest common denominator** - For $\frac{3}{5},\frac{1}{2},\frac{13}{20},\frac{7}{12}$, the lowest common denominator is **60** - So change them to $\frac{36}{60},\frac{30}{60},\frac{39}{60},\frac{35}{60}$ and then** order them by their numerators** - From smallest to largest: $\frac{30}{60},\frac{35}{60},\frac{36}{60},\»
- Upstream: T-C32 join notes/1-numbers-and-the-number-system/fractions-decimals-and-percentages/ordering-fdp.json::spcpt_KNXbNby67zKvX8SX — tier P2_operator_content_join — score n/a — wording EXACT — validation tier AI_VALIDATED (operator-delegated chain)
- Rationale: SME span 'Ordering FDP' on note 'Ordering Fractions, Decimals & Percentages' is anchored by the corpus spec_point block spcpt_KNXbNby67zKvX8SX and joined to 4MA1-1.3C via T-SPEC-9 operator verdict (no upstream; PMT excluded as source); this section chunk sits inside that span.
- Verdict: [ ] CONFIRM — this chunk belongs to this SP   [ ] REJECT — wrong chunk/SP   [ ] HOLD — needs rework

### 4MA1-3.3B — apply to the graph ofy = f(x)the transformations y = f(x) + a, y = f(ax), y = f(x + a), y = af(x) for linear, quadratic, sine and cosine functions
- Note: Reflections of Graphs (`notes/3-sequences-functions-and-graphs/transformations-of-graphs/reflections-of-graphs.json`)
- Chunk: ordinal 6 — heading `How does a reflection affect the equation of the graph?` — sha256_16 `22c886748bc2e4a8` — 728 chars
- Evidence quote (verbatim self-slice, markdown-safe): "How does a reflection affect the equation of the graph?
- When a graph is reflected, you can **change its equation algebraically **

  - There is no need to sketch the graph
- Reflecting in the $x$-axis puts a $-$** in front **of the whole "
- Chunk excerpt: «How does a reflection affect the equation of the graph? - When a graph is reflected, you can **change its equation algebraically ** - There is no need to sketch the graph - Reflecting in the $x$-axis puts a $-$** in front **of the whole **equation** - For example, $y=x^{2}+2x$ becomes `y equals negative open parentheses x squared plus 2 x close parentheses` - This simplifies to $y=-x^{2}-2x$ - Reflecting in the $y$-a»
- Upstream: T-C32 join notes/3-sequences-functions-and-graphs/transformations-of-graphs/reflections-of-graphs.json::spcpt_qNDqnmZtzYttZDnz — tier P2_operator_content_join — score n/a — wording EXACT — validation tier AI_VALIDATED (operator-delegated chain)
- Rationale: SME span 'Reflections of Graphs' on note 'Reflections of Graphs' is anchored by the corpus spec_point block spcpt_qNDqnmZtzYttZDnz and joined to 4MA1-3.3B via T-SPEC-9 operator verdict (no upstream; PMT excluded as source); this section chunk sits inside that span.
- Verdict: [ ] CONFIRM — this chunk belongs to this SP   [ ] REJECT — wrong chunk/SP   [ ] HOLD — needs rework

### 4MA1-1.3C — order decimals
- Note: Ordering Fractions, Decimals & Percentages (`notes/1-numbers-and-the-number-system/fractions-decimals-and-percentages/ordering-fdp.json`)
- Chunk: ordinal 2 — heading `How do I put fractions, decimals and percentages in order of size?` — sha256_16 `ec0651862c738210` — 273 chars
- Evidence quote (verbatim self-slice, markdown-safe): "How do I put fractions, decimals and percentages in order of size?
- When comparing a mixture of fractions, decimals and percentages, **change everything into decimals**
Ordering fractions, decimals, and percentages
Order by Size Notes fig5"
- Chunk excerpt: «How do I put fractions, decimals and percentages in order of size? - When comparing a mixture of fractions, decimals and percentages, **change everything into decimals** Ordering fractions, decimals, and percentages Order by Size Notes fig5 (2) Order by Size Notes fig5 (3)»
- Upstream: T-C32 join notes/1-numbers-and-the-number-system/fractions-decimals-and-percentages/ordering-fdp.json::spcpt_KNXbNby67zKvX8SX — tier P2_operator_content_join — score n/a — wording EXACT — validation tier AI_VALIDATED (operator-delegated chain)
- Rationale: SME span 'Ordering FDP' on note 'Ordering Fractions, Decimals & Percentages' is anchored by the corpus spec_point block spcpt_KNXbNby67zKvX8SX and joined to 4MA1-1.3C via T-SPEC-9 operator verdict (no upstream; PMT excluded as source); this section chunk sits inside that span.
- Verdict: [ ] CONFIRM — this chunk belongs to this SP   [ ] REJECT — wrong chunk/SP   [ ] HOLD — needs rework

### 4MA1-1.6G — use compound interest and depreciation
- Note: Compound Interest (`notes/1-numbers-and-the-number-system/compound-interest-and-depreciation/compound-interest.json`)
- Chunk: ordinal 4 — heading `How do I solve reverse compound interest problems?` — sha256_16 `6f9498924a42abd9` — 1904 chars
- Evidence quote (verbatim self-slice, markdown-safe): "How do I solve reverse compound interest problems?
- You could be **told the final balance** **after **compound interest has been applied, and **need to find the original amount**

  - This could be referred to as a "**reverse compound inte"
- Chunk excerpt: «How do I solve reverse compound interest problems? - You could be **told the final balance** **after **compound interest has been applied, and **need to find the original amount** - This could be referred to as a "**reverse compound interest**" problem - For example if: - The final balance is £432 - After 20% interest has been applied each year - For 3 years - Using the same method as above, this can be written as an»
- Upstream: T-C32 join notes/1-numbers-and-the-number-system/compound-interest-and-depreciation/compound-interest.json::spcpt_vyd4VnJDqBJWvTNc — tier P1_name_fragment_join — score n/a — wording EXACT — validation tier AI_VALIDATED (operator-delegated chain)
- Rationale: SME span 'Compound Interest' on note 'Compound Interest' is anchored by the corpus spec_point block spcpt_vyd4VnJDqBJWvTNc and joined to 4MA1-1.6G via operator-verdict name-fragment join (T-SPEC-7; PMT excluded as source); this section chunk sits inside that span.
- Verdict: [ ] CONFIRM — this chunk belongs to this SP   [ ] REJECT — wrong chunk/SP   [ ] HOLD — needs rework

### 4MA1-6.2B — understand the concept of a measure of spread
- Note: Comparing Data Sets (`notes/6-statistics-and-probability/statistics-toolkit/comparing-distributions.json`)
- Chunk: ordinal 4 — heading `What else could I be asked?` — sha256_16 `34d3e4017a99fa1a` — 1604 chars
- Evidence quote (verbatim self-slice, markdown-safe): "What else could I be asked?
- You may need to** choose** which, out of mode, median and mean, to compare

  - Check for **extreme values** (outliers) in the data
  
    - Avoid using the** mean **as it is affected by extreme values
- You ma"
- Chunk excerpt: «What else could I be asked? - You may need to** choose** which, out of mode, median and mean, to compare - Check for **extreme values** (outliers) in the data - Avoid using the** mean **as it is affected by extreme values - You may need to think from the **point of view** of another person - A teacher might not want a large spread of marks - It might show that they haven't taught the topic very well! - An examiner mi»
- Upstream: T-C32 join notes/6-statistics-and-probability/statistics-toolkit/comparing-distributions.json::spcpt_vDScwbWGWfmFC3TT — tier P2_operator_content_join — score n/a — wording EXACT — validation tier AI_VALIDATED (operator-delegated chain)
- Rationale: SME span 'Comparing Distributions' on note 'Comparing Data Sets' is anchored by the corpus spec_point block spcpt_vDScwbWGWfmFC3TT and joined to 4MA1-6.2B via T-SPEC-9 operator verdict (no upstream; PMT excluded as source); this section chunk sits inside that span.
- Verdict: [ ] CONFIRM — this chunk belongs to this SP   [ ] REJECT — wrong chunk/SP   [ ] HOLD — needs rework

### 4MA1-6.1C — use cumulative frequency diagrams
- Note: Probability Tree Diagrams (`notes/6-statistics-and-probability/probability-diagrams---venn-and-tree-diagrams/tree-diagrams.json`)
- Chunk: ordinal 1 — heading `How do I draw a tree diagram?` — sha256_16 `c2a210174010bc3a` — 476 chars
- Evidence quote (verbatim self-slice, markdown-safe): "How do I draw a tree diagram?
- **Tree diagrams** can be used for** repeated** **experiments** with **two outcomes**

  - The **1st experiment **has outcome **A** or **not A**
  - The **2nd experiment **has outcome **B** or not **B**
- Read"
- Chunk excerpt: «How do I draw a tree diagram? - **Tree diagrams** can be used for** repeated** **experiments** with **two outcomes** - The **1st experiment **has outcome **A** or **not A** - The **2nd experiment **has outcome **B** or not **B** - Read the tree diagram from** left to right** along its **branches** - For example, the top branches give A followed by B - This is called A** and** B How to set up a tree diagram for two ex»
- Upstream: T-C32 join notes/6-statistics-and-probability/probability-diagrams---venn-and-tree-diagrams/tree-diagrams.json::spcpt_hTsm2dz7xmwM4jwW — tier P1_name_fragment_join — score n/a — wording EXACT — validation tier AI_VALIDATED (operator-delegated chain)
- Rationale: SME span 'Tree Diagrams' on note 'Probability Tree Diagrams' is anchored by the corpus spec_point block spcpt_hTsm2dz7xmwM4jwW and joined to 4MA1-6.1C via operator-verdict name-fragment join (T-SPEC-7; PMT excluded as source); this section chunk sits inside that span.
- Verdict: [ ] CONFIRM — this chunk belongs to this SP   [ ] REJECT — wrong chunk/SP   [ ] HOLD — needs rework

### 4MA1-1.3A — convert recurring decimals into fractions
- Note: Recurring Decimals (`notes/1-numbers-and-the-number-system/fractions-decimals-and-percentages/recurring-decimals.json`)
- Chunk: ordinal 2 — heading `How do I write recurring decimals as fractions?` — sha256_16 `7b51471115f44a86` — 1912 chars
- Evidence quote (verbatim self-slice, markdown-safe): "How do I write recurring decimals as fractions?
Write out the first few decimal places to show the recurring pattern and then:
- **STEP 1**
Write the recurring decimal as $x=...$

  - $x=0.35353535...$
- **STEP 2**
**Multiply both sides by "
- Chunk excerpt: «How do I write recurring decimals as fractions? Write out the first few decimal places to show the recurring pattern and then: - **STEP 1** Write the recurring decimal as $x=...$ - $x=0.35353535...$ - **STEP 2** **Multiply both sides by 10** **repeatedly** until two lines have the same recurring decimal part - `table row x equals cell 0.35353535... end cell end table` - `table row cell 10 x end cell equals cell 3.535»
- Upstream: T-C32 join notes/1-numbers-and-the-number-system/fractions-decimals-and-percentages/recurring-decimals.json::spcpt_BVf2GTX8FCvzJjJN — tier R1_parse_repair_statement_join — score n/a — wording EXACT — validation tier AI_VALIDATED (operator-delegated chain)
- Rationale: SME span 'Recurring Decimals' on note 'Recurring Decimals' is anchored by the corpus spec_point block spcpt_BVf2GTX8FCvzJjJN and joined to 4MA1-1.3A via operator-verdict statement join after T-SPEC-8 parse repair (PMT excluded as source); this section chunk sits inside that span.
- Verdict: [ ] CONFIRM — this chunk belongs to this SP   [ ] REJECT — wrong chunk/SP   [ ] HOLD — needs rework

### 4MA1-4.9A — find perimeters and areas of sectors of circles
- Note: Arc Lengths & Sector Areas (`notes/4-geometry-and-trigonometry/circles-arcs-and-sectors/arcs-and-sectors.json`)
- Chunk: ordinal 5 — heading `How do I find the area of a sector?` — sha256_16 `0e6cb5f2bc7858cb` — 1524 chars
- Evidence quote (verbatim self-slice, markdown-safe): "How do I find the area of a sector?
- **STEP 1**
**Divide** the **angle** by **360** to form a fraction

  - $\frac{θ}{360}$
- **STEP 2**
Calculate the **area** of the **full circle**

  - $πr^{2}$
- **STEP 3**
**Multiply** the **fraction**"
- Chunk excerpt: «How do I find the area of a sector? - **STEP 1** **Divide** the **angle** by **360** to form a fraction - $\frac{θ}{360}$ - **STEP 2** Calculate the **area** of the **full circle** - $πr^{2}$ - **STEP 3** **Multiply** the **fraction** by the **area** - $\frac{θ}{360}\timesπr^{2}$ Exam Hint: Make sure you remember the formulas for the **circumference **and **area **of a circle, as they are not given in the exam. **Arc»
- Upstream: T-C32 join notes/4-geometry-and-trigonometry/circles-arcs-and-sectors/arcs-and-sectors.json::spcpt_dvX7WnB2FSdky4jW — tier R1_parse_repair_statement_join — score n/a — wording EXACT — validation tier AI_VALIDATED (operator-delegated chain)
- Rationale: SME span 'Arc Lengths & Sector Areas' on note 'Arc Lengths & Sector Areas' is anchored by the corpus spec_point block spcpt_dvX7WnB2FSdky4jW and joined to 4MA1-4.9A via operator-verdict statement join after T-SPEC-8 parse repair (PMT excluded as source); this section chunk sits inside that span.
- Verdict: [ ] CONFIRM — this chunk belongs to this SP   [ ] REJECT — wrong chunk/SP   [ ] HOLD — needs rework

### 4MA1-2.2C — manipulate algebraic fractions where the numerator and/or the denominator can be numeric, linear or quadratic
- Note: Solving Equations with Algebraic Fractions (`notes/2-equations-formulae-and-identities/algebraic-fractions/solving-algebraic-fractions.json`)
- Chunk: ordinal 1 — heading `How do I solve an equation that contains algebraic fractions?` — sha256_16 `2dacd9d22e6f7efe` — 5030 chars
- Evidence quote (verbatim self-slice, markdown-safe): "How do I solve an equation that contains algebraic fractions?
- There are **two methods** for **solving equations** that contain algebraic fractions
- One method is to **add **or** subtract **the **algebraic fractions first** and then solve"
- Chunk excerpt: «How do I solve an equation that contains algebraic fractions? - There are **two methods** for **solving equations** that contain algebraic fractions - One method is to **add **or** subtract **the **algebraic fractions first** and then solve as usual - For example, to solve $\frac{8}{x+1}-\frac{5}{x+2}=1$ - First subtract the fractions and simplify, `fraction numerator 3 x plus 11 over denominator open parentheses x p»
- Upstream: T-C32 join notes/2-equations-formulae-and-identities/algebraic-fractions/solving-algebraic-fractions.json::spcpt_xwx7PVk7fQ5QpdMk — tier R1_parse_repair_statement_join — score n/a — wording EXACT — validation tier AI_VALIDATED (operator-delegated chain)
- Rationale: SME span 'Solving Algebraic Fractions' on note 'Solving Equations with Algebraic Fractions' is anchored by the corpus spec_point block spcpt_xwx7PVk7fQ5QpdMk and joined to 4MA1-2.2C via operator-verdict statement join after T-SPEC-8 parse repair (PMT excluded as source); this section chunk sits inside that span.
- Verdict: [ ] CONFIRM — this chunk belongs to this SP   [ ] REJECT — wrong chunk/SP   [ ] HOLD — needs rework

### 4MA1-1.3C — order decimals
- Note: Ordering Fractions, Decimals & Percentages (`notes/1-numbers-and-the-number-system/fractions-decimals-and-percentages/ordering-fdp.json`)
- Chunk: ordinal 0 — heading `Ordering FDP` — sha256_16 `f808945e91a16071` — 12 chars
- Evidence quote (verbatim self-slice, markdown-safe): "Ordering FDP"
- Chunk excerpt: «Ordering FDP»
- Upstream: T-C32 join notes/1-numbers-and-the-number-system/fractions-decimals-and-percentages/ordering-fdp.json::spcpt_KNXbNby67zKvX8SX — tier P2_operator_content_join — score n/a — wording EXACT — validation tier AI_VALIDATED (operator-delegated chain)
- Rationale: SME span 'Ordering FDP' on note 'Ordering Fractions, Decimals & Percentages' is anchored by the corpus spec_point block spcpt_KNXbNby67zKvX8SX and joined to 4MA1-1.3C via T-SPEC-9 operator verdict (no upstream; PMT excluded as source); this section chunk sits inside that span.
- Verdict: [ ] CONFIRM — this chunk belongs to this SP   [ ] REJECT — wrong chunk/SP   [ ] HOLD — needs rework

### 4MA1-3.3B — apply to the graph ofy = f(x)the transformations y = f(x) + a, y = f(ax), y = f(x + a), y = af(x) for linear, quadratic, sine and cosine functions
- Note: Reflections of Graphs (`notes/3-sequences-functions-and-graphs/transformations-of-graphs/reflections-of-graphs.json`)
- Chunk: ordinal 0 — heading `Reflections of graphs` — sha256_16 `8c3613d51e9095f6` — 21 chars
- Evidence quote (verbatim self-slice, markdown-safe): "Reflections of graphs"
- Chunk excerpt: «Reflections of graphs»
- Upstream: T-C32 join notes/3-sequences-functions-and-graphs/transformations-of-graphs/reflections-of-graphs.json::spcpt_qNDqnmZtzYttZDnz — tier P2_operator_content_join — score n/a — wording EXACT — validation tier AI_VALIDATED (operator-delegated chain)
- Rationale: SME span 'Reflections of Graphs' on note 'Reflections of Graphs' is anchored by the corpus spec_point block spcpt_qNDqnmZtzYttZDnz and joined to 4MA1-3.3B via T-SPEC-9 operator verdict (no upstream; PMT excluded as source); this section chunk sits inside that span.
- Verdict: [ ] CONFIRM — this chunk belongs to this SP   [ ] REJECT — wrong chunk/SP   [ ] HOLD — needs rework

### 4MA1-3.3B — apply to the graph ofy = f(x)the transformations y = f(x) + a, y = f(ax), y = f(x + a), y = af(x) for linear, quadratic, sine and cosine functions
- Note: Reflections of Graphs (`notes/3-sequences-functions-and-graphs/transformations-of-graphs/reflections-of-graphs.json`)
- Chunk: ordinal 2 — heading `How do I reflect graphs?` — sha256_16 `e43481bf7db6f420` — 135 chars
- Evidence quote (verbatim self-slice, markdown-safe): "How do I reflect graphs?
- Let `y equals straight f open parentheses x close parentheses` be the **equation** of the **original graph**"
- Chunk excerpt: «How do I reflect graphs? - Let `y equals straight f open parentheses x close parentheses` be the **equation** of the **original graph**»
- Upstream: T-C32 join notes/3-sequences-functions-and-graphs/transformations-of-graphs/reflections-of-graphs.json::spcpt_qNDqnmZtzYttZDnz — tier P2_operator_content_join — score n/a — wording EXACT — validation tier AI_VALIDATED (operator-delegated chain)
- Rationale: SME span 'Reflections of Graphs' on note 'Reflections of Graphs' is anchored by the corpus spec_point block spcpt_qNDqnmZtzYttZDnz and joined to 4MA1-3.3B via T-SPEC-9 operator verdict (no upstream; PMT excluded as source); this section chunk sits inside that span.
- Verdict: [ ] CONFIRM — this chunk belongs to this SP   [ ] REJECT — wrong chunk/SP   [ ] HOLD — needs rework

### 4MA1-4.6A — understand and use the internal and external intersecting chord properties
- Note: Intersecting Chord Theorem (`notes/4-geometry-and-trigonometry/circle-theorems/intersecting-chord-theorem.json`)
- Chunk: ordinal 4 — heading `Intersecting Chord Theorem (External)` — sha256_16 `f645c4c25808c71a` — 37 chars
- Evidence quote (verbatim self-slice, markdown-safe): "Intersecting Chord Theorem (External)"
- Chunk excerpt: «Intersecting Chord Theorem (External)»
- Upstream: T-C32 join notes/4-geometry-and-trigonometry/circle-theorems/intersecting-chord-theorem.json::spcpt_syhVK6wH6NDDfgdB — tier R1_parse_repair_statement_join — score n/a — wording EXACT — validation tier AI_VALIDATED (operator-delegated chain)
- Rationale: SME span 'Intersecting Chord Theorem (External)' on note 'Intersecting Chord Theorem' is anchored by the corpus spec_point block spcpt_syhVK6wH6NDDfgdB and joined to 4MA1-4.6A via operator-verdict statement join after T-SPEC-8 parse repair (PMT excluded as source); this section chunk sits inside that span.
- Verdict: [ ] CONFIRM — this chunk belongs to this SP   [ ] REJECT — wrong chunk/SP   [ ] HOLD — needs rework

### 4MA1-6.1B — construct cumulative frequency diagrams from tabulated data
- Note: Interpreting Cumulative Frequency Diagrams (`notes/6-statistics-and-probability/cumulative-frequency-diagrams/interpreting-cumulative-frequency-diagrams.json`)
- Chunk: ordinal 0 — heading `Interpreting cumulative frequency diagrams` — sha256_16 `e2c4a9a80ce897b2` — 42 chars
- Evidence quote (verbatim self-slice, markdown-safe): "Interpreting cumulative frequency diagrams"
- Chunk excerpt: «Interpreting cumulative frequency diagrams»
- Upstream: T-C32 join notes/6-statistics-and-probability/cumulative-frequency-diagrams/interpreting-cumulative-frequency-diagrams.json::spcpt_8sCVwmD5VVBv6xWg — tier R1_parse_repair_statement_join — score n/a — wording EXACT — validation tier AI_VALIDATED (operator-delegated chain)
- Rationale: SME span 'Interpreting Cumulative Frequency Diagrams' on note 'Interpreting Cumulative Frequency Diagrams' is anchored by the corpus spec_point block spcpt_8sCVwmD5VVBv6xWg and joined to 4MA1-6.1B via operator-verdict statement join after T-SPEC-8 parse repair (PMT excluded as source); this section chunk sits inside that span.
- Verdict: [ ] CONFIRM — this chunk belongs to this SP   [ ] REJECT — wrong chunk/SP   [ ] HOLD — needs rework

### 4MA1-3.3B — apply to the graph ofy = f(x)the transformations y = f(x) + a, y = f(ax), y = f(x + a), y = af(x) for linear, quadratic, sine and cosine functions
- Note: Stretches of Graphs (`notes/3-sequences-functions-and-graphs/transformations-of-graphs/stretches-of-graphs.json`)
- Chunk: ordinal 4 — heading `Horizontal stretches: y=f(ax)` — sha256_16 `9a80dc243fcc61cd` — 1006 chars
- Evidence quote (verbatim self-slice, markdown-safe): "Horizontal stretches: y=f(ax)
- `y equals straight f open parentheses a x close parentheses` is a **horizontal stretch **(in the $y$-direction) of **scale factor **$\frac{1}{a}$ (not $a$)

  - The $y$-coordinates stay the same but the $x$ c"
- Chunk excerpt: «Horizontal stretches: y=f(ax) - `y equals straight f open parentheses a x close parentheses` is a **horizontal stretch **(in the $y$-direction) of **scale factor **$\frac{1}{a}$ (not $a$) - The $y$-coordinates stay the same but the $x$ coordinates are multiplied by $\frac{1}{a}$ (divided by $a$) - Points appear to move **parallel to the **$x$**-axis** - either squashing horizontally towards the $y$-axis if $a>1$ - or»
- Upstream: T-C32 join notes/3-sequences-functions-and-graphs/transformations-of-graphs/stretches-of-graphs.json::spcpt_YcMPxJgtrjtBzMkV — tier P2_operator_content_join — score n/a — wording EXACT — validation tier AI_VALIDATED (operator-delegated chain)
- Rationale: SME span 'Stretches of Graphs' on note 'Stretches of Graphs' is anchored by the corpus spec_point block spcpt_YcMPxJgtrjtBzMkV and joined to 4MA1-3.3B via T-SPEC-9 operator verdict (no upstream; PMT excluded as source); this section chunk sits inside that span.
- Verdict: [ ] CONFIRM — this chunk belongs to this SP   [ ] REJECT — wrong chunk/SP   [ ] HOLD — needs rework

### 4MA1-4.8B — understand and use angles of elevation and depression
- Note: Angles of Elevation & Depression (`notes/4-geometry-and-trigonometry/right-angled-triangles---pythagoras-and-trigonometry/angles-of-elevation-and-depression.json`)
- Chunk: ordinal 0 — heading `Elevation & depression` — sha256_16 `ad6b45ccce9d3f2b` — 22 chars
- Evidence quote (verbatim self-slice, markdown-safe): "Elevation & depression"
- Chunk excerpt: «Elevation & depression»
- Upstream: T-C32 join notes/4-geometry-and-trigonometry/right-angled-triangles---pythagoras-and-trigonometry/angles-of-elevation-and-depression.json::spcpt_9JzR7VMzsQqT4KHq — tier R1_parse_repair_statement_join — score n/a — wording EXACT — validation tier AI_VALIDATED (operator-delegated chain)
- Rationale: SME span 'Elevation & Depression' on note 'Angles of Elevation & Depression' is anchored by the corpus spec_point block spcpt_9JzR7VMzsQqT4KHq and joined to 4MA1-4.8B via operator-verdict statement join after T-SPEC-8 parse repair (PMT excluded as source); this section chunk sits inside that span.
- Verdict: [ ] CONFIRM — this chunk belongs to this SP   [ ] REJECT — wrong chunk/SP   [ ] HOLD — needs rework

### 4MA1-3.3B — apply to the graph ofy = f(x)the transformations y = f(x) + a, y = f(ax), y = f(x + a), y = af(x) for linear, quadratic, sine and cosine functions
- Note: Stretches of Graphs (`notes/3-sequences-functions-and-graphs/transformations-of-graphs/stretches-of-graphs.json`)
- Chunk: ordinal 7 — heading `How do I apply a combined stretch?` — sha256_16 `3e98955edc0e5d37` — 1723 chars
- Evidence quote (verbatim self-slice, markdown-safe): "How do I apply a combined stretch?
- The graph of `y equals b straight f open parentheses a x close parentheses` is a **combined stretch**<sub>**,**</sub> both horizontally and vertically

  - It **does not matter which order **you apply th"
- Chunk excerpt: «How do I apply a combined stretch? - The graph of `y equals b straight f open parentheses a x close parentheses` is a **combined stretch**<sub>**,**</sub> both horizontally and vertically - It **does not matter which order **you apply these in - For example, a horizontal stretch of scale factor $\frac{1}{a}$ followed by a vertical stretch of scale factor $b$ Worked Example: The diagram below shows the graph of `y equ»
- Upstream: T-C32 join notes/3-sequences-functions-and-graphs/transformations-of-graphs/stretches-of-graphs.json::spcpt_YcMPxJgtrjtBzMkV — tier P2_operator_content_join — score n/a — wording EXACT — validation tier AI_VALIDATED (operator-delegated chain)
- Rationale: SME span 'Stretches of Graphs' on note 'Stretches of Graphs' is anchored by the corpus spec_point block spcpt_YcMPxJgtrjtBzMkV and joined to 4MA1-3.3B via T-SPEC-9 operator verdict (no upstream; PMT excluded as source); this section chunk sits inside that span.
- Verdict: [ ] CONFIRM — this chunk belongs to this SP   [ ] REJECT — wrong chunk/SP   [ ] HOLD — needs rework

### 4MA1-4.9A — find perimeters and areas of sectors of circles
- Note: Arc Lengths & Sector Areas (`notes/4-geometry-and-trigonometry/circles-arcs-and-sectors/arcs-and-sectors.json`)
- Chunk: ordinal 0 — heading `Arc lengths & sector areas` — sha256_16 `7c36a17fb226c67f` — 26 chars
- Evidence quote (verbatim self-slice, markdown-safe): "Arc lengths & sector areas"
- Chunk excerpt: «Arc lengths & sector areas»
- Upstream: T-C32 join notes/4-geometry-and-trigonometry/circles-arcs-and-sectors/arcs-and-sectors.json::spcpt_dvX7WnB2FSdky4jW — tier R1_parse_repair_statement_join — score n/a — wording EXACT — validation tier AI_VALIDATED (operator-delegated chain)
- Rationale: SME span 'Arc Lengths & Sector Areas' on note 'Arc Lengths & Sector Areas' is anchored by the corpus spec_point block spcpt_dvX7WnB2FSdky4jW and joined to 4MA1-4.9A via operator-verdict statement join after T-SPEC-8 parse repair (PMT excluded as source); this section chunk sits inside that span.
- Verdict: [ ] CONFIRM — this chunk belongs to this SP   [ ] REJECT — wrong chunk/SP   [ ] HOLD — needs rework

### 4MA1-3.3B — apply to the graph ofy = f(x)the transformations y = f(x) + a, y = f(ax), y = f(x + a), y = af(x) for linear, quadratic, sine and cosine functions
- Note: Stretches of Graphs (`notes/3-sequences-functions-and-graphs/transformations-of-graphs/stretches-of-graphs.json`)
- Chunk: ordinal 2 — heading `How do I stretch graphs?` — sha256_16 `fee591ee4b729e0b` — 135 chars
- Evidence quote (verbatim self-slice, markdown-safe): "How do I stretch graphs?
- Let `y equals straight f open parentheses x close parentheses` be the **equation** of the **original graph**"
- Chunk excerpt: «How do I stretch graphs? - Let `y equals straight f open parentheses x close parentheses` be the **equation** of the **original graph**»
- Upstream: T-C32 join notes/3-sequences-functions-and-graphs/transformations-of-graphs/stretches-of-graphs.json::spcpt_YcMPxJgtrjtBzMkV — tier P2_operator_content_join — score n/a — wording EXACT — validation tier AI_VALIDATED (operator-delegated chain)
- Rationale: SME span 'Stretches of Graphs' on note 'Stretches of Graphs' is anchored by the corpus spec_point block spcpt_YcMPxJgtrjtBzMkV and joined to 4MA1-3.3B via T-SPEC-9 operator verdict (no upstream; PMT excluded as source); this section chunk sits inside that span.
- Verdict: [ ] CONFIRM — this chunk belongs to this SP   [ ] REJECT — wrong chunk/SP   [ ] HOLD — needs rework

### 4MA1-6.2B — understand the concept of a measure of spread
- Note: Comparing Data Sets (`notes/6-statistics-and-probability/statistics-toolkit/comparing-distributions.json`)
- Chunk: ordinal 1 — heading `How do I compare two data sets?` — sha256_16 `4b8cb99979b23b4d` — 269 chars
- Evidence quote (verbatim self-slice, markdown-safe): "How do I compare two data sets?
- You may be given **two **sets of data that relate to a context
- To **compare **data sets, you need to

  - compare their **averages**
  
    - Mode, median or mean
  - compare their **spreads**
  
    - Ra"
- Chunk excerpt: «How do I compare two data sets? - You may be given **two **sets of data that relate to a context - To **compare **data sets, you need to - compare their **averages** - Mode, median or mean - compare their **spreads** - Range - Interquartile range»
- Upstream: T-C32 join notes/6-statistics-and-probability/statistics-toolkit/comparing-distributions.json::spcpt_vDScwbWGWfmFC3TT — tier P2_operator_content_join — score n/a — wording EXACT — validation tier AI_VALIDATED (operator-delegated chain)
- Rationale: SME span 'Comparing Distributions' on note 'Comparing Data Sets' is anchored by the corpus spec_point block spcpt_vDScwbWGWfmFC3TT and joined to 4MA1-6.2B via T-SPEC-9 operator verdict (no upstream; PMT excluded as source); this section chunk sits inside that span.
- Verdict: [ ] CONFIRM — this chunk belongs to this SP   [ ] REJECT — wrong chunk/SP   [ ] HOLD — needs rework

### 4MA1-3.3B — apply to the graph ofy = f(x)the transformations y = f(x) + a, y = f(ax), y = f(x + a), y = af(x) for linear, quadratic, sine and cosine functions
- Note: Reflections of Graphs (`notes/3-sequences-functions-and-graphs/transformations-of-graphs/reflections-of-graphs.json`)
- Chunk: ordinal 1 — heading `What are reflections of graphs?` — sha256_16 `b704ed4ea8ae253d` — 179 chars
- Evidence quote (verbatim self-slice, markdown-safe): "What are reflections of graphs?
- **Reflections **of graphs are a type of **transformation** where the **curve **is **reflected **about one of the** axes**
Examples of reflections"
- Chunk excerpt: «What are reflections of graphs? - **Reflections **of graphs are a type of **transformation** where the **curve **is **reflected **about one of the** axes** Examples of reflections»
- Upstream: T-C32 join notes/3-sequences-functions-and-graphs/transformations-of-graphs/reflections-of-graphs.json::spcpt_qNDqnmZtzYttZDnz — tier P2_operator_content_join — score n/a — wording EXACT — validation tier AI_VALIDATED (operator-delegated chain)
- Rationale: SME span 'Reflections of Graphs' on note 'Reflections of Graphs' is anchored by the corpus spec_point block spcpt_qNDqnmZtzYttZDnz and joined to 4MA1-3.3B via T-SPEC-9 operator verdict (no upstream; PMT excluded as source); this section chunk sits inside that span.
- Verdict: [ ] CONFIRM — this chunk belongs to this SP   [ ] REJECT — wrong chunk/SP   [ ] HOLD — needs rework

### 4MA1-4.9A — find perimeters and areas of sectors of circles
- Note: Arc Lengths & Sector Areas (`notes/4-geometry-and-trigonometry/circles-arcs-and-sectors/arcs-and-sectors.json`)
- Chunk: ordinal 2 — heading `What is a sector?` — sha256_16 `72bb236f2eeca470` — 372 chars
- Evidence quote (verbatim self-slice, markdown-safe): "What is a sector?
- A **sector** is the part of a circle enclosed by two **radii** (radiuses) and an arc

  - A sector looks like a slice of a circular pizza
  - The curved edge of a sector is the arc
- Two radii in a circle will create **t"
- Chunk excerpt: «What is a sector? - A **sector** is the part of a circle enclosed by two **radii** (radiuses) and an arc - A sector looks like a slice of a circular pizza - The curved edge of a sector is the arc - Two radii in a circle will create **two sectors** - The **smaller** sector is known as the **minor sector** - The **bigger** sector is known as the **major sector**»
- Upstream: T-C32 join notes/4-geometry-and-trigonometry/circles-arcs-and-sectors/arcs-and-sectors.json::spcpt_dvX7WnB2FSdky4jW — tier R1_parse_repair_statement_join — score n/a — wording EXACT — validation tier AI_VALIDATED (operator-delegated chain)
- Rationale: SME span 'Arc Lengths & Sector Areas' on note 'Arc Lengths & Sector Areas' is anchored by the corpus spec_point block spcpt_dvX7WnB2FSdky4jW and joined to 4MA1-4.9A via operator-verdict statement join after T-SPEC-8 parse repair (PMT excluded as source); this section chunk sits inside that span.
- Verdict: [ ] CONFIRM — this chunk belongs to this SP   [ ] REJECT — wrong chunk/SP   [ ] HOLD — needs rework

### 4MA1-3.3B — apply to the graph ofy = f(x)the transformations y = f(x) + a, y = f(ax), y = f(x + a), y = af(x) for linear, quadratic, sine and cosine functions
- Note: Stretches of Graphs (`notes/3-sequences-functions-and-graphs/transformations-of-graphs/stretches-of-graphs.json`)
- Chunk: ordinal 6 — heading `How does a stretch affect the equation of the graph?` — sha256_16 `4356f9311d5418c6` — 800 chars
- Evidence quote (verbatim self-slice, markdown-safe): "How does a stretch affect the equation of the graph?
- When a graph is stretched, you can **change its equation algebraically **

  - There is no need to sketch the graph
- Stretching vertically by a scale factor of 3 puts a 3** in front **"
- Chunk excerpt: «How does a stretch affect the equation of the graph? - When a graph is stretched, you can **change its equation algebraically ** - There is no need to sketch the graph - Stretching vertically by a scale factor of 3 puts a 3** in front **of the whole **equation** - For example, $y=x^{2}+2x$ becomes `y equals 3 open parentheses x squared plus 2 x close parentheses` - This simplifies to $y=3x^{2}+6x$ - Stretching horizo»
- Upstream: T-C32 join notes/3-sequences-functions-and-graphs/transformations-of-graphs/stretches-of-graphs.json::spcpt_YcMPxJgtrjtBzMkV — tier P2_operator_content_join — score n/a — wording EXACT — validation tier AI_VALIDATED (operator-delegated chain)
- Rationale: SME span 'Stretches of Graphs' on note 'Stretches of Graphs' is anchored by the corpus spec_point block spcpt_YcMPxJgtrjtBzMkV and joined to 4MA1-3.3B via T-SPEC-9 operator verdict (no upstream; PMT excluded as source); this section chunk sits inside that span.
- Verdict: [ ] CONFIRM — this chunk belongs to this SP   [ ] REJECT — wrong chunk/SP   [ ] HOLD — needs rework

### 4MA1-4.6A — understand and use the internal and external intersecting chord properties
- Note: Intersecting Chord Theorem (`notes/4-geometry-and-trigonometry/circle-theorems/intersecting-chord-theorem.json`)
- Chunk: ordinal 2 — heading `How do I use the intersecting chord theorem to solve problems?` — sha256_16 `34cd51268ea791d7` — 542 chars
- Evidence quote (verbatim self-slice, markdown-safe): "How do I use the intersecting chord theorem to solve problems?
- If two chords intersect, you can find a missing length using the intersecting chord theorem

  - You can usually choose to solve the problem either using multiplication (**AP "
- Chunk excerpt: «How do I use the intersecting chord theorem to solve problems? - If two chords intersect, you can find a missing length using the intersecting chord theorem - You can usually choose to solve the problem either using multiplication (**AP × PB = CP × PD**) or using ratio (**AP : PD ≡ CP : PB)** - Carefully keep track of which distance is associated with each part of each chord Diagram of a circle with intersecting chor»
- Upstream: T-C32 join notes/4-geometry-and-trigonometry/circle-theorems/intersecting-chord-theorem.json::spcpt_znWXTZjqCR7PspTc — tier R1_parse_repair_statement_join — score n/a — wording EXACT — validation tier AI_VALIDATED (operator-delegated chain)
- Rationale: SME span 'Intersecting Chord Theorem' on note 'Intersecting Chord Theorem' is anchored by the corpus spec_point block spcpt_znWXTZjqCR7PspTc and joined to 4MA1-4.6A via operator-verdict statement join after T-SPEC-8 parse repair (PMT excluded as source); this section chunk sits inside that span.
- Verdict: [ ] CONFIRM — this chunk belongs to this SP   [ ] REJECT — wrong chunk/SP   [ ] HOLD — needs rework

### 4MA1-1.10C — understand and carry out calculations using time, and carry out calculations using money, including converting between currencies
- Note: Money Calculations (`notes/1-numbers-and-the-number-system/number-toolkit/money-calculations.json`)
- Chunk: ordinal 4 — heading `What should I do when money calculations involve more than two decimal places?` — sha256_16 `208c99d4d14c0ba2` — 1331 chars
- Evidence quote (verbatim self-slice, markdown-safe): "What should I do when money calculations involve more than two decimal places?
- In some contexts money facts may be given to **more** **than two decimal places**

  - E.g. One litre of petrol in the UK costs an average price of £1.579
- Us"
- Chunk excerpt: «What should I do when money calculations involve more than two decimal places? - In some contexts money facts may be given to **more** **than two decimal places** - E.g. One litre of petrol in the UK costs an average price of £1.579 - Use **all of the decimal places** given in your **working** - Round (to two decimal places or whatever is appropriate) for your **final answer only** Exam Hint: Use the **information gi»
- Upstream: T-C32 join notes/1-numbers-and-the-number-system/number-toolkit/money-calculations.json::spcpt_bMYrxtVc2SZgt8mX — tier S1_name_match — score 0.6772 — wording EXACT — validation tier AI_VALIDATED (operator-delegated chain)
- Rationale: SME span 'Money Calculations' on note 'Money Calculations' is anchored by the corpus spec_point block spcpt_bMYrxtVc2SZgt8mX and joined to 4MA1-1.10C via name_to_statement_join; this section chunk sits inside that span.
- Verdict: [ ] CONFIRM — this chunk belongs to this SP   [ ] REJECT — wrong chunk/SP   [ ] HOLD — needs rework

### 4MA1-3.4C — determine gradients, rates of change, stationary points, turning points (maxima and minima) by differentiation and relate these to graphs
- Note: Differentiation (`notes/3-sequences-functions-and-graphs/differentiation/differentiation.json`)
- Chunk: ordinal 3 — heading `How do I differentiate negative powers of x?` — sha256_16 `70639f070fcad765` — 1140 chars
- Evidence quote (verbatim self-slice, markdown-safe): "How do I differentiate negative powers of x?
- The** same rules** apply to negative powers, $y=x^{n}$ becomes $\frac{dy}{dx}=nx^{n-1}$

  - Be careful: subtracting 1 from a negative power creates a **larger negative** number!
  
    - E.g. "
- Chunk excerpt: «How do I differentiate negative powers of x? - The** same rules** apply to negative powers, $y=x^{n}$ becomes $\frac{dy}{dx}=nx^{n-1}$ - Be careful: subtracting 1 from a negative power creates a **larger negative** number! - E.g. $y=x^{-3}$ becomes $\frac{dy}{dx}=-3x^{-3-1}=-3x^{-4}$ - You may need to use** index laws **to convert **algebraic fractions** into **negative powers** (and vice versa) - For example - $y=\f»
- Upstream: T-C32 join notes/3-sequences-functions-and-graphs/differentiation/differentiation.json::spcpt_fGGbSYFZH9DW4sgm — tier S1_name_match — score 0.6805 — wording EXACT — validation tier AI_VALIDATED (operator-delegated chain)
- Rationale: SME span 'Differentiation' on note 'Differentiation' is anchored by the corpus spec_point block spcpt_fGGbSYFZH9DW4sgm and joined to 4MA1-3.4C via name_to_statement_join; this section chunk sits inside that span.
- Verdict: [ ] CONFIRM — this chunk belongs to this SP   [ ] REJECT — wrong chunk/SP   [ ] HOLD — needs rework

### 4MA1-5.2H — understand and use column vectors in translations
- Note: Translations (`notes/5-vectors-and-transformation-geometry/transformations/translations.json`)
- Chunk: ordinal 2 — heading `What is a translation?` — sha256_16 `2f760ed59f47821a` — 200 chars
- Evidence quote (verbatim self-slice, markdown-safe): "What is a translation?
- A **translation** **moves** a shape
- The **size** and **orientation** (which way up it is) of the shape **stays the same**

  - The** object **and** image **are** congruent**"
- Chunk excerpt: «What is a translation? - A **translation** **moves** a shape - The **size** and **orientation** (which way up it is) of the shape **stays the same** - The** object **and** image **are** congruent**»
- Upstream: T-C32 join notes/5-vectors-and-transformation-geometry/transformations/translations.json::spcpt_YQX35KWR6v8thX5T — tier S1_name_match — score 0.7574 — wording EXACT — validation tier AI_VALIDATED (operator-delegated chain)
- Rationale: SME span 'Translations' on note 'Translations' is anchored by the corpus spec_point block spcpt_YQX35KWR6v8thX5T and joined to 4MA1-5.2H via name_to_statement_join; this section chunk sits inside that span.
- Verdict: [ ] CONFIRM — this chunk belongs to this SP   [ ] REJECT — wrong chunk/SP   [ ] HOLD — needs rework

### 4MA1-2.7D — solve simultaneous equations in two unknowns, one equation being linear and the other being quadratic
- Note: Linear Simultaneous Equations (`notes/2-equations-formulae-and-identities/simultaneous-equations/linear.json`)
- Chunk: ordinal 2 — heading `How do I solve linear simultaneous equations by elimination?` — sha256_16 `a2a8533f2f33a4c6` — 1872 chars
- Evidence quote (verbatim self-slice, markdown-safe): "How do I solve linear simultaneous equations by elimination?
- **Elimination** removes one of the variables, *x *or *y*
- To eliminate the *x*'s from 3*x* + 2*y* = 11 and 2*x* - *y *= 5, make the number in front of the *x* (the **coefficien"
- Chunk excerpt: «How do I solve linear simultaneous equations by elimination? - **Elimination** removes one of the variables, *x *or *y* - To eliminate the *x*'s from 3*x* + 2*y* = 11 and 2*x* - *y *= 5, make the number in front of the *x* (the **coefficient**) in both equations the same (the sign may be different) - Multiply** every term** in the **first** equation **by 2** - 6*x* + 4*y* = 22 - Multiply **every term** in the **secon»
- Upstream: T-C32 join notes/2-equations-formulae-and-identities/simultaneous-equations/linear.json::spcpt_h5yjgd2WdgmJqHJM — tier S1_name_match — score 0.755 — wording EXACT — validation tier AI_VALIDATED (operator-delegated chain)
- Rationale: SME span 'Linear Simultaneous Equations' on note 'Linear Simultaneous Equations' is anchored by the corpus spec_point block spcpt_h5yjgd2WdgmJqHJM and joined to 4MA1-2.7D via name_to_statement_join; this section chunk sits inside that span.
- Verdict: [ ] CONFIRM — this chunk belongs to this SP   [ ] REJECT — wrong chunk/SP   [ ] HOLD — needs rework

### 4MA1-1.6G — use compound interest and depreciation
- Note: Depreciation (`notes/1-numbers-and-the-number-system/compound-interest-and-depreciation/depreciation.json`)
- Chunk: ordinal 0 — heading `Depreciation` — sha256_16 `88e93c4c0bae5e12` — 12 chars
- Evidence quote (verbatim self-slice, markdown-safe): "Depreciation"
- Chunk excerpt: «Depreciation»
- Upstream: T-C32 join notes/1-numbers-and-the-number-system/compound-interest-and-depreciation/depreciation.json::spcpt_rDHZfZ8PrdwXcT2y — tier S1_name_match — score 0.792 — wording EXACT — validation tier AI_VALIDATED (operator-delegated chain)
- Rationale: SME span 'Depreciation' on note 'Depreciation' is anchored by the corpus spec_point block spcpt_rDHZfZ8PrdwXcT2y and joined to 4MA1-1.6G via name_to_statement_join; this section chunk sits inside that span.
- Verdict: [ ] CONFIRM — this chunk belongs to this SP   [ ] REJECT — wrong chunk/SP   [ ] HOLD — needs rework

### 4MA1-1.7B — divide a quantity in a given ratio or ratios
- Note: Introduction to Ratios (`notes/1-numbers-and-the-number-system/ratio-toolkit/simple-ratio.json`)
- Chunk: ordinal 5 — heading `What is a simplified ratio?` — sha256_16 `081044cf9af3814b` — 437 chars
- Evidence quote (verbatim self-slice, markdown-safe): "What is a simplified ratio?
- **Simplifying a ratio** involves finding an **equivalent ratio** where the numbers involved are **smaller**

  - E.g. The ratio **45 : 30** is equivalent to **9 : 6**
- A ratio is in its **simplest form** when
"
- Chunk excerpt: «What is a simplified ratio? - **Simplifying a ratio** involves finding an **equivalent ratio** where the numbers involved are **smaller** - E.g. The ratio **45 : 30** is equivalent to **9 : 6** - A ratio is in its **simplest form** when - All of the values in the ratio are ***integers*** - There are no ***common factors*** between each of the values in the ratio - E.g. The simplest form of the ratio **45 : 30** is **»
- Upstream: T-C32 join notes/1-numbers-and-the-number-system/ratio-toolkit/simple-ratio.json::spcpt_qpSmD6yNY5t5GrW6 — tier S1_name_match — score 0.696 — wording EXACT — validation tier AI_VALIDATED (operator-delegated chain)
- Rationale: SME span 'Ratios' on note 'Introduction to Ratios' is anchored by the corpus spec_point block spcpt_qpSmD6yNY5t5GrW6 and joined to 4MA1-1.7B via name_to_statement_join; this section chunk sits inside that span.
- Verdict: [ ] CONFIRM — this chunk belongs to this SP   [ ] REJECT — wrong chunk/SP   [ ] HOLD — needs rework

### 4MA1-2.7B — solve quadratic equations by using the quadratic formula or completing the square
- Note: The Quadratic Formula (`notes/2-equations-formulae-and-identities/solving-quadratic-equations/quadratic-formula.json`)
- Chunk: ordinal 0 — heading `Quadratic formula` — sha256_16 `3418eac977731135` — 17 chars
- Evidence quote (verbatim self-slice, markdown-safe): "Quadratic formula"
- Chunk excerpt: «Quadratic formula»
- Upstream: T-C32 join notes/2-equations-formulae-and-identities/solving-quadratic-equations/quadratic-formula.json::spcpt_JRX7QS29KrY2hCCW — tier S1_name_match — score 0.7388 — wording EXACT — validation tier AI_VALIDATED (operator-delegated chain)
- Rationale: SME span 'Quadratic Formula' on note 'The Quadratic Formula' is anchored by the corpus spec_point block spcpt_JRX7QS29KrY2hCCW and joined to 4MA1-2.7B via name_to_statement_join; this section chunk sits inside that span.
- Verdict: [ ] CONFIRM — this chunk belongs to this SP   [ ] REJECT — wrong chunk/SP   [ ] HOLD — needs rework

### 4MA1-3.3I — recognise, generate points and plot graphs of linear and quadratic functions
- Note: Quadratic Graphs (`notes/3-sequences-functions-and-graphs/graphs-of-functions/quadratic-graphs.json`)
- Chunk: ordinal 5 — heading `How do I find the coordinates of the turning point using differentiation?` — sha256_16 `afa457a9045d2d5a` — 3970 chars
- Evidence quote (verbatim self-slice, markdown-safe): "How do I find the coordinates of the turning point using differentiation?
- The coordinates of the **turning point **(maximum/minimum) of a quadratic can be found through **differentiation**
- To find the coordinates of the turning point

 "
- Chunk excerpt: «How do I find the coordinates of the turning point using differentiation? - The coordinates of the **turning point **(maximum/minimum) of a quadratic can be found through **differentiation** - To find the coordinates of the turning point - Differentiate the quadratic equation $y=ax^{2}+bx+c$ - This will give you $\frac{dy}{dx}$ - Set $\frac{dy}{dx}=0$ and solve for $x$ - The solution will be the $x$-coordinate of the»
- Upstream: T-C32 join notes/3-sequences-functions-and-graphs/graphs-of-functions/quadratic-graphs.json::spcpt_76gVqdMN62jnrZg6 — tier S1_name_match — score 0.6967 — wording EXACT — validation tier AI_VALIDATED (operator-delegated chain)
- Rationale: SME span 'Quadratic Graphs' on note 'Quadratic Graphs' is anchored by the corpus spec_point block spcpt_76gVqdMN62jnrZg6 and joined to 4MA1-3.3I via name_to_statement_join; this section chunk sits inside that span.
- Verdict: [ ] CONFIRM — this chunk belongs to this SP   [ ] REJECT — wrong chunk/SP   [ ] HOLD — needs rework

### 4MA1-4.9B — find the perimeter of shapes made from triangles and rectangles
- Note: Perimeter (`notes/4-geometry-and-trigonometry/area-and-perimeter/perimeter.json`)
- Chunk: ordinal 2 — heading `How do I find the perimeter of a 2D shape?` — sha256_16 `be65ea69893d94c8` — 320 chars
- Evidence quote (verbatim self-slice, markdown-safe): "How do I find the perimeter of a 2D shape?
- **Add together** the **lengths** of all of the sides of the shape
- For any ***regular***** **2D shape, the perimeter will be the **number of sides**, multiplied by the **length of one side**

  "
- Chunk excerpt: «How do I find the perimeter of a 2D shape? - **Add together** the **lengths** of all of the sides of the shape - For any ***regular***** **2D shape, the perimeter will be the **number of sides**, multiplied by the **length of one side** - For example, the perimeter of a square of side length *x* cm will be 4*x* cm»
- Upstream: T-C32 join notes/4-geometry-and-trigonometry/area-and-perimeter/perimeter.json::spcpt_W2yYk784rNVZBxPh — tier S1_name_match — score 0.7 — wording EXACT — validation tier AI_VALIDATED (operator-delegated chain)
- Rationale: SME span 'Perimeter' on note 'Perimeter' is anchored by the corpus spec_point block spcpt_W2yYk784rNVZBxPh and joined to 4MA1-4.9B via name_to_statement_join; this section chunk sits inside that span.
- Verdict: [ ] CONFIRM — this chunk belongs to this SP   [ ] REJECT — wrong chunk/SP   [ ] HOLD — needs rework

### 4MA1-4.11B — understand that volumes of similar figures are in the ratio of the cube of corresponding sides
- Note: Scale (`notes/4-geometry-and-trigonometry/bearings-scale-drawing-and-constructions/scale.json`)
- Chunk: ordinal 2 — heading `Maps` — sha256_16 `119e66d117ae8f0c` — 4 chars
- Evidence quote (verbatim self-slice, markdown-safe): "Maps"
- Chunk excerpt: «Maps»
- Upstream: T-C32 join notes/4-geometry-and-trigonometry/bearings-scale-drawing-and-constructions/scale.json::spcpt_wnkGx4MqYbQSFdnb — tier S1_name_match — score 0.6711 — wording EXACT — validation tier AI_VALIDATED (operator-delegated chain)
- Rationale: SME span 'Maps' on note 'Scale' is anchored by the corpus spec_point block spcpt_wnkGx4MqYbQSFdnb and joined to 4MA1-4.11B via name_to_statement_join; this section chunk sits inside that span.
- Verdict: [ ] CONFIRM — this chunk belongs to this SP   [ ] REJECT — wrong chunk/SP   [ ] HOLD — needs rework

### 4MA1-3.4E — apply calculus to linear kinematics and to other simple practical problems
- Note: Using Differentiation for Kinematics (`notes/3-sequences-functions-and-graphs/differentiation/kinematics.json`)
- Chunk: ordinal 1 — heading `What does kinematics mean?` — sha256_16 `952b723e35ae0175` — 442 chars
- Evidence quote (verbatim self-slice, markdown-safe): "What does kinematics mean?
- **Kinematics **is the study of the **motion of an object**

  - It is a branch of Physics
- Objects are called **particles **

  - They are modelled as single moving **points**
- Over time, the particles move an"
- Chunk excerpt: «What does kinematics mean? - **Kinematics **is the study of the **motion of an object** - It is a branch of Physics - Objects are called **particles ** - They are modelled as single moving **points** - Over time, the particles move and - can be at different distances from a fixed **origin** (**displacement**) - can move with different speeds in different directions (v**elocity**) - can speed up or slow down (**accele»
- Upstream: T-C32 join notes/3-sequences-functions-and-graphs/differentiation/kinematics.json::spcpt_vYsrWKqpQDpSwnPj — tier S1_name_match — score 0.6952 — wording EXACT — validation tier AI_VALIDATED (operator-delegated chain)
- Rationale: SME span 'Kinematics' on note 'Using Differentiation for Kinematics' is anchored by the corpus spec_point block spcpt_vYsrWKqpQDpSwnPj and joined to 4MA1-3.4E via name_to_statement_join; this section chunk sits inside that span.
- Verdict: [ ] CONFIRM — this chunk belongs to this SP   [ ] REJECT — wrong chunk/SP   [ ] HOLD — needs rework

### 4MA1-2.7D — solve simultaneous equations in two unknowns, one equation being linear and the other being quadratic
- Note: Quadratic Simultaneous Equations (`notes/2-equations-formulae-and-identities/simultaneous-equations/quadratic.json`)
- Chunk: ordinal 0 — heading `Quadratic simultaneous equations` — sha256_16 `4964ed529a8cb999` — 32 chars
- Evidence quote (verbatim self-slice, markdown-safe): "Quadratic simultaneous equations"
- Chunk excerpt: «Quadratic simultaneous equations»
- Upstream: T-C32 join notes/2-equations-formulae-and-identities/simultaneous-equations/quadratic.json::spcpt_pGsqq7xcztBg59Yh — tier S1_name_match — score 0.7394 — wording EXACT — validation tier AI_VALIDATED (operator-delegated chain)
- Rationale: SME span 'Quadratic Simultaneous Equations' on note 'Quadratic Simultaneous Equations' is anchored by the corpus spec_point block spcpt_pGsqq7xcztBg59Yh and joined to 4MA1-2.7D via name_to_statement_join; this section chunk sits inside that span.
- Verdict: [ ] CONFIRM — this chunk belongs to this SP   [ ] REJECT — wrong chunk/SP   [ ] HOLD — needs rework

### 4MA1-2.7B — solve quadratic equations by using the quadratic formula or completing the square
- Note: Completing the Square (`notes/2-equations-formulae-and-identities/completing-the-square/completing-the-square.json`)
- Chunk: ordinal 0 — heading `Completing the square` — sha256_16 `2661517009028341` — 21 chars
- Evidence quote (verbatim self-slice, markdown-safe): "Completing the square"
- Chunk excerpt: «Completing the square»
- Upstream: T-C32 join notes/2-equations-formulae-and-identities/completing-the-square/completing-the-square.json::spcpt_9Stcxtj75Q3wpqJF — tier S1_name_match — score 0.7647 — wording EXACT — validation tier AI_VALIDATED (operator-delegated chain)
- Rationale: SME span 'Completing the Square' on note 'Completing the Square' is anchored by the corpus spec_point block spcpt_9Stcxtj75Q3wpqJF and joined to 4MA1-2.7B via name_to_statement_join; this section chunk sits inside that span.
- Verdict: [ ] CONFIRM — this chunk belongs to this SP   [ ] REJECT — wrong chunk/SP   [ ] HOLD — needs rework

### 4MA1-3.3I — recognise, generate points and plot graphs of linear and quadratic functions
- Note: Quadratic Graphs (`notes/3-sequences-functions-and-graphs/graphs-of-functions/quadratic-graphs.json`)
- Chunk: ordinal 0 — heading `Quadratic graphs` — sha256_16 `fad7921e79cb1166` — 16 chars
- Evidence quote (verbatim self-slice, markdown-safe): "Quadratic graphs"
- Chunk excerpt: «Quadratic graphs»
- Upstream: T-C32 join notes/3-sequences-functions-and-graphs/graphs-of-functions/quadratic-graphs.json::spcpt_76gVqdMN62jnrZg6 — tier S1_name_match — score 0.6967 — wording EXACT — validation tier AI_VALIDATED (operator-delegated chain)
- Rationale: SME span 'Quadratic Graphs' on note 'Quadratic Graphs' is anchored by the corpus spec_point block spcpt_76gVqdMN62jnrZg6 and joined to 4MA1-3.3I via name_to_statement_join; this section chunk sits inside that span.
- Verdict: [ ] CONFIRM — this chunk belongs to this SP   [ ] REJECT — wrong chunk/SP   [ ] HOLD — needs rework

### 4MA1-5.2H — understand and use column vectors in translations
- Note: Translations (`notes/5-vectors-and-transformation-geometry/transformations/translations.json`)
- Chunk: ordinal 4 — heading `How do I translate a shape?` — sha256_16 `c425bfbbd21a4cf5` — 1388 chars
- Evidence quote (verbatim self-slice, markdown-safe): "How do I translate a shape?
- **STEP 1** **Interpret** the translation vector

  - `open parentheses table row 3 row cell negative 1 end cell end table close parentheses`  means 3 to the **right** and 1 **down**
- **STEP 2**
**Move each ver"
- Chunk excerpt: «How do I translate a shape? - **STEP 1** **Interpret** the translation vector - `open parentheses table row 3 row cell negative 1 end cell end table close parentheses` means 3 to the **right** and 1 **down** - **STEP 2** **Move each vertex** on the **original object **according to the vector - **STEP 3** **Connect** the **new vertices** and label the **translated image** - It should look **identical** to the **origin»
- Upstream: T-C32 join notes/5-vectors-and-transformation-geometry/transformations/translations.json::spcpt_YQX35KWR6v8thX5T — tier S1_name_match — score 0.7574 — wording EXACT — validation tier AI_VALIDATED (operator-delegated chain)
- Rationale: SME span 'Translations' on note 'Translations' is anchored by the corpus spec_point block spcpt_YQX35KWR6v8thX5T and joined to 4MA1-5.2H via name_to_statement_join; this section chunk sits inside that span.
- Verdict: [ ] CONFIRM — this chunk belongs to this SP   [ ] REJECT — wrong chunk/SP   [ ] HOLD — needs rework

### 4MA1-3.3F — calculate the gradient of a straight line given the coordinates of two points
- Note: Conversion Graphs (`notes/3-sequences-functions-and-graphs/real-life-graphs/conversion-graphs.json`)
- Chunk: ordinal 3 — heading `How do I use a conversion graph that does not start at the origin?` — sha256_16 `b716dc1075f90ab7` — 2516 chars
- Evidence quote (verbatim self-slice, markdown-safe): "How do I use a conversion graph that does not start at the origin?
- Convert 100°F into Celsius using the conversion graph below

  - **Start** at 100°F on the ***y*****-axis**
  - Draw a** horizontal line** to the graph
  - Then a **vertic"
- Chunk excerpt: «How do I use a conversion graph that does not start at the origin? - Convert 100°F into Celsius using the conversion graph below - **Start** at 100°F on the ***y*****-axis** - Draw a** horizontal line** to the graph - Then a **vertical line** down to the *x*-axis - **Read off** the value - $\approx$37.5°C - Answers **between** 37°C and 38°C would be **accepted** - (The true answer is 37.8°C to 1 decimal place) - The »
- Upstream: T-C32 join notes/3-sequences-functions-and-graphs/real-life-graphs/conversion-graphs.json::spcpt_Nh8WWWGQxmJGVvvf — tier S1_name_match — score 0.803 — wording EXACT — validation tier AI_VALIDATED (operator-delegated chain)
- Rationale: SME span 'Conversion Graphs' on note 'Conversion Graphs' is anchored by the corpus spec_point block spcpt_Nh8WWWGQxmJGVvvf and joined to 4MA1-3.3F via name_to_statement_join; this section chunk sits inside that span.
- Verdict: [ ] CONFIRM — this chunk belongs to this SP   [ ] REJECT — wrong chunk/SP   [ ] HOLD — needs rework

### 4MA1-1.4E — find highest common factors (HCF) and lowest common multiples (LCM)
- Note: HCF & LCM (`notes/1-numbers-and-the-number-system/prime-factors-hcf-and-lcm/hcf-and-lcm.json`)
- Chunk: ordinal 8 — heading `How can I use a Venn diagram to find the lowest common multiple (LCM) of two numbers?` — sha256_16 `5745d340152470b1` — 950 chars
- Evidence quote (verbatim self-slice, markdown-safe): "How can I use a Venn diagram to find the lowest common multiple (LCM) of two numbers?
- Write each number as a **product of its prime factors**

  - 42 = 2×3×7 and 90 = 2×3×3×5
- Find the prime factors that are **common** to **both numbers*"
- Chunk excerpt: «How can I use a Venn diagram to find the lowest common multiple (LCM) of two numbers? - Write each number as a **product of its prime factors** - 42 = 2×3×7 and 90 = 2×3×3×5 - Find the prime factors that are **common** to **both numbers** and put these in the **centre of the Venn diagram** - 42 and 90 both have a prime factor of 2 - Put a 2 in the centre of the diagram - Although 3 appears twice in the prime factors »
- Upstream: T-C32 join notes/1-numbers-and-the-number-system/prime-factors-hcf-and-lcm/hcf-and-lcm.json::spcpt_bmqbWbZM8HXPwsFF — tier S1_name_match — score 0.6858 — wording EXACT — validation tier AI_VALIDATED (operator-delegated chain)
- Rationale: SME span 'Lowest Common Multiple (LCM)' on note 'HCF & LCM' is anchored by the corpus spec_point block spcpt_bmqbWbZM8HXPwsFF and joined to 4MA1-1.4E via name_to_statement_join; this section chunk sits inside that span.
- Verdict: [ ] CONFIRM — this chunk belongs to this SP   [ ] REJECT — wrong chunk/SP   [ ] HOLD — needs rework

### 4MA1-4.8E — understand and use the formula ab sin C for the area of a triangle
- Note: Area of a Triangle (`notes/4-geometry-and-trigonometry/sine-cosine-rule-and-area-of-triangles/area-of-a-triangle.json`)
- Chunk: ordinal 0 — heading `Area of a triangle` — sha256_16 `f67b0d966e2611e0` — 18 chars
- Evidence quote (verbatim self-slice, markdown-safe): "Area of a triangle"
- Chunk excerpt: «Area of a triangle»
- Upstream: T-C32 join notes/4-geometry-and-trigonometry/sine-cosine-rule-and-area-of-triangles/area-of-a-triangle.json::spcpt_djG6mt4Gk3T4wJwC — tier S1_name_match — score 0.7714 — wording EXACT — validation tier AI_VALIDATED (operator-delegated chain)
- Rationale: SME span 'Area of a Triangle' on note 'Area of a Triangle' is anchored by the corpus spec_point block spcpt_djG6mt4Gk3T4wJwC and joined to 4MA1-4.8E via name_to_statement_join; this section chunk sits inside that span.
- Verdict: [ ] CONFIRM — this chunk belongs to this SP   [ ] REJECT — wrong chunk/SP   [ ] HOLD — needs rework

### 4MA1-2.7D — solve simultaneous equations in two unknowns, one equation being linear and the other being quadratic
- Note: Linear Simultaneous Equations (`notes/2-equations-formulae-and-identities/simultaneous-equations/linear.json`)
- Chunk: ordinal 1 — heading `What are linear simultaneous equations?` — sha256_16 `8f6d55d893ee23e8` — 392 chars
- Evidence quote (verbatim self-slice, markdown-safe): "What are linear simultaneous equations?
- When there are **two unknowns** (***x***** and *****y***), we need **two equations** to find them both

  - For example, 3*x *+ 2*y* = 11 and 2*x* - *y *= 5
  
    - The values that work are *x* = 3"
- Chunk excerpt: «What are linear simultaneous equations? - When there are **two unknowns** (***x***** and *****y***), we need **two equations** to find them both - For example, 3*x *+ 2*y* = 11 and 2*x* - *y *= 5 - The values that work are *x* = 3 and *y* = 1 - These are called **linear** **simultaneous equations** - **Linear **because there are no terms like *x*<sup>2</sup> or *y*<sup>2</sup>»
- Upstream: T-C32 join notes/2-equations-formulae-and-identities/simultaneous-equations/linear.json::spcpt_h5yjgd2WdgmJqHJM — tier S1_name_match — score 0.755 — wording EXACT — validation tier AI_VALIDATED (operator-delegated chain)
- Rationale: SME span 'Linear Simultaneous Equations' on note 'Linear Simultaneous Equations' is anchored by the corpus spec_point block spcpt_h5yjgd2WdgmJqHJM and joined to 4MA1-2.7D via name_to_statement_join; this section chunk sits inside that span.
- Verdict: [ ] CONFIRM — this chunk belongs to this SP   [ ] REJECT — wrong chunk/SP   [ ] HOLD — needs rework

### 4MA1-3.4E — apply calculus to linear kinematics and to other simple practical problems
- Note: Using Differentiation for Kinematics (`notes/3-sequences-functions-and-graphs/differentiation/kinematics.json`)
- Chunk: ordinal 5 — heading `What is the acceleration and how do I find it?` — sha256_16 `d2db19aa8ecb48a2` — 711 chars
- Evidence quote (verbatim self-slice, markdown-safe): "What is the acceleration and how do I find it?
- **Acceleration **is **rate** at which the **velocity changes**

  - It is **positive** if speeding up (when moving forwards)
  - It is** negative** if slowing down (when moving forwards)
  
 "
- Chunk excerpt: «What is the acceleration and how do I find it? - **Acceleration **is **rate** at which the **velocity changes** - It is **positive** if speeding up (when moving forwards) - It is** negative** if slowing down (when moving forwards) - A **negative** acceleration is also called a** deceleration** - The **magnitude of acceleration** is always** positive** - To find the **acceleration **of an object, $a$ metres per second»
- Upstream: T-C32 join notes/3-sequences-functions-and-graphs/differentiation/kinematics.json::spcpt_vYsrWKqpQDpSwnPj — tier S1_name_match — score 0.6952 — wording EXACT — validation tier AI_VALIDATED (operator-delegated chain)
- Rationale: SME span 'Kinematics' on note 'Using Differentiation for Kinematics' is anchored by the corpus spec_point block spcpt_vYsrWKqpQDpSwnPj and joined to 4MA1-3.4E via name_to_statement_join; this section chunk sits inside that span.
- Verdict: [ ] CONFIRM — this chunk belongs to this SP   [ ] REJECT — wrong chunk/SP   [ ] HOLD — needs rework

### 4MA1-6.2B — understand the concept of a measure of spread
- Note: Mean, Median & Mode (`notes/6-statistics-and-probability/statistics-toolkit/mean-median-and-mode.json`)
- Chunk: ordinal 2 — heading `What is the median?` — sha256_16 `b8b9fe97888a1717` — 477 chars
- Evidence quote (verbatim self-slice, markdown-safe): "What is the median?
- The** median** is the **middle **value when you put values** in size order**

  - The median of 4, 2, 3 can be found by
  
    - ordering the numbers: 2, 3, 4
    - and choosing the middle value, 3
- If you have an **e"
- Chunk excerpt: «What is the median? - The** median** is the **middle **value when you put values** in size order** - The median of 4, 2, 3 can be found by - ordering the numbers: 2, 3, 4 - and choosing the middle value, 3 - If you have an **even** number of values, find the **midpoint **of the **middle two** values - The median of 1, 2, 3, 4 is 2.5 - 2.5 is the midpoint of 2 and 3 - The **midpoint** is the **sum** of the **two middl»
- Upstream: T-C32 join notes/6-statistics-and-probability/statistics-toolkit/mean-median-and-mode.json::spcpt_myNYhxstM7xnZd9P — tier S1_name_match — score 0.76 — wording EXACT — validation tier AI_VALIDATED (operator-delegated chain)
- Rationale: SME span 'Mean, Median & Mode' on note 'Mean, Median & Mode' is anchored by the corpus spec_point block spcpt_myNYhxstM7xnZd9P and joined to 4MA1-6.2B via name_to_statement_join; this section chunk sits inside that span.
- Verdict: [ ] CONFIRM — this chunk belongs to this SP   [ ] REJECT — wrong chunk/SP   [ ] HOLD — needs rework

### 4MA1-2.7D — solve simultaneous equations in two unknowns, one equation being linear and the other being quadratic
- Note: Quadratic Simultaneous Equations (`notes/2-equations-formulae-and-identities/simultaneous-equations/quadratic.json`)
- Chunk: ordinal 3 — heading `How do I solve quadratic simultaneous equations using algebra?` — sha256_16 `24d3701d8f091169` — 1502 chars
- Evidence quote (verbatim self-slice, markdown-safe): "How do I solve quadratic simultaneous equations using algebra?
- Use** substitution**

  - **Substitute** the** linear** equation, *y* = ... (or *x* = ...), into the quadratic equation
  
    - Do not try to substitute the quadratic equatio"
- Chunk excerpt: «How do I solve quadratic simultaneous equations using algebra? - Use** substitution** - **Substitute** the** linear** equation, *y* = ... (or *x* = ...), into the quadratic equation - Do not try to substitute the quadratic equation into the linear equation - E.g. To solve $x^{2}+y^{2}=25$ and $y-2x=5$ - **Rearrange** the **linear** equation into $y=2x+5$ - **Substitute** this into the quadratic equation, replacing al»
- Upstream: T-C32 join notes/2-equations-formulae-and-identities/simultaneous-equations/quadratic.json::spcpt_pGsqq7xcztBg59Yh — tier S1_name_match — score 0.7394 — wording EXACT — validation tier AI_VALIDATED (operator-delegated chain)
- Rationale: SME span 'Quadratic Simultaneous Equations' on note 'Quadratic Simultaneous Equations' is anchored by the corpus spec_point block spcpt_pGsqq7xcztBg59Yh and joined to 4MA1-2.7D via name_to_statement_join; this section chunk sits inside that span.
- Verdict: [ ] CONFIRM — this chunk belongs to this SP   [ ] REJECT — wrong chunk/SP   [ ] HOLD — needs rework

### 4MA1-4.2D — understand the term ‘regular polygon’ and calculate interior and exterior angles of regular polygons
- Note: Angles in Polygons (`notes/4-geometry-and-trigonometry/angles-in-polygons-and-parallel-lines/angles-in-polygons.json`)
- Chunk: ordinal 6 — heading `How do I find a missing angle in a polygon?` — sha256_16 `9a6336e07cb76db0` — 287 chars
- Evidence quote (verbatim self-slice, markdown-safe): "How do I find a missing angle in a polygon?
- To find a **missing angle** in a polygon:

  - Use the formula `180 degree cross times open parentheses n minus 2 close parentheses` to work out the** sum** of the interior angles
  - **Subtract"
- Chunk excerpt: «How do I find a missing angle in a polygon? - To find a **missing angle** in a polygon: - Use the formula `180 degree cross times open parentheses n minus 2 close parentheses` to work out the** sum** of the interior angles - **Subtract** the **other interior angles** in the polygon»
- Upstream: T-C32 join notes/4-geometry-and-trigonometry/angles-in-polygons-and-parallel-lines/angles-in-polygons.json::spcpt_gzykj64JBx2RtBJ7 — tier S2_name_ambiguous — score 0.7085 — wording EXACT — validation tier AI_VALIDATED (operator-delegated chain)
- Rationale: SME span 'Angles in Polygons' on note 'Angles in Polygons' is anchored by the corpus spec_point block spcpt_gzykj64JBx2RtBJ7 and joined to 4MA1-4.2D via name_to_statement_join; this section chunk sits inside that span.
- Verdict: [ ] CONFIRM — this chunk belongs to this SP   [ ] REJECT — wrong chunk/SP   [ ] HOLD — needs rework

### 4MA1-5.2A — understand that rotations are specified by a centre and an angle
- Note: Rotations (`notes/5-vectors-and-transformation-geometry/transformations/rotations.json`)
- Chunk: ordinal 3 — heading `How do I describe a rotation?` — sha256_16 `67b83666f7daa236` — 981 chars
- Evidence quote (verbatim self-slice, markdown-safe): "How do I describe a rotation?
- To describe a **rotation**, you must:

  - State that the transformation is a **rotation**
  - State the **centre of rotation**
  - State the **angle of rotation**
  
    - This will be 90°, 180° or 270°
  - "
- Chunk excerpt: «How do I describe a rotation? - To describe a **rotation**, you must: - State that the transformation is a **rotation** - State the **centre of rotation** - State the **angle of rotation** - This will be 90°, 180° or 270° - State the **direction of rotation** - Clockwise or anti-clockwise - A direction is not required if the angle is 180° - 90° clockwise is the same as 270° anti-clockwise - To find the **centre of ro»
- Upstream: T-C32 join notes/5-vectors-and-transformation-geometry/transformations/rotations.json::spcpt_N5xf2wmr4yCNxHBj — tier S1_name_match — score 0.6986 — wording EXACT — validation tier AI_VALIDATED (operator-delegated chain)
- Rationale: SME span 'Rotations' on note 'Rotations' is anchored by the corpus spec_point block spcpt_N5xf2wmr4yCNxHBj and joined to 4MA1-5.2A via name_to_statement_join; this section chunk sits inside that span.
- Verdict: [ ] CONFIRM — this chunk belongs to this SP   [ ] REJECT — wrong chunk/SP   [ ] HOLD — needs rework

### 4MA1-4.9B — find the perimeter of shapes made from triangles and rectangles
- Note: Perimeter (`notes/4-geometry-and-trigonometry/area-and-perimeter/perimeter.json`)
- Chunk: ordinal 3 — heading `How do I find the perimeter of a compound shape?` — sha256_16 `180988e796cac3b3` — 2061 chars
- Evidence quote (verbatim self-slice, markdown-safe): "How do I find the perimeter of a compound shape?
- Shapes may be made up of two or more 2D shapes, these are called **compound shapes**

  - Compound shapes can usually be split into** rectangles**, **triangles **and** parts of circles**
  "
- Chunk excerpt: «How do I find the perimeter of a compound shape? - Shapes may be made up of two or more 2D shapes, these are called **compound shapes** - Compound shapes can usually be split into** rectangles**, **triangles **and** parts of circles** - You will need to be confident with the **properties of 2D shapes** - For example, the distance between the** centre point **of a** circle **and a** **point on the** circumference **is»
- Upstream: T-C32 join notes/4-geometry-and-trigonometry/area-and-perimeter/perimeter.json::spcpt_W2yYk784rNVZBxPh — tier S1_name_match — score 0.7 — wording EXACT — validation tier AI_VALIDATED (operator-delegated chain)
- Rationale: SME span 'Perimeter' on note 'Perimeter' is anchored by the corpus spec_point block spcpt_W2yYk784rNVZBxPh and joined to 4MA1-4.9B via name_to_statement_join; this section chunk sits inside that span.
- Verdict: [ ] CONFIRM — this chunk belongs to this SP   [ ] REJECT — wrong chunk/SP   [ ] HOLD — needs rework

### 4MA1-4.11B — understand that volumes of similar figures are in the ratio of the cube of corresponding sides
- Note: Scale (`notes/4-geometry-and-trigonometry/bearings-scale-drawing-and-constructions/scale.json`)
- Chunk: ordinal 3 — heading `How can I use a scale to find the actual lengths from a map?` — sha256_16 `62927078f3d6bf26` — 1830 chars
- Evidence quote (verbatim self-slice, markdown-safe): "How can I use a scale to find the actual lengths from a map?
- A map can be used to calculate the real-life distances between points
- **STEP 1**
Use a ruler to **measure** the **distance accurately** on the **map**

  - For example, measur"
- Chunk excerpt: «How can I use a scale to find the actual lengths from a map? - A map can be used to calculate the real-life distances between points - **STEP 1** Use a ruler to **measure** the **distance accurately** on the **map** - For example, measuring a length from A to B as 5.8 cm - **STEP 2** Use the **scale** to find the **actual distance** in the **same units** - For example, if the scale is 1 : 150 000 the actual distance »
- Upstream: T-C32 join notes/4-geometry-and-trigonometry/bearings-scale-drawing-and-constructions/scale.json::spcpt_wnkGx4MqYbQSFdnb — tier S1_name_match — score 0.6711 — wording EXACT — validation tier AI_VALIDATED (operator-delegated chain)
- Rationale: SME span 'Maps' on note 'Scale' is anchored by the corpus spec_point block spcpt_wnkGx4MqYbQSFdnb and joined to 4MA1-4.11B via name_to_statement_join; this section chunk sits inside that span.
- Verdict: [ ] CONFIRM — this chunk belongs to this SP   [ ] REJECT — wrong chunk/SP   [ ] HOLD — needs rework

### 4MA1-6.1C — use cumulative frequency diagrams
- Note: Reading & Interpreting Statistical Diagrams (`notes/6-statistics-and-probability/statistics-toolkit/working-with-statistical-diagrams.json`)
- Chunk: ordinal 2 — heading `How do I draw conclusions from diagrams?` — sha256_16 `a4ec532ceb469ef2` — 2609 chars
- Evidence quote (verbatim self-slice, markdown-safe): "How do I draw conclusions from diagrams?
- Look for **overall trends** in the diagram

  - Prices **increase **year on year
  - The temperature **peaks** in June
- Use** numbers** from the graphs
- Refer to any **changes**

  - The **steepn"
- Chunk excerpt: «How do I draw conclusions from diagrams? - Look for **overall trends** in the diagram - Prices **increase **year on year - The temperature **peaks** in June - Use** numbers** from the graphs - Refer to any **changes** - The **steepness** (gradient) of graph may change - Write in **full sentences** that copy the **exact wording** from the question - 'The number of goats in farm A has decreased by 12 over the 8 month p»
- Upstream: T-C32 join notes/6-statistics-and-probability/statistics-toolkit/working-with-statistical-diagrams.json::spcpt_bGtx4SMcX6BRS6KP — tier S1_name_match — score 0.638 — wording EXACT — validation tier AI_VALIDATED (operator-delegated chain)
- Rationale: SME span 'Reading & Interpreting Statistical Diagrams' on note 'Reading & Interpreting Statistical Diagrams' is anchored by the corpus spec_point block spcpt_bGtx4SMcX6BRS6KP and joined to 4MA1-6.1C via name_to_statement_join; this section chunk sits inside that span.
- Verdict: [ ] CONFIRM — this chunk belongs to this SP   [ ] REJECT — wrong chunk/SP   [ ] HOLD — needs rework

### 4MA1-2.5A — set up problems involving direct or inverse proportion and relate algebraic solutions to graphical representation of the equations
- Note: Inverse Proportion (`notes/1-numbers-and-the-number-system/direct-and-inverse-proportion/inverse-proportion.json`)
- Chunk: ordinal 1 — heading `What is inverse proportion?` — sha256_16 `6b91fef9d2a9be35` — 763 chars
- Evidence quote (verbatim self-slice, markdown-safe): "What is inverse proportion?
- **Inverse** proportion means as **one variable goes up** the **other goes** **down** by the same **factor**

  - If two quantities are **inversely proportional**, then we can say that one is **directly proporti"
- Chunk excerpt: «What is inverse proportion? - **Inverse** proportion means as **one variable goes up** the **other goes** **down** by the same **factor** - If two quantities are **inversely proportional**, then we can say that one is **directly proportional **to the **reciprocal** of the other - The symbol, $\propto$, is used to show that one quantity is "directly proportional to the reciprocal of" (inversely proportional to) anothe»
- Upstream: T-C32 join notes/1-numbers-and-the-number-system/direct-and-inverse-proportion/inverse-proportion.json::spcpt_b7HzYMMwjGWQSz77 — tier S1_name_match — score 0.6973 — wording EXACT — validation tier AI_VALIDATED (operator-delegated chain)
- Rationale: SME span 'Inverse Proportion' on note 'Inverse Proportion' is anchored by the corpus spec_point block spcpt_b7HzYMMwjGWQSz77 and joined to 4MA1-2.5A via name_to_statement_join; this section chunk sits inside that span.
- Verdict: [ ] CONFIRM — this chunk belongs to this SP   [ ] REJECT — wrong chunk/SP   [ ] HOLD — needs rework

### 4MA1-4.11A — understand that areas of similar figures are in the ratio of the square of corresponding sides
- Note: Similar Lengths (`notes/4-geometry-and-trigonometry/congruence-similarity-and-geometrical-proof/similar-lengths.json`)
- Chunk: ordinal 2 — heading `How do I find missing lengths on similar shapes?` — sha256_16 `382f78e821f97b46` — 48 chars
- Evidence quote (verbatim self-slice, markdown-safe): "How do I find missing lengths on similar shapes?"
- Chunk excerpt: «How do I find missing lengths on similar shapes?»
- Upstream: T-C32 join notes/4-geometry-and-trigonometry/congruence-similarity-and-geometrical-proof/similar-lengths.json::spcpt_xDpKVBxDTCk2x6vS — tier S1_name_match — score 0.6714 — wording EXACT — validation tier AI_VALIDATED (operator-delegated chain)
- Rationale: SME span 'Similar Lengths' on note 'Similar Lengths' is anchored by the corpus spec_point block spcpt_xDpKVBxDTCk2x6vS and joined to 4MA1-4.11A via name_to_statement_join; this section chunk sits inside that span.
- Verdict: [ ] CONFIRM — this chunk belongs to this SP   [ ] REJECT — wrong chunk/SP   [ ] HOLD — needs rework

### 4MA1-4.3A — identify any lines of symmetry and the order of rotational symmetry of a given two-dimensional figure
- Note: Rotational Symmetry (`notes/4-geometry-and-trigonometry/congruence-similarity-and-geometrical-proof/symmetry.json`)
- Chunk: ordinal 0 — heading `Rotational symmetry` — sha256_16 `31c124599c91ba33` — 19 chars
- Evidence quote (verbatim self-slice, markdown-safe): "Rotational symmetry"
- Chunk excerpt: «Rotational symmetry»
- Upstream: T-C32 join notes/4-geometry-and-trigonometry/congruence-similarity-and-geometrical-proof/symmetry.json::spcpt_7gdmq8MbcShywrkB — tier S1_name_match — score 0.7267 — wording EXACT — validation tier AI_VALIDATED (operator-delegated chain)
- Rationale: SME span 'Rotational Symmetry' on note 'Rotational Symmetry' is anchored by the corpus spec_point block spcpt_7gdmq8MbcShywrkB and joined to 4MA1-4.3A via name_to_statement_join; this section chunk sits inside that span.
- Verdict: [ ] CONFIRM — this chunk belongs to this SP   [ ] REJECT — wrong chunk/SP   [ ] HOLD — needs rework

### 4MA1-4.2D — understand the term ‘regular polygon’ and calculate interior and exterior angles of regular polygons
- Note: Angles in Polygons (`notes/4-geometry-and-trigonometry/angles-in-polygons-and-parallel-lines/angles-in-polygons.json`)
- Chunk: ordinal 1 — heading `What is a polygon?` — sha256_16 `b1914d417dbfaec4` — 467 chars
- Evidence quote (verbatim self-slice, markdown-safe): "What is a polygon?
- A **polygon** is a 2D shape with $n$* *straight sides

  - A **triangle** is a polygon with **3 sides**
  - A **quadrilateral** is a polygon with **4 sides**
  - A **pentagon** is a polygon with **5 sides**
- In a **reg"
- Chunk excerpt: «What is a polygon? - A **polygon** is a 2D shape with $n$* *straight sides - A **triangle** is a polygon with **3 sides** - A **quadrilateral** is a polygon with **4 sides** - A **pentagon** is a polygon with **5 sides** - In a **regular** polygon **all the sides are the same length** and a**ll the angles are the same size** - A **regular polygon** with **3 sides** is an **equilateral triangle** - A **regular polygon»
- Upstream: T-C32 join notes/4-geometry-and-trigonometry/angles-in-polygons-and-parallel-lines/angles-in-polygons.json::spcpt_gzykj64JBx2RtBJ7 — tier S2_name_ambiguous — score 0.7085 — wording EXACT — validation tier AI_VALIDATED (operator-delegated chain)
- Rationale: SME span 'Angles in Polygons' on note 'Angles in Polygons' is anchored by the corpus spec_point block spcpt_gzykj64JBx2RtBJ7 and joined to 4MA1-4.2D via name_to_statement_join; this section chunk sits inside that span.
- Verdict: [ ] CONFIRM — this chunk belongs to this SP   [ ] REJECT — wrong chunk/SP   [ ] HOLD — needs rework

### 4MA1-3.3B — apply to the graph ofy = f(x)the transformations y = f(x) + a, y = f(ax), y = f(x + a), y = af(x) for linear, quadratic, sine and cosine functions
- Note: 2D Coordinates (`notes/3-sequences-functions-and-graphs/coordinate-geometry/coordinates.json`)
- Chunk: ordinal 2 — heading `What are coordinates?` — sha256_16 `24b733977f22c40c` — 1606 chars
- Evidence quote (verbatim self-slice, markdown-safe): "What are coordinates?
- **Coordinates** are a** pair **of **numbers**, *x * and *y *, that describe the** location** of a **point **on the grid

  - They are written in **brackets** as **(*****x *****, *****y *****)**
  - The point is
  
  "
- Chunk excerpt: «What are coordinates? - **Coordinates** are a** pair **of **numbers**, *x * and *y *, that describe the** location** of a **point **on the grid - They are written in **brackets** as **(*****x *****, *****y *****)** - The point is - ***x ***** units **on the **horizontal** scale - ***y***** units **on the **vertical **scale - The **origin** is **(0, 0)** - **Positive** values of ***x **** *are to the **right** of the »
- Upstream: T-C32 join notes/3-sequences-functions-and-graphs/coordinate-geometry/coordinates.json::spcpt_Jw35TTKhvXxmGGfP — tier S2_name_ambiguous — score 0.7268 — wording EXACT — validation tier AI_VALIDATED (operator-delegated chain)
- Rationale: SME span '2D Coordinates' on note '2D Coordinates' is anchored by the corpus spec_point block spcpt_Jw35TTKhvXxmGGfP and joined to 4MA1-3.3B via name_to_statement_join; this section chunk sits inside that span.
- Verdict: [ ] CONFIRM — this chunk belongs to this SP   [ ] REJECT — wrong chunk/SP   [ ] HOLD — needs rework

### 4MA1-1.4E — find highest common factors (HCF) and lowest common multiples (LCM)
- Note: HCF & LCM (`notes/1-numbers-and-the-number-system/prime-factors-hcf-and-lcm/hcf-and-lcm.json`)
- Chunk: ordinal 2 — heading `How do I find the highest common factor (HCF) of two numbers?` — sha256_16 `14f3cc02e43f0256` — 296 chars
- Evidence quote (verbatim self-slice, markdown-safe): "How do I find the highest common factor (HCF) of two numbers?
- To find **common factors**:

  - write out the **factors** of each number in a list
  - identify the numbers that appear in** both **lists
- The **highest **common factor will "
- Chunk excerpt: «How do I find the highest common factor (HCF) of two numbers? - To find **common factors**: - write out the **factors** of each number in a list - identify the numbers that appear in** both **lists - The **highest **common factor will be the **largest factor** that appears in **both **lists»
- Upstream: T-C32 join notes/1-numbers-and-the-number-system/prime-factors-hcf-and-lcm/hcf-and-lcm.json::spcpt_P88yS9wysymQ2brq — tier S1_name_match — score 0.6798 — wording EXACT — validation tier AI_VALIDATED (operator-delegated chain)
- Rationale: SME span 'Highest Common Factor (HCF)' on note 'HCF & LCM' is anchored by the corpus spec_point block spcpt_P88yS9wysymQ2brq and joined to 4MA1-1.4E via name_to_statement_join; this section chunk sits inside that span.
- Verdict: [ ] CONFIRM — this chunk belongs to this SP   [ ] REJECT — wrong chunk/SP   [ ] HOLD — needs rework

### 4MA1-5.2K — understand that enlargements preserve angles and not lengths
- Note: Enlargements (`notes/5-vectors-and-transformation-geometry/transformations/enlargements.json`)
- Chunk: ordinal 2 — heading `How do I enlarge a shape?` — sha256_16 `8c989e7c4003cbac` — 742 chars
- Evidence quote (verbatim self-slice, markdown-safe): "How do I enlarge a shape?
- **STEP 1** Pick a **vertex** of the shape and count the **horizontal and vertical distances** from the **centre of enlargement**
- **STEP 2**
Multiply **both** the horizontal and vertical distances by the given *"
- Chunk excerpt: «How do I enlarge a shape? - **STEP 1** Pick a **vertex** of the shape and count the **horizontal and vertical distances** from the **centre of enlargement** - **STEP 2** Multiply **both** the horizontal and vertical distances by the given **scale factor** - **STEP 3** **Start at the centre of enlargement** and **measure the new distances** to find the **enlarged vertex** - **STEP 4** **Repeat **the steps for the **ot»
- Upstream: T-C32 join notes/5-vectors-and-transformation-geometry/transformations/enlargements.json::spcpt_c3ZTz62W4HKyb4zk — tier S2_name_ambiguous — score 0.7333 — wording EXACT — validation tier AI_VALIDATED (operator-delegated chain)
- Rationale: SME span 'Enlargements' on note 'Enlargements' is anchored by the corpus spec_point block spcpt_c3ZTz62W4HKyb4zk and joined to 4MA1-5.2K via name_to_statement_join; this section chunk sits inside that span.
- Verdict: [ ] CONFIRM — this chunk belongs to this SP   [ ] REJECT — wrong chunk/SP   [ ] HOLD — needs rework

### 4MA1-4.1B — use angle properties of intersecting lines, parallel lines and angles on a straight line
- Note: Angles in Parallel Lines (`notes/4-geometry-and-trigonometry/angles-in-polygons-and-parallel-lines/angles-in-parallel-lines.json`)
- Chunk: ordinal 1 — heading `What are parallel lines?` — sha256_16 `eb87db0ffa7b7edd` — 286 chars
- Evidence quote (verbatim self-slice, markdown-safe): "What are parallel lines?
- Parallel lines are lines that are always **equidistant **(the same distance apart)

  - No matter how far the lines are extended in either direction, they will **never meet**
- **Angles** are formed when a **strai"
- Chunk excerpt: «What are parallel lines? - Parallel lines are lines that are always **equidistant **(the same distance apart) - No matter how far the lines are extended in either direction, they will **never meet** - **Angles** are formed when a **straight line** cuts through **two parallel lines**»
- Upstream: T-C32 join notes/4-geometry-and-trigonometry/angles-in-polygons-and-parallel-lines/angles-in-parallel-lines.json::spcpt_2SfTVFKHJRBby3QK — tier S1_name_match — score 0.773 — wording EXACT — validation tier AI_VALIDATED (operator-delegated chain)
- Rationale: SME span 'Angles in Parallel Lines' on note 'Angles in Parallel Lines' is anchored by the corpus spec_point block spcpt_2SfTVFKHJRBby3QK and joined to 4MA1-4.1B via name_to_statement_join; this section chunk sits inside that span.
- Verdict: [ ] CONFIRM — this chunk belongs to this SP   [ ] REJECT — wrong chunk/SP   [ ] HOLD — needs rework

### 4MA1-5.2K — understand that enlargements preserve angles and not lengths
- Note: Enlargements (`notes/5-vectors-and-transformation-geometry/transformations/enlargements.json`)
- Chunk: ordinal 1 — heading `What is an enlargement?` — sha256_16 `912337acc5ca46e9` — 777 chars
- Evidence quote (verbatim self-slice, markdown-safe): "What is an enlargement?
- An **enlargement** **changes** the **size **and **position **of a shape
- The **length of each side** of the shape is **multiplied** by a **scale factor**

  - If the scale factor is **greater than 1 **then the **e"
- Chunk excerpt: «What is an enlargement? - An **enlargement** **changes** the **size **and **position **of a shape - The **length of each side** of the shape is **multiplied** by a **scale factor** - If the scale factor is **greater than 1 **then the **enlarged image** will be **bigger** than the** original object** - If the scale factor is **between 0 and 1 (fractional) **then the **enlarged image** will be **smaller** than the **or»
- Upstream: T-C32 join notes/5-vectors-and-transformation-geometry/transformations/enlargements.json::spcpt_c3ZTz62W4HKyb4zk — tier S2_name_ambiguous — score 0.7333 — wording EXACT — validation tier AI_VALIDATED (operator-delegated chain)
- Rationale: SME span 'Enlargements' on note 'Enlargements' is anchored by the corpus spec_point block spcpt_c3ZTz62W4HKyb4zk and joined to 4MA1-5.2K via name_to_statement_join; this section chunk sits inside that span.
- Verdict: [ ] CONFIRM — this chunk belongs to this SP   [ ] REJECT — wrong chunk/SP   [ ] HOLD — needs rework

### 4MA1-4.11A — understand that areas of similar figures are in the ratio of the square of corresponding sides
- Note: Similar Lengths (`notes/4-geometry-and-trigonometry/congruence-similarity-and-geometrical-proof/similar-lengths.json`)
- Chunk: ordinal 4 — heading `Method 2` — sha256_16 `b27a0812afdaa012` — 2442 chars
- Evidence quote (verbatim self-slice, markdown-safe): "Method 2
- **STEP 1**
Find the **scale factor **to get from the **smaller **shape to the **bigger **shape

  - **Divide **a length on the **bigger **shape by the corresponding length on the **smaller **shape
  - The scale factor is **always"
- Chunk excerpt: «Method 2 - **STEP 1** Find the **scale factor **to get from the **smaller **shape to the **bigger **shape - **Divide **a length on the **bigger **shape by the corresponding length on the **smaller **shape - The scale factor is **always greater than 1** for this method - **STEP 2** Use the scale factor to find the **length **you need - To find a missing length on the **bigger shape** - **Multiply **the corresponding l»
- Upstream: T-C32 join notes/4-geometry-and-trigonometry/congruence-similarity-and-geometrical-proof/similar-lengths.json::spcpt_xDpKVBxDTCk2x6vS — tier S1_name_match — score 0.6714 — wording EXACT — validation tier AI_VALIDATED (operator-delegated chain)
- Rationale: SME span 'Similar Lengths' on note 'Similar Lengths' is anchored by the corpus spec_point block spcpt_xDpKVBxDTCk2x6vS and joined to 4MA1-4.11A via name_to_statement_join; this section chunk sits inside that span.
- Verdict: [ ] CONFIRM — this chunk belongs to this SP   [ ] REJECT — wrong chunk/SP   [ ] HOLD — needs rework

### 4MA1-2.7B — solve quadratic equations by using the quadratic formula or completing the square
- Note: Solving by Completing the Square (`notes/2-equations-formulae-and-identities/solving-quadratic-equations/solving-by-completing-the-square.json`)
- Chunk: ordinal 0 — heading `Solving by completing the square` — sha256_16 `2d1475802f409cf3` — 32 chars
- Evidence quote (verbatim self-slice, markdown-safe): "Solving by completing the square"
- Chunk excerpt: «Solving by completing the square»
- Upstream: T-C32 join notes/2-equations-formulae-and-identities/solving-quadratic-equations/solving-by-completing-the-square.json::spcpt_W2v94nxskTtpWxWd — tier S1_name_match — score 0.6624 — wording EXACT — validation tier AI_VALIDATED (operator-delegated chain)
- Rationale: SME span 'Solving by Completing the Square' on note 'Solving by Completing the Square' is anchored by the corpus spec_point block spcpt_W2v94nxskTtpWxWd and joined to 4MA1-2.7B via name_to_statement_join; this section chunk sits inside that span.
- Verdict: [ ] CONFIRM — this chunk belongs to this SP   [ ] REJECT — wrong chunk/SP   [ ] HOLD — needs rework

### 4MA1-5.2D — understand that reflections are specified by a mirror line
- Note: Reflections (`notes/5-vectors-and-transformation-geometry/transformations/reflections.json`)
- Chunk: ordinal 4 — heading `How do I describe a reflection?` — sha256_16 `97d93e12aad69747` — 617 chars
- Evidence quote (verbatim self-slice, markdown-safe): "How do I describe a reflection?
- To describe a **reflection**, you must:

  - State that the transformation is a **reflection**
  - Give the mathematical **equation of the mirror line**
- To find the **equation** of the **reflection line**"
- Chunk excerpt: «How do I describe a reflection? - To describe a **reflection**, you must: - State that the transformation is a **reflection** - Give the mathematical **equation of the mirror line** - To find the **equation** of the **reflection line**: - **Horizontal** lines are of the form $y=k$ - $k$ is the number that the **line passes through on the y-axis** - **Vertical** lines are of the form $x=k$ - $k$ is the number that the»
- Upstream: T-C32 join notes/5-vectors-and-transformation-geometry/transformations/reflections.json::spcpt_DQrkJGG4Mngch9xc — tier S1_name_match — score 0.7275 — wording EXACT — validation tier AI_VALIDATED (operator-delegated chain)
- Rationale: SME span 'Reflections' on note 'Reflections' is anchored by the corpus spec_point block spcpt_DQrkJGG4Mngch9xc and joined to 4MA1-5.2D via name_to_statement_join; this section chunk sits inside that span.
- Verdict: [ ] CONFIRM — this chunk belongs to this SP   [ ] REJECT — wrong chunk/SP   [ ] HOLD — needs rework

### 4MA1-2.7B — solve quadratic equations by using the quadratic formula or completing the square
- Note: Solving by Completing the Square (`notes/2-equations-formulae-and-identities/solving-quadratic-equations/solving-by-completing-the-square.json`)
- Chunk: ordinal 3 — heading `How does completing the square link to the quadratic formula?` — sha256_16 `5ed3973252482616` — 1707 chars
- Evidence quote (verbatim self-slice, markdown-safe): "How does completing the square link to the quadratic formula?
- The **quadratic formula** actually comes from **completing the square** to solve *ax*<sup>2</sup> + *bx* + *c* = 0

  - *a*, *b* and *c* are left as letters when completing the"
- Chunk excerpt: «How does completing the square link to the quadratic formula? - The **quadratic formula** actually comes from **completing the square** to solve *ax*<sup>2</sup> + *bx* + *c* = 0 - *a*, *b* and *c* are left as letters when completing the square - This makes it as general as possible - You can see hints of this when you solve quadratics - For example, solving *x*<sup>2</sup> + 10*x* + 9 = 0 - by completing the square,»
- Upstream: T-C32 join notes/2-equations-formulae-and-identities/solving-quadratic-equations/solving-by-completing-the-square.json::spcpt_W2v94nxskTtpWxWd — tier S1_name_match — score 0.6624 — wording EXACT — validation tier AI_VALIDATED (operator-delegated chain)
- Rationale: SME span 'Solving by Completing the Square' on note 'Solving by Completing the Square' is anchored by the corpus spec_point block spcpt_W2v94nxskTtpWxWd and joined to 4MA1-2.7B via name_to_statement_join; this section chunk sits inside that span.
- Verdict: [ ] CONFIRM — this chunk belongs to this SP   [ ] REJECT — wrong chunk/SP   [ ] HOLD — needs rework

### 4MA1-3.4C — determine gradients, rates of change, stationary points, turning points (maxima and minima) by differentiation and relate these to graphs
- Note: Differentiation (`notes/3-sequences-functions-and-graphs/differentiation/differentiation.json`)
- Chunk: ordinal 4 — heading `How do I differentiate sums and differences of terms?` — sha256_16 `40b4ccb5eae3ebd4` — 1183 chars
- Evidence quote (verbatim self-slice, markdown-safe): "How do I differentiate sums and differences of terms?
- The equation of a curve may include a number of different terms

  - You can differentiate each term **individually**
  
    - Differentiating $y=x^{5}+x^{8}$ gives $\frac{dy}{dx}=5x^{"
- Chunk excerpt: «How do I differentiate sums and differences of terms? - The equation of a curve may include a number of different terms - You can differentiate each term **individually** - Differentiating $y=x^{5}+x^{8}$ gives $\frac{dy}{dx}=5x^{4}+8x^{7}$ - Differentiating $y=4x^{3}-10x^{6}$ gives $\frac{dy}{dx}=12x^{2}-60x^{5}$ - Remember the two special cases of: - $kx$ differentiating to just $k$ - and** constant **terms, $c$, d»
- Upstream: T-C32 join notes/3-sequences-functions-and-graphs/differentiation/differentiation.json::spcpt_fGGbSYFZH9DW4sgm — tier S1_name_match — score 0.6805 — wording EXACT — validation tier AI_VALIDATED (operator-delegated chain)
- Rationale: SME span 'Differentiation' on note 'Differentiation' is anchored by the corpus spec_point block spcpt_fGGbSYFZH9DW4sgm and joined to 4MA1-3.4C via name_to_statement_join; this section chunk sits inside that span.
- Verdict: [ ] CONFIRM — this chunk belongs to this SP   [ ] REJECT — wrong chunk/SP   [ ] HOLD — needs rework

### 4MA1-4.11C — use areas and volumes of similar figures in solving problems
- Note: Similar Areas & Volumes (`notes/4-geometry-and-trigonometry/area-and-volume-of-similar-shapes/similar-areas-and-volumes.json`)
- Chunk: ordinal 0 — heading `Similar areas & volumes` — sha256_16 `47a4b8da90feb981` — 23 chars
- Evidence quote (verbatim self-slice, markdown-safe): "Similar areas & volumes"
- Chunk excerpt: «Similar areas & volumes»
- Upstream: T-C32 join notes/4-geometry-and-trigonometry/area-and-volume-of-similar-shapes/similar-areas-and-volumes.json::spcpt_dBwfqg3wJvDp9PNs — tier S1_name_match — score 0.758 — wording EXACT — validation tier AI_VALIDATED (operator-delegated chain)
- Rationale: SME span 'Similar Areas & Volumes' on note 'Similar Areas & Volumes' is anchored by the corpus spec_point block spcpt_dBwfqg3wJvDp9PNs and joined to 4MA1-4.11C via name_to_statement_join; this section chunk sits inside that span.
- Verdict: [ ] CONFIRM — this chunk belongs to this SP   [ ] REJECT — wrong chunk/SP   [ ] HOLD — needs rework

### 4MA1-3.3G — find the equation of a straight line parallel to a given line; find the equation of a straight line perpendicular to a given line
- Note: Gradient of a Line (`notes/3-sequences-functions-and-graphs/coordinate-geometry/gradient-of-a-line.json`)
- Chunk: ordinal 3 — heading `How do I draw a line with a given gradient?` — sha256_16 `5634c2d1769aacde` — 1936 chars
- Evidence quote (verbatim self-slice, markdown-safe): "How do I draw a line with a given gradient?
- To draw the gradient $\frac{2}{3}$

  - The **rise** is 2
  - The **run** is 3
  - It is **positive** (uphill)
  
    - Move 3 units to the **right** and 2 units **up**
- To draw the gradient $-"
- Chunk excerpt: «How do I draw a line with a given gradient? - To draw the gradient $\frac{2}{3}$ - The **rise** is 2 - The **run** is 3 - It is **positive** (uphill) - Move 3 units to the **right** and 2 units **up** - To draw the gradient $-5$ make it a fraction, $-\frac{5}{1}$ - The **rise** is 5 - The **run** is 1 - It is **negative** (downhill) - Move 1 unit to the **right** and 5 units **down** Exam Hint: A lot of students forg»
- Upstream: T-C32 join notes/3-sequences-functions-and-graphs/coordinate-geometry/gradient-of-a-line.json::spcpt_XhXhg6sRyMQ88chp — tier S1_name_match — score 0.8667 — wording EXACT — validation tier AI_VALIDATED (operator-delegated chain)
- Rationale: SME span 'Gradient of a Line' on note 'Gradient of a Line' is anchored by the corpus spec_point block spcpt_XhXhg6sRyMQ88chp and joined to 4MA1-3.3G via name_to_statement_join; this section chunk sits inside that span.
- Verdict: [ ] CONFIRM — this chunk belongs to this SP   [ ] REJECT — wrong chunk/SP   [ ] HOLD — needs rework

### 4MA1-4.10D — find the surface area of a cylinder
- Note: Surface Area (`notes/4-geometry-and-trigonometry/volume-and-surface-area/surface-area.json`)
- Chunk: ordinal 5 — heading `How do I find the surface area of a sphere?` — sha256_16 `0ac3ba728d674184` — 1690 chars
- Evidence quote (verbatim self-slice, markdown-safe): "How do I find the surface area of a sphere?
- A sphere has a **single curved surface**
A sphere
- The surface area of a sphere, *A*, with radius, *r*, can be found using the formula

  - $A=4πr^{2}$
  - This formula is given to you in the e"
- Chunk excerpt: «How do I find the surface area of a sphere? - A sphere has a **single curved surface** A sphere - The surface area of a sphere, *A*, with radius, *r*, can be found using the formula - $A=4πr^{2}$ - This formula is given to you in the exam - A **hemisphere** has half the curved surface area of a sphere and the flat circular base Surface area of a hemisphere - The surface area of a hemisphere, *A*, with radius, *r*, ca»
- Upstream: T-C32 join notes/4-geometry-and-trigonometry/volume-and-surface-area/surface-area.json::spcpt_2w9hbV5pTbvc5Smj — tier S1_name_match — score 0.8043 — wording EXACT — validation tier AI_VALIDATED (operator-delegated chain)
- Rationale: SME span 'Surface Area' on note 'Surface Area' is anchored by the corpus spec_point block spcpt_2w9hbV5pTbvc5Smj and joined to 4MA1-4.10D via name_to_statement_join; this section chunk sits inside that span.
- Verdict: [ ] CONFIRM — this chunk belongs to this SP   [ ] REJECT — wrong chunk/SP   [ ] HOLD — needs rework

### 4MA1-5.2D — understand that reflections are specified by a mirror line
- Note: Reflections (`notes/5-vectors-and-transformation-geometry/transformations/reflections.json`)
- Chunk: ordinal 1 — heading `What is a reflection?` — sha256_16 `af0419a3c4a59f36` — 636 chars
- Evidence quote (verbatim self-slice, markdown-safe): "What is a reflection?
- A** reflection flips **a shape across a **mirror line**

  - This is called the **line of reflection**
- The **reflected image **is the **same size **as the** original object**

  - It has been** flipped **across the"
- Chunk excerpt: «What is a reflection? - A** reflection flips **a shape across a **mirror line** - This is called the **line of reflection** - The **reflected image **is the **same size **as the** original object** - It has been** flipped **across the mirror line to a **new position **and **orientation** - The following two **distances will be equal** for each point: - The **perpendicular distance** between the **original point and t»
- Upstream: T-C32 join notes/5-vectors-and-transformation-geometry/transformations/reflections.json::spcpt_DQrkJGG4Mngch9xc — tier S1_name_match — score 0.7275 — wording EXACT — validation tier AI_VALIDATED (operator-delegated chain)
- Rationale: SME span 'Reflections' on note 'Reflections' is anchored by the corpus spec_point block spcpt_DQrkJGG4Mngch9xc and joined to 4MA1-5.2D via name_to_statement_join; this section chunk sits inside that span.
- Verdict: [ ] CONFIRM — this chunk belongs to this SP   [ ] REJECT — wrong chunk/SP   [ ] HOLD — needs rework

### 4MA1-3.1C — find the sum of the firstnterms of an arithmetic series(Sn)
- Note: Arithmetic Sequences (`notes/3-sequences-functions-and-graphs/sequences/arithmetic-sequences.json`)
- Chunk: ordinal 1 — heading `What is an arithmetic sequence?` — sha256_16 `f488ad55441a9d4b` — 515 chars
- Evidence quote (verbatim self-slice, markdown-safe): "What is an arithmetic sequence?
- An **arithmetic sequence **is a sequence where terms increase by the **same amount each time**

  - The amount it increases by is called the **common difference**
  
    - For example: 3, 5, 7, 9, ...
    -"
- Chunk excerpt: «What is an arithmetic sequence? - An **arithmetic sequence **is a sequence where terms increase by the **same amount each time** - The amount it increases by is called the **common difference** - For example: 3, 5, 7, 9, ... - The common difference is 2 - Common differences can be **negative** - These arithmetic sequences decrease by the same amount each time - For example: 11, 8, 5, 2, -1, ... - The common differenc»
- Upstream: T-C32 join notes/3-sequences-functions-and-graphs/sequences/arithmetic-sequences.json::spcpt_fhF2H4HM3cxqsGdd — tier S1_name_match — score 0.7758 — wording EXACT — validation tier AI_VALIDATED (operator-delegated chain)
- Rationale: SME span 'Arithmetic Sequences' on note 'Arithmetic Sequences' is anchored by the corpus spec_point block spcpt_fhF2H4HM3cxqsGdd and joined to 4MA1-3.1C via name_to_statement_join; this section chunk sits inside that span.
- Verdict: [ ] CONFIRM — this chunk belongs to this SP   [ ] REJECT — wrong chunk/SP   [ ] HOLD — needs rework

### 4MA1-4.2F — understand congruence as meaning the same shape and size
- Note: Congruence (`notes/4-geometry-and-trigonometry/congruence-similarity-and-geometrical-proof/congruence.json`)
- Chunk: ordinal 0 — heading `Congruence` — sha256_16 `8d1495c2ef0543c7` — 10 chars
- Evidence quote (verbatim self-slice, markdown-safe): "Congruence"
- Chunk excerpt: «Congruence»
- Upstream: T-C32 join notes/4-geometry-and-trigonometry/congruence-similarity-and-geometrical-proof/congruence.json::spcpt_3nz4CDxVDMqZNQNR — tier S1_name_match — score 0.7212 — wording EXACT — validation tier AI_VALIDATED (operator-delegated chain)
- Rationale: SME span 'Congruence' on note 'Congruence' is anchored by the corpus spec_point block spcpt_3nz4CDxVDMqZNQNR and joined to 4MA1-4.2F via name_to_statement_join; this section chunk sits inside that span.
- Verdict: [ ] CONFIRM — this chunk belongs to this SP   [ ] REJECT — wrong chunk/SP   [ ] HOLD — needs rework

### 4MA1-3.3I — recognise, generate points and plot graphs of linear and quadratic functions
- Note: Quadratic Graphs (`notes/3-sequences-functions-and-graphs/graphs-of-functions/quadratic-graphs.json`)
- Chunk: ordinal 6 — heading `How do I find the equation of a quadratic from its graph?` — sha256_16 `7275f2f8a1f35d18` — 3273 chars
- Evidence quote (verbatim self-slice, markdown-safe): "How do I find the equation of a quadratic from its graph?
- If the **vertex **and **one other point **are known

  - Use the form `y equals a open parentheses x minus p close parentheses squared plus q` to fill in $p$ and $q$
  
    - The v"
- Chunk excerpt: «How do I find the equation of a quadratic from its graph? - If the **vertex **and **one other point **are known - Use the form `y equals a open parentheses x minus p close parentheses squared plus q` to fill in $p$ and $q$ - The vertex is at `open parentheses p comma space q close parentheses` - Then substitute in the other known point `open parentheses x comma space y close parentheses` to find $a$ - If the **roots »
- Upstream: T-C32 join notes/3-sequences-functions-and-graphs/graphs-of-functions/quadratic-graphs.json::spcpt_76gVqdMN62jnrZg6 — tier S1_name_match — score 0.6967 — wording EXACT — validation tier AI_VALIDATED (operator-delegated chain)
- Rationale: SME span 'Quadratic Graphs' on note 'Quadratic Graphs' is anchored by the corpus spec_point block spcpt_76gVqdMN62jnrZg6 and joined to 4MA1-3.3I via name_to_statement_join; this section chunk sits inside that span.
- Verdict: [ ] CONFIRM — this chunk belongs to this SP   [ ] REJECT — wrong chunk/SP   [ ] HOLD — needs rework

### 4MA1-5.2H — understand and use column vectors in translations
- Note: Translations (`notes/5-vectors-and-transformation-geometry/transformations/translations.json`)
- Chunk: ordinal 1 — heading `What are transformations in maths?` — sha256_16 `61fcffe06d29631a` — 536 chars
- Evidence quote (verbatim self-slice, markdown-safe): "What are transformations in maths?
- There are **four transformations** to learn

  - **translations**,** rotations**,** reflections **and** enlargements**
- A transformation can **change** the **position**, **orientation** and/or **size** "
- Chunk excerpt: «What are transformations in maths? - There are **four transformations** to learn - **translations**,** rotations**,** reflections **and** enlargements** - A transformation can **change** the **position**, **orientation** and/or **size** of a **shape** - The **original shape** is called the **object** - The **transformed shape** is called the **image** - Vertices are labelled to show **corresponding points** - Vertice»
- Upstream: T-C32 join notes/5-vectors-and-transformation-geometry/transformations/translations.json::spcpt_YQX35KWR6v8thX5T — tier S1_name_match — score 0.7574 — wording EXACT — validation tier AI_VALIDATED (operator-delegated chain)
- Rationale: SME span 'Translations' on note 'Translations' is anchored by the corpus spec_point block spcpt_YQX35KWR6v8thX5T and joined to 4MA1-5.2H via name_to_statement_join; this section chunk sits inside that span.
- Verdict: [ ] CONFIRM — this chunk belongs to this SP   [ ] REJECT — wrong chunk/SP   [ ] HOLD — needs rework

### 4MA1-3.3I — recognise, generate points and plot graphs of linear and quadratic functions
- Note: Quadratic Graphs (`notes/3-sequences-functions-and-graphs/graphs-of-functions/quadratic-graphs.json`)
- Chunk: ordinal 4 — heading `How do I find the coordinates of the turning point by completing the square?` — sha256_16 `7e005e1096e6a686` — 1415 chars
- Evidence quote (verbatim self-slice, markdown-safe): "How do I find the coordinates of the turning point by completing the square?
- The coordinates of the **turning point **(vertex) of a quadratic graph can be found by **completing the square**
- For a quadratic graph written in the form `y e"
- Chunk excerpt: «How do I find the coordinates of the turning point by completing the square? - The coordinates of the **turning point **(vertex) of a quadratic graph can be found by **completing the square** - For a quadratic graph written in the form `y equals a open parentheses x minus p close parentheses squared plus q` - the minimum or maximum point has **coordinates **`open parentheses p comma space q close parentheses` - Bewar»
- Upstream: T-C32 join notes/3-sequences-functions-and-graphs/graphs-of-functions/quadratic-graphs.json::spcpt_76gVqdMN62jnrZg6 — tier S1_name_match — score 0.6967 — wording EXACT — validation tier AI_VALIDATED (operator-delegated chain)
- Rationale: SME span 'Quadratic Graphs' on note 'Quadratic Graphs' is anchored by the corpus spec_point block spcpt_76gVqdMN62jnrZg6 and joined to 4MA1-3.3I via name_to_statement_join; this section chunk sits inside that span.
- Verdict: [ ] CONFIRM — this chunk belongs to this SP   [ ] REJECT — wrong chunk/SP   [ ] HOLD — needs rework

### 4MA1-4.4D — understand angle measure including three-figure bearings
- Note: Bearings (`notes/4-geometry-and-trigonometry/bearings-scale-drawing-and-constructions/bearings.json`)
- Chunk: ordinal 0 — heading `Bearings` — sha256_16 `7c35ebce2e0dbdb4` — 8 chars
- Evidence quote (verbatim self-slice, markdown-safe): "Bearings"
- Chunk excerpt: «Bearings»
- Upstream: T-C32 join notes/4-geometry-and-trigonometry/bearings-scale-drawing-and-constructions/bearings.json::spcpt_38XcCSfT6hW33fDn — tier S1_name_match — score 0.7 — wording EXACT — validation tier AI_VALIDATED (operator-delegated chain)
- Rationale: SME span 'Bearings' on note 'Bearings' is anchored by the corpus spec_point block spcpt_38XcCSfT6hW33fDn and joined to 4MA1-4.4D via name_to_statement_join; this section chunk sits inside that span.
- Verdict: [ ] CONFIRM — this chunk belongs to this SP   [ ] REJECT — wrong chunk/SP   [ ] HOLD — needs rework

### 4MA1-3.4C — determine gradients, rates of change, stationary points, turning points (maxima and minima) by differentiation and relate these to graphs
- Note: Differentiation (`notes/3-sequences-functions-and-graphs/differentiation/differentiation.json`)
- Chunk: ordinal 2 — heading `What is differentiation and how does it work?` — sha256_16 `4476744dd77e1adf` — 1414 chars
- Evidence quote (verbatim self-slice, markdown-safe): "What is differentiation and how does it work?
- **Differentiation** is an **algebraic method** that changes the **equation **of a curve, $y=...$, into a **gradient function**, $\frac{dy}{dx}=...$
- To differentiate a power of $x$, **bring d"
- Chunk excerpt: «What is differentiation and how does it work? - **Differentiation** is an **algebraic method** that changes the **equation **of a curve, $y=...$, into a **gradient function**, $\frac{dy}{dx}=...$ - To differentiate a power of $x$, **bring down the power** and** reduce the power by 1** - Differentiating $y=x^{5}$ gives $\frac{dy}{dx}=5x^{4}$ - Differentiating $y=x^{8}$ gives $\frac{dy}{dx}=8x^{7}$ - Differentiating $y»
- Upstream: T-C32 join notes/3-sequences-functions-and-graphs/differentiation/differentiation.json::spcpt_fGGbSYFZH9DW4sgm — tier S1_name_match — score 0.6805 — wording EXACT — validation tier AI_VALIDATED (operator-delegated chain)
- Rationale: SME span 'Differentiation' on note 'Differentiation' is anchored by the corpus spec_point block spcpt_fGGbSYFZH9DW4sgm and joined to 4MA1-3.4C via name_to_statement_join; this section chunk sits inside that span.
- Verdict: [ ] CONFIRM — this chunk belongs to this SP   [ ] REJECT — wrong chunk/SP   [ ] HOLD — needs rework

### 4MA1-3.1C — find the sum of the firstnterms of an arithmetic series(Sn)
- Note: Arithmetic Sequences (`notes/3-sequences-functions-and-graphs/sequences/arithmetic-sequences.json`)
- Chunk: ordinal 0 — heading `Arithmetic sequences` — sha256_16 `1ccecddcb3748f7a` — 20 chars
- Evidence quote (verbatim self-slice, markdown-safe): "Arithmetic sequences"
- Chunk excerpt: «Arithmetic sequences»
- Upstream: T-C32 join notes/3-sequences-functions-and-graphs/sequences/arithmetic-sequences.json::spcpt_fhF2H4HM3cxqsGdd — tier S1_name_match — score 0.7758 — wording EXACT — validation tier AI_VALIDATED (operator-delegated chain)
- Rationale: SME span 'Arithmetic Sequences' on note 'Arithmetic Sequences' is anchored by the corpus spec_point block spcpt_fhF2H4HM3cxqsGdd and joined to 4MA1-3.1C via name_to_statement_join; this section chunk sits inside that span.
- Verdict: [ ] CONFIRM — this chunk belongs to this SP   [ ] REJECT — wrong chunk/SP   [ ] HOLD — needs rework

### 4MA1-4.4G — use compound measure such as speed, density and pressure
- Note: Speed, Density & Pressure (`notes/4-geometry-and-trigonometry/standard-and-compound-units/speed-density-and-pressure.json`)
- Chunk: ordinal 4 — heading `What should I know about pressure, force and area?` — sha256_16 `8a0b059a1c625df2` — 2857 chars
- Evidence quote (verbatim self-slice, markdown-safe): "What should I know about pressure, force and area?
- Pressure is usually measured in Newtons per square metre (**N/m**<sup>**2**</sup>)

  - The units of pressure are often called **Pascals** (**Pa**) rather than **N/m**<sup>**2**</sup>
  -"
- Chunk excerpt: «What should I know about pressure, force and area? - Pressure is usually measured in Newtons per square metre (**N/m**<sup>**2**</sup>) - The units of pressure are often called **Pascals** (**Pa**) rather than **N/m**<sup>**2**</sup> - The units indicate that **pressure** is **force per area** $\mathrm{Pressure}=\frac{\mathrm{Force}}{\mathrm{Area}}$ - You will be **given **this formula in the exam if it is needed - R»
- Upstream: T-C32 join notes/4-geometry-and-trigonometry/standard-and-compound-units/speed-density-and-pressure.json::spcpt_jJPhXSKYBg6x4d2Q — tier S1_name_match — score 0.8286 — wording EXACT — validation tier AI_VALIDATED (operator-delegated chain)
- Rationale: SME span 'Speed, Density & Pressure' on note 'Speed, Density & Pressure' is anchored by the corpus spec_point block spcpt_jJPhXSKYBg6x4d2Q and joined to 4MA1-4.4G via name_to_statement_join; this section chunk sits inside that span.
- Verdict: [ ] CONFIRM — this chunk belongs to this SP   [ ] REJECT — wrong chunk/SP   [ ] HOLD — needs rework

### 4MA1-2.2B — understand the concept of a quadratic expression and be able to factorise such expressions
- Note: Collecting Like Terms (`notes/2-equations-formulae-and-identities/algebra-toolkit/collecting-like-terms.json`)
- Chunk: ordinal 0 — heading `Collecting like terms` — sha256_16 `5a9864012219656d` — 21 chars
- Evidence quote (verbatim self-slice, markdown-safe): "Collecting like terms"
- Chunk excerpt: «Collecting like terms»
- Upstream: T-C32 join notes/2-equations-formulae-and-identities/algebra-toolkit/collecting-like-terms.json::spcpt_rsCdKqXKjhfmkyqT — tier S1_name_match — score 0.7692 — wording EXACT — validation tier AI_VALIDATED (operator-delegated chain)
- Rationale: SME span 'Collecting Like Terms' on note 'Collecting Like Terms' is anchored by the corpus spec_point block spcpt_rsCdKqXKjhfmkyqT and joined to 4MA1-2.2B via name_to_statement_join; this section chunk sits inside that span.
- Verdict: [ ] CONFIRM — this chunk belongs to this SP   [ ] REJECT — wrong chunk/SP   [ ] HOLD — needs rework

### 4MA1-4.4B — calculate time intervals in terms of the 24-hour and the 12-hour clock
- Note: Time (`notes/4-geometry-and-trigonometry/standard-and-compound-units/time.json`)
- Chunk: ordinal 3 — heading `How do I read the time from an analogue clock?` — sha256_16 `a132671c353a34bd` — 444 chars
- Evidence quote (verbatim self-slice, markdown-safe): "How do I read the time from an analogue clock?
- An **analogue** clock works in **12-hour **time

  - The **short hand** is the **hour hand**
  
    - Each number on the clock represents **one hour** for the hour hand
  - The **long hand** "
- Chunk excerpt: «How do I read the time from an analogue clock? - An **analogue** clock works in **12-hour **time - The **short hand** is the **hour hand** - Each number on the clock represents **one hour** for the hour hand - The **long hand** is the **minute hand** - Each number on the clock represents **five minutes** for the minute hand - Some clocks will have markings for individual minutes Reading the time from an analogue cloc»
- Upstream: T-C32 join notes/4-geometry-and-trigonometry/standard-and-compound-units/time.json::spcpt_h2p7nv6zkR4xFJ3P — tier S2_name_ambiguous — score 0.6432 — wording EXACT — validation tier AI_VALIDATED (operator-delegated chain)
- Rationale: SME span 'Time' on note 'Time' is anchored by the corpus spec_point block spcpt_h2p7nv6zkR4xFJ3P and joined to 4MA1-4.4B via name_to_statement_join; this section chunk sits inside that span.
- Verdict: [ ] CONFIRM — this chunk belongs to this SP   [ ] REJECT — wrong chunk/SP   [ ] HOLD — needs rework

### 4MA1-1.7B — divide a quantity in a given ratio or ratios
- Note: Introduction to Ratios (`notes/1-numbers-and-the-number-system/ratio-toolkit/simple-ratio.json`)
- Chunk: ordinal 4 — heading `How do I find an equivalent ratio?` — sha256_16 `2250c6c1158dfe92` — 2541 chars
- Evidence quote (verbatim self-slice, markdown-safe): "How do I find an equivalent ratio?
- You can find an **equivalent ratio** by **multiplying **(or **dividing**) **each part** of the ratio by the **same value**

  - E.g. Multiply each part of the ratio 2 : 3 : 7 by 4 to find an equivalent r"
- Chunk excerpt: «How do I find an equivalent ratio? - You can find an **equivalent ratio** by **multiplying **(or **dividing**) **each part** of the ratio by the **same value** - E.g. Multiply each part of the ratio 2 : 3 : 7 by 4 to find an equivalent ratio of 8 : 12 : 28 - Ratios can be scaled up or down to suit the context of a question - The size of each part in the ratio, **relative** to the others, is still the same - The **act»
- Upstream: T-C32 join notes/1-numbers-and-the-number-system/ratio-toolkit/simple-ratio.json::spcpt_qpSmD6yNY5t5GrW6 — tier S1_name_match — score 0.696 — wording EXACT — validation tier AI_VALIDATED (operator-delegated chain)
- Rationale: SME span 'Ratios' on note 'Introduction to Ratios' is anchored by the corpus spec_point block spcpt_qpSmD6yNY5t5GrW6 and joined to 4MA1-1.7B via name_to_statement_join; this section chunk sits inside that span.
- Verdict: [ ] CONFIRM — this chunk belongs to this SP   [ ] REJECT — wrong chunk/SP   [ ] HOLD — needs rework

### 4MA1-4.10F — convert between units of volume within the metric system
- Note: Volume (`notes/4-geometry-and-trigonometry/volume-and-surface-area/volume.json`)
- Chunk: ordinal 6 — heading `How do I find the volume of a sphere?` — sha256_16 `bfd68800e72d28f2` — 998 chars
- Evidence quote (verbatim self-slice, markdown-safe): "How do I find the volume of a sphere?
- To calculate the volume, *V*, of a **sphere** with radius, *r*, use the formula

  - $V=\frac{4}{3}πr^{3}$
  - This formula is given to you in your exam
Sphere Radius r, IGCSE & GCSE Maths revision no"
- Chunk excerpt: «How do I find the volume of a sphere? - To calculate the volume, *V*, of a **sphere** with radius, *r*, use the formula - $V=\frac{4}{3}πr^{3}$ - This formula is given to you in your exam Sphere Radius r, IGCSE & GCSE Maths revision notes Exam Hint: You only need to memorise the volume formulae for **cuboids**! Worked Example: A cylinder is shown. ![Cylinder](assets/acd173315545-55219-volume-7.png) The radius, *r*, i»
- Upstream: T-C32 join notes/4-geometry-and-trigonometry/volume-and-surface-area/volume.json::spcpt_pKCFj25GzzqW6sr3 — tier S2_name_ambiguous — score 0.6774 — wording EXACT — validation tier AI_VALIDATED (operator-delegated chain)
- Rationale: SME span 'Volume' on note 'Volume' is anchored by the corpus spec_point block spcpt_pKCFj25GzzqW6sr3 and joined to 4MA1-4.10F via name_to_statement_join; this section chunk sits inside that span.
- Verdict: [ ] CONFIRM — this chunk belongs to this SP   [ ] REJECT — wrong chunk/SP   [ ] HOLD — needs rework

### 4MA1-4.2F — understand congruence as meaning the same shape and size
- Note: Congruence (`notes/4-geometry-and-trigonometry/congruence-similarity-and-geometrical-proof/congruence.json`)
- Chunk: ordinal 1 — heading `What is congruence?` — sha256_16 `6e6c3775d90ed74e` — 371 chars
- Evidence quote (verbatim self-slice, markdown-safe): "What is congruence?
- Two shapes are **congruent **if they are **identical **in **shape** and **size**

  - One may be a **reflection**, **rotation**, or **translation **of the other
- If one shape is an **enlargement **of the other, then t"
- Chunk excerpt: «What is congruence? - Two shapes are **congruent **if they are **identical **in **shape** and **size** - One may be a **reflection**, **rotation**, or **translation **of the other - If one shape is an **enlargement **of the other, then they are **not identical in size** and so are **not** congruent - If all the angles are the same, then the shapes are **similar**»
- Upstream: T-C32 join notes/4-geometry-and-trigonometry/congruence-similarity-and-geometrical-proof/congruence.json::spcpt_3nz4CDxVDMqZNQNR — tier S1_name_match — score 0.7212 — wording EXACT — validation tier AI_VALIDATED (operator-delegated chain)
- Rationale: SME span 'Congruence' on note 'Congruence' is anchored by the corpus spec_point block spcpt_3nz4CDxVDMqZNQNR and joined to 4MA1-4.2F via name_to_statement_join; this section chunk sits inside that span.
- Verdict: [ ] CONFIRM — this chunk belongs to this SP   [ ] REJECT — wrong chunk/SP   [ ] HOLD — needs rework

### 4MA1-6.2B — understand the concept of a measure of spread
- Note: Mean, Median & Mode (`notes/6-statistics-and-probability/statistics-toolkit/mean-median-and-mode.json`)
- Chunk: ordinal 3 — heading `What is the mean?` — sha256_16 `0a80920cff89d04b` — 349 chars
- Evidence quote (verbatim self-slice, markdown-safe): "What is the mean?
- The **mean** is the **sum** of the values **divided **by the **number **of values

  - The mean of 1, 2, 6 is (1 + 2 + 6) ÷ 3 = 3
- The mean can be **fraction **or a **decimal**

  - It may need **rounding**
  - You do *"
- Chunk excerpt: «What is the mean? - The **mean** is the **sum** of the values **divided **by the **number **of values - The mean of 1, 2, 6 is (1 + 2 + 6) ÷ 3 = 3 - The mean can be **fraction **or a **decimal** - It may need **rounding** - You do **not **need to force it to be a **whole** number - You** can** have a mean of 7.5 people, for example!»
- Upstream: T-C32 join notes/6-statistics-and-probability/statistics-toolkit/mean-median-and-mode.json::spcpt_myNYhxstM7xnZd9P — tier S1_name_match — score 0.76 — wording EXACT — validation tier AI_VALIDATED (operator-delegated chain)
- Rationale: SME span 'Mean, Median & Mode' on note 'Mean, Median & Mode' is anchored by the corpus spec_point block spcpt_myNYhxstM7xnZd9P and joined to 4MA1-6.2B via name_to_statement_join; this section chunk sits inside that span.
- Verdict: [ ] CONFIRM — this chunk belongs to this SP   [ ] REJECT — wrong chunk/SP   [ ] HOLD — needs rework

### 4MA1-4.10F — convert between units of volume within the metric system
- Note: Volume (`notes/4-geometry-and-trigonometry/volume-and-surface-area/volume.json`)
- Chunk: ordinal 3 — heading `How do I find the volume of a prism?` — sha256_16 `a042c9fd791a3df4` — 560 chars
- Evidence quote (verbatim self-slice, markdown-safe): "How do I find the volume of a prism?
- A **prism** is a 3D object with a **constant cross-sectional area**
- To find the volume, *V*, of a **prism**, with cross-sectional area, *A*, and length, *l*, use the formula

  - $V=Al$
  - This form"
- Chunk excerpt: «How do I find the volume of a prism? - A **prism** is a 3D object with a **constant cross-sectional area** - To find the volume, *V*, of a **prism**, with cross-sectional area, *A*, and length, *l*, use the formula - $V=Al$ - This formula is given to you in the exam Volume of a prism - Note that the cross-section can be **any shape**, so as long as you know its **area **and the** length **of the prism, you can calcul»
- Upstream: T-C32 join notes/4-geometry-and-trigonometry/volume-and-surface-area/volume.json::spcpt_pKCFj25GzzqW6sr3 — tier S2_name_ambiguous — score 0.6774 — wording EXACT — validation tier AI_VALIDATED (operator-delegated chain)
- Rationale: SME span 'Volume' on note 'Volume' is anchored by the corpus spec_point block spcpt_pKCFj25GzzqW6sr3 and joined to 4MA1-4.10F via name_to_statement_join; this section chunk sits inside that span.
- Verdict: [ ] CONFIRM — this chunk belongs to this SP   [ ] REJECT — wrong chunk/SP   [ ] HOLD — needs rework

### 4MA1-3.4C — determine gradients, rates of change, stationary points, turning points (maxima and minima) by differentiation and relate these to graphs
- Note: Differentiation (`notes/3-sequences-functions-and-graphs/differentiation/differentiation.json`)
- Chunk: ordinal 0 — heading `Differentiation` — sha256_16 `26e732f5bd6a7594` — 15 chars
- Evidence quote (verbatim self-slice, markdown-safe): "Differentiation"
- Chunk excerpt: «Differentiation»
- Upstream: T-C32 join notes/3-sequences-functions-and-graphs/differentiation/differentiation.json::spcpt_fGGbSYFZH9DW4sgm — tier S1_name_match — score 0.6805 — wording EXACT — validation tier AI_VALIDATED (operator-delegated chain)
- Rationale: SME span 'Differentiation' on note 'Differentiation' is anchored by the corpus spec_point block spcpt_fGGbSYFZH9DW4sgm and joined to 4MA1-3.4C via name_to_statement_join; this section chunk sits inside that span.
- Verdict: [ ] CONFIRM — this chunk belongs to this SP   [ ] REJECT — wrong chunk/SP   [ ] HOLD — needs rework

### 4MA1-4.1B — use angle properties of intersecting lines, parallel lines and angles on a straight line
- Note: Parallel Lines (`notes/3-sequences-functions-and-graphs/linear-graphs-y-equals-mx-plus-c/parallel-lines.json`)
- Chunk: ordinal 1 — heading `What are parallel lines?` — sha256_16 `6eb99bd050b1eaf4` — 380 chars
- Evidence quote (verbatim self-slice, markdown-safe): "What are parallel lines?
- **Parallel lines** are** straight lines **with the **same gradient**

  - Two parallel lines will **never meet**
  
    - They just stay side-by-side forever
- The **equation** of the line **parallel** to *y*  = *"
- Chunk excerpt: «What are parallel lines? - **Parallel lines** are** straight lines **with the **same gradient** - Two parallel lines will **never meet** - They just stay side-by-side forever - The **equation** of the line **parallel** to *y* = *mx* + *c* is ***y***** = *****mx***** + *****d*** - $y=2x+1$ and $y=2x+5$ are parallel - $y=2x+1$ and $y=3x+1$ are **not** parallel»
- Upstream: T-C32 join notes/3-sequences-functions-and-graphs/linear-graphs-y-equals-mx-plus-c/parallel-lines.json::spcpt_qPRh2fycSMYwytcV — tier S1_name_match — score 0.7109 — wording EXACT — validation tier AI_VALIDATED (operator-delegated chain)
- Rationale: SME span 'Parallel Lines' on note 'Parallel Lines' is anchored by the corpus spec_point block spcpt_qPRh2fycSMYwytcV and joined to 4MA1-4.1B via name_to_statement_join; this section chunk sits inside that span.
- Verdict: [ ] CONFIRM — this chunk belongs to this SP   [ ] REJECT — wrong chunk/SP   [ ] HOLD — needs rework

### 4MA1-4.4D — understand angle measure including three-figure bearings
- Note: Bearings (`notes/4-geometry-and-trigonometry/bearings-scale-drawing-and-constructions/bearings.json`)
- Chunk: ordinal 2 — heading `How do I find a bearing between two points?` — sha256_16 `eaa995ebfd43b813` — 500 chars
- Evidence quote (verbatim self-slice, markdown-safe): "How do I find a bearing between two points?
- Identify where you need to **start**

  - "The bearing **of A from B**" means **start at B** and find the bearing to A
  - "The bearing **of B from A**" means **start at A** and find the bearing"
- Chunk excerpt: «How do I find a bearing between two points? - Identify where you need to **start** - "The bearing **of A from B**" means **start at B** and find the bearing to A - "The bearing **of B from A**" means **start at A** and find the bearing to B - Draw a **North line** at the **starting point** - Draw a **line between the two points** - **Measure** the angle between the **North line** and the l**ine joining the points** -»
- Upstream: T-C32 join notes/4-geometry-and-trigonometry/bearings-scale-drawing-and-constructions/bearings.json::spcpt_38XcCSfT6hW33fDn — tier S1_name_match — score 0.7 — wording EXACT — validation tier AI_VALIDATED (operator-delegated chain)
- Rationale: SME span 'Bearings' on note 'Bearings' is anchored by the corpus spec_point block spcpt_38XcCSfT6hW33fDn and joined to 4MA1-4.4D via name_to_statement_join; this section chunk sits inside that span.
- Verdict: [ ] CONFIRM — this chunk belongs to this SP   [ ] REJECT — wrong chunk/SP   [ ] HOLD — needs rework

### 4MA1-3.3E — find the intersection points of two graphs, one linear ( y ) and one non-linear ( y ), and and recognise that the solutions correspond to the solutions of ( y − y ) = 0 2 1
- Note: Midpoint of a Line (`notes/3-sequences-functions-and-graphs/coordinate-geometry/midpoint-of-a-line.json`)
- Chunk: ordinal 0 — heading `Midpoint of a line` — sha256_16 `883d619d8a00dfb3` — 18 chars
- Evidence quote (verbatim self-slice, markdown-safe): "Midpoint of a line"
- Chunk excerpt: «Midpoint of a line»
- Upstream: T-C32 join notes/3-sequences-functions-and-graphs/coordinate-geometry/midpoint-of-a-line.json::spcpt_84hZy4pDd8nBGN3r — tier S1_name_match — score 0.719 — wording EXACT — validation tier AI_VALIDATED (operator-delegated chain)
- Rationale: SME span 'Midpoint of a Line' on note 'Midpoint of a Line' is anchored by the corpus spec_point block spcpt_84hZy4pDd8nBGN3r and joined to 4MA1-3.3E via name_to_statement_join; this section chunk sits inside that span.
- Verdict: [ ] CONFIRM — this chunk belongs to this SP   [ ] REJECT — wrong chunk/SP   [ ] HOLD — needs rework

### 4MA1-1.10C — understand and carry out calculations using time, and carry out calculations using money, including converting between currencies
- Note: Money Calculations (`notes/1-numbers-and-the-number-system/number-toolkit/money-calculations.json`)
- Chunk: ordinal 1 — heading `What currencies can be used?` — sha256_16 `01a3e3ca5cf854b4` — 265 chars
- Evidence quote (verbatim self-slice, markdown-safe): "What currencies can be used?
- Many different currencies are used
- The** most commonly** used **currencies **are

  - US Dollars (\$ or USD)
  - Pounds (£ or GBP)
  - Euros (€ or Euros)
  - It is possible to see other currencies used, with"
- Chunk excerpt: «What currencies can be used? - Many different currencies are used - The** most commonly** used **currencies **are - US Dollars (\$ or USD) - Pounds (£ or GBP) - Euros (€ or Euros) - It is possible to see other currencies used, with or without their symbols»
- Upstream: T-C32 join notes/1-numbers-and-the-number-system/number-toolkit/money-calculations.json::spcpt_bMYrxtVc2SZgt8mX — tier S1_name_match — score 0.6772 — wording EXACT — validation tier AI_VALIDATED (operator-delegated chain)
- Rationale: SME span 'Money Calculations' on note 'Money Calculations' is anchored by the corpus spec_point block spcpt_bMYrxtVc2SZgt8mX and joined to 4MA1-1.10C via name_to_statement_join; this section chunk sits inside that span.
- Verdict: [ ] CONFIRM — this chunk belongs to this SP   [ ] REJECT — wrong chunk/SP   [ ] HOLD — needs rework

### 4MA1-1.6F — use reverse percentages
- Note: Reverse Percentages (`notes/1-numbers-and-the-number-system/percentages/reverse-percentages.json`)
- Chunk: ordinal 2 — heading `How do I solve reverse percentage questions?` — sha256_16 `472f5793f7086d6b` — 1691 chars
- Evidence quote (verbatim self-slice, markdown-safe): "How do I solve reverse percentage questions?
- You should think about the **before** **quantity**

  - even though it is not given in the question
- Find the percentage change as a **multiplier**, *p*

  - This is the decimal equivalent of "
- Chunk excerpt: «How do I solve reverse percentage questions? - You should think about the **before** **quantity** - even though it is not given in the question - Find the percentage change as a **multiplier**, *p* - This is the decimal equivalent of a percentage change - A percentage increase of 4% means *p* = 1 + 0.04 = 1.04 - A percentage decrease of 5% means *p* = 1 - 0.05 = 0.95 - Use **before × *****p***** = after** to write an»
- Upstream: T-C32 join notes/1-numbers-and-the-number-system/percentages/reverse-percentages.json::spcpt_5CHMgxBWhBwxh5Y6 — tier S1_name_match — score 0.9619 — wording EXACT — validation tier AI_VALIDATED (operator-delegated chain)
- Rationale: SME span 'Reverse Percentages' on note 'Reverse Percentages' is anchored by the corpus spec_point block spcpt_5CHMgxBWhBwxh5Y6 and joined to 4MA1-1.6F via name_to_statement_join; this section chunk sits inside that span.
- Verdict: [ ] CONFIRM — this chunk belongs to this SP   [ ] REJECT — wrong chunk/SP   [ ] HOLD — needs rework

### 4MA1-3.3G — find the equation of a straight line parallel to a given line; find the equation of a straight line perpendicular to a given line
- Note: Gradient of a Line (`notes/3-sequences-functions-and-graphs/coordinate-geometry/gradient-of-a-line.json`)
- Chunk: ordinal 1 — heading `What is the gradient of a line?` — sha256_16 `ac3e7eb09c9ec3a4` — 542 chars
- Evidence quote (verbatim self-slice, markdown-safe): "What is the gradient of a line?
- The** gradient **is a measure of how **steep** a straight line is
- A gradient of 3 means:

  - For every **1 unit** to the right, go **up** by 3
- A gradient of -4 means:

  - For every **1 unit **to the r"
- Chunk excerpt: «What is the gradient of a line? - The** gradient **is a measure of how **steep** a straight line is - A gradient of 3 means: - For every **1 unit** to the right, go **up** by 3 - A gradient of -4 means: - For every **1 unit **to the right, go **down** by 4 - A gradient of 3 is **steeper** than 2 - A gradient of -5 is **steeper **than -4 - A **positive** gradient means the line goes **upwards** (uphill) - Bottom left »
- Upstream: T-C32 join notes/3-sequences-functions-and-graphs/coordinate-geometry/gradient-of-a-line.json::spcpt_XhXhg6sRyMQ88chp — tier S1_name_match — score 0.8667 — wording EXACT — validation tier AI_VALIDATED (operator-delegated chain)
- Rationale: SME span 'Gradient of a Line' on note 'Gradient of a Line' is anchored by the corpus spec_point block spcpt_XhXhg6sRyMQ88chp and joined to 4MA1-3.3G via name_to_statement_join; this section chunk sits inside that span.
- Verdict: [ ] CONFIRM — this chunk belongs to this SP   [ ] REJECT — wrong chunk/SP   [ ] HOLD — needs rework

### 4MA1-6.1A — construct and interpret histograms
- Note: Bar Charts & Pictograms (`notes/6-statistics-and-probability/statistics-toolkit/bar-charts-and-pictograms.json`)
- Chunk: ordinal 1 — heading `What is a bar chart?` — sha256_16 `e2fb6df3266bb2c8` — 963 chars
- Evidence quote (verbatim self-slice, markdown-safe): "What is a bar chart?
- A **bar chart** is a visual way to represent **discrete** data

  - Discrete data is data that can be **counted**
  
    - This can be **numerical **like** **shoe sizes in a class
    - Or **non-numerical **(categoric"
- Chunk excerpt: «What is a bar chart? - A **bar chart** is a visual way to represent **discrete** data - Discrete data is data that can be **counted** - This can be **numerical **like** **shoe sizes in a class - Or **non-numerical **(categorical) like colours of cars down a road - The **horizontal axis** shows the different **outcomes** - The **vertical axis** shows the **frequency** - The **heights** of the **bars **show the frequen»
- Upstream: T-C32 join notes/6-statistics-and-probability/statistics-toolkit/bar-charts-and-pictograms.json::spcpt_kHwc5r3247TGRwyS — tier S1_name_match — score 0.7253 — wording EXACT — validation tier AI_VALIDATED (operator-delegated chain)
- Rationale: SME span 'Bar Charts & Pictograms' on note 'Bar Charts & Pictograms' is anchored by the corpus spec_point block spcpt_kHwc5r3247TGRwyS and joined to 4MA1-6.1A via name_to_statement_join; this section chunk sits inside that span.
- Verdict: [ ] CONFIRM — this chunk belongs to this SP   [ ] REJECT — wrong chunk/SP   [ ] HOLD — needs rework

### 4MA1-2.5A — set up problems involving direct or inverse proportion and relate algebraic solutions to graphical representation of the equations
- Note: Inverse Proportion (`notes/1-numbers-and-the-number-system/direct-and-inverse-proportion/inverse-proportion.json`)
- Chunk: ordinal 2 — heading `How do I use inverse proportion with powers and roots?` — sha256_16 `07bd6da9deb1de52` — 701 chars
- Evidence quote (verbatim self-slice, markdown-safe): "How do I use inverse proportion with powers and roots?
- Problems may involve a variable* *being **inversely proportional** to a** power or root **of another variable
- For example

  - *y* is **inversely** proportional to the **square of *"
- Chunk excerpt: «How do I use inverse proportion with powers and roots? - Problems may involve a variable* *being **inversely proportional** to a** power or root **of another variable - For example - *y* is **inversely** proportional to the **square of *****x*** - * *$y\propto\frac{1}{x^{2}}$ - means that $y=\frac{k}{x^{2}}$ - *y* is** inversely** proportional to the **square root of *****x*** - $y\propto\frac{1}{\sqrt{x}}$ - means t»
- Upstream: T-C32 join notes/1-numbers-and-the-number-system/direct-and-inverse-proportion/inverse-proportion.json::spcpt_b7HzYMMwjGWQSz77 — tier S1_name_match — score 0.6973 — wording EXACT — validation tier AI_VALIDATED (operator-delegated chain)
- Rationale: SME span 'Inverse Proportion' on note 'Inverse Proportion' is anchored by the corpus spec_point block spcpt_b7HzYMMwjGWQSz77 and joined to 4MA1-2.5A via name_to_statement_join; this section chunk sits inside that span.
- Verdict: [ ] CONFIRM — this chunk belongs to this SP   [ ] REJECT — wrong chunk/SP   [ ] HOLD — needs rework

### 4MA1-2.7B — solve quadratic equations by using the quadratic formula or completing the square
- Note: The Quadratic Formula (`notes/2-equations-formulae-and-identities/solving-quadratic-equations/quadratic-formula.json`)
- Chunk: ordinal 1 — heading `What is the quadratic formula?` — sha256_16 `660cefb2fd77379f` — 401 chars
- Evidence quote (verbatim self-slice, markdown-safe): "What is the quadratic formula?
- A **quadratic equation** has the form *ax*<sup>2</sup> + *bx* + *c* = 0 (where *a* ≠ 0)

  - you need "**= 0**" on one side
- The **quadratic formula** is a formula that gives both solutions to a quadratic e"
- Chunk excerpt: «What is the quadratic formula? - A **quadratic equation** has the form *ax*<sup>2</sup> + *bx* + *c* = 0 (where *a* ≠ 0) - you need "**= 0**" on one side - The **quadratic formula** is a formula that gives both solutions to a quadratic equation: $x=\frac{-b\pm\sqrt{b^{2}-4ac}}{2a}$ Exam Hint: Make sure the quadratic equation has "= 0" on the right-hand side, otherwise it needs rearranging first.»
- Upstream: T-C32 join notes/2-equations-formulae-and-identities/solving-quadratic-equations/quadratic-formula.json::spcpt_JRX7QS29KrY2hCCW — tier S1_name_match — score 0.7388 — wording EXACT — validation tier AI_VALIDATED (operator-delegated chain)
- Rationale: SME span 'Quadratic Formula' on note 'The Quadratic Formula' is anchored by the corpus spec_point block spcpt_JRX7QS29KrY2hCCW and joined to 4MA1-2.7B via name_to_statement_join; this section chunk sits inside that span.
- Verdict: [ ] CONFIRM — this chunk belongs to this SP   [ ] REJECT — wrong chunk/SP   [ ] HOLD — needs rework

### 4MA1-5.2D — understand that reflections are specified by a mirror line
- Note: Reflections (`notes/5-vectors-and-transformation-geometry/transformations/reflections.json`)
- Chunk: ordinal 2 — heading `How do I reflect a shape?` — sha256_16 `e1b100421055e774` — 725 chars
- Evidence quote (verbatim self-slice, markdown-safe): "How do I reflect a shape?
- **STEP 1**
**Draw** the **line of reflection**

  - This will usually be a **vertical** line ($x=k$) or a **horizontal** line ($y=k$)
  - A **diagonal** line will either be $y=x$ or $y=-x$
- **STEP 2**
From **eac"
- Chunk excerpt: «How do I reflect a shape? - **STEP 1** **Draw** the **line of reflection** - This will usually be a **vertical** line ($x=k$) or a **horizontal** line ($y=k$) - A **diagonal** line will either be $y=x$ or $y=-x$ - **STEP 2** From **each vertex** on the **original object** measure the **perpendicular distance** to the **mirror line** - You can usually do this by **counting squares** on the grid - If the line is **diag»
- Upstream: T-C32 join notes/5-vectors-and-transformation-geometry/transformations/reflections.json::spcpt_DQrkJGG4Mngch9xc — tier S1_name_match — score 0.7275 — wording EXACT — validation tier AI_VALIDATED (operator-delegated chain)
- Rationale: SME span 'Reflections' on note 'Reflections' is anchored by the corpus spec_point block spcpt_DQrkJGG4Mngch9xc and joined to 4MA1-5.2D via name_to_statement_join; this section chunk sits inside that span.
- Verdict: [ ] CONFIRM — this chunk belongs to this SP   [ ] REJECT — wrong chunk/SP   [ ] HOLD — needs rework

### 4MA1-4.10F — convert between units of volume within the metric system
- Note: Volume (`notes/4-geometry-and-trigonometry/volume-and-surface-area/volume.json`)
- Chunk: ordinal 5 — heading `How do I find the volume of a cone?` — sha256_16 `70a633840b8d3d8c` — 362 chars
- Evidence quote (verbatim self-slice, markdown-safe): "How do I find the volume of a cone?
- To calculate the volume, *V*, of a **cone** with base radius, *r,* and perpendicular height, *h*, use the formula

  - $V=\frac{1}{3}πr^{2}h$
  - This formula is given to you in the exam
- The height mu"
- Chunk excerpt: «How do I find the volume of a cone? - To calculate the volume, *V*, of a **cone** with base radius, *r,* and perpendicular height, *h*, use the formula - $V=\frac{1}{3}πr^{2}h$ - This formula is given to you in the exam - The height must be a line from the top of the cone that is **perpendicular** to the base Cone volume, IGCSE & GCSE Maths revision notes»
- Upstream: T-C32 join notes/4-geometry-and-trigonometry/volume-and-surface-area/volume.json::spcpt_pKCFj25GzzqW6sr3 — tier S2_name_ambiguous — score 0.6774 — wording EXACT — validation tier AI_VALIDATED (operator-delegated chain)
- Rationale: SME span 'Volume' on note 'Volume' is anchored by the corpus spec_point block spcpt_pKCFj25GzzqW6sr3 and joined to 4MA1-4.10F via name_to_statement_join; this section chunk sits inside that span.
- Verdict: [ ] CONFIRM — this chunk belongs to this SP   [ ] REJECT — wrong chunk/SP   [ ] HOLD — needs rework

### 4MA1-4.4B — calculate time intervals in terms of the 24-hour and the 12-hour clock
- Note: Time (`notes/4-geometry-and-trigonometry/standard-and-compound-units/time.json`)
- Chunk: ordinal 0 — heading `Time` — sha256_16 `33b93476cf597a33` — 4 chars
- Evidence quote (verbatim self-slice, markdown-safe): "Time"
- Chunk excerpt: «Time»
- Upstream: T-C32 join notes/4-geometry-and-trigonometry/standard-and-compound-units/time.json::spcpt_h2p7nv6zkR4xFJ3P — tier S2_name_ambiguous — score 0.6432 — wording EXACT — validation tier AI_VALIDATED (operator-delegated chain)
- Rationale: SME span 'Time' on note 'Time' is anchored by the corpus spec_point block spcpt_h2p7nv6zkR4xFJ3P and joined to 4MA1-4.4B via name_to_statement_join; this section chunk sits inside that span.
- Verdict: [ ] CONFIRM — this chunk belongs to this SP   [ ] REJECT — wrong chunk/SP   [ ] HOLD — needs rework

### 4MA1-1.7B — divide a quantity in a given ratio or ratios
- Note: Introduction to Ratios (`notes/1-numbers-and-the-number-system/ratio-toolkit/simple-ratio.json`)
- Chunk: ordinal 6 — heading `How do I simplify a ratio?` — sha256_16 `4628be93b81459c4` — 1448 chars
- Evidence quote (verbatim self-slice, markdown-safe): "How do I simplify a ratio?
- **Divide each part** of the ratio by the **same** **value**

  - This value should be a **common factor** of all parts of the ratio
  
    - Ideally, the ***highest common factor*** **(HCF)** should be used to g"
- Chunk excerpt: «How do I simplify a ratio? - **Divide each part** of the ratio by the **same** **value** - This value should be a **common factor** of all parts of the ratio - Ideally, the ***highest common factor*** **(HCF)** should be used to get the ratio into its simplest form in one go - If the HCF is not used, we can repeat the process of simplifying - E.g. Divide all parts of the ratio **30 : 66 : 12** by 6 to find the ratio »
- Upstream: T-C32 join notes/1-numbers-and-the-number-system/ratio-toolkit/simple-ratio.json::spcpt_qpSmD6yNY5t5GrW6 — tier S1_name_match — score 0.696 — wording EXACT — validation tier AI_VALIDATED (operator-delegated chain)
- Rationale: SME span 'Ratios' on note 'Introduction to Ratios' is anchored by the corpus spec_point block spcpt_qpSmD6yNY5t5GrW6 and joined to 4MA1-1.7B via name_to_statement_join; this section chunk sits inside that span.
- Verdict: [ ] CONFIRM — this chunk belongs to this SP   [ ] REJECT — wrong chunk/SP   [ ] HOLD — needs rework

### 4MA1-3.4C — determine gradients, rates of change, stationary points, turning points (maxima and minima) by differentiation and relate these to graphs
- Note: Finding Stationary Points & Turning Points (`notes/3-sequences-functions-and-graphs/differentiation/applications-of-differentiation.json`)
- Chunk: ordinal 0 — heading `Finding stationary points & turning points` — sha256_16 `20f9a8d6b62d7509` — 42 chars
- Evidence quote (verbatim self-slice, markdown-safe): "Finding stationary points & turning points"
- Chunk excerpt: «Finding stationary points & turning points»
- Upstream: T-C32 join notes/3-sequences-functions-and-graphs/differentiation/applications-of-differentiation.json::spcpt_pKJ7Y3jd7PDzZQpP — tier S1_name_match — score 0.6293 — wording EXACT — validation tier AI_VALIDATED (operator-delegated chain)
- Rationale: SME span 'Finding Stationary Points & Turning Points' on note 'Finding Stationary Points & Turning Points' is anchored by the corpus spec_point block spcpt_pKJ7Y3jd7PDzZQpP and joined to 4MA1-3.4C via name_to_statement_join; this section chunk sits inside that span.
- Verdict: [ ] CONFIRM — this chunk belongs to this SP   [ ] REJECT — wrong chunk/SP   [ ] HOLD — needs rework

### 4MA1-4.2D — understand the term ‘regular polygon’ and calculate interior and exterior angles of regular polygons
- Note: Angles in Polygons (`notes/4-geometry-and-trigonometry/angles-in-polygons-and-parallel-lines/angles-in-polygons.json`)
- Chunk: ordinal 3 — heading `What is the sum of the interior angles in a polygon?` — sha256_16 `24f392352c5194e7` — 529 chars
- Evidence quote (verbatim self-slice, markdown-safe): "What is the sum of the interior angles in a polygon?
- To find the **sum of the** **interior angles **in a polygon of $n$ sides, use the rule

  - Sum of interior angles = $180^{\circ}\times(n--2)$
  
    - This formula comes from the fact "
- Chunk excerpt: «What is the sum of the interior angles in a polygon? - To find the **sum of the** **interior angles **in a polygon of $n$ sides, use the rule - Sum of interior angles = $180^{\circ}\times(n--2)$ - This formula comes from the fact that $n$-sided polygons can be split into $n-2$ triangles - **Remember** the sums for these polygons - The interior angles of a **triangle** add up to **180°** - The interior angles of a **q»
- Upstream: T-C32 join notes/4-geometry-and-trigonometry/angles-in-polygons-and-parallel-lines/angles-in-polygons.json::spcpt_gzykj64JBx2RtBJ7 — tier S2_name_ambiguous — score 0.7085 — wording EXACT — validation tier AI_VALIDATED (operator-delegated chain)
- Rationale: SME span 'Angles in Polygons' on note 'Angles in Polygons' is anchored by the corpus spec_point block spcpt_gzykj64JBx2RtBJ7 and joined to 4MA1-4.2D via name_to_statement_join; this section chunk sits inside that span.
- Verdict: [ ] CONFIRM — this chunk belongs to this SP   [ ] REJECT — wrong chunk/SP   [ ] HOLD — needs rework

### 4MA1-1.6F — use reverse percentages
- Note: Reverse Percentages (`notes/1-numbers-and-the-number-system/percentages/reverse-percentages.json`)
- Chunk: ordinal 1 — heading `What is a reverse percentage?` — sha256_16 `e9e882ed5a73bed0` — 362 chars
- Evidence quote (verbatim self-slice, markdown-safe): "What is a reverse percentage?
- A reverse percentage question is one where we are given the **value after a percentage increase or decrease** and asked to find the value **before** the change
Exam Hint: To spot a reverse percentage question"
- Chunk excerpt: «What is a reverse percentage? - A reverse percentage question is one where we are given the **value after a percentage increase or decrease** and asked to find the value **before** the change Exam Hint: To spot a reverse percentage question, see if you are being asked to find a quantity in the past. E.g. Find the **old** / **original** / **before** amount ...»
- Upstream: T-C32 join notes/1-numbers-and-the-number-system/percentages/reverse-percentages.json::spcpt_5CHMgxBWhBwxh5Y6 — tier S1_name_match — score 0.9619 — wording EXACT — validation tier AI_VALIDATED (operator-delegated chain)
- Rationale: SME span 'Reverse Percentages' on note 'Reverse Percentages' is anchored by the corpus spec_point block spcpt_5CHMgxBWhBwxh5Y6 and joined to 4MA1-1.6F via name_to_statement_join; this section chunk sits inside that span.
- Verdict: [ ] CONFIRM — this chunk belongs to this SP   [ ] REJECT — wrong chunk/SP   [ ] HOLD — needs rework

### 4MA1-3.3B — apply to the graph ofy = f(x)the transformations y = f(x) + a, y = f(ax), y = f(x + a), y = af(x) for linear, quadratic, sine and cosine functions
- Note: 2D Coordinates (`notes/3-sequences-functions-and-graphs/coordinate-geometry/coordinates.json`)
- Chunk: ordinal 0 — heading `2D coordinates` — sha256_16 `4987da584d1547c9` — 14 chars
- Evidence quote (verbatim self-slice, markdown-safe): "2D coordinates"
- Chunk excerpt: «2D coordinates»
- Upstream: T-C32 join notes/3-sequences-functions-and-graphs/coordinate-geometry/coordinates.json::spcpt_Jw35TTKhvXxmGGfP — tier S2_name_ambiguous — score 0.7268 — wording EXACT — validation tier AI_VALIDATED (operator-delegated chain)
- Rationale: SME span '2D Coordinates' on note '2D Coordinates' is anchored by the corpus spec_point block spcpt_Jw35TTKhvXxmGGfP and joined to 4MA1-3.3B via name_to_statement_join; this section chunk sits inside that span.
- Verdict: [ ] CONFIRM — this chunk belongs to this SP   [ ] REJECT — wrong chunk/SP   [ ] HOLD — needs rework

### 4MA1-5.1A — understand that a vector has both magnitude and direction
- Note: Magnitude of a Vector (`notes/5-vectors-and-transformation-geometry/vectors/magnitude-of-a-vector.json`)
- Chunk: ordinal 0 — heading `Magnitude of a vector` — sha256_16 `259ea5933a60f102` — 21 chars
- Evidence quote (verbatim self-slice, markdown-safe): "Magnitude of a vector"
- Chunk excerpt: «Magnitude of a vector»
- Upstream: T-C32 join notes/5-vectors-and-transformation-geometry/vectors/magnitude-of-a-vector.json::spcpt_vqmZYnJx9pH7mGMC — tier S1_name_match — score 0.7538 — wording EXACT — validation tier AI_VALIDATED (operator-delegated chain)
- Rationale: SME span 'Magnitude of a Vector' on note 'Magnitude of a Vector' is anchored by the corpus spec_point block spcpt_vqmZYnJx9pH7mGMC and joined to 4MA1-5.1A via name_to_statement_join; this section chunk sits inside that span.
- Verdict: [ ] CONFIRM — this chunk belongs to this SP   [ ] REJECT — wrong chunk/SP   [ ] HOLD — needs rework

### 4MA1-4.2F — understand congruence as meaning the same shape and size
- Note: Congruence (`notes/4-geometry-and-trigonometry/congruence-similarity-and-geometrical-proof/congruence.json`)
- Chunk: ordinal 2 — heading `How do we prove that two shapes are congruent?` — sha256_16 `48eb91d95c7291bb` — 920 chars
- Evidence quote (verbatim self-slice, markdown-safe): "How do we prove that two shapes are congruent?
- To show that two shapes are** congruent** you need to show that they are both the **same shape **and the **same size**

  - If a shape has been reflected, rotated or translated, then its imag"
- Chunk excerpt: «How do we prove that two shapes are congruent? - To show that two shapes are** congruent** you need to show that they are both the **same shape **and the **same size** - If a shape has been reflected, rotated or translated, then its image is** congruent **to it - Show that **corresponding sides** are the **same length** - Show that **corresponding angles** are the **same size** - You do **not **need to show that they»
- Upstream: T-C32 join notes/4-geometry-and-trigonometry/congruence-similarity-and-geometrical-proof/congruence.json::spcpt_3nz4CDxVDMqZNQNR — tier S1_name_match — score 0.7212 — wording EXACT — validation tier AI_VALIDATED (operator-delegated chain)
- Rationale: SME span 'Congruence' on note 'Congruence' is anchored by the corpus spec_point block spcpt_3nz4CDxVDMqZNQNR and joined to 4MA1-4.2F via name_to_statement_join; this section chunk sits inside that span.
- Verdict: [ ] CONFIRM — this chunk belongs to this SP   [ ] REJECT — wrong chunk/SP   [ ] HOLD — needs rework

### 4MA1-4.4G — use compound measure such as speed, density and pressure
- Note: Speed, Density & Pressure (`notes/4-geometry-and-trigonometry/standard-and-compound-units/speed-density-and-pressure.json`)
- Chunk: ordinal 3 — heading `What should I know about density, mass and volume?` — sha256_16 `87f8980f5d6d0299` — 445 chars
- Evidence quote (verbatim self-slice, markdown-safe): "What should I know about density, mass and volume?
- Density is usually measured in **grams per centimetre cubed** (**g/cm**<sup>**3**</sup>) or **kilograms per metre cubed** (**kg/m**<sup>**3**</sup>)

  - The units indicate that **density"
- Chunk excerpt: «What should I know about density, mass and volume? - Density is usually measured in **grams per centimetre cubed** (**g/cm**<sup>**3**</sup>) or **kilograms per metre cubed** (**kg/m**<sup>**3**</sup>) - The units indicate that **density** is **mass per volume** $\mathrm{Density}=\frac{\mathrm{Mass}}{\mathrm{Volume}}$ - You need to learn this formula - You may need to use a **volume formula** to find the volume of an»
- Upstream: T-C32 join notes/4-geometry-and-trigonometry/standard-and-compound-units/speed-density-and-pressure.json::spcpt_jJPhXSKYBg6x4d2Q — tier S1_name_match — score 0.8286 — wording EXACT — validation tier AI_VALIDATED (operator-delegated chain)
- Rationale: SME span 'Speed, Density & Pressure' on note 'Speed, Density & Pressure' is anchored by the corpus spec_point block spcpt_jJPhXSKYBg6x4d2Q and joined to 4MA1-4.4G via name_to_statement_join; this section chunk sits inside that span.
- Verdict: [ ] CONFIRM — this chunk belongs to this SP   [ ] REJECT — wrong chunk/SP   [ ] HOLD — needs rework

### 4MA1-3.3G — find the equation of a straight line parallel to a given line; find the equation of a straight line perpendicular to a given line
- Note: Gradient of a Line (`notes/3-sequences-functions-and-graphs/coordinate-geometry/gradient-of-a-line.json`)
- Chunk: ordinal 2 — heading `How do I find the gradient of a line?` — sha256_16 `1c28333dc089bbd9` — 779 chars
- Evidence quote (verbatim self-slice, markdown-safe): "How do I find the gradient of a line?
- Find** two points** on the line and draw a** right-angled triangle**

  - Then $\mathrm{gradient}=\frac{\mathrm{change} \mathrm{in}y}{\mathrm{change} \mathrm{in}x}$
  - Or, in short, $\frac{\mathrm{ri"
- Chunk excerpt: «How do I find the gradient of a line? - Find** two points** on the line and draw a** right-angled triangle** - Then $\mathrm{gradient}=\frac{\mathrm{change} \mathrm{in}y}{\mathrm{change} \mathrm{in}x}$ - Or, in short, $\frac{\mathrm{rise}}{\mathrm{run}}$ - The **rise** is the vertical length of the triangle - The **run** is the horizontal length of the triangle - Put the correct **sign** on your answer - **Positive *»
- Upstream: T-C32 join notes/3-sequences-functions-and-graphs/coordinate-geometry/gradient-of-a-line.json::spcpt_XhXhg6sRyMQ88chp — tier S1_name_match — score 0.8667 — wording EXACT — validation tier AI_VALIDATED (operator-delegated chain)
- Rationale: SME span 'Gradient of a Line' on note 'Gradient of a Line' is anchored by the corpus spec_point block spcpt_XhXhg6sRyMQ88chp and joined to 4MA1-3.3G via name_to_statement_join; this section chunk sits inside that span.
- Verdict: [ ] CONFIRM — this chunk belongs to this SP   [ ] REJECT — wrong chunk/SP   [ ] HOLD — needs rework

### 4MA1-3.3I — recognise, generate points and plot graphs of linear and quadratic functions
- Note: Quadratic Graphs (`notes/3-sequences-functions-and-graphs/graphs-of-functions/quadratic-graphs.json`)
- Chunk: ordinal 2 — heading `What does a quadratic graph look like?` — sha256_16 `659eeaf74284caca` — 919 chars
- Evidence quote (verbatim self-slice, markdown-safe): "What does a quadratic graph look like?
- A quadratic graph is a smooth curve with a **vertical line of symmetry**

  - A **positive** number in front of $x^{2}$ gives a **u-shaped curve**
  - A **negative **number in front of $x^{2}$ gives "
- Chunk excerpt: «What does a quadratic graph look like? - A quadratic graph is a smooth curve with a **vertical line of symmetry** - A **positive** number in front of $x^{2}$ gives a **u-shaped curve** - A **negative **number in front of $x^{2}$ gives an **n-shaped curve** - The shape made by a quadratic graph is known as a **parabola** - A quadratic graph will **always **cross the $y$**-axis** - A quadratic graph** **intersects the*»
- Upstream: T-C32 join notes/3-sequences-functions-and-graphs/graphs-of-functions/quadratic-graphs.json::spcpt_76gVqdMN62jnrZg6 — tier S1_name_match — score 0.6967 — wording EXACT — validation tier AI_VALIDATED (operator-delegated chain)
- Rationale: SME span 'Quadratic Graphs' on note 'Quadratic Graphs' is anchored by the corpus spec_point block spcpt_76gVqdMN62jnrZg6 and joined to 4MA1-3.3I via name_to_statement_join; this section chunk sits inside that span.
- Verdict: [ ] CONFIRM — this chunk belongs to this SP   [ ] REJECT — wrong chunk/SP   [ ] HOLD — needs rework

### 4MA1-4.1B — use angle properties of intersecting lines, parallel lines and angles on a straight line
- Note: Angles in Parallel Lines (`notes/4-geometry-and-trigonometry/angles-in-polygons-and-parallel-lines/angles-in-parallel-lines.json`)
- Chunk: ordinal 2 — heading `What are corresponding angles in parallel lines?` — sha256_16 `64750f12ac90b6fa` — 176 chars
- Evidence quote (verbatim self-slice, markdown-safe): "What are corresponding angles in parallel lines?
- Find **corresponding angles** by looking for an **F-shape**
- **Corresponding **angles** **are** equal**
Corresponding angles"
- Chunk excerpt: «What are corresponding angles in parallel lines? - Find **corresponding angles** by looking for an **F-shape** - **Corresponding **angles** **are** equal** Corresponding angles»
- Upstream: T-C32 join notes/4-geometry-and-trigonometry/angles-in-polygons-and-parallel-lines/angles-in-parallel-lines.json::spcpt_2SfTVFKHJRBby3QK — tier S1_name_match — score 0.773 — wording EXACT — validation tier AI_VALIDATED (operator-delegated chain)
- Rationale: SME span 'Angles in Parallel Lines' on note 'Angles in Parallel Lines' is anchored by the corpus spec_point block spcpt_2SfTVFKHJRBby3QK and joined to 4MA1-4.1B via name_to_statement_join; this section chunk sits inside that span.
- Verdict: [ ] CONFIRM — this chunk belongs to this SP   [ ] REJECT — wrong chunk/SP   [ ] HOLD — needs rework

### 4MA1-4.1B — use angle properties of intersecting lines, parallel lines and angles on a straight line
- Note: Angles in Parallel Lines (`notes/4-geometry-and-trigonometry/angles-in-polygons-and-parallel-lines/angles-in-parallel-lines.json`)
- Chunk: ordinal 3 — heading `What are alternate angles in parallel lines?` — sha256_16 `0acdfc6be381b31e` — 159 chars
- Evidence quote (verbatim self-slice, markdown-safe): "What are alternate angles in parallel lines?
- Find **alternate angles** by looking for a **Z-shape**
- **Alternate **angles** **are** equal**
Alternate angles"
- Chunk excerpt: «What are alternate angles in parallel lines? - Find **alternate angles** by looking for a **Z-shape** - **Alternate **angles** **are** equal** Alternate angles»
- Upstream: T-C32 join notes/4-geometry-and-trigonometry/angles-in-polygons-and-parallel-lines/angles-in-parallel-lines.json::spcpt_2SfTVFKHJRBby3QK — tier S1_name_match — score 0.773 — wording EXACT — validation tier AI_VALIDATED (operator-delegated chain)
- Rationale: SME span 'Angles in Parallel Lines' on note 'Angles in Parallel Lines' is anchored by the corpus spec_point block spcpt_2SfTVFKHJRBby3QK and joined to 4MA1-4.1B via name_to_statement_join; this section chunk sits inside that span.
- Verdict: [ ] CONFIRM — this chunk belongs to this SP   [ ] REJECT — wrong chunk/SP   [ ] HOLD — needs rework

### 4MA1-5.2H — understand and use column vectors in translations
- Note: Translations (`notes/5-vectors-and-transformation-geometry/transformations/translations.json`)
- Chunk: ordinal 3 — heading `What is a translation vector?` — sha256_16 `00f4d343e0fa71ec` — 611 chars
- Evidence quote (verbatim self-slice, markdown-safe): "What is a translation vector?
- The movement of a translation is described by a **vector**
- You need to know how to write a translation using a vector (rather than words)
- Vectors are written as **column vectors** in the form  `stretchy l"
- Chunk excerpt: «What is a translation vector? - The movement of a translation is described by a **vector** - You need to know how to write a translation using a vector (rather than words) - Vectors are written as **column vectors** in the form `stretchy left parenthesis table row bold italic x row bold italic y end table stretchy right parenthesis` where: - $x$ is the distance moved **horizontally** - **Negative** means move to the »
- Upstream: T-C32 join notes/5-vectors-and-transformation-geometry/transformations/translations.json::spcpt_YQX35KWR6v8thX5T — tier S1_name_match — score 0.7574 — wording EXACT — validation tier AI_VALIDATED (operator-delegated chain)
- Rationale: SME span 'Translations' on note 'Translations' is anchored by the corpus spec_point block spcpt_YQX35KWR6v8thX5T and joined to 4MA1-5.2H via name_to_statement_join; this section chunk sits inside that span.
- Verdict: [ ] CONFIRM — this chunk belongs to this SP   [ ] REJECT — wrong chunk/SP   [ ] HOLD — needs rework

### 4MA1-3.4E — apply calculus to linear kinematics and to other simple practical problems
- Note: Using Differentiation for Kinematics (`notes/3-sequences-functions-and-graphs/differentiation/kinematics.json`)
- Chunk: ordinal 6 — heading `How do I find the acceleration from the displacement?` — sha256_16 `5fefe11c05133567` — 2368 chars
- Evidence quote (verbatim self-slice, markdown-safe): "How do I find the acceleration from the displacement?
- You **differentiate displacement** to get **velocity**, then **differentiate velocity** to get **acceleration**

  - So you differentiate displacement twice to get acceleration
Diagram"
- Chunk excerpt: «How do I find the acceleration from the displacement? - You **differentiate displacement** to get **velocity**, then **differentiate velocity** to get **acceleration** - So you differentiate displacement twice to get acceleration Diagram showing the relationship between displacement (s), velocity (v), and acceleration (a), with differentiation denoted as ds/dt for velocity and dv/dt for acceleration. Exam Hint: - Har»
- Upstream: T-C32 join notes/3-sequences-functions-and-graphs/differentiation/kinematics.json::spcpt_vYsrWKqpQDpSwnPj — tier S1_name_match — score 0.6952 — wording EXACT — validation tier AI_VALIDATED (operator-delegated chain)
- Rationale: SME span 'Kinematics' on note 'Using Differentiation for Kinematics' is anchored by the corpus spec_point block spcpt_vYsrWKqpQDpSwnPj and joined to 4MA1-3.4E via name_to_statement_join; this section chunk sits inside that span.
- Verdict: [ ] CONFIRM — this chunk belongs to this SP   [ ] REJECT — wrong chunk/SP   [ ] HOLD — needs rework

### 4MA1-1.7B — divide a quantity in a given ratio or ratios
- Note: Introduction to Ratios (`notes/1-numbers-and-the-number-system/ratio-toolkit/simple-ratio.json`)
- Chunk: ordinal 2 — heading `What do ratios look like?` — sha256_16 `00850dae023793cb` — 1833 chars
- Evidence quote (verbatim self-slice, markdown-safe): "What do ratios look like?
- Ratios involve **two or three different numbers **separated using a **colon**

  - E.g. 2 : 5,  3 : 1,  4 : 2 : 3
- In all ratio questions, who or what is **mentioned first** in the question, will be associated w"
- Chunk excerpt: «What do ratios look like? - Ratios involve **two or three different numbers **separated using a **colon** - E.g. 2 : 5, 3 : 1, 4 : 2 : 3 - In all ratio questions, who or what is **mentioned first** in the question, will be associated with the **first part of the ratio** - E.g. The cake recipe with flour and butter in the ratio 2 : 1 - 'Flour' is associated with '2' and 'butter' is associated with '1' - The numbers in»
- Upstream: T-C32 join notes/1-numbers-and-the-number-system/ratio-toolkit/simple-ratio.json::spcpt_qpSmD6yNY5t5GrW6 — tier S1_name_match — score 0.696 — wording EXACT — validation tier AI_VALIDATED (operator-delegated chain)
- Rationale: SME span 'Ratios' on note 'Introduction to Ratios' is anchored by the corpus spec_point block spcpt_qpSmD6yNY5t5GrW6 and joined to 4MA1-1.7B via name_to_statement_join; this section chunk sits inside that span.
- Verdict: [ ] CONFIRM — this chunk belongs to this SP   [ ] REJECT — wrong chunk/SP   [ ] HOLD — needs rework

### 4MA1-6.1C — use cumulative frequency diagrams
- Note: Comparing Statistical Diagrams (`notes/6-statistics-and-probability/statistics-toolkit/comparing-statistical-diagrams.json`)
- Chunk: ordinal 0 — heading `Comparing statistical diagrams` — sha256_16 `daf72b12c8bb285f` — 30 chars
- Evidence quote (verbatim self-slice, markdown-safe): "Comparing statistical diagrams"
- Chunk excerpt: «Comparing statistical diagrams»
- Upstream: T-C32 join notes/6-statistics-and-probability/statistics-toolkit/comparing-statistical-diagrams.json::spcpt_nXY9n4Vt3cVTmKcR — tier S1_name_match — score 0.7067 — wording EXACT — validation tier AI_VALIDATED (operator-delegated chain)
- Rationale: SME span 'Comparing Statistical Diagrams' on note 'Comparing Statistical Diagrams' is anchored by the corpus spec_point block spcpt_nXY9n4Vt3cVTmKcR and joined to 4MA1-6.1C via name_to_statement_join; this section chunk sits inside that span.
- Verdict: [ ] CONFIRM — this chunk belongs to this SP   [ ] REJECT — wrong chunk/SP   [ ] HOLD — needs rework

### 4MA1-4.1B — use angle properties of intersecting lines, parallel lines and angles on a straight line
- Note: Angles in Parallel Lines (`notes/4-geometry-and-trigonometry/angles-in-polygons-and-parallel-lines/angles-in-parallel-lines.json`)
- Chunk: ordinal 0 — heading `Angles in parallel lines` — sha256_16 `8ee00447a4289566` — 24 chars
- Evidence quote (verbatim self-slice, markdown-safe): "Angles in parallel lines"
- Chunk excerpt: «Angles in parallel lines»
- Upstream: T-C32 join notes/4-geometry-and-trigonometry/angles-in-polygons-and-parallel-lines/angles-in-parallel-lines.json::spcpt_2SfTVFKHJRBby3QK — tier S1_name_match — score 0.773 — wording EXACT — validation tier AI_VALIDATED (operator-delegated chain)
- Rationale: SME span 'Angles in Parallel Lines' on note 'Angles in Parallel Lines' is anchored by the corpus spec_point block spcpt_2SfTVFKHJRBby3QK and joined to 4MA1-4.1B via name_to_statement_join; this section chunk sits inside that span.
- Verdict: [ ] CONFIRM — this chunk belongs to this SP   [ ] REJECT — wrong chunk/SP   [ ] HOLD — needs rework

### 4MA1-1.10C — understand and carry out calculations using time, and carry out calculations using money, including converting between currencies
- Note: Money Calculations (`notes/1-numbers-and-the-number-system/number-toolkit/money-calculations.json`)
- Chunk: ordinal 3 — heading `How should I round values in a money calculation?` — sha256_16 `1ea658ae989af429` — 894 chars
- Evidence quote (verbatim self-slice, markdown-safe): "How should I round values in a money calculation?
- Many currencies will be rounded to **two decimal places**

  - Dollars, pounds and euro should all be used to two decimal places
  - Always write** down** **both decimal places**, even if "
- Chunk excerpt: «How should I round values in a money calculation? - Many currencies will be rounded to **two decimal places** - Dollars, pounds and euro should all be used to two decimal places - Always write** down** **both decimal places**, even if the second is zero - This is particularly important when using a** calculator** - 1.4 pounds on a calculator should be written as £1.40 - For a question involving **large numbers** such»
- Upstream: T-C32 join notes/1-numbers-and-the-number-system/number-toolkit/money-calculations.json::spcpt_bMYrxtVc2SZgt8mX — tier S1_name_match — score 0.6772 — wording EXACT — validation tier AI_VALIDATED (operator-delegated chain)
- Rationale: SME span 'Money Calculations' on note 'Money Calculations' is anchored by the corpus spec_point block spcpt_bMYrxtVc2SZgt8mX and joined to 4MA1-1.10C via name_to_statement_join; this section chunk sits inside that span.
- Verdict: [ ] CONFIRM — this chunk belongs to this SP   [ ] REJECT — wrong chunk/SP   [ ] HOLD — needs rework

### 4MA1-1.2B — understand and use mixed numbers and vulgar fractions
- Note: Mixed Numbers & Improper Fractions (`notes/1-numbers-and-the-number-system/fractions/mixed-numbers-and-improper-fractions.json`)
- Chunk: ordinal 3 — heading `How do I convert an improper fraction into a mixed number?` — sha256_16 `28589abb63bb0bae` — 1021 chars
- Evidence quote (verbatim self-slice, markdown-safe): "How do I convert an improper fraction into a mixed number?
- **Divide** the numerator by the bottom

  - For example, convert $\frac{22}{3}$ into a mixed number
  - $22\div3=7$ remainder $1$
- The **integer part** of the mixed number is the"
- Chunk excerpt: «How do I convert an improper fraction into a mixed number? - **Divide** the numerator by the bottom - For example, convert $\frac{22}{3}$ into a mixed number - $22\div3=7$ remainder $1$ - The **integer part** of the mixed number is the **whole number** - The **fraction part** is the **remainder** over the denominator - $\frac{22}{3}=7\frac{1}{3}$ Exam Hint: In your exam, you have a calculator. You can use this to con»
- Upstream: T-C32 join notes/1-numbers-and-the-number-system/fractions/mixed-numbers-and-improper-fractions.json::spcpt_6XysCMWvYY936jw8 — tier S1_name_match — score 0.6853 — wording EXACT — validation tier AI_VALIDATED (operator-delegated chain)
- Rationale: SME span 'Mixed Numbers & Improper Fractions' on note 'Mixed Numbers & Improper Fractions' is anchored by the corpus spec_point block spcpt_6XysCMWvYY936jw8 and joined to 4MA1-1.2B via name_to_statement_join; this section chunk sits inside that span.
- Verdict: [ ] CONFIRM — this chunk belongs to this SP   [ ] REJECT — wrong chunk/SP   [ ] HOLD — needs rework

### 4MA1-3.3F — calculate the gradient of a straight line given the coordinates of two points
- Note: Conversion Graphs (`notes/3-sequences-functions-and-graphs/real-life-graphs/conversion-graphs.json`)
- Chunk: ordinal 0 — heading `Conversion graphs` — sha256_16 `50d2e616e30f8dca` — 17 chars
- Evidence quote (verbatim self-slice, markdown-safe): "Conversion graphs"
- Chunk excerpt: «Conversion graphs»
- Upstream: T-C32 join notes/3-sequences-functions-and-graphs/real-life-graphs/conversion-graphs.json::spcpt_Nh8WWWGQxmJGVvvf — tier S1_name_match — score 0.803 — wording EXACT — validation tier AI_VALIDATED (operator-delegated chain)
- Rationale: SME span 'Conversion Graphs' on note 'Conversion Graphs' is anchored by the corpus spec_point block spcpt_Nh8WWWGQxmJGVvvf and joined to 4MA1-3.3F via name_to_statement_join; this section chunk sits inside that span.
- Verdict: [ ] CONFIRM — this chunk belongs to this SP   [ ] REJECT — wrong chunk/SP   [ ] HOLD — needs rework

### 4MA1-4.5C — solve problems using scale drawings
- Note: Scale (`notes/4-geometry-and-trigonometry/bearings-scale-drawing-and-constructions/scale.json`)
- Chunk: ordinal 5 — heading `How can I use a scale to find lengths for an accurate drawing?` — sha256_16 `ddaf4d78189cd61c` — 669 chars
- Evidence quote (verbatim self-slice, markdown-safe): "How can I use a scale to find lengths for an accurate drawing?
- A scale can be used to produce an accurate drawing or model of an object
- **STEP 1**
**Convert** the scale into a **ratio** where one side is **1 cm** and the other side uses"
- Chunk excerpt: «How can I use a scale to find lengths for an accurate drawing? - A scale can be used to produce an accurate drawing or model of an object - **STEP 1** **Convert** the scale into a **ratio** where one side is **1 cm** and the other side uses the **units the real distance** is measured in - For example, if the real distance is in km and the scale is 1 : 500 000, - 1 : 500 000 = 1 cm : 500 000 cm = 1 cm : 5 000 m = 1 cm»
- Upstream: T-C32 join notes/4-geometry-and-trigonometry/bearings-scale-drawing-and-constructions/scale.json::spcpt_D6T5FMtYgmDGKKXB — tier S2_name_ambiguous — score 0.8286 — wording EXACT — validation tier AI_VALIDATED (operator-delegated chain)
- Rationale: SME span 'Scale Drawings' on note 'Scale' is anchored by the corpus spec_point block spcpt_D6T5FMtYgmDGKKXB and joined to 4MA1-4.5C via name_to_statement_join; this section chunk sits inside that span.
- Verdict: [ ] CONFIRM — this chunk belongs to this SP   [ ] REJECT — wrong chunk/SP   [ ] HOLD — needs rework

### 4MA1-2.5A — set up problems involving direct or inverse proportion and relate algebraic solutions to graphical representation of the equations
- Note: Inverse Proportion (`notes/1-numbers-and-the-number-system/direct-and-inverse-proportion/inverse-proportion.json`)
- Chunk: ordinal 0 — heading `Inverse proportion` — sha256_16 `635aaac4b4dfcf99` — 18 chars
- Evidence quote (verbatim self-slice, markdown-safe): "Inverse proportion"
- Chunk excerpt: «Inverse proportion»
- Upstream: T-C32 join notes/1-numbers-and-the-number-system/direct-and-inverse-proportion/inverse-proportion.json::spcpt_b7HzYMMwjGWQSz77 — tier S1_name_match — score 0.6973 — wording EXACT — validation tier AI_VALIDATED (operator-delegated chain)
- Rationale: SME span 'Inverse Proportion' on note 'Inverse Proportion' is anchored by the corpus spec_point block spcpt_b7HzYMMwjGWQSz77 and joined to 4MA1-2.5A via name_to_statement_join; this section chunk sits inside that span.
- Verdict: [ ] CONFIRM — this chunk belongs to this SP   [ ] REJECT — wrong chunk/SP   [ ] HOLD — needs rework

### 4MA1-3.3G — find the equation of a straight line parallel to a given line; find the equation of a straight line perpendicular to a given line
- Note: Gradient of a Line (`notes/3-sequences-functions-and-graphs/coordinate-geometry/gradient-of-a-line.json`)
- Chunk: ordinal 0 — heading `Gradient of a line` — sha256_16 `e194a25332023875` — 18 chars
- Evidence quote (verbatim self-slice, markdown-safe): "Gradient of a line"
- Chunk excerpt: «Gradient of a line»
- Upstream: T-C32 join notes/3-sequences-functions-and-graphs/coordinate-geometry/gradient-of-a-line.json::spcpt_XhXhg6sRyMQ88chp — tier S1_name_match — score 0.8667 — wording EXACT — validation tier AI_VALIDATED (operator-delegated chain)
- Rationale: SME span 'Gradient of a Line' on note 'Gradient of a Line' is anchored by the corpus spec_point block spcpt_XhXhg6sRyMQ88chp and joined to 4MA1-3.3G via name_to_statement_join; this section chunk sits inside that span.
- Verdict: [ ] CONFIRM — this chunk belongs to this SP   [ ] REJECT — wrong chunk/SP   [ ] HOLD — needs rework

### 4MA1-1.6F — use reverse percentages
- Note: Reverse Percentages (`notes/1-numbers-and-the-number-system/percentages/reverse-percentages.json`)
- Chunk: ordinal 0 — heading `Reverse percentages` — sha256_16 `487aee2909961455` — 19 chars
- Evidence quote (verbatim self-slice, markdown-safe): "Reverse percentages"
- Chunk excerpt: «Reverse percentages»
- Upstream: T-C32 join notes/1-numbers-and-the-number-system/percentages/reverse-percentages.json::spcpt_5CHMgxBWhBwxh5Y6 — tier S1_name_match — score 0.9619 — wording EXACT — validation tier AI_VALIDATED (operator-delegated chain)
- Rationale: SME span 'Reverse Percentages' on note 'Reverse Percentages' is anchored by the corpus spec_point block spcpt_5CHMgxBWhBwxh5Y6 and joined to 4MA1-1.6F via name_to_statement_join; this section chunk sits inside that span.
- Verdict: [ ] CONFIRM — this chunk belongs to this SP   [ ] REJECT — wrong chunk/SP   [ ] HOLD — needs rework

### 4MA1-4.5C — solve problems using scale drawings
- Note: Scale (`notes/4-geometry-and-trigonometry/bearings-scale-drawing-and-constructions/scale.json`)
- Chunk: ordinal 4 — heading `Scale drawings` — sha256_16 `9a9c03ba55c03708` — 14 chars
- Evidence quote (verbatim self-slice, markdown-safe): "Scale drawings"
- Chunk excerpt: «Scale drawings»
- Upstream: T-C32 join notes/4-geometry-and-trigonometry/bearings-scale-drawing-and-constructions/scale.json::spcpt_D6T5FMtYgmDGKKXB — tier S2_name_ambiguous — score 0.8286 — wording EXACT — validation tier AI_VALIDATED (operator-delegated chain)
- Rationale: SME span 'Scale Drawings' on note 'Scale' is anchored by the corpus spec_point block spcpt_D6T5FMtYgmDGKKXB and joined to 4MA1-4.5C via name_to_statement_join; this section chunk sits inside that span.
- Verdict: [ ] CONFIRM — this chunk belongs to this SP   [ ] REJECT — wrong chunk/SP   [ ] HOLD — needs rework

### 4MA1-2.7B — solve quadratic equations by using the quadratic formula or completing the square
- Note: Solving by Completing the Square (`notes/2-equations-formulae-and-identities/solving-quadratic-equations/solving-by-completing-the-square.json`)
- Chunk: ordinal 1 — heading `How do I solve a quadratic equation by completing the square?` — sha256_16 `7060aa6b349de5b0` — 1279 chars
- Evidence quote (verbatim self-slice, markdown-safe): "How do I solve a quadratic equation by completing the square?
- To solve *x*<sup>2</sup> + *bx *+* c* = 0

  - **replace** the first two terms, ***x***<sup>**2**</sup>** + *****bx***, with **(*****x***** + *****p*****)**<sup>**2**</sup>** -"
- Chunk excerpt: «How do I solve a quadratic equation by completing the square? - To solve *x*<sup>2</sup> + *bx *+* c* = 0 - **replace** the first two terms, ***x***<sup>**2**</sup>** + *****bx***, with **(*****x***** + *****p*****)**<sup>**2**</sup>** - *****p***<sup>**2**</sup> where ***p***** is half of *****b*** - This is** completing the square** - *x*<sup>2</sup> + *bx *+* c* = 0 becomes (*x* + *p*)<sup>2</sup> - *p*<sup>2</sup»
- Upstream: T-C32 join notes/2-equations-formulae-and-identities/solving-quadratic-equations/solving-by-completing-the-square.json::spcpt_W2v94nxskTtpWxWd — tier S1_name_match — score 0.6624 — wording EXACT — validation tier AI_VALIDATED (operator-delegated chain)
- Rationale: SME span 'Solving by Completing the Square' on note 'Solving by Completing the Square' is anchored by the corpus spec_point block spcpt_W2v94nxskTtpWxWd and joined to 4MA1-2.7B via name_to_statement_join; this section chunk sits inside that span.
- Verdict: [ ] CONFIRM — this chunk belongs to this SP   [ ] REJECT — wrong chunk/SP   [ ] HOLD — needs rework

### 4MA1-4.4D — understand angle measure including three-figure bearings
- Note: Bearings (`notes/4-geometry-and-trigonometry/bearings-scale-drawing-and-constructions/bearings.json`)
- Chunk: ordinal 3 — heading `How do I draw a point on a bearing?` — sha256_16 `df88dbb9ec04a60a` — 501 chars
- Evidence quote (verbatim self-slice, markdown-safe): "How do I draw a point on a bearing?
- You might be asked to plot a point that is a **given distance** from another point and on a **given bearing**
- **STEP 1**
Draw a **North line** at the point you wish to measure the bearing **from**

  "
- Chunk excerpt: «How do I draw a point on a bearing? - You might be asked to plot a point that is a **given distance** from another point and on a **given bearing** - **STEP 1** Draw a **North line** at the point you wish to measure the bearing **from** - If you are given the bearing **from A to B **draw the North line at **A** - **STEP 2** Measure the **angle** of the bearing given **from the North line** in the **clockwise directio»
- Upstream: T-C32 join notes/4-geometry-and-trigonometry/bearings-scale-drawing-and-constructions/bearings.json::spcpt_38XcCSfT6hW33fDn — tier S1_name_match — score 0.7 — wording EXACT — validation tier AI_VALIDATED (operator-delegated chain)
- Rationale: SME span 'Bearings' on note 'Bearings' is anchored by the corpus spec_point block spcpt_38XcCSfT6hW33fDn and joined to 4MA1-4.4D via name_to_statement_join; this section chunk sits inside that span.
- Verdict: [ ] CONFIRM — this chunk belongs to this SP   [ ] REJECT — wrong chunk/SP   [ ] HOLD — needs rework

### 4MA1-1.10C — understand and carry out calculations using time, and carry out calculations using money, including converting between currencies
- Note: Money Calculations (`notes/1-numbers-and-the-number-system/number-toolkit/money-calculations.json`)
- Chunk: ordinal 0 — heading `Money calculations` — sha256_16 `aab6edf0c75ec13b` — 18 chars
- Evidence quote (verbatim self-slice, markdown-safe): "Money calculations"
- Chunk excerpt: «Money calculations»
- Upstream: T-C32 join notes/1-numbers-and-the-number-system/number-toolkit/money-calculations.json::spcpt_bMYrxtVc2SZgt8mX — tier S1_name_match — score 0.6772 — wording EXACT — validation tier AI_VALIDATED (operator-delegated chain)
- Rationale: SME span 'Money Calculations' on note 'Money Calculations' is anchored by the corpus spec_point block spcpt_bMYrxtVc2SZgt8mX and joined to 4MA1-1.10C via name_to_statement_join; this section chunk sits inside that span.
- Verdict: [ ] CONFIRM — this chunk belongs to this SP   [ ] REJECT — wrong chunk/SP   [ ] HOLD — needs rework

### 4MA1-2.2B — understand the concept of a quadratic expression and be able to factorise such expressions
- Note: Collecting Like Terms (`notes/2-equations-formulae-and-identities/algebra-toolkit/collecting-like-terms.json`)
- Chunk: ordinal 1 — heading `What happens if there is more than one term?` — sha256_16 `03e9c54eca15d506` — 892 chars
- Evidence quote (verbatim self-slice, markdown-safe): "What happens if there is more than one term?
- **Terms** can be **added** and **subtracted **
- The** numbers **in front of the letters are called** coefficients**

  - If the coefficient is 1 or -1, then it is conventional not to write the"
- Chunk excerpt: «What happens if there is more than one term? - **Terms** can be **added** and **subtracted ** - The** numbers **in front of the letters are called** coefficients** - If the coefficient is 1 or -1, then it is conventional not to write the 1 - The coefficient of *x* is 1 - The coefficient of -*y* s -1 - Each term has a positive or negative** sign** in front - In 2*x* - 3*y *the coefficient of *x* is 2 (positive) and th»
- Upstream: T-C32 join notes/2-equations-formulae-and-identities/algebra-toolkit/collecting-like-terms.json::spcpt_rsCdKqXKjhfmkyqT — tier S1_name_match — score 0.7692 — wording EXACT — validation tier AI_VALIDATED (operator-delegated chain)
- Rationale: SME span 'Collecting Like Terms' on note 'Collecting Like Terms' is anchored by the corpus spec_point block spcpt_rsCdKqXKjhfmkyqT and joined to 4MA1-2.2B via name_to_statement_join; this section chunk sits inside that span.
- Verdict: [ ] CONFIRM — this chunk belongs to this SP   [ ] REJECT — wrong chunk/SP   [ ] HOLD — needs rework

### 4MA1-5.2K — understand that enlargements preserve angles and not lengths
- Note: Enlargements (`notes/5-vectors-and-transformation-geometry/transformations/enlargements.json`)
- Chunk: ordinal 0 — heading `Enlargements` — sha256_16 `7ab3fb5f70162ac1` — 12 chars
- Evidence quote (verbatim self-slice, markdown-safe): "Enlargements"
- Chunk excerpt: «Enlargements»
- Upstream: T-C32 join notes/5-vectors-and-transformation-geometry/transformations/enlargements.json::spcpt_c3ZTz62W4HKyb4zk — tier S2_name_ambiguous — score 0.7333 — wording EXACT — validation tier AI_VALIDATED (operator-delegated chain)
- Rationale: SME span 'Enlargements' on note 'Enlargements' is anchored by the corpus spec_point block spcpt_c3ZTz62W4HKyb4zk and joined to 4MA1-5.2K via name_to_statement_join; this section chunk sits inside that span.
- Verdict: [ ] CONFIRM — this chunk belongs to this SP   [ ] REJECT — wrong chunk/SP   [ ] HOLD — needs rework

### 4MA1-2.2B — understand the concept of a quadratic expression and be able to factorise such expressions
- Note: Collecting Like Terms (`notes/2-equations-formulae-and-identities/algebra-toolkit/collecting-like-terms.json`)
- Chunk: ordinal 3 — heading `How do I collect like terms?` — sha256_16 `f08436607baae89e` — 867 chars
- Evidence quote (verbatim self-slice, markdown-safe): "How do I collect like terms?
- **Collecting like terms **means simplifying by **adding** or **subtracting **the **coefficients**

  - 2*x* + 3*x*  becomes 5*x*
  - 4*y* - 10*y * becomes -6*y*
  
    - A negative sign is needed here
- If the"
- Chunk excerpt: «How do I collect like terms? - **Collecting like terms **means simplifying by **adding** or **subtracting **the **coefficients** - 2*x* + 3*x* becomes 5*x* - 4*y* - 10*y * becomes -6*y* - A negative sign is needed here - If there are **different** **types **of like terms, **collect** them **separately** - For 2*x* + 4*y* + 5*x* - 3*y* - Collecting the *x*'s gives 2*x* + 5*x* = 7*x* - Collecting the *y*'s gives 4*y* -»
- Upstream: T-C32 join notes/2-equations-formulae-and-identities/algebra-toolkit/collecting-like-terms.json::spcpt_rsCdKqXKjhfmkyqT — tier S1_name_match — score 0.7692 — wording EXACT — validation tier AI_VALIDATED (operator-delegated chain)
- Rationale: SME span 'Collecting Like Terms' on note 'Collecting Like Terms' is anchored by the corpus spec_point block spcpt_rsCdKqXKjhfmkyqT and joined to 4MA1-2.2B via name_to_statement_join; this section chunk sits inside that span.
- Verdict: [ ] CONFIRM — this chunk belongs to this SP   [ ] REJECT — wrong chunk/SP   [ ] HOLD — needs rework

### 4MA1-4.10F — convert between units of volume within the metric system
- Note: Volume (`notes/4-geometry-and-trigonometry/volume-and-surface-area/volume.json`)
- Chunk: ordinal 2 — heading `How do I find the volume of a cube or a cuboid?` — sha256_16 `de3a3087ed82e135` — 507 chars
- Evidence quote (verbatim self-slice, markdown-safe): "How do I find the volume of a cube or a cuboid?
- A **cube** is a special **cuboid**, where the length, width and height are all of **equal length**
- A** cuboid** is another name for a rectangular-based **prism**
- To find the volume, *V*,"
- Chunk excerpt: «How do I find the volume of a cube or a cuboid? - A **cube** is a special **cuboid**, where the length, width and height are all of **equal length** - A** cuboid** is another name for a rectangular-based **prism** - To find the volume, *V*, of a **cube** or a **cuboid**, with length, *l*, width, *w*, and height, *h*, use the formula - $V=lwh$ - This formula is **not** given to you in the exam Volume of a cuboid - You»
- Upstream: T-C32 join notes/4-geometry-and-trigonometry/volume-and-surface-area/volume.json::spcpt_pKCFj25GzzqW6sr3 — tier S2_name_ambiguous — score 0.6774 — wording EXACT — validation tier AI_VALIDATED (operator-delegated chain)
- Rationale: SME span 'Volume' on note 'Volume' is anchored by the corpus spec_point block spcpt_pKCFj25GzzqW6sr3 and joined to 4MA1-4.10F via name_to_statement_join; this section chunk sits inside that span.
- Verdict: [ ] CONFIRM — this chunk belongs to this SP   [ ] REJECT — wrong chunk/SP   [ ] HOLD — needs rework

### 4MA1-3.1C — find the sum of the firstnterms of an arithmetic series(Sn)
- Note: Arithmetic Sequences (`notes/3-sequences-functions-and-graphs/sequences/arithmetic-sequences.json`)
- Chunk: ordinal 2 — heading `What is the formula for the nth term of an arithmetic sequence?` — sha256_16 `24a5c9c0457fbbff` — 376 chars
- Evidence quote (verbatim self-slice, markdown-safe): "What is the formula for the nth term of an arithmetic sequence?
- The** formula **for the $n$<sup>th</sup> term of an arithmetic sequence is `u subscript n equals a plus open parentheses n minus 1 close parentheses d`

  - $a$ is the **firs"
- Chunk excerpt: «What is the formula for the nth term of an arithmetic sequence? - The** formula **for the $n$<sup>th</sup> term of an arithmetic sequence is `u subscript n equals a plus open parentheses n minus 1 close parentheses d` - $a$ is the **first term** - $d$ is the **common difference** - $u_{n}$ is the $n$<sup>th</sup> term - e.g. $n=5$ gives the fifth term, $u_{5}$»
- Upstream: T-C32 join notes/3-sequences-functions-and-graphs/sequences/arithmetic-sequences.json::spcpt_fhF2H4HM3cxqsGdd — tier S1_name_match — score 0.7758 — wording EXACT — validation tier AI_VALIDATED (operator-delegated chain)
- Rationale: SME span 'Arithmetic Sequences' on note 'Arithmetic Sequences' is anchored by the corpus spec_point block spcpt_fhF2H4HM3cxqsGdd and joined to 4MA1-3.1C via name_to_statement_join; this section chunk sits inside that span.
- Verdict: [ ] CONFIRM — this chunk belongs to this SP   [ ] REJECT — wrong chunk/SP   [ ] HOLD — needs rework

### 4MA1-4.10D — find the surface area of a cylinder
- Note: Surface Area (`notes/4-geometry-and-trigonometry/volume-and-surface-area/surface-area.json`)
- Chunk: ordinal 0 — heading `Surface area` — sha256_16 `05ba10a2667aa584` — 12 chars
- Evidence quote (verbatim self-slice, markdown-safe): "Surface area"
- Chunk excerpt: «Surface area»
- Upstream: T-C32 join notes/4-geometry-and-trigonometry/volume-and-surface-area/surface-area.json::spcpt_2w9hbV5pTbvc5Smj — tier S1_name_match — score 0.8043 — wording EXACT — validation tier AI_VALIDATED (operator-delegated chain)
- Rationale: SME span 'Surface Area' on note 'Surface Area' is anchored by the corpus spec_point block spcpt_2w9hbV5pTbvc5Smj and joined to 4MA1-4.10D via name_to_statement_join; this section chunk sits inside that span.
- Verdict: [ ] CONFIRM — this chunk belongs to this SP   [ ] REJECT — wrong chunk/SP   [ ] HOLD — needs rework

### 4MA1-2.7D — solve simultaneous equations in two unknowns, one equation being linear and the other being quadratic
- Note: Quadratic Simultaneous Equations (`notes/2-equations-formulae-and-identities/simultaneous-equations/quadratic.json`)
- Chunk: ordinal 2 — heading `How do I use a graph to solve quadratic simultaneous equations?` — sha256_16 `2101f9e681a2da00` — 737 chars
- Evidence quote (verbatim self-slice, markdown-safe): "How do I use a graph to solve quadratic simultaneous equations?
- **Plot** both equations on the same set of axes

  - To do this, you can use a table of values
  - Or for straight lines it can help to rearrange into *y* = *mx* + *c*
- Find"
- Chunk excerpt: «How do I use a graph to solve quadratic simultaneous equations? - **Plot** both equations on the same set of axes - To do this, you can use a table of values - Or for straight lines it can help to rearrange into *y* = *mx* + *c* - Find the point where the lines **intersect** - The *x* and *y ***solutions** to the simultaneous equations are the *x *and *y ***coordinates** of the point of **intersection** - E.g. To sol»
- Upstream: T-C32 join notes/2-equations-formulae-and-identities/simultaneous-equations/quadratic.json::spcpt_pGsqq7xcztBg59Yh — tier S1_name_match — score 0.7394 — wording EXACT — validation tier AI_VALIDATED (operator-delegated chain)
- Rationale: SME span 'Quadratic Simultaneous Equations' on note 'Quadratic Simultaneous Equations' is anchored by the corpus spec_point block spcpt_pGsqq7xcztBg59Yh and joined to 4MA1-2.7D via name_to_statement_join; this section chunk sits inside that span.
- Verdict: [ ] CONFIRM — this chunk belongs to this SP   [ ] REJECT — wrong chunk/SP   [ ] HOLD — needs rework

### 4MA1-2.7B — solve quadratic equations by using the quadratic formula or completing the square
- Note: Completing the Square (`notes/2-equations-formulae-and-identities/completing-the-square/completing-the-square.json`)
- Chunk: ordinal 1 — heading `How can I rewrite the first two terms of a quadratic expression as the difference of two squares?` — sha256_16 `45f7cf48274b3978` — 983 chars
- Evidence quote (verbatim self-slice, markdown-safe): "How can I rewrite the first two terms of a quadratic expression as the difference of two squares?
- Look at the quadratic expression *x*<sup>2</sup> + *bx* + *c *
- The first** two terms** can be written as the **difference of two squares**"
- Chunk excerpt: «How can I rewrite the first two terms of a quadratic expression as the difference of two squares? - Look at the quadratic expression *x*<sup>2</sup> + *bx* + *c * - The first** two terms** can be written as the **difference of two squares** using the following rule $x^{2}+bx$ is the same as `open parentheses x plus p close parentheses squared minus p squared` where $p$ is **half** of $b$ - Check this is true by expan»
- Upstream: T-C32 join notes/2-equations-formulae-and-identities/completing-the-square/completing-the-square.json::spcpt_9Stcxtj75Q3wpqJF — tier S1_name_match — score 0.7647 — wording EXACT — validation tier AI_VALIDATED (operator-delegated chain)
- Rationale: SME span 'Completing the Square' on note 'Completing the Square' is anchored by the corpus spec_point block spcpt_9Stcxtj75Q3wpqJF and joined to 4MA1-2.7B via name_to_statement_join; this section chunk sits inside that span.
- Verdict: [ ] CONFIRM — this chunk belongs to this SP   [ ] REJECT — wrong chunk/SP   [ ] HOLD — needs rework

### 4MA1-3.3F — calculate the gradient of a straight line given the coordinates of two points
- Note: Conversion Graphs (`notes/3-sequences-functions-and-graphs/real-life-graphs/conversion-graphs.json`)
- Chunk: ordinal 2 — heading `How do I use a conversion graph?` — sha256_16 `d31407d0fbffaa5f` — 792 chars
- Evidence quote (verbatim self-slice, markdown-safe): "How do I use a conversion graph?
- Find the cost of 20kg using the conversion graph below

  - **Start** at 20kg on the ***x*****-axis**
  - Draw a** vertical line** to the graph
  - Then a **horizontal line** across to the *y*-axis
  - **R"
- Chunk excerpt: «How do I use a conversion graph? - Find the cost of 20kg using the conversion graph below - **Start** at 20kg on the ***x*****-axis** - Draw a** vertical line** to the graph - Then a **horizontal line** across to the *y*-axis - **Read off** the value - £12 - Find how many kilograms can be bought with £30 - **Start** at £30 on the ***y*****-axis** - Draw a** horizontal line** to the graph - Then a **vertical line** do»
- Upstream: T-C32 join notes/3-sequences-functions-and-graphs/real-life-graphs/conversion-graphs.json::spcpt_Nh8WWWGQxmJGVvvf — tier S1_name_match — score 0.803 — wording EXACT — validation tier AI_VALIDATED (operator-delegated chain)
- Rationale: SME span 'Conversion Graphs' on note 'Conversion Graphs' is anchored by the corpus spec_point block spcpt_Nh8WWWGQxmJGVvvf and joined to 4MA1-3.3F via name_to_statement_join; this section chunk sits inside that span.
- Verdict: [ ] CONFIRM — this chunk belongs to this SP   [ ] REJECT — wrong chunk/SP   [ ] HOLD — needs rework

### 4MA1-4.10F — convert between units of volume within the metric system
- Note: Volume (`notes/4-geometry-and-trigonometry/volume-and-surface-area/volume.json`)
- Chunk: ordinal 1 — heading `What is volume?` — sha256_16 `60c934757a067ddb` — 258 chars
- Evidence quote (verbatim self-slice, markdown-safe): "What is volume?
- The **volume **of a 3D shape is a measure of how much **space** it takes up
- You need to be able to calculate the volumes of a number of **common 3D shapes**, including:

  - Cubes and cuboids
  - Prisms
  - Cylinders
  -"
- Chunk excerpt: «What is volume? - The **volume **of a 3D shape is a measure of how much **space** it takes up - You need to be able to calculate the volumes of a number of **common 3D shapes**, including: - Cubes and cuboids - Prisms - Cylinders - Spheres - Cones»
- Upstream: T-C32 join notes/4-geometry-and-trigonometry/volume-and-surface-area/volume.json::spcpt_pKCFj25GzzqW6sr3 — tier S2_name_ambiguous — score 0.6774 — wording EXACT — validation tier AI_VALIDATED (operator-delegated chain)
- Rationale: SME span 'Volume' on note 'Volume' is anchored by the corpus spec_point block spcpt_pKCFj25GzzqW6sr3 and joined to 4MA1-4.10F via name_to_statement_join; this section chunk sits inside that span.
- Verdict: [ ] CONFIRM — this chunk belongs to this SP   [ ] REJECT — wrong chunk/SP   [ ] HOLD — needs rework

### 4MA1-4.10F — convert between units of volume within the metric system
- Note: Volume (`notes/4-geometry-and-trigonometry/volume-and-surface-area/volume.json`)
- Chunk: ordinal 4 — heading `How do I find the volume of a cylinder?` — sha256_16 `6061feaceeb9c1e0` — 345 chars
- Evidence quote (verbatim self-slice, markdown-safe): "How do I find the volume of a cylinder?
- To calculate the volume, *V*, of a **cylinder** with radius, *r*, and height, *h*, use the formula

  - $V=πr^{2}h$
  - This formula is given to you in the exam
Volume of a cylinder
- Note that a cy"
- Chunk excerpt: «How do I find the volume of a cylinder? - To calculate the volume, *V*, of a **cylinder** with radius, *r*, and height, *h*, use the formula - $V=πr^{2}h$ - This formula is given to you in the exam Volume of a cylinder - Note that a cylinder is similar to a **prism,** its cross-section is a circle with area $πr^{2}$, and its length is *h*»
- Upstream: T-C32 join notes/4-geometry-and-trigonometry/volume-and-surface-area/volume.json::spcpt_pKCFj25GzzqW6sr3 — tier S2_name_ambiguous — score 0.6774 — wording EXACT — validation tier AI_VALIDATED (operator-delegated chain)
- Rationale: SME span 'Volume' on note 'Volume' is anchored by the corpus spec_point block spcpt_pKCFj25GzzqW6sr3 and joined to 4MA1-4.10F via name_to_statement_join; this section chunk sits inside that span.
- Verdict: [ ] CONFIRM — this chunk belongs to this SP   [ ] REJECT — wrong chunk/SP   [ ] HOLD — needs rework

### 4MA1-1.7D — calculate an unknown quantity from quantities that vary in direct proportion
- Note: Direct Proportion (`notes/1-numbers-and-the-number-system/direct-and-inverse-proportion/direct-proportion.json`)
- Chunk: ordinal 2 — heading `How do I use direct proportion with powers and roots?` — sha256_16 `8e368f61a6c24842` — 625 chars
- Evidence quote (verbatim self-slice, markdown-safe): "How do I use direct proportion with powers and roots?
- Problems may involve a variable* *being **directly proportional** to a** power or root **of another variable
- For example

  - *y* is directly proportional to the **square of *****x *"
- Chunk excerpt: «How do I use direct proportion with powers and roots? - Problems may involve a variable* *being **directly proportional** to a** power or root **of another variable - For example - *y* is directly proportional to the **square of *****x *** - $y\proptox^{2}$ - means that $y=kx^{2}$ - *y* is directly proportional to the **square root of *****x*** - $y\propto\sqrt{x}$ - means that $y=k\sqrt{x}$ - *y* is directly proport»
- Upstream: T-C32 join notes/1-numbers-and-the-number-system/direct-and-inverse-proportion/direct-proportion.json::spcpt_BktcXhHcVFw8R9Q2 — tier S1_name_match — score 0.7462 — wording EXACT — validation tier AI_VALIDATED (operator-delegated chain)
- Rationale: SME span 'Direct Proportion' on note 'Direct Proportion' is anchored by the corpus spec_point block spcpt_BktcXhHcVFw8R9Q2 and joined to 4MA1-1.7D via name_to_statement_join; this section chunk sits inside that span.
- Verdict: [ ] CONFIRM — this chunk belongs to this SP   [ ] REJECT — wrong chunk/SP   [ ] HOLD — needs rework

### 4MA1-1.10C — understand and carry out calculations using time, and carry out calculations using money, including converting between currencies
- Note: Money Calculations (`notes/1-numbers-and-the-number-system/number-toolkit/money-calculations.json`)
- Chunk: ordinal 2 — heading `What might I be asked to do in money calculations?` — sha256_16 `0b478a77d63683bc` — 603 chars
- Evidence quote (verbatim self-slice, markdown-safe): "What might I be asked to do in money calculations?
- Read exam questions carefully to identify **keywords**

  - **Total** or **sum** will mean to** add up**
  - **Difference** or **increase/decrease** in costs will involve **subtracting**
"
- Chunk excerpt: «What might I be asked to do in money calculations? - Read exam questions carefully to identify **keywords** - **Total** or **sum** will mean to** add up** - **Difference** or **increase/decrease** in costs will involve **subtracting** - Changing from one currency to another (**exchange rates**) will involve **multiplying or dividing** - Some questions may involve a **combination** of these - E.g., Working out the tot»
- Upstream: T-C32 join notes/1-numbers-and-the-number-system/number-toolkit/money-calculations.json::spcpt_bMYrxtVc2SZgt8mX — tier S1_name_match — score 0.6772 — wording EXACT — validation tier AI_VALIDATED (operator-delegated chain)
- Rationale: SME span 'Money Calculations' on note 'Money Calculations' is anchored by the corpus spec_point block spcpt_bMYrxtVc2SZgt8mX and joined to 4MA1-1.10C via name_to_statement_join; this section chunk sits inside that span.
- Verdict: [ ] CONFIRM — this chunk belongs to this SP   [ ] REJECT — wrong chunk/SP   [ ] HOLD — needs rework

### 4MA1-1.4E — find highest common factors (HCF) and lowest common multiples (LCM)
- Note: HCF & LCM (`notes/1-numbers-and-the-number-system/prime-factors-hcf-and-lcm/hcf-and-lcm.json`)
- Chunk: ordinal 5 — heading `Lowest common multiple (LCM)` — sha256_16 `8949e327659e8bf4` — 28 chars
- Evidence quote (verbatim self-slice, markdown-safe): "Lowest common multiple (LCM)"
- Chunk excerpt: «Lowest common multiple (LCM)»
- Upstream: T-C32 join notes/1-numbers-and-the-number-system/prime-factors-hcf-and-lcm/hcf-and-lcm.json::spcpt_bmqbWbZM8HXPwsFF — tier S1_name_match — score 0.6858 — wording EXACT — validation tier AI_VALIDATED (operator-delegated chain)
- Rationale: SME span 'Lowest Common Multiple (LCM)' on note 'HCF & LCM' is anchored by the corpus spec_point block spcpt_bmqbWbZM8HXPwsFF and joined to 4MA1-1.4E via name_to_statement_join; this section chunk sits inside that span.
- Verdict: [ ] CONFIRM — this chunk belongs to this SP   [ ] REJECT — wrong chunk/SP   [ ] HOLD — needs rework

### 4MA1-6.2B — understand the concept of a measure of spread
- Note: Mean, Median & Mode (`notes/6-statistics-and-probability/statistics-toolkit/mean-median-and-mode.json`)
- Chunk: ordinal 1 — heading `What is the mode?` — sha256_16 `b7d07250596a5005` — 248 chars
- Evidence quote (verbatim self-slice, markdown-safe): "What is the mode?
- The** mode** is the value that appears the **most often**

  - The mode of 1, 2, 2, 5, 6 is 2
- There can be **more than one** mode

  - The modes of 1, 2, 2, 5, 5, 6 are 2 and 5
- The mode can also be called the **modal"
- Chunk excerpt: «What is the mode? - The** mode** is the value that appears the **most often** - The mode of 1, 2, 2, 5, 6 is 2 - There can be **more than one** mode - The modes of 1, 2, 2, 5, 5, 6 are 2 and 5 - The mode can also be called the **modal value**»
- Upstream: T-C32 join notes/6-statistics-and-probability/statistics-toolkit/mean-median-and-mode.json::spcpt_myNYhxstM7xnZd9P — tier S1_name_match — score 0.76 — wording EXACT — validation tier AI_VALIDATED (operator-delegated chain)
- Rationale: SME span 'Mean, Median & Mode' on note 'Mean, Median & Mode' is anchored by the corpus spec_point block spcpt_myNYhxstM7xnZd9P and joined to 4MA1-6.2B via name_to_statement_join; this section chunk sits inside that span.
- Verdict: [ ] CONFIRM — this chunk belongs to this SP   [ ] REJECT — wrong chunk/SP   [ ] HOLD — needs rework

### 4MA1-2.7B — solve quadratic equations by using the quadratic formula or completing the square
- Note: The Quadratic Formula (`notes/2-equations-formulae-and-identities/solving-quadratic-equations/quadratic-formula.json`)
- Chunk: ordinal 4 — heading `What is the discriminant?` — sha256_16 `6900d4eb2037d4f5` — 817 chars
- Evidence quote (verbatim self-slice, markdown-safe): "What is the discriminant?
- The part of the formula under the square root (*b*<sup>2</sup> – 4*ac*) is called the **discriminant**
- The **sign** of this value tells you if there are 0, 1 or 2 solutions

  - If ***b***<sup>**2**</sup>** – 4"
- Chunk excerpt: «What is the discriminant? - The part of the formula under the square root (*b*<sup>2</sup> – 4*ac*) is called the **discriminant** - The **sign** of this value tells you if there are 0, 1 or 2 solutions - If ***b***<sup>**2**</sup>** – 4*****ac***** > 0** (positive) - then there are 2 different solutions - If ***b***<sup>**2**</sup>** – 4*****ac***** = 0** - then there is only 1 solution - If ***b***<sup>**2**</sup>*»
- Upstream: T-C32 join notes/2-equations-formulae-and-identities/solving-quadratic-equations/quadratic-formula.json::spcpt_JRX7QS29KrY2hCCW — tier S1_name_match — score 0.7388 — wording EXACT — validation tier AI_VALIDATED (operator-delegated chain)
- Rationale: SME span 'Quadratic Formula' on note 'The Quadratic Formula' is anchored by the corpus spec_point block spcpt_JRX7QS29KrY2hCCW and joined to 4MA1-2.7B via name_to_statement_join; this section chunk sits inside that span.
- Verdict: [ ] CONFIRM — this chunk belongs to this SP   [ ] REJECT — wrong chunk/SP   [ ] HOLD — needs rework

### 4MA1-4.2D — understand the term ‘regular polygon’ and calculate interior and exterior angles of regular polygons
- Note: Angles in Polygons (`notes/4-geometry-and-trigonometry/angles-in-polygons-and-parallel-lines/angles-in-polygons.json`)
- Chunk: ordinal 0 — heading `Angles in polygons` — sha256_16 `712afcf81ba5e0c5` — 18 chars
- Evidence quote (verbatim self-slice, markdown-safe): "Angles in polygons"
- Chunk excerpt: «Angles in polygons»
- Upstream: T-C32 join notes/4-geometry-and-trigonometry/angles-in-polygons-and-parallel-lines/angles-in-polygons.json::spcpt_gzykj64JBx2RtBJ7 — tier S2_name_ambiguous — score 0.7085 — wording EXACT — validation tier AI_VALIDATED (operator-delegated chain)
- Rationale: SME span 'Angles in Polygons' on note 'Angles in Polygons' is anchored by the corpus spec_point block spcpt_gzykj64JBx2RtBJ7 and joined to 4MA1-4.2D via name_to_statement_join; this section chunk sits inside that span.
- Verdict: [ ] CONFIRM — this chunk belongs to this SP   [ ] REJECT — wrong chunk/SP   [ ] HOLD — needs rework

### 4MA1-3.3I — recognise, generate points and plot graphs of linear and quadratic functions
- Note: Quadratic Graphs (`notes/3-sequences-functions-and-graphs/graphs-of-functions/quadratic-graphs.json`)
- Chunk: ordinal 3 — heading `How do I sketch a quadratic graph?` — sha256_16 `d87eb84c4afe767e` — 1129 chars
- Evidence quote (verbatim self-slice, markdown-safe): "How do I sketch a quadratic graph?
- It is important to know how to** sketch **a quadratic curve

  - A simple drawing showing the **key features** is often sufficient
  - (For a more accurate graph, create a table of values and plot the po"
- Chunk excerpt: «How do I sketch a quadratic graph? - It is important to know how to** sketch **a quadratic curve - A simple drawing showing the **key features** is often sufficient - (For a more accurate graph, create a table of values and plot the points) - To **sketch a quadratic graph**: - First sketch the $x$ and $y$-axes - Identify the $y$-intercept and mark it on the $y$-axis - The $y$-intercept of $y=ax^{2}+bx+c$ will be `ope»
- Upstream: T-C32 join notes/3-sequences-functions-and-graphs/graphs-of-functions/quadratic-graphs.json::spcpt_76gVqdMN62jnrZg6 — tier S1_name_match — score 0.6967 — wording EXACT — validation tier AI_VALIDATED (operator-delegated chain)
- Rationale: SME span 'Quadratic Graphs' on note 'Quadratic Graphs' is anchored by the corpus spec_point block spcpt_76gVqdMN62jnrZg6 and joined to 4MA1-3.3I via name_to_statement_join; this section chunk sits inside that span.
- Verdict: [ ] CONFIRM — this chunk belongs to this SP   [ ] REJECT — wrong chunk/SP   [ ] HOLD — needs rework

### 4MA1-1.5E — use Venn diagrams to represent sets
- Note: Venn Diagrams with Three Sets (`notes/1-numbers-and-the-number-system/set-notation-and-venn-diagrams/venn-diagrams-with-three-sets.json`)
- Chunk: ordinal 1 — heading `What does a Venn diagram with three sets look like?` — sha256_16 `d6ccde54822accea` — 1019 chars
- Evidence quote (verbatim self-slice, markdown-safe): "What does a Venn diagram with three sets look like?
- There is a **rectangle** representing the universal set
- There are **three circles**

  - One for each of the sets
  
    - E.g.  $A$, $B$ and $C$
- The three circles intersect and spli"
- Chunk excerpt: «What does a Venn diagram with three sets look like? - There is a **rectangle** representing the universal set - There are **three circles** - One for each of the sets - E.g. $A$, $B$ and $C$ - The three circles intersect and split the rectangle into **eight regions** - A region where all **three circles intersect** - $A\capB\capC$ - Three regions where **exactly two circles intersect** - $A\capB\capC'$, $A\capB'\capC»
- Upstream: T-C32 join notes/1-numbers-and-the-number-system/set-notation-and-venn-diagrams/venn-diagrams-with-three-sets.json::spcpt_vfPNw2mzksvxf2JP — tier S1_name_match — score 0.66 — wording EXACT — validation tier AI_VALIDATED (operator-delegated chain)
- Rationale: SME span 'Venn diagrams with three sets' on note 'Venn Diagrams with Three Sets' is anchored by the corpus spec_point block spcpt_vfPNw2mzksvxf2JP and joined to 4MA1-1.5E via name_to_statement_join; this section chunk sits inside that span.
- Verdict: [ ] CONFIRM — this chunk belongs to this SP   [ ] REJECT — wrong chunk/SP   [ ] HOLD — needs rework

### 4MA1-1.4E — find highest common factors (HCF) and lowest common multiples (LCM)
- Note: HCF & LCM (`notes/1-numbers-and-the-number-system/prime-factors-hcf-and-lcm/hcf-and-lcm.json`)
- Chunk: ordinal 6 — heading `What is the lowest common multiple (LCM) of two numbers?` — sha256_16 `3381db44a6b5fae5` — 673 chars
- Evidence quote (verbatim self-slice, markdown-safe): "What is the lowest common multiple (LCM) of two numbers?
- A **common multiple** of two numbers is** **a number that appears in** both **of their times tables

  - The **product** of the original two numbers is always a common multiple (but"
- Chunk excerpt: «What is the lowest common multiple (LCM) of two numbers? - A **common multiple** of two numbers is** **a number that appears in** both **of their times tables - The **product** of the original two numbers is always a common multiple (but not necessarily the lowest) - **Any multiple** of a **common multiple** will **also be a common multiple** of the original two numbers - 30 is a common multiple of 3 and 10 - Therefo»
- Upstream: T-C32 join notes/1-numbers-and-the-number-system/prime-factors-hcf-and-lcm/hcf-and-lcm.json::spcpt_bmqbWbZM8HXPwsFF — tier S1_name_match — score 0.6858 — wording EXACT — validation tier AI_VALIDATED (operator-delegated chain)
- Rationale: SME span 'Lowest Common Multiple (LCM)' on note 'HCF & LCM' is anchored by the corpus spec_point block spcpt_bmqbWbZM8HXPwsFF and joined to 4MA1-1.4E via name_to_statement_join; this section chunk sits inside that span.
- Verdict: [ ] CONFIRM — this chunk belongs to this SP   [ ] REJECT — wrong chunk/SP   [ ] HOLD — needs rework

### 4MA1-6.1C — use cumulative frequency diagrams
- Note: Comparing Statistical Diagrams (`notes/6-statistics-and-probability/statistics-toolkit/comparing-statistical-diagrams.json`)
- Chunk: ordinal 1 — heading `How do I compare statistical diagrams?` — sha256_16 `586aa65baf2769d4` — 2817 chars
- Evidence quote (verbatim self-slice, markdown-safe): "How do I compare statistical diagrams?
- You may be given **two graphs** for two different **data sets** with the same **context**
- Compare** trends** in the graphs

  - **Increases**, **decreases**, **maximum points**
  - **Steepness** of"
- Chunk excerpt: «How do I compare statistical diagrams? - You may be given **two graphs** for two different **data sets** with the same **context** - Compare** trends** in the graphs - **Increases**, **decreases**, **maximum points** - **Steepness** of the change - Comment on **differences** and **similarities** - Explain **clearly** which **part** of the graph you are talking about - Use** numbers **from each data set in your compar»
- Upstream: T-C32 join notes/6-statistics-and-probability/statistics-toolkit/comparing-statistical-diagrams.json::spcpt_nXY9n4Vt3cVTmKcR — tier S1_name_match — score 0.7067 — wording EXACT — validation tier AI_VALIDATED (operator-delegated chain)
- Rationale: SME span 'Comparing Statistical Diagrams' on note 'Comparing Statistical Diagrams' is anchored by the corpus spec_point block spcpt_nXY9n4Vt3cVTmKcR and joined to 4MA1-6.1C via name_to_statement_join; this section chunk sits inside that span.
- Verdict: [ ] CONFIRM — this chunk belongs to this SP   [ ] REJECT — wrong chunk/SP   [ ] HOLD — needs rework

### 4MA1-2.2B — understand the concept of a quadratic expression and be able to factorise such expressions
- Note: Collecting Like Terms (`notes/2-equations-formulae-and-identities/algebra-toolkit/collecting-like-terms.json`)
- Chunk: ordinal 2 — heading `What is a like term?` — sha256_16 `beac036e54f1f05e` — 576 chars
- Evidence quote (verbatim self-slice, markdown-safe): "What is a like term?
- **Like terms **are terms with exactly the same** letters **and **powers**

  - The **coefficients** can be **different**
  
    - For example:
    - 2*x*  and 3*x*
    - 4*x*<sup>2</sup>  and 6*x*<sup>2</sup>
    - 5*"
- Chunk excerpt: «What is a like term? - **Like terms **are terms with exactly the same** letters **and **powers** - The **coefficients** can be **different** - For example: - 2*x* and 3*x* - 4*x*<sup>2</sup> and 6*x*<sup>2</sup> - 5*xy *and -7*xy* - These are **not** like terms: - 2*x* and 3*y *(different letters) - 4*x*<sup>2</sup> and 6*x*<sup>4 </sup>(different powers) - 5*xy *and 7*xyz *(different letters) - Remember **multiplica»
- Upstream: T-C32 join notes/2-equations-formulae-and-identities/algebra-toolkit/collecting-like-terms.json::spcpt_rsCdKqXKjhfmkyqT — tier S1_name_match — score 0.7692 — wording EXACT — validation tier AI_VALIDATED (operator-delegated chain)
- Rationale: SME span 'Collecting Like Terms' on note 'Collecting Like Terms' is anchored by the corpus spec_point block spcpt_rsCdKqXKjhfmkyqT and joined to 4MA1-2.2B via name_to_statement_join; this section chunk sits inside that span.
- Verdict: [ ] CONFIRM — this chunk belongs to this SP   [ ] REJECT — wrong chunk/SP   [ ] HOLD — needs rework

### 4MA1-4.1B — use angle properties of intersecting lines, parallel lines and angles on a straight line
- Note: Parallel Lines (`notes/3-sequences-functions-and-graphs/linear-graphs-y-equals-mx-plus-c/parallel-lines.json`)
- Chunk: ordinal 0 — heading `Parallel lines` — sha256_16 `0bbc82b60e0c298f` — 14 chars
- Evidence quote (verbatim self-slice, markdown-safe): "Parallel lines"
- Chunk excerpt: «Parallel lines»
- Upstream: T-C32 join notes/3-sequences-functions-and-graphs/linear-graphs-y-equals-mx-plus-c/parallel-lines.json::spcpt_qPRh2fycSMYwytcV — tier S1_name_match — score 0.7109 — wording EXACT — validation tier AI_VALIDATED (operator-delegated chain)
- Rationale: SME span 'Parallel Lines' on note 'Parallel Lines' is anchored by the corpus spec_point block spcpt_qPRh2fycSMYwytcV and joined to 4MA1-4.1B via name_to_statement_join; this section chunk sits inside that span.
- Verdict: [ ] CONFIRM — this chunk belongs to this SP   [ ] REJECT — wrong chunk/SP   [ ] HOLD — needs rework

### 4MA1-1.5B — use Venn diagrams to represent sets and the number of elements in sets
- Note: Set Notation & Venn Diagrams (`notes/1-numbers-and-the-number-system/set-notation-and-venn-diagrams/set-notation-and-venn-diagrams.json`)
- Chunk: ordinal 0 — heading `Set notation` — sha256_16 `77352ea1938af2c7` — 12 chars
- Evidence quote (verbatim self-slice, markdown-safe): "Set notation"
- Chunk excerpt: «Set notation»
- Upstream: T-C32 join notes/1-numbers-and-the-number-system/set-notation-and-venn-diagrams/set-notation-and-venn-diagrams.json::spcpt_CG8ZcZX8Ny5yGBch — tier S1_name_match — score 0.84 — wording EXACT — validation tier AI_VALIDATED (operator-delegated chain)
- Rationale: SME span 'Set Notation' on note 'Set Notation & Venn Diagrams' is anchored by the corpus spec_point block spcpt_CG8ZcZX8Ny5yGBch and joined to 4MA1-1.5B via name_to_statement_join; this section chunk sits inside that span.
- Verdict: [ ] CONFIRM — this chunk belongs to this SP   [ ] REJECT — wrong chunk/SP   [ ] HOLD — needs rework

### 4MA1-2.7B — solve quadratic equations by using the quadratic formula or completing the square
- Note: Completing the Square (`notes/2-equations-formulae-and-identities/completing-the-square/completing-the-square.json`)
- Chunk: ordinal 3 — heading `How do I complete the square when there is a coefficient in front of the x<sup>2</sup> term?` — sha256_16 `1f50c83d74094c43` — 1827 chars
- Evidence quote (verbatim self-slice, markdown-safe): "How do I complete the square when there is a coefficient in front of the x<sup>2</sup> term?
- You first need to take $a$ out as a **factor** of the *x*<sup>2</sup> and *x* terms only

  - **Factorise** the** first two terms**
  - `a x squa"
- Chunk excerpt: «How do I complete the square when there is a coefficient in front of the x<sup>2</sup> term? - You first need to take $a$ out as a **factor** of the *x*<sup>2</sup> and *x* terms only - **Factorise** the** first two terms** - `a x squared plus b x plus c equals a open square brackets x squared plus b over a x close square brackets plus c` - Use **square-shaped** **brackets** here to avoid confusion with round bracket»
- Upstream: T-C32 join notes/2-equations-formulae-and-identities/completing-the-square/completing-the-square.json::spcpt_9Stcxtj75Q3wpqJF — tier S1_name_match — score 0.7647 — wording EXACT — validation tier AI_VALIDATED (operator-delegated chain)
- Rationale: SME span 'Completing the Square' on note 'Completing the Square' is anchored by the corpus spec_point block spcpt_9Stcxtj75Q3wpqJF and joined to 4MA1-2.7B via name_to_statement_join; this section chunk sits inside that span.
- Verdict: [ ] CONFIRM — this chunk belongs to this SP   [ ] REJECT — wrong chunk/SP   [ ] HOLD — needs rework

### 4MA1-3.4E — apply calculus to linear kinematics and to other simple practical problems
- Note: Using Differentiation for Kinematics (`notes/3-sequences-functions-and-graphs/differentiation/kinematics.json`)
- Chunk: ordinal 3 — heading `What is a displacement function?` — sha256_16 `3d0c37a7002c7503` — 490 chars
- Evidence quote (verbatim self-slice, markdown-safe): "What is a displacement function?
- The **displacement** of an object, $s$ metres, can be written as a **function of time**, $t$ seconds

  - `s equals straight f open parentheses t close parentheses`
- **Substitute **a value of time in to *"
- Chunk excerpt: «What is a displacement function? - The **displacement** of an object, $s$ metres, can be written as a **function of time**, $t$ seconds - `s equals straight f open parentheses t close parentheses` - **Substitute **a value of time in to **find its displacement **at that time - For example, $s=2t-t^{2}+1$ - **Initially**, $t=0$ gives $s=2\times0-0^{2}+1=1$ (1 metre in front of the origin) - After 3 seconds, $t=3$ gives»
- Upstream: T-C32 join notes/3-sequences-functions-and-graphs/differentiation/kinematics.json::spcpt_vYsrWKqpQDpSwnPj — tier S1_name_match — score 0.6952 — wording EXACT — validation tier AI_VALIDATED (operator-delegated chain)
- Rationale: SME span 'Kinematics' on note 'Using Differentiation for Kinematics' is anchored by the corpus spec_point block spcpt_vYsrWKqpQDpSwnPj and joined to 4MA1-3.4E via name_to_statement_join; this section chunk sits inside that span.
- Verdict: [ ] CONFIRM — this chunk belongs to this SP   [ ] REJECT — wrong chunk/SP   [ ] HOLD — needs rework

### 4MA1-4.10D — find the surface area of a cylinder
- Note: Surface Area (`notes/4-geometry-and-trigonometry/volume-and-surface-area/surface-area.json`)
- Chunk: ordinal 2 — heading `How do I find the surface area of cubes, cuboids, and prisms?` — sha256_16 `0769a614326f0d81` — 538 chars
- Evidence quote (verbatim self-slice, markdown-safe): "How do I find the surface area of cubes, cuboids, and prisms?
- In cubes, cuboids, and polygonal-based prisms (prisms whose bases have straight sides), **all the faces are flat**
- The **surface area** is found by

  - calculating the area "
- Chunk excerpt: «How do I find the surface area of cubes, cuboids, and prisms? - In cubes, cuboids, and polygonal-based prisms (prisms whose bases have straight sides), **all the faces are flat** - The **surface area** is found by - calculating the area of each individual flat face - adding these areas together - You should remember the formulas for the **area of a rectangle**, a **triangle**, and a **circle **to help you calculate s»
- Upstream: T-C32 join notes/4-geometry-and-trigonometry/volume-and-surface-area/surface-area.json::spcpt_2w9hbV5pTbvc5Smj — tier S1_name_match — score 0.8043 — wording EXACT — validation tier AI_VALIDATED (operator-delegated chain)
- Rationale: SME span 'Surface Area' on note 'Surface Area' is anchored by the corpus spec_point block spcpt_2w9hbV5pTbvc5Smj and joined to 4MA1-4.10D via name_to_statement_join; this section chunk sits inside that span.
- Verdict: [ ] CONFIRM — this chunk belongs to this SP   [ ] REJECT — wrong chunk/SP   [ ] HOLD — needs rework

### 4MA1-4.11C — use areas and volumes of similar figures in solving problems
- Note: Similar Areas & Volumes (`notes/4-geometry-and-trigonometry/area-and-volume-of-similar-shapes/similar-areas-and-volumes.json`)
- Chunk: ordinal 3 — heading `How do I find missing lengths, areas and volumes for similar shapes?` — sha256_16 `bf48f8aa6fb6df7e` — 2175 chars
- Evidence quote (verbatim self-slice, markdown-safe): "How do I find missing lengths, areas and volumes for similar shapes?
- **STEP 1**
Identify the **equivalent** known quantities

  - Recognise if the quantities are lengths, areas or volumes
- **STEP 2**
Find the **scale factor** from two kn"
- Chunk excerpt: «How do I find missing lengths, areas and volumes for similar shapes? - **STEP 1** Identify the **equivalent** known quantities - Recognise if the quantities are lengths, areas or volumes - **STEP 2** Find the **scale factor** from two known **lengths, areas **or **volumes** - $\mathrm{scale} \mathrm{factor}=\frac{\mathrm{second} \mathrm{quantity}}{\mathrm{first} \mathrm{quantity}}$ - **STEP 3** Use the scale factor y»
- Upstream: T-C32 join notes/4-geometry-and-trigonometry/area-and-volume-of-similar-shapes/similar-areas-and-volumes.json::spcpt_dBwfqg3wJvDp9PNs — tier S1_name_match — score 0.758 — wording EXACT — validation tier AI_VALIDATED (operator-delegated chain)
- Rationale: SME span 'Similar Areas & Volumes' on note 'Similar Areas & Volumes' is anchored by the corpus spec_point block spcpt_dBwfqg3wJvDp9PNs and joined to 4MA1-4.11C via name_to_statement_join; this section chunk sits inside that span.
- Verdict: [ ] CONFIRM — this chunk belongs to this SP   [ ] REJECT — wrong chunk/SP   [ ] HOLD — needs rework

### 4MA1-5.1A — understand that a vector has both magnitude and direction
- Note: Magnitude of a Vector (`notes/5-vectors-and-transformation-geometry/vectors/magnitude-of-a-vector.json`)
- Chunk: ordinal 1 — heading `How do I find the magnitude of a vector?` — sha256_16 `8ff6c102ec463b53` — 4084 chars
- Evidence quote (verbatim self-slice, markdown-safe): "How do I find the magnitude of a vector?
- The **magnitude **of a **vector** is its **length **(distance)

  - It is also called the **modulus**
  - This is always a **positive** value
  - The direction of the vector is irrelevant
- The mag"
- Chunk excerpt: «How do I find the magnitude of a vector? - The **magnitude **of a **vector** is its **length **(distance) - It is also called the **modulus** - This is always a **positive** value - The direction of the vector is irrelevant - The magnitude of $\overset{\rightarrow}{AB}$ is written `open vertical bar stack A B with rightwards arrow on top close vertical bar` - The magnitude of **a** is written |**a**| - Depending on t»
- Upstream: T-C32 join notes/5-vectors-and-transformation-geometry/vectors/magnitude-of-a-vector.json::spcpt_vqmZYnJx9pH7mGMC — tier S1_name_match — score 0.7538 — wording EXACT — validation tier AI_VALIDATED (operator-delegated chain)
- Rationale: SME span 'Magnitude of a Vector' on note 'Magnitude of a Vector' is anchored by the corpus spec_point block spcpt_vqmZYnJx9pH7mGMC and joined to 4MA1-5.1A via name_to_statement_join; this section chunk sits inside that span.
- Verdict: [ ] CONFIRM — this chunk belongs to this SP   [ ] REJECT — wrong chunk/SP   [ ] HOLD — needs rework

### 4MA1-1.6G — use compound interest and depreciation
- Note: Depreciation (`notes/1-numbers-and-the-number-system/compound-interest-and-depreciation/depreciation.json`)
- Chunk: ordinal 1 — heading `What does depreciation mean?` — sha256_16 `d3b1753085dfeceb` — 289 chars
- Evidence quote (verbatim self-slice, markdown-safe): "What does depreciation mean?
- Depreciation is where an item **loses value** over time

  - E.g. cars, mobile phones, etc
- Depreciation is usually calculated as a percentage decrease at the end of each year

  - This works the same as comp"
- Chunk excerpt: «What does depreciation mean? - Depreciation is where an item **loses value** over time - E.g. cars, mobile phones, etc - Depreciation is usually calculated as a percentage decrease at the end of each year - This works the same as compound interest, but with a percentage** decrease**»
- Upstream: T-C32 join notes/1-numbers-and-the-number-system/compound-interest-and-depreciation/depreciation.json::spcpt_rDHZfZ8PrdwXcT2y — tier S1_name_match — score 0.792 — wording EXACT — validation tier AI_VALIDATED (operator-delegated chain)
- Rationale: SME span 'Depreciation' on note 'Depreciation' is anchored by the corpus spec_point block spcpt_rDHZfZ8PrdwXcT2y and joined to 4MA1-1.6G via name_to_statement_join; this section chunk sits inside that span.
- Verdict: [ ] CONFIRM — this chunk belongs to this SP   [ ] REJECT — wrong chunk/SP   [ ] HOLD — needs rework

### 4MA1-1.5B — use Venn diagrams to represent sets and the number of elements in sets
- Note: Set Notation & Venn Diagrams (`notes/1-numbers-and-the-number-system/set-notation-and-venn-diagrams/set-notation-and-venn-diagrams.json`)
- Chunk: ordinal 1 — heading `What is a set?` — sha256_16 `8ca34b75d6a802b6` — 1058 chars
- Evidence quote (verbatim self-slice, markdown-safe): "What is a set?
- A set is a **collection of elements**

  - Elements could be anything
  
    - Numbers, letters, coordinates, ...
- You could describe a set by writing its elements inside **curly brackets** {}

  - {1, 2, 3, 6} , is the se"
- Chunk excerpt: «What is a set? - A set is a **collection of elements** - Elements could be anything - Numbers, letters, coordinates, ... - You could describe a set by writing its elements inside **curly brackets** {} - {1, 2, 3, 6} , is the set of factors of 6 - If the set of elements **follow a rule** then you can write this using a **colon inside the curly brackets** {... : ...} - The bit before the colon is the type of element - »
- Upstream: T-C32 join notes/1-numbers-and-the-number-system/set-notation-and-venn-diagrams/set-notation-and-venn-diagrams.json::spcpt_CG8ZcZX8Ny5yGBch — tier S1_name_match — score 0.84 — wording EXACT — validation tier AI_VALIDATED (operator-delegated chain)
- Rationale: SME span 'Set Notation' on note 'Set Notation & Venn Diagrams' is anchored by the corpus spec_point block spcpt_CG8ZcZX8Ny5yGBch and joined to 4MA1-1.5B via name_to_statement_join; this section chunk sits inside that span.
- Verdict: [ ] CONFIRM — this chunk belongs to this SP   [ ] REJECT — wrong chunk/SP   [ ] HOLD — needs rework

### 4MA1-3.3B — apply to the graph ofy = f(x)the transformations y = f(x) + a, y = f(ax), y = f(x + a), y = af(x) for linear, quadratic, sine and cosine functions
- Note: 2D Coordinates (`notes/3-sequences-functions-and-graphs/coordinate-geometry/coordinates.json`)
- Chunk: ordinal 1 — heading `What is the Cartesian plane?` — sha256_16 `2d6c4d47d43c6e59` — 310 chars
- Evidence quote (verbatim self-slice, markdown-safe): "What is the Cartesian plane?
- The **Cartesian plane** is a **two-dimensional **grid that has

  - a** horizontal** scale, called the** *****x*****-axis**
  - a** vertical **scale, called the** *****y*****-axis**
- The two** **axes** meet**"
- Chunk excerpt: «What is the Cartesian plane? - The **Cartesian plane** is a **two-dimensional **grid that has - a** horizontal** scale, called the** *****x*****-axis** - a** vertical **scale, called the** *****y*****-axis** - The two** **axes** meet** at the **origin** - where ***x *****and***** y *****are both 0**»
- Upstream: T-C32 join notes/3-sequences-functions-and-graphs/coordinate-geometry/coordinates.json::spcpt_Jw35TTKhvXxmGGfP — tier S2_name_ambiguous — score 0.7268 — wording EXACT — validation tier AI_VALIDATED (operator-delegated chain)
- Rationale: SME span '2D Coordinates' on note '2D Coordinates' is anchored by the corpus spec_point block spcpt_Jw35TTKhvXxmGGfP and joined to 4MA1-3.3B via name_to_statement_join; this section chunk sits inside that span.
- Verdict: [ ] CONFIRM — this chunk belongs to this SP   [ ] REJECT — wrong chunk/SP   [ ] HOLD — needs rework

### 4MA1-2.7D — solve simultaneous equations in two unknowns, one equation being linear and the other being quadratic
- Note: Quadratic Simultaneous Equations (`notes/2-equations-formulae-and-identities/simultaneous-equations/quadratic.json`)
- Chunk: ordinal 1 — heading `What are quadratic simultaneous equations?` — sha256_16 `74cbc6e8b4c1540c` — 356 chars
- Evidence quote (verbatim self-slice, markdown-safe): "What are quadratic simultaneous equations?
- When there are two unknowns (e.g. *x* and *y*) in a problem, we need two equations to be able to find them both; these are called** simultaneous equations**
- If there is an *x*<sup>2</sup> or *y"
- Chunk excerpt: «What are quadratic simultaneous equations? - When there are two unknowns (e.g. *x* and *y*) in a problem, we need two equations to be able to find them both; these are called** simultaneous equations** - If there is an *x*<sup>2</sup> or *y*<sup>2</sup> or *xy *in one of the equations then they are **quadratic** (or **non-linear**) simultaneous equations»
- Upstream: T-C32 join notes/2-equations-formulae-and-identities/simultaneous-equations/quadratic.json::spcpt_pGsqq7xcztBg59Yh — tier S1_name_match — score 0.7394 — wording EXACT — validation tier AI_VALIDATED (operator-delegated chain)
- Rationale: SME span 'Quadratic Simultaneous Equations' on note 'Quadratic Simultaneous Equations' is anchored by the corpus spec_point block spcpt_pGsqq7xcztBg59Yh and joined to 4MA1-2.7D via name_to_statement_join; this section chunk sits inside that span.
- Verdict: [ ] CONFIRM — this chunk belongs to this SP   [ ] REJECT — wrong chunk/SP   [ ] HOLD — needs rework

### 4MA1-1.5E — use Venn diagrams to represent sets
- Note: Venn Diagrams with Three Sets (`notes/1-numbers-and-the-number-system/set-notation-and-venn-diagrams/venn-diagrams-with-three-sets.json`)
- Chunk: ordinal 2 — heading `How do I find the number of elements in a subset?` — sha256_16 `a60593fef6db38f3` — 296 chars
- Evidence quote (verbatim self-slice, markdown-safe): "How do I find the number of elements in a subset?
- Identify the **intersections **which make up the subset

  - E.g. the subset $A\capB$ is made up of $A\capB\capC$ and $A\capB\capC'$
- **Add together** the number of elements in the inters"
- Chunk excerpt: «How do I find the number of elements in a subset? - Identify the **intersections **which make up the subset - E.g. the subset $A\capB$ is made up of $A\capB\capC$ and $A\capB\capC'$ - **Add together** the number of elements in the intersections Example of finding number of elements in subsets»
- Upstream: T-C32 join notes/1-numbers-and-the-number-system/set-notation-and-venn-diagrams/venn-diagrams-with-three-sets.json::spcpt_vfPNw2mzksvxf2JP — tier S1_name_match — score 0.66 — wording EXACT — validation tier AI_VALIDATED (operator-delegated chain)
- Rationale: SME span 'Venn diagrams with three sets' on note 'Venn Diagrams with Three Sets' is anchored by the corpus spec_point block spcpt_vfPNw2mzksvxf2JP and joined to 4MA1-1.5E via name_to_statement_join; this section chunk sits inside that span.
- Verdict: [ ] CONFIRM — this chunk belongs to this SP   [ ] REJECT — wrong chunk/SP   [ ] HOLD — needs rework

### 4MA1-4.4B — calculate time intervals in terms of the 24-hour and the 12-hour clock
- Note: Time (`notes/4-geometry-and-trigonometry/standard-and-compound-units/time.json`)
- Chunk: ordinal 1 — heading `How do I convert between different units of time?` — sha256_16 `d3a37f541460bb0c` — 397 chars
- Evidence quote (verbatim self-slice, markdown-safe): "How do I convert between different units of time?
- **Time** has a **number of different conversions** and does not use the decimal number system (based on 10s, 100s, etc)

  - You need to know the follow time conversions
Common time conver"
- Chunk excerpt: «How do I convert between different units of time? - **Time** has a **number of different conversions** and does not use the decimal number system (based on 10s, 100s, etc) - You need to know the follow time conversions Common time conversions - You should also know the **number of days** in each **calendar month** ![Number of days in each calendar month](assets/0e43a3b3f4fe-36234-time-2.png)»
- Upstream: T-C32 join notes/4-geometry-and-trigonometry/standard-and-compound-units/time.json::spcpt_h2p7nv6zkR4xFJ3P — tier S2_name_ambiguous — score 0.6432 — wording EXACT — validation tier AI_VALIDATED (operator-delegated chain)
- Rationale: SME span 'Time' on note 'Time' is anchored by the corpus spec_point block spcpt_h2p7nv6zkR4xFJ3P and joined to 4MA1-4.4B via name_to_statement_join; this section chunk sits inside that span.
- Verdict: [ ] CONFIRM — this chunk belongs to this SP   [ ] REJECT — wrong chunk/SP   [ ] HOLD — needs rework

### 4MA1-3.4C — determine gradients, rates of change, stationary points, turning points (maxima and minima) by differentiation and relate these to graphs
- Note: Finding Stationary Points & Turning Points (`notes/3-sequences-functions-and-graphs/differentiation/applications-of-differentiation.json`)
- Chunk: ordinal 2 — heading `How do I find the coordinates of a turning point?` — sha256_16 `125db52496bc74b2` — 1816 chars
- Evidence quote (verbatim self-slice, markdown-safe): "How do I find the coordinates of a turning point?
- **STEP 1**
Find the **gradient function **(derivative) $\frac{dy}{dx}$ of the** original equation**

  - E.g. Find the coordinates of the turning point of the equation $y=4x^{2}-8x+9$
  - "
- Chunk excerpt: «How do I find the coordinates of a turning point? - **STEP 1** Find the **gradient function **(derivative) $\frac{dy}{dx}$ of the** original equation** - E.g. Find the coordinates of the turning point of the equation $y=4x^{2}-8x+9$ - $\frac{dy}{dx}=8x-8$ - **STEP 2** Set the** gradient function **(derivative) **equal to** **zero** and** solve for **$x$ - This will find the ***x*****-coordinate** of the turning point»
- Upstream: T-C32 join notes/3-sequences-functions-and-graphs/differentiation/applications-of-differentiation.json::spcpt_pKJ7Y3jd7PDzZQpP — tier S1_name_match — score 0.6293 — wording EXACT — validation tier AI_VALIDATED (operator-delegated chain)
- Rationale: SME span 'Finding Stationary Points & Turning Points' on note 'Finding Stationary Points & Turning Points' is anchored by the corpus spec_point block spcpt_pKJ7Y3jd7PDzZQpP and joined to 4MA1-3.4C via name_to_statement_join; this section chunk sits inside that span.
- Verdict: [ ] CONFIRM — this chunk belongs to this SP   [ ] REJECT — wrong chunk/SP   [ ] HOLD — needs rework

### 4MA1-6.2B — understand the concept of a measure of spread
- Note: Mean, Median & Mode (`notes/6-statistics-and-probability/statistics-toolkit/mean-median-and-mode.json`)
- Chunk: ordinal 0 — heading `Mean, median & mode` — sha256_16 `d5a71620fbc61af5` — 19 chars
- Evidence quote (verbatim self-slice, markdown-safe): "Mean, median & mode"
- Chunk excerpt: «Mean, median & mode»
- Upstream: T-C32 join notes/6-statistics-and-probability/statistics-toolkit/mean-median-and-mode.json::spcpt_myNYhxstM7xnZd9P — tier S1_name_match — score 0.76 — wording EXACT — validation tier AI_VALIDATED (operator-delegated chain)
- Rationale: SME span 'Mean, Median & Mode' on note 'Mean, Median & Mode' is anchored by the corpus spec_point block spcpt_myNYhxstM7xnZd9P and joined to 4MA1-6.2B via name_to_statement_join; this section chunk sits inside that span.
- Verdict: [ ] CONFIRM — this chunk belongs to this SP   [ ] REJECT — wrong chunk/SP   [ ] HOLD — needs rework

### 4MA1-1.5E — use Venn diagrams to represent sets
- Note: Set Notation & Venn Diagrams (`notes/1-numbers-and-the-number-system/set-notation-and-venn-diagrams/set-notation-and-venn-diagrams.json`)
- Chunk: ordinal 3 — heading `Sets & Venn diagrams` — sha256_16 `29aac49258c8eec1` — 20 chars
- Evidence quote (verbatim self-slice, markdown-safe): "Sets & Venn diagrams"
- Chunk excerpt: «Sets & Venn diagrams»
- Upstream: T-C32 join notes/1-numbers-and-the-number-system/set-notation-and-venn-diagrams/set-notation-and-venn-diagrams.json::spcpt_XT9QGzbhpThbfcB6 — tier S1_name_match — score 0.8415 — wording EXACT — validation tier AI_VALIDATED (operator-delegated chain)
- Rationale: SME span 'Sets & Venn Diagrams' on note 'Set Notation & Venn Diagrams' is anchored by the corpus spec_point block spcpt_XT9QGzbhpThbfcB6 and joined to 4MA1-1.5E via name_to_statement_join; this section chunk sits inside that span.
- Verdict: [ ] CONFIRM — this chunk belongs to this SP   [ ] REJECT — wrong chunk/SP   [ ] HOLD — needs rework

### 4MA1-3.4C — determine gradients, rates of change, stationary points, turning points (maxima and minima) by differentiation and relate these to graphs
- Note: Differentiation (`notes/3-sequences-functions-and-graphs/differentiation/differentiation.json`)
- Chunk: ordinal 6 — heading `How is the gradient function related to drawing tangents?` — sha256_16 `bf41aee019ff626b` — 3469 chars
- Evidence quote (verbatim self-slice, markdown-safe): "How is the gradient function related to drawing tangents?
- The gradient of a curve changes as you move along the curve

  - To find the gradient at a particular point you can **draw a tangent **and find its **gradient **
  - This is a **gr"
- Chunk excerpt: «How is the gradient function related to drawing tangents? - The gradient of a curve changes as you move along the curve - To find the gradient at a particular point you can **draw a tangent **and find its **gradient ** - This is a **graphical** method that is **not accurate** - It depends on how well you draw the tangent - Instead, you can use **differentiation** to find the **gradient function**, then **substitute t»
- Upstream: T-C32 join notes/3-sequences-functions-and-graphs/differentiation/differentiation.json::spcpt_fGGbSYFZH9DW4sgm — tier S1_name_match — score 0.6805 — wording EXACT — validation tier AI_VALIDATED (operator-delegated chain)
- Rationale: SME span 'Differentiation' on note 'Differentiation' is anchored by the corpus spec_point block spcpt_fGGbSYFZH9DW4sgm and joined to 4MA1-3.4C via name_to_statement_join; this section chunk sits inside that span.
- Verdict: [ ] CONFIRM — this chunk belongs to this SP   [ ] REJECT — wrong chunk/SP   [ ] HOLD — needs rework

### 4MA1-6.1C — use cumulative frequency diagrams
- Note: Reading & Interpreting Statistical Diagrams (`notes/6-statistics-and-probability/statistics-toolkit/working-with-statistical-diagrams.json`)
- Chunk: ordinal 0 — heading `Reading & interpreting statistical diagrams` — sha256_16 `da3570591b55948a` — 43 chars
- Evidence quote (verbatim self-slice, markdown-safe): "Reading & interpreting statistical diagrams"
- Chunk excerpt: «Reading & interpreting statistical diagrams»
- Upstream: T-C32 join notes/6-statistics-and-probability/statistics-toolkit/working-with-statistical-diagrams.json::spcpt_bGtx4SMcX6BRS6KP — tier S1_name_match — score 0.638 — wording EXACT — validation tier AI_VALIDATED (operator-delegated chain)
- Rationale: SME span 'Reading & Interpreting Statistical Diagrams' on note 'Reading & Interpreting Statistical Diagrams' is anchored by the corpus spec_point block spcpt_bGtx4SMcX6BRS6KP and joined to 4MA1-6.1C via name_to_statement_join; this section chunk sits inside that span.
- Verdict: [ ] CONFIRM — this chunk belongs to this SP   [ ] REJECT — wrong chunk/SP   [ ] HOLD — needs rework

### 4MA1-1.4E — find highest common factors (HCF) and lowest common multiples (LCM)
- Note: HCF & LCM (`notes/1-numbers-and-the-number-system/prime-factors-hcf-and-lcm/hcf-and-lcm.json`)
- Chunk: ordinal 7 — heading `How do I find the lowest common multiple (LCM) of two numbers?` — sha256_16 `9d7dff5153f9718a` — 453 chars
- Evidence quote (verbatim self-slice, markdown-safe): "How do I find the lowest common multiple (LCM) of two numbers?
- To find the **lowest common multiple **of two numbers:

  - write out the first few **multiples** of each number
  - identify the multiples that appear in** both **lists
  
  "
- Chunk excerpt: «How do I find the lowest common multiple (LCM) of two numbers? - To find the **lowest common multiple **of two numbers: - write out the first few **multiples** of each number - identify the multiples that appear in** both **lists - If there are **none** then write out the **next few multiples** of each number until you find a common multiple - The **lowest common multiple** will be the **smallest **multiple that appe»
- Upstream: T-C32 join notes/1-numbers-and-the-number-system/prime-factors-hcf-and-lcm/hcf-and-lcm.json::spcpt_bmqbWbZM8HXPwsFF — tier S1_name_match — score 0.6858 — wording EXACT — validation tier AI_VALIDATED (operator-delegated chain)
- Rationale: SME span 'Lowest Common Multiple (LCM)' on note 'HCF & LCM' is anchored by the corpus spec_point block spcpt_bmqbWbZM8HXPwsFF and joined to 4MA1-1.4E via name_to_statement_join; this section chunk sits inside that span.
- Verdict: [ ] CONFIRM — this chunk belongs to this SP   [ ] REJECT — wrong chunk/SP   [ ] HOLD — needs rework

### 4MA1-1.4E — find highest common factors (HCF) and lowest common multiples (LCM)
- Note: HCF & LCM (`notes/1-numbers-and-the-number-system/prime-factors-hcf-and-lcm/hcf-and-lcm.json`)
- Chunk: ordinal 4 — heading `How can I use the powers of prime factors to find the highest common factor (HCF) of two numbers?` — sha256_16 `6c46a91f1d1ba705` — 1687 chars
- Evidence quote (verbatim self-slice, markdown-safe): "How can I use the powers of prime factors to find the highest common factor (HCF) of two numbers?
- Write each number as a **product of the powers of its prime factors**

  - 24 = 2<sup>3</sup>×3 and 60 = 2<sup>2</sup>×3×5
- Find all **comm"
- Chunk excerpt: «How can I use the powers of prime factors to find the highest common factor (HCF) of two numbers? - Write each number as a **product of the powers of its prime factors** - 24 = 2<sup>3</sup>×3 and 60 = 2<sup>2</sup>×3×5 - Find all **common **prime factors and identify the **highest power** that appears in both numbers - The highest power of 2 in both is 2<sup>2</sup> - 2<sup>2</sup> is a common factor - The highest p»
- Upstream: T-C32 join notes/1-numbers-and-the-number-system/prime-factors-hcf-and-lcm/hcf-and-lcm.json::spcpt_P88yS9wysymQ2brq — tier S1_name_match — score 0.6798 — wording EXACT — validation tier AI_VALIDATED (operator-delegated chain)
- Rationale: SME span 'Highest Common Factor (HCF)' on note 'HCF & LCM' is anchored by the corpus spec_point block spcpt_P88yS9wysymQ2brq and joined to 4MA1-1.4E via name_to_statement_join; this section chunk sits inside that span.
- Verdict: [ ] CONFIRM — this chunk belongs to this SP   [ ] REJECT — wrong chunk/SP   [ ] HOLD — needs rework

### 4MA1-2.7B — solve quadratic equations by using the quadratic formula or completing the square
- Note: Completing the Square (`notes/2-equations-formulae-and-identities/completing-the-square/completing-the-square.json`)
- Chunk: ordinal 4 — heading `How do I find the turning point by completing the square?` — sha256_16 `1698cbe2056006ec` — 3563 chars
- Evidence quote (verbatim self-slice, markdown-safe): "How do I find the turning point by completing the square?
- Completing the square helps us find the **turning** **point** on a quadratic graph

  - If `y equals open parentheses x plus p close parentheses squared plus q` then the turning po"
- Chunk excerpt: «How do I find the turning point by completing the square? - Completing the square helps us find the **turning** **point** on a quadratic graph - If `y equals open parentheses x plus p close parentheses squared plus q` then the turning point is at `open parentheses negative p comma q close parentheses` - Notice the negative sign in the *x*-coordinate - This links to transformations of graphs - A translation of $y=x^{2»
- Upstream: T-C32 join notes/2-equations-formulae-and-identities/completing-the-square/completing-the-square.json::spcpt_9Stcxtj75Q3wpqJF — tier S1_name_match — score 0.7647 — wording EXACT — validation tier AI_VALIDATED (operator-delegated chain)
- Rationale: SME span 'Completing the Square' on note 'Completing the Square' is anchored by the corpus spec_point block spcpt_9Stcxtj75Q3wpqJF and joined to 4MA1-2.7B via name_to_statement_join; this section chunk sits inside that span.
- Verdict: [ ] CONFIRM — this chunk belongs to this SP   [ ] REJECT — wrong chunk/SP   [ ] HOLD — needs rework

### 4MA1-5.2A — understand that rotations are specified by a centre and an angle
- Note: Rotations (`notes/5-vectors-and-transformation-geometry/transformations/rotations.json`)
- Chunk: ordinal 0 — heading `Rotations` — sha256_16 `077244282d7247f2` — 9 chars
- Evidence quote (verbatim self-slice, markdown-safe): "Rotations"
- Chunk excerpt: «Rotations»
- Upstream: T-C32 join notes/5-vectors-and-transformation-geometry/transformations/rotations.json::spcpt_N5xf2wmr4yCNxHBj — tier S1_name_match — score 0.6986 — wording EXACT — validation tier AI_VALIDATED (operator-delegated chain)
- Rationale: SME span 'Rotations' on note 'Rotations' is anchored by the corpus spec_point block spcpt_N5xf2wmr4yCNxHBj and joined to 4MA1-5.2A via name_to_statement_join; this section chunk sits inside that span.
- Verdict: [ ] CONFIRM — this chunk belongs to this SP   [ ] REJECT — wrong chunk/SP   [ ] HOLD — needs rework

### 4MA1-1.5E — use Venn diagrams to represent sets
- Note: Venn Diagrams with Three Sets (`notes/1-numbers-and-the-number-system/set-notation-and-venn-diagrams/venn-diagrams-with-three-sets.json`)
- Chunk: ordinal 3 — heading `How do I fill in a Venn diagram with three sets?` — sha256_16 `a45249906cec0a11` — 3800 chars
- Evidence quote (verbatim self-slice, markdown-safe): "How do I fill in a Venn diagram with three sets?
- Start with the **intersection **of **all three** circles $A\capB\capC$

  - Fill in the number or label it $x$ if it is unknown
- Fill in regions where **exactly two circles intersect**

  "
- Chunk excerpt: «How do I fill in a Venn diagram with three sets? - Start with the **intersection **of **all three** circles $A\capB\capC$ - Fill in the number or label it $x$ if it is unknown - Fill in regions where **exactly two circles intersect** - You might be given the total number of elements in the intersection between those two sets - E.g. There are 20 elements that are in both set $A$ and set $C$ - Subtract the number in th»
- Upstream: T-C32 join notes/1-numbers-and-the-number-system/set-notation-and-venn-diagrams/venn-diagrams-with-three-sets.json::spcpt_vfPNw2mzksvxf2JP — tier S1_name_match — score 0.66 — wording EXACT — validation tier AI_VALIDATED (operator-delegated chain)
- Rationale: SME span 'Venn diagrams with three sets' on note 'Venn Diagrams with Three Sets' is anchored by the corpus spec_point block spcpt_vfPNw2mzksvxf2JP and joined to 4MA1-1.5E via name_to_statement_join; this section chunk sits inside that span.
- Verdict: [ ] CONFIRM — this chunk belongs to this SP   [ ] REJECT — wrong chunk/SP   [ ] HOLD — needs rework

### 4MA1-2.7B — solve quadratic equations by using the quadratic formula or completing the square
- Note: The Quadratic Formula (`notes/2-equations-formulae-and-identities/solving-quadratic-equations/quadratic-formula.json`)
- Chunk: ordinal 5 — heading `Can I use my calculator to solve quadratic equations?` — sha256_16 `d69e20305bd461e0` — 1208 chars
- Evidence quote (verbatim self-slice, markdown-safe): "Can I use my calculator to solve quadratic equations?
- If your calculator solves quadratic equations, use it to** check** your **final answers**

  - But a correct method and working must still be shown
Worked Example: Use the quadratic fo"
- Chunk excerpt: «Can I use my calculator to solve quadratic equations? - If your calculator solves quadratic equations, use it to** check** your **final answers** - But a correct method and working must still be shown Worked Example: Use the quadratic formula to find the solutions of the equation 3*x*<sup>2</sup> - 2*x* - 4 = 0. Give each solution as an exact value in its simplest form. **Answer:** > *Write down the values of **a**, »
- Upstream: T-C32 join notes/2-equations-formulae-and-identities/solving-quadratic-equations/quadratic-formula.json::spcpt_JRX7QS29KrY2hCCW — tier S1_name_match — score 0.7388 — wording EXACT — validation tier AI_VALIDATED (operator-delegated chain)
- Rationale: SME span 'Quadratic Formula' on note 'The Quadratic Formula' is anchored by the corpus spec_point block spcpt_JRX7QS29KrY2hCCW and joined to 4MA1-2.7B via name_to_statement_join; this section chunk sits inside that span.
- Verdict: [ ] CONFIRM — this chunk belongs to this SP   [ ] REJECT — wrong chunk/SP   [ ] HOLD — needs rework

### 4MA1-4.4G — use compound measure such as speed, density and pressure
- Note: Speed, Density & Pressure (`notes/4-geometry-and-trigonometry/standard-and-compound-units/speed-density-and-pressure.json`)
- Chunk: ordinal 1 — heading `What are speed, density and pressure?` — sha256_16 `538a25b35e128678` — 349 chars
- Evidence quote (verbatim self-slice, markdown-safe): "What are speed, density and pressure?
- **Speed**, **density** and **pressure** are frequently used **compound measures**

  - **Speed** is equal to **distance **divided by **time**
  - **Density** is equal to **mass** divided by **volume**"
- Chunk excerpt: «What are speed, density and pressure? - **Speed**, **density** and **pressure** are frequently used **compound measures** - **Speed** is equal to **distance **divided by **time** - **Density** is equal to **mass** divided by **volume** - **Pressure** is equal to **force** divided by **area** Formula Triangles for Speed, Density and Pressure»
- Upstream: T-C32 join notes/4-geometry-and-trigonometry/standard-and-compound-units/speed-density-and-pressure.json::spcpt_jJPhXSKYBg6x4d2Q — tier S1_name_match — score 0.8286 — wording EXACT — validation tier AI_VALIDATED (operator-delegated chain)
- Rationale: SME span 'Speed, Density & Pressure' on note 'Speed, Density & Pressure' is anchored by the corpus spec_point block spcpt_jJPhXSKYBg6x4d2Q and joined to 4MA1-4.4G via name_to_statement_join; this section chunk sits inside that span.
- Verdict: [ ] CONFIRM — this chunk belongs to this SP   [ ] REJECT — wrong chunk/SP   [ ] HOLD — needs rework

### 4MA1-4.11A — understand that areas of similar figures are in the ratio of the square of corresponding sides
- Note: Similar Lengths (`notes/4-geometry-and-trigonometry/congruence-similarity-and-geometrical-proof/similar-lengths.json`)
- Chunk: ordinal 0 — heading `Similar lengths` — sha256_16 `e8aee3cb0f8cdc61` — 15 chars
- Evidence quote (verbatim self-slice, markdown-safe): "Similar lengths"
- Chunk excerpt: «Similar lengths»
- Upstream: T-C32 join notes/4-geometry-and-trigonometry/congruence-similarity-and-geometrical-proof/similar-lengths.json::spcpt_xDpKVBxDTCk2x6vS — tier S1_name_match — score 0.6714 — wording EXACT — validation tier AI_VALIDATED (operator-delegated chain)
- Rationale: SME span 'Similar Lengths' on note 'Similar Lengths' is anchored by the corpus spec_point block spcpt_xDpKVBxDTCk2x6vS and joined to 4MA1-4.11A via name_to_statement_join; this section chunk sits inside that span.
- Verdict: [ ] CONFIRM — this chunk belongs to this SP   [ ] REJECT — wrong chunk/SP   [ ] HOLD — needs rework

### 4MA1-1.7D — calculate an unknown quantity from quantities that vary in direct proportion
- Note: Direct Proportion (`notes/1-numbers-and-the-number-system/direct-and-inverse-proportion/direct-proportion.json`)
- Chunk: ordinal 3 — heading `How do I find the equation between two directly proportional variables?` — sha256_16 `a6a2f27d0f577600` — 1928 chars
- Evidence quote (verbatim self-slice, markdown-safe): "How do I find the equation between two directly proportional variables?
- Direct proportion questions always have the same process:

  - **STEP 1**
  **Identify** the two variables and write down the **formula in terms of *****k***
  
    -"
- Chunk excerpt: «How do I find the equation between two directly proportional variables? - Direct proportion questions always have the same process: - **STEP 1** **Identify** the two variables and write down the **formula in terms of *****k*** - E.g. ***y*** is **directly **proportional to ***x*** - write down the formula $y=kx$ - **STEP 2** **Find** ***k*** by substituting any given values **from the question** into your formula, th»
- Upstream: T-C32 join notes/1-numbers-and-the-number-system/direct-and-inverse-proportion/direct-proportion.json::spcpt_BktcXhHcVFw8R9Q2 — tier S1_name_match — score 0.7462 — wording EXACT — validation tier AI_VALIDATED (operator-delegated chain)
- Rationale: SME span 'Direct Proportion' on note 'Direct Proportion' is anchored by the corpus spec_point block spcpt_BktcXhHcVFw8R9Q2 and joined to 4MA1-1.7D via name_to_statement_join; this section chunk sits inside that span.
- Verdict: [ ] CONFIRM — this chunk belongs to this SP   [ ] REJECT — wrong chunk/SP   [ ] HOLD — needs rework

### 4MA1-4.4B — calculate time intervals in terms of the 24-hour and the 12-hour clock
- Note: Time (`notes/4-geometry-and-trigonometry/standard-and-compound-units/time.json`)
- Chunk: ordinal 2 — heading `What is the difference between a 12-hour clock and a 24-hour clock?` — sha256_16 `4dbe204a5d33bd23` — 774 chars
- Evidence quote (verbatim self-slice, markdown-safe): "What is the difference between a 12-hour clock and a 24-hour clock?
- A **12-hour clock** goes around once for AM and once for PM in **one complete day**

  - AM is between midnight (12 am) and midday (12 pm)
  - PM is between midday (12 pm"
- Chunk excerpt: «What is the difference between a 12-hour clock and a 24-hour clock? - A **12-hour clock** goes around once for AM and once for PM in **one complete day** - AM is between midnight (12 am) and midday (12 pm) - PM is between midday (12 pm) and midnight (12 am) - A **24-hour clock** goes around once for **one complete day** - The display uses four digits, two for the hour, two for the minutes - The day starts at midnight»
- Upstream: T-C32 join notes/4-geometry-and-trigonometry/standard-and-compound-units/time.json::spcpt_h2p7nv6zkR4xFJ3P — tier S2_name_ambiguous — score 0.6432 — wording EXACT — validation tier AI_VALIDATED (operator-delegated chain)
- Rationale: SME span 'Time' on note 'Time' is anchored by the corpus spec_point block spcpt_h2p7nv6zkR4xFJ3P and joined to 4MA1-4.4B via name_to_statement_join; this section chunk sits inside that span.
- Verdict: [ ] CONFIRM — this chunk belongs to this SP   [ ] REJECT — wrong chunk/SP   [ ] HOLD — needs rework

### 4MA1-1.5E — use Venn diagrams to represent sets
- Note: Set Notation & Venn Diagrams (`notes/1-numbers-and-the-number-system/set-notation-and-venn-diagrams/set-notation-and-venn-diagrams.json`)
- Chunk: ordinal 5 — heading `What do the different regions mean on a Venn diagram?` — sha256_16 `713025fdbad526b9` — 2168 chars
- Evidence quote (verbatim self-slice, markdown-safe): "What do the different regions mean on a Venn diagram?
- $A\cupB$  is represented by the regions that **are in** *A * or *B * or both
- $A\capB$  is represented by the region where the *A*  and *B  *circles **overlap**
Venn diagrams showing "
- Chunk excerpt: «What do the different regions mean on a Venn diagram? - $A\cupB$ is represented by the regions that **are in** *A * or *B * or both - $A\capB$ is represented by the region where the *A* and *B *circles **overlap** Venn diagrams showing the union and the intersection of sets A and B - The two circles intersect and split the rectangle into **four regions** - A region where **both circles intersect** - $A\capB$ - Two re»
- Upstream: T-C32 join notes/1-numbers-and-the-number-system/set-notation-and-venn-diagrams/set-notation-and-venn-diagrams.json::spcpt_XT9QGzbhpThbfcB6 — tier S1_name_match — score 0.8415 — wording EXACT — validation tier AI_VALIDATED (operator-delegated chain)
- Rationale: SME span 'Sets & Venn Diagrams' on note 'Set Notation & Venn Diagrams' is anchored by the corpus spec_point block spcpt_XT9QGzbhpThbfcB6 and joined to 4MA1-1.5E via name_to_statement_join; this section chunk sits inside that span.
- Verdict: [ ] CONFIRM — this chunk belongs to this SP   [ ] REJECT — wrong chunk/SP   [ ] HOLD — needs rework

### 4MA1-1.7B — divide a quantity in a given ratio or ratios
- Note: Introduction to Ratios (`notes/1-numbers-and-the-number-system/ratio-toolkit/simple-ratio.json`)
- Chunk: ordinal 3 — heading `What is an equivalent ratio?` — sha256_16 `4c59d6d8a58fa7f9` — 544 chars
- Evidence quote (verbatim self-slice, markdown-safe): "What is an equivalent ratio?
- **Equivalent ratios** are two ratios that represent the **same proportion **of quantities within a whole

  - E.g. The ratio **5 : 10** is equivalent to **20 : 40**
- Equivalent ratios are frequently used when"
- Chunk excerpt: «What is an equivalent ratio? - **Equivalent ratios** are two ratios that represent the **same proportion **of quantities within a whole - E.g. The ratio **5 : 10** is equivalent to **20 : 40** - Equivalent ratios are frequently used when the values involved take on a **real-life meaning** - E.g. A cake recipe involves flour and butter being mixed in the ratio 3 : 2 - 3 g of flour and 2 g of butter would not lead to a»
- Upstream: T-C32 join notes/1-numbers-and-the-number-system/ratio-toolkit/simple-ratio.json::spcpt_qpSmD6yNY5t5GrW6 — tier S1_name_match — score 0.696 — wording EXACT — validation tier AI_VALIDATED (operator-delegated chain)
- Rationale: SME span 'Ratios' on note 'Introduction to Ratios' is anchored by the corpus spec_point block spcpt_qpSmD6yNY5t5GrW6 and joined to 4MA1-1.7B via name_to_statement_join; this section chunk sits inside that span.
- Verdict: [ ] CONFIRM — this chunk belongs to this SP   [ ] REJECT — wrong chunk/SP   [ ] HOLD — needs rework

### 4MA1-4.4B — calculate time intervals in terms of the 24-hour and the 12-hour clock
- Note: Time (`notes/4-geometry-and-trigonometry/standard-and-compound-units/time.json`)
- Chunk: ordinal 4 — heading `How do I read the time from a digital clock?` — sha256_16 `ab24e37c3fadf491` — 483 chars
- Evidence quote (verbatim self-slice, markdown-safe): "How do I read the time from a digital clock?
- A **digital** clock can use either **24 hour** time or **12-hour** time

  - A colon ':' is often displayed between the hours and minutes
  
    - E.g.,  1245 would be displayed as 12:45
  - AM"
- Chunk excerpt: «How do I read the time from a digital clock? - A **digital** clock can use either **24 hour** time or **12-hour** time - A colon ':' is often displayed between the hours and minutes - E.g., 1245 would be displayed as 12:45 - AM or PM does **not** need to be specified with 24-hour time - it may or may not be shown on a 12-hour time digital clock - For** single-digit** hours, clocks often miss out the first zero - e.g.»
- Upstream: T-C32 join notes/4-geometry-and-trigonometry/standard-and-compound-units/time.json::spcpt_h2p7nv6zkR4xFJ3P — tier S2_name_ambiguous — score 0.6432 — wording EXACT — validation tier AI_VALIDATED (operator-delegated chain)
- Rationale: SME span 'Time' on note 'Time' is anchored by the corpus spec_point block spcpt_h2p7nv6zkR4xFJ3P and joined to 4MA1-4.4B via name_to_statement_join; this section chunk sits inside that span.
- Verdict: [ ] CONFIRM — this chunk belongs to this SP   [ ] REJECT — wrong chunk/SP   [ ] HOLD — needs rework

### 4MA1-4.4D — understand angle measure including three-figure bearings
- Note: Bearings (`notes/4-geometry-and-trigonometry/bearings-scale-drawing-and-constructions/bearings.json`)
- Chunk: ordinal 5 — heading `How do I answer trickier questions involving bearings?` — sha256_16 `6bef600ae7340312` — 2435 chars
- Evidence quote (verbatim self-slice, markdown-safe): "How do I answer trickier questions involving bearings?
- Bearings questions may involve the use of **Pythagoras** or **trigonometry** to find missing distances (lengths) and directions (angles)

  - You should always** draw a diagram** if t"
- Chunk excerpt: «How do I answer trickier questions involving bearings? - Bearings questions may involve the use of **Pythagoras** or **trigonometry** to find missing distances (lengths) and directions (angles) - You should always** draw a diagram** if there isn't one given Exam Hint: Make sure you have all the **equipment **you need for your maths exams. A rubber and pencil sharpener can be essential as these questions are all about»
- Upstream: T-C32 join notes/4-geometry-and-trigonometry/bearings-scale-drawing-and-constructions/bearings.json::spcpt_38XcCSfT6hW33fDn — tier S1_name_match — score 0.7 — wording EXACT — validation tier AI_VALIDATED (operator-delegated chain)
- Rationale: SME span 'Bearings' on note 'Bearings' is anchored by the corpus spec_point block spcpt_38XcCSfT6hW33fDn and joined to 4MA1-4.4D via name_to_statement_join; this section chunk sits inside that span.
- Verdict: [ ] CONFIRM — this chunk belongs to this SP   [ ] REJECT — wrong chunk/SP   [ ] HOLD — needs rework

### 4MA1-1.2B — understand and use mixed numbers and vulgar fractions
- Note: Mixed Numbers & Improper Fractions (`notes/1-numbers-and-the-number-system/fractions/mixed-numbers-and-improper-fractions.json`)
- Chunk: ordinal 0 — heading `Mixed numbers & improper fractions` — sha256_16 `397f69703f1a6c49` — 34 chars
- Evidence quote (verbatim self-slice, markdown-safe): "Mixed numbers & improper fractions"
- Chunk excerpt: «Mixed numbers & improper fractions»
- Upstream: T-C32 join notes/1-numbers-and-the-number-system/fractions/mixed-numbers-and-improper-fractions.json::spcpt_6XysCMWvYY936jw8 — tier S1_name_match — score 0.6853 — wording EXACT — validation tier AI_VALIDATED (operator-delegated chain)
- Rationale: SME span 'Mixed Numbers & Improper Fractions' on note 'Mixed Numbers & Improper Fractions' is anchored by the corpus spec_point block spcpt_6XysCMWvYY936jw8 and joined to 4MA1-1.2B via name_to_statement_join; this section chunk sits inside that span.
- Verdict: [ ] CONFIRM — this chunk belongs to this SP   [ ] REJECT — wrong chunk/SP   [ ] HOLD — needs rework

### 4MA1-2.7D — solve simultaneous equations in two unknowns, one equation being linear and the other being quadratic
- Note: Linear Simultaneous Equations (`notes/2-equations-formulae-and-identities/simultaneous-equations/linear.json`)
- Chunk: ordinal 0 — heading `Linear simultaneous equations` — sha256_16 `90413a58ba9b459e` — 29 chars
- Evidence quote (verbatim self-slice, markdown-safe): "Linear simultaneous equations"
- Chunk excerpt: «Linear simultaneous equations»
- Upstream: T-C32 join notes/2-equations-formulae-and-identities/simultaneous-equations/linear.json::spcpt_h5yjgd2WdgmJqHJM — tier S1_name_match — score 0.755 — wording EXACT — validation tier AI_VALIDATED (operator-delegated chain)
- Rationale: SME span 'Linear Simultaneous Equations' on note 'Linear Simultaneous Equations' is anchored by the corpus spec_point block spcpt_h5yjgd2WdgmJqHJM and joined to 4MA1-2.7D via name_to_statement_join; this section chunk sits inside that span.
- Verdict: [ ] CONFIRM — this chunk belongs to this SP   [ ] REJECT — wrong chunk/SP   [ ] HOLD — needs rework

### 4MA1-4.2D — understand the term ‘regular polygon’ and calculate interior and exterior angles of regular polygons
- Note: Angles in Polygons (`notes/4-geometry-and-trigonometry/angles-in-polygons-and-parallel-lines/angles-in-polygons.json`)
- Chunk: ordinal 4 — heading `What is the sum of the exterior angles in a polygon?` — sha256_16 `40a68e5c3e23b75c` — 120 chars
- Evidence quote (verbatim self-slice, markdown-safe): "What is the sum of the exterior angles in a polygon?
- The** exterior angles **in **any **polygon always **sum to 360°**"
- Chunk excerpt: «What is the sum of the exterior angles in a polygon? - The** exterior angles **in **any **polygon always **sum to 360°**»
- Upstream: T-C32 join notes/4-geometry-and-trigonometry/angles-in-polygons-and-parallel-lines/angles-in-polygons.json::spcpt_gzykj64JBx2RtBJ7 — tier S2_name_ambiguous — score 0.7085 — wording EXACT — validation tier AI_VALIDATED (operator-delegated chain)
- Rationale: SME span 'Angles in Polygons' on note 'Angles in Polygons' is anchored by the corpus spec_point block spcpt_gzykj64JBx2RtBJ7 and joined to 4MA1-4.2D via name_to_statement_join; this section chunk sits inside that span.
- Verdict: [ ] CONFIRM — this chunk belongs to this SP   [ ] REJECT — wrong chunk/SP   [ ] HOLD — needs rework

### 4MA1-1.4E — find highest common factors (HCF) and lowest common multiples (LCM)
- Note: HCF & LCM (`notes/1-numbers-and-the-number-system/prime-factors-hcf-and-lcm/hcf-and-lcm.json`)
- Chunk: ordinal 0 — heading `Highest common factor (HCF)` — sha256_16 `1d62b40f7b235b97` — 27 chars
- Evidence quote (verbatim self-slice, markdown-safe): "Highest common factor (HCF)"
- Chunk excerpt: «Highest common factor (HCF)»
- Upstream: T-C32 join notes/1-numbers-and-the-number-system/prime-factors-hcf-and-lcm/hcf-and-lcm.json::spcpt_P88yS9wysymQ2brq — tier S1_name_match — score 0.6798 — wording EXACT — validation tier AI_VALIDATED (operator-delegated chain)
- Rationale: SME span 'Highest Common Factor (HCF)' on note 'HCF & LCM' is anchored by the corpus spec_point block spcpt_P88yS9wysymQ2brq and joined to 4MA1-1.4E via name_to_statement_join; this section chunk sits inside that span.
- Verdict: [ ] CONFIRM — this chunk belongs to this SP   [ ] REJECT — wrong chunk/SP   [ ] HOLD — needs rework

### 4MA1-3.3I — recognise, generate points and plot graphs of linear and quadratic functions
- Note: Quadratic Graphs (`notes/3-sequences-functions-and-graphs/graphs-of-functions/quadratic-graphs.json`)
- Chunk: ordinal 1 — heading `What is a quadratic graph?` — sha256_16 `05c51a1cb7985b95` — 106 chars
- Evidence quote (verbatim self-slice, markdown-safe): "What is a quadratic graph?
- A **quadratic graph** has the form $y=ax^{2}+bx+c$

  - where $a$ is not zero"
- Chunk excerpt: «What is a quadratic graph? - A **quadratic graph** has the form $y=ax^{2}+bx+c$ - where $a$ is not zero»
- Upstream: T-C32 join notes/3-sequences-functions-and-graphs/graphs-of-functions/quadratic-graphs.json::spcpt_76gVqdMN62jnrZg6 — tier S1_name_match — score 0.6967 — wording EXACT — validation tier AI_VALIDATED (operator-delegated chain)
- Rationale: SME span 'Quadratic Graphs' on note 'Quadratic Graphs' is anchored by the corpus spec_point block spcpt_76gVqdMN62jnrZg6 and joined to 4MA1-3.3I via name_to_statement_join; this section chunk sits inside that span.
- Verdict: [ ] CONFIRM — this chunk belongs to this SP   [ ] REJECT — wrong chunk/SP   [ ] HOLD — needs rework

### 4MA1-4.9B — find the perimeter of shapes made from triangles and rectangles
- Note: Perimeter (`notes/4-geometry-and-trigonometry/area-and-perimeter/perimeter.json`)
- Chunk: ordinal 0 — heading `Perimeter` — sha256_16 `e015df51e98adda5` — 9 chars
- Evidence quote (verbatim self-slice, markdown-safe): "Perimeter"
- Chunk excerpt: «Perimeter»
- Upstream: T-C32 join notes/4-geometry-and-trigonometry/area-and-perimeter/perimeter.json::spcpt_W2yYk784rNVZBxPh — tier S1_name_match — score 0.7 — wording EXACT — validation tier AI_VALIDATED (operator-delegated chain)
- Rationale: SME span 'Perimeter' on note 'Perimeter' is anchored by the corpus spec_point block spcpt_W2yYk784rNVZBxPh and joined to 4MA1-4.9B via name_to_statement_join; this section chunk sits inside that span.
- Verdict: [ ] CONFIRM — this chunk belongs to this SP   [ ] REJECT — wrong chunk/SP   [ ] HOLD — needs rework

### 4MA1-6.1C — use cumulative frequency diagrams
- Note: Reading & Interpreting Statistical Diagrams (`notes/6-statistics-and-probability/statistics-toolkit/working-with-statistical-diagrams.json`)
- Chunk: ordinal 1 — heading `How do I interpret statistical diagrams?` — sha256_16 `e29667d77b3c32e9` — 1003 chars
- Evidence quote (verbatim self-slice, markdown-safe): "How do I interpret statistical diagrams?
- Read and **understand** the initial sentences describing the **situation** (context)

  - **Underline** important words if necessary
- Look for any** keys **that may help you to understand the diag"
- Chunk excerpt: «How do I interpret statistical diagrams? - Read and **understand** the initial sentences describing the **situation** (context) - **Underline** important words if necessary - Look for any** keys **that may help you to understand the diagram - For example - 1 unit represents 20 people - Year 10 is the **solid** line, Year 11 is the **dotted** line - Class A is **shaded**, class B is **striped** - **Read **the **titles»
- Upstream: T-C32 join notes/6-statistics-and-probability/statistics-toolkit/working-with-statistical-diagrams.json::spcpt_bGtx4SMcX6BRS6KP — tier S1_name_match — score 0.638 — wording EXACT — validation tier AI_VALIDATED (operator-delegated chain)
- Rationale: SME span 'Reading & Interpreting Statistical Diagrams' on note 'Reading & Interpreting Statistical Diagrams' is anchored by the corpus spec_point block spcpt_bGtx4SMcX6BRS6KP and joined to 4MA1-6.1C via name_to_statement_join; this section chunk sits inside that span.
- Verdict: [ ] CONFIRM — this chunk belongs to this SP   [ ] REJECT — wrong chunk/SP   [ ] HOLD — needs rework

### 4MA1-2.7B — solve quadratic equations by using the quadratic formula or completing the square
- Note: Completing the Square (`notes/2-equations-formulae-and-identities/completing-the-square/completing-the-square.json`)
- Chunk: ordinal 2 — heading `How do I complete the square?` — sha256_16 `69ca60a331f5ceb0` — 498 chars
- Evidence quote (verbatim self-slice, markdown-safe): "How do I complete the square?
- **Completing the square** is a way to rewrite a quadratic expression in a form containing a **squared bracket**
- To complete the square on *x*<sup>2</sup> + 10*x* + 9

  - Use the rule above to replace the f"
- Chunk excerpt: «How do I complete the square? - **Completing the square** is a way to rewrite a quadratic expression in a form containing a **squared bracket** - To complete the square on *x*<sup>2</sup> + 10*x* + 9 - Use the rule above to replace the first two terms, *x*<sup>2</sup> + 10*x, *with (*x* + 5)<sup>2</sup> - 5<sup>2</sup> - then add 9: (*x* + 5)<sup>2</sup> - 5<sup>2 </sup>+ 9 - **simplify** the **numbers**: (*x* + 5)<s»
- Upstream: T-C32 join notes/2-equations-formulae-and-identities/completing-the-square/completing-the-square.json::spcpt_9Stcxtj75Q3wpqJF — tier S1_name_match — score 0.7647 — wording EXACT — validation tier AI_VALIDATED (operator-delegated chain)
- Rationale: SME span 'Completing the Square' on note 'Completing the Square' is anchored by the corpus spec_point block spcpt_9Stcxtj75Q3wpqJF and joined to 4MA1-2.7B via name_to_statement_join; this section chunk sits inside that span.
- Verdict: [ ] CONFIRM — this chunk belongs to this SP   [ ] REJECT — wrong chunk/SP   [ ] HOLD — needs rework

### 4MA1-3.4C — determine gradients, rates of change, stationary points, turning points (maxima and minima) by differentiation and relate these to graphs
- Note: Finding Stationary Points & Turning Points (`notes/3-sequences-functions-and-graphs/differentiation/applications-of-differentiation.json`)
- Chunk: ordinal 1 — heading `What is a stationary point?` — sha256_16 `cf93f9cd7c2054c1` — 1118 chars
- Evidence quote (verbatim self-slice, markdown-safe): "What is a stationary point?
- A **stationary point** is a point on the graph at which the **gradient is zero** (a tangent drawn at this point will be **horizontal**)

  - These* include *peaks (**maximum points**) and troughs (**minimum poi"
- Chunk excerpt: «What is a stationary point? - A **stationary point** is a point on the graph at which the **gradient is zero** (a tangent drawn at this point will be **horizontal**) - These* include *peaks (**maximum points**) and troughs (**minimum points**) - Maximum points and minimum points are collectively know as **turning points** - At a turning point a curve **changes** from **moving upwards** to **moving downwards**, or vic»
- Upstream: T-C32 join notes/3-sequences-functions-and-graphs/differentiation/applications-of-differentiation.json::spcpt_pKJ7Y3jd7PDzZQpP — tier S1_name_match — score 0.6293 — wording EXACT — validation tier AI_VALIDATED (operator-delegated chain)
- Rationale: SME span 'Finding Stationary Points & Turning Points' on note 'Finding Stationary Points & Turning Points' is anchored by the corpus spec_point block spcpt_pKJ7Y3jd7PDzZQpP and joined to 4MA1-3.4C via name_to_statement_join; this section chunk sits inside that span.
- Verdict: [ ] CONFIRM — this chunk belongs to this SP   [ ] REJECT — wrong chunk/SP   [ ] HOLD — needs rework

### 4MA1-4.10F — convert between units of volume within the metric system
- Note: Volume (`notes/4-geometry-and-trigonometry/volume-and-surface-area/volume.json`)
- Chunk: ordinal 0 — heading `Volume` — sha256_16 `b10fb966d72063f5` — 6 chars
- Evidence quote (verbatim self-slice, markdown-safe): "Volume"
- Chunk excerpt: «Volume»
- Upstream: T-C32 join notes/4-geometry-and-trigonometry/volume-and-surface-area/volume.json::spcpt_pKCFj25GzzqW6sr3 — tier S2_name_ambiguous — score 0.6774 — wording EXACT — validation tier AI_VALIDATED (operator-delegated chain)
- Rationale: SME span 'Volume' on note 'Volume' is anchored by the corpus spec_point block spcpt_pKCFj25GzzqW6sr3 and joined to 4MA1-4.10F via name_to_statement_join; this section chunk sits inside that span.
- Verdict: [ ] CONFIRM — this chunk belongs to this SP   [ ] REJECT — wrong chunk/SP   [ ] HOLD — needs rework

### 4MA1-3.4E — apply calculus to linear kinematics and to other simple practical problems
- Note: Using Differentiation for Kinematics (`notes/3-sequences-functions-and-graphs/differentiation/kinematics.json`)
- Chunk: ordinal 0 — heading `Kinematics` — sha256_16 `3c44d96f7f5bea9f` — 10 chars
- Evidence quote (verbatim self-slice, markdown-safe): "Kinematics"
- Chunk excerpt: «Kinematics»
- Upstream: T-C32 join notes/3-sequences-functions-and-graphs/differentiation/kinematics.json::spcpt_vYsrWKqpQDpSwnPj — tier S1_name_match — score 0.6952 — wording EXACT — validation tier AI_VALIDATED (operator-delegated chain)
- Rationale: SME span 'Kinematics' on note 'Using Differentiation for Kinematics' is anchored by the corpus spec_point block spcpt_vYsrWKqpQDpSwnPj and joined to 4MA1-3.4E via name_to_statement_join; this section chunk sits inside that span.
- Verdict: [ ] CONFIRM — this chunk belongs to this SP   [ ] REJECT — wrong chunk/SP   [ ] HOLD — needs rework

### 4MA1-6.1A — construct and interpret histograms
- Note: Bar Charts & Pictograms (`notes/6-statistics-and-probability/statistics-toolkit/bar-charts-and-pictograms.json`)
- Chunk: ordinal 0 — heading `Bar charts & pictograms` — sha256_16 `38027656f2cb269a` — 23 chars
- Evidence quote (verbatim self-slice, markdown-safe): "Bar charts & pictograms"
- Chunk excerpt: «Bar charts & pictograms»
- Upstream: T-C32 join notes/6-statistics-and-probability/statistics-toolkit/bar-charts-and-pictograms.json::spcpt_kHwc5r3247TGRwyS — tier S1_name_match — score 0.7253 — wording EXACT — validation tier AI_VALIDATED (operator-delegated chain)
- Rationale: SME span 'Bar Charts & Pictograms' on note 'Bar Charts & Pictograms' is anchored by the corpus spec_point block spcpt_kHwc5r3247TGRwyS and joined to 4MA1-6.1A via name_to_statement_join; this section chunk sits inside that span.
- Verdict: [ ] CONFIRM — this chunk belongs to this SP   [ ] REJECT — wrong chunk/SP   [ ] HOLD — needs rework

### 4MA1-6.1A — construct and interpret histograms
- Note: Bar Charts & Pictograms (`notes/6-statistics-and-probability/statistics-toolkit/bar-charts-and-pictograms.json`)
- Chunk: ordinal 2 — heading `What is a pictogram?` — sha256_16 `5c1aabea6bf5921c` — 1553 chars
- Evidence quote (verbatim self-slice, markdown-safe): "What is a pictogram?
- A **pictogram** is an **alternative **to a bar chart

  - It is used in the same situations
- There are **no axes**

  - **Frequency** is represented by **symbols**
  - A** key **shows the value of 1 symbol
  
    - F"
- Chunk excerpt: «What is a pictogram? - A **pictogram** is an **alternative **to a bar chart - It is used in the same situations - There are **no axes** - **Frequency** is represented by **symbols** - A** key **shows the value of 1 symbol - For example, 1 symbol represents a frequency of 2 - Half and quarter symbols are often used Example of a pictogram - The pictogram above shows the shoe sizes of students in a class - As 1 picture »
- Upstream: T-C32 join notes/6-statistics-and-probability/statistics-toolkit/bar-charts-and-pictograms.json::spcpt_kHwc5r3247TGRwyS — tier S1_name_match — score 0.7253 — wording EXACT — validation tier AI_VALIDATED (operator-delegated chain)
- Rationale: SME span 'Bar Charts & Pictograms' on note 'Bar Charts & Pictograms' is anchored by the corpus spec_point block spcpt_kHwc5r3247TGRwyS and joined to 4MA1-6.1A via name_to_statement_join; this section chunk sits inside that span.
- Verdict: [ ] CONFIRM — this chunk belongs to this SP   [ ] REJECT — wrong chunk/SP   [ ] HOLD — needs rework

### 4MA1-4.5C — solve problems using scale drawings
- Note: Scale (`notes/4-geometry-and-trigonometry/bearings-scale-drawing-and-constructions/scale.json`)
- Chunk: ordinal 0 — heading `Scale` — sha256_16 `f102986b39effb31` — 5 chars
- Evidence quote (verbatim self-slice, markdown-safe): "Scale"
- Chunk excerpt: «Scale»
- Upstream: T-C32 join notes/4-geometry-and-trigonometry/bearings-scale-drawing-and-constructions/scale.json::spcpt_5Wj647RsttH6ZNfd — tier S2_name_ambiguous — score 0.7 — wording EXACT — validation tier AI_VALIDATED (operator-delegated chain)
- Rationale: SME span 'Scale' on note 'Scale' is anchored by the corpus spec_point block spcpt_5Wj647RsttH6ZNfd and joined to 4MA1-4.5C via name_to_statement_join; this section chunk sits inside that span.
- Verdict: [ ] CONFIRM — this chunk belongs to this SP   [ ] REJECT — wrong chunk/SP   [ ] HOLD — needs rework

### 4MA1-1.6G — use compound interest and depreciation
- Note: Depreciation (`notes/1-numbers-and-the-number-system/compound-interest-and-depreciation/depreciation.json`)
- Chunk: ordinal 2 — heading `How do I calculate depreciation?` — sha256_16 `2e9f9daaa742bbf5` — 511 chars
- Evidence quote (verbatim self-slice, markdown-safe): "How do I calculate depreciation?
- A similar method  to **compound interest** can be used
- Change the **multiplier **to one which represents a **percentage decrease**

  - e.g. a **decrease of 15%** would be a **multiplier **of **0.85**
- "
- Chunk excerpt: «How do I calculate depreciation? - A similar method to **compound interest** can be used - Change the **multiplier **to one which represents a **percentage decrease** - e.g. a **decrease of 15%** would be a **multiplier **of **0.85** - If a car worth \$16 000 depreciates by 15% each year for 6 years - Its value will be 16 000 × 0.85<sup>6</sup>, which is \$6034.39 - If you are asked to find the amount the value has d»
- Upstream: T-C32 join notes/1-numbers-and-the-number-system/compound-interest-and-depreciation/depreciation.json::spcpt_rDHZfZ8PrdwXcT2y — tier S1_name_match — score 0.792 — wording EXACT — validation tier AI_VALIDATED (operator-delegated chain)
- Rationale: SME span 'Depreciation' on note 'Depreciation' is anchored by the corpus spec_point block spcpt_rDHZfZ8PrdwXcT2y and joined to 4MA1-1.6G via name_to_statement_join; this section chunk sits inside that span.
- Verdict: [ ] CONFIRM — this chunk belongs to this SP   [ ] REJECT — wrong chunk/SP   [ ] HOLD — needs rework

### 4MA1-5.2D — understand that reflections are specified by a mirror line
- Note: Reflections (`notes/5-vectors-and-transformation-geometry/transformations/reflections.json`)
- Chunk: ordinal 5 — heading `How do I reverse a reflection?` — sha256_16 `a603cf4c263669c6` — 1590 chars
- Evidence quote (verbatim self-slice, markdown-safe): "How do I reverse a reflection?
- If a shape has been reflected to a new position, you can perform a single transformation to **return the shape** to its **original position**

  - You can **reverse the reflection**
- The transformation to *"
- Chunk excerpt: «How do I reverse a reflection? - If a shape has been reflected to a new position, you can perform a single transformation to **return the shape** to its **original position** - You can **reverse the reflection** - The transformation to **reverse a reflection**, is the **same transformation **as the** original ** - E.g. If a shape is reflected in the *x*-axis, then reflecting it again in the *x*-axis will return it to»
- Upstream: T-C32 join notes/5-vectors-and-transformation-geometry/transformations/reflections.json::spcpt_DQrkJGG4Mngch9xc — tier S1_name_match — score 0.7275 — wording EXACT — validation tier AI_VALIDATED (operator-delegated chain)
- Rationale: SME span 'Reflections' on note 'Reflections' is anchored by the corpus spec_point block spcpt_DQrkJGG4Mngch9xc and joined to 4MA1-5.2D via name_to_statement_join; this section chunk sits inside that span.
- Verdict: [ ] CONFIRM — this chunk belongs to this SP   [ ] REJECT — wrong chunk/SP   [ ] HOLD — needs rework

### 4MA1-1.5B — use Venn diagrams to represent sets and the number of elements in sets
- Note: Set Notation & Venn Diagrams (`notes/1-numbers-and-the-number-system/set-notation-and-venn-diagrams/set-notation-and-venn-diagrams.json`)
- Chunk: ordinal 2 — heading `What do I need to know about set notation?` — sha256_16 `ec138af6ec59be04` — 2145 chars
- Evidence quote (verbatim self-slice, markdown-safe): "What do I need to know about set notation?
- $E$ is the **universal** set (the set of **everything**)

  - For example, if we are only interested in factors of 24 then $E$ = {1, 2, 3, 4, 6, 8, 12, 24}
- We use **upper case** letters to repr"
- Chunk excerpt: «What do I need to know about set notation? - $E$ is the **universal** set (the set of **everything**) - For example, if we are only interested in factors of 24 then $E$ = {1, 2, 3, 4, 6, 8, 12, 24} - We use **upper case** letters to represent **sets** (*A*,* B*,* C*, ...) and **lower case** letters to represent **elements **(*a*,* b*,* c*, ...) - n(*A*) is the **number of elements** in set *A* - For example, if $E$ =»
- Upstream: T-C32 join notes/1-numbers-and-the-number-system/set-notation-and-venn-diagrams/set-notation-and-venn-diagrams.json::spcpt_CG8ZcZX8Ny5yGBch — tier S1_name_match — score 0.84 — wording EXACT — validation tier AI_VALIDATED (operator-delegated chain)
- Rationale: SME span 'Set Notation' on note 'Set Notation & Venn Diagrams' is anchored by the corpus spec_point block spcpt_CG8ZcZX8Ny5yGBch and joined to 4MA1-1.5B via name_to_statement_join; this section chunk sits inside that span.
- Verdict: [ ] CONFIRM — this chunk belongs to this SP   [ ] REJECT — wrong chunk/SP   [ ] HOLD — needs rework

### 4MA1-4.10D — find the surface area of a cylinder
- Note: Surface Area (`notes/4-geometry-and-trigonometry/volume-and-surface-area/surface-area.json`)
- Chunk: ordinal 4 — heading `How do I find the surface area of a cone?` — sha256_16 `57338688d506a532` — 743 chars
- Evidence quote (verbatim self-slice, markdown-safe): "How do I find the surface area of a cone?
- A cone has **one flat surface** (the base) and **one curved surface**
- The net of a cone, with radius, *r*, perpendicular height, *h*, and sloping edge, (slant height), *l*, consists of

  - A **"
- Chunk excerpt: «How do I find the surface area of a cone? - A cone has **one flat surface** (the base) and **one curved surface** - The net of a cone, with radius, *r*, perpendicular height, *h*, and sloping edge, (slant height), *l*, consists of - A **circular** **base** - A **sector** with radius, *l*, and an arc length equal to the circumference of the base A cone and its net - The **curved surface area** of a cone, *A*, with rad»
- Upstream: T-C32 join notes/4-geometry-and-trigonometry/volume-and-surface-area/surface-area.json::spcpt_2w9hbV5pTbvc5Smj — tier S1_name_match — score 0.8043 — wording EXACT — validation tier AI_VALIDATED (operator-delegated chain)
- Rationale: SME span 'Surface Area' on note 'Surface Area' is anchored by the corpus spec_point block spcpt_2w9hbV5pTbvc5Smj and joined to 4MA1-4.10D via name_to_statement_join; this section chunk sits inside that span.
- Verdict: [ ] CONFIRM — this chunk belongs to this SP   [ ] REJECT — wrong chunk/SP   [ ] HOLD — needs rework

### 4MA1-4.4B — calculate time intervals in terms of the 24-hour and the 12-hour clock
- Note: Time (`notes/4-geometry-and-trigonometry/standard-and-compound-units/time.json`)
- Chunk: ordinal 5 — heading `How do I calculate with time using the 12-hour clock?` — sha256_16 `b1c7fd791b249718` — 2635 chars
- Evidence quote (verbatim self-slice, markdown-safe): "How do I calculate with time using the 12-hour clock?
- Work in **chunks** of time

  - Calculate the **minutes until the** **next hour**, then **whole hours**, then **minutes until a final time**
- Ensure you know when the 12-hour clock **"
- Chunk excerpt: «How do I calculate with time using the 12-hour clock? - Work in **chunks** of time - Calculate the **minutes until the** **next hour**, then **whole hours**, then **minutes until a final time** - Ensure you know when the 12-hour clock **switches** from **AM to PM** and vice versa Calculations with the 12-hour clock Exam Hint: Be careful when using a calculator, as they can often cause problems in time-based questions»
- Upstream: T-C32 join notes/4-geometry-and-trigonometry/standard-and-compound-units/time.json::spcpt_h2p7nv6zkR4xFJ3P — tier S2_name_ambiguous — score 0.6432 — wording EXACT — validation tier AI_VALIDATED (operator-delegated chain)
- Rationale: SME span 'Time' on note 'Time' is anchored by the corpus spec_point block spcpt_h2p7nv6zkR4xFJ3P and joined to 4MA1-4.4B via name_to_statement_join; this section chunk sits inside that span.
- Verdict: [ ] CONFIRM — this chunk belongs to this SP   [ ] REJECT — wrong chunk/SP   [ ] HOLD — needs rework

### 4MA1-2.7D — solve simultaneous equations in two unknowns, one equation being linear and the other being quadratic
- Note: Quadratic Simultaneous Equations (`notes/2-equations-formulae-and-identities/simultaneous-equations/quadratic.json`)
- Chunk: ordinal 5 — heading `What if I can't substitute one equation into the other straight away?` — sha256_16 `8736b9d0bdef63c6` — 3730 chars
- Evidence quote (verbatim self-slice, markdown-safe): "What if I can't substitute one equation into the other straight away?
- If the linear equation is **not **in the form *y* = ...  or  *x* = ...

  - You will need to **rearrange **it first, so that it can be **substituted **into the quadrati"
- Chunk excerpt: «What if I can't substitute one equation into the other straight away? - If the linear equation is **not **in the form *y* = ... or *x* = ... - You will need to **rearrange **it first, so that it can be **substituted **into the quadratic equation - Consider solving $xy=3$ and $x+y=4$ - Either: - Rearrange the second equation to $y=4-x$ and substitute into $xy=3$ - `x open parentheses 4 minus x close parentheses equals»
- Upstream: T-C32 join notes/2-equations-formulae-and-identities/simultaneous-equations/quadratic.json::spcpt_pGsqq7xcztBg59Yh — tier S1_name_match — score 0.7394 — wording EXACT — validation tier AI_VALIDATED (operator-delegated chain)
- Rationale: SME span 'Quadratic Simultaneous Equations' on note 'Quadratic Simultaneous Equations' is anchored by the corpus spec_point block spcpt_pGsqq7xcztBg59Yh and joined to 4MA1-2.7D via name_to_statement_join; this section chunk sits inside that span.
- Verdict: [ ] CONFIRM — this chunk belongs to this SP   [ ] REJECT — wrong chunk/SP   [ ] HOLD — needs rework

### 4MA1-4.5C — solve problems using scale drawings
- Note: Scale (`notes/4-geometry-and-trigonometry/bearings-scale-drawing-and-constructions/scale.json`)
- Chunk: ordinal 1 — heading `What is a scale?` — sha256_16 `a5003664927457a0` — 705 chars
- Evidence quote (verbatim self-slice, markdown-safe): "What is a scale?
- For **accurate drawings** and **constructions** scale refers to a **ratio**

  - This ratio describes the relationship between the **drawn size** and the **real-life size**
- **Maps** are usually drawn to a scale
- The ra"
- Chunk excerpt: «What is a scale? - For **accurate drawings** and **constructions** scale refers to a **ratio** - This ratio describes the relationship between the **drawn size** and the **real-life size** - **Maps** are usually drawn to a scale - The ratio will work for **any unit of length** applied to both sides - For example, the scale 1: 50 000 could mean 1 cm = 50 000 cm, 1 km = 50 000 km or even 1 yard = 50 000 yards - If you’»
- Upstream: T-C32 join notes/4-geometry-and-trigonometry/bearings-scale-drawing-and-constructions/scale.json::spcpt_5Wj647RsttH6ZNfd — tier S2_name_ambiguous — score 0.7 — wording EXACT — validation tier AI_VALIDATED (operator-delegated chain)
- Rationale: SME span 'Scale' on note 'Scale' is anchored by the corpus spec_point block spcpt_5Wj647RsttH6ZNfd and joined to 4MA1-4.5C via name_to_statement_join; this section chunk sits inside that span.
- Verdict: [ ] CONFIRM — this chunk belongs to this SP   [ ] REJECT — wrong chunk/SP   [ ] HOLD — needs rework

### 4MA1-5.2D — understand that reflections are specified by a mirror line
- Note: Reflections (`notes/5-vectors-and-transformation-geometry/transformations/reflections.json`)
- Chunk: ordinal 3 — heading `How do I reflect a shape when the line of reflection goes through the shape?` — sha256_16 `a6678d235bfbc6b2` — 1319 chars
- Evidence quote (verbatim self-slice, markdown-safe): "How do I reflect a shape when the line of reflection goes through the shape?
- You follow the **same steps** as above
- Part of the shape gets reflected on **one side** of the mirror line, and the other part gets reflected on the other side"
- Chunk excerpt: «How do I reflect a shape when the line of reflection goes through the shape? - You follow the **same steps** as above - Part of the shape gets reflected on **one side** of the mirror line, and the other part gets reflected on the other side Reflection of a shape where the mirror line goes through the shape Worked Example: On the grid below, reflect shape S in the line $x=-1$. State the coordinates of all of the verti»
- Upstream: T-C32 join notes/5-vectors-and-transformation-geometry/transformations/reflections.json::spcpt_DQrkJGG4Mngch9xc — tier S1_name_match — score 0.7275 — wording EXACT — validation tier AI_VALIDATED (operator-delegated chain)
- Rationale: SME span 'Reflections' on note 'Reflections' is anchored by the corpus spec_point block spcpt_DQrkJGG4Mngch9xc and joined to 4MA1-5.2D via name_to_statement_join; this section chunk sits inside that span.
- Verdict: [ ] CONFIRM — this chunk belongs to this SP   [ ] REJECT — wrong chunk/SP   [ ] HOLD — needs rework

### 4MA1-4.10D — find the surface area of a cylinder
- Note: Surface Area (`notes/4-geometry-and-trigonometry/volume-and-surface-area/surface-area.json`)
- Chunk: ordinal 1 — heading `What is surface area?` — sha256_16 `31a45690102b7145` — 262 chars
- Evidence quote (verbatim self-slice, markdown-safe): "What is surface area?
- The **surface area** of a 3D object is the **sum of the areas of all the faces **that make up the shape

  - Area is a 2D idea being applied into a 3D situation
  - A face is one of the flat or curved **surfaces** th"
- Chunk excerpt: «What is surface area? - The **surface area** of a 3D object is the **sum of the areas of all the faces **that make up the shape - Area is a 2D idea being applied into a 3D situation - A face is one of the flat or curved **surfaces** that make up a 3D object»
- Upstream: T-C32 join notes/4-geometry-and-trigonometry/volume-and-surface-area/surface-area.json::spcpt_2w9hbV5pTbvc5Smj — tier S1_name_match — score 0.8043 — wording EXACT — validation tier AI_VALIDATED (operator-delegated chain)
- Rationale: SME span 'Surface Area' on note 'Surface Area' is anchored by the corpus spec_point block spcpt_2w9hbV5pTbvc5Smj and joined to 4MA1-4.10D via name_to_statement_join; this section chunk sits inside that span.
- Verdict: [ ] CONFIRM — this chunk belongs to this SP   [ ] REJECT — wrong chunk/SP   [ ] HOLD — needs rework

### 4MA1-1.2B — understand and use mixed numbers and vulgar fractions
- Note: Mixed Numbers & Improper Fractions (`notes/1-numbers-and-the-number-system/fractions/mixed-numbers-and-improper-fractions.json`)
- Chunk: ordinal 2 — heading `How do I convert a mixed number into an improper fraction?` — sha256_16 `bf7bb1794c11b0b7` — 388 chars
- Evidence quote (verbatim self-slice, markdown-safe): "How do I convert a mixed number into an improper fraction?
- Consider $5\frac{2}{7}$
- **STEP 1**
**Split **the **whole number **into multiples of the **denominator**

  - 1 whole is equal to 7 sevenths Therefore, 5 is equal to 5 × 7 = 35 s"
- Chunk excerpt: «How do I convert a mixed number into an improper fraction? - Consider $5\frac{2}{7}$ - **STEP 1** **Split **the **whole number **into multiples of the **denominator** - 1 whole is equal to 7 sevenths Therefore, 5 is equal to 5 × 7 = 35 sevenths - **STEP 2** **Add **the **numerator** of the fraction part - 35 sevenths and 2 sevenths make 37 sevenths - $5\frac{2}{7}=\frac{37}{7}$»
- Upstream: T-C32 join notes/1-numbers-and-the-number-system/fractions/mixed-numbers-and-improper-fractions.json::spcpt_6XysCMWvYY936jw8 — tier S1_name_match — score 0.6853 — wording EXACT — validation tier AI_VALIDATED (operator-delegated chain)
- Rationale: SME span 'Mixed Numbers & Improper Fractions' on note 'Mixed Numbers & Improper Fractions' is anchored by the corpus spec_point block spcpt_6XysCMWvYY936jw8 and joined to 4MA1-1.2B via name_to_statement_join; this section chunk sits inside that span.
- Verdict: [ ] CONFIRM — this chunk belongs to this SP   [ ] REJECT — wrong chunk/SP   [ ] HOLD — needs rework

### 4MA1-3.3F — calculate the gradient of a straight line given the coordinates of two points
- Note: Conversion Graphs (`notes/3-sequences-functions-and-graphs/real-life-graphs/conversion-graphs.json`)
- Chunk: ordinal 1 — heading `What is a conversion graph?` — sha256_16 `2277397fba08c318` — 785 chars
- Evidence quote (verbatim self-slice, markdown-safe): "What is a conversion graph?
- A **conversion graph** is a **straight-line** graph relating **two quantities**

  - You can** convert** (change) between them by **reading values** off the graph
- Common examples include

  - **Temperature**
"
- Chunk excerpt: «What is a conversion graph? - A **conversion graph** is a **straight-line** graph relating **two quantities** - You can** convert** (change) between them by **reading values** off the graph - Common examples include - **Temperature** - degrees Celsius (°C) and degrees Fahrenheit (°F) - **Currency** - Dollars (\$) and pounds (£) - **Volume** - Litres and gallons - **Prices** - A taxi driver charging per kilometre driv»
- Upstream: T-C32 join notes/3-sequences-functions-and-graphs/real-life-graphs/conversion-graphs.json::spcpt_Nh8WWWGQxmJGVvvf — tier S1_name_match — score 0.803 — wording EXACT — validation tier AI_VALIDATED (operator-delegated chain)
- Rationale: SME span 'Conversion Graphs' on note 'Conversion Graphs' is anchored by the corpus spec_point block spcpt_Nh8WWWGQxmJGVvvf and joined to 4MA1-3.3F via name_to_statement_join; this section chunk sits inside that span.
- Verdict: [ ] CONFIRM — this chunk belongs to this SP   [ ] REJECT — wrong chunk/SP   [ ] HOLD — needs rework

### 4MA1-4.3A — identify any lines of symmetry and the order of rotational symmetry of a given two-dimensional figure
- Note: Rotational Symmetry (`notes/4-geometry-and-trigonometry/congruence-similarity-and-geometrical-proof/symmetry.json`)
- Chunk: ordinal 1 — heading `What is the order of rotational symmetry?` — sha256_16 `4efecd225e742034` — 1297 chars
- Evidence quote (verbatim self-slice, markdown-safe): "What is the order of rotational symmetry?
- **Rotational** **symmetry** refers to the number of times a shape looks the same as it is **rotated** **360°** about its **centre**
- This number is called the **order** of **rotational** **symmet"
- Chunk excerpt: «What is the order of rotational symmetry? - **Rotational** **symmetry** refers to the number of times a shape looks the same as it is **rotated** **360°** about its **centre** - This number is called the **order** of **rotational** **symmetry** - Tracing paper can help work out the order of rotational symmetry - Draw an arrow on the tracing paper so you can easily tell when you have turned it through 360° finding the»
- Upstream: T-C32 join notes/4-geometry-and-trigonometry/congruence-similarity-and-geometrical-proof/symmetry.json::spcpt_7gdmq8MbcShywrkB — tier S1_name_match — score 0.7267 — wording EXACT — validation tier AI_VALIDATED (operator-delegated chain)
- Rationale: SME span 'Rotational Symmetry' on note 'Rotational Symmetry' is anchored by the corpus spec_point block spcpt_7gdmq8MbcShywrkB and joined to 4MA1-4.3A via name_to_statement_join; this section chunk sits inside that span.
- Verdict: [ ] CONFIRM — this chunk belongs to this SP   [ ] REJECT — wrong chunk/SP   [ ] HOLD — needs rework

### 4MA1-4.11A — understand that areas of similar figures are in the ratio of the square of corresponding sides
- Note: Similar Lengths (`notes/4-geometry-and-trigonometry/congruence-similarity-and-geometrical-proof/similar-lengths.json`)
- Chunk: ordinal 3 — heading `Method 1` — sha256_16 `caa6917d2fdae4ca` — 593 chars
- Evidence quote (verbatim self-slice, markdown-safe): "Method 1
- **STEP 1**
Find the **scale factor **to get from the **first **shape to the **second **shape

  - **Divide **a length on the **second **by the corresponding length on the **first**
  - The scale factor **can be less than 1** for "
- Chunk excerpt: «Method 1 - **STEP 1** Find the **scale factor **to get from the **first **shape to the **second **shape - **Divide **a length on the **second **by the corresponding length on the **first** - The scale factor **can be less than 1** for this method - **STEP 2** Use the scale factor to find the **length **you need - To find a missing length on the **second shape** - **Multiply **the corresponding length on the first sha»
- Upstream: T-C32 join notes/4-geometry-and-trigonometry/congruence-similarity-and-geometrical-proof/similar-lengths.json::spcpt_xDpKVBxDTCk2x6vS — tier S1_name_match — score 0.6714 — wording EXACT — validation tier AI_VALIDATED (operator-delegated chain)
- Rationale: SME span 'Similar Lengths' on note 'Similar Lengths' is anchored by the corpus spec_point block spcpt_xDpKVBxDTCk2x6vS and joined to 4MA1-4.11A via name_to_statement_join; this section chunk sits inside that span.
- Verdict: [ ] CONFIRM — this chunk belongs to this SP   [ ] REJECT — wrong chunk/SP   [ ] HOLD — needs rework

### 4MA1-1.7D — calculate an unknown quantity from quantities that vary in direct proportion
- Note: Direct Proportion (`notes/1-numbers-and-the-number-system/direct-and-inverse-proportion/direct-proportion.json`)
- Chunk: ordinal 0 — heading `Direct proportion` — sha256_16 `f0767da728996c40` — 17 chars
- Evidence quote (verbatim self-slice, markdown-safe): "Direct proportion"
- Chunk excerpt: «Direct proportion»
- Upstream: T-C32 join notes/1-numbers-and-the-number-system/direct-and-inverse-proportion/direct-proportion.json::spcpt_BktcXhHcVFw8R9Q2 — tier S1_name_match — score 0.7462 — wording EXACT — validation tier AI_VALIDATED (operator-delegated chain)
- Rationale: SME span 'Direct Proportion' on note 'Direct Proportion' is anchored by the corpus spec_point block spcpt_BktcXhHcVFw8R9Q2 and joined to 4MA1-1.7D via name_to_statement_join; this section chunk sits inside that span.
- Verdict: [ ] CONFIRM — this chunk belongs to this SP   [ ] REJECT — wrong chunk/SP   [ ] HOLD — needs rework

### 4MA1-6.2B — understand the concept of a measure of spread
- Note: Mean, Median & Mode (`notes/6-statistics-and-probability/statistics-toolkit/mean-median-and-mode.json`)
- Chunk: ordinal 4 — heading `How do I know when to use the mode, median or mean?` — sha256_16 `423d1f64367036a1` — 2941 chars
- Evidence quote (verbatim self-slice, markdown-safe): "How do I know when to use the mode, median or mean?
- The mode, median and mean are different ways to measure an **average**
- In certain situations it is **better** to use one average over another
- For example:

  - If the data has **extr"
- Chunk excerpt: «How do I know when to use the mode, median or mean? - The mode, median and mean are different ways to measure an **average** - In certain situations it is **better** to use one average over another - For example: - If the data has **extreme values** (outliers) like 1, 1, 4, 50 The mode is 1 The median is 2.5 The mean is 14 - **Don't use the mean** (it's badly affected by extreme values) - If the data has **more** tha»
- Upstream: T-C32 join notes/6-statistics-and-probability/statistics-toolkit/mean-median-and-mode.json::spcpt_myNYhxstM7xnZd9P — tier S1_name_match — score 0.76 — wording EXACT — validation tier AI_VALIDATED (operator-delegated chain)
- Rationale: SME span 'Mean, Median & Mode' on note 'Mean, Median & Mode' is anchored by the corpus spec_point block spcpt_myNYhxstM7xnZd9P and joined to 4MA1-6.2B via name_to_statement_join; this section chunk sits inside that span.
- Verdict: [ ] CONFIRM — this chunk belongs to this SP   [ ] REJECT — wrong chunk/SP   [ ] HOLD — needs rework

### 4MA1-4.1B — use angle properties of intersecting lines, parallel lines and angles on a straight line
- Note: Angles in Parallel Lines (`notes/4-geometry-and-trigonometry/angles-in-polygons-and-parallel-lines/angles-in-parallel-lines.json`)
- Chunk: ordinal 4 — heading `What are allied angles in parallel lines?` — sha256_16 `107b9d513fa911a4` — 236 chars
- Evidence quote (verbatim self-slice, markdown-safe): "What are allied angles in parallel lines?
- Find **allied angles** by looking for a **C-shape**
- **Allied **angles** add **up to** 180°**
- You may also see allied angles referred to as co-interior or supplementary angles
Allied angles"
- Chunk excerpt: «What are allied angles in parallel lines? - Find **allied angles** by looking for a **C-shape** - **Allied **angles** add **up to** 180°** - You may also see allied angles referred to as co-interior or supplementary angles Allied angles»
- Upstream: T-C32 join notes/4-geometry-and-trigonometry/angles-in-polygons-and-parallel-lines/angles-in-parallel-lines.json::spcpt_2SfTVFKHJRBby3QK — tier S1_name_match — score 0.773 — wording EXACT — validation tier AI_VALIDATED (operator-delegated chain)
- Rationale: SME span 'Angles in Parallel Lines' on note 'Angles in Parallel Lines' is anchored by the corpus spec_point block spcpt_2SfTVFKHJRBby3QK and joined to 4MA1-4.1B via name_to_statement_join; this section chunk sits inside that span.
- Verdict: [ ] CONFIRM — this chunk belongs to this SP   [ ] REJECT — wrong chunk/SP   [ ] HOLD — needs rework

### 4MA1-5.2A — understand that rotations are specified by a centre and an angle
- Note: Rotations (`notes/5-vectors-and-transformation-geometry/transformations/rotations.json`)
- Chunk: ordinal 2 — heading `How do I rotate a shape?` — sha256_16 `210eb60eeddf62be` — 2026 chars
- Evidence quote (verbatim self-slice, markdown-safe): "How do I rotate a shape?
- **STEP 1** Place the **tracing paper** over page and draw over the original object
- **STEP 2** Place the point of your pencil on the **centre of rotation**
- **STEP 3** **Rotate** the tracing paper by the **given"
- Chunk excerpt: «How do I rotate a shape? - **STEP 1** Place the **tracing paper** over page and draw over the original object - **STEP 2** Place the point of your pencil on the **centre of rotation** - **STEP 3** **Rotate** the tracing paper by the **given angle** in the **given direction** - The angle will be **90°**, **180°** or **270°** - **STEP 4** **Carefully draw** the image onto the coordinate grid in the **position shown by »
- Upstream: T-C32 join notes/5-vectors-and-transformation-geometry/transformations/rotations.json::spcpt_N5xf2wmr4yCNxHBj — tier S1_name_match — score 0.6986 — wording EXACT — validation tier AI_VALIDATED (operator-delegated chain)
- Rationale: SME span 'Rotations' on note 'Rotations' is anchored by the corpus spec_point block spcpt_N5xf2wmr4yCNxHBj and joined to 4MA1-5.2A via name_to_statement_join; this section chunk sits inside that span.
- Verdict: [ ] CONFIRM — this chunk belongs to this SP   [ ] REJECT — wrong chunk/SP   [ ] HOLD — needs rework

### 4MA1-4.1B — use angle properties of intersecting lines, parallel lines and angles on a straight line
- Note: Parallel Lines (`notes/3-sequences-functions-and-graphs/linear-graphs-y-equals-mx-plus-c/parallel-lines.json`)
- Chunk: ordinal 2 — heading `How do I find the equation of a parallel line?` — sha256_16 `6abd0dc2b9f713df` — 978 chars
- Evidence quote (verbatim self-slice, markdown-safe): "How do I find the equation of a parallel line?
- For example, to find the** equation** of the line **parallel** to *y * = 2*x * + 1 which **passes through** the **point **(3, 14)

  - write the parallel line as *y*  = 2*x*  + *d*
  
    - u"
- Chunk excerpt: «How do I find the equation of a parallel line? - For example, to find the** equation** of the line **parallel** to *y * = 2*x * + 1 which **passes through** the **point **(3, 14) - write the parallel line as *y* = 2*x* + *d* - using the same gradient of 2 - **substitute** *x* = 3 and *y* = 14 into this** **equation - 14 = 2 × 3 + *d* - 14 = 6 + *d* - **solve** to **find *****d*** - *d * = 8 - The equation is *y * = 2»
- Upstream: T-C32 join notes/3-sequences-functions-and-graphs/linear-graphs-y-equals-mx-plus-c/parallel-lines.json::spcpt_qPRh2fycSMYwytcV — tier S1_name_match — score 0.7109 — wording EXACT — validation tier AI_VALIDATED (operator-delegated chain)
- Rationale: SME span 'Parallel Lines' on note 'Parallel Lines' is anchored by the corpus spec_point block spcpt_qPRh2fycSMYwytcV and joined to 4MA1-4.1B via name_to_statement_join; this section chunk sits inside that span.
- Verdict: [ ] CONFIRM — this chunk belongs to this SP   [ ] REJECT — wrong chunk/SP   [ ] HOLD — needs rework

### 4MA1-4.11A — understand that areas of similar figures are in the ratio of the square of corresponding sides
- Note: Similar Lengths (`notes/4-geometry-and-trigonometry/congruence-similarity-and-geometrical-proof/similar-lengths.json`)
- Chunk: ordinal 1 — heading `How do I find the scale factor between lengths on similar shapes?` — sha256_16 `c420b3449338ac01` — 622 chars
- Evidence quote (verbatim self-slice, markdown-safe): "How do I find the scale factor between lengths on similar shapes?
- Equivalent** lengths** on two similar shapes will be in the same ratio and are linked by a **scale factor**
- Establish the **type** of enlargement

  - If the second shape"
- Chunk excerpt: «How do I find the scale factor between lengths on similar shapes? - Equivalent** lengths** on two similar shapes will be in the same ratio and are linked by a **scale factor** - Establish the **type** of enlargement - If the second shape is **bigger** - then the **scale factor** is** greater than 1** - If the second shape is **smaller** - then the **scale factor **is** greater than 0 **but** less than 1** - To find t»
- Upstream: T-C32 join notes/4-geometry-and-trigonometry/congruence-similarity-and-geometrical-proof/similar-lengths.json::spcpt_xDpKVBxDTCk2x6vS — tier S1_name_match — score 0.6714 — wording EXACT — validation tier AI_VALIDATED (operator-delegated chain)
- Rationale: SME span 'Similar Lengths' on note 'Similar Lengths' is anchored by the corpus spec_point block spcpt_xDpKVBxDTCk2x6vS and joined to 4MA1-4.11A via name_to_statement_join; this section chunk sits inside that span.
- Verdict: [ ] CONFIRM — this chunk belongs to this SP   [ ] REJECT — wrong chunk/SP   [ ] HOLD — needs rework

### 4MA1-1.7B — divide a quantity in a given ratio or ratios
- Note: Introduction to Ratios (`notes/1-numbers-and-the-number-system/ratio-toolkit/simple-ratio.json`)
- Chunk: ordinal 1 — heading `What is a ratio?` — sha256_16 `a33651ae20fbad50` — 168 chars
- Evidence quote (verbatim self-slice, markdown-safe): "What is a ratio?
- A **ratio** is a way of comparing one **part** of a **whole** to another

  - **Ratios** are used to compare **one** **part** to **another** **part**"
- Chunk excerpt: «What is a ratio? - A **ratio** is a way of comparing one **part** of a **whole** to another - **Ratios** are used to compare **one** **part** to **another** **part**»
- Upstream: T-C32 join notes/1-numbers-and-the-number-system/ratio-toolkit/simple-ratio.json::spcpt_qpSmD6yNY5t5GrW6 — tier S1_name_match — score 0.696 — wording EXACT — validation tier AI_VALIDATED (operator-delegated chain)
- Rationale: SME span 'Ratios' on note 'Introduction to Ratios' is anchored by the corpus spec_point block spcpt_qpSmD6yNY5t5GrW6 and joined to 4MA1-1.7B via name_to_statement_join; this section chunk sits inside that span.
- Verdict: [ ] CONFIRM — this chunk belongs to this SP   [ ] REJECT — wrong chunk/SP   [ ] HOLD — needs rework

### 4MA1-3.3E — find the intersection points of two graphs, one linear ( y ) and one non-linear ( y ), and and recognise that the solutions correspond to the solutions of ( y − y ) = 0 2 1
- Note: Midpoint of a Line (`notes/3-sequences-functions-and-graphs/coordinate-geometry/midpoint-of-a-line.json`)
- Chunk: ordinal 1 — heading `How do I find the midpoint of a line?` — sha256_16 `9877b60c1cce1ed4` — 1477 chars
- Evidence quote (verbatim self-slice, markdown-safe): "How do I find the midpoint of a line?
- The **midpoint **of a line will be the **same distance from both endpoints**
- You can think of a midpoint as being the average (**mean**) of two coordinates
- The **midpoint **of `open parentheses x "
- Chunk excerpt: «How do I find the midpoint of a line? - The **midpoint **of a line will be the **same distance from both endpoints** - You can think of a midpoint as being the average (**mean**) of two coordinates - The **midpoint **of `open parentheses x subscript 1 comma space y subscript 1 close parentheses` and `open parentheses x subscript 2 comma space y subscript 2 close parentheses` is `open parentheses fraction numerator x »
- Upstream: T-C32 join notes/3-sequences-functions-and-graphs/coordinate-geometry/midpoint-of-a-line.json::spcpt_84hZy4pDd8nBGN3r — tier S1_name_match — score 0.719 — wording EXACT — validation tier AI_VALIDATED (operator-delegated chain)
- Rationale: SME span 'Midpoint of a Line' on note 'Midpoint of a Line' is anchored by the corpus spec_point block spcpt_84hZy4pDd8nBGN3r and joined to 4MA1-3.3E via name_to_statement_join; this section chunk sits inside that span.
- Verdict: [ ] CONFIRM — this chunk belongs to this SP   [ ] REJECT — wrong chunk/SP   [ ] HOLD — needs rework

### 4MA1-1.4E — find highest common factors (HCF) and lowest common multiples (LCM)
- Note: HCF & LCM (`notes/1-numbers-and-the-number-system/prime-factors-hcf-and-lcm/hcf-and-lcm.json`)
- Chunk: ordinal 9 — heading `How can I use the powers of prime factors to find the lowest common multiple (LCM) of two numbers?` — sha256_16 `badd1413a73deb27` — 1804 chars
- Evidence quote (verbatim self-slice, markdown-safe): "How can I use the powers of prime factors to find the lowest common multiple (LCM) of two numbers?
- Write each number as a **product of the powers of its prime factors**

  - $72=2^{3}\times3^{2}$ and $540=2^{2}\times3^{3}\times5$
- Find t"
- Chunk excerpt: «How can I use the powers of prime factors to find the lowest common multiple (LCM) of two numbers? - Write each number as a **product of the powers of its prime factors** - $72=2^{3}\times3^{2}$ and $540=2^{2}\times3^{3}\times5$ - Find the **highest power** of **each and every** prime that appears in either number (they do **not** have to be **common** primes) - 2<sup>3</sup> is the highest power of 2 shown (from 72)»
- Upstream: T-C32 join notes/1-numbers-and-the-number-system/prime-factors-hcf-and-lcm/hcf-and-lcm.json::spcpt_bmqbWbZM8HXPwsFF — tier S1_name_match — score 0.6858 — wording EXACT — validation tier AI_VALIDATED (operator-delegated chain)
- Rationale: SME span 'Lowest Common Multiple (LCM)' on note 'HCF & LCM' is anchored by the corpus spec_point block spcpt_bmqbWbZM8HXPwsFF and joined to 4MA1-1.4E via name_to_statement_join; this section chunk sits inside that span.
- Verdict: [ ] CONFIRM — this chunk belongs to this SP   [ ] REJECT — wrong chunk/SP   [ ] HOLD — needs rework

### 4MA1-1.5E — use Venn diagrams to represent sets
- Note: Venn Diagrams with Three Sets (`notes/1-numbers-and-the-number-system/set-notation-and-venn-diagrams/venn-diagrams-with-three-sets.json`)
- Chunk: ordinal 0 — heading `Venn diagrams with three sets` — sha256_16 `ceb161b911311fae` — 29 chars
- Evidence quote (verbatim self-slice, markdown-safe): "Venn diagrams with three sets"
- Chunk excerpt: «Venn diagrams with three sets»
- Upstream: T-C32 join notes/1-numbers-and-the-number-system/set-notation-and-venn-diagrams/venn-diagrams-with-three-sets.json::spcpt_vfPNw2mzksvxf2JP — tier S1_name_match — score 0.66 — wording EXACT — validation tier AI_VALIDATED (operator-delegated chain)
- Rationale: SME span 'Venn diagrams with three sets' on note 'Venn Diagrams with Three Sets' is anchored by the corpus spec_point block spcpt_vfPNw2mzksvxf2JP and joined to 4MA1-1.5E via name_to_statement_join; this section chunk sits inside that span.
- Verdict: [ ] CONFIRM — this chunk belongs to this SP   [ ] REJECT — wrong chunk/SP   [ ] HOLD — needs rework

### 4MA1-4.8E — understand and use the formula ab sin C for the area of a triangle
- Note: Area of a Triangle (`notes/4-geometry-and-trigonometry/sine-cosine-rule-and-area-of-triangles/area-of-a-triangle.json`)
- Chunk: ordinal 1 — heading `How do I find the area of a non-right-angled triangle?` — sha256_16 `a495620c3cf2093f` — 1769 chars
- Evidence quote (verbatim self-slice, markdown-safe): "How do I find the area of a non-right-angled triangle?
- The area of **any triangle** can be found using the formula
$\mathrm{Area}=\frac{1}{2}ab\mathrm{sin}C$
- *C *is the angle **between **sides $a$* *and $b$
Non Right-Angled Triangle lab"
- Chunk excerpt: «How do I find the area of a non-right-angled triangle? - The area of **any triangle** can be found using the formula $\mathrm{Area}=\frac{1}{2}ab\mathrm{sin}C$ - *C *is the angle **between **sides $a$* *and $b$ Non Right-Angled Triangle labelled with angles A, B and C and opposite corresponding sides a, b and c. - Label your triangle correctly - Make sure that *C* is always the angle **between** the two sides - If an»
- Upstream: T-C32 join notes/4-geometry-and-trigonometry/sine-cosine-rule-and-area-of-triangles/area-of-a-triangle.json::spcpt_djG6mt4Gk3T4wJwC — tier S1_name_match — score 0.7714 — wording EXACT — validation tier AI_VALIDATED (operator-delegated chain)
- Rationale: SME span 'Area of a Triangle' on note 'Area of a Triangle' is anchored by the corpus spec_point block spcpt_djG6mt4Gk3T4wJwC and joined to 4MA1-4.8E via name_to_statement_join; this section chunk sits inside that span.
- Verdict: [ ] CONFIRM — this chunk belongs to this SP   [ ] REJECT — wrong chunk/SP   [ ] HOLD — needs rework

### 4MA1-5.2A — understand that rotations are specified by a centre and an angle
- Note: Rotations (`notes/5-vectors-and-transformation-geometry/transformations/rotations.json`)
- Chunk: ordinal 4 — heading `How do I reverse a rotation?` — sha256_16 `d8a55fc6735815fd` — 1712 chars
- Evidence quote (verbatim self-slice, markdown-safe): "How do I reverse a rotation?
- If a shape has been **rotated** to a new position, you can perform a single transformation to **return the shape** to its **original position**
- A rotation can be **reversed** by simply **reversing the direct"
- Chunk excerpt: «How do I reverse a rotation? - If a shape has been **rotated** to a new position, you can perform a single transformation to **return the shape** to its **original position** - A rotation can be **reversed** by simply **reversing the direction** of rotation - The angle of rotation is the same - The centre of rotation is the same - For a shape rotated by 45º in a clockwise direction about the point (0, 3) - The **reve»
- Upstream: T-C32 join notes/5-vectors-and-transformation-geometry/transformations/rotations.json::spcpt_N5xf2wmr4yCNxHBj — tier S1_name_match — score 0.6986 — wording EXACT — validation tier AI_VALIDATED (operator-delegated chain)
- Rationale: SME span 'Rotations' on note 'Rotations' is anchored by the corpus spec_point block spcpt_N5xf2wmr4yCNxHBj and joined to 4MA1-5.2A via name_to_statement_join; this section chunk sits inside that span.
- Verdict: [ ] CONFIRM — this chunk belongs to this SP   [ ] REJECT — wrong chunk/SP   [ ] HOLD — needs rework

### 4MA1-4.2D — understand the term ‘regular polygon’ and calculate interior and exterior angles of regular polygons
- Note: Angles in Polygons (`notes/4-geometry-and-trigonometry/angles-in-polygons-and-parallel-lines/angles-in-polygons.json`)
- Chunk: ordinal 7 — heading `How do I find the number of sides in a regular polygon?` — sha256_16 `7ce557f673ab2806` — 1094 chars
- Evidence quote (verbatim self-slice, markdown-safe): "How do I find the number of sides in a regular polygon?
- If you are given the interior angle of a regular polygon

  - set the angle equal to `fraction numerator 180 open parentheses n minus 2 close parentheses over denominator n end fract"
- Chunk excerpt: «How do I find the number of sides in a regular polygon? - If you are given the interior angle of a regular polygon - set the angle equal to `fraction numerator 180 open parentheses n minus 2 close parentheses over denominator n end fraction` - then solve the equation to find $n$ Exam Hint: Make sure you identify whether you are dealing with a **regular **or **irregular **polygon before you start a question. Finding t»
- Upstream: T-C32 join notes/4-geometry-and-trigonometry/angles-in-polygons-and-parallel-lines/angles-in-polygons.json::spcpt_gzykj64JBx2RtBJ7 — tier S2_name_ambiguous — score 0.7085 — wording EXACT — validation tier AI_VALIDATED (operator-delegated chain)
- Rationale: SME span 'Angles in Polygons' on note 'Angles in Polygons' is anchored by the corpus spec_point block spcpt_gzykj64JBx2RtBJ7 and joined to 4MA1-4.2D via name_to_statement_join; this section chunk sits inside that span.
- Verdict: [ ] CONFIRM — this chunk belongs to this SP   [ ] REJECT — wrong chunk/SP   [ ] HOLD — needs rework

### 4MA1-2.7B — solve quadratic equations by using the quadratic formula or completing the square
- Note: The Quadratic Formula (`notes/2-equations-formulae-and-identities/solving-quadratic-equations/quadratic-formula.json`)
- Chunk: ordinal 3 — heading `How do I write the solutions in an exact (surd) form?` — sha256_16 `57946f4d397caab2` — 1132 chars
- Evidence quote (verbatim self-slice, markdown-safe): "How do I write the solutions in an exact (surd) form?
- You may be asked to give answers in an **exact** (**surd**) form
- In the example above, work out the **number **under the **square root **sign

  - Be careful with negatives!
  
    -"
- Chunk excerpt: «How do I write the solutions in an exact (surd) form? - You may be asked to give answers in an **exact** (**surd**) form - In the example above, work out the **number **under the **square root **sign - Be careful with negatives! - `open parentheses negative 8 close parentheses squared minus 4 cross times 2 cross times open parentheses negative 3 close parentheses equals 64 plus 24 equals 88` - Now square root this nu»
- Upstream: T-C32 join notes/2-equations-formulae-and-identities/solving-quadratic-equations/quadratic-formula.json::spcpt_JRX7QS29KrY2hCCW — tier S1_name_match — score 0.7388 — wording EXACT — validation tier AI_VALIDATED (operator-delegated chain)
- Rationale: SME span 'Quadratic Formula' on note 'The Quadratic Formula' is anchored by the corpus spec_point block spcpt_JRX7QS29KrY2hCCW and joined to 4MA1-2.7B via name_to_statement_join; this section chunk sits inside that span.
- Verdict: [ ] CONFIRM — this chunk belongs to this SP   [ ] REJECT — wrong chunk/SP   [ ] HOLD — needs rework

### 4MA1-3.4C — determine gradients, rates of change, stationary points, turning points (maxima and minima) by differentiation and relate these to graphs
- Note: Differentiation (`notes/3-sequences-functions-and-graphs/differentiation/differentiation.json`)
- Chunk: ordinal 5 — heading `How do I find the gradient of a curve using the gradient function?` — sha256_16 `9ebc3d202e8b73d5` — 897 chars
- Evidence quote (verbatim self-slice, markdown-safe): "How do I find the gradient of a curve using the gradient function?
- Find the ***x*****-coordinate** of the point on the curve you're interested in
- Use **differentiation** to turn the equation of the curve, $y=...$, into the gradient func"
- Chunk excerpt: «How do I find the gradient of a curve using the gradient function? - Find the ***x*****-coordinate** of the point on the curve you're interested in - Use **differentiation** to turn the equation of the curve, $y=...$, into the gradient function, $\frac{dy}{dx}=...$ - **Substitute** the *x*-coordinate into the gradient function to find the gradient - The *y*-coordinate is not needed Image showing how the gradient of t»
- Upstream: T-C32 join notes/3-sequences-functions-and-graphs/differentiation/differentiation.json::spcpt_fGGbSYFZH9DW4sgm — tier S1_name_match — score 0.6805 — wording EXACT — validation tier AI_VALIDATED (operator-delegated chain)
- Rationale: SME span 'Differentiation' on note 'Differentiation' is anchored by the corpus spec_point block spcpt_fGGbSYFZH9DW4sgm and joined to 4MA1-3.4C via name_to_statement_join; this section chunk sits inside that span.
- Verdict: [ ] CONFIRM — this chunk belongs to this SP   [ ] REJECT — wrong chunk/SP   [ ] HOLD — needs rework

### 4MA1-3.4E — apply calculus to linear kinematics and to other simple practical problems
- Note: Using Differentiation for Kinematics (`notes/3-sequences-functions-and-graphs/differentiation/kinematics.json`)
- Chunk: ordinal 4 — heading `What is the velocity and how do I find it?` — sha256_16 `5fe9809afa4a63d4` — 1006 chars
- Evidence quote (verbatim self-slice, markdown-safe): "What is the velocity and how do I find it?
- **Velocity **is the **speed and direction** of an object

  - It is **positive** if moving **forwards**
  - It is** negative** if moving **backwards**
  - Do **not** confuse velocity and speed
  "
- Chunk excerpt: «What is the velocity and how do I find it? - **Velocity **is the **speed and direction** of an object - It is **positive** if moving **forwards** - It is** negative** if moving **backwards** - Do **not** confuse velocity and speed - **Speed** is **always positive! ** - To find the **velocity** of an object, $v$ metres per second, **differentiate** its **displacement **function - $v=\frac{ds}{dt}$ - For example, if $s»
- Upstream: T-C32 join notes/3-sequences-functions-and-graphs/differentiation/kinematics.json::spcpt_vYsrWKqpQDpSwnPj — tier S1_name_match — score 0.6952 — wording EXACT — validation tier AI_VALIDATED (operator-delegated chain)
- Rationale: SME span 'Kinematics' on note 'Using Differentiation for Kinematics' is anchored by the corpus spec_point block spcpt_vYsrWKqpQDpSwnPj and joined to 4MA1-3.4E via name_to_statement_join; this section chunk sits inside that span.
- Verdict: [ ] CONFIRM — this chunk belongs to this SP   [ ] REJECT — wrong chunk/SP   [ ] HOLD — needs rework

### 4MA1-3.1C — find the sum of the firstnterms of an arithmetic series(Sn)
- Note: Arithmetic Sequences (`notes/3-sequences-functions-and-graphs/sequences/arithmetic-sequences.json`)
- Chunk: ordinal 3 — heading `How do I use the formula for the nth term of an arithmetic sequence?` — sha256_16 `92399d9bc5ef8b7b` — 2679 chars
- Evidence quote (verbatim self-slice, markdown-safe): "How do I use the formula for the nth term of an arithmetic sequence?
- You can** substitute** in the values of $a$, $d$ and $n$ to find a particular term

  - e.g. $a=10$, $d=4$ and $n=3$ gives  `u subscript 3 equals 10 plus open parenthese"
- Chunk excerpt: «How do I use the formula for the nth term of an arithmetic sequence? - You can** substitute** in the values of $a$, $d$ and $n$ to find a particular term - e.g. $a=10$, $d=4$ and $n=3$ gives `u subscript 3 equals 10 plus open parentheses 3 minus 1 close parentheses cross times 4 equals 18` - So 18 is the 3<sup>rd</sup> term - You can** substitute** in the values of $a$ and $d$ to find an expression for $u_{n}$ - e.g.»
- Upstream: T-C32 join notes/3-sequences-functions-and-graphs/sequences/arithmetic-sequences.json::spcpt_fhF2H4HM3cxqsGdd — tier S1_name_match — score 0.7758 — wording EXACT — validation tier AI_VALIDATED (operator-delegated chain)
- Rationale: SME span 'Arithmetic Sequences' on note 'Arithmetic Sequences' is anchored by the corpus spec_point block spcpt_fhF2H4HM3cxqsGdd and joined to 4MA1-3.1C via name_to_statement_join; this section chunk sits inside that span.
- Verdict: [ ] CONFIRM — this chunk belongs to this SP   [ ] REJECT — wrong chunk/SP   [ ] HOLD — needs rework

### 4MA1-2.5A — set up problems involving direct or inverse proportion and relate algebraic solutions to graphical representation of the equations
- Note: Inverse Proportion (`notes/1-numbers-and-the-number-system/direct-and-inverse-proportion/inverse-proportion.json`)
- Chunk: ordinal 3 — heading `How do I find the equation between two inversely proportional variables?` — sha256_16 `03bae7f293adc46d` — 2536 chars
- Evidence quote (verbatim self-slice, markdown-safe): "How do I find the equation between two inversely proportional variables?
- Inverse proportion questions always have the same process:

  - **STEP 1**
  **Identify** the two variables and write down the **formula in terms of *****k***
  
   "
- Chunk excerpt: «How do I find the equation between two inversely proportional variables? - Inverse proportion questions always have the same process: - **STEP 1** **Identify** the two variables and write down the **formula in terms of *****k*** - E.g. ***y*** is **inversely **proportional to ***x*** - write down the formula $y=\frac{k}{x}$ - **STEP 2** **Find** ***k*** by substituting any given values **from the question** into your»
- Upstream: T-C32 join notes/1-numbers-and-the-number-system/direct-and-inverse-proportion/inverse-proportion.json::spcpt_b7HzYMMwjGWQSz77 — tier S1_name_match — score 0.6973 — wording EXACT — validation tier AI_VALIDATED (operator-delegated chain)
- Rationale: SME span 'Inverse Proportion' on note 'Inverse Proportion' is anchored by the corpus spec_point block spcpt_b7HzYMMwjGWQSz77 and joined to 4MA1-2.5A via name_to_statement_join; this section chunk sits inside that span.
- Verdict: [ ] CONFIRM — this chunk belongs to this SP   [ ] REJECT — wrong chunk/SP   [ ] HOLD — needs rework

### 4MA1-1.6G — use compound interest and depreciation
- Note: Depreciation (`notes/1-numbers-and-the-number-system/compound-interest-and-depreciation/depreciation.json`)
- Chunk: ordinal 3 — heading `Depreciation formula` — sha256_16 `7f36b45de5d992f1` — 1216 chars
- Evidence quote (verbatim self-slice, markdown-safe): "Depreciation formula
- An **alternate method** is to use the **following formula** to calculate the final balance

  - Final balance = `P open parentheses 1 minus r over 100 close parentheses to the power of n space end exponent` where
  
 "
- Chunk excerpt: «Depreciation formula - An **alternate method** is to use the **following formula** to calculate the final balance - Final balance = `P open parentheses 1 minus r over 100 close parentheses to the power of n space end exponent` where - *P* is the original amount, - *r* is the % increase - and *n* is the number of years - Note that all of $1-\frac{r}{100}$ is the **multiplier** - e.g. 0.75 for a 25% depreciation - This»
- Upstream: T-C32 join notes/1-numbers-and-the-number-system/compound-interest-and-depreciation/depreciation.json::spcpt_rDHZfZ8PrdwXcT2y — tier S1_name_match — score 0.792 — wording EXACT — validation tier AI_VALIDATED (operator-delegated chain)
- Rationale: SME span 'Depreciation' on note 'Depreciation' is anchored by the corpus spec_point block spcpt_rDHZfZ8PrdwXcT2y and joined to 4MA1-1.6G via name_to_statement_join; this section chunk sits inside that span.
- Verdict: [ ] CONFIRM — this chunk belongs to this SP   [ ] REJECT — wrong chunk/SP   [ ] HOLD — needs rework

### 4MA1-5.2H — understand and use column vectors in translations
- Note: Translations (`notes/5-vectors-and-transformation-geometry/transformations/translations.json`)
- Chunk: ordinal 0 — heading `Translations` — sha256_16 `266a41b90d4f831e` — 12 chars
- Evidence quote (verbatim self-slice, markdown-safe): "Translations"
- Chunk excerpt: «Translations»
- Upstream: T-C32 join notes/5-vectors-and-transformation-geometry/transformations/translations.json::spcpt_YQX35KWR6v8thX5T — tier S1_name_match — score 0.7574 — wording EXACT — validation tier AI_VALIDATED (operator-delegated chain)
- Rationale: SME span 'Translations' on note 'Translations' is anchored by the corpus spec_point block spcpt_YQX35KWR6v8thX5T and joined to 4MA1-5.2H via name_to_statement_join; this section chunk sits inside that span.
- Verdict: [ ] CONFIRM — this chunk belongs to this SP   [ ] REJECT — wrong chunk/SP   [ ] HOLD — needs rework

### 4MA1-4.4G — use compound measure such as speed, density and pressure
- Note: Speed, Density & Pressure (`notes/4-geometry-and-trigonometry/standard-and-compound-units/speed-density-and-pressure.json`)
- Chunk: ordinal 0 — heading `Speed, density & pressure` — sha256_16 `5f044771e00b4846` — 25 chars
- Evidence quote (verbatim self-slice, markdown-safe): "Speed, density & pressure"
- Chunk excerpt: «Speed, density & pressure»
- Upstream: T-C32 join notes/4-geometry-and-trigonometry/standard-and-compound-units/speed-density-and-pressure.json::spcpt_jJPhXSKYBg6x4d2Q — tier S1_name_match — score 0.8286 — wording EXACT — validation tier AI_VALIDATED (operator-delegated chain)
- Rationale: SME span 'Speed, Density & Pressure' on note 'Speed, Density & Pressure' is anchored by the corpus spec_point block spcpt_jJPhXSKYBg6x4d2Q and joined to 4MA1-4.4G via name_to_statement_join; this section chunk sits inside that span.
- Verdict: [ ] CONFIRM — this chunk belongs to this SP   [ ] REJECT — wrong chunk/SP   [ ] HOLD — needs rework

### 4MA1-5.2H — understand and use column vectors in translations
- Note: Translations (`notes/5-vectors-and-transformation-geometry/transformations/translations.json`)
- Chunk: ordinal 6 — heading `How do I reverse a translation?` — sha256_16 `002be1050e3d10c2` — 1074 chars
- Evidence quote (verbatim self-slice, markdown-safe): "How do I reverse a translation?
- To **return a shape to its original position** after a translation

  - the **horizontal **and **vertical** translations must **both **be **reversed**
- The** column vector** to **reverse a translation** is"
- Chunk excerpt: «How do I reverse a translation? - To **return a shape to its original position** after a translation - the **horizontal **and **vertical** translations must **both **be **reversed** - The** column vector** to **reverse a translation** is simply the same as the original vector, but with the **sign of both values changed** - E.g. For a translation described by the column vector `open parentheses table row cell negative»
- Upstream: T-C32 join notes/5-vectors-and-transformation-geometry/transformations/translations.json::spcpt_YQX35KWR6v8thX5T — tier S1_name_match — score 0.7574 — wording EXACT — validation tier AI_VALIDATED (operator-delegated chain)
- Rationale: SME span 'Translations' on note 'Translations' is anchored by the corpus spec_point block spcpt_YQX35KWR6v8thX5T and joined to 4MA1-5.2H via name_to_statement_join; this section chunk sits inside that span.
- Verdict: [ ] CONFIRM — this chunk belongs to this SP   [ ] REJECT — wrong chunk/SP   [ ] HOLD — needs rework

### 4MA1-4.3A — identify any lines of symmetry and the order of rotational symmetry of a given two-dimensional figure
- Note: Lines of Symmetry (`notes/4-geometry-and-trigonometry/congruence-similarity-and-geometrical-proof/lines-of-symmetry.json`)
- Chunk: ordinal 1 — heading `What is line symmetry?` — sha256_16 `be5fe8ff575c0f0d` — 1909 chars
- Evidence quote (verbatim self-slice, markdown-safe): "What is line symmetry?
- **Line** **symmetry** refers to shapes that can have **mirror** lines added to them

  - Each side of the line of symmetry is a **reflection** of the other side
- Lines of symmetry can be thought of as a **folding**"
- Chunk excerpt: «What is line symmetry? - **Line** **symmetry** refers to shapes that can have **mirror** lines added to them - Each side of the line of symmetry is a **reflection** of the other side - Lines of symmetry can be thought of as a **folding** line too - **Folding** a shape along a line of symmetry results in the two parts sitting **exactly** on top of each other Lines of symmetry in isosceles triangles, squares, and recta»
- Upstream: T-C32 join notes/4-geometry-and-trigonometry/congruence-similarity-and-geometrical-proof/lines-of-symmetry.json::spcpt_NyC8VYj2kktfwnZP — tier S1_name_match — score 0.7153 — wording EXACT — validation tier AI_VALIDATED (operator-delegated chain)
- Rationale: SME span 'Lines of Symmetry' on note 'Lines of Symmetry' is anchored by the corpus spec_point block spcpt_NyC8VYj2kktfwnZP and joined to 4MA1-4.3A via name_to_statement_join; this section chunk sits inside that span.
- Verdict: [ ] CONFIRM — this chunk belongs to this SP   [ ] REJECT — wrong chunk/SP   [ ] HOLD — needs rework

### 4MA1-1.7D — calculate an unknown quantity from quantities that vary in direct proportion
- Note: Direct Proportion (`notes/1-numbers-and-the-number-system/direct-and-inverse-proportion/direct-proportion.json`)
- Chunk: ordinal 1 — heading `What is direct proportion?` — sha256_16 `af3cf18864247af0` — 737 chars
- Evidence quote (verbatim self-slice, markdown-safe): "What is direct proportion?
- **Proportion** is a way of talking about how two **variables** are related to each other
- **Direct** proportion means that as one variable goes **up** the other goes up by the same **factor**

  - The** ratio**"
- Chunk excerpt: «What is direct proportion? - **Proportion** is a way of talking about how two **variables** are related to each other - **Direct** proportion means that as one variable goes **up** the other goes up by the same **factor** - The** ratio** between the two amounts will always stay the** same** - The symbol $\propto$ means "proportional to" - E.g. *y *is directly proportional to *x*, *y*$\propto$*x* - If *x *and *y* are »
- Upstream: T-C32 join notes/1-numbers-and-the-number-system/direct-and-inverse-proportion/direct-proportion.json::spcpt_BktcXhHcVFw8R9Q2 — tier S1_name_match — score 0.7462 — wording EXACT — validation tier AI_VALIDATED (operator-delegated chain)
- Rationale: SME span 'Direct Proportion' on note 'Direct Proportion' is anchored by the corpus spec_point block spcpt_BktcXhHcVFw8R9Q2 and joined to 4MA1-1.7D via name_to_statement_join; this section chunk sits inside that span.
- Verdict: [ ] CONFIRM — this chunk belongs to this SP   [ ] REJECT — wrong chunk/SP   [ ] HOLD — needs rework

### 4MA1-1.7B — divide a quantity in a given ratio or ratios
- Note: Introduction to Ratios (`notes/1-numbers-and-the-number-system/ratio-toolkit/simple-ratio.json`)
- Chunk: ordinal 0 — heading `Ratios` — sha256_16 `a9c9b62cc34f0fc1` — 6 chars
- Evidence quote (verbatim self-slice, markdown-safe): "Ratios"
- Chunk excerpt: «Ratios»
- Upstream: T-C32 join notes/1-numbers-and-the-number-system/ratio-toolkit/simple-ratio.json::spcpt_qpSmD6yNY5t5GrW6 — tier S1_name_match — score 0.696 — wording EXACT — validation tier AI_VALIDATED (operator-delegated chain)
- Rationale: SME span 'Ratios' on note 'Introduction to Ratios' is anchored by the corpus spec_point block spcpt_qpSmD6yNY5t5GrW6 and joined to 4MA1-1.7B via name_to_statement_join; this section chunk sits inside that span.
- Verdict: [ ] CONFIRM — this chunk belongs to this SP   [ ] REJECT — wrong chunk/SP   [ ] HOLD — needs rework

### 4MA1-2.7B — solve quadratic equations by using the quadratic formula or completing the square
- Note: The Quadratic Formula (`notes/2-equations-formulae-and-identities/solving-quadratic-equations/quadratic-formula.json`)
- Chunk: ordinal 2 — heading `How do I use the quadratic formula to solve a quadratic equation?` — sha256_16 `b8091350aa820045` — 1144 chars
- Evidence quote (verbatim self-slice, markdown-safe): "How do I use the quadratic formula to solve a quadratic equation?
- Read off the **values** of *a*, *b* and *c* from the equation
- **Substitute** these into the formula

  - **Write** this line of working in the exam
  - Put **brackets** a"
- Chunk excerpt: «How do I use the quadratic formula to solve a quadratic equation? - Read off the **values** of *a*, *b* and *c* from the equation - **Substitute** these into the formula - **Write** this line of working in the exam - Put **brackets** around any **negative numbers** being substituted in - To solve 2*x*<sup>2</sup> - 8*x* - 3 = 0 using the quadratic formula: - *a* = 2, *b* = -8 and *c* = -3 - `x equals fraction numerat»
- Upstream: T-C32 join notes/2-equations-formulae-and-identities/solving-quadratic-equations/quadratic-formula.json::spcpt_JRX7QS29KrY2hCCW — tier S1_name_match — score 0.7388 — wording EXACT — validation tier AI_VALIDATED (operator-delegated chain)
- Rationale: SME span 'Quadratic Formula' on note 'The Quadratic Formula' is anchored by the corpus spec_point block spcpt_JRX7QS29KrY2hCCW and joined to 4MA1-2.7B via name_to_statement_join; this section chunk sits inside that span.
- Verdict: [ ] CONFIRM — this chunk belongs to this SP   [ ] REJECT — wrong chunk/SP   [ ] HOLD — needs rework

### 4MA1-3.4C — determine gradients, rates of change, stationary points, turning points (maxima and minima) by differentiation and relate these to graphs
- Note: Differentiation (`notes/3-sequences-functions-and-graphs/differentiation/differentiation.json`)
- Chunk: ordinal 1 — heading `What is a gradient function?` — sha256_16 `445c9e47ecac211f` — 880 chars
- Evidence quote (verbatim self-slice, markdown-safe): "What is a gradient function?
- Recall that the **equation of a curve** gives the ***y*****-coordinate** of a point when you substitute in its* x*-coordinate

  - For example, $y=x^{2}+3x+5$
  
    - Substitute $x=2$ in to get $y=2^{2}+3\tim"
- Chunk excerpt: «What is a gradient function? - Recall that the **equation of a curve** gives the ***y*****-coordinate** of a point when you substitute in its* x*-coordinate - For example, $y=x^{2}+3x+5$ - Substitute $x=2$ in to get $y=2^{2}+3\times2+5=15$ - The point `open parentheses 2 comma space 15 close parentheses` lies on the curve - A **gradient function** gives the **gradient** of the curve at a point when you substitute in »
- Upstream: T-C32 join notes/3-sequences-functions-and-graphs/differentiation/differentiation.json::spcpt_fGGbSYFZH9DW4sgm — tier S1_name_match — score 0.6805 — wording EXACT — validation tier AI_VALIDATED (operator-delegated chain)
- Rationale: SME span 'Differentiation' on note 'Differentiation' is anchored by the corpus spec_point block spcpt_fGGbSYFZH9DW4sgm and joined to 4MA1-3.4C via name_to_statement_join; this section chunk sits inside that span.
- Verdict: [ ] CONFIRM — this chunk belongs to this SP   [ ] REJECT — wrong chunk/SP   [ ] HOLD — needs rework

### 4MA1-2.7D — solve simultaneous equations in two unknowns, one equation being linear and the other being quadratic
- Note: Quadratic Simultaneous Equations (`notes/2-equations-formulae-and-identities/simultaneous-equations/quadratic.json`)
- Chunk: ordinal 4 — heading `What if the quadratic has repeated roots or no roots?` — sha256_16 `69d8a72e606a361a` — 538 chars
- Evidence quote (verbatim self-slice, markdown-safe): "What if the quadratic has repeated roots or no roots?
- If the resulting quadratic after substituting has a **repeated root**,

  - then the line is a **tangent** to the curve
  
    - i.e. the curve and the line intersect in one place only"
- Chunk excerpt: «What if the quadratic has repeated roots or no roots? - If the resulting quadratic after substituting has a **repeated root**, - then the line is a **tangent** to the curve - i.e. the curve and the line intersect in one place only - There is only **one solution** for *x* and *y* - If the resulting quadratic to be solved has **no roots**, - then the line does not intersect with the curve - There are **no solutions** t»
- Upstream: T-C32 join notes/2-equations-formulae-and-identities/simultaneous-equations/quadratic.json::spcpt_pGsqq7xcztBg59Yh — tier S1_name_match — score 0.7394 — wording EXACT — validation tier AI_VALIDATED (operator-delegated chain)
- Rationale: SME span 'Quadratic Simultaneous Equations' on note 'Quadratic Simultaneous Equations' is anchored by the corpus spec_point block spcpt_pGsqq7xcztBg59Yh and joined to 4MA1-2.7D via name_to_statement_join; this section chunk sits inside that span.
- Verdict: [ ] CONFIRM — this chunk belongs to this SP   [ ] REJECT — wrong chunk/SP   [ ] HOLD — needs rework

### 4MA1-1.4E — find highest common factors (HCF) and lowest common multiples (LCM)
- Note: HCF & LCM (`notes/1-numbers-and-the-number-system/prime-factors-hcf-and-lcm/hcf-and-lcm.json`)
- Chunk: ordinal 3 — heading `How can I use a Venn diagram to find the highest common factor (HCF) of two numbers?` — sha256_16 `2a61a96ccb12833f` — 994 chars
- Evidence quote (verbatim self-slice, markdown-safe): "How can I use a Venn diagram to find the highest common factor (HCF) of two numbers?
- Write each number as a **product of its prime factors**

  - 42 = 2×3×7 and 90 = 2×3×3×5
- Find the prime factors that are **common** to **both numbers**"
- Chunk excerpt: «How can I use a Venn diagram to find the highest common factor (HCF) of two numbers? - Write each number as a **product of its prime factors** - 42 = 2×3×7 and 90 = 2×3×3×5 - Find the prime factors that are **common** to **both numbers** and put these in the **centre of the Venn diagram** - 42 and 90 both have a prime factor of 2 - Put 2 in the centre of the diagram - Although 3 appears twice in the prime factors of »
- Upstream: T-C32 join notes/1-numbers-and-the-number-system/prime-factors-hcf-and-lcm/hcf-and-lcm.json::spcpt_P88yS9wysymQ2brq — tier S1_name_match — score 0.6798 — wording EXACT — validation tier AI_VALIDATED (operator-delegated chain)
- Rationale: SME span 'Highest Common Factor (HCF)' on note 'HCF & LCM' is anchored by the corpus spec_point block spcpt_P88yS9wysymQ2brq and joined to 4MA1-1.4E via name_to_statement_join; this section chunk sits inside that span.
- Verdict: [ ] CONFIRM — this chunk belongs to this SP   [ ] REJECT — wrong chunk/SP   [ ] HOLD — needs rework

### 4MA1-2.7D — solve simultaneous equations in two unknowns, one equation being linear and the other being quadratic
- Note: Linear Simultaneous Equations (`notes/2-equations-formulae-and-identities/simultaneous-equations/linear.json`)
- Chunk: ordinal 3 — heading `How do I solve linear simultaneous equations by substitution?` — sha256_16 `33bdc506a8a927fb` — 728 chars
- Evidence quote (verbatim self-slice, markdown-safe): "How do I solve linear simultaneous equations by substitution?
- **Substitution **means substituting one equation into the other

  - This is an **alternative** method to **elimination**
  
    - You can still use elimination if you prefer
-"
- Chunk excerpt: «How do I solve linear simultaneous equations by substitution? - **Substitution **means substituting one equation into the other - This is an **alternative** method to **elimination** - You can still use elimination if you prefer - To solve 3*x* + 2*y *= 11 and 2*x* - *y* = 5 by substitution - **Rearrange** one of the equations into ***y***** =** ... (or *x *= ...) - For example, the second equation becomes *y* = 2*x*»
- Upstream: T-C32 join notes/2-equations-formulae-and-identities/simultaneous-equations/linear.json::spcpt_h5yjgd2WdgmJqHJM — tier S1_name_match — score 0.755 — wording EXACT — validation tier AI_VALIDATED (operator-delegated chain)
- Rationale: SME span 'Linear Simultaneous Equations' on note 'Linear Simultaneous Equations' is anchored by the corpus spec_point block spcpt_h5yjgd2WdgmJqHJM and joined to 4MA1-2.7D via name_to_statement_join; this section chunk sits inside that span.
- Verdict: [ ] CONFIRM — this chunk belongs to this SP   [ ] REJECT — wrong chunk/SP   [ ] HOLD — needs rework

### 4MA1-4.2D — understand the term ‘regular polygon’ and calculate interior and exterior angles of regular polygons
- Note: Angles in Polygons (`notes/4-geometry-and-trigonometry/angles-in-polygons-and-parallel-lines/angles-in-polygons.json`)
- Chunk: ordinal 2 — heading `What are the interior angles and the exterior angles of a polygon?` — sha256_16 `c7cdbb474ed2095c` — 495 chars
- Evidence quote (verbatim self-slice, markdown-safe): "What are the interior angles and the exterior angles of a polygon?
- **Interior angles** are the angles **inside** a polygon at the corners
- The **exterior angle** at a corner is the angle needed to **make a straight line with the interior"
- Chunk excerpt: «What are the interior angles and the exterior angles of a polygon? - **Interior angles** are the angles **inside** a polygon at the corners - The **exterior angle** at a corner is the angle needed to **make a straight line with the interior angles** - It is **not** the angle that forms a **full turn** at the corner Interior and exterior angles in a hexagon - The **interior **angle and **exterior **angle **add up to 1»
- Upstream: T-C32 join notes/4-geometry-and-trigonometry/angles-in-polygons-and-parallel-lines/angles-in-polygons.json::spcpt_gzykj64JBx2RtBJ7 — tier S2_name_ambiguous — score 0.7085 — wording EXACT — validation tier AI_VALIDATED (operator-delegated chain)
- Rationale: SME span 'Angles in Polygons' on note 'Angles in Polygons' is anchored by the corpus spec_point block spcpt_gzykj64JBx2RtBJ7 and joined to 4MA1-4.2D via name_to_statement_join; this section chunk sits inside that span.
- Verdict: [ ] CONFIRM — this chunk belongs to this SP   [ ] REJECT — wrong chunk/SP   [ ] HOLD — needs rework

### 4MA1-4.1B — use angle properties of intersecting lines, parallel lines and angles on a straight line
- Note: Angles in Parallel Lines (`notes/4-geometry-and-trigonometry/angles-in-polygons-and-parallel-lines/angles-in-parallel-lines.json`)
- Chunk: ordinal 5 — heading `How do I find missing angles in parallel lines?` — sha256_16 `06e5bd24ad790b66` — 1275 chars
- Evidence quote (verbatim self-slice, markdown-safe): "How do I find missing angles in parallel lines?
- Look for shapes that look like **F**, **Z**, or **C**
- **Vertically opposite angles** can also be used in problems involving parallel lines

  - The below diagram shows how identifying angl"
- Chunk excerpt: «How do I find missing angles in parallel lines? - Look for shapes that look like **F**, **Z**, or **C** - **Vertically opposite angles** can also be used in problems involving parallel lines - The below diagram shows how identifying angle x, can lead to knowing information about several other angles - The green angle opposite is also x, as it is vertically opposite - The orange angle must be 180-x as angles on a stra»
- Upstream: T-C32 join notes/4-geometry-and-trigonometry/angles-in-polygons-and-parallel-lines/angles-in-parallel-lines.json::spcpt_2SfTVFKHJRBby3QK — tier S1_name_match — score 0.773 — wording EXACT — validation tier AI_VALIDATED (operator-delegated chain)
- Rationale: SME span 'Angles in Parallel Lines' on note 'Angles in Parallel Lines' is anchored by the corpus spec_point block spcpt_2SfTVFKHJRBby3QK and joined to 4MA1-4.1B via name_to_statement_join; this section chunk sits inside that span.
- Verdict: [ ] CONFIRM — this chunk belongs to this SP   [ ] REJECT — wrong chunk/SP   [ ] HOLD — needs rework

### 4MA1-1.4E — find highest common factors (HCF) and lowest common multiples (LCM)
- Note: HCF & LCM (`notes/1-numbers-and-the-number-system/prime-factors-hcf-and-lcm/hcf-and-lcm.json`)
- Chunk: ordinal 1 — heading `What is the highest common factor (HCF) of two numbers?` — sha256_16 `31f117cc775344ec` — 602 chars
- Evidence quote (verbatim self-slice, markdown-safe): "What is the highest common factor (HCF) of two numbers?
- A **common factor** of two numbers is a value that **both numbers **can be divided by, leaving no remainder

  - **1 **is always a common factor of any two numbers
  - Any** factor**"
- Chunk excerpt: «What is the highest common factor (HCF) of two numbers? - A **common factor** of two numbers is a value that **both numbers **can be divided by, leaving no remainder - **1 **is always a common factor of any two numbers - Any** factor** of a **common factor** will also be a common factor of the original two numbers - 6 is a common factor of 24 and 30 - Therefore 1, 2 and 3 are also common factors of 24 and 30 - The **»
- Upstream: T-C32 join notes/1-numbers-and-the-number-system/prime-factors-hcf-and-lcm/hcf-and-lcm.json::spcpt_P88yS9wysymQ2brq — tier S1_name_match — score 0.6798 — wording EXACT — validation tier AI_VALIDATED (operator-delegated chain)
- Rationale: SME span 'Highest Common Factor (HCF)' on note 'HCF & LCM' is anchored by the corpus spec_point block spcpt_P88yS9wysymQ2brq and joined to 4MA1-1.4E via name_to_statement_join; this section chunk sits inside that span.
- Verdict: [ ] CONFIRM — this chunk belongs to this SP   [ ] REJECT — wrong chunk/SP   [ ] HOLD — needs rework

### 4MA1-4.4B — calculate time intervals in terms of the 24-hour and the 12-hour clock
- Note: Time (`notes/4-geometry-and-trigonometry/standard-and-compound-units/time.json`)
- Chunk: ordinal 7 — heading `How do I convert time between time zones?` — sha256_16 `f1e37113a1e9de06` — 1365 chars
- Evidence quote (verbatim self-slice, markdown-safe): "How do I convert time between time zones?
- Different countries are in different **time zones**, depending on where they are on the planet
- For example when it is 11:36 in London in the UK, it may be 06:36 in New York in the USA

  - So Ne"
- Chunk excerpt: «How do I convert time between time zones? - Different countries are in different **time zones**, depending on where they are on the planet - For example when it is 11:36 in London in the UK, it may be 06:36 in New York in the USA - So New York is 5 hours **behind** London - London is 5 hours **ahead** of New York - You must consider: - What is the **time difference** between the two locations (**in hours**)? - Which »
- Upstream: T-C32 join notes/4-geometry-and-trigonometry/standard-and-compound-units/time.json::spcpt_h2p7nv6zkR4xFJ3P — tier S2_name_ambiguous — score 0.6432 — wording EXACT — validation tier AI_VALIDATED (operator-delegated chain)
- Rationale: SME span 'Time' on note 'Time' is anchored by the corpus spec_point block spcpt_h2p7nv6zkR4xFJ3P and joined to 4MA1-4.4B via name_to_statement_join; this section chunk sits inside that span.
- Verdict: [ ] CONFIRM — this chunk belongs to this SP   [ ] REJECT — wrong chunk/SP   [ ] HOLD — needs rework

### 4MA1-4.4G — use compound measure such as speed, density and pressure
- Note: Speed, Density & Pressure (`notes/4-geometry-and-trigonometry/standard-and-compound-units/speed-density-and-pressure.json`)
- Chunk: ordinal 2 — heading `What should I know about speed, distance and time?` — sha256_16 `dcc507f1906d399d` — 469 chars
- Evidence quote (verbatim self-slice, markdown-safe): "What should I know about speed, distance and time?
- **Speed **is commonly measured in **metres per second** (**m/s**) or **kilometres per hour** (**km/h**)

  - The units indicate **speed** is **distance per time**
  $\mathrm{Speed}=\frac{"
- Chunk excerpt: «What should I know about speed, distance and time? - **Speed **is commonly measured in **metres per second** (**m/s**) or **kilometres per hour** (**km/h**) - The units indicate **speed** is **distance per time** $\mathrm{Speed}=\frac{\mathrm{Distance}}{\mathrm{Time}}$ - You need to learn this formula - '**Speed**' (in this formula) means '**average** **speed**' - In harder problems there are often **two journeys **o»
- Upstream: T-C32 join notes/4-geometry-and-trigonometry/standard-and-compound-units/speed-density-and-pressure.json::spcpt_jJPhXSKYBg6x4d2Q — tier S1_name_match — score 0.8286 — wording EXACT — validation tier AI_VALIDATED (operator-delegated chain)
- Rationale: SME span 'Speed, Density & Pressure' on note 'Speed, Density & Pressure' is anchored by the corpus spec_point block spcpt_jJPhXSKYBg6x4d2Q and joined to 4MA1-4.4G via name_to_statement_join; this section chunk sits inside that span.
- Verdict: [ ] CONFIRM — this chunk belongs to this SP   [ ] REJECT — wrong chunk/SP   [ ] HOLD — needs rework

### 4MA1-5.2A — understand that rotations are specified by a centre and an angle
- Note: Rotations (`notes/5-vectors-and-transformation-geometry/transformations/rotations.json`)
- Chunk: ordinal 1 — heading `What is a rotation?` — sha256_16 `c513b1bf2b807f19` — 411 chars
- Evidence quote (verbatim self-slice, markdown-safe): "What is a rotation?
- A **rotation** **turns** a shape** around a point**

  - This is called the** centre of rotation**
- The **rotated image** is the **same size** as the **original image**

  - It will have a **new position and orientati"
- Chunk excerpt: «What is a rotation? - A **rotation** **turns** a shape** around a point** - This is called the** centre of rotation** - The **rotated image** is the **same size** as the **original image** - It will have a **new position and orientation** - If the centre is a point on the original shape then that point is **not changed** by the rotation - It is called an **invariant point** Orientation of a rotation»
- Upstream: T-C32 join notes/5-vectors-and-transformation-geometry/transformations/rotations.json::spcpt_N5xf2wmr4yCNxHBj — tier S1_name_match — score 0.6986 — wording EXACT — validation tier AI_VALIDATED (operator-delegated chain)
- Rationale: SME span 'Rotations' on note 'Rotations' is anchored by the corpus spec_point block spcpt_N5xf2wmr4yCNxHBj and joined to 4MA1-5.2A via name_to_statement_join; this section chunk sits inside that span.
- Verdict: [ ] CONFIRM — this chunk belongs to this SP   [ ] REJECT — wrong chunk/SP   [ ] HOLD — needs rework

### 4MA1-5.2K — understand that enlargements preserve angles and not lengths
- Note: Enlargements (`notes/5-vectors-and-transformation-geometry/transformations/enlargements.json`)
- Chunk: ordinal 4 — heading `How do I reverse an enlargement?` — sha256_16 `84df3dea4e40caaf` — 5944 chars
- Evidence quote (verbatim self-slice, markdown-safe): "How do I reverse an enlargement?
- If a shape has been **enlarged**, you can perform a single transformation to **return the shape** to its **original size and position**
- An enlargement can be **reversed** by multiplying the enlarged shap"
- Chunk excerpt: «How do I reverse an enlargement? - If a shape has been **enlarged**, you can perform a single transformation to **return the shape** to its **original size and position** - An enlargement can be **reversed** by multiplying the enlarged shape by the **reciprocal of the original scale factor** - The centre of enlargement is the same - For a shape enlarged by a scale factor of 3 with centre of enlargement (-1, 6) - The »
- Upstream: T-C32 join notes/5-vectors-and-transformation-geometry/transformations/enlargements.json::spcpt_c3ZTz62W4HKyb4zk — tier S2_name_ambiguous — score 0.7333 — wording EXACT — validation tier AI_VALIDATED (operator-delegated chain)
- Rationale: SME span 'Enlargements' on note 'Enlargements' is anchored by the corpus spec_point block spcpt_c3ZTz62W4HKyb4zk and joined to 4MA1-5.2K via name_to_statement_join; this section chunk sits inside that span.
- Verdict: [ ] CONFIRM — this chunk belongs to this SP   [ ] REJECT — wrong chunk/SP   [ ] HOLD — needs rework

### 4MA1-4.4B — calculate time intervals in terms of the 24-hour and the 12-hour clock
- Note: Time (`notes/4-geometry-and-trigonometry/standard-and-compound-units/time.json`)
- Chunk: ordinal 6 — heading `How do I use bus and train timetables?` — sha256_16 `cf40a82bc993b133` — 992 chars
- Evidence quote (verbatim self-slice, markdown-safe): "How do I use bus and train timetables?
- Bus and train **timetables **tend to use the **24-hour **clock system

  - Each **column** represents a **different bus or train**
  - **Times** are listed as **four digits** without the colon ':'
  "
- Chunk excerpt: «How do I use bus and train timetables? - Bus and train **timetables **tend to use the **24-hour **clock system - Each **column** represents a **different bus or train** - **Times** are listed as **four digits** without the colon ':' - The time in each cell usually indicates the **departure time **(when the bus/train leaves that stop/station) - The **last location** on the list usually shows the** arrival time** A bus»
- Upstream: T-C32 join notes/4-geometry-and-trigonometry/standard-and-compound-units/time.json::spcpt_h2p7nv6zkR4xFJ3P — tier S2_name_ambiguous — score 0.6432 — wording EXACT — validation tier AI_VALIDATED (operator-delegated chain)
- Rationale: SME span 'Time' on note 'Time' is anchored by the corpus spec_point block spcpt_h2p7nv6zkR4xFJ3P and joined to 4MA1-4.4B via name_to_statement_join; this section chunk sits inside that span.
- Verdict: [ ] CONFIRM — this chunk belongs to this SP   [ ] REJECT — wrong chunk/SP   [ ] HOLD — needs rework

### 4MA1-4.3A — identify any lines of symmetry and the order of rotational symmetry of a given two-dimensional figure
- Note: Lines of Symmetry (`notes/4-geometry-and-trigonometry/congruence-similarity-and-geometrical-proof/lines-of-symmetry.json`)
- Chunk: ordinal 0 — heading `Lines of symmetry` — sha256_16 `0de7e3275d472c58` — 17 chars
- Evidence quote (verbatim self-slice, markdown-safe): "Lines of symmetry"
- Chunk excerpt: «Lines of symmetry»
- Upstream: T-C32 join notes/4-geometry-and-trigonometry/congruence-similarity-and-geometrical-proof/lines-of-symmetry.json::spcpt_NyC8VYj2kktfwnZP — tier S1_name_match — score 0.7153 — wording EXACT — validation tier AI_VALIDATED (operator-delegated chain)
- Rationale: SME span 'Lines of Symmetry' on note 'Lines of Symmetry' is anchored by the corpus spec_point block spcpt_NyC8VYj2kktfwnZP and joined to 4MA1-4.3A via name_to_statement_join; this section chunk sits inside that span.
- Verdict: [ ] CONFIRM — this chunk belongs to this SP   [ ] REJECT — wrong chunk/SP   [ ] HOLD — needs rework

### 4MA1-2.7D — solve simultaneous equations in two unknowns, one equation being linear and the other being quadratic
- Note: Linear Simultaneous Equations (`notes/2-equations-formulae-and-identities/simultaneous-equations/linear.json`)
- Chunk: ordinal 4 — heading `How do I solve linear simultaneous equations graphically?` — sha256_16 `098d2071fabcead5` — 3737 chars
- Evidence quote (verbatim self-slice, markdown-safe): "How do I solve linear simultaneous equations graphically?
- **Plot** both equations on the same set of axes

  - To do this, you can use a **table of values**
  
    - or rearrange into *y* = *mx* + *c  *if that helps
- Find where the lines"
- Chunk excerpt: «How do I solve linear simultaneous equations graphically? - **Plot** both equations on the same set of axes - To do this, you can use a **table of values** - or rearrange into *y* = *mx* + *c *if that helps - Find where the lines **intersect** (cross over) - The *x *and *y ***solutions** to the simultaneous equations are the *x *and *y ***coordinates** of the point of **intersection** - For example, to solve 2*x *- *»
- Upstream: T-C32 join notes/2-equations-formulae-and-identities/simultaneous-equations/linear.json::spcpt_h5yjgd2WdgmJqHJM — tier S1_name_match — score 0.755 — wording EXACT — validation tier AI_VALIDATED (operator-delegated chain)
- Rationale: SME span 'Linear Simultaneous Equations' on note 'Linear Simultaneous Equations' is anchored by the corpus spec_point block spcpt_h5yjgd2WdgmJqHJM and joined to 4MA1-2.7D via name_to_statement_join; this section chunk sits inside that span.
- Verdict: [ ] CONFIRM — this chunk belongs to this SP   [ ] REJECT — wrong chunk/SP   [ ] HOLD — needs rework

### 4MA1-4.11C — use areas and volumes of similar figures in solving problems
- Note: Similar Areas & Volumes (`notes/4-geometry-and-trigonometry/area-and-volume-of-similar-shapes/similar-areas-and-volumes.json`)
- Chunk: ordinal 2 — heading `What is the connection between the scale factors for lengths, areas and volumes of similar shapes?` — sha256_16 `8b4e70d5b750e126` — 1276 chars
- Evidence quote (verbatim self-slice, markdown-safe): "What is the connection between the scale factors for lengths, areas and volumes of similar shapes?
- The **length**, **area **and **volume scale factors** are powers with the same base number
- If the length **scale factor **is *k* then

  "
- Chunk excerpt: «What is the connection between the scale factors for lengths, areas and volumes of similar shapes? - The **length**, **area **and **volume scale factors** are powers with the same base number - If the length **scale factor **is *k* then - The **area scale factor **is *k*<sup>2</sup> - The **volume scale factor **is *k*<sup>3</sup> - If you know one scale factor, you can find the **scale factors** - If you have the **»
- Upstream: T-C32 join notes/4-geometry-and-trigonometry/area-and-volume-of-similar-shapes/similar-areas-and-volumes.json::spcpt_dBwfqg3wJvDp9PNs — tier S1_name_match — score 0.758 — wording EXACT — validation tier AI_VALIDATED (operator-delegated chain)
- Rationale: SME span 'Similar Areas & Volumes' on note 'Similar Areas & Volumes' is anchored by the corpus spec_point block spcpt_dBwfqg3wJvDp9PNs and joined to 4MA1-4.11C via name_to_statement_join; this section chunk sits inside that span.
- Verdict: [ ] CONFIRM — this chunk belongs to this SP   [ ] REJECT — wrong chunk/SP   [ ] HOLD — needs rework

### 4MA1-5.2K — understand that enlargements preserve angles and not lengths
- Note: Enlargements (`notes/5-vectors-and-transformation-geometry/transformations/enlargements.json`)
- Chunk: ordinal 3 — heading `How do I describe an enlargement?` — sha256_16 `7e792c4885f191f8` — 992 chars
- Evidence quote (verbatim self-slice, markdown-safe): "How do I describe an enlargement?
- To describe an **enlargement**, you must:

  - State that the transformation is an** enlargement**
  - State the **scale factor**
  
    - This may be an integer or a fraction
  - Give the coordinates of "
- Chunk excerpt: «How do I describe an enlargement? - To describe an **enlargement**, you must: - State that the transformation is an** enlargement** - State the **scale factor** - This may be an integer or a fraction - Give the coordinates of the **centre of enlargement** - To find the **scale factor**: - **Pick a side** of the **original shape** - Identify the **corresponding side** on the **enlarged image** - For a fractional enlar»
- Upstream: T-C32 join notes/5-vectors-and-transformation-geometry/transformations/enlargements.json::spcpt_c3ZTz62W4HKyb4zk — tier S2_name_ambiguous — score 0.7333 — wording EXACT — validation tier AI_VALIDATED (operator-delegated chain)
- Rationale: SME span 'Enlargements' on note 'Enlargements' is anchored by the corpus spec_point block spcpt_c3ZTz62W4HKyb4zk and joined to 4MA1-5.2K via name_to_statement_join; this section chunk sits inside that span.
- Verdict: [ ] CONFIRM — this chunk belongs to this SP   [ ] REJECT — wrong chunk/SP   [ ] HOLD — needs rework

### 4MA1-3.4E — apply calculus to linear kinematics and to other simple practical problems
- Note: Using Differentiation for Kinematics (`notes/3-sequences-functions-and-graphs/differentiation/kinematics.json`)
- Chunk: ordinal 2 — heading `What is displacement?` — sha256_16 `aba2ab9607310ce3` — 639 chars
- Evidence quote (verbatim self-slice, markdown-safe): "What is displacement?
- The **displacement **of an object is **how far away **it is from a **fixed origin**

  - It can be **positive** (**in front** of the origin)
  - or **negative **(**behind **the origin)
- Do **not** confuse displaceme"
- Chunk excerpt: «What is displacement? - The **displacement **of an object is **how far away **it is from a **fixed origin** - It can be **positive** (**in front** of the origin) - or **negative **(**behind **the origin) - Do **not** confuse displacement with distance - **Distance** is **always positive!** - Displacement can have a $\pm$ sign - Displacement is given the **letter **$s$ in kinematics - Do **not** confuse this letter fo»
- Upstream: T-C32 join notes/3-sequences-functions-and-graphs/differentiation/kinematics.json::spcpt_vYsrWKqpQDpSwnPj — tier S1_name_match — score 0.6952 — wording EXACT — validation tier AI_VALIDATED (operator-delegated chain)
- Rationale: SME span 'Kinematics' on note 'Using Differentiation for Kinematics' is anchored by the corpus spec_point block spcpt_vYsrWKqpQDpSwnPj and joined to 4MA1-3.4E via name_to_statement_join; this section chunk sits inside that span.
- Verdict: [ ] CONFIRM — this chunk belongs to this SP   [ ] REJECT — wrong chunk/SP   [ ] HOLD — needs rework

### 4MA1-4.9B — find the perimeter of shapes made from triangles and rectangles
- Note: Perimeter (`notes/4-geometry-and-trigonometry/area-and-perimeter/perimeter.json`)
- Chunk: ordinal 1 — heading `What is perimeter?` — sha256_16 `685ae4ce362cfb43` — 257 chars
- Evidence quote (verbatim self-slice, markdown-safe): "What is perimeter?
- Perimeter is the **total distance** around the **outside** of a 2D shape

  - The perimeter of a **circle** is called the **circumference**
- Perimeter is a length** **in** one dimension**

  - **Units of measure** incl"
- Chunk excerpt: «What is perimeter? - Perimeter is the **total distance** around the **outside** of a 2D shape - The perimeter of a **circle** is called the **circumference** - Perimeter is a length** **in** one dimension** - **Units of measure** include mm, cm, m etc»
- Upstream: T-C32 join notes/4-geometry-and-trigonometry/area-and-perimeter/perimeter.json::spcpt_W2yYk784rNVZBxPh — tier S1_name_match — score 0.7 — wording EXACT — validation tier AI_VALIDATED (operator-delegated chain)
- Rationale: SME span 'Perimeter' on note 'Perimeter' is anchored by the corpus spec_point block spcpt_W2yYk784rNVZBxPh and joined to 4MA1-4.9B via name_to_statement_join; this section chunk sits inside that span.
- Verdict: [ ] CONFIRM — this chunk belongs to this SP   [ ] REJECT — wrong chunk/SP   [ ] HOLD — needs rework

### 4MA1-2.7B — solve quadratic equations by using the quadratic formula or completing the square
- Note: Solving by Completing the Square (`notes/2-equations-formulae-and-identities/solving-quadratic-equations/solving-by-completing-the-square.json`)
- Chunk: ordinal 2 — heading `How do I solve by completing the square when there is a coefficient in front of the x<sup>2</sup> term?` — sha256_16 `f08cccce553891f4` — 975 chars
- Evidence quote (verbatim self-slice, markdown-safe): "How do I solve by completing the square when there is a coefficient in front of the x<sup>2</sup> term?
- If the equation is *ax*<sup>2</sup> + *bx* + *c* = 0 with a **number** (other than 1)  **in front of *****x***<sup>**2**</sup>

  - yo"
- Chunk excerpt: «How do I solve by completing the square when there is a coefficient in front of the x<sup>2</sup> term? - If the equation is *ax*<sup>2</sup> + *bx* + *c* = 0 with a **number** (other than 1) **in front of *****x***<sup>**2**</sup> - you can **divide both sides by *****a**** *first (before completing the square) - For example 3*x*<sup>2</sup> + 12*x* + 9 = 0 - Divide both sides by 3 - *x*<sup>2</sup> + 4*x* + 3 = 0 -»
- Upstream: T-C32 join notes/2-equations-formulae-and-identities/solving-quadratic-equations/solving-by-completing-the-square.json::spcpt_W2v94nxskTtpWxWd — tier S1_name_match — score 0.6624 — wording EXACT — validation tier AI_VALIDATED (operator-delegated chain)
- Rationale: SME span 'Solving by Completing the Square' on note 'Solving by Completing the Square' is anchored by the corpus spec_point block spcpt_W2v94nxskTtpWxWd and joined to 4MA1-2.7B via name_to_statement_join; this section chunk sits inside that span.
- Verdict: [ ] CONFIRM — this chunk belongs to this SP   [ ] REJECT — wrong chunk/SP   [ ] HOLD — needs rework

### 4MA1-5.2D — understand that reflections are specified by a mirror line
- Note: Reflections (`notes/5-vectors-and-transformation-geometry/transformations/reflections.json`)
- Chunk: ordinal 0 — heading `Reflections` — sha256_16 `9e676ed4a2c9d570` — 11 chars
- Evidence quote (verbatim self-slice, markdown-safe): "Reflections"
- Chunk excerpt: «Reflections»
- Upstream: T-C32 join notes/5-vectors-and-transformation-geometry/transformations/reflections.json::spcpt_DQrkJGG4Mngch9xc — tier S1_name_match — score 0.7275 — wording EXACT — validation tier AI_VALIDATED (operator-delegated chain)
- Rationale: SME span 'Reflections' on note 'Reflections' is anchored by the corpus spec_point block spcpt_DQrkJGG4Mngch9xc and joined to 4MA1-5.2D via name_to_statement_join; this section chunk sits inside that span.
- Verdict: [ ] CONFIRM — this chunk belongs to this SP   [ ] REJECT — wrong chunk/SP   [ ] HOLD — needs rework

### 4MA1-4.10D — find the surface area of a cylinder
- Note: Surface Area (`notes/4-geometry-and-trigonometry/volume-and-surface-area/surface-area.json`)
- Chunk: ordinal 3 — heading `How do I find the surface area of a cylinder?` — sha256_16 `bf95a031fdc79d58` — 634 chars
- Evidence quote (verbatim self-slice, markdown-safe): "How do I find the surface area of a cylinder?
- A cylinder has **two flat surfaces** (the top and the base) and** one curved surface**
- The **net** of a cylinder consists of** two circles** and a **rectangle**"
- Chunk excerpt: «How do I find the surface area of a cylinder? - A cylinder has **two flat surfaces** (the top and the base) and** one curved surface** - The **net** of a cylinder consists of** two circles** and a **rectangle** ![A cylinder and its net](assets/ec94c591acff-52892-surface-area-2.png) - The **curved surface area** of a cylinder, *A*, with base radius, *r*, and height, *h*, is therefore given by - $A=2πrh$ - This formula»
- Upstream: T-C32 join notes/4-geometry-and-trigonometry/volume-and-surface-area/surface-area.json::spcpt_2w9hbV5pTbvc5Smj — tier S1_name_match — score 0.8043 — wording EXACT — validation tier AI_VALIDATED (operator-delegated chain)
- Rationale: SME span 'Surface Area' on note 'Surface Area' is anchored by the corpus spec_point block spcpt_2w9hbV5pTbvc5Smj and joined to 4MA1-4.10D via name_to_statement_join; this section chunk sits inside that span.
- Verdict: [ ] CONFIRM — this chunk belongs to this SP   [ ] REJECT — wrong chunk/SP   [ ] HOLD — needs rework

### 4MA1-1.5E — use Venn diagrams to represent sets
- Note: Set Notation & Venn Diagrams (`notes/1-numbers-and-the-number-system/set-notation-and-venn-diagrams/set-notation-and-venn-diagrams.json`)
- Chunk: ordinal 4 — heading `What is a Venn diagram?` — sha256_16 `43e5f2adde17500b` — 484 chars
- Evidence quote (verbatim self-slice, markdown-safe): "What is a Venn diagram?
- A Venn diagram is a way to illustrate **all the elements within sets **and any** intersections **
- A Venn diagram consists of

  - a **rectangle** representing the **universal set (**$E$**)**
  - a **circle** for "
- Chunk excerpt: «What is a Venn diagram? - A Venn diagram is a way to illustrate **all the elements within sets **and any** intersections ** - A Venn diagram consists of - a **rectangle** representing the **universal set (**$E$**)** - a **circle** for each **set** - Circles may or may not overlap depending on which **elements** are shared between **sets** - A Venn diagram either shows: - the **elements **in each intersection - the **»
- Upstream: T-C32 join notes/1-numbers-and-the-number-system/set-notation-and-venn-diagrams/set-notation-and-venn-diagrams.json::spcpt_XT9QGzbhpThbfcB6 — tier S1_name_match — score 0.8415 — wording EXACT — validation tier AI_VALIDATED (operator-delegated chain)
- Rationale: SME span 'Sets & Venn Diagrams' on note 'Set Notation & Venn Diagrams' is anchored by the corpus spec_point block spcpt_XT9QGzbhpThbfcB6 and joined to 4MA1-1.5E via name_to_statement_join; this section chunk sits inside that span.
- Verdict: [ ] CONFIRM — this chunk belongs to this SP   [ ] REJECT — wrong chunk/SP   [ ] HOLD — needs rework

### 4MA1-1.2B — understand and use mixed numbers and vulgar fractions
- Note: Mixed Numbers & Improper Fractions (`notes/1-numbers-and-the-number-system/fractions/mixed-numbers-and-improper-fractions.json`)
- Chunk: ordinal 1 — heading `What are mixed numbers & improper fractions?` — sha256_16 `0402778d4eedf876` — 572 chars
- Evidence quote (verbatim self-slice, markdown-safe): "What are mixed numbers & improper fractions?
- A **mixed number **has an ***integer*** part and a **fraction** part

  - $3\frac{3}{4}$ has the whole number 3 and the fraction $\frac{3}{4}$, meaning “three and three quarters”
- An **imprope"
- Chunk excerpt: «What are mixed numbers & improper fractions? - A **mixed number **has an ***integer*** part and a **fraction** part - $3\frac{3}{4}$ has the whole number 3 and the fraction $\frac{3}{4}$, meaning “three and three quarters” - An **improper fraction** is also known as a **top-heavy fraction** - An **improper fraction** is a fraction where the ***numerator*** is **bigger **than the ***denominator*** - $\frac{15}{4}$ mea»
- Upstream: T-C32 join notes/1-numbers-and-the-number-system/fractions/mixed-numbers-and-improper-fractions.json::spcpt_6XysCMWvYY936jw8 — tier S1_name_match — score 0.6853 — wording EXACT — validation tier AI_VALIDATED (operator-delegated chain)
- Rationale: SME span 'Mixed Numbers & Improper Fractions' on note 'Mixed Numbers & Improper Fractions' is anchored by the corpus spec_point block spcpt_6XysCMWvYY936jw8 and joined to 4MA1-1.2B via name_to_statement_join; this section chunk sits inside that span.
- Verdict: [ ] CONFIRM — this chunk belongs to this SP   [ ] REJECT — wrong chunk/SP   [ ] HOLD — needs rework

### 4MA1-5.2H — understand and use column vectors in translations
- Note: Translations (`notes/5-vectors-and-transformation-geometry/transformations/translations.json`)
- Chunk: ordinal 5 — heading `How do I describe a translation?` — sha256_16 `72749f54c8ba909d` — 1872 chars
- Evidence quote (verbatim self-slice, markdown-safe): "How do I describe a translation?
- To describe a **translation**, you must:

  - State that the transformation is a **translation**
  - Give the** column vector **that describes the movement
- To find the **vector**:

  - **Pick** a **point"
- Chunk excerpt: «How do I describe a translation? - To describe a **translation**, you must: - State that the transformation is a **translation** - Give the** column vector **that describes the movement - To find the **vector**: - **Pick** a **point** on the **original **shape - **Identify** the **corresponding point** on the **image** - Count how far **left or right** ($x$) you need to go **from the object** to get **to the image** »
- Upstream: T-C32 join notes/5-vectors-and-transformation-geometry/transformations/translations.json::spcpt_YQX35KWR6v8thX5T — tier S1_name_match — score 0.7574 — wording EXACT — validation tier AI_VALIDATED (operator-delegated chain)
- Rationale: SME span 'Translations' on note 'Translations' is anchored by the corpus spec_point block spcpt_YQX35KWR6v8thX5T and joined to 4MA1-5.2H via name_to_statement_join; this section chunk sits inside that span.
- Verdict: [ ] CONFIRM — this chunk belongs to this SP   [ ] REJECT — wrong chunk/SP   [ ] HOLD — needs rework

### 4MA1-4.2D — understand the term ‘regular polygon’ and calculate interior and exterior angles of regular polygons
- Note: Angles in Polygons (`notes/4-geometry-and-trigonometry/angles-in-polygons-and-parallel-lines/angles-in-polygons.json`)
- Chunk: ordinal 5 — heading `How do I find the size of an interior or exterior angle in a regular polygon?` — sha256_16 `a3f785814857040d` — 1467 chars
- Evidence quote (verbatim self-slice, markdown-safe): "How do I find the size of an interior or exterior angle in a regular polygon?
- To find the **size of an interior angle** in a **regular polygon**:
- **Method 1**
Find the **sum** of the **interior angles**

  - For a pentagon: `180 degree "
- Chunk excerpt: «How do I find the size of an interior or exterior angle in a regular polygon? - To find the **size of an interior angle** in a **regular polygon**: - **Method 1** Find the **sum** of the **interior angles** - For a pentagon: `180 degree cross times open parentheses 5 minus 2 close parentheses space equals space 540 degree` - **Divide** by the **number of sides** ($n$) - For a pentagon: $540^{\circ}\div5=108^{\circ}$ »
- Upstream: T-C32 join notes/4-geometry-and-trigonometry/angles-in-polygons-and-parallel-lines/angles-in-polygons.json::spcpt_gzykj64JBx2RtBJ7 — tier S2_name_ambiguous — score 0.7085 — wording EXACT — validation tier AI_VALIDATED (operator-delegated chain)
- Rationale: SME span 'Angles in Polygons' on note 'Angles in Polygons' is anchored by the corpus spec_point block spcpt_gzykj64JBx2RtBJ7 and joined to 4MA1-4.2D via name_to_statement_join; this section chunk sits inside that span.
- Verdict: [ ] CONFIRM — this chunk belongs to this SP   [ ] REJECT — wrong chunk/SP   [ ] HOLD — needs rework

### 4MA1-4.4D — understand angle measure including three-figure bearings
- Note: Bearings (`notes/4-geometry-and-trigonometry/bearings-scale-drawing-and-constructions/bearings.json`)
- Chunk: ordinal 1 — heading `What are bearings?` — sha256_16 `d593af2f08c9b539` — 575 chars
- Evidence quote (verbatim self-slice, markdown-safe): "What are bearings?
- **Bearings **are a way of describing an **angle**

  - They are commonly used in **navigation**
- There are **three rules** which must be followed when using a bearing:

  - They are measured **from North**
  
    - Nor"
- Chunk excerpt: «What are bearings? - **Bearings **are a way of describing an **angle** - They are commonly used in **navigation** - There are **three rules** which must be followed when using a bearing: - They are measured **from North** - North is usually straight up on a scale drawing or map, and should be labelled on the diagram - They are measured** clockwise** - The angle should always be written with **3 digits** - 059° instea»
- Upstream: T-C32 join notes/4-geometry-and-trigonometry/bearings-scale-drawing-and-constructions/bearings.json::spcpt_38XcCSfT6hW33fDn — tier S1_name_match — score 0.7 — wording EXACT — validation tier AI_VALIDATED (operator-delegated chain)
- Rationale: SME span 'Bearings' on note 'Bearings' is anchored by the corpus spec_point block spcpt_38XcCSfT6hW33fDn and joined to 4MA1-4.4D via name_to_statement_join; this section chunk sits inside that span.
- Verdict: [ ] CONFIRM — this chunk belongs to this SP   [ ] REJECT — wrong chunk/SP   [ ] HOLD — needs rework

### 4MA1-2.7D — solve simultaneous equations in two unknowns, one equation being linear and the other being quadratic
- Note: Linear Simultaneous Equations (`notes/2-equations-formulae-and-identities/simultaneous-equations/linear.json`)
- Chunk: ordinal 5 — heading `How do I form simultaneous equations?` — sha256_16 `85d7785806365ca4` — 3216 chars
- Evidence quote (verbatim self-slice, markdown-safe): "How do I form simultaneous equations?
- Introduce **two letters**, *x* and *y*, to represent **two unknowns**

  - Make sure you know exactly what they stand for (and any units)
- Create **two different equations** from the words or context"
- Chunk excerpt: «How do I form simultaneous equations? - Introduce **two letters**, *x* and *y*, to represent **two unknowns** - Make sure you know exactly what they stand for (and any units) - Create **two different equations** from the words or contexts - 3 apples and 2 bananas cost £1.80, while 5 apples and 1 banana cost £2.30 - 3*x* + 2*y* = 180 and 5*x* + *y *= 230 *x *is the **price** of an apple, in **pence** *y *is the **pric»
- Upstream: T-C32 join notes/2-equations-formulae-and-identities/simultaneous-equations/linear.json::spcpt_h5yjgd2WdgmJqHJM — tier S1_name_match — score 0.755 — wording EXACT — validation tier AI_VALIDATED (operator-delegated chain)
- Rationale: SME span 'Linear Simultaneous Equations' on note 'Linear Simultaneous Equations' is anchored by the corpus spec_point block spcpt_h5yjgd2WdgmJqHJM and joined to 4MA1-2.7D via name_to_statement_join; this section chunk sits inside that span.
- Verdict: [ ] CONFIRM — this chunk belongs to this SP   [ ] REJECT — wrong chunk/SP   [ ] HOLD — needs rework

### 4MA1-4.4D — understand angle measure including three-figure bearings
- Note: Bearings (`notes/4-geometry-and-trigonometry/bearings-scale-drawing-and-constructions/bearings.json`)
- Chunk: ordinal 4 — heading `How do I find the bearing of B from A if I know the bearing of A from B?` — sha256_16 `231e9a1ccd4010ba` — 309 chars
- Evidence quote (verbatim self-slice, markdown-safe): "How do I find the bearing of B from A if I know the bearing of A from B?
- If the **bearing of A from B** is **less than 180°**

  - **Add 180°** to it to find the **bearing of B from A**
- If the **bearing of A from B** is **more than 180°"
- Chunk excerpt: «How do I find the bearing of B from A if I know the bearing of A from B? - If the **bearing of A from B** is **less than 180°** - **Add 180°** to it to find the **bearing of B from A** - If the **bearing of A from B** is **more than 180°** - **Subtract 180°** from it to find the **bearing of B from A**»
- Upstream: T-C32 join notes/4-geometry-and-trigonometry/bearings-scale-drawing-and-constructions/bearings.json::spcpt_38XcCSfT6hW33fDn — tier S1_name_match — score 0.7 — wording EXACT — validation tier AI_VALIDATED (operator-delegated chain)
- Rationale: SME span 'Bearings' on note 'Bearings' is anchored by the corpus spec_point block spcpt_38XcCSfT6hW33fDn and joined to 4MA1-4.4D via name_to_statement_join; this section chunk sits inside that span.
- Verdict: [ ] CONFIRM — this chunk belongs to this SP   [ ] REJECT — wrong chunk/SP   [ ] HOLD — needs rework

### 4MA1-4.11C — use areas and volumes of similar figures in solving problems
- Note: Similar Areas & Volumes (`notes/4-geometry-and-trigonometry/area-and-volume-of-similar-shapes/similar-areas-and-volumes.json`)
- Chunk: ordinal 1 — heading `How do I find the length, area or volume scale factors of similar shapes?` — sha256_16 `0a1e0fafbbf471a0` — 745 chars
- Evidence quote (verbatim self-slice, markdown-safe): "How do I find the length, area or volume scale factors of similar shapes?
- The **scale factor** (SF) for a given quantity (length, area or volume) between **two similar shapes** can be found by dividing the quantity on one shape by the qua"
- Chunk excerpt: «How do I find the length, area or volume scale factors of similar shapes? - The **scale factor** (SF) for a given quantity (length, area or volume) between **two similar shapes** can be found by dividing the quantity on one shape by the quantity on the other shape - $\mathrm{scale} \mathrm{factor}=\frac{\mathrm{quantity} \mathrm{on} \mathrm{one} \mathrm{shape}}{\mathrm{corresponding} \mathrm{quantity} \mathrm{on} \ma»
- Upstream: T-C32 join notes/4-geometry-and-trigonometry/area-and-volume-of-similar-shapes/similar-areas-and-volumes.json::spcpt_dBwfqg3wJvDp9PNs — tier S1_name_match — score 0.758 — wording EXACT — validation tier AI_VALIDATED (operator-delegated chain)
- Rationale: SME span 'Similar Areas & Volumes' on note 'Similar Areas & Volumes' is anchored by the corpus spec_point block spcpt_dBwfqg3wJvDp9PNs and joined to 4MA1-4.11C via name_to_statement_join; this section chunk sits inside that span.
- Verdict: [ ] CONFIRM — this chunk belongs to this SP   [ ] REJECT — wrong chunk/SP   [ ] HOLD — needs rework


## Part B — worklist decisions (79 rows)

### (anchor unresolved) — 
- Note: `notes/6-statistics-and-probability/statistics-toolkit/discrete-and-continuous-data.json`
- Chunk: ordinal 0 — heading `Discrete & continuous data`
- Reason: span anchor spcpt_QWXhzVp2S3VYZdZc ('Discrete & Continuous Data') is the T-C32 join's single unresolved anchor — operator adjudication pending (PROPOSAL-ONLY; never fabricated)
- Disposition: WORKLIST — chunk-level mapping waits on the anchor's operator adjudication (C32 §3 residual)
- Verdict: [ ] AUTHOR an anchor   [ ] REPAIR corpus/markdown   [x] DEFER (record why)

### (anchor unresolved) — 
- Note: `notes/6-statistics-and-probability/statistics-toolkit/discrete-and-continuous-data.json`
- Chunk: ordinal 1 — heading `What is discrete and continuous data?`
- Reason: span anchor spcpt_QWXhzVp2S3VYZdZc ('Discrete & Continuous Data') is the T-C32 join's single unresolved anchor — operator adjudication pending (PROPOSAL-ONLY; never fabricated)
- Disposition: WORKLIST — chunk-level mapping waits on the anchor's operator adjudication (C32 §3 residual)
- Verdict: [ ] AUTHOR an anchor   [ ] REPAIR corpus/markdown   [x] DEFER (record why)

### 4MA1-1.11A — use a scientific electronic calculator to determine numerical results
- Note: `(no notes coverage)`
- Chunk: (corpus gap — no chunk exists)
- Reason: no notes-corpus anchor resolves to this SP in the T-C32 join (registered corpus gap: the notes coverage is bounded by the 111-code census)
- Disposition: WORKLIST — chunk-level mapping needs notes coverage or an operator-authored anchor; recorded, not forced (C31 §6)
- Verdict: [ ] AUTHOR an anchor   [ ] REPAIR corpus/markdown   [x] DEFER (record why)

### 4MA1-1.1A — understand and use integers (positive, negative and zero)
- Note: `(no notes coverage)`
- Chunk: (corpus gap — no chunk exists)
- Reason: no notes-corpus anchor resolves to this SP in the T-C32 join (registered corpus gap: the notes coverage is bounded by the 111-code census)
- Disposition: WORKLIST — chunk-level mapping needs notes coverage or an operator-authored anchor; recorded, not forced (C31 §6)
- Verdict: [ ] AUTHOR an anchor   [ ] REPAIR corpus/markdown   [x] DEFER (record why)

### 4MA1-1.1B — understand place value
- Note: `(no notes coverage)`
- Chunk: (corpus gap — no chunk exists)
- Reason: no notes-corpus anchor resolves to this SP in the T-C32 join (registered corpus gap: the notes coverage is bounded by the 111-code census)
- Disposition: WORKLIST — chunk-level mapping needs notes coverage or an operator-authored anchor; recorded, not forced (C31 §6)
- Verdict: [ ] AUTHOR an anchor   [ ] REPAIR corpus/markdown   [x] DEFER (record why)

### 4MA1-1.1C — use directed numbers in practical situations
- Note: `(no notes coverage)`
- Chunk: (corpus gap — no chunk exists)
- Reason: no notes-corpus anchor resolves to this SP in the T-C32 join (registered corpus gap: the notes coverage is bounded by the 111-code census)
- Disposition: WORKLIST — chunk-level mapping needs notes coverage or an operator-authored anchor; recorded, not forced (C31 §6)
- Verdict: [ ] AUTHOR an anchor   [ ] REPAIR corpus/markdown   [x] DEFER (record why)

### 4MA1-1.1D — order integers
- Note: `(no notes coverage)`
- Chunk: (corpus gap — no chunk exists)
- Reason: no notes-corpus anchor resolves to this SP in the T-C32 join (registered corpus gap: the notes coverage is bounded by the 111-code census)
- Disposition: WORKLIST — chunk-level mapping needs notes coverage or an operator-authored anchor; recorded, not forced (C31 §6)
- Verdict: [ ] AUTHOR an anchor   [ ] REPAIR corpus/markdown   [x] DEFER (record why)

### 4MA1-1.1E — use the four rules of addition, subtraction, multiplication and division
- Note: `(no notes coverage)`
- Chunk: (corpus gap — no chunk exists)
- Reason: no notes-corpus anchor resolves to this SP in the T-C32 join (registered corpus gap: the notes coverage is bounded by the 111-code census)
- Disposition: WORKLIST — chunk-level mapping needs notes coverage or an operator-authored anchor; recorded, not forced (C31 §6)
- Verdict: [ ] AUTHOR an anchor   [ ] REPAIR corpus/markdown   [x] DEFER (record why)

### 4MA1-1.1H — identify prime factors, common factors and common multiples
- Note: `(no notes coverage)`
- Chunk: (corpus gap — no chunk exists)
- Reason: no notes-corpus anchor resolves to this SP in the T-C32 join (registered corpus gap: the notes coverage is bounded by the 111-code census)
- Disposition: WORKLIST — chunk-level mapping needs notes coverage or an operator-authored anchor; recorded, not forced (C31 §6)
- Verdict: [ ] AUTHOR an anchor   [ ] REPAIR corpus/markdown   [x] DEFER (record why)

### 4MA1-1.2C — identify common denominators
- Note: `(no notes coverage)`
- Chunk: (corpus gap — no chunk exists)
- Reason: no notes-corpus anchor resolves to this SP in the T-C32 join (registered corpus gap: the notes coverage is bounded by the 111-code census)
- Disposition: WORKLIST — chunk-level mapping needs notes coverage or an operator-authored anchor; recorded, not forced (C31 §6)
- Verdict: [ ] AUTHOR an anchor   [ ] REPAIR corpus/markdown   [x] DEFER (record why)

### 4MA1-1.2D — order fractions and calculate a given fraction of a given quantity
- Note: `(no notes coverage)`
- Chunk: (corpus gap — no chunk exists)
- Reason: no notes-corpus anchor resolves to this SP in the T-C32 join (registered corpus gap: the notes coverage is bounded by the 111-code census)
- Disposition: WORKLIST — chunk-level mapping needs notes coverage or an operator-authored anchor; recorded, not forced (C31 §6)
- Verdict: [ ] AUTHOR an anchor   [ ] REPAIR corpus/markdown   [x] DEFER (record why)

### 4MA1-1.2E — express a given number as a fraction of another number
- Note: `(no notes coverage)`
- Chunk: (corpus gap — no chunk exists)
- Reason: no notes-corpus anchor resolves to this SP in the T-C32 join (registered corpus gap: the notes coverage is bounded by the 111-code census)
- Disposition: WORKLIST — chunk-level mapping needs notes coverage or an operator-authored anchor; recorded, not forced (C31 §6)
- Verdict: [ ] AUTHOR an anchor   [ ] REPAIR corpus/markdown   [x] DEFER (record why)

### 4MA1-1.2H — understand and use unit fractions as multiplicative inverses
- Note: `(no notes coverage)`
- Chunk: (corpus gap — no chunk exists)
- Reason: no notes-corpus anchor resolves to this SP in the T-C32 join (registered corpus gap: the notes coverage is bounded by the 111-code census)
- Disposition: WORKLIST — chunk-level mapping needs notes coverage or an operator-authored anchor; recorded, not forced (C31 §6)
- Verdict: [ ] AUTHOR an anchor   [ ] REPAIR corpus/markdown   [x] DEFER (record why)

### 4MA1-1.3B — understand place value
- Note: `(no notes coverage)`
- Chunk: (corpus gap — no chunk exists)
- Reason: no notes-corpus anchor resolves to this SP in the T-C32 join (registered corpus gap: the notes coverage is bounded by the 111-code census)
- Disposition: WORKLIST — chunk-level mapping needs notes coverage or an operator-authored anchor; recorded, not forced (C31 §6)
- Verdict: [ ] AUTHOR an anchor   [ ] REPAIR corpus/markdown   [x] DEFER (record why)

### 4MA1-1.3D — convert a decimal to a fraction or a percentage
- Note: `(no notes coverage)`
- Chunk: (corpus gap — no chunk exists)
- Reason: no notes-corpus anchor resolves to this SP in the T-C32 join (registered corpus gap: the notes coverage is bounded by the 111-code census)
- Disposition: WORKLIST — chunk-level mapping needs notes coverage or an operator-authored anchor; recorded, not forced (C31 §6)
- Verdict: [ ] AUTHOR an anchor   [ ] REPAIR corpus/markdown   [x] DEFER (record why)

### 4MA1-1.3E — recognise that a terminating decimal is a fraction
- Note: `(no notes coverage)`
- Chunk: (corpus gap — no chunk exists)
- Reason: no notes-corpus anchor resolves to this SP in the T-C32 join (registered corpus gap: the notes coverage is bounded by the 111-code census)
- Disposition: WORKLIST — chunk-level mapping needs notes coverage or an operator-authored anchor; recorded, not forced (C31 §6)
- Verdict: [ ] AUTHOR an anchor   [ ] REPAIR corpus/markdown   [x] DEFER (record why)

### 4MA1-1.5A — understand sets defined in algebraic terms, and understand and use subsets
- Note: `(no notes coverage)`
- Chunk: (corpus gap — no chunk exists)
- Reason: no notes-corpus anchor resolves to this SP in the T-C32 join (registered corpus gap: the notes coverage is bounded by the 111-code census)
- Disposition: WORKLIST — chunk-level mapping needs notes coverage or an operator-authored anchor; recorded, not forced (C31 §6)
- Verdict: [ ] AUTHOR an anchor   [ ] REPAIR corpus/markdown   [x] DEFER (record why)

### 4MA1-1.5D — use sets in practical situations
- Note: `(no notes coverage)`
- Chunk: (corpus gap — no chunk exists)
- Reason: no notes-corpus anchor resolves to this SP in the T-C32 join (registered corpus gap: the notes coverage is bounded by the 111-code census)
- Disposition: WORKLIST — chunk-level mapping needs notes coverage or an operator-authored anchor; recorded, not forced (C31 §6)
- Verdict: [ ] AUTHOR an anchor   [ ] REPAIR corpus/markdown   [x] DEFER (record why)

### 4MA1-1.6A — use repeated percentage change
- Note: `(no notes coverage)`
- Chunk: (corpus gap — no chunk exists)
- Reason: no notes-corpus anchor resolves to this SP in the T-C32 join (registered corpus gap: the notes coverage is bounded by the 111-code census)
- Disposition: WORKLIST — chunk-level mapping needs notes coverage or an operator-authored anchor; recorded, not forced (C31 §6)
- Verdict: [ ] AUTHOR an anchor   [ ] REPAIR corpus/markdown   [x] DEFER (record why)

### 4MA1-1.6B — solve compound interest problems
- Note: `(no notes coverage)`
- Chunk: (corpus gap — no chunk exists)
- Reason: no notes-corpus anchor resolves to this SP in the T-C32 join (registered corpus gap: the notes coverage is bounded by the 111-code census)
- Disposition: WORKLIST — chunk-level mapping needs notes coverage or an operator-authored anchor; recorded, not forced (C31 §6)
- Verdict: [ ] AUTHOR an anchor   [ ] REPAIR corpus/markdown   [x] DEFER (record why)

### 4MA1-1.6C — express a percentage as a fraction and as a decimal
- Note: `(no notes coverage)`
- Chunk: (corpus gap — no chunk exists)
- Reason: no notes-corpus anchor resolves to this SP in the T-C32 join (registered corpus gap: the notes coverage is bounded by the 111-code census)
- Disposition: WORKLIST — chunk-level mapping needs notes coverage or an operator-authored anchor; recorded, not forced (C31 §6)
- Verdict: [ ] AUTHOR an anchor   [ ] REPAIR corpus/markdown   [x] DEFER (record why)

### 4MA1-1.6D — understand the multiplicative nature of percentages as operators
- Note: `(no notes coverage)`
- Chunk: (corpus gap — no chunk exists)
- Reason: no notes-corpus anchor resolves to this SP in the T-C32 join (registered corpus gap: the notes coverage is bounded by the 111-code census)
- Disposition: WORKLIST — chunk-level mapping needs notes coverage or an operator-authored anchor; recorded, not forced (C31 §6)
- Verdict: [ ] AUTHOR an anchor   [ ] REPAIR corpus/markdown   [x] DEFER (record why)

### 4MA1-1.7A — use ratio notation, including reduction to its simplest form and its various links to fraction notation
- Note: `(no notes coverage)`
- Chunk: (corpus gap — no chunk exists)
- Reason: no notes-corpus anchor resolves to this SP in the T-C32 join (registered corpus gap: the notes coverage is bounded by the 111-code census)
- Disposition: WORKLIST — chunk-level mapping needs notes coverage or an operator-authored anchor; recorded, not forced (C31 §6)
- Verdict: [ ] AUTHOR an anchor   [ ] REPAIR corpus/markdown   [x] DEFER (record why)

### 4MA1-1.8A — solve problems using upper and lower bounds where values are given to a degree of accuracy
- Note: `(no notes coverage)`
- Chunk: (corpus gap — no chunk exists)
- Reason: no notes-corpus anchor resolves to this SP in the T-C32 join (registered corpus gap: the notes coverage is bounded by the 111-code census)
- Disposition: WORKLIST — chunk-level mapping needs notes coverage or an operator-authored anchor; recorded, not forced (C31 §6)
- Verdict: [ ] AUTHOR an anchor   [ ] REPAIR corpus/markdown   [x] DEFER (record why)

### 4MA1-2.1B — understand that algebraic expressions follow the generalised rules of arithmetic
- Note: `(no notes coverage)`
- Chunk: (corpus gap — no chunk exists)
- Reason: no notes-corpus anchor resolves to this SP in the T-C32 join (registered corpus gap: the notes coverage is bounded by the 111-code census)
- Disposition: WORKLIST — chunk-level mapping needs notes coverage or an operator-authored anchor; recorded, not forced (C31 §6)
- Verdict: [ ] AUTHOR an anchor   [ ] REPAIR corpus/markdown   [x] DEFER (record why)

### 4MA1-2.1C — use index notation for positive and negative integer powers (including zero)
- Note: `(no notes coverage)`
- Chunk: (corpus gap — no chunk exists)
- Reason: no notes-corpus anchor resolves to this SP in the T-C32 join (registered corpus gap: the notes coverage is bounded by the 111-code census)
- Disposition: WORKLIST — chunk-level mapping needs notes coverage or an operator-authored anchor; recorded, not forced (C31 §6)
- Verdict: [ ] AUTHOR an anchor   [ ] REPAIR corpus/markdown   [x] DEFER (record why)

### 4MA1-2.1D — use index laws in simple cases
- Note: `(no notes coverage)`
- Chunk: (corpus gap — no chunk exists)
- Reason: no notes-corpus anchor resolves to this SP in the T-C32 join (registered corpus gap: the notes coverage is bounded by the 111-code census)
- Disposition: WORKLIST — chunk-level mapping needs notes coverage or an operator-authored anchor; recorded, not forced (C31 §6)
- Verdict: [ ] AUTHOR an anchor   [ ] REPAIR corpus/markdown   [x] DEFER (record why)

### 4MA1-2.3A — understand the process of manipulating formulae or equations to change the subject, to include cases where the subject may appear twice or a power of the subject occurs
- Note: `(no notes coverage)`
- Chunk: (corpus gap — no chunk exists)
- Reason: no notes-corpus anchor resolves to this SP in the T-C32 join (registered corpus gap: the notes coverage is bounded by the 111-code census)
- Disposition: WORKLIST — chunk-level mapping needs notes coverage or an operator-authored anchor; recorded, not forced (C31 §6)
- Verdict: [ ] AUTHOR an anchor   [ ] REPAIR corpus/markdown   [x] DEFER (record why)

### 4MA1-2.3B — use correct notational conventions for algebraic expressions and formulae
- Note: `(no notes coverage)`
- Chunk: (corpus gap — no chunk exists)
- Reason: no notes-corpus anchor resolves to this SP in the T-C32 join (registered corpus gap: the notes coverage is bounded by the 111-code census)
- Disposition: WORKLIST — chunk-level mapping needs notes coverage or an operator-authored anchor; recorded, not forced (C31 §6)
- Verdict: [ ] AUTHOR an anchor   [ ] REPAIR corpus/markdown   [x] DEFER (record why)

### 4MA1-2.3C — substitute positive and negative integers, decimals and fractions for words and letters in expressions and formulae
- Note: `(no notes coverage)`
- Chunk: (corpus gap — no chunk exists)
- Reason: no notes-corpus anchor resolves to this SP in the T-C32 join (registered corpus gap: the notes coverage is bounded by the 111-code census)
- Disposition: WORKLIST — chunk-level mapping needs notes coverage or an operator-authored anchor; recorded, not forced (C31 §6)
- Verdict: [ ] AUTHOR an anchor   [ ] REPAIR corpus/markdown   [x] DEFER (record why)

### 4MA1-2.3D — use formulae from mathematics and other real-life contexts expressed initially in words or diagrammatic form and convert to letters and symbols
- Note: `(no notes coverage)`
- Chunk: (corpus gap — no chunk exists)
- Reason: no notes-corpus anchor resolves to this SP in the T-C32 join (registered corpus gap: the notes coverage is bounded by the 111-code census)
- Disposition: WORKLIST — chunk-level mapping needs notes coverage or an operator-authored anchor; recorded, not forced (C31 §6)
- Verdict: [ ] AUTHOR an anchor   [ ] REPAIR corpus/markdown   [x] DEFER (record why)

### 4MA1-2.3E — derive a formula or expression
- Note: `(no notes coverage)`
- Chunk: (corpus gap — no chunk exists)
- Reason: no notes-corpus anchor resolves to this SP in the T-C32 join (registered corpus gap: the notes coverage is bounded by the 111-code census)
- Disposition: WORKLIST — chunk-level mapping needs notes coverage or an operator-authored anchor; recorded, not forced (C31 §6)
- Verdict: [ ] AUTHOR an anchor   [ ] REPAIR corpus/markdown   [x] DEFER (record why)

### 4MA1-2.4A — solve linear equations, with integer or fractional coefficients, in one unknown in which the unknown appears on either side or both sides of the equation
- Note: `(no notes coverage)`
- Chunk: (corpus gap — no chunk exists)
- Reason: no notes-corpus anchor resolves to this SP in the T-C32 join (registered corpus gap: the notes coverage is bounded by the 111-code census)
- Disposition: WORKLIST — chunk-level mapping needs notes coverage or an operator-authored anchor; recorded, not forced (C31 §6)
- Verdict: [ ] AUTHOR an anchor   [ ] REPAIR corpus/markdown   [x] DEFER (record why)

### 4MA1-2.6A — calculate the exact solution of two simultaneous equations in two unknowns
- Note: `(no notes coverage)`
- Chunk: (corpus gap — no chunk exists)
- Reason: no notes-corpus anchor resolves to this SP in the T-C32 join (registered corpus gap: the notes coverage is bounded by the 111-code census)
- Disposition: WORKLIST — chunk-level mapping needs notes coverage or an operator-authored anchor; recorded, not forced (C31 §6)
- Verdict: [ ] AUTHOR an anchor   [ ] REPAIR corpus/markdown   [x] DEFER (record why)

### 4MA1-2.7C — form and solve quadratic equations from data given in a context
- Note: `(no notes coverage)`
- Chunk: (corpus gap — no chunk exists)
- Reason: no notes-corpus anchor resolves to this SP in the T-C32 join (registered corpus gap: the notes coverage is bounded by the 111-code census)
- Disposition: WORKLIST — chunk-level mapping needs notes coverage or an operator-authored anchor; recorded, not forced (C31 §6)
- Verdict: [ ] AUTHOR an anchor   [ ] REPAIR corpus/markdown   [x] DEFER (record why)

### 4MA1-2.8B — identify harder examples of regions defined by linear inequalities
- Note: `(no notes coverage)`
- Chunk: (corpus gap — no chunk exists)
- Reason: no notes-corpus anchor resolves to this SP in the T-C32 join (registered corpus gap: the notes coverage is bounded by the 111-code census)
- Disposition: WORKLIST — chunk-level mapping needs notes coverage or an operator-authored anchor; recorded, not forced (C31 §6)
- Verdict: [ ] AUTHOR an anchor   [ ] REPAIR corpus/markdown   [x] DEFER (record why)

### 4MA1-2.8C — solve simple linear inequalities in one variable and represent the solution set on a number line
- Note: `(no notes coverage)`
- Chunk: (corpus gap — no chunk exists)
- Reason: no notes-corpus anchor resolves to this SP in the T-C32 join (registered corpus gap: the notes coverage is bounded by the 111-code census)
- Disposition: WORKLIST — chunk-level mapping needs notes coverage or an operator-authored anchor; recorded, not forced (C31 §6)
- Verdict: [ ] AUTHOR an anchor   [ ] REPAIR corpus/markdown   [x] DEFER (record why)

### 4MA1-3.1B — know and use nth term = a + ( n − 1)d
- Note: `(no notes coverage)`
- Chunk: (corpus gap — no chunk exists)
- Reason: no notes-corpus anchor resolves to this SP in the T-C32 join (registered corpus gap: the notes coverage is bounded by the 111-code census)
- Disposition: WORKLIST — chunk-level mapping needs notes coverage or an operator-authored anchor; recorded, not forced (C31 §6)
- Verdict: [ ] AUTHOR an anchor   [ ] REPAIR corpus/markdown   [x] DEFER (record why)

### 4MA1-3.2B — use function notations of the form f(x) = …and f :x …
- Note: `(no notes coverage)`
- Chunk: (corpus gap — no chunk exists)
- Reason: no notes-corpus anchor resolves to this SP in the T-C32 join (registered corpus gap: the notes coverage is bounded by the 111-code census)
- Disposition: WORKLIST — chunk-level mapping needs notes coverage or an operator-authored anchor; recorded, not forced (C31 §6)
- Verdict: [ ] AUTHOR an anchor   [ ] REPAIR corpus/markdown   [x] DEFER (record why)

### 4MA1-3.2D — understand and find the composite -1 functionfgand the inverse functionf
- Note: `(no notes coverage)`
- Chunk: (corpus gap — no chunk exists)
- Reason: no notes-corpus anchor resolves to this SP in the T-C32 join (registered corpus gap: the notes coverage is bounded by the 111-code census)
- Disposition: WORKLIST — chunk-level mapping needs notes coverage or an operator-authored anchor; recorded, not forced (C31 §6)
- Verdict: [ ] AUTHOR an anchor   [ ] REPAIR corpus/markdown   [x] DEFER (record why)

### 4MA1-3.3A — recognise, plot and draw graphs with equation: 3 2 y = Ax + Bx + Cx + D in which: (i) the constants are integers and some could be zero (ii) the lettersxandycan be replaced with any other two letters or: 3 2 E F y = Ax + Bx + Cx + D + + x x in which: (i) the constants are numerical and at least three of them are zero (ii) the lettersxandycan be replaced with any other two letters or: y = sin x, y = cos x, y = tan x for angles of any size (in degrees)
- Note: `(no notes coverage)`
- Chunk: (corpus gap — no chunk exists)
- Reason: no notes-corpus anchor resolves to this SP in the T-C32 join (registered corpus gap: the notes coverage is bounded by the 111-code census)
- Disposition: WORKLIST — chunk-level mapping needs notes coverage or an operator-authored anchor; recorded, not forced (C31 §6)
- Verdict: [ ] AUTHOR an anchor   [ ] REPAIR corpus/markdown   [x] DEFER (record why)

### 4MA1-3.3C — interpret and analyse transformations of functions and write the functions algebraically
- Note: `(no notes coverage)`
- Chunk: (corpus gap — no chunk exists)
- Reason: no notes-corpus anchor resolves to this SP in the T-C32 join (registered corpus gap: the notes coverage is bounded by the 111-code census)
- Disposition: WORKLIST — chunk-level mapping needs notes coverage or an operator-authored anchor; recorded, not forced (C31 §6)
- Verdict: [ ] AUTHOR an anchor   [ ] REPAIR corpus/markdown   [x] DEFER (record why)

### 4MA1-3.3D — find the gradients of non-linear graphs
- Note: `(no notes coverage)`
- Chunk: (corpus gap — no chunk exists)
- Reason: no notes-corpus anchor resolves to this SP in the T-C32 join (registered corpus gap: the notes coverage is bounded by the 111-code census)
- Disposition: WORKLIST — chunk-level mapping needs notes coverage or an operator-authored anchor; recorded, not forced (C31 §6)
- Verdict: [ ] AUTHOR an anchor   [ ] REPAIR corpus/markdown   [x] DEFER (record why)

### 4MA1-3.4A — understand the concept of a variable rate of change
- Note: `(no notes coverage)`
- Chunk: (corpus gap — no chunk exists)
- Reason: no notes-corpus anchor resolves to this SP in the T-C32 join (registered corpus gap: the notes coverage is bounded by the 111-code census)
- Disposition: WORKLIST — chunk-level mapping needs notes coverage or an operator-authored anchor; recorded, not forced (C31 §6)
- Verdict: [ ] AUTHOR an anchor   [ ] REPAIR corpus/markdown   [x] DEFER (record why)

### 4MA1-3.4B — differentiate integer powers ofx
- Note: `(no notes coverage)`
- Chunk: (corpus gap — no chunk exists)
- Reason: no notes-corpus anchor resolves to this SP in the T-C32 join (registered corpus gap: the notes coverage is bounded by the 111-code census)
- Disposition: WORKLIST — chunk-level mapping needs notes coverage or an operator-authored anchor; recorded, not forced (C31 §6)
- Verdict: [ ] AUTHOR an anchor   [ ] REPAIR corpus/markdown   [x] DEFER (record why)

### 4MA1-3.4D — distinguish between maxima and minima by considering the general shape of the graph only
- Note: `(no notes coverage)`
- Chunk: (corpus gap — no chunk exists)
- Reason: no notes-corpus anchor resolves to this SP in the T-C32 join (registered corpus gap: the notes coverage is bounded by the 111-code census)
- Disposition: WORKLIST — chunk-level mapping needs notes coverage or an operator-authored anchor; recorded, not forced (C31 §6)
- Verdict: [ ] AUTHOR an anchor   [ ] REPAIR corpus/markdown   [x] DEFER (record why)

### 4MA1-4.10B — understand the terms ‘face’, ‘edge’ and ‘vertex’ in the context of 3D solids
- Note: `(no notes coverage)`
- Chunk: (corpus gap — no chunk exists)
- Reason: no notes-corpus anchor resolves to this SP in the T-C32 join (registered corpus gap: the notes coverage is bounded by the 111-code census)
- Disposition: WORKLIST — chunk-level mapping needs notes coverage or an operator-authored anchor; recorded, not forced (C31 §6)
- Verdict: [ ] AUTHOR an anchor   [ ] REPAIR corpus/markdown   [x] DEFER (record why)

### 4MA1-4.10C — find the surface area of simple shapes using the area formulae for triangles and rectangles
- Note: `(no notes coverage)`
- Chunk: (corpus gap — no chunk exists)
- Reason: no notes-corpus anchor resolves to this SP in the T-C32 join (registered corpus gap: the notes coverage is bounded by the 111-code census)
- Disposition: WORKLIST — chunk-level mapping needs notes coverage or an operator-authored anchor; recorded, not forced (C31 §6)
- Verdict: [ ] AUTHOR an anchor   [ ] REPAIR corpus/markdown   [x] DEFER (record why)

### 4MA1-4.10E — find the volume of prisms, including cuboids and cylinders, using an appropriate formula
- Note: `(no notes coverage)`
- Chunk: (corpus gap — no chunk exists)
- Reason: no notes-corpus anchor resolves to this SP in the T-C32 join (registered corpus gap: the notes coverage is bounded by the 111-code census)
- Disposition: WORKLIST — chunk-level mapping needs notes coverage or an operator-authored anchor; recorded, not forced (C31 §6)
- Verdict: [ ] AUTHOR an anchor   [ ] REPAIR corpus/markdown   [x] DEFER (record why)

### 4MA1-4.1A — distinguish between acute, obtuse, reflex and right angles
- Note: `(no notes coverage)`
- Chunk: (corpus gap — no chunk exists)
- Reason: no notes-corpus anchor resolves to this SP in the T-C32 join (registered corpus gap: the notes coverage is bounded by the 111-code census)
- Disposition: WORKLIST — chunk-level mapping needs notes coverage or an operator-authored anchor; recorded, not forced (C31 §6)
- Verdict: [ ] AUTHOR an anchor   [ ] REPAIR corpus/markdown   [x] DEFER (record why)

### 4MA1-4.1C — understand the exterior angle of a triangle property and the angle sum of a triangle property
- Note: `(no notes coverage)`
- Chunk: (corpus gap — no chunk exists)
- Reason: no notes-corpus anchor resolves to this SP in the T-C32 join (registered corpus gap: the notes coverage is bounded by the 111-code census)
- Disposition: WORKLIST — chunk-level mapping needs notes coverage or an operator-authored anchor; recorded, not forced (C31 §6)
- Verdict: [ ] AUTHOR an anchor   [ ] REPAIR corpus/markdown   [x] DEFER (record why)

### 4MA1-4.1D — understand the terms ‘isosceles’, ‘equilateral’ and ‘right-angled triangles’ and the angle properties of these triangles
- Note: `(no notes coverage)`
- Chunk: (corpus gap — no chunk exists)
- Reason: no notes-corpus anchor resolves to this SP in the T-C32 join (registered corpus gap: the notes coverage is bounded by the 111-code census)
- Disposition: WORKLIST — chunk-level mapping needs notes coverage or an operator-authored anchor; recorded, not forced (C31 §6)
- Verdict: [ ] AUTHOR an anchor   [ ] REPAIR corpus/markdown   [x] DEFER (record why)

### 4MA1-4.2A — recognise and give the names of polygons
- Note: `(no notes coverage)`
- Chunk: (corpus gap — no chunk exists)
- Reason: no notes-corpus anchor resolves to this SP in the T-C32 join (registered corpus gap: the notes coverage is bounded by the 111-code census)
- Disposition: WORKLIST — chunk-level mapping needs notes coverage or an operator-authored anchor; recorded, not forced (C31 §6)
- Verdict: [ ] AUTHOR an anchor   [ ] REPAIR corpus/markdown   [x] DEFER (record why)

### 4MA1-4.2E — understand and use the angle sum of polygons
- Note: `(no notes coverage)`
- Chunk: (corpus gap — no chunk exists)
- Reason: no notes-corpus anchor resolves to this SP in the T-C32 join (registered corpus gap: the notes coverage is bounded by the 111-code census)
- Disposition: WORKLIST — chunk-level mapping needs notes coverage or an operator-authored anchor; recorded, not forced (C31 §6)
- Verdict: [ ] AUTHOR an anchor   [ ] REPAIR corpus/markdown   [x] DEFER (record why)

### 4MA1-4.2G — understand that two or more polygons with the same shape and size are said to be congruent to each other
- Note: `(no notes coverage)`
- Chunk: (corpus gap — no chunk exists)
- Reason: no notes-corpus anchor resolves to this SP in the T-C32 join (registered corpus gap: the notes coverage is bounded by the 111-code census)
- Disposition: WORKLIST — chunk-level mapping needs notes coverage or an operator-authored anchor; recorded, not forced (C31 §6)
- Verdict: [ ] AUTHOR an anchor   [ ] REPAIR corpus/markdown   [x] DEFER (record why)

### 4MA1-4.4A — interpret scales on a range of measuring instruments
- Note: `(no notes coverage)`
- Chunk: (corpus gap — no chunk exists)
- Reason: no notes-corpus anchor resolves to this SP in the T-C32 join (registered corpus gap: the notes coverage is bounded by the 111-code census)
- Disposition: WORKLIST — chunk-level mapping needs notes coverage or an operator-authored anchor; recorded, not forced (C31 §6)
- Verdict: [ ] AUTHOR an anchor   [ ] REPAIR corpus/markdown   [x] DEFER (record why)

### 4MA1-4.4E — measure an angle to the nearest degree
- Note: `(no notes coverage)`
- Chunk: (corpus gap — no chunk exists)
- Reason: no notes-corpus anchor resolves to this SP in the T-C32 join (registered corpus gap: the notes coverage is bounded by the 111-code census)
- Disposition: WORKLIST — chunk-level mapping needs notes coverage or an operator-authored anchor; recorded, not forced (C31 §6)
- Verdict: [ ] AUTHOR an anchor   [ ] REPAIR corpus/markdown   [x] DEFER (record why)

### 4MA1-4.4F — understand and use the relationship between average speed, distance and time
- Note: `(no notes coverage)`
- Chunk: (corpus gap — no chunk exists)
- Reason: no notes-corpus anchor resolves to this SP in the T-C32 join (registered corpus gap: the notes coverage is bounded by the 111-code census)
- Disposition: WORKLIST — chunk-level mapping needs notes coverage or an operator-authored anchor; recorded, not forced (C31 §6)
- Verdict: [ ] AUTHOR an anchor   [ ] REPAIR corpus/markdown   [x] DEFER (record why)

### 4MA1-4.5A — measure and draw lines to the nearest millimetre
- Note: `(no notes coverage)`
- Chunk: (corpus gap — no chunk exists)
- Reason: no notes-corpus anchor resolves to this SP in the T-C32 join (registered corpus gap: the notes coverage is bounded by the 111-code census)
- Disposition: WORKLIST — chunk-level mapping needs notes coverage or an operator-authored anchor; recorded, not forced (C31 §6)
- Verdict: [ ] AUTHOR an anchor   [ ] REPAIR corpus/markdown   [x] DEFER (record why)

### 4MA1-4.7A — provide reasons, using standard geometrical statements, to support numerical values for angles obtained in any geometrical context involving lines, polygons and circles
- Note: `(no notes coverage)`
- Chunk: (corpus gap — no chunk exists)
- Reason: no notes-corpus anchor resolves to this SP in the T-C32 join (registered corpus gap: the notes coverage is bounded by the 111-code census)
- Disposition: WORKLIST — chunk-level mapping needs notes coverage or an operator-authored anchor; recorded, not forced (C31 §6)
- Verdict: [ ] AUTHOR an anchor   [ ] REPAIR corpus/markdown   [x] DEFER (record why)

### 4MA1-4.8F — apply trigonometrical methods to solve problems in three dimensions, including finding the angle between a line and a plane
- Note: `(no notes coverage)`
- Chunk: (corpus gap — no chunk exists)
- Reason: no notes-corpus anchor resolves to this SP in the T-C32 join (registered corpus gap: the notes coverage is bounded by the 111-code census)
- Disposition: WORKLIST — chunk-level mapping needs notes coverage or an operator-authored anchor; recorded, not forced (C31 §6)
- Verdict: [ ] AUTHOR an anchor   [ ] REPAIR corpus/markdown   [x] DEFER (record why)

### 4MA1-4.9D — find the area of parallelograms and trapezia
- Note: `(no notes coverage)`
- Chunk: (corpus gap — no chunk exists)
- Reason: no notes-corpus anchor resolves to this SP in the T-C32 join (registered corpus gap: the notes coverage is bounded by the 111-code census)
- Disposition: WORKLIST — chunk-level mapping needs notes coverage or an operator-authored anchor; recorded, not forced (C31 §6)
- Verdict: [ ] AUTHOR an anchor   [ ] REPAIR corpus/markdown   [x] DEFER (record why)

### 4MA1-5.1C — multiply vectors by scalar quantities
- Note: `(no notes coverage)`
- Chunk: (corpus gap — no chunk exists)
- Reason: no notes-corpus anchor resolves to this SP in the T-C32 join (registered corpus gap: the notes coverage is bounded by the 111-code census)
- Disposition: WORKLIST — chunk-level mapping needs notes coverage or an operator-authored anchor; recorded, not forced (C31 §6)
- Verdict: [ ] AUTHOR an anchor   [ ] REPAIR corpus/markdown   [x] DEFER (record why)

### 4MA1-5.1E — calculate the modulus (magnitude) of a vector
- Note: `(no notes coverage)`
- Chunk: (corpus gap — no chunk exists)
- Reason: no notes-corpus anchor resolves to this SP in the T-C32 join (registered corpus gap: the notes coverage is bounded by the 111-code census)
- Disposition: WORKLIST — chunk-level mapping needs notes coverage or an operator-authored anchor; recorded, not forced (C31 §6)
- Verdict: [ ] AUTHOR an anchor   [ ] REPAIR corpus/markdown   [x] DEFER (record why)

### 4MA1-5.2B — rotate a shape about a point through a given angle
- Note: `(no notes coverage)`
- Chunk: (corpus gap — no chunk exists)
- Reason: no notes-corpus anchor resolves to this SP in the T-C32 join (registered corpus gap: the notes coverage is bounded by the 111-code census)
- Disposition: WORKLIST — chunk-level mapping needs notes coverage or an operator-authored anchor; recorded, not forced (C31 §6)
- Verdict: [ ] AUTHOR an anchor   [ ] REPAIR corpus/markdown   [x] DEFER (record why)

### 4MA1-5.2C — recognise that an anti-clockwise rotation is apositiveangle of rotation and a clockwise rotation is anegativeangle of rotation
- Note: `(no notes coverage)`
- Chunk: (corpus gap — no chunk exists)
- Reason: no notes-corpus anchor resolves to this SP in the T-C32 join (registered corpus gap: the notes coverage is bounded by the 111-code census)
- Disposition: WORKLIST — chunk-level mapping needs notes coverage or an operator-authored anchor; recorded, not forced (C31 §6)
- Verdict: [ ] AUTHOR an anchor   [ ] REPAIR corpus/markdown   [x] DEFER (record why)

### 4MA1-5.2E — construct a mirror line given an object and reflect a shape given a mirror line
- Note: `(no notes coverage)`
- Chunk: (corpus gap — no chunk exists)
- Reason: no notes-corpus anchor resolves to this SP in the T-C32 join (registered corpus gap: the notes coverage is bounded by the 111-code census)
- Disposition: WORKLIST — chunk-level mapping needs notes coverage or an operator-authored anchor; recorded, not forced (C31 §6)
- Verdict: [ ] AUTHOR an anchor   [ ] REPAIR corpus/markdown   [x] DEFER (record why)

### 4MA1-5.2F — understand that translations are specified by a distance and direction
- Note: `(no notes coverage)`
- Chunk: (corpus gap — no chunk exists)
- Reason: no notes-corpus anchor resolves to this SP in the T-C32 join (registered corpus gap: the notes coverage is bounded by the 111-code census)
- Disposition: WORKLIST — chunk-level mapping needs notes coverage or an operator-authored anchor; recorded, not forced (C31 §6)
- Verdict: [ ] AUTHOR an anchor   [ ] REPAIR corpus/markdown   [x] DEFER (record why)

### 4MA1-5.2G — translate a shape
- Note: `(no notes coverage)`
- Chunk: (corpus gap — no chunk exists)
- Reason: no notes-corpus anchor resolves to this SP in the T-C32 join (registered corpus gap: the notes coverage is bounded by the 111-code census)
- Disposition: WORKLIST — chunk-level mapping needs notes coverage or an operator-authored anchor; recorded, not forced (C31 §6)
- Verdict: [ ] AUTHOR an anchor   [ ] REPAIR corpus/markdown   [x] DEFER (record why)

### 4MA1-5.2I — understand that rotations, reflections and translations preserve length and angle so that a transformed shape under any of these transformations remains congruent to the original shape
- Note: `(no notes coverage)`
- Chunk: (corpus gap — no chunk exists)
- Reason: no notes-corpus anchor resolves to this SP in the T-C32 join (registered corpus gap: the notes coverage is bounded by the 111-code census)
- Disposition: WORKLIST — chunk-level mapping needs notes coverage or an operator-authored anchor; recorded, not forced (C31 §6)
- Verdict: [ ] AUTHOR an anchor   [ ] REPAIR corpus/markdown   [x] DEFER (record why)

### 4MA1-5.2J — understand that enlargements are specified by a centre and a scale factor
- Note: `(no notes coverage)`
- Chunk: (corpus gap — no chunk exists)
- Reason: no notes-corpus anchor resolves to this SP in the T-C32 join (registered corpus gap: the notes coverage is bounded by the 111-code census)
- Disposition: WORKLIST — chunk-level mapping needs notes coverage or an operator-authored anchor; recorded, not forced (C31 §6)
- Verdict: [ ] AUTHOR an anchor   [ ] REPAIR corpus/markdown   [x] DEFER (record why)

### 4MA1-5.2L — enlarge a shape given the scale factor
- Note: `(no notes coverage)`
- Chunk: (corpus gap — no chunk exists)
- Reason: no notes-corpus anchor resolves to this SP in the T-C32 join (registered corpus gap: the notes coverage is bounded by the 111-code census)
- Disposition: WORKLIST — chunk-level mapping needs notes coverage or an operator-authored anchor; recorded, not forced (C31 §6)
- Verdict: [ ] AUTHOR an anchor   [ ] REPAIR corpus/markdown   [x] DEFER (record why)

### 4MA1-5.2M — identify and give complete descriptions of transformations
- Note: `(no notes coverage)`
- Chunk: (corpus gap — no chunk exists)
- Reason: no notes-corpus anchor resolves to this SP in the T-C32 join (registered corpus gap: the notes coverage is bounded by the 111-code census)
- Disposition: WORKLIST — chunk-level mapping needs notes coverage or an operator-authored anchor; recorded, not forced (C31 §6)
- Verdict: [ ] AUTHOR an anchor   [ ] REPAIR corpus/markdown   [x] DEFER (record why)

### 4MA1-6.2A — estimate the median from a cumulative frequency diagram
- Note: `(no notes coverage)`
- Chunk: (corpus gap — no chunk exists)
- Reason: no notes-corpus anchor resolves to this SP in the T-C32 join (registered corpus gap: the notes coverage is bounded by the 111-code census)
- Disposition: WORKLIST — chunk-level mapping needs notes coverage or an operator-authored anchor; recorded, not forced (C31 §6)
- Verdict: [ ] AUTHOR an anchor   [ ] REPAIR corpus/markdown   [x] DEFER (record why)

### 4MA1-6.2D — estimate the interquartile range from a cumulative frequency diagram
- Note: `(no notes coverage)`
- Chunk: (corpus gap — no chunk exists)
- Reason: no notes-corpus anchor resolves to this SP in the T-C32 join (registered corpus gap: the notes coverage is bounded by the 111-code census)
- Disposition: WORKLIST — chunk-level mapping needs notes coverage or an operator-authored anchor; recorded, not forced (C31 §6)
- Verdict: [ ] AUTHOR an anchor   [ ] REPAIR corpus/markdown   [x] DEFER (record why)

### 4MA1-6.3C — use simple conditional probability when combining events
- Note: `(no notes coverage)`
- Chunk: (corpus gap — no chunk exists)
- Reason: no notes-corpus anchor resolves to this SP in the T-C32 join (registered corpus gap: the notes coverage is bounded by the 111-code census)
- Disposition: WORKLIST — chunk-level mapping needs notes coverage or an operator-authored anchor; recorded, not forced (C31 §6)
- Verdict: [ ] AUTHOR an anchor   [ ] REPAIR corpus/markdown   [x] DEFER (record why)

### 4MA1-6.3D — apply probability to simple problems
- Note: `(no notes coverage)`
- Chunk: (corpus gap — no chunk exists)
- Reason: no notes-corpus anchor resolves to this SP in the T-C32 join (registered corpus gap: the notes coverage is bounded by the 111-code census)
- Disposition: WORKLIST — chunk-level mapping needs notes coverage or an operator-authored anchor; recorded, not forced (C31 §6)
- Verdict: [ ] AUTHOR an anchor   [ ] REPAIR corpus/markdown   [x] DEFER (record why)

### 4MA1-6.3H — calculate the probability of the complement of an event happening
- Note: `(no notes coverage)`
- Chunk: (corpus gap — no chunk exists)
- Reason: no notes-corpus anchor resolves to this SP in the T-C32 join (registered corpus gap: the notes coverage is bounded by the 111-code census)
- Disposition: WORKLIST — chunk-level mapping needs notes coverage or an operator-authored anchor; recorded, not forced (C31 §6)
- Verdict: [ ] AUTHOR an anchor   [ ] REPAIR corpus/markdown   [x] DEFER (record why)

### 4MA1-6.3I — use the addition rule of probability for mutually exclusive events
- Note: `(no notes coverage)`
- Chunk: (corpus gap — no chunk exists)
- Reason: no notes-corpus anchor resolves to this SP in the T-C32 join (registered corpus gap: the notes coverage is bounded by the 111-code census)
- Disposition: WORKLIST — chunk-level mapping needs notes coverage or an operator-authored anchor; recorded, not forced (C31 §6)
- Verdict: [ ] AUTHOR an anchor   [ ] REPAIR corpus/markdown   [x] DEFER (record why)


## Rollup

| Part | Rows | CONFIRM | REJECT | HOLD | Precision |
|---|---|---|---|---|---|
| A (anchored spot-check) | 468 | | | | |
| A stratum: join score == 1.0 | 98 | | | | |
| A stratum: join score < 1.0 | 238 | | | | |
| A stratum: join score n/a | 132 | | | | |
| B (worklist) | 79 | | 79 decided | | |

Gate: Part A precision >= 90% per class AND every Part B row decided -> the store
may be promoted (rows flip to HUMAN_VALIDATED in a recorded, deterministic apply
step — never hand-edits).

