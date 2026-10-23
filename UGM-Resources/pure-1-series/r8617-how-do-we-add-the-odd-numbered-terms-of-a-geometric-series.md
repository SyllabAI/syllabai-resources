---
created: 2026-10-23T21:23:05 (UTC +06:00)
source: https://undergroundmathematics.org/sequences/r8617
author: Underground Mathematics (University of Cambridge)
rights: © University of Cambridge (Underground Mathematics). Use inside SyllabAI is authorised by the
  operator attestation of 2026-10-23 — see LICENSE-DATA.md (Amendment 2026-10-23) in this repository.
  Takedown / correction handling as stated in LICENSE-DATA.md.
tags:
- underground-mathematics
- sequences
- type/review-question
resource_identity:
  ugm_id: r8617
  station: sequences
  station_title: Sequences
  resource_type_id: 10
  resource_type_label: Review question
  level: null
  ref: 8617
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
      evidence: GP sum to infinity 8; odd-numbered terms sum to infinity 6 — find r — canonical S_∞
        work
      rationale: 'Canonical UGM title: "How do we add the odd-numbered terms of a geometric series?";
        exam provenance: UCLES A level Mathematics C 1, 1986, Q3'
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
  exam_reference: UCLES A level Mathematics C 1, 1986, Q3
task: T-UGM-IMPORT-6
---

# How do we add the odd-numbered terms of a geometric series?

## Question

A geometric series has first term \(a\) and common ratio \(r\), where \(|r|<1\). The sum to infinity of the series is \(8\). The sum to infinity of the series obtained by adding all the odd-numbered terms (i.e. 1st term + 3rd term + 5th term + …) is \(6\). Find the value of \(r\).

## Suggestion

A geometric series has first term \(a\) and common ratio \(r\), where \(|r|<1\). The sum to infinity of the series is \(8\). The sum to infinity of the series obtained by adding all the off-numbered terms (i.e. 1st term + 3rd term + 5th term + …) is \(6\). Find the value of \(r\).

We know the terms of the series we are given form a geometric series.

What can we say about the series formed by taking the odd-numbered terms instead?

## Solution

A geometric series has first term \(a\) and common ratio \(r\), where \(|r|<1\). The sum to infinity of the series is \(8\). The sum to infinity of the series obtained by adding all the off-numbered terms (i.e. 1st term + 3rd term + 5th term + …) is \(6\). Find the value of \(r\).

If \(|r|<1\), we know that the sum to infinity of the GP ([geometric progression](https://undergroundmathematics.org/glossary/geometric-sequence)) $a, ar, ar^2, … $ is given by

\[S_\infty=\frac{a}{1-r}.\]

Hence in our case we have that \[\dfrac{a}{1-r}=8.\]

The odd-numbered terms of the above series are \(a, ar^2, ar^4, ....\) which themselves form a GP with first term \(a\), common ratio \(r^2\).

We have \(|r|<1 \iff |r^2|<1\), and so this series also has a sum to infinity, \(T_\infty\), where \[T_\infty =\frac{a}{1-r^2} =6.\]

Dividing \(\dfrac{a}{1-r}=8\) by \(\dfrac{a}{1-r^2} =6\) gives us \[\frac{1-r^2}{1-r} =\dfrac{8}{6} \implies 1+r = \dfrac{8}{6} \implies r =\dfrac{1}{3}.\]
