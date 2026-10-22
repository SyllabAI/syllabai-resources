---
created: 2026-10-23T02:04:16 (UTC +06:00)
source: https://undergroundmathematics.org/circles/cutting-spheres
author: Underground Mathematics (University of Cambridge)
rights: © University of Cambridge (Underground Mathematics). Use inside SyllabAI is authorised by the operator attestation of 2026-10-23 — see LICENSE-DATA.md (Amendment 2026-10-23) in this repository. 
  Takedown / correction handling as stated in LICENSE-DATA.md.
tags:
- underground-mathematics
- circles
- type/food-for-thought
- level/developing
resource_identity:
  ugm_id: cutting-spheres
  station: circles
  station_title: Circles
  resource_type_id: 9
  resource_type_label: Food for thought
  level: Developing
  ref: 7101
  old_site_id: G4_RT12_3
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
- path: https://undergroundmathematics.org/circles/cutting-spheres/download/teacher-notes.pdf
  kind: printable
---

# Cutting spheres

## Problem

The sphere in the diagram has radius \(r\) and is cut by two parallel planes distance \(h\) apart.

One of these planes is at a distance \(x\) from the “north pole” of the sphere, as shown in the diagram.

What is the surface area of the part of the sphere lying between these two parallel planes?

## Suggestion

Perhaps we could try to find some exact or *approximate* answers in certain special cases to get us started – that might give us some insight into the problem. What values could we pick for \(h\) and/or \(x\) which would make the problem either simpler, or allow us to give a reasonable approximate answer?

Suggestion 1

You could consider the case \(x=0\). What values of \(h\) would be straightforward in this case?

Suggestion 2 (part a)

You could consider the case where \(h\) is very small indeed. What does the part of the sphere between the planes look like in this case? Can you work out the area (approximately) in this case? The next box gives a further suggestion for how to do this.

Suggestion 2 (part b)

Does this remind you of the [Cones](https://undergroundmathematics.org/circles/cones) problem?

Suggestion 2 (part c)

Once you’ve done this, can you solve the main problem by chopping up the part of the sphere between the planes in a helpful way?

## Solution

The suggestion proposed considering special cases, so that’s what we’ll do.

One special case we could consider is when \(x=0\). If \(h=r\), then we have a hemisphere. You may have learnt that the surface area of a sphere is \(4\pi r^2\), so the answer in this case is \(2\pi r^2\). Likewise, we can consider the most extreme cases: when \(h=2r\), we get an area of \(4\pi r^2\) (the entire sphere), and when \(h=0\), we get zero area.

So if we do manage to get a general formula, we will be able to check it in these special cases.

Another possible idea when \(x=0\) is to consider what happens when \(h\) is very small. In this case, the surface area looks a lot like a circle, but the radius of the circle does not seem particularly easy to work out, so maybe we’ll leave this one for a moment. (There are things we can do to approximate the radius using more advanced techniques, but they are currently beyond us.)

Another thing we could consider is the situation where \(h\) is *very small*. Then the part of the sphere between the planes looks very much like the frustum of a cone, and we know how to find the (surface) area of such a shape – see [Cones](https://undergroundmathematics.org/circles/cones).

If we recall our answer from that problem, we find the formulae for the surface area \[\pi(R+r)s=\frac{\pi(R+r)h}{\cos\theta}= \frac{\pi(R^2-r^2)}{\sin\theta}.\] Here, \(R\) is the radius of the base of the frustum, \(r\) is the radius of the top, \(h\) is the perpendicular height, \(s\) is the slant length and \(\theta\) is the angle the slant makes with the vertical.

Confusingly, that problem also used an \(r\) (to mean the radius of the top of the frustum), but our problem uses \(r\) to mean the radius of the sphere. So we’re going to have to be very careful when using the formula here to avoid getting confused.

Let’s draw a thin slice of our sphere to see which of these values are easy to work out.

The perpendicular height of this frustum is just \(h\), the thickness of our slice.

The radii of both the base and top of this frustum are about \(r\cos\varphi\), as can be seen from the diagram; the difference between the two radii is tiny.

The slant length \(s\) is a little harder to work out, but the slant angle is easier to see from the diagram. Because the slant of the slice is perpendicular to the radius of the sphere meeting it, the slant is at an angle of \(\varphi\) to the vertical:

So now we have everything we need to work out the surface area of this frustum. We’ll use the formula \(\dfrac{\pi(R+r)h}{\cos\theta}\).

We don’t know \(s\), so we can’t use \(\pi(R+r)s\) directly. We also don’t know \(R\) and \(r\) accurately enough to be able to work out \(R^2-r^2\), so we can’t use the third formula.

Substituting in our values: both radii are \(r\cos\varphi\), the perpendicular height is \(h\) and the angle the slant makes with the vertical is \(\varphi\), so the area is \[\dfrac{\pi(r\cos\varphi+r\cos\varphi)h}{\cos\varphi}=2\pi rh.\]

This is a real surprise! The answer does not depend on \(\varphi\) (or equivalently, \(x\)) at all! And it is the same as the surface area of a cylinder also of radius \(r\) and height \(h\).

So when \(h\) is really small, the area of the strip of the sphere is about \(2\pi rh\). The smaller we make \(h\), the more accurate this estimate becomes, as the slice will look more and more like a frustum of a cone.

We are now in a position to solve the main problem. We have a section of the sphere with height \(h\). If we slice it into \(n\) slices, each with height \(h/n\), then the surface area of each one will be about \(2\pi rh/n\), so in total, the area will be about \[n\times 2\pi rh/n=2\pi rh.\]

If we take more slices, our frustum-of-a-cone-shaped slices will become closer and closer to the actual shape of the sphere, so our approximation will become more and more accurate.

So the area of the section of the sphere really is \(2\pi rh\). This is the same as the surface area of a cylinder of the same radius as the sphere and height \(h\).

We can check this with our special cases: if \(h=r\), then this formula gives \(2\pi r^2\), and if \(h=2r\), we get \(4\pi r^2\).

## Taking it further...

What about the two-dimensional analogue of this problem? That is, we take the original problem and change every “sphere” into “circle”, every “plane” into “line”, and ask about lengths instead of areas, as follows:

The circle in the diagram has radius \(r\) and is cut by two parallel lines distance \(h\) apart.

One of these lines is at a distance \(x\) from the “top” of the circle, as shown.

What is the length of the parts of the circle lying between these two parallel lines?

How does this question compare to and contrast with the original sphere problem?

## Background

[Archimedes](http://www-groups.dcs.st-and.ac.uk/~history/Biographies/Archimedes.html) was the first person to determine the surface area of a sphere, which he wrote in a work called *On the sphere and cylinder* in the 3rd century BCE.

The fact that the area of a sphere is equal to the area of the cylinder surrounding the sphere led to the creation of a variety of area-preserving world maps, such as the [Lambert](http://www-history.mcs.st-and.ac.uk/Biographies/Lambert.html) Projection (1772). In general, these are known as cylindrical equal-area projections. In these maps, equal areas on the Earth’s surface correspond to equal areas on the map.

Here is a modern example of such a map:

(Image taken from [Wikimedia Commons](http://en.wikipedia.org/wiki/File:Lambert_cylindrical_equal-area_projection_SW.jpg), copyright Strebe 2011, licensed under the [Creative Commons Attribution-Share Alike 3.0 Unported license](http://creativecommons.org/licenses/by-sa/3.0/deed.en).)

What interesting things do you notice about the world when it is mapped in this way?
