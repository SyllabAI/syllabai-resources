---
created: 2026-10-25T01:37:17 (UTC +06:00)
source: https://undergroundmathematics.org/polynomials/r9330
author: Underground Mathematics (University of Cambridge)
rights: © University of Cambridge (Underground Mathematics). Use inside SyllabAI is authorised by the
  operator attestation of 2026-10-23 — see LICENSE-DATA.md (Amendment 2026-10-23) in this repository.
  Takedown / correction handling as stated in LICENSE-DATA.md.
tags:
- underground-mathematics
- polynomials
- type/review-question
resource_identity:
  ugm_id: r9330
  station: polynomials
  station_title: Polynomials & Rational Functions
  resource_type_id: 10
  resource_type_label: Review question
  level: null
  ref: 9330
  old_site_id: "Q73"
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
      confidence: high
      model_version: "GLM (Super Z agent, z.ai) — P3c lane-9 cross-map (cross-map-algebra.json (P3c lane 9) @ syllabai-experimental 3098d8eb)"
      evidence: "f(−½)=0 and f(2)=0 (factor theorem) pin a and b; the quartic is factorised into three factors and the f(x)>0 set read from the signs"
      rationale: "Canonical UGM title: Can we find the coefficients and factorise this quartic?"
      validation_status: SUGGESTED
    title: "use the factor theorem and the remainder theorem"
  mapped_date: '2026-10-25'
  mapper: cross-map-algebra.json (P3c lane 9) @ syllabai-experimental 3098d8eb
provenance:
  capture_date: '2026-10-22'
  capture_tool: P2 full-site crawl (ugm-crawl) → ugm-clean extraction; text-only import
  content_language: en
  exam_reference: "UCLES A level Mathematics A 1 and Pure Mathematics 1, QP 9200/1 and 9208/1, 1984, Q10"
  task: T-UGM-IMPORT-9
---

# Can we find the coefficients and factorise this quartic?

## Question

The expression \[2x^4+ax^3+bx^2-4x-4\] where \(a\) and \(b\) are constants, is denoted by \(f(x)\). Given that \(f\left(-\dfrac{1}{2}\right)=0\) and \(f(2)=0\), find the values of \(a\) and \(b\).

With these values for \(a\) and \(b\)

1. express \(f(x)\) as the product of three algebraic factors, and hence show that the equation \(f(x)=0\) has only two real roots;

---

1. find the set of values of \(x\) for which \(f(x)>0\).

## Suggestion

You could use this applet to try some values. The green curve is \(y=f(x)\).

> [interactive embed (geogebra-iframe): //www.geogebratube.org/material/iframe/id/pyUm9gmV/width/600/height/400/border/888888/rc/false/ai/false/sdz/false/smb/false/stb/false/stbh/false/ld/false/sri/true/asb/false/at/html5] — not part of the text import; see the source page.

[Download GeoGebra file](https://www.geogebratube.org/material/download/format/file/id/pyUm9gmV)

Could we find two equations involving \(a\) and \(b\) that must be simultaneously true?

How would the [Factor Theorem](https://undergroundmathematics.org/glossary/factor-theorem) help us here?

How can we find the number of real roots of a quadratic equation?

Could sketching the graph of \(f(x)\) help with this?

## Solution

Substituting

\(x=-\frac{1}{2}\)

we have

\[\begin{align*} f\left(-\frac{1}{2}\right) &= 0\\ \implies\quad \frac{2}{16}-\frac{a}{8}+\frac{b}{4}+2-4 &= 0\\ \iff\quad 1 - a + 2b - 16 &= 0\\ \iff\quad -a+2b &= 15 \end{align*}\]

Also we have that

\[\begin{align*} f(2) &= 0\\ \implies\quad 32+8a+4b-8-4 &= 0\\ \iff\quad 2a+b &= -5 \end{align*}\]

We now have two simultaneous equations in \(a\) and \(b\). If we add twice the first to the second, to eliminate \(a\), we see that \(5b = 25\) and so \(b = 5\).

We can then use either equation to find that \(a = -5\).

Since \(f\left(-\frac{1}{2}\right)=0\) and \(f(2)=0\) we know that \(2x+1\) and \(x-2\) are two factors of \(f(x)\).

So \[f(x)=2x^4 - 5x^3 + 5x^2 - 4x - 4 =(2x+1)(x-2)g(x) = (2x^2 - 3x -2)g(x),\] where \(g(x)\) is a quadratic polynomial. By inspection, we can see that \(g(x)=x^2-x+2\).

Can you explain, ‘by inspection’?

To find the expression for \(g(x)\), let’s write \(g(x)=ax^2+bx+c\) and try to find \(a\), \(b\) and \(c\) such that \[(2x^2 - 3x -2)(ax^2+bx+c)=2x^4 - 5x^3 + 5x^2 - 4x - 4.\] We can either multiply out the brackets on the left hand side, group the terms and find what \(a\), \(b\) and \(c\) must be, or we can try to `inspect’ the equation.

For example, the only terms that contribute to the \(x^4\) term will be \(2x^2\) from the first bracket and \(ax^2\) from the second.

This tells us that \(a=1\). Similarly, the constant term must come from the constant terms in both of the brackets, so we find that \(-2c=-4\) and so \(c=2\).

To find \(b\), we check the coefficient of \(x\), so that \(-2b-3c=-4\). We know already that \(c=2\), so we see that \(b=-1\). So \(g(x)=x^2-x+2\).

Therefore we have \[f(x)=(2x+1)(x-2)(x^2-x+2).\]

To show that \(f(x)\) only has two real roots we need to show that \(g(x)=x^2-x+2\) has no real roots.

The [discriminant](https://undergroundmathematics.org/glossary/discriminant) of \(g(x)\) is \(1 - 4 \times 2 = -7\), and since this is negative, we see that \(g(x)\) has no real roots.

So, we can conclude that \(f(x)\) has exactly two real roots, which are \(x=-\dfrac{1}{2}\) and \(x=2\).

If we sketch the graph of \(f(x)\), we’ll clearly see the regions for which \(f(x)>0\). We know that there are only two real roots, and we observe that the \(y\)-intercept is \(-4\).

So the graph is

From this, we can see that the values of \(x\) for which \(f(x)>0\) are \(x<-\dfrac{1}{2}\) and \(x>2\).
