---
created: 2026-10-23T16:39:11 (UTC +06:00)
source: https://undergroundmathematics.org/trigonometry-compound-angles/transformation-or-not
author: Underground Mathematics (University of Cambridge)
rights: © University of Cambridge (Underground Mathematics). Use inside SyllabAI is authorised by the
  operator attestation of 2026-10-23 — see LICENSE-DATA.md (Amendment 2026-10-23) in this repository.
  Takedown / correction handling as stated in LICENSE-DATA.md.
tags:
- underground-mathematics
- trigonometry-compound-angles
- type/investigation
- level/developing
resource_identity:
  ugm_id: transformation-or-not
  station: trigonometry-compound-angles
  station_title: 'Trigonometry: Compound Angles'
  resource_type_id: 7
  resource_type_label: Investigation
  level: Developing
  ref: 7043
  old_site_id: F2_RT1_1
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
- path: https://undergroundmathematics.org/trigonometry-compound-angles/transformation-or-not/download/teacher-notes.pdf
  kind: printable
---

# Transformation... or not?

## Problem

**Do we always get new functions from old ones?**

Take a look at the graph below.

How would we describe it?

Can we describe it using a function we know?

## Things you might have noticed

The graph looks like a sine graph, so we could try and describe it using a transformation of the sine curve, \(y=R\sin(x+\alpha)\) where \(R>0\) and \(0<\alpha<\frac{\pi}{2}\).

Why can we choose \(0<\alpha<\frac{\pi}{2}\)?

Looking at the graph we can see that if this was given by a transformation of a sine graph the closest way to get to this graph is by a translation of a sine graph to the left, so \(\alpha\) will be positive. However, since the *peak* is between the \(x=0\) and \(x=\frac{\pi}{2}\) lines we can choose \(0<\alpha<\frac{\pi}{2}\) as our smallest amount we need to translate the curve.

Once we find this value for \(\alpha\), we can create similar graphs using \(\alpha+2\pi\) instead of \(\alpha\), since sine has a period of \(2\pi\).

We can also find the value of \(R\). Since the function has a maximum value of \(5\) and a minimum of \(-5\), we can conclude that \(R=5\).

Why can we choose \(R>0\)?

When trying to find \(\alpha\), we cannot obtain an exact value by looking at the graph, but we can see that \(\frac{\pi}{4}<\alpha<\frac{3\pi}{8}\).

Is there any way we could find out what \(\alpha\) is precisely?

**An alternative to sine**

We could have also have described this as a translated cosine graph, writing it in the form \(y=R\cos(x-\beta)\) where \(R>0\) and \(0<\beta<\frac{\pi}{2}\).

Why can we choose \(0<\beta<\frac{\pi}{2}\) this time?

Again, \(R=5\) by looking at the maximum \(y\) coordinate the graph has, but this time we can see that the translation of the cosine curve will mean that \(\frac{\pi}{8}<\beta<\frac{\pi}{4}\).

Is there any way we could find out what \(\beta\) is precisely?

Is there any connection between the value of \(\alpha\) and the value of \(\beta\)?

## Further questions

Below is the graph of \(y=3\sin x+4\cos x\).

How does this compare with the previous graph?

What function did you use to describe the previous graph?

Below are three graphs of similar functions, namely \[y=A\sin x+B\cos x,\] where \(A\) and \(B\) are real numbers.

Can you work out what \(A\) and \(B\) are for each of these graphs?

Can you describe each of them using a single trigonometric function?

