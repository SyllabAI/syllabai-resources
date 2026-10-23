---
created: 2026-10-24T01:49:53 (UTC +06:00)
source: https://undergroundmathematics.org/calculus-of-powers/r7724
author: Underground Mathematics (University of Cambridge)
rights: © University of Cambridge (Underground Mathematics). Use inside SyllabAI is authorised by the
  operator attestation of 2026-10-23 — see LICENSE-DATA.md (Amendment 2026-10-23) in this repository.
  Takedown / correction handling as stated in LICENSE-DATA.md.
tags:
- underground-mathematics
- calculus-of-powers
- type/review-question
resource_identity:
  ugm_id: r7724
  station: calculus-of-powers
  station_title: Calculus of Powers
  resource_type_id: 10
  resource_type_label: Review question
  level: null
  ref: 7724
  old_site_id: null
spec_map:
  curriculum_code: CIE-9709-P1-2023
  lane: cie-a-level-maths-20-pure-1
  board: Cambridge CIE
  syllabus_version: 2023-2025
  subsection: calculus-of-powers
  subsection_provenance:
    tier: PROVIDER
    signal: source-url-slug
    slug: calculus-of-powers
    validation_status: SUGGESTED
  spec_points: []
  coverage_note: 'no CIE P1 spec point asserted — resource remains in the corpus unmapped (AGENT.md
    rule 3: coverage is never manufactured)'
  mapped_date: '2026-10-24'
  mapper: cross-map-differentiation.json (P3c lane 7) @ syllabai-experimental 93575e69
provenance:
  capture_date: '2026-10-22'
  capture_tool: P2 full-site crawl (ugm-crawl) → ugm-clean extraction; text-only import
  content_language: en
  exam_reference: O&C O level Additional Mathematics 2, 1968, Q8
task: T-UGM-IMPORT-7
---

# Can we explain why this integral is zero?

## Question

The curve \(y = 4(x+1)(x-1)(x-3)\) meets the \(x\)-axis at three points. Verify, by finding the numerical value of each, that the two areas formed between the curve and the \(x\)-axis are of equal size.

Explain why the value of \(\displaystyle \int_{-1}^3 y \:dx\) is zero.

## Solution

The three intercepts with the \(x\)-axis are at \(x = -1\), \(x = 1\), and \(x = 3\).

The curve has a positive \(x^3\) coefficient, so we know the rough shape of the curve. The region enclosed between the curve and the \(x\)-axis between \(x = -1\) and \(x = 1\) is above the \(x\)-axis, while the region enclosed between \(x = 1\) and \(x = 3\) is below the \(x\)-axis.

We can expand the expression that defines

\(y\)

:

\[\begin{align*} y = 4(x+1)(x-1)(x-3) &= 4(x^2 - 1)(x-3) \\ &= 4(x^3 - 3x^2 - x + 3). \end{align*}\]

The first area is

\[\begin{equation*} \int_{-1}^1 y \:dx = 4 \int_{-1}^1 x^3 - 3x^2 - x + 3 \:dx = \left[ x^4 - 4x^3 - 2x^2 + 12x \right]_{-1}^{1} = (7)-(-9) = 16. \end{equation*}\]

We can find the second area by evaluating

\[\begin{align*} \left[ x^4 - 4x^3 - 2x^2 + 12x \right]_{1}^{3} = -16. \end{align*}\]

This is negative since the curve lies beneath the \(x\)-axis here. Hence the value of the second area is \(16\), and the magnitudes of the two areas are equal, as required.

We can split

\[\begin{equation*} \int_{-1}^3 y \:dx = \int_{-1}^1 y \:dx + \int_1^3 y \:dx. \end{equation*}\]

We have seen that the two integrals are equal in magnitude, but opposite in sign (as the second region lies below the \(x\)-axis), and so the above quantity vanishes.
