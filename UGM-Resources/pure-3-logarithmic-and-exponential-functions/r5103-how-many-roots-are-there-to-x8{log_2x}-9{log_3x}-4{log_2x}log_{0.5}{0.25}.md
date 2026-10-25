---
created: 2026-10-24T22:06:39 (UTC +06:00)
source: https://undergroundmathematics.org/exp-and-log/r5103
author: Underground Mathematics (University of Cambridge)
rights: © University of Cambridge (Underground Mathematics). Use inside SyllabAI is authorised by the
  operator attestation of 2026-10-23 — see LICENSE-DATA.md (Amendment 2026-10-23) in this repository.
  Takedown / correction handling as stated in LICENSE-DATA.md.
tags:
- underground-mathematics
- exp-and-log
- type/review-question
resource_identity:
  ugm_id: r5103
  station: exp-and-log
  station_title: Exponentials & Logarithms
  resource_type_id: 10
  resource_type_label: Review question
  level: null
  ref: 5103
  old_site_id: "Q128"
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
      evidence: "8^{log_2 x}=(2^{log_2 x})^3=x^3 and log_{0.5}0.25=2 reduce the equation to a polynomial root count - the a^{log_b c} identity at work"
      rationale: "Canonical UGM title: How many roots are there to $x=8^{\\log_2x} -9^{\\log_3x}-4^{\\log_2x}+\\log_{0.5}{0.25}$?"
      validation_status: SUGGESTED
    title: "use logarithms to solve equations and e.g. inequalities in which the unknown appears in indices"
  mapped_date: '2026-10-25'
  mapper: cross-map-log-and-exp.json (P3c lane 10) @ syllabai-experimental 980556af
provenance:
  capture_date: '2026-10-22'
  capture_tool: P2 full-site crawl (ugm-crawl) → ugm-clean extraction; text-only import
  content_language: en
  exam_reference: "Oxford University Mathematics Aptitude Test, 2011, Q1H"
  task: T-UGM-IMPORT-10
---

# How many roots are there to $x=8^{\log_2x} -9^{\log_3x}-4^{\log_2x}+\log_{0.5}{0.25}$?

## Question

The number of *positive* values \(x\) which satisfy the equation \[x=8^{\log_2x} -9^{\log_3x}-4^{\log_2x}+\log_{0.5}{0.25}\] is

1. 0;

---

1. 1;

---

1. 2;

---

1. 3.

## Suggestion

Can we evaluate \(\log_{0.5}{0.25}\) ?

We know that \(8\) is a power of \(2\) – could use this fact to rewrite \(8^{\log_2x}\)?

## Solution

We note that \(\log_{0.5}0.25=\log_{0.5}(0.5)^2=2\).

If \(x>0\) then \[8^{\log_2x}=(2^3)^{\log_2x}=(2^{\log_2x})^3=x^3.\]

Similarly, \[9^{\log_3x}=(3^2)^{\log_3x}=(3^{\log_3x})^2=x^2\] and \[4^{\log_2x}=(2^2)^{\log_2x}=(2^{\log_2x})^2=x^2.\]

So the equation becomes \[x=x^3-x^2-x^2+2,\] that is, \[x^3-2x^2-x+2=0.\]

We can see that \(x=2\) is a solution, so \((x-2)\) is a factor. By inspection, we find \[(x-2)(x^2-1)=0\] and so \[(x-2)(x-1)(x+1)=0.\]

So the roots are \(x=-1\), \(1\) and \(2\).

There are two positive values of \(x\) satisfying the equation so the answer is c.
