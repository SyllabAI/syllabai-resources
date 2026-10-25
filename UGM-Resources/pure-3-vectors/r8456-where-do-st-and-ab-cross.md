---
created: 2026-10-26T04:13:07 (UTC +06:00)
source: https://undergroundmathematics.org/combining-vectors/r8456
author: Underground Mathematics (University of Cambridge)
rights: © University of Cambridge (Underground Mathematics). Use inside SyllabAI is authorised by the
  operator attestation of 2026-10-23 — see LICENSE-DATA.md (Amendment 2026-10-23) in this repository.
  Takedown / correction handling as stated in LICENSE-DATA.md.
tags:
- underground-mathematics
- combining-vectors
- type/review-question
resource_identity:
  ugm_id: r8456
  station: combining-vectors
  station_title: Combining Vectors
  resource_type_id: 10
  resource_type_label: Review question
  level: null
  ref: 8456
  old_site_id: null
spec_map:
  curriculum_code: CIE-9709-P3-2023
  lane: cie-a-level-maths-20-pure-3
  board: Cambridge CIE
  syllabus_version: 2023-2025
  subsection: combining-vectors
  subsection_provenance:
    tier: PROVIDER
    signal: source-url-slug
    slug: combining-vectors
    validation_status: SUGGESTED
  spec_points:
  - code: 3.7.2
    provenance:
      tier: AI_SUGGESTED
      confidence: high
      model_version: GLM (Super Z agent, z.ai) — P3c lane-15 cross-map (cross-map-p3-vectors.json (P3c
        lane 15) @ syllabai-experimental 16c5f80)
      evidence: 'Two-part exam-register question: (i) ''evaluate OM.ON and hence calculate angle MON to
        the nearest degree'' — the scalar product formula and its angle use, 3.7.6 verbatim; (ii) S, T
        at 2p, 2q with OA = AS (midpoint) and OT = 2TB, then AR = lambda*AB, SR = mu*ST and ''express
        OR in terms of p and q'' twice, solving the two expressions — midpoint/ratio understanding (3.7.2)
        and the intersection-of-lines lambda/mu technique. PROMOTION: supersedes its stale lane-3-algebra
        non-overlap row of record (the r8013 precedent — the resource''s centre of gravity is vector machinery,
        not algebra).'
      rationale: 'Canonical UGM title: Where do $ST$ and $AB$ cross?'
      validation_status: SUGGESTED
    title: carry out addition and subtraction of vectors and multiplication of a vector by a scalar, and
      interpret these operations in geometrical terms The general form of the ratio theorem is not included,
      but understanding that the midpoint of
  - code: 3.7.6
    provenance:
      tier: AI_SUGGESTED
      confidence: high
      model_version: GLM (Super Z agent, z.ai) — P3c lane-15 cross-map (cross-map-p3-vectors.json (P3c
        lane 15) @ syllabai-experimental 16c5f80)
      evidence: 'Two-part exam-register question: (i) ''evaluate OM.ON and hence calculate angle MON to
        the nearest degree'' — the scalar product formula and its angle use, 3.7.6 verbatim; (ii) S, T
        at 2p, 2q with OA = AS (midpoint) and OT = 2TB, then AR = lambda*AB, SR = mu*ST and ''express
        OR in terms of p and q'' twice, solving the two expressions — midpoint/ratio understanding (3.7.2)
        and the intersection-of-lines lambda/mu technique. PROMOTION: supersedes its stale lane-3-algebra
        non-overlap row of record (the r8013 precedent — the resource''s centre of gravity is vector machinery,
        not algebra).'
      rationale: 'Canonical UGM title: Where do $ST$ and $AB$ cross?'
      validation_status: SUGGESTED
    title: use formulae to calculate the scalar product of e.g. finding the angle between two lines, and
      finding two vectors, and use scalar products in problems the foot of the perpendicular from a point
      to a line; involving lines and points. questions may involve 3D objects such as cuboids, tetrahedra
      (pyramids), etc.
  mapped_date: '2026-10-26'
  mapper: cross-map-p3-vectors.json (P3c lane 15) @ syllabai-experimental 16c5f80
provenance:
  capture_date: '2026-10-22'
  capture_tool: P2 full-site crawl (ugm-crawl) → ugm-clean extraction; text-only import
  content_language: en
  task: T-UGM-IMPORT-15
---

# Where do $ST$ and $AB$ cross?

## Question

