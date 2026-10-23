---
created: 2026-10-23T16:39:11 (UTC +06:00)
source: https://undergroundmathematics.org/trigonometry-compound-angles/r6807
author: Underground Mathematics (University of Cambridge)
rights: © University of Cambridge (Underground Mathematics). Use inside SyllabAI is authorised by the
  operator attestation of 2026-10-23 — see LICENSE-DATA.md (Amendment 2026-10-23) in this repository.
  Takedown / correction handling as stated in LICENSE-DATA.md.
tags:
- underground-mathematics
- trigonometry-compound-angles
- type/review-question
resource_identity:
  ugm_id: r6807
  station: trigonometry-compound-angles
  station_title: 'Trigonometry: Compound Angles'
  resource_type_id: 10
  resource_type_label: Review question
  level: null
  ref: 6807
  old_site_id: Q252
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
  exam_reference: UCLES A level Mathematics A 1, QP 9200/1, 1980, Q4
task: T-UGM-IMPORT-5
---

# Can we simplify $\cos 3\theta \sin 2\theta - \cos 4\theta \sin \theta$?

## Question

1. Prove that \[\cos 3\theta \sin 2\theta - \cos 4\theta \sin \theta = \cos 2\theta \sin \theta.\]

---

1. Starting from the relations \[\begin{align*} \sin(A+B) &{}= \sin A \cos B + \cos A \sin B,\\ \cos(A+B) &{}= \cos A \cos B - \sin A \sin B, \end{align*}\] obtain an expression for \(\tan(A+B)\) in terms of \(\tan A\) and \(\tan B\). Without the use of a calculator or tables, show that the sum of the three acute angles whose tangents are \(\dfrac{2}{9}\), \(\dfrac{1}{4}\) and \(\dfrac{1}{3}\) is \(\dfrac{\pi}{4}\).

## Suggestion

I don’t know any formulae that I think will help me directly to answer this question.

Perhaps I can use some of the formulae that I do know to get me started, at least? That might then give me some ideas for how to continue…

For the second part, I don’t know the angles themselves, and working out \(\arctan\frac{2}{9}\) and so on seems difficult (especially as I’m not allowed to use a calculator). Perhaps the question is hinting that I should use the formula for \(\tan(A+B)\) that I’ve just derived?

But there are three angles to add. Is there some way I can break down the problem?

Also, I know that the three acute angles are each less than …, so their sum is less than …

## Solution

**Approach 1**

We know

\(\sin 2\theta=2\sin\theta\cos\theta\)

, so the left hand side becomes

\[\begin{align*} \cos 3\theta \sin 2\theta - \cos 4\theta \sin \theta &{}= \cos 3\theta (2\sin\theta\cos\theta) - \cos 4\theta \sin \theta\\ &{}= \sin\theta(2\cos 3\theta\cos\theta - \cos 4\theta) \end{align*}\]

Now

\(\cos3\theta\cos\theta\)

appears in the expansion of

\(\cos 4\theta=\cos(3\theta+\theta)\)

, giving

\[\begin{align*} &\cos 3\theta \sin 2\theta - \cos 4\theta \sin \theta\\ &\qquad{}=\sin\theta(2\cos 3\theta\cos\theta - \cos 4\theta)\\ &\qquad{}=\sin\theta(2\cos 3\theta \cos\theta - (\cos 3\theta\cos\theta- \sin3\theta\sin\theta))\\ &\qquad{}=\sin\theta(\cos 3\theta \cos\theta + \sin3\theta\sin\theta)\\ &\qquad{}=\sin\theta\cos(3\theta-\theta)\\ &\qquad{}=\sin\theta\cos 2\theta. \end{align*}\]

**Approach 2**

Using the trig expansions we know for \(\sin(P+Q), \sin(P-Q), \cos(P+Q)\) and \(\cos(P-Q)\), we have

\[\begin{align*} \sin P\cos Q &{}= \dfrac{1}{2}(\sin(P+Q)+\sin(P-Q))\\ \cos P\sin Q &{}= \dfrac{1}{2}(\sin(P+Q)-\sin(P-Q))\\ \cos P\cos Q &{}= \dfrac{1}{2}(\cos(P+Q)+\cos(P-Q))\\ \sin P\sin Q &{}= -\dfrac{1}{2}(\cos(P+Q)-\cos(P-Q)) \end{align*}\]

Now putting \(A = P+Q\) and \(B = P-Q\), we have

\[\begin{align*} \sin A+\sin B &{}= 2\sin \frac{A+B}{2}\cos \frac{A-B}{2} \\ \sin A-\sin B &{}= 2\cos \frac{A+B}{2}\sin \frac{A-B}{2} \\ \cos A+\cos B &{}= 2\cos \frac{A+B}{2}\cos \frac{A-B}{2} \\ \cos A-\cos B &{}= -2\sin \frac{A+B}{2}\sin \frac{A-B}{2} \end{align*}\]

This gives

\[\begin{align*} \cos 3\theta \sin 2\theta &{}- \cos 4\theta \sin \theta \\ &\quad{}=\dfrac{1}{2}(\sin 5\theta-\sin\theta-\sin 5\theta+\sin 3\theta)\\ &\quad{}=\dfrac{1}{2}(\sin 3\theta-\sin\theta)\\ &\quad{}=\cos 2\theta \sin \theta. \end{align*}\]

We know \(\tan\theta=\dfrac{\sin\theta}{\cos\theta}\), giving

\[\begin{align*} \tan(A+B) &{}= \frac{\sin(A+B)}{\cos(A+B)} \\ &{}= \frac{\sin A\cos B + \cos A\sin B}{\cos A\cos B - \sin A\sin B}. \end{align*}\]

Now we divide the numerator and denominator of the fraction by \(\cos A\cos B\), giving

\[\begin{align*} \tan(A+B) &{}= \dfrac{\dfrac{\sin A}{\cos A} + \dfrac{\sin B}{\cos B}}{1 - \dfrac{\sin A\sin B}{\cos A\cos B}} \\ &{}= \dfrac{\tan A + \tan B}{1 - \tan A\tan B} \end{align*}\]

Call the three angles \(A\), \(B\) and \(C\), so that \(\tan A = \dfrac{2}{9}\), \(\tan B = \dfrac{1}{4}\) and \(\tan C = \dfrac{1}{3}\).

Then

\[\begin{align*} \tan(A+C) &{}= \frac{\tan A + \tan C}{1 - \tan A\tan C}\\ &= \frac{\frac{2}{9}+\frac{1}{3}}{1 - \frac{2}{9}\frac{1}{3}}\\ &= \frac{(\frac{5}{9})}{(\frac{25}{27})}\\ &= \frac{3}{5}. \end{align*}\]

Now

\[\begin{align*} \tan(A+C+B) &{}= \frac{\tan(A+C) + \tan B}{1 - \tan(A+C)\tan B}\\ &= \frac{\frac{3}{5}+\frac{1}{4}}{1 - \frac{3}{5}\frac{1}{4}}\\ &= \frac{(\frac{17}{20})}{(\frac{17}{20})}\\ &= 1. \end{align*}\]

We are told that \(A\), \(B\) and \(C\) are acute. Also, since \(\tan A\), \(\tan B\) and \(\tan C\) are all less than \(1\), the angles \(A\), \(B\) and \(C\) are all between \(0\) and \(\dfrac{\pi}{4}\). Therefore,\(0 < A + B + C < \dfrac{3\pi}{4}\).

So the only possible solution of \(\tan (A+B+C) = 1\) with \(A+B+C\) in this range is \(A+B+C = \dfrac{\pi}{4}\), as required.
