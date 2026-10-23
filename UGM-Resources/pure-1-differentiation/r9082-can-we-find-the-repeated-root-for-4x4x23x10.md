---
created: 2026-10-24T01:49:53 (UTC +06:00)
source: https://undergroundmathematics.org/product-rule/r9082
author: Underground Mathematics (University of Cambridge)
rights: © University of Cambridge (Underground Mathematics). Use inside SyllabAI is authorised by the
  operator attestation of 2026-10-23 — see LICENSE-DATA.md (Amendment 2026-10-23) in this repository.
  Takedown / correction handling as stated in LICENSE-DATA.md.
tags:
- underground-mathematics
- product-rule
- type/review-question
resource_identity:
  ugm_id: r9082
  station: product-rule
  station_title: Product Rule & Integration by Parts
  resource_type_id: 10
  resource_type_label: Review question
  level: null
  ref: 9082
  old_site_id: Q51
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
  - code: 1.7.2
    provenance:
      tier: AI_SUGGESTED
      confidence: medium
      model_version: GLM (Super Z agent, z.ai) — P3c lane-7 cross-map (cross-map-differentiation.json
        (P3c lane 7) @ syllabai-experimental 93575e69)
      evidence: repeated root => root of f'(x)=0, applied to 4x^4+x^2+3x+1 — polynomial differentiation
        load-bearing; the general proof anticipates the product rule (P3 bearing recorded)
      rationale: 'Canonical UGM title: "Can we find the repeated root for  $4x^4+x^2+3x+1=0$?"; exam
        provenance: UCLES A level Further Mathematics 2, 1953, Q2'
      validation_status: SUGGESTED
    title: use the derivative of x (for any rational n ), together with constant multiples, sums and
      differences of functions, and of composite functions using the chain rule
  mapped_date: '2026-10-24'
  mapper: cross-map-differentiation.json (P3c lane 7) @ syllabai-experimental 93575e69
provenance:
  capture_date: '2026-10-22'
  capture_tool: P2 full-site crawl (ugm-crawl) → ugm-clean extraction; text-only import
  content_language: en
  exam_reference: UCLES A level Further Mathematics 2, 1953, Q2
task: T-UGM-IMPORT-7
---

# Can we find the repeated root for  $4x^4+x^2+3x+1=0$?

## Question

Prove that, if \(\alpha\) is a repeated root of \(f(x)=0\), where \(f(x)\) is a polynomial, then \(\alpha\) is a root of the equation \(f'(x)=0\).

Given that the equation \(4x^4+x^2+3x+1=0\) has a repeated root, find its value.

## Suggestion

If \(f\) has a repeated root at \(\alpha\), how can we write \(f\)? Can we now differentiate?

Can we apply the first part of the question, together with the Factor Theorem?

## Solution

Since we know that \(f(x)=0\) has a repeated root \(\alpha\), we may write \[f(x)=(x-\alpha)^2 g(x),\] where \(g(x)\) is some polynomial. By the product rule we have \[f'(x)=2(x-\alpha)g(x)+(x-\alpha)^2 g'(x)=(x-\alpha)\left[2g(x)+(x-\alpha)g'(x)\right],\] so we have that \(\alpha\) is a root of \(f'(x)=0\).

If \(f(x)=4x^4+x^2+3x+1\), then \[f'(x)=16x^3+2x+3.\]

We are told that \(f(x) = 0\) has a repeated root, which we may call \(\alpha\). From the above, we now know that \(\alpha\) is a root of \(f'(x) = 0\).

So we seek a root of \(16x^3+2x+3=0\).

Clearly the root \(x\) can’t be a whole number, since \(16x^3+2x\) would be even and \(3\) odd.

The coefficients \(16\) and \(2\) make us think the substitution \(x = \dfrac{y}{2}\) would be helpful, where \(y\) is a whole number.

That gives \(2y^3 + y + 3 = 0\), and clearly \(y = -1\) is a root here. We have \(2y^3 + y + 3 = (y + 1)(2y^2 -2y + 3)\).

Note the roots of the quadratic bracket are complex, since \(b^2 < 4ac\).

So the repeated root we seek must be \(-\dfrac{1}{2}\). We can check this, finding

\[f(x) = (2x + 1)(2x^3 - x^2 + x + 1) = (2x + 1)^2(x^2 - x + 1).\]

Alternatively, we could note that \(f'(0)\) = 3, and \(f'(-1) = -15\), so \(f'(x) = 0\) must have a root between \(-1\) and \(0\), since \(f'(x)\) is continuous and we have a change of sign.

The value \(-1/2\) is a sensible choice to test as a possible root, and it works.
