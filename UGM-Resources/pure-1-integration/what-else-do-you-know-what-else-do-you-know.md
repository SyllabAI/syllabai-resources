---
created: 2026-10-24T04:45:46 (UTC +06:00)
source: https://undergroundmathematics.org/calculus-meets-functions/what-else-do-you-know
author: Underground Mathematics (University of Cambridge)
rights: © University of Cambridge (Underground Mathematics). Use inside SyllabAI is authorised by the
  operator attestation of 2026-10-23 — see LICENSE-DATA.md (Amendment 2026-10-23) in this repository.
  Takedown / correction handling as stated in LICENSE-DATA.md.
tags:
- underground-mathematics
- calculus-meets-functions
- type/food-for-thought
resource_identity:
  ugm_id: what-else-do-you-know
  station: calculus-meets-functions
  station_title: Calculus meets Functions
  resource_type_id: 9
  resource_type_label: Food for thought
  level: Developing
  ref: 8489
  old_site_id: C3_RT12_2
spec_map:
  curriculum_code: CIE-9709-P1-2023
  lane: cie-a-level-maths-20-pure-1
  board: Cambridge CIE
  syllabus_version: 2023-2025
  subsection: calculus-meets-functions
  subsection_provenance:
    tier: PROVIDER
    signal: source-url-slug
    slug: calculus-meets-functions
    validation_status: SUGGESTED
  spec_points:
  - code: 1.8.3
    provenance:
      tier: AI_SUGGESTED
      confidence: medium
      model_version: "GLM (Super Z agent, z.ai) — P3c lane-8 cross-map (cross-map-integration.json (P3c lane 8) @ syllabai-experimental c04abfbd)"
      evidence: "from an area datum, evaluates definite integrals of f+5, f(x+2) and -f over shifted intervals — linearity and translation properties of the definite integral (the lane-7 routing recorded the 1.8 bearing)"
      rationale: "Canonical UGM title: \"What else do you know?\""
      validation_status: SUGGESTED
    title: "evaluate definite integrals"
  mapped_date: '2026-10-24'
  mapper: cross-map-integration.json (P3c lane 8) @ syllabai-experimental c04abfbd
provenance:
  capture_date: '2026-10-22'
  capture_tool: P2 full-site crawl (ugm-crawl) → ugm-clean extraction; text-only import
  content_language: en
task: T-UGM-IMPORT-8
---

# What else do you know?

> Excerpt: Students are given the area under an unknown curve in a specified region and asked to consider what they can deduce about a selection of integrals involving transformations of the original function.

## Problem

If you know that the area of the shaded region is 40 square units, which of the following can you evaluate?

- \(\int_2^6 (f(x) + 5) \ dx\)

- \(\int_2^6 (f(x) - 3) \ dx\)

- \(\int_0^4 f(x + 2) \ dx\)

- \(\int_2^6 f(x + 2) \ dx\)

- \(\int_4^8 f(x + 2) \ dx\)

- \(\int_2^6 -f(x) \ dx\)

- \(\int_2^6 f(-x) \ dx\)

If there are any that you cannot evaluate, what additional information would you need in order to do so?

Can you find the value of the constant \(k\) for which

\[\int_2^6 (f(x) + k) \ dx = 0\]

How does your thinking change if instead you start with this image, in which the shaded area is 8 square units?

