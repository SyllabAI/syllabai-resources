---
created: 2026-10-23T21:23:05 (UTC +06:00)
source: https://undergroundmathematics.org/product-rule/r9312
author: Underground Mathematics (University of Cambridge)
rights: © University of Cambridge (Underground Mathematics). Use inside SyllabAI is authorised by the
  operator attestation of 2026-10-23 — see LICENSE-DATA.md (Amendment 2026-10-23) in this repository.
  Takedown / correction handling as stated in LICENSE-DATA.md.
tags:
- underground-mathematics
- product-rule
- type/review-question
resource_identity:
  ugm_id: r9312
  station: product-rule
  station_title: Product Rule & Integration by Parts
  resource_type_id: 10
  resource_type_label: Review question
  level: null
  ref: 9312
  old_site_id: Q1026
spec_map:
  curriculum_code: CIE-9709-P1-2023
  lane: cie-a-level-maths-20-pure-1
  board: Cambridge CIE
  syllabus_version: 2023-2025
  subsection: product-rule
  subsection_provenance:
    tier: PROVIDER
    signal: source-url-slug
    slug: product-rule
    validation_status: SUGGESTED
  spec_points:
  - code: 1.6.4
    provenance:
      tier: AI_SUGGESTED
      confidence: medium
      model_version: GLM (Super Z agent, z.ai) — P3c lane-6 cross-map (cross-map-series.json (P3c lane
        6) @ syllabai-experimental 82964ce4)
      evidence: ΣA_n for the e^{-x}/e^{-x}sin x areas closes as a GP sum to infinity (integration is
        the vehicle)
      rationale: 'Canonical UGM title: "Can we find the area between $y=e^{-x}$ and $y=e^{-x}\sin x$?";
        exam provenance: UCLES STEP Mathematics II, 2010, Q8'
      validation_status: SUGGESTED
    title: 'Questions may involve more than one progression. geometric progression, and the formula
      for the sum to infinity of a convergent geometric progression.: • use the condition for the convergence
      of a'
  mapped_date: '2026-10-23'
  mapper: cross-map-series.json (P3c lane 6) @ syllabai-experimental 82964ce4
provenance:
  capture_date: '2026-10-22'
  capture_tool: P2 full-site crawl (ugm-crawl) → ugm-clean extraction; text-only import
  content_language: en
  exam_reference: UCLES STEP Mathematics II, 2010, Q8
task: T-UGM-IMPORT-6
---

# Can we find the area between $y=e^{-x}$ and $y=e^{-x}\sin x$?

## Question

The curves \(C_1\) and \(C_2\) are defined by \[y=e^{-x}\qquad (x>0)\qquad \text{and}\qquad y=e^{-x}\sin x \qquad (x>0),\] respectively. Sketch roughly \(C_1\) and \(C_2\) on the same diagram.

Let \(x_n\) denote the \(x\)-coordinate of the \(n\)th point of contact between the two curves, where \(0<x_1< x_2<\dotsb\), and let \(A_n\) denote the area of the region enclosed by the two curves between \(x_n\) and \(x_{n+1}\). Show that \[A_n=\frac{1}{2}\left(e^{2\pi}-1\right)e^{-(4n+1)\pi/2}\] and hence find \(\displaystyle\sum\limits_{n=1}^{\infty} A_n\).

## Suggestion

When does \(e^{-x}\sin x\) equal \(e^{-x}\)?

Where do the points \(x_n\) occur?

If we look at the area that forms \(A_1\) on your graph, how can we write that in terms of integrals? What about \(A_n\)?

How could we find \(I = \int e^{-x}\sin x \,dx\)? Could we use integration by parts twice?

…and hence find \(\displaystyle\sum\limits_{n=1}^{\infty} A_n\).

Could we write out the first few terms of the infinite sum \(\sum\limits_{n=1}^{\infty} A_n\)?

What’s the expression for the infinite sum in this case? Can we spot a geometric series anywhere? What’s the sum to infinity for this?

## Solution

For \(C_1\) and \(C_2\), we need the parts of these curves that satisfy \(x > 0\).

