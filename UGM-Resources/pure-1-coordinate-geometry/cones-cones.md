---
created: 2026-10-23T02:04:16 (UTC +06:00)
source: https://undergroundmathematics.org/circles/cones
author: Underground Mathematics (University of Cambridge)
rights: © University of Cambridge (Underground Mathematics). Use inside SyllabAI is authorised by the operator attestation of 2026-10-23 — see LICENSE-DATA.md (Amendment 2026-10-23) in this repository. 
  Takedown / correction handling as stated in LICENSE-DATA.md.
tags:
- underground-mathematics
- circles
- type/building-blocks
- level/developing
resource_identity:
  ugm_id: cones
  station: circles
  station_title: Circles
  resource_type_id: 1
  resource_type_label: Building blocks
  level: Developing
  ref: 9266
  old_site_id: G4_RT2_1
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
  spec_points: []
  mapped_date: '2026-10-23'
  mapper: cross-map-coordinate-geometry.json (P3c lane 3) @ syllabai-experimental cb947595
  coverage_note: 'no CIE P1 spec point asserted — resource remains in the corpus unmapped (AGENT.md rule 3: coverage is never manufactured)'
provenance:
  capture_date: '2026-10-22'
  capture_tool: P2 full-site crawl (ugm-crawl) → ugm-clean extraction; text-only import
  content_language: en
task: T-UGM-IMPORT-3
assets:
- path: https://undergroundmathematics.org/circles/cones/download/teacher-notes.pdf
  kind: printable
---

# Cones

> Excerpt: This resource poses a straight-forward question about the volume of part of a cone, and provides a structured approach to solving the problem in a number of different ways.

## Problem

You may have used sports “cones” like these at school:

The mathematical name for a truncated cone such as this is a *[frustum of a cone](https://undergroundmathematics.org/glossary/frustum-of-a-cone)*.

What volume of plastic is needed to make such a “cone”?

## Solution

Our chosen approach is to begin by finding the surface area of the frustum.

Once we have done this, if we know the thickness of the plastic, then a good estimate of the volume would be the surface area multiplied by the thickness. (This does not give the exact volume, but the error will be small in comparison to the error in measuring the thickness of the plastic.)

Therefore, to get a decent estimate of the volume of the “cone”, get a sports “cone”, measure various lengths, and use these to work out the surface area. Then estimate or measure the thickness and use these to work out the volume.

So let us return to the question of working out the surface area.

The images in the suggestions proposed thinking about a whole cone or about cutting the frustum open.

Throughout this solution, we’ve chosen to use algebra rather than actual measurements from a real “cone”. We will then put in our measurements at the end to arrive at a final numerical answer.

Why might we have done this?

Some suggestions

- It allows us to compare our algebra with someone else’s algebra

- It allows us to see how changes in different measurements (or inaccuracies in them) will affect the final answer

- It allows us to work out the surface area and volume of different sizes of frustums and “cones” without repeating the work

We begin by drawing a sketch of the frustum within a complete cone, as in the suggestion, and indicating a variety of lengths and angles on it.

With an actual sports “cone”, we can easily find \(r\) and \(R\) (by measuring the diameters and halving them) and \(s\) (by direct measurement). With a bit of effort, we can measure \(h\) (by holding a straight edge vertically and seeing where the top of the “cone” lies on it). None of the other lengths or angles are easy to measure directly, so we will have to work them out from \(r\), \(R\) and \(s\) (or possibly \(h\)) as needed.

Here are two different routes to finding the surface area, based on the two ideas in the suggestions.

Route 1: Thinking of the frustum as a cone with top sliced off

As in the suggestion and the above sketch, we can extend the sloping surface upwards to create a complete cone.

We can then find the surface area of the complete cone and subtract the surface area of the small cone to find the area of the frustum.

The [Appendix](https://undergroundmathematics.org/circles/cones/appendix) to this resource discusses some formulae for finding the surface area of a cone, which we will make use of here.

The surface area of the whole cone is

\(\pi RL\)

, while the surface area of the small cone is

\(\pi rl\)

. Therefore the surface area

\(A\)

of the frustum is

\[\begin{equation} A=\pi RL-\pi rl=\pi(RL-rl).\label{eq:area1} \end{equation}\]

This is good, but we still have to find \(L\) and \(l\) in terms of \(r\), \(R\) and \(s\).

Looking at the diagram, we see that we have two similar right-angled triangles with one vertex at the

apex

of the cone. We can use these to find that:

\[\begin{equation} \frac{L}{R}=\frac{l}{r}.\label{eq:ratio1} \end{equation}\]

We would like to combine these together to obtain a formula for the area in terms of

\(R\)

,

\(r\)

and

\(s\)

. To do this, we will also need to use a formula for

\(s\)

:

\[\begin{equation} s=L-l,\label{eq:s1} \end{equation}\]

which is obvious from the above diagram.

Route 2: Unwrapping the frustum

If we cut a cone open, we get a sector of a circle. If we do the same with a frustum, we get the shaded region in the following diagram, which is a sector of an [annulus](https://undergroundmathematics.org/glossary/annulus).

The outer arc is the unwrapped base of the frustum, so has length \(2\pi R\), while the inner arc is the unwrapped top of the frustum, so has length \(2\pi r\).

The radius of the inner circle is the slant length of the upper part of the cone (which is cut off to make the frustum), and similarly for the radius of the outer circle, giving the lengths as shown. We also let \(\phi\) be the angle of the sector.

Then using the formula for area of a sector (“\(A=\frac12 r^2\theta\)”), we see that the curved surface area of the frustum, which is the shaded area, is \[A=\tfrac{1}{2}L^2\phi-\tfrac{1}{2}l^2\phi.\]

We need to eliminate \(\phi\), as we cannot measure this angle on the physical “cone”. We can use the formula for arc length (“\(l=r\theta\)”) to find \(\phi\), as we know the length of the outer and inner arcs. So we obtain \[2\pi r=l\phi\quad\text{and}\quad 2\pi R=L\phi.\]

This gives

\(\phi=\frac{2\pi r}{l}=\frac{2\pi R}{L}\)

, and so we also get the useful incidental result that

\[\begin{equation} \frac{r}{l}=\frac{R}{L}.\label{eq:ratio2} \end{equation}\]

(We could also have deduced this by using similar triangles as in the first route, or by noting that the inner and outer sectors in the unwrapped frustum are similar.)

Now, substituting our formulae for

\(\phi\)

into our formula for the shaded area gives:

\[\begin{align*} A&=\tfrac{1}{2}L^2\phi-\tfrac{1}{2}l^2\phi\\ &=\tfrac{1}{2}L^2.\tfrac{2\pi R}{L}-\tfrac{1}{2}l^2.\tfrac{2\pi r}{l}\\ &=\pi LR-\pi lr \end{align*}\]

so that

\[\begin{equation} A=\pi RL-\pi rl=\pi(RL-rl).\label{eq:area2} \end{equation}\]

We would like to combine this together with

\(\eqref{eq:ratio2}\)

to obtain a formula for the area in terms of

\(R\)

,

\(r\)

and

\(s\)

. To do this, we will also need to use a formula for

\(s\)

:

\[\begin{equation} s=L-l,\label{eq:s2} \end{equation}\]

which is obvious from the first diagram above.

Finishing the algebra – both routes

We have equation \(\eqref{eq:area1}\) or \(\eqref{eq:area2}\) for the area \(A\) in terms of \(R\), \(r\), \(L\) and \(l\), and we will need to use equations \(\eqref{eq:ratio1}\) and \(\eqref{eq:s1}\) or \(\eqref{eq:ratio2}\) and \(\eqref{eq:s2}\) to obtain a formula for \(A\) in terms of \(R\), \(r\) and \(s\).

One approach is to rearrange equation \(\eqref{eq:ratio1}\) or \(\eqref{eq:ratio2}\) to obtain \(l\) in terms of \(r\), \(R\) and \(s\), and then to substitute this into \(\eqref{eq:s1}\) or \(\eqref{eq:s2}\) and rearrange to obtain an expression for \(L\) in terms of \(r\), \(R\) and \(s\). We could then use \(\eqref{eq:ratio1}\) or \(\eqref{eq:ratio2}\) again to obtain a similar formula for \(l\). Substituting these into our formula for \(A\) will give us the answer we seek.

But there is a nicer approach, though it is not that obvious.

Equation

\(\eqref{eq:area1}\)

(or

\(\eqref{eq:area2}\)

) reads

\[A=\pi(RL-rl),\]

relating

\(RL\)

and

\(rl\)

, while equation

\(\eqref{eq:ratio1}\)

, which reads

\(\frac{L}{R}=\frac{l}{r}\)

, can be rearranged to get

\[\begin{equation} rL=Rl.\label{eq:ratio3} \end{equation}\]

(Equation \(\eqref{eq:ratio2}\) can be rearranged to give this same result.)

It would have been lovely if this equation had related \(RL\) and \(rl\), which are what we are interested in, but unfortunately it does not.

However, the terms do have the same “shape”: they all involve \(R\) or \(r\) multiplied by \(L\) or \(l\). This might make us think of quadratic expressions of the form \[(R\pm r)(L\pm l).\] Since we want to end up with \(RL-rl\) for the area formula, we need one positive sign and one negative sign. Furthermore, as we know that \(s=L-l\) (equation \(\eqref{eq:s1}\) or \(\eqref{eq:s2}\)), we’ll go for \[(R+r)(L-l)=RL+rL-Rl-rl.\] The middle two terms cancel each other out by equation \(\eqref{eq:ratio3}\), so this equation simplifies to \[(R+r)s=RL-rl.\]

Therefore we get our desired formula:

\[\begin{equation} A=\pi(R+r)s.\label{eq:area3} \end{equation}\]

Finally, if we want to write our answer in terms of \(h\) instead of \(s\), we can use Pythagoras’s Theorem to get \(s^2=(R-r)^2+h^2\), giving us \(A=\pi(R+r)\sqrt{(R-r)^2+h^2}\). The other version certainly looks simpler!

An interesting observation

This answer can also be written as \(A=2\pi\bigl(\frac{R+r}{2}\bigr)s\), which is the curved surface area of a cylinder with radius \(\frac{R+r}{2}\) (the average of the top and bottom radii of the frustum) and height \(s\).

This sounds like it might be interesting, if we can figure out what it means. Can you see why this should be the case?

This problem can also be answered using Pappus's Second Theorem; see [Pappus's Theorems](/) to find out more.

The answer we obtained was in terms of \(R\), \(r\) and \(s\). It might also be useful also to have an answer in terms of \(\theta\) but not \(s\). How can we rewrite it?

Rewriting the answer

Looking at the sketch of the frustum at the start of this solution, we see that we can write \(h=s\cos\theta\) and \(R-r=s\sin\theta\). Therefore we can rewrite \(\eqref{eq:area3}\) in two different ways to get

\[A=\frac{\pi(R+r)h}{\cos\theta}=\pi(R+r)h\sec\theta\] and \[A=\frac{\pi(R+r)(R-r)}{\sin\theta}= \frac{\pi(R^2-r^2)}{\sin\theta}= \pi(R^2-r^2)\cosec\theta.\]

How can we check that our answer is sensible?

Methods of checking our answer

1. *Try special values.* We know the slanted surface area of a complete cone from the [Appendix](https://undergroundmathematics.org/circles/cones/appendix), so if we put \(r=0\), we should get the same answer. And sure enough, when we do so, we get \(\pi(R+0)s=\pi Rs\) as expected. Another special case is if \(R\) and \(r\) are almost the same and the slant is almost vertical, so the that the frustum looks more like a cylinder. In that case, \(s\approx h\) and \(R\approx r\), so the area is approximately \(\pi(r+r)h=2\pi rh\). This is the surface area of a cylinder, which is another good check.

---

1. *Check the dimensions.* Again, we are looking for an area, which has [dimension](https://undergroundmathematics.org/glossary/dimensional-analysis) \([\mathrm{L}^2]\). The right hand side is \(\pi\), which is dimensionless, times \(R+r\), which is the sum of two lengths, so is a length, times \(s\), which is a length, giving dimension \([\mathrm{L}]\times[\mathrm{L}]=[\mathrm{L}^2]\) as we require.

---

1. *Put some numbers in and consider whether the answer is realistic.* A frustum with a small slant and small top radius (\(r\)) should have an area a bit less than a square which surrounds the base of the cone. Put in some numbers and see whether this is the case.

Numerical calculations

We measured a real “cone” and obtained the following measurements:

- base diameter: \(\quantity{19.1}{cm}\) (outer rim), \(\quantity{18.7}{cm}\) (inner rim), so base radius: \(\quantity{9.55}{cm}\) (outer rim), \(\quantity{9.35}{cm}\) (inner rim)

- top diameter between \(\quantity{6.0}{cm}\) and \(\quantity{6.3}{cm}\) – it was not exactly circular – so top radius approximately \(\quantity{3.1}{cm}\)

- slant length: \(\quantity{8.4}{cm}\)

So the surface area is approximately \(\pi(9.45+3.15)\times \quantity{8.4}{cm^2}=\quantity{331}{cm^2}\). The base width is \(\quantity{0.2}{cm}\) (the difference between the outer and inner rim base radii: the “cone” sits on a flat edge at its base). This sketch shows the base of the “cone” and part of the sloping side, and shows how we can estimate the thickness from the base:

We see that \(\text{thickness}=\text{base}\times\cos\theta\), so we need to work out \(\theta\). We see from the earlier diagram that \(R-r=s\sin\theta\), so our figures give, approximately, \(9.45-3.1=8.4\sin\theta\), so \(\theta\approx49^\circ\). Thus the thickness is approximately \(\quantity{0.2}{cm}\times\cos49^\circ=\quantity{0.13}{cm}\).

Thus the volume is approximately \(\quantity{331}{cm^2}\times \quantity{0.13}{cm}\approx\quantity{40}{cm^3}\) to 1 significant figure. The most difficult part of the measurement was measuring or estimating the thickness of the “cone”, and even our final answer may be quite inaccurate if it turns out that the actual thickness is \(\quantity{0.16}{cm}\) or \(\quantity{0.10}{cm}\), say. We may have done better to use calipers to measure the thickness, instead of trying to calculate it using the base width and trigonometry. We were also not helped by the “cone” turning out to be not exactly the shape we first thought it was, but this is probably much less significant.

If we think now of some of the other possible approaches, it seems that approaches (3) or (4) would be much more accurate. But at least we have worked out how to find the surface area of a frustum along the way!

## Appendix

This appendix reviews various formulae for finding the curved surface area and volume of a cone.

**Surface area of a cone**

Here’s a diagram of a cone. We’ve drawn some lengths and an angle on it.

When we cut the (slanted) surface of the cone in a straight line from the vertex to the base and then unwrap it, we end up with a sector of a circle, like this:

The radius of this sector is the slant length of the cone, which is \(l\). The outer arc of the sector was the circumference of the base circle of the cone, so its length is \(2\pi r\).

Now the circumference of the whole of this circle is \(2\pi l\), and therefore the sector is a fraction \(\dfrac{2\pi r}{2\pi l}\) of the whole circle. The area of the sector, and hence of the slanted surface of the cone, is therefore \[\dfrac{2\pi r}{2\pi l}\times \pi l^2=\pi rl.\]

Alternatively, we could have worked out \(\phi\) first, using the formula for the arc length of a sector “\(l=r\theta\)”, giving in this case \(2\pi r=l\phi\), so \(\phi=\frac{2\pi r}{l}\). Then the area of the sector is given by the formula “\(A=\frac12 r^2\theta\)”, so calculating \(\frac12 l^2 .\frac{2\pi r}{l}=\pi rl\) gives us the area as before.

It’s always good to check that our answers are sensible before going too far in a problem!

How could we do this here?

Ways of checking our answer

Here are a few things that we can do to check that our answer is sensible.

1. *Try special values.* What values could we put in to our variables that would give us something we can check? In this case, if we make our cone very “flat”, so the vertex is barely above the base, the cone will look very much like a circular disk of radius \(r\). Then the slant length \(l\) will be almost the same as \(r\), and the answer our formula gives us, \(\pi rs\) will be almost the same as \(\pi rr=\pi r^2\), which is the area of a circular disk of radius \(r\). This gives us some confidence that our answer is reasonable.

---

1. *Check the dimensions.* The formula we have come up with, \(A=\pi rl\) (where \(A\) is the sloping surface area), must have correct dimensions to stand any chance of being correct. The left hand side is an area, measured in \(\quantity{}{m^2}\), so we say it has dimension \([\mathrm{L}^2]\), where \([\mathrm{L}]\) means a length. The right hand side is \(\pi\), a pure number (so dimensionless), times \(r\), which is a length, times \(l\), which is a length. So it has dimension \([\mathrm{L}]\times[\mathrm{L}]=[\mathrm{L}^2]\). So the dimensions of the left and right hand sides agree, giving us confidence that our answer is at least plausible.

Sometimes we will know some measurements more readily than others. So we could try rewriting this answer using other variables.

Since \(l^2=r^2+h^2\) using Pythagoras, we could also write the surface area as \(\pi r\sqrt{r^2+h^2}\) or \(\pi l\sqrt{l^2-h^2}\) if we wish.

If we draw a cross-section of the cone, we see that we have a right-angled triangle:

From this diagram, we see that \(h=l\cos\theta\) and \(r=l\sin\theta\), so we can substitute for \(l\) in our earlier answer \(\pi rl\) to find that we can also write the surface area as \[\pi rl=\frac{\pi rh}{\cos\theta}=\frac{\pi r^2}{\sin\theta}.\]

Using the reciprocal trigonometric functions, we could also write these as \(A=\pi rh\sec\theta=\pi r^2\cosec\theta\).

**Volume of a cone**

The area of the base of the cone is \(\pi r^2\). The volume of any pyramidal shape is given by \[\tfrac13\times\text{base area}\times\text{perpendicular height}\] so in this case, the volume is \(\frac13\pi r^2h\). This result can be proved using calculus.
