---
created: 2026-10-26T04:13:07 (UTC +06:00)
source: https://undergroundmathematics.org/vector-geometry/r6007
author: Underground Mathematics (University of Cambridge)
rights: © University of Cambridge (Underground Mathematics). Use inside SyllabAI is authorised by the
  operator attestation of 2026-10-23 — see LICENSE-DATA.md (Amendment 2026-10-23) in this repository.
  Takedown / correction handling as stated in LICENSE-DATA.md.
tags:
- underground-mathematics
- vector-geometry
- type/review-question
resource_identity:
  ugm_id: r6007
  station: vector-geometry
  station_title: Vector Geometry
  resource_type_id: 10
  resource_type_label: Review question
  level: null
  ref: 6007
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
      evidence: '''Can we find the position vector of the intersection from the given ratios?'' — two
        lines given by position-vector/ratio data; the solution writes the intersection point two ways
        (via each line''s parameter) and equates — position vectors of points on lines (3.7.3) meeting
        the intersection of two lines (3.7.5) through ratio reasoning.'
      rationale: 'Canonical UGM title: Can we find the position vector of the intersection from the given
        ratios?'
      validation_status: SUGGESTED
    title: calculate the magnitude of a vector, and use In 2 or 3 dimensions. unit vectors, displacement
      vectors and position vectors
  - code: 3.7.5
    provenance:
      tier: AI_SUGGESTED
      confidence: high
      model_version: GLM (Super Z agent, z.ai) — P3c lane-15 cross-map (cross-map-p3-vectors.json (P3c
        lane 15) @ syllabai-experimental 16c5f80)
      evidence: '''Can we find the position vector of the intersection from the given ratios?'' — two
        lines given by position-vector/ratio data; the solution writes the intersection point two ways
        (via each line''s parameter) and equates — position vectors of points on lines (3.7.3) meeting
        the intersection of two lines (3.7.5) through ratio reasoning.'
      rationale: 'Canonical UGM title: Can we find the position vector of the intersection from the given
        ratios?'
      validation_status: SUGGESTED
    title: determine whether two lines are parallel, Calculation of the shortest distance between two
      intersect or are skew, and find the point of skew lines is not required. Finding the equation of
      intersection of two lines when it exists the common perpendicular to two skew lines is also not
      required.
  mapped_date: '2026-10-26'
  mapper: cross-map-p3-vectors.json (P3c lane 15) @ syllabai-experimental 16c5f80
provenance:
  capture_date: '2026-10-22'
  capture_tool: P2 full-site crawl (ugm-crawl) → ugm-clean extraction; text-only import
  content_language: en
  task: T-UGM-IMPORT-15
---

# Can we find the position vector of the intersection from the given ratios?

## Question

The position vectors of three points \(O, A\) and \(B\) are \(\begin{pmatrix}0\\0\end{pmatrix}, \begin{pmatrix}3\\3.5\end{pmatrix}\) and \(\begin{pmatrix}6\\-1.5\end{pmatrix}\) respectively. Given that \(\mathbf{OD} = \dfrac{1}{3}\mathbf{OB}\) and \(\mathbf{AE} = \dfrac{1}{4}\mathbf{AB}\) write down the position vectors of \(D\) and \(E\).

Given also that \(OE\) and \(AD\) intersect at \(X\), and that \(\mathbf{OX} = p\:\mathbf{OE}\), and that \(\mathbf{XD} = q\:\mathbf{AD}\), find the position vector of \(X\) in terms of (i) \(p\) (ii) \(q\).

Hence calculate \(p\) and \(q\).

## Suggestion

How can we express the position vector of \(E\) in terms of things we already know? (A diagram might help.)

What other ways can we express \(\mathbf{XD}\)? Which of these use the position vector of \(X\)? Can we rearrange this in a helpful way?

How can we derive two simultaneous equations in \(p\) and \(q\) from our work above?

## Solution

For convenience, we define \(\mathbf{a}=\mathbf{OA}\) and similarly \(\mathbf{b}\), \(\mathbf{d}\), \(\mathbf{e}\) and \(\mathbf{x}\).

We are told that \[\mathbf{d}=\dfrac{1}{3}\mathbf{b}=\begin{pmatrix}2\\-\frac{1}{2}\end{pmatrix}.\]

We also have that

\[\begin{align*} \mathbf{AE} &= \frac{1}{4}\mathbf{AB} \\ \implies\quad (\mathbf{e}-\mathbf{a}) &= \frac{1}{4}(\mathbf{b}-\mathbf{a}) \\ \implies\quad \mathbf{e} &= \frac{1}{4}\mathbf{b} + \frac{3}{4}\mathbf{a} = \cmarraystretch{1.4}\begin{pmatrix}\frac{15}{4}\\\frac{9}{4}\end{pmatrix}. \end{align*}\]

We have \[\mathbf{x} = p\:\mathbf{e} = \cmarraystretch{1.4}\begin{pmatrix}\frac{15}{4}p\\\frac{9}{4}p\end{pmatrix}.\]

We also know that

\[\begin{align*} \mathbf{x} &= \mathbf{d} + \mathbf{DX}\\ &=\mathbf{d} + q(\mathbf{a}-\mathbf{d})\\ &=\begin{pmatrix}2\\-\frac{1}{2}\end{pmatrix}+q\begin{pmatrix}1\\4\end{pmatrix}\\ &=\cmarraystretch{1.4}\begin{pmatrix}2+q\\-\frac{1}{2}+4q\end{pmatrix}. \end{align*}\]

Our two expressions for \(\mathbf{x}\) must be the same, so \[\cmarraystretch{1.4}\begin{pmatrix}\frac{15}{4}p\\\frac{9}{4}p\end{pmatrix} = \begin{pmatrix}2+q\\-\frac{1}{2}+4q\end{pmatrix}.\]

Equating the \(x\) and \(y\) components separately gives us two simultaneous equations which we can solve to find \[p = \dfrac{2}{3} \quad\text{and}\quad q = \dfrac{1}{2}.\]
