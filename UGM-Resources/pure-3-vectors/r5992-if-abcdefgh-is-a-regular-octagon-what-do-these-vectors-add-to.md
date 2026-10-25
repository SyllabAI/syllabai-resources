---
created: 2026-10-26T04:13:07 (UTC +06:00)
source: https://undergroundmathematics.org/vector-geometry/r5992
author: Underground Mathematics (University of Cambridge)
rights: © University of Cambridge (Underground Mathematics). Use inside SyllabAI is authorised by the
  operator attestation of 2026-10-23 — see LICENSE-DATA.md (Amendment 2026-10-23) in this repository.
  Takedown / correction handling as stated in LICENSE-DATA.md.
tags:
- underground-mathematics
- vector-geometry
- type/review-question
resource_identity:
  ugm_id: r5992
  station: vector-geometry
  station_title: Vector Geometry
  resource_type_id: 10
  resource_type_label: Review question
  level: null
  ref: 5992
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
      evidence: '''If ABCDEFGH is a regular octagon, what do these vectors add to?'' — the well sequences
        vector sums around a regular polygon (AB + BC + ... chains, diagonals as differences), and the
        solutions read the resultants off the symmetry (''What can we say about the lines... is parallel
        to'') — vector addition and subtraction interpreted in geometrical terms, 3.7.2 verbatim.'
      rationale: 'Canonical UGM title: If $ABCDEFGH$ is a regular octagon, what do these vectors add to?'
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

# If $ABCDEFGH$ is a regular octagon, what do these vectors add to?

## Question

\(ABCDEFGH\) is a regular octagon. Express in terms of a single vector the sum of the vectors

1. \(\mathbf{AC},\mathbf{AH},\mathbf{HG}\),

---

1. \(\mathbf{AB},\mathbf{AC},\mathbf{AF},\mathbf{AH},\mathbf{HG}\).

Given that \(\big \vert \mathbf{AB} \big \vert = 2,\) calculate \(\big \vert \mathbf{AF} \big \vert\).

## Suggestion

We can start by choosing one convenient pair to add. Remember that as long as we keep the sense correct we can add them in whatever order we like.

What can we say about the lines \(AF\) and \(GH\)?

## Solution

Vector addition tells us that \(\mathbf{AH} + \mathbf{HG} = \mathbf{AG}\).

From the symmetry of the octagon, \(ACEG\) must be a square, so the vector \(\mathbf{AG}\) is the same as \(\mathbf{CE}\). The vector sum of \(\mathbf{AC}\) and \(\mathbf{CE}\) is \(\mathbf{AE}\).

Thus we have \(\mathbf{AC} + \mathbf{AH} + \mathbf{HG} = \mathbf{AE}\).

Using the first part, we can say immediately that \(\mathbf{AC} + \mathbf{AH} + \mathbf{HG} = \mathbf{AE}\) so we are left to sum \(\mathbf{AB}\), \(\mathbf{AE}\) and \(\mathbf{AF}\).

But the diagram above shows us that \(\mathbf{AB} + \mathbf{AF} = \mathbf{AE}\), since \(\mathbf{AE}\) is the diagonal of the rectangle \(ABEF\).

Thus \(\mathbf{AB} + \mathbf{AC} + \mathbf{A} + \mathbf{AH} + \mathbf{HG} = 2\mathbf{AE}\).

From the symmetry of the octagon, we can see that \(AF\) is parallel to \(GH\). The small triangles on \(AH\) and \(FG\) are isoscelese and right-angled, and so \[\big \vert \mathbf{AF} \big \vert = 2 + 2\times \frac{2}{\sqrt{2}} = 2 + 2\sqrt{2}.\]
