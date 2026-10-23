---
created: 2026-10-23T21:23:05 (UTC +06:00)
source: https://undergroundmathematics.org/sequences/r8249
author: Underground Mathematics (University of Cambridge)
rights: © University of Cambridge (Underground Mathematics). Use inside SyllabAI is authorised by the
  operator attestation of 2026-10-23 — see LICENSE-DATA.md (Amendment 2026-10-23) in this repository.
  Takedown / correction handling as stated in LICENSE-DATA.md.
tags:
- underground-mathematics
- sequences
- type/review-question
resource_identity:
  ugm_id: r8249
  station: sequences
  station_title: Sequences
  resource_type_id: 10
  resource_type_label: Review question
  level: null
  ref: 8249
  old_site_id: Q2007
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
      evidence: sum of multiples of 5 or 8 but not both up to 1000 — three AP-sum applications with
        inclusion-exclusion
      rationale: 'Canonical UGM title: "What is the sum of the multiples of 5 or 8 but not both?"; exam
        provenance: UCLES A level Mathematics A 1 and Pure Mathematics 1, 1985, Q3'
      validation_status: SUGGESTED
    title: use the formulae for the n th term and for the Including knowledge that numbers sum of the
      first n terms to solve problems involving arithmetic or geometric progressions equivalent).
  mapped_date: '2026-10-23'
  mapper: cross-map-series.json (P3c lane 6) @ syllabai-experimental 82964ce4
provenance:
  capture_date: '2026-10-22'
  capture_tool: P2 full-site crawl (ugm-crawl) → ugm-clean extraction; text-only import
  content_language: en
  exam_reference: UCLES A level Mathematics A 1 and Pure Mathematics 1, 1985, Q3
task: T-UGM-IMPORT-6
---

# What is the sum of the multiples of 5 or 8 but not both?

## Question

Considering only the integers from \(1\) to \(1000\) inclusive, find the sum of those integers which are either multiples of \(5\) (i.e., \(5\), \(10\), \(15\), …) or multiples of \(8\) (i.e., \(8\), \(16\), \(24\), …) but are *not* multiples of both \(5\) and \(8\).

## Solution

We need \((5 + 10 + 15 \ldots + 1000) + (8+16+24+\ldots +1000) - 2(40 + 80 + \ldots + 1000).\)

We’ll use the formula that the sum of the first \(n\) terms of an arithmetic progression is \[\dfrac{n}{2}(u_1 + u_n),\]

where \(u_n\) is the \(n\)th term. So here we have

\[\dfrac{200}{2}(5+1000) + \dfrac{125}{2}(8+1000)- 2\times \dfrac{25}{2}(40+1000) = 137 500.\]

Alternatively, we have

\[(5 + 10 + 15 \ldots + 1000) + (8+16+24+\ldots +1000) - 2(40 + 80 + \ldots + 1000)\]

\[= 5(1+2+3\ldots+200) + 8(1+2+3+\ldots+125) - 2\times 40(1+2+3+\ldots + 25).\]

Now we know \(1 + 2 + \ldots + n = \dfrac{n(n+1)}{2}\), so this becomes

\[5\dfrac{200(201)}{2}+8\dfrac{125(126)}{2}-80\dfrac{25(26)}{2} = 137 500.\]
