---
created: 2026-10-23T12:00:00 (UTC +06:00)
source: https://undergroundmathematics.org/quadratics/r6387
author: Underground Mathematics (University of Cambridge)
rights: © University of Cambridge (Underground Mathematics). Use inside SyllabAI is authorised by the
  operator attestation of 2026-10-23 — see LICENSE-DATA.md (Amendment 2026-10-23) in this repository.
  Takedown / correction handling as stated in LICENSE-DATA.md.
tags:
- underground-mathematics
- quadratics
- type/review-question
resource_identity:
  ugm_id: r6387
  station: quadratics
  station_title: Quadratics
  resource_type_id: 10
  resource_type_label: Review question
  level: null
  ref: 6387
  old_site_id: Q1017
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
      confidence: medium
      model_version: GLM (Super Z agent, z.ai) — P3c quadratics cross-map (cross-map-quadratics.json @
        syllabai-experimental 915bfa8c)
      evidence: Three-square-root inequality — extension of 1.1.3/1.1.5 techniques.
      rationale: 'Canonical UGM title: “Can we solve this inequality with three square roots?”; exam provenance:
        UCLES 1958 Q3(i)'
      validation_status: SUGGESTED
    title: recognise and solve equations in x which are quadratic in some function of x . tan
  mapped_date: '2026-10-23'
  mapper: cross-map-quadratics.json (P3c) @ syllabai-experimental 915bfa8c
  coverage_note: null
provenance:
  capture_date: '2026-10-22'
  capture_tool: P2 full-site crawl (ugm-crawl) → ugm-clean extraction; text-only import
  content_language: en
  exam_reference: UCLES 1958 Q3(i)
task: T-UGM-IMPORT-1
---

# Can we solve this inequality with three square roots?

## Question

Solve the inequality \[\sqrt{x+2}-\sqrt{x-1}>\sqrt{2x-3}\] for real values of \(x\) and of the square roots.

(The positive values of the square roots are to be taken.)

## Suggestion

Beware! Multiplying an inequality through by a negative number will change the direction of the inequality sign.

How can we get rid of the square root signs?

What values of \(x\) are permissible in this question?

## Solution

Square both sides of the inequality (this is permissible as the left hand side is positive, since

\(\sqrt{x+2}>\sqrt{x-1}\)

for real values of the square root):

\[\begin{align*} && x+2 -2\sqrt{(x-1)(x+2)} + x-1 &> 2x-3&&\quad \\ \iff&& 2x+1 -2\sqrt{(x-1)(x+2)} &> 2x-3 \\ \iff&& \sqrt{(x-1)(x+2)} &< 2. \end{align*}\]

Squaring again gives \[(x-1)(x+2)<4\] which rearranges to \[x^2+x-6<0.\]

By factorising the quadratic expression as \((x+3)(x-2)\) we can see that the roots are \(x=-3\) and \(2\).

A quick sketch of the quadratic \(y=x^2+x-6\) shows that the inequality \(x^2+x-6<0\) is satisfied when

\[\begin{equation} -3< x <2. \label{eq:1} \end{equation}\]

However, considering the original inequality we see that

\[\begin{align*} \sqrt{x+2} &\quad\text{is real for} \quad x\geq -2 \\ \sqrt{x-1} &\quad\text{is real for} \quad x\geq 1 \\ \sqrt{2x-3} &\quad\text{is real for} \quad x\geq \frac{3}{2} \end{align*}\]

We must therefore restrict the inequality \(\eqref{eq:1}\) to \[\frac{3}{2}\leq x < 2.\]

Do we need to check that our solution works in the original inequality, since we squared the inequality along the way?

It turns out that we are fine on this occasion.

If we have an inequality \(\sqrt{\vphantom{b}a}>\sqrt{b}\) and square it to get \(a>b\) (where both \(a\) and \(b\) are non-negative, and we have taken the positive square roots), then we can square root to get back to \(\sqrt{\vphantom{b}a}>\sqrt{b}\).

In other words, \[\sqrt{\vphantom{b}a}>\sqrt{b}\quad\iff\quad a>b.\]

However, it’s not true in general that \(a^2>b^2\) if and only if \(a>b\); if \(a=1\) and \(b=-2\), for example, then \(a>b\) but \(a^2<b^2\).

In our case, we relied upon the extra knowledge that both of the square roots were non-negative.
