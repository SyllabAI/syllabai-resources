---
created: 2026-10-23T16:39:11 (UTC +06:00)
source: https://undergroundmathematics.org/trigonometry-compound-angles/equation-or-identity-ii
author: Underground Mathematics (University of Cambridge)
rights: © University of Cambridge (Underground Mathematics). Use inside SyllabAI is authorised by the
  operator attestation of 2026-10-23 — see LICENSE-DATA.md (Amendment 2026-10-23) in this repository.
  Takedown / correction handling as stated in LICENSE-DATA.md.
tags:
- underground-mathematics
- trigonometry-compound-angles
- type/package-of-problems
- level/developing
resource_identity:
  ugm_id: equation-or-identity-ii
  station: trigonometry-compound-angles
  station_title: 'Trigonometry: Compound Angles'
  resource_type_id: 5
  resource_type_label: Package of problems
  level: Developing
  ref: 5687
  old_site_id: G5_RT7_1
spec_map:
  curriculum_code: CIE-9709-P1-2023
  lane: cie-a-level-maths-20-pure-1
  board: Cambridge CIE
  syllabus_version: 2023-2025
  subsection: trigonometry-compound-angles
  subsection_provenance:
    tier: PROVIDER
    signal: source-url-slug
    slug: trigonometry-compound-angles
    validation_status: SUGGESTED
  spec_points: []
  coverage_note: 'no CIE P1 spec point asserted — resource remains in the corpus unmapped (AGENT.md rule
    3: coverage is never manufactured)'
  mapped_date: '2026-10-23'
  mapper: cross-map-trigonometry.json (P3c lane 5) @ syllabai-experimental f3ef5745
provenance:
  capture_date: '2026-10-22'
  capture_tool: P2 full-site crawl (ugm-crawl) → ugm-clean extraction; text-only import
  content_language: en
task: T-UGM-IMPORT-5
assets:
- path: https://undergroundmathematics.org/trigonometry-compound-angles/equation-or-identity-ii/download/teacher-notes.pdf
  kind: printable
---

# Equation or identity? (II)

## Problem

Throughout, \(A\), \(B\) and \(C\) are the angles of a triangle.

For each of the following, decide whether it is an *identity* (true for all triangles) or an *equation* (there is a triangle for which it is not true).

If it is an identity, true for all triangles, then you should prove it (using trigonometric identities that you already know).

If it is an equation, then at the very least you should give an example of a triangle for which it is not true. You could also try to solve the equation (that is, find all triangles for which it is true).

1. \(\sin(A + 2B) = \sin A + 2\sin B \cos(A + B)\).

---

1. \(\tan(A - B) + \tan(B - C) + \tan(C - A) = 0\).

---

1. \(2\sin A \cos^2\left(\frac{B}{2}\right) + 2\cos^2\left(\frac{A}{2}\right)\sin B = \sin(A + B) + \sin(B + C) + \sin(C + A)\).

---

1. \(\sin(A+B) = \cos C\).

---

1. \(\cos C = -\cos(A+B)\).

---

1. \(4(\cos^2 A \cos^2 B + \sin^2 A \sin^2 B) - 2 \sin(2A) \sin(2B) = 3\).

---

1. \(\sin(2A) + \sin(2B) + \sin(2C) = 4\sin A \sin B \sin C\).

## Suggestion

To help you decide whether an expression is an equation or an identity, you could test it out on some particular triangles, perhaps using angles where you can easily evaluate the expression, or perhaps using particular types of triangle (isosceles or right-angled or equilateral, for example).

You might find it helpful to make a list of the trigonometric identities that you know, so that you can think about which, if any, might be helpful at any given moment.

## Solution

We have to decide whether to try to show that this is true for all triangles (because it’s an identity), or to find the triangles for which it’s true (because it’s an equation). To help us to decide which to go for, we could pick some values to try.

For example, if

\(A = \frac{\pi}{3}\)

and

\(B = \frac{\pi}{6}\)

(because those lead to values that we can easily compute), the left-hand side is

\[\sin\left(\frac{\pi}{3} + \frac{\pi}{3}\right) = \sin\left(\frac{2\pi}{3}\right) = \frac{\sqrt{3}}{2},\]

and the right-hand side is

\[\begin{align*} &\sin\left(\frac{\pi}{3}\right) + 2\sin\left(\frac{\pi}{6}\right) \cos\left(\frac{\pi}{3} + \frac{\pi}{6}\right) \\ &\qquad = \frac{\sqrt{3}}{2} + 2 \times \frac{1}{2} \times \cos\left(\frac{\pi}{2}\right) \\ &\qquad = \frac{\sqrt{3}}{2}, \end{align*}\]

