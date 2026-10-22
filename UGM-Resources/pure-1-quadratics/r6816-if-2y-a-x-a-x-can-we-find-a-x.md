---
created: 2026-10-23T12:00:00 (UTC +06:00)
source: https://undergroundmathematics.org/quadratics/r6816
author: Underground Mathematics (University of Cambridge)
rights: © University of Cambridge (Underground Mathematics). Use inside SyllabAI is authorised by the
  operator attestation of 2026-10-23 — see LICENSE-DATA.md (Amendment 2026-10-23) in this repository.
  Takedown / correction handling as stated in LICENSE-DATA.md.
tags:
- underground-mathematics
- quadratics
- type/review-question
resource_identity:
  ugm_id: r6816
  station: quadratics
  station_title: Quadratics
  resource_type_id: 10
  resource_type_label: Review question
  level: null
  ref: 6816
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
      evidence: Hidden quadratic in a^x; then a^{-x} read off reciprocally.
      rationale: 'Canonical UGM title: “If $2y = a^x + a^{-x}$, can we find $a^x$?”; exam provenance:
        UCLES 1973 Q2'
      validation_status: SUGGESTED
    title: recognise and solve equations in x which are quadratic in some function of x . tan
  mapped_date: '2026-10-23'
  mapper: cross-map-quadratics.json (P3c) @ syllabai-experimental 915bfa8c
  coverage_note: null
provenance:
  capture_date: '2026-10-22'
  capture_tool: P2 full-site crawl (ugm-crawl) → ugm-clean extraction; text-only import
  content_language: en
  exam_reference: UCLES 1973 Q2
task: T-UGM-IMPORT-1
---

# If $2y = a^x + a^{-x}$, can we find $a^x$?

## Question

Given that

\(2y = a^x + a^{-x}\)

, where

\(a > 1\)

,

\(x > 0\)

, prove that

\[\begin{equation*} a^x = y + \sqrt{y^2-1}. \end{equation*}\]

If, further,

\(2z = a^{3x} + a^{-3x}\)

, prove that

\[\begin{equation*} z = 4y^3 - 3y. \end{equation*}\]

## Suggestion

What are we asked to find? Do we need to find \(x\) itself?

We could just cube the expression for \(a^x\) and then work out \(a^{-x}\) and so on. But that seems quite painful. I wonder whether there is a simpler way?

## Solution

The question asks about \(a^x\), not about \(x\) itself. So if we write \(u=a^x\), the problem will look a little simpler. As \(a>1\) and \(x>0\), it follows that \(u>1\). Then the question becomes:

Given that \(2y=u+1/u\), where \(u>1\), prove that \(u=y+\sqrt{y^2-1}\). If we multiply both sides of the equation by \(u\), we get \[2yu=u^2 + 1,\] which rearranges to \(u^2-2yu+1=0\). Then using the [quadratic formula](https://undergroundmathematics.org/glossary/quadratic-equation-solution) we get \[u=\frac{2y\pm\sqrt{(-2y)^2-4}}{2}=y\pm\sqrt{y^2-1}.\]

There are two roots to the equation \(2y=u+1/u\), and they will be reciprocals of each other, as replacing \(u\) by \(1/u\) gives exactly the same equation. So one of the roots will be greater than \(1\), the other will be less than \(1\). Since we require \(u>1\), we need to take the positive sign.

So \(a^x=u=y+\sqrt{y^2-1}\).

Another way of arguing which sign to use goes like this.

Since \(u>1\), \(1/u<1<u\), so \(2y=u+1/u<u+u=2u\), and thus \(y<u\) or \(u>y\). So we have to use the positive sign.

Continuing to write \(u=a^x\), we are told that \(2z=u^3+\dfrac{1}{u^3}\). If we cube \(2y=u+\dfrac{1}{u}\), we obtain \[(2y)^3 = \left(u + \frac{1}{u} \right)^3 = u^3+3u+\frac{3}{u}+\frac{1}{u^3} = 2z + 3(2y),\] so \(8y^3=2z+6y\). Dividing by \(2\) and rearranging gives \[4y^3 - 3y = z.\]

This is related to the [hyperbolic functions](https://undergroundmathematics.org/glossary/hyperbolic-function). If \(a = e\), then \(y = \cosh x\) and \(z = \cosh 3x\), while in general, since \(a^x=e^{x\ln a}\), we have \(y=\cosh (x\ln a)\) and \(z=\cosh (3x\ln a)\). The second result then shows that \(\cosh 3x=4\cosh^3 x-3\cosh x\), which is the same as the corresponding formula for (ordinary) cosines.
