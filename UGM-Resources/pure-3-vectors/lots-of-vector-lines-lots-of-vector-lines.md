---
created: 2026-10-26T04:13:07 (UTC +06:00)
source: https://undergroundmathematics.org/vector-geometry/lots-of-vector-lines
author: Underground Mathematics (University of Cambridge)
rights: © University of Cambridge (Underground Mathematics). Use inside SyllabAI is authorised by the
  operator attestation of 2026-10-23 — see LICENSE-DATA.md (Amendment 2026-10-23) in this repository.
  Takedown / correction handling as stated in LICENSE-DATA.md.
tags:
- underground-mathematics
- vector-geometry
- type/fluency-exercise
resource_identity:
  ugm_id: lots-of-vector-lines
  station: vector-geometry
  station_title: Vector Geometry
  resource_type_id: 8
  resource_type_label: Fluency exercise
  level: Developing
  ref: 7131
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
  - code: 3.7.4
    provenance:
      tier: AI_SUGGESTED
      confidence: high
      model_version: GLM (Super Z agent, z.ai) — P3c lane-15 cross-map (cross-map-p3-vectors.json (P3c
        lane 15) @ syllabai-experimental 16c5f80)
      evidence: 'Twelve lines given ONLY as r = a + mu*b column-vector equations, to be paired by shared
        properties (''These lines are parallel. These lines are perpendicular. These lines have the same
        y-intercept...'') — the equation of a straight line in vector form r = a + t b (3.7.4) is the
        raw material, and the pairing includes parallel/perpendicular determination from direction vectors
        (3.7.5); the teacher notes ask ''Are there any pairs we can match up by just looking at the equations?''
        — reading direction and position vectors off the vector form. PICK 3.7.4: the purest vector-line-equation
        material in the corpus.'
      rationale: 'Canonical UGM title: Lots of vector lines!'
      validation_status: SUGGESTED
    title: understand the significance of all the symbols e.g. finding the equation of a line given the
      position used when the equation of a straight line is vector of a point on the line and a direction
      vector, or expressed in the form r = a + t b , and find the the position vectors of two points on
      the line. equation of a line, given sufficient information
  - code: 3.7.5
    provenance:
      tier: AI_SUGGESTED
      confidence: high
      model_version: GLM (Super Z agent, z.ai) — P3c lane-15 cross-map (cross-map-p3-vectors.json (P3c
        lane 15) @ syllabai-experimental 16c5f80)
      evidence: 'Twelve lines given ONLY as r = a + mu*b column-vector equations, to be paired by shared
        properties (''These lines are parallel. These lines are perpendicular. These lines have the same
        y-intercept...'') — the equation of a straight line in vector form r = a + t b (3.7.4) is the
        raw material, and the pairing includes parallel/perpendicular determination from direction vectors
        (3.7.5); the teacher notes ask ''Are there any pairs we can match up by just looking at the equations?''
        — reading direction and position vectors off the vector form. PICK 3.7.4: the purest vector-line-equation
        material in the corpus.'
      rationale: 'Canonical UGM title: Lots of vector lines!'
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

# Lots of vector lines!

> Excerpt: Students pair up equations of lines based on shared properties such as being parallel, perpendicular, sharing a $y$-intercept, etc.

## Problem

Here are the equations of 12 straight lines.

\(\mathbf{r}= \begin{pmatrix} 0 \\ -6 \\ \end{pmatrix} + \mu \begin{pmatrix} -1 \\ 4 \end{pmatrix}\)

\(\mathbf{r}= \begin{pmatrix} 0 \\ -3 \\ \end{pmatrix} + \mu \begin{pmatrix} 1 \\ 8 \end{pmatrix}\)

\(\mathbf{r}= \begin{pmatrix} 2 \\ 9.5 \\ \end{pmatrix} + \mu \begin{pmatrix} -2 \\ -8 \end{pmatrix}\)

\(\mathbf{r}= \begin{pmatrix} 0 \\ 2 \\ \end{pmatrix} + \mu \begin{pmatrix} -2 \\ 1 \end{pmatrix}\)

\(\mathbf{r}= \begin{pmatrix} 1 \\ 1 \\ \end{pmatrix} + \mu \begin{pmatrix} 4 \\ 1 \end{pmatrix}\)

\(\mathbf{r}= \begin{pmatrix} 0 \\ 4 \\ \end{pmatrix} + \mu \begin{pmatrix} 1 \\ 4 \end{pmatrix}\)

\(\mathbf{r}= \begin{pmatrix} 0 \\ -4 \\ \end{pmatrix} + \mu \begin{pmatrix} 4 \\ 6 \end{pmatrix}\)

\(\mathbf{r}= \begin{pmatrix} 0 \\ 6 \\ \end{pmatrix} + \mu \begin{pmatrix} -2 \\ 10 \end{pmatrix}\)

\(\mathbf{r}= \begin{pmatrix} -4 \\ 2 \\ \end{pmatrix} + \mu \begin{pmatrix} 5 \\ -1 \end{pmatrix}\)

\(\mathbf{r}= \begin{pmatrix} 0 \\ -4 \\ \end{pmatrix} + \mu \begin{pmatrix} 1 \\ 6 \end{pmatrix}\)

