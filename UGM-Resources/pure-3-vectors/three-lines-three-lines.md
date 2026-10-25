---
created: 2026-10-26T04:13:07 (UTC +06:00)
source: https://undergroundmathematics.org/vector-geometry/three-lines
author: Underground Mathematics (University of Cambridge)
rights: © University of Cambridge (Underground Mathematics). Use inside SyllabAI is authorised by the
  operator attestation of 2026-10-23 — see LICENSE-DATA.md (Amendment 2026-10-23) in this repository.
  Takedown / correction handling as stated in LICENSE-DATA.md.
tags:
- underground-mathematics
- vector-geometry
- type/building-blocks
resource_identity:
  ugm_id: three-lines
  station: vector-geometry
  station_title: Vector Geometry
  resource_type_id: 1
  resource_type_label: Building blocks
  level: Developing
  ref: 9776
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
      evidence: 'Three lines in 3D given as vector equations a = (4,0,-2) + alpha(-1,1,4) etc.; students
        predict parallel/perpendicular/intersecting relationships then verify: ''If any two of the lines
        were parallel, their direction vectors would be the same or related by a scalar multiple''; intersections
        via ''three equations and two unknowns. If there is a unique solution, then the two lines intersect.
        If there is no solution they do not'' — the skew/intersection determination of 3.7.5 over the
        r = a + t b form of 3.7.4, with the dot product named for the perpendicularity check. PICK 3.7.5:
        the corpus''s only genuine 3D parallel/skew/intersection Determination exercise.'
      rationale: 'Canonical UGM title: Three lines'
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
      evidence: 'Three lines in 3D given as vector equations a = (4,0,-2) + alpha(-1,1,4) etc.; students
        predict parallel/perpendicular/intersecting relationships then verify: ''If any two of the lines
        were parallel, their direction vectors would be the same or related by a scalar multiple''; intersections
        via ''three equations and two unknowns. If there is a unique solution, then the two lines intersect.
        If there is no solution they do not'' — the skew/intersection determination of 3.7.5 over the
        r = a + t b form of 3.7.4, with the dot product named for the perpendicularity check. PICK 3.7.5:
        the corpus''s only genuine 3D parallel/skew/intersection Determination exercise.'
      rationale: 'Canonical UGM title: Three lines'
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

# Three lines

> Excerpt: Students are given vector equations of three lines in 3D, and are asked to discover the geometric pattern they form.

## Problem

Here are vector equations of three lines.

\(\mathbf{a}=\begin{pmatrix}4\\0\\-2\end{pmatrix}+\alpha\begin{pmatrix}-1\\1\\4\end{pmatrix}\)

\(\mathbf{b}=\begin{pmatrix}1\\3\\10\end{pmatrix}+\beta\begin{pmatrix}-2\\-1\\2\end{pmatrix}\)

\(\mathbf{c}=\begin{pmatrix}2\\-1\\0\end{pmatrix}+\gamma\begin{pmatrix}1\\2\\2\end{pmatrix}\)

Before doing any calculations,

- try to visualise the lines in 3D space. What can you say about them?

- do you think any of them might be parallel or perpendicular?

- might they intersect?

Now check your predictions and work out what geometrical shape or pattern the lines make.

## Interactive diagram

This applet shows the three lines described in the question.

Press and slide to change the direction of view. Click the buttons at the left to make the other lines and points visible.

