---
created: 2026-10-23T12:00:00 (UTC +06:00)
source: https://undergroundmathematics.org/combining-functions/r8028
author: Underground Mathematics (University of Cambridge)
rights: © University of Cambridge (Underground Mathematics). Use inside SyllabAI is authorised by the
  operator attestation of 2026-10-23 — see LICENSE-DATA.md (Amendment 2026-10-23) in this repository.
  Takedown / correction handling as stated in LICENSE-DATA.md.
tags:
- underground-mathematics
- combining-functions
- type/review-question
resource_identity:
  ugm_id: r8028
  station: combining-functions
  station_title: Combining Functions
  resource_type_id: 10
  resource_type_label: Review question
  level: null
  ref: 8028
  old_site_id: Q1010
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
  - code: 1.2.3
    provenance:
      tier: AI_SUGGESTED
      confidence: high
      model_version: GLM (Super Z agent, z.ai) — P3c functions cross-map (generalisation lane 2) (cross-map-functions.json
        @ syllabai-experimental 4a592ed0)
      evidence: Range of a three-part function, sketch, inverse relation and whether it is a function
        (one-one reasoning). Piecewise form extends "simple cases".
      rationale: 'Canonical UGM title: “Can we find the inverse of a function in three parts?”; exam provenance:
        UCLES 1972 Q[''Q2''] [848/1]'
      validation_status: SUGGESTED
    title: determine whether or not a given function is one-one, and find the inverse of a one-one function
      in simple cases
  - code: 1.2.2
    provenance:
      tier: AI_SUGGESTED
      confidence: high
      model_version: GLM (Super Z agent, z.ai) — P3c functions cross-map (generalisation lane 2) (cross-map-functions.json
        @ syllabai-experimental 4a592ed0)
      evidence: Range of a three-part function, sketch, inverse relation and whether it is a function
        (one-one reasoning). Piecewise form extends "simple cases".
      rationale: 'Canonical UGM title: “Can we find the inverse of a function in three parts?”; exam provenance:
        UCLES 1972 Q[''Q2''] [848/1]'
      validation_status: SUGGESTED
    title: identify the range of a given function in simple cases, and find the composition of two given
      functions condition that a composite function
  mapped_date: '2026-10-23'
  mapper: cross-map-functions.json (P3c) @ syllabai-experimental 4a592ed0
  coverage_note: null
provenance:
  capture_date: '2026-10-22'
  capture_tool: P2 full-site crawl (ugm-crawl) → ugm-clean extraction; text-only import
  content_language: en
  exam_reference: UCLES 1972 Q['Q2'] [848/1]
task: T-UGM-IMPORT-2
assets:
- path: https://undergroundmathematics.org/combining-functions/r8028/images/sketch.png
  kind: figure
---

# Can we find the inverse of a function in three parts?

## Question

The function

\(f\)

has domain

\(\{x: -3< x <3, x \text{ is real}\}\)

and is defined by

\[\begin{align*} f:x\to -5-x, \qquad &(-3< x \le -1) \\ f:x\to 2x^3, \qquad &(-1< x \le 1) \\ f:x\to 5-x, \qquad &(1< x <3). \end{align*}\]

State the range of the function and sketch the graph of \(y=f(x)\). Define the inverse relation in similar form and determine whether this inverse relation is a function.

## Suggestion

State the range of the function and sketch the graph of \(y=f(x)\). Define the inverse relation in similar form and determine whether this inverse relation is a function.

 The function

\(f\)

 has domain

\(\{x: -3< x <3, x \text{ is real}\}\)

 and is defined by

\[\begin{align*} f:x\to -5-x, \qquad &(-3< x \le -1) \\ f: x\to 2x^3, \qquad&(-1< x \le 1) \\ f:x\to 5-x, \qquad &(1< x <3). \end{align*}\]

A *relation* is a set of pairs of values, where the order matters, for example, {(1,4), (2,8), (3,12)}.

You can see that this relation could be associated with the function \(f(x) = 4x\).

Can you give an example of a relation which cannot be associated with a function like this?

What is the property of a relation that makes it a function? Can you tell if the inverse you found for this question has this property?

## Solution

State the range of the function and sketch the graph of \(y=f(x)\).

 The function

\(f\)

 has domain

\(\{x: -3< x <3, x \text{ is real}\}\)

 and is defined by

\[\begin{align*} f:x\to -5-x, \qquad &(-3< x \le -1) \\ f: x\to 2x^3, \qquad&(-1< x \le 1) \\ f:x\to 5-x, \qquad &(1< x <3). \end{align*}\]

We know that the graph \(y=-5-x\) is a straight line on the given interval, running from (-3, -2) down to \((-1,-4)\). Note that \((-1,-4)\) is included in the graph, but \((-3,-2)\) is not.

Similarly, we know that the graph \(y=5-x\) is a straight line on the given interval, running from \((1,4)\) down to \((3,2)\). Note that neither \((1,4)\) nor \((3,2)\) is included in the graph.

We should know the graph of \(y = x^3\), and \(y = 2x^3\) is a stretch of this by a scale factor of \(2\) in the \(y\)-direction. Its starting point on the given interval is \((-1,-2)\), and its endpoint is \((1,2)\). Note that \((1,2)\) is included in the graph, but \((-1,-2)\) is not.

The graph of \(y=f(x)\) is

> [figure: The graph of y. It is in three pieces, the first linearly decreasing, the second a cubic, and the third linearly decreasing again. The graph touches each y value between minus 4 and 4 exactly once. — `https://undergroundmathematics.org/combining-functions/r8028/images/sketch.png`] (image not included in the text import; path of record).

*A sketch of \(y=f(x)\)*

The solid endpoints are included in the graph, while the empty endpoints are not. Therefore the range of \(f\) is \(\{y:-4\le y<4, y\ne -2\}\).

We have that

\(g\)

is given by

\[\begin{align*} g:x\to -5-x, \qquad &(-4\le x<-2) \\ g:x\to (x/2)^{1/3}, \qquad &(-2< x \le2) \\ g:x\to 5-x. \qquad &(2< x <4) \end{align*}\]

Then \(g\) IS a function because, as we can see from our sketch, the function \(f\) is \(1-1\). The evidence for this is that no horizontal line cuts our graph of \(y = f(x)\) in two places.

We say the original function \(f\) is [injective](https://undergroundmathematics.org/glossary/injective); no point is mapped to two different points by \(g\), the inverse.
