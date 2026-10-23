---
created: 2026-10-24T01:49:53 (UTC +06:00)
source: https://undergroundmathematics.org/calculus-of-powers/stretch-the-function
author: Underground Mathematics (University of Cambridge)
rights: © University of Cambridge (Underground Mathematics). Use inside SyllabAI is authorised by the
  operator attestation of 2026-10-23 — see LICENSE-DATA.md (Amendment 2026-10-23) in this repository.
  Takedown / correction handling as stated in LICENSE-DATA.md.
tags:
- underground-mathematics
- calculus-of-powers
- type/food-for-thought
- level/developing
resource_identity:
  ugm_id: stretch-the-function
  station: calculus-of-powers
  station_title: Calculus of Powers
  resource_type_id: 9
  resource_type_label: Food for thought
  level: Developing
  ref: 6033
  old_site_id: C2_RT6_1
spec_map:
  curriculum_code: CIE-9709-P1-2023
  lane: cie-a-level-maths-20-pure-1
  board: Cambridge CIE
  syllabus_version: 2023-2025
  subsection: calculus-of-powers
  subsection_provenance:
    tier: PROVIDER
    signal: source-url-slug
    slug: calculus-of-powers
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
- path: https://undergroundmathematics.org/calculus-of-powers/stretch-the-function/download/teacher-notes.pdf
  kind: printable
---

# Stretch the function

> Excerpt: Students evaluate definite integrals in order to find a scale factor that makes each function satisfy a pair of conditions.
A connection is made between the definite integral and the area between the graph and the axis.

## Warm-up

Evaluate the definite integral \[\int_{-1}^2 (x+1)^2 \,dx .\]

Find the value of the constant \(a\) so that \[\int_{-1}^2 a(x+1)^2 \,dx = 1 .\]

Sketch graphs to illustrate how these definite integrals are related.

Solution

Probably the easiest way to evaluate this integral is to expand the bracket (later you will learn about other ways to do it). \[\int_{-1}^2 x^2+2x+1\,dx =\left[\frac{x^3}{3}+x^2+x\right]_{-1}^{2}=\left(\frac{8}{3}+4+2\right)-\left(-\frac{1}{3}+1-1\right)=9\]

If we want \[\int_{-1}^2 a(x+1)^2 \,dx = 1\] then we need our integral to be \(9\) times smaller. We can do this by scaling (i.e. vertically stretching) our function by a factor of \(\dfrac{1}{9}\). So \(a=\dfrac{1}{9}\).

We have used the fact that for a function \(f(x)\), \[a\int f(x)\,dx = \int af(x)\,dx.\] Is this always true?

## Problem

In the Warm-up we scaled (or stretched) a function \(f(x)\) so that \[\int_{-1}^{2} a\,f(x) \, dx = 1.\]

- Which of the following functions could we scale to satisfy this condition and what is the value of \(a\) in each case?

- Which ones lead to problems and why?

- How would your answers be different if we changed the condition to \[\textit{an area of }\,1 \textit{ is enclosed by the curve }y=a\,f(x) \textit{, the }x\textit{-axis and the lines }x=-1\textit{ and }x=2\text{ ?}\]

The functions

| \(f(x)=x\) | \(f(x)=x(1-x)\) |
|---|---|
| \(f(x)=\sqrt x\) | \(f(x)=(x+1)(x-1)^2\) |
| \(f(x)=(x-2)(2x-1)(x+1)\) | \(f(x)=\dfrac{1}{x^2}\) |

Can you think of some other functions which cannot be scaled to satisfy one or both of our conditions?

## Solution

1) \(f(x)=x\)

If we evaluate the integral, we find \[\int_{-1}^2 x\,dx = \left[\frac{x^2}{2}\right]_{-1}^2 = \frac{3}{2} .\] So we could scale this function to satisfy the integral condition, \[\int_{-1}^2 \frac{2}{3}x \,dx = 1\] and we have \(a=\dfrac{2}{3}\).

To find the area between the curve \(y=f(x)\) and the \(x\)-axis, we could either evaluate the integral in two parts or work out the areas of two triangles. \[\text{Area} = \frac{1}{2}\times1\times1 + \frac{1}{2}\times 2\times2 = \frac{5}{2}\]

