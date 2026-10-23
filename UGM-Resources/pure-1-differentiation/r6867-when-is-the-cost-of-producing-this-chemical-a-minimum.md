---
created: 2026-10-24T01:49:53 (UTC +06:00)
source: https://undergroundmathematics.org/calculus-meets-functions/r6867
author: Underground Mathematics (University of Cambridge)
rights: © University of Cambridge (Underground Mathematics). Use inside SyllabAI is authorised by the
  operator attestation of 2026-10-23 — see LICENSE-DATA.md (Amendment 2026-10-23) in this repository.
  Takedown / correction handling as stated in LICENSE-DATA.md.
tags:
- underground-mathematics
- calculus-meets-functions
- type/review-question
resource_identity:
  ugm_id: r6867
  station: calculus-meets-functions
  station_title: Calculus meets Functions
  resource_type_id: 10
  resource_type_label: Review question
  level: null
  ref: 6867
  old_site_id: Q4044
spec_map:
  curriculum_code: CIE-9709-P1-2023
  lane: cie-a-level-maths-20-pure-1
  board: Cambridge CIE
  syllabus_version: 2023-2025
  subsection: calculus-meets-functions
  subsection_provenance:
    tier: PROVIDER
    signal: source-url-slug
    slug: calculus-meets-functions
    validation_status: SUGGESTED
  spec_points:
  - code: 1.7.2
    provenance:
      tier: AI_SUGGESTED
      confidence: high
      model_version: GLM (Super Z agent, z.ai) — P3c lane-7 cross-map (cross-map-differentiation.json
        (P3c lane 7) @ syllabai-experimental 93575e69)
      evidence: cost C=3x+100/x minimised — derivative 3-100/x^2 with a second-derivative confirmation
      rationale: 'Canonical UGM title: "When is the cost of producing this chemical a minimum?"; exam
        provenance: UCLES AO level Applicable Mathematics 1, 1989, Q5'
      validation_status: SUGGESTED
    title: use the derivative of x (for any rational n ), together with constant multiples, sums and
      differences of functions, and of composite functions using the chain rule
  - code: 1.7.4
    provenance:
      tier: AI_SUGGESTED
      confidence: high
      model_version: GLM (Super Z agent, z.ai) — P3c lane-7 cross-map (cross-map-differentiation.json
        (P3c lane 7) @ syllabai-experimental 93575e69)
      evidence: cost C=3x+100/x minimised — derivative 3-100/x^2 with a second-derivative confirmation
      rationale: 'Canonical UGM title: "When is the cost of producing this chemical a minimum?"; exam
        provenance: UCLES AO level Applicable Mathematics 1, 1989, Q5'
      validation_status: SUGGESTED
    title: locate stationary points and determine their nature, and use information about stationary
      points in sketching graphs.
  mapped_date: '2026-10-24'
  mapper: cross-map-differentiation.json (P3c lane 7) @ syllabai-experimental 93575e69
provenance:
  capture_date: '2026-10-22'
  capture_tool: P2 full-site crawl (ugm-crawl) → ugm-clean extraction; text-only import
  content_language: en
  exam_reference: UCLES AO level Applicable Mathematics 1, 1989, Q5
task: T-UGM-IMPORT-7
---

# When is the cost of producing this chemical a minimum?

## Question

The production cost per kilogram, \(C\) (in thousands of pounds) when \(x\) kilograms of a chemical are made is given by \[C=3x+\frac{100}{x},\; x>0.\] Find the value of \(x\) for which the cost is a minimum, and the minimum cost. Show, also, that this cost is a minimum rather than a maximum.

## Solution

We find the stationary points of

\(C\)

by differentiating:

\[ \frac{dC}{dx}=3-\frac{100}{x^2}. \]

Setting the derivative to zero, we find that the stationary points of

\(C\)

are given by the solutions of

\[ 3=\frac{100}{x^2}, \]

which means that

\[ x^2=\frac{100}{3}. \]

We only need to take the positive square root, since

\(x>0\)

, and so

\[ x=\frac{10}{\sqrt{3}}=\frac{10\sqrt{3}}{3}. \]

The cost at this value of

\(x\)

is

\[\begin{align*} C&=3\times\frac{10\sqrt{3}}{3}+100\times\frac{\sqrt{3}}{10} \\ &=10\sqrt{3}+10\sqrt{3} \\ &=20\sqrt{3}. \end{align*}\]

We could take the second derivative, \[\frac{d^2C}{dx^2}=\frac{200}{x^3}.\] Since \(x>0\), the second derivative is positive. Therefore the stationary point at \(x=\dfrac{10\sqrt{3}}{3}\) is certainly a *local* minimum.

As there is only one stationary point for \(x>0\), the local minimum at \(x=\dfrac{10\sqrt{3}}{3}\) gives the smallest value of \(C\) over all \(x>0\), so we have found the minimum cost of producing the chemical.

We can also decide whether a stationary point is a maximum or a minimum by looking at how the function or the first derivative behaves near the stationary point. This is particularly helpful if it would be difficult to compute the second derivative, or if the second derivative is \(0\).
