---
created: 2026-10-26T02:40:04 (UTC +06:00)
source: https://undergroundmathematics.org/chain-rule/integral-sorting
author: Underground Mathematics (University of Cambridge)
rights: © University of Cambridge (Underground Mathematics). Use inside SyllabAI is authorised by the
  operator attestation of 2026-10-23 — see LICENSE-DATA.md (Amendment 2026-10-23) in this repository.
  Takedown / correction handling as stated in LICENSE-DATA.md.
tags:
- underground-mathematics
- chain-rule
- type/fluency-exercise
resource_identity:
  ugm_id: integral-sorting
  station: chain-rule
  station_title: Chain Rule & Integration by Substitution
  resource_type_id: 8
  resource_type_label: Fluency exercise
  level: Developing
  ref: 6859
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
  - code: 3.5.6
    provenance:
      tier: AI_SUGGESTED
      confidence: high
      model_version: GLM (Super Z agent, z.ai) — P3c lane-13 cross-map (cross-map-p3-integration.json
        (P3c lane 13) @ syllabai-experimental 21845f3)
      evidence: eight integrals matched to answers with the substitution named for each (u = 1-9x^2, u
        = x^3-3x, ...) and the pairs sorted by technique - the substitution-fluency resource; the arcsin/beyond-list
        cards disclosed of record (flips the lane-12 non-overlap row of record routed 'P3 3.5 Integration')
      rationale: 'Canonical UGM title: Integral sorting'
      validation_status: SUGGESTED
    title: use a given substitution to simplify and evaluate e.g. to integrate either a definite or an
      indefinite integral.
  mapped_date: '2026-10-26'
  mapper: cross-map-p3-integration.json (P3c lane 13) @ syllabai-experimental 21845f3
provenance:
  capture_date: '2026-10-22'
  capture_tool: P2 full-site crawl (ugm-crawl) → ugm-clean extraction; text-only import
  content_language: en
  task: T-UGM-IMPORT-13
---

# Integral sorting

> Excerpt: Students are asked to pair up cards containing integrals and their answers, as well as find a suitable substitution that could be used to solve the integral.

## Problem

Below are 8 integrals and their solutions. Can you:

