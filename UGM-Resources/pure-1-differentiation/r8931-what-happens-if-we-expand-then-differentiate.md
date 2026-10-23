---
created: 2026-10-24T01:49:53 (UTC +06:00)
source: https://undergroundmathematics.org/calculus-of-powers/r8931
author: Underground Mathematics (University of Cambridge)
rights: © University of Cambridge (Underground Mathematics). Use inside SyllabAI is authorised by the
  operator attestation of 2026-10-23 — see LICENSE-DATA.md (Amendment 2026-10-23) in this repository.
  Takedown / correction handling as stated in LICENSE-DATA.md.
tags:
- underground-mathematics
- calculus-of-powers
- type/review-question
resource_identity:
  ugm_id: r8931
  station: calculus-of-powers
  station_title: Calculus of Powers
  resource_type_id: 10
  resource_type_label: Review question
  level: null
  ref: 8931
  old_site_id: Q240
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
  exam_reference: Oxford University Mathematics Aptitude Test, 2013, Q1E
task: T-UGM-IMPORT-7
---

# What happens if we expand, then differentiate?

## Question

The expression \[\frac{d^2}{dx^2}\bigl[(2x-1)^4(1-x)^5\bigr] + \frac{d}{dx}\bigl[(2x+1)^4(3x^2-2)^2\bigr]\] is a polynomial of degree

1. \(9\);

---

1. \(8\);

---

1. \(7\);

---

1. less than \(7\).

## Solution

Let’s observe that

1. multiplying two polynomials of degrees \(p\) and \(q\) gives a polynomial of degree \(p+q\), and

---

1. differentiating a polynomial of degree \(p\) gives a polynomial of degree \(p-1\).

From this we can quickly see that the expression in the question is a sum of two polynomials, each of degree 7.

Does this mean their sum has to be a polynomial of degree 7 too?

Yes, unless the leading terms of the two expressions cancel when you add them together.

So what are our leading terms here?

The expression \((2x-1)^4(1-x)^5\) gives first term \((2x)^4(-x)^5=-16x^9\), which differentiates twice to \[-9 \times 8 \times 16 x^7.\]

The leading term of the expression \((2x+1)^4(3x^2-2)^2\) is \((2x)^4(3x^2)^2=16 \times 9x^8\), which differentiates to \[16 \times 9 \times 8x^7.\]

So in fact the two leading terms here DO cancel, and we’re left with a polynomial of degree less than \(7\), so the answer is (d).