\(\mathbf{r}= \begin{pmatrix} 0 \\ 11 \\ \end{pmatrix} + \mu \begin{pmatrix} 1 \\ -6 \end{pmatrix}\)

\(\mathbf{r}= \begin{pmatrix} 1 \\ -2 \\ \end{pmatrix} + \mu \begin{pmatrix} 3 \\ 2 \end{pmatrix}\)

These 12 straight lines can be divided up into six pairs, each pair matching one of the following descriptions:

- These lines are parallel.

- These lines are perpendicular.

- These lines have the same \(y\)-intercept.

- These lines have the same \(x\)-intercept.

- These lines both go through the point \((1, 5)\).

- These lines …

Can you sort them into the correct pairs and complete the final description?

## Solution

While sketching the lines could be helpful, 12 might be too many on one graph. Are there any pairs we can match up by just looking at the equations?

\(\mathbf{r}= \begin{pmatrix} 0 \\ -4 \\ \end{pmatrix} + \mu \begin{pmatrix} 4 \\ 6 \end{pmatrix}\)

\(\mathbf{r}= \begin{pmatrix} 0 \\ -4 \\ \end{pmatrix} + \mu \begin{pmatrix} 1 \\ 6 \end{pmatrix}\)

Equations 7 and 10 have the same position vector which also happens to be their \(y\)-interept.

Do you think there are particular features of lines that are easier to spot when the equation is written in vector form compared to Cartesian form?

\(\mathbf{r}= \begin{pmatrix} 2 \\ 9.5 \\ \end{pmatrix} + \mu \begin{pmatrix} -2 \\ -8 \end{pmatrix}\)

\(\mathbf{r}= \begin{pmatrix} 0 \\ 4 \\ \end{pmatrix} + \mu \begin{pmatrix} 1 \\ 4 \end{pmatrix}\)

Equations 3 and 6 are parallel lines, but it looks like they have different direction vectors.

How do you know these lines are parallel? What is the same about the two direction vectors?

\(\mathbf{r}= \begin{pmatrix} 0 \\ -6 \\ \end{pmatrix} + \mu \begin{pmatrix} -1 \\ 4 \end{pmatrix}\)

\(\mathbf{r}= \begin{pmatrix} 1 \\ 1 \\ \end{pmatrix} + \mu \begin{pmatrix} 4 \\ 1 \end{pmatrix}\)

Equations 1 and 5 are perpendicular lines.

Can you use a diagram to convince yourself that the two are perpendicular?

Can you find a different direction vector for equation 1 that would still make it perpendicular to equation 5?

Now we’ve paired up 6 equations, a sketch of the remaining 6 will be easier to work with.

Depending on how accurate our sketch is, we may be able to write down some of the pairs straight away, or we might need to check the intersection points. For example, it looks like equations 4 and 12 share the same \(x\)-intercept.

\(\mathbf{r}= \begin{pmatrix} 0 \\ 2 \\ \end{pmatrix} + \mu \begin{pmatrix} -2 \\ 1 \end{pmatrix}\)

\(\mathbf{r}= \begin{pmatrix} 1 \\ -2 \\ \end{pmatrix} + \mu \begin{pmatrix} 3 \\ 2 \end{pmatrix}\)

We could check by finding the value of \(\mu\) for each equation that gives \(y = 0\), or we could solve the equations simultaneously.

Writing them as simultaneous equations gives us \(-2\mu = 1+3\lambda\) and \(2+\mu = -2+2\lambda\), which solve to give \(\mu = -2\) and \(\lambda=1\). Substituting either of these values into their equation confirms that the two lines meet at their \(x\)-intercept of \((4,0)\).

\(\mu\) was changed into \(\lambda\) for the second equation. Why? What would happen if we used the same variable for both equations?

From the graph it looks like equation 2 and 11 meet at the point

\((1, 5).\)

\(\mathbf{r}= \begin{pmatrix} 0 \\ -3 \\ \end{pmatrix} + \mu \begin{pmatrix} 1 \\ 8 \end{pmatrix}\)

\(\mathbf{r}= \begin{pmatrix} 0 \\ 11 \\ \end{pmatrix} + \mu \begin{pmatrix} 1 \\ -6 \end{pmatrix}\)

We could solve the equations for their intersection points, or we could notice that setting \(\mu = 1\) for both equations gives an \(x\)-coordinate of \(1\). Does it give the correct \(y\)-coordinate for both lines?

\(\mathbf{r}= \begin{pmatrix} 0 \\ 6 \\ \end{pmatrix} + \mu \begin{pmatrix} -2 \\ 10 \end{pmatrix}\)

\(\mathbf{r}= \begin{pmatrix} -4 \\ 2 \\ \end{pmatrix} + \mu \begin{pmatrix} 5 \\ -1 \end{pmatrix}\)

What do the final two lines have in common?

Possible descriptions

These lines…

- both have negative gradients.

- intersect at the point \((1, 1)\).

- are a reflection of each other in the line \(y = x\).

- create an acute angle of \(67.4^{\circ}\) at their intersection.

**Taking it further**

Can you come up with the equation of a line that would match with 2 different pairs at the same time?

If the lines were given in three dimensions would you still be able to match up pairs with the same properties? Which properties might be the most challenging to match; parallel, perpendicular, shared \(x\)-intercepts, shared \(y\)-intercepts or a point of intersection?
