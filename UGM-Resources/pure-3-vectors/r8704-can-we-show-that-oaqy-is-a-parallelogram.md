---
created: 2026-10-26T04:13:07 (UTC +06:00)
source: https://undergroundmathematics.org/vector-geometry/r8704
author: Underground Mathematics (University of Cambridge)
rights: © University of Cambridge (Underground Mathematics). Use inside SyllabAI is authorised by the
  operator attestation of 2026-10-23 — see LICENSE-DATA.md (Amendment 2026-10-23) in this repository.
  Takedown / correction handling as stated in LICENSE-DATA.md.
tags:
- underground-mathematics
- vector-geometry
- type/review-question
resource_identity:
  ugm_id: r8704
  station: vector-geometry
  station_title: Vector Geometry
  resource_type_id: 10
  resource_type_label: Review question
  level: null
  ref: 8704
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
      evidence: '''Can we show that OAQY is a parallelogram?'' — the solution proves OA parallel-and-equal
        to YQ via position-vector arithmetic — proving a quadrilateral is a parallelogram BY vector operations
        is the geometrical-interpretation clause of 3.7.2 verbatim.'
      rationale: 'Canonical UGM title: Can we  show that $OAQY$ is a parallelogram?'
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

# Can we  show that $OAQY$ is a parallelogram?

## Question

*Note; this figure is not intended to be completely accurately drawn.*

In the figure the points \(X\) and \(Y\) are such that \(AX = \dfrac{1}{2}XB\) and \(OY = YX\), while the point \(P\) is such that \(OA = 3AP\). The lines \(YQ\) and \(PQ\) are parallel to \(OA\) and \(OB\) respectively.

Given that \(\mathbf{OA} = \mathbf{a}\) and \(\mathbf{OB} = \mathbf{b}\), express \(\mathbf{OP}\) and \(\mathbf{OY}\) in terms of \(\mathbf{a}\) and \(\mathbf{b}\).

Given that \(\mathbf{YQ} = m\mathbf{a}\) and \(\mathbf{PQ} = n\mathbf{b}\), find the values of \(m\) and \(n\). Hence show that \(OAQY\) is a parallelogram.

## Solution

Since \(\mathbf{OA} = 3\mathbf{AP}\), we know \(\mathbf{OP}\) is \(\dfrac{4}{3}\mathbf{a}\).

We can see that the vector \[\mathbf{OX} = \mathbf{OA} + \mathbf{AX} = \mathbf{a} + \dfrac{1}{3}(\mathbf{b}-\mathbf{a}) = \dfrac{2}{3}\mathbf{a} + \dfrac{1}{3}\mathbf{b}.\]

We also have that the vector \[\mathbf{OY}=\dfrac{1}{2}\mathbf{OX} = \dfrac{1}{3}\mathbf{a} + \dfrac{1}{6}\mathbf{b}.\]

The diagram tells us that \(\mathbf{OP} + \mathbf{PQ} = \mathbf{OY} + \mathbf{YQ}\).

Thus \[\dfrac{4}{3}\mathbf{a} + n\mathbf{b} = \dfrac{1}{3}\mathbf{a}+\dfrac{1}{6}\mathbf{b} + m\mathbf{a}.\]

Since \(\mathbf{a}\) and \(\mathbf{b}\) are linearly independent (they are not parallel) we can equate coefficients of \(\mathbf{a}\) and \(\mathbf{b}\) on either side of this equation.

We are effectively saying here that if \(\alpha \mathbf{a} + \beta \mathbf{b} = \gamma \mathbf{a} + \delta \mathbf{b},\) then \(\alpha = \gamma, \beta = \delta.\) Is that always true?

This tells us \[\dfrac{4}{3}= \dfrac{1}{3} + m \implies m = 1,\] and \[n =\dfrac{1}{6}.\]

Since \(m = 1\), we have that \(\big \vert \mathbf{AO} \big \vert= \big \vert\mathbf{QY}\big \vert\), and we know these two lines are parallel, so therefore \(OAQY\) is a parallelogram.
