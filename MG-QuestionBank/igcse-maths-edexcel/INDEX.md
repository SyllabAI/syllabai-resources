# igcse-maths-edexcel — MG-QuestionBank lane index

MathsGenie IGCSE Maths (Edexcel) per-topic exam questions. 118/118 topics extracted, 1438 questions total.
Source lane: https://www.mathsgenie.co.uk/igcse/maths/edexcel · live lane: https://mathsgenie.co.uk/igcse/maths/edexcel · task `T-MG-QB-2/run-001`.

- Past-paper / predicted-paper banks are **excluded by operator decision (2026-11-07)** — no paper PDFs in this corpus.
- Mode presence per `T-MG-VERIFY-1/run-000` + live re-verification: 118 topics, zero drift; booklet 118, questions-mode 99, videos 116, flashcards 103, lessons 96; no revision-guides or question-rush mode exists in this lane.
- Source kinds: `ws` = exam-question sheet, `booklet` = booklet-only topic, `booklet*` = booklet fallback (image-only ws generation).
- Marks not printed on a sheet stay `null` in `questions.json` — never inferred (booklet "Total for question" lines are not parsed, per the T-MG-QB-1 marks law).
- Solutions are per-page scans of the source answer booklets; where the ans PDF is the covered booklet scanned with solutions, the cover page is dropped by page-count match (see `manifest.json` → `answers_cover_rule`).
- Zero-question topics (grade-3-3-1-fractions, grade-3-3-17-area-of-compound-shapes): question sheets exist at source but their text layer carries no sequentially anchorable question numbers (image-only sheets / fraction-fragment layers) — recorded `question_count: 0` with an honest gap in the manifest, never padded; content stays reachable via the recorded source URLs and the solution scans.

