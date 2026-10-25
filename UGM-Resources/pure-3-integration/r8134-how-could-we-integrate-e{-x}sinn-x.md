---
created: 2026-10-26T02:40:04 (UTC +06:00)
source: https://undergroundmathematics.org/product-rule/r8134
author: Underground Mathematics (University of Cambridge)
rights: © University of Cambridge (Underground Mathematics). Use inside SyllabAI is authorised by the
  operator attestation of 2026-10-23 — see LICENSE-DATA.md (Amendment 2026-10-23) in this repository.
  Takedown / correction handling as stated in LICENSE-DATA.md.
tags:
- underground-mathematics
- product-rule
- type/review-question
resource_identity:
  ugm_id: r8134
  station: product-rule
  station_title: Product Rule & Integration by Parts
  resource_type_id: 10
  resource_type_label: Review question
  level: null
  ref: 8134
  old_site_id: Q249
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
  - code: 3.5.5
    provenance:
      tier: AI_SUGGESTED
      confidence: high
      model_version: GLM (Super Z agent, z.ai) — P3c lane-13 cross-map (cross-map-p3-integration.json
        (P3c lane 13) @ syllabai-experimental 21845f3)
      evidence: 'I_n = INT e^-x sin^n x dx: the product-rule derivative identity, the parts recurrence
        I_n = -e^(-pi/2) + n INT e^-x cos x sin^(n-1) x, and the reduction formula (n^2+1)I_n = -e^(-pi/2)
        + n(n-1)I_(n-2) with I_4 evaluated - the canonical by-parts reduction-formula showcase; the cos^2
        = 1 - sin^2 identity work is the recorded 3.5.2 clothing (flips the lane-10 ''P3 3.4/3.5'' and
        lane-12 ''P3 3.5 Integration'' rows of record)'
      rationale: 'Canonical UGM title: How could we integrate $e^{-x}\sin^n x$?'
      validation_status: SUGGESTED
    title: recognise when an integrand can usefully be e.g. integration of regarded as a product, and
      use integration by parts
  - code: 3.5.2
    provenance:
      tier: AI_SUGGESTED
      confidence: high
      model_version: GLM (Super Z agent, z.ai) — P3c lane-13 cross-map (cross-map-p3-integration.json
        (P3c lane 13) @ syllabai-experimental 21845f3)
      evidence: 'I_n = INT e^-x sin^n x dx: the product-rule derivative identity, the parts recurrence
        I_n = -e^(-pi/2) + n INT e^-x cos x sin^(n-1) x, and the reduction formula (n^2+1)I_n = -e^(-pi/2)
        + n(n-1)I_(n-2) with I_4 evaluated - the canonical by-parts reduction-formula showcase; the cos^2
        = 1 - sin^2 identity work is the recorded 3.5.2 clothing (flips the lane-10 ''P3 3.4/3.5'' and
        lane-12 ''P3 3.5 Integration'' rows of record)'
      rationale: 'Canonical UGM title: How could we integrate $e^{-x}\sin^n x$?'
      validation_status: SUGGESTED
    title: use trigonometrical relationships in carrying out integration or
  mapped_date: '2026-10-26'
  mapper: cross-map-p3-integration.json (P3c lane 13) @ syllabai-experimental 21845f3
provenance:
  capture_date: '2026-10-22'
  capture_tool: P2 full-site crawl (ugm-crawl) → ugm-clean extraction; text-only import
  content_language: en
  task: T-UGM-IMPORT-13
---

# How could we integrate $e^{-x}\sin^n x$?

## Question

1. Show that \(\dfrac{d}{dx} (\cos x \sin^{n-1}x) = (n-1) \sin^{n-2}x - n \sin^{n}x\).

---

1. Given that \(I_n = \displaystyle\int_0^{\frac{1}{2}\pi} e^{-x} \sin^n x \, dx\), show that \[I_n = -e^{-\frac{1}{2}\pi} + n \int_0^{\frac{1}{2}\pi} e^{-x} \cos x \sin^{n-1}x \, dx, \quad (n \ge 1).\]

---

1. By using the results of (i) and (ii), or otherwise, show that \[(n^2 + 1) I_n = -e^{-\frac{1}{2}\pi} + n(n-1) I_{n-2}, \quad (n \ge 2).\]

---

1. Show that \(I_4 = \frac{1}{85} (24 - 41 e^{-\frac{1}{2}\pi})\).

## Suggestion

Would it help us to use \(s\) for \(\sin x\) and \(c\) for \(\cos x\)?

How can we differentiate a product?

How could we convert any \(\cos x\) terms into \(\sin x\) terms?

Do we know a ‘product rule’ for integration?

Could we use our ‘product rule’ for integration a second time?

How would the earlier parts help us here?

## Solution

How can we differentiate a product?

What techniques could we use to remove any occurrence of \(\cos x\) from the resulting expression?

Differentiating using the product rule gives

\[\frac{d}{dx} (\cos x \sin^{n-1}x) = -\sin x\sin^{n-1}x +(n-1)\cos^2x \sin^{n-2}x,\]

and then by using the identity

