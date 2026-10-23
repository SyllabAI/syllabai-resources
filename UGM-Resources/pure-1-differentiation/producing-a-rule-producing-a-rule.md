---
created: 2026-10-24T01:49:53 (UTC +06:00)
source: https://undergroundmathematics.org/product-rule/producing-a-rule
author: Underground Mathematics (University of Cambridge)
rights: © University of Cambridge (Underground Mathematics). Use inside SyllabAI is authorised by the
  operator attestation of 2026-10-23 — see LICENSE-DATA.md (Amendment 2026-10-23) in this repository.
  Takedown / correction handling as stated in LICENSE-DATA.md.
tags:
- underground-mathematics
- product-rule
- type/building-blocks
- level/introducing
resource_identity:
  ugm_id: producing-a-rule
  station: product-rule
  station_title: Product Rule & Integration by Parts
  resource_type_id: 1
  resource_type_label: Building blocks
  level: Introducing
  ref: 5185
  old_site_id: null
spec_map:
  curriculum_code: CIE-9709-P1-2023
  lane: cie-a-level-maths-20-pure-1
  board: Cambridge CIE
  syllabus_version: 2023-2025
  subsection: product-rule
  subsection_provenance:
    tier: PROVIDER
    signal: source-url-slug
    slug: product-rule
    validation_status: SUGGESTED
  spec_points:
  - code: 1.7.2
    provenance:
      tier: AI_SUGGESTED
      confidence: medium
      model_version: GLM (Super Z agent, z.ai) — P3c lane-7 cross-map (cross-map-differentiation.json
        (P3c lane 7) @ syllabai-experimental 93575e69)
      evidence: differentiating quadratics in factorised form — the discovered shortcut is the linear-factor
        product structure; expand-and-differentiate keeps it P1-compatible (the generalisation clause
        anticipates the P3 product rule, recorded)
      rationale: 'Canonical UGM title: "Producing a rule"'
      validation_status: SUGGESTED
    title: use the derivative of x (for any rational n ), together with constant multiples, sums and
      differences of functions, and of composite functions using the chain rule
  mapped_date: '2026-10-24'
  mapper: cross-map-differentiation.json (P3c lane 7) @ syllabai-experimental 93575e69
provenance:
  capture_date: '2026-10-22'
  capture_tool: P2 full-site crawl (ugm-crawl) → ugm-clean extraction; text-only import
  content_language: en
task: T-UGM-IMPORT-7
assets:
- path: https://undergroundmathematics.org/product-rule/producing-a-rule/download/teacher-notes.pdf
  kind: printable
---

# Producing a rule

> Excerpt: Students are invited to find a short-cut to differentiating quadratics written in factorised form. The rule may need to be adapted as more complicated examples are encountered.

## Warm-up

Differentiate these functions and compare the results with the original functions.

\[\begin{align} y&=(x+2)(x+3) \label{eq 1}\\ y&=(x+2)(x-1) \label{eq 2} \end{align}\]

- What do you notice?

If you don’t notice anything, or you want to check out whether there is a pattern emerging you could try a few more examples of your own.

- Can you create a rule to find the derivative of a function like this without expanding the brackets?

Solution

Since \(\eqref{eq 1}\) could be written \(y= x^2 +5x +6\) then \(\frac{dy}{dx} = 2x +5\)

and since \(\eqref{eq 2}\) could be written \(y=x^2 +x -2\) then \(\frac{dy}{dx} = 2x +1\).

If we compare these with the original functions we can see that each derivative is the sum of the two brackets that were multiplied in the original function.

- Can you understand why this happens?

- Will this always be the case?

## Problem

