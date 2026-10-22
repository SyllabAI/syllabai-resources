---
created: 2026-10-23T12:00:00 (UTC +06:00)
source: https://undergroundmathematics.org/quadratics/inequalities-for-some-occasions
author: Underground Mathematics (University of Cambridge)
rights: © University of Cambridge (Underground Mathematics). Use inside SyllabAI is authorised by the
  operator attestation of 2026-10-23 — see LICENSE-DATA.md (Amendment 2026-10-23) in this repository.
  Takedown / correction handling as stated in LICENSE-DATA.md.
tags:
- underground-mathematics
- quadratics
- type/fluency-exercise
- level/developing
resource_identity:
  ugm_id: inequalities-for-some-occasions
  station: quadratics
  station_title: Quadratics
  resource_type_id: 8
  resource_type_label: Fluency exercise
  level: Developing
  ref: 5194
  old_site_id: E2_RT7_1
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
  - code: 1.1.3
    provenance:
      tier: AI_SUGGESTED
      confidence: high
      model_version: GLM (Super Z agent, z.ai) — P3c quadratics cross-map (cross-map-quadratics.json @
        syllabai-experimental 915bfa8c)
      evidence: Quadratic-inequality fluency exercise.
      rationale: 'Canonical UGM title: “Inequalities for some occasions”'
      validation_status: SUGGESTED
    title: solve quadratic equations, and quadratic By factorising, completing the square and using the
      inequalities, in one unknown formula.
  mapped_date: '2026-10-23'
  mapper: cross-map-quadratics.json (P3c) @ syllabai-experimental 915bfa8c
  coverage_note: null
provenance:
  capture_date: '2026-10-22'
  capture_tool: P2 full-site crawl (ugm-crawl) → ugm-clean extraction; text-only import
  content_language: en
task: T-UGM-IMPORT-1
assets:
- path: https://undergroundmathematics.org/quadratics/inequalities-for-some-occasions/images/empty-venn.svg
  kind: figure
- path: https://undergroundmathematics.org/quadratics/inequalities-for-some-occasions/images/finalvenn.png
  kind: figure
---

# Inequalities for some occasions

> Excerpt: Students are given three conditions and asked to fill a Venn diagram with quadratic inequalities that satisfy some, none, or all of the conditions.

## Problem

Can we find a quadratic inequality for each region of the Venn diagram?

The regions are defined as follows.

A: The solution set is a subset of \(x≤1\).

B: The solutions are given by \(a≤x≤b\) where \(a\) and \(b\) are real numbers.

C: The inequality is satisfied by \(x=4\), e.g. \(x=4\) satisfies the inequality \(x≥2\).

> [figure: Diagram shows three intersecting circles A, B and C — `https://undergroundmathematics.org/quadratics/inequalities-for-some-occasions/images/empty-venn.svg`] (image not included in the text import; path of record).

Here are some possible inequalities. Start by placing these into the correct region of the Venn diagram.

\(x^2≤9\)

\(11x≥2x^2\)

\(x^2+3≥2\)

\(3x^2≥21x-30\)

\(x^2≤-x\)

\(x^2≤x-2\)

\(6x^2-1≥5x\)

\(-2x^2≤x-6\)

## Suggestion

If our inequality needs to be satisfied by \(x=4\) and \(a≤x≤b\), what values for \(a\) and \(b\) could we choose?

If \(x=4\) satisfies the inequality, but the inequality cannot be written in the form \(a≤x≤b\), what form will it take?

Some of the regions of the Venn diagram might be empty. Can you find a quadratic inequality to fit this region? If not, can you explain why it is impossible to fill this region. It may be useful to try and sketch a graph of the situation.

## Solution

We will solve the given quadratic inequalities so they can be placed in the Venn diagram. We will start with the more straightforward ones.

| \(x^2-9≤0\) \((x+3)(x-3)≤0\) From the graph we can see \(-3≤x≤3\) are the only real values of \(x\) that satisfy the inequality. Therefore, this inequality satisfies condition B only. | > [figure: graph of y=x^2-9 with the x axis in red between -3 and 3 — `https://undergroundmathematics.org/quadratics/inequalities-for-some-occasions/images/inov3.png`] (image not included in the text import; path of record). |
| --- | --- |

|  |  |
| --- | --- |
| \(0≥2x^2-11x\) \(0≥x(2x-11)\) \(0≤x≤\frac{11}{2}\) This inequality satisfies conditions B and C. | > [figure: graph of y=2x^2-11x with x in red between 0 and 5.5 — `https://undergroundmathematics.org/quadratics/inequalities-for-some-occasions/images/ino2.png`] (image not included in the text import; path of record). |

