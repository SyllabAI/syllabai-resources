---
created: 2026-10-23T12:00:00 (UTC +06:00)
source: https://undergroundmathematics.org/combining-functions/r5595
author: Underground Mathematics (University of Cambridge)
rights: © University of Cambridge (Underground Mathematics). Use inside SyllabAI is authorised by the
  operator attestation of 2026-10-23 — see LICENSE-DATA.md (Amendment 2026-10-23) in this repository.
  Takedown / correction handling as stated in LICENSE-DATA.md.
tags:
- underground-mathematics
- combining-functions
- type/review-question
resource_identity:
  ugm_id: r5595
  station: combining-functions
  station_title: Combining Functions
  resource_type_id: 10
  resource_type_label: Review question
  level: null
  ref: 5595
  old_site_id: Q89
spec_map:
  curriculum_code: CIE-9709-P1-2023
  lane: cie-a-level-maths-20-pure-1
  board: Cambridge CIE
  syllabus_version: 2023-2025
  subsection: combining-functions
  subsection_provenance:
    tier: PROVIDER
    signal: source-url-slug
    slug: combining-functions
    validation_status: SUGGESTED
  spec_points:
  - code: 1.2.2
    provenance:
      tier: AI_SUGGESTED
      confidence: high
      model_version: GLM (Super Z agent, z.ai) — P3c functions cross-map (generalisation lane 2) (cross-map-functions.json
        @ syllabai-experimental 4a592ed0)
      evidence: Sketch and describe f, gf, fg (e^x and x-1); the shifted-graph relationships read as translations.
        e^x vocabulary is P2/P3 in CIE.
      rationale: 'Canonical UGM title: “Can we sketch and describe these composite functions?”; exam provenance:
        UCLES 1986 Q[''Q13''] [9205/1 and 9206/1]'
      validation_status: SUGGESTED
    title: identify the range of a given function in simple cases, and find the composition of two given
      functions condition that a composite function
  - code: 1.2.5
    provenance:
      tier: AI_SUGGESTED
      confidence: high
      model_version: GLM (Super Z agent, z.ai) — P3c functions cross-map (generalisation lane 2) (cross-map-functions.json
        @ syllabai-experimental 4a592ed0)
      evidence: Sketch and describe f, gf, fg (e^x and x-1); the shifted-graph relationships read as translations.
        e^x vocabulary is P2/P3 in CIE.
      rationale: 'Canonical UGM title: “Can we sketch and describe these composite functions?”; exam provenance:
        UCLES 1986 Q[''Q13''] [9205/1 and 9206/1]'
      validation_status: SUGGESTED
    title: understand and use the transformations of the Including use of the terms 'translation', 'reflection'
      graph of y = f( x ) given by and 'stretch' in describing transformations. Questions y = f( x ) +
      a , y = f( x + a ) , may involve algebraic or trigonometric functions, or other graphs with given
      features. y = a f( x ) , y = f( ax ) and simple combinations of these.
  mapped_date: '2026-10-23'
  mapper: cross-map-functions.json (P3c) @ syllabai-experimental 4a592ed0
  coverage_note: null
provenance:
  capture_date: '2026-10-22'
  capture_tool: P2 full-site crawl (ugm-crawl) → ugm-clean extraction; text-only import
  content_language: en
  exam_reference: UCLES 1986 Q['Q13'] [9205/1 and 9206/1]
task: T-UGM-IMPORT-2
assets:
- path: https://undergroundmathematics.org/combining-functions/r5595/images/sketch1.png
  kind: figure
- path: https://undergroundmathematics.org/combining-functions/r5595/images/sketch2.png
  kind: figure
- path: https://undergroundmathematics.org/combining-functions/r5595/images/sketch3.png
  kind: figure
- path: https://undergroundmathematics.org/combining-functions/r5595/images/sketch4.png
  kind: figure
---

# Can we sketch and describe these composite functions?

## Question

