---
created: 2026-10-24T01:49:53 (UTC +06:00)
source: https://undergroundmathematics.org/calculus-of-powers/r7785
author: Underground Mathematics (University of Cambridge)
rights: © University of Cambridge (Underground Mathematics). Use inside SyllabAI is authorised by the
  operator attestation of 2026-10-23 — see LICENSE-DATA.md (Amendment 2026-10-23) in this repository.
  Takedown / correction handling as stated in LICENSE-DATA.md.
tags:
- underground-mathematics
- calculus-of-powers
- type/review-question
resource_identity:
  ugm_id: r7785
  station: calculus-of-powers
  station_title: Calculus of Powers
  resource_type_id: 10
  resource_type_label: Review question
  level: null
  ref: 7785
  old_site_id: null
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
      evidence: 'cylinder inscribed in a truncated cone: maximum volume by polynomial optimisation'
      rationale: 'Canonical UGM title: "When is the volume of this cylinder inside a cone a maximum?";
        exam provenance: UCLES A level Mathematics A 1 and Pure Mathematics 1 QP9200/1 and 9208/1, 1982,
        Q17'
      validation_status: SUGGESTED
    title: use the derivative of x (for any rational n ), together with constant multiples, sums and
      differences of functions, and of composite functions using the chain rule
  - code: 1.7.4
    provenance:
      tier: AI_SUGGESTED
      confidence: high
      model_version: GLM (Super Z agent, z.ai) — P3c lane-7 cross-map (cross-map-differentiation.json
        (P3c lane 7) @ syllabai-experimental 93575e69)
      evidence: 'cylinder inscribed in a truncated cone: maximum volume by polynomial optimisation'
      rationale: 'Canonical UGM title: "When is the volume of this cylinder inside a cone a maximum?";
        exam provenance: UCLES A level Mathematics A 1 and Pure Mathematics 1 QP9200/1 and 9208/1, 1982,
        Q17'
      validation_status: SUGGESTED
    title: locate stationary points and determine their nature, and use information about stationary
      points in sketching graphs.
  mapped_date: '2026-10-24'
  mapper: cross-map-differentiation.json (P3c lane 7) @ syllabai-experimental 93575e69
provenance:
  capture_date: '2026-10-22'
  capture_tool: P2 full-site crawl (ugm-crawl) → ugm-clean extraction; text-only import
  content_language: en
  exam_reference: UCLES A level Mathematics A 1 and Pure Mathematics 1 QP9200/1 and 9208/1, 1982, Q17
task: T-UGM-IMPORT-7
---

# When is the volume of this cylinder inside a cone a maximum?

## Question

A truncated cone of height \(h\) has circular ends of radii \(2r\) and \(r\). In this cone is inserted a circular cyclinder having its axis along the axis of the cone. One end of the cylinder lies in that face of the cone which is of radius \(2r\) and the circumference of the other end lies in the curved surface of the cone (see diagram). Given that the radius of the base of the cylinder is \(s\), show that the volume of the cylinder is

\[\frac{\pi h s^2(2r - s)}{r}.\]

If \(s\) is allowed to vary, find, in terms of \(h\) and \(r\), the maximum volume of the cylinder.

## Solution

A truncated cone of height \(h\) has circular ends of radii \(2r\) and \(r\). In this cone is inserted a circular cylinder having its axis along the axis of the cone. One end of the cylinder lies in that face of the cone which is of radius \(2r\) and the circumference of the other end lies in the curved surface of the cone (see diagram). Given that the radius of the base of the cylinder is \(s\), show that the volume of the cylinder is

\[\frac{\pi h s^2(2r - s)}{r}.\]

The volume of a cylinder is given by (area of the base)\(\times\)(height).

Since the radius of the cylinder is \(s\), the area of its base is \(\pi s^2\).

We now need to find the height of the cylinder which we shall call \(a\). For this, consider the following cross section of the diagram above.

From the two similar triangles at the left hand side we can see that

\[\begin{align*} \frac{h}{r}&=\frac{a}{2r-s} \\ \iff\quad a&=\frac{h}{r}(2r-s) \end{align*}\]

In order to find $a$, we'll choose axes as follows.

Since the radii of the two faces of the truncated cone differ by $r$, the equation of the left-hand line is $y = \dfrac{h}{r}x$. Note that in this coordinate system, the left side of the cylinder has equation $x=2r-s$. Thus, the intersection point of this line with the truncated cone has $y$-coordinate $$y = \frac{h}{r}(2r - s),$$ which is the height $a$ of the cylinder.

Thus the volume of the cylinder is \[\frac{\pi s^2 \times h(2r - s)}{r}\] as required.

We have

\[\begin{align*} V &= \frac{\pi s^2 h (2r - s)}{r} \\ &= (2 \pi h)s^2 - \frac{\pi h}{r}s^3 \\ \frac{dV}{ds} &= (2 \pi h) 2s - \frac{\pi h}{r}3s^2\\ &= \pi h s \left(4-\frac{3s}{r}\right). \end{align*}\]

Putting \(\dfrac{dV}{ds} = 0\), we have \[s = 0 \quad \text{ or } \quad 4-\frac{3s}{r} = 0.\]

The second case is clearly the one we require, giving \(s = \dfrac{4}{3}r\). This yields \[V_{max} = \frac{32\pi r^2 h}{27}.\]