so the equation is satisfied by that triangle.

We could try another triangle. If \(A = B = \frac{\pi}{4}\), then the left-hand side is \[\sin\left(\frac{3\pi}{4}\right) = \frac{1}{\sqrt{2}},\] and the right-hand side is \[\sin\left(\frac{\pi}{4}\right) + 2\sin\left(\frac{\pi}{4}\right) \cos\left(\frac{\pi}{2}\right) = \frac{1}{\sqrt{2}} + 2 \times \frac{1}{\sqrt{2}} \times 0 = \frac{1}{\sqrt{2}},\] so the equation is satisfied by this triangle too.

Of course, it might be that we’ve somehow managed to pick two examples where it works even though it’s not true for all triangles, but that’s not a big problem. We can try to prove the identity, and see what happens. If we succeed, then of course that’s great. If we don’t, then it may be that is because it’s not an identity after all, but in the course of not managing to come up with a proof we’ll hopefully have learned something about the problem that may enable us to construct a triangle that doesn’t satisfy the equation. The important thing at this stage is that we have to dive in (try to prove it), but just have at the back of our minds the idea that it may turn out not to be true after all.

We start with the left-hand side, which we can rewrite using the compound angle formulae. We have \[\sin(A + 2B) = \sin A \cos(2B) + \cos A \sin(2B).\]

It is always worth pausing in manipulations like this to decide what might be the most helpful next step. We have a very natural way to expand \(\sin(2B)\) as \(2 \sin B \cos B\), but we could consider for a moment whether we might want to expand \(\cos(2B)\) as \(\cos^2 B - \sin^2 B\) or \(2\cos^2 B - 1\) or \(1 - 2\sin^2 B\). In order to get a \(\sin A\) by itself (looking ahead to the right-hand side, to see what we want to show), we might pick \(1 - 2\sin^2 B\), perhaps.

We have

\[\sin(A + 2B) = \sin A - 2\sin A \sin^2 B + 2 \cos A \sin B \cos B.\]

Now we can collect together the last two terms, to get

\[\begin{align*} \sin(A + 2B) &= \sin A + 2 \sin B (-\sin A \sin B + \cos A \cos B) \\ & = \sin A + 2\sin B \cos(A+B), \end{align*}\]

as we had hoped.

So this is indeed an identity, and we have just proved it.

Notice that here it was not relevant that \(A\) and \(B\) were two of the three angles of a triangle: our calculations did not rely on them lying in a particular range of values, for example. So this is true for any \(A\) and \(B\).

Let’s try this for a triangle. One way to make the left-hand side easy to evaluate would be to pick a triangle where say

\(A = B\)

. Then we have

\[\begin{align*} &\tan(A - B) + \tan(B - C) + \tan(C - A) \\ & \qquad = \tan 0 + \tan(A - C) + \tan(C - A) \\ & \qquad = \tan(A - C) - \tan(A - C) \\ & \qquad = 0. \end{align*}\]

So the equation holds for isosceles triangles.

Let’s try a triangle that is not isosceles. If

\(A = \frac{\pi}{3}\)

and

\(B = \frac{\pi}{6}\)

, then

\(C = \pi - \frac{\pi}{3} - \frac{\pi}{6} = \frac{\pi}{2}\)

and so

\[\begin{align*} &\tan(A - B) + \tan(B - C) + \tan(C - A) \\ & \qquad = \tan\left(\frac{\pi}{6}\right) + \tan\left(-\frac{\pi}{3}\right) + \tan\left(\frac{\pi}{6}\right) \\ & \qquad = \frac{1}{\sqrt{3}} - \sqrt{3} + \frac{1}{\sqrt{3}},\\ \end{align*}\]

and this is not \(0\).

So we see that the equation is not satisfied by this triangle, but is satisfied by all isosceles triangle. Now we need to try to find all triangles for which the equation holds.

We have

\(A - B = (A - C) + (C - B)\)

, and so

\[\begin{align*} &\tan(A - B) + \tan(B - C) + \tan(C - A) \\ &\quad = \tan((A - C) + (C - B)) + \tan(B - C) + \tan(C - A) \\ &\quad = \frac{\tan(A - C) + \tan(C - B)}{1 - \tan(A - C)\tan(C - B)} + \tan(B - C) + \tan(C - A). \end{align*}\]

Since all we need to know is whether this is \(0\), we can put it over a single denominator, which we can then disregard, and save some algebra.

This is

\(0\)

if and only if

