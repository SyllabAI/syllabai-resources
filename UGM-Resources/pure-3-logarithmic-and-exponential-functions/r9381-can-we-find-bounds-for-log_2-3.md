---
created: 2026-10-24T22:06:39 (UTC +06:00)
source: https://undergroundmathematics.org/exp-and-log/r9381
author: Underground Mathematics (University of Cambridge)
rights: © University of Cambridge (Underground Mathematics). Use inside SyllabAI is authorised by the
  operator attestation of 2026-10-23 — see LICENSE-DATA.md (Amendment 2026-10-23) in this repository.
  Takedown / correction handling as stated in LICENSE-DATA.md.
tags:
- underground-mathematics
- exp-and-log
- type/review-question
resource_identity:
  ugm_id: r9381
  station: exp-and-log
  station_title: Exponentials & Logarithms
  resource_type_id: 10
  resource_type_label: Review question
  level: null
  ref: 9381
  old_site_id: "Q110"
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
      confidence: medium
      model_version: "GLM (Super Z agent, z.ai) — P3c lane-10 cross-map (cross-map-log-and-exp.json (P3c lane 10) @ syllabai-experimental 980556af)"
      evidence: "bounds for log_2 3 deduced from 2^3=8, 2^5=32, 3^2=9, 3^3=27 - the logarithm read as the index, with 'log_2 x is an increasing function'"
      rationale: "Canonical UGM title: Can we find bounds for $\\log_2 3$?"
      validation_status: SUGGESTED
    title: "understand the relationship between logarithms and indices, and use the laws of logarithms (excluding change of base)"
  mapped_date: '2026-10-25'
  mapper: cross-map-log-and-exp.json (P3c lane 10) @ syllabai-experimental 980556af
provenance:
  capture_date: '2026-10-22'
  capture_tool: P2 full-site crawl (ugm-crawl) → ugm-clean extraction; text-only import
  content_language: en
  exam_reference: "Oxford University Mathematics Aptitude Test, Specimen 2, Q1I"
  task: T-UGM-IMPORT-10
---

# Can we find bounds for $\log_2 3$?

## Question

Observe that \(2^3 = 8\), \(2^5 = 32\), \(3^2 = 9\) and \(3^3 = 27\). From these facts, we can deduce that \(\log_{2}3\), the logarithm of \(3\) to base \(2\), is

1. between \(1\frac{1}{3}\) and \(1\frac{1}{2}\);

---

1. between \(1\frac{1}{2}\) and \(1\frac{2}{3}\);

---

1. between \(1\frac{2}{3}\) and \(2\);

---

1. between \(2\) and \(3\).

## Suggestion

Can we create any inequalities from the information we’re given in the question?

Is it helpful to note that \(\log_{2}x\) is an increasing function?

## Solution

We are told that \[2^3 < 3^2 < 3^3 < 2^5.\]

As \(\log_{2}x\) is an increasing function (which means that \(\log_2x < \log_2y\) if and only if \(x < y\), or the gradient of the graph \(y = \log_2x\) is always positive), we can take logarithms to base \(2\) of these inequalities. This gives \[3 < 2\log_{2}3 < 3\log_{2}3 < 5.\]

From the first inequality we get \[\frac{3}{2} < \log_{2}3,\] and from the last inequality we get \[\log_{2}3 < \frac{5}{3}.\]

Combining these gives \[\frac{3}{2} < \log_{2}3 < \frac{5}{3},\] so the answer is (b).

An alternative approach might say, let \(\log_23 = k\), so \(3 = 2^k\). Now \(9 = 2^{2k} > 8\), so \(2k > 3\).

We also have \(27 = 2^{3k} < 32 = 2^5\), so \(3k < 5\).

We use here that \(y = 2^x\) is an increasing function.
