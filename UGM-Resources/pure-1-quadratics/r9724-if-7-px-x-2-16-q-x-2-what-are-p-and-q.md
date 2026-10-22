---
created: 2026-10-23T12:00:00 (UTC +06:00)
source: https://undergroundmathematics.org/quadratics/r9724
author: Underground Mathematics (University of Cambridge)
rights: © University of Cambridge (Underground Mathematics). Use inside SyllabAI is authorised by the
  operator attestation of 2026-10-23 — see LICENSE-DATA.md (Amendment 2026-10-23) in this repository.
  Takedown / correction handling as stated in LICENSE-DATA.md.
tags:
- underground-mathematics
- quadratics
- type/review-question
resource_identity:
  ugm_id: r9724
  station: quadratics
  station_title: Quadratics
  resource_type_id: 10
  resource_type_label: Review question
  level: null
  ref: 9724
  old_site_id: Q3014
spec_map:
  curriculum_code: CIE-9709-P1-2023
  lane: cie-a-level-maths-20-pure-1
  board: Cambridge CIE
  syllabus_version: 2023-2025
  subsection: quadratics
  subsection_provenance:
    tier: PROVIDER
    signal: source-url-slug
    slug: quadratics
    validation_status: SUGGESTED
  spec_points:
  - code: 1.1.1
    provenance:
      tier: AI_SUGGESTED
      confidence: high
      model_version: GLM (Super Z agent, z.ai) — P3c quadratics cross-map (cross-map-quadratics.json @
        syllabai-experimental 915bfa8c)
      evidence: Identity comparison after completing the square.
      rationale: 'Canonical UGM title: “If $7 - px - x^2 = 16 - (q + x)^2$, what are $p$ and $q$?”; exam
        provenance: UCLES 1980 Q13'
      validation_status: SUGGESTED
    title: carry out the process of completing the square for a quadratic polynomial ax + bx + c and use
      y a completed square form
  mapped_date: '2026-10-23'
  mapper: cross-map-quadratics.json (P3c) @ syllabai-experimental 915bfa8c
  coverage_note: null
provenance:
  capture_date: '2026-10-22'
  capture_tool: P2 full-site crawl (ugm-crawl) → ugm-clean extraction; text-only import
  content_language: en
  exam_reference: UCLES 1980 Q13
task: T-UGM-IMPORT-1
---

# If $7 - px - x^2 = 16 - (q + x)^2$, what are $p$ and $q$?

## Question

Given that \(y = 7 - px - x^2 = 16 - (q + x)^2\) for all values of \(x\), where \(p\) and \(q\) are both positive,

1. calculate the values of \(p\) and \(q\),
2. state the maximum value of \(y\) and the value of \(x\) at which it occurs,
3. find the range of values of \(x\) for which \(y\) is positive.

## Solution

By expanding the equation \[ 7 - px - x^2 = 16 - (q + x)^2, \] we arrive at the equation \[ 7 - px - x^2 = 16 - q^2 - 2qx - x^2. \] Since this is true for all \(x\), we can equate coefficients, giving \(7 = 16 - q^2\) and \(-p = -2q\).

Thus \(q^2=9\). Since the question tells us that \(p\) and \(q\) are both positive, we must have \(q=3\), so \(p=6\).

Thus \(y=7-6x-x^2=16-(3+x)^2\).

As \(y = 16 - (3 + x)^2\), we see that the maximum value of \(y\) is \(16\), and this occurs when \(x = -3\).

(This is because \((3 + x)^2 \ge 0\) no matter what the value of \(x\), so \(y\) is maximised when \((3 + x)^2=0\).)

Again, the second representation is useful here: \(y\) is positive when \(16 - (3 + x)^2 > 0\), that is, when \((3 + x)^2 < 16\). This gives \(-4 < 3 + x < 4\), so \(-7<x<1\).

Alternatively, we can use the first representation, \(y=7-6x-x^2=-(x^2+6x-7)=-(x-1)(x+7)\). This is zero when \(x=1\) or \(x=-7\). As this is a “vertex-up” parabola (since the coefficient of \(x^2\) is negative), \(y>0\) when \(-7<x<1\).
