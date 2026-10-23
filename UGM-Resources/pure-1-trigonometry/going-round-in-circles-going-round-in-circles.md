---
created: 2026-10-23T16:39:10 (UTC +06:00)
source: https://undergroundmathematics.org/trigonometry-triangles-to-functions/going-round-in-circles
author: Underground Mathematics (University of Cambridge)
rights: © University of Cambridge (Underground Mathematics). Use inside SyllabAI is authorised by the
  operator attestation of 2026-10-23 — see LICENSE-DATA.md (Amendment 2026-10-23) in this repository.
  Takedown / correction handling as stated in LICENSE-DATA.md.
tags:
- underground-mathematics
- trigonometry-triangles-to-functions
- type/building-blocks
- level/introducing
resource_identity:
  ugm_id: going-round-in-circles
  station: trigonometry-triangles-to-functions
  station_title: 'Trigonometry: Triangles to Functions'
  resource_type_id: 1
  resource_type_label: Building blocks
  level: Introducing
  ref: 6460
  old_site_id: null
spec_map:
  curriculum_code: CIE-9709-P1-2023
  lane: cie-a-level-maths-20-pure-1
  board: Cambridge CIE
  syllabus_version: 2023-2025
  subsection: trigonometry-triangles-to-functions
  subsection_provenance:
    tier: PROVIDER
    signal: source-url-slug
    slug: trigonometry-triangles-to-functions
    validation_status: SUGGESTED
  spec_points:
  - code: 1.5.1
    provenance:
      tier: AI_SUGGESTED
      confidence: high
      model_version: GLM (Super Z agent, z.ai) — P3c lane-5 cross-map (cross-map-trigonometry.json (P3c
        lane 5) @ syllabai-experimental 75f1cfb8)
      evidence: 'unit-circle definitions: similar right triangles give sinθ, cosθ, tanθ and the point
        (cosθ, sinθ) on the circle — the canonical 1.5.1 foundation'
      rationale: 'Canonical UGM title: “Going round in circles”'
      validation_status: SUGGESTED
      primaryPick: true
    title: sketch and use graphs of the sine, cosine and Including e.g. tangent functions (for angles
      of any size, and using either degrees or radians)
  mapped_date: '2026-10-23'
  mapper: cross-map-trigonometry.json (P3c lane 5) @ syllabai-experimental f3ef5745
provenance:
  capture_date: '2026-10-22'
  capture_tool: P2 full-site crawl (ugm-crawl) → ugm-clean extraction; text-only import
  content_language: en
task: T-UGM-IMPORT-5
assets:
- path: https://undergroundmathematics.org/trigonometry-triangles-to-functions/going-round-in-circles/download/teacher-notes.pdf
  kind: printable
interactive:
- src: //www.geogebratube.org/material/iframe/id/eCfgTTuZ/width/595/height/467/border/888888/rc/false/ai/false/sdz/false/smb/false/stb/false/stbh/false/ld/false/sri/true/asb/false/at/html5
  kind: geogebra-iframe
- src: //www.geogebratube.org/material/iframe/id/Apf35Vug/width/595/height/467/border/888888/rc/false/ai/false/sdz/false/smb/false/stb/false/stbh/false/ld/false/sri/true/asb/false/at/html5
  kind: geogebra-iframe
---

# Going round in circles

> Excerpt: Right-angled triangles are used to introduce $\sec \theta$, $\cosec \theta$ and $\cot \theta$ and identities relating all six trigonometric functions.  Then the unit circle is used to explore how these functions behave as $\theta$ varies.

## Triangles

Here are three triangles with some side lengths and angles marked. Express the missing side lengths in terms of \(\sin \theta\), \(\cos \theta\) and \(\tan \theta.\)

- How can using side length ratios for \(\sin \theta\), \(\cos \theta\) and \(\tan \theta\) help you?

- These triangles are all similar. How can you use this to help you?

What do you notice if you compare the results of the two approaches?

