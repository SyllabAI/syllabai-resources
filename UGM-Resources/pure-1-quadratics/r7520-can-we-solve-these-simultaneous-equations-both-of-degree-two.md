---
created: 2026-10-23T12:00:00 (UTC +06:00)
source: https://undergroundmathematics.org/quadratics/r7520
author: Underground Mathematics (University of Cambridge)
rights: © University of Cambridge (Underground Mathematics). Use inside SyllabAI is authorised by the
  operator attestation of 2026-10-23 — see LICENSE-DATA.md (Amendment 2026-10-23) in this repository.
  Takedown / correction handling as stated in LICENSE-DATA.md.
tags:
- underground-mathematics
- quadratics
- type/review-question
resource_identity:
  ugm_id: r7520
  station: quadratics
  station_title: Quadratics
  resource_type_id: 10
  resource_type_label: Review question
  level: null
  ref: 7520
  old_site_id: Q206
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
  - code: 1.1.4
    provenance:
      tier: AI_SUGGESTED
      confidence: medium
      model_version: GLM (Super Z agent, z.ai) — P3c quadratics cross-map (cross-map-quadratics.json @
        syllabai-experimental 915bfa8c)
      evidence: Both equations degree two — extends the P1 linear+quadratic case (1.1.4).
      rationale: 'Canonical UGM title: “Can we solve these simultaneous equations, both of degree two?”;
        exam provenance: UCLES 1980 Q2(b)'
      validation_status: SUGGESTED
    title: solve by substitution a pair of simultaneous e.g. equations of which one is linear and one
      is 2 quadratic
  mapped_date: '2026-10-23'
  mapper: cross-map-quadratics.json (P3c) @ syllabai-experimental 915bfa8c
  coverage_note: null
provenance:
  capture_date: '2026-10-22'
  capture_tool: P2 full-site crawl (ugm-crawl) → ugm-clean extraction; text-only import
  content_language: en
  exam_reference: UCLES 1980 Q2(b)
task: T-UGM-IMPORT-1
assets:
- path: https://undergroundmathematics.org/quadratics/r7520/images/hyperbolas.png
  kind: figure
---

# Can we solve these simultaneous equations, both of degree two?

## Question

Solve the simultaneous equations

\[\begin{align*} 3x^2-13xy+9y^2&=15, \\ 7x^2-5y^2+17&=0. \end{align*}\]

## Suggestion

Can we rearrange one of these equations to find an expression for \(x\) or \(y\)? Or for \(x^2\) or \(y^2\)?

## Solution

Rearranging the second equation, we find that \[y^2=\frac{7x^2+17}{5}.\]

Substituting this in to the first equation gives \[3x^2-13xy+9\left(\frac{7x^2+17}{5}\right)=15.\]

Making \(y\) the subject here gives \(y = \dfrac{6x^2+6}{5x}\).

Now substituting this into the second equation gives

\[7x^2-5\left(\frac{6x^2+6}{5x}\right)^2+17=0,\]

which simplifies to

\[x^4-13x^2+36=0.\] This is a quadratic in \(x^2\) that we can factorise: \[x^4-13x^2+36=(x^2-9)(x^2-4)=0.\] So we deduce that \(x=\pm2\) or \(x=\pm3\).

To find \(y\), we can return to \(y = \dfrac{6x^2+6}{5x}\).

This gives us the four solutions \((x,y)=(2,3)\), \((-2,-3)\), \((3,4)\), and \((-3,-4)\).

We can then check that each of these pairs does, indeed, satisfy both equations.

We might notice that both of the starting equations are of degree 2 in \(x\) and \(y\). Graphically, each of these represents a [conic](https://undergroundmathematics.org/glossary/conic), that is, a circle, an ellipse, a parabola or a hyperbola. (There are also some degenerate possibilities, which we will not consider here.)

In this case, both equations give hyperbolas.

> [figure: The two hyperbolas defined in the question, intersecting in four points — `https://undergroundmathematics.org/quadratics/r7520/images/hyperbolas.png`] (image not included in the text import; path of record).

Two conics intersect in at most four points (as here), although there may be fewer crossing points (two circles may not intersect at all, for example). This is an example of [Bézout’s Theorem](https://undergroundmathematics.org/glossary/bezouts-theorem).
