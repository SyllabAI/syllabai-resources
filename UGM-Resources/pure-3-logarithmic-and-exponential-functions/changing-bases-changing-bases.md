---
created: 2026-10-24T22:06:39 (UTC +06:00)
source: https://undergroundmathematics.org/exp-and-log/changing-bases
author: Underground Mathematics (University of Cambridge)
rights: © University of Cambridge (Underground Mathematics). Use inside SyllabAI is authorised by the
  operator attestation of 2026-10-23 — see LICENSE-DATA.md (Amendment 2026-10-23) in this repository.
  Takedown / correction handling as stated in LICENSE-DATA.md.
tags:
- underground-mathematics
- exp-and-log
- type/package-of-problems
- level/developing
resource_identity:
  ugm_id: changing-bases
  station: exp-and-log
  station_title: Exponentials & Logarithms
  resource_type_id: 5
  resource_type_label: Package of problems
  level: Developing
  ref: 9018
  old_site_id: "A4_RT7_1"
spec_map:
  curriculum_code: CIE-9709-P3-2023
  lane: cie-a-level-maths-20-pure-3
  board: Cambridge CIE
  syllabus_version: 2023-2025
  subsection: exp-and-log
  subsection_provenance:
    tier: PROVIDER
    signal: source-url-slug
    slug: exp-and-log
    validation_status: SUGGESTED
  spec_points:
  - code: 3.2.1
    provenance:
      tier: AI_SUGGESTED
      confidence: medium
      model_version: "GLM (Super Z agent, z.ai) — P3c lane-10 cross-map (cross-map-log-and-exp.json (P3c lane 10) @ syllabai-experimental 980556af)"
      evidence: "2log_4 x = log_2 x and the y=log_5 x graph family - base relations derived from the definition of a logarithm as the index; the change-of-base FORMULA itself is not required, so the 3.2.1 exclusion is respected (prior routing of record: lane-5 '2.2')"
      rationale: "Canonical UGM title: Changing bases"
      validation_status: SUGGESTED
    title: "understand the relationship between logarithms and indices, and use the laws of logarithms (excluding change of base)"
  mapped_date: '2026-10-25'
  mapper: cross-map-log-and-exp.json (P3c lane 10) @ syllabai-experimental 980556af
provenance:
  capture_date: '2026-10-22'
  capture_tool: P2 full-site crawl (ugm-crawl) → ugm-clean extraction; text-only import
  content_language: en
  task: T-UGM-IMPORT-10
---

# Changing bases

> Excerpt: In this resource students explore how logarithms of different bases are related. A set of graphical problems are presented, based on a graph of $\log_5 x$, and a set of algebraic problems.

## Warm-up

For any positive number \(x\), can you *explain* why this result is true?

\[2\log_4 x=\log_2 x\]

Can you describe what \(\log_4 x\) and \(\log_2 x\) are in words?

Suggestion

\(\log_4 x\) is the power that we’d need to raise \(4\) to if we wanted to get \(x\), and \(\log_2 x\) is the power that we’d need to raise \(2\) to if we wanted to get \(x\).

Which of the following is correct?

\[2\log_6 x=\log_3 x \quad 3\log_9 x=\log_3 x \quad 2\log_9 x=\log_3 x\]

Test your answer

Thinking about how logarithms are defined, the equation \(2\log_4 x=\log_2 x\) seems to hold because \(4\) is \(2^2\), rather than because \(4\) is \(2\) ‘doubled’. Therefore of the three alternatives, \(2\log_9 x=\log_3 x\) is likely to be the equivalent result, but for base \(3\) and \(9\). To check this, let \(\log_{9} x = k.\) Then \(x=9^{k}\), so \[\log_{3}x= \log_{3}9^{k}=\log_{3}3^{2k}=2k= 2\log_9 x.\]

What is a general statement of this result?

Suggestion

There are various relationships here that we can start to generalise.

- How is \(\log_{a}x\) related to \(\log_{a^{2}}x\) ?

- How is \(\log_{a}x\) related to \(\log_{a^{n}}x\)?