New functions from old…

Functions such as \(\dfrac{1}{\cos \theta}\) are often called *reciprocal trig functions* and have special names

\[\dfrac{1}{\cos \theta}=\sec \theta \quad \quad \dfrac{1}{\sin \theta}=\cosec \theta \quad \quad \dfrac{1}{\tan \theta}=\cot \theta.\]

These are short for “secant”, “cosecant” and “cotangent” respectively; they are usually referred to by their short names.

We now have six trigonometric functions. From the side lengths in the triangles above, what relationships can you find between these functions?

## Triangles solution

Here are three triangles with some side lengths and angles marked. Express the missing side lengths in terms of \(\sin \theta\), \(\cos \theta\) and \(\tan \theta.\)

- How can using side length ratios for \(\sin \theta\), \(\cos \theta\) and \(\tan \theta\) help you?

- How can using similar triangles help you?

Using trigonometric ratios

In triangle \(OAB\) we are given the hyptenuse and we want to find the opposite and adjacent sides. We know that \(\sin \theta = \dfrac{AB}{OB}\) and \(\cos \theta = \dfrac{OA}{OB}\), so using \(OB=1\) gives us \(AB =\sin \theta\) and \(OA= \cos \theta.\)

If we use \(\sin \theta = \dfrac{CD}{OD}\) in triangle \(OCD\) we obtain \(OD = \dfrac{1}{\sin \theta}.\) Using \(\tan \theta = \dfrac{AB}{OA}\) gives us \(OC =\dfrac{1}{\tan \theta}.\)

We can also find the side lengths in triangle \(OEF\) using these approaches.

Using similar triangles

Note that triangle \(OCD\) is similar to triangle \(OAB\) and the scale factor for side length is \(\dfrac{1}{\sin \theta}\). This gives us \(OD = \dfrac{1}{\sin \theta}\) and \(OC=\dfrac{\cos \theta}{\sin \theta}.\)

What happens if we use a similar approach for triangle \(OEF\)?

Solutions

Using trig ratios we obtain the following side lengths.

Using similar triangles we obtain these side lengths.

What do you notice if you compare the results of the two approaches?

From side \(EF\) we have \(\tan \theta = \dfrac{\sin \theta}{\cos \theta}.\)

We now have six trigonometric functions. From the side lengths in the triangles above, what relationships can you find between these functions?

We can start by relabelling the triangles’ sides using \(\sec \theta\), \(\cosec \theta\) and \(\cot \theta.\)

Using Pythagoras’ theorem for each triangle gives us three results relating pairs of functions \[\cos^2 \theta + \sin^2 \theta = 1 \quad \cot^2 \theta + 1 = \cosec^2 \theta \quad \text{and} \quad 1 + \tan^2 \theta = \sec^2 \theta.\]

## Circles

In the diagram below, \(P\) is a point on a circle of radius \(1\) and \(\theta\) is the angle between \(OP\) and the positive \(x\)-axis.

We have drawn in the diameter through \(P.\)

- \(M\) is the point where the diameter through \(P\) meets the line \(x=1\)

- \(N\) is the point where the diameter through \(P\) meets the line \(y=1\)

Using the functions from the triangles problem, work out the coordinates of points \(P\), \(M\) and \(N.\)

As \(\theta\) varies, how will \(M\) and \(N\) move? What happens when \(\theta\) isn’t acute?

- When will \(M\) and \(N\) be moving quickly?

- Do \(M\) and \(N\) always move smoothly?

- When will their \(x\)- or \(y\)-coordinates change sign?

In the next diagram, we have drawn the tangent to the circle at \(P\) and marked the points where the tangent at \(P\) meets the axes.

What are the coordinates of \(K\) and \(L\)? How will \(K\) and \(L\) move along the axes as \(\theta\) varies?

## Things you might have noticed

The triangles in the previous part of the problem may help you to work out some side lengths.

We have added some extra labels to the diagram.

