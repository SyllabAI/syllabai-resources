---
created: 2026-10-24T01:49:53 (UTC +06:00)
source: https://undergroundmathematics.org/calculus-meets-functions/r9671
author: Underground Mathematics (University of Cambridge)
rights: © University of Cambridge (Underground Mathematics). Use inside SyllabAI is authorised by the
  operator attestation of 2026-10-23 — see LICENSE-DATA.md (Amendment 2026-10-23) in this repository.
  Takedown / correction handling as stated in LICENSE-DATA.md.
tags:
- underground-mathematics
- calculus-meets-functions
- type/review-question
resource_identity:
  ugm_id: r9671
  station: calculus-meets-functions
  station_title: Calculus meets Functions
  resource_type_id: 10
  resource_type_label: Review question
  level: null
  ref: 9671
  old_site_id: Q1066
spec_map:
  curriculum_code: CIE-9709-P1-2023
  lane: cie-a-level-maths-20-pure-1
  board: Cambridge CIE
  syllabus_version: 2023-2025
  subsection: calculus-meets-functions
  subsection_provenance:
    tier: PROVIDER
    signal: source-url-slug
    slug: calculus-meets-functions
    validation_status: SUGGESTED
  spec_points:
  - code: 1.7.2
    provenance:
      tier: AI_SUGGESTED
      confidence: high
      model_version: GLM (Super Z agent, z.ai) — P3c lane-7 cross-map (cross-map-differentiation.json
        (P3c lane 7) @ syllabai-experimental 93575e69)
      evidence: 'x^4y=8 with z=x+y: stationary value and its nature via z=x+8/x^4 — rational-power derivative
        in a constrained optimisation'
      rationale: 'Canonical UGM title: "When does this function of two variables have a minimum?"; exam
        provenance: UCLES AO level Additional Mathematics 2, 1984, Q4'
      validation_status: SUGGESTED
    title: use the derivative of x (for any rational n ), together with constant multiples, sums and
      differences of functions, and of composite functions using the chain rule
  - code: 1.7.4
    provenance:
      tier: AI_SUGGESTED
      confidence: high
      model_version: GLM (Super Z agent, z.ai) — P3c lane-7 cross-map (cross-map-differentiation.json
        (P3c lane 7) @ syllabai-experimental 93575e69)
      evidence: 'x^4y=8 with z=x+y: stationary value and its nature via z=x+8/x^4 — rational-power derivative
        in a constrained optimisation'
      rationale: 'Canonical UGM title: "When does this function of two variables have a minimum?"; exam
        provenance: UCLES AO level Additional Mathematics 2, 1984, Q4'
      validation_status: SUGGESTED
    title: locate stationary points and determine their nature, and use information about stationary
      points in sketching graphs.
  mapped_date: '2026-10-24'
  mapper: cross-map-differentiation.json (P3c lane 7) @ syllabai-experimental 93575e69
provenance:
  capture_date: '2026-10-22'
  capture_tool: P2 full-site crawl (ugm-crawl) → ugm-clean extraction; text-only import
  content_language: en
  exam_reference: UCLES AO level Additional Mathematics 2, 1984, Q4
task: T-UGM-IMPORT-7
---

# When does this function of two variables have a minimum?

## Question

The variables \(x\) and \(y\) are such that \(x^4y=8\). A third variable \(z\) is defined by \(z=x+y\).

Find the values of \(x\) and \(y\) that give \(z\) a stationary value and show that this value of \(z\) is a minimum.

## Suggestion

The variables \(x\) and \(y\) are such that \(x^4y=8\). A third variable \(z\) is defined by \(z=x+y\).

Find the values of \(x\) and \(y\) that give \(z\) a stationary value…

This looks tricky as \(z\) is given as a function of two variables. Can we use the equation connecting \(x\) and \(y\) to turn \(z\) into a function of just one variable?

How do we then calculate stationary points for \(z\)?

… and show that this value of \(z\) is a minimum.

What does the second derivative tell us about a stationary point?

## Solution

The variables \(x\) and \(y\) are such that \(x^4y=8\). A third variable \(z\) is defined by \(z=x+y\). Find the values of \(x\) and \(y\) that give \(z\) a stationary value…

We want to find the stationary points of \(z\), which (unfortunately) is a function of both \(x\) and \(y\).

But (luckily) we’ve been given a constraint connecting those two variables, namely, the first equation.

If

\(x=0\)

, the constraint wouldn’t be satisfied, so we can divide both sides by

\(x^4\)

to give

\[\begin{equation} y=8x^{-4}.\label{eq:1} \end{equation}\]

We can substitute this for

\(y\)

in the equation we are given for

\(z\)

to get

\[\begin{equation} z=x+8x^{-4}. \label{eq:2} \end{equation}\]

Here \(z\) is a function of \(x\) alone. From this we can calculate stationary points, by setting the first derivative equal to zero.

\[\begin{align*} z'(x) &= 1 - 32x^{-5} \\ \text{so} \qquad 1 - 32x^{-5} &= 0 \\ 1 &= 32x^{-5} \\ x^5 &= 32 \\ x &= 2. \end{align*}\]

As \(x=2\) is the only solution of \(x^5=32\), we only have one stationary point.

Substituting this value into equation

\(\eqref{eq:1}\)

gives us the corresponding

\(y\)

-value of our stationary point

\[y=\frac{8}{16}=\frac{1}{2}.\]

… and show that this value of \(z\) is a minimum.

To check whether \(z\) has a minimum when \(x=2\) and \(y=\dfrac{1}{2}\), we can look at the second derivative of \(z\) with respect to \(x\). A positive second derivative corresponds to a local minimum. From \(\eqref{eq:2}\) we obtain \[z''(x) = 160x^{-6},\] which gives \(z''(2)=2.5>0\) (or we could note that \(z''(x)\) is positive for all values of \(x\)). Therefore the value of \(z\) when \(x=2\) and \(y=\dfrac{1}{2}\) is indeed a minimum.