- match up the [cards](https://undergroundmathematics.org/chain-rule/integral-sorting/components/cards.pdf) and fill in the blanks?

- write down a substitution that could have been used to solve each integral?

- sort the pairs into groups. What features could be used to define the groups?

\(\displaystyle{\int 9x\sqrt{1-9x^2} \, dx}\)

\(\displaystyle{\int \dfrac{x^2-1}{(x^3 - 3x)^2} \, dx}\)

\(\displaystyle{\int \dfrac{1}{\sqrt{1-9x^2}} \, dx}\)

\(\displaystyle{\int \dfrac{9x}{\sqrt{1-9x^2}} \, dx}\)

\(\displaystyle{\int \dfrac{6-6x^2}{x^3 - 3x} \, dx}\)

\(\displaystyle{\int \dfrac{\cos x}{\sin^3 x} \, dx}\)

\(\displaystyle{\int \dfrac{\cos x}{\sin x} \, dx}\)

\(\dfrac{-1}{2\sin^2x}+c\)

\(\frac{2}{9} (x^3 - 3x)^{3/2} +c\)

\(\ln{|\sin x|}+c\)

\(\frac{1}{3}\arcsin 3x +c\)

\(\dfrac{-1}{3(x^3-3x)}+c\)

\(-\frac{1}{3}\left(1-9x^2\right)^{\frac{3}{2}} +c\)

\(-2\ln{|x^3-3x|}+c\)

## Solution

In some of the integrals there are similar expressions we could use for sorting. B and F both contain \(x^3 - 3x\), as do the solutions 2, 6 and 8. To match them we could try to integrate B and F, or differentiate 2, 6 and 8. We find that we can pair them up, and that card 2 differentiates to \(\frac{1}{3}(x^3-3x)^{1/2}(3x^2-3)\) which must match the blank card C.

\(\displaystyle{\int \dfrac{x^2-1}{(x^3 - 3x)^2} \, dx}\)

\(\dfrac{-1}{3(x^3-3x)}+c\)

\(\displaystyle{\int \dfrac{6-6x^2}{x^3 - 3x} \, dx}\)

\(-2\ln{|x^3-3x|}+c\)

\(\displaystyle{\int {(x^2-1)}\sqrt{x^3 - 3x} \, dx}\)

\(\frac{2}{9} (x^3 - 3x)^{3/2} +c\)

To help us find the correct substitutions let us think about the chain rule. We should be familiar with how we differentiate a composite function.

\[\dfrac{d}{dx} \Big(g(f(x))\Big) = g'(f(x))\times f'(x)\]

If we integrate both sides we can write

\[g(f(x)) = \int g'(f(x))\times f'(x) \, dx.\]

This integral is made up of a composite function multiplied by the differential of the inner function.

If you spot this pattern in an integral, you may be able to integrate it by inspection without needing to substitute. However, as integrals get more complex, it will help to find a substitution that will reduce the integral to \[g(u) = \int g'(u) \, du.\]

Taking a closer look at the integrals above, we find that B, C and F all include a function of \(x^3 - 3x\), as well as a multiple of \(3x^2 - 3\), which is the derivative of \(x^3 - 3x\). This suggests that the substitution \(u = x^3 - 3x\) will work for all three integrals.

Try using this substitution to check that it works. Are there any other options for the substitution?

Now let’s look at the integrals which involve trigonometric functions.

\(\displaystyle{\int \dfrac{\cos x}{\sin^3 x} \, dx}\)

\(\dfrac{-1}{2\sin^2x}+c\)

\(\displaystyle{\int \dfrac{\cos x}{\sin x} \, dx}\)

\(\ln{|\sin x|}+c\)

For G we see that \(\dfrac{1}{\sin^3 x}\) is the composite function. As \(\sin^3 x\) is more clearly written as \((\sin x)^3\) we see that \(\sin x\) is the inner function and so \(u = \sin x\) is a suitable substitution.

For H it is less obvious, but remember \(\dfrac{1}{\sin x}\) is a composite function of \(\dfrac{1}{x}\) and \(\sin x\), so we can use the same substitution of \(u = \sin x\).

Why can’t we use the substitution \(u = \cos x\)? What happens if we do?

Our final three cards match up like this:

\(\displaystyle{\int 9x\sqrt{1-9x^2} \, dx}\)

\(-\frac{1}{3}\left(1-9x^2\right)^{\frac{3}{2}} +c\)

\(\displaystyle{\int \dfrac{1}{\sqrt{1-9x^2}} \, dx}\)

\(\frac{1}{3}\arcsin 3x +c\)

\(\displaystyle{\int \dfrac{9x}{\sqrt{1-9x^2}} \, dx}\)

\(-\sqrt{1-9x^2} +c\)

A and E are similar problems with composite functions \(\sqrt{1-9x^2}\) and \(\dfrac{1}{\sqrt{1-9x^2}}\). For both, a suitable substitution is \(u = 1-9x^2\). This allows us to complete the blank card 5 to match with E.

D also includes \(\dfrac{1}{\sqrt{1-9x^2}}\), but not the derivative of \(1-9x^2\). What happens if you try the substitution \(u = 1-9x^2\)?

For this type of integral a trigonometric substitution is useful since \(\sin^2 x + \cos^2 x =1\). One possible substitution is \(3x = \sin u.\)

- How is this different from the other substitutions that have been used?

- Would it matter if you used \(x = \sin u\) or \(3x = \cos u\) instead?

Rather than focusing on the expressions the integrals contained we could think about the structure of each integral.

\(\displaystyle{\int \dfrac{6-6x^2}{x^3 - 3x} \, dx}\)

\(\displaystyle{\int \dfrac{\cos x}{\sin x} \, dx}\)

\(\displaystyle{\int \dfrac{x^2-1}{(x^3 - 3x)^2} \, dx}\)

\(\displaystyle{\int \dfrac{9x}{\sqrt{1-9x^2}} \, dx}\)

\(\displaystyle{\int \dfrac{\cos x}{\sin^3 x} \, dx}\)

\(\displaystyle{\int 9x\sqrt{1-9x^2} \, dx}\)

\(\displaystyle{\int {(x^2-1)}\sqrt{x^3 - 3x} \, dx}\)

\(\displaystyle{\int \dfrac{1}{\sqrt{1-9x^2}} \, dx}\)

What are the features of each group?

Can you write down a different integral that would fit into each group?
