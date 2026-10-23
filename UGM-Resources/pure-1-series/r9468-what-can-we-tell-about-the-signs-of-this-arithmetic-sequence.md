---
created: 2026-10-23T21:23:05 (UTC +06:00)
source: https://undergroundmathematics.org/sequences/r9468
author: Underground Mathematics (University of Cambridge)
rights: © University of Cambridge (Underground Mathematics). Use inside SyllabAI is authorised by the
  operator attestation of 2026-10-23 — see LICENSE-DATA.md (Amendment 2026-10-23) in this repository.
  Takedown / correction handling as stated in LICENSE-DATA.md.
tags:
- underground-mathematics
- sequences
- type/review-question
resource_identity:
  ugm_id: r9468
  station: sequences
  station_title: Sequences
  resource_type_id: 10
  resource_type_label: Review question
  level: null
  ref: 9468
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
      evidence: S_8>3S_6 — deduce the signs of a and d from the AP sum formula — formula-driven reasoning
        MC
      rationale: 'Canonical UGM title: "What can we tell about the signs of this arithmetic sequence?";
        exam provenance: TMUA paper 2, 2016, Q12'
      validation_status: SUGGESTED
    title: use the formulae for the n th term and for the Including knowledge that numbers sum of the
      first n terms to solve problems involving arithmetic or geometric progressions equivalent).
  mapped_date: '2026-10-23'
  mapper: cross-map-series.json (P3c lane 6) @ syllabai-experimental 82964ce4
provenance:
  capture_date: '2026-10-22'
  capture_tool: P2 full-site crawl (ugm-crawl) → ugm-clean extraction; text-only import
  content_language: en
  exam_reference: TMUA paper 2, 2016, Q12
task: T-UGM-IMPORT-6
---

# What can we tell about the signs of this arithmetic sequence?

## Question

The first term of an arithmetic sequence is \(a\) and the common difference is \(d\).

The sum of the first \(n\) terms is denoted by \(S_n\).

If \(S_8>3S_6\), what can be deduced about the sign of \(a\) and the sign of \(d\)?

1. both \(a\) and \(d\) are negative

---

1. \(a\) is positive, \(d\) is negative

---

1. \(a\) is negative, \(d\) is positive

---

1. \(a\) is negative, but the sign of \(d\) cannot be deduced

---

1. \(d\) is negative, but the sign of \(a\) cannot be deduced

---

1. neither the sign of \(a\) nor the sign of \(d\) can be deduced

*[Choose the one correct answer and explain your reasoning.]*

## Solution

The most appropriate formula for

\(S_n\)

in this context is

\(S_n=\frac{1}{2}n(2a+(n-1)d)\)

. Substituting

\(n=6\)

and

\(n=8\)

gives

\[\begin{align*} S_6&=3(2a+5d)=6a+15d\\ S_8&=4(2a+7d)=8a+28d. \end{align*}\]

Now we are told that \(S_8>3S_6\), so \(8a+28d>3(6a+15d)\), which gives \[-10a -17d > 0.\] As this is the only information we have, the only thing we can say about the signs of \(a\) and \(d\) is that at least one of them is negative, but we cannot determine which one. For example, we could have \(a=1\) and \(d=-1\), or \(a=-2\) and \(d=1\), or \(a=d=-1\).

So the correct answer is (F).
