---
created: 2026-10-25T21:48:43 (UTC +06:00)
source: https://undergroundmathematics.org/calculus-trig-log/similar-derivatives
author: Underground Mathematics (University of Cambridge)
rights: © University of Cambridge (Underground Mathematics). Use inside SyllabAI is authorised by the
  operator attestation of 2026-10-23 — see LICENSE-DATA.md (Amendment 2026-10-23) in this repository.
  Takedown / correction handling as stated in LICENSE-DATA.md.
tags:
- underground-mathematics
- calculus-trig-log
- type/building-blocks
resource_identity:
  ugm_id: similar-derivatives
  station: calculus-trig-log
  station_title: Calculus of Trigonometry & Logarithms
  resource_type_id: 1
  resource_type_label: Building blocks
  level: Developing
  ref: 5178
  old_site_id: null
spec_map:
  curriculum_code: CIE-9709-P3-2023
  lane: cie-a-level-maths-20-pure-3
  board: Cambridge CIE
  syllabus_version: 2023-2025
  subsection: calculus-trig-log
  subsection_provenance:
    tier: PROVIDER
    signal: source-url-slug
    slug: calculus-trig-log
    validation_status: SUGGESTED
  spec_points:
  - code: 3.4.1
    provenance:
      tier: AI_SUGGESTED
      confidence: medium
      model_version: GLM (Super Z agent, z.ai) — P3c lane-12 cross-map (cross-map-p3-differentiation.json
        (P3c lane 12) @ syllabai-experimental 506ea24f8e61cc75c4662f8ebb08cfd2b1d458d4)
      evidence: d(tan theta)/dtheta via similar triangles with vertices (1, tan theta) and (cot theta,
        1) - in-spec for the tan limb of 3.4.1; the sec/cot extensions are beyond the 3.4.1 list and are
        disclosed (flips the lane-11 non-overlap row of record routed 'P3 3.4 Differentiation')
      rationale: 'Canonical UGM title: Similar derivatives'
      validation_status: SUGGESTED
    title: use the derivatives of e , ln x , sin x , cos x , tan x , tan x , together with constant multiples,
      sums, differences and composites
  mapped_date: '2026-10-25'
  mapper: cross-map-p3-differentiation.json (P3c lane 12) @ syllabai-experimental 506ea24f8e61cc75c4662f8ebb08cfd2b1d458d4
provenance:
  capture_date: '2026-10-22'
  capture_tool: P2 full-site crawl (ugm-crawl) → ugm-clean extraction; text-only import
  content_language: en
  task: T-UGM-IMPORT-12
---

# Similar derivatives

> Excerpt: By considering a small change in angle, students use similar triangles to give a geometric explanation of the derivatives of $\tan \theta$, $\sec \theta$, $\cot \theta$ and $\cosec \theta$. There are opportunities to make geometric sense of the factors of $\sec \theta$ and $\cosec \theta$ that arise in the derivatives.

## Problem

Can you explain why the points given in the diagram below have coordinates \((1, \tan \theta)\) and \((\cot \theta, 1)\)?

Now move the slider for \(\delta \theta\).

- What is the relationship between the blue angle and the red angle?

- What can you say about the blue triangles and the red triangle as \(\delta \theta\) decreases to \(0\)?

