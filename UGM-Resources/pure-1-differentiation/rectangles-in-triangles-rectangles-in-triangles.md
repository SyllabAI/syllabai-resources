---
created: 2026-10-24T01:49:53 (UTC +06:00)
source: https://undergroundmathematics.org/introducing-calculus/rectangles-in-triangles
author: Underground Mathematics (University of Cambridge)
rights: © University of Cambridge (Underground Mathematics). Use inside SyllabAI is authorised by the
  operator attestation of 2026-10-23 — see LICENSE-DATA.md (Amendment 2026-10-23) in this repository.
  Takedown / correction handling as stated in LICENSE-DATA.md.
tags:
- underground-mathematics
- introducing-calculus
- type/many-ways-problem
- level/developing
resource_identity:
  ugm_id: rectangles-in-triangles
  station: introducing-calculus
  station_title: Introducing Calculus
  resource_type_id: 4
  resource_type_label: Many ways problem
  level: Developing
  ref: 6214
  old_site_id: C1_RT6_2
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
  spec_points: []
  coverage_note: 'no CIE P1 spec point asserted — resource remains in the corpus unmapped (AGENT.md
    rule 3: coverage is never manufactured)'
  mapped_date: '2026-10-24'
  mapper: cross-map-differentiation.json (P3c lane 7) @ syllabai-experimental 93575e69
provenance:
  capture_date: '2026-10-22'
  capture_tool: P2 full-site crawl (ugm-crawl) → ugm-clean extraction; text-only import
  content_language: en
task: T-UGM-IMPORT-7
assets:
- path: https://undergroundmathematics.org/introducing-calculus/rectangles-in-triangles/download/teacher-notes.pdf
  kind: printable
---

# Rectangles in triangles

> Excerpt: This is a maximising problem that students are expected to tackle without calculus. Ideally students should be allowed the time to explore their own chosen approach before comparing its efficiency and accuracy to those of others.

## Problem

What is the greatest area of a rectangle inscribed in a given right-angled triangle?

Consider this situation, where \(C\) is a vertex of both the rectangle and the triangle.

Suggestion

If the horizontal length of the rectangle is labelled \(x\), what is the vertical length of the rectangle in terms of \(x\) and side lengths \(a\) and \(b\)?

Next step

Consider this situation, where one edge of the rectangle lies on the line \(AB\).

- How does your approach to each situation compare?

- How does the area of the rectangle identified in each situation compare?

## Solution

What is the greatest area of a rectangle inscribed inside a given right-angled triangle?

Consider this situation, where C is a vertex of both the rectangle and the triangle.

This problem can be tackled in many ways, some of which are more effective than others.

We might consider an algebraic approach.

Step 1

**Consider a specific case.**

Let’s say that for simplicity I choose to consider a \(3\), \(4\), \(5\) right-angled triangle. If I set the width of the rectangle to be \(1\), how would I calculate the area of the resulting rectangle?

Well, if \(DE=1\) then length \(AF=2\) and if I notice that triangle \(AEF\) is similar to triangle \(ABC\) then I can calculate the linear scale factor of enlargement.

The linear scale factor is calculated as the ratio of corresponding lengths in the two similar triangles. In this case I want to consider going from the larger triangle \(ABC\) to the smaller triangle \(AEF\) so I have

\[\text{Linear scale factor}= \frac{AF}{AC} = \frac{2}{3}.\]

I can now calculate length \(EF\) as \[\frac{2}{3} \times 4 = \frac{8}{3}.\]

So the area of this particular rectangle is \[1 \times \frac{8}{3} = \frac{8}{3}.\]

I have successfully calculated the area of one particular rectangle inscribed inside my \(3\), \(4\), \(5\) right-angled triangle. However, I still need to answer the bigger question: What is the greatest area of a rectangle inscribed inside a right-angled triangle?

To do this I will need to now move towards a more general case.

Step 2

**Moving towards a more general case.**

Applying the method used for my specific case to a general rectangle of horizontal length \(x\) inscribed inside a \(3\), \(4\), \(5\) right-angled triangle, the linear scale factor will be given by \(\dfrac{3-x}{3}\).

The area of rectangle \(CDEF\) will now be given by

\[\begin{equation} 4x\left(\frac{3-x}{3}\right) = \frac{4}{3}x(3-x)\label{eq:1} \end{equation}\]

I can now see that I am dealing with a quadratic expression. This will look like a parabola with, in this case, a maximum point. If I can sketch the parabola then I may be able to locate the \(x\)-coordinate of the maximum, which corresponds to the horizontal length of the rectangle with maximum area.

I can see that the maximum area will occur when \(x=\dfrac{3}{2}\) (I am exploiting the vertical symmetry property of the parabola) and I can now substitute this into \(\eqref{eq:1}\) to identify the maximum area as \[\frac{4}{3}x(3-x) = \frac{12}{6}\left(\frac{3}{2}\right) = 3.\]

Notice that this is exactly half the area of the original \(3\), \(4\), \(5\) triangle!

I wonder if this is true in general for any right-angled triangle?

Step 3

**A general case**

Applying the same method as before but to a right-angled triangle of side lengths \(a\), \(b\), \(c\), I see that the linear scale factor is \[\frac{b-x}{b}.\]

Using this I can now identify the length of the vertical side of the rectangle as \[a\left(\frac{b-x}{b}\right)\] and therefore the area is given by \[ax\left(\frac{b-x}{b}\right) = \frac{a}{b}x(b - x).\]

