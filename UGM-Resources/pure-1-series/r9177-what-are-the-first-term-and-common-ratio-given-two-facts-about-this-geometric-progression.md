---
created: 2026-10-23T21:23:05 (UTC +06:00)
source: https://undergroundmathematics.org/sequences/r9177
author: Underground Mathematics (University of Cambridge)
rights: © University of Cambridge (Underground Mathematics). Use inside SyllabAI is authorised by the
  operator attestation of 2026-10-23 — see LICENSE-DATA.md (Amendment 2026-10-23) in this repository.
  Takedown / correction handling as stated in LICENSE-DATA.md.
tags:
- underground-mathematics
- sequences
- type/review-question
resource_identity:
  ugm_id: r9177
  station: sequences
  station_title: Sequences
  resource_type_id: 10
  resource_type_label: Review question
  level: null
  ref: 9177
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
      evidence: GP with a exceeds second term by 2, u_2+u_3=4/3 — two (a,r) pairs; positive-terms branch
        summed to infinity
      rationale: 'Canonical UGM title: "What are the first term and common ratio given two facts about
        this geometric progression?"; exam provenance: UCLES AO level Additional Mathematics 2, 1987,
        Q2(b)'
      validation_status: SUGGESTED
    title: use the formulae for the n th term and for the Including knowledge that numbers sum of the
      first n terms to solve problems involving arithmetic or geometric progressions equivalent).
  - code: 1.6.4
    provenance:
      tier: AI_SUGGESTED
      confidence: high
      model_version: GLM (Super Z agent, z.ai) — P3c lane-6 cross-map (cross-map-series.json (P3c lane
        6) @ syllabai-experimental 82964ce4)
      evidence: GP with a exceeds second term by 2, u_2+u_3=4/3 — two (a,r) pairs; positive-terms branch
        summed to infinity
      rationale: 'Canonical UGM title: "What are the first term and common ratio given two facts about
        this geometric progression?"; exam provenance: UCLES AO level Additional Mathematics 2, 1987,
        Q2(b)'
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
  exam_reference: UCLES AO level Additional Mathematics 2, 1987, Q2(b)
task: T-UGM-IMPORT-6
---

# What are the first term and common ratio given two facts about this geometric progression?

## Question

The first term of a geometric progression exceeds the second term by \(2\), and the sum of the second and third terms is \(\frac{4}{3}\). Calculate the possible values of the first term and of the common ratio of the progression.

Given further that all the terms of the progression are positive, calculate the sum to infinity.

## Solution

The terms of our sequence can be written as

\(a,ar,ar^2,...\)

and the given facts tell us that

\[\begin{align*} a&=ar+2 \\ ar+ar^2&=\frac{4}{3}. \end{align*}\]

Rearranging and factorising, these equations become

\[\begin{align*} a(1-r) &= 2 \\ ar(1+r) &=\frac{4}{3}. \end{align*}\]

We can then divide our second equation by our first giving

\[\frac{r(1+r)}{1-r}=\frac{2}{3}\]

which we can rearrange into a quadratic.

\[\begin{align*} 3r(1+r)&=2(1-r) \\ 3r^2+5r-2&=0 \end{align*}\]

Using the quadratic formula or by factorisation we find that the common ratio \[r=\frac{1}{3}\quad\text{or}\quad-2.\]

Now that we have the common difference we can calculate our first term \[a=\frac{2}{1-r}=3\quad\text{or}\quad\frac{2}{3}.\]

If all the terms are positive the common ratio cannot be negative, so we must have \(r=\frac{1}{3}\) and \(a=3\).

Substituting these values into the formula for the sum to infinity we have

\[\begin{align*} S_\infty &= \frac{a}{1-r} \\ &=\frac{3}{2/3}=\frac{9}{2}. \end{align*}\]