Does it matter whether we move the terms to the left or the right hand side of the inequality? What would change if we solved \(11x - 2x^2 ≥ 0\) instead?

|  |  |
| --- | --- |
| \(6x^2-5x-1≥0\) \((6x+1)(x-1)≥0\) \(-\frac{1}{6}≤x\), \(x≥1\) This inequality satisfies condition C. | > [figure: graph of y=6x^2-1-5x with x in red above 1 and below -1/6 — `https://undergroundmathematics.org/quadratics/inequalities-for-some-occasions/images/ino3a.png`] (image not included in the text import; path of record). |

|  |  |
| --- | --- |
| Divide both sides of the inequality by \(3\) \(x^2≥7x-10\) \(x^2-7x+10≥0\) \((x-5)(x-2)≥0\) \(x≥5\), \(x≤2\) This inequality does not satisfy any of the conditions. | > [figure: graph of y=3x^2-21x+30 with x in red below 2 and above 5 — `https://undergroundmathematics.org/quadratics/inequalities-for-some-occasions/images/ino4a.png`] (image not included in the text import; path of record). |

Why can we divide both sides by \(3\)? How does the graph of \(y = 3x^2 - 21x + 30\) compare to the graph of \(y = x^2 - 7x +10\)?

|  |  |
| --- | --- |
| \(x^2+x≤0\) \(x(x+1)≤0\) \(-1≤x≤0\) This inequality satisfies conditions A and B. | > [figure: graph of y=x^2+x with x in red between -1 and 0 — `https://undergroundmathematics.org/quadratics/inequalities-for-some-occasions/images/ino5b.png`] (image not included in the text import; path of record). |

|  |  |
| --- | --- |
| \(0≤2x^2+x-6\) \(0≤(2x-3)(x+2)\) \(x≤-2\), \(x≥\frac{3}{2}\) This inequality satisfies C only. | > [figure: graph of y=2x^2+x-6 with x in red below -2 and above 3/2 — `https://undergroundmathematics.org/quadratics/inequalities-for-some-occasions/images/ino6b.png`] (image not included in the text import; path of record). |

| \(x^2≥-1\) From the graph we can see that this inequality is true for all real values of \(x\). Therefore, this inequality satisfies C only. | > [figure: graph of y=x^2 with x=-1 in red — `https://undergroundmathematics.org/quadratics/inequalities-for-some-occasions/images/ino7b.png`] (image not included in the text import; path of record). |
| --- | --- |

We didn’t try to solve this algebraically because of what we know about \(x^2\). What would happen if we did try to solve it algebraically?

| \(x^2-x+2≤0\) The discriminant of the quadratic \(x^2-x+2=0\) is \((-1)^2-4\times 1\times 2 = -7\). This means there are no real solutions to the quadratic equation and therefore no real solutions to the quadratic inequality. This can be seen from the graph. For all real values of \(x\), it is impossible for the graph \(y=x-2\) to be greater than the graph \(y=x^2\). Therefore, this inequality does not satisfy any of the conditions. | > [figure: graph of y=x^2-x+2, nothing in red — `https://undergroundmathematics.org/quadratics/inequalities-for-some-occasions/images/ino8a.png`] (image not included in the text import; path of record). |
| --- | --- |

What other graph might we have sketched to see there are no solutions?

---

Here are the given inequalities presented in the Venn Diagram.

> [figure: Venn diagram showing where each inequality lies with empty regions A and C, and A, B and C. — `https://undergroundmathematics.org/quadratics/inequalities-for-some-occasions/images/finalvenn.png`] (image not included in the text import; path of record).

It is impossible for a number to be less than 1 and equal to 4 simultaneously. Therefore it is impossible to fill these regions.

**Are there any inequalities which satisfy conditions A and C or conditions A, B and C?**

One of the ways for the solution set to be a subset of \(x≤1\) is if it is bounded by two values, e.g. \(-3≤x≤0\), but this would mean the solution set also satisfies condition B.

Another would be if the solution set only has one bound, e.g. \(x ≤-4\), but this is impossible for a quadratic inequality.

However, we could consider a case whose solution set is a point, e.g. \((x+1)^2≤0\) has the solution set \(x=-1\) which satisfies condition A only.

There is some discussion about this solution, as this can also be written as \(-1≤x≤-1\) which then means it also satisfies condition B.

You might have suggested a quadratic inequality with a solution set such as \(-3<x<0\) (using different inequality signs) and this would indeed satisfy only condition A. However we chose to only use the signs \(≤\) and \(≥\).

**Are there any inequalities which satisfy only condition A?**
