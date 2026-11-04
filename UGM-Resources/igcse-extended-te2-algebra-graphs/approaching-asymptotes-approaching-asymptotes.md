---
created: 2026-11-04T12:00:00 (UTC +06:00)
source: https://undergroundmathematics.org/thinking-about-functions/approaching-asymptotes
author: Underground Mathematics (University of Cambridge)
rights: © University of Cambridge (Underground Mathematics). Use inside SyllabAI is authorised by the
  operator attestation of 2026-10-23 — see LICENSE-DATA.md (Amendment 2026-10-23) in this repository.
  Takedown / correction handling as stated in LICENSE-DATA.md.
tags:
- underground-mathematics
- thinking-about-functions
- type/building-blocks
- level/introducing
resource_identity:
  ugm_id: approaching-asymptotes
  station: thinking-about-functions
  station_title: Thinking about Functions
  resource_type_id: 1
  resource_type_label: Building blocks
  level: Introducing
  ref: 6163
  old_site_id: F1_RT2_3
spec_map:
  curriculum_code: CIE-IGCSE-0580-2025
  lane: cie-igcse-maths-25-extended
  board: Cambridge CIE
  syllabus_version: 2025-2027
  subsection: thinking-about-functions
  subsection_provenance:
    tier: PROVIDER
    signal: source-url-slug
    slug: thinking-about-functions
    validation_status: SUGGESTED
  spec_points:
  - code: E2.11.3
    provenance:
      tier: AI_SUGGESTED
      confidence: medium
      model_version: GLM (Super Z agent, z.ai) — the 0580 igcse-extended TE2 cross-map (generalisation
        lane 19) (cross-map-0580-te2-algebra-graphs.json @ syllabai-experimental 79088f34)
      evidence: Algebra-free build-up of what asymptotes are, from y=1/x outward — the E2.11.3 register
        (vertical and horizontal asymptotes).
      rationale: 'Canonical UGM title: “Approaching asymptotes”'
      validation_status: SUGGESTED
  mapped_date: '2026-11-04'
  mapper: cross-map-0580-te2-algebra-graphs.json (P3c) @ syllabai-experimental 79088f34
  coverage_note: null
provenance:
  capture_date: '2026-10-22'
  capture_tool: P2 full-site crawl (ugm-crawl) → ugm-clean extraction; text-only import
  content_language: en
task: T-UGM-IMPORT-19
assets:
- path: https://undergroundmathematics.org/thinking-about-functions/approaching-asymptotes/images/oneoverxgraph.png
  kind: figure
- path: https://undergroundmathematics.org/thinking-about-functions/approaching-asymptotes/images/coolingtea.png
  kind: figure
- path: https://undergroundmathematics.org/thinking-about-functions/approaching-asymptotes/images/cuberoot.png
  kind: figure
- path: https://undergroundmathematics.org/thinking-about-functions/approaching-asymptotes/images/heavydamping.png
  kind: figure
- path: https://undergroundmathematics.org/thinking-about-functions/approaching-asymptotes/images/hyperbola.png
  kind: figure
- path: https://undergroundmathematics.org/thinking-about-functions/approaching-asymptotes/images/logx.png
  kind: figure
- path: https://undergroundmathematics.org/thinking-about-functions/approaching-asymptotes/images/normal.png
  kind: figure
- path: https://undergroundmathematics.org/thinking-about-functions/approaching-asymptotes/images/parabola.png
  kind: figure
- path: https://undergroundmathematics.org/thinking-about-functions/approaching-asymptotes/images/cuberootsquared.png
  kind: figure
- path: https://undergroundmathematics.org/thinking-about-functions/approaching-asymptotes/images/sqrtx.png
  kind: figure
- path: https://undergroundmathematics.org/thinking-about-functions/approaching-asymptotes/images/lightdamping.png
  kind: figure
- path: https://undergroundmathematics.org/thinking-about-functions/approaching-asymptotes/images/tanh.png
  kind: figure
- path: https://undergroundmathematics.org/thinking-about-functions/approaching-asymptotes/images/negativeoblique.png
  kind: figure
