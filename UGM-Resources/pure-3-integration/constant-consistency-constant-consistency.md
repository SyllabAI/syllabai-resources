---
created: 2026-10-26T02:40:04 (UTC +06:00)
source: https://undergroundmathematics.org/product-rule/constant-consistency
author: Underground Mathematics (University of Cambridge)
rights: © University of Cambridge (Underground Mathematics). Use inside SyllabAI is authorised by the
  operator attestation of 2026-10-23 — see LICENSE-DATA.md (Amendment 2026-10-23) in this repository.
  Takedown / correction handling as stated in LICENSE-DATA.md.
tags:
- underground-mathematics
- product-rule
- type/many-ways-problem
resource_identity:
  ugm_id: constant-consistency
  station: product-rule
  station_title: Product Rule & Integration by Parts
  resource_type_id: 4
  resource_type_label: Many ways problem
  level: Developing
  ref: 6507
  old_site_id: null
spec_map:
  curriculum_code: CIE-9709-P3-2023
  lane: cie-a-level-maths-20-pure-3
  board: Cambridge CIE
  syllabus_version: 2023-2025
  subsection: product-rule
  subsection_provenance:
    tier: PROVIDER
    signal: source-url-slug
    slug: product-rule
    validation_status: SUGGESTED
  spec_points:
  - code: 3.5.2
    provenance:
      tier: AI_SUGGESTED
      confidence: high
      model_version: GLM (Super Z agent, z.ai) — P3c lane-13 cross-map (cross-map-p3-integration.json
        (P3c lane 13) @ syllabai-experimental 21845f3)
      evidence: INT cos x sin x dx three ways - the sin 2x identity route (3.5.2), the u = cos x substitution
        route (3.5.6), the parts route (3.5.5) - and the constant-discrepancy reconciliation; the canonical
        many-ways integration resource (flips the lane-11 non-overlap row of record routed 'P3 3.5 Integration')
      rationale: 'Canonical UGM title: Constant consistency'
      validation_status: SUGGESTED
    title: use trigonometrical relationships in carrying out integration or
  - code: 3.5.5
    provenance:
      tier: AI_SUGGESTED
      confidence: high
      model_version: GLM (Super Z agent, z.ai) — P3c lane-13 cross-map (cross-map-p3-integration.json
        (P3c lane 13) @ syllabai-experimental 21845f3)
      evidence: INT cos x sin x dx three ways - the sin 2x identity route (3.5.2), the u = cos x substitution
        route (3.5.6), the parts route (3.5.5) - and the constant-discrepancy reconciliation; the canonical
        many-ways integration resource (flips the lane-11 non-overlap row of record routed 'P3 3.5 Integration')
      rationale: 'Canonical UGM title: Constant consistency'
      validation_status: SUGGESTED
    title: recognise when an integrand can usefully be e.g. integration of regarded as a product, and
      use integration by parts
  - code: 3.5.6
    provenance:
      tier: AI_SUGGESTED
      confidence: high
      model_version: GLM (Super Z agent, z.ai) — P3c lane-13 cross-map (cross-map-p3-integration.json
        (P3c lane 13) @ syllabai-experimental 21845f3)
      evidence: INT cos x sin x dx three ways - the sin 2x identity route (3.5.2), the u = cos x substitution
        route (3.5.6), the parts route (3.5.5) - and the constant-discrepancy reconciliation; the canonical
        many-ways integration resource (flips the lane-11 non-overlap row of record routed 'P3 3.5 Integration')
      rationale: 'Canonical UGM title: Constant consistency'
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

# Constant consistency

> Excerpt: Three different ways to work out an integral give results that appear to be very different. What is going on?

## Problem

In how many different ways can you find this? \[\displaystyle{\int {\cos (x) \sin (x)} \, dx}\]

Some suggested approaches

Could you use a trigonometric identity?

Could you use a substitution?

Could you integrate by parts?

Anything else?

## Some solutions

Using a trigonometric identity

