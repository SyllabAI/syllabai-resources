---
created: 2026-10-23T12:00:00 (UTC +06:00)
source: https://undergroundmathematics.org/combining-functions/its-a-matter-of-perspective
author: Underground Mathematics (University of Cambridge)
rights: © University of Cambridge (Underground Mathematics). Use inside SyllabAI is authorised by the
  operator attestation of 2026-10-23 — see LICENSE-DATA.md (Amendment 2026-10-23) in this repository.
  Takedown / correction handling as stated in LICENSE-DATA.md.
tags:
- underground-mathematics
- combining-functions
- type/bigger-picture
- level/developing
resource_identity:
  ugm_id: its-a-matter-of-perspective
  station: combining-functions
  station_title: Combining Functions
  resource_type_id: 12
  resource_type_label: Bigger picture
  level: Developing
  ref: 6114
  old_site_id: F2_RT3_3
spec_map:
  curriculum_code: CIE-9709-P1-2023
  lane: cie-a-level-maths-20-pure-1
  board: Cambridge CIE
  syllabus_version: 2023-2025
  subsection: combining-functions
  subsection_provenance:
    tier: PROVIDER
    signal: source-url-slug
    slug: combining-functions
    validation_status: SUGGESTED
  spec_points:
  - code: 1.2.5
    provenance:
      tier: AI_SUGGESTED
      confidence: medium
      model_version: GLM (Super Z agent, z.ai) — P3c functions cross-map (generalisation lane 2) (cross-map-functions.json
        @ syllabai-experimental 4a592ed0)
      evidence: Animated translation thinking on a parabola (GeoGebra applet; interactive recorded, not
        fetched).
      rationale: 'Canonical UGM title: “It''s a matter of perspective”'
      validation_status: SUGGESTED
    title: understand and use the transformations of the Including use of the terms 'translation', 'reflection'
      graph of y = f( x ) given by and 'stretch' in describing transformations. Questions y = f( x ) +
      a , y = f( x + a ) , may involve algebraic or trigonometric functions, or other graphs with given
      features. y = a f( x ) , y = f( ax ) and simple combinations of these.
  mapped_date: '2026-10-23'
  mapper: cross-map-functions.json (P3c) @ syllabai-experimental 4a592ed0
  coverage_note: null
provenance:
  capture_date: '2026-10-22'
  capture_tool: P2 full-site crawl (ugm-crawl) → ugm-clean extraction; text-only import
  content_language: en
task: T-UGM-IMPORT-2
assets:
- path: https://undergroundmathematics.org/combining-functions/its-a-matter-of-perspective/images/parabola-2.png
  kind: figure
interactive:
- src: //www.geogebratube.org/material/iframe/id/kgWsjQfY/width/600/height/400/border/888888/rc/false/ai/false/sdz/false/smb/false/stb/false/stbh/false/ld/false/sri/true/asb/false/at/html5
  kind: geogebra-iframe
---

# It's a matter of perspective

> Excerpt: This resource asks students to find the equation of a parabola given three points. It can be used as a follow-on from 'Name that graph again', and it introduces a wider range of transformations than those previously encountered.

## Problem

We would like to find an equation for this parabola in the form \(y=f(x)\).

> [figure: Upward facing parabola passing through the points (0,5), (2,1) and (4,13) — `https://undergroundmathematics.org/combining-functions/its-a-matter-of-perspective/images/parabola-2.png`] (image not included in the text import; path of record).

What ways come to mind straight away?

## A certain point of view

Click on the *Animate* button in the applet below or move the slider.

> [interactive embed (geogebra-iframe): //www.geogebratube.org/material/iframe/id/kgWsjQfY/width/600/height/400/border/888888/rc/false/ai/false/sdz/false/smb/false/stb/false/stbh/false/ld/false/sri/true/asb/false/at/html5] — not part of the text import; see the source page.

[Download GeoGebra file](https://www.geogebratube.org/material/download/format/file/id/kgWsjQfY)

What is happening in the animation as the value of \(u\) increases from \(0\) to \(1\)?

As \(u\) increases, the points \((0,5)\) and \((2,1)\) are moved in such a way that their \(x\)-coordinates stay the same but their \(y\)-coordinates smoothly change to \(0\). They are transformed to \((0,0)\) and \((2,0)\).

The red dashed line is drawn passing through the two points described above. This line becomes horizontal (and lies on the \(x\)-axis) when \(u=1\).

The original parabola is transformed so that it always passes through these two points. It appears to remain as a parabola.

The point \(C\) marked on the parabola remains fixed throughout.

**An answer**

Which characteristics of the parabola are being preserved and which are being changed?

The curve does remain as a parabola as \(u\) increases, so we could say that its “parabolic” shape stays the same. Its orientation remains upward facing.

However, it is transformed so that when \(u=1\) it passes through the points \((0,0)\) and \((2,0)\) rather than the points \((0,5)\) and \((2,1)\). The original parabola does not intersect the \(x\)-axis but the transformed one does.

**An answer**

How can we describe the transformation that is happening to the parabola?

Each point on the parabola is being transformed in the same way as each point on the straight line.

The equation of the original straight line can be written as \(y=5-2x\). As \(u\) increases, we are gradually subtracting from its \(y\) values until when \(u=1\) the equation of the line has become \(y=0\). At this stage, we have therefore subtracted \((5-2x)\) from the \(y\) value of each point on the line.

This type of transformation is called a [shear](https://undergroundmathematics.org/glossary/shear); in this case, it is a shear parallel to the \(y\)-axis. A shear is a particular example of an [affine transformation](https://undergroundmathematics.org/glossary/affine-transformation).

 Similarly, if we write the equation of the original parabola as

\(y=f(x)\)

 and subtract

\((5-2x)\)

 when

\(u=1\)

, we can say that the transformed parabola has equation

\[\begin{equation} y=f(x)-(5-2x).\label{eq1} \end{equation}\]

**An answer**

What can we say about the transformed parabola?

where \(K\) is some constant.

 We can see that the transformed parabola intersects the

\(x\)

-axis at

\(x=0\)

 and

\(x=2\)

, so its equation can be written as

\[\begin{equation} y=Kx(x-2),\label{eq2} \end{equation}\]

**An answer**

Can we use the transformed parabola to find the equation of the original parabola, \(y=f(x)\)?

We saw above \(\eqref{eq1}\) that the transformed parabola has equation \(y=f(x)-(5-2x)\), and also \(\eqref{eq2}\) that it can be written as \(y=Kx(x-2)\). Therefore \[f(x)-(5-2x)=Kx(x-2),\] and we can rearrange this to get \[f(x)=5-2x+Kx(x-2).\]

and the equation of the original parabola is \[y = 2x^2-6x+5.\]

 We can find the value of

\(K\)

 by using the third given point on the original parabola

\((4,13)\)

:

\[13 = 5-2\times4+4K(4-2)\]

 and solving this gives

\(K = 2\)

. Thus

\[\begin{align*} f(x) &= 5-2x+2x(x-2)\\ &= 2x^2-6x+5 \end{align*}\]

**An answer**

A point \(C\) is marked on the diagram. What happens to the point \(C\) as \(u\) varies and what condition must the point \(C\) satisfy?

**A final thought**
