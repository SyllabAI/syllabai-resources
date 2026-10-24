---
created: 2026-10-25T01:37:17 (UTC +06:00)
source: https://undergroundmathematics.org/polynomials/how-not-to-solve-a-cubic
author: Underground Mathematics (University of Cambridge)
rights: © University of Cambridge (Underground Mathematics). Use inside SyllabAI is authorised by the
  operator attestation of 2026-10-23 — see LICENSE-DATA.md (Amendment 2026-10-23) in this repository.
  Takedown / correction handling as stated in LICENSE-DATA.md.
tags:
- underground-mathematics
- polynomials
- type/food-for-thought
- level/developing
resource_identity:
  ugm_id: how-not-to-solve-a-cubic
  station: polynomials
  station_title: Polynomials & Rational Functions
  resource_type_id: 9
  resource_type_label: Food for thought
  level: Developing
  ref: 9677
  old_site_id: null
spec_map:
  curriculum_code: CIE-9709-P3-2023
  lane: cie-a-level-maths-20-pure-3
  board: Cambridge CIE
  syllabus_version: 2023-2025
  subsection: polynomials
  subsection_provenance:
    tier: PROVIDER
    signal: source-url-slug
    slug: polynomials
    validation_status: SUGGESTED
  spec_points:
  - code: 3.1.4
    provenance:
      tier: AI_SUGGESTED
      confidence: medium
      model_version: "GLM (Super Z agent, z.ai) — P3c lane-9 cross-map (cross-map-algebra.json (P3c lane 9) @ syllabai-experimental 3098d8eb)"
      evidence: "common-root condition formalised by the factor theorem: f(k)=g(k)=0 ⟹ (x−k) divides both polynomials, forcing k∈{0,1} and the two families of shared-root cubics"
      rationale: "Canonical UGM title: How not to solve a cubic..."
      validation_status: SUGGESTED
    title: "use the factor theorem and the remainder theorem"
  mapped_date: '2026-10-25'
  mapper: cross-map-algebra.json (P3c lane 9) @ syllabai-experimental 3098d8eb
provenance:
  capture_date: '2026-10-22'
  capture_tool: P2 full-site crawl (ugm-crawl) → ugm-clean extraction; text-only import
  content_language: en
  task: T-UGM-IMPORT-9
---

# How not to solve a cubic...

> Excerpt: Students are invited to find a cubic which can (surprisingly) be partially solved using an obviously incorrect method.

## Warm-up

Can you find a cubic and quadratic graph that both pass through the \(x\)-axis at \(x=3\)?

Are these curves unique?