| Code | Topic | Grade band | Questions | Answers | Source |
|---|---|---|---|---|---|
| 1.1 | [Addition and Subtraction](grade-1-1-1-addition-and-subtraction/) | 1 | 15 | yes | ws |
| 1.2 | [Multiplication and Division](grade-1-1-2-multiplication-and-division/) | 1 | 15 | yes | ws |
| 1.3 | [Time](grade-1-1-3-time/) | 1 | 10 | yes | ws |
| 1.4 | [Writing, Simplifying and Ordering Fractions](grade-1-1-4-writing-simplifying-and-ordering-fractions/) | 1 | 19 | yes | ws |
| 1.5 | [Place Value](grade-1-1-5-place-value/) | 1 | 16 | yes | ws |
| 1.6 | [Rounding](grade-1-1-6-rounding/) | 1 | 21 | yes | ws |
| 1.7 | [Negative Numbers](grade-1-1-7-negative-numbers/) | 1 | 25 | yes | ws |
| 1.8 | [Powers and Roots](grade-1-1-8-powers-and-roots/) | 1 | 20 | yes | ws |
| 1.9 | [BIDMAS](grade-1-1-9-bidmas/) | 1 | 21 | yes | ws |
| 1.10 | [Factors and Multiples](grade-1-1-10-factors-and-multiples/) | 1 | 24 | yes | ws |
| 1.11 | [Coordinates](grade-1-1-11-coordinates/) | 1 | 9 | yes | booklet |
| 1.12 | [Pictograms](grade-1-1-12-pictograms/) | 1 | 5 | yes | booklet |
| 2.1 | [Calculation Problems](grade-2-2-1-calculation-problems/) | 2 | 14 | yes | ws |
| 2.2 | [Using a Calculator](grade-2-2-2-using-a-calculator/) | 2 | 12 | yes | ws |
| 2.3 | [Systematic Listing](grade-2-2-3-systematic-listing/) | 2 | 12 | yes | ws |
| 2.4 | [Fractions of an Amount](grade-2-2-4-fractions-of-an-amount/) | 2 | 22 | yes | ws |
| 2.5 | [Fractions, Decimals and Percentages](grade-2-2-5-fractions-decimals-and-percentages/) | 2 | 28 | yes | ws |
| 2.6 | [Simplifying Algebra](grade-2-2-6-simplifying-algebra/) | 2 | 22 | yes | ws |
| 2.7 | [Writing an Expression](grade-2-2-7-writing-an-expression/) | 2 | 16 | yes | ws |
| 2.8 | [Function Machines](grade-2-2-8-function-machines/) | 2 | 10 | yes | ws |
| 2.9 | [Solving One Step Equations](grade-2-2-9-solving-one-step-equations/) | 2 | 14 | yes | ws |
| 2.10 | [Angles](grade-2-2-10-angles/) | 2 | 14 | yes | ws |
| 2.11 | [Area and Perimeter](grade-2-2-11-area-and-perimeter/) | 2 | 13 | yes | ws |
| 2.12 | [Probability](grade-2-2-12-probability/) | 2 | 11 | yes | ws |
| 2.13 | [Frequency Polygons](grade-2-2-13-frequency-polygons/) | 2 | 7 | yes | booklet |
| 2.14 | [Averages](grade-2-2-14-averages/) | 2 | 12 | yes | ws |
| 2.15 | [Bar Charts](grade-2-2-15-bar-charts/) | 2 | 7 | yes | booklet |
| 2.16 | [Pie Charts](grade-2-2-16-pie-charts/) | 2 | 8 | yes | ws |
| 3.1 | [Fractions](grade-3-3-1-fractions/) | 3 | 0 | yes | ws |
| 3.2 | [Estimating](grade-3-3-2-estimating/) | 3 | 16 | yes | ws |
| 3.3 | [Writing and Simplifying Ratio](grade-3-3-3-writing-and-simplifying-ratio/) | 3 | 4 | yes | ws |
| 3.4 | [Ratio](grade-3-3-4-ratio/) | 3 | 24 | yes | ws |
| 3.5 | [Proportion](grade-3-3-5-proportion/) | 3 | 5 | yes | booklet |
| 3.6 | [Percentages](grade-3-3-6-percentages/) | 3 | 19 | yes | ws |
| 3.7 | [Percentage Change](grade-3-3-7-percentage-change/) | 3 | 4 | yes | ws |
| 3.8 | [Exchange Rates](grade-3-3-8-exchange-rates/) | 3 | 14 | yes | ws |
| 3.9 | [Conversions and Units](grade-3-3-9-conversions-and-units/) | 3 | 9 | yes | booklet |
| 3.10 | [Scale Drawings](grade-3-3-10-scale-drawings/) | 3 | 9 | yes | booklet* |
| 3.11 | [Best Buy Questions](grade-3-3-11-best-buy-questions/) | 3 | 6 | yes | ws |
| 3.12 | [Substitution](grade-3-3-12-substitution/) | 3 | 27 | yes | ws |
| 3.13 | [Solving Equations](grade-3-3-13-solving-equations/) | 3 | 27 | yes | ws |
| 3.14 | [Drawing Graphs](grade-3-3-14-drawing-graphs/) | 3 | 7 | yes | booklet |
| 3.15 | [Area and Circumference of Circles](grade-3-3-15-area-and-circumference-of-circles/) | 3 | 14 | yes | ws |
| 3.16 | [Transformations](grade-3-3-16-transformations/) | 3 | 8 | yes | booklet |
| 3.17 | [Area of Compound Shapes](grade-3-3-17-area-of-compound-shapes/) | 3 | 0 | yes | ws |
| 3.18 | [Frequency Trees](grade-3-3-18-frequency-trees/) | 3 | 7 | yes | ws |
| 4.1 | [Compound Interest and Depreciation](grade-4-4-1-compound-interest-and-depreciation/) | 4 | 11 | yes | ws |
| 4.2 | [Indices](grade-4-4-2-indices/) | 4 | 14 | yes | ws |
| 4.3 | [Prime Factors, HCF and LCM](grade-4-4-3-prime-factors-hcf-and-lcm/) | 4 | 10 | yes | ws |
| 4.4 | [Real Life and Distance Time Graphs](grade-4-4-4-real-life-and-distance-time-graphs/) | 4 | 7 | yes | booklet |
| 4.5 | [Inequalities](grade-4-4-5-inequalities/) | 4 | 17 | yes | ws |
| 4.6 | [Forming and Solving Equations](grade-4-4-6-forming-and-solving-equations/) | 4 | 12 | yes | ws |
| 4.7 | [Sequences (Nth Term)](grade-4-4-7-sequences-nth-term/) | 4 | 20 | yes | ws |
| 4.8 | [Expanding and Factorising](grade-4-4-8-expanding-and-factorising/) | 4 | 21 | yes | ws |
| 4.9 | [Pythagoras](grade-4-4-9-pythagoras/) | 4 | 14 | yes | ws |
| 4.10 | [Angles in Parallel Lines](grade-4-4-10-angles-in-parallel-lines/) | 4 | 8 | yes | ws |
| 4.11 | [Angles in Polygons](grade-4-4-11-angles-in-polygons/) | 4 | 7 | yes | ws |
| 4.12 | [Surface Area](grade-4-4-12-surface-area/) | 4 | 7 | yes | ws |
| 4.13 | [Volume of a Prism](grade-4-4-13-volume-of-a-prism/) | 4 | 7 | yes | ws |
| 4.14 | [Cylinders](grade-4-4-14-cylinders/) | 4 | 13 | yes | ws |
| 4.15 | [Construction](grade-4-4-15-construction/) | 4 | 6 | yes | booklet |
| 4.16 | [Bearings](grade-4-4-16-bearings/) | 4 | 9 | yes | booklet* |
| 4.17 | [Averages from Frequency Tables](grade-4-4-17-averages-from-frequency-tables/) | 4 | 8 | yes | ws |
| 4.18 | [Probability](grade-4-4-18-probability/) | 4 | 16 | yes | ws |
| 5.1 | [Reverse Percentages](grade-5-5-1-reverse-percentages/) | 5 | 9 | yes | ws |
| 5.2 | [Standard Form](grade-5-5-2-standard-form/) | 5 | 24 | yes | booklet* |
| 5.3 | [Speed and Density](grade-5-5-3-speed-and-density/) | 5 | 12 | yes | ws |
| 5.4 | [Changing the Subject of a Formula](grade-5-5-4-changing-the-subject-of-a-formula/) | 5 | 20 | yes | ws |
| 5.5 | [Expanding and Factorising Quadratics](grade-5-5-5-expanding-and-factorising-quadratics/) | 5 | 21 | yes | ws |
| 5.6 | [Solving Quadratics](grade-5-5-6-solving-quadratics/) | 5 | 18 | yes | ws |
| 5.7 | [Drawing Quadratic Graphs](grade-5-5-7-drawing-quadratic-graphs/) | 5 | 7 | yes | booklet* |
| 5.8 | [Simultaneous Equations](grade-5-5-8-simultaneous-equations/) | 5 | 14 | yes | ws |
| 5.9 | [Inequalities on Graphs](grade-5-5-9-inequalities-on-graphs/) | 5 | 7 | yes | booklet |
| 5.10 | [Similar Shapes (Lengths)](grade-5-5-10-similar-shapes-lengths/) | 5 | 7 | yes | ws |
| 5.11 | [Venn Diagrams](grade-5-5-11-venn-diagrams/) | 5 | 13 | yes | ws |
| 5.12 | [Data](grade-5-5-12-data/) | 5 | 3 | yes | booklet* |
| 6.1 | [Recurring Decimals to Fractions](grade-6-6-1-recurring-decimals-to-fractions/) | 6 | 19 | yes | booklet* |
| 6.2 | [Fractional and Negative Indices](grade-6-6-2-fractional-and-negative-indices/) | 6 | 32 | yes | ws |
| 6.3 | [Direct and Inverse Proportion](grade-6-6-3-direct-and-inverse-proportion/) | 6 | 13 | yes | booklet* |
| 6.4 | [Expanding Triple Brackets](grade-6-6-4-expanding-triple-brackets/) | 6 | 14 | yes | booklet* |
| 6.5 | [Drawing Other Graphs: Cubic/Reciprocal](grade-6-6-5-drawing-other-graphs-cubic-reciprocal/) | 6 | 7 | yes | booklet |
| 6.6 | [Solving Simultaneous Equations Graphically](grade-6-6-6-solving-simultaneous-equations-graphically/) | 6 | 5 | yes | ws |
| 6.7 | [Gradient of a Line](grade-6-6-7-gradient-of-a-line/) | 6 | 18 | yes | booklet* |
| 6.8 | [Equation of a Line](grade-6-6-8-equation-of-a-line/) | 6 | 13 | yes | ws |
| 6.9 | [Inequalities on Graphs](grade-6-6-9-inequalities-on-graphs/) | 6 | 7 | yes | booklet |
| 6.10 | [Spheres and Cones](grade-6-6-10-spheres-and-cones/) | 6 | 7 | yes | ws |
| 6.11 | [Sector Areas and Arc Lengths](grade-6-6-11-sector-areas-and-arc-lengths/) | 6 | 10 | yes | ws |
| 6.12 | [Parallel and Perpendicular Lines](grade-6-6-12-parallel-and-perpendicular-lines/) | 6 | 3 | yes | ws |
| 6.13 | [Similar Shapes (Area and Volume)](grade-6-6-13-similar-shapes-area-and-volume/) | 6 | 7 | yes | booklet* |
| 6.14 | [Circle Theorems](grade-6-6-14-circle-theorems/) | 6 | 21 | yes | ws |
| 6.15 | [Cumulative Frequency](grade-6-6-15-cumulative-frequency/) | 6 | 6 | yes | booklet* |
| 6.16 | [Vectors](grade-6-6-16-vectors/) | 6 | 9 | yes | booklet |
| 6.17 | [Probability Trees](grade-6-6-17-probability-trees/) | 6 | 7 | yes | ws |
| 7.1 | [Surds](grade-7-7-1-surds/) | 7 | 20 | yes | ws |
| 7.2 | [Bounds](grade-7-7-2-bounds/) | 7 | 13 | yes | booklet* |
| 7.3 | [Direct and Inverse Proportion](grade-7-7-3-direct-and-inverse-proportion/) | 7 | 11 | yes | ws |
| 7.4 | [Quadratic Formula](grade-7-7-4-quadratic-formula/) | 7 | 13 | yes | ws |
| 7.5 | [Factorising Harder Quadratics](grade-7-7-5-factorising-harder-quadratics/) | 7 | 21 | yes | booklet* |
| 7.6 | [Algebraic Fractions](grade-7-7-6-algebraic-fractions/) | 7 | 16 | yes | ws |
| 7.7 | [Rearranging Harder Formulae](grade-7-7-7-rearranging-harder-formulae/) | 7 | 13 | yes | booklet* |
| 7.8 | [Trigonometric and Exponential Graphs](grade-7-7-8-trigonometric-and-exponential-graphs/) | 7 | 9 | yes | booklet |
| 7.9 | [Finding the Area of Any Triangle](grade-7-7-9-finding-the-area-of-any-triangle/) | 7 | 11 | yes | ws |
| 7.10 | [The Sine Rule](grade-7-7-10-the-sine-rule/) | 7 | 10 | yes | booklet* |
| 7.11 | [The Cosine Rule](grade-7-7-11-the-cosine-rule/) | 7 | 11 | yes | booklet* |
| 7.12 | [3d Pythagoras and Trigonometry](grade-7-7-12-3d-pythagoras-and-trigonometry/) | 7 | 7 | yes | ws |
| 7.13 | [The Magnitude of a Vector](grade-7-7-13-the-magnitude-of-a-vector/) | 7 | 3 | yes | ws |
| 7.14 | [Histograms](grade-7-7-14-histograms/) | 7 | 7 | yes | booklet* |
| 7.15 | [Conditional Probability](grade-7-7-15-conditional-probability/) | 7 | 5 | yes | ws |
| 8.1 | [Quadratic Simultaneous Equations](grade-8-9-8-1-quadratic-simultaneous-equations/) | 8-9 | 9 | yes | ws |
| 8.2 | [Transforming Graphs y=f(x)](grade-8-9-8-2-transforming-graphs-y-f-x/) | 8-9 | 7 | yes | booklet* |
| 8.3 | [Proof](grade-8-9-8-3-proof/) | 8-9 | 14 | yes | ws |
| 8.4 | [Completing the Square](grade-8-9-8-4-completing-the-square/) | 8-9 | 14 | yes | booklet* |
| 8.5 | [Inverse and Composite Functions](grade-8-9-8-5-inverse-and-composite-functions/) | 8-9 | 4 | yes | ws |
| 8.6 | [Quadratic Inequalities](grade-8-9-8-6-quadratic-inequalities/) | 8-9 | 14 | yes | booklet* |
| 8.7 | [Sequences (Higher)](grade-8-9-8-7-sequences-higher/) | 8-9 | 4 | yes | ws |
| 8.8 | [Differentiation](grade-8-9-8-8-differentiation/) | 8-9 | 5 | yes | ws |
| 8.9 | [Vectors Proof Questions](grade-8-9-8-9-vectors-proof-questions/) | 8-9 | 7 | yes | booklet* |
| 8.10 | [Probability Equation Questions](grade-8-9-8-10-probability-equation-questions/) | 8-9 | 8 | yes | ws |
