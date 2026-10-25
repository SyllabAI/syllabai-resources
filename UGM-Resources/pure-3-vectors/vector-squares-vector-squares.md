---
created: 2026-10-26T04:13:07 (UTC +06:00)
source: https://undergroundmathematics.org/vector-geometry/vector-squares
author: Underground Mathematics (University of Cambridge)
rights: © University of Cambridge (Underground Mathematics). Use inside SyllabAI is authorised by the
  operator attestation of 2026-10-23 — see LICENSE-DATA.md (Amendment 2026-10-23) in this repository.
  Takedown / correction handling as stated in LICENSE-DATA.md.
tags:
- underground-mathematics
- vector-geometry
- type/fluency-exercise
resource_identity:
  ugm_id: vector-squares
  station: vector-geometry
  station_title: Vector Geometry
  resource_type_id: 8
  resource_type_label: Fluency exercise
  level: Introducing
  ref: 8672
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
      confidence: medium
      model_version: GLM (Super Z agent, z.ai) — P3c lane-15 cross-map (cross-map-p3-vectors.json (P3c
        lane 15) @ syllabai-experimental 16c5f80)
      evidence: 'A square is enclosed by four lines given by vector equations; students find vertices
        as intersections of line pairs (''the point that is common to equations (1) and (4)'') and prove
        adjacent edges perpendicular from direction vectors — 3.7.4''s vector line form plus 3.7.5''s
        intersection work in a 2D geometry package. Medium: the perpendicularity argument is diagrammatic
        rather than scalar-product formal.'
      rationale: 'Canonical UGM title: Vector squares'
      validation_status: SUGGESTED
    title: understand the significance of all the symbols e.g. finding the equation of a line given the
      position used when the equation of a straight line is vector of a point on the line and a direction
      vector, or expressed in the form r = a + t b , and find the the position vectors of two points on
      the line. equation of a line, given sufficient information
  - code: 3.7.5
    provenance:
      tier: AI_SUGGESTED
      confidence: medium
      model_version: GLM (Super Z agent, z.ai) — P3c lane-15 cross-map (cross-map-p3-vectors.json (P3c
        lane 15) @ syllabai-experimental 16c5f80)
      evidence: 'A square is enclosed by four lines given by vector equations; students find vertices
        as intersections of line pairs (''the point that is common to equations (1) and (4)'') and prove
        adjacent edges perpendicular from direction vectors — 3.7.4''s vector line form plus 3.7.5''s
        intersection work in a 2D geometry package. Medium: the perpendicularity argument is diagrammatic
        rather than scalar-product formal.'
      rationale: 'Canonical UGM title: Vector squares'
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

# Vector squares

> Excerpt: Can you find the area of a square enclosed by four lines, given by their vector equations?

## Problem

A square is enclosed by the lines:

1. \(\mathbf{r}=\begin{pmatrix}0\\2\end{pmatrix} + a\begin{pmatrix}1\\1\end{pmatrix}\)

1. \(\mathbf{r}=\begin{pmatrix}0\\6\end{pmatrix} + b\begin{pmatrix}-1\\1\end{pmatrix}\)

1. \(\mathbf{r}=\begin{pmatrix}2\\1\end{pmatrix} + c\begin{pmatrix}2\\2\end{pmatrix}\)

1. \(\mathbf{r}=\begin{pmatrix}1\\2\end{pmatrix} + d\begin{pmatrix}1\\-1\end{pmatrix}\)

- Can you convince yourself that the adjacent edges are perpendicular?

- Find the area of the square.

- Find a vector equation for each of the two diagonals.

## Suggestion

A square is enclosed by the lines:

1. \(\mathbf{r}=\begin{pmatrix}0\\2\end{pmatrix} + a\begin{pmatrix}1\\1\end{pmatrix}\)

1. \(\mathbf{r}=\begin{pmatrix}0\\6\end{pmatrix} + b\begin{pmatrix}-1\\1\end{pmatrix}\)

1. \(\mathbf{r}=\begin{pmatrix}2\\1\end{pmatrix} + c\begin{pmatrix}2\\2\end{pmatrix}\)

1. \(\mathbf{r}=\begin{pmatrix}1\\2\end{pmatrix} + d\begin{pmatrix}1\\-1\end{pmatrix}\)

Find the area of the square.

- Which line is which?

- What are the positions of the vertices of the square?

- Could you have predicted that the enclosed square would lie entirely within the first quadrant?

## Solution

