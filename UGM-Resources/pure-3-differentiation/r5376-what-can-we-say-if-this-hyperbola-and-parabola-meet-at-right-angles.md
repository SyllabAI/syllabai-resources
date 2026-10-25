---
created: 2026-10-25T21:48:43 (UTC +06:00)
source: https://undergroundmathematics.org/chain-rule/r5376
author: Underground Mathematics (University of Cambridge)
rights: © University of Cambridge (Underground Mathematics). Use inside SyllabAI is authorised by the
  operator attestation of 2026-10-23 — see LICENSE-DATA.md (Amendment 2026-10-23) in this repository.
  Takedown / correction handling as stated in LICENSE-DATA.md.
tags:
- underground-mathematics
- chain-rule
- type/review-question
resource_identity:
  ugm_id: r5376
  station: chain-rule
  station_title: Chain Rule & Integration by Substitution
  resource_type_id: 10
  resource_type_label: Review question
  level: null
  ref: 5376
  old_site_id: Q27
spec_map:
  curriculum_code: CIE-9709-P3-2023
  lane: cie-a-level-maths-20-pure-3
  board: Cambridge CIE
  syllabus_version: 2023-2025
  subsection: chain-rule
  subsection_provenance:
    tier: PROVIDER
    signal: source-url-slug
    slug: chain-rule
    validation_status: SUGGESTED
  spec_points:
  - code: 3.4.3
    provenance:
      tier: AI_SUGGESTED
      confidence: high
      model_version: GLM (Super Z agent, z.ai) — P3c lane-12 cross-map (cross-map-p3-differentiation.json
        (P3c lane 12) @ syllabai-experimental 506ea24f8e61cc75c4662f8ebb08cfd2b1d458d4)
      evidence: y^2 = 4ax and xy = c^2 intersecting at right angles via their derivatives, giving c^4
        = 32a^4 and TG = 6a - implicit/parametric derivative work on both curves
      rationale: 'Canonical UGM title: What can we say if this hyperbola and parabola meet at right angles?'
      validation_status: SUGGESTED
    title: find and use the first derivative of a function e.g. which is defined parametrically or implicitly.
  mapped_date: '2026-10-25'
  mapper: cross-map-p3-differentiation.json (P3c lane 12) @ syllabai-experimental 506ea24f8e61cc75c4662f8ebb08cfd2b1d458d4
provenance:
  capture_date: '2026-10-22'
  capture_tool: P2 full-site crawl (ugm-crawl) → ugm-clean extraction; text-only import
  content_language: en
  task: T-UGM-IMPORT-12
---

# What can we say if this hyperbola and parabola meet at right angles?

## Question

The curves \(y^2=4ax\) and \(xy=c^2\) intersect at right angles. Prove that

1. \(c^4=32a^4\) and

---

1. if the tangent and normal to either curve at the point of intersection meet the \(x\)-axis at \(T\) and \(G\), then \(TG=6a\).

## Suggestion

The curves \(y^2=4ax\) and \(xy=c^2\) intersect at right angles. Prove that (i) \(c^4=32a^4\)

What do the curves \(y^2=4ax\) and \(xy=c^2\) look like? Could we sketch a diagram?

If the curves meet at \((p,q)\), what are the gradients of the curves there?

What condition on the slopes of two lines corresponds to them being at right angles?

What are the equations of the tangent and normal?

Where do these lines meet the \(x\)-axis?

## Solution

The curves \(y^2=4ax\) and \(xy=c^2\) intersect at right angles. Prove that (i) \(c^4=32a^4\)

Let the point of intersection be

\((p,q)\)

. Thus

\[\begin{equation} q^2 = 4ap \text{, and } pq=c^2.\label{eq:intersection} \end{equation}\]

Using implicit differentiation on \(y^2 =4ax\), we have \(2y\dfrac{dy}{dx} = 4a\), so the gradient at \((p,q)\) is \(\dfrac{dy}{dx} = \dfrac{2a}{q}\).

Similarly, differentiating \(xy=c^2\), we have \(y+x\dfrac{dy}{dx} = 0\), so \(\dfrac{dy}{dx}= \dfrac{-y}{x}\), and the gradient at \((p,q)\) is \(\dfrac{-q}{p}\).

Since the curves are at right angles at \((p,q)\), we have \(\dfrac{2a}{q}\times\dfrac{-q}{p}=-1\), which simplifies to \(p = 2a\).

Combining this with \(\eqref{eq:intersection}\) we have \(q^2 = 8a^2\), and since \(p^2q^2=c^4\) we have \((2a)^28a^2 = c^4\), or \(c^4=32a^4\), as required.

Prove that (ii) if the tangent and normal to either curve at the point of intersection meet the \(x\)-axis at \(T\) and \(G\), then \(TG=6a\).

The tangent and normal both pass through \((p,q)\) and have gradients \(\dfrac{2a}{q}\) and \(\dfrac{-q}{p}\). So we can write their equations as \[x-p = \dfrac{2a}{q}(y-q),\qquad\text{and}\quad x-p = \dfrac{-q}{p}(y-q) .\]

Let these lines meet the \(x\)-axis at \((x_1,0)\) and \((x_2,0)\). Then we have \[x_1-p = -\dfrac{2a}{q}q,\qquad\text{and}\quad x_2-p = \dfrac{q}{p}q .\]

Subtracting these two and substituting from \(\eqref{eq:intersection}\), \[x_2-x_1 = \frac{q^2}{p}+2a = \frac{4ap}{p}+2a = 6a\] as required.

We have the two lines $$x-p = m_1(y-q),\qquad x-p = m_2(y-q)$$ where $m_1$ is the gradient of the hyperbola, and $m_2$ is the gradient of the parabola, both evaluated at $(p,q)$. These meet the $x$-axis when $y=0$. Let these points be at $x_1$ and $x_2$ respectively -- we can be sure from the graph that $x_1>x_2$. Subtracting the two equations, we get $$(x_1-p) - (x_2-p) = -q(m_1-m_2)$$ or $$x_1 - x_2 = -q(m_1-m_2).$$ Now $m_1=-\dfrac{q}{p}$ and $m_2=\dfrac{q}{2a}$ so $$x_1 - x_2 = -q\left(-\frac{2a}{q}-\frac{q}{2a}\right) = \frac{4a^2+q^2}{2a} = \frac{4a^2 + 8a^2}{2a} = 6a,$$ as required.
