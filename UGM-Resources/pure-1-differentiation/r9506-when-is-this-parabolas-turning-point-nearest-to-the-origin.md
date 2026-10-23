---
created: 2026-10-24T01:49:53 (UTC +06:00)
source: https://undergroundmathematics.org/introducing-calculus/r9506
author: Underground Mathematics (University of Cambridge)
rights: © University of Cambridge (Underground Mathematics). Use inside SyllabAI is authorised by the
  operator attestation of 2026-10-23 — see LICENSE-DATA.md (Amendment 2026-10-23) in this repository.
  Takedown / correction handling as stated in LICENSE-DATA.md.
tags:
- underground-mathematics
- introducing-calculus
- type/review-question
resource_identity:
  ugm_id: r9506
  station: introducing-calculus
  station_title: Introducing Calculus
  resource_type_id: 10
  resource_type_label: Review question
  level: null
  ref: 9506
  old_site_id: Q114
spec_map:
  curriculum_code: CIE-9709-P1-2023
  lane: cie-a-level-maths-20-pure-1
  board: Cambridge CIE
  syllabus_version: 2023-2025
  subsection: introducing-calculus
  subsection_provenance:
    tier: PROVIDER
    signal: source-url-slug
    slug: introducing-calculus
    validation_status: SUGGESTED
  spec_points:
  - code: 1.7.4
    provenance:
      tier: AI_SUGGESTED
      confidence: medium
      model_version: GLM (Super Z agent, z.ai) — P3c lane-7 cross-map (cross-map-differentiation.json
        (P3c lane 7) @ syllabai-experimental 93575e69)
      evidence: turning point of y=x^2-2ax+1 closest to the origin as a varies — stationary-point location
        with transformations as the alternative approach
      rationale: 'Canonical UGM title: "When is this parabola''s turning point nearest to the origin?";
        exam provenance: Oxford University Mathematics Aptitude Test, None, Q1F'
      validation_status: SUGGESTED
    title: locate stationary points and determine their nature, and use information about stationary
      points in sketching graphs.
  mapped_date: '2026-10-24'
  mapper: cross-map-differentiation.json (P3c lane 7) @ syllabai-experimental 93575e69
provenance:
  capture_date: '2026-10-22'
  capture_tool: P2 full-site crawl (ugm-crawl) → ugm-clean extraction; text-only import
  content_language: en
  exam_reference: Oxford University Mathematics Aptitude Test, None, Q1F
task: T-UGM-IMPORT-7
interactive:
- src: //www.geogebratube.org/material/iframe/id/YGjuzvmT/width/400/height/600/border/888888/rc/false/ai/false/sdz/false/smb/false/stb/false/stbh/false/ld/false/sri/true/asb/false/at/html5
  kind: geogebra-iframe
---

# When is this parabola's turning point nearest to the origin?

## Question

The turning point of the parabola \[y=x^2-2ax+1\] is closest to the origin when

1. \(a=0\),

---

1. \(a=\pm1\),

---

1. \(a=\pm \frac{1}{\sqrt{2}}\) or \(a=0\),

---

1. \(a=\pm \frac{1}{\sqrt{2}}\).

## Suggestion

First we need to find the turning point of the parabola. How might we do this?

How can we work out the distance between this point and the origin?

## Solution

One approach is to think about each case in turn and rely on [transformations](https://undergroundmathematics.org/pervasive-ideas/transforming). For ease we will let \(f(x)=x^2\)

1. If \(a=0\) we have \(y=f(x)+1\): the turning point is \(1\) unit from the origin.

---

1. If \(a=\pm1\) I can recognise this as an expanded square bracket of \(x\pm1\) so I have \(y=f(x\mp1)\): again the turning point is \(1\) unit from the origin.

---

1. can’t be correct from a logical point of view: since in cases (a) and (b) the turning points are the same distance from the origin then (c) must also include \(a=\pm1\) if \(\pm \frac{1}{\sqrt{2}}\) and \(a=0\) are both options (i.e. the turning point has the same proximity in both cases), so \(\pm \frac{1}{\sqrt{2}}\) is different and therefore smaller (because if it were larger there would need to be the answer \(\, \text{"} a=0\) or \(a=\pm1 \text{"}\,\) available).

Hence the answer is (d).

A second approach is to find the turning point of the parabola. Completing the square, we have

\[\begin{align*} y &= x^2 - 2ax + 1 \\ &= (x - a)^2 + 1 - a^2, \end{align*}\]

so the minimum occurs when \(x = a\) and then \(y = 1 - a^2\). So the turning point is at \[(a, 1 - a^2).\]

Now the distance from the turning point to the origin is given by

\[\begin{align*} D &= \sqrt{a^2 + (1-a^2)^2} \\ &= \sqrt{a^4 - a^2 + 1} \\ &= \sqrt{\left(a^2 - \dfrac{1}{2}\right)^2 + \dfrac{3}{4}}, \end{align*}\]

where we have again completed the square.

So this distance is minimised when \[\left(a^2 - \frac{1}{2}\right)^2=0,\] which is when \(a=\pm\dfrac{1}{\sqrt{2}}\).

So the answer is (d).

Being able to minimise or maximse something is a useful tool (think costs, profits, time etc.). We could minimise our distance here because we were able to complete the square, but in order to minimise different functions we will need to explore ideas that appear at the [Calculus of Powers](https://undergroundmathematics.org/calculus-of-powers) station and beyond.

This GeoGebra file helps us to see what is happening.

> [interactive embed (geogebra-iframe): //www.geogebratube.org/material/iframe/id/YGjuzvmT/width/400/height/600/border/888888/rc/false/ai/false/sdz/false/smb/false/stb/false/stbh/false/ld/false/sri/true/asb/false/at/html5] — not part of the text import; see the source page.

[Download GeoGebra file](https://www.geogebratube.org/material/download/format/file/id/YGjuzvmT)