So to satisfy the area condition we need \(a=\dfrac{2}{5}\).

The answers for the two conditions are different because the curve \(y=f(x)\) is below the axis for part of the interval \(-1\leq x\leq2\).

Note that the definite integral does tell us about the area, but that it *subtracts* the areas below the axis from those above.

The definite integral tells us something about the average value of the function over the given interval.

2) \(f(x)=x(1-x)\)

We need to evaluate

\[\int_{-1}^2 x(1-x)\,dx = \int_{-1}^2 x-x^2\,dx=\left[\frac{x^2}{2}-\frac{x^3}{3}\right]_{-1}^2 = \left(\frac{4}{2}-\frac{8}{3}\right)-\left(\frac{1}{2}-\frac{-1}{3}\right) = -\frac{3}{2}\]

and we find that

\(a=-\dfrac{2}{3}\)

satisfies the integral condition.

Why does \(a\) need to be negative? What does that mean geometrically?

We notice that \(f(x)=0\) at \(x=0\) and \(x=1\) which are both within our interval, so the curve crosses the \(x\)-axis twice. Drawing a sketch will help us to think about the area condition – we will need to work out the integral in several parts.

The area will be given by

\[-\int_{-1}^0 x-x^2\,dx+ \int_{0}^1 x-x^2\,dx-\int_{1}^2 x-x^2\,dx=\frac{11}{6} .\]

Note how we subtract the integrals for the parts of the curve that lie below the \(x\)-axis because these integrals have negative values.

The symmetry of the curve means that we actually only have to calculate two integrals.

So we need \(a=\dfrac{6}{11}\) to satisfy the area condition.

We hit a problem with this function as we can't integrate it directly across the interval. For $x<0$ the function is essentially $f(x)=-x$, whereas for $x \geq 0$ it is $f(x)=x$. So we can do the integral in two pieces or more simply look at the two triangles. The graph of this function is entirely above the axis so the same scale factor, $\dfrac {2}{5}$, satisfies both conditions.

3) \(f(x)=\sqrt x\)

This function is undefined for \(x<0\) so we can’t integrate it over the whole interval or find a scale factor for the integral condition.

However, we can find the area under the curve by integrating from \(0\) to \(2\). It is \[\int_{0}^2 \sqrt x\,dx = \left[\frac{2}{3}x^{3/2}\right]_0^2 = \frac{4}{3}\sqrt 2\]

so \(a=\dfrac{3}{4\sqrt 2} = \dfrac{3 \sqrt 2}{8}\) would scale the area as required.

4) \(f(x)=(x+1)(x-1)^2\)

To integrate this we will need to expand the brackets, giving \(f(x)=x^3-x^2-x+1\).

\[\int_{-1}^2 f(x)\,dx= \left[\frac{x^4}{4}-\frac{x^3}{3}-\frac{x^2}{2}+x\right]_{-1}^2 = (4-\frac{8}{3}-2+2)-(\frac{1}{4}+\frac{1}{3}-\frac{1}{2}-1)=\frac{9}{4}\] so we find \(a=\dfrac{4}{9}\) for the integral condition.

For the area condition we need to consider where the integral has a negative value.

How many times does the curve **cross** the \(x\)-axis in the interval from \(-1\) to \(2\)?

As the graph is entirely above the axis, the same scale factor will work for the area condition as for the integral condition.

We see that we only need to split this into two parts. $$\text{Area} =-\int_{-1}^{-\frac{1}{2}} f(x)\,dx + \int_{-\frac{1}{2}}^2 f(x)\,dx = \frac{51}{16}$$ and thus for an area of $1$ the scaled function must be $\frac{16}{51}(2x+1)(x-1)^2$.

5) \(f(x)=(x-2)(2x-1)(x+1)\)

This time when we expand and integrate we find the interesting result that \(\int_{-1}^2 2x^3-3x^2-3x+2\,dx= 0\). This will always be \(0\) whatever scaling we use.

Can you explain why this has happened?