\[\begin{align*} 0 &= \tan(A - C) + \tan(C - B) - \tan(C - B) - \tan(A - C)\\ &\quad + [\tan(A - C) + \tan(C - B)]\tan(A - C)\tan(C - B) \\ &= \tan(A - C)\tan(C - B) [\tan(A - C) + \tan(C - B)]. \end{align*}\]

So we see that \(\tan(A - C) = 0\), or \(\tan(C - B) = 0\), or \(\tan(A - C) = - \tan(C- B)\).

Since \(A\), \(B\) and \(C\) are angles of a triangle, we are restricted in the range that they can take, and we find that \(A = C\), or \(C = B\), or \(A - C = - C + B\). This last possibility is equivalent to \(A = B\).

We have established that the equation holds if and only if the triangle is isosceles.

Note that it was relatively straightforward to show that if the triangle is isosceles then its angles satisfy the equation—that was the first thing we did. The bit that required more thought was showing that this is the only possibility: that if the equation is satisfied, then the triangle must be isosceles.

Let’s try expanding the right-hand side, using compound angle formulae, and hopefully either we’ll get closer to the left-hand side or we’ll learn something about which triangles do or don’t satisfy the equation.

We might notice that the left-hand side does not involve \(C\), so we could try to eliminate that.

We have

\[\begin{align*} &\sin(A + B) + \sin(B + C) + \sin(C + A) \\ &\quad = \sin(A + B) + \sin(B + \pi - A - B) + \sin(\pi - A - B + A) \\ &\quad = \sin(A + B) + \sin(\pi - A) + \sin(\pi - B) \\ &\quad = \sin A \cos B + \cos A \sin B + \sin A + \sin B \\ &\quad = \sin A (1 + \cos B) + \sin B (1 + \cos A). \end{align*}\]

Here we have collected terms inspired by the left-hand side.

We now want to consider \(1 + \cos B\), in the hope that it may turn out to be \(\cos^2(\frac{B}{2})\).

Now

\[\cos B = \cos\left(2 \times \frac{B}{2}\right) = 2\cos^2\left(\frac{B}{2}\right) - 1,\]

and similarly for

\(A\)

, and so

\[\begin{align*} &\sin(A + B) + \sin(B + C) + \sin(C + A) \\ & \qquad = \sin A \left(2 \cos^2 \left(\frac{B}{2}\right)\right) + \sin B \left(2 \cos^2 \left(\frac{A}{2}\right)\right), \end{align*}\]

and so we have proved the identity.

1. \(\sin(A + B) = \cos C\).

We might notice that \(A + B = \pi - C\), so this statement starts to look like a more familiar statement. Let’s dive in and try to prove it (and if it turns out that we’re wrong then that will become clear because our proof won’t work).

Since

\(A\)

,

\(B\)

and

\(C\)

are the angles of a triangle, we see that

\[\begin{align*} \sin(A + B) &= \sin(\pi - C) \\ &= \sin \pi \cos C - \cos \pi \sin C \\ &= \sin C. \end{align*}\]

Oh dear, that’s not quite what we wanted. But this effort isn’t wasted, we can just try to solve the equation using this extra information.

So the triangle satisfies the equation if and only if \(\sin C = \cos C\). We cannot have \(\cos C = 0\) (because we cannot have both \(\cos C = 0\) and \(\sin C = 0\) simultaneously), so we can divide through: the triangle satisfies the equation if and only if \(\tan C = 1\).

Since \(C\) is an angle of a triangle, we must have \(0 < C < \pi\), so we see that the only solution is \(C = \dfrac{\pi}{4}\).

So the triangle satisfies the equation if and only if one angle is \(\dfrac{\pi}{4}\).

1. \(\cos C = -\cos(A + B)\).

Sometimes it is a good idea to start with the right-hand side rather than the left-hand side. Let’s try that here, manipulating it to see whether we can make it look more like the left-hand side (either to prove the identity, or to get more information that will help us to solve the equation).

We have

\[\begin{align*} -\cos(A + B) &= -\cos(\pi - C) \\ &= \sin \pi \sin C - \cos \pi \cos C \\ &= \cos C, \end{align*}\]

and so the identity is true for all triangles.

It’s hard to know what to make of this one, so let’s try it for a triangle or two to try to get a feel for it.

If

\(A = \frac{\pi}{3}\)

and

\(B = \frac{\pi}{6}\)

, then

\[\begin{align*} 4(\cos^2 A \cos^2 B + &\sin^2 A \sin^2 B) - 2\sin(2A) \sin(2B) \\ &= 4\left(\frac{1}{4} \times \frac{3}{4} + \frac{3}{4} \times \frac{1}{4}\right) - 2 \times \frac{\sqrt{3}}{2} \times \frac{\sqrt{3}}{2}\\ &= \frac{3}{2} - \frac{3}{2} \\ &= 0. \end{align*}\]

