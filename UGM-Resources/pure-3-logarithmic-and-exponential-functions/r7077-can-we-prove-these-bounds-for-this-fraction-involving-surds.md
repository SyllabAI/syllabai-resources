---
created: 2026-10-24T22:06:39 (UTC +06:00)
source: https://undergroundmathematics.org/thinking-about-algebra/r7077
author: Underground Mathematics (University of Cambridge)
rights: © University of Cambridge (Underground Mathematics). Use inside SyllabAI is authorised by the
  operator attestation of 2026-10-23 — see LICENSE-DATA.md (Amendment 2026-10-23) in this repository.
  Takedown / correction handling as stated in LICENSE-DATA.md.
tags:
- underground-mathematics
- thinking-about-algebra
- type/review-question
resource_identity:
  ugm_id: r7077
  station: thinking-about-algebra
  station_title: Thinking about Algebra
  resource_type_id: 10
  resource_type_label: Review question
  level: null
  ref: 7077
  old_site_id: "Q69"
spec_map:
  curriculum_code: CIE-9709-P3-2023
  lane: cie-a-level-maths-20-pure-3
  board: Cambridge CIE
  syllabus_version: 2023-2025
  subsection: thinking-about-algebra
  subsection_provenance:
    tier: PROVIDER
    signal: source-url-slug
    slug: thinking-about-algebra
    validation_status: SUGGESTED
  spec_points:
  - code: 3.2.3
    provenance:
      tier: AI_SUGGESTED
      confidence: medium
      model_version: "GLM (Super Z agent, z.ai) — P3c lane-10 cross-map (cross-map-log-and-exp.json (P3c lane 10) @ syllabai-experimental 980556af)"
      evidence: "y=ax^n from data: (9/4)^n=2/3 solved exactly as powers of 2 and 3 (n=-1/2) - the indicial-equation limb of a composite question; prior routing of record: lane-5 '2.2 Logarithmic and exponential functions'"
      rationale: "Canonical UGM title: Can we prove these bounds for this fraction involving surds?"
      validation_status: SUGGESTED
    title: "use logarithms to solve equations and e.g. inequalities in which the unknown appears in indices"
  mapped_date: '2026-10-25'
  mapper: cross-map-log-and-exp.json (P3c lane 10) @ syllabai-experimental 980556af
provenance:
  capture_date: '2026-10-22'
  capture_tool: P2 full-site crawl (ugm-crawl) → ugm-clean extraction; text-only import
  content_language: en
  exam_reference: "UCLES A level Mathematics A 1, QP 9200/1, 1980, Q3"
  task: T-UGM-IMPORT-10
---

# Can we prove these bounds for this fraction involving surds?

## Question

1. The variables \(x\) and \(y\) are connected by the relation \(y = ax^n\), where \(a\) and \(n\) are constants; \(y = 3\) when \(x = 4\) and \(y = 2\) when \(x = 9\). Find the exact values of \(n\) and \(a\).

---

1. Express \[\frac{\sqrt{a}+\sqrt{b}}{\sqrt{a}-\sqrt{b}}\] as a fraction having a rational denominator. Show that, if \(n\) is a positive integer, then \(n(n+2)\) lies between \(n^2\) and \((n+1)^2\). If \(n\) is a positive integer, use the results in (i) and (ii) to find in terms of \(n\) two consecutive integers between which \[\frac{\sqrt{n+2}+\sqrt{n}}{\sqrt{n+2}-\sqrt{n}}\] must lie.

## Suggestion

The question asks us to get rid of the square roots in the denominator; what method might we use?

Can we multiply \(\sqrt{a}-\sqrt{b}\) by something so that we lose the square roots?

What is \(n(n+2) - (n+1)^2\)?

The question tells us to use results we’ve already proved… like many exam questions!

## Solution

By substituting the information we’re given in the question, we obtain the equations

\[\begin{equation} 3 = 4^n a \qquad \label{eq:1} \end{equation}\]

and

\[\begin{equation} 2 = 9^n a. \qquad \label{eq:2} \end{equation}\]

Dividing the second by the first to eliminate \(a\) gives \[\frac{2}{3} = \left(\frac{9}{4}\right)^n.\]

To work with this, it will be more convenient to write everything as powers of \(2\) and \(3\).

That is, \(2^{2n+1}=3^{2n+1}\), which can only be the case when \(2n+1=0\) (as \(2\) and \(3\) have highest common factor \(1\)).

Therefore, \(n=-\frac{1}{2}\).

Now we can go back to equation \(\eqref{eq:1}\) or equation \(\eqref{eq:2}\) to find that \(a=6\).

Alternatively, if you know about logarithms…

Taking logs to base \(10\) with our starting equations (any base will do, in fact) we get \[\log3 = \log a + 2n\log2, \log2 = \log a + 2n \log3.\]

Subtracting these gives \(\log3 - \log2 = 2n(\log2-\log3)\), and so \(n = -\dfrac{1}{2}\).

Substituting back into one of our starting equations gives \(a = 6\).

If we multiply both the numerator and the denominator by \(\sqrt{a} + \sqrt{b}\), then the fraction becomes \[\dfrac{(\sqrt{a}+\sqrt{b})(\sqrt{a}+\sqrt{b})}{(\sqrt{a}-\sqrt{b})(\sqrt{a}+\sqrt{b})}=\frac{(\sqrt{a}+\sqrt{b})^2}{a-b}=\dfrac{a+b+2\sqrt{ab}}{a-b}.\] This has a rational denominator.

Note \(n(n+2)-n^2 = 2n > 0\), so \(n(n+2)>n^2\).

We also have \[n(n+2)-(n+1)^2=n^2 + 2n - n^2 - 2n -1=-1 < 0,\] so \(n(n+2)<(n+1)^2\).

So \(n(n+2)\) lies between \(n^2\) and \((n+1)^2\).

1. If \(n\) is a positive integer, use the results in (i) and (ii) to find in terms of \(n\) two consecutive integers between which \[\dfrac{\sqrt{n+2}+\sqrt{n}}{\sqrt{n+2}-\sqrt{n}}\] must lie.

By using (i) we get \[\dfrac{\sqrt{n+2}+\sqrt{n}}{\sqrt{n+2}-\sqrt{n}}=\dfrac{2n+2+2\sqrt{n(n+2)}}{2}=n+1+\sqrt{(n+2)n}.\]

Now we know \((n+1)^2>n(n+2)>n^2\), which implies \(n+1>\sqrt{n(n+2)}>n\).

So adding \(n+1\) to each part of the inequality, we get \[2n+2>n+1+\sqrt{(n+2)n}>2n+1,\]

and so \(\dfrac{\sqrt{n+2}+\sqrt{n}}{\sqrt{n+2}-\sqrt{n}}\) lies between \(2n+1\) and \(2n+2\).
