---
created: 2026-10-24T01:49:53 (UTC +06:00)
source: https://undergroundmathematics.org/calculus-of-powers/floppy-hair
author: Underground Mathematics (University of Cambridge)
rights: © University of Cambridge (Underground Mathematics). Use inside SyllabAI is authorised by the
  operator attestation of 2026-10-23 — see LICENSE-DATA.md (Amendment 2026-10-23) in this repository.
  Takedown / correction handling as stated in LICENSE-DATA.md.
tags:
- underground-mathematics
- calculus-of-powers
- type/fluency-exercise
- level/developing
resource_identity:
  ugm_id: floppy-hair
  station: calculus-of-powers
  station_title: Calculus of Powers
  resource_type_id: 8
  resource_type_label: Fluency exercise
  level: Developing
  ref: 5439
  old_site_id: null
spec_map:
  curriculum_code: CIE-9709-P1-2023
  lane: cie-a-level-maths-20-pure-1
  board: Cambridge CIE
  syllabus_version: 2023-2025
  subsection: calculus-of-powers
  subsection_provenance:
    tier: PROVIDER
    signal: source-url-slug
    slug: calculus-of-powers
    validation_status: SUGGESTED
  spec_points:
  - code: 1.7.2
    provenance:
      tier: AI_SUGGESTED
      confidence: high
      model_version: GLM (Super Z agent, z.ai) — P3c lane-7 cross-map (cross-map-differentiation.json
        (P3c lane 7) @ syllabai-experimental 93575e69)
      evidence: differentiate five curves with fractional indices, locate each maximum, match equations
        to curves — rational-n power rule load-bearing
      rationale: 'Canonical UGM title: "Floppy hair"'
      validation_status: SUGGESTED
    title: use the derivative of x (for any rational n ), together with constant multiples, sums and
      differences of functions, and of composite functions using the chain rule
  - code: 1.7.4
    provenance:
      tier: AI_SUGGESTED
      confidence: high
      model_version: GLM (Super Z agent, z.ai) — P3c lane-7 cross-map (cross-map-differentiation.json
        (P3c lane 7) @ syllabai-experimental 93575e69)
      evidence: differentiate five curves with fractional indices, locate each maximum, match equations
        to curves — rational-n power rule load-bearing
      rationale: 'Canonical UGM title: "Floppy hair"'
      validation_status: SUGGESTED
    title: locate stationary points and determine their nature, and use information about stationary
      points in sketching graphs.
  mapped_date: '2026-10-24'
  mapper: cross-map-differentiation.json (P3c lane 7) @ syllabai-experimental 93575e69
provenance:
  capture_date: '2026-10-22'
  capture_tool: P2 full-site crawl (ugm-crawl) → ugm-clean extraction; text-only import
  content_language: en
task: T-UGM-IMPORT-7
assets:
- path: https://undergroundmathematics.org/calculus-of-powers/floppy-hair/download/teacher-notes.pdf
  kind: printable
---

# Floppy hair

> Excerpt: Students use differentiation to locate stationary points on curves. They also have to manipulate some fractional indices and solve equations in order to decide which equation goes with which curve.

## Problem

This graph shows five curves, \(a\), \(b\), \(c\), \(d\) and \(e\), which all pass through the origin and the points \((1,2)\) and \((3,0)\). They each have one local maximum between \(x=0\) and \(x=3\).

Below are the equations of the five curves plus one extra equation. Find the coordinates of the maxima and hence identify which equation goes with which curve.

| \(y=x(3-x)\) |  | \(y=\sqrt[3]x(3-x)\) |
|---|---|---|
| \(y=\sqrt x(3-x)\) |  | \(y=\dfrac{1}{6}x(3-x)(5+x)\) |
| \(y=\dfrac{1}{4}x(3-x)(5-x)\) |  | \(y=\dfrac{2}{\sqrt[3] 9 -1} \left( \sqrt[3]{9x} -x \right)\) |

Add a sketch of the missing curve on the same axes.

Suggestion

How does knowing the gradient of a curve help us to locate the local maximum?

You might need to rewrite the equations with each term a power of \(x\) before you can differentiate them.

## Solution

To find the coordinates of the maximum of each curve, we can differentiate each equation. This gives us a formula for the gradient and this is zero at the maximum.

