---
created: 2026-10-23T12:00:00 (UTC +06:00)
source: https://undergroundmathematics.org/combining-functions/r5646
author: Underground Mathematics (University of Cambridge)
rights: © University of Cambridge (Underground Mathematics). Use inside SyllabAI is authorised by the
  operator attestation of 2026-10-23 — see LICENSE-DATA.md (Amendment 2026-10-23) in this repository.
  Takedown / correction handling as stated in LICENSE-DATA.md.
tags:
- underground-mathematics
- combining-functions
- type/review-question
resource_identity:
  ugm_id: r5646
  station: combining-functions
  station_title: Combining Functions
  resource_type_id: 10
  resource_type_label: Review question
  level: null
  ref: 5646
  old_site_id: Q4043
spec_map:
  curriculum_code: CIE-9709-P1-2023
  lane: cie-a-level-maths-20-pure-1
  board: Cambridge CIE
  syllabus_version: 2023-2025
  subsection: combining-functions
  subsection_provenance:
    tier: PROVIDER
    signal: source-url-slug
    slug: combining-functions
    validation_status: SUGGESTED
  spec_points:
  - code: 1.2.3
    provenance:
      tier: AI_SUGGESTED
      confidence: high
      model_version: GLM (Super Z agent, z.ai) — P3c functions cross-map (generalisation lane 2) (cross-map-functions.json
        @ syllabai-experimental 4a592ed0)
      evidence: Find f⁻¹ for f:x->1/(3-2x); ff(2); self-mapping values. The |x^2-4x+3| sketch part is
        modulus-graph work beyond P1 1.2 (P2/P3 territory).
      rationale: 'Canonical UGM title: “Can we find an inverse and sketch a modulus function?”; exam provenance:
        UCLES 1989 Q[''Q17''] [8175/1]'
      validation_status: SUGGESTED
    title: determine whether or not a given function is one-one, and find the inverse of a one-one function
      in simple cases
  - code: 1.2.2
    provenance:
      tier: AI_SUGGESTED
      confidence: high
      model_version: GLM (Super Z agent, z.ai) — P3c functions cross-map (generalisation lane 2) (cross-map-functions.json
        @ syllabai-experimental 4a592ed0)
      evidence: Find f⁻¹ for f:x->1/(3-2x); ff(2); self-mapping values. The |x^2-4x+3| sketch part is
        modulus-graph work beyond P1 1.2 (P2/P3 territory).
      rationale: 'Canonical UGM title: “Can we find an inverse and sketch a modulus function?”; exam provenance:
        UCLES 1989 Q[''Q17''] [8175/1]'
      validation_status: SUGGESTED
    title: identify the range of a given function in simple cases, and find the composition of two given
      functions condition that a composite function
  mapped_date: '2026-10-23'
  mapper: cross-map-functions.json (P3c) @ syllabai-experimental 4a592ed0
  coverage_note: null
provenance:
  capture_date: '2026-10-22'
  capture_tool: P2 full-site crawl (ugm-crawl) → ugm-clean extraction; text-only import
  content_language: en
  exam_reference: UCLES 1989 Q['Q17'] [8175/1]
task: T-UGM-IMPORT-2
assets:
- path: https://undergroundmathematics.org/combining-functions/r5646/images/sketch1.png
  kind: figure
- path: https://undergroundmathematics.org/combining-functions/r5646/images/sketch2.png
  kind: figure
---

# Can we find an inverse and sketch a modulus function?

## Question

1. A function is defined by \(f:x\mapsto \dfrac{1}{3-2x}\) for all values of \(x\) except \(x=\dfrac{3}{2}\).
  1. Find the values of \(x\) which map on to themselves under the function \(f\).
  2. Find an expression for \(f^{-1}\).
  3. Evaluate \(ff(2)\).
2. **Sketch** the graph of \(y=|x^2-4x+3|\) for the domain \(0\le x \le 5\), and state the corresponding range of \(y\).

## Solution

We seek \(x\) such that \(f(x)=x\), so we need to solve \[ x=\frac{1}{3-2x}. \] Multiplying both sides by \(3-2x\), we find that \[ 3x-2x^2=1, \] so we must solve the quadratic equation \[ 2x^2-3x+1=0. \] By inspection, we see that \[ 2x^2-3x+1=(2x-1)(x-1), \] therefore the points which are mapped to themselves by \(f\) are \(x=\dfrac{1}{2}\) and \(x=1\).

1. A function is defined by \(f:x\mapsto \dfrac{1}{3-2x}\) for all values of \(x\) except \(x=\dfrac{3}{2}\).
  1. Find an expression for \(f^{-1}\).

Write

\(y=\dfrac{1}{3-2x}\)

. If we can write

\(x\)

in terms of

\(y\)

then we have found

\(f^{-1}\)

. We have that

\[ 3y-2xy=1, \]

and so

\[ 2xy=3y-1, \]

therefore

\[ x=\frac{3y-1}{2y}. \]

So we have that

\[ f^{-1}(x)=\frac{3x-1}{2x}. \]

1. A function is defined by \(f:x\mapsto \dfrac{1}{3-2x}\) for all values of \(x\) except \(x=\dfrac{3}{2}\).
  1. Evaluate \(ff(2)\).

We have that \(f(2)=\dfrac{1}{3-4}=-1\), so \(ff(2)=f(-1)=\dfrac{1}{3+2}=\dfrac{1}{5}\).

To start with, let’s consider \(x^2-4x+3=(x-1)(x-3)\). Using our knowledge of quadratics, we can sketch this straightforwardly.

When \(x=0\), \(x^2-4x+3=3\), and when \(x=5\), \(x^2-4x+3=8\). The minimum occurs at the midpoint of the two roots, when \(x=2\), and here \(x^2-4x+3=-1\).

> [figure: parabola through 1, 0 and 3, 0 — `https://undergroundmathematics.org/combining-functions/r5646/images/sketch1.png`] (image not included in the text import; path of record).

To make this into a sketch of \(y=|x^2-4x+3|\), we must reflect the part where \(x^2-4x+3<0\) in the \(x\)-axis.

> [figure: modulus of a vertex-down parabola through 1 and 3 on the x axis — `https://undergroundmathematics.org/combining-functions/r5646/images/sketch2.png`] (image not included in the text import; path of record).

The largest value of \(y\) is \(8\) when \(x=5\). Therefore for the domain \(0\le x\le 5\), we have that the range of \(y=|x^2-4x+3|\) is \(0\le y\le 8\).
