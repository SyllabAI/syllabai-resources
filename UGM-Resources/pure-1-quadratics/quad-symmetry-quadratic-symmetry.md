---
created: 2026-10-23T12:00:00 (UTC +06:00)
source: https://undergroundmathematics.org/quadratics/quad-symmetry
author: Underground Mathematics (University of Cambridge)
rights: © University of Cambridge (Underground Mathematics). Use inside SyllabAI is authorised by the
  operator attestation of 2026-10-23 — see LICENSE-DATA.md (Amendment 2026-10-23) in this repository.
  Takedown / correction handling as stated in LICENSE-DATA.md.
tags:
- underground-mathematics
- quadratics
- type/package-of-problems
- level/developing
resource_identity:
  ugm_id: quad-symmetry
  station: quadratics
  station_title: Quadratics
  resource_type_id: 5
  resource_type_label: Package of problems
  level: Developing
  ref: 8685
  old_site_id: E1_RT7_4a
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
  - code: 1.1.1
    provenance:
      tier: AI_SUGGESTED
      confidence: high
      model_version: GLM (Super Z agent, z.ai) — P3c quadratics cross-map (cross-map-quadratics.json @
        syllabai-experimental 915bfa8c)
      evidence: Axis of symmetry and vertex via completed-square form.
      rationale: 'Canonical UGM title: “Quadratic symmetry”'
      validation_status: SUGGESTED
    title: carry out the process of completing the square for a quadratic polynomial ax + bx + c and use
      y a completed square form
  mapped_date: '2026-10-23'
  mapper: cross-map-quadratics.json (P3c) @ syllabai-experimental 915bfa8c
  coverage_note: null
provenance:
  capture_date: '2026-10-22'
  capture_tool: P2 full-site crawl (ugm-crawl) → ugm-clean extraction; text-only import
  content_language: en
task: T-UGM-IMPORT-1
assets:
- path: https://undergroundmathematics.org/quadratics/quad-symmetry/images/parabola1.png
  kind: figure
- path: https://undergroundmathematics.org/quadratics/quad-symmetry/images/quad-symm.png
  kind: figure
---

# Quadratic symmetry

> Excerpt: Are all quadratic graphs symmetrical? Students are asked to come up with a convincing argument to answer this question.

## Problem

**Are all quadratic graphs symmetrical?**

Take a look at the graph below.

> [figure: Plot of a parabola. — `https://undergroundmathematics.org/quadratics/quad-symmetry/images/parabola1.png`] (image not included in the text import; path of record).

The equation of this graph is \(y = x^2 - 8x + 10\)

Is this graph symmetrical? Are you convinced? How can you convince someone else?

## Suggestion

How would you define symmetrical in this context?

If the graph has a line of symmetry, what is it? How can we use this idea?

Does the graph look similar to any other graph you know? How can we use this idea?

## Solution

### Approach 1

It looks like the graph has a line of symmetry with equation \(x = 4\).

If we can show that each point on the curve has a mirror image about the line \(x=4\), then we will be correct.

> [figure: graph of parabola with line x equals 4 and points at x equals 4 plus k and x equals 4 minus k — `https://undergroundmathematics.org/quadratics/quad-symmetry/images/quad-symm.png`] (image not included in the text import; path of record).

Let’s choose \(x\) coordinates such that they are equidistant from the line \(x=4\), e.g. \(x=4+k\) and \(x=4-k\).

When \(x = 4 + k\), \(\quad y = (4 + k)^2 - 8(4 + k) + 10 = k^2 - 6\).

When \(x = 4 - k\), \(\quad y = (4 - k)^2 - 8(4 - k) + 10 = k^2 - 6\).

The \(y\) coordinates are equal. This shows we are correct and the graph \(y = x^2 - 8x + 10\) is symmetrical about the line \(x = 4\).

Alternatively, we can perform the same calculation with the completed square form. What do you notice?

By completing the square, we have \(y=(x−4)^2−6=(4−x)^2−6\). From this, we can see the \(y\) coordinates of two points equidistant from \(x=4\) must be the same and the quadratic graph is symmetrical about the line \(x=4\).

**Completed square form approach**

What did we do in this approach? We made a conjecture (an educated guess) and then went on to prove that this was correct. This is a fundamental process in doing mathematics.

### Approach 2

It looks like the graph of \(y = x^2 - 8x + 10\) has the same shape as \(y = x^2\) but is in a different position.

If we can show that \(y = x^2\) is symmetrical and we can translate the graph \(y = x^2\) to \(y = x^2 - 8x + 10\), then we have shown that \(y = x^2 - 8x + 10\) is symmetrical. We do this in two steps.

**Step 1**: Show that the graph \(y = x^2\) is symmetrical about the \(y\) axis.

When \(x = k\), \(\quad \phantom{-}y = k^2\).

When \(x = -k\), \(\quad y = k^2\).

By a similar argument to Approach 1 above, the graph of \(y = x^2\) is symmetrical about the \(y\) axis.

Note: A function where \(f(x) = f(-x)\) for all \(x\) is called an *even function* and is symmetrical about the \(y\) axis. There is more on this topic in [Odd or even or …](https://undergroundmathematics.org/thinking-about-functions/odd-or-even-or).

**Step 2**: Rewrite \(y = x^2 - 8x + 10\) as a translation of \(y = x^2\).

By [completing the square](https://undergroundmathematics.org/glossary/completing-the-square), we have \(y=x^2 - 8x + 10 = (x - 4)^2 - 6\) which is a translation of the graph \(y = x^2\) by \(\dbinom{4}{-6}\). The line of symmetry is therefore translated to \(x = 4\) and the vertex is translated to (\(4,-6\)).

Therefore the graph \(y = x^2 - 8x + 10\) is symmetrical.

How do these approaches compare?

Which is the more easily generalised?

How would these approaches help us to consider whether all quadratics are symmmetrical?
