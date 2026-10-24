---
created: 2026-10-25T01:37:17 (UTC +06:00)
source: https://undergroundmathematics.org/product-rule/r5126
author: Underground Mathematics (University of Cambridge)
rights: © University of Cambridge (Underground Mathematics). Use inside SyllabAI is authorised by the
  operator attestation of 2026-10-23 — see LICENSE-DATA.md (Amendment 2026-10-23) in this repository.
  Takedown / correction handling as stated in LICENSE-DATA.md.
tags:
- underground-mathematics
- product-rule
- type/review-question
resource_identity:
  ugm_id: r5126
  station: product-rule
  station_title: Product Rule & Integration by Parts
  resource_type_id: 10
  resource_type_label: Review question
  level: null
  ref: 5126
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
  - code: 3.1.5
    provenance:
      tier: AI_SUGGESTED
      confidence: medium
      model_version: "GLM (Super Z agent, z.ai) — P3c lane-9 cross-map (cross-map-algebra.json (P3c lane 9) @ syllabai-experimental 3098d8eb)"
      evidence: "1/(4−sin²x) decomposed as (1/4)(1/(2−sinx)+1/(2+sinx)) after u=sinx — an (ax+b)(cx+d)-type decomposition carried out inside the integral proof"
      rationale: "Canonical UGM title: Can we find all three integrals?"
      validation_status: SUGGESTED
    title: "recall an appropriate form for expressing rational functions in partial fractions, and carry out the decomposition, in cases where the denominator is no more complicated than ( ax + b )( cx + d )( ex + f ), ( ax + b )( cx + d )², ( ax + b )( cx² + d )"
  mapped_date: '2026-10-25'
  mapper: cross-map-algebra.json (P3c lane 9) @ syllabai-experimental 3098d8eb
provenance:
  capture_date: '2026-10-22'
  capture_tool: P2 full-site crawl (ugm-crawl) → ugm-clean extraction; text-only import
  content_language: en
  exam_reference: "UCLES A level Pure Mathematics 2, QP 842/2, 1973, Q4"
  task: T-UGM-IMPORT-9
---

# Can we find all three integrals?

## Question

1. Prove that \[\begin{equation*} \int_0^{\frac{1}{2}\pi} \frac{\cos x}{3 + \cos^2 x} \:dx = \tfrac{1}{4} \ln 3. \end{equation*}\]

---

1. Integrate with respect to \(x\) \[\begin{equation*} (a)\; \frac{x}{(x-1)^3}, \quad (b)\;(\ln x)^2. \end{equation*}\]

## Solution

If the denominator of the integrand were an expression involving \(\sin x\) we might be able to integrate by substitution…

Since

\(\cos^2 x = 1 - \sin^2 x\)

, we can write

\[\begin{equation*} \int_0^{\frac{1}{2}\pi} \frac{\cos x}{3 + \cos^2 x} \:dx = \int_0^{\frac{1}{2}\pi} \frac{\cos x}{4 - \sin^2 x} \:dx. \end{equation*}\]

Now using

partial fractions

we can expand,

\(\dfrac{1}{4-z^2} = \dfrac{1}{4}\left(\dfrac{1}{2-z}+\dfrac{1}{2+z}\right)\)

. Then we can integrate using the substitutions

\(u=2\pm\sin x\)

.

\[\begin{align*} \int_0^{\frac{1}{2}\pi} \frac{\cos x}{4 - \sin^2 x} \:dx &= \dfrac{1}{4}\int_0^{\frac{1}{2}\pi} \frac{\cos x}{2 - \sin x}+\frac{\cos x}{2 + \sin x} \:dx\\ &= \dfrac{1}{4}\bigl[-\ln\big\vert 2-\sin x\big\vert +\ln \big\vert 2+\sin x\big\vert\bigr]_0^{\frac{1}{2}\pi}\\ &= \dfrac{1}{4}\left[\ln \bigg\vert \dfrac{2+\sin x}{2-\sin x}\bigg\vert\right]_0^{\frac{1}{2}\pi}\\ &= \dfrac{1}{4}\ln 3 \end{align*}\]

1. Integrate with respect to \(x\) \[\begin{equation*} (a)\; \frac{x}{(x-1)^3} \end{equation*}\]

If the numerator were a constant, this would look much more straight-forward, so let’s try rearranging…

We can write,

\[\begin{equation*} \int \frac{x}{(x-1)^3} \:dx = \int \frac{x-1}{(x-1)^3} + \frac{1}{(x-1)^3} \:dx = \int \frac{1}{(x-1)^2} + \frac{1}{(x-1)^3} \:dx. \end{equation*}\]

If

\(u = x-1\)

, then

\[\begin{equation*} \int \frac{1}{(x-1)^2} + \frac{1}{(x-1)^3} \:dx = \int u^{-2} + u^{-3} \:du = \frac{u^{-1}}{-1} + \frac{u^{-2}}{-2} + c = \frac{1}{1-x} - \frac{1}{2(x-1)^2} + c \end{equation*}\]

where \(c\) is a constant of integration.

1. Integrate with respect to \(x\) \[\begin{equation*} (b)\;(\ln x)^2. \end{equation*}\]

The general formula for integration by parts is \[\int u \frac{dv}{dx} \, dx = uv - \int v\frac{du}{dx} \, dx.\]

If we let \(u = (\ln x)^2\) and \(v = x\) then \(\frac{dv}{dx}=1\) and \(\frac{du}{dx}=2\ln x\times\frac{1}{x}\). Integrating by parts, we see that

\[\begin{equation}\label{eq:ii-b-second-ibp} \int (\ln x)^2 \:dx = x (\ln x)^2 - 2 \int \ln x \:dx. \end{equation}\]

In order to integrate

\(\ln x\)

, we again integrate by parts using

\(u = \ln x\)

and

\(v = x\)

. Then

\(\frac{dv}{dx}=1\)

and

\(\frac{du}{dx}=\frac{1}{x}\)

and we have

\[\begin{equation*} \int \ln x \:dx = x \ln x - \int x \frac{1}{x} \:dx = x \ln x - x. \end{equation*}\]

After substituting this into

\(\eqref{eq:ii-b-second-ibp}\)

, we can conclude that

\[\begin{equation*} \int (\ln x)^2 \:dx = x (\ln x)^2 - 2 \left( x \ln x - x \right) = x (\ln x)^2 - 2 x \ln x + 2x + c \end{equation*}\]

where \(c\) is, again, a constant of integration.