The integrand is familiar from the identity \(\sin(2x) \equiv 2\sin(x) \cos(x)\) so we could use this to help us.

\[\displaystyle{\int {\cos (x) \sin (x)} \, dx} = \displaystyle{\int \dfrac{1}{2} {\sin (2x)} \, dx} = -\dfrac{1}{4} \cos(2x) + C\]

Using a substitution

If we use the substitution \(u=\cos(x)\), then \(\dfrac{du}{dx} = -\sin(x)\).

Therefore, \[\displaystyle{\int {\cos (x) \sin (x)} \, dx} = \displaystyle{\int {-u} \, du} = -\dfrac{1}{2} \cos^2 (x) + C\]

Is this the only possible substitution we could use?

Integration by parts

We have a product of two different functions, so integration by parts may be useful. \[\int uv' \, dx = uv - \int u'v \, dx\]

We let \(u=\sin(x)\) and \(v'=\cos(x)\), so that \(u'=\cos x\) and \(v=\sin x\).

\[\displaystyle{\int {\cos (x) \sin (x)} \, dx}= \sin^2(x) - \displaystyle{\int {\cos (x) \sin (x)} \, dx}\]

The integral on the right hand side is the same as our original. Has this helped?

Let’s define \[\displaystyle{\int {\cos (x) \sin (x)} \ dx} = I.\]

Then we have \[I = \sin^2(x) -I +c.\]

Making

\(I\)

the subject, we have

\[\begin{align*} 2I &= sin^2(x) +c\\ \implies\quad I&= \dfrac{1}{2} \sin^2(x) + C. \end{align*}\]

Would the answer have been different if we had swapped the \(u\) and \(v'\)?

We’ve integrated the function in three different ways and seem to have three different answers. What has happened?

- Would thinking about these solutions graphically help?

- Can we make sense of it algebraically?

## Are these the same?

**Graphical Approach**

From the graphs we can see that each is a translation parallel to the \(y\)-axis of the same curve. Therefore we can add a constant value to each function and get the other solutions.

We used the same symbol, \(C\) for the constant of integration in each case, but in fact they must be different constants.

**Algebraic Approach**

If the constants are different, let’s call them \(P\), \(Q\) and \(R\) rather than \(C\).

So we have the three answers as:

| \(-\dfrac{1}{4} \cos(2x) + P\) | \(-\dfrac{1}{2} \cos^2 (x) + Q\) | \(\dfrac{1}{2} \sin^2(x) + R\) |
|---|---|---|

Are there any trigonometric identities that connect the trigonometric functions?

We know that \(\cos(2x) \equiv 2\cos^2(x)-1 \equiv 1-2\sin^2(x)\) and \(\cos^2(x) \equiv 1-\sin^2(x)\).

Therefore, \[-\dfrac{1}{4} \cos(2x) + P = -\dfrac{1}{4} (2\cos^2(x)-1) +P = -\dfrac{1}{2} \cos^2(x) + \dfrac{1}{4} + P.\]

Comparing \(-\dfrac{1}{2} \cos^2(x) + \dfrac{1}{4} + P\) to \(-\dfrac{1}{2} \cos^2 (x) + Q\) we can see they are the same except for the constants. If we equate them then \(Q=\dfrac{1}{4} +P\).

Similarly, \[-\dfrac{1}{4} \cos(2x) + P = -\dfrac{1}{4} (1-2\sin^2(x)) +P = \dfrac{1}{2} \sin^2(x) - \dfrac{1}{4} + P.\]

Comparing again, we can see \(R=-\dfrac{1}{4} +P\)

So we can see the constant is not the same but the functions are equivalent.

How are the differences in the constants related to the translations of the graphs?

We worked out the integral in three different ways and got what at first seemed to be different answers. What would happen if we used the different methods to evaluate a definite integral such as \[\displaystyle{\int_0^{\pi/2} {\cos (x) \sin (x)} \, dx}\text{ ?}\]
