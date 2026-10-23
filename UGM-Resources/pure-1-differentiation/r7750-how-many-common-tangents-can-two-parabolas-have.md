---
created: 2026-10-24T01:49:53 (UTC +06:00)
source: https://undergroundmathematics.org/calculus-of-powers/r7750
author: Underground Mathematics (University of Cambridge)
rights: © University of Cambridge (Underground Mathematics). Use inside SyllabAI is authorised by the
  operator attestation of 2026-10-23 — see LICENSE-DATA.md (Amendment 2026-10-23) in this repository.
  Takedown / correction handling as stated in LICENSE-DATA.md.
tags:
- underground-mathematics
- calculus-of-powers
- type/review-question
resource_identity:
  ugm_id: r7750
  station: calculus-of-powers
  station_title: Calculus of Powers
  resource_type_id: 10
  resource_type_label: Review question
  level: null
  ref: 7750
  old_site_id: Q109
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
  - code: 1.7.3
    provenance:
      tier: AI_SUGGESTED
      confidence: high
      model_version: GLM (Super Z agent, z.ai) — P3c lane-7 cross-map (cross-map-differentiation.json
        (P3c lane 7) @ syllabai-experimental 93575e69)
      evidence: 'tangent to a parabola at the point of gradient m: y-mx = c-(m-b)^2/(4a), then common-tangent
        analysis for two parabolas'
      rationale: 'Canonical UGM title: "How many common tangents can two parabolas have?"; exam provenance:
        UCLES STEP Mathematics III, 2005, Q5'
      validation_status: SUGGESTED
    title: apply differentiation to gradients, tangents and normals, increasing and decreasing functions
      and rates of change
  mapped_date: '2026-10-24'
  mapper: cross-map-differentiation.json (P3c lane 7) @ syllabai-experimental 93575e69
provenance:
  capture_date: '2026-10-22'
  capture_tool: P2 full-site crawl (ugm-crawl) → ugm-clean extraction; text-only import
  content_language: en
  exam_reference: UCLES STEP Mathematics III, 2005, Q5
task: T-UGM-IMPORT-7
---

# How many common tangents can two parabolas have?

## Question

Let \(P\) be the point on the curve \(y=ax^2+bx+c\) (where \(a\) is non-zero) at which the gradient is \(m\). Show that the equation of the tangent at \(P\) is \[y-mx=c-\frac{(m-b)^2}{4a}.\]

Show that the curves \(y=a_1x^2+b_1x+c_1\) and \(y=a_2x^2+b_2x+c_2\) (where \(a_1\) and \(a_2\) are non-zero) have a common tangent with gradient \(m\) if and only if \[(a_2-a_1)m^2+2(a_1b_2-a_2b_1)m+4a_1a_2(c_2-c_1)+a_2b_1^2-a_1b_2^2=0.\]

Show that, in the case \(a_1\neq a_2\), the two curves have exactly one common tangent if and only if they touch each other. In the case \(a_1=a_2\), find a necessary and sufficient condition for the two curves to have exactly one common tangent.

## Suggestion

What is the gradient of the quadratic anywhere on the curve? What is it at \(P\)? Therefore, what are the coordinates of \(P\)?

The rest of this question requires you to think what statements imply others (and whether it works in reverse). Curves have a common tangent if and only if the equations of the tangents are the same if and only if gradients and intercepts are the same.

It may be helpful for clarity to think about the two directions separately: show that if they have a common tangent then the equation holds, and that if the equation holds then they have a common tangent.

This part requires arguments in both the forward \(\Longrightarrow\) direction and in the backward \(\Longleftarrow\) direction to get the full ‘if and only if’.

