---
created: 2026-10-23T21:23:05 (UTC +06:00)
source: https://undergroundmathematics.org/sequences/r8248
author: Underground Mathematics (University of Cambridge)
rights: © University of Cambridge (Underground Mathematics). Use inside SyllabAI is authorised by the
  operator attestation of 2026-10-23 — see LICENSE-DATA.md (Amendment 2026-10-23) in this repository.
  Takedown / correction handling as stated in LICENSE-DATA.md.
tags:
- underground-mathematics
- sequences
- type/review-question
resource_identity:
  ugm_id: r8248
  station: sequences
  station_title: Sequences
  resource_type_id: 10
  resource_type_label: Review question
  level: null
  ref: 8248
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
      confidence: medium
      model_version: GLM (Super Z agent, z.ai) — P3c lane-6 cross-map (cross-map-series.json (P3c lane
        6) @ syllabai-experimental 82964ce4)
      evidence: recursion x_n=Σx_k gives x_n=2^{n-1}; Σ1/x_k closes by the GP sum to infinity — one-to-many
        extension of 1.6.4 inside a recursion question
      rationale: 'Canonical UGM title: "Given the sequence $(x_n)$, what is  $\sum_{k=0}^\infty 1/x_k$?";
        exam provenance: Oxford University Mathematics Aptitude Test, 2016, Q1F'
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
  exam_reference: Oxford University Mathematics Aptitude Test, 2016, Q1F
task: T-UGM-IMPORT-6
---

# Given the sequence $(x_n)$, what is  $\sum_{k=0}^\infty 1/x_k$?

## Question

The sequence \((x_n)\), where \(n \geq 0\), is defined by \(x_0 =1\) and

\[x_n = \sum_{k=0}^{n-1}x_k \quad \text{for} \quad n \geq 1.\]

The sum

\[\sum_{k=0}^\infty \dfrac{1}{x_k}\]

equals

1. \(1\), (b) \(\dfrac{6}{5}\), (c) \(\dfrac{8}{5}\), (d) \(3\), (e) \(\dfrac{27}{5}\).

## Suggestion

Can we write the sequence \(x_0, x_1, x_2,...\) out? What kind of a sequence is this (almost)?

So what kind of a sequence is \(\dfrac{1}{x_n}\) (almost)?

How do we sum this kind of sequence?

## Solution

Can we write the sequence \((x_n)\) out?

Using the rule, we have:

\(x_0 = 1\),

\(x_1 =x_0= 1\),

\(x_2=x_0+x_1=1+1=2\),

\(x_3 =x_0+x_1+x_2= 1+1+2 = 4\),

\(x_4=x_0+x_1+x_2+x_3 = 1+1+2+4 = 8, ...\)

So \(x_n = 2^{n-1}\) for \(n \geq 1\), and apart from the first term, we have a geometric sequence.

We also have that \(\dfrac{1}{x_n} = \dfrac{1}{2^{n-1}}\), and so the sequence \(\left(\dfrac{1}{x_n}\right)\) is also geometric except for the first term.

We can remember now that the sum to infinity of a geometric progression with first term \(a\) and common ratio \(r\) is \(\dfrac{a}{1-r}\).

So \[\sum_{k=0}^\infty \dfrac{1}{x_k} = 1 + 1 + \dfrac{1}{2}+\dfrac{1}{4}+\dfrac{1}{8}+...\]

\[= 1 + \dfrac{1}{1-\dfrac{1}{2}} = 3,\]

and so that answer is (d).
