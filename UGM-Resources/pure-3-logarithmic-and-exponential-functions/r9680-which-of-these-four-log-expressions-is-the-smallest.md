---
created: 2026-10-24T22:06:39 (UTC +06:00)
source: https://undergroundmathematics.org/exp-and-log/r9680
author: Underground Mathematics (University of Cambridge)
rights: © University of Cambridge (Underground Mathematics). Use inside SyllabAI is authorised by the
  operator attestation of 2026-10-23 — see LICENSE-DATA.md (Amendment 2026-10-23) in this repository.
  Takedown / correction handling as stated in LICENSE-DATA.md.
tags:
- underground-mathematics
- exp-and-log
- type/review-question
resource_identity:
  ugm_id: r9680
  station: exp-and-log
  station_title: Exponentials & Logarithms
  resource_type_id: 10
  resource_type_label: Review question
  level: null
  ref: 9680
  old_site_id: "Q153"
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
      evidence: "L=log_10 pi substitution rewrites all four candidates via the laws (log_10(pi^2)=2L, 1/log_10(sqrt(pi))=2/L) and index comparisons"
      rationale: "Canonical UGM title: Which of these four log expressions is the smallest?"
      validation_status: SUGGESTED
    title: "understand the relationship between logarithms and indices, and use the laws of logarithms (excluding change of base)"
  mapped_date: '2026-10-25'
  mapper: cross-map-log-and-exp.json (P3c lane 10) @ syllabai-experimental 980556af
provenance:
  capture_date: '2026-10-22'
  capture_tool: P2 full-site crawl (ugm-crawl) → ugm-clean extraction; text-only import
  content_language: en
  exam_reference: "Oxford University Mathematics Aptitude Test, 2008, Q1B"
  task: T-UGM-IMPORT-10
---

# Which of these four log expressions is the smallest?

## Question

Which is the smallest of these values?

1. \(\log_{10}\pi\),

---

1. \(\sqrt{\log_{10}(\pi^2)}\),

---

1. \(\left(\dfrac{1}{\log_{10}\pi}\right)^3\),

---

1. \(\dfrac{1}{\log_{10}\sqrt{\pi}}\).

## Suggestion

Can we rewrite the expressions using the laws of logs and indices? Is the substitution \(L = \log_{10}\pi\) helpful to us?

## Solution

Let \(L = \log_{10}\pi\). Since \(\pi < 10\), we have \(L < 1\). Then

1. \(\log_{10}\pi = L\);

---

1. \(\sqrt{\log_{10}(\pi^2)}= \sqrt{2\log_{10}\pi} = \sqrt{2L} > \sqrt{L \times L} = L\);

---

1. \(\left(\dfrac{1}{\log_{10}\pi}\right)^3 = L^{-3} > 1\);

---

1. \(\dfrac{1}{\log_{10}\sqrt{\pi}} = \dfrac{1}{\dfrac{1}{2}\log_{10}\pi} = \dfrac{2}{L} > 2\).

So the smallest value is \(L\), and the answer is (a).
