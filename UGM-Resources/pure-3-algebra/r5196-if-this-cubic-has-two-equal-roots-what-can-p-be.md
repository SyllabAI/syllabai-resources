---
created: 2026-10-25T01:37:17 (UTC +06:00)
source: https://undergroundmathematics.org/product-rule/r5196
author: Underground Mathematics (University of Cambridge)
rights: © University of Cambridge (Underground Mathematics). Use inside SyllabAI is authorised by the
  operator attestation of 2026-10-23 — see LICENSE-DATA.md (Amendment 2026-10-23) in this repository.
  Takedown / correction handling as stated in LICENSE-DATA.md.
tags:
- underground-mathematics
- product-rule
- type/review-question
resource_identity:
  ugm_id: r5196
  station: product-rule
  station_title: Product Rule & Integration by Parts
  resource_type_id: 10
  resource_type_label: Review question
  level: null
  ref: 5196
  old_site_id: null
spec_map:
  curriculum_code: CIE-9709-P3-2023
  lane: cie-a-level-maths-20-pure-3
  board: Cambridge CIE
  syllabus_version: 2023-2025
  subsection: product-rule
  subsection_provenance:
    tier: PROVIDER
    signal: source-url-slug
    slug: product-rule
    validation_status: SUGGESTED
  spec_points:
  - code: 3.1.4
    provenance:
      tier: AI_SUGGESTED
      confidence: medium
      model_version: "GLM (Super Z agent, z.ai) — P3c lane-9 cross-map (cross-map-algebra.json (P3c lane 9) @ syllabai-experimental 3098d8eb)"
      evidence: "f=(x−a)²g(x) ⟹ (x−a) divides f′(x) via the product rule; the two-equal-roots condition on x³−4x²−3x+p resolved through the factor theorem on f and f′"
      rationale: "Canonical UGM title: If this cubic has two equal roots, what can $p$ be?"
      validation_status: SUGGESTED
    title: "use the factor theorem and the remainder theorem"
  mapped_date: '2026-10-25'
  mapper: cross-map-algebra.json (P3c lane 9) @ syllabai-experimental 3098d8eb
provenance:
  capture_date: '2026-10-22'
  capture_tool: P2 full-site crawl (ugm-crawl) → ugm-clean extraction; text-only import
  content_language: en
  exam_reference: "UCLES A level Mathematics A Special paper, QP 840/0, 1978, Q1(b)"
  task: T-UGM-IMPORT-9
---

# If this cubic has two equal roots, what can $p$ be?

## Question

A polynomial \(f(x)\) has a factor \((x-a)^2\). Show that \((x-a)\) is a factor of \(f'(x)\).

The equation \(x^3 - 4x^2 - 3x + p = 0\) has two equal roots; find the two possible values of \(p\).

## Solution

If

\(f(x)\)

has a factor

\((x-a)^2\)

then by we can write

\[\begin{equation*} f(x) = (x-a)^2g(x) \end{equation*}\]

for a polynomial

\(g(x)\)

(which may be constant). Thus, by the

product rule

\[\begin{align*} f'(x) &= \frac{d}{dx} \left( (x-a)^2 \right) g(x) + (x-a)^2 \frac{d}{dx} \left( g(x) \right) \\ &= 2(x-a)g(x) + (x-a)^2g'(x) \\ &= (x-a) \left( 2g(x) + (x-a)g'(x) \right). \end{align*}\]

Since \(g(x)\) and \(g'(x)\) are polynomials, we have shown that \(f'(x)\) has \((x-a)\) as a factor.

We can understand this result graphically as follows. If \((x-a)^2\) is a factor, then \(f(x)=0\) has a repeated root at \(x=a\) and the graph of \(y=f(x)\) touches the \(x\)-axis here. The gradient of the graph must therefore be zero at this point, \(f'(a)=0\) and therefore \((x-a)\) is a factor of \(f'(x)\).

Let \(f(x) = x^3 - 4x^2 - 3x + p\), and let’s assume the repeated root is at \(x = a\). Then \((x-a)^2\) is a factor of \(f(x)\).

From the result above,

\((x-a)\)

is a factor of

\[\begin{equation*} f'(x) = 3x^2 - 8x - 3 = (3x + 1)(x - 3) \end{equation*}\]

so that \(a = 3\) or \(a = -\dfrac{1}{3}\).

If \(a = 3\), then substituting \(x=a\) into \(x^3-4x^2-3x+p=0\), we have \(p = 18\).

If \(a = -\dfrac{1}{3}\), then from \(x^3-4x^2-3x+p=0,\) we have \(p = -\dfrac{14}{27}\).

Thus \(p = 18\) and \(p = -\dfrac{14}{27}\) are the two possible values for \(p\).
