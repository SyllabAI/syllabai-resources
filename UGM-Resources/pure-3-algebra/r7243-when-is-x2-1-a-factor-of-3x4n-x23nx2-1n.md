---
created: 2026-10-25T01:37:17 (UTC +06:00)
source: https://undergroundmathematics.org/polynomials/r7243
author: Underground Mathematics (University of Cambridge)
rights: © University of Cambridge (Underground Mathematics). Use inside SyllabAI is authorised by the
  operator attestation of 2026-10-23 — see LICENSE-DATA.md (Amendment 2026-10-23) in this repository.
  Takedown / correction handling as stated in LICENSE-DATA.md.
tags:
- underground-mathematics
- polynomials
- type/review-question
resource_identity:
  ugm_id: r7243
  station: polynomials
  station_title: Polynomials & Rational Functions
  resource_type_id: 10
  resource_type_label: Review question
  level: null
  ref: 7243
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
      evidence: "x²+1 | (3+x⁴)ⁿ−(x²+3)ⁿ(x²−1)ⁿ resolved by the factor theorem on the composed polynomial f(x²) at x²=−1 (complex-root route noted)"
      rationale: "Canonical UGM title: When is $x^2 +1$ a factor of  $(3+x^4)^n-(x^2+3)^n(x^2-1)^n$?"
      validation_status: SUGGESTED
    title: "use the factor theorem and the remainder theorem"
  mapped_date: '2026-10-25'
  mapper: cross-map-algebra.json (P3c lane 9) @ syllabai-experimental 3098d8eb
provenance:
  capture_date: '2026-10-22'
  capture_tool: P2 full-site crawl (ugm-crawl) → ugm-clean extraction; text-only import
  content_language: en
  exam_reference: "Oxford University Mathematics Aptitude Test, 2016, Q1F"
  task: T-UGM-IMPORT-9
---

# When is $x^2 +1$ a factor of  $(3+x^4)^n-(x^2+3)^n(x^2-1)^n$?

## Question

Let \(n\) be a positive integer. Then \(x^2 +1\) is a factor of

\[(3+x^4)^n-(x^2+3)^n(x^2-1)^n\]

for

1. all \(n\);

---

1. even \(n\);

---

1. odd \(n\);

---

1. \(n \geq 3\);

---

1. no values of \(n\).

## Suggestion

What ideas can we use if we know \(x^2+1\) is a factor?

What is the same and what is different about this question compared to other polynomial factorisation questions?

## Solution

Note that the polynomial is a function of \(x^2\).

Therefore, let the polynomial \((3+x^4)^n-(x^2+3)^n(x^2-1)^n = f(x^2)\).

From the [factor theorem](https://undergroundmathematics.org/glossary/factor-theorem) we know that if \(x^2+1\) is a factor of \(f(x^2)\), then \(f(-1) = 0\).

This gives:

\[(3+1)^n-(-1+3)^n(-1-1)^n = 4^n - (-1)^n4^n.\]

This is zero if and only if \(n\) is even, and so the factor theorem tells us the answer is (b).

If we know about complex numbers, we can say the solution to \(x^2 +1 = 0\) is \(x = i, -i.\)

Putting either of these values into \((3+x^4)^n-(x^2+3)^n(x^2-1)^n\) for \(x\) gives us \(4^n - (-1)^n4^n\), as before.
