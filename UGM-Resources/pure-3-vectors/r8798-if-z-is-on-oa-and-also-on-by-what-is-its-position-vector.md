---
created: 2026-10-26T04:13:07 (UTC +06:00)
source: https://undergroundmathematics.org/vector-geometry/r8798
author: Underground Mathematics (University of Cambridge)
rights: © University of Cambridge (Underground Mathematics). Use inside SyllabAI is authorised by the
  operator attestation of 2026-10-23 — see LICENSE-DATA.md (Amendment 2026-10-23) in this repository.
  Takedown / correction handling as stated in LICENSE-DATA.md.
tags:
- underground-mathematics
- vector-geometry
- type/review-question
resource_identity:
  ugm_id: r8798
  station: vector-geometry
  station_title: Vector Geometry
  resource_type_id: 10
  resource_type_label: Review question
  level: null
  ref: 8798
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
      confidence: high
      model_version: GLM (Super Z agent, z.ai) — P3c lane-15 cross-map (cross-map-p3-vectors.json (P3c
        lane 15) @ syllabai-experimental 16c5f80)
      evidence: '''If Z is on OA and also on BY, what is its position vector?'' — two line-membership
        conditions in position-vector form solved simultaneously — vector addition with parameters interpreted
        geometrically (points on lines), 3.7.2.'
      rationale: 'Canonical UGM title: If $Z$ is on $OA$ and also on $BY$, what is its position vector?'
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

# If $Z$ is on $OA$ and also on $BY$, what is its position vector?

## Question

\(O\) is the origin, \(\overrightarrow{OA} = \mathbf{a}\), and \(\overrightarrow{OB} = \mathbf{b}\). The point \(X\) is on \(AB\) such that \(AX = 2XB\) and \(Y\) is the midpoint of \(OX\).

Find \(\overrightarrow{OX}\) and hence show that \(\overrightarrow{BY} = \dfrac{1}{6}\mathbf{a}-\dfrac{2}{3}\mathbf{b}\).

\(BY\) produced meets \(OA\) at \(Z\). Using the facts that \[\overrightarrow{OZ} = \mathbf{b} + k\,\overrightarrow{BY} \quad \text{for some value of } k\] and \[\overrightarrow{OZ} = h\,\mathbf{a} \quad \text{for some value of } h,\] find the position vector of \(Z\).

## Solution

The vector \(\overrightarrow{AB} = \mathbf{b} - \mathbf{a}\). Thus \[\overrightarrow{OX} = \overrightarrow{OA} + \overrightarrow{AX} = \mathbf{a} + \dfrac{2}{3}(\mathbf{b}-\mathbf{a}) = \dfrac{1}{3}\mathbf{a}+ \dfrac{2}{3}\mathbf{b}.\]

This means that \[\overrightarrow{OY} = \dfrac{1}{2}\overrightarrow{OX} = \dfrac{1}{6}\mathbf{a} + \dfrac{1}{3}\mathbf{b}.\]

Now we can say that \[\overrightarrow{BY} = \overrightarrow{OY} - \overrightarrow{OB} = \left(\dfrac{1}{6}\mathbf{a} + \dfrac{1}{3}\mathbf{b}\right) - \mathbf{b} = \dfrac{1}{6}\mathbf{a} - \dfrac{2}{3}\mathbf{b},\] as required.

We can see from the diagram why the two given facts are true. Firstly, \(Z\) is on \(BY\), and secondly, \(Z\) is on \(OA\).

The two facts together give us that \[h\,\mathbf{a}=\mathbf{b}+k\,\overrightarrow{BY} = \mathbf{b} + k\left(\frac{1}{6}\mathbf{a} - \frac{2}{3}\mathbf{b}\right) \implies h\,\mathbf{a}= \frac{k}{6}\mathbf{a}+\left(1-\dfrac{2k}{3}\right)\mathbf{b}.\]

Assuming \(\mathbf{a}\) and \(\mathbf{b}\) are linearly independent vectors (i.e. they are not parallel), we can equate the coefficients of \(\mathbf{a}\) and \(\mathbf{b}\) on either side of this equation.

Thus \[h = \frac{k}{6} \;\text{ and }\; 0 = 1-\frac{2k}{3} \quad\implies\quad k = \frac{3}{2} \;\text{ and }\; h = \frac{1}{4}.\]

So \(\overrightarrow{OZ} = \dfrac{1}{4}\mathbf{a}\), and we have the position vector of \(Z\).

What would happen if \(\mathbf{a}\) and \(\mathbf{b}\) were parallel or anti-parallel?