We need to consider the direction vector of each line. Lines (1) and (2) do not have the same direction vector and so they will cross at some point. If we now think about the behaviour of each line as it moves away from the crossing point we can show that they are perpendicular using the diagram below.

Can you use a similar argument to convince yourself about the other adjacent edges of the square?

To do this we need to identify the positions of some of the vertices. We could aim to find the length of one side by finding two adjacent vertices, or we could find the length of the diagonal by identifying vertices opposite each other. It doesn’t matter which pair we choose to find so let’s say we look for vertices A and B shown on the diagram below.

To find the position of point A, we need to find the point that is common to equations (1) and (4), (they need to have the same position vector \(\mathbf{r}\)). With that in mind, we can write down that \(a=1+d\) and \(2+a=2-d\). Solving these equations simultaneously we find that \(a=\frac{1}{2}\) and \(d=-\frac{1}{2}\).

Substituting these values into either equation (1) or equation (4) we find the position vector of point A to be \(\mathbf{r}=\begin{pmatrix}\frac{1}{2}\\\frac{5}{2}\end{pmatrix}\).

Repeating the process to find the position of point B, from equations (1) and (2) we can write down that \(a=-b\) and \(2 + a = 6 + b\). Solving these equations simultaneously we find that \(a=2\) and \(b=-2\).

Substituting these values into either equation (1) or equation (2) we find the position vector of point B to be \(\mathbf{r}=\begin{pmatrix}2\\4\end{pmatrix}\).

We might have found the position of vertex B in another way. The line represented by vector equation (1) could have been constructed by starting at the position vector \(\begin{pmatrix}0\\2\end{pmatrix}\) and ‘stepping out’ the direction vector as shown below. If the same process was then repeated to construct the line represented by vector equation (2) then we notice that the two lines intersect at point B with position vector \(\begin{pmatrix}2\\4\end{pmatrix}\).

If the process is repeated to construct the lines represented by vector equations (3) and (4) then we notice that this pair intersect at \(\begin{pmatrix}2\\1\end{pmatrix}\), forming the vertex opposite B in the enclosed square. These two vertices are aligned vertically and the line joining them forms the diagonal, length 3, of the enclosed square.

Now that we have the position vectors of vertices A and B we could find the length of the line AB using Pythagoras.

However, you might notice that the area of the square will be given by \(AB^2\) and we can write this down directly, \[AB^2 = 2 \times \left(\frac{3}{2}\right)^2 = \frac{9}{2}.\]

You could also have noticed that the right-angled triangle joining points A and B is isosceles. This tells us that the square could be divided up into four of these triangles.

We can now show that the area of the square is again equal to \[4 \times \frac{1}{2}\left(\frac{3}{2}\right)^2 = \frac{9}{2}.\]

What can we now say about the positions of the other vertices and the diagonals of the square?

In order to write down a vector equation of a line we need to know the position of a point on that line and a direction vector. For the vertical diagonal of the square we know that point B, with position vector \(\begin{pmatrix}2\\4\end{pmatrix}\) lies on the line and that the direction vector is \(\begin{pmatrix}0\\1\end{pmatrix}\).

A vector equation of the vertical diagonal of the square is therefore \[\mathbf{r}=\begin{pmatrix}2\\4\end{pmatrix} + p\begin{pmatrix}0\\1\end{pmatrix}.\]

We could also have written \[\mathbf{r}=\begin{pmatrix}2\\1\end{pmatrix} + p\begin{pmatrix}0\\1\end{pmatrix},\] or any vector equation of the form \[\mathbf{r}=\begin{pmatrix}2\\s\end{pmatrix} + p\begin{pmatrix}0\\q\end{pmatrix}\] for any non-zero \(q\).

The horizontal diagonal could be written as any vector equation of the form \[\mathbf{r}=\begin{pmatrix}s\\\frac{5}{2}\end{pmatrix} + p\begin{pmatrix}q\\0\end{pmatrix}\] for any non-zero \(q\).

## Taking it further

Three of the four lines enclosing a square are given by the following equations.

1. \(\mathbf{r}=\begin{pmatrix}0\\2\end{pmatrix} + a\begin{pmatrix}1\\3\end{pmatrix}\)

1. \(\mathbf{r}=\begin{pmatrix}5\\1\end{pmatrix} + b\begin{pmatrix}-3\\1\end{pmatrix}\)

1. \(\mathbf{r}=\begin{pmatrix}3\\3\end{pmatrix} + c\begin{pmatrix}3\\-1\end{pmatrix}\)

Find the fourth equation and the area of the square.
