---
created: 2026-10-23T21:23:05 (UTC +06:00)
source: https://undergroundmathematics.org/sequences/r6153
author: Underground Mathematics (University of Cambridge)
rights: © University of Cambridge (Underground Mathematics). Use inside SyllabAI is authorised by the
  operator attestation of 2026-10-23 — see LICENSE-DATA.md (Amendment 2026-10-23) in this repository.
  Takedown / correction handling as stated in LICENSE-DATA.md.
tags:
- underground-mathematics
- sequences
- type/review-question
resource_identity:
  ugm_id: r6153
  station: sequences
  station_title: Sequences
  resource_type_id: 10
  resource_type_label: Review question
  level: null
  ref: 6153
  old_site_id: Q202
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
      confidence: medium
      model_version: GLM (Super Z agent, z.ai) — P3c lane-6 cross-map (cross-map-series.json (P3c lane
        6) @ syllabai-experimental 82964ce4)
      evidence: u_n = a+bn+c 2^n summed over n terms — the sum splits into an AP part (a n + b Σk) and
        a GP part (c Σ2^k); both 1.6.3 formulae load-bearing
      rationale: 'Canonical UGM title: "If $u_n = a + bn + c2^n$, what''s the sum of the first $n$ terms?";
        exam provenance: UCLES A level Mathematics 1, 1953, Q1'
      validation_status: SUGGESTED
    title: use the formulae for the n th term and for the Including knowledge that numbers sum of the
      first n terms to solve problems involving arithmetic or geometric progressions equivalent).
  mapped_date: '2026-10-23'
  mapper: cross-map-series.json (P3c lane 6) @ syllabai-experimental 82964ce4
provenance:
  capture_date: '2026-10-22'
  capture_tool: P2 full-site crawl (ugm-crawl) → ugm-clean extraction; text-only import
  content_language: en
  exam_reference: UCLES A level Mathematics 1, 1953, Q1
task: T-UGM-IMPORT-6
---

# If $u_n = a + bn + c2^n$, what's the sum of the first $n$ terms?

## Question

The \(n\)th term of a certain series is of the form \(a+bn+c2^n\), where \(a\), \(b\), and \(c\) are numbers. If the first three terms are \(2\), \(-1\), and \(3\), find the values of \(a\), \(b\), and \(c\), and the sum of the first \(n\) terms.

## Solution

We have

\(u_n = a+bn+c2^n,\)

so

\[\begin{align} a+b+2c&=2, \label{eq:1}\\ a+2b+4c&=-1, \label{eq:2}\\ a+3b+8c&=3. \label{eq:3} \end{align}\]

Taking \(\eqref{eq:2}\)\(-\)\(\eqref{eq:1}\) gives \(b+2c=-3\), while \(\eqref{eq:3}\)\(-\)\(\eqref{eq:2}\) gives \(b + 4c = 4\).

Subtracting these two equations gives \(2c = 7\), and so \(c = \dfrac{7}{2}\).

Substituting back into the earlier equations gives \(b = -10\), and \(a = 5\).

So the \(n^{th}\) term \(u_n = 5-10n+\dfrac{7}{2}2^n= 5-10n+7\times2^{n-1}.\)

Check for the third term: does \(3 = 5 - 30 + 28\)? Yes.

… and the sum of the first \(n\) terms.

This will be

\[\begin{align*} (a + b + 2c) + (a + 2b + 4c) + &(a + 3b + 8c) +...+ (a+nb+2^nc)\\ &= na + b(1 + 2 + .. + n) + c( 2 + 2^2 + 2^3 + ... + 2^n)\\ &= na + b\dfrac{n(n+1)}{2}+ 2c(2^{n}-1)\\ &= 5n -5n^2 - 5n +7\times 2^n -7\\ &= -5n^2 +7\times 2^n -7. \end{align*}\]

Check: when \(n= 3\), the sum of the first \(n\) terms is \(4\). Our formula gives \(-45+56-7 = 4\), so we have agreement.