- path: https://undergroundmathematics.org/thinking-about-functions/approaching-asymptotes/images/tan.png
  kind: figure
- path: https://undergroundmathematics.org/thinking-about-functions/approaching-asymptotes/images/terminalvelocity.png
  kind: figure
- path: https://undergroundmathematics.org/thinking-about-functions/approaching-asymptotes/images/rationaloblique.png
  kind: figure
- path: https://undergroundmathematics.org/thinking-about-functions/approaching-asymptotes/images/funnel.png
  kind: figure
---

# Approaching asymptotes

> Excerpt: This algebra-free resource is designed to provoke discussion and help build up students’ sense of what asymptotes are.  This extends ideas beyond the classic example of $y=\tfrac{1}{x}$, which is used as a warm-up.

## Warm-up

This is a graph of \(y=\dfrac{1}{x}.\)

> [figure: A curve tending to the x-axis from above as x tends to negative infinity, and to the x-axis from below as x tends to positive infinity, and tending to negative infinity as x tends to 0 from the left, and tending to positive infinity as x tends to 0 from the right. — `https://undergroundmathematics.org/thinking-about-functions/approaching-asymptotes/images/oneoverxgraph.png`] (image not included in the text import; path of record).

The graph has two asymptotes.

How would you describe what an asymptote is?

## Descriptions and graphs

Here are some descriptions or statements about asymptotes.

1. “An asymptote is a line which a curve gets closer and closer to but doesn’t meet.”
2. “An asymptote is a line which a curve approaches as \(x\) tends to infinity.”
3. “A curve can’t cross an asymptote.”
4. “Asymptotes are parallel to the coordinate axes.”
5. “A graph can only have one asymptote parallel to each axis.”
6. “Asymptotes occur when a function isn’t defined for certain input values.”
7. “A function tends to positive infinity on one side of an asymptote and tends to negative infinity on the other side.”

Here are some examples of curves, some of which have asymptotes. Use these to help you decide whether you agree with the statements above.

> [figure: Downward sloping curve tending to a horizontal line as x tends to positive infinity. — `https://undergroundmathematics.org/thinking-about-functions/approaching-asymptotes/images/coolingtea.png`] (image not included in the text import; path of record).

> [figure: Graph of cube root x; an upward sloping curve tangent to and crossing the y-axis at the origin. — `https://undergroundmathematics.org/thinking-about-functions/approaching-asymptotes/images/cuberoot.png`] (image not included in the text import; path of record).

> [figure: Curve which crosses the x-axis but also tends to the x-axis as x tends to positive infinity. — `https://undergroundmathematics.org/thinking-about-functions/approaching-asymptotes/images/heavydamping.png`] (image not included in the text import; path of record).

> [figure: This curve has two asymptotes, one positively sloped and one negatively sloped both passing through the origin together forming a cross shape. The two components of the curve lie in the left and right sections of this cross shape. — `https://undergroundmathematics.org/thinking-about-functions/approaching-asymptotes/images/hyperbola.png`] (image not included in the text import; path of record).

> [figure: Curve of the logarithm function; an always increasing function with always decreasing slope which tends to negative infinity as x tends to 0 from the right. — `https://undergroundmathematics.org/thinking-about-functions/approaching-asymptotes/images/logx.png`] (image not included in the text import; path of record).

> [figure: A curve which has a maximum at x=0 and tends to the x-axis from above as x tends to both positive and negative infinitity. — `https://undergroundmathematics.org/thinking-about-functions/approaching-asymptotes/images/normal.png`] (image not included in the text import; path of record).

> [figure: Graph of the parabola x squared — `https://undergroundmathematics.org/thinking-about-functions/approaching-asymptotes/images/parabola.png`] (image not included in the text import; path of record).

> [figure: Curve which is a curvy v shape with vertex at the origin — `https://undergroundmathematics.org/thinking-about-functions/approaching-asymptotes/images/cuberootsquared.png`] (image not included in the text import; path of record).

> [figure: Graph of square root x, translated to the right — `https://undergroundmathematics.org/thinking-about-functions/approaching-asymptotes/images/sqrtx.png`] (image not included in the text import; path of record).

