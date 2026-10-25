---
created: 2026-10-25T21:48:43 (UTC +06:00)
source: https://undergroundmathematics.org/chain-rule/can-you-find-chain-rule-edition
author: Underground Mathematics (University of Cambridge)
rights: © University of Cambridge (Underground Mathematics). Use inside SyllabAI is authorised by the
  operator attestation of 2026-10-23 — see LICENSE-DATA.md (Amendment 2026-10-23) in this repository.
  Takedown / correction handling as stated in LICENSE-DATA.md.
tags:
- underground-mathematics
- chain-rule
- type/many-ways-problem
resource_identity:
  ugm_id: can-you-find-chain-rule-edition
  station: chain-rule
  station_title: Chain Rule & Integration by Substitution
  resource_type_id: 4
  resource_type_label: Many ways problem
  level: Developing
  ref: 9008
  old_site_id: null
spec_map:
  curriculum_code: CIE-9709-P3-2023
  lane: cie-a-level-maths-20-pure-3
  board: Cambridge CIE
  syllabus_version: 2023-2025
  subsection: chain-rule
  subsection_provenance:
    tier: PROVIDER
    signal: source-url-slug
    slug: chain-rule
    validation_status: SUGGESTED
  spec_points:
  - code: 3.4.1
    provenance:
      tier: AI_SUGGESTED
      confidence: high
      model_version: GLM (Super Z agent, z.ai) — P3c lane-12 cross-map (cross-map-p3-differentiation.json
        (P3c lane 12) @ syllabai-experimental 506ea24f8e61cc75c4662f8ebb08cfd2b1d458d4)
      evidence: working backwards from conditions on f(g(x)) (stationary points at prescribed x, a local
        minimum of ln g(x), no stationary points) - chain-rule composition reasoning with the 3.4.1 list
        as the toolset (flips the lane-10 non-overlap row of record routed 'P3 3.4 Differentiation')
      rationale: 'Canonical UGM title: Can you find... chain rule edition'
      validation_status: SUGGESTED
    title: use the derivatives of e , ln x , sin x , cos x , tan x , tan x , together with constant multiples,
      sums, differences and composites
  mapped_date: '2026-10-25'
  mapper: cross-map-p3-differentiation.json (P3c lane 12) @ syllabai-experimental 506ea24f8e61cc75c4662f8ebb08cfd2b1d458d4
provenance:
  capture_date: '2026-10-22'
  capture_tool: P2 full-site crawl (ugm-crawl) → ugm-clean extraction; text-only import
  content_language: en
  task: T-UGM-IMPORT-12
---

# Can you find... chain rule edition

> Excerpt: Students use the chain rule to work backwards from conditions that the derivative of a function of a function must satisfy.

## Problem

Can you find …

(b) ... functions $f(x)$ and $g(x)$ so that $f(g(x))$ is always increasing but $f(x)$ or $g(x)$ is not always increasing?

1. … functions \(f(x)\) and \(g(x)\) so that \(f(g(x))\) has stationary points when \(x=-1\) and \(x=5\)?

---

1. … a function \(g(x)\) so that \(\ln{g(x)}\) has a local minimum?

---

1. … functions \(f(x)\) and \(g(x)\) so that \(f(g(x))\) has no stationary points?

(d) ... a function $f(x)$ so that $f(\ln{x})$ has a local minimum when $x=3$?

(d) ... functions $f(x)$ and $g(x)$ so that $f(g(x))$ has a local maximum where $g(x)$ has a local minimum? (e) ... functions $f(x)$ and $g(x)$ so that $y=2x+1$ is a tangent to $y=f(g(x)).$

## Suggestion

The derivative of \(f(g(x))\) is the product of \(f'(g(x))\) and \(g'(x)\), provided these are defined.

- When is a product zero?

- When is a product positive or negative?

As well as making sure that \(f(g(x))\) is defined, we need to make sure that \(f'(g(x))\) and \(g'(x)\) are defined, so we need to keep an eye on the domains, ranges and derivatives of \(f(x)\) and \(g(x).\)

Here are a few more suggestions for separate parts of the problem.

Part (a)

How can we ensure that \(f'(g(x))g'(x)=0\) when \(x=-1\) and when \(x=5\)?

Do we only want stationary points at \(x=-1\) and \(x=5\) or will we allow others?

Part (b)

If a function has a local minimum when \(x=a\), what can we say about the sign of its derivative on either side of \(a\)?

If a function has a local minimum, try composing it with an increasing function. Now try composing it with a decreasing function.

Part (c)

What are some functions that have no stationary points?

What’s the simplest function that has no stationary points?

If a function has a local minimum when $x=a$, what can we say about the sign of its derivative on either side of $a$? If a function has a local minimum, try composing it with an increasing function. Now try composing it with a decreasing function.

