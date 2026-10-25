---
created: 2026-10-26T04:13:07 (UTC +06:00)
source: https://undergroundmathematics.org/combining-vectors/r5813
author: Underground Mathematics (University of Cambridge)
rights: © University of Cambridge (Underground Mathematics). Use inside SyllabAI is authorised by the
  operator attestation of 2026-10-23 — see LICENSE-DATA.md (Amendment 2026-10-23) in this repository.
  Takedown / correction handling as stated in LICENSE-DATA.md.
tags:
- underground-mathematics
- combining-vectors
- type/review-question
resource_identity:
  ugm_id: r5813
  station: combining-vectors
  station_title: Combining Vectors
  resource_type_id: 10
  resource_type_label: Review question
  level: null
  ref: 5813
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
  - code: 3.7.6
    provenance:
      tier: AI_SUGGESTED
      confidence: medium
      model_version: GLM (Super Z agent, z.ai) — P3c lane-15 cross-map (cross-map-p3-vectors.json (P3c
        lane 15) @ syllabai-experimental 16c5f80)
      evidence: '''Given three vectors [lines], can we find a point equidistant from them all?'' — the
        solution measures perpendicular distances to the three lines and states the machinery choice (''X
        was defined to be equidistant from the lines, which suggests using the scalar product'') — scalar
        products in problems involving lines and points, 3.7.6. Medium: the locus wrapper leans on plane
        intersections beyond the P3 line syllabus; the served skill is the perpendicular-distance computation.'
      rationale: 'Canonical UGM title: Given three vectors, can we find a point equidistant from them
        all?'
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

# Given three vectors, can we find a point equidistant from them all?

## Question

The position vectors of points \(A\), \(B\) and \(C\), referred to an origin \(O\), are \(\mathbf{a}\), \(\mathbf{b}\) and \(\mathbf{c}\) respectively, where

\[\begin{align*} \mathbf{a} &= 3\mathbf{i} + 4 \mathbf{j} + 5\mathbf{k}, \\ \mathbf{b} &= 7\mathbf{i} - \mathbf{k}, \\ \mathbf{c} &= 5\mathbf{i} + 5 \mathbf{j}. \\ \end{align*}\]

\(P\) is a point which is equidistant from the lines \(OA\), \(OB\) and \(OC\). Write down expressions for the cosine of the angle between \(OP\) and \(\mathbf{a}\), \(\mathbf{b}\) and \(\mathbf{c}\) respectively and hence deduce an expression for a unit vector in the direction of \(\mathbf{OP}\).

Given that the line \(OP\) meets the plane \(ABC\) at \(Q\), find \(\mathbf{OQ}\).

Given that \(G\) is the centroid of the triangle \(ABC\), show that \(QG\) is parallel to the coordinate plane \(Oyz\).

## Suggestion

We want to find the cosine of an angle between vectors. What does this suggest?

We are also interested in the distance of \(P\) from the lines. Can you draw a diagram showing the point on \(OA\) closest to \(P\)?

We will need equations for both the line \(OP\) and the plane \(ABC\) to find the intersection point.

Can you write the equation of the plane in a helpful form?

Can we define the position vector of \(G\) in terms of the those of the three corners?

Which vectors are parallel to the coordinate plane \(Oyz\)?

## Solution

Let \(A'\) be a point on \(OA\) such that \(A'P\) is perpendicular to \(OA\) and let \(B'\) and \(C'\) be the equivalent points on \(OB\) and \(OC\) respectively.

If we think about the three right angled triangles \(A'OP\), \(B'OP\) and \(C'OP\) we have hypotenuse \(OP\) common to each and \(P\) was defined to be equidistant from the lines \(OA\), \(OB\) and \(OC\). So \(OA'=OB'=OC'\) making the triangles congruent (RHS).

The question asks about the cosine of the angle \(\alpha\), which suggests using the scalar product. Let the vector \(OP\) be \(\mathbf{p} = \begin{pmatrix}p_i \\ p_j \\ p_k\end{pmatrix}\), so we have \(\mathbf{p}.\mathbf{a} = 3p_i+4p_j+5p_k\).

But \(\mathbf{p}.\mathbf{a} = |\mathbf{p}||\mathbf{a}|\cos \alpha\), so \(\cos \alpha = \dfrac{\mathbf{p}.\mathbf{a}}{|\mathbf{p}|\sqrt{50}}=\dfrac{3p_i+4p_j+5p_k}{|\mathbf{p}|\sqrt{50}}\). We have used the fact that \(|\mathbf{a}|=\sqrt{3^2+4^2+5^2} = \sqrt{50}\).

Since the three triangles are congruent, they each contain the same angle \(\alpha\). Also notice that \(|\mathbf{b}|=|\mathbf{c}|=\sqrt{50}\).

So for vector \(\mathbf{b}\) we have \(\cos \alpha= \dfrac{7p_i-p_k}{|\mathbf{p}|\sqrt{50}}\), and for \(\mathbf{c}\) we have \(\cos \alpha = \dfrac{5p_i+5p_j}{|\mathbf{p}|\sqrt{50}}\).

Combining these we can write \(3p_i+4p_j+5p_k = 7p_i-p_k= 5p_i+5p_j\).

Using the second and third parts gives \(p_k = 2p_i - 5p_j\), and substituting this into the first two parts gives \(3p_i+4p_j+5(2p_i - 5p_j) = 7p_i-(2p_i - 5p_j)\).

Thus \(p_j = \dfrac{4}{13} p_i\), and \(p_k = \dfrac{6}{13} p_i\), and so the vector \(\mathbf{p}\) is \(t \begin{pmatrix}13 \\ 4 \\ 6\end{pmatrix}\) for some scalar \(t\).

To find the unit vector in this direction, we divide by the magnitude \(\sqrt{13^2+4^2+6^2} = \sqrt{221}\), and so the unit vector in the direction of \(\mathbf{OP}\) is \[\hat{\mathbf{p}} = \frac{13}{\sqrt{221}} \mathbf{i} + \frac{4}{\sqrt{221}}\mathbf{j} + \frac{6}{\sqrt{221}}\mathbf{k}.\]

We can define the plane \(ABC\) from the three position vectors \(\mathbf{a}\), \(\mathbf{b}\) and \(\mathbf{c}\) via \[\mathbf{r} = \mathbf{a} + \lambda(\mathbf{b}-\mathbf{a}) + \mu(\mathbf{c}-\mathbf{a}),\] where \(\lambda\) and \(\mu\) are scalar parameters.

If we start at the origin, \(\mathbf{a}\) takes us onto the plane. The vectors \((\mathbf{b}-\mathbf{a})\) and \((\mathbf{c}-\mathbf{a})\) are distinct vectors lying in the plane, so a linear combination of these will take us anywhere on the plane from \(\mathbf{a}\).

Thus the plane \(ABC\) is \[\mathbf{r} = (3+4\lambda+2\mu)\mathbf{i} + (4-4\lambda+\mu) \mathbf{j} + (5-6\lambda-5\mu)\mathbf{k}.\]

The line \(OP\) is given by \(\mathbf{r} = t (13\mathbf{i}+ 4\mathbf{j}+ 6\mathbf{k})\). To find the intersection we set these equal, then the three components give us three equations in three unknowns, \(\lambda\), \(\mu\) and \(t\).

Solving these simultaneously gives

\(t = \dfrac{5}{13}\)

and so

\(\mathbf{OQ}\)

=

\(5\mathbf{i} + \frac{20}{13}\mathbf{j} +\frac{30}{13}\mathbf{k}\)

.

The position vector of the [centroid](https://undergroundmathematics.org/glossary/centroid) \(G\) of a triangle whose vertices have position vectors \(\mathbf{a}\), \(\mathbf{b}\) and \(\mathbf{c}\) is given by \[\mathbf{g}=\frac{\mathbf{a}+\mathbf{b}+\mathbf{c}}{3}.\] In our case \[\mathbf{g}=5 \mathbf{i} + 3 \mathbf{j} + \frac{4}{3} \mathbf{k}.\]

The direction of the line \(QG\) is given by the vector \(\mathbf{g}-\mathbf{OQ}\).

If this direction vector is parallel to the \(Oyz\) plane, its \(x\)-component will be zero. Hence we have to show that \(q_i = g_i\).

The \(x\)-components of \(\mathbf{g}\) and \(\mathbf{OQ}\) are both \(5\), so \(QG\) is indeed parallel to the plane.
