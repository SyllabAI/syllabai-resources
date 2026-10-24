---
created: 2026-10-25T01:37:17 (UTC +06:00)
source: https://undergroundmathematics.org/polynomials/r5032
author: Underground Mathematics (University of Cambridge)
rights: © University of Cambridge (Underground Mathematics). Use inside SyllabAI is authorised by the
  operator attestation of 2026-10-23 — see LICENSE-DATA.md (Amendment 2026-10-23) in this repository.
  Takedown / correction handling as stated in LICENSE-DATA.md.
tags:
- underground-mathematics
- polynomials
- type/review-question
resource_identity:
  ugm_id: r5032
  station: polynomials
  station_title: Polynomials & Rational Functions
  resource_type_id: 10
  resource_type_label: Review question
  level: null
  ref: 5032
  old_site_id: null
spec_map:
  curriculum_code: CIE-9709-P3-2023
  lane: cie-a-level-maths-20-pure-3
  board: Cambridge CIE
  syllabus_version: 2023-2025
  subsection: polynomials
  subsection_provenance:
    tier: PROVIDER
    signal: source-url-slug
    slug: polynomials
    validation_status: SUGGESTED
  spec_points:
  - code: 3.1.4
    provenance:
      tier: AI_SUGGESTED
      confidence: high
      model_version: "GLM (Super Z agent, z.ai) — P3c lane-9 cross-map (cross-map-algebra.json (P3c lane 9) @ syllabai-experimental 3098d8eb)"
      evidence: "factor-theorem proof that x−1 is a factor of x^m−1 for all positive integers m, powering the deduction that 26ⁿ ends in the same two digits"
      rationale: "Canonical UGM title: Can we prove that $26^n$ always ends in the same two digits?"
      validation_status: SUGGESTED
    title: "use the factor theorem and the remainder theorem"
  mapped_date: '2026-10-25'
  mapper: cross-map-algebra.json (P3c lane 9) @ syllabai-experimental 3098d8eb
provenance:
  capture_date: '2026-10-22'
  capture_tool: P2 full-site crawl (ugm-crawl) → ugm-clean extraction; text-only import
  content_language: en
  exam_reference: "UCLES A level Pure Mathematics 1, QP 9210/1, 1980, Q1(b)"
  task: T-UGM-IMPORT-9
---

# Can we prove that $26^n$ always ends in the same two digits?

## Question

Prove that, for all positive integral values of \(m\), \(x-1\) is a factor of \(x^m - 1\).

Prove that, if \(n\) is an integer greater than \(1\), then \(26^n - 26\) is an odd multiple of \(50\).

Hence, or otherwise, show that, if \(26^n\) is evaluated for any integral value of \(n\) greater than \(1\), then the last two digits of the result are independent of \(n\).

[*The phrase ‘integral values’ means the same as ‘integer values’.* ]

## Solution

By the [factor theorem](https://undergroundmathematics.org/glossary/factor-theorem), a polynomial \(p(x)\) has a linear factor \((x-a)\) if and only if \(p(a) = 0\).

If we take \(m\) to be a positive integer and set \(p(x) = x^m - 1\), then \(p(1) = 1^m - 1 = 0\) and therefore \((x-1)\) is a factor of \(x^m - 1\).

Moreover, we can write \[x^m - 1 = (x-1)(x^{m-1} + \dotsb + 1).\]

As

\(n > 1\)

is an integer, we can write (using the first part of the question)

\[\begin{align*} 26^n - 26 &= 26 \times ( 26^{n-1} - 1 ) \\ &= 26 \times (26 - 1) \times (26^{n-2} + \dotsb +26^1 +1) \\ &= 50 \times 13 \times (26^{n-2} + \dotsb + 26^1 + 1). \end{align*}\]

Since \(26^{n-2} + \dotsb + 26^1\) is an even integer, the bracketed factor is odd, and so \(13\) times the bracketed factor is also odd. That is, \(26^n - 26\) is an odd multiple of \(50\).

We can write \[26^n = \left( 26^n - 26 \right) + 26.\] By the second part of the question (which applies as \(n > 1\) is an integer), as the bracketed term is an odd multiple of \(50\), its final two digits will always be \(50\).

Thus, the final two digits of the right-hand side of the above will be \(76\); this is independent of the value of \(n\).
