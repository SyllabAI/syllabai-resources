---
created: 2026-10-23T21:23:05 (UTC +06:00)
source: https://undergroundmathematics.org/sequences/r8121
author: Underground Mathematics (University of Cambridge)
rights: © University of Cambridge (Underground Mathematics). Use inside SyllabAI is authorised by the
  operator attestation of 2026-10-23 — see LICENSE-DATA.md (Amendment 2026-10-23) in this repository.
  Takedown / correction handling as stated in LICENSE-DATA.md.
tags:
- underground-mathematics
- sequences
- type/review-question
resource_identity:
  ugm_id: r8121
  station: sequences
  station_title: Sequences
  resource_type_id: 10
  resource_type_label: Review question
  level: null
  ref: 8121
  old_site_id: Q31
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
      evidence: recognise 3/n^3+4/n^3+...+(n^3-3)/n^3 as an AP and solve for n — AP recognition + sum
        formula
      rationale: 'Canonical UGM title: "When does the sum of this series equal $60$?"; exam provenance:
        UKMT Senior Mathematical Challenge, 2006, Q22'
      validation_status: SUGGESTED
    title: use the formulae for the n th term and for the Including knowledge that numbers sum of the
      first n terms to solve problems involving arithmetic or geometric progressions equivalent).
  mapped_date: '2026-10-23'
  mapper: cross-map-series.json (P3c lane 6) @ syllabai-experimental 82964ce4
provenance:
  capture_date: '2026-10-22'
  capture_tool: P2 full-site crawl (ugm-crawl) → ugm-clean extraction; text-only import
  content_language: en
  exam_reference: UKMT Senior Mathematical Challenge, 2006, Q22
task: T-UGM-IMPORT-6
---

# When does the sum of this series equal $60$?

## Question

Which positive integer \(n\) satisfies the equation \[\frac{3}{n^3}+\frac{4}{n^3}+\frac{5}{n^3}+\dotsb +\frac{n^3-5}{n^3}+\frac{n^3-4}{n^3}+\frac{n^3-3}{n^3}=60?\]

## Suggestion

What type of sequence do we have on the left hand side of the equation? How many terms are there in the sequence?

## Solution

This is an arithmetic progression with common difference \(\dfrac{1}{n^3}\). There are \(n^3-5\) terms.

The formula for the sum of \(k\) terms of an arithmetic progression \(a_1 + \dotsb + a_k\) is given by \(\dfrac{k}{2}\left(a_1 + a_k\right).\)

Alternatively, if the first term is \(a\), and the common difference is \(d\), and if there are \(n\) terms, then the sum of the first \(n\) terms is \(S_n = \dfrac{n}{2}(2a + (n-1)d)\).

Their sum is therefore \[60=\frac{n^3-5}{2}\left(\frac{3}{n^3}+\frac{n^3-3}{n^3}\right)=\frac{n^3-5}{2}\left(\frac{n^3}{n^3}\right)=\frac{n^3-5}{2},\] so we can rearrange to get \[n^3-5=120\implies n^3=125\implies n=5.\]

Alternatively, we could have written the sum as

\[\frac{3}{n^3}+\frac{4}{n^3}+\frac{5}{n^3}+\dotsb +\frac{n^3-5}{n^3}+\frac{n^3-4}{n^3}+\frac{n^3-3}{n^3}=\frac{3+4+\dotsb+(n^3-3)}{n^3}\]

Now we can treat the numerator as an arithmetic series giving \[\frac{\frac{(n^3-3)(n^3-2)}{2}-1-2}{n^3} =\frac{n^6-5 n^3+6-6}{2 n^3} =\frac{n^3-5}{2} = 60, n = 5.\]
