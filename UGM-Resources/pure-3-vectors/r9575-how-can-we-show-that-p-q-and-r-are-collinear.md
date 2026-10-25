---
created: 2026-10-26T04:13:07 (UTC +06:00)
source: https://undergroundmathematics.org/vector-geometry/r9575
author: Underground Mathematics (University of Cambridge)
rights: © University of Cambridge (Underground Mathematics). Use inside SyllabAI is authorised by the
  operator attestation of 2026-10-23 — see LICENSE-DATA.md (Amendment 2026-10-23) in this repository.
  Takedown / correction handling as stated in LICENSE-DATA.md.
tags:
- underground-mathematics
- vector-geometry
- type/review-question
resource_identity:
  ugm_id: r9575
  station: vector-geometry
  station_title: Vector Geometry
  resource_type_id: 10
  resource_type_label: Review question
  level: null
  ref: 9575
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
  - code: 3.7.3
    provenance:
      tier: AI_SUGGESTED
      confidence: high
      model_version: GLM (Super Z agent, z.ai) — P3c lane-15 cross-map (cross-map-p3-vectors.json (P3c
        lane 15) @ syllabai-experimental 16c5f80)
      evidence: '''How can we show that P, Q and R are collinear?'' — the solution states the criterion
        verbatim (''Three points with position vectors ... are collinear if and only if the vectors [PQ
        and PR are parallel]'') and executes it — position-vector collinearity, the 3.7.3 displacement/position-vector
        skill of record. PICK 3.7.3: the definitive criterion statement.'
      rationale: 'Canonical UGM title: How can we show that $P, Q$ and $R$ are collinear?'
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

# How can we show that $P, Q$ and $R$ are collinear?

## Question

1. A vector of magnitude \(OP\) in the direction from \(O\) to \(P\) is represented by \(\mathbf{OP}\). If \(\mathbf{OP}-3\mathbf{OQ}+2\mathbf{OR}=\mathbf{0}\), show that \(P\),\(Q\),\(R\) are collinear.

---

1. A unit vector parallel to the \(x\)-axis is represented by \(\mathbf{i}\) and a unit vector parallel to the \(y\)-axis by \(\mathbf{j}\). If \(\mathbf{OP}=a\mathbf{i}+s\mathbf{j}\) and \(\mathbf{OQ}=-a\mathbf{i}+t\mathbf{j}\), where \(a\) is a constant and \(s\) and \(t\) are variables, show that the loci of \(P\) and \(Q\) are parallel straight lines. In this case find \(\mathbf{OQ}\) when \(\mathbf{OP}=2\mathbf{i}+3\mathbf{j}\) and \(OQ\) is perpendicular to \(OP\).

## Suggestion

If three points \(\mathbf{a}, \mathbf{b}\) and \(\mathbf{c}\) are collinear, can we find a connection between \(\mathbf{a}, \mathbf{b}\) and \(\mathbf{c}\)?

Can we draw a helpful diagram? What is the gradient of each line? What do we know if two lines are perpendicular?

## Solution

Three points with position vectors \(\mathbf{a}\), \(\mathbf{b}\) and \(\mathbf{c}\) are collinear if and only if the vectors \((\mathbf{a}-\mathbf{b})\) and \((\mathbf{a}-\mathbf{c})\) are parallel.

In other words, to prove collinearity, we would need to show \((\mathbf{a}-\mathbf{b})=k(\mathbf{a}-\mathbf{c})\) for some constant \(k\).

For our example, we have \(\mathbf{OP}-\mathbf{OQ}= 2(\mathbf{OQ}-\mathbf{OR})\), and so \(\mathbf{OQ}-\mathbf{OP}= -2(\mathbf{OQ}-\mathbf{OR})\), telling us that \(P, Q\) and \(R\) are collinear.

The locus of \(P\) will be the line \(x = a\), while the locus of \(Q\) will be \(x = -a\). These are parallel straight lines.

The diagram shows the case \(a = 2\). The point \(P\) is at \((2,3)\), and \(Q\) is at \((-2,k)\).

We are told that \(OP\) and \(OQ\) are perpendicular, so the gradients of \(OP\) and \(OQ\) must multiply to \(-1\).

We could alternatively use that \(\mathbf{OP}.\mathbf{OQ}=0\).

Thus \(\dfrac{3}{2} \times \dfrac{k}{-2}=-1 \implies k = \dfrac{4}{3}\). Thus \(\mathbf{OQ} = -2\mathbf{i}+\dfrac{4}{3}\mathbf{j}\).
