---
created: 2026-10-24T04:45:46 (UTC +06:00)
source: https://undergroundmathematics.org/calculus-meets-functions/r5090
author: Underground Mathematics (University of Cambridge)
rights: © University of Cambridge (Underground Mathematics). Use inside SyllabAI is authorised by the
  operator attestation of 2026-10-23 — see LICENSE-DATA.md (Amendment 2026-10-23) in this repository.
  Takedown / correction handling as stated in LICENSE-DATA.md.
tags:
- underground-mathematics
- calculus-meets-functions
- type/review-question
resource_identity:
  ugm_id: r5090
  station: calculus-meets-functions
  station_title: Calculus meets Functions
  resource_type_id: 10
  resource_type_label: Review question
  level: null
  ref: 5090
  old_site_id: None
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
  - code: 1.8.3
    provenance:
      tier: AI_SUGGESTED
      confidence: medium
      model_version: "GLM (Super Z agent, z.ai) — P3c lane-8 cross-map (cross-map-integration.json (P3c lane 8) @ syllabai-experimental c04abfbd)"
      evidence: "bilateral-function question proves the order-reversal identity for polynomial definite integrals and reasons about G(t) as a signed area — polynomial definite integration is load-bearing (extension-style framing)"
      rationale: "Canonical UGM title: \"What does it mean if a function $f(x)=f(2\\alpha-x)$?\""
      validation_status: SUGGESTED
    title: "evaluate definite integrals"
  mapped_date: '2026-10-24'
  mapper: cross-map-integration.json (P3c lane 8) @ syllabai-experimental c04abfbd
provenance:
  capture_date: '2026-10-22'
  capture_tool: P2 full-site crawl (ugm-crawl) → ugm-clean extraction; text-only import
  content_language: en
task: T-UGM-IMPORT-8
---

# What does it mean if a function $f(x)=f(2\alpha-x)$?

## Question

In this question we fix a real number \(\alpha\) which will be the same throughout. We say that a function \(f\) is *bilateral* if \[f(x) = f(2\alpha - x)\] for all \(x\).

1. Show that if \(f(x) = (x-\alpha)^2\) for all \(x\) then the function \(f\) is bilateral.

---

1. On the other hand, if \(f(x) = x-\alpha\) for all \(x\) then the function \(f\) is not bilateral.

---

1. Show that if \(n\) is a non-negative integer and \(a\) and \(b\) are any real numbers then \[\int_a^b x^n \:dx = -\int_b^a x^n \:dx.\]

---

1. Hence show that if \(f\) is a polynomial (and \(a\) and \(b\) are any reals) then \[\int_a^b f(x) \:dx = -\int_b^a f(x) \:dx.\]

---

1. Suppose that \(f\) is any bilateral function. By considering the area under the curve \(y = f(x)\) explain why for any \(t \geq \alpha\) we have \[\int_\alpha^t f(x) \:dx = \int_{2\alpha-t}^\alpha f(x) \:dx.\]

If \(f\) is a function we write \(G\) for the function defined by \[G(t) = \int_\alpha^t f(x) \:dx\] for all \(t\).

1. Suppose now that \(f\) is any bilateral function. Show that \[G(t) = -G(2\alpha-t)\] for all \(t\).

---

1. Suppose that \(f\) is a bilateral polynomial such that \(G\) is also bilateral. Show that \(G(x) = 0\) for all \(x\).

## Solution

We have \[f(x) = f(2\alpha - x) \iff f((x-\alpha)+\alpha)= f(-(x-\alpha)+\alpha),\] and so \(f(x)\) is bilateral if and only if \(x=\alpha\) is a line of symmetry for the curve \(y=f(x)\).

In the special case of \(\alpha=0\), this would mean that \(f\) is an even function.

If \(f(x) = (x-\alpha)^2\), then \[f(2\alpha - x) = ((2\alpha - x) -\alpha)^2 = (\alpha-x)^2 = (x-\alpha)^2 = f(x),\] for all \(x\), and so \(f\) is bilateral.

If \(f(x) = x-\alpha\), then \[f(2\alpha - x) = ((2\alpha - x) -\alpha) = (\alpha-x) = -f(x),\] for all \(x\), and so \(f\) is not bilateral.

The only solution to \(f(x) = -f(x)\) for all \(x\) is \(f(x) = 0\) for all \(x\), which is not the \(f(x)\) we have here.

We know \(\displaystyle\int_a^b x^n \:dx = \left[\dfrac{x^{n+1}}{n+1}\right]_a^b = \dfrac{b^{n+1}-a^{n+1}}{n+1}\).

We also know that \(\displaystyle\int_b^a x^n \:dx = \left[\dfrac{x^{n+1}}{n+1}\right]_b^a = \dfrac{a^{n+1}-b^{n+1}}{n+1}\).

Thus we have that \(\displaystyle\int_a^b x^n \:dx = -\displaystyle\int_b^a x^n \:dx\).

Let \(f(x)\) be the polynomial \(\sum\limits_{0}^{n} a_nx^n\). Then

\[\begin{align*} \int_a^b f(x) \:dx &= \int_a^b \sum_0^n a_nx^n \:dx \\ &= \sum_0^n \left(a_n\left(\int_a^b x^n \:dx\right)\right)\\ &= \sum_0^n \left(a_n\left(-\int_b^a x^n \:dx\right)\right)\\ &= -\int_b^a \sum_0^n a_nx^n \:dx\\ &= -\int_b^a f(x) \:dx. \end{align*}\]

1. Suppose that \(f\) is any bilateral function. By considering the area under the curve \(y = f(x)\) explain why for any \(t \geq \alpha\) we have \[\int_\alpha^t f(x) dx = \int_{2\alpha-t}^\alpha f(x) dx.\]

The symmetry of the bilateral function \(f(x)\) about \(x = \alpha\) guarantees that the two areas in the diagram above are equal, and so \[\int_\alpha^t f(x) \:dx = \int_{2\alpha-t}^\alpha f(x) \:dx.\]

Using the results from above we have

\[\begin{align*} -G(2\alpha-t) &= -\int_\alpha^{2\alpha-t} f(x) \:dx\\ &= \int_{2\alpha-t}^\alpha f(x) \:dx\\ &= \int_{\alpha}^t f(x) \:dx\\ &= G(t). \end{align*}\]

If \(f\) is bilateral, then \(G(t) = -G(2\alpha-t)\), but if \(G\) is bilateral, then \(G(2\alpha-t)=G(t)\).

Thus on adding these equations \(G(t) = 0\) for all \(t\) (or equivalently \(G(x) = 0\) for all \(x\)).
