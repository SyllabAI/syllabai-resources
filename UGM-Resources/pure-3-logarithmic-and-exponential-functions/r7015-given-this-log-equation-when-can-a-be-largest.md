---
created: 2026-10-24T22:06:39 (UTC +06:00)
source: https://undergroundmathematics.org/exp-and-log/r7015
author: Underground Mathematics (University of Cambridge)
rights: © University of Cambridge (Underground Mathematics). Use inside SyllabAI is authorised by the
  operator attestation of 2026-10-23 — see LICENSE-DATA.md (Amendment 2026-10-23) in this repository.
  Takedown / correction handling as stated in LICENSE-DATA.md.
tags:
- underground-mathematics
- exp-and-log
- type/review-question
resource_identity:
  ugm_id: r7015
  station: exp-and-log
  station_title: Exponentials & Logarithms
  resource_type_id: 10
  resource_type_label: Review question
  level: null
  ref: 7015
  old_site_id: "Q100"
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
      evidence: "4(log_10 a)^2 + (log_10 b)^2 = 1 - greatest a when (log_10 b)^2 is least, 'since log is an increasing function'; quadratic-in-log technique"
      rationale: "Canonical UGM title: Given this log equation, when can $a$ be largest?"
      validation_status: SUGGESTED
    title: "use logarithms to solve equations and e.g. inequalities in which the unknown appears in indices"
  mapped_date: '2026-10-25'
  mapper: cross-map-log-and-exp.json (P3c lane 10) @ syllabai-experimental 980556af
provenance:
  capture_date: '2026-10-22'
  capture_tool: P2 full-site crawl (ugm-crawl) → ugm-clean extraction; text-only import
  content_language: en
  exam_reference: "Oxford University Mathematics Aptitude Test, 2007, Q1I"
  task: T-UGM-IMPORT-10
---

# Given this log equation, when can $a$ be largest?

## Question

Given that \(a\) and \(b\) are positive and \[4(\log_{10}a)^2+(\log_{10}b)^2=1\] then the greatest possible value of \(a\) is

1. \(\frac{1}{10}\),

---

1. \(1\),

---

1. \(\sqrt{10}\),

---

1. \(10^{\sqrt{2}}\).

## Solution

**Approach 1**

Note first that \(a\) is largest when \(\log_{10}a\) is largest, since \(\log\) is an increasing function. So \(a\) is largest when \((\log_{10}b)^2\) is smallest.

For positive \(b\), the minimum value that \((\log_{10}b)^2\) can take is \(0\) (when \(b=1\)). Then we have \[4(\log_{10}a)^2=1,\] which is equivalent to \[\log_{10}a =\pm \frac{1}{2}.\]

So the largest value this takes is \(\log_{10}a = \frac{1}{2}\), which is when \(a=\sqrt{10}\).

Therefore the answer is (c).

In fact, this also shows that the minimum value for \(\log_{10}a\) happens when \(b = 1\) and \(\log_{10}a = -1/2\). That is, when \(a = 1/\sqrt{10}\).

The ellipse \(4x^2 + y^2 = 1\)

**Approach 2**

Alternatively, we could take a geometrical approach. Let \(x = \log_{10}a\), \(y = \log_{10}b\). The maximum value for \(x=\log_{10}a\) is achieved when \(a\) takes its maximum value, since \(\log\) is an increasing function.

Our equation now becomes \(4x^2 + y^2 = 1\), which is an ellipse.

From the sketch, we can see that \(x\) has maximum \(\frac{1}{2}\) and so \(a\) has maximum \(\sqrt{10}\), by the same calculation as above.

As before, the answer must be (c).