You might want to refer back to [Things you might have noticed](https://undergroundmathematics.org/trigonometry-compound-angles/transformation-or-not/things-you-might-have-noticed) to help with this.

**Graph 1**

**Graph 2**

**Graph 3**

## Solution

How does this compare with the previous graph?

What function did you use to describe it?

The graphs are identical.

It therefore appears that we can rewrite a function of the form \[A\sin x+B\cos x,\] where \(A\) and \(B\) are real numbers, as \(R\sin(x+\alpha)\) where \(R>0\) and \(0<\alpha<\frac{\pi}{2}\).

Notice here that we found

\[\begin{equation} \label{eq:1} 5\sin(x+\alpha) = 3\sin x+4\cos x, \end{equation}\]

with \(\frac{\pi}{4}<\alpha<\frac{3\pi}{8}\) from the first problem. The numbers \(3\), \(4\) and \(5\) appear in this equation; does this give you any ideas about a possible relationship between \(A\), \(B\) and \(R\)?

What happens if we substitute different values of \(x\) into this identity?

Substituting \(x=0\) into equation \(\eqref{eq:1}\) gives \(5\sin\alpha=4\) and thus \(\sin\alpha=\frac{4}{5}\).

Below are three graphs of similar functions, namely \[y=A\sin x+B\cos x,\] where \(A\) and \(B\) are real numbers.

- Can you work out what \(A\) and \(B\) are for each of these graphs?

- Can you describe each of them using a single trigonometric function?

The question here is, how can we use the graphs and our knowledge of sine and cosine functions to find the values \(A\), \(B\), \(R\) and \(\alpha\)?

What does \(A\sin x+B\cos x\) tell us when \(x=0\) and when \(x=\frac{\pi}{2}\)?

**Graph 1**

From the graph we can see that when \(x=0\), \(A\sin x+B\cos x=-1\). This means that \(B=-1\).

When \(x=\frac{\pi}{2}\), \(A\sin x-1\cos x=1\) and thus \(A=1\). Hence we have one way of writing this function: \[y=\sin x-\cos x.\]

To write it as a single trigonometric function, we note this this looks like a sine graph which has been translated to the right by a little less than \(\frac{\pi}{3}\), so we could write it in the form \(y=R\sin(x-\alpha)\), where \(R>0\) and \(0<\alpha<\frac{\pi}{2}\).

Our initial idea that we could write a function of the form \(A\sin x+B\cos x\) as \(R\sin(x+\alpha)\), where \(R>0\) and \(0<\alpha<\frac{\pi}{2}\), therefore turns out to not be quite correct: we may have to translate the sine graph in the opposite direction. So maybe we can always write \(A\sin x+B\cos x\) as \(R\sin(x+\alpha)\) where \(R>0\) and \(-\frac{\pi}{2}<\alpha<\frac{\pi}{2}\)?

This new idea is certainly better; is it now correct, or does it need further modification?

Mathematicians frequently have initial ideas and then work to refine them by testing their ideas out with several well-chosen examples. These examples are designed to find the flaws in their initial ideas, which may sound a bit strange at first: don’t you want to show that your ideas work by finding lots of nice examples? Well, yes, but you also need to check that they doesn’t break on nasty ones!

We already know that our function is \(y=\sin x-\cos x\), and so we could begin by looking to work out \(\alpha\).

Starting with \[R\sin(x-\alpha)=\sin x -\cos x,\] we see that if we substitute \(x=\alpha\), then the left hand side is zero, and so we must have \(\sin\alpha=\cos\alpha\). As we are looking for \(0<\alpha<\frac{\pi}{2}\), this gives us \(\alpha=\frac{\pi}{4}\).

We now have \(R\sin(x-\frac{\pi}{4})=\sin x-\cos x\). How can we find \(R\)?

If we substitute in \(x=0\), we end up with something very nice, just as we did earlier: \[R\sin(-\tfrac{\pi}{4})=-1.\] Since \(\sin(-\frac{\pi}{4})=-\frac{1}{\sqrt{2}}\), we deduce that \(R=\sqrt{2}\), hence \[y=\sin x-\cos x=\sqrt{2}\sin(x-\tfrac{\pi}{4}).\]

**Graph 2**

From the graph we can see that when \(x=\frac{\pi}{2}\), \(A\sin x+B\cos x=1\), thus \(A=1\).

When \(x=\frac{\pi}{6}\), \(\sin x+B\cos x=2\), so \(\frac{1}{2}+B\frac{\sqrt{3}}{2}=2\) and thus \(B=\sqrt{3}\).

Hence we have one way of writing this function: \[y=\sin x+\sqrt{3}\cos x.\]

The graph also looks like a translated sine graph: it has a maximum value of \(2\), and has been translated \(\frac{\pi}{3}\) to the left. So we can also write it as \[y=2\sin(x+\tfrac{\pi}{3}).\]

Alternatively, we could think of it as a cosine graph shifted to the right by \(\frac{\pi}{6}\), giving \[y=2\cos(x-\tfrac{\pi}{6}).\]

**Graph 3**

We can see that this graph is just a reflection of Graph 2 in the \(x\)-axis. So we can immediately write down equations for the graph from our equations for Graph 2: \[y=-\sin x-\sqrt{3}\cos x=-2\sin(x+\tfrac{\pi}{3})=-2\cos(x-\tfrac{\pi}{6}).\]