> [figure: Oscillating curve with decreasing amplitude that tends to 0 as x tends to positive infinity. — `https://undergroundmathematics.org/thinking-about-functions/approaching-asymptotes/images/lightdamping.png`] (image not included in the text import; path of record).

> [figure: Graph of tanh x; a curve tending to a horizontal line below the x-axis as x tends to negative infinity, passing through the origin, and tending to a horizontal line above the x-axis as x tends to positive infinity. — `https://undergroundmathematics.org/thinking-about-functions/approaching-asymptotes/images/tanh.png`] (image not included in the text import; path of record).

> [figure: Curve consisting of two components one in the second quadrant and one in the fourth. The curve tends to a negative sloping line as x tends to both positive and negative infinity and the curve tends to positive infinity and negative infinity as x tends to 0 from the left and right respectively. — `https://undergroundmathematics.org/thinking-about-functions/approaching-asymptotes/images/negativeoblique.png`] (image not included in the text import; path of record).

> [figure: Graph of tan x — `https://undergroundmathematics.org/thinking-about-functions/approaching-asymptotes/images/tan.png`] (image not included in the text import; path of record).

> [figure: Curve passing through the origin with positive slope and tending to a horizontal line above the x-axis as x tends to positive infinity. — `https://undergroundmathematics.org/thinking-about-functions/approaching-asymptotes/images/terminalvelocity.png`] (image not included in the text import; path of record).

> [figure: This curve has 3 components; one component is like the component of the graph of tan x which passes throught the origin, the other two components tend towards the line which is tangent to tan x at the origin, from above as x tends to negative infinity and from below as x tends to positive infinity. These components also tend towards vertical lines as they approach the tan x component — `https://undergroundmathematics.org/thinking-about-functions/approaching-asymptotes/images/rationaloblique.png`] (image not included in the text import; path of record).

> [figure: This curve has the shape of an upside down funnel; it tends towards a horizontal line from above as x tends to both positive and negative infinity, and at a particular value of x it tends to positive infinity from both the left and the right. — `https://undergroundmathematics.org/thinking-about-functions/approaching-asymptotes/images/funnel.png`] (image not included in the text import; path of record).

## Things you might have noticed

| Graph A This graph has one asymptote which is parallel to the \(x\)-axis. As \(x\) gets larger, the \(y\)-value decreases and the graph gets closer and closer to the asymptote but does not touch it. Part of this graph could model the temperature of a cup of tea as it cools over time. | > [figure: Downward sloping curve tending to a horizontal line as x tends to positive infinity. — `https://undergroundmathematics.org/thinking-about-functions/approaching-asymptotes/images/coolingteaasymp.png`] (image not included in the text import; path of record). |
| --- | --- |

| Graph B This graph does not have an asymptote. The curve gets steeper and closer to the \(y\)-axis as \(x\) gets closer to \(0\), but the \(y\)-axis is a vertical tangent to the curve at \((0,0)\) and is not an asymptote. | > [figure: Graph of cube root x; an upward sloping curve tangent to and crossing the y-axis at the origin. — `https://undergroundmathematics.org/thinking-about-functions/approaching-asymptotes/images/cuberoot.png`] (image not included in the text import; path of record). |
| --- | --- |

| Graph C The \(x\)-axis is an asymptote of this graph, even though the curve crosses the \(x\)-axis at some point. Part of this graph could model the displacement of a particle on the end of a stretched spring in a highly resistive fluid, such as oil. The particle initially moves quickly until the spring is actually compressed, but then moves slowly back towards the point where the spring is neither stretched nor compressed. This is described as heavy damping. | > [figure: Curve which crosses the x-axis but also tends to the x-axis as x tends to positive infinity. — `https://undergroundmathematics.org/thinking-about-functions/approaching-asymptotes/images/heavydamping.png`] (image not included in the text import; path of record). |
| --- | --- |