Forward direction (left to right, \(\Longrightarrow\)): Curves have *one* common tangent, so we want only one solution to the quadratic \[(a_2-a_1)m^2+2(a_1b_2-a_2b_1)m+4a_1a_2(c_2-c_1)+a_2b_1^2-a_1b_2^2=0.\] What is the [discriminant](https://undergroundmathematics.org/glossary/discriminant)?

If the two quadratics touch each other, we want only one solution to \[a_1x^2+b_1x+c_1=a_2x^2+b_2x+c_2.\]

What is meant by a necessary and sufficient condition?

What is a necessary and sufficient condition for a linear equation of the form \(dx+e=f\) to have a solution for \(x\)?

## Solution

The gradient of the quadratic is \[\frac{dy}{dx}=2ax+b=m.\]

Let the coordinates at

\(P\)

be

\(P(x_P,y_P)\)

. Then

\[\begin{align*} x_P &= \frac{m-b}{2a}, \quad \textrm{and} \\ y_P &= a\left(\frac{m-b}{2a}\right)^2+b\left(\frac{m-b}{2a}\right)+c. \end{align*}\]

Thus the tangent at

\(P\)

has the equation

\[y-\left[a\left(\frac{m-b}{2a}\right)^2+b\left(\frac{m-b}{2a}\right)+c\right] = m\left(x-\frac{m-b}{2a}\right),\]

that is,

\[\begin{align*} y-mx &= \frac{(m-b)^2}{4a}+\frac{b(m-b)}{2a}+c-\frac{m(m-b)}{2a}\\ &= c+\frac{1}{4a}(m-b)\left[2b-2m+(m-b)\right]\\ &= c- \frac{(m-b)^2}{4a} \end{align*}\]

as required.

The curves have a common tangent with gradient

\(m\)

if and only if the equations of the tangents to the two curves with gradient

\(m\)

are identical. Thus they need the

\(y\)

-intercepts to be identical (as they have the same gradients). We have

\[\begin{align} & c_1-\frac{(m-b_1)^2}{4a_1}=c_2-\frac{(m-b_2)^2}{4a_2} \notag\\ \iff & 4a_1a_2c_1-a_2(m-b_1)^2=4a_1a_2c_2-a_1(m-b_2)^2 \notag \\ \iff & (a_2-a_1)m^2+4a_1a_2(c_2-c_1)+2m(a_1b_2-a_2b_1)+a_2b_1^2-a_1b_2^2=0 \quad \label{eq:1} \end{align}\]

as required.

If \(a_1\neq a_2\) then to get exactly one root of \(\eqref{eq:1}\) we need the discriminant of the quadratic to be zero, that is, \[4(a_1b_2-a_2b_1)^2=4(a_2-a_1)(4a_1a_2(c_2-c_1)+a_2b_1^2-a_1b_2^2),\] so \[-2a_1a_2b_1b_2=4a_1a_2(a_2-a_1)(c_2-c_1)-a_1a_2b_1^2-a_1a_2b_2^2.\] Since \(a_1\) and \(a_2\) are non-zero by definition, we can cancel the \(a_1a_2\) factor: \[b_1^2-2b_1b_2+b_2^2=4(a_1-a_2)(c_2-c_1),\] so \[(b_2-b_1)^2=4(a_2-a_1)(c_2-c_1).\] The curves touch if and only if there is exactly one solution to \[a_1x^2+b_1x+c_1=a_2x^2+b_2x+c_2,\] that is, \[(a_2-a_1)x^2+(b_2-b_1)x+(c_2-c_1)=0.\] For one solution we need \[(b_2-b_1)^2=4(a_2-a_1)(c_2-c_1)\] which is the same condition for having exactly one common tangent.

If \(a_1=a_2\) then there is exactly one solution to \[2a_1(b_2-b_1)m+4a_1^2(c_2-c_1)+a_1(b_1^2 - b_2^2)=0.\] This is a linear equation and the only condition needed for there to be a solution for \(m\) is \(b_1\neq b_2\).

If \(b_1 = b_2\), then there are no solutions for \(m\) unless \(c_1 = c_2\), in which case there are infinitely many solutions.
