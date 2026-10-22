---
created: 2026-10-23T02:04:16 (UTC +06:00)
source: https://undergroundmathematics.org/geometry-of-equations/the-circle-of-apollonius-coordinate-edition
author: Underground Mathematics (University of Cambridge)
rights: © University of Cambridge (Underground Mathematics). Use inside SyllabAI is authorised by the operator attestation of 2026-10-23 — see LICENSE-DATA.md (Amendment 2026-10-23) in this repository. 
  Takedown / correction handling as stated in LICENSE-DATA.md.
tags:
- underground-mathematics
- geometry-of-equations
- type/many-ways-problem
- level/developing
resource_identity:
  ugm_id: the-circle-of-apollonius-coordinate-edition
  station: geometry-of-equations
  station_title: Geometry of Equations
  resource_type_id: 4
  resource_type_label: Many ways problem
  level: Developing
  ref: 7968
  old_site_id: G2_RT6_3
spec_map:
  curriculum_code: CIE-9709-P1-2023
  lane: cie-a-level-maths-20-pure-1
  board: Cambridge CIE
  syllabus_version: 2023-2025
  subsection: geometry-of-equations
  subsection_provenance:
    tier: PROVIDER
    signal: source-url-slug
    slug: geometry-of-equations
    validation_status: SUGGESTED
  spec_points:
  - code: 1.3.2
    provenance:
      tier: AI_SUGGESTED
      confidence: high
      model_version: GLM (Super Z agent, z.ai) — P3c lane-3 cross-map (cross-map-coordinate-geometry.json (P3c lane 3) @
        syllabai-experimental cb947595)
      evidence: 'Apollonius circle PA/PB=lambda derived by coordinates — the distance-ratio locus family generalised. Pattern exemplar.'
      rationale: 'Canonical UGM title: “The circle of Apollonius... coordinate edition”'
      validation_status: SUGGESTED
    title: interpret and use any of the forms y = mx + c , y – y = m ( x – x ) , ax + by + c = 0 in solving
  mapped_date: '2026-10-23'
  mapper: cross-map-coordinate-geometry.json (P3c lane 3) @ syllabai-experimental cb947595
provenance:
  capture_date: '2026-10-22'
  capture_tool: P2 full-site crawl (ugm-crawl) → ugm-clean extraction; text-only import
  content_language: en
task: T-UGM-IMPORT-3
interactive:
- src: https://www.geogebratube.org/material/iframe/id/UwzKjXjC/width/587/height/502/border/888888/rc/false/ai/false/sdz/false/smb/false/stb/false/stbh/false/ld/false/sri/true/asb/false/at/html5
  kind: geogebra-iframe
assets:
- path: https://undergroundmathematics.org/geometry-of-equations/the-circle-of-apollonius-coordinate-edition/download/teacher-notes.pdf
  kind: printable
---

# The circle of Apollonius... coordinate edition

> Excerpt: Coordinate geometry is used to explore and solve an ancient geometry problem involving loci.

## Problem 1

Two fixed points \(A\) and \(B\) lie in the plane, and the distance between them is \(AB=2a\), where \(a>0\).

A point \(P\) moves in the plane so that the ratio of its distances from \(A\) and \(B\) is constant: \[\frac{PA}{PB}=\lambda,\] where \(\lambda>0\).

1. Can you sketch the locus of the point \(P\) for different values of \(\lambda\)?

---