1. The functions \(f\) and \(g\) are defined by \[\begin{align*} f&: x\mapsto e^x, &&x\in\mathbb{R}, \\ g&: x\mapsto x-1, &&x\in\mathbb{R}. \end{align*}\]  Sketch in a single diagram the graphs of \(f\) and the composite functions \(gf\) and \(fg\), labelling each graph clearly.  State briefly the relationship
  1. between the graphs of \(f\) and \(gf\),
  2. between the graphs of \(f\) and \(fg\).
2. Express \((1-x)(x-3)\) in the form \(a-(x-b)^2\), where \(a\) and \(b\) are constants. State the coordinates of the maximum point on the graph of \(y=(1-x)(x-3)\), and state what symmetry the graph possesses.  Sketch the graph of \(y=e^{(1-x)(x-3)}\).

## Suggestion

How do we compose two functions together?

---

How does expressing \((1-x)(x-3)\) in the form \(a-(x-b)^2\) help us find the maximum value of \(y\)?

---

Things to look out for when sketching a curve:

- can I find the asymptotes?
- can I find the intercepts with the axes?
- can I find the stationary points and their nature?
- what happens to the curve as \(x\rightarrow \pm \infty ?\)

## Solution

First, we’ll find the composite functions \(gf\) and \(fg\). We have \[gf = e^x-1\] and \[fg = e^{x-1}.\]

Let’s first sketch \(y=e^x\). We know that \(e^x\to 0\) as \(x\to -\infty\), the graph crosses the \(y\)-axis at \((1,0)\) and it is strictly increasing. So it looks roughly like this:

> [figure: the graph of y = e to the x — `https://undergroundmathematics.org/combining-functions/r5595/images/sketch1.png`] (image not included in the text import; path of record).

*\(y=e^x\)*

Now let’s add a sketch of \(e^x-1\). We know that this is a translation of \(y=e^x\) by \(-1\) in the \(y\)-direction, and that \(y=e^x\) and \(y=e^x-1\) cannot intersect. So our graph now looks like:

> [figure: the graphs of y equals e to the x and y equals e to the x - 1 — `https://undergroundmathematics.org/combining-functions/r5595/images/sketch2.png`] (image not included in the text import; path of record).

*\(y=e^x\) and \(y=e^x -1\)*

Finally, we add \(y=e^{x-1}\). This is a translation of \(y=e^x\) by \(1\) in the \(x\)-direction. The graphs of \(y = e^x\) and \(y=e^{x-1}\) don’t meet, but \(y=e^{x-1}\) does meet \(y=e^x-1\). So a sketch of the three functions looks like this:

> [figure: the three graphs y equals e to the x, y equals e to the x brackets minus 1, and y = e to the brackets x minus 1 — `https://undergroundmathematics.org/combining-functions/r5595/images/sketch3.png`] (image not included in the text import; path of record).

*\(y=e^x\) and \(y=e^x -1\) and \(y=e^{(x-1)}\)*

The graph of \(gf\) is a translation of \(f\) by one unit in the negative \(y\) direction.

The graph of \(fg\) is a translation of \(f\) by one unit in the positive \(x\) direction.

We expand \((1-x)(x-3)\) to obtain \(-x^2+4x-3\).

Completing the square, we find that \((1-x)(x-3)=-x^2+4x-3=-(x-2)^2+4-3=1-(x-2)^2.\)

We could also do this by expanding both expressions and solving for \(a\) and \(b\) after comparing coefficients.

From the rewriting of the equation \(y=(1-x)(x-3)\) in the form \(y=1-(x-2)^2\), we see that the maximum point on the graph occurs when \(y=1\) because the expression \(-(x-2)^2\) must be negative or zero. The expression \(-(x-2)^2\) is \(0\) when \(x=2\) so the maximum point has coordinates \((2,1)\). The graph possesses line symmetry about \(x=2\).

So the graph

- has a maximum at \(x=2\), \(y=e\);
- has symmetry about \(x=2\);
- has its \(y\)-intercept at \(e^{-3}\);
- sees \(y\rightarrow0\) as \(x\rightarrow\pm\infty\).

The sketch is

> [figure: Sketch of y equals e to the power 1 minus bracket x minus 2 squared — `https://undergroundmathematics.org/combining-functions/r5595/images/sketch4.png`] (image not included in the text import; path of record).
