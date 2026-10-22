---
created: 2026-10-23T12:00:00 (UTC +06:00)
source: https://undergroundmathematics.org/combining-functions/r7553
author: Underground Mathematics (University of Cambridge)
rights: © University of Cambridge (Underground Mathematics). Use inside SyllabAI is authorised by the
  operator attestation of 2026-10-23 — see LICENSE-DATA.md (Amendment 2026-10-23) in this repository.
  Takedown / correction handling as stated in LICENSE-DATA.md.
tags:
- underground-mathematics
- combining-functions
- type/review-question
resource_identity:
  ugm_id: r7553
  station: combining-functions
  station_title: Combining Functions
  resource_type_id: 10
  resource_type_label: Review question
  level: null
  ref: 7553
  old_site_id: Q150
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
  - code: 1.2.2
    provenance:
      tier: AI_SUGGESTED
      confidence: high
      model_version: GLM (Super Z agent, z.ai) — P3c functions cross-map (generalisation lane 2) (cross-map-functions.json
        @ syllabai-experimental 4a592ed0)
      evidence: Composition/iteration of polynomial functions f_n(f_n(...)); the maximum-value part rides
        P1 1.1 quadratics.
      rationale: 'Canonical UGM title: “Can we compose these polynomial functions?”; exam provenance:
        Oxford (MAT) 2007 Q[''Q2'']'
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
  exam_reference: Oxford (MAT) 2007 Q['Q2']
task: T-UGM-IMPORT-2
interactive:
- src: //www.geogebratube.org/material/iframe/id/t7SMRyQP/width/600/height/400/border/888888/rc/false/ai/false/sdz/false/smb/false/stb/false/stbh/false/ld/false/sri/true/asb/false/at/html5
  kind: geogebra-iframe
---

# Can we compose these polynomial functions?

## Question

Let \[f_n(x)=(2+(-2)^n)x^2+(n+3)x+n^2\] where \(n\) is a positive integer and \(x\) is any real number.

1. Write down \(f_3(x)\).  Find the maximum value of \(f_3(x)\).  For what values of \(n\) does \(f_n(x)\) have a maximum value (as \(x\) varies)? [Note you are not being asked to calculate the value of this maximum].
2. Write down \(f_1(x)\).  Calculate \(f_1(f_1(x))\) and \(f_1(f_1(f_1(x)))\).  Find an expression, simplified as much as possible, for \[f_1(f_1(f_1(...f_1(x))))\] where \(f_1\) is applied \(k\) times. [Here \(k\) is a positive integer.]
3. Write down \(f_2(x)\).  The function \[f_2(f_2(f_2(...f_2(x)))),\] where \(f_2\) is applied \(k\) times, is a polynomial in \(x\). What is the degree of this polynomial?

## Suggestion

> [interactive embed (geogebra-iframe): //www.geogebratube.org/material/iframe/id/t7SMRyQP/width/600/height/400/border/888888/rc/false/ai/false/sdz/false/smb/false/stb/false/stbh/false/ld/false/sri/true/asb/false/at/html5] — not part of the text import; see the source page.

[Download GeoGebra file](https://www.geogebratube.org/material/download/format/file/id/t7SMRyQP)

The green curve here is \(y=(2+(-2)^n)x^2+(n+3)x+n^2\), where \(n\) is a positive integer.

What happens as we vary \(n\)? Make sure you can explain algebraically the behaviour you can see here.

## Solution

First,

\[\begin{align*} f_3(x)&=(2+(-2)^3)x^2+(3+3)x+3^2\\ &=-6x^2+6x+9. \end{align*}\]

To find the maximum value, we can complete the square:

\[\begin{align*} f_3(x)&=-6x^2+6x+9\\ &=-6\left(x-\frac{1}{2}\right)^2+\frac{3}{2}+9\\ &=-6\left(x-\frac{1}{2}\right)^2+\frac{21}{2}. \end{align*}\]

The maximum value is therefore \(21/2\), achieved at \(x=1/2\).

The graph of \(y = f_n(x)\) will be a parabola – it will have a maximum if it points upwards.

So for \(f_n\) to have a maximum we require the coefficient of \(x^2\) in \(f_n\) to be negative.

Consider \(2 + (-2)^n\) – this will be negative exactly when \(n\) is an odd number greater than \(1\).

---

\[f_1(x)=4x+1\]

So

\[\begin{align*} f_1(f_1(x))&=4(4x+1)+1\\ &=16x+5 \end{align*}\]

and

\[\begin{align*} f_1(f_1(f_1(x)))&=f_1[f_1(f_1(x))]\\ &=4(16x+5)+1\\ &=64x+21. \end{align*}\]

We have \[f_1(x)=4(4(...4(4x+1)+1...)+1)+1\] The coefficient of \(x\) is \(4^k\). The constant term is \[1+4+ ... +4^{k-1}.\] This is a geometric progression with common ratio \(4\), so its sum is \[1 \times \frac{4^k-1}{4-1}=\frac{4^k-1}{3}\] So \(f_1^k(x)=4^kx+\dfrac{4^k-1}{3}\).

---

\(f_2(x)=6x^2+5x+4\).

If a question says ‘Write down…’ then that is just what we do — no justification is required.

Every time we apply \(f_2\) to a polynomial, the degree of the polynomial is doubled. So \(f_2^k\) is a polynomial of degree \(2^k\).
