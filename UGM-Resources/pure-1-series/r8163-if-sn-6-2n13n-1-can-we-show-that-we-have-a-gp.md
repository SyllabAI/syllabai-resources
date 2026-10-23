---
created: 2026-10-23T21:23:05 (UTC +06:00)
source: https://undergroundmathematics.org/sequences/r8163
author: Underground Mathematics (University of Cambridge)
rights: © University of Cambridge (Underground Mathematics). Use inside SyllabAI is authorised by the
  operator attestation of 2026-10-23 — see LICENSE-DATA.md (Amendment 2026-10-23) in this repository.
  Takedown / correction handling as stated in LICENSE-DATA.md.
tags:
- underground-mathematics
- sequences
- type/review-question
resource_identity:
  ugm_id: r8163
  station: sequences
  station_title: Sequences
  resource_type_id: 10
  resource_type_label: Review question
  level: null
  ref: 8163
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
  - code: 1.6.3
    provenance:
      tier: AI_SUGGESTED
      confidence: high
      model_version: GLM (Super Z agent, z.ai) — P3c lane-6 cross-map (cross-map-series.json (P3c lane
        6) @ syllabai-experimental 82964ce4)
      evidence: S_n = 6 - 2^{n+1}/3^{n-1} — show the series is geometric; state a and r — canonical
        S_n-to-GP question
      rationale: 'Canonical UGM title: "If $S_n =  6 - 2^{n+1}/3^{n-1}$, can we show that we have a
        GP?"; exam provenance: UCLES A level Mathematics B 1, 1981, Q1(b)'
      validation_status: SUGGESTED
    title: use the formulae for the n th term and for the Including knowledge that numbers sum of the
      first n terms to solve problems involving arithmetic or geometric progressions equivalent).
  mapped_date: '2026-10-23'
  mapper: cross-map-series.json (P3c lane 6) @ syllabai-experimental 82964ce4
provenance:
  capture_date: '2026-10-22'
  capture_tool: P2 full-site crawl (ugm-crawl) → ugm-clean extraction; text-only import
  content_language: en
  exam_reference: UCLES A level Mathematics B 1, 1981, Q1(b)
task: T-UGM-IMPORT-6
---

# If $S_n =  6 - 2^{n+1}/3^{n-1}$, can we show that we have a GP?

## Question

The sum of the first

\(n\)

terms of a series is given by the expression

\[\begin{equation*} 6 - \frac{2^{n+1}}{3^{n-1}}. \end{equation*}\]

By finding an expression for the \(n\)th term of the series, or otherwise, show that this is a geometric series, and state the values of the first term and the common ratio.

## Solution

Let the sequence that we are summing be

\((a_n)\)

for

\(n \ge 1\)

, so that

\[\begin{equation*} a_1 + \dotsb + a_n = 6 - \frac{2^{n+1}}{3^{n-1}} \end{equation*}\]

for every

\(n \ge 1\)

. In particular,

\[\begin{equation*} a_1 = 6 - \frac{2^2}{3^0} = 6 - 4 = 2, \end{equation*}\]

and, for every

\(n \ge 2\)

,

\[\begin{align*} a_{n} = \left( a_1 + \dotsb + a_{n} \right) - \left( a_1 + \dotsb + a_{n-1} \right) &= \left( 6 - \frac{2^{n+1}}{3^{n-1}} \right) - \left( 6 - \frac{2^{n}}{3^{n-2}} \right) \\ &= \frac{2^{n}}{3^{n-2}} - \frac{2^{n+1}}{3^{n-1}} \\ &= \frac{2^{n}}{3^{n-2}} \left( 1 - \frac{2}{3} \right) \\ &= \frac{2^{n}}{3^{n-2}} \frac{1}{3} \\ &= \frac{2^{n}}{3^{n-1}} \\ &= 2 \left( \frac{2}{3} \right)^{n-1}. \end{align*}\]

Thus, \((a_n)\) is a geometric progression with first term \(a_1 = 2\) and common ratio \(\dfrac{2}{3}\).
