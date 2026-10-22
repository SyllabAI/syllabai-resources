---
created: 2026-10-23T12:00:00 (UTC +06:00)
source: https://undergroundmathematics.org/combining-functions/r6607
author: Underground Mathematics (University of Cambridge)
rights: © University of Cambridge (Underground Mathematics). Use inside SyllabAI is authorised by the
  operator attestation of 2026-10-23 — see LICENSE-DATA.md (Amendment 2026-10-23) in this repository.
  Takedown / correction handling as stated in LICENSE-DATA.md.
tags:
- underground-mathematics
- combining-functions
- type/review-question
resource_identity:
  ugm_id: r6607
  station: combining-functions
  station_title: Combining Functions
  resource_type_id: 10
  resource_type_label: Review question
  level: null
  ref: 6607
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
      evidence: Reach y=2^(x^2-4x+3) from y=2^(x^2) by stretch + translation — "simple combinations of
        these" verbatim. 2^x vocabulary is P2/P3 in CIE.
      rationale: 'Canonical UGM title: “Which transformations give us the graph of $y=2^{x^2-4x+3}$?”;
        exam provenance: Oxford (MAT) 2014 Q[''Q1I'']'
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
  exam_reference: Oxford (MAT) 2014 Q['Q1I']
task: T-UGM-IMPORT-2
---

# Which transformations give us the graph of $y=2^{x^2-4x+3}$?

## Question

The graph of the function \[y=2^{x^2-4x+3}\] can be obtained from the graph of \(y = 2^{x^2}\) by

1. a stretch parallel to the \(y\)-axis followed by a translation parallel to the \(y\)-axis.
2. a translation parallel to the \(x\)-axis followed by a stretch parallel to the \(y\)-axis.
3. a translation parallel to the \(x\)-axis followed by one parallel to the \(x\)-axis.
4. a translation parallel to the \(x\)-axis followed by a reflection in the \(y\)-axis.
5. a reflection parallel to the \(y\)-axis followed by a translation parallel to the \(y\)-axis.

## Suggestion

The starting and finishing functions differ by \(x^2 \mapsto x^2-4x+3\). Could we rewrite the latter to look like a transformation?

## Solution

Completing the square, we can see \(x^2-4x+3 = (x-2)^2-1\), and thus \(y=2^{x^2-4x+3} = 2^{(x-2)^2-1} = \dfrac{1}{2}\times 2^{(x-2)^2}\).

So if \(f(x) = 2^{x^2}\), then \(y=\dfrac{1}{2}\times 2^{(x-2)^2} = \dfrac{1}{2}f(x-2)\).

Now \(y=af(x+b)\) represents stretching \(y = f(x)\) in the \(y\)-direction by a scale factor of \(a\), and translating left by \(b\).

We can apply these transformations in either order for the same result. So the answer is (b).
