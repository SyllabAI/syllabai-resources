---
created: 2026-10-26T02:40:04 (UTC +06:00)
source: https://undergroundmathematics.org/product-rule/r6620
author: Underground Mathematics (University of Cambridge)
rights: © University of Cambridge (Underground Mathematics). Use inside SyllabAI is authorised by the
  operator attestation of 2026-10-23 — see LICENSE-DATA.md (Amendment 2026-10-23) in this repository.
  Takedown / correction handling as stated in LICENSE-DATA.md.
tags:
- underground-mathematics
- product-rule
- type/review-question
resource_identity:
  ugm_id: r6620
  station: product-rule
  station_title: Product Rule & Integration by Parts
  resource_type_id: 10
  resource_type_label: Review question
  level: null
  ref: 6620
  old_site_id: Q1024
spec_map:
  curriculum_code: CIE-9709-P3-2023
  lane: cie-a-level-maths-20-pure-3
  board: Cambridge CIE
  syllabus_version: 2023-2025
  subsection: product-rule
  subsection_provenance:
    tier: PROVIDER
    signal: source-url-slug
    slug: product-rule
    validation_status: SUGGESTED
  spec_points:
  - code: 3.5.5
    provenance:
      tier: AI_SUGGESTED
      confidence: high
      model_version: GLM (Super Z agent, z.ai) — P3c lane-13 cross-map (cross-map-p3-integration.json
        (P3c lane 13) @ syllabai-experimental 21845f3)
      evidence: 'C1 from its gradient dy/dx = x(1-x^2)e^(-x^2): the y(+/-1) coordinates REQUIRE integrating
        - the of-record solution integrates by parts (dv/dx = xe^(-x^2), v = -e^(-x^2)/2) giving y = (1/2)x^2
        e^(-x^2), the trial-solution method beside it; the C2 coda where both methods fail is the honest
        disclosure (flips the lane-10 ''P3 3.4/3.5'' and lane-12 ''P3 3.5 Integration'' rows of record)'
      rationale: 'Canonical UGM title: If the gradient is $x(1-x^2)e^{-x^2}$ can we find the stationary
        points?'
      validation_status: SUGGESTED
    title: recognise when an integrand can usefully be e.g. integration of regarded as a product, and
      use integration by parts
  mapped_date: '2026-10-26'
  mapper: cross-map-p3-integration.json (P3c lane 13) @ syllabai-experimental 21845f3
provenance:
  capture_date: '2026-10-22'
  capture_tool: P2 full-site crawl (ugm-crawl) → ugm-clean extraction; text-only import
  content_language: en
  task: T-UGM-IMPORT-13
---

# If the gradient is $x(1-x^2)e^{-x^2}$ can we find the stationary points?

## Question

The curve \(C_1\) passes through the origin in the \(x\text{-}y\) plane and its gradient is given by \[\frac{dy}{dx}=x(1-x^2)e^{-x^2}.\] Show that \(C_1\) has a minimum point at the origin and a maximum point at \((1,\frac{1}{2}e^{-1})\). Find the coordinates of the other stationary point. Give a rough sketch of \(C_1\).

The curve \(C_2\) passes through the origin in the \(x\text{-}y\) plane and its gradient is given by \[\frac{dy}{dx}=x(1-x^2)e^{-x^3}.\] Show that \(C_2\) has a minimum point at the origin and a maximum point at \((1,k)\), where \(k>\frac{1}{2}e^{-1}\). (You need not find \(k\).)

## Suggestion

What condition is required for a stationary point, and how do we classify them?

To find the coordinates of the maxima, we need to know \(y\) as a function of \(x\). What form do you think the function will take?

Other things to consider when sketching this function:

1. what happens as \(x \rightarrow \pm\infty\)?

---

1. is this function even or odd (or neither)?

Can we find the \(x\) coordinates of the stationary points? Can we classify them?

Can we prove the inequality involving \(k\) by comparing with the function \(C_1\)?

## Solution

\[\frac{dy}{dx}=x(1-x^2)e^{-x^2}.\]

This is zero when

\(x=0,\pm 1\)

. To classify these stationary points we need the second derivative:

\[\begin{align*} \frac{d^2y}{dx^2} &= (1-x^2)e^{-x^2}+x(-2x)e^{-x^2}-2x^2(1-x^2)e^{-x^2}\\ &= (1-5x^2+2x^4)e^{-x^2}. \end{align*}\]

Thus

\[\begin{align*} y''(0) &= 1 > 0 \quad \Longrightarrow \quad \text{this is a minimum point,} \\ y''(-1)=y''(1) &= (1-5+2)e^{-1} = -\frac{2}{e} < 0 \quad \Longrightarrow \quad \text{these are maximum points.} \end{align*}\]

Since we know the curve passes through the origin, \((0,0)\) must be a minimum point.

