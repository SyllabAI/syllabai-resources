---
created: 2026-10-26T04:13:07 (UTC +06:00)
source: https://undergroundmathematics.org/vector-geometry/hit-the-spot
author: Underground Mathematics (University of Cambridge)
rights: © University of Cambridge (Underground Mathematics). Use inside SyllabAI is authorised by the
  operator attestation of 2026-10-23 — see LICENSE-DATA.md (Amendment 2026-10-23) in this repository.
  Takedown / correction handling as stated in LICENSE-DATA.md.
tags:
- underground-mathematics
- vector-geometry
- type/building-blocks
resource_identity:
  ugm_id: hit-the-spot
  station: vector-geometry
  station_title: Vector Geometry
  resource_type_id: 1
  resource_type_label: Building blocks
  level: Introducing
  ref: 5796
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
  - code: 3.7.1
    provenance:
      tier: AI_SUGGESTED
      confidence: medium
      model_version: GLM (Super Z agent, z.ai) — P3c lane-15 cross-map (cross-map-p3-vectors.json (P3c
        lane 15) @ syllabai-experimental 16c5f80)
      evidence: 'The task has students ''select vectors from a list so that the sum of the vectors gets
        you from the start to the target'', converting between representations (''has magnitude'' cards,
        direction phrases, component form) — 3.7.1''s standard-notation work at card level; the follow-ups
        ask what shape the two equal-sum routes form (the parallelogram law of addition) and whether multiples
        (including negatives) also reach the target — scalar multiplication and its geometrical interpretation,
        3.7.2. Medium: the register is informal (descriptions and diagrams) rather than i-j-k formalism.'
      rationale: 'Canonical UGM title: Hit the spot'
      validation_status: SUGGESTED
    title: use standard notations for vectors, i.e. f p , x i + y j , f p y , x i + y j + z k , AB , a
  - code: 3.7.2
    provenance:
      tier: AI_SUGGESTED
      confidence: medium
      model_version: GLM (Super Z agent, z.ai) — P3c lane-15 cross-map (cross-map-p3-vectors.json (P3c
        lane 15) @ syllabai-experimental 16c5f80)
      evidence: 'The task has students ''select vectors from a list so that the sum of the vectors gets
        you from the start to the target'', converting between representations (''has magnitude'' cards,
        direction phrases, component form) — 3.7.1''s standard-notation work at card level; the follow-ups
        ask what shape the two equal-sum routes form (the parallelogram law of addition) and whether multiples
        (including negatives) also reach the target — scalar multiplication and its geometrical interpretation,
        3.7.2. Medium: the register is informal (descriptions and diagrams) rather than i-j-k formalism.'
      rationale: 'Canonical UGM title: Hit the spot'
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

# Hit the spot

> Excerpt: Students select vectors from a list so that the sum of the vectors gets you from the start to the target. They will convert between different representations of vectors
and practise adding vectors in two dimensions.

## Problem

Here are some vectors:

- \(\mathbf{a}=\begin{pmatrix}6\\1\end{pmatrix}\)

- \(\mathbf{b}\) has magnitude \(2\sqrt{2}\) and direction \(45^\circ\) anti-clockwise from the \(x\)-axis

- \(\mathbf{c}\) has magnitude \(4\) in the positive \(x\) direction

- \(\mathbf{d}=3\mathbf{i}-\mathbf{j}\)

- \(\mathbf{e}=7\mathbf{i}-3\mathbf{j}\)

- \(\mathbf{f}\) is \(2\) units in the negative \(x\) direction and \(3\) units in the positive \(y\) direction

- \(\mathbf{g}=\begin{pmatrix}-2\\4\end{pmatrix}\)

Select a starting point, \(M(2,5)\) or \(N(3,1)\), and two of the vectors from the list so that the [sum of the vectors](https://undergroundmathematics.org/glossary/vector-addition) will get you from your start to the target, \(T(7,6)\).

How many different ways can you pair up vectors from the list to get to the target?

Can you add *three* of the vectors to get from one of the starts to the target?

## Interactive diagram

Select a starting point, \(M(2,5)\) or \(N(3,1)\), and two of the vectors \(\mathbf{a}\) to \(\mathbf{g}\) so that the [sum of the vectors](https://undergroundmathematics.org/glossary/vector-addition) will get you from your start to the target, \(T(7,6)\).

> [interactive embed (geogebra-iframe): //www.geogebratube.org/material/iframe/id/Z3QkV9Wd/width/600/height/500/border/888888/rc/false/ai/false/sdz/false/smb/false/stb/false/stbh/false/ld/false/sri/true/asb/false/at/html5] — not part of the text import; see the source page.

[Download GeoGebra file](https://www.geogebratube.org/material/download/format/file/id/Z3QkV9Wd)

How many different ways can you pair up the vectors to get to the target?

Can you add *three* of the vectors to get from one of the starts to the target?

## Solution

First, let’s write all of the vectors in the same format. We’ve chosen to use column vectors.

\[\mathbf{a}=\begin{pmatrix}6\\1\end{pmatrix},\: \mathbf{b}=\begin{pmatrix}2\\2\end{pmatrix},\: \mathbf{c}=\begin{pmatrix}4\\0\end{pmatrix},\: \mathbf{d}=\begin{pmatrix}3\\-1\end{pmatrix},\: \mathbf{e}=\begin{pmatrix}7\\-3\end{pmatrix},\: \mathbf{f}=\begin{pmatrix}-2\\3\end{pmatrix},\: \mathbf{g}=\begin{pmatrix}-2\\4\end{pmatrix}\]

The vector from \(M\) to \(T\) is \(\overrightarrow{MT}=\begin{pmatrix}5\\1\end{pmatrix}\) and we can make this by adding, \[\mathbf{b}+\mathbf{d}=\begin{pmatrix}2+3\\2-1\end{pmatrix}=\begin{pmatrix}5\\1\end{pmatrix}.\]

Notice that we can add these two vectors the other way round, \(\mathbf{d}+\mathbf{b}\), with the same result. If we draw these two “routes” they look like this.

You can decide whether these two are different solutions or the same solution!

What shape have we constructed? Can you prove it?

We can also make \(\overrightarrow{MT}\) by adding \(\mathbf{e}\) and \(\mathbf{g}\), and we can make \(\overrightarrow{NT}\) by adding \(\mathbf{a}\) and \(\mathbf{g}\).

In all, we have three different pairs of vectors which will get us to the target, \(T\), and each pair can be combined in either of two orders.

You might also have noticed that starting at \(M\), if we apply \(\mathbf{c}\) first then \(\mathbf{b}\) it takes us through \(T\) but overshoots. So can you write \(\overrightarrow{MT}\) as a combination of *multiples* of \(\mathbf{c}\) and \(\mathbf{b}\)?

If we allow multiples (including negatives), is it also possible to write \(\overrightarrow{NT}\) as a combination of \(\mathbf{c}\) and \(\mathbf{b}\)? Which other points can you reach by adding multiples of \(\mathbf{c}\) and \(\mathbf{b}\)?

\[\overrightarrow{NT}=\mathbf{b}+\mathbf{c}+\mathbf{f}\]

In how many different orders could we arrange these three vectors?
