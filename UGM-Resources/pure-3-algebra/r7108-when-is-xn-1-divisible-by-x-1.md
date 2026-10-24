---
created: 2026-10-25T01:37:17 (UTC +06:00)
source: https://undergroundmathematics.org/polynomials/r7108
author: Underground Mathematics (University of Cambridge)
rights: © University of Cambridge (Underground Mathematics). Use inside SyllabAI is authorised by the
  operator attestation of 2026-10-23 — see LICENSE-DATA.md (Amendment 2026-10-23) in this repository.
  Takedown / correction handling as stated in LICENSE-DATA.md.
tags:
- underground-mathematics
- polynomials
- type/review-question
resource_identity:
  ugm_id: r7108
  station: polynomials
  station_title: Polynomials & Rational Functions
  resource_type_id: 10
  resource_type_label: Review question
  level: null
  ref: 7108
  old_site_id: "Q3043"
spec_map:
  curriculum_code: CIE-9709-P3-2023
  lane: cie-a-level-maths-20-pure-3
  board: Cambridge CIE
  syllabus_version: 2023-2025
  subsection: polynomials
  subsection_provenance:
    tier: PROVIDER
    signal: source-url-slug
    slug: polynomials
    validation_status: SUGGESTED
  spec_points:
  - code: 3.1.4
    provenance:
      tier: AI_SUGGESTED
      confidence: high
      model_version: "GLM (Super Z agent, z.ai) — P3c lane-9 cross-map (cross-map-algebra.json (P3c lane 9) @ syllabai-experimental 3098d8eb)"
      evidence: "xⁿ+1 divisible by x+1 ⟺ (−1)ⁿ=−1 ⟺ n odd — a pure factor-theorem iff argument"
      rationale: "Canonical UGM title: When is  $x^n + 1$ divisible by $x + 1$?"
      validation_status: SUGGESTED
    title: "use the factor theorem and the remainder theorem"
  mapped_date: '2026-10-25'
  mapper: cross-map-algebra.json (P3c lane 9) @ syllabai-experimental 3098d8eb
provenance:
  capture_date: '2026-10-22'
  capture_tool: P2 full-site crawl (ugm-crawl) → ugm-clean extraction; text-only import
  content_language: en
  exam_reference: "UCLES O level Additional Mathematics 2, QP 471/2, 1968, Q5(iii)"
  task: T-UGM-IMPORT-9
---

# When is  $x^n + 1$ divisible by $x + 1$?

## Question

Show that \(x^n + 1\) is divisible by \(x + 1\) when, and only when, \(n\) is an odd integer.

## Suggestion

We are being asked when a polynomial \(p(x)\) is divisible by \(x-a\).

Could we use the factor theorem here?

## Solution

By the [factor theorem](https://undergroundmathematics.org/glossary/factor-theorem), given a polynomial \(p(x)\) with real coefficients and some real number \(a\), we know that \(x-a\) is a factor of \(p(x)\) if and only if \(p(a) = 0\).

If we let

\(p(x) = x^n + 1\)

and

\(a = -1\)

, by the factor theorem we have that

\[\begin{align*} \text{$x^n + 1$ is divisible by $x + 1$} &\iff (-1)^n + 1 = 0 \\ &\iff (-1)^n = -1 \\ &\iff \text{$n$ is an odd integer}. \end{align*}\]
