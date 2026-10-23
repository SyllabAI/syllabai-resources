---
created: 2026-10-24T01:49:53 (UTC +06:00)
source: https://undergroundmathematics.org/calculus-of-powers/r5732
author: Underground Mathematics (University of Cambridge)
rights: © University of Cambridge (Underground Mathematics). Use inside SyllabAI is authorised by the
  operator attestation of 2026-10-23 — see LICENSE-DATA.md (Amendment 2026-10-23) in this repository.
  Takedown / correction handling as stated in LICENSE-DATA.md.
tags:
- underground-mathematics
- calculus-of-powers
- type/review-question
resource_identity:
  ugm_id: r5732
  station: calculus-of-powers
  station_title: Calculus of Powers
  resource_type_id: 10
  resource_type_label: Review question
  level: null
  ref: 5732
  old_site_id: Q133
spec_map:
  curriculum_code: CIE-9709-P1-2023
  lane: cie-a-level-maths-20-pure-1
  board: Cambridge CIE
  syllabus_version: 2023-2025
  subsection: calculus-of-powers
  subsection_provenance:
    tier: PROVIDER
    signal: source-url-slug
    slug: calculus-of-powers
    validation_status: SUGGESTED
  spec_points:
  - code: 1.7.2
    provenance:
      tier: AI_SUGGESTED
      confidence: high
      model_version: GLM (Super Z agent, z.ai) — P3c lane-7 cross-map (cross-map-differentiation.json
        (P3c lane 7) @ syllabai-experimental 93575e69)
      evidence: f(x)=x^2-2px+3 has one stationary value in 0<x<1 iff 0<p<1 — parameterised stationary
        analysis
      rationale: 'Canonical UGM title: "Where does $f(x) = x^2 - 2px + 3$ have its minimum?"; exam provenance:
        Oxford University Mathematics Aptitude Test, None, Q3'
      validation_status: SUGGESTED
    title: use the derivative of x (for any rational n ), together with constant multiples, sums and
      differences of functions, and of composite functions using the chain rule
  - code: 1.7.4
    provenance:
      tier: AI_SUGGESTED
      confidence: high
      model_version: GLM (Super Z agent, z.ai) — P3c lane-7 cross-map (cross-map-differentiation.json
        (P3c lane 7) @ syllabai-experimental 93575e69)
      evidence: f(x)=x^2-2px+3 has one stationary value in 0<x<1 iff 0<p<1 — parameterised stationary
        analysis
      rationale: 'Canonical UGM title: "Where does $f(x) = x^2 - 2px + 3$ have its minimum?"; exam provenance:
        Oxford University Mathematics Aptitude Test, None, Q3'
      validation_status: SUGGESTED
    title: locate stationary points and determine their nature, and use information about stationary
      points in sketching graphs.
  mapped_date: '2026-10-24'
  mapper: cross-map-differentiation.json (P3c lane 7) @ syllabai-experimental 93575e69
provenance:
  capture_date: '2026-10-22'
  capture_tool: P2 full-site crawl (ugm-crawl) → ugm-clean extraction; text-only import
  content_language: en
  exam_reference: Oxford University Mathematics Aptitude Test, None, Q3
task: T-UGM-IMPORT-7
interactive:
- src: //www.geogebratube.org/material/iframe/id/h6xZbc2V/width/600/height/400/border/888888/rc/false/ai/false/sdz/false/smb/false/stb/false/stbh/false/ld/false/sri/true/asb/false/at/html5
  kind: geogebra-iframe
---

# Where does $f(x) = x^2 - 2px + 3$ have its minimum?

## Question

In this question we shall consider the function \(f(x)\) defined by \[f(x) = x^2 - 2px + 3\] where \(p\) is a constant.

1. Show that the function \(f(x)\) has one stationary value in the range \(0< x <1\) if \(0< p <1\), and no stationary values in that range otherwise.

In the remainder of the question we shall be interested in the smallest value attained by \(f(x)\) in the range \(0 \le x \le 1\). Of course, this value, which we shall call \(m\), will depend on \(p\).

1. Show that if \(p \ge 1\) then \(m=4-2p\).

---

1. What is the value of \(m\) if \(p \le 0\)?

---

1. Obtain a formula for \(m\) in terms of \(p\), valid for \(0 < p < 1\).

---

1. Using the axes opposite, sketch the graph of \(m\) as a function of \(p\) in the range \(-2 \le p \le 2\).

## Solution

We know that \(y = f(x)\) is a parabola, and since the coefficient of \(x^2\) is positive, it is ‘vertex-down’ and has a minimum. It can only have one stationary value.

Differentiating \(f(x)\) gives \[f'(x) = 2x - 2p,\] so the stationary point occurs when \(x=p\), which is in the range \(0<x<1\) if and only if \(0<p<1\).

Or else completing the square, \(f(x) = (x-p)^2 + 3 - p^2\), and so the vertex of the parabola is at \((p, 3-p^2)\), which is in the range \(0<x<1\) if and only if \(0<p<1\).

The minimum value \(m(p)\) attained by \(f(x)\) in the range \(0 \le x \le 1\) will occur either at an endpoint (\(x=0\) or \(x=1\)), or at a stationary point in between 0 and 1.

If \(p \ge 1\) then we have seen there is no stationary point in that interval. So as \(f(1)=4-2p<3=f(0)\), we have \(m(p)=4-2p\).

For \(p \le 0\), again, no stationary point exists in the range \(0 \le x \le 1\). We now have \(f(0) = 3 < 4 - 2p = f(1)\), so \(m(p)=3\).

If \(0 < p < 1\), then we know there is a stationary point of \(f\) at \(x=p\), which is at the parabola’s vertex.

So the minimum value \(m(p)=f(p)=3-p^2.\)

To summarise the results of parts ii), iii) and iv) the function \(m(p)\) is: \[m(p)= \begin{cases} 3 &\text{if } p \le 0 \\ 3-p^2 &\text{if } 0 < p < 1 \\ 4-2p &\text{if } 1 \le p \end{cases}\]

A sketch of this looks like

How do we know for sure that the join at \(p=1\) is smooth? Because the gradient of \(3-p^2\) is \(-2p\) and the gradient of \(4-2p\) is \(-2,\) which agree when \(p=1\).

> [interactive embed (geogebra-iframe): //www.geogebratube.org/material/iframe/id/h6xZbc2V/width/600/height/400/border/888888/rc/false/ai/false/sdz/false/smb/false/stb/false/stbh/false/ld/false/sri/true/asb/false/at/html5] — not part of the text import; see the source page.

[Download GeoGebra file](https://www.geogebratube.org/material/download/format/file/id/h6xZbc2V)
