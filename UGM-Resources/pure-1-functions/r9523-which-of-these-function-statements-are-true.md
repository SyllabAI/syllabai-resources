---
created: 2026-10-23T12:00:00 (UTC +06:00)
source: https://undergroundmathematics.org/combining-functions/r9523
author: Underground Mathematics (University of Cambridge)
rights: © University of Cambridge (Underground Mathematics). Use inside SyllabAI is authorised by the
  operator attestation of 2026-10-23 — see LICENSE-DATA.md (Amendment 2026-10-23) in this repository.
  Takedown / correction handling as stated in LICENSE-DATA.md.
tags:
- underground-mathematics
- combining-functions
- type/review-question
resource_identity:
  ugm_id: r9523
  station: combining-functions
  station_title: Combining Functions
  resource_type_id: 10
  resource_type_label: Review question
  level: null
  ref: 9523
  old_site_id: Q4060
spec_map:
  curriculum_code: CIE-9709-P1-2023
  lane: cie-a-level-maths-20-pure-1
  board: Cambridge CIE
  syllabus_version: 2023-2025
  subsection: combining-functions
  subsection_provenance:
    tier: PROVIDER
    signal: source-url-slug
    slug: combining-functions
    validation_status: SUGGESTED
  spec_points:
  - code: 1.2.2
    provenance:
      tier: AI_SUGGESTED
      confidence: medium
      model_version: GLM (Super Z agent, z.ai) — P3c functions cross-map (generalisation lane 2) (cross-map-functions.json
        @ syllabai-experimental 4a592ed0)
      evidence: True/false including the fg-order misconception (f:x^2, g:x^3 gives fg=x^6, not x^5);
        the implication-logic items sit beyond 1.2.
      rationale: 'Canonical UGM title: “Which of these function statements are true?”; exam provenance:
        UCLES 1979 Q[''Q9''] [986/2]'
      validation_status: SUGGESTED
    title: identify the range of a given function in simple cases, and find the composition of two given
      functions condition that a composite function
  mapped_date: '2026-10-23'
  mapper: cross-map-functions.json (P3c) @ syllabai-experimental 4a592ed0
  coverage_note: null
provenance:
  capture_date: '2026-10-22'
  capture_tool: P2 full-site crawl (ugm-crawl) → ugm-clean extraction; text-only import
  content_language: en
  exam_reference: UCLES 1979 Q['Q9'] [986/2]
task: T-UGM-IMPORT-2
---

# Which of these function statements are true?

## Question

State whether each of the following statements is true or false. If you decide that a statement is false, explain why this is the case.

1. \(x^2 -5x +6 =0\ \implies\ x = 2\).
2. \(f:x\rightarrow x^2\) and \(g:x\rightarrow x^3\ \implies\ fg: x\rightarrow x^5\).
3. \(|x+1| < 1\ \implies\ x < 0\).

## Solution

We have \(x^2 -5x +6\) factorises to \((x-2)(x-3)\), and so the equation \(x^2 -5x +6 =0\) has the solution \(x = 2\) or \(3\).

Hence the equation does NOT definitively tell us \(x\) is \(2\) (it could be \(3\)) and the statement is false.

Note that these are TRUE statements:

\(1. \quad x^2 -5x +6 =0 \implies x = 2 \quad \text{OR} \quad x=3\).

\(2. \quad x = 2 \implies x^2 -5x +6 =0\).

Applying the two functions \(f\) and \(g\) one after another on a number \(x\) gives \[ f\left( g(x) \right) = \left( x^3 \right)^2 = x^6,\]

using the rule \(\left(x^m\right)^n = x^{mn}\). So the given statement is false.

Note that there are two values of \(x\) so that \(x^5 = x^6\), namely \(x=0\) and \(x=1\).

So if we restrict the domain in the question to the \(x\)-values \(0\) and \(1\), the statement is true.

When does \(|x+1| < 1\)? This is equivalent to -1 < \(x+1\) < 1, or \(-2 < x < 0\), which is only possibly true when \(x\) is negative.

So this statement is definitely true.
