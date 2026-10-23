---
created: 2026-10-24T01:49:53 (UTC +06:00)
source: https://undergroundmathematics.org/introducing-calculus/serpentine-lake
author: Underground Mathematics (University of Cambridge)
rights: © University of Cambridge (Underground Mathematics). Use inside SyllabAI is authorised by the
  operator attestation of 2026-10-23 — see LICENSE-DATA.md (Amendment 2026-10-23) in this repository.
  Takedown / correction handling as stated in LICENSE-DATA.md.
tags:
- underground-mathematics
- introducing-calculus
- type/building-blocks
- level/introducing
resource_identity:
  ugm_id: serpentine-lake
  station: introducing-calculus
  station_title: Introducing Calculus
  resource_type_id: 1
  resource_type_label: Building blocks
  level: Introducing
  ref: 8785
  old_site_id: C1_RT2_4
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
  exam_reference: ', None'
task: T-UGM-IMPORT-7
assets:
- path: https://undergroundmathematics.org/introducing-calculus/serpentine-lake/download/teacher-notes.pdf
  kind: printable
---

# Is the Serpentine Lake really 40 acres?

> Excerpt: A ‘practical’ example to introduce the approximation of area using trapezia and the trapezium rule. It is claimed that the area of the Serpentine Lake is $40$ acres. Students are asked to test this claim by using a map of the lake and coordinates.

## Problem

Here is a map showing the Serpentine Lake in London. It is claimed that the Serpentine covers an area of \(40\) acres. How can you test this claim?

**Getting started**

For a start, there is a question about what is meant by the “Serpentine Lake” in the claim. Technically the Serpentine is only the part to the east of the bridge. The other part of the lake is called the Long Water. How can we decide whether the claim is talking about the whole lake, or just the part to the east of the bridge?

Suggestion 1

Use a rectangle to approximate the part of the lake to the east of the bridge.

Suggestion 2

What is the scale on the map?

How big is an acre?

Which part of the lake do we mean?

We can approximate the part of the lake to the east of the bridge as a rectangle. Using the scale on the map, the rectangle is approximately \(\quantity{850}{m}\) by \(\quantity{150}{m}\) or \(\quantity{127\,500}{m^2}.\) An acre is approximately \(\quantity{4047}{m^2}\), so the area of the part of the lake which is to the east of the bridge is only about \(32\) acres. Therefore we can assume that the \(40\) acre claim is about the whole lake.

## Approximating the area

Here is a map showing the Serpentine Lake in London. It is claimed that the Serpentine covers an area of \(40\) acres. How can you test this?

In the warm-up we were able to approximate part of the lake using a rectangle. This was a good enough estimate to show that the claim is talking about the area of the whole lake, but might not be good enough to check whether \(40\) acres is a reasonable estimate. Here are some things we can do to find the approximate area of the lake and test the claim.

**Simplify the shape**

One problem is that the lake has a curved boundary. However, we can approximate the shape of the lake by joining up points on the boundary using straight-line segments. We can then use several triangles or quadrilaterals to approximate the area of the shape.

**Use coordinates**

To avoid lots of measurements, we can draw axes on the map and use the coordinates of the points on the boundary in our calculations.

**Look at the shape differently**

As suggested above, to find the area of the lake we could split the shape up into smaller shapes, but this could involve lots of calculations to find the area of irregular shapes. We can think of the boundary of the lake as having an upper part (formed by joining points A,B,…,G and marked in blue on the diagram above) and a lower part (formed by joining points P,Q,…,U,G and marked in red). To find the area between the upper and lower parts of the boundary we could find the area between the blue boundary and the \(x\)-axis and subtract the area between the red boundary and the \(x\)-axis.

Viewing the region we want as a difference between two other regions may seem to make the problem more complicated, but it actually makes it simpler. Can you think of other situations in mathematics where you have made a problem simpler by writing something as a difference of two things you can work out?

**Splitting up the shapes**

We’ve approximated the boundaries using straight line segments, so we can slice the regions into trapezia such as those shown.

- Why is it helpful to split the region we want into trapezia?

- How do the coordinates of the points on the boundary help?

**Is the area of the Serpentine really \(40\) acres?**

We have provided a copy of the map with the axes drawn on it. Use the ideas discussed here to decide whether \(40\) acres is a good estimate for the lake size. How could you develop these ideas to find a systematic way to approximate the area of irregular shapes like this.

- Does it matter if the trapezia have different widths?

- What happens if the trapezia all have the same width?

- What happens if the blue and red points occur in pairs with the same \(x\)-coordinates?

- How will the number of trapezia affect the approximation?

## Things you might have noticed

Can you explain why the following equation will give us the area of the region covered by the two trapezia in this diagram?

\[\text{area} = (2.0-0.8) \times \dfrac{5.0+3.0}{2}+ (4.4-2.0)\times \dfrac{3.0+2.0}{2}\]

We can extend this idea to find the area of the entire region between the \(x\)-axis and the top (blue) boundary, formed by joining the points A,B,…,G, and use this to find the area of the lake.