> [interactive embed (geogebra-iframe): //www.geogebratube.org/material/iframe/id/TTZRczW4/width/541/height/408/border/888888/rc/false/ai/false/sdz/false/smb/false/stb/false/stbh/false/ld/false/sri/true/asb/false/at/html5] — not part of the text import; see the source page.

[Download GeoGebra file](https://www.geogebratube.org/material/download/format/file/id/TTZRczW4)

Consider the blue triangle which has one vertex at \((1, \tan \theta)\).

- What is the length of the circular arc drawn through \((1, \tan \theta)\) and subtended by \(\delta \theta\)?

- Which side length shows the increase in \(\tan \theta\) as \(\theta\) increases by \(\delta \theta\)? This can be denoted by \(\delta(\tan\theta)\).

How can you use these ideas to find the derivative of \(\tan \theta\)?

What about the derivative of \(\sec \theta\)?

Can you take a similar approach to find the derivatives of \(\cot \theta\) and \(\cosec \theta\)? You may be able to do this in more than one way.

## Suggestion

Can you explain why the points given in the diagram below have coordinates \((1, \tan \theta)\) and \((\cot \theta, 1)\)?

> [interactive embed (geogebra-iframe): //www.geogebratube.org/material/iframe/id/TTZRczW4/width/541/height/408/border/888888/rc/false/ai/false/sdz/false/smb/false/stb/false/stbh/false/ld/false/sri/true/asb/false/at/html5] — not part of the text import; see the source page.

[Download GeoGebra file](https://www.geogebratube.org/material/download/format/file/id/TTZRczW4)

You may find it helpful to consider similar triangles, or look at [Going round in circles](https://undergroundmathematics.org/trigonometry-triangles-to-functions/going-round-in-circles).

Take a look at the triangles in the diagram.

What similar triangles can you find?

What do you see as \(\delta \theta \rightarrow 0\)?

It may be helpful to label some points in the diagram.

How can the length of the hypotenuse of the red triangle be expressed in terms of \(\theta\)?

How can this help us to find the arc length?

\(QP\) is \(\tan \theta\) and \(QT\) is \(\tan (\theta+ \delta \theta)\).

When \(\delta \theta\) is small, one side of each blue triangle can be approximated by a circular arc.

As \(\delta \theta \rightarrow 0\), the red and blue triangles get closer and closer to being similar. Which are the corresponding sides in the red and blue triangles?

## Solution

You may find it helpful to look at the [circles](https://undergroundmathematics.org/trigonometry-triangles-to-functions/going-round-in-circles/circles-problem) section of [Going round in circles](https://undergroundmathematics.org/trigonometry-triangles-to-functions/going-round-in-circles/) to see how \(\tan \theta\) and \(\cot \theta\) relate to the unit circle.

Move the slider so that the blue triangles are visible. Note that the blue angle is \(\theta + \delta \theta\) and the red angle is \(\theta\). Therefore the blue triangles are both similar to the triangle with angle \(\theta + \delta \theta\) and right-angle at \((1,0).\) This triangle tends to the red triangle as \(\delta \theta\) tends to \(0\) (written \(\delta \theta \rightarrow 0\)), so the blue triangles get closer and closer to being similar to the red triangle as \(\delta \theta \rightarrow 0\).

Consider the blue triangle with one vertex at \((1, \tan \theta)\).

- What is the length of the circular arc drawn through \((1, \tan \theta)\) and subtended by \(\delta \theta\)?

In triangle \(OQP\), Pythagoras’ theorem tells us that \(OP=\sec \theta\) (note that \(\theta\) is acute in this case, so \(\sec \theta >0\)).

Alternatively, \(\cos \theta = \dfrac{1}{OP}\) so \(OP=\dfrac{1}{\cos \theta}= \sec \theta\).

\(OP\) is the radius of the circular arc drawn through \(P\) and subtended by \(\delta \theta\), so the length of this arc is \(\sec \theta \,\delta \theta.\) For small \(\delta \theta\), we can therefore approximate \(PS\) by \[PS \approx \sec \theta \,\delta \theta.\]

Why is it important that \(\theta\) and \(\delta \theta\) are measured in radians?

- Which side length shows the increase in \(\tan \theta\) as \(\theta\) increases by \(\delta \theta\)? This can be denoted by \(\delta (\tan \theta)\).

\(PT=\tan (\theta+ \delta \theta) -\tan \theta\), so \(PT\) shows the increase in \(\tan \theta\) as \(\theta\) increases by \(\delta \theta\). We’ll write this as \(\delta (\tan \theta)\) as it is the change in \(\tan \theta\).

The derivative of \(\tan \theta\) is given by \[\lim_{\delta \theta \rightarrow 0} \dfrac{\tan (\theta+ \delta \theta) -\tan \theta}{\delta \theta}\] so using our notation, we are interested in \(\dfrac{\delta (\tan \theta)}{\delta \theta}.\)

What can the blue and red triangles tell us about this fraction?

We have approximations for the lengths of two sides of the blue triangle when \(\delta \theta\) is small. As \(\delta \theta \rightarrow 0\), the blue and red triangles get closer to being similar, so it may help to consider corresponding sides and angles in the two triangles.

For small \(\delta \theta\), the corresponding ratios of sides gives us \(\dfrac{PT}{PS}\approx\dfrac{OP}{OQ}\), so

\[\dfrac{\delta (\tan \theta)}{\sec \theta \,\delta \theta}\approx \dfrac{\sec \theta }{1} \quad \text{or equivalently} \quad \dfrac{\delta (\tan \theta)}{\delta \theta}\approx \sec^2 \theta.\]

Taking the limit as \(\delta \theta \rightarrow 0\) then gives the derivative of \(\tan \theta\),

\[\dfrac{d}{d\theta}(\tan \theta) = \sec^2 \theta.\]

What does this say about the sign of the gradient function of \(\tan \theta\)? Can you connect this with the graph of \(\tan \theta\)?

We’ll refer back to our first labelled diagram. The length of the hypotenuse of triangle \(OQP\) is \(\sec \theta\), so as \(\theta\) increases by \(\delta \theta,\) \(ST\) shows the increase in \(\sec \theta.\)

How can you use these triangles to show that \(\dfrac{d}{d \theta}(\sec \theta) = \sec \theta \tan \theta\)?

The blue triangle with a vertex at \((\cot \theta, 1)\) can be used to find derivatives of \(\cot \theta\) and \(\cosec \theta\), so we’ll label the vertices of this triangle as well.

You could use a similar approach to before, by considering ratios of sides in

- triangles \(UVM\) and \(MNO\) (since \(MNO\) is similar to \(OQP\) and \(OM =\cosec \theta\)), or

- triangles \(UVM\) and \(OQP\) (since the sides of \(OQP\) don’t depend on \(\delta \theta\)), or

- triangles \(UVM\) and \(PST\) (these are similar even if \(\delta \theta\) isn’t small).

We’ll use triangles \(UVM\) and \(MNO\), but what happens if you use different triangles?

Derivatives

We can start in a similar way, noting that \(MV\approx \cosec \theta \,\delta \theta.\) One thing we have to be careful about though is that as \(\theta\) increases by \(\delta \theta\), \(\cot \theta\) and \(\cosec \theta\) *decrease*. Therefore we’ll write \(UM=-\delta(\cot \theta).\)

We can compare ratios of sides in triangles \(UVM\) and \(MNO\) to get \(\dfrac{UM}{VM}\approx \dfrac{NM}{1}\).

Therefore we have \(\dfrac{-\delta (\cot \theta)}{\cosec \theta\,\delta \theta}\approx \dfrac{\cosec \theta }{1}\) which leads to \(\dfrac{d}{d\theta}(\cot \theta) = -\cosec^2 \theta.\)

By writing \(UV=-\delta (\cosec \theta)\), we can also show that \(\dfrac{d}{d\theta}(\cosec \theta) = -\cosec \theta \cot \theta.\)

We have worked with a diagram in which \(\theta\) is acute. Do these results hold for any value of \(\theta\)?
