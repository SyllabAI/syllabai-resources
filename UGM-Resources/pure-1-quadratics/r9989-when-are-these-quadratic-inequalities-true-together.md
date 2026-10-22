---
created: 2026-10-23T12:00:00 (UTC +06:00)
source: https://undergroundmathematics.org/quadratics/r9989
author: Underground Mathematics (University of Cambridge)
rights: © University of Cambridge (Underground Mathematics). Use inside SyllabAI is authorised by the
  operator attestation of 2026-10-23 — see LICENSE-DATA.md (Amendment 2026-10-23) in this repository.
  Takedown / correction handling as stated in LICENSE-DATA.md.
tags:
- underground-mathematics
- quadratics
- type/review-question
resource_identity:
  ugm_id: r9989
  station: quadratics
  station_title: Quadratics
  resource_type_id: 10
  resource_type_label: Review question
  level: null
  ref: 9989
  old_site_id: Q78
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
  - code: 1.1.3
    provenance:
      tier: AI_SUGGESTED
      confidence: high
      model_version: GLM (Super Z agent, z.ai) — P3c quadratics cross-map (cross-map-quadratics.json @
        syllabai-experimental 915bfa8c)
      evidence: Two quadratic inequalities true together.
      rationale: 'Canonical UGM title: “When are these quadratic inequalities true together?”; exam provenance:
        Oxford (MAT) Specimen 1 Q1G'
      validation_status: SUGGESTED
    title: solve quadratic equations, and quadratic By factorising, completing the square and using the
      inequalities, in one unknown formula.
  mapped_date: '2026-10-23'
  mapper: cross-map-quadratics.json (P3c) @ syllabai-experimental 915bfa8c
  coverage_note: null
provenance:
  capture_date: '2026-10-22'
  capture_tool: P2 full-site crawl (ugm-crawl) → ugm-clean extraction; text-only import
  content_language: en
  exam_reference: Oxford (MAT) Specimen 1 Q1G
task: T-UGM-IMPORT-1
assets:
- path: https://undergroundmathematics.org/quadratics/r9989/images/ineqs.png
  kind: figure
---

# When are these quadratic inequalities true together?

## Question

The inequalities \(x^2 + 3x + 2 > 0\) and \(x^2 + x < 2\) are met by all \(x\) in the region:

1. \(x < -2\);
2. \(-1 < x < 1\);
3. \(x > -1\);
4. \(x > -2\).

## Suggestion

Can we write the quadratic expressions in a more useful form?

What would the inequalities look like on a graph?

## Solution

What happens if we sketch the graphs of \(y = x^2+3x+2\) and \(y = x^2 + x -2\)?

Note that \[x^2 + 3x + 2 = (x+1)(x+2),\] so \(y= 0\) for this curve when \(x = -1\) or \(x=-2\).

Similarly, \[x^2 + x - 2 = (x-1)(x+2)\] so \(y = 0\) for this curve when \(x = 1\) or \(x=-2\).

If we draw a sketch, we can quickly see the regions where each inequality is satisfied.

> [figure: The two graphs x squared + 3 x + 2 and x squared + x minus 2. The solution first inequality is the is the part of the x axis above the first curve, and the second is the part below the second curve, as previously calculated. — `https://undergroundmathematics.org/quadratics/r9989/images/ineqs.png`] (image not included in the text import; path of record).

We need the region where the blue curve is below the \(x\)-axis, **and** where the red curve is above the \(x\)-axis.

We can see that both inequalities are satisfied in the range \(-1 < x < 1\), and the answer is (b).

For this multiple choice question, we could have been even more efficient. The second inequality \(x^2+x<2\) is only met by a finite interval of \(x\) values as the quadratic tends to infinity for large values of \(x\) (either positive or negative). The only option which offers a finite interval of \(x\) values is (b), so this must be the correct answer.