The hypotenuse of \(OPQ\) has length \(1\), so \(OQ\) has length \(\cos \theta\) and \(QP\) has length \(\sin \theta\). This means that the coordinates of \(P\) are \((\cos \theta, \sin \theta)\).

To find the \(y\)-coordinate of \(M\), note that \(OU\) has length \(1\) so \(UM\) has length \(\tan \theta\). Therefore \(M\) has coordinates \((1, \tan \theta)\). The similarity of triangles \(OPQ\) and \(OMU\) again tells us that \(\tan \theta = \dfrac{\sin \theta}{\cos \theta}\).

To find the \(x\)-coordinate of \(N\), note that \(y=1\) is parallel to the \(x\)-axis so angle \(ONV\) is \(\theta.\) As \(OV\) has length \(1\), this means the coordinates of \(N\) are \((\cot \theta, 1)\).

As \(\theta\) varies, how will \(M\) and \(N\) move? What happens when \(\theta\) isn’t acute?

- When will \(M\) and \(N\) be moving quickly?

- Do \(M\) and \(N\) always move smoothly?

- When will their \(x\)- or \(y\)-coordinates change sign?

You can see how \(M\) and \(N\) move as \(\theta\) varies in the GeoGebra file below.

> [interactive embed (geogebra-iframe): //www.geogebratube.org/material/iframe/id/eCfgTTuZ/width/595/height/467/border/888888/rc/false/ai/false/sdz/false/smb/false/stb/false/stbh/false/ld/false/sri/true/asb/false/at/html5] — not part of the text import; see the source page.

[Download GeoGebra file](https://www.geogebratube.org/material/download/format/file/id/eCfgTTuZ)

Could you sketch graphs of \(\tan \theta\) against \(\theta\) and \(\cot \theta\) against \(\theta\)? Download [this](https://undergroundmathematics.org/trigonometry-triangles-to-functions/going-round-in-circles/assets/mgraphtrace.ggb) file to see the graph of \(y=\tan \theta\) traced out.

In the next diagram, we have drawn the tangent to the circle at \(P\) and marked the points where the tangent at \(P\) meets the axes.

What are the coordinates of \(K\) and \(L\)? How will \(K\) and \(L\) move along the axes as \(\theta\) varies?

The line \(LK\) is a tangent to the circle at \(P\), so \(OP\) is at right angles to \(LK\).

Therefore triangle \(OPK\) is right-angled with angle \(\theta\) at \(O\) and adjacent side of length \(1\). This means that \(OK\) has length \(\sec \theta\) and the coordinates of \(K\) are \((\sec \theta, 0)\).

Likewise, triangle \(OPL\) is right-angled with angle \(\theta\) at \(L\), so \(L\) has coordinates \((0,\cosec \theta)\).

You can see how \(K\) and \(L\) move as \(\theta\) varies in the GeoGebra file below. Could you sketch graphs of \(\sec \theta\) and \(\cosec \theta\) against \(\theta\)?

> [interactive embed (geogebra-iframe): //www.geogebratube.org/material/iframe/id/Apf35Vug/width/595/height/467/border/888888/rc/false/ai/false/sdz/false/smb/false/stb/false/stbh/false/ld/false/sri/true/asb/false/at/html5] — not part of the text import; see the source page.

[Download GeoGebra file](https://www.geogebratube.org/material/download/format/file/id/Apf35Vug)

We have used \(\theta\) to parametrise the circle because as \(\theta\) varies, the locus of the point \(P(\cos \theta, \sin \theta)\) is a circle, centre \(0\), radius \(1.\) We could say that \(\theta\) parametrises the lines \(x=1\) and \(y=1\) because the points \(M(1, \tan \theta)\) and \(N(\cot \theta,1)\) trace out these lines as \(\theta\) varies. Similarly, we could say that the \(x\) and \(y\) axes are parametrised by \(\theta\) via the points \(K(\sec \theta,0)\) and \(L(0, \cosec \theta)\) respectively.