| Graph D This curve has two asymptotes, but neither is parallel to the coordinate axes. They are called ‘oblique’ asymptotes and the two branches of the curve get closer and closer to these as \(x\) gets further away from \(0\). This curve, a hyperbola, is one of the conic sections. These are curves produced by slicing a double cone at different angles. (Note that apart from where the curve crosses the \(x\)-axis, there are always two points on the curve with the same \(x\)-value, so this curve is not the graph of a function.) | > [figure: Curve consisting of two components which are mirror images of each other in the y-axis. Each component has the shape of a sideways parabola except that the curve appears to tend toward straight lines as x tends to positive and negative infinity. — `https://undergroundmathematics.org/thinking-about-functions/approaching-asymptotes/images/hyperbolaasymp.png`] (image not included in the text import; path of record). |
| --- | --- |

| Graph E The \(y\)-axis is a vertical asymptote and the graph gets closer to this as \(x\) gets closer to \(0\) from the positive side. This function is not defined for \(x=0\) or for negative values of \(x\). It may look as if the graph approaches an oblique asymptote (a line which is not parallel to the axes) as \(x\) gets larger, but this is not the case. Although the value of the function keeps increasing, the graph keeps getting flatter as \(x\) increases. This might suggest that the graph has a horizontal asymptote, but for any horizontal line that you could draw, this graph would actually pass through the line and keep rising as \(x\) increases. | > [figure: Curve of the logarithm function; an always increasing function with always decreasing slope which tends to negative infinity as x tends to 0 from the right. — `https://undergroundmathematics.org/thinking-about-functions/approaching-asymptotes/images/logx.png`] (image not included in the text import; path of record). |
| --- | --- |

Without more information, such as an equation for the graph, it can be difficult to judge whether a graph has an asymptote. This is one reason we use dotted lines to denote asymptotes on sketch graphs.

| Graph F The \(x\) axis is a horizontal asymptote for this graph. The function is defined and gives positive values for all values of \(x\), but as \(x\) gets further away from \(0\) the value of the function keeps decreasing and gets closer to \(0\). | > [figure: A curve which has a maximum at x=0 and tends to the x-axis from above as x tends to both positive and negative infinitity. — `https://undergroundmathematics.org/thinking-about-functions/approaching-asymptotes/images/normal.png`] (image not included in the text import; path of record). |
| --- | --- |

| Graph G This graph does not have any asymptotes, even though the curve gets closer and closer to the \(x\)-axis as \(x\) gets closer to \(0\) from the negative or positive sides. Since the curve meets the \(x\) axis at \((0,0)\) and is horizontal at \((0,0)\), the \(x\)-axis is actually a tangent to the curve, rather than an asymptote. | > [figure: Graph of the parabola x squared — `https://undergroundmathematics.org/thinking-about-functions/approaching-asymptotes/images/parabola.png`] (image not included in the text import; path of record). |
| --- | --- |

| Graph H This graph doesn’t have any asymptotes. The curve gets steeper and closer to the \(y\)-axis as \(x\) approaches \(0\) from the negative or positive sides, but the curve meets the \(y\)-axis at \((0,0)\) and does not descend further. This is an example of what’s called a ‘cusp’. | > [figure: Curve which is a curvy v shape with vertex at the origin — `https://undergroundmathematics.org/thinking-about-functions/approaching-asymptotes/images/cuberootsquared.png`] (image not included in the text import; path of record). |
| --- | --- |

| Graph I This graph doesn’t have any asymptotes. The function is only defined for values of \(x\) greater than a certain value, say for \(x\geq 3\). As \(x\) decreases to \(3\), the curve gets steeper and steeper. The line \(x=3\) is a vertical tangent to the curve at \((3,0)\) rather than an asymptote. | > [figure: Graph of square root x, translated to the right — `https://undergroundmathematics.org/thinking-about-functions/approaching-asymptotes/images/sqrtx.png`] (image not included in the text import; path of record). |
| --- | --- |

| Graph J Although this graph crosses the \(x\)-axis multiple times, the \(x\)-axis is an asymptote to the curve. This is because the curve gets arbitrarily close to the \(x\)-axis as \(x\) tends to infinity. That is, if you drew two horizontal lines, one above and one below the \(x\)-axis and as close as you liked to the \(x\)-axis, after some point the curve would be completely contained between these lines and would remain so as \(x\) continued to increase. Part of this graph could model the angle of oscillation of a pendulum over time if we took air resistance into account. | > [figure: Oscillating curve with decreasing amplitude that tends to 0 as x tends to positive infinity. — `https://undergroundmathematics.org/thinking-about-functions/approaching-asymptotes/images/lightdamping.png`] (image not included in the text import; path of record). |
| --- | --- |