1. Given that \(\overrightarrow{OM}=\mathbf{i}+3\mathbf{j}\) and \(\overrightarrow{ON}=\mathbf{i}+\mathbf{j}\), evaluate \(\overrightarrow{OM}.\overrightarrow{ON}\) and hence calculate \(\widehat{MON}\) to the nearest degree.

---

1. The position vectors, relative to an Origin \(O\), of two points \(S\) and \(T\) are \(2\mathbf{p}\) and \(2\mathbf{q}\) respectively. The point \(A\) lies on \(OS\) and is such that \(OA=AS\). The point \(B\) lies on \(OT\) produced and is such that \(OT=2TB\). The lines \(ST\) and \(AB\) intersect at \(R\). Given that \(\overrightarrow{AR}=\lambda \overrightarrow{AB}\) and that \(\overrightarrow{SR}=\mu \overrightarrow{ST}\), express \(\overrightarrow{OR}\)  in terms of \(\mathbf{p}\), \(\mathbf{q}\) and \(\lambda\), (ii) in terms of \(\mathbf{p}\), \(\mathbf{q}\) and \(\mu\).  Hence evaluate \(\lambda\) and \(\mu\) and express \(\overrightarrow{OR}\) in terms of \(\mathbf{p}\) and \(\mathbf{q}\).

## Solution

Given two vectors \(\mathbf{f} = \begin{pmatrix}a\\b\end{pmatrix}\) and \(\mathbf{g} = \begin{pmatrix}c\\d\end{pmatrix}\), the [dot product](https://undergroundmathematics.org/glossary/dot-product) is defined as \[\mathbf{f.g} = ac+bd = \big \vert \mathbf{f} \big\vert \big\vert \mathbf{g} \big \vert \cos \theta,\] where \(\theta\) is the angle between \(\mathbf{f}\) and \(\mathbf{g}\), and where \(\big \vert \mathbf{f} \big\vert\) is the [modulus](https://undergroundmathematics.org/glossary/modulus) of the vector \(\mathbf{f}\).

Here we have \(\overrightarrow{OM}.\overrightarrow{ON} = \begin{pmatrix}1\\3\end{pmatrix}.\begin{pmatrix}1\\1\end{pmatrix} = 1 + 3 = 4\).

And we have \(\overrightarrow{OM}.\overrightarrow{ON}=\sqrt{1^2+3^2}\sqrt{1^2+1^2} \cos \widehat{MON}\), which yields \[\cos\widehat{MON} = \frac{4}{\sqrt{10}\sqrt{2}} = \frac{2}{\sqrt{5}}.\]

Substituting in the values and rounding to the nearest degree, we find \[\widehat{MON} =27^\circ.\]

The diagram shows the positions of \(O, A, B, R, S\), and \(T\). Travelling from \(O\) to \(R\) along the red line gives \(\overrightarrow{OR} = \overrightarrow{OA} + \lambda \overrightarrow{AB} = \mathbf{p} + \lambda (3\mathbf{q}-\mathbf{p})\).

Following the new red path, we have \[\overrightarrow{OR} = 2\mathbf{q}+(1-\mu)(2\mathbf{p}-2\mathbf{q})=2\mathbf{p}+2\mu(\mathbf{q}-\mathbf{p}).\]

The two expressions we derived for \(\overrightarrow{OR}\) have to be equal. Hence we know that \[\mathbf{p}+\lambda(3\mathbf{q}-\mathbf{p})=2\mathbf{p}+2\mu(\mathbf{q}-\mathbf{p}).\]

Rearranging this equation, we find \((3\lambda-2\mu)\mathbf{q}-(\lambda+1-2\mu)\mathbf{p}=0.\)

Assuming that vectors \(\mathbf{p}\) and \(\mathbf{q}\) are not parallel or zero, then no linear combination of them can vanish unless both coefficients vanish.

In other words, if \(a\mathbf{p} + b\mathbf{q} = 0\) for constants \(a\) and \(b\), then \(a = b = 0\).

Hence we have the pair of simultaneous equations

\[\begin{align*} 3\lambda-2\mu &= 0,\\ \lambda+1-2\mu &=0, \end{align*}\]

from which we conclude \(\lambda=\dfrac{1}{2}\) and \(\mu=\dfrac{3}{4}\), and so \[\overrightarrow{OR} = \frac{3}{2}\mathbf{q}+\frac{1}{2}\mathbf{p}.\]
