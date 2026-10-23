---
created: 2026-10-23T21:23:05 (UTC +06:00)
source: https://undergroundmathematics.org/divisibility-and-induction/r9916
author: Underground Mathematics (University of Cambridge)
rights: © University of Cambridge (Underground Mathematics). Use inside SyllabAI is authorised by the
  operator attestation of 2026-10-23 — see LICENSE-DATA.md (Amendment 2026-10-23) in this repository.
  Takedown / correction handling as stated in LICENSE-DATA.md.
tags:
- underground-mathematics
- divisibility-and-induction
- type/review-question
resource_identity:
  ugm_id: r9916
  station: divisibility-and-induction
  station_title: Divisibility & Induction
  resource_type_id: 10
  resource_type_label: Review question
  level: null
  ref: 9916
  old_site_id: Q17
spec_map:
  curriculum_code: CIE-9709-P1-2023
  lane: cie-a-level-maths-20-pure-1
  board: Cambridge CIE
  syllabus_version: 2023-2025
  subsection: divisibility-and-induction
  subsection_provenance:
    tier: PROVIDER
    signal: source-url-slug
    slug: divisibility-and-induction
    validation_status: SUGGESTED
  spec_points:
  - code: 1.6.3
    provenance:
      tier: AI_SUGGESTED
      confidence: medium
      model_version: GLM (Super Z agent, z.ai) — P3c lane-6 cross-map (cross-map-series.json (P3c lane
        6) @ syllabai-experimental 82964ce4)
      evidence: common term of two APs via nth-term forms 2005+7j and 2005+9k (LCM structure)
      rationale: 'Canonical UGM title: "What''s the next number to occur in both sequences?"; exam provenance:
        UKMT Senior Mathematical Challenge, 2005, Q7'
      validation_status: SUGGESTED
    title: use the formulae for the n th term and for the Including knowledge that numbers sum of the
      first n terms to solve problems involving arithmetic or geometric progressions equivalent).
  mapped_date: '2026-10-23'
  mapper: cross-map-series.json (P3c lane 6) @ syllabai-experimental 82964ce4
provenance:
  capture_date: '2026-10-22'
  capture_tool: P2 full-site crawl (ugm-crawl) → ugm-clean extraction; text-only import
  content_language: en
  exam_reference: UKMT Senior Mathematical Challenge, 2005, Q7
task: T-UGM-IMPORT-6
---

# What's the next number to occur in both sequences?

## Question

Consider the arithmetic sequences \(1998\), \(2005\), \(2012\), … and \(1996\), \(2005\), \(2014\), …. What is the next number after \(2005\) that appears in both sequences?

## Suggestion

What is the common difference for each sequence? How is this useful?

## Solution

The sequences have common differences of \(7\) and \(9\) respectively.

So the numbers in the first sequence can be written as \(2005 + 7j\) for whole numbers \(j\).

The numbers in the second sequence can be written as \(2005 + 9k\) for whole number \(k\).

So we are looking for the smallest positive \(j\) and \(k\) so that \(2005 + 7j = 2005 + 9k\), or \(7j = 9k\).

Since \(7\) and \(9\) have no common factor, these values for \(j\) and \(k\) are \(9\) and \(7\).

So we have that the next number in both sequences is \(2005 + 7.9 = 2068\).

Alternatively, the next number in both lists is \(m = 2005 + n\).

Since \(m\) is in List \(1, 7\) goes into \(n\), and since \(m\) is in List \(2, 9\) goes into \(n\).

Thus the smallest possible \(n\) is \(7 \times 9 = 63\), and \(m=2068\) is the number we want.
