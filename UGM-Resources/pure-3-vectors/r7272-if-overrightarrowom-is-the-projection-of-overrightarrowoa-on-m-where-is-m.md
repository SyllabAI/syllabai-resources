---
created: 2026-10-26T04:13:07 (UTC +06:00)
source: https://undergroundmathematics.org/combining-vectors/r7272
author: Underground Mathematics (University of Cambridge)
rights: © University of Cambridge (Underground Mathematics). Use inside SyllabAI is authorised by the
  operator attestation of 2026-10-23 — see LICENSE-DATA.md (Amendment 2026-10-23) in this repository.
  Takedown / correction handling as stated in LICENSE-DATA.md.
tags:
- underground-mathematics
- combining-vectors
- type/review-question
resource_identity:
  ugm_id: r7272
  station: combining-vectors
  station_title: Combining Vectors
  resource_type_id: 10
  resource_type_label: Review question
  level: null
  ref: 7272
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
      confidence: high
      model_version: GLM (Super Z agent, z.ai) — P3c lane-15 cross-map (cross-map-p3-vectors.json (P3c
        lane 15) @ syllabai-experimental 16c5f80)
      evidence: '''If OM is the projection of OA on m, where is M?'' — the solution identifies M as ''the
        foot of the perpendicular from A to the line m'' and computes it with the scalar product — ''finding
        the foot of the perpendicular from a point to a line'' is 3.7.6''s own example language, here
        done BY scalar products.'
      rationale: 'Canonical UGM title: If $\overrightarrow{OM}$ is the projection of $\overrightarrow{OA}$
        on $m$, where is $M$?'
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

# If $\overrightarrow{OM}$ is the projection of $\overrightarrow{OA}$ on $m$, where is $M$?

## Question

The straight lines \(l\) and \(m\) intersect at the origin \(O\), and their directions are parallel to \(\mathbf{i}\) and \(\mathbf{i}+2\mathbf{j}\) respectively. The point \(A\) has position vector \(\overrightarrow{OA}\) given by \(2\mathbf{i}+3\mathbf{j}+5\mathbf{k}\). The point \(L\) on \(l\) is such that \(\overrightarrow{OL}\) is the projection of \(\overrightarrow{OA}\) on \(l\), and the point \(M\) on \(m\) is such that \(\overrightarrow{OM}\) is the projection of \(\overrightarrow{OA}\) on \(m\). State the position vector of \(L\), and show that \(\overrightarrow{OM} = \dfrac{8}{5}\mathbf{i}+ \dfrac{16}{5}\mathbf{j}\).

Calculate the angle \(MAL\), giving your answer correct to the nearest degree.

The point \(N\), where \(\overrightarrow{ON} = 2\mathbf{i} + 3\mathbf{j}\), is the foot of the perpendicular from \(A\) on to the plane \(OLM\). The lines \(ON\) and \(LM\) intersect at \(X\). Show that \(\dfrac{OX}{ON} = \dfrac{16}{19}\).

## Suggestion

Drawing a diagram should help to clarify what is being described here.

If \(\overrightarrow{OL}\) is the projection of \(\overrightarrow{OA}\) on \(l\) it means that \(\overrightarrow{OL}\) is the component of \(\overrightarrow{OA}\) in the direction of \(l\). So we can find \(L\) by dropping a perpendicular…

To find the angle between vectors we can often use the dot product.

Can we find the position vector of \(N\)? From there, can we find the position vector of \(X\)?

## Solution

Since \(l\) is parallel to \(\mathbf{i}\) (or the \(x\)-axis), the vector \(\overrightarrow{OL}\) is the \(\mathbf{i}\)-component of \(\overrightarrow{OA}\). So the position vector of \(L\) is \(2\mathbf{i}\).

The point

\(M\)

is on

\(m\)

, so its position vector can be written as

\(\mu(\mathbf{i}+2\mathbf{j})\)

for some number

\(\mu\)

. Since it is the projection, it follows that

\(m\)

and

\(\overrightarrow{AM}\)

are perpendicular. In other words, their

dot product

is zero.

\[\begin{align*} (\mathbf{i}+2\mathbf{j}) . ((\mu-2)\mathbf{i}+(2\mu-3)\mathbf{j}-5\mathbf{k}) &= 0 \\ \implies\quad (\mu-2)+2(2\mu-3) &= 0 \\ \implies\quad \mu &= \frac{8}{5} \end{align*}\]

So \(\overrightarrow{OM} = \dfrac{8}{5}\mathbf{i}+ \dfrac{16}{5}\mathbf{j}\) as required.

We require the angle between the vectors \(\overrightarrow{AM}\) and \(\overrightarrow{AL}\) and we can find this using the dot product.

\[\begin{align*} \overrightarrow{AM} &= \overrightarrow{OM} -\overrightarrow{OA} = \dfrac{8}{5}\mathbf{i}+ \dfrac{16}{5}\mathbf{j} - (2\mathbf{i}+3\mathbf{j}+5\mathbf{k}) = -\frac{2}{5}\mathbf{i} + \frac{1}{5}\mathbf{j} - 5\mathbf{k} \\ \overrightarrow{AL} &= \overrightarrow{OL} -\overrightarrow{OA} = 2\mathbf{i} - (2\mathbf{i}+3\mathbf{j}+5\mathbf{k}) = -3\mathbf{j}-5\mathbf{k} \end{align*}\]

So now,

\[\begin{align*} \overrightarrow{AM} . \overrightarrow{AL} &= 0-\frac{3}{5}+25 = \frac{122}{5} \\ &= \big\vert AM\big\vert\times\big\vert AL\big\vert\cos\theta \\ &= \sqrt{\left(\tfrac{2}{5}\right)^2 + \left(\tfrac{1}{5}\right)^2 +5^2}\sqrt{3^2+5^2}\cos\theta \\ &= \sqrt{\tfrac{126}{5}}\sqrt{34}\cos\theta \\ \implies\quad \cos\theta &=\frac{122/5}{\sqrt{126/5}\sqrt{34}}\approx0.8336 \\ \implies\quad \theta &\approx33.53^\circ \end{align*}\]

The angle \(MAL\) is \(34^\circ\).

We can now work in two dimensions. We have that \(\overrightarrow{OL} = 2\mathbf{i}\), \(\overrightarrow{OM} = \frac{8}{5}\mathbf{i}+\frac{16}{5}\mathbf{j}\) and \(\overrightarrow{ON} = 2\mathbf{i}+3\mathbf{j}\). Let \(\overrightarrow{OX} = \alpha (2\mathbf{i}+3\mathbf{j})\) so that \(\alpha\) is the required ratio.

The vector \(\overrightarrow{LM} = \frac{8}{5}\mathbf{i}+\frac{16}{5}\mathbf{j} - 2\mathbf{i} = -\frac{2}{5}\mathbf{i}+\frac{16}{5}\mathbf{j}\).

The line

\(LM\)

is

\(\mathbf{r} = 2\mathbf{i} + \beta(-\frac{2}{5}\mathbf{i}+\frac{16}{5}\mathbf{j})\)

. So at

\(X\)

,

\[ \alpha (2\mathbf{i}+3\mathbf{j}) = 2\mathbf{i} + \beta\left(-\tfrac{2}{5}\mathbf{i}+\tfrac{16}{5}\mathbf{j}\right) \]

Comparing coefficients, we have

\[\begin{align*} 2\alpha &= 2-\tfrac{2}{5}\beta \text{ and } 3\alpha = \tfrac{16}{5}\beta \\ \implies\quad \alpha &= \frac{16}{19} \end{align*}\]

as required.

The line $LM$ is $\mathbf{r} = \begin{pmatrix}2\\0\end{pmatrix} + \mu \begin{pmatrix}-2/5\\16/5\end{pmatrix}$, and so $\lambda \begin{pmatrix}2\\3\end{pmatrix} = \begin{pmatrix}2\\0\end{pmatrix} + \mu \begin{pmatrix}-2/5\\16/5\end{pmatrix}$ for some $\mu$. Thus $2\lambda = 2 + -\dfrac{2}{5}\mu$, and $3\lambda = \dfrac{16}{5}\mu \implies \mu = \dfrac{15}{16}\lambda \implies 2 \lambda = 2 + -\dfrac{2}{5}\times \dfrac{15}{16}\lambda$, which gives us $\lambda = \dfrac{16}{19}$. So $\dfrac{OX}{ON} = \dfrac{16}{19}$, as required.