To find the coordinates of the other stationary points we need to know the values of \(y(\pm1)\) which requires us to integrate the given expression. There are (at least) two different ways of doing this.

Method 1: integration by parts

Let’s try to integrate

\(x(1-x^2)e^{-x^2}\)

by parts.

Remember that the formula for integration by parts is \[\int u\frac{dv}{dx}\:dx=uv-\int v\frac{du}{dx}\:dx\]

Notice that \(xe^{-x^2}\) is the derivative of \(-\frac{1}{2}e^{-x^2}\). So let’s set \[\frac{dv}{dx}=xe^{-x^2}, \implies v=-\frac{1}{2}e^{-x^2},\] and \[u=1-x^2, \implies \frac{du}{dx}=-2x.\]

So we have that

\[\begin{align*} y=\int x(1-x^2)e^{-x^2}\:dx &= -\frac{1}{2}(1-x^2)e^{-x^2}-\int x e^{-x^2}\:dx\\ &=-\frac{1}{2}(1-x^2)e^{-x^2}+\frac{1}{2}e^{-x^2}=\frac{1}{2}x^2e^{-x^2}. \end{align*}\]

Notice that we don’t need to add a constant because the curve passes though the origin (or we could say the constant of integration is 0).

Method 2: trial solution

We’ll guess at a solution of the form

\(y=(ax^2+bx+c)e^{-x^2}\)

.

From the work above finding \(\frac{d^2y}{dx^2}\) we can see that differentiating an expression of this form tends to increase the degree of the leading polynomial by one. So when integrating, we expect the leading cubic to become a quadratic.

\[\begin{align*} \frac{dy}{dx} &= (2ax+b)e^{-x^2}-2x\left(ax^2+bx+c\right)e^{-x^2} \\ &= \left(-2ax^3-2bx^2+2(a-c)x+b\right)e^{-x^2} \end{align*}\]

Comparing coefficients with \(\dfrac{dy}{dx}=x(1-x^2)e^{-x^2}\), we find that

\[\begin{align*} b &= 0,\\ -2a &= -1 ,\quad \Longrightarrow \quad a=\frac{1}{2},\\ 2\left(\frac{1}{2}-c\right) &= 1\quad \Longrightarrow \quad c=0 \end{align*}\]

Thus \[y=\frac{1}{2}x^2e^{-x^2},\] which we can see satisfies the boundary condition \(x=0,\,y=0.\)

Our maxima are therefore found at \(\left(\pm 1,\dfrac{1}{2e}\right)\). Furthermore, the function is [even](https://undergroundmathematics.org/glossary/even-function), that is \(f(-x)=f(x)\) for all \(x\); and as \(x \rightarrow \pm\infty\), \(y \rightarrow 0\).

So now \[\frac{dy}{dx}=x(1-x^2)e^{-x^3}.\]

Note the change from \(-x^2\) to \(-x^3\) in the power of \(e\) means this becomes a really hard differential equation to solve.

The methods we used above both fail. Fortunately we can complete the question without directly solving this equation.

The stationary points are again at

\(x=0,\,\pm 1\)

. Classifying these:

\[\begin{align*} \frac{d^2y}{dx^2} &= \left(1-x^2\right)e^{-x^3} -2x^2e^{-x^3} -3x^3\left(1-x^2\right)e^{-x^3} \\ &= \left(1-3x^2-3x^3+3x^5\right)e^{-x^3}. \end{align*}\]

Thus

\[\begin{align*} y''(0) &= 1 > 0 \quad \Longrightarrow \quad \text{this is a minimum point,} \\ y''(\pm1) &= (1-3\mp3\pm3)e^{-1} = -\frac{2}{e} < 0 \quad \Longrightarrow \quad \text{these are maximum points.} \end{align*}\]

Now we need to show the maximum point at \((1,k)\) satisfies \(k>\frac{1}{2}e^{-1}\). We cannot evaluate the function directly, but we know that the curve passes through the origin, like \(C_1\), and that \(C_1\) has a maximum at \((1,\frac{1}{2}e^{-1})\). So we know \(C_1\) reaches this point, and we want to show \(C_2\) goes above it. For \(0<x<1\), we have:

\[\begin{align*} x^2 &> x^3 \\ \Longrightarrow \quad -x^2 &< -x^3 \\ \Longrightarrow x(1-x^2)e^{-x^2} &< x(1-x^2)e^{-x^3}. \end{align*}\]

So the derivative of \(C_2\) is greater than that of \(C_1\) in this range. That means that \(C_2\)’s \(y\) value is “growing” faster than \(C_1\)’s between the origin and the maximum point at \(x=1\), so its maximum point will have greater \(y\)-coordinate, that is to say, the maximum occurs at \((1,k)\), where

\[k>\frac{1}{2}e^{-1}\]