Once we draw a sketch and think about the areas above and below the axis, we can find the area and hence meet the area condition using \(a=\frac{16}{81}\).

Note that we do not need to evaluate two integrals to find the area. Using the symmetry of the graph we can instead evaluate \(2\int_{-1}^{\frac{1}{2}} f(x)\,dx\).

You may not know how to integrate this yet. If you do, we still have an issue as the function is undefined at $x=0$ where there is a vertical asymptote. There is an infinite area between the curve and the $x$-axis. A definite integral is only properly defined if the function is *continuous* between the two limits, otherwise it is called an

.

It looks intuitively as though the integral from $-1$ to $0$ would exactly cancel the integral from $0$ to $1$, but that involves subtracting infinities which is not really safe. It can be allowed under some circumstances and we'll explore that in [the next section](disagreement).

6) \(f(x)=\dfrac{1}{x^2}\)

This function is undefined at \(x=0\) where there is a vertical asymptote. There is an infinite area between the curve and the \(x\)-axis. A definite integral is only properly defined if the function is *continuous* between the two limits, otherwise it is called an [improper integral](https://undergroundmathematics.org/glossary/improper-integral).

So although it *looks* as though we can find \[\int_{-1}^2 \dfrac{1}{x^2}\,dx = \int_{-1}^2 x^{-2}\,dx = \left[\frac{x^{-1}}{-1}\right]_{-1}^2 = \left[\frac{-1}{x}\right]_{-1}^2 = \left(\frac{-1}{2}\right)-\left(\frac{-1}{-1}\right) = -\frac{3}{2} ,\] this is in fact absurd. We should always check that a function is *continuous* over the interval before evaluating a definite integral.

Any function which is undefined over part of the interval will be a problem for the integral condition.

Any function with a singularity (vertical asymptote) in the interval will be a problem, except in a few special cases.

When a function has rotational symmetry about the mid point of the interval, i.e. \(x=\frac{1}{2}\), then the area above and below the axis will be equal. The integral will evaluate to \(0\) which cannot be scaled to \(1\) however hard we try! So the integral condition cannot be satisfied, but often the area condition can.

There are other cases with zero integral which are not symmetrical in this way. For instance, starting with a simple function like \(f(x)=x^2-c\) we can find \[\int_{-1}^2 x^2-c\,dx= \left[\frac{x^3}{3}-cx\right]_{-1}^2\] and choose a value of \(c\) which gives \(\int_{-1}^2f(x)\,dx=0\). Can you extend that to find other functions?

Are there any functions without singularities for which an *area* of \(1\) cannot be achieved?

## A disagreement

In the main problem, we were trying to find a function, \(f(x)\), such that \[\int_{-1}^2 f(x)\,dx=1\]

Abi says, \[\int_{-1}^2 \frac{1}{x^2}\,dx = \left[\frac{x^{-1}}{-1}\right]_{-1}^2 = \frac{1/2}{-1} - \frac{-1}{-1} = -\frac{3}{2}\] so \(f(x)=-\dfrac{2}{3x^2}\) would satisfy the condition.

Ben says, \[\int_{-1}^2 \frac{1}{x^3}\,dx = \left[\frac{x^{-2}}{-2}\right]_{-1}^2 = \frac{1/4}{-2} - \frac{1}{-2} = \frac{3}{8}\] so \(f(x)=\dfrac{8}{3x^3}\) would satisfy the condition.

Charlie says, \[\int_{-1}^2 \frac{1}{x^{1/3}}\,dx = \left[\frac{3}{2}x^{2/3}\right]_{-1}^2 = \frac{3}{2} (\sqrt[3]4 -1)\] so \(f(x)=\dfrac{2}{3(\sqrt[3]4 -1)}\dfrac{1}{x^{1/3}}\) would satisfy the condition.

Are any of them right?

## A resolution

In the main problem, we were trying to find a function, \(f(x)\), such that \[\int_{-1}^2 f(x)\,dx=1\]

Abi says, \[\int_{-1}^2 \frac{1}{x^2}\,dx = \left[\frac{x^{-1}}{-1}\right]_{-1}^2 = \frac{1/2}{-1} - \frac{-1}{-1} = -\frac{3}{2}\] so \(f(x)=-\dfrac{2}{3x^2}\) would satisfy the condition.

If you haven’t already sketched graphs of the suggested functions it would be a good idea to do so now.

The three functions all have vertical asymptotes at \(x=0\). An integral of any of these over \(x=0\) must therefore be treated with extreme caution. They are known as [improper integrals](https://undergroundmathematics.org/glossary/improper-integral).

A sketch graph suggests that Abi’s proposal is wrong. The graph is entirely above the \(x\)-axis and appears to contain an infinite area between the graph and the axis.

If we split the region into two we find we cannot evaluate either piece, \[\int_{-1}^2 f(x)\,dx = \int_{-1}^0 x^{-2}\,dx + \int_0^2 x^{-2}\,dx = \left[\frac{-1}{x}\right]_{-1}^0 + \left[\frac{-1}{x}\right]_0^2 .\]

There is no way round this. Abi is wrong.

Charlie says, \[\int_{-1}^2 \frac{1}{x^{1/3}}\,dx = \left[\frac{3}{2}x^{2/3}\right]_{-1}^2 = \frac{3}{2} (\sqrt[3]4 -1)\] so \(f(x)=\dfrac{2}{3(\sqrt[3]4 -1)}\dfrac{1}{x^{1/3}}\) would satisfy the condition.

Charlie’s function has a vertical asymptote so we should see what happens if we try to integrate it in pieces. \[\int_{-1}^0 \frac{1}{x^{1/3}}\,dx = \left[\frac{3}{2}x^{2/3}\right]_{-1}^0 = 0 - \frac{3}{2}\sqrt[3]{(-1)^2} = - \frac{3}{2}\] and \[\int_0^1 \frac{1}{x^{1/3}}\,dx = \left[\frac{3}{2}x^{2/3}\right]_0^1 = \frac{3}{2}\sqrt[3]{(1)^2} - 0 = \frac{3}{2}\] and \[\int_1^2 \frac{1}{x^{1/3}}\,dx = \left[\frac{3}{2}x^{2/3}\right]_1^2 = \frac{3}{2}\sqrt[3]{(2)^2} - \frac{3}{2}\sqrt[3]{(1)^2} = \frac{3}{2} (\sqrt[3]4 -1) .\]

Surprisingly, we can integrate up to the asymptote without a problem. The piece from \(-1\) to \(0\) exactly cancels the piece from \(0\) to \(1\) and so integrating from \(-1\) to \(2\) gives the same result as integrating from \(1\) to \(2\). Although the function is undefined at \(x=0\), the curve encloses a finite area. This is a bit like summing an infinite series and getting a finite result.

Charlie is correct.

Ben says, \[\int_{-1}^2 \frac{1}{x^3}\,dx = \left[\frac{x^{-2}}{-2}\right]_{-1}^2 = \frac{1/4}{-2} - \frac{1}{-2} = \frac{3}{8}\] so \(f(x)=\dfrac{8}{3x^3}\) would satisfy the condition.

Ben’s function \(\dfrac{1}{x^3}\) has a similar shape to Charlie’s. But this time we cannot evaluate the integral \(\displaystyle\int_{0}^2 \frac{1}{x^3}\,dx\) because it involves dividing by zero. So the integral does not have a proper value.

The geometry of the graph suggests that the pieces either side of \(x=0\) should cancel out as they did for Charlie. But this is problematic because it involves subtracting one infinity from another which is not a safe thing to do.

The mathematics is really beyond this level, but it is possible to construct an argument based on symmetrical limiting cases which allows us to effectively cancel the two areas. This result is known as the Cauchy Principal Value of the ill-defined integral. You may learn about this if you go on to study mathematics at university.

In this case, the value does work out at \(\frac{3}{8}\) as Ben stated, so we can say that Ben is correct.

So why does Charlie’s function work properly whereas Ben’s only works improperly?

The distinction is to do with how quickly the function converges with the vertical asymptote. A function \(\dfrac{1}{x^{n}}\) has a finite area close to the \(y\)-axis if \(0<n<1\).
