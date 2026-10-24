---
created: 2026-10-25T01:37:17 (UTC +06:00)
source: https://undergroundmathematics.org/polynomials/r8701
author: Underground Mathematics (University of Cambridge)
rights: © University of Cambridge (Underground Mathematics). Use inside SyllabAI is authorised by the
  operator attestation of 2026-10-23 — see LICENSE-DATA.md (Amendment 2026-10-23) in this repository.
  Takedown / correction handling as stated in LICENSE-DATA.md.
tags:
- underground-mathematics
- polynomials
- type/review-question
resource_identity:
  ugm_id: r8701
  station: polynomials
  station_title: Polynomials & Rational Functions
  resource_type_id: 10
  resource_type_label: Review question
  level: null
  ref: 8701
  old_site_id: "Q197"
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
      evidence: "remainder theorem gives f(k)=k → cubic 2k³−3k+1=0 factorised by the factor theorem; the remainder under (x−1)(x−2) read from p=(x−1)(x−2)q(x)+Ax+B"
      rationale: "Canonical UGM title: What if the remainder when we divide by $x-k$ is $k$?"
      validation_status: SUGGESTED
    title: "use the factor theorem and the remainder theorem"
  mapped_date: '2026-10-25'
  mapper: cross-map-algebra.json (P3c lane 9) @ syllabai-experimental 3098d8eb
provenance:
  capture_date: '2026-10-22'
  capture_tool: P2 full-site crawl (ugm-crawl) → ugm-clean extraction; text-only import
  content_language: en
  exam_reference: "UCLES A level Mathematics B 2, QP 9202/2, 1981, Q1"
  task: T-UGM-IMPORT-9
---

# What if the remainder when we divide by $x-k$ is $k$?

## Question

1. Given that \(f(x)=x^3+kx^2-2x+1\) and that when \(f(x)\) is divided by \((x-k)\) the remainder is \(k\), find the possible values of \(k\).

---

1. When the polynomial \(p(x)\) is divided by \((x-1)\) the remainder is \(5\) and when \(p(x)\) is divided by \((x-2)\) the remainder is \(7\). Given that \(p(x)\) may be written in the form \[(x-1)(x-2)q(x)+Ax+B,\] where \(q(x)\) is a polynomial and \(A\) and \(B\) are numbers, find the remainder when \(p(x)\) is divided by \((x-1)(x-2)\).

## Suggestion

What does the remainder theorem tell us?

Do we need to calculate \(q(x)\)?

How might we use the remainder theorem?

## Solution

Using the remainder theorem, we know that the remainder when we divide by \((x-k)\) is the same as \(f(k)=2k^3-2k+1\).

So we need to find solutions for \(2k^3-2k+1=k\), that is \(2k^3-3k+1=0\).

It is easy to guess and check that \(k=1\) is a solution, so \((k-1)\) is a factor; taking out a factor of \(k-1\) gives \[2k^3-3k+1=(k-1)(2k^2+2k-1).\] So either \(k=1\) or \(2k^2+2k-1=0\). Solutions for the latter are, using the quadratic formula, \[k=\frac{-2 \pm \sqrt{2^2-4\times 2\times (-1)}}{2\times 2} =\frac{-1 \pm \sqrt{3}}{2}\]

So the solutions are \(k=1\), \(k=\dfrac{-1 \pm \sqrt{3}}{2}\).

Using the remainder theorem again, the remainder when we divide \(p(x)\) by \((x-1)\) is the same as \(p(1)=A+B\), so \(A+B=5\).

Likewise, the remainder when we divide \(p(x)\) by \((x-2)\) is the same as \(p(2)=2A+B\), so \(2A+B=7\).

These simultaneous equations in \(A\) and \(B\) give as solutions \(A=2\) and \(B=3\).

The remainder when \(p(x)\) is divided by \((x-1)(x-2)\) is \(Ax+B\), since \((x-1)(x-2)\) is a factor of \((x-1)(x-2)q(x)\), and \(Ax+B\) has a smaller degree than \((x-1)(x-2)\). So the remainder is \(2x+3\).
