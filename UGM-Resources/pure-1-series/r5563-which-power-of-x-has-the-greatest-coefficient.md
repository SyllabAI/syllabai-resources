---
created: 2026-10-23T21:23:05 (UTC +06:00)
source: https://undergroundmathematics.org/counting-and-binomials/r5563
author: Underground Mathematics (University of Cambridge)
rights: © University of Cambridge (Underground Mathematics). Use inside SyllabAI is authorised by the
  operator attestation of 2026-10-23 — see LICENSE-DATA.md (Amendment 2026-10-23) in this repository.
  Takedown / correction handling as stated in LICENSE-DATA.md.
tags:
- underground-mathematics
- counting-and-binomials
- type/review-question
resource_identity:
  ugm_id: r5563
  station: counting-and-binomials
  station_title: Counting & Binomials
  resource_type_id: 10
  resource_type_label: Review question
  level: null
  ref: 5563
  old_site_id: Q93
spec_map:
  curriculum_code: CIE-9709-P1-2023
  lane: cie-a-level-maths-20-pure-1
  board: Cambridge CIE
  syllabus_version: 2023-2025
  subsection: counting-and-binomials
  subsection_provenance:
    tier: PROVIDER
    signal: source-url-slug
    slug: counting-and-binomials
    validation_status: SUGGESTED
  spec_points:
  - code: 1.6.1
    provenance:
      tier: AI_SUGGESTED
      confidence: high
      model_version: GLM (Super Z agent, z.ai) — P3c lane-6 cross-map (cross-map-series.json (P3c lane
        6) @ syllabai-experimental 82964ce4)
      evidence: greatest-coefficient comparison for (1+1/2 x)^10 via c_{k+1}/c_k or direct ℒ₂ evaluation
      rationale: 'Canonical UGM title: "Which power of $x$ has the greatest coefficient?"; exam provenance:
        Oxford University Mathematics Aptitude Test, None, Q1I'
      validation_status: SUGGESTED
    title: use the expansion of ( a + b ) , where n is a positive integer
  mapped_date: '2026-10-23'
  mapper: cross-map-series.json (P3c lane 6) @ syllabai-experimental 82964ce4
provenance:
  capture_date: '2026-10-22'
  capture_tool: P2 full-site crawl (ugm-crawl) → ugm-clean extraction; text-only import
  content_language: en
  exam_reference: Oxford University Mathematics Aptitude Test, None, Q1I
task: T-UGM-IMPORT-6
---

# Which power of $x$ has the greatest coefficient?

## Question

The power of \(x\) which has the greatest coefficient in the expansion of \((1 + \frac{1}{2} x)^{10}\) is

1. \(x^2\),

---

1. \(x^3\),

---

1. \(x^5\),

---

1. \(x^{10}\).

## Solution

The coefficient of \(x^k\), where \(1 \leq k \leq 10\) is a whole number, is \[c_k ={^{10}C_k}\left(\frac{1}{2}\right)^k = \binom{10}{k}\left(\frac{1}{2}\right)^k=\frac{10!}{k!(10 - k)!} \left(\frac{1}{2}\right)^k.\]

1. For \(k = 2\), this is \(11.25\),

---

1. for \(k = 3\), this is \(15\),

---

1. for \(k = 5\), this is \(7.875\),

---

1. for \(k = 10\), this is \(9.76... \times 10^{-4}\), and so the answer is (b).

Alternatively, look at \(\dfrac{c_{k+1}}{c_k}\). We have

\[\frac{c_{k+1}}{c_k} = \frac{10!}{(k+1)!(9-k)!} \times \frac{k!(10-k)!}{10!} \times \frac{2^k}{2^{k+1}} = \frac{10-k}{2(k+1)}.\]

So the \(c_k\) are growing when \(\dfrac{c_{k+1}}{c_k} > 1\), that is, when \(10-k > 2(k+1) \iff k < \frac{8}{3}\), or \(k \leq 2\).

So if \(k = 2\), then \(\dfrac{c_{k+1}}{c_k} > 1\), which means that \(c_3 > c_2\).

For \(k > 2\), we know \(\dfrac{c_{k+1}}{c_k} < 1\), and so \(c_k\) decreases from its value at \(c_3\).

Therefore \(x^3\) has the greatest coefficient, and the answer is (b).
