---
created: 2026-10-23T14:47:57 (UTC +06:00)
source: https://undergroundmathematics.org/product-rule/r8936
author: Underground Mathematics (University of Cambridge)
rights: © University of Cambridge (Underground Mathematics). Use inside SyllabAI is authorised by the
  operator attestation of 2026-10-23 — see LICENSE-DATA.md (Amendment 2026-10-23) in this repository.
  Takedown / correction handling as stated in LICENSE-DATA.md.
tags:
- underground-mathematics
- product-rule
- type/review-question
resource_identity:
  ugm_id: r8936
  station: product-rule
  station_title: Product Rule & Integration by Parts
  resource_type_id: 10
  resource_type_label: Review question
  level: null
  ref: 8936
  old_site_id: Q3024
spec_map:
  curriculum_code: CIE-9709-P1-2023
  lane: cie-a-level-maths-20-pure-1
  board: Cambridge CIE
  syllabus_version: 2023-2025
  subsection: product-rule
  subsection_provenance:
    tier: PROVIDER
    signal: source-url-slug
    slug: product-rule
    validation_status: SUGGESTED
  spec_points:
  - code: 1.4.1
    provenance:
      tier: AI_SUGGESTED
      confidence: medium
      model_version: GLM (Super Z agent, z.ai) — P3c lane-4 cross-map (cross-map-circular-measure.json
        (P3c lane 4) @ syllabai-experimental b52cf1bf)
      evidence: 'Arc QR of a circle centred at P with radius PQ: arc length s = rθ modelled; the maximisation
        rides 1.7.'
      rationale: 'Canonical UGM title: “When will the arclength $QR$ take a maximum value?”; exam provenance:
        UCLES 1970 Q6(ii)'
      validation_status: SUGGESTED
    title: understand the definition of a radian, and use the relationship between radians and degrees
  mapped_date: '2026-10-23'
  mapper: cross-map-circular-measure.json (P3c lane 4) @ syllabai-experimental b52cf1bf
provenance:
  capture_date: '2026-10-22'
  capture_tool: P2 full-site crawl (ugm-crawl) → ugm-clean extraction; text-only import
  content_language: en
  exam_reference: UCLES 1970 Q6(ii)
task: T-UGM-IMPORT-4
interactive:
- src: //www.geogebratube.org/material/iframe/id/NFaPz3AU/width/700/height/450/border/888888/rc/false/ai/false/sdz/false/smb/false/stb/false/stbh/false/ld/false/sri/true/asb/false/at/html5
  kind: geogebra-iframe
---

# When will the arclength $QR$ take a maximum value?

## Question

\(P\) is a point on the circumference of a circle \(X\) of diameter \(\quantity{3}{in.}\) An arc of another circle \(Y\) is drawn with centre \(P\), intersecting \(X\) at \(Q\) and \(R\). Express the lengths of \(PQ\) and the minor arc \(QR\) of \(Y\) in terms of \(\theta\), where \(\theta\) is the angle, in radians, between \(PQ\) and the diameter of \(X\) through \(P\).

Prove that the length of the arc \(QR\) has a stationary value when \(\theta = \cot \theta\), and that this value is a maximum.

## Suggestion

We ought to begin by drawing the configuration described in the question. How can we find the length of \(PQ\)? Could we try adding to the configuration?

A further suggestion

If we let \(P'\) denote the other end of the diameter of \(X\) that passes through \(P\), what can we say about \(\triangle P'QP\)?

A final suggestion

Do we know anything about \(\angle P'QP\)?

When checking that a value is a maximum of a function, do we *have* to calculate the second derivative of the function?

## Solution

\(P\) is a point on the circumference of a circle \(X\) of diameter \(\quantity{3}{in.}\) . An arc of another circle \(Y\) is drawn with centre \(P\), intersecting \(X\) at \(Q\) and \(R\). Express the lengths of \(PQ\) and the minor arc \(QR\) of \(Y\) in terms of \(\theta\), where \(\theta\) is the angle, in radians, between \(PQ\) and the diameter of \(X\) through \(P\).

Here’s a diagram of the two circles \(X\) and \(Y\).

If you drew your circle \(Y\) larger than your circle \(X\), your diagram will look quite different to this: there’s no need to worry, the mathematics works just the same.

You can explore different versions of the diagram with this interactive:

Varying \(Y\)

> [interactive embed (geogebra-iframe): //www.geogebratube.org/material/iframe/id/NFaPz3AU/width/700/height/450/border/888888/rc/false/ai/false/sdz/false/smb/false/stb/false/stbh/false/ld/false/sri/true/asb/false/at/html5] — not part of the text import; see the source page.

[Download GeoGebra file](https://www.geogebratube.org/material/download/format/file/id/NFaPz3AU)

Drag the point \(R\) to change the size of \(Y\).

We’ll calculate the two lengths in turn. Firstly, to find \(PQ\), let’s look at the circle \(X\).

Since the angle \(PQP'\) lies in a semicircle, it must be a right angle. Now, from trigonometry, \[\cos \theta = \frac{\text{adjacent}}{\text{hypotenuse}} = \frac{\text{length of $PQ$}}{\text{length of $PP'$}} \implies \text{length of $PQ$} = 3 \cos \theta.\]

Secondly, to find the length of the minor arc \(QR\), let’s look at the circle \(Y\).

The length of an arc of a circle is \(r\phi\), where \(\phi\) is the angle subtended at the centre of the circle by the arc.

By symmetry, \(\angle QPR = \theta + \theta = 2\theta\), and so the length of the minor arc \(QR\) is \(PQ \times 2\theta = 6\theta\cos\theta.\)

We know that \[QR = 6 \theta \cos \theta.\] Using the [product rule](https://undergroundmathematics.org/glossary/product-rule), we have \[\dfrac{d(QR)}{d\theta}= 6\theta (-\sin \theta) + 6\cos \theta = 6 (\cos \theta - \theta \sin \theta).\]

So the stationary points are those values of \(\theta\) for which \[\cos \theta = \theta \sin \theta,\] which is true if and only if \[\theta = \cot \theta.\]

We can divide through here by \(\sin \theta\), since \(\theta = 0\) is not going to be a solution to our equation.

We are only concerned with the interval \(0 \le \theta \le \dfrac{\pi}{2}\).

Since \(\theta\) increases from zero and \(\cot \theta\) descends from infinity, as illustrated below, our equation has just one solution.

Is this a maximum? We know that \(QR > 0\) when \(0 < \theta < \dfrac{\pi}{2}\), that \(QR = 0\) when \(\theta = 0\) and \(\dfrac{\pi}{2}\), and that there’s only one stationary point between \(0\) and \(\dfrac{\pi}{2}\); therefore, this point *has* to be a maximum.

We can see this in the changing values in the GeoGebra illustration above.

If we try dragging \(R\), what happens to \(QR\)? For what value of \(\theta\) is this a maximum? Does \(\theta = \cot \theta\) here?

Alternatively, we could calculate the second derivative \(f''(\theta)\) and check that it’s negative on this interval.