Calculating the area of the Serpentine

Using the coordinates of the points A,B,…,G in the diagrams above, we can compute the area of the region between the blue boundary and the \(x\)-axis. We’ll call this the ‘blue area’.

\[\begin{align*} \text{blue area}&= 0.4\left(\dfrac{6.5+6.5}{2}\right)+0.4\left(\dfrac{6.5+5.0}{2}\right)+1.2\left(\dfrac{5.0+3.0}{2}\right)\\ & \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad+2.4\left(\dfrac{3.0+2.0}{2}\right)+3.9\left(\dfrac{2.0+2.0}{2}\right)+2.3\left(\dfrac{2.0+1.2}{2}\right)\\ &=27.18 \end{align*}\]

We can do the same using points P,Q,…U,G to find the region between the lower (red) boundary and the \(x\)-axis. We’ll call this the ‘red area’, and use both areas (blue and red) to find the area of the lake. Note that this will be the area in terms of square units on the graph, rather than acres.

\[\begin{align*} \text{red area}&= 1.5\left(\dfrac{5.1+2.3}{2}\right)+2.6\left(\dfrac{2.3+1.0}{2}\right)+2.9\left(\dfrac{1.0+0.6}{2}\right)\\ & \quad \quad \quad \quad \quad \quad +2.3\left(\dfrac{0.6+0.0}{2}\right)+0.9\left(\dfrac{0.0+0.0}{2}\right)+0.4\left(\dfrac{0.0+1.2}{2}\right)\\ &=13.09 \end{align*}\]

Therefore the area of the region between the blue area and the red area (our approximation for the lake) is \(14.09\) square units. Using the scale on the map (\(1\) unit \(= \quantity{100}{m}\)) we can convert this into acres (\(1\) acre \(\approx \quantity{4047}{m^2}\)). Calculating the area of the lake this way gives us \(34.8\) acres.

Does this answer suggest that the \(40\) acre claim is reasonable?

**Streamlining the calculations**

In the previous calculations we had to work out the area of each trapezium separately, but you may have noticed that the lengths of the parallel sides of most of the trapezia occur twice in the equations. For example, \(3.0\) occurs twice in the equation which gives the blue area. It would be nice to exploit this in some way.

How might the calculations have been different if the points on the boundary had been chosen in this way?

Suggestion

In the first calculation the length of the shared side of the two trapezia is multiplied by the widths of the two trapezia. What would happen if you had three trapezia instead? By arranging the points along the lake boundary so that their \(x\)-coordinates are evenly spaced, all the trapezia have the same width and this width is a common factor of each term in the expression for the whole area.

We’ll look in more detail at how the choice of points affects the calculation of the area between the blue boundary and the \(x\)-axis.

\[\begin{align*} \text{blue area}&= 2\left(\dfrac{6.5+3.2}{2}\right)+2\left(\dfrac{3.2+2.1}{2}\right)+2\left(\dfrac{2.1+2.0}{2}\right)\\ & \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad+2\left(\dfrac{2.0+2.0}{2}\right)+2\left(\dfrac{2.0+1.5}{2}\right)\\ &=\dfrac{2}{2} \Big( 6.5+3.2+3.2+2.1+2.1+2.0+2.0+2.0+2.0+1.5 \Big)\\ &=\dfrac{2}{2}\Big( 6.5+2(3.2+2.1+2.0+2.0)+1.5\Big) \end{align*}\]

You may be wondering why this equation hasn’t been simplified further. If you’re trying to generalise, it can be helpful not to simplify expressions too much before looking at them carefully.

For example, there are lots of terms in these calculations and there are lots of \(2\)s.

- Can you explain where each of \(2\)s in the equation comes from?

- Which parts of the equation would change if the trapezia were of width 3?

- How many trapezia have we used and how many points have we drawn on the lake boundary?

The choice of evenly spaced coordinates allows us to streamline the calculations for finding the blue area and the red areas. In this particular problem we actually want to find the area between the blue and the red boundaries. How could you combine the information from the coordinates of the red and blue points into a single calculation?

The choice of evenly spaced points with the same \(x\)-coordinates means that we can choose between calulating the red and blue areas separately or combining the coordinates into a single calculation.

What could be the advantages or disadvantages of the two approaches?

## Area under a curve

Some of the ideas in the Serpentine example can be used to find the area between a curve and the \(x\)-axis. They can also be used to find the area between curves. The result for the area between a curve and the \(x\)-axis, called the trapezium rule, is illustrated below.

In this graph the points are spread out evenly, so that the \(x\)-coordinates increase by \(h\) each time. By approximating the area under the graph using trapezia, we have \[\text{Area between graph and $x$-axis}\approx \dfrac{h}{2}\Big(y_{0}+2(y_{1}+y_{2}+ y_{3}+y_{4}+y_{5})+y_{6}\Big)\]

What would the formula be if we had \(n+1\) evenly spaced points?

How could the formula be written if we knew we had the graph of a function, \(f(x)\)?
