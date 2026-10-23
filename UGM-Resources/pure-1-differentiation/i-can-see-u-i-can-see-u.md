---
created: 2026-10-24T01:49:53 (UTC +06:00)
source: https://undergroundmathematics.org/chain-rule/i-can-see-u
author: Underground Mathematics (University of Cambridge)
rights: © University of Cambridge (Underground Mathematics). Use inside SyllabAI is authorised by the
  operator attestation of 2026-10-23 — see LICENSE-DATA.md (Amendment 2026-10-23) in this repository.
  Takedown / correction handling as stated in LICENSE-DATA.md.
tags:
- underground-mathematics
- chain-rule
- type/fluency-exercise
- level/developing
resource_identity:
  ugm_id: i-can-see-u
  station: chain-rule
  station_title: Chain Rule & Integration by Substitution
  resource_type_id: 8
  resource_type_label: Fluency exercise
  level: Developing
  ref: 6535
  old_site_id: null
spec_map:
  curriculum_code: CIE-9709-P1-2023
  lane: cie-a-level-maths-20-pure-1
  board: Cambridge CIE
  syllabus_version: 2023-2025
  subsection: chain-rule
  subsection_provenance:
    tier: PROVIDER
    signal: source-url-slug
    slug: chain-rule
    validation_status: SUGGESTED
  spec_points:
  - code: 1.7.2
    provenance:
      tier: AI_SUGGESTED
      confidence: high
      model_version: GLM (Super Z agent, z.ai) — P3c lane-7 cross-map (cross-map-differentiation.json
        (P3c lane 7) @ syllabai-experimental 93575e69)
      evidence: identify the inner function for (2x+3)^-2-style composites and differentiate dy/dx —
        the P1 linear-inner chain-rule clause in fluency form
      rationale: 'Canonical UGM title: "I can see $u$!"'
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
- path: https://undergroundmathematics.org/chain-rule/i-can-see-u/download/teacher-notes.pdf
  kind: printable
---

# I can see $u$!

> Excerpt: Students are asked to identify a suitable $u$ or ‘inner function’ for each of the given functions and then find $\tfrac{dy}{dx}.$ Different ways of rewriting the expressions involved may lead to alternative options for $u.$

## Problem

If \(u=2x+1\) and \(y=u^3\) what is \(y\) as a function \(x\)?

Working backwards, if \(y=(2x+3)^{-2}\), how could you express \(y\) as a function of \(u\) where \(u\) is a function of \(x\)?

If you also wanted to work out \(\dfrac{dy}{dx}\), how would this affect your choice of \(u\)?

Take a look at the functions in the table below.

Write \(y\) as a function of \(u\) where \(u\) is a function of \(x\) so that you can use these to find \(\dfrac{dy}{dx}.\)

You may be able to do this in more than one way.

| \(y=(5-2x)^3\) | \(y=\sqrt{3x-1}\) | \(y=\dfrac{5}{\sqrt{x}}\) |
|---|---|---|
| \(y=9x^2-6x+1\) | \(y=e^{5x}\) | \(y=\ln{3x}\) |
| \(y=\dfrac{1}{x^2+4x+4}\) | \(y=e^{x+4}\) | \(y=\ln{x^2}\) |
| \(y=\cot x\) | \(y=x\) | \(y=\ln{x^2}+\ln{8x}\) |
| \(y=\sin x^2\) | \(y=\tan x (\sec^2 x-1)\) | \(y=\tfrac{1}{2}(1-\cos 2x)\) |

## Solution

If \(u=2x+1\) then substituting \(2x+1\) for \(u\) in \(y=u^3\) gives \(y=(2x+1)^3.\)

Looking at \(y=(2x+3)^{-2}\), I might describe it as “one over something squared”, so one option is to let the “something” be \(u.\) In a function machine for \(y\), the squaring could happen before or after taking the reciprocal, giving further options.

Here are some possibilities for writing \(y\) as a function of \(u\) where \(u\) is a function of \(x.\)

- \(y=u^{-2}\) and \(u=2x+3\)

- \(y=u^{-1}\) and \(u=(2x+3)^2\)

- \(y=u^2\) and \(u=(2x+3)^{-1}\)

However, there is no reason why \(y\) can’t be the identity function of \(u\) or \(u\) can’t be the identity function of \(x\), so there are two other possibilities.

- \(y=(2u+3)^{-2}\) and \(u=x\)

- \(y=u\) and \(u=(2x+3)^{-2}\)

If you also wanted to work out \(\dfrac{dy}{dx}\), how would this affect your choices of \(u\)?