To make this easier to differentiate, we multiply out the bracket first.

\[\begin{align*} y &= 3x-x^2\\ \frac{dy}{dx} &= 3-2x \end{align*}\]

Setting \(\frac{dy}{dx}=0\) gives us \(3-2x=0\) and hence \(x=\frac{3}{2}\). The black curve, \(e\), appears to have a maximum at \(x=1.5\), suggesting that this is the equation of \(e\).

This equation is a quadratic, so we could have located it’s maximum without using calculus.

We start by writing the square root in index form and multiplying out the bracket.

\[\begin{align*} y &= x^{\frac{1}{2}}(3-x)\\ &= 3x^{\frac{1}{2}} - x^{\frac{3}{2}}\\ \frac{dy}{dx} &= \frac{3}{2}x^{-\frac{1}{2}} - \frac{3}{2}x^{\frac{1}{2}} \end{align*}\]

So the maximum is when

\[\begin{align*} \frac{3}{2}x^{-\frac{1}{2}} - \frac{3}{2}x^{\frac{1}{2}} &= 0\\ x^{-\frac{1}{2}} &= x^{\frac{1}{2}}\\ x &= 1 \end{align*}\]

So this is the green curve, \(c\).

As before, we start by multiplying out the brackets, then differentiate to find the gradient.

\[\begin{align*} y &= \frac{1}{4}\left( x^3-8x^2+15x \right)\\ \frac{dy}{dx} &= \frac{1}{4}\left( 3x^2-16x+15 \right) \end{align*}\]

Setting the gradient equal to zero gives us a quadratic equation with roots \(x=\dfrac{8}{3}\pm\dfrac{\sqrt{19}}{3}\). The one of these roots that is between zero and three is at \(x\approx1.21\), so this appears to be the purple curve, \(d\).

\[\begin{align*} y &= 3x^{\frac{1}{3}} - x^{\frac{4}{3}}\\ \frac{dy}{dx} &= x^{-\frac{2}{3}} - \frac{4}{3}x^{\frac{1}{3}} \end{align*}\]

At the maximum,

\[\begin{align*} x^{-\frac{2}{3}} - \frac{4}{3}x^{\frac{1}{3}} &= 0\\ x^{-\frac{2}{3}} &= \frac{4}{3}x^{\frac{1}{3}}\\ \frac{3}{4} &= x \end{align*}\]

So this appears to be the blue curve, \(b\).

\[\begin{align*} y &= \frac{1}{6}\left( -x^3-2x^2+15x \right)\\ \frac{dy}{dx} &= \frac{1}{6}\left( -3x^2-4x+15 \right) \end{align*}\]

As above, we have a quadratic equation which factorises to give \(x=-3\) or \(\frac{5}{3}\). The black curve, \(e\), has a maximum close to \(x=\frac{5}{3}\), but we have already suggested the first equation for this curve. The first equation does look a better fit, but to check we could calculate the \(y\) values of the two candidates at their maxima and see which ones matches.

The first equation at \(x=\frac{3}{2}\) gives \(y=\frac{9}{4}=2.25\).

This equation at \(x=\frac{5}{3}\) gives \(y=\frac{200}{81}\approx2.5\).

The first equation is definitely a better match for curve \(e\), so this equation is the one without a graph.

By elimination, this must be the remaining curve, \(a\), but let’s do the calculation to be sure.

\[\begin{align*} y &= \frac{2}{\sqrt[3] 9 -1} \left( \sqrt[3]{9}x^\frac{1}{3} -x \right)\\ \frac{dy}{dx} &= \frac{2}{\sqrt[3] 9 -1} \left( \frac{\sqrt[3]{9}}{3}x^{-\frac{2}{3}} -1 \right) \end{align*}\]

So at the maximum,

\[\begin{align*} \frac{\sqrt[3]{9}}{3}x^{-\frac{2}{3}} -1 &= 0\\ x^{\frac{2}{3}} &= \frac{\sqrt[3]{9}}{3}\\ x^2 &= \frac{9}{3^3} = \frac{1}{3}\\ x &= \pm \frac{1}{\sqrt{3}} \approx \pm 0.58 \end{align*}\]

This does indeed match graph \(a\).
