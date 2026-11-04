---
created: 2026-11-04T12:00:00 (UTC +06:00)
source: https://undergroundmathematics.org/thinking-about-algebra/r5364
author: Underground Mathematics (University of Cambridge)
rights: © University of Cambridge (Underground Mathematics). Use inside SyllabAI is authorised by the
  operator attestation of 2026-10-23 — see LICENSE-DATA.md (Amendment 2026-10-23) in this repository.
  Takedown / correction handling as stated in LICENSE-DATA.md.
tags:
- underground-mathematics
- thinking-about-algebra
- type/review-question
resource_identity:
  ugm_id: r5364
  station: thinking-about-algebra
  station_title: Thinking about Algebra
  resource_type_id: 10
  resource_type_label: Review question
  level: null
  ref: 5364
  old_site_id: null
spec_map:
  curriculum_code: CIE-IGCSE-0580-2025
  lane: cie-igcse-maths-25-extended
  board: Cambridge CIE
  syllabus_version: 2025-2027
  subsection: thinking-about-algebra
  subsection_provenance:
    tier: PROVIDER
    signal: source-url-slug
    slug: thinking-about-algebra
    validation_status: SUGGESTED
  spec_points:
  - code: E2.3.1
    provenance:
      tier: AI_SUGGESTED
      confidence: high
      model_version: GLM (Super Z agent, z.ai) — the 0580 igcse-extended TE2 cross-map (generalisation
        lane 19) (cross-map-0580-te2-algebra-graphs.json @ syllabai-experimental 79088f34)
      evidence: Simplify these algebraic fractions — the E2.3.1 manipulate-algebraic-fractions register
        verbatim.
      rationale: 'Canonical UGM title: “Can we simplify these algebraic fractions?”; exam provenance:
        O&C O level Elementary Mathematics 1 (Alternative Paper), QP S665, 1956, Q5

        Question reproduced by kind permission of Cambridge Assessment Group Archives. The question remains
        Copyright University of Cambridge Local Examinations Syndicate (“UCLES”),

        All rights reserved

        .'
      validation_status: SUGGESTED
  - code: E2.3.2
    provenance:
      tier: AI_SUGGESTED
      confidence: high
      model_version: GLM (Super Z agent, z.ai) — the 0580 igcse-extended TE2 cross-map (generalisation
        lane 19) (cross-map-0580-te2-algebra-graphs.json @ syllabai-experimental 79088f34)
      evidence: Simplify these algebraic fractions — the E2.3.1 manipulate-algebraic-fractions register
        verbatim.
      rationale: 'Canonical UGM title: “Can we simplify these algebraic fractions?”; exam provenance:
        O&C O level Elementary Mathematics 1 (Alternative Paper), QP S665, 1956, Q5

        Question reproduced by kind permission of Cambridge Assessment Group Archives. The question remains
        Copyright University of Cambridge Local Examinations Syndicate (“UCLES”),

        All rights reserved

        .'
      validation_status: SUGGESTED
  mapped_date: '2026-11-04'
  mapper: cross-map-0580-te2-algebra-graphs.json (P3c) @ syllabai-experimental 79088f34
  coverage_note: null
provenance:
  capture_date: '2026-10-22'
  capture_tool: P2 full-site crawl (ugm-crawl) → ugm-clean extraction; text-only import
  content_language: en
  exam_reference: 'O&C O level Elementary Mathematics 1 (Alternative Paper), QP S665, 1956, Q5

    Question reproduced by kind permission of Cambridge Assessment Group Archives. The question remains
    Copyright University of Cambridge Local Examinations Syndicate (“UCLES”),

    All rights reserved

    .'
task: T-UGM-IMPORT-19
---

# Can we simplify these algebraic fractions?

## Question

Simplify the expression \[ \frac{1}{x^2 - x} - \frac{1}{x^3 - x}. \]

Find for what values of \(x\) this expression is equal to \(1\).

## Solution

Each denominator has a factor

\(x\)

, so we can write

\[ \frac{1}{x^2 - x} - \frac{1}{x^3 - x} = \frac{1}{x(x-1)} - \frac{1}{x(x^2-1)}. \]

Next, we can write

\(x^2 - 1 = (x-1)(x+1)\)

, and so

\[\begin{align*} \frac{1}{x(x-1)} - \frac{1}{x(x^2-1)} &= \frac{1}{x(x-1)} - \frac{1}{x(x-1)(x+1)} \\ &= \frac{x+1}{x(x-1)(x+1)} - \frac{1}{x(x-1)(x+1)} \\ &= \frac{x}{x(x-1)(x+1)} \\ &= \frac{1}{(x-1)(x+1)}. \end{align*}\]

We know that \(x\) is not \(0, 1\) or \(-1\), since in these cases, the question makes no sense.

By using the simplified form we found above, this is equivalent to asking us to find the values of

\(x\)

for which

\[ \frac{1}{(x-1)(x+1)} = 1. \]

By rearranging, we have that

\[\begin{align*} 1 = (x-1)(x+1) &\iff 1 = x^2 - 1 \\ &\iff x^2 - 2 = 0 \\ &\iff x = \pm\sqrt{2}. \end{align*}\]