You might find it helpful to use graphing software such as [Desmos](https://www.desmos.com/calculator).

## Problem

A student was trying to solve the cubic \[x^3-2x-1=0.\]

Unfortunately, they thought they were dealing with the quadratic \(x^2-2x-1=0\) and used the quadratic formula. They got the two solutions \(x=1\pm\sqrt{2}\), neither of which is a root of the original cubic.

Could this wrong method ever work?

Can you find a cubic equation \(ax^3+bx+c=0\) where (at least) one of the roots of the corresponding quadratic \(ax^2+bx+c=0\) is also a root of the cubic?

## Suggestion

Can you sketch what a solution to this problem might look like? What are the important features on this sketch?

How can we use algebra to express the condition that the cubic and quadratic share a root?

## Things you might have noticed

Before diving into this question we might begin by taking a step back to think about what it is asking us to find.

- Can we represent the problem graphically?

- Do we expect there to be a unique solution?

We are essentially looking for a quadratic and cubic curve that both pass through a given point (or pair of points) on the \(x\)-axis. It feels as though there may be lots of pairs of curves like this, and indeed we may have already found an example of a cubic and quadratic curve that each pass through \((0,3)\) in the [Warm-up problem](https://undergroundmathematics.org/polynomials/how-not-to-solve-a-cubic/).

But are both equations in the form \(ax^3+bx+c=0\) and \(ax^2+bx+c=0\) as required?

This constraint narrows down the problem. We might need to consider algebraic representations of the problem to help us make progress.

Let’s label the quadratic and cubic equations

\(f(x)\)

and

\(g(x)\)

so that

\[\begin{align*} f(x)&=ax^2+bx+c\\ g(x)&=ax^3+bx+c. \end{align*}\]

Now if \(f(k)=0\) and \(g(k)=0\), so that \(k\) is a root of both equations, we can write \[ak^2 + bk + c = 0\quad\text{and}\quad ak^3 + bk + c =0.\] We can now equate the left hand sides to get \(ak^2 + bk + c = ak^3 + bk + c\). Subtracting \(bk+c\) gives \(ak^2=ak^3\), and this is only true for \(k=1\) or \(k=0\). (It is also true if \(a=0\), but then we don’t have a cubic equation, so we can ignore this possibility.)

Did you remember to consider the possibility that \(k=0\)?

If

\(k=0\)

, there is a common root at

\(x=0\)

, so

\(c=0\)

and we can rewrite the equations as

\[\begin{align*} f(x)&=ax^2+bx=x(ax+b)\\ g(x)&=ax^3+bx=x(ax^2+b). \end{align*}\]

How did we know that \(c=0\) in this case?

You might like to use the GeoGebra applet below to convince yourself of our findings so far. You can adjust the sliders to see how the functions change for different values of \(a\) and \(b\) (but with our common root staying fixed at \(x=0\)).

> [interactive embed (geogebra-iframe): //www.geogebratube.org/material/iframe/id/nUtPxpV2/width/600/height/400/border/888888/rc/false/ai/false/sdz/false/smb/false/stb/false/stbh/false/ld/false/sri/true/asb/false/at/html5] — not part of the text import; see the source page.

[Download GeoGebra file](https://www.geogebratube.org/material/download/format/file/id/nUtPxpV2)

Can you adjust the sliders to find a case where the functions share two roots?

Is this case unique or can you find another?

Where do you expect the second shared root to be?

We began this line of thinking by considering the case where \(k=0\). How might we now consider the other possibility that \(k=1\), so there is a common root at \(x=1\)?

By the factor theorem we can say that if \(f(k)=0\) and \(g(k)=0\), so that \(k\) is a root of both equations, we also have \((x-k)\) as a factor of both \(f(x)\) and \(g(x)\). So in this case, \(x-1\) is a factor of both \(f(x)\) and \(g(x)\).

> [interactive embed (geogebra-iframe): //www.geogebratube.org/material/iframe/id/mZmRVEWX/width/600/height/400/border/888888/rc/false/ai/false/sdz/false/smb/false/stb/false/stbh/false/ld/false/sri/true/asb/false/at/html5] — not part of the text import; see the source page.

[Download GeoGebra file](https://www.geogebratube.org/material/download/format/file/id/mZmRVEWX)

What’s the same and what’s different about this GeoGebra applet, when compared to the first one?

Can you suggest a pair of functions for which \(x=1\) is a root but \(x=0\) is not?

Looking at the graph, it is also interesting to think about the behaviour of the graphs at the points where they meet: how do the behaviours at \(x=0\) and \(x=1\) compare?

**On reflection…**

When we reflected on our approach, we realised that there is an easier way to think about the problem.

Where do the cubic and quadratic graphs intersect?

The intersections

The original question asks when are \(ax^3+bx+c=0\) and \(ax^2+bx+c=0\) both true. This means in particular that we require the cubic \(y=ax^3+bx+c\) and quadratic \(y=ax^2+bx+c\) to intersect, so we need \(ax^3+bx+c=ax^2+bx+c\).

If we now subtract \(bx+c\) from this, we get \(ax^3=ax^2\). Therefore the cubic and quadratic *always* intersect at \(x=0\) and \(x=1\)!

We can now finish the problem off by determining whether \(ax^2+bx+c=0\) at either of these points. There will be a (shared) root at \(x=0\) if and only if \(c=0\), and a (shared) root at \(x=1\) if and only if \(a+b+c=0\). And we are done!

**An alternative algebraic approach**

One way to approach this problem using algebra is to write the cubic and quadratic in terms of their roots. Let us assume that \(\alpha\) is a common root, let the other roots of the cubic be \(\beta\) and \(\gamma\), and the other root of the quadratic be \(\delta\). Then we can write the cubic as \(a(x-\alpha)(x-\beta)(x-\gamma)=0\) and the quadratic as \(a(x-\alpha)(x-\delta)=0\).

We could now expand the left hand sides to get \[ax^3-a(\alpha+\beta+\gamma)x^2+a(\alpha\beta+\beta\gamma+\gamma\alpha)x-a\alpha\beta\gamma=ax^3+bx+c\] and \[ax^2-a(\alpha+\delta)x+a\alpha\delta=ax^2+bx+c.\]

Equating coefficients (and noting

\(a\ne0\)

throughout, as the first equation is a cubic), we obtain:

\[\begin{align} \alpha+\beta+\gamma &= 0 \label{eq:1}\\ \alpha\beta+\beta\gamma+\gamma\alpha &= -(\alpha+\delta) \label{eq:2}\\ \alpha\beta\gamma &= -\alpha\delta. \label{eq:3} \end{align}\]

Now all that is left to do is to solve these equations!

Solving the equations

Looking at equation \(\eqref{eq:3}\), which we can rearrange as \(\alpha(\beta\gamma+\delta)=0\), we see that either \(\alpha=0\) or \(\beta\gamma=-\delta\).

**Case 1: \(\alpha=0\)**

This means that \(c=0\), so the equations are \(ax^3+bx=0\) and \(ax^2+bx=0\).

Is there any choice for \(a\) and \(b\) which would mean that *both* roots of the quadratic are roots of the cubic?

**Case 2: \(\beta\gamma=-\delta\)**

If we substitute this into \(\eqref{eq:2}\), we get \[\alpha\beta-\delta+\gamma\alpha = -(\alpha+\delta),\] which simplifies to \(\alpha(\beta+\gamma)=-\alpha\), so \(\alpha=0\) (bringing us back to Case 1) or \(\beta+\gamma=-1\).

In the latter case, equation \(\eqref{eq:1}\) then gives \(\alpha=1\), so the cubic and quadratic share the root \(\alpha=1\), and they become \[ax^3-a(\delta+1)x+a\delta=0 \quad\text{and}\quad ax^2-a(\delta+1)x+a\delta=0.\] or \[ax^3+bx+c=0\quad\text{and}\quad ax^2+bx+c=0\] where \(a+b+c=0\).

Is there any choice here which would mean that *both* roots of the quadratic are roots of the cubic?

Is there another way of seeing why \(a+b+c=0\) would give a common root of \(x=1\)? And is it always the case that if \(x=1\) is a root of \(ax^3+bx+c=0\), then it is also a root of \(ax^2+bx+c=0\)?
