---
created: 2026-10-23T21:23:05 (UTC +06:00)
source: https://undergroundmathematics.org/sequences/r9613
author: Underground Mathematics (University of Cambridge)
rights: © University of Cambridge (Underground Mathematics). Use inside SyllabAI is authorised by the
  operator attestation of 2026-10-23 — see LICENSE-DATA.md (Amendment 2026-10-23) in this repository.
  Takedown / correction handling as stated in LICENSE-DATA.md.
tags:
- underground-mathematics
- sequences
- type/review-question
resource_identity:
  ugm_id: r9613
  station: sequences
  station_title: Sequences
  resource_type_id: 10
  resource_type_label: Review question
  level: null
  ref: 9613
  old_site_id: Q76
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
      evidence: S_n=S_3n with d=-1 — express a in terms of n — clean AP-sum-formula algebra
      rationale: 'Canonical UGM title: "Given $S_n = S_{3n}$, can we express $a$ in terms of $n$?";
        exam provenance: UCLES A level Mathematics C 1, 1988, Q3'
      validation_status: SUGGESTED
    title: use the formulae for the n th term and for the Including knowledge that numbers sum of the
      first n terms to solve problems involving arithmetic or geometric progressions equivalent).
  mapped_date: '2026-10-23'
  mapper: cross-map-series.json (P3c lane 6) @ syllabai-experimental 82964ce4
provenance:
  capture_date: '2026-10-22'
  capture_tool: P2 full-site crawl (ugm-crawl) → ugm-clean extraction; text-only import
  content_language: en
  exam_reference: UCLES A level Mathematics C 1, 1988, Q3
task: T-UGM-IMPORT-6
---

# Given $S_n = S_{3n}$, can we express $a$ in terms of $n$?

## Question

An arithmetic progression has first term \(a\) and common difference \(-1\). The sum of the first \(n\) terms is equal to the sum of the first \(3n\) terms. Express \(a\) in terms of \(n\).

## Solution

For an arithmetic progression, the sum of the first \(n\) terms, \(S_n = \dfrac{n}{2}(2a+(n-1)d)\).

So here, \(S_n = \dfrac{n}{2}(2a-n+1)\), and \(S_{3n} = \dfrac{3n}{2}(2a-3n+1)\).

Equating these gives

\[\begin{align*} \dfrac{n}{2}(2a-n+1) &= \dfrac{3n}{2}(2a-3n+1)\\ \implies\quad 2a-n+1 &= 6a-9n+3\\ \implies\quad 4a &= 8n-2\\ \implies\quad a &= 2n - \dfrac{1}{2}. \end{align*}\]
