---
created: 2026-10-24T22:06:39 (UTC +06:00)
source: https://undergroundmathematics.org/exp-and-log/log-lattice
author: Underground Mathematics (University of Cambridge)
rights: © University of Cambridge (Underground Mathematics). Use inside SyllabAI is authorised by the
  operator attestation of 2026-10-23 — see LICENSE-DATA.md (Amendment 2026-10-23) in this repository.
  Takedown / correction handling as stated in LICENSE-DATA.md.
tags:
- underground-mathematics
- exp-and-log
- type/fluency-exercise
- level/developing
resource_identity:
  ugm_id: log-lattice
  station: exp-and-log
  station_title: Exponentials & Logarithms
  resource_type_id: 8
  resource_type_label: Fluency exercise
  level: Developing
  ref: 6986
  old_site_id: "A4_RT11_3"
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
      evidence: "logarithms in different bases arranged into a grid 'without using a calculator' - bounds from indices plus monotonicity of log functions"
      rationale: "Canonical UGM title: Logarithm lattice"
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

# Logarithm lattice

> Excerpt: This resource asks students to arrange some logarithms in size order and complete a grid. Students have to think about different bases as well as logarithms of different numbers. The task starts with specific numbers but can be generalised to thinking about increasing and decreasing logarithmic functions.

## Problem

Can you arrange some of these logarithms to complete the grid below? The values of the logarithms need to increase along the rows and down the columns. Try to do this without using a calculator.

\(\log_{3} 2\)

\(\log_{4} 5\)

\(\log_{2} 5\)

\(\log_{3} 4\)

\(\log_{3} 5\)

\(\log_{5} 3\)

\(\log_{2} 3\)

\(\log_{5} 2\)

\(\log_{5} 4\)

\(\log_{4} 3\)

\(\log_{4} 2\)

\(\log_{2} 4\)

You might find it helpful to think about the following questions:

- Can you put pairs of logarithms from the list in order of size?

- Which logarithms are bigger than \(1\) and which ones are smaller?

Suggestion 1

Which is bigger:

- \(\log_{2} 5\) or \(\log_{2} 3\)?

- \(\log_{2} 5\) or \(\log_{3} 5\)?

Suggestion 2

Can you explain why this inequality is true?

\[\log_{5} 2 < 1 < \log_{2} 5\]

You could do this by thinking about what \(\log_{5} 2\) means or by thinking about how you could write \(1\) as a logarithm.

Can you use the same logarithms to complete this grid too?

\(\log_{3} 2\)

\(\log_{4} 5\)

\(\log_{2} 5\)

\(\log_{3} 4\)

\(\log_{3} 5\)

\(\log_{5} 3\)

\(\log_{2} 3\)

\(\log_{5} 2\)

\(\log_{5} 4\)

\(\log_{4} 3\)

## Solution

Can you arrange some of these logarithms to complete the grid below? The values of the logarithms need to increase along the rows and down the columns. Try to do this without using a calculator.

\[\log_{3} 2 \quad \log_{4} 5 \quad \log_{2} 5 \quad \log_{3} 4 \quad \log_{3} 5 \quad \log_{5} 3\] \[\log_{2} 3 \quad \log_{5} 2 \quad \log_{5} 4 \quad \log_{4} 3 \quad \log_{4} 2 \quad \log_{2} 4\]

|  | Increasing size \(\longrightarrow\) |  |  |
|---|---|---|---|
| Increasing size \(\downarrow\) | \(\log_{\square} \square\) | \(\log_{\square} \square\) | \(\log_{\square} \square\) |
| \(\log_{\square} \square\) | \(1\) | \(\log_{\square} \square\) |  |
| \(\log_{\square} \square\) | \(\log_{\square} \square\) | \(\log_{\square} \square\) |  |

If we think about putting some of these logarithms in order, perhaps by visualising the graph of a logarithmic function or remembering that \(\log_2 x\) is an increasing function, we can form inequalities such as \[\log_{2} 3 < \log_{2} 4 < \log_{2} 5\] and \[\log_{3} 2 < \log_{3} 4 < \log_{3} 5 .\]

