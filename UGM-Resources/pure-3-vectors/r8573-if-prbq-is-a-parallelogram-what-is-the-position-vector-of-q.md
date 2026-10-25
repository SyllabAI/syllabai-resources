---
created: 2026-10-26T04:13:07 (UTC +06:00)
source: https://undergroundmathematics.org/vector-geometry/r8573
author: Underground Mathematics (University of Cambridge)
rights: © University of Cambridge (Underground Mathematics). Use inside SyllabAI is authorised by the
  operator attestation of 2026-10-23 — see LICENSE-DATA.md (Amendment 2026-10-23) in this repository.
  Takedown / correction handling as stated in LICENSE-DATA.md.
tags:
- underground-mathematics
- vector-geometry
- type/review-question
resource_identity:
  ugm_id: r8573
  station: vector-geometry
  station_title: Vector Geometry
  resource_type_id: 10
  resource_type_label: Review question
  level: null
  ref: 8573
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
      evidence: '''If PRBQ is a parallelogram, what is the position vector of Q?'' with P, R, B given
        by position vectors and ratio language (''in the ratio'') — the fourth-vertex demand closes via
        PR = BQ rearranged and section-division addition — 3.7.2''s addition/subtraction in geometrical
        terms.'
      rationale: 'Canonical UGM title: If $PRBQ$ is a parallelogram, what is the position vector of $Q$?'
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

# If $PRBQ$ is a parallelogram, what is the position vector of $Q$?

## Question

The points \(A\) and \(B\) have position vectors \(\mathbf{a}\) and \(\mathbf{b}\) respectively, relative to an origin \(O\). The point \(P\) divides the line segment \(OA\) in the ratio \(1:3\), and the point \(R\) divides the line segment \(AB\) in the ratio \(1:2\). Given that \(PRBQ\) is a parallelogram, determine the position vector of \(Q\).

## Solution

For convenience, we write \(\mathbf{p}\) and \(\mathbf{q}\) for the position vectors of \(P\) and \(Q\).

Since \(PRBQ\) is a parallelogram, \(\overrightarrow{PQ} = \overrightarrow{RB}\).

Using the ratios given in the question we have,

\[\begin{align*} \mathbf{p} &= \frac{1}{4} \mathbf{a} \\ \text{and}\quad \mathbf{q} &= \mathbf{p}+\overrightarrow{PQ} = \mathbf{p}+\overrightarrow{RB} = \frac{1}{4} \mathbf{a} +\frac{2}{3}(\mathbf{b}-\mathbf{a}) \\ &= \dfrac{2}{3}\mathbf{b}-\dfrac{5}{12}\mathbf{a}. \end{align*}\]

The GeoGebra applet below allows us to explore the behaviour as we move \(A\) and \(B\).

> [interactive embed (geogebra-iframe): //www.geogebratube.org/material/iframe/id/tpe4c9Un/width/600/height/317/border/888888/rc/false/ai/false/sdz/false/smb/false/stb/false/stbh/false/ld/false/sri/true/asb/false/at/html5] — not part of the text import; see the source page.

[Download GeoGebra file](https://www.geogebratube.org/material/download/format/file/id/tpe4c9Un)
