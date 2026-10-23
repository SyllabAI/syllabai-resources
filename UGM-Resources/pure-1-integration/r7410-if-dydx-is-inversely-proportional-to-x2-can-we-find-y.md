---
created: 2026-10-24T04:45:46 (UTC +06:00)
source: https://undergroundmathematics.org/product-rule/r7410
author: Underground Mathematics (University of Cambridge)
rights: © University of Cambridge (Underground Mathematics). Use inside SyllabAI is authorised by the
  operator attestation of 2026-10-23 — see LICENSE-DATA.md (Amendment 2026-10-23) in this repository.
  Takedown / correction handling as stated in LICENSE-DATA.md.
tags:
- underground-mathematics
- product-rule
- type/review-question
resource_identity:
  ugm_id: r7410
  station: product-rule
  station_title: Product Rule & Integration by Parts
  resource_type_id: 10
  resource_type_label: Review question
  level: null
  ref: 7410
  old_site_id: Q1039
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
  - code: 1.8.2
    provenance:
      tier: AI_SUGGESTED
      confidence: medium
      model_version: "GLM (Super Z agent, z.ai) — P3c lane-8 cross-map (cross-map-integration.json (P3c lane 8) @ syllabai-experimental c04abfbd)"
      evidence: "part (ii) integrates dy/dx = 4/x^2 to y = -4/x + d and evaluates d from y(2)=1 — reverse-process integration of x^(-2) with constant-of-integration evaluation; part (i) is product-rule turning-point work (1.7.4-dressed)"
      rationale: "Canonical UGM title: \"If $dy/dx$ is inversely proportional to $x^2$, can we find $y$?\"; exam provenance: UCLES O level Additional Mathematics 1, QP 471/1, 1969, Q4"
      validation_status: SUGGESTED
    title: "solve problems involving the evaluation of a constant of integration"
  mapped_date: '2026-10-24'
  mapper: cross-map-integration.json (P3c lane 8) @ syllabai-experimental c04abfbd
provenance:
  capture_date: '2026-10-22'
  capture_tool: P2 full-site crawl (ugm-crawl) → ugm-clean extraction; text-only import
  content_language: en
  exam_reference: "UCLES O level Additional Mathematics 1, QP 471/1, 1969, Q4"
task: T-UGM-IMPORT-8
---

# If $dy/dx$ is inversely proportional to $x^2$, can we find $y$?

## Question

1. Show that the curve \(y=x(5-x)^4\) has a turning point where \(x=5\). Determine whether this turning point is a maximum or a minimum.

---

1. It is given that that \(\dfrac{dy}{dx}\) is inversely proportional to \(x^2\) and that \(y\) and \(\dfrac{dy}{dx}\) are each equal to \(1\) when \(x=2\). Express \(y\) in terms of \(x\).

## Suggestion

How can we find the turning points of a function?

What methods do we know for determining the nature of a turning point?

Which method works best in this case?

What does it mean for \(a\) to be inversely proportional to \(b\)? Can you write this mathematically?

Can we now replace \(a\) with \(\dfrac{dy}{dx}\), and \(b\) with \(x^2\), and use the information in the question?

## Solution

Using the Product Rule, we have that

\[\begin{align*} \frac{dy}{dx}&=(5-x)^4-4x(5-x)^3\\ &=(5-x)^3[5-x-4x] \\ &=5(5-x)^3(1-x). \end{align*}\]

We see that \(\dfrac{dy}{dx}\) vanishes when \(x=5\), therefore \((5,0)\) is a turning point.

We can see from the expression for \(\dfrac{dy}{dx}\) that \(\dfrac{d^2y}{dx^2}\) will also vanish at \((5,0)\), so calculating this won’t help decide if we have a maximum or a minimum.

Let’s instead look at the expression for \(y\).

We know that when \(x=5\), \(y=0\).

When \(x\) is slightly smaller than \(5\), \(y\) is positive, and the same is true when \(x\) is slightly larger than \(5\), as \(x\) and \((5-x)^4\) are both positive.

Therefore \((5,0)\) is a local minimum for \(y\).

If \(\dfrac{dy}{dx}\) is inversely proportional to \(x^2\), then we can write \[\frac{dy}{dx}=\frac{c}{x^2}.\] Since \(\dfrac{dy}{dx}=1\) when \(x=2\), we see that \(c=4\), and so \[\frac{dy}{dx}=\frac{4}{x^2}.\] We now integrate this, and see that \[y=-\frac{4}{x}+d.\] Using that \(y=1\) when \(x=2\), we see that \(d=3\).

Therefore \(y=3-\dfrac{4}{x}\).
