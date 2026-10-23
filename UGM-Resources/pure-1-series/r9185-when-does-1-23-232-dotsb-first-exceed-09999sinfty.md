---
created: 2026-10-23T21:23:05 (UTC +06:00)
source: https://undergroundmathematics.org/sequences/r9185
author: Underground Mathematics (University of Cambridge)
rights: © University of Cambridge (Underground Mathematics). Use inside SyllabAI is authorised by the
  operator attestation of 2026-10-23 — see LICENSE-DATA.md (Amendment 2026-10-23) in this repository.
  Takedown / correction handling as stated in LICENSE-DATA.md.
tags:
- underground-mathematics
- sequences
- type/review-question
resource_identity:
  ugm_id: r9185
  station: sequences
  station_title: Sequences
  resource_type_id: 10
  resource_type_label: Review question
  level: null
  ref: 9185
  old_site_id: null
spec_map:
  curriculum_code: CIE-9709-P1-2023
  lane: cie-a-level-maths-20-pure-1
  board: Cambridge CIE
  syllabus_version: 2023-2025
  subsection: sequences
  subsection_provenance:
    tier: PROVIDER
    signal: source-url-slug
    slug: sequences
    validation_status: SUGGESTED
  spec_points:
  - code: 1.6.4
    provenance:
      tier: AI_SUGGESTED
      confidence: high
      model_version: GLM (Super Z agent, z.ai) — P3c lane-6 cross-map (cross-map-series.json (P3c lane
        6) @ syllabai-experimental 82964ce4)
      evidence: least number of terms of 1+2/3+(2/3)^2+... exceeding 99.99% of S_∞ — convergence + remainder
      rationale: 'Canonical UGM title: "When does $1 + 2/3 + (2/3)^2 + \dotsb$ first exceed $0.9999S_\infty$?";
        exam provenance: UCLES A level Mathematics A 1, 1976, Q3(b)'
      validation_status: SUGGESTED
    title: 'Questions may involve more than one progression. geometric progression, and the formula
      for the sum to infinity of a convergent geometric progression.: • use the condition for the convergence
      of a'
  mapped_date: '2026-10-23'
  mapper: cross-map-series.json (P3c lane 6) @ syllabai-experimental 82964ce4
provenance:
  capture_date: '2026-10-22'
  capture_tool: P2 full-site crawl (ugm-crawl) → ugm-clean extraction; text-only import
  content_language: en
  exam_reference: UCLES A level Mathematics A 1, 1976, Q3(b)
task: T-UGM-IMPORT-6
---

# When does $1 + 2/3 + (2/3)^2 + \dotsb$ first exceed $0.9999S_\infty$?

## Question

Find the least number of terms of the geometric series

\[\begin{equation*} 1 + \frac{2}{3} + \left( \frac{2}{3} \right)^2 + \dotsb \end{equation*}\]

that must be taken so that the sum of these terms exceeds \(99.99\%\) of the sum to infinity of the series.

## Solution

The sum of \(n\) terms of a GP is \(S_n = \dfrac{a(1-r^n)}{1-r}.\) For the GP above, \(a = 1\) and \(r = \dfrac{2}{3}\).

Since in our case \(\vert r \vert < 1,\) we can say the sum to infinity of the GP is \(S_\infty = \dfrac{1}{1-2/3} = 3.\)

We need to find the smallest \(n\) so that \(S_n > \dfrac{99.99 \times 3}{100}= 2.9997.\)

Let’s try to solve \(S_n = 2.9997.\) We have

\[S_n = \dfrac{1\times(1-(2/3)^n)}{1-2/3} = 3\left(1-\left(\dfrac{2}{3}\right)^n\right) = 2.9997.\]

Rearranging now tells us \(\left(\dfrac{2}{3}\right)^n = 0.0001.\) Taking logs to base \(e\), we have

\[n = \dfrac{\ln 0.0001}{\ln (2/3)} = 22.7....,\]

and so the value of \(n\) we seek is \(23\).

Alternatively, we could solve \(\left(\dfrac{2}{3}\right)^n = 0.0001\) by taking logs to base \(\dfrac{2}{3}\).

If you haven’t studied logs yet, you could find the threshold where \(\left(\dfrac{2}{3}\right)^n\) becomes small enough by trialling different \(n\) values.