- How is \(\log_{a}x\) related to \(\log_{b}x\)? How can we express the relationship between \(a\) and \(b\)?

Test your answer

From the examples above, we can see that \[\log_{a}x= 2\log_{a^{2}}x,\] which we could generalise to \[\log_{a}x= n\log_{a^{n}}x.\] Thinking about \(n\)’s role in this equation brings us to

\[\log_a x=(\log_a b)(\log_b x)\] or equivalently \[\log_{b}x=\frac{\log_{a}x}{\log_{a}b}.\]

What conditions must \(x,a,b\) satisfy here? Could the second of these ever risk division by \(0\)?

## Some graphical problems

Here is a graph of \(y=\log_{5} x\)

Use this graph of \(y=\log_{5} x\) to help you to draw graphs of

1. \(\log_{25}x\)

---

1. \(\log_{\sqrt{5}}x\)

---

1. \(\log_{\frac{1}{5}}x\)

---

1. \(\log_{10} x\)

---

1. \(\log_{x} 5\)

Try to make your graphs as accurate as you can, but use the graph of \(y=\log_{5}x\) to help you, rather than a calculator.

You could try to sketch the graphs first, thinking about which points the graphs go through and which graphs will give larger or smaller values for the same value of \(x\). You may find it helpful to look back at the warm-up.

