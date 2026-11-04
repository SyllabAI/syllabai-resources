---
created: 2026-11-04T12:00:00 (UTC +06:00)
source: https://undergroundmathematics.org/thinking-about-algebra/r9160
author: Underground Mathematics (University of Cambridge)
rights: © University of Cambridge (Underground Mathematics). Use inside SyllabAI is authorised by the
  operator attestation of 2026-10-23 — see LICENSE-DATA.md (Amendment 2026-10-23) in this repository.
  Takedown / correction handling as stated in LICENSE-DATA.md.
tags:
- underground-mathematics
- thinking-about-algebra
- type/review-question
resource_identity:
  ugm_id: r9160
  station: thinking-about-algebra
  station_title: Thinking about Algebra
  resource_type_id: 10
  resource_type_label: Review question
  level: null
  ref: 9160
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
  - code: E2.4.2
    provenance:
      tier: AI_SUGGESTED
      confidence: medium
      model_version: GLM (Super Z agent, z.ai) — the 0580 igcse-extended TE2 cross-map (generalisation
        lane 19) (cross-map-0580-te2-algebra-graphs.json @ syllabai-experimental 79088f34)
      evidence: Given power facts, show z^6=cx — index-law manipulation; E2.4.2 register.
      rationale: 'Canonical UGM title: “Given these power facts, can we show $z^6=cx$?”; exam provenance:
        O&C O level Additional Mathematics 2, 1967, Q2(ii)

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
  exam_reference: 'O&C O level Additional Mathematics 2, 1967, Q2(ii)

    Question reproduced by kind permission of Cambridge Assessment Group Archives. The question remains
    Copyright University of Cambridge Local Examinations Syndicate (“UCLES”),

    All rights reserved

    .'
task: T-UGM-IMPORT-19
---

# Given these power facts, can we show $z^6=cx$?

## Question

If \(x = ay^{\frac{3}{4}}\) and \(z = b \sqrt{(y/x)}\), prove that \(z^6 = cx\), where \(c\) is independent of \(x\), \(y\) and \(z\), stating the value of \(c\) in terms of \(a\) and \(b\).

## Solution

The rules of indices include

\[(pq)^r = p^rq^r\] \[(p^q)^r = p^{qr}\] \[p^qp^r = p^{q+r}\]

We will apply these rules repeatedly here. We have that

\[z = b \sqrt{y/x} \implies z = b x^{-1/2}y^{1/2} \implies z^6 = b^6y^3x^{-3}.\]

We also have that

\[x = ay^{3/4} \implies x^4=a^4y^3 \implies y^3 = x^4a^{-4}.\]

So \(z^6 = b^6a^{-4}x^4x^{-3} = b^6a^{-4}x\), and so \(c = \dfrac{b^6}{a^4}.\)