What information about a function does a tangent give us? What if you choose the point where you want $y=2x+1$ to be a tangent? Think about some particular cases, e.g. try to find $f(x)$ if $g(x)=x^2$ or $g(x)=\sin x$ or $g(x)=\tan x$?

## Things you might have noticed

The [chain rule](https://undergroundmathematics.org/glossary/chain-rule) tells us that the derivative of \(f(g(x))\) is the product of \(f'(g(x))\) and \(g'(x)\), provided these are defined. How can we ensure \(f'(g(x))g'(x)=0\) at \(x=-1\) and \(x=5\)?

Note first that we could let \(f(x)\) or \(g(x)\) be the identity function and then try to ensure that either \(g(x)\) or \(f(x)\) has stationary points at \(x=-1\) and \(x=5.\) How could we do this?

We could let \(g'(x)=(x+1)(x-5)\), so that \(g(x)=\tfrac{1}{3}x^{3}-2x^{2}-5x+c\) where \(c\) is a constant. Changing \(c\) or rescaling parallel to the \(y\)-axis doesn’t change the \(x\)-values of the stationary points, so we could let \(g(x)=x^3-6x^2-15x\) instead.

We could also think about repeated roots of polynomials. For example, if we let \(g(x)=(x+1)^{2}(x-5)^2\) then we don’t have to integrate or differentiate anything.

At this point we may have to consider our interpretation of the problem. Do we only want stationary points at \(x=-1\) and \(x=5\) or will we allow others?

So far we have found functions that could be composed with the identity function. But what if we let \(g(x)\) be one of these and compose it with, say, \(f(x)=x+1\), \(f(x)=x^2\), \(f(x)=e^{x}\) or \(f(x)=\sin x\)? Is the composition \(f(g(x))\) defined and where are its stationary points?

Here are more functions that meet the conditions. Can you explain how they do this?

- \(g(x)=x^2\) and \(f'(x)=(x-1)(x-25)\)

- \(g(x)=x^2-10x\) and \(f(x)=(x-11)^2\)

- \(g(x)=(x+1)^2\) and \(f(x)=(x-36)^2\)

Some things to think about

If \(g(x)=x^2\) and \(f'(x)=(x-1)(x-25)\) then \(f'(g(x))=(x^2-1)(x^2-25).\)

If \(g(x)=x^2-10x\) and \(f(x)=(x-11)^2\), what happens to \(f(g(x))\) when \(g(x)=11\)?

If \(g(x)=(x+1)^2\) and \(f(x)=(x-36)^2\), where does \(f(g(x))\) have stationary points?

These examples offer a chance to combine calculus and algebra with thinking about functions and their graphs. What were the key things you noticed and how do these relate to the chain rule?

As long as $f(x)$ and $g(x)$ can be composed, we can ensure that $f'(g(-1))g'(-1)=0$ and $f'(g(5))g'(5)=0$ by making sure $g(x)$ has stationary points at $x=-1$ and $x=5.$ For example, we could let $g'(x)=(x+1)(x-5)$, so that $g(x)=\tfrac{1}{3}x^{3}-2x^{2}-5x+c$ where $c$ is a constant. Changing $c$ or rescaling parallel to the $y$-axis doesn't change the $x$-values of the stationary points, so we could take $c=0$ and multiply through by $3.$ We need to think about the domain and range of $g(x)$ because to ensure that the composite function $f(g(x))$ is defined. One approach is to let $f(x)=x$. For example, we could have $f(x)=x^2$ or $f(x)=e^{x}$ or $f(x)=\sin x.$ Suppose instead we had $g(x)=x^2$ and $f'(x)=(x-1)(x-25).$ What would $f(x)$ be and where are the stationary points of $f(g(x))$? What about $g(x)=x^2-10x$ and $f(x)=(x-11)^2$? Why would this satisfy the required conditions? If we allow ourselves to have other stationary points as well, we could take a different approach. For example, we could ensure that either $f(x)$ or $g(x)$ has stationary points

We need \(g(x)>0\) for all \(x\) in the domain of \(g(x)\) because otherwise \(\ln{g(x)}\) will not be defined. If we also want \(\ln{g(x)}\) to have a minimum, we need \(g(x)\) to have a stationary point, since \(\ln{x}\) has no stationary points. But what type of stationary point should it be?

If a function has a minimum when \(x=a\), what can we say about the sign of its derivative on either side of \(x=a\)?

The gradient is negative to the left of a local minimum and positive to the right of it.

For \(\ln{g(x)}\) to have a minimum at \(a\), we want its derivative to behave like this near \(a.\)

We already know from the chain rule that the derivative of \(\ln{g(x)}\) is the product of the derivative of \(\ln{x}\) at \(g(x)\) and the derivative of \(g(x).\) But since \(\ln{x}\) is an increasing function, the sign of the derivative of \(\ln{g(x)}\) is the same as the sign of \(g'(x).\)

Therefore we are looking for a function \(g(x)\) which has at least one local minimum and is always positive. One example could be \(g(x)=1+x^2.\) What other examples can you find?

Functions of the form \(\ln{g(x)}\) arise as integrals of \(\tfrac{g'(x)}{g(x)}.\) Which functions are of the form \(\tfrac{g'(x)}{g(x)}\)?

The derivative of \(f(g(x))\) is \(f'(g(x))g'(x)\). How can we ensure that a product is zero?

If we want to ensure that \(f(g(x))\) does not have any stationary points, we could choose \(g(x)\) and \(f(x)\) with no stationary points, as long as \(f(x)\) and \(g(x)\) can be composed.

What are some functions that have no stationary points?

What’s the simplest function that has no stationary points?

The simplest function with no stationary points is the identity function and if we let \(g(x)=x\) and \(f(x)=x\) we get \(f(g(x))=x\), which has no stationary points.

Broadening our search out to other functions with no stationary points, we could take any function of the form \(ax+b\) if \(a\neq0\), or we could have \(e^x\), \(\ln{x}\), \(\tan x\), \(\sqrt[3]{x}\), \(x^3+x\) or even \(2x+\sin x.\) What happens if we try to compose some of these functions?

As this problem can be solved by composing functions that don’t have stationary points, it seems worth thinking about whether \(g(x)\) or \(f(x)\) could have stationary points.

For example, we could choose a \(g(x)\) without stationary points, but \(f(x)\) with stationary points that are outside the range of \(g(x).\) An example is \(g(x)=e^x\) and \(f(x)=x^2.\) Alternatively, if \(g(x)\) has a stationary point at \(x=a\) but \(f(g(a))\) is not defined, we can exclude \(a\) from the domain of \(f(g(x)).\) For example, \(g(x)=x^2\) for \(x\neq 0\) and \(f(x)=\ln{x}.\)

One final example worth mentioning is \(g(x)=x^3\) and \(f(x)=\sqrt[3]{x}.\) Here \(f(g(x))=x\), which has no stationary points, even though \(g'(0)=0.\) How could this be explained?

If we use the chain rule to differentiate \(f(g(x))\) for \(x\neq 0\), then we obtain \(1\) as expected. Problems arise at \(x=0\) though, because the gradient of \(\sqrt[3]{x}\) is not defined when \(x=0.\) This means that the expression \(f'(g(0))g'(0)\) is not defined at \(x=0\), so we can’t use the chain rule to find the gradient function of \(f(g(x))\) here. However, the gradient function does exist at \(x=0\) because \(f(g(x))=x\) for all \(x\), so its gradient function must be \(1\) everywhere.

Inverse functions and their derivatives can be is explored further in [Reflecting on change](https://undergroundmathematics.org/chain-rule/reflecting-on-change).

Thinking again about the example of $f(x)=\ln{x}$ and $g(x)=e^x$ might suggest some other functions which are inverses of each other, and in particular, $g(x)=x^3$ and $f(x)=\sqrt[3]{x}.$ Then $g(x)$ has a stationary point but $f(g(x))$ does not. The way inverse functions and their derivatives behave is explored further in [Reflecting on change](/chain-rule/reflecting-on-change).

If we want to ensure that $f(g(x))$ does not have any stationary points, we could choose $g(x)$ so that $g'(x)\neq 0$ for all $x$ in the domain of $g$ and $f'(x)\neq 0$ for all $x$ in the range of $g.$ We'd also need to make sure that $f(x)$ and $g(x)$ can be composed.

(c) ... functions $f(x)$ and $g(x)$ so that $f(g(x))$ has no stationary points?

The derivative of $f(g(x))$ is $f'(g(x))g'(x)$. When can a product be zero?

If we want to ensure that $f(g(x))$ does not have stationary points, we could choose a $g(x)$ so that $g'(x)\neq 0$ for all $x$ in the domain of $g$ and $f'(x)\neq 0$ for all $x$ in the range of $g.$ We'd also need to make sure that $f(x)$ and $g(x)$ can be composed.

What's the simplest function that has no stationary points?

Any function of the form $ax+b$ has no stationary points if $a\neq0.$ Other examples of functions without stationary points are $e^x$ and $\ln{x}$, $\dfrac{1}{x}$ and $x^3+x.$ What happens if we try to compose some of these functions? We could choose $f(x)$ and $g(x)$ to be functions with no stationary points to ensure that $f(g(x))$ doesn't. For example, we could let $f(x)=e^x$ and $g(x)=x+2.$ What if we chose $f(x)=\ln{x}$ instead? Alternatively, we could let $f(x)=\ln{x}$ and $g(x)=e^x.$ Why do we know that this doesn't have stationary points?

If we were less cautious and allowed $f(x)$ to have stationary points, we could have $f(x)=x^2$ and $g(x)=e^x.$ Can you think of other functions which have stationary points but whose composition does not? Thinking again about the example of $f(x)=\ln{x}$ and $g(x)=e^x$ might suggest some other functions which are inverses of each other, and in particular, $g(x)=x^3$ and $f(x)=\sqrt[3]{x}.$ Then $g(x)$ has a stationary point but $f(g(x))$ does not. The way inverse functions and their derivatives behave is explored further in [Reflecting on change](/chain-rule/reflecting-on-change).

When is a product of functions positive?

If $g(x)=e^{-x}$ and $f(x)=\dfrac{1}{x}$, what is $f(g(x))$ and how does it behave? Suppose instead we have $g(x)=\dfrac{1}{x}$ and $f(x)=-x^3$.

(d) ... a function $f(x)$ so that $f(\ln{x})$ has a local minimum when $x=3$?

(d) ... functions $f(x)$ and $g(x)$ so that $f(g(x))$ has a local maximum where $g(x)$ has a local minimum?

Why was it important in part (c) that $\ln{x}$ is an increasing function?

Suppose we let $g(x)= x^2+1.$ Then $g(x)$ has a minimum when $x=0$, so $g'(x)<0$ for $x<0$ and $g'(x)>0$ for $x>0$. Therefore we need $f'(x)$ to be defined around $x=1$, and to be negative on either side of $1$, i.e. we need $f(x)$ to be a decreasing function near $x=1.$ For example, we could have $f(x)=\dfrac{1}{x}$ or $f(x)=e^{-x}$ or $f(x)=-x$ or even $f(x)=-x^2.$ How could you check that the stationary point at $x=0$ is a maximum in each case?

There are lots of options for $f(x)$ if we take $g(x)=x^2+1$, but can you explain why $f(x)=(x-2)^2$ would satisfy the required conditions but $x^2$ would not?

<cm-chalk> How would your approach to (d) have been different if we'd asked for $f(g(x))$ to have a maximum where $f(x)$ has a minimum? </cm-chalk> <cm-qwell> (e) ... functions $f(x)$ and $g(x)$ so that $y=2x+1$ is a tangent to $y=f(g(x)).$ </cm-qwell> The question doesn't specify where $y=2x+1$ is a tangent, so we get to choose this. Let's say it's at $x=a.$ Working backwards from the equation of the tangent, we must have $f'(g(a))g'(a)=2$ and $f(g(a))=2a+1$. Let's consider the example $g(x)=\tan x.$ We know quite a few nice values of $\tan x$ which could be candidates for $a$ and we can work out the corresponding values of $\sec^2 x$ which is $g'(x).$ For example, $\tan 0=0$ and $\sec^2 0=1$, or $\tan \tfrac{\pi}{4}=1$ and $\sec^2 \tfrac{\pi}{4}=2$, so we could choose either $a=0$ or $a=\tfrac{\pi}{4}.$ If we choose $a=0$ then we'll need to find an $f(x)$ for which $f'(0)=2$ and if we choose $\tfrac{\pi}{4}$, we'll need $f'(1)=1.$ Note that in the first case we could choose $f(x)=2x+1$! If we choose $a=\tfrac{\pi}{4}$, how can we construct a suitable function for $f(x)$? We need to ensure that the tangent and graph meet at $x=\tfrac{\pi}{4}.$ <cm-chalk> What could $g(x)$ be if instead we made $f(x)=\tan x$? </cm-chalk> <!-- Since $\tan x$ has a gradient of $1$ when $x=0$ and the tangent we are aiming at has a gradient of $2$, we can find an $f(x)$ which will stretch and translate $\tan x$ appropriately, and one such function would be $f(x)=2x+1$. Alternatively we could look for a place on $\tan x$ which has a gradient of $2$: When $g(x)=\tan x$, $$g'(x)=\sec^2(x)$$ $g'(x)=2$ when $\sec x=\sqrt{2}$ so $\cos x=\frac{1}{\sqrt{2}}$ giving $x=\pm \frac{\pi}{4}$. If we look at the point where $x=\frac{\pi}{4}$, here $y=\tan {\frac{\pi}{4}}=1$ and gradient is $2$. If we find the equation of a line through this point we get $y-1=2(x-\frac{\pi}{4})$ or $y=2x-\frac{\pi}{2}+1$ so if we translate our tangent curve by $\frac{\pi}{2}$ we have another solution: $g(x)=\tan x$ and $f(x)=x+\frac{\pi}{2}$.