| Graph K This graph has two asymptotes parallel to the \(x\)-axis. As \(x\) tends to infinity the value of the function keeps increasing, but does not go above a certain value. Similarly, as \(x\) tends to negative infinity, the value of the function keeps decreasing, but doesn’t fall below a certain value. | > [figure: Graph of tanh x; showing the two horizontal asymptotes which the curve lies between. — `https://undergroundmathematics.org/thinking-about-functions/approaching-asymptotes/images/tanhasymp.png`] (image not included in the text import; path of record). |
| --- | --- |

| Graph L This graph has two asymptotes. The \(y\)-axis is an asymptote because as \(x\) approaches \(0\) from the negative side, the function gets larger and larger, tending towards infinity, whereas when \(x\) approaches \(0\) from the positive side the value of the function tends towards negative infinity. There is also an oblique aymptote which the curve gets closer to as \(x\) gets further and further away from \(0\). | > [figure: Curve consisting of two components one in the second quadrant and one in the fourth. The curve tends to a negative sloping asymptote as x tends to both positive and negative infinity and the curve tends to positive infinity and negative infinity as x tends to 0 from the left and right respectively. — `https://undergroundmathematics.org/thinking-about-functions/approaching-asymptotes/images/negativeobliqueasymp.png`] (image not included in the text import; path of record). |
| --- | --- |

| Graph M This graph has several asymptotes parallel to the \(y\)-axis. For each of these asymptotes, the function approaches infinity on the left side of the asymptote and approaches negative infinity on the right side. | > [figure: Graph of tan x, showing the vertical asymptotes as dotted lines — `https://undergroundmathematics.org/thinking-about-functions/approaching-asymptotes/images/tanasymp.png`] (image not included in the text import; path of record). |
| --- | --- |

| Graph N This graph has one asymptote parallel to the \(x\)-axis. As \(x\) increases, the value of the function also increases, but it doesn’t go above a certain value. Part of this graph could model the velocity of an object falling from rest if we take air resistance into account. In this situation, the value that \(y\) approaches is often called the terminal velocity. | > [figure: Curve passing through the origin with positive slope and tending to a horizontal asymptote above the x-axis as x tends to positive infinity. — `https://undergroundmathematics.org/thinking-about-functions/approaching-asymptotes/images/terminalvelocityasymp.png`] (image not included in the text import; path of record). |
| --- | --- |

| Graph O This graph has two asymptotes parallel to the \(y\)-axis and on either side of these the value of the function tends to positive or negative infinity. The graph also has an oblique asymptote which the curve approaches as \(x\) gets further away from \(0\). The curve doesn’t cross the vertical asymptotes, but it does cross the oblique asymptote at \((0,0)\). | > [figure: This curve has 3 components; one component is like the component of the graph of tan x which passes throught the origin, the other two components tend towards the line which is tangent to tan x at the origin, from above as x tends to negative infinity and from below as x tends to positive infinity. These components also tend towards vertical lines as they approach the tan x component. These three asymptotes are marked. — `https://undergroundmathematics.org/thinking-about-functions/approaching-asymptotes/images/rationalobliqueasymp.png`] (image not included in the text import; path of record). |
| --- | --- |

| Graph P The curve approaches the asymptote parallel to the \(x\)-axis as \(x\) tends to positive infinity and as \(x\) tends to negative infinity. There is an asymptote parallel to the \(y\)-axis and on either side of this asymptote the value of the function tends to infinity. | > [figure: This curve has the shape of an upside down funnel; it tends towards a horizontal line from above as x tends to both positive and negative infinity, and at a particular value of x it tends to positive infinity from both the left and the right. The horizontal and vertical asymptote are marked as dotted lines. — `https://undergroundmathematics.org/thinking-about-functions/approaching-asymptotes/images/funnelasymp.png`] (image not included in the text import; path of record). |
| --- | --- |
