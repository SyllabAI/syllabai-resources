---
created: 2026-10-23T02:04:16 (UTC +06:00)
source: https://undergroundmathematics.org/circles/r6390
author: Underground Mathematics (University of Cambridge)
rights: © University of Cambridge (Underground Mathematics). Use inside SyllabAI is authorised by the operator attestation of 2026-10-23 — see LICENSE-DATA.md (Amendment 2026-10-23) in this repository. 
  Takedown / correction handling as stated in LICENSE-DATA.md.
tags:
- underground-mathematics
- circles
- type/review-question
resource_identity:
  ugm_id: r6390
  station: circles
  station_title: Circles
  resource_type_id: 10
  resource_type_label: Review question
  level: null
  ref: 6390
  old_site_id: Q1
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
      confidence: high
      model_version: GLM (Super Z agent, z.ai) — P3c lane-3 cross-map (cross-map-coordinate-geometry.json (P3c lane 3) @
        syllabai-experimental cb947595)
      evidence: 'General form x^2+y^2+2gx+2fy+c=0 -> centre/radius proof; two circles shown to lie entirely outside each other — general-form mastery.'
      rationale: 'Canonical UGM title: “Can we show these two circles lie entirely outside each other?”; exam provenance: UCLES 1953 Q2'
      validation_status: SUGGESTED
    title: interpret and use any of the forms y = mx + c , y – y = m ( x – x ) , ax + by + c = 0 in solving
  mapped_date: '2026-10-23'
  mapper: cross-map-coordinate-geometry.json (P3c lane 3) @ syllabai-experimental cb947595
provenance:
  capture_date: '2026-10-22'
  capture_tool: P2 full-site crawl (ugm-crawl) → ugm-clean extraction; text-only import
  content_language: en
  exam_reference: UCLES 1953 Q2
task: T-UGM-IMPORT-3
---

# Can we show these two circles lie entirely outside each other?

## Question

Prove that the points whose coordinates satisfy the equation \[x^2+y^2+2gx+2fy+c=0\] lie on a circle. State the coordinates of the centre of the circle and the length of its radius.

Prove that the circles \[x^2+y^2-20x-16y+128=0\] and \[4x^2+4y^2+16x-24y-29=0\] lie entirely outside each other, and find the length of the shortest distance from a point on one circle to a point on the other.

## Suggestion

Do we know a standard form for the equation of a circle?

Can we rewrite the above equation into this form?

To “prove” the points are on a circle, we need to do more than state a standard equation. Can we show that all the points are the same distance from the centre?

Drawing a diagram will probably help.

Can we use the results from the first part of the question?

## Solution

Completing the square

gives us

\[(x+g)^2-g^2+(y+f)^2-f^2=c,\]

or

\[\begin{equation} (x+g)^2+(y+f)^2=g^2+f^2 - c.\label{eq:1} \end{equation}\]

This looks like the standard equation of a circle, but the circle only exists if \(g^2+f^2 - c>0\).

By [Pythagoras’s theorem](https://undergroundmathematics.org/glossary/pythagoras-theorem), the distance between the points \((x_1,y_1)\) and \((x_2,y_2)\) is \[\sqrt{(x_2-x_1)^2+(y_2-y_1)^2}.\]

Taking square roots of both sides of \(\eqref{eq:1}\) gives \[\sqrt{(x+g)^2+(y+f)^2}=\sqrt{g^2+f^2 - c}\] and so the distance between points \((x,y)\) and \((-g,-f)\) is \(\sqrt{g^2+f^2 - c}\). Therefore all points which satisfy this equation are the same distance away from \((-g,-f)\), which shows they lie on a circle.

The circle has centre \((-g,-f)\) and radius \(\sqrt{g^2+f^2 - c}\).

We have explained why the points satisfying \[(x-a)^2+(y-b)^2=r^2\] lie on a circle with centre \((a,b)\) and radius \(r\); in this case, we had \(a=-g\), \(b=-f\) and \(r=\sqrt{g^2+f^2 - c}\).

In the next part of the question we can use this to quickly identify the centres and radii of the circles.

Call the first circle \(A\) and the second circle \(B\).

Circle \(A\): Using the form of the first part, \(g=-10\), \(f=-8\), \(c=128\). So \(A\) is a circle with centre \((10,8)\) and radius \(\sqrt{(-10)^2+(-8)^2-128}=\sqrt{36}=6\).

Circle \(B\): Divide the equation by \(4\) to give \[x^2+y^2+4x-6y-\frac{29}{4}=0\] which is of the same form as the first part. Then \(g=2\), \(f=-3\), \(c=-\dfrac{29}{4}\), so this is a circle with centre \((-2,3)\) and radius \(\sqrt{2^2+(-3)^2+\dfrac{29}{4}}=\sqrt{\dfrac{81}{4}}=\dfrac{9}{2}\).

The distance between the circles’ centres is, by Pythagoras’ theorem, \[\sqrt{\left(10 - (-2)\right)^2 + (8 - 3)^2} = \sqrt{169} = 13,\] but for there to be a point inside both circles, it would have to be a distance of less than \(6\) away from one centre and a distance of less than \(\dfrac{9}{2}\) from the other.

The sum of these distances, however, is only \(10.5\), less than the distance between the two centres themselves, so this cannot be.

So the circles lie entirely outside each other.

The points with the shortest distance between them are the points lying on the line joining the two centres.

To find the length of the shortest distance between the two circles consider the diagram below.

As calculated before, the length of the hypotenuse of the right-angled triangle in the diagram is \(13\).

Therefore the shortest distance between points on the two circles is \(13-\left(6+\dfrac{9}{2}\right)=\dfrac{5}{2}\).