\(\cos^2x = 1 - \sin^2x\)

we get

\[\begin{align*} \frac{d}{dx} (\cos x \sin^{n-1}x) &{}= -\sin^n x + (n-1)(1-\sin^2x)\sin^{n-2}x\\ &{}=(n-1)\sin^{n-2}x - n\sin^nx, \end{align*}\]

as required.

Writing

\(s = \sin x\)

and

\(c = \cos x\)

can be helpful. We have

\[\frac{d}{dx} (cs^{n-1}) = -ss^{n-1} +(n-1)c^2s^{n-2}.\]

Using

\(c^2 = 1 - s^2\)

we get

\[\begin{align*} \frac{d}{dx} (cs^{n-1}) &{}=-s^n + (n-1)(1-s^2)s^{n-2}\\ &{}=(n-1)s^{n-2} - ns^n\\ &{}=(n-1)\sin^{n-2}x - n\sin^nx \end{align*}\]

as required.

Here we want to integrate by parts (our ‘product rule’ for integration).

The general formula for integration by parts is \[\int_a^b u \frac{dv}{dx} \, dx = \bigl[uv\bigr]_a^b - \int_a^b v\frac{du}{dx} \, dx.\]

We know how to integrate

\(e^{-x}\)

and differentiate

\(\sin^n x\)

, so we take

\(u=\sin^nx\)

and

\(\dfrac{dv}{dx} = e^{-x}\)

, giving

\(v=-e^{-x}\)

. Then integration by parts yields

\[I_n = \bigl[ -e^{-x} \sin^nx \bigr]_0^{\frac{1}{2}\pi} -\int_0^{\frac{1}{2}\pi} -e^{-x} n \sin^{n-1}x \cos x \, dx,\]

which, after evaluating the limits, becomes

\[\begin{equation} I_n = -e^{-\frac{1}{2}\pi} + n\int_0^{\frac{1}{2}\pi} e^{-x} \cos x \sin^{n-1}x \, dx. \label{eq:1} \end{equation}\]

Integrating the integral in

\(\eqref{eq:1}\)

by parts, taking

\(u = \cos x\sin^{n-1}x\)

and

\(\dfrac{dv}{dx} = e^{-x}\)

(and noticing that we’ve already worked out

\(\dfrac{du}{dx}\)

in part (i)) gives

\[\begin{align*} \int_0^{\frac{1}{2}\pi} &e^{-x} \cos x \sin^{n-1}x \, dx\\ &\quad{}= \bigl[-e^{-x}\cos x \sin^{n-1}x \bigr]_0^{\frac{1}{2}\pi} + \int_0^{\frac{1}{2}\pi} e^{-x} \bigl((n-1) \sin^{n-2}x - n \sin^n x\bigr) \, dx\\ &\quad{}= (n-1)\int_0^{\frac{1}{2}\pi} e^{-x} \sin^{n-2}x \, dx -n \int_0^{\frac{1}{2}\pi} e^{-x} \sin^n x \, dx\\ &\quad{}= (n-1)I_{n-2} - nI_n \end{align*}\]

(The third line follows by evaluating the limits, which are both zero as long as \(n>1\); we are specifically told \(n\ge2\) here.)

Substituting this into \(\eqref{eq:1}\) now gives \[I_n = -e^{-\frac{1}{2}\pi} + n(n-1) I_{n-2} - n^2 I_n.\]

Rearranging gives

\[\begin{equation} (n^2 + 1) I_n = -e^{-\frac{1}{2}\pi} + n(n-1) I_{n-2} \label{eq:2} \end{equation}\]

as required.

Rearranging \(\eqref{eq:2}\) gives \[I_n = \frac{1}{n^2 + 1} \bigl( -e^{-\frac{1}{2}\pi} + n(n-1) I_{n-2}\bigr).\]

So by setting \(n=4\) we get \[I_4 = \frac{1}{17} \bigl( -e^{-\frac{1}{2}\pi} + 12 I_2\bigr),\] and similarly, setting \(n=2\) gives \[I_2 = \frac{1}{5} \bigl( -e^{-\frac{1}{2}\pi} + 2 I_0\bigr).\]

By substituting the expression for \(I_2\) into that for \(I_4\) we get \[I_4 = \frac{1}{17} \left( -e^{-\frac{1}{2}\pi} + 12 \left(\frac{1}{5} \bigl( -e^{-\frac{1}{2}\pi} + 2 I_0\bigr)\right)\right),\] which rearranges to give \[I_4 = \frac{1}{85} \bigl(24 I_0 - 17e^{-\frac{1}{2}\pi}\bigr).\]

Now, by the definition of

\(I_n\)

,

\[\begin{align*} I_0 &{}=\int_0^{\frac{1}{2}\pi} e^{-x} \, dx \\ &{}= \bigl[-e^{-x}\bigr]_0^{\frac{1}{2}\pi} \\ &{}= 1 - e^{-\frac{1}{2}\pi}, \end{align*}\]

so the expression for \(I_{4}\) becomes \[I_4 = \frac{1}{85} \bigl(24 - 41 e^{-\frac{1}{2}\pi}\bigr).\]
