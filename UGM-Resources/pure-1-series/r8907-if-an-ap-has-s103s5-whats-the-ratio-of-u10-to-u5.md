---
created: 2026-10-23T21:23:05 (UTC +06:00)
source: https://undergroundmathematics.org/sequences/r8907
author: Underground Mathematics (University of Cambridge)
rights: © University of Cambridge (Underground Mathematics). Use inside SyllabAI is authorised by the
  operator attestation of 2026-10-23 — see LICENSE-DATA.md (Amendment 2026-10-23) in this repository.
  Takedown / correction handling as stated in LICENSE-DATA.md.
tags:
- underground-mathematics
- sequences
- type/review-question
resource_identity:
  ugm_id: r8907
  station: sequences
  station_title: Sequences
  resource_type_id: 10
  resource_type_label: Review question
  level: null
  ref: 8907
  old_site_id: Q1062
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
      evidence: S_10=3S_5 gives a=3d; ratio u_10/u_5=12/7; then S_200 from u_5=0.14 — S_n and u_n formulae
        together
      rationale: 'Canonical UGM title: "If an AP has $S_{10}=3S_5$, what''s the ratio of $u_{10}$ to
        $u_5$?"; exam provenance: UCLES AO level Additional Mathematics 2, 1986, Q2(a)'
      validation_status: SUGGESTED
      primaryPick: true
    title: use the formulae for the n th term and for the Including knowledge that numbers sum of the
      first n terms to solve problems involving arithmetic or geometric progressions equivalent).
  mapped_date: '2026-10-23'
  mapper: cross-map-series.json (P3c lane 6) @ syllabai-experimental 82964ce4
provenance:
  capture_date: '2026-10-22'
  capture_tool: P2 full-site crawl (ugm-crawl) → ugm-clean extraction; text-only import
  content_language: en
  exam_reference: UCLES AO level Additional Mathematics 2, 1986, Q2(a)
task: T-UGM-IMPORT-6
---

# If an AP has $S_{10}=3S_5$, what's the ratio of $u_{10}$ to $u_5$?

## Question

An arithmetic progression is such that the sum of the first 10 terms is 3 times the sum of the first 5 terms. Find the ratio of the 10th term to the 5th term.

Given further that the 5th term is \(0.14\), calculate the sum of the first 200 terms.

## Suggestion

An arithmetic progression is such that the sum of the first \(10\) terms is \(3\) times the sum of the first \(5\) terms. Find the ratio of the \(10\)th term to the \(5\)th term.

If \(S_n\) is the sum of the first n terms, do we have a formula for \(S_n\)?

If \(u_n\) is the nth term, do we have a formula for \(u_n\)?

Can we find the common difference with this added information?

## Solution

An arithmetic progression is such that the sum of the first \(10\) terms is \(3\) times the sum of the first \(5\) terms. Find the ratio of the \(10\)th term to the \(5\)th term.

We know that for an arithmetic progression, if \(S_n\) is the sum of the first \(n\) terms, then

\[S_n =\dfrac{n}{2}(2a + (n-1)d).\]

Here we have that \[S_{10}=3S_5 \implies \dfrac{10}{2}(2a + 9d)=3\dfrac{5}{2}(2a + 4d) \implies 3d = a.\]

We also know that if \(u_n\) is the \(n\)th term, then \(u_n = a + (n-1)d.\)

Thus \[\dfrac{u_{10}}{u_5} = \dfrac{a+9d}{a+4d} = \dfrac{12d}{7d} = \dfrac{12}{7}.\]

Given further that the \(5\)th term is \(0.14\), calculate the sum of the first \(200\) terms.

If we have that \(a + 4d = 0.14\), then \(7d = 0.14\), and \(d = 0.02, a = 0.06\).

Now \[S_{200} = \dfrac{200}{2}(0.12 + (199)0.02)= 410.\]