Next, we can form inequalities such as \[\log_{5} 3 < \log_{4} 3 < \log_{2} 3\] either by

- thinking about what the base of a logarithm means (we require a smaller power of \(5\) than of \(4\) to make \(3\)), or by

- changing the base (\(\log_{4} 3=\log_{4} 5\times\log_{5} 3\) and \(\log_{4} 5>1\)), or by

- noting that \(\log_x 3\) is a decreasing function.

Finally, there are a number of ways to obtain an inequality such as \[\log_{5} 2 < 1 < \log_{2} 5 .\] For instance,

- remember that \(\log_{2} 5\) is the power to which we need to raise \(2\) in order to get \(5\), so it must be greater than \(1\). Similarly, \(\log_{5} 2\) must be less than \(1\). Or,

- write \(1\) as \(\log_{5} 5\) and use the ideas above to obtain the inequality \(\log_{5} 2 < \log_{5} 5 =1\). Similarly, \(\log_2 5>\log_{2} 2=1\). Or,

- use the rule for changing the base: \(\log_{5} 2\times\log_{2} 5=\log_{5} 5=1\) so the two logarithms are reciprocals.

We have referred to a lot of different ideas here. Make sure you can convince yourself that the reasoning is all correct.

Using all these ideas, can you summarise what we know about the order of the logarithms in some kind of a diagram?

Here is a network in order of increasing value

Here is one possible way to complete the first grid

|  | Increasing size \(\longrightarrow\) |  |  |
|---|---|---|---|
| Increasing size \(\downarrow\) | \(\log_{5} 2\) | \(\log_{4} 2\) | \(\log_{3} 2\) |
| \(\log_{5} 3\) | \(1\) | \(\log_{2} 4\) |  |
| \(\log_{2} 3\) | \(\log_{3} 5\) | \(\log_{2} 5\) |  |

For the second grid, our network of inequalities doesn’t give quite enough information to complete the bottom-left and top-right cells. However, we know that \(\log_{2}4 = 2\), and if we let \(\log_{3} 5=x\) then \(3^{x}=5\), so \(x\) must be less than \(2\). Therefore \[\log_{3} 5 < \log_{2}4 .\]

We can use a similar argument starting with \(\log_{4}2\) to give us a solution. Or we could think about reciprocals: \[\log_{5} 3=\frac{1}{\log_{3} 5} \quad\text{ and }\quad \log_{4}2=\frac{1}{\log_{2}4}\] and use that to write another inequality based on the one above.

Here is one possible way to complete the second grid

|  | Increasing size \(\longrightarrow\) |  |  |
|---|---|---|---|
| Increasing size \(\downarrow\) | \(\log_{4} 2\) | \(\log_{4} 3\) | \(\log_{4} 5\) |
| \(\log_{5} 3\) | \(1\) | \(\log_{3} 5\) |  |
| \(\log_{5} 4\) | \(\log_{3} 4\) | \(\log_{2} 4\) |  |

