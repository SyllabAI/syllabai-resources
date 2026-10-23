---
created: 2026-10-23T16:39:10 (UTC +06:00)
source: https://undergroundmathematics.org/trigonometry-triangles-to-functions/equation-or-identity-i
author: Underground Mathematics (University of Cambridge)
rights: © University of Cambridge (Underground Mathematics). Use inside SyllabAI is authorised by the
  operator attestation of 2026-10-23 — see LICENSE-DATA.md (Amendment 2026-10-23) in this repository.
  Takedown / correction handling as stated in LICENSE-DATA.md.
tags:
- underground-mathematics
- trigonometry-triangles-to-functions
- type/package-of-problems
- level/developing
resource_identity:
  ugm_id: equation-or-identity-i
  station: trigonometry-triangles-to-functions
  station_title: 'Trigonometry: Triangles to Functions'
  resource_type_id: 5
  resource_type_label: Package of problems
  level: Developing
  ref: 6680
  old_site_id: G3_RT7_1
spec_map:
  curriculum_code: CIE-9709-P1-2023
  lane: cie-a-level-maths-20-pure-1
  board: Cambridge CIE
  syllabus_version: 2023-2025
  subsection: trigonometry-triangles-to-functions
  subsection_provenance:
    tier: PROVIDER
    signal: source-url-slug
    slug: trigonometry-triangles-to-functions
    validation_status: SUGGESTED
  spec_points:
  - code: 1.5.4
    provenance:
      tier: AI_SUGGESTED
      confidence: medium
      model_version: GLM (Super Z agent, z.ai) — P3c lane-5 cross-map (cross-map-trigonometry.json (P3c
        lane 5) @ syllabai-experimental 75f1cfb8)
      evidence: 'identity-vs-equation discipline on triangle-angle statements: complementary/supplementary
        symmetry (sin(pi/2−A)=cos A, sin(pi−A)=sin B) and sin^2+cos^2 work; the reciprocal (sec^2−tan^2=1)
        and compound (tan(A+B)=−tan C) statements ride P3/0606 — recorded'
      rationale: 'Canonical UGM title: “Equation or identity? (I)”'
      validation_status: SUGGESTED
    title: use the identities / tan i and cos i sin i + cos i / 1
  mapped_date: '2026-10-23'
  mapper: cross-map-trigonometry.json (P3c lane 5) @ syllabai-experimental f3ef5745
provenance:
  capture_date: '2026-10-22'
  capture_tool: P2 full-site crawl (ugm-crawl) → ugm-clean extraction; text-only import
  content_language: en
task: T-UGM-IMPORT-5
assets:
- path: https://undergroundmathematics.org/trigonometry-triangles-to-functions/equation-or-identity-i/download/teacher-notes.pdf
  kind: printable
---

# Equation or identity? (I)

> Excerpt: Here students consider some trigonometric equations in the context of triangles only, deciding whether any of these is in fact an identity. This should help to reinforce the distinction between equations and identities. There are plenty of opportunities for students try to justify their decisions, prove identities and find counter examples.

## Problem

Throughout, \(A\), \(B\) and \(C\) are the angles of a triangle.

For each of the following, decide whether it is an *identity* (true for all triangles) or an *equation* (there is a triangle for which it is not true).

If it is an identity, true for all triangles, then you should prove it (perhaps using trigonometric identities that you already know).

If it is an equation, then at the very least you should give an example of a triangle for which it is not true. You could also try to solve the equation (that is, find all triangles for which it is true).

1. \(\sin(\frac{\pi}{2} - A) = \cos A\)

---

1. \(\sec^2 A - \tan^2 A = 1\)

---

1. \(\tan(A + B) = - \tan C\)

---

1. \(\sin^2 A - \cos^2 B = 1\)

---

1. \(\sin(\pi - A) = \sin B\)

---

1. \(\sin^2 A - 3\cos A = \cosec^2 C - \cot^2 C\)

## Suggestion

To help you decide whether an expression is an equation or an identity, you could test it out on some particular triangles, perhaps using angles where you can easily evaluate the expression, or perhaps using particular types of triangle (isosceles or right-angled or equilateral, for example).

You might find it helpful to note down any properties of trigonometric functions or trigonometric identities that you know, so that you can think about which, if any, might be helpful at any given moment.

## Solution

1. We have to decide whether to show that this is an identity or to solve the equation. To help us decide, we could try some particular values. We should choose values that will lead to sines and cosines that we can compute easily, but not such special cases that they run the risk of misleading us. If we try \(A = \frac{\pi}{3}\), the left-hand side becomes \(\sin(\frac{\pi}{6}) = \frac{1}{2}\) and the right-hand side is \(\cos(\frac{\pi}{3}) = \frac{1}{2}\). So the equation holds in this case. Doing that example might have reminded us of a useful diagram.        We define \(\cos A\) to be the adjacent over the hypotenuse. But we can see that this is precisely the sine of the other angle that isn’t a right angle, which is \(\frac{\pi}{2} - A\). So we have \(\sin(\frac{\pi}{2} - A) = \cos A\).  Alternatively we could think about the connection between the graphs of sine and cosine.