> [interactive embed (geogebra-iframe): //www.geogebratube.org/material/iframe/id/eUAH8M2V/width/780/height/600/border/888888/rc/false/ai/false/sdz/true/smb/false/stb/false/stbh/false/ld/false/sri/true/asb/false/at/html5] — not part of the text import; see the source page.

[Download GeoGebra file](https://www.geogebratube.org/material/download/format/file/id/eUAH8M2V)

## Solution

Here are the vector equations of three lines.

\(\mathbf{a}=\begin{pmatrix}4\\0\\-2\end{pmatrix}+\alpha\begin{pmatrix}-1\\1\\4\end{pmatrix}\)

\(\mathbf{b}=\begin{pmatrix}1\\3\\10\end{pmatrix}+\beta\begin{pmatrix}-2\\-1\\2\end{pmatrix}\)

\(\mathbf{c}=\begin{pmatrix}2\\-1\\0\end{pmatrix}+\gamma\begin{pmatrix}1\\2\\2\end{pmatrix}\)

Before doing any calculations,

- try to visualise the lines in 3D space. What can you say about them?

- do you think any of them might be parallel or perpendicular?

- might they intersect?

If any two of the lines were parallel, their direction vectors would be the same or related by a scalar multiple. The distribution of positive and negative components is enough to see that this isn’t going to be the case.

Spotting perpendiculars and intersections is tricky without calculation but you may have been able to predict by visualising the lines.

If you have learnt about the [dot product](https://undergroundmathematics.org/glossary/dot-product) then you can check for perpendicular vectors with a straightforward calculation, but intersections require the solution of simultaneous equations as we shall see below.

In 2D, a pair of lines always have an intersection unless they are parallel. Is this true in 3D?

Let’s start by looking for an intersection between lines (A) and (B). If they intersect, there will be some values of \(\alpha\) and \(\beta\) for which \(\mathbf{a}=\mathbf{b}\). In other words, \[\begin{pmatrix}4\\0\\-2\end{pmatrix}+\alpha\begin{pmatrix}-1\\1\\4\end{pmatrix}=\begin{pmatrix}1\\3\\10\end{pmatrix}+\beta\begin{pmatrix}-2\\-1\\2\end{pmatrix}\]

Equating each of the

\(x\)

,

\(y\)

and

\(z\)

components we have,

\[\begin{align} 4-\alpha &=1-2\beta \label{eq:ab-x} \\ 0+\alpha &= 3-\beta \label{eq:ab-y} \\ -2+4\alpha &= 10+2\beta \label{eq:ab-z} \end{align}\]

We have three equations and two unknowns. If there is a unique solution, then the two lines intersect. If there is no solution they do not.

Why do we have to check all three equations? What would it mean if we had a solution to \(\eqref{eq:ab-x}\) and \(\eqref{eq:ab-y}\) that did not satisfy \(\eqref{eq:ab-z}\)?

Combining \(\eqref{eq:ab-x}\) and \(\eqref{eq:ab-y}\) we get \(\beta=0\) and \(\alpha=3\). By substituting, we find that these values do satisfy \(\eqref{eq:ab-z}\) and so the two lines do intersect. The point of intersection is found by substituting \(\alpha\) into (A) or \(\beta\) into (B). It is \((1,3,10)\).

Repeating this process for the other pairs of lines we find that each pair intersects. We decided to label the points of intersection as follows.

- and (C) intersect at \(P=(3,1,2)\)

- and (B) intersect at \(Q=(1,3,10)\)

- and (C) intersect at \(R=(5,5,6)\)

These coordinates have nothing obvious in common, but thinking about the geometry we can see that if three straight lines all intersect at distinct points they must all lie in a plane. The lines form the edges of a triangle in that plane.

What kind of triangle?

Working out angles between lines in 3D is hard (unless you have learnt about the

dot product

). So instead, let’s work out the side lengths of the triangle, which we can do using

Pythagoras’ theorem

.

\[\begin{align*} \overrightarrow{PQ} &= \begin{pmatrix}1-3\\3-1\\10-2\end{pmatrix} = \begin{pmatrix}-2\\2\\8\end{pmatrix} \\ \big|PQ\big| &= \sqrt{(-2)^2+2^2+8^2} \\ &= \sqrt{72} = 6\sqrt{2} \end{align*}\]

Notice that \(\overrightarrow{PQ}\) is a scalar multiple of the direction vector in equation (A). Why must this be the case?

Similarly,

\[\begin{align*} \big|PR\big| &= \sqrt{2^2+4^2+4^2} = 6, \\ \big|QR\big| &= \sqrt{4^2+2^2+(-4)^2} = 6. \end{align*}\]

We have side lengths in the ratio \(1:1:\sqrt{2}\), so \(PQR\) is an isosceles right-angled triangle, with its right-angle at \(R\). Line (A) forms its hypotenuse.
