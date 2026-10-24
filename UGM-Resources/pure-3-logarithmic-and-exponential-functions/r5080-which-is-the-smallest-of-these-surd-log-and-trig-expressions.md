---
created: 2026-10-24T22:06:39 (UTC +06:00)
source: https://undergroundmathematics.org/exp-and-log/r5080
author: Underground Mathematics (University of Cambridge)
rights: © University of Cambridge (Underground Mathematics). Use inside SyllabAI is authorised by the
  operator attestation of 2026-10-23 — see LICENSE-DATA.md (Amendment 2026-10-23) in this repository.
  Takedown / correction handling as stated in LICENSE-DATA.md.
tags:
- underground-mathematics
- exp-and-log
- type/review-question
resource_identity:
  ugm_id: r5080
  station: exp-and-log
  station_title: Exponentials & Logarithms
  resource_type_id: 10
  resource_type_label: Review question
  level: null
  ref: 5080
  old_site_id: "Q218"
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
      evidence: "log_3(9^2)=2log_3 9=4 and log_2(log_2(8^5)) evaluated exactly against surd/trig competitors; prior routing of record: lane-5 sweepRouting '2.2 Logarithmic and exponential functions'"
      rationale: "Canonical UGM title: Which is the smallest of these surd, log and trig expressions?"
      validation_status: SUGGESTED
    title: "understand the relationship between logarithms and indices, and use the laws of logarithms (excluding change of base)"
  mapped_date: '2026-10-25'
  mapper: cross-map-log-and-exp.json (P3c lane 10) @ syllabai-experimental 980556af
provenance:
  capture_date: '2026-10-22'
  capture_tool: P2 full-site crawl (ugm-crawl) → ugm-clean extraction; text-only import
  content_language: en
  exam_reference: "Oxford University Mathematics Aptitude Test, 2012, Q1C"
  task: T-UGM-IMPORT-10
---

# Which is the smallest of these surd, log and trig expressions?

## Question

Which is the *smallest* of the following numbers?

1. \(\left(\sqrt{3}\right)^3\),

---

1. \(\log_3 \left(9^2\right)\),

---

1. \(\left( 3\sin{\dfrac{\pi}{3}}\right) ^2\),

---

1. \(\log_2 \left(\log_2 \left(8^5\right)\right)\).

## Suggestion

Can we evaluate any of the expressions exactly?

If so, how do the other expressions compare with the exact value(s)?

## Solution

First we note that the value for b. is \(\log_3 (9^2) = 2\log_3 9 = 2\times2 = 4\).

In comparison with this,

a: \(\quad(\sqrt{3})^3 = 3 \sqrt{3} > 4\), since \(\sqrt{3} > 1.5\).

c: \(\quad\left(3\sin{\dfrac{\pi}{3}}\right)^2 = \left(\dfrac{3 \sqrt{3}}{2} \right)^2 = \frac{27}{4} > 4\).

d: \(\quad\log_2 (\log_2 (8^5)) = \log_2 (5\log_2 8) = \log_2 15 < \log_2 16 = 4\).

Hence the answer is d.