---

1. One of our key trigonometric identities is that \(\sin^2 A + \cos^2 A = 1\) for all angles \(A\) (not just those in a triangle). We might recognise the equation in the question as a common variant.  We know the familiar identity \[\sin^2 A + \cos^2 A = 1.\] Dividing through by \(\cos^2 A\) gives \[\tan^2 A + 1 = \sec^2 A,\] and we can rearrange this to \[\sec^2 A - \tan^2 A = 1.\] We should be slightly more careful, however: we cannot divide by \(\cos^2 A\) if it is zero, and this could happen when \(A\) is an angle of a triangle. The equation holds for all values of \(A\) in the range except \(A = \frac{\pi}{2}\) (when the left-hand side is undefined).

---

1. We might try some values here. We might also remember that \(A\), \(B\) and \(C\) are the angles of a triangle, so \(A + B + C = \pi\).  We have \[\tan(A + B) = \tan(\pi - C)\] whenever both sides are defined (that is, whenever \(C\) is not a right angle).  It may be convenient to refer to a sketch of \(y = \tan x\).     We know that tan is a [periodic](https://undergroundmathematics.org/glossary/periodic-function) function, with period \(\pi\), so \[\tan(\pi - C) = \tan(-C).\] Since tan is an [odd function](https://undergroundmathematics.org/glossary/odd-function), we have \[\tan(-C) = -\tan C.\] Putting this together, we find that \[\tan(A + B) = - \tan C\] for all triangles where \(C\) is not a right angle.

---

1. Let’s try some values to try to get a feel for whether this is an equation or an identity. If \(A = B = \frac{\pi}{4}\) (note that these are indeed possible angles in a triangle), then \[\sin^2 A - \cos^2 B = 0.\] So it is not an identity; we should try to find the values for which the equation does hold. One difficulty about the given equation is that the two terms on the left differ in two ways: sine versus cosine, and \(A\) versus \(B\). We could do something about that by replacing the \(1\) on the right-hand side by \(\sin^2 A + \cos^2 A\).  If \[\sin^2 A - \cos^2 B = 1,\] then \[\sin^2 A - \cos^2 B = \sin^2 A + \cos^2 A,\] so \[-\cos^2 B = \cos^2 A.\] The right-hand side is always at least zero, whereas the left-hand side is always at most zero. The only way they can be the same is if they are both zero. So if \(A\) and \(B\) are part of a triangle that satisfies the equation, then \(\cos A = \cos B = 0\). This means that \(A = B = \frac{\pi}{2}\), and this is not possible in a triangle (at least in a non-[degenerate](https://undergroundmathematics.org/glossary/degenerate) triangle). So there are no solutions to the equation.

---

1. It’s reasonably clear that this cannot be an identity; it will be easy to think of examples of angles for which it does not hold, because there’s so much flexibility about choosing \(A\) on the left-hand side and \(B\) on the right-hand side. So we should try to solve the equation.  We know that \(\sin(\pi - A) = \sin A\), so we are looking to solve \[\sin A = \sin B.\] This has the obvious solutions \(A = B\), but also the slightly less obvious solutions \(B = \pi - A\). The latter cannot happen for a (non-degenerate) triangle, so we see that a triangle satisfies the equation if and only if it is isosceles with \(A = B\).

---

1. This is rather complicated. How might we simplify it? We might recognise the right-hand side as something that we could simplify.  We have \[\sin^2 C + \cos^2 C = 1,\] so dividing through by \(\sin^2 C\) gives \[1 + \cot^2 C = \cosec^2 C,\] and so \[\cosec^2 C - \cot^2 C = 1.\] This holds as long as \(\sin C\) is not zero, and this will be true when \(C\) is an angle of a (non-degenerate) triangle. So the equation we’re given is \[\sin^2 A - 3 \cos A = 1.\]  We can make this more manageable by replacing \(\sin^2 A\) with something involving \(\cos A\).  This is equivalent to \[(1 - \cos^2 A) - 3\cos A = 1,\] that is, \[\cos^2 A + 3\cos A = 0.\] Factorising, this becomes \[\cos A (\cos A + 3) = 0,\] so \(\cos A = 0\) or \(\cos A = -3\). The latter option is not possible, so if we have a solution then we must have \(\cos A = 0\) and so \(A = \frac{\pi}{2}\). We see that a triangle with angles \(A\), \(B\) and \(C\) satisfies the equation if and only if it is right-angled with a right angle at \(A\).  Notice that although \(C\) appears in the equation we’re given, whether or not there is a solution does not depend on \(C\).