1. Using [Cartesian coordinates](https://undergroundmathematics.org/glossary/cartesian-coordinates), work out (the equation of) the locus of \(P\). Suggestion You may find it more straightforward to first work with specific values of \(a\) and \(\lambda\), say \(a=2\) and \(\lambda=3\).

## Suggestion 1

Two fixed points \(A\) and \(B\) lie in the plane, and the distance between them is \(AB=2a\), where \(a>0\).

A point \(P\) moves in the plane so that the ratio of its distances from \(A\) and \(B\) is constant: \[\frac{PA}{PB}=\lambda,\] where \(\lambda>0\).

1. Can you sketch the locus of the point \(P\) for different values of \(\lambda\)? You might find it helpful to fix the value of \(a\), say \(a=2\). Here are some values of \(\lambda\) you might consider: \(\lambda=1\) \(\lambda=3\) \(\lambda=\frac{1}{3}\) If you choose to draw things on a coordinate grid, it might make things simpler if you place \(A\) and \(B\) at convenient locations.

---

1. Using [Cartesian coordinates](https://undergroundmathematics.org/glossary/cartesian-coordinates), work out (the equation of) the locus of \(P\). You may find it more straightforward to first work with specific values of \(a\) and \(\lambda\), say \(a=2\) and \(\lambda=3\). The question has not specified the coordinates of the points \(A\) or \(B\), so what options do we have? In particular, what would be “nice” coordinates to choose for the points \(A\) and \(B\)? If we let \(P\) be at \((x,y)\), how can we work out the distances \(PA\) and \(PB\) (in terms of \(x\) and \(y\)) once we have specified the coordinates of \(A\) and \(B\)?

## Solution 1

Two fixed points \(A\) and \(B\) lie in the plane, and the distance between them is \(AB=2a\), where \(a>0\).

A point \(P\) moves in the plane so that the ratio of its distances from \(A\) and \(B\) is constant: \[\frac{PA}{PB}=\lambda,\] where \(\lambda>0\).

1. Can you sketch the locus of the point \(P\) for different values of \(\lambda\)? Here are some values of \(\lambda\) you might consider: \(\lambda=1\) \(\lambda=3\) \(\lambda=\frac{1}{3}\) This GeoGebra applet shows the locus of \(P\). The points \(A\) and \(B\) are movable, and the value of \(\lambda\) can be adjusted using the slider. You can use this applet to check your sketches for the cases \(\lambda=1\), \(\lambda=3\) and \(\lambda=\frac{1}{3}\). > [interactive embed (geogebra-iframe): https://www.geogebratube.org/material/iframe/id/UwzKjXjC/width/587/height/502/border/888888/rc/false/ai/false/sdz/false/smb/false/stb/false/stbh/false/ld/false/sri/true/asb/false/at/html5] — not part of the text import; see the source page. [Download GeoGebra file](https://www.geogebratube.org/material/download/format/file/id/UwzKjXjC) You may have noticed that the loci for the cases \(\lambda=3\) and \(\lambda=\frac{1}{3}\) look essentially the same as each other, just reflected. Why should this be the case? Reason If we write out the equations for these two loci, we see: \[\frac{PA}{PB}=3\quad\text{and}\quad \frac{PA}{PB}=\frac{1}{3}.\] If we now take the reciprocal of the second equation, these become \[\frac{PA}{PB}=3\quad\text{and}\quad \frac{PB}{PA}=3.\] The equations are identical, except that \(A\) and \(B\) have swapped roles. So the loci are identical except for swapping \(A\) and \(B\), which can be achieved by reflecting in the perpendicular bisector of \(AB\). We’d like to show that the locus really *is* a circle, which brings us to question 2.

---

1. Using Cartesian coordinates, work out (the equation of) the locus of \(P\). You may find it more straightforward to first work with specific values of \(a\) and \(\lambda\), say \(a=2\) and \(\lambda=3\). Suggestion: The question has not specified the coordinates of the points \(A\) or \(B\), so what options do we have? In particular, what would be “nice” coordinates to choose for the points \(A\) and \(B\)? As we are going to be using coordinates in this problem, and are looking for the locus of \(P\), we will let \(P\) have coordinates \((x,y)\). We could let \(A\) be at \((q,r)\) and \(B\) be at \((s,t)\), for example. However, this is likely to make our algebra very messy, having so many letters around. A better approach is to choose “nice” coordinates for \(A\) and \(B\). Let’s take \(A\) to be at the origin, and \(B\) to be on the \(x\)-axis. This way, \(A=(0,0)\) and \(B=(2a,0)\), and most of the coordinates involved are zero. Another good choice would be \(A=(-a,0)\) and \(B=(a,0)\), so that the points are symmetrically placed about the origin. We will go with the first option in this solution, but you might like to have a go with this alternative choice and compare them. We let \(P\) have the coordinates \((x,y)\), and then apply Pythagoras to find \[PA=\sqrt{x^2 + y^2}\ \text{and}\ PB=\sqrt{(x-2a)^2 + y^2},\] as seen in this sketch: > [figure: Triangle A, B, P with the lengths of its sides. — `https://undergroundmathematics.org/geometry-of-equations/the-circle-of-apollonius-coordinate-edition/images/distances.png`] (image not included in the text import; path of record). Using these, we then see that \[\begin{equation} \label{eq:1} \frac{PA}{PB}=\frac{\sqrt{x^2 + y^2}}{\sqrt{(x-2a)^2 + y^2}} = \lambda. \end{equation}\] We will give the rest of the solution first for the specific example suggested, \(a=2\) and \(\lambda=3\), and then for the general case. A specific example We rewrite \(\eqref{eq:1}\) with \(a=2\) and \(\lambda=3\), giving \[\begin{equation}\label{eq:frac1} \frac{\sqrt{x^2 + y^2}}{\sqrt{(x-4)^2 + y^2}} = 3. \end{equation}\] If we now square this to get rid of the square roots, we get \[\frac{x^2 + y^2}{(x-4)^2 + y^2} = 9.\] We can multiply through to lose the fractions, obtaining: \[x^2 + y^2 = 9 \bigl((x-4)^2 + y^2\bigr).\] It now makes sense to expand the inner brackets, giving \[x^2 + y^2 = 9 (x^2-8x+16 + y^2).\] We can then rearrange this to collect all of the terms on one side, giving \[8x^2+8y^2-72x+144 = 0,\] which can be divided by \(8\) to give \[\begin{equation}\label{eq:circ1} x^2+y^2-9x+18 = 0. \end{equation}\] This is the equation of a circle, so we’ve achieved what we set out to do after question 1! We also observe that every step of this argument can be reversed, so if the point \((x,y)\) lies on the circle, which means that it satisfies \(\eqref{eq:circ1}\), it will also satisfy \(\eqref{eq:frac1}\). (Note too that \((4,0)\) does not satisfy \(\eqref{eq:circ1}\), so there is no problem of dividing by zero in \(\eqref{eq:frac1}\) when working backwards.) To find the centre and radius of the circle, we complete the square to get \[\bigl(x-\tfrac{9}{2}\bigr)^2-\bigl(\tfrac{9}{2}\bigr)^2+y^2+18=0,\] so \[\bigl(x-\tfrac{9}{2}\bigr)^2+y^2=\tfrac{9}{4}.\] Therefore the locus is a circle with centre at \(\bigl(\tfrac{9}{2},0\bigr)\) and radius \(\tfrac{3}{2}\). The general case To do the general case, we do exactly the same as in the specific example, we simply use \(a\) in place of \(2\) and \(\lambda\) in place of \(3\). So we again begin with \(\eqref{eq:1}\), square it and multiply through to get \[x^2 + y^2 = \lambda^2 \bigl((x-2a)^2 + y^2\bigr).\] We then expand and rearrange to find \[\begin{equation} \label{eq:2} (\lambda^2-1)(x^2+y^2)-4\lambda^2 ax + 4\lambda^2 a^2 = 0. \end{equation}\] If \(\lambda^2-1\ne0\), that is, \(\lambda\ne1\) (as \(\lambda>0\)), we can divide by \(\lambda^2-1\) to get \[x^2+y^2-\frac{4\lambda^2 ax}{\lambda^2-1} + \frac{4\lambda^2 a^2}{\lambda^2-1} = 0.\] This is the equation of a circle. As in the specific example above, the argument can be reversed, and so every point on the circle satisfies the original condition. To find the centre and radius of the circle, we now complete the square to get \[\begin{align*} \left(x-\frac{2\lambda^2 a}{\lambda^2-1}\right)^2+y^2 &=\frac{4\lambda^4 a^2}{(\lambda^2-1)^2}- \frac{4\lambda^2 a^2}{\lambda^2-1}\\ &=\frac{4\lambda^2 a^2}{(\lambda^2-1)^2}. \end{align*}\] Thus the locus is a circle with centre \(\left(\dfrac{2\lambda^2 a} {\lambda^2-1}, 0\right)\) and radius \(\dfrac{2\lambda a} {|\lambda^2-1|}\). Do check that this gives the same answer as we had above in the case \(a=2\) and \(\lambda=3\)! We need the absolute value in the formula for the radius to handle the case \(0<\lambda<1\): try substituting in \(a=2\) and \(\lambda=\frac{1}{3}\) to see why. If \(\lambda>1\), then \(B\) lies within the circle, whereas if \(\lambda<1\), then \(A\) lies within the circle, as shown in the applet above. (You might like to try showing this is the case from the algebra.) The only remaining case is when \(\lambda=1\), where we know that the answer is a straight line. We can obtain this from the algebra: when \(\lambda=1\), equation \(\eqref{eq:2}\) becomes \[-4ax + 4a^2 = 0.\] Dividing by \(4a\) (which is not zero) gives \(-x+a=0\) or equivalently \(x=a\): this is the perpendicular bisector of \(AB\). This makes sense, because the case \(\lambda=1\) gives \(PA=PB\), and the locus of all points equidistant from \(A\) and \(B\) is their perpendicular bisector. You might like to consider what happens as \(\lambda\) tends to zero or infinity, or when \(\lambda\) tends to \(1\). How does the algebra relate to what you have seen in the applet? If you did try this question with coordinates such as \((q,r)\) for \(A\) and \((s,t)\) for \(B\), you will have found that the algebra was very messy indeed. It is always worth asking oneself what options one has when choosing coordinates: a good choice can have huge advantages. In this situation, we were free to choose both the origin and the orientation of the axes, so we were able to choose useful ones.

The locus of \(P\) is known as the *circle of Apollonius*. See the [Historical background](https://undergroundmathematics.org/geometry-of-equations/the-circle-of-apollonius-coordinate-edition/historical-background) for this problem to read more about Apollonius and this circle.

A further question to consider: Can we go backwards?

In other words, if we begin with a specified circle, is it always possible to find two points \(A\) and \(B\) and a value \(\lambda>0\) so that the given circle is the locus of the point \(P\) satisfying \(PA/PB=\lambda\)?

If it is possible, is there any choice in how we can choose \(A\), \(B\) and \(\lambda\)?

## Problem 2

Following on from problem 1, we have two fixed points \(A\) and \(B\) in the plane with \(AB=2a\), where \(a>0\).

A point \(P\) moves in the plane so that \[\frac{PA}{PB}=\lambda,\] where \(\lambda>0\).

We shall now assume that \(\lambda\ne1\), so that the locus of \(P\) is a circle.

What is the length of the tangent to this circle from the mid-point of \(AB\), that is, the length \(MN\) in the applet below?

What is the locus of \(N\) as \(\lambda\) varies?

*If you have not already done so, you will first need to find the radius and centre of the circle traced by \(P\).*

(In this applet, \(\lambda\) may be adjusted and the point \(N\) will be traced if you click the button. \(C\) is the centre of the circle that \(P\) describes.)

[Download GeoGebra file](https://www.geogebratube.org/material/download/format/file/id/CgGjPQ9f)

The locus of \(P\) is known as the *circle of Apollonius*. See the [Historical background](https://undergroundmathematics.org/geometry-of-equations/the-circle-of-apollonius-coordinate-edition/historical-background) for this problem to read more about Apollonius and this circle.

## Solution 2

The radius and centre of the circle were found in the [solution to problem 1](https://undergroundmathematics.org/geometry-of-equations/the-circle-of-apollonius-coordinate-edition/solution-1).

This image shows the situation described in the case \(\lambda=2\), where a coordinate system has been imposed and the line \(CN\) has been drawn in.

Incidentally, there are actually two tangents from \(M\) to the circle, but their lengths are equal. (Can you prove this?) We have only drawn one of them.

We note first that the tangent at \(N\) is perpendicular to the radius at \(N\), so the triangle \(CMN\) is right-angled. We can therefore use Pythagoras’s Theorem: \[CM^2=CN^2+MN^2.\]

Since we know the coordinates of \(C\) from the first part of the problem and \(M\) is the midpoint of \(AB\), we can easily work out the length \(CM\). The length \(CN\) is the known radius of the circle, and so we can deduce the length \(CM\).

We use the nice coordinates approach from the first solution to perform our calculations: \(A\) is at \((0,0)\) and \(B\) is \((2a,0)\), as in the diagram above. Then \(C\) is \(\left(\dfrac{2\lambda^2 a}{\lambda^2-1}, 0\right)\) and the circle has radius \(\dfrac{2\lambda a} {|\lambda^2-1|}\).

The midpoint

\(M\)

has coordinates

\((a,0)\)

, so

\[\begin{align*} MN^2&=CM^2-CN^2\\ &=\left(\frac{2\lambda^2 a}{\lambda^2-1}-a\right)^2- \left(\frac{2\lambda a} {|\lambda^2-1|}\right)^2\\ &=\left(\frac{(\lambda^2+1)a}{\lambda^2-1}\right)^2- \left(\frac{2\lambda a}{\lambda^2-1}\right)^2\\ &=\frac{(\lambda^4+2\lambda^2+1)a^2-4\lambda^2a^2}{(\lambda^2-1)^2}\\ &=\frac{(\lambda^4-2\lambda^2+1)a^2}{(\lambda^2-1)^2}\\ &=a^2. \end{align*}\]

Therefore \(MN=a\), which is \(\frac{1}{2}AB\), independent of the choice of \(\lambda\)!

What is the locus of \(N\) as \(\lambda\) varies?

As \(MN=a\) is a constant and \(M\) is fixed, it follows that the locus of \(N\) as \(\lambda\) varies is (part of) the circle with diameter \(AB\), which is very pretty.

Which parts of this circle are included in the locus of \(N\) as \(\lambda\) varies? Are there any parts which are not?

## Historical background

[Apollonius of Perga](http://www-groups.dcs.st-and.ac.uk/~history/Biographies/Apollonius.html) was a famous Greek geometer (262 BCE – 190 BCE), who studied [conics](https://undergroundmathematics.org/glossary/conic) intensively, and invented the terms [parabola](https://undergroundmathematics.org/glossary/parabola), [ellipse](https://undergroundmathematics.org/glossary/ellipse) and [hyperbola](https://undergroundmathematics.org/glossary/hyperbola) still in common use today. Among other things, he invented the parabolic mirror.

Regarding this “Circle of Apollonius”, Heath1 writes:

“This locus was discussed by Apollonius in his *Plane Loci*, Book II, as we know from Pappus…

But the construction was not discovered by Apollonius; it belongs to a much earlier date, since it appears in exactly the same form in [Aristotle](http://www-groups.dcs.st-and.ac.uk/~history/Biographies/Aristotle.html), *Meteorologica* III. 5, 376 a 3 sqq."

1. Heath, Thomas L., *Euclid: The thirteen books of the elements*, 2nd. ed, Cambridge 1926 (reprinted by Dover, 1956), vol. 2, pp. 198–200.↩