Which of the integrals above can you evaluate for the [linear function](https://undergroundmathematics.org/glossary/linear-function) \(g(x)\)?

- How does this compare to your answer for \(f(x)\)?

- What makes this function different from \(f(x)\)?

- What else do you know about \(g(x)\)?

## Solution part 1

A summary of the integrals and their values is provided below:

| Integral | Value |
|---|---|
| \(\int_2^6 (f(x) + 5) \ dx\) | \(60\) |
| \(\int_2^6 (f(x) - 3) \ dx\) | \(28\) |
| \(\int_0^4 f(x + 2) \ dx\) | \(40\) |
| \(\int_2^6 f(x + 2) \ dx\) | ? |
| \(\int_4^8 f(x + 2) \ dx\) | ? |
| \(\int_2^6 -f(x) \ dx\) | \(-40\) |
| \(\int_2^6 f(-x) \ dx\) | ? |

We can consider each in turn to understand how these values can be calculated.

\(\int_2^6 (f(x) + 5) \ dx\)

\(f(x) + 5\) represents a vertical translation of the original function by \(5\) units ‘upwards’. In the following diagram the light blue ‘portion’ still represents 40 square units. The darker blue rectangle represents the additional area which can be calculated as \(5 \times 4\).

The sum of these two ‘portions’ gives us the value of the integral \(\int_2^6 (f(x) + 5) \ dx\).

Notice that if we had thought algebraically we might have considered the integral as a sum of two functions, leading us to re-write it as \[\int_2^6 (f(x) + 5) \ dx = \int_2^6 f(x) \ dx + \int_2^6 5 \ dx.\]

This of course produces the same result: the sum of the original area, \(\int_2^6 f(x) \ dx = 40\), and the rectangle, \(\int_2^6 5 \ dx = 20\).

\(\int_2^6 (f(x) - 3) \ dx\)

\(f(x) - 3\) represents a vertical translation of the original function by \(3\) units ‘downwards’. However, because we don’t know the ‘height’ of the maximum in this region, a translation ‘downwards’ could result in one of these four images.

|  |  |
|---|---|
|  |  |

Does it matter which of the four images is correct in this scenario?

Will each image give a different result?

We will consider the first image in more detail.

In this case the area of the light blue ‘portion’ represents the value of the integral \(\int_2^6 f(x) - 3 \ dx\).

The dark blue rectangle has an area of \(3 \times 4 = 12\) square units.

The area of the light blue ‘portion’ can now be written as \(40 - \textrm{dark blue} = 40 - 12 = 28\) square units.

Now the second image.

In this case the value of the integral \(\int_2^6 f(x) - 3 \ dx\) will be equal to the area of ‘portion’ \(A\) - the area of ‘portion’ \(C\). (From now on we will use \(A\) to represent the area of ‘portion’ \(A\) and similarly for \(B\) and \(C\).)

The area of ‘portion’ \(B\) can be written in two ways: \(40 - A\) or \(12 - C\).

If we equate these two expressions then we have \(40 - A = 12 - C\) which can be rearranged to provide the value of the integral \[\int_2^6 f(x) - 3 \ dx = A - C = 40 - 12 = 28.\]

Can you apply a similar method to evaluate the integral using the final two diagrams?

What do you notice about the result from the final (bottom right) diagram?

Can you explain why this diagram is NOT actually a possible representation of \(f(x) - 3\)?

Notice that once again, if we had thought algebraically we might have considered the integral as a sum of two functions, leading us to re-write it as \[\int_2^6 (f(x) -3) \ dx = \int_2^6 f(x) \ dx - \int_2^6 3 \ dx.\]

This of course produces the same result: the sum of the original area, \(\int_2^6 f(x) \ dx = 40\), and the rectangle, \(-\int_2^6 3 \ dx = -12\).

\(\int_0^4 f(x + 2) \ dx\)

\(f(x + 2)\) represents a horizontal translation of the original function by \(2\) units to the left.

The shaded region under the curve has also been translated so that it lies between \(x=0\) and \(x=4\).

The value of the integral \(\int_0^4 f(x + 2) \ dx\) is equal to the area of the light blue ‘portion’.

\(\int_2^6 f(x + 2) \ dx\)

This is very similar to the previous integral. The function itself has once again been translated horizontally \(2\) units to the left. However, the region that we are looking at has not changed. Given that we do not know what the original function \(f(x)\) is, we are now looking at a region for which we do not have enough information. We cannot even determine the precise position of the \(x\)-intercept in this region.

All we can say is that the area is likely to be less than the original 40 square units given that we now have a negative component.

\(\int_4^8 f(x + 2) \ dx\)

This is very similar to the previous integral. The function itself has once again been translated horizontally \(2\) units to the left. In addition to this, the region that we are looking at has changed. Given that we do not know what the original function \(f(x)\) is, we are now looking at a region for which we do not have enough information. We cannot even determine the precise position of the \(x\)-intercept in this region.

We now have a much larger negative component to the integral which suggests that this value will be less than 40 square units and less than the integral above in the region \(x=2\) to \(x=6\). The image suggests that the value will in fact be negative given that the negative portion appears much larger than the positive portion.

It is worth noting that if the integral had instead been given as \(\int_4^8 f(x - 2) \ dx\) then we would be able to evaluate it in exactly the same way as for \(\int_0^4 f(x + 2) \ dx\).

\(\int_2^6 -f(x) \ dx\)

\(-f(x)\) represents a reflection in the \(x\)-axis. The area of the region is preserved but the value of the integral is now negative as the region lies below the \(x\)-axis.

If we had taken an algebraic approach here we might have remembered that the integral could be re-written as \[\int_2^6 -f(x) \ dx = -\int_2^6 f(x) \ dx.\]

\(\int_2^6 f(-x) \ dx\)

\(f(-x)\) represents a reflection in the \(y\)-axis. The area of the reflected region, between \(x=-6\) and \(x=-2\), is preserved but the area in the original region is now unknown. If we knew something about the symmetry properties of the original function \(f(x)\) then we might be able to deduce something about this area. If \(f(x)\) has rotational symmetry about the origin then we could deduce that the integral will take the same value as for the curve \(-f(x)\) described above.

We cannot even meaningfully sketch this transformation because the original image doesn’t show the part of the curve between \(x=-6\) and \(x=-2\).

Notice that this means that we could evaluate the integral \(\int_{-6}^{-2} f(-x) \ dx\).

For the integral to equal \(0\), we need to introduce a negative component. In order to do this we need to translate the curve ‘downwards’ such that we achieve a situation like this, in which the area under the curve located ‘above’ the \(x\)-axis is equal to that ‘below’ the \(x\)-axis. This in turn means that \(k\) will be negative.

We have a maximum of three portions to consider. In the diagram shown, the area of ‘portion’ \(B\) must be equal to the sum of the areas of ‘portions’ \(A\) and \(C\).

From now on we will use \(A\) to represent the area of ‘portion’ \(A\), \(B\) to represent the area of ‘portion’ \(B\), etc.)

