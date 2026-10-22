---
created: 2026-10-23T12:00:00 (UTC +06:00)
source: https://undergroundmathematics.org/quadratics/r6215
author: Underground Mathematics (University of Cambridge)
rights: © University of Cambridge (Underground Mathematics). Use inside SyllabAI is authorised by the
  operator attestation of 2026-10-23 — see LICENSE-DATA.md (Amendment 2026-10-23) in this repository.
  Takedown / correction handling as stated in LICENSE-DATA.md.
tags:
- underground-mathematics
- quadratics
- type/review-question
resource_identity:
  ugm_id: r6215
  station: quadratics
  station_title: Quadratics
  resource_type_id: 10
  resource_type_label: Review question
  level: null
  ref: 6215
  old_site_id: Q49
spec_map:
  curriculum_code: CIE-9709-P1-2023
  lane: cie-a-level-maths-20-pure-1
  board: Cambridge CIE
  syllabus_version: 2023-2025
  subsection: quadratics
  subsection_provenance:
    tier: PROVIDER
    signal: source-url-slug
    slug: quadratics
    validation_status: SUGGESTED
  spec_points:
  - code: 1.1.5
    provenance:
      tier: AI_SUGGESTED
      confidence: high
      model_version: GLM (Super Z agent, z.ai) — P3c quadratics cross-map (cross-map-quadratics.json @
        syllabai-experimental 915bfa8c)
      evidence: 'Canonical hidden quadratic: x + 3sqrt(x) - 1/2 = 0.'
      rationale: 'Canonical UGM title: “How do we  solve $x + 3\sqrt{x} − 1/2 = 0$?”; exam provenance:
        UCLES 2013 Q1; cross-mapped primary pick of record (UGM-Enrichment perSpecPoint primaryPick, syllabai-resources#55)'
      validation_status: SUGGESTED
      primaryPick: true
    title: recognise and solve equations in x which are quadratic in some function of x . tan
  mapped_date: '2026-10-23'
  mapper: cross-map-quadratics.json (P3c) @ syllabai-experimental 915bfa8c
  coverage_note: null
provenance:
  capture_date: '2026-10-22'
  capture_tool: P2 full-site crawl (ugm-crawl) → ugm-clean extraction; text-only import
  content_language: en
  exam_reference: UCLES 2013 Q1
task: T-UGM-IMPORT-1
---

# How do we  solve $x + 3\sqrt{x} − 1/2 = 0$?

## Question

1. Use the substitution \(\sqrt{x} = y\) (where \(y \geq 0\)) to find the real root of the equation \[x + 3\sqrt{x} − \tfrac{1}{2} = 0.\]
2. Find all real roots of the following equations:
  1. \(x + 10\sqrt{x + 2} − 22 = 0\);
  2. \(x^2 − 4x + \sqrt{2x^2−8x−3} − 9 = 0\).

## Solution

Why must we have \(y\geq 0\)? It is because when we write \(\sqrt{x}\), we specifically mean the positive square root (or zero if \(x=0\)).

So when we solve the quadratic in \(y\), we must be careful to only consider positive roots of that quadratic.

As the question suggests, we rewrite the equation with \(y\) for \(\sqrt{x}\), and therefore \(y^2=x\) so \[y^2+3y-\tfrac{1}{2}=0.\]

We solve this by completing the square:

\[\begin{align*} &&&\left(y+\frac{3}{2}\right)^2-\frac{9}{4}-\frac{1}{2}=0&&\qquad \\ \iff &&&\qquad \left(y+\frac{3}{2}\right)^2=\frac{11}{4} \\ \iff &&&\qquad y+\frac{3}{2}=\pm \frac{\sqrt{11}}{2} \\ \iff &&&\qquad y=\frac{-3\pm\sqrt{11}}{2}. \end{align*}\]

We could also solve this equation using the quadratic formula or any other method you know.

We need to be a bit careful here—recall that the question told us that we must have \(y\geq 0\). So we take \[y=\frac{-3+\sqrt{11}}{2},\] and so we have \[x=y^2=\frac{10-3\sqrt{11}}{2}.\]

We can check that this satisfies the original equation (remembering we know what \(\sqrt{x}\) is since this is the value we found for \(y\)): \[x+3\sqrt{x}-\frac{1}{2}=\frac{10-3\sqrt{11}}{2}+3\frac{-3+\sqrt{11}}{2}-\frac{1}{2}=\frac{1}{2}-\frac{1}{2}=0.\]

---

A good general tip: if you’re given a suggestion for the first part of the question, and you can’t immediately see how to solve the next part, try using a similar method to that suggested in the suggestion.

You may have to modify the suggestion a little, though!

Following the method for the first question, we try the substitution \(y=\sqrt{x+2}\), again for \(y\geq 0\). This time, we have \(y^2=x+2\), or \(x=y^2-2\), so we are now solving the equation \[y^2+10y-24=0.\] This equation can be factorised as \[y^2+10y-24=(y+12)(y-2)=0.\] Again, we can disregard the solution \(y=-12\), since \(y \geq 0\), and see that \(y=2\). This implies that \(x=2\) is the only possible solution. We check whether this is a valid solution: \[x+10\sqrt{x+2}-22=2+10(2)-22=0. \quad \checkmark\]

---

1. Find all real roots of the following equations:
  1. \(x^2 − 4x + \sqrt{2x^2−8x−3} − 9 = 0\).

Let’s try the substitution \(y=\sqrt{2x^2-8x-3}\). We can rearrange this to find that \(x^2-4x=(y^2+3)/2\), and so we this time study the equation \[\frac{y^2+3}{2}+y-9=0,\] or equivalently, \[y^2+2y-15=0.\]

We can again factorise to find that \[y^2+2y-15=(y+5)(y-3)=0.\] We must again discard the negative solution, and consider \(y=3\). To find \(x\), we must now solve \(x^2-4x=(3^2+3)/2=6\), so \(x^2-4x-6=0\). Applying the [quadratic formula](https://undergroundmathematics.org/glossary/quadratic-equation-solution), we deduce that \[x=2\pm\sqrt{10}.\]

When squaring to solve equations, we may gain extra ‘solutions’ that don’t satisfy the original equation, so we must check them.

But in this case, we have \[(x^2 − 4x) + \sqrt{2x^2−8x−3} − 9= 6+3-9=0,\] so the two solutions are indeed \(x=2\pm\sqrt{10}\).