See the resource [Changing bases](https://undergroundmathematics.org/exp-and-log/changing-bases) for an exploration of the rule for changing bases and the behaviour of logarithmic functions.

## Taking it further

We have extended one possible solution grid. Can you use other logarithms to complete the four blank cells of this grid or one based on your own solution grid?

|  | Increasing size \(\longrightarrow\) |  |  |  |  |
|---|---|---|---|---|---|
| Increasing size \(\downarrow\) |  |  | \(\log_{\square} \square\) |  |  |
|  | \(\log_{4} 2\) | \(\log_4 3\) | \(\log_{4} 5\) |  |  |
| \(\log_{\square} \square\) | \(\log_{5} 3\) | \(1\) | \(\log_{3} 5\) | \(\log_{\square} \square\) |  |
|  | \(\log_{5} 4\) | \(\log_3 4\) | \(\log_{2} 4\) |  |  |
|  |  | \(\log_{\square} \square\) |  |  |  |

Some things to think about:

- Try to make your extra logarithms as general as possible. For instance if you want \(\log_{a} 3\) to be less than \(\log_{5} 3\), what conditions must \(a\) satisfy?

- How could you include fractions or irrational numbers in your logarithms?

## Further solution

We have extended one possible solution grid. Can you use other logarithms to complete the four blank cells of this grid or one based on your own solution grid?

|  | Increasing size \(\longrightarrow\) |  |  |  |  |
|---|---|---|---|---|---|
| Increasing size \(\downarrow\) |  |  | \(\log_{\square} \square\) |  |  |
|  | \(\log_{4} 2\) | \(\log_4 3\) | \(\log_{4} 5\) |  |  |
| \(\log_{\square} \square\) | \(\log_{5} 3\) | \(1\) | \(\log_{3} 5\) | \(\log_{\square} \square\) |  |
|  | \(\log_{5} 4\) | \(\log_3 4\) | \(\log_{2} 4\) |  |  |
|  |  | \(\log_{\square} \square\) |  |  |  |

Some things to think about

- Try to make your extra logarithms as general as possible. For instance if you want \(\log_{a} 3\) to be less than \(\log_{5} 3\) what conditions must \(a\) satisfy?

- How could you include fractions or irrational numbers in your logarithms?

In order to fill in the box at the left of the grid, we require a logarithm that is smaller than \(\log_{5} 3\). Two possible solutions are \(\log_{6} 3\) and \(\log_{5} 2\). Both of these are less than \(\log_{5} 3\).

In order to give a more general logarithm for this cell, let’s think about when \(\log_{5} a < \log_{5} 3\). We know \(a\) cannot be zero or negative because then it would not be possible to calculate its logarithm. In addition to this, \(\log_{5} a\) will only be smaller than \(\log_{5} 3\) when \(a < 3\). So we need \(0 < a < 3\).

Notice that \(a\) does not have to be a whole number—it could be a fraction or an irrational number. Note too that the value of the logarithm can be negative.

Alternatively, still thinking about the same cell, we could try a logarithm of the form \(\log_{b} 3\). This would be smaller than \(\log_{5} 3\) if \(b > 5\). Is it possible for the base of the logarithm, \(b\), to be a fraction or an irrational number? If so, are there any other values of \(b\) that would make \(\log_{b} 3\) smaller than \(\log_{5} 3\)?

Now suppose we wrote \(\log_{b} 4\) in the box at the bottom of the grid. This must be greater than \(\log_{3} 4\) so we need \(b < 3\), but this time there are other constraints on \(b\) because you cannot use \(1\), \(0\) or any negative number as the base of a logarithm. Also, if the base, \(b\) is between \(0\) and \(1\), then \(\log_b 4\) will be negative, so the correct constraint would be \(1 < b < 3\).

To understand fractional bases of logarithms, it might help to think about \(\log_{\frac{1}{2}} 4\). \[\big(\frac{1}{2}\big)^{-2}=(2)^2=4 \quad\text{ so }\quad \log_{\frac{1}{2}} 4=-2\]

Can you sketch the graph of \(y=\log_x 4\)? Try using graphing software such as [Desmos](https://www.desmos.com/calculator) (find \(\log_a\) on its functions menu). You might also find the resource [Changing bases](https://undergroundmathematics.org/exp-and-log/changing-bases) helpful for thinking about the behaviour of logarithmic functions with different bases.

Here is one possible way to complete the grid

|  | Increasing size \(\longrightarrow\) |  |  |  |  |
|---|---|---|---|---|---|
| Increasing size \(\downarrow\) |  |  | \(\log_{4} a\) \(0 < a < 3\) |  |  |
|  | \(\log_{4} 2\) | \(\log_4 3\) | \(\log_{4} 5\) |  |  |
| \(\log_{b} 3\) \(b > 5\) or \(0 < b < 1\) | \(\log_{5} 3\) | \(1\) | \(\log_{3} 5\) | \(\log_{3} a\) \(a > 5\) |  |
|  | \(\log_{5} 4\) | \(\log_3 4\) | \(\log_{2} 4\) |  |  |
|  |  | \(\log_{b} 4\) \(1 < b < 3\) |  |  |  |
