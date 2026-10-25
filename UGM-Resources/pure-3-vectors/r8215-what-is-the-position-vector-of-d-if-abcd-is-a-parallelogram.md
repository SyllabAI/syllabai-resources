---
created: 2026-10-26T04:13:07 (UTC +06:00)
source: https://undergroundmathematics.org/vector-geometry/r8215
author: Underground Mathematics (University of Cambridge)
rights: © University of Cambridge (Underground Mathematics). Use inside SyllabAI is authorised by the
  operator attestation of 2026-10-23 — see LICENSE-DATA.md (Amendment 2026-10-23) in this repository.
  Takedown / correction handling as stated in LICENSE-DATA.md.
tags:
- underground-mathematics
- vector-geometry
- type/review-question
resource_identity:
  ugm_id: r8215
  station: vector-geometry
  station_title: Vector Geometry
  resource_type_id: 10
  resource_type_label: Review question
  level: null
  ref: 8215
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
      evidence: 'Two-part position-vector exercise: (i) ''What is the position vector of D if ABCD is
        a parallelogram?'' — the parallelogram law AB = DC rearranged for the fourth vertex; (ii) collinearity
        with a parameter (''The position vectors of points ... are collinear'', ''collinear if and only
        if'') — addition/subtraction geometry (3.7.2) and position-vector collinearity reasoning (3.7.3)
        in one exam-register question. PICK 3.7.2: the purest parallelogram-law exercise in the corpus.'
      rationale: 'Canonical UGM title: What is the position vector of $D$ if $ABCD$ is a parallelogram?'
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
      evidence: 'Two-part position-vector exercise: (i) ''What is the position vector of D if ABCD is
        a parallelogram?'' — the parallelogram law AB = DC rearranged for the fourth vertex; (ii) collinearity
        with a parameter (''The position vectors of points ... are collinear'', ''collinear if and only
        if'') — addition/subtraction geometry (3.7.2) and position-vector collinearity reasoning (3.7.3)
        in one exam-register question. PICK 3.7.2: the purest parallelogram-law exercise in the corpus.'
      rationale: 'Canonical UGM title: What is the position vector of $D$ if $ABCD$ is a parallelogram?'
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

# What is the position vector of $D$ if $ABCD$ is a parallelogram?

## Question

The position vectors of points

\(A\)

,

\(B\)

and

\(C\)

are

\[\begin{equation*} \mathbf{a} = 4\mathbf{i} - 9\mathbf{j} - \mathbf{k}, \quad \mathbf{b} = \mathbf{i} + 3\mathbf{j} + 5\mathbf{k}, \quad\text{and}\quad \mathbf{c} = p\mathbf{i} - \mathbf{j} + 3\mathbf{k}. \end{equation*}\]

1. Find the unit vector parallel to the vector \(\mathbf{AB}\).

---

1. Find the value of \(p\) such that \(A\), \(B\) and \(C\) are collinear.

---

1. If \(p = -2\), find the position vector of \(D\) so that \(ABCD\) is a parallelogram.

## Solution

The vector \(\overrightarrow{AB}\) begins at \(A\) and ends at \(B\). We have the following diagram.

From the diagram, we have that

\(\mathbf{a} + \overrightarrow{AB} = \mathbf{b}\)

, i.e. that

\[\begin{equation*} \overrightarrow{AB} = \mathbf{b} - \mathbf{a} = (\mathbf{i} + 3\mathbf{j} + 5\mathbf{k}) - (4\mathbf{i} - 9\mathbf{j} - \mathbf{k}) = -3 \mathbf{i} + 12 \mathbf{j} + 6 \mathbf{k}. \end{equation*}\]

The length of this vector is

\[\begin{equation*} \sqrt{(-3)^2 + 12^2 + 6^2} = \sqrt{9 + 144 + 36} = \sqrt{189} = 3\sqrt{21}, \end{equation*}\]

and therefore the unit vector parallel to

\(\overrightarrow{AB}\)

is

\[\begin{align*} &\frac{-3}{3\sqrt{21}} \mathbf{i} + \frac{12}{3\sqrt{21}} \mathbf{j} + \frac{6}{3\sqrt{21}} \mathbf{k} \\ =&\frac{-1}{\sqrt{21}} \mathbf{i} + \frac{4}{\sqrt{21}} \mathbf{j} + \frac{2}{\sqrt{21}} \mathbf{k}. \end{align*}\]

The points \(A, B\) and \(C\) are collinear \(\iff \overrightarrow{AB}\) is parallel to \(\overrightarrow{AC} \iff \overrightarrow{AB} = k\overrightarrow{AC}\) for some constant \(k\).

Now

\[\overrightarrow{AB} = -3 \mathbf{i} + 12 \mathbf{j} + 6 \mathbf{k},\quad \overrightarrow{AC} = (p-4) \mathbf{i} + 8 \mathbf{j} + 4 \mathbf{k},\]

and thus

\[2\overrightarrow{AB} = -6 \mathbf{i} + 24 \mathbf{j} + 12 \mathbf{k},\quad 3\overrightarrow{AC} = 3(p-4) \mathbf{i} + 24 \mathbf{j} + 12 \mathbf{k}.\]

Comparing coefficients, we can say that \(A, B\) and \(C\) are collinear if and only if \(-6 = 3(p-4)\), which is true if and only if \(p = 2\).

Alternatively, we could you use the fact that \(C\) lies on the straight line \(AB\). We could find the equation of the line \(AB\) and then substitute \(C\) into this equation to find \(p\).

We have the following sketch.

The position vector of

\(D\)

is therefore

\[\begin{align*} \mathbf{d} = \mathbf{a} + \overrightarrow{AD} = \mathbf{a} + \overrightarrow{BC}&= \mathbf{a} + \mathbf{c} - \mathbf{b} \\ &= \left( 4\mathbf{i} - 9\mathbf{j} - \mathbf{k} \right) + \left( -2\mathbf{i} - \mathbf{j} + 3\mathbf{k} \right) - \left( \mathbf{i} + 3\mathbf{j} + 5\mathbf{k} \right) \\ &= (4 - 2 - 1) \mathbf{i} + (-9 - 1 - 3) \mathbf{j} + (-1 + 3 - 5) \mathbf{k} \\ &= \mathbf{i} - 13 \mathbf{j} - 3 \mathbf{k}. \end{align*}\]

Check: does

\(\overrightarrow{DC} = \overrightarrow{AB}\)

? We have that

\[\begin{align*} \overrightarrow{AB} &= \mathbf{b} - \mathbf{a} \\ &= \left( \mathbf{i} + 3\mathbf{j} + 5\mathbf{k} \right) - \left( 4\mathbf{i} - 9\mathbf{j} - \mathbf{k} \right) \\ &= -3 \mathbf{i} + 12 \mathbf{j} + 6 \mathbf{k}, \end{align*}\]

and that

\[\begin{align*} \overrightarrow{DC} &= \mathbf{c} - \mathbf{d} \\ &= \left( -2\mathbf{i} - \mathbf{j} + 3\mathbf{k} \right) - \left( \mathbf{i} - 13 \mathbf{j} - 3 \mathbf{k} \right) \\ &= -3 \mathbf{i} + 12 \mathbf{j} + 6 \mathbf{k}. \end{align*}\]
