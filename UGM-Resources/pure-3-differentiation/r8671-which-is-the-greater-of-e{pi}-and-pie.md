---
created: 2026-10-25T21:48:43 (UTC +06:00)
source: https://undergroundmathematics.org/product-rule/r8671
author: Underground Mathematics (University of Cambridge)
rights: © University of Cambridge (Underground Mathematics). Use inside SyllabAI is authorised by the
  operator attestation of 2026-10-23 — see LICENSE-DATA.md (Amendment 2026-10-23) in this repository.
  Takedown / correction handling as stated in LICENSE-DATA.md.
tags:
- underground-mathematics
- product-rule
- type/review-question
resource_identity:
  ugm_id: r8671
  station: product-rule
  station_title: Product Rule & Integration by Parts
  resource_type_id: 10
  resource_type_label: Review question
  level: null
  ref: 8671
  old_site_id: Q182
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
  - code: 3.4.1
    provenance:
      tier: AI_SUGGESTED
      confidence: high
      model_version: GLM (Super Z agent, z.ai) — P3c lane-12 cross-map (cross-map-p3-differentiation.json
        (P3c lane 12) @ syllabai-experimental 506ea24f8e61cc75c4662f8ebb08cfd2b1d458d4)
      evidence: stationary point of x^(1/x) via d/dx(ln y) = (1 - ln x)/x^2 - ln/composite 3.4.1 work
        deciding e^pi > pi^e without a calculator (flips the lane-10 non-overlap row of record routed
        'P3 3.4 Differentiation')
      rationale: 'Canonical UGM title: Which is the greater of $e^{\pi}$ and $\pi^e$?'
      validation_status: SUGGESTED
    title: use the derivatives of e , ln x , sin x , cos x , tan x , tan x , together with constant multiples,
      sums, differences and composites
  mapped_date: '2026-10-25'
  mapper: cross-map-p3-differentiation.json (P3c lane 12) @ syllabai-experimental 506ea24f8e61cc75c4662f8ebb08cfd2b1d458d4
provenance:
  capture_date: '2026-10-22'
  capture_tool: P2 full-site crawl (ugm-crawl) → ugm-clean extraction; text-only import
  content_language: en
  task: T-UGM-IMPORT-12
---

# Which is the greater of $e^{\pi}$ and $\pi^e$?

## Question

Show that for \(x>0\), \(x^{1/x}\) has its greatest value when \(x=e\).

Hence, or otherwise, but without use of a calculator, determine which is the greater of \(e^{\pi}\) and \(\pi^e\).

## Suggestion

How would you differentiate an exponential function such as \(2^x\)?

Could you apply a modification of that technique here?

Could we write \(x^{1/x}\) as “\(e\) to the power something”?

## Solution

Let’s write

\(y=x^{1/x}\)

, and take the natural logarithm of both sides, giving

\[\ln y=\frac{1}{x} \ln x.\]

Differentiating this with respect to

\(x\)

using the product and chain rules gives

\[\begin{align*} \frac{1}{y} \frac{dy}{dx}&=-\frac{1}{x^2}\ln x+\frac{1}{x^2}\\ &=\frac{1-\ln x}{x^2} \end{align*}\]

so \[\frac{dy}{dx}=\frac{y(1-\ln x)}{x^2}=\frac{x^{1/x}(1-\ln x)}{x^2}.\] Turning points occur when \(\dfrac{dy}{dx}=0\), which is precisely when \[1-\ln x=0,\] as \(x^{1/x}\) is never zero for \(x>0\). So \(\ln x=1\), and the only stationary point is at \(x=e\).

Alternatively we can say, let \(x^{1/x} = e^{f(x)}.\) Taking natural logs shows that \(f(x) = \dfrac{\ln x}{x}\).

We can now differentiate \(y = e^{f(x)}\) using the chain and quotient rules.

To determine the nature of the stationary point, we’ll look at the value of \(y\) or \(\dfrac{dy}{dx}\) either side of \(x=e\).

We have \(\dfrac{dy}{dx}=\dfrac{x^{1/x}(1-\ln x)}{x^2},\) and since \(x^{1/x}\) and \(x^2\) are always positive for \(x>0\), the sign of the derivative is determined by the sign of \(1-\ln x\).

So when \(x<e\), \(\dfrac{dy}{dx}>0\) and the function is increasing; when \(x>e\), \(\dfrac{dy}{dx}<0\) and the function is decreasing.

Therefore the function has a maximum at \(x=e\), and this is the global maximum of the function.

From our argument above, we must have \(\pi^{1/\pi} < e^{1/e}\).

Raising both sides to the power \(e \pi\) gives \(\pi^e<e^{\pi}\) (this step is valid, since the function \(f(x)=x^{e \pi}\) is strictly increasing for \(x > 0\)).

So \(e^{\pi}\) is larger.
