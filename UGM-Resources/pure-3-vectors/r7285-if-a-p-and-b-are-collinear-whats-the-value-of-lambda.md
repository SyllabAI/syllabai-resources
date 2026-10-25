---
created: 2026-10-26T04:13:07 (UTC +06:00)
source: https://undergroundmathematics.org/vector-geometry/r7285
author: Underground Mathematics (University of Cambridge)
rights: © University of Cambridge (Underground Mathematics). Use inside SyllabAI is authorised by the
  operator attestation of 2026-10-23 — see LICENSE-DATA.md (Amendment 2026-10-23) in this repository.
  Takedown / correction handling as stated in LICENSE-DATA.md.
tags:
- underground-mathematics
- vector-geometry
- type/review-question
resource_identity:
  ugm_id: r7285
  station: vector-geometry
  station_title: Vector Geometry
  resource_type_id: 10
  resource_type_label: Review question
  level: null
  ref: 7285
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
      evidence: '''If A, P and B are collinear, what is the value of lambda?'' — the solution writes OP
        = OL + lambda*LM, expands in the basis {a, b}, and invokes unique decomposition (''any vector
        in the plane can be written uniquely as'') to solve 3*lambda = mu and 1/2 + lambda/2 = mu — collinearity
        via position vectors (3.7.3) riding vector algebra with geometrical meaning (3.7.2).'
      rationale: 'Canonical UGM title: If $A$, $P$ and $B$ are collinear, what''s the value of $\lambda$?'
      validation_status: SUGGESTED
    title: carry out addition and subtraction of vectors and multiplication of a vector by a scalar, and
      interpret these operations in geometrical terms The general form of the ratio theorem is not included,
      but understanding that the midpoint of
  - code: 3.7.3
    provenance:
      tier: AI_SUGGESTED
      confidence: high
      model_version: GLM (Super Z agent, z.ai) — P3c lane-15 cross-map (cross-map-p3-vectors.json (P3c
        lane 15) @ syllabai-experimental 16c5f80)
      evidence: '''If A, P and B are collinear, what is the value of lambda?'' — the solution writes OP
        = OL + lambda*LM, expands in the basis {a, b}, and invokes unique decomposition (''any vector
        in the plane can be written uniquely as'') to solve 3*lambda = mu and 1/2 + lambda/2 = mu — collinearity
        via position vectors (3.7.3) riding vector algebra with geometrical meaning (3.7.2).'
      rationale: 'Canonical UGM title: If $A$, $P$ and $B$ are collinear, what''s the value of $\lambda$?'
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

# If $A$, $P$ and $B$ are collinear, what's the value of $\lambda$?

## Question

Points \(A\) and \(B\) have position vectors \(\mathbf{a}\) and \(\mathbf{b}\) respectively relative to a point \(O\). Given that \(L\) is the midpoint of \(OA\), and that \(M\) is the point on \(OB\) produced such that \(OM = 3OB\), express \(\overrightarrow{LM}\) in terms of \(\mathbf{a}\) and \(\mathbf{b}\).

Given further that \(P\) is the point on \(LM\) such that \(LP = \lambda LM\), express \(\overrightarrow{AP}\) in terms of \(\mathbf{a, b}\) and \(\lambda\).

In the case where \(A, P\) and \(B\) are collinear, calculate the value of

1. \(\lambda\)

---

1. \(\dfrac{AP}{PB}\).

## Solution

We have that \(\overrightarrow{OM} = 3\mathbf{b}, \overrightarrow{OL} = \dfrac{1}{2}\mathbf{a}\), so \(\overrightarrow{LM}= 3\mathbf{b}- \dfrac{1}{2}\mathbf{a}.\)

The vector

\[\begin{align*} \overrightarrow{AP} &= \overrightarrow{OP} - \overrightarrow{OA} \\ &= (\overrightarrow{OL}+\lambda \overrightarrow{LM}) - \mathbf{a} \\ &= \dfrac{1}{2}\mathbf{a}+\lambda\left( 3\mathbf{b}- \dfrac{1}{2}\mathbf{a}\right) -\mathbf{a}\\ &=3\lambda \mathbf{b} - \dfrac{1}{2}\mathbf{a}(1+\lambda). \end{align*}\]

If \(P\) is on \(AB\), then \(\overrightarrow{AP} = \mu\overrightarrow{AB}\) for some scalar \(\mu\). This means that \[3\lambda \mathbf{b} - \dfrac{1}{2}\mathbf{a}(1+\lambda) = \mu(\mathbf{b}-\mathbf{a}).\]

Now any vector in the plane can be written uniquely as \(\alpha\, \mathbf{a} + \beta\, \mathbf{b}\), so we can compare the coefficients of \(\mathbf{a}\) and \(\mathbf{b}\) here, giving \[3\lambda = \mu \quad\text{and}\quad \dfrac{1}{2} + \dfrac{\lambda}{2} = \mu,\] which solve to give \[\lambda = \dfrac{1}{5}, \mu = \dfrac{3}{5}.\]

Thus

1. \(\lambda = \dfrac{1}{5}\)

---

1. \(\dfrac{AP}{PB} = \dfrac{\mu}{1-\mu} = \dfrac{3/5}{2/5} = \dfrac{3}{2}\).
