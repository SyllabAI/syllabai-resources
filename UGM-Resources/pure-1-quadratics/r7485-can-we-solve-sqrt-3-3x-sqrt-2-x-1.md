---
created: 2026-10-23T12:00:00 (UTC +06:00)
source: https://undergroundmathematics.org/quadratics/r7485
author: Underground Mathematics (University of Cambridge)
rights: © University of Cambridge (Underground Mathematics). Use inside SyllabAI is authorised by the
  operator attestation of 2026-10-23 — see LICENSE-DATA.md (Amendment 2026-10-23) in this repository.
  Takedown / correction handling as stated in LICENSE-DATA.md.
tags:
- underground-mathematics
- quadratics
- type/review-question
resource_identity:
  ugm_id: r7485
  station: quadratics
  station_title: Quadratics
  resource_type_id: 10
  resource_type_label: Review question
  level: null
  ref: 7485
  old_site_id: null
spec_map:
  curriculum_code: CIE-9709-P1-2023
  lane: cie-a-level-maths-20-pure-1
  board: Cambridge CIE
  syllabus_version: 2023-2025
  subsection: quadratics
  subsection_provenance:
    tier: PROVIDER
    signal: source-url-slug
    slug: quadratics
    validation_status: SUGGESTED
  spec_points:
  - code: 1.1.5
    provenance:
      tier: AI_SUGGESTED
      confidence: high
      model_version: GLM (Super Z agent, z.ai) — P3c quadratics cross-map (cross-map-quadratics.json @
        syllabai-experimental 915bfa8c)
      evidence: Surds equation squared down to a quadratic.
      rationale: 'Canonical UGM title: “Can we solve $\sqrt{3-3x} - \sqrt{2-x} = 1$?”; exam provenance:
        UCLES 1979 Q1'
      validation_status: SUGGESTED
    title: recognise and solve equations in x which are quadratic in some function of x . tan
  mapped_date: '2026-10-23'
  mapper: cross-map-quadratics.json (P3c) @ syllabai-experimental 915bfa8c
  coverage_note: null
provenance:
  capture_date: '2026-10-22'
  capture_tool: P2 full-site crawl (ugm-crawl) → ugm-clean extraction; text-only import
  content_language: en
  exam_reference: UCLES 1979 Q1
task: T-UGM-IMPORT-1
---

# Can we solve $\sqrt{3-3x} - \sqrt{2-x} = 1$?

## Question

1. Find all pairs of values of \(x\) and \(y\) for which \[\begin{equation*} \frac{3x+y+1}{8} = \frac{x-y}{5} = \frac{x^2 - y^2}{5}. \end{equation*}\]
2. Solve the equation \[\begin{equation*} \sqrt{3-3x} - \sqrt{2-x} = 1. \end{equation*}\] *The expression \(\sqrt{u}\) denotes the positive square root of \(u\).*

## Suggestion

I have two equations here with two unknowns. So I seem to be dealing with simultaneous equations, though they have been disguised a little.

I really don’t like all these square roots. Perhaps squaring will help?

## Solution

Since

\(x^2 - y^2 = (x-y)(x+y)\)

, we can write the second equation (after multiplying both sides by

\(5\)

) as

\[\begin{equation*} x-y = (x-y)(x+y). \end{equation*}\]

So either \(x-y=0\), or we can divide by \(x-y\) to give \(x+y=1\).

#### Case 1: \(x - y = 0\)

In this case, the first equation holds if and only if \(3x+y+1=0\).

But as \(x=y\), this gives \(4x+1=0\), so \(x=y=-\frac14\) is a solution.

#### Case 2: \(x+y = 1\)

In this case, we can write

\(y = 1 - x\)

and thus the first equation becomes

\[\begin{align*} &&\frac{3x + (1-x) + 1}{8} &= \frac{x - (1-x)}{5} \\ \iff&& \frac{2x + 2}{8} &= \frac{2x - 1}{5} \\ \iff&& 5(x+1) &= 4(2x-1) \\ \iff&& 9 &= 3x \\ \iff&& x &= 3. \end{align*}\]

So \(x=3\), \(y=-2\) is a second solution.

By squaring both sides, we have

\[\begin{align*} 1 &= \left( \sqrt{3-3x} - \sqrt{2-x} \right)^2 \\ &= (3-3x) - 2\sqrt{3-3x}\sqrt{2-x} + (2-x) \\ &= 5 - 4x - 2\sqrt{3-3x}\sqrt{2-x}. \end{align*}\]

We can rearrange this to put the square roots on one side, giving

\[\begin{equation*} \sqrt{3-3x}\sqrt{2-x} = 2-2x. \end{equation*}\]

By squaring both sides again to get rid of the square root, this implies that

\[\begin{align*} &&(3-3x)(2-x) &= (2-2x)^2 \\ \iff&& 6 - 9x + 3x^2 &= 4 - 8x + 4x^2 \\ \iff&& x^2 + x - 2 &= 0 \\ \iff&& (x+2)(x-1) &= 0 \end{align*}\]

so that \(x = 1\) or \(x = -2\).

These are only *candidate solutions*; the original equation implies these are the only solutions possible, but they are only possibilities. Our squaring may have introduced extra ‘solutions’. (For example, if \(x=1\), then \(x^2=1\), but \(x^2=1\) has two solutions, \(x=1\) and \(x=-1\).) So we need to check whether these candidate solutions are actually solutions of the original equation.

If

\(x = 1\)

, then

\[\begin{equation*} \sqrt{3-3x} - \sqrt{2-x} = -1 \ne 1, \end{equation*}\]

so this is *not* a solution to the original problem.

If

\(x = -2\)

, then

\[\begin{equation*} \sqrt{3-3x} - \sqrt{2-x} = \sqrt{9} - \sqrt{4} = 3 - 2 = 1. \end{equation*}\]

So \(x = -2\) is the unique solution to the original problem.
