---
created: 2026-10-24T22:06:39 (UTC +06:00)
source: https://undergroundmathematics.org/exp-and-log/r6045
author: Underground Mathematics (University of Cambridge)
rights: © University of Cambridge (Underground Mathematics). Use inside SyllabAI is authorised by the
  operator attestation of 2026-10-23 — see LICENSE-DATA.md (Amendment 2026-10-23) in this repository.
  Takedown / correction handling as stated in LICENSE-DATA.md.
tags:
- underground-mathematics
- exp-and-log
- type/review-question
resource_identity:
  ugm_id: r6045
  station: exp-and-log
  station_title: Exponentials & Logarithms
  resource_type_id: 10
  resource_type_label: Review question
  level: null
  ref: 6045
  old_site_id: "Q108"
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
  - code: 3.2.3
    provenance:
      tier: AI_SUGGESTED
      confidence: high
      model_version: "GLM (Super Z agent, z.ai) — P3c lane-10 cross-map (cross-map-log-and-exp.json (P3c lane 10) @ syllabai-experimental 980556af)"
      evidence: "log_10 2 = 0.3010 with 10^0.2 < 2 deduces that 2^100 is 31 digits long and finds its first digit - logarithms on indices"
      rationale: "Canonical UGM title: How large is $2^{100}$, and what is its starting digit?"
      validation_status: SUGGESTED
    title: "use logarithms to solve equations and e.g. inequalities in which the unknown appears in indices"
  mapped_date: '2026-10-25'
  mapper: cross-map-log-and-exp.json (P3c lane 10) @ syllabai-experimental 980556af
provenance:
  capture_date: '2026-10-22'
  capture_tool: P2 full-site crawl (ugm-crawl) → ugm-clean extraction; text-only import
  content_language: en
  exam_reference: "Oxford University Mathematics Aptitude Test, Specimen 1, Q1H"
  task: T-UGM-IMPORT-10
---

# How large is $2^{100}$, and what is its starting digit?

## Question

Given that \[\log_{10} 2 = 0.3010 \; \text{ (to }4\text{ d.p.)}\] and that \[10^{0.2} < 2\] it is possible to deduce that

1. \(2^{100}\) begins in a \(1\) and is \(30\) digits long;

---

1. \(2^{100}\) begins in a \(2\) and is \(30\) digits long;

---

1. \(2^{100}\) begins in a \(1\) and is \(31\) digits long;

---

1. \(2^{100}\) begins in a \(2\) and is \(31\) digits long.

## Solution

From the first given property, we have that \[\log_{10} 2^{100} = 100\log_{10} 2 = 30.10\dotsc\] so \[2^{100} = 10^{30.10 \dotsc} = 10^{0.10\dotsc} \times 10^{30}\] and so \(2^{100}\) is \(31\) digits long, with the first digit being the first digit of \(10^{0.10\dotsc}\).

Now we use the second given property: \[1 < 10^{0.10\dotsc} < 10^{0.2} < 2.\] The first digit is less than \(2\) and so must be a \(1\), and the answer is (c).
