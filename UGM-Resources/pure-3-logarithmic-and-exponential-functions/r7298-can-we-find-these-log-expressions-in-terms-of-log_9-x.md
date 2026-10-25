---
created: 2026-10-24T22:06:39 (UTC +06:00)
source: https://undergroundmathematics.org/exp-and-log/r7298
author: Underground Mathematics (University of Cambridge)
rights: © University of Cambridge (Underground Mathematics). Use inside SyllabAI is authorised by the
  operator attestation of 2026-10-23 — see LICENSE-DATA.md (Amendment 2026-10-23) in this repository.
  Takedown / correction handling as stated in LICENSE-DATA.md.
tags:
- underground-mathematics
- exp-and-log
- type/review-question
resource_identity:
  ugm_id: r7298
  station: exp-and-log
  station_title: Exponentials & Logarithms
  resource_type_id: 10
  resource_type_label: Review question
  level: null
  ref: 7298
  old_site_id: "Q1043"
spec_map:
  curriculum_code: CIE-9709-P3-2023
  lane: cie-a-level-maths-20-pure-3
  board: Cambridge CIE
  syllabus_version: 2023-2025
  subsection: exp-and-log
  subsection_provenance:
    tier: PROVIDER
    signal: source-url-slug
    slug: exp-and-log
    validation_status: SUGGESTED
  spec_points:
  - code: 3.2.1
    provenance:
      tier: AI_SUGGESTED
      confidence: high
      model_version: "GLM (Super Z agent, z.ai) — P3c lane-10 cross-map (cross-map-log-and-exp.json (P3c lane 10) @ syllabai-experimental 980556af)"
      evidence: "u=log_9 x gives x=9^u 'by definition'; log_9(3x)=1/2+u by the product law; log_x 81 derived from the definition - 'answers may not contain the word log'"
      rationale: "Canonical UGM title: Can we find these log expressions in terms of $\\log_9 x$?"
      validation_status: SUGGESTED
    title: "understand the relationship between logarithms and indices, and use the laws of logarithms (excluding change of base)"
  mapped_date: '2026-10-25'
  mapper: cross-map-log-and-exp.json (P3c lane 10) @ syllabai-experimental 980556af
provenance:
  capture_date: '2026-10-22'
  capture_tool: P2 full-site crawl (ugm-crawl) → ugm-clean extraction; text-only import
  content_language: en
  exam_reference: "UCLES O level Additional Mathematics 2, QP 420/2, 1966, Q5(i)"
  task: T-UGM-IMPORT-10
---

# Can we find these log expressions in terms of $\log_9 x$?

## Question

Given that \(u=\log_9 x\), find, in terms of \(u\):

1. \(x\),

---

1. \(\log_9(3x)\),

---

1. \(\log_x 81\).

(Answers may not contain the word \(\log\).)

## Solution

Given that \(u=\log_9 x\), find, in terms of \(u\)

1. \(x\)

By definition, we have that \(x=9^u\).

Using what we know about the logarithm of a product, we get that \[\log_9(3x)=\log_9 3+\log_9 x=\frac{1}{2}+u.\]

Let’s start by writing \(v=\log_x 81\).

By definition, we see that \(81=x^v\) and so using part (a), \(81=(9^u)^v\).

Since \(9^2=81\), we must have that \(uv=2\), or \(v=2/u\). Therefore, \(\log_x 81=2/u\).