Try applying the rule you came up with in the [Warm-up](https://undergroundmathematics.org/product-rule/producing-a-rule/) to these functions.

\[\begin{align} y&=(2x-3)(x+2) \\ y&=(2-x)(x+3) \\ y&=(x+3)(1-2x) \\ y&=(3x+4)(2x-5) \\ y&=(3-2x)(5-3x) \end{align}\]

- Does your original rule give you the correct derivative for these functions?

- If your original rule works for these functions, can you justify why? If not, then can you adapt your rule to make it work for all of the examples so far?

Now try these

Does your (new) rule work for \(y=(x^2+3)(x^2+2)\)?

If not, try to adapt it.

Now try it on \(y=(2x^2+3x-2)(x-1)\).

What have you noticed?

## Things you may have noticed

Try applying the rule you came up with in the [Warm-up](https://undergroundmathematics.org/product-rule/producing-a-rule/) to these functions.

\[\begin{align} y&=(2x-3)(x+2) \label{eq:notice1}\\ y&=(2-x)(x+3) \\ y&=(x+3)(1-2x) \\ y&=(3x+4)(2x-5) \\ y&=(3-2x)(5-3x) \end{align}\]

- Does your original rule give you the correct derivative for these functions?

- If your original rule works for these functions, can you justify why? If not, then can you adapt your rule to make it work for all of the examples so far?

From the Warm-up, we had a rule that said, *add together the brackets to find the derivative*.

If we start to look at these, we don’t seem to be able to use this rule. In \(\eqref{eq:notice1}\), we see that the expansion will give us \(2x^2\) so our derivative needs to include \(4x\), but following the rule of adding the brackets would give us \(3x\).

We could check it out thoroughly by expanding and differentiating:

\[\begin{align*} y&=(2x-3)(x+2) \\ &=2x^2+x-6 \\ \implies\quad\frac{dy}{dx}&=4x+1 \\ \end{align*}\]

But \((2x-3)+(x+2)=3x-1\), which is not equal to the derivative. We notice that we’re out by \(x+2\), which means that the derivative is actually \((2x-3)+2(x+2)\).

- How could we adapt our rule to work for these examples?

- Can we find a similar way of creating the derivatives of all these functions?

- Could we adapt our rule for any pair of linear brackets, or something more general (think about what that might be)?

Alternatively we could rewrite the original function to have brackets starting with only a single \(x\), so for \(\eqref{eq:notice1}\) we have \(y=2(x-\frac{3}{2})(x+2)\).

- Now what would the adaptation to the rule be?
  How are these two versions linked?

Now try these

Does your rule work for \(y=(x^2+3)(x^2+2)\)?

If not try to adapt it.

For this function, adding constant multiples of the brackets will not work. We can see that expanding it would give us a quartic expression, so the derivative will be cubic.

What would we need to multiply the brackets by before adding, to get the right answer this time?

We might think of applying the chain rule by rewriting this as \(y=(u+3)(u+2)\) where \(u=x^2\). Our original rule would then give \(\frac{dy}{du}=2u+5\).

Now applying the chain rule gives \(\frac{dy}{dx}= (2u+5)(2x)= (2x^2+5)(2x) = 4x^3+10x\).

Can we find a way to adapt our earlier rule to account for this?

Looking at \(y=(2x^2+3x-2)(x-1)\) might give us a hint about how to adapt the rule so that it works for all cases. We can’t use the chain rule here because one bracket is linear, but the application of chain rule above might give us a hint for a general adaptation.

Again we can see that expanding would give us a term \(2x^3\) which would differentiate to \(6x^2\). As only one bracket contains \(x^2\) we would have to multiply that bracket by \(3\) before adding, but there doesn’t seem a good reason for using \(3\). Thinking still about multiplying and adding, we could instead multiply the second bracket by \(4x\) to give us the total of \(2x^2+4x^2=6x^2\) when added to the quadratic bracket. We might derive \(4x\) from the first bracket by differentiating, this is similar to using the \(x\) coefficient from a linear bracket so there seems like a good reason for doing it.

General rule

We have gradually worked up in complexity to see that rather than expanding brackets to create a single polynomial to differentiate, we can instead multiply each bracket by the differential of the other and add them. So for polynomials \(f(x)\) and \(g(x)\) if \(y=f(x)g(x)\) then \(\dfrac{dy}{dx}=f'(x)g(x)+g'(x)f(x)\).

This is called the [Product Rule](https://undergroundmathematics.org/glossary/product-rule) and can be shown to be true for any functions, not just polynomials. You might like to read [this](https://undergroundmathematics.org/product-rule/producing-a-rule/perspective) explanation.

## A certain perspective

In the [Problem](https://undergroundmathematics.org/product-rule/producing-a-rule/problem) section, we found out that the derivative of \((ax+b)(cx+d)\) is \(a(cx+d)+c(ax+b)\). It turns out that we can use this result to differentiate the product of *any* two functions, and in this section, we explore how to do so.

Our key question is:

What is the derivative of the product \(h(x)=f(x)g(x)\) for any functions \(f\) and \(g\)?

We will find the derivative of \(h(x)\) at the point \(x=x_0\).

In [A tangent is…](https://undergroundmathematics.org/introducing-calculus/a-tangent-is), we saw that we can [locally](https://undergroundmathematics.org/glossary/local) approximate any function by a straight line (so long as we avoid any points where the gradient is not well defined). So near \(x_0\), \(f(x)\approx ax+b\) for some \(a\) and \(b\).

We can find \(a\) and \(b\) by matching the gradients and \(y\)-values: \[f'(x_0)=a \quad\text{and}\quad f(x_0)=ax_0+b\] Likewise, near \(x_0\), \(g(x)\approx cx+d\) where \(c\) and \(d\) are such that \(g'(x_0)=c\) and \(g(x_0)=cx_0+d\).

So near \(x_0\), we have \(h(x)=f(x)g(x)\approx (ax+b)(cx+d)\), so using the rule we found out, we see that the derivative of \(h(x)\) at \(x_0\) is \(a(cx_0+d)+c(ax_0+b)\). Substituting in our values for \(a\), \(b\), \(c\) and \(d\), we find \[h'(x_0)=f'(x_0)g(x_0)+g'(x_0)f(x_0).\] So in general, \[h'(x)=f'(x)g(x)+g'(x)f(x).\]

An alternative notation which is commonly used is to write \(u=f(x)\) and \(v=g(x)\). Then we have \[\frac{d}{dx}(uv)=u\frac{dv}{dx}+v\frac{du}{dx}.\]