The value of the integral \(\int_2^6 (f(x) + k) \ dx\) will be equal to \(B - (A + C)\).

The area of ‘portion’ \(D\) can be written in two ways: \(4 \vert k \vert - (A+C)\) or \(40 - B\).

In this approach we have chosen to think about areas of ‘portions’ of the diagram. This means that even though \(k\) must be negative (by our own initial reasoning), we will use the magnitude of \(k\) (its positive value) for area calculations.

\(\vert k \vert\) denotes the magnitude of \(k\).

Equating these two expressions we have \(D = 4 \vert k \vert - (A+C) = 40 - B\) and rearranging we find that \[B - (A+C) = 40 - 4 \vert k \vert.\]

In this instance we want the integral to equal \(0\) so we can write \[0 = 40 - 4 \vert k \vert\] and therefore \[\vert k \vert = 10.\]

We know that \(k\) is in fact negative given the set up of our diagram and therefore \(\int_2^6 f(x) - 10 \ dx = 0\).

As in our approach to some of the original integrals, it may be worth noting that an algebraic approach here will also work. Re-writing the integral as \[\int_2^6 (f(x) + k) \ dx = \int_2^6 f(x) \ dx + \int_2^6 k \ dx = 0\] enables us to see that \(\int_2^6 k \ dx = -40\).

Proceeding with the integration we then find that \(4k = -40\) and therefore \(k=-10\) as before.

## Solution part 2

A summary of the integrals and their values is provided below:

| Integral | Value |
|---|---|
| \(\int_2^6 g(x) + 5 \ dx\) | \(28\) |
| \(\int_2^6 g(x) - 3 \ dx\) | \(-4\) |
| \(\int_0^4 g(x + 2) \ dx\) | \(8\) |
| \(\int_2^6 g(x + 2) \ dx\) | \(12\) |
| \(\int_4^8 g(x + 2) \ dx\) | \(16\) |
| \(\int_2^6 -g(x) \ dx\) | \(-8\) |
| \(\int_2^6 g(-x) \ dx\) | \(-8\) |

It is possible to evaluate all of the integrals for \(g(x)\) whereas for \(f(x)\) it was only possible to evaluate four of them.

What other integrals can we evaluate for \(g(x)\)?

Starting with the obvious, the graph of \(y=g(x)\) is a straight line whereas the graph of \(y=f(x)\) is not. What this means is that we actually know a lot more about the behaviour of \(g(x)\) compared to \(f(x)\).

- \(g(x)\) can be written in the form \(ax + b\) and from the diagram we can see that \(b=0\).

- \(g(x)\) has rotational symmetry about the origin.

- \(g(x)\) has a constant gradient, \(a\). This means that we can write \[a = \dfrac{y_{1}}{2} = \dfrac{y_{2}}{6},\] where \(y_{1}\) and \(y_{2}\) are the \(y\)-values when \(x=2\) and \(x=6\) respectively. Rearranging we have that \[\begin{equation} 3y_{1} = y_{2}. \label{eq:1} \end{equation}\]

- We know that the shaded area in the diagram is a trapezium so we can therefore write \[8 = \frac{1}{2}(y_{1} + y_{2}) \times 4 = 2(y_{1} + y_{2}).\] Rearranging we have that \[\begin{equation} y_{1} + y_{2} = 4. \label{eq:2} \end{equation}\]

Solving \(\eqref{eq:1}\) and \(\eqref{eq:2}\) simultaneously we find that \(y_{1}=1\) and \(y_{2}=3\). Substituting this back into the equation for the line we have that \[y=g(x) = \dfrac{1}{2}x.\]

Now that we know the function \(g(x)\) we are able to evaluate all of the integrals. We can use this to identify important, previously unknown values such as for \(\int_2^6 g(x + 2) \ dx\) as shown below.

Identifying the equation of the straight line allows us evaluate all of the specified integrals, and indeed any other integral that we may choose. However, it is worth noticing that, in comparison to the non-linear function \(f(x)\), we can still evaluate many more integrals without this information.

For instance, consider how you might evaluate the integral \(\int_2^6 g(8 - x) \ dx\) without knowing the function \(g(x)\).