The two curves \(\,y=e^{-x}\) and \(\,y=-e^{-x}\) form what is known as an `envelope’ around \(\,y=e^{-x}\sin x\).

First we need to know what the points \(x_n\) are. Solving \[e^{-x}=e^{-x}\sin x,\qquad \left(e^{-x}\neq 0 \right)\] \[\Longrightarrow \sin x = 1 \qquad \Longrightarrow \qquad x_1=\frac{\pi}{2},\, x_2=2\pi+\frac{\pi}{2} \dotsb\] Thus \[x_n=2\pi(n-1)+\frac{\pi}{2}=\frac{1}{2}(4n-3)\pi\] and \[A_n=\int_{\frac{1}{2}(4n-3)\pi}^{\frac{1}{2}(4n+1)\pi}\,e^{-x}\left(1-\sin x\right)\,dx,\] the difference between the two curves \(C_1\) and \(C_2\). This can be seen below.

Consider

\(I=\int e^{-x}\sin x\,dx\)

. We can solve this via integration by parts, with

\(u=\sin x\)

and

\(v'=e^{-x}\)

:

\[\begin{align*} I &= \int e^{-x}\sin x \,dx \\ &= \left[-e^{-x}\sin x \right] + \int e^{-x}\cos x \,dx \\ &= \left[-e^{-x}\sin x \right] + \left[-e^{-x}\cos x \right] - \int e^{-x}\sin x \,dx \, \, \text{ (by integrating the integral above by parts again)}\\ &= \left[-e^{-x}\sin x \right] + \left[-e^{-x}\cos x \right] - I\\ \Longrightarrow \quad 2I &= -e^{-x}\left(\sin x+ \cos x\right)\\ \Longrightarrow \quad I &= -\frac{1}{2}e^{-x}\left(\sin x+ \cos x\right) \end{align*}\]

Thus

\[\begin{align*} A_n &=\int_{x_n}^{x_{n+1}}\,e^{-x}\left(1-\sin x\right)\,dx \\ &= \int_{\frac{1}{2}(4n-3)\pi}^{\frac{1}{2}(4n+1)\pi} \,e^{-x}\,dx - \int_{\frac{1}{2}(4n-3)\pi}^{\frac{1}{2}(4n+1)\pi} \,e^{-x}\sin x\,dx \\ &= \left[-e^{-x} + \frac{1}{2}e^{-x}\left(\sin x+ \cos x\right)\right]_{\frac{1}{2}(4n-3)\pi}^{\frac{1}{2}(4n+1)\pi} \, \, \text{(recognising the second integral above as $I$)}\\ &= \left[\frac{1}{2}e^{-x}\left(\sin x+ \cos x-2\right)\right]_{\frac{1}{2}(4n-3)\pi}^{\frac{1}{2}(4n+1)\pi} \\ &= \frac{1}{2}e^{-\frac{1}{2}(4n+1)\pi}\left[\sin \left(2n\pi+\frac{\pi}{2}\right) + \cos \left(2n\pi+\frac{\pi}{2}\right) -2\right] \\ &\quad - \frac{1}{2}e^{-\frac{1}{2}(4n+1)\pi}e^{2\pi}\left[\sin \left(2(n-1)\pi+\frac{\pi}{2}\right) + \cos \left(2(n-1)\pi+\frac{\pi}{2}\right) -2\right]. \end{align*}\]

With

\(\,\sin\left(2n\pi + \frac{\pi}{2}\right)=\sin\frac{\pi}{2}=1\)

and

\(\,\cos\left(2n\pi + \frac{\pi}{2}\right)=\cos\frac{\pi}{2}=0\)

for all integers

\(n\)

, we find

\[\begin{align*} A_n &= \frac{1}{2}e^{-\frac{1}{2}(4n+1)\pi}\left(1 + 0 -2 \right) - \frac{1}{2}e^{-\frac{1}{2}(4n+1)\pi}e^{2\pi}\left(1 + 0 -2\right) \\ &= \frac{1}{2}e^{-\frac{1}{2}(4n+1)\pi}\left(-1 +e^{2\pi} \right) \\ &= \frac{1}{2}\left(e^{2\pi} -1\right)e^{-\frac{1}{2}(4n+1)\pi}, \end{align*}\]

as required.

[…] and hence find \(\displaystyle\sum\limits_{n=1}^{\infty} A_n\).

Let

\(\,A=\displaystyle\sum\limits_{n=1}^{\infty} A_n\)

. Then

\[\begin{align*} A &= \sum\limits_{n=1}^{\infty} \frac{1}{2}\left(e^{2\pi} -1\right)e^{-\frac{1}{2}(4n+1)\pi} \\ A &= \frac{1}{2}\left(e^{2\pi} -1\right) \sum\limits_{n=1}^{\infty} e^{-2n\pi}e^{-\frac{\pi}{2}} \\ A &= \frac{1}{2}\left(e^{2\pi} -1\right) e^{-\frac{\pi}{2}} \sum\limits_{n=1}^{\infty} (e^{-2\pi})^n \\ A &= \frac{1}{2}\left(e^{2\pi} -1\right) e^{-\frac{\pi}{2}} \left[e^{-2\pi} + (e^{-2\pi})^2 + (e^{-2\pi})^3 + \dotsb\right]\\ A &= \frac{1}{2}\left(e^{2\pi} -1\right) e^{-\frac{\pi}{2}} e^{-2\pi} \left[1+ e^{-2\pi} + (e^{-2\pi})^2 + \dotsb\right] \end{align*}\]

We therefore have the infinite sum of a geometric series, with first term

\(\,a=\frac{1}{2}\left(e^{2\pi} -1\right) e^{-\frac{5\pi}{2}}\)

and ratio

\(\,r=e^{-2\pi}\)

. Since

\(\,2\pi > 0\)

,

\(e^{-2\pi}<1\)

and the series converges, with infinite sum

\(\,S_{\infty}=\frac{a}{1-r}\)

. Therefore

\[\begin{align*} A &= \frac{1}{2}\left(e^{2\pi} -1\right) e^{-\frac{5\pi}{2}}\times \frac{1}{1-e^{-2\pi}} \\ &= \frac{1}{2}\left(e^{2\pi} -1\right) e^{-\frac{5\pi}{2}} \times \frac{e^{2\pi}}{e^{2\pi}-1} \\ &= \frac{1}{2}e^{-\frac{5\pi}{2}} \times e^{2\pi} = \frac{1}{2}e^{-\frac{\pi}{2}}. \end{align*}\]

So \(\displaystyle\sum\limits_{n=1}^{\infty} A_n = \frac{1}{2}e^{-\frac{\pi}{2}}\).