Sketching the graph of this expression as before I can see that the rectangle of maximum area occurs when \(x=\dfrac{b}{2}\). Substituting this into the general formula for the area I find that \[\textrm{Maximum area} = \frac{a}{b}\left(\frac{b}{2}\right)\left(b - \frac{b}{2}\right) = \frac{a}{2}\left(\frac{b}{2}\right) = \frac{ab}{4}.\]

The area of the original triangle \(ABC\) is given by \(\dfrac{ab}{2}\).

Therefore it is the case that if a rectangle is inscribed inside a right-angled triangle in this way, its greatest area will be exactly half that of the triangle.

One of the first things we must do when taking an algebraic approach is to decide which length in the diagram to consider as our variable. The suggestion in the main problem page suggested that we choose the horizontal length of the rectangle, \(x\). However, we could just have easily chosen the vertical length of the rectangle. We may have even chosen to work with one of the other lengths in the diagram.

So how do we know which will be the best choice of variable? We might assume that it will make no difference to the final result but does it make a difference to the journey? Will one choice of variable be ‘easier’ to work with than another?

Additional thinking

In this particular scenario, because the sides of the rectangle are each parallel to a side of the original triangle, selecting the length or width of the rectangle as our variable will in fact lead to a symmetrical chain of reasoning, an equivalent amount of work required to reach a solution.

If however, we choose to vary a length along the hypotenuse, say from point B to the top right-hand vertex of the rectangle, then we might expect some extra ‘journey time’ in order to identify the length and width of the rectangle and hence the area.

Sometimes it is hard to predict which choice of variable will be ‘best’. It is often with hindsight and experience of the problem that we can see an alternative, potentially more effective, approach.

Alternatively we might consider a possible geometric approach.

Step 1

**Suppose \(x<\frac{b}{2}\).**

Folding along the line \(EF\) we have this:

By showing that triangles \(GDE\) and \(BDE\) are congruent we can see that the area outside of the red rectangle is greater (by triangle \(A'CG\)) than the area inside of it. Therefore the area of the red rectangle is less than half of the area of the triangle \(ABC\).

Step 2

**Suppose \(x=\frac{b}{2}\).**

Folding along the line \(EF\) we have this:

By showing that this splits the original triangle \(ABC\) into four smaller, congruent triangles we can see that the area outside of the red rectangle is equal to the area inside of it. Therefore as \(x\) increases to \(\dfrac{b}{2}\) the area of the red rectangle increases to half of the area of the triangle \(ABC\).

Step 3

**Suppose \(x>\frac{b}{2}\).**

Folding along the line \(DE\) we have this:

By showing that triangles \(AEF\) and \(HEF\) are congruent we can see that the area outside of the red rectangle is greater (by triangle \(B'CH\)) than the area inside of it. Therefore the area of the red rectangle is, once again, less than half of the area of triangle \(ABC\).

**Conclusion**

By considering each of these three cases we have shown that the red rectangle will have a maximum area equal to half that of the original triangle \(ABC\). This will occur when the horizontal length of the rectangle, \(x=\frac{b}{2}\).

You might like to reconsider your approach to this problem after exploring some of the ideas at [Calculus of Powers](https://undergroundmathematics.org/calculus-of-powers).

## Next step solution

It would seem sensible to attempt to approach this using methods similar to those used in the first problem.

As before, one of the first things needed in an algebraic approach is to identify the length of the rectangle that lies on the line \(AB\) in terms of \(y\) and the side lengths of the triangle \(a\), \(b\), \(c\).

As before, one of the first things we must do is decide which length in the diagram to consider as our variable. In the original scenario it seemed sensible to select one of the sides of the rectangle to vary.

So which will be the best choice of variable this time? Why might we choose to label length \(y\)?

In the previous situation I used similar triangles to identify the missing lengths. By considering the interior angles of each of the smaller white triangles (\(GFA\), \(CEF\), and \(BDE\)) I can show that all are in fact similar to triangle \(ABC\).

If I now consider triangle \(DBE\) I can calculate the linear scale factor from this to triangle \(ABC\) as \[\frac{BE}{BA} = \frac{y}{c}\] and therefore the length \(ED=\dfrac{by}{c}\).

Now I consider triangle \(FEC\). Length \(EC=a-y\) and so the linear scale factor from this triangle to triangle \(ABC\) is given by \[\frac{EC}{BC} = \frac{a-y}{a}.\] Length \(EF\) can now be written as \(\dfrac{c(a-y)}{a}\).

The area of the blue rectangle can now be expressed as \[\left(\frac{by}{c}\right)\left(\frac{c(a-y)}{a}\right) = \frac{by(a-y)}{a} = \left(\frac{b}{a}\right)(ay-y^2).\]

Once again I am dealing with a quadratic equation that has a maximum point that can be located by sketching the graph.

The maximum value occurs when \(y=\dfrac{a}{2}\) which corresponds to a maximum area of \(\dfrac{ab}{4}\).

Notice that once again it is the case that if a rectangle is inscribed inside a right-angled triangle in this way, its greatest area will be exactly half that of the triangle.

The algebraic approach is not the only valid method. Often we use algebra as part of our first attempt to solve a problem, but it may be beneficial to think about other approaches first. We can also consider a geometric approach here. Can you construct a similar folding argument to the one that was used in the first problem?
