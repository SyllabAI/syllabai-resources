---
created: 2026-10-23T12:00:00 (UTC +06:00)
source: https://undergroundmathematics.org/combining-functions/r9673
author: Underground Mathematics (University of Cambridge)
rights: © University of Cambridge (Underground Mathematics). Use inside SyllabAI is authorised by the
  operator attestation of 2026-10-23 — see LICENSE-DATA.md (Amendment 2026-10-23) in this repository.
  Takedown / correction handling as stated in LICENSE-DATA.md.
tags:
- underground-mathematics
- combining-functions
- type/review-question
resource_identity:
  ugm_id: r9673
  station: combining-functions
  station_title: Combining Functions
  resource_type_id: 10
  resource_type_label: Review question
  level: null
  ref: 9673
  old_site_id: null
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
  - code: 1.2.5
    provenance:
      tier: AI_SUGGESTED
      confidence: high
      model_version: GLM (Super Z agent, z.ai) — P3c functions cross-map (generalisation lane 2) (cross-map-functions.json
        @ syllabai-experimental 4a592ed0)
      evidence: Sketch y=f(x)+2, y=f(x+2), y=f(2x) tracking the maximum point — the spec list verbatim.
      rationale: 'Canonical UGM title: “How do these transformations change the graph of $f(x)$?”; exam
        provenance: UCLES 1988 Q[''Q6''] [9205/1 and 9206/1]'
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
  exam_reference: UCLES 1988 Q['Q6'] [9205/1 and 9206/1]
task: T-UGM-IMPORT-2
assets:
- path: https://undergroundmathematics.org/combining-functions/r9673/images/img-9673-1.png
  kind: figure
- path: https://undergroundmathematics.org/combining-functions/r9673/images/img-9673-1.png
  kind: figure
- path: https://undergroundmathematics.org/combining-functions/r9673/images/img-9673-2.png
  kind: figure
- path: https://undergroundmathematics.org/combining-functions/r9673/images/img-9673-3.png
  kind: figure
- path: https://undergroundmathematics.org/combining-functions/r9673/images/img-9673-4.png
  kind: figure
---

# How do these transformations change the graph of $f(x)$?

## Question

> [figure: graph of y = f of x — `https://undergroundmathematics.org/combining-functions/r9673/images/img-9673-1.png`] (image not included in the text import; path of record).

The diagram shows the graph for \(y = f(x)\). The curve passes through the origin, and has a maximum point at \((1, 1)\). Sketch, on separate diagrams, the graphs of

1. \(y = f(x) + 2\),
2. \(y = f(x + 2)\),
3. \(y = f(2x)\),

giving the coordinates of the maximum point in each case.

## Solution

> [figure: graph of y = f of x — `https://undergroundmathematics.org/combining-functions/r9673/images/img-9673-1.png`] (image not included in the text import; path of record).

The diagram shows the graph for \(y = f(x)\). The curve passes through the origin, and has a maximum point at \((1, 1)\). Sketch, on separate diagrams, the graphs of

1. \(y = f(x) + 2\),

… giving the coordinates of the maximum point in each case.

The graph of the function \(y = f(x) + 2\) can be obtained from the graph of the original function \(f\) by raising the \(y\)-coordinate of each point on the graph by \(2\). In particular, the maximum becomes \((1, 3)\). The new graph looks like this.

> [figure: graph of y = f(x) + 2 — `https://undergroundmathematics.org/combining-functions/r9673/images/img-9673-2.png`] (image not included in the text import; path of record).

Now the graph of the function

\(y = f(x + 2)\)

can be obtained from the graph of the original function

\(f\)

by translating each point on the graph

\(2\)

units to the left.

You might expect a shift to the right, but if you think that the \(y\)-coordinate associated with \(x = 0\) on the old graph is now associated with \(x = -2\) on the new graph, you can see it is a translation to the left.

In particular, the maximum becomes \((-1, 1)\). The new graph looks like this.

> [figure: graph of y = f(x + 2) — `https://undergroundmathematics.org/combining-functions/r9673/images/img-9673-3.png`] (image not included in the text import; path of record).

1. \(y = f(2x)\).

The graph of the function \(y = f(2x)\) can be obtained from the graph of the original function \(f\) by compressing the graph by a scale factor of \(2\) in the \(x\)-direction.

We could describe this as a stretch in the \(x\)-direction with scale factor \(\dfrac{1}{2}\).

In particular, the maximum becomes \((0.5, 1)\). The new graph looks like this.

> [figure: graph of y = f(2x) — `https://undergroundmathematics.org/combining-functions/r9673/images/img-9673-4.png`] (image not included in the text import; path of record).

Can you think of an \(f(x)\) that would give something like the starting graph above? You might use graphing software to try a few functions.
