---
created: 2026-10-23T12:00:00 (UTC +06:00)
source: https://undergroundmathematics.org/quadratics/discriminating
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
  ugm_id: discriminating
  station: quadratics
  station_title: Quadratics
  resource_type_id: 5
  resource_type_label: Package of problems
  level: Developing
  ref: 9676
  old_site_id: E1_RT7_3
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
  - code: 1.1.2
    provenance:
      tier: AI_SUGGESTED
      confidence: high
      model_version: GLM (Super Z agent, z.ai) — P3c quadratics cross-map (cross-map-quadratics.json @
        syllabai-experimental 915bfa8c)
      evidence: MUST/MAY/CAN'T discriminant family; teacher support available (pattern exemplar).
      rationale: 'Canonical UGM title: “Discriminating”; cross-mapped primary pick of record (UGM-Enrichment
        perSpecPoint primaryPick, syllabai-resources#55)'
      validation_status: SUGGESTED
      primaryPick: true
    title: find the discriminant of a quadratic polynomial ax + bx + c and use the discriminant ‘repeated
      root’ is included.
  mapped_date: '2026-10-23'
  mapper: cross-map-quadratics.json (P3c) @ syllabai-experimental 915bfa8c
  coverage_note: null
provenance:
  capture_date: '2026-10-22'
  capture_tool: P2 full-site crawl (ugm-crawl) → ugm-clean extraction; text-only import
  content_language: en
task: T-UGM-IMPORT-1
assets:
- path: https://undergroundmathematics.org/quadratics/discriminating/images/q5a.png
  kind: figure
interactive:
- src: //www.geogebratube.org/material/iframe/id/bhSGAxMC/width/627/height/427/border/888888/rc/false/ai/false/sdz/true/smb/false/stb/false/stbh/false/ld/false/sri/true/asb/false/at/html5
  kind: geogebra-iframe
---

# Discriminating

> Excerpt: Discriminating can be used to consolidate understanding of the discriminant and make connections between graphs and algebra. Students are given statements about the number of solutions of a quadratic equation and asked to decide whether MUST, MAY or CAN’T is the correct choice of word within the statement. For detailed notes on this resource, please see [Discriminating - teacher support](/quadratics/discriminating-teacher-support).

## Problem

Below are several statements about the quadratic equation \[ax^2 + bx + c = 0,\] where \(a\), \(b\) and \(c\) are allowed to be any real numbers except that \(a\) is not \(0\).

For each statement, decide whether MUST, MAY or CAN’T is the correct word to use in the statement.

To say that something MUST be the case, we need it to be true in *all* cases; we will need to give a convincing explanation (a proof) of why this must be always true.

To show that something CAN’T be the case, we likewise need to give a convincing explanation (a proof) of why.

To show that something MAY be the case, we need to give an example when it is true and an example when it is false. If you want a harder challenge, can you determine exactly when it is and when it is not true?

