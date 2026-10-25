---
created: 2026-10-26T02:40:04 (UTC +06:00)
source: https://undergroundmathematics.org/calculus-trig-log/r8679
author: Underground Mathematics (University of Cambridge)
rights: © University of Cambridge (Underground Mathematics). Use inside SyllabAI is authorised by the
  operator attestation of 2026-10-23 — see LICENSE-DATA.md (Amendment 2026-10-23) in this repository.
  Takedown / correction handling as stated in LICENSE-DATA.md.
tags:
- underground-mathematics
- calculus-trig-log
- type/review-question
resource_identity:
  ugm_id: r8679
  station: calculus-trig-log
  station_title: Calculus of Trigonometry & Logarithms
  resource_type_id: 10
  resource_type_label: Review question
  level: null
  ref: 8679
  old_site_id: null
spec_map:
  curriculum_code: CIE-9709-P3-2023
  lane: cie-a-level-maths-20-pure-3
  board: Cambridge CIE
  syllabus_version: 2023-2025
  subsection: calculus-trig-log
  subsection_provenance:
    tier: PROVIDER
    signal: source-url-slug
    slug: calculus-trig-log
    validation_status: SUGGESTED
  spec_points:
  - code: 3.5.1
    provenance:
      tier: AI_SUGGESTED
      confidence: high
      model_version: GLM (Super Z agent, z.ai) — P3c lane-13 cross-map (cross-map-p3-integration.json
        (P3c lane 13) @ syllabai-experimental 21845f3)
      evidence: 'area under y = cos x - sin x + 2: A(a) = [sin x + cos x + 2x]_0^a with the 3.5.1 standard
        antiderivatives load-bearing, verified A(1.5)=3.07, then the Newton second approximation - the
        exact CIE standard-function-integration task (flips the lane-12 non-overlap row of record routed
        ''P3 3.5 Integration'')'
      rationale: 'Canonical UGM title: What is the area under the curve $y = \cos x - \sin x +2$?'
      validation_status: SUGGESTED
    title: extend the idea of ‘reverse differentiation’ to Including examples such as ax + b 1 include
      the integration of e , , ax + b sin( ax + b ) , cos( ax + b ) , sec ( ax + b ) and 2 2 x + a
  mapped_date: '2026-10-26'
  mapper: cross-map-p3-integration.json (P3c lane 13) @ syllabai-experimental 21845f3
provenance:
  capture_date: '2026-10-22'
  capture_tool: P2 full-site crawl (ugm-crawl) → ugm-clean extraction; text-only import
  content_language: en
  task: T-UGM-IMPORT-13
---

# What is the area under the curve $y = \cos x - \sin x +2$?

## Question

Given the curve \[y = \cos x - \sin x +2\] find in terms of \(a\) an expression for the area \(A\) enclosed between the axes, the ordinate \(a \; (> 0)\) and this curve. Verify that when \(a = 1.5\), \(A = 3.07\) approximately.

It is required to find the value of \(a\) for which \(A = 3\). Taking \(1.5\) as a first approximation to \(a\), find a second approximation, giving three significant figures in your answer.

## Solution

The ordinate \(a\) means the line \(x=a\). Our curve lies entirely above the \(x\)-axis. It is something like this.

To calculate the area, we integrate:

\[\begin{align*} A &= \int_0^a \cos x- \sin x+2 \:dx \\ &= \big[\sin x + \cos x + 2x\big]_0^a \\ &= \sin a + \cos a + 2a -1. \end{align*}\]

Substituting \(a = 1.5\) gives \(A = 3.0682... \approx 3.07\) as required.

So we need to find an approximate solution to \(3 = \sin a + \cos a + 2a -1\) that is better than \(a=1.5\).

There are a number of methods we could use here; decimal search, binary search, linear interpolation, the rearrangement method or simply zooming in with graphing software.

We will use the Newton-Raphson method. This says that given a guess \(x_0\) at the root \(\alpha\) (a solution to \(f(x) = 0\)), then as long as \(x_0\) is reasonably close to \(\alpha\), a better approximation to \(\alpha\) is \(x_1\) where

\[x_1 = x_0 - \dfrac{f(x_0)}{f'(x_0)}.\]

So our equation is \(f(x) = 0\) where \(f(x) = \sin x + \cos x + 2x - 4\), which gives \(f'(x) = \cos x -\sin x + 2\).

Thus \(x_1 = 1.5 - \dfrac{\sin 1.5 + \cos 1.5 + 3 - 4}{\cos 1.5 -\sin 1.5 + 2} = 1.4264...\)

So we have a better approximation to \(a\) than \(1.5\), namely \(1.43\) (\(3\)sf).

Check – \(\sin 1.43 + \cos 1.43 + 2\times 1.43 -1 = 2.99\) (\(3\)sf).
