---
created: 2026-10-24T01:49:53 (UTC +06:00)
source: https://undergroundmathematics.org/calculus-meets-functions/r8588
author: Underground Mathematics (University of Cambridge)
rights: © University of Cambridge (Underground Mathematics). Use inside SyllabAI is authorised by the
  operator attestation of 2026-10-23 — see LICENSE-DATA.md (Amendment 2026-10-23) in this repository.
  Takedown / correction handling as stated in LICENSE-DATA.md.
tags:
- underground-mathematics
- calculus-meets-functions
- type/review-question
resource_identity:
  ugm_id: r8588
  station: calculus-meets-functions
  station_title: Calculus meets Functions
  resource_type_id: 10
  resource_type_label: Review question
  level: null
  ref: 8588
  old_site_id: Q227
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
      confidence: medium
      model_version: GLM (Super Z agent, z.ai) — P3c lane-7 cross-map (cross-map-differentiation.json
        (P3c lane 7) @ syllabai-experimental 93575e69)
      evidence: f'(x)=g(x+1), g'(x)=h(x-1) => f''(2x)=h(2x) — translation-chain differentiation and
        second-derivative notation bookkeeping
      rationale: 'Canonical UGM title: "Given $f''(x)$ and $g''(x)$, what is $f''''(2x)$?"; exam provenance:
        Oxford University Mathematics Aptitude Test, 2013, Q1C'
      validation_status: SUGGESTED
    title: use the derivative of x (for any rational n ), together with constant multiples, sums and
      differences of functions, and of composite functions using the chain rule
  mapped_date: '2026-10-24'
  mapper: cross-map-differentiation.json (P3c lane 7) @ syllabai-experimental 93575e69
provenance:
  capture_date: '2026-10-22'
  capture_tool: P2 full-site crawl (ugm-crawl) → ugm-clean extraction; text-only import
  content_language: en
  exam_reference: Oxford University Mathematics Aptitude Test, 2013, Q1C
task: T-UGM-IMPORT-7
---

# Given $f'(x)$ and $g'(x)$, what is $f''(2x)$?

## Question

The functions \(f\), \(g\) and \(h\) are related by \[f'(x) = g(x+1), \qquad g'(x)=h(x-1).\] It follows that \(f''(2x)\) equals

1. \(h(2x+1)\);

---

1. \(2h'(2x)\);

---

1. \(h(2x)\);

---

1. \(4h(2x)\).

## Solution

Differentiating the first expression gives \[f''(x) = g'(x+1).\] Then by replacing \(x\) with \(x+1\) in the second expression, we have \[g'(x+1)=h(x)\] and so \[f''(x)=h(x).\] Finally, if we replace \(x\) with \(2x\), we have \[f''(2x)=h(2x)\] and so the answer is (c).

You might want to look at [A tricky derivative](https://undergroundmathematics.org/calculus-meets-functions/tricky-derivative) for more on this problem.
