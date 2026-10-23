---
created: 2026-10-23T21:23:05 (UTC +06:00)
source: https://undergroundmathematics.org/thinking-about-algebra/r9404
author: Underground Mathematics (University of Cambridge)
rights: © University of Cambridge (Underground Mathematics). Use inside SyllabAI is authorised by the
  operator attestation of 2026-10-23 — see LICENSE-DATA.md (Amendment 2026-10-23) in this repository.
  Takedown / correction handling as stated in LICENSE-DATA.md.
tags:
- underground-mathematics
- thinking-about-algebra
- type/review-question
resource_identity:
  ugm_id: r9404
  station: thinking-about-algebra
  station_title: Thinking about Algebra
  resource_type_id: 10
  resource_type_label: Review question
  level: null
  ref: 9404
  old_site_id: null
spec_map:
  curriculum_code: CIE-9709-P1-2023
  lane: cie-a-level-maths-20-pure-1
  board: Cambridge CIE
  syllabus_version: 2023-2025
  subsection: thinking-about-algebra
  subsection_provenance:
    tier: PROVIDER
    signal: source-url-slug
    slug: thinking-about-algebra
    validation_status: SUGGESTED
  spec_points:
  - code: 1.6.1
    provenance:
      tier: AI_SUGGESTED
      confidence: medium
      model_version: GLM (Super Z agent, z.ai) — P3c lane-6 cross-map (cross-map-series.json (P3c lane
        6) @ syllabai-experimental 82964ce4)
      evidence: all three solution routes run through binomial expansions of (x±y)^6 (factorisation
        is the wrapper)
      rationale: 'Canonical UGM title: "Can we factorise  $(x+y)^6 - (x-y)^6$ completely?"; exam provenance:
        UCLES A level Mathematics A 1, 1979, Q3(a)'
      validation_status: SUGGESTED
    title: use the expansion of ( a + b ) , where n is a positive integer
  mapped_date: '2026-10-23'
  mapper: cross-map-series.json (P3c lane 6) @ syllabai-experimental 82964ce4
provenance:
  capture_date: '2026-10-22'
  capture_tool: P2 full-site crawl (ugm-crawl) → ugm-clean extraction; text-only import
  content_language: en
  exam_reference: UCLES A level Mathematics A 1, 1979, Q3(a)
task: T-UGM-IMPORT-6
---

# Can we factorise  $(x+y)^6 - (x-y)^6$ completely?

## Question

Factorise completely

\[\begin{equation*} (x+y)^6 - (x-y)^6. \end{equation*}\]

## Suggestion

Can we factorise simpler things? \(6=2\times3\), so how about thinking about \(a^2-b^2\)? Or \(a^3 - b^3\)? Or even \(a^3 + b^3\)?

Or else we might wonder if, while it’s usually a bad idea, it’s worth trying to expand…

## Solution

Since \(6=2\times3\), we can think of this expression as \(((x+y)^2)^3-((x-y)^2)^3\) or as \(((x+y)^3)^2-((x-y)^3)^2\).

There are then several identities that are helpful to us here:

1. \(a^2-b^2 = (a+b)(a-b)\),

---

1. \(a^3-b^3 = (a-b)(a^2+ab+b^2)\),

---

1. \(a^3+b^3 = (a+b)(a^2-ab+b^2)\),

---

1. \((a+b)^3 = a^3+3a^2b+3ab^2+b^3\),

---

1. \((a-b)^3 = a^3-3a^2b+3ab^2-b^3\).

We can check these identities by multiplying out the brackets. Identities (4) and (5) are examples of the [binomial theorem](https://undergroundmathematics.org/glossary/binomial-theorem).

If we start with \((x+y)^6-(x-y)^6=((x+y)^3)^2-((x-y)^3)^2\), we can use (1) to get \[(x+y)^6 - (x-y)^6 = \bigl((x+y)^3-(x-y)^3\bigr)\bigl((x+y)^3+(x-y)^3\bigr).\]

Now we can expand the inner brackets using the binomial theorem to get

\[\begin{align*} (x+y)^6 - (x-y)^6 &= \bigl((x^3+3x^2y+3xy^2+y^3)-(x^3-3x^2y+3xy^2-y^3)\bigr)\\ &\qquad\times \bigl((x^3+3x^2y+3xy^2+y^3)+(x^3-3x^2y+3xy^2-y^3)\bigr)\\ &= (6x^2y+2y^3)(2x^3+6xy^2)\\ &= 4xy(3x^2+y^2)(x^2+3y^2). \end{align*}\]

We cannot factorise this any further, as each bracket is the sum of two squares.

Alternatively, if we start with \((x+y)^6-(x-y)^6=((x+y)^2)^3-((x-y)^2)^3\), we can use (2) to get \[(x+y)^6 - (x-y)^6 = \bigl((x+y)^2-(x-y)^2\bigr)\bigl((x+y)^4+(x+y)^2(x-y)^2+(x-y)^4\bigr).\]

Expanding the inner brackets using the binomial theorem and then simplifying will eventually give the same result, but it seems like a lot more work.

As a third route, we can simply expand the brackets in

\((x+y)^6 - (x-y)^6\)

directly using the

binomial theorem

. We have

\[\begin{align*} (x+y)^6 &= x^6 + \binom{6}{1} x^5y + \dotsb + \binom{6}{5} xy^5 + y^6\\ &= x^6 + 6x^5y + 15x^4y^2 + 20x^3y^3 + 15x^2y^4 + 6xy^5 + y^6\\ (x-y)^6 &= x^6 - 6x^5y + 15x^4y^2 - 20x^3y^3 + 15x^2y^4 - 6xy^5 + y^6, \end{align*}\]

so that

\[\begin{align*} (x+y)^6 - (x-y)^6 &= 12x^5y + 40x^3y^3 + 12xy^5 \\ &= 4xy(3x^4+10x^2y^2+3y^4)\\ &= 4xy(x^2+3y^2)(3x^2+y^2). \end{align*}\]
