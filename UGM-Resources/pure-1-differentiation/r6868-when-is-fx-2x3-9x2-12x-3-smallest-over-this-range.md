---
created: 2026-10-24T01:49:53 (UTC +06:00)
source: https://undergroundmathematics.org/calculus-meets-functions/r6868
author: Underground Mathematics (University of Cambridge)
rights: © University of Cambridge (Underground Mathematics). Use inside SyllabAI is authorised by the
  operator attestation of 2026-10-23 — see LICENSE-DATA.md (Amendment 2026-10-23) in this repository.
  Takedown / correction handling as stated in LICENSE-DATA.md.
tags:
- underground-mathematics
- calculus-meets-functions
- type/review-question
resource_identity:
  ugm_id: r6868
  station: calculus-meets-functions
  station_title: Calculus meets Functions
  resource_type_id: 10
  resource_type_label: Review question
  level: null
  ref: 6868
  old_site_id: Q97
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
      evidence: smallest value of 2x^3-9x^2+12x+3 on 0<=x<=2 — stationary points plus endpoint comparison
      rationale: 'Canonical UGM title: "When is $f(x) = 2x^3 − 9x^2 + 12x + 3$ smallest over this range?";
        exam provenance: Oxford University Mathematics Aptitude Test, None, Q1B'
      validation_status: SUGGESTED
    title: use the derivative of x (for any rational n ), together with constant multiples, sums and
      differences of functions, and of composite functions using the chain rule
  - code: 1.7.4
    provenance:
      tier: AI_SUGGESTED
      confidence: high
      model_version: GLM (Super Z agent, z.ai) — P3c lane-7 cross-map (cross-map-differentiation.json
        (P3c lane 7) @ syllabai-experimental 93575e69)
      evidence: smallest value of 2x^3-9x^2+12x+3 on 0<=x<=2 — stationary points plus endpoint comparison
      rationale: 'Canonical UGM title: "When is $f(x) = 2x^3 − 9x^2 + 12x + 3$ smallest over this range?";
        exam provenance: Oxford University Mathematics Aptitude Test, None, Q1B'
      validation_status: SUGGESTED
    title: locate stationary points and determine their nature, and use information about stationary
      points in sketching graphs.
  mapped_date: '2026-10-24'
  mapper: cross-map-differentiation.json (P3c lane 7) @ syllabai-experimental 93575e69
provenance:
  capture_date: '2026-10-22'
  capture_tool: P2 full-site crawl (ugm-crawl) → ugm-clean extraction; text-only import
  content_language: en
  exam_reference: Oxford University Mathematics Aptitude Test, None, Q1B
task: T-UGM-IMPORT-7
---

# When is $f(x) = 2x^3 − 9x^2 + 12x + 3$ smallest over this range?

## Question

The smallest value of the function \[f(x) = 2x^3 − 9x^2 + 12x + 3\] in the range \(0 \leq x \leq 2\) is

1. \(1\),

---

1. \(3\),

---

1. \(5\),

---

1. \(7\).

## Suggestion

Could we see ‘the smallest value’ as ‘the minimum value’?

How do we find the minimum values of a function?

Could we sketch the graph of \(y = f(x)\)?

## Solution

The smallest value will occur either at a stationary point of \(f(x)\), or at one of the endpoints of the range, \(x = 0\) or \(x = 2\).

To find stationary points, we solve \(f'(x) = 6x^2 - 18x + 12 = 0\), or equivalently \(0 =x^2 - 3x + 2 = (x - 1)(x - 2)\).

So \(x = 1\) and \(x = 2\) are the stationary points of \(f(x)\), and are in the desired range. From our knowledge of the shape of cubics, or from looking at \(f''(x)\), we know that \(x = 1\) is a maximum and \(x = 2\) is a minimum.

Then the minimum value of

\(f(x)\)

is either at

\(x = 2\)

or

\(x = 0\)

, so we can check the values. We have

\[\begin{align*} f(2) &= 16 - 36 + 24 + 3 = 7 \\ f(0) &= 3. \end{align*}\]

So the minimum value of \(f(x)\) for \(0 \leq x \leq 2\) is \(3\), and the answer is (b).