You might want to [download cards](https://undergroundmathematics.org/quadratics/discriminating/components/cards.pdf) with the statements on them, so that you can sort them into piles.

If \(a < 0\), then \(ax^2+bx+c=0\)
 MUST / MAY / CAN’T have real roots.

If \(b^2 - 4ac = 0\), then \(ax^2+bx+c=0\)
 MUST / MAY / CAN’T have one repeated real root.

If \(ax^2+bx+c=0\) has no real roots, then \(ax^2 + bx - c = 0\)
 MUST / MAY / CAN’T have two distinct real roots.

If \(\frac{b^2}{a} < 4c\), then \(ax^2+bx+c=0\)
 MUST / MAY / CAN’T have two distinct real roots.

If \(b = 0\), then \(ax^2+bx+c=0\)
 MUST / MAY / CAN’T have one repeated real root.

The equation \(ax^2+bx+c=0\)
 MUST / MAY / CAN’T have three real roots.

If \(c = 0\), then \(ax^2+bx+c=0\)
 MUST / MAY / CAN’T have real roots.

The equation \(ax^2+bx+c=0\)
 MUST / MAY / CAN’T have the same number of real roots as \(ax^2 - bx + c = 0\).

If \(ax^2+bx+c=0\) has two distinct real roots, then we
 MUST / MAY / CAN’T have \(ac < \frac{b^2}{4}\).

If \(c > 0\), then \(ax^2+bx+c=0\)
 MUST / MAY / CAN’T have two distinct real roots.

The equation \(ax^2+bx+c=0\)
 MUST / MAY / CAN’T have the same number of real roots as \(cx^2 + bx + a = 0\).

If \(ax^2+bx+c=0\) has no real roots, then \(-ax^2 - bx - c = 0\)
 MUST / MAY / CAN’T have two distinct real roots.

## Suggestion

Do you have any favourite examples of quadratics with different numbers of real roots? Having some examples to test is a good way to begin on a problem like this.

How can we use the coefficients to determine the number of real roots?

How can thinking about the graph of the quadratic \(y=ax^2+bx+c\) help us to think about some of these statements?

As well as trying to visualise this, it may be helpful to use the [interactive graph](https://undergroundmathematics.org/quadratics/discriminating/interactive-graph).

## Solution

To say that something MUST be the case, we need it to be true in *all* cases; we will need to give a convincing explanation (a proof) of why this must be always true.

To show that something CAN’T be the case, we likewise need to give a convincing explanation (a proof) of why.

To show that something MAY be the case, we need to give an example when it is true and an example when it is false. If you want a harder challenge, can you determine exactly when it is and when it is not true?

---

You may like to explore some of the scenarios on the cards using graphing software or the [interactive graph](https://undergroundmathematics.org/quadratics/discriminating/interactive-graph) in this resource.

Knowing that \(a<0\) tells us that this is a “vertex up” parabola. For example, it could look like one of these two graphs:

| > [figure: graph showing y equals minus x squared plus 1 — `https://undergroundmathematics.org/quadratics/discriminating/images/q1a.png`] (image not included in the text import; path of record). | > [figure: graph showing y equals minus x squared minus 1 — `https://undergroundmathematics.org/quadratics/discriminating/images/q1b.png`] (image not included in the text import; path of record). |
| --- | --- |

The graph of the left is a sketch of \(y=-x^2+1\), while the one on the right is \(y=-x^2-1\).

This shows that if \(a < 0\), then \(ax^2+bx+c=0\) MAY have real roots.

---

From the quadratic formula, we know that the equation \(ax^2 + bx + c = 0\) (with \(a \neq 0\)) has roots \[x = \frac{-b \pm \sqrt{b^2 - 4ac}}{2a}.\] In this case, we are told that the [discriminant](https://undergroundmathematics.org/glossary/discriminant) \(b^2 - 4ac\) is \(0\), so the only real root of the equation is \(x = \frac{-b}{2a}\).

Therefore, if \(b^2 - 4ac = 0\), then \(ax^2+bx+c=0\) MUST have one repeated real root.

---

If the equation has no real roots, then the graph of \(y=ax^2+bx+c\) (which intersects the \(y\)-axis at \(c\)) does not cut the \(x\)-axis, and its vertex is on the same side of the \(x\)-axis as \(c\), as in the following sketches, the left one showing the case of \(a>0\) and the right one showing \(a<0\):

| > [figure: Sketch of y equals a x squared plus b x plus c and minus c where a is positive — `https://undergroundmathematics.org/quadratics/discriminating/images/q3a.png`] (image not included in the text import; path of record). | > [figure: Sketch of y equals a x squared plus b x plus c and minus c where a is negative — `https://undergroundmathematics.org/quadratics/discriminating/images/q3b.png`] (image not included in the text import; path of record). |
| --- | --- |

The graph of \(y=ax^2+bx-c\) is obtained by translating the first graph in the \(y\)-direction until it intersects the \(y\)-axis at \(-c\). Since the direction of the parabola does not change (it remains “vertex up” or “vertex down”), it must now intersect the \(x\)-axis in two distinct points.

Therefore, if \(ax^2+bx+c=0\) has no real roots, then \(ax^2 + bx - c = 0\) MUST have two distinct real roots.

Alternatively, we can argue algebraically. Since the equation \(ax^2 + bx + c = 0\) has no real roots, we can say something about the discriminant: we know that \(b^2 - 4ac < 0\).

Since \(b^2\) is the square of a real number, it is always non-negative (that is, \(b^2 \geq 0\)), so \(b^2 < 4ac\) tells us that \(4ac\) is positive.

The equation \(ax^2 + bx - c = 0\) has discriminant \(b^2 + 4ac\), and now this must be positive.

So \(ax^2 + bx - c = 0\) has two distinct real roots.

---

The tempting thing to do is to multiply both sides of the inequality by \(a\), to obtain \(b^2<4ac\). This would give \(b^2-4ac<0\), so that the equation couldn’t have two distinct real roots – it would have no real roots.

Unfortunately, we don’t know whether \(a\) is positive or negative, so when we multiply both sides of the inequality by \(a\), we may be changing the direction of the inequality.

If \(a\) is positive, then \(b^2<4ac\) and the equation has no real roots.

However, if \(a\) is negative, then multiplying the given inequality by \(a\) will yield \(b^2>4ac\), so \(b^2-4ac>0\) and the equation has two distinct real roots.

So if \(\frac{b^2}{a} < 4c\), then \(ax^2+bx+c=0\) MAY have two distinct real roots, depending upon the sign of \(a\).

---

If we start by taking \(a=1\), then we have the family of quadratics \(y=x^2+c\), which look like this:

> [figure: A graph showing three parabolas with equations y equals x squared plus c, with c negative, zero and positive — `https://undergroundmathematics.org/quadratics/discriminating/images/q5a.png`] (image not included in the text import; path of record).

We can clearly see that we may have two real roots, one repeated real root (when \(c=0\)) or no real roots.

So if \(b = 0\), then \(ax^2+bx+c=0\) MAY have one repeated real root.

Alternatively, we could consider this from an algebraic perspective.

The discriminant is \(b^2-4ac=-4ac\), since \(b=0\). For the equation to have one repeated real root, we require the discriminant to be zero. This will be true if and only if \(c=0\) (as \(a\ne0\)), so \(ax^2+bx+c=0\) MAY have one repeated real root.

---

The equation CAN’T have three real roots, as a quadratic equation can have at most two roots. (We can see this from the quadratic formula or from thinking about the shape of the graph.)

---

If \(c = 0\), then the equation is of the form \(ax^2 + bx = x(ax + b) = 0\), and so \(x = 0\) is a real root.

In fact \(x = - \frac{b}{a}\) is also a real root, so if \(b \neq 0\) then the equation has two distinct real roots, while if \(b=0\), it has one repeated real root.

Alternatively, we could calculate the discriminant, \(b^2-4ac=b^2\) (since \(c=0\)). Since \(b^2\) is a square, it is never negative, so the equation always has either two distinct or one repeated real root.

So if \(c = 0\), then \(ax^2+bx+c=0\) MUST have real roots.

---

Changing the \(+bx\) term to \(-bx\) in the equation \(y=ax^2+bx+c\) has the same effect as replacing \(x\) by \(-x\) (since \(a(-x)^2=ax^2\)).

So the effect on the graph of \(y=ax^2+bx+c\) is to reflect it in the \(y\)-axis, as in the following sketches:

| > [figure: Sketch of the graph and its reflection when the graph does not cross the x axis — `https://undergroundmathematics.org/quadratics/discriminating/images/q8a.png`] (image not included in the text import; path of record). | > [figure: Sketch of the graph and its reflection when the graph touches the x axis — `https://undergroundmathematics.org/quadratics/discriminating/images/q8b.png`] (image not included in the text import; path of record). | > [figure: Sketch of the graph and its reflection when the graph crosses the x axis — `https://undergroundmathematics.org/quadratics/discriminating/images/q8c.png`] (image not included in the text import; path of record). |
| --- | --- | --- |

So we see that \(ax^2+bx+c=0\) and \(ax^2-bx+c=0\) MUST have the same number of real roots. We can even see more than this: the roots of \(ax^2-bx+c=0\) are the negatives of the roots of \(ax^2+bx+c=0\).

Alternatively, we could think in terms of the discriminant.

The equations \(ax^2 + bx + c = 0\) and \(ax^2 - bx + c = 0\) both have discriminant \(b^2 - 4ac\), so they must have the same number of real roots (whatever that number is).

---

If the equation has two distinct real roots, then its discriminant must be positive, that is, \(b^2 - 4ac > 0\).

Now we can rearrange that to obtain \(4ac < b^2\). We can now divide this inequality by \(4\) (which is positive) to obtain \(ac < \frac{b^2}{4}\).

So if \(ax^2+bx+c=0\) has two distinct real roots, then we MUST have \(ac < \frac{b^2}{4}\).

---

The value of \(c\) tells us where the quadratic crosses the \(y\)-axis. Here are some sketches of graphs with a positive \(y\)-intercept.

| > [figure: Sketch of a quadratic graph passing through c on the y axis and crossing the x axis — `https://undergroundmathematics.org/quadratics/discriminating/images/q10a.png`] (image not included in the text import; path of record). | > [figure: Sketch of a quadratic graph passing through c on the y axis and touching the x axis — `https://undergroundmathematics.org/quadratics/discriminating/images/q10b.png`] (image not included in the text import; path of record). | > [figure: Sketch of a quadratic graph passing through c on the y axis and not meeting the x axis — `https://undergroundmathematics.org/quadratics/discriminating/images/q10c.png`] (image not included in the text import; path of record). |
| --- | --- | --- |

So we can see from this that if \(c > 0\), then \(ax^2+bx+c=0\) MAY have two distinct real roots.

Explicit examples of quadratic equations would include \(x^2 - 3x + 2 = (x-1)(x-2) = 0\), which has two distinct real roots, and \(x^2+1=0\), which has no real roots.

Alternatively, if we consider the discriminant \(b^2-4ac\), if we take \(a>0\), then \(4ac\) is positive. So if we choose \(b\) with \(b^2>4ac\), we will have \(b^2-4ac>0\) (giving two distinct real roots), while if we choose \(b\) with \(0\le b^2<4ac\), then \(b^2-4ac<0\) and there are no real roots.

---

There is no obvious way of relating the graph of \(y=ax^2+bx+c\) to that of \(y=cx^2+bx+a\), though it would be fine to draw them both and compare them.

We consider instead the discriminants of the two equations. The discriminant of \(ax^2+bx+c=0\) is \(b^2-4ac\), while that of \(cx^2+bx+a=0\) is \(b^2-4ca\). So the discriminants are equal, and so the equations have the same number of roots.

However, we made an assumption here which may not be valid. The equation \(ax^2+bx+c=0\) is certainly a quadratic, as \(a\) is non-zero. However, \(cx^2+bx+c=0\) is only a quadratic if \(c\) is non-zero. But what if \(c=0\)? In this case, \(cx^2+bx+a=0\) is just the linear equation \(bx+a=0\) (assuming \(b\) is non-zero). So if \(c=0\), the equation \(cx^2+bx+a=0\) has one real root, which will not be the same number of real roots as \(ax^2+bx+c=0\).

As explicit examples, the equation \(x^2 - 3x + 2 = (x-1)(x-2) = 0\) has two distinct real roots. The equation obtained by reversing the coefficients is \(2x^2 - 3x + 1 = 0\), and this factorises as \(2x^2 - 3x + 1 = (2x - 1)(x - 1) = 0\) so has roots \(1\) and \(\frac{1}{2}\)—it too has two distinct real roots.

On the other hand, the equation \(x^2 - x = 0\) has two distinct real roots (since \(x^2 - x = x(x-1) = 0\), which has roots \(x = 0\) and \(x = 1\)). The equation obtained by reversing the coefficients is \(0x^2 - x + 1 = 0\), that is, \(-x + 1 = 0\), and this has just one real root (\(x = 1\)).

Therefore, the equation \(ax^2+bx+c=0\) MAY have the same number of real roots as \(cx^2 + bx + a = 0\).

---

One way to think about this is that the graph of \(y=-ax^2-bx-c\) is the reflection of the graph \(y=ax^2+bx+c\) in the \(x\)-axis. They therefore have the same number of roots as each other.

These two graphs show examples of this. On the left, \(y=(x-1)(x-2)\) has two real roots; on the right, \(y=x^2+1\) has none. It is clear that their reflections have the same number of real roots.

| > [figure: graph showing y equals x minus 1 times x minus 2 and its reflection — `https://undergroundmathematics.org/quadratics/discriminating/images/q12a.png`] (image not included in the text import; path of record). | > [figure: graph showing y equals x squared plus 1 and its reflection — `https://undergroundmathematics.org/quadratics/discriminating/images/q12b.png`] (image not included in the text import; path of record). |
| --- | --- |

Algebraically, if we multiply \(-ax^2-bx-c=0\) by \(-1\), we obtain \(ax^2+bx+c=0\), which must therefore have the same roots as the original equation. In some sense, they are essentially the same equation.

Therefore, if \(ax^2+bx+c=0\) has no real roots, then \(-ax^2 - bx - c = 0\) CAN’T have two distinct real roots.

## Interactive graph

Here is an interactive graph which you might find useful for exploring some of the scenarios on the cards.

> [interactive embed (geogebra-iframe): //www.geogebratube.org/material/iframe/id/bhSGAxMC/width/627/height/427/border/888888/rc/false/ai/false/sdz/true/smb/false/stb/false/stbh/false/ld/false/sri/true/asb/false/at/html5] — not part of the text import; see the source page.

[Download GeoGebra file](https://www.geogebratube.org/material/download/format/file/id/bhSGAxMC)