So we have found a triangle for which the equation does not hold, and we know that this is an equation that we should try to solve, rather than an identity that we need to prove.

We have little choice but to think about the left-hand side.

We have

\[\begin{align*} &4(\cos^2 A \cos^2 B + \sin^2 A + \sin^2 B) - 2\sin(2A) \sin(2B) \\ &\ = 4(\cos^2 A \cos^2 B + \sin^2 A + \sin^2 B) - 8 \sin A \cos A \sin B \cos B. \end{align*}\]

We might think of reordering the terms in the final product: we could think of it as \(\sin A \sin B \cos A \cos B\), and it all starts to look a bit as though it involves things like \((\cos A \cos B - \sin A \sin B)^2 = \cos^2(A + B)\).

We have

\[\begin{align*} &\cos^2 (A + B) \\ &\qquad = (\cos A \cos B - \sin A \sin B)^2 \\ &\qquad = \cos^2 A \cos^2 B + \sin^2 A \sin^2 B - 2\sin A \sin B \cos A \cos B, \end{align*}\]

and so our original equation is equivalent to \[4\cos^2 (A + B) = 3.\] We see that this is equivalent to \[\cos (A+B) = \pm\frac{\sqrt{3}}{2}.\]

Since \(A\) and \(B\) are angles of a triangle, we know that \(0 < A + B < \pi\), and so the possible solutions are \[A + B = \frac{\pi}{6}\] and \[A + B = \frac{5\pi}{6}.\]

This tells us that the angles of a triangle satisfy the original equation if and only if one angle is \(\frac{\pi}{6}\) or \(\frac{5\pi}{6}\).

If \(A = \frac{\pi}{3}\) and \(B = \frac{\pi}{6}\), then \(C = \frac{\pi}{2}\) and so \[\sin(2A) + \sin(2B) + \sin(2C) = \frac{\sqrt{3}}{2} + \frac{\sqrt{3}}{2} = \sqrt{3},\] while \[4\sin A \sin B \sin C = 4 \times \frac{\sqrt{3}}{2} \times \frac{1}{2} \times 1 = \sqrt{3},\] so the equation holds for this triangle.

If \(A = B = \frac{\pi}{4}\), so \(C = \frac{\pi}{2}\), then the left-hand side is \[\sin(2A) + \sin(2B) + \sin(2C) = 1 + 1 + 0 = 2,\] and the right-hand side is \[4 \sin A \sin B \sin C = 4 \times \frac{1}{\sqrt{2}} \times \frac{1}{\sqrt{2}} \times 1 = 2,\] so the equation holds for this triangle too.

Prompted by these two examples, let’s see whether we can prove the identity in general. It seems slightly more natural to expand the left-hand side, so let’s do that and see whether we can make it look more like the right-hand side. We want to keep sines, but if we get a cosine then we should try to eliminate it, perhaps using the fact that the angles sum to \(\pi\).

We have

\[\begin{align*} \sin(2A) &+ \sin(2B) + \sin(2C) \\ &= 2\sin A \cos A + 2\sin B \cos B + 2\sin C \cos(\pi - (A+B)) \\ &= 2\sin A \cos A + 2\sin B \cos B - 2\sin C \cos(A + B) \\ &= 2\sin A \cos(\pi - (B + C)) + 2\sin B \cos (\pi - (A+C)) \\ &\quad - 2\sin C \cos A \cos B + 2\sin C \sin A \sin B \\ &= 2\sin A (\sin B \sin C - \cos B \cos C) + \\ &\quad 2\sin B (\sin A \sin C - \cos A \cos C) - 2\cos A \cos B \sin C \\ &\quad + 2\sin A \sin B \sin C \\ &= 6\sin A \sin B \sin C - 2\sin A \cos B \cos C \\ &\quad - 2\cos A \sin B \cos C - 2\cos A \cos B \sin C \\ &= 6\sin A \sin B \sin C - 2\cos C \sin(A+B) \\ &\quad - 2\cos A \cos B \sin C \\ &= 6 \sin A \sin B \sin C - 2\cos C \sin C - 2\cos A \cos B \sin C \\ &= 6\sin A \sin B \sin C - 2\sin C (-\cos(A+B) +\cos A \cos B) \\ &= 6 \sin A \sin B \sin C - 2\sin C (\sin A \sin B) \\ &= 4\sin A \sin B \sin C. \end{align*}\]

So we have proved the identity.
