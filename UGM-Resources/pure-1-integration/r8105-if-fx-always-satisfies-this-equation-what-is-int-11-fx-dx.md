---
created: 2026-10-24T04:45:46 (UTC +06:00)
source: https://undergroundmathematics.org/calculus-meets-functions/r8105
author: Underground Mathematics (University of Cambridge)
rights: © University of Cambridge (Underground Mathematics). Use inside SyllabAI is authorised by the
  operator attestation of 2026-10-23 — see LICENSE-DATA.md (Amendment 2026-10-23) in this repository.
  Takedown / correction handling as stated in LICENSE-DATA.md.
tags:
- underground-mathematics
- calculus-meets-functions
- type/review-question
resource_identity:
  ugm_id: r8105
  station: calculus-meets-functions
  station_title: Calculus meets Functions
  resource_type_id: 10
  resource_type_label: Review question
  level: null
  ref: 8105
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
      evidence: "functional-equation multiple choice resolved by integrating a polynomial identity over [-1,1] with the definite integral as an unknown constant"
      rationale: "Canonical UGM title: \"If $f(x)$ always satisfies this equation, what is $\\int_{-1}^1 f(x)\\: dx$?\""
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

# If $f(x)$ always satisfies this equation, what is $\int_{-1}^1 f(x)\: dx$?

## Question

For all real values of \(x\), the function \(f(x)\) satisfies

\[6+f(x)=2f(-x)+3x^2\left(\int_{-1}^1 f(t)\: dt\right).\]

It follows that \(\displaystyle\int_{-1}^1 f(x)\: dx\) equals

\[\text{(a)}\quad 4, \quad\text{(b)}\quad 6, \quad\text{(c)}\quad 11, \quad\text{(d)}\quad \dfrac{17}{2}, \quad\text{(e)}\quad 23.\]

## Suggestion

The value of the definite integral in the given equation is a constant. We could call it \(A\).

The equation holds for all values of \(x\). What happens if we substitute \(-x\) for \(x\)?

To find \(\int_{-1}^1 f(x)\: dx\), we might try integrating both sides of the equation.

## Solution

Let \(\int_{-1}^1 f(x) dx = A\).

This means that \(\int_{-1}^1 f(t) dt = A\) also; the choice of variable within the integral is unimportant.

Thus for all \(x, 6+f(x)=2f(-x)+3x^2A\), and so replacing \(x\) with \(-x\), we also have \(6+f(-x)=2f(x)+3x^2A\).

Subtracting these two equations gives us \(f(x)-f(-x)= 2f(-x)-2f(x) \implies f(x) = f(-x)\) for all \(x\), and so \(f(x)\) is even.

So returning to our equation, \(6=f(x) +3x^2A\).

Now we can integrate this from \(-1\) to \(1\), giving us \(\bigl[6x\bigr]_{-1}^1=A + \bigl[x^3\bigr]_{-1}^1A\).

So we have \(12=A + 2A\), so \(A = 4\), and the answer is (a).

Strictly speaking we could have found \(A\) without establishing the evenness of \(f(x)\), but it is a good technique to see.
