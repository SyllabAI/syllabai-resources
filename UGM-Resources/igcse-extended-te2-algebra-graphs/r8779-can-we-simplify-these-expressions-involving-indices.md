---
created: 2026-11-04T12:00:00 (UTC +06:00)
source: https://undergroundmathematics.org/thinking-about-algebra/r8779
author: Underground Mathematics (University of Cambridge)
rights: © University of Cambridge (Underground Mathematics). Use inside SyllabAI is authorised by the
  operator attestation of 2026-10-23 — see LICENSE-DATA.md (Amendment 2026-10-23) in this repository.
  Takedown / correction handling as stated in LICENSE-DATA.md.
tags:
- underground-mathematics
- thinking-about-algebra
- type/review-question
resource_identity:
  ugm_id: r8779
  station: thinking-about-algebra
  station_title: Thinking about Algebra
  resource_type_id: 10
  resource_type_label: Review question
  level: null
  ref: 8779
  old_site_id: Q4026
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
  - code: E2.4.2
    provenance:
      tier: AI_SUGGESTED
      confidence: high
      model_version: GLM (Super Z agent, z.ai) — the 0580 igcse-extended TE2 cross-map (generalisation
        lane 19) (cross-map-0580-te2-algebra-graphs.json @ syllabai-experimental 79088f34)
      evidence: Simplify these expressions involving indices — the E2.4.2 register verbatim.
      rationale: 'Canonical UGM title: “Can we simplify  these expressions involving indices?”; exam provenance:
        UCLES O level Mathematics Alternative A Algebra, QP 450/3, 1973, Q6(ii)

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
  exam_reference: 'UCLES O level Mathematics Alternative A Algebra, QP 450/3, 1973, Q6(ii)

    Question reproduced by kind permission of Cambridge Assessment Group Archives. The question remains
    Copyright University of Cambridge Local Examinations Syndicate (“UCLES”),

    All rights reserved

    .'
task: T-UGM-IMPORT-19
---

# Can we simplify  these expressions involving indices?

## Question

Given that \(p=24\) and \(q=-16\), simplify

1. \(\dfrac{x^px^q}{x^7}\),
2. \((x^2)^p(x^3)^q\).

## Suggestion

Notice that all the powers in these expressions have the same base, namely \(x\). How do we combine powers when multiplying, dividing, etc?

## Solution

There are three identities we need for this question, namely \[ x^ax^b = x^{a+b},\qquad \frac{x^a}{x^b} = x^{a-b},\qquad \left( x^a \right)^b = x^{ab}. \]

Applying them to \((a)\) we find

\[\begin{align*} \frac{x^px^q}{x^7}&=\frac{x^{p+q}}{x^7}\\ &=x^{p+q-7}\\ &=x^{1}=x. \end{align*}\]

For \((b)\) we have

\[\begin{align*} \left(x^2 \right)^p \left(x^3 \right)^q &= x^{2p}x^{3q}\\ &=x^{2p+3q} \\ &= x^0=1. \end{align*}\]