You can draw your graphs on the [printable larger version](https://undergroundmathematics.org/exp-and-log/changing-bases/components/graph.pdf) of the \(y=\log_{5}x\) graph.

## Graph solutions

Here are graphs 1 and 2 drawn using values from the \(y=\log_{5}x\). The relationships between each graph and the graph of \(y=\log_{5}x\) are described below.

1. \(\log_{25} x = (\log_{25} 5)(\log_{5} x) = \frac{1}{2}\log_{5} x\), so the graph of \(y = \log_{25} x\) is a stretch of the graph \(y=\log_{5}x\) parallel to the \(y\)-axis and scale factor \(\frac{1}{2}\).

---

1. \(\log_{\sqrt{5}}x= (\log_{\sqrt{5}} 5)(\log_{5} x)=2\log_{5} x\), so the graph of \(y=\log_{\sqrt{5}}x\) is a stretch of the graph \(y=\log_{5}x\) parallel to the \(y\)-axis and scale factor \(2\).

Thinking about the definition of logarithms, as we did in the warm-up, these results make sense. For example, we’d expect the power that we’d raise \(5\) to in order to get a given value of \(x\) to be twice as much as the power we’d need to raise \(25\) to.

1. As \(\dfrac{1}{5} = 5^{-1}\), the power that we’d raise \(\dfrac{1}{5}\) to in order to get a given value of \(x\) is \(-1\) times the power we’d need to raise \(5\) to. Alternatively, using the idea from the warm-up, \[\log_{\frac{1}{5}}x=(\log_{\frac{1}{5}} 5)(\log_{5}x)=-\log_{5}x\] and so the graph of \(y = \log_{\frac{1}{5}}x\) is a reflection in the \(x\)-axis of the graph of \(y=\log_{5}x\).

1. More work is needed for the graph of \(y=\log_{10} x\). We know that \(\log_{10}x= \dfrac{\log_{5} x}{\log_{5} 10}\), so we need to divide by \(\log_{5}10\) to get the graph of \(y=\log_{10}x\). The given graph doesn’t go up as far as \(x=10\), but \(\log_{5}10 = \log_{5}5+ \log_{5}2 = 1+ \log_{5}2\). From the graph, \(\log_{5} 2 \approx 0.42\). Now, \(1 \div 1.42 = \frac{100}{142}=\frac{50}{71}\approx\frac{49}{70} = 0.7\) so the graph of \(y=\log_{10}x\) is a stretch of \(y=\log_{5}x\) parallel to the \(y\)-axis, scale factor \(0.7\).

1. For \(x>0\) with \(x\neq 1\), (\(\log_{5}x)(\log_{x}5)= \log_{5}5=1\), so \(\log_{x}5\) is the reciprocal of \(y=\log_{5}x\). We can use this to plot particular points to get an idea of the shape of the graph \(y=\log_{x}5\).

Alternatively, we can use the behaviour of the function \(\log_{5} x\) to sketch the behaviour. For \(x>1\), as \(x\) increases, \(\log_{5}x\) increases and is positive, so \(\log_{x}5\) decreases and is positive. For \(x\) close to \(1\), \(\log_{5} x\) is close to \(0\), and the graph of \(y=\log_{x}5\) has an asymptote at \(x=1\). For \(0< x <1\), \(\log_{5}x\) is negative. It increases to \(0\) as \(x\) increases to \(1\), and tends to \(-\infty\) as \(x\) decreases to \(0\). The graph of \(y=\log_{x}5\) gets steeper and closer to the \(y\)-axis as \(x\) decreases to \(0\), but it doesn’t actually meet the \(y\)-axis because \(\log_{x}5\) isn’t defined for \(x=0\).

## Some algebraic problems

1. Evaluate the following. Can you do this without calculating each factor separately?  \((\log_3 9)(\log_9 81)\) \((\log_3 81)(\log_{81} 9)\)

---

1. Write the following as a single logarithm. What conditions must \(x\) and \(y\) satisfy?  \((\log_{10} 5)(\log_{5} x)\) \((\log_{10} x)(\log_{x} y)(\log_{y} 3)\)

---

1. Simplify the following. What conditions must \(x\) and \(y\) satisfy?  \((\log_{x} y)(\log_{y} 10)(\log_{8} x)\) \((\log_{x} y)(\log_{8} x)(\log_{y} 8)\)

---

1. The value of \(\log_2 3\) is approximately \(1.6\). Can you use this to approximate \(\log_4 27\)? What about \(\log_8 27?\) Can you generalise this result?

---

1. Evaluate  \(\dfrac{\log_{2} 5}{\log_{2} 25}\) \(\dfrac{\log_{10} 5}{\log_{10} 3}\)

---

1. Given that \(\log_x y=4\) and \(\log_y 2 = 9\), evaluate  \((\log_x 2)(\log_y x)\) \(\dfrac{\log_x 2}{\log_y x}\)

---

1. What is \((\log_a b^3)(\log_b a^3)\)?

---

1. What is the relationship between \(\log_a b\) and \(\log_b a\)?

---

1. Solve \(\log_{x} 7 = \log_{7} x\).

## Algebra solutions

1. Evaluate the following. Can you do this without calculating each factor separately?  \((\log_3 9)(\log_9 81)\) \((\log_3 81)(\log_{81} 9)\)

Using the generalised version of the result in the warm-up,

1. \((\log_3 9)(\log_9 81)=\log_{3}81=4\)

---

1. \((\log_3 81)(\log_{81} 9)= \log_{3}9=2\).

1. Write the following as a single logarithm. What conditions must \(x\) and \(y\) satisfy?  \((\log_{10} 5)(\log_{5} x)\) \((\log_{10} x)(\log_{x} y)(\log_{y} 3)\)

Using the same idea as in question 1, (a) \((\log_{10} 5)(\log_{5} x)=\log_{10} x\).

For part (b), one approach is

\[(\log_{10} x)(\log_{x} y)(\log_{y} 3) = (\log_{10} y)(\log_{y} 3) = \log_{10}3\]

Since \(x\) and \(y\) both occur as bases of logarithms in these expressions, \(x\) and \(y\) must both be positive, but can’t be \(1\).

1. Simplify the following. What conditions must \(x\) and \(y\) satisfy?  \((\log_{x} y)(\log_{y} 10)(\log_{8} x)\) \((\log_{x} y)(\log_{8} x)(\log_{y} 8)\)

1. \((\log_{x} y)(\log_{y} 10)(\log_{8} x)=(\log_{x} 10)(\log_{8} x)= (\log_{8} x)(\log_{x} 10)= \log_{8}10\).

---

1. \((\log_{x} y)(\log_{8} x)(\log_{y} 8)= (\log_{8} x)(\log_{x} y)(\log_{y} 8)= (\log_{8} y)(\log_{y} 8) = \log_{8}8=1\).

Again, since \(x\) and \(y\) both occur as bases of logarithms in these expressions, \(x\) and \(y\) must both be positive, but can’t be \(1\).

1. The value of \(\log_2 3\) is approximately \(1.6\). Can you use this to approximate \(\log_4 27\)? What about \(\log_8 27?\)

If we start by using the law for manipulating logs of powers, we get \(\log_{4} 27 = 3 \log_{4} 3\).

From the definition of logarithms, we know that \(\log_{4}3\) is smaller than \(\log_{2} 3\), so we can expect the answer to be less than \(4.8\). In fact, we can say more than this, because \(\log_{4} 3< 1 < \log_{2} 3\), so we should expect the answer to be less than \(3\).

From the warm-up we know that \(\log_{4} 3 = \frac{1}{2}\log_{2} 3\). Therefore \(\log_{4} 27 = 3 (\log_{4} 2)(\log_{2}3) \approx 3 \times \frac{1}{2}\times 1.6 = 2.4\).

We know that \(\log_{8} 27\) will be smaller than \(\log_4 27\). By manipulating powers and changing the base, we get \(\log_{8} 27 = 3(\log_{8}2)(\log_{2}3)= \log_{2}3 \approx 1.6\).

Note that from the second part we have \(\log_{2^{3}}3^{3}= \log_{2} 3\). In general, \(\log_{a^{k}}b^{k}= \log_{a} b\) for any positive \(a\), \(b\) with \(a\neq 1\) and any power \(k\). How could you prove this?

1. Evaluate  \(\dfrac{\log_{2} 5}{\log_{2} 25}\) \(\dfrac{\log_{10} 5}{\log_{10} 3}\)

1. \(\dfrac{\log_{2} 5}{\log_{2} 25}= \dfrac{\log_{2} 5}{(\log_{2}5)(\log_{5}25)}= \dfrac{1}{2}\)

---

1. \(\dfrac{\log_{10} 5}{\log_{10} 3}=\dfrac{(\log_{10} 3)(\log_{3}5)}{\log_{10} 3}=\log_{3}5\)

Alternatively, we could use the fraction form of the general result in the warm-up.

1. Given that \(\log_x y=4\) and \(\log_y 2 = 9\), evaluate  \((\log_x 2)(\log_y x)\) \(\dfrac{\log_x 2}{\log_y x}\)

1. \((\log_x 2)(\log_y x)= (\log_y x)(\log_x 2)= \log_{y} 2 = 9\).

---

1. Using ideas from question 5, or the two forms for changing base given in the warm-up, the numerator can be rewritten as \((\log_x y)(\log_{y}2)\) and the denominator as \(\dfrac{\log_{x}x}{\log_x y}\).

Therefore

\[\begin{align*} \frac{\log_x 2}{\log_y x} &{}= \frac{(\log_x y)(\log_{y}2)}{\dfrac{\log_{x}x}{\log_x y}}\\ &{}= (\log_{x}y)^{2}\log_{y}2\\ &{}= 16 \times 9\\ &{}= 144 \end{align*}\]

1. What is \((\log_a b^3)(\log_b a^3)\)?

Using laws for manipulating logs of powers, \[(\log_a b^3)(\log_b a^3)=9(\log_a b)(\log_b a) = 9 \log_{a} a = 9.\]

1. What is the relationship between \(\log_a b\) and \(\log_b a\)?

In questions 3 and 7 we had something of the form \((\log_{a} b)(\log_{b} a) = \log_{a} a\), so \((\log_{a} b)(\log_{b} a)=1\), or equivalently \(\log_{a} b = \dfrac{1}{\log_{b}a}\). Is there any danger of dividing by \(0\) here?

1. Solve \(\log_{x} 7 = \log_{7} x\).

Using the relationship in question 8, solving \(\log_{x} 7 = \log_{7} x\) is equivalent to solving \((\log_{7}x)^{2} = 1\). Therefore we need to solve \(\log_{7} x = 1\) and \(\log_{7} x = -1\), which give us \(x=7\) and \(x=\dfrac{1}{7}\) as solutions.
