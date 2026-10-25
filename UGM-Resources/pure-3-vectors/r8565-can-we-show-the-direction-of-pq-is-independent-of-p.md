---
created: 2026-10-26T04:13:07 (UTC +06:00)
source: https://undergroundmathematics.org/combining-vectors/r8565
author: Underground Mathematics (University of Cambridge)
rights: © University of Cambridge (Underground Mathematics). Use inside SyllabAI is authorised by the
  operator attestation of 2026-10-23 — see LICENSE-DATA.md (Amendment 2026-10-23) in this repository.
  Takedown / correction handling as stated in LICENSE-DATA.md.
tags:
- underground-mathematics
- combining-vectors
- type/review-question
resource_identity:
  ugm_id: r8565
  station: combining-vectors
  station_title: Combining Vectors
  resource_type_id: 10
  resource_type_label: Review question
  level: null
  ref: 8565
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
      confidence: medium
      model_version: GLM (Super Z agent, z.ai) — P3c lane-15 cross-map (cross-map-p3-vectors.json (P3c
        lane 15) @ syllabai-experimental 16c5f80)
      evidence: '''Can we show the direction of P''Q'' is independent of P?'' — an affine-invariance proof
        by vector arithmetic: P'' and Q'' defined by the same construction rule from variable P, and P''Q''
        telescopes to a P-free combination — addition/subtraction of displacement vectors interpreted
        geometrically (3.7.2). Medium: the target is the invariance, not the operations themselves.'
      rationale: 'Canonical UGM title: Can we show the direction of $P''Q''$ is independent of $P$?'
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

# Can we show the direction of $P'Q'$ is independent of $P$?

## Question

The plane \(\pi\) has equation \(\mathbf{r} = \mathbf{a} + \lambda \mathbf{b}+ \mu \mathbf{c}\) and the plane \(\pi'\) has equation \(\mathbf{r} = \mathbf{d}+ \lambda'\mathbf{e}+\mu'\mathbf{f}\), where \(\lambda\), \(\mu\), \(\lambda'\) and \(\mu'\) are scalar parameters. It is given that

\[\mathbf{a}=\begin{pmatrix}1 \\ 0 \\ -1\end{pmatrix}, \mathbf{b}=\begin{pmatrix}2\\ -1 \\ -1\end{pmatrix}, \mathbf{c} = \begin{pmatrix}-1 \\ 2 \\ 1\end{pmatrix}, \mathbf{d} = \begin{pmatrix}0 \\ 1 \\ 1\end{pmatrix}, \mathbf{e} = \begin{pmatrix}p \\ q \\ r\end{pmatrix}, \mathbf{f} = \begin{pmatrix}q\\ r\\ p\end{pmatrix},\]

\(\big \vert\mathbf{e}\big \vert=\big \vert\mathbf{f}\big \vert = \sqrt{30}\) and that \(p\) is negative. The planes \(\pi\) and \(\pi'\) are parallel. Find \(p\), \(q\) and \(r\).

Show that \(\pi'\) is the reflection of \(\pi\) in the origin.

The line \(L\) has equation \[\dfrac{x+1}{9}=\dfrac{y-1}{-6}=\dfrac{z}{-5}\] and lies in \(\pi\). The point \(P\) is in \(\pi\) with parameters \(\lambda = l\) and \(\mu = m\), and \(P'\) is in \(\pi'\) with \(\lambda' = l\) and \(\mu' = m\). The point \(Q'\) is the reflection of \(P\) in the origin. Show that when \(P\) lies on \(L\) the direction of \(P'Q'\) is independent of the position of \(P\) on \(L\).

## Suggestion

If \(\pi\) and \(\pi'\) are parallel, what must be true about the normal of either plane?

How could we use the vector and scalar products here?

If \(P\) is the point \((x,y,z)\), what are the coordinates of the reflection of \(P\) in the origin?

If \(P\) is on \(L\), can we find the coordinates of \(P\) in terms of a parameter \(\alpha\)?

Can we now find the coordinates of \(P'\) and \(Q'\) in terms of \(\alpha\)?

## Solution

We can find a vector perpendicular to \(\pi\) using the [cross product](https://undergroundmathematics.org/glossary/cross-product) \(\mathbf{b} \times \mathbf{c}= \begin{pmatrix}1\\ -1 \\ 3\end{pmatrix}\).

Since the two planes are parallel this is also perpendicular to \(\pi'\). We can use this fact in the dot product with the two direction vectors \(\mathbf{e}\) and \(\mathbf{f}\) in the plane \(\pi'\).

So \(\mathbf{e} . (\mathbf{b} \times \mathbf{c})=0\) and \(\mathbf{f} . (\mathbf{b} \times \mathbf{c})=0\).

Giving us

\[\begin{align} p-q+3r &=0 \\ q-r+3p &=0 \end{align}\]

Adding gives \(4p+2r=0 \quad \implies r=-2p\) and substituting in the second gives \(q=-5p\).

We now know that \(\mathbf{e}= t\begin{pmatrix}1\\-5 \\ -2\end{pmatrix}\). We also know \(\big \vert\mathbf{e}\big \vert = \sqrt{30}\) and \(p\) is negative, hence \(t=-1\) and we have

\(\mathbf{e}= \begin{pmatrix}-1\\5 \\ 2\end{pmatrix}\) and \(\mathbf{f}= \begin{pmatrix}5\\2 \\-1\end{pmatrix}\).

It might be tempting to proceed with vectors perpendicular to \(\pi\) and \(\pi'\) being \(\mathbf{b} \times \mathbf{c}\) and \(\mathbf{e} \times \mathbf{f}\).

\[\mathbf{b}\times \mathbf{c} = \left \vert \begin{matrix}\mathbf{i}&\mathbf{j}&\mathbf{k}\\ 2&-1&-1 \\ -1&2&1\end{matrix}\right \vert = \mathbf{i}-\mathbf{j}+3\mathbf{k}.\]

\[\mathbf{e}\times \mathbf{f}= \left \vert \begin{matrix}\mathbf{i}&\mathbf{j}&\mathbf{k}\\ p&q&r \\ q&r&p\end{matrix}\right \vert = (qp-r^2)\mathbf{i}+(rq-p^2)\mathbf{j}+(pr-q^2)\mathbf{k}.\]

However, the resulting set of simultaneous equations is very difficult to solve.

By adding them we can then simplify using \(\big \vert\mathbf{e}\big \vert=\big \vert\mathbf{f}\big \vert = \sqrt{30}\) in other words \(p^2+q^2+r^2=30\). We can think about \((p+q+r)^2\) to continue the manipulation. Try it if you like!

Using the form of the plane equation \(\mathbf{r}.\mathbf{n}=\mathbf{a}.\mathbf{n}\) with \(\mathbf{n}\) as the normal vector we found earlier, we have the equation of \(\pi\) as \[x - y + 3z = -2.\] Similarly using the point \(\mathbf{d}\), the plane \(\pi'\) is \[x - y + 3z = 2.\]

If \((x_1,y_1,z_1)\) is a point on \(\pi\) then \(x_1 - y_1 + 3z_1 = -2\). Multiplying by \(-1\) gives \((-x_1) -(-y_1) + 3(-z_1) = 2\). So the point \((-x_1,-y_1,-z_1)\) lies on \(\pi'\). Since every point on \(\pi\) has its image reflected in the origin lying on \(\pi'\), the two planes must be reflections in the origin.

Let \(\mathbf{p}\), \(\mathbf{p}'\) and \(\mathbf{q}'\) be the position vectors of \(P\), \(P'\) and \(Q'\) respectively.

We can write the vector equation of the line \(L\) by putting \(\dfrac{x+1}{9}=\dfrac{y-1}{-6}=\dfrac{z}{-5}=\alpha\), and getting \(\mathbf{r} = \begin{pmatrix}9\alpha-1\\-6\alpha+1\\-5\alpha\end{pmatrix}\). So if \(P\) is on \(L\) we have \(\mathbf{p} = \begin{pmatrix}9\alpha-1\\-6\alpha+1\\-5\alpha\end{pmatrix}\) for some \(\alpha\).

We are also told that \(P\) is on \(\pi\) with parameters \(l\) and \(m\), so we have \(\mathbf{p} = \begin{pmatrix}1+2l-m\\-l+2m\\-1-l+m\end{pmatrix}\). This gives us three equations for \(l\), \(m\) and \(\alpha\) which solve to give \[l = 4\alpha -1\text{, and } m = -\alpha.\]

Similarly we have \(\mathbf{p'}= \begin{pmatrix}-l+5m\\1+5l+2m\\1+2l-m\end{pmatrix}\), since \(P'\) is on \(\pi'\) with parameters \(l\) and \(m\) and \(\mathbf{q'}\) is \(\begin{pmatrix}-1-2l+m\\l-2m\\1+l-m\end{pmatrix}\), since \(\mathbf{q'}=-\mathbf{p}\).

Substituting in for \(l\) and \(m\), we find \(\mathbf{p'} = \begin{pmatrix}1-9\alpha\\-4+18\alpha\\-1+9\alpha\end{pmatrix}\), and \(\mathbf{q'}\) is \(\begin{pmatrix}1-9\alpha\\-1+6\alpha\\5\alpha\end{pmatrix}\).

Thus \(\mathbf{q'}-\mathbf{p'}= \begin{pmatrix}0\\-3+12\alpha\\-1+4\alpha\end{pmatrix} = (4\alpha-1)\begin{pmatrix}0\\3\\1\end{pmatrix}\), which is constant in direction whatever the value of \(\alpha\).
