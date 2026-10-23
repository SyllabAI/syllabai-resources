---
created: 2026-10-24T01:49:53 (UTC +06:00)
source: https://undergroundmathematics.org/calculus-of-powers/r9260
author: Underground Mathematics (University of Cambridge)
rights: © University of Cambridge (Underground Mathematics). Use inside SyllabAI is authorised by the
  operator attestation of 2026-10-23 — see LICENSE-DATA.md (Amendment 2026-10-23) in this repository.
  Takedown / correction handling as stated in LICENSE-DATA.md.
tags:
- underground-mathematics
- calculus-of-powers
- type/review-question
resource_identity:
  ugm_id: r9260
  station: calculus-of-powers
  station_title: Calculus of Powers
  resource_type_id: 10
  resource_type_label: Review question
  level: null
  ref: 9260
  old_site_id: Q1060
spec_map:
  curriculum_code: CIE-9709-P1-2023
  lane: cie-a-level-maths-20-pure-1
  board: Cambridge CIE
  syllabus_version: 2023-2025
  subsection: calculus-of-powers
  subsection_provenance:
    tier: PROVIDER
    signal: source-url-slug
    slug: calculus-of-powers
    validation_status: SUGGESTED
  spec_points:
  - code: 1.7.2
    provenance:
      tier: AI_SUGGESTED
      confidence: high
      model_version: GLM (Super Z agent, z.ai) — P3c lane-7 cross-map (cross-map-differentiation.json
        (P3c lane 7) @ syllabai-experimental 93575e69)
      evidence: 'cuboid of surface area 150 cm^2: show h=(75-x^2)/2x then maximise the volume — canonical
        CIE P1 optimisation'
      rationale: 'Canonical UGM title: "When is the volume of this cuboid a maximum?"; exam provenance:
        UCLES AO level Additional Mathematics 2, 1986, Q12(a)'
      validation_status: SUGGESTED
    title: use the derivative of x (for any rational n ), together with constant multiples, sums and
      differences of functions, and of composite functions using the chain rule
  - code: 1.7.4
    provenance:
      tier: AI_SUGGESTED
      confidence: high
      model_version: GLM (Super Z agent, z.ai) — P3c lane-7 cross-map (cross-map-differentiation.json
        (P3c lane 7) @ syllabai-experimental 93575e69)
      evidence: 'cuboid of surface area 150 cm^2: show h=(75-x^2)/2x then maximise the volume — canonical
        CIE P1 optimisation'
      rationale: 'Canonical UGM title: "When is the volume of this cuboid a maximum?"; exam provenance:
        UCLES AO level Additional Mathematics 2, 1986, Q12(a)'
      validation_status: SUGGESTED
      primaryPick: true
    title: locate stationary points and determine their nature, and use information about stationary
      points in sketching graphs.
  mapped_date: '2026-10-24'
  mapper: cross-map-differentiation.json (P3c lane 7) @ syllabai-experimental 93575e69
provenance:
  capture_date: '2026-10-22'
  capture_tool: P2 full-site crawl (ugm-crawl) → ugm-clean extraction; text-only import
  content_language: en
  exam_reference: UCLES AO level Additional Mathematics 2, 1986, Q12(a)
task: T-UGM-IMPORT-7
interactive:
- src: //www.geogebratube.org/material/iframe/id/qG6ubfmq/width/700/height/400/border/888888/rc/false/ai/false/sdz/false/smb/false/stb/false/stbh/false/ld/false/sri/true/asb/false/at/html5
  kind: geogebra-iframe
---

# When is the volume of this cuboid a maximum?

## Question

A cuboid has a total surface area of \(\quantity{150} {cm^2}\) and is such that its base is a square of side \(\quantity{x}{cm}\).

Show that the height, \(\quantity{h}{cm}\), of the cuboid is given by \(h=\frac{75-x^2}{2x}\).

Express the volume of the cuboid in terms of \(x\). Hence determine, as \(x\) varies, its maximum volume and show that this volume is a maximum.

## Suggestion

How can we find the surface area of a cuboid from its sides?

Can we write the volume of the cuboid in terms of \(x\) and \(h\)? Can we now substitute for \(h\)?

How can we find the maximum value?

This applet shows how the shape of the cuboid changes as we vary \(x\). The surface area is fixed and the length of the red line is proportional to the volume.

> [interactive embed (geogebra-iframe): //www.geogebratube.org/material/iframe/id/qG6ubfmq/width/700/height/400/border/888888/rc/false/ai/false/sdz/false/smb/false/stb/false/stbh/false/ld/false/sri/true/asb/false/at/html5] — not part of the text import; see the source page.

[Download GeoGebra file](https://www.geogebratube.org/material/download/format/file/id/qG6ubfmq)

## Solution

A cuboid with side lengths \(x\), \(x\) and \(h\) has a surface area of\[S=2x^2+4xh.\]

We know that the total surface area should be \(\quantity{150} {cm^2}\), so

\[\begin{align*} 150 &= 2x^2+4xh\\ \implies 150 -2x^2 &= 4xh\\ \implies h &= \frac{75-x^2}{2x}. \end{align*}\]

A cuboid with side lengths \(x\), \(x\) and \(h\) has a volume of \(V=x^2h\). Now

\[\begin{align*} V &= x^2h\\ &= x^2\bigl(\frac{75-x^2}{2x}\bigr)\\ &= \frac{75}{2}x-\frac{1}{2}x^3. \end{align*}\]

We have \(V\) as a function of \(x\), so to find the stationary points we differentiate, and set the result equal to zero. We have

\[V' (x) = \frac{75}{2} - \frac{3}{2} x^2.\]

Putting this equal to zero, we see

\[\begin{align*} \frac{75}{2} - \frac{3}{2} x^2 &=0\\ \implies \frac{75}{2} &= \frac{3}{2} x^2 \\ \implies 25 &= x^2 \\ \implies x &= \pm5. \end{align*}\]

Since \(x\) is a length, it must be positive, implying \(x=5\).

Is our solution a maximum? We know \(V = 0.5x(75-x^2)\), and so the equation \(V=0\) has three roots, \(0\) and \(\pm \sqrt{75}\). Given the coefficient of \(x^3\) is negative, the curve must look like this:

Thus \(x = 5\) gives us a maximum for \(V\).

Or we could show \(x = 5\) gives a maximum by evaluating the second derivative of \(V\), giving

\[\begin{align*} V''(x)&=-3x\\ \implies V''(5) &=-15. \end{align*}\]

The second derivative is negative at \(x=5\), so the volume has a maximum here, as required.

Now all that remains is to find the volume of the cuboid when \(x=5\), which is given by

\[\begin{align*} V(x) &= \frac{75}{2}x-\frac{1}{2}x^3 \\ \implies V(5) &= \frac{75}{2} \times 5 - \frac{1}{2} \times 5^3 \\ &= \frac{375}{2} - \frac{125}{2} \\ &= \frac{250}{2} \\ &= 125. \end{align*}\]

Therefore the maximum volume of the cuboid is \(\quantity{125} {cm^3}\).
