---
created: 2026-10-26T04:13:07 (UTC +06:00)
source: https://undergroundmathematics.org/vector-geometry/r9629
author: Underground Mathematics (University of Cambridge)
rights: © University of Cambridge (Underground Mathematics). Use inside SyllabAI is authorised by the
  operator attestation of 2026-10-23 — see LICENSE-DATA.md (Amendment 2026-10-23) in this repository.
  Takedown / correction handling as stated in LICENSE-DATA.md.
tags:
- underground-mathematics
- vector-geometry
- type/review-question
resource_identity:
  ugm_id: r9629
  station: vector-geometry
  station_title: Vector Geometry
  resource_type_id: 10
  resource_type_label: Review question
  level: null
  ref: 9629
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
  - code: 3.7.1
    provenance:
      tier: AI_SUGGESTED
      confidence: high
      model_version: GLM (Super Z agent, z.ai) — P3c lane-15 cross-map (cross-map-p3-vectors.json (P3c
        lane 15) @ syllabai-experimental 16c5f80)
      evidence: 'The resource classifies vector pairs as ''is parallel to / is perpendicular to / have
        the same length'': the solutions establish parallel iff one is a scalar multiple of the other,
        perpendicular in 2D iff the gradients multiply to -1, and equal magnitude via Pythagoras on the
        components — the component notation and magnitude computation of 3.7.1/3.7.3 with the scaling-parallelism
        geometry of 3.7.2''s territory (coded 3.7.1/3.7.3: the classification language — parallel/perpendicular/magnitude
        — is exactly the notation-and-magnitude core).'
      rationale: 'Canonical UGM title: When are these vectors parallel/perpendicular/the same length?'
      validation_status: SUGGESTED
    title: use standard notations for vectors, i.e. f p , x i + y j , f p y , x i + y j + z k , AB , a
  - code: 3.7.3
    provenance:
      tier: AI_SUGGESTED
      confidence: high
      model_version: GLM (Super Z agent, z.ai) — P3c lane-15 cross-map (cross-map-p3-vectors.json (P3c
        lane 15) @ syllabai-experimental 16c5f80)
      evidence: 'The resource classifies vector pairs as ''is parallel to / is perpendicular to / have
        the same length'': the solutions establish parallel iff one is a scalar multiple of the other,
        perpendicular in 2D iff the gradients multiply to -1, and equal magnitude via Pythagoras on the
        components — the component notation and magnitude computation of 3.7.1/3.7.3 with the scaling-parallelism
        geometry of 3.7.2''s territory (coded 3.7.1/3.7.3: the classification language — parallel/perpendicular/magnitude
        — is exactly the notation-and-magnitude core).'
      rationale: 'Canonical UGM title: When are these vectors parallel/perpendicular/the same length?'
      validation_status: SUGGESTED
    title: calculate the magnitude of a vector, and use In 2 or 3 dimensions. unit vectors, displacement
      vectors and position vectors
  mapped_date: '2026-10-26'
  mapper: cross-map-p3-vectors.json (P3c lane 15) @ syllabai-experimental 16c5f80
provenance:
  capture_date: '2026-10-22'
  capture_tool: P2 full-site crawl (ugm-crawl) → ugm-clean extraction; text-only import
  content_language: en
  task: T-UGM-IMPORT-15
---

# When are these vectors parallel/perpendicular/the same length?

## Question

Given the vectors \(\mathbf{U}=\begin{pmatrix}7 \\ 6\end{pmatrix}\) and \(\mathbf{V}=\begin{pmatrix}2 \\ x\end{pmatrix}\), find the value or values of \(x\) for which

1. \(\mathbf{U}\) is parallel to \(\mathbf{V}\),

---

1. \(\mathbf{U}\) is perpendicular to \(\mathbf{V}\),

---

1. \(\mathbf{U}\) and \(\mathbf{V}\) have the same magnitude.

## Solution

Two vectors \(\mathbf{U}\) and \(\mathbf{V}\) are parallel if and only if \(\mathbf{U}=k\mathbf{V}\) for some scalar \(k\).

This happens in our case if and only if \(7 = k \times 2\), and \(6 = k \times x\). This means \(k = 3.5\), and so \(x = \dfrac{12}{7} = 1.71 \quad (3\)sf).

Given the vectors \(\mathbf{U}=\begin{pmatrix}7 \\ 6\end{pmatrix}\) and \(\mathbf{V}=\begin{pmatrix}2 \\ x\end{pmatrix}\), find the value or values of \(x\) for which

1. \(\mathbf{U}\) is perpendicular to \(\mathbf{V}\),

Two vectors in two dimensions are perpendicular if and only if their gradients multiply to \(-1\).

This happens here if and only if

\[\dfrac{6}{7} \times \dfrac{x}{2} = -1 \implies x = -\dfrac{7}{3}= -2.33 \quad (3\text{sf}).\]

Given the vectors \(\mathbf{U}=\begin{pmatrix}7 \\ 6\end{pmatrix}\) and \(\mathbf{V}=\begin{pmatrix}2 \\ x\end{pmatrix}\), find the value or values of \(x\) for which

1. \(\mathbf{U}\) and \(\mathbf{V}\) have the same magnitude.

We know that the magnitude of \(\begin{pmatrix}a \\ b\end{pmatrix}\) is \(\sqrt{a^2+b^2}\).

So we need in our case to have

\(\sqrt{7^2+6^2}=\sqrt{x^2+2^2}\)

, which gives us that

\[\begin{align*} x^2 &= 7^2+6^2-2^2 \\ x &= \pm 9. \end{align*}\]

We can check our answers for all three parts using the GeoGebra applet below.

> [interactive embed (geogebra-iframe): //www.geogebratube.org/material/iframe/id/KzQhNUqH/width/600/height/600/border/888888/rc/false/ai/false/sdz/false/smb/false/stb/false/stbh/false/ld/false/sri/true/asb/false/at/html5] — not part of the text import; see the source page.

[Download GeoGebra file](https://www.geogebratube.org/material/download/format/file/id/KzQhNUqH)