As \(y\) is a function of a function, I can use the [chain rule](https://undergroundmathematics.org/glossary/chain-rule) to differentiate it if I can find \(\dfrac{dy}{du}\) and \(\dfrac{du}{dx}.\) Can I do this for all the possibilities I found for \(u\)?

For the first case I can find \(\dfrac{dy}{du}\) and \(\dfrac{du}{dx}\) directly. In the second and third cases, I can find \(\dfrac{dy}{du}\) but need to think a bit more about how I could differentiate \(u.\) The chain rule could help, or I could look at [Slippery slopes …. another derivative](https://undergroundmathematics.org/chain-rule/slippery-slopes-another-derivative) to help me. differentiate $(2x+3)^{-1}.$

The final two cases don’t help me either because I’d need the chain rule to find \(\dfrac{dy}{du}\) or \(\dfrac{du}{dx}.\)

I can tackle these functions in any order, but scanning the table suggests a few ways to group the functions. As in the previous example, I could use the identity function and say either \(y=u\) or \(u=x\), but this won’t necessarily help me to find \(\dfrac{dy}{dx}\), so I’ll need to look for other options in most cases. I’ll find possibilities for \(u\) first then try to differentiate. There is a table with suggestions for \(u\) and expressions for \(\dfrac{dy}{dx}\) at the end of this section.

**Possibilities for \(u\)**

Powers of a linear polynomial

The functions in the top row are all powers of a linear polynomial. This makes me wonder if I could also express \(9x^2-6x+1\) and \(\dfrac{1}{x^2+4x+4}\) as powers of a linear polynomial.

For \(y=\dfrac{1}{x^2+4x+4}\) I can choose \(u=x+2\) and \(y=u^{-2}.\) But I could also choose \(u=(x+2)^2\) and \(y=\dfrac{1}{u}.\) If I now look at \(\dfrac{5}{\sqrt{x}}\) with this in mind, I notice that it can also be written as \(\sqrt{\dfrac{25}{x}}.\) How does this affect my choices for \(u\)?

Exponential and logarithmic functions

Several functions in the table involve either exponential or logarithmic functions and I can see more than one \(u\) for several of these functions. For example, \(e^{5x}\) could be thought of as \(5x\) composed with \(e^x\), but also as \(e^{x}\) composed with \(x^5.\) In a similar way, rewriting the logarithms may help me to see different possibilities for \(u.\) However, if I am rewriting expressions, I need to think about which values of \(x\) the original expression is defined for, and whether my new expression is also defined for all these values of \(x.\) For example, where are \(\ln{x^2}\) and \(2\ln{x}\) defined?

The logarithms in \(y=\ln{x^2}+\ln{8x}\) can be combined and separated in different ways, including \(\ln{8x^3}\), \(\ln{(2x)^3}\) and \(3\ln{2x}\), which gives me lots of options for \(u.\)

Trigonometric functions

Looking now at the trigonometric functions at the bottom left of the table, I can see that \(\sin x^2\) is a function of \(x^2.\) But how can \(y=\cot x\) be treated as a composition of functions? I recall that \(\cot x=\dfrac{1}{\tan x}\), which gives me an idea for \(u.\)

The other functions look a bit more complicated, and I may need to rewrite them using identities. For example, \(\sec^2 x=1+\tan^2 x\) so maybe I can express \(\tan x (\sec^2 x-1)\) in terms of \(\tan x.\)

I can think of \(\tfrac{1}{2}(1-\cos 2x)\) as a function of \(\cos 2x\), or of \(2x\), but I also recognise it from the [double angle formulae](https://undergroundmathematics.org/glossary/double-angle-formula), where \(\tfrac{1}{2}(1-\cos 2x)=\sin^2 x.\) This looks like a very different function!

The identity function

The only remaining function in the table is \(y=x\), which looks like the simplest function in the table. I could have included \(y=x\) in the powers of linear polynomials group, but there may be some other ways of thinking about it.

As a first step, I can think about the function that has no effect on its inputs: the identity function. So I can let \(u=x\) and then I need \(y=u.\)

Looking around the table gives me an idea. I need the composition of two functions to have no effect, but each of the functions can change its inputs into something else. For example, I could let \(u=e^x\) and have \(y=\ln{u}.\) Similarly, provided \(x\neq 0\), I could let \(u=\dfrac{1}{x}\) and \(y=\dfrac{1}{u}.\) I need to be careful about the domains, but what other functions could I choose?

Looking back, I realise that almost all of the functions in the table can be thought of as a composition of a linear polynomial and another function. It may be interesting to think about how this affects their derivatives.

I also notice that I could think of a few of these functions as a composition of three functions. For example, for \(y=\dfrac{1}{x^2+4x+4}\) I could have had \(u=x+2\), \(v=u^2\) and \(y=\dfrac{1}{v}.\) Which others could I break down using three functions instead of two? How do I differentiate a composition of three functions?

**Finding the derivatives**

Also work out $\dfrac{dy}{dx}$ in each case. How does your choice of $u$ affect how you find $\dfrac{dy}{dx}$?

I can use the chain rule to differentiate these functions. But as I found earlier, some of the possibilities for \(u\) may not be as helpful as others. Do I know how to find $\dfrac{dy}{du}$ and $\dfrac{du}{dx}$ for all the possibilities I found for $u$?

Derivatives of the powers of linear polynomials

For the powers of linear polynomials, I’ll just consider a few examples.

For \(y=(5-2x)^3\), \(u\) could be \(5-2x\) and then \(y=u^3.\) Applying the chain rule gives \(\dfrac{dy}{dx}=3u^2 \cdot -2=-6(5-2x)^2\), so the \(-2\) from \(5-2x\) is acting as a scale factor in the derivative. If I had \((ax+b)^3\) instead, what could I choose as \(a\) and \(b\) if I didn’t want to introduce a scale factor in the derivative like this?

Earlier I found that I could write \(y=9x^2-6x+1\) as a composition of functions, but I already know how to differentiate it directly, so I could just take \(y=u\) and \(u=9x^2-6x+1\). How does differentiating \(y=9x^2-6x+1\) using these different functions compare with differentiating it directly?

Again, I can differentiate \(y=\dfrac{5}{\sqrt{x}}\) directly, so I could have taken \(y=u\) and \(u=\dfrac{5}{\sqrt{x}}.\) If instead I differentiate \(y\) using \(u=\sqrt{x}\) and \(y=\dfrac{5}{u}\) then I get \[\dfrac{dy}{dx}=\dfrac{-5}{u^2}\cdot \dfrac{1}{2\sqrt{x}}=\dfrac{-5}{2x^{3/2}}\]

but what happens if I use \(u=\dfrac{25}{x}\) and \(y=\sqrt{u}\) instead?

Derivatives of the exponential and logarithmic functions

I saw two different possibilities for \(u\) for \(e^{5x}\) and \(e^{x+4}\) and one might make the differentiation simpler than the other.

I also noticed that \(e^{5x}\) and \(e^{x+4}\) are both functions of linear polynomials, so when I differentiate them using the chain rule will I see the same effect of scale factors in the derivatives as I found for powers of linear polynomials?

Differentiating \(y=\ln{3x}\) using \(u=3x\) and \(y=\ln{u}\) gives me \[\dfrac{dy}{dx}=\dfrac{1}{u}\cdot 3=\dfrac{1}{x}\] which seems surprising. I might have expected a scale factor of \(3\) in the derivative, but looking at my other option for \(u\) helps to confirm that my derivative is correct. Another thing to think about is that \(y=\ln{3x}\) is the inverse of an exponential function and I have already differentiated some exponential functions. What is the inverse of \(y=\ln{3x}\) and how could I use its derivative to find the derivative of \(y=\ln{3x}\)?

Looking now at \(y=\ln{x^2}\), I can use \(u=x^2\) and \(y=\ln{u}\) to give \[\dfrac{dy}{dx}=\dfrac{1}{u}\cdot 2x=\dfrac{2}{x}\] but what if I had rewritten \(y\) as \(y=2\ln{x}\) instead?

Turning now to \(y=\ln{x^2}+\ln{8x}\), I have lots of options for \(u\) based on different ways of rewriting \(\ln{x^2}+\ln{8x}\) and some may help me to differentiate the function more simply than others. However, having differentiated \(y=\ln{x^2}\) and \(y=\ln{3x}\), I can already conjecture what the derivative of \(y=\ln{x^2}+\ln{8x}\) is.

Derivatives of the trigonometric functions

Again, I’ll just consider a couple of examples.

Using \(u=\tan x\) and \(y=\dfrac{1}{u}\) to differentiate \(y=\cot x\) gives \[\dfrac{dy}{dx}=\dfrac{-1}{u^2}\cdot \sec^{2}x=\dfrac{-\sec^2 x}{\tan^2 x}\] and writing this in terms of \(\sin x\) and \(\cos x\) could help show how this could be simplified.

I had lots of options for \(u\) for \(y=\tfrac{1}{2}(1-\cos 2x)\), but the first was \(u=\cos 2x\), which I could differentiate using the chain rule or ideas from [Sine stretching](https://undergroundmathematics.org/calculus-trig-log/sine-stretching). Alternatively I could use \(u=2x\) and \(y=\tfrac{1}{2}-\tfrac{1}{2}\cos u\) since then I can can find \(\dfrac{dy}{du}\) directly. Both of these lead me to \(\dfrac{dy}{dx}=\sin 2x.\)

But I also noticed that I can write \(\tfrac{1}{2}(1-\cos 2x)\) as \(\sin^2 x.\) How does using \(u=\sin x\) and \(y=u^2\) lead to the same derivative as the other routes?

Derivative of the identity function

I already know the derivative, but what happens if I write \(y=u\) and \(u=x\) and use the chain rule?

How do the different possibilities for writing \(y=x\) as a composition of functions lead to this same result?

What other expressions could be seen as a composition of functions? Can you suggest some that you can also differentiate? Are there different options for \(u\) as there were with many of the functions in this table?

| \(y=(5-2x)^3\) | \(y=\sqrt{3x-1}\) | \(y=\dfrac{5}{\sqrt{x}}\) |
|---|---|---|
| \(u=5-2x\) and \(y=u^3\) | \(u=3x-1\) and \(y=\sqrt{u}\) | \(u=\sqrt{x}\) and \(y=\dfrac{5}{u}\) or \(u=\dfrac{25}{x}\) and \(y=\sqrt{u}\) |
| \(\dfrac{dy}{dx}=-6(5-2x)^2\) | \(\dfrac{dy}{dx}=\dfrac{3}{2\sqrt{3x-1}}\) | \(\dfrac{dy}{dx}=\dfrac{-5}{2x^{3/2}}\) |
| \(y=9x^2-6x+1\) | \(y=e^{5x}\) | \(y=\ln{3x}\) |
| \(u=3x-1\) and \(y=u^2\) | \(u=5x\) and \(y=e^u\) or \(u=e^x\) and \(y=u^5\) | \(u=3x\) and \(y=\ln{u}\) or \(u=\ln{x}\) and \(y=u+\ln{3}\) |
| \(\dfrac{dy}{dx}=6(3x-1)\) | \(\dfrac{dy}{dx}=5e^{5x}\) | \(\dfrac{dy}{dx}=\dfrac{1}{x}\) |
| \(y=\dfrac{1}{x^2+4x+4}\) | \(y=e^{x+4}\) | \(y=\ln{x^2}\) |
| \(u=x+2\) and \(y=u^{-2}\) or \(u=(x+2)^2\) and \(y=\dfrac{1}{u}\) | \(u=x+4\) and \(y=e^x\) or \(u=e^x\) and \(y=e^{4}u\) | \(u=x^2\) and \(y=\ln{u}\) or \(u=\ln{x}\) and \(y=2u\) if \(x>0\) |
| \(\dfrac{dy}{dx}=-2(x+2)^{-3}\) | \(\dfrac{dy}{dx}=e^{x+4}\) | \(\dfrac{dy}{dx}=\dfrac{2}{x}\) |
| \(y=\cot x\) | \(y=x\) | \(y=\ln{x^2}+\ln{8x}\) |
| \(u=\tan x\) and \(y=\dfrac{1}{u}\) | \(u=x\) and \(y=u\) or \(u=e^x\) and \(y=\ln{u}\) | \(u=8x^3\) and \(y=\ln{u}\) or \(u=2x\) and \(y=3\ln{u}\) or \(u=\ln{x}\) and \(y=3u+3\ln{2}\) |
| \(\dfrac{dy}{dx}=-\cosec^2 x\) | \(\dfrac{dy}{dx}=1\) | \(\dfrac{dy}{dx}=\dfrac{3}{x}\) |
| \(y=\sin x^2\) | \(y=\tan x (\sec^2 x-1)\) | \(y=\tfrac{1}{2}(1-\cos 2x)\) |
| \(u=x^2\) and \(y=\sin u\) | \(u=\tan x\) and \(y=u^3\) | \(u=\cos 2x\) and \(y=\tfrac{1}{2}-\tfrac{1}{2}u\) or \(u=2x\) and \(y=\tfrac{1}{2}-\tfrac{1}{2}\cos u\) or \(u=\sin x\) and \(y=u^2\) |
| \(\dfrac{dy}{dx}=2x\cos x^2\) | \(\dfrac{dy}{dx}=3\tan^2 x \sec^2 x\) | \(\dfrac{dy}{dx}=2\sin x \cos x=\sin 2x\) |
