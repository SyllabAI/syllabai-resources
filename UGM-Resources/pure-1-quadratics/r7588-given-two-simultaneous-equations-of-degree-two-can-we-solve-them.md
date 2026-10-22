---
created: 2026-10-23T12:00:00 (UTC +06:00)
source: https://undergroundmathematics.org/quadratics/r7588
author: Underground Mathematics (University of Cambridge)
rights: © University of Cambridge (Underground Mathematics). Use inside SyllabAI is authorised by the
  operator attestation of 2026-10-23 — see LICENSE-DATA.md (Amendment 2026-10-23) in this repository.
  Takedown / correction handling as stated in LICENSE-DATA.md.
tags:
- underground-mathematics
- quadratics
- type/review-question
resource_identity:
  ugm_id: r7588
  station: quadratics
  station_title: Quadratics
  resource_type_id: 10
  resource_type_label: Review question
  level: null
  ref: 7588
  old_site_id: Q50
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
      evidence: Two quadratics simultaneously — extension of 1.1.4.
      rationale: 'Canonical UGM title: “Given two simultaneous equations of degree two, can we solve them?”;
        exam provenance: UCLES 2010 Q1'
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
  exam_reference: UCLES 2010 Q1
task: T-UGM-IMPORT-1
assets:
- path: https://undergroundmathematics.org/quadratics/r7588/images/ellipses.png
  kind: figure
---

# Given two simultaneous equations of degree two, can we solve them?

## Question

Given that \[5x^2 + 2y^2 − 6xy + 4x − 4y \equiv a (x − y + 2)^2 + b (cx + y)^2 + d,\] find the values of the constants \(a\), \(b\), \(c\) and \(d\).

Solve the simultaneous equations

\[\begin{align*} 5x^2 + 2y^2 − 6xy + 4x − 4y &= 9 , \\ 6x^2 + 3y^2 − 8xy + 8x − 8y &= 14 . \end{align*}\]

## Solution

We will do this by expanding the right-hand side and comparing coefficients with the left-hand side. The right-hand side becomes \[(a+bc^2)x^2 + (a+b)y^2 + (2bc-2a)xy + 4ax - 4ay + 4a + d.\] Comparing coefficients with the left-hand side yields the following six equations:

1. \(a+bc^2=5\),
2. \(a+b=2\),
3. \(2bc-2a=-6\),
4. \(4a=4\),
5. \(-4a=-4\),
6. \(4a+d=0\).

Equations 4 and 5 tell us that \(a=1\). Substituting this in to equation 6 yields \(d=-4\). From equation 2 we find that \(b=1\). Equation 3 then gives \(c = -2\), and this also works in equation 1. So we have \[5x^2 + 2y^2 − 6xy + 4x − 4y \equiv (x − y + 2)^2 + (-2x + y)^2 -4.\]

---

Since the first part of the question told us to write the left-hand side of the first equation in a special form, perhaps we should try to write the left-hand side of the second equation in the same form.

Using the same technique as in the first part of the question, attempting to write \[6x^2 + 3y^2 − 8xy + 8x − 8y \equiv a (x − y + 2)^2 + b (cx + y)^2 + d,\] we get the following six equations:

1. \(a+bc^2=6\),
2. \(a+b=3\),
3. \(2bc-2a=-8\),
4. \(4a=8\),
5. \(-4a=-8\),
6. \(4a+d=0\).

This time, equations 4 and 5 show that \(a=2\), then equation 6 gives \(d=-8\), and then \(b=1\) by equation 2. Then equation 3 gives \(c = -2\), and this also works in equation 1.

So now let us try to solve the simultaneous equations

\[\begin{equation} (x − y + 2)^2 + (-2x + y)^2 -4=9, \label{eq:1} \end{equation}\]

and

\[\begin{equation} 2(x − y + 2)^2 + (-2x + y)^2 -8=14.\label{eq:2} \end{equation}\]

Looking at these two equations, we see that if we subtract them in certain ways, we get simpler equations, for example

\(\eqref{eq:2}\)

\(-\)

\(\eqref{eq:1}\)

yields the equation

\[(x-y+2)^2-4=5,\]

which simplifies to

\[\begin{equation} x-y+2=\pm3. \label{eq:3} \end{equation}\]

We now cancel the first term instead, by calculating

\(\eqref{eq:2}\)

\(-2\times \eqref{eq:1}\)

. We get

\[-(-2x+y)^2=-4,\]

which we simplify to find

\[\begin{equation} -2x+y=\pm2. \label{eq:4} \end{equation}\]

We now solve the four pairs of simultaneous equations given by \(\eqref{eq:3}\) and \(\eqref{eq:4}\).

1. \(x-y+2=3\) and \(-2x+y=2\) gives \(x=-3\), \(y=-4\).
2. \(x-y+2=-3\) and \(-2x+y=2\) gives \(x=3\), \(y=8\).
3. \(x-y+2=3\) and \(-2x+y=-2\) gives \(x=1\), \(y=0\).
4. \(x-y+2=-3\) and \(-2x+y=-2\) gives \(x=7\), \(y = 12\).

We briefly check using the equations we were given in the question that we have the correct solutions:

1. For \(x=-3\) and \(y=-4\), \[45+32-72-12+16=9 \; \checkmark \quad\text{and}\quad 54+48-96-24+32=14\; \checkmark\]
2. For \(x=3\) and \(y=8\), \[45+128-144+12-32=9 \; \checkmark \quad\text{and}\quad 54+192-192+24-64=14 \;\checkmark\]
3. For \(x=1\) and \(y=0\), \[5+4=9 \; \checkmark \quad\text{and}\quad 6+8=14 \;\checkmark\]
4. For \(x=7\) and \(y=12\), \[245+288-504+28-48=9 \;\checkmark \quad\text{and}\quad 294+432-672+56-96=14 \; \checkmark\]

The equations we are given in the question in fact represent ellipses, and we know that two ellipses can meet in at most four points. (This is an example of [Bézout’s Theorem](https://undergroundmathematics.org/glossary/bezouts-theorem).) The two curves in the question are graphed below.

> [figure: the two ellipses given in the question intesrsecting in four points — `https://undergroundmathematics.org/quadratics/r7588/images/ellipses.png`] (image not included in the text import; path of record).
