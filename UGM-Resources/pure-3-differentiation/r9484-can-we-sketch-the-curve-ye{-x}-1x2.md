---
created: 2026-10-25T21:48:43 (UTC +06:00)
source: https://undergroundmathematics.org/product-rule/r9484
author: Underground Mathematics (University of Cambridge)
rights: © University of Cambridge (Underground Mathematics). Use inside SyllabAI is authorised by the
  operator attestation of 2026-10-23 — see LICENSE-DATA.md (Amendment 2026-10-23) in this repository.
  Takedown / correction handling as stated in LICENSE-DATA.md.
tags:
- underground-mathematics
- product-rule
- type/review-question
resource_identity:
  ugm_id: r9484
  station: product-rule
  station_title: Product Rule & Integration by Parts
  resource_type_id: 10
  resource_type_label: Review question
  level: null
  ref: 9484
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
  - code: 3.4.2
    provenance:
      tier: AI_SUGGESTED
      confidence: high
      model_version: GLM (Super Z agent, z.ai) — P3c lane-12 cross-map (cross-map-p3-differentiation.json
        (P3c lane 12) @ syllabai-experimental 506ea24f8e61cc75c4662f8ebb08cfd2b1d458d4)
      evidence: 'y = e^-x/(1+x^2): y always positive and dy/dx never positive by the quotient rule, the
        stationary point where dy/dx = 0, and the sketch (flips the lane-10 non-overlap row of record
        routed ''P3 3.4 Differentiation'')'
      rationale: 'Canonical UGM title: Can we sketch the curve $y=e^{-x}/(1+x^2)$?'
      validation_status: SUGGESTED
    title: differentiate products and quotients e.g.
  mapped_date: '2026-10-25'
  mapper: cross-map-p3-differentiation.json (P3c lane 12) @ syllabai-experimental 506ea24f8e61cc75c4662f8ebb08cfd2b1d458d4
provenance:
  capture_date: '2026-10-22'
  capture_tool: P2 full-site crawl (ugm-crawl) → ugm-clean extraction; text-only import
  content_language: en
  task: T-UGM-IMPORT-12
---

# Can we sketch the curve $y=e^{-x}/(1+x^2)$?

## Question

If \(y=\dfrac{e^{-x}}{1+x^2}\), prove that (i) \(y\) is always positive, (ii) \(\dfrac{\mathrm{d}y}{\mathrm{d}x}\) is never positive.

Find the coordinates of the point where \(\dfrac{\mathrm{d}y}{\mathrm{d}x}=0\), and sketch the graph of the function.

(It can be assume that as \(x \to -\infty\), \(y \to \infty\).)

## Solution

If \(y=\dfrac{e^{-x}}{1+x^2}\), prove that (i) \(y\) is always positive, …

We know \(e^x > 0\) for every \(x\), so \(e^{-x}\) has to be always positive too. We also know \(x^2\geq 0\), so \(\dfrac{1}{1+x^2}\) must be always positive.

The product of two positive numbers is also positive, and so \[\dfrac{e^{-x}}{1+x^2}>0,\] for every value of \(x\).

…, (ii) \(\dfrac{\mathrm{d}y}{\mathrm{d}x}\) is never positive.

We can find

\(y'\)

using the

quotient rule

. We find

\[\begin{align*} \dfrac{\mathrm{d}y}{\mathrm{d}x}&= \dfrac{-e^{-x}(1+x^2)-e^{-x}2x}{(1+x^2)^2}\\ &= \dfrac{-e^{-x}(1+x^2+2x)}{(1+x^2)^2}\\ &= \dfrac{-e^{-x}(1+x)^2}{(1+x^2)^2}. \end{align*}\]

We have that

\(e^{-x}, (1+x)^2\)

and

\((1+x^2)^2\)

are all always positive or zero, and thus

\(y'\)

is never positive.

We can see that \(y' = 0 \implies x = -1, y = \dfrac{e}{2}.\)

Since \(y' \leq 0\), we know the function is never-increasing, so this point isn’t a maximum or a minimum, and must be a point of inflection.

To sketch the function, it’s useful to calculate a few more characteristics.

We have that the point \((0,1)\) is on the curve; we know from the question that \(y \to \infty\) as \(x \to -\infty\), and we can see that \(y \to 0\) for \(x \to \infty\).
