---
created: 2026-10-26T04:13:07 (UTC +06:00)
source: https://undergroundmathematics.org/vector-geometry/r8339
author: Underground Mathematics (University of Cambridge)
rights: © University of Cambridge (Underground Mathematics). Use inside SyllabAI is authorised by the
  operator attestation of 2026-10-23 — see LICENSE-DATA.md (Amendment 2026-10-23) in this repository.
  Takedown / correction handling as stated in LICENSE-DATA.md.
tags:
- underground-mathematics
- vector-geometry
- type/review-question
resource_identity:
  ugm_id: r8339
  station: vector-geometry
  station_title: Vector Geometry
  resource_type_id: 10
  resource_type_label: Review question
  level: null
  ref: 8339
  old_site_id: null
spec_map:
  curriculum_code: CIE-9709-P3-2023
  lane: cie-a-level-maths-20-pure-3
  board: Cambridge CIE
  syllabus_version: 2023-2025
  subsection: vector-geometry
  subsection_provenance:
    tier: PROVIDER
    signal: source-url-slug
    slug: vector-geometry
    validation_status: SUGGESTED
  spec_points:
  - code: 3.7.2
    provenance:
      tier: AI_SUGGESTED
      confidence: medium
      model_version: GLM (Super Z agent, z.ai) — P3c lane-15 cross-map (cross-map-p3-vectors.json (P3c
        lane 15) @ syllabai-experimental 16c5f80)
      evidence: '''What if we join the midpoints of opposite sides of a quadrilateral?'' — the solution
        computes midpoints as position vectors ((a+b)/2 arithmetic), shows the two joining segments bisect
        each other — the midpoint understanding 3.7.2 names explicitly (''understanding that the midpoint
        of a line segment is (a+b)/2''-class work). Medium: no exam-register demand; an exploratory generalisation.'
      rationale: 'Canonical UGM title: What if we join the midpoints of opposite sides of a quadrilateral?'
      validation_status: SUGGESTED
    title: carry out addition and subtraction of vectors and multiplication of a vector by a scalar, and
      interpret these operations in geometrical terms The general form of the ratio theorem is not included,
      but understanding that the midpoint of
  mapped_date: '2026-10-26'
  mapper: cross-map-p3-vectors.json (P3c lane 15) @ syllabai-experimental 16c5f80
provenance:
  capture_date: '2026-10-22'
  capture_tool: P2 full-site crawl (ugm-crawl) → ugm-clean extraction; text-only import
  content_language: en
  task: T-UGM-IMPORT-15
---

# What if we join the midpoints of opposite sides of a quadrilateral?

## Question

The position vectors of four points \(A, B, C, D\) relative to an origin \(O\) are \(\mathbf{a}\), \(\mathbf{b}\), \(\mathbf{c}\), \(\mathbf{d}\) respectively. Obtain the equation of the line \(l\) joining the midpoints of \(AB\) and \(CD\). Show that \(l\) intersects the line joining the midpoints of \(AC\) and \(BD\) and find the position vector \(\mathbf{p}\) of the point \(P\) of intersection.

Deduce that the line joining the midpoints of \(AD\) and \(BC\) also passes through \(P\).

## Solution

The midpoint of \(AB\) is \(\dfrac{\mathbf{a}+\mathbf{b}}{2}\) while the midpoint of \(CD\) is \(\dfrac{\mathbf{c}+\mathbf{d}}{2}\). Using the standard form for a vector line \[\mathbf{r} = \mathbf{u} + \lambda \mathbf{v},\] where \(\mathbf{u}\) is the position vector of a point on the line and \(\mathbf{v}\) is the direction of the line, we have that \(l\) is the line \[\mathbf{r} = \dfrac{\mathbf{a}+\mathbf{b}}{2} + \lambda \left(\left(\dfrac{\mathbf{c}+\mathbf{d}}{2}\right)-\left(\dfrac{\mathbf{a}+\mathbf{b}}{2} \right)\right),\] which becomes after simplification \[\mathbf{r} = \dfrac{1-\lambda}{2}\mathbf{a}+ \dfrac{1-\lambda}{2}\mathbf{b}+ \dfrac{\lambda}{2}\mathbf{c}+ \dfrac{\lambda}{2}\mathbf{d}.\]

If we do exactly the same for the line joining the midpoints of \(AC\) and \(BD\) (let’s call this \(m\)) using the parameter \(\mu\) rather than \(\lambda\), we arrive at the equation \[\mathbf{r} = \dfrac{1-\mu}{2}\mathbf{a}+ \dfrac{\mu}{2}\mathbf{b} + \dfrac{1-\mu}{2}\mathbf{c} + \dfrac{\mu}{2}\mathbf{d}.\]

Notice that if \(\lambda = 0.5\), we get the point on \(l\) given by \[\mathbf{r} = \dfrac{1}{4}(\mathbf{a}+ \mathbf{b}+\mathbf{c}+\mathbf{d}).\]

This is also the point on \(m\) such that \(\mu = 0.5\).

Thus the two lines \(l\) and \(m\) intersect at the point \(P\) with position vector \(\mathbf{p} = \dfrac{1}{4}(\mathbf{a}+ \mathbf{b} + \mathbf{c} + \mathbf{d})\).

We found the point \(P\) by inspection, having noted the similarities between the two line equations.

The point \(P\) is called the centroid of the four points \(A\), \(B\) , \(C\) and \(D\).

The above argument is completely symmetrical in \(\mathbf{a}\), \(\mathbf{b}\), \(\mathbf{c}\) and \(\mathbf{d}\), which means that the line joining the midpoints of \(AD\) and \(BC\) must also pass through \(P\).
