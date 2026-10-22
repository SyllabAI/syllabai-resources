---
created: 2026-10-23T02:04:16 (UTC +06:00)
source: https://undergroundmathematics.org/circles/r7656
author: Underground Mathematics (University of Cambridge)
rights: © University of Cambridge (Underground Mathematics). Use inside SyllabAI is authorised by the operator attestation of 2026-10-23 — see LICENSE-DATA.md (Amendment 2026-10-23) in this repository. 
  Takedown / correction handling as stated in LICENSE-DATA.md.
tags:
- underground-mathematics
- circles
- type/review-question
resource_identity:
  ugm_id: r7656
  station: circles
  station_title: Circles
  resource_type_id: 10
  resource_type_label: Review question
  level: null
  ref: 7656
  old_site_id: Q176
spec_map:
  curriculum_code: CIE-9709-P1-2023
  lane: cie-a-level-maths-20-pure-1
  board: Cambridge CIE
  syllabus_version: 2023-2025
  subsection: circles
  subsection_provenance:
    tier: PROVIDER
    signal: source-url-slug
    slug: circles
    validation_status: SUGGESTED
  spec_points:
  - code: 1.3.2
    provenance:
      tier: AI_SUGGESTED
      confidence: medium
      model_version: GLM (Super Z agent, z.ai) — P3c lane-3 cross-map (cross-map-coordinate-geometry.json (P3c lane 3) @
        syllabai-experimental cb947595)
      evidence: 'x^2-px+y^2-qy=0, centre and area; the area-ratio >= pi part rides inequality reasoning (recorded medium).'
      rationale: 'Canonical UGM title: “Can we show that (circle area)/(triangle area) $\geq \pi$?”; exam provenance: Oxford (MAT) 2008 Q4'
      validation_status: SUGGESTED
    title: interpret and use any of the forms y = mx + c , y – y = m ( x – x ) , ax + by + c = 0 in solving
  mapped_date: '2026-10-23'
  mapper: cross-map-coordinate-geometry.json (P3c lane 3) @ syllabai-experimental cb947595
provenance:
  capture_date: '2026-10-22'
  capture_tool: P2 full-site crawl (ugm-crawl) → ugm-clean extraction; text-only import
  content_language: en
  exam_reference: Oxford (MAT) 2008 Q4
task: T-UGM-IMPORT-3
---

# Can we show that (circle area)/(triangle area) $\geq \pi$?

## Question

Let \(p\) and \(q\) be positive real numbers. Let \(P\) denote the point \((p,0)\) and \(Q\) denote the point \((0,q)\).

1. Show that the equation of the circle \(C\) which passes through \(P\), \(Q\) and the origin \(O\) is \[x^2 - px + y^2 - qy = 0.\] Find the centre and area of \(C\).

---

1. Show that \[\frac{\text{area of circle $C$}}{\text{area of triangle $OPQ$}} \ge \pi.\]

---

1. Find the angles \(OPQ\) and \(OQP\) if \[\frac{\text{area of circle $C$}}{\text{area of triangle $OPQ$}} = 2\pi.\]

## Suggestion

[Download GeoGebra file](https://www.geogebratube.org/material/download/format/file/id/mhPnAX3R)

The areas of the circle and triangle are shown, as is their ratio.

## Solution

Substituting in the coordinates \((p,0)\), \((0,q)\) and \((0,0)\), we find that all three points satisfy the equation and so lie on the circle, so we are done.

Alternatively, we can deduce the equation from scratch once we know the centre of the circle.

The line \(PQ\) is a diameter of \(C\), since the angle \(POQ\) is a right-angle, and we know that the angle in a semi-circle is a right-angle.

So the midpoint of \(PQ\), which is \(M \left(\dfrac{p}{2}, \dfrac{q}{2}\right)\), is the centre of the circle. Thus the circle has equation \[\left(x-\frac{p}{2}\right)^2+\left(y-\frac{q}{2}\right)^2=r^2,\] for some \(r\). We can find \(r\) either by substituting the coordinates of a point on \(C\), say \((x,y)=(0,0)\), which gives \(r^2=\left(\dfrac{p}{2}\right)^2+\left(\dfrac{q}{2}\right)^2=\dfrac{p^2+q^2}{4}\), or by finding the radius, which is \(OM=AM=BM\), giving the same result.

Just using the given equation, we can complete the square to obtain \[\left(x - \frac{p}{2}\right)^2 + \left(y - \frac{q}{2}\right)^2 -\frac{p^2 + q^2}{4} = 0\] which is the equation of the circle with centre \(\left(\dfrac{p}{2},\dfrac{q}{2}\right)\) and area \(\pi\dfrac{p^2+q^2}{4}\).

Alternatively, using the argument above, we already know the centre of the circle and \(r^2\), and the area is \(\pi r^2=\pi\dfrac{p^2+q^2}{4}\).

The area of \(OPQ\) is \(\dfrac{1}{2}pq\), so \[\frac{\text{area of circle $C$}}{\text{area of triangle $OPQ$}} = \pi\frac{(p^2+q^2)/4}{pq/2} = \pi\frac{p^2+q^2}{2pq}\]

Then we note that \[\pi\dfrac{p^2 + q^2}{2pq} \ge \pi \iff p^2 + q^2 \ge 2pq \iff (p-q)^2 \ge 0\] which always holds, and so the required inequality is true.

From our previous expression we have \[\pi\frac{p^2+q^2}{2pq} = 2\pi \iff p^2 + q^2 = 4pq.\]

Then if we divide through by \(q^2\) (which we know is non-zero), we get \[\left(\frac{p}{q}\right)^2 - 4\left(\frac{p}{q}\right) + 1 = 0\] which is a quadratic in \(\dfrac{p}{q}\) with solution \[\frac{p}{q} = \frac{4 \pm \sqrt{16-4}}{2} = 2 \pm \sqrt{3}.\]

Now since triangle \(OPQ\) is right-angled, we have that \(\dfrac{p}{q} = \tan OQP\) and \(\dfrac{q}{p} = \tan OPQ\).

Then since the solutions are reciprocals of each other, we have \[\{\tan OQP, \tan OPQ\} = \{2 + \sqrt{3}, 2 - \sqrt{3}\},\] where the order depends on which of \(p\) and \(q\) is larger: if \(p>q\), then \(\tan OQP=2+\sqrt{3}\); if \(p<q\), then \(\tan OQP=2-\sqrt{3}\).

Thus \(\{OQP, OPQ\}=\{\arctan(2+\sqrt{3}), \arctan(2-\sqrt{3}\}\) in some order, depending on whether \(p>q\) or \(p<q\).

[Incidentally, it turns out that \(\arctan(2-\sqrt{3})=\dfrac{\pi}{12}\) and \(\arctan(2+\sqrt{3})=5\dfrac{\pi}{12}\), as we will learn at [Trigonometry: Compound Angles](https://undergroundmathematics.org/trigonometry-compound-angles).]
