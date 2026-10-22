---
created: 2026-10-23T12:00:00 (UTC +06:00)
source: https://undergroundmathematics.org/quadratics/factorisable-quads
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
  ugm_id: factorisable-quads
  station: quadratics
  station_title: Quadratics
  resource_type_id: 5
  resource_type_label: Package of problems
  level: Developing
  ref: 7954
  old_site_id: E1_RT7_1
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
      evidence: Fluency family on factorisable quadratics.
      rationale: 'Canonical UGM title: “Factorisable quadratics”'
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
---

# Factorisable quadratics

> Excerpt: This problem encourages students to think about the structure of factorisable quadratics and how the coefficients of such quadratics are related to each other.  It also offers practice in factorisation and multiplying out pairs of brackets.

## Problem

1. The quadratic \(x^2+4x+3\) factorises as \((x+1)(x+3)\). In both the original quadratic and the factorised form, all of the coefficients are integers.  The quadratic \(x^2-4x+3=(x-1)(x-3)\) similarly factorises with all of the coefficients being integers.  **How many** quadratics of the following forms factorise with integer coefficients? Here, \(b\) is allowed to be any integer (positive, negative or zero). For example, in (a), \(b\) could be \(-7\), since \((x-2)(x-5)=x^2-7x+10\).
  1. \(x^2+bx+10\)
  2. \(x^2+bx+30\)
  3. \(x^2+bx-8\)
  4. \(x^2+bx-16\)
  5. \(2x^2+bx+6\)
  6. \(6x^2+bx-20\)
2. This time, it is the constant which is allowed to vary.  How many quadratics of the following forms factorise with integer coefficients? Here, \(c\) is allowed to be any **positive** integer.
  1. \(x^2+6x+c\)
  2. \(x^2-10x+c\)
  3. \(3x^2+5x+c\)
  4. \(10x^2-6x+c\)
3. What are the answers to question 2 if \(c\) is only allowed to be a **negative** integer?

### Generalising

1. Can you generalise your answers to the above questions?
  1. Generalising question 1, if \(c\) is a fixed integer, how many quadratics of the form \(x^2+bx+c\) factorise with integer coefficients? Here, \(b\) is allowed to be any integer.
  2. Further generalising question 1, if \(a\) and \(c\) are fixed integers, with \(a\) positive, how many quadratics of the form \(ax^2+bx+c\) factorise with integer coefficients? Again, \(b\) is allowed to be any integer.
  3. How can we generalise questions 2 and 3?

## Suggestion

1. What happens when you multiply out a pair of brackets?   Alternatively, if we knew the value of \(b\), how would we go about attempting to factorise the quadratic?  How might this help us to work out which values of \(b\) allow us to factorise the quadratic?

If you need a reminder of how to factorise quadratics where the \(x^2\) term has a coefficient other than \(1\), you may wish to look at the [Quadratic grids](https://undergroundmathematics.org/quadratics/quadratic-grids) resource.

## Solution

1. 1. We attempt to factorise the quadratic by finding two integers which multiply to \(10\) and add to \(b\). This is because if our quadratic factorises as \((x+r)(x+s)\), then expanding the brackets gives \[(x+r)(x+s)=x^2+(r+s)x+rs=x^2+bx+10,\] so we need \(r+s=b\) and \(rs=10\).  We therefore need to find two integers which multiply to \(10\), and there are four such pairs:      \(m\) and \(n\)   \(b\)     \(1\) and \(10\)   \(11\)     \(2\) and \(5\)   \(7\)     \(-1\) and \(-10\)   \(-11\)     \(-2\) and \(-5\)   \(-7\)     Therefore there are four possible values of \(b\).  (Why do we not also need to consider \(10\) and \(1\) the other way round, and \(5\) and \(2\) the other way round, and so on?)
  2. This is very similar; this time we are looking for pairs of numbers which multiply to \(30\), and there are eight of these: \(\pm1\) and \(\pm30\); \(\pm2\) and \(\pm15\); \(\pm3\) and \(\pm10\); \(\pm5\) and \(\pm6\). Thus there are eight possible values of \(b\).
  3. There are four pairs of numbers which multiply to \(-8\): \(\pm1\) and \(\mp8\) (this means the pair \(+1\) and \(-8\) and the pair \(-1\) and \(+8\)); \(\pm2\) and \(\mp4\). Thus there are four possible values of \(b\).
  4. Now there are five pairs of numbers which multiply to \(-16\): \(\pm1\) and \(\mp16\); \(\pm2\) and \(\mp8\); \(4\) and \(-4\). Thus there are five possible values of \(b\).  Note that the final pair gives \(b=0\), and the quadratic which results is \(x^2-16=(x+4)(x-4)\). This is an example of the difference of two squares.
  5. Thinking about how we factorise this expression (see [Quadratic grids](https://undergroundmathematics.org/quadratics/quadratic-grids) for more information on this), we realise that we are looking for two numbers which multiply to \(2\times6=12\) and add to \(b\).  There are six pairs of numbers which multiply to \(12\), and each pair has a different sum: \(\pm1\) and \(\pm12\); \(\pm2\) and \(\pm6\); \(\pm3\) and \(\pm4\). Therefore there are six possible values for \(b\).  Another way of approaching this is to note that the quadratic will factorise as \((px+r)(qx+s)\) with \(pq=2\) and \(rs=6\). Therefore we could have \(p=1\) and \(q=2\), and \(r=\pm1\), \(s=\pm6\) or \(r=\pm2\), \(s=\pm3\) or \(r=\pm3\), \(s=\pm2\) or \(r=\pm6\), \(s=\pm1\). This gives \(8\) solutions. (Why do we not need to consider \(p=2\), \(q=1\)? And why do we need both \(r=1\), \(s=6\) and \(r=6\), \(s=1\), for example?) But our other approach gave \(6\) solutions, so what’s going on here? And which is correct?
  6. This time we seek pairs of numbers which add to \(b\) and multiply to \(6\times -20=-120\). There are lots of these: \(\pm1\) and \(\mp120\); \(\pm2\) and \(\mp60\); \(\pm3\) and \(\mp40\); \(\pm4\) and \(\mp30\); \(\pm5\) and \(\mp24\); \(\pm6\) and \(\mp20\); \(\pm8\) and \(\mp15\); \(\pm10\) and \(\mp12\), so there are \(16\) pairs and so \(16\) possible values for \(b\).
2. This time, it is the constant which is allowed to vary: How many quadratics of the following forms factorise with integer coefficients, where \(c\) is a **positive** integer.
  1. We want two integers which add to \(6\) and multiply to \(c\). Since \(c\) has to be positive, the integers must either be both positive or both negative. But as they have to add to \(+6\), they must therefore both be positive. There are therefore only \(3\) possible pairs: \(1\) and \(5\) (so \(c=5\)); \(2\) and \(4\) (so \(c=8\)); \(3\) and \(3\) (so \(c=9\)).
  2. This time, the pair of integers have to multiply to \(c\) and add to \(-10\), so they must both be negative, giving the possible pairs \(-1\) and \(-9\); \(-2\) and \(-8\); \(-3\) and \(-7\); \(-4\) and \(-6\); \(-5\) and \(-5\), so there are \(5\) possibilities for \(c\).
  3. We now need two integers which add to \(5\) and multiply to \(3c\), so they must both be positive. Of the pairs which add to \(5\) (being \(1\) and \(4\); \(2\) and \(3\)), only \(2\times3=6\) gives a multiple of \(3\), so there is only one possible value for \(c\).
  4. This time, the integers add to \(-6\) and multiply to \(10c\); no pairs which add to \(-6\) multiply to give a positive multiple of \(10\), so there are no possible values for \(c\).
3. 1. Now we require two integers which add to \(6\) and multiply to the negative integer \(c\). There are infinitely many such pairs: \(-1\) and \(7\); \(-2\) and \(8\); \(-3\) and \(9\); …; in general \(-n\) and \(6+n\) for any positive integer \(n\). So there are infinitely many possible values for \(c\).
  2. The same happens here: \(-11\) and \(1\); \(-12\) and \(2\), and so on, so again there are infinitely many possible values for \(c\).
  3. This time, we require two numbers which add to \(5\) and multiply to \(3c\), a negative multiple of \(3\). We could have \(-1\) and \(6\); \(-4\) and \(9\); \(-7\) and \(12\); in general, \(3n\) and \(5-3n\) (where \(n\ge2\)); or we could have \(-3\) and \(8\); \(-6\) and \(11\); \(-9\) and \(14\); in general, \(-3n\) and \(5+3n\) (where \(n\ge1\)). Therefore there are infinitely many possible values for \(c\).
  4. Here, we need two integers which add to \(-6\) and multiply to a negative multiple of \(10\). \(-10\) and \(4\); \(-20\) and \(14\); \(-30\) and \(24\); … will do (in general \(-10n\) and \(10n-6\)), so there are infinitely many possible values for \(c\). (There is also another families of solutions, namely \(10\) and \(-16\); \(20\) and \(-26\); …)
4. 1. If we write \(x^2+bx+c=(x+r)(x+s)=x^2+(r+s)x+rs\), we find that we need \(c=rs\), and every different pair of numbers \(r\), \(s\) gives a different value of \(b=r+s\). (Swapping \(r\) and \(s\) doesn’t give a different value of \(b\), though.)  So the number of different possible values of \(b\) is the number of pairs \(r\) and \(s\) where \(rs=c\) and where we ignore the order of \(r\) and \(s\). (Note that \(r\) and/or \(s\) are allowed to be negative.)  A further challenge is to find some sort of formula for the number of such pairs; we will not pursue that here.
  2. As before, we think about how we factorise this expression (see [Quadratic grids](https://undergroundmathematics.org/quadratics/quadratic-grids) for more information on this). We see that we are looking for two numbers which multiply to \(ac\) and add to \(b\).  Each possible pair of numbers which multiplies to \(ac\) will give a different sum, and so the number of possible quadratics is the number of pairs of numbers which multiply to \(ac\).  As in (a), it would be nice to have some sort of formula for this number.
  3. We can generalise question 2 in the case that \(a=1\) by asking the following:  If \(b\) is a fixed integer, how many quadratics of the form \(x^2+bx+c\) factorise with integer coefficients? Here, \(c\) is allowed to be any positive integer.  Here is one approach to answering this:  If we again write \(x^2+bx+c=(x+r)(x+s)=x^2+(r+s)x+rs\), we find that we need \(b=r+s\), and every different pair of numbers \(r\), \(s\) gives a different value of \(c=rs\). (Swapping \(r\) and \(s\) doesn’t give a different value of \(b\), though.)  In addition, since \(c\) has to be positive, we require \(r\) and \(s\) to either both be positive or both be negative.  We’ll look at the case where \(b\) is positive. Then our pair \(r\), \(s\) can be \(1\), \(b-1\), or \(2\), \(b-2\), or …, or \(b-1\), \(1\). So there are \(b-1\) pairs. But the order doesn’t matter, and \(r=1\), \(s=b-1\) gives the same value of \(c\) as \(r=b-1\), \(s=1\), so we’ve counted each answer twice. So there are \((b-1)/2\) *different* pairs, and so this many possible values of \(c\).  Is this correct, though? What happens if \(b\) is odd? And what if \(b\) is even?   We’ll leave the case where \(b\) is negative for you to think about.   If we try generalising question 2 in the case that \(a\) is not necessarily \(1\), we can make our life a little simpler by assuming that \(a\) is positive.  Why are we allowed to do this? Consider \(3x^2+bx+c\) and \(-3x^2-bx-c\). They have almost the same factorisations, if any, since the second expression is just \(-1\) times the first one, so we can write \[-3x^2-bx-c=-1(3x^2+bx+c).\] Then if we can factorise \(3x^2+bx+c\), we get a factorisation of \(-3x^2-bx-c\). So if \(a\) is negative in a quadratic, we can just take out a factor of \(-1\) and answer the resulting question, with the “\(c\) positive” and “\(c\) negative” questions swapping.   So our generalised question will be:  If \(a\) and \(b\) are fixed integers, with \(a\) positive, how many quadratics of the form \(ax^2+bx+c\) factorise with integer coefficients? Here, \(c\) is allowed to be any positive integer.  This time, as in (b), we require two numbers which add to \(b\) and multiply to \(ac\). Since \(a\) and \(c\) are positive, \(ac\) is also positive, and so the two numbers which add to \(b\) must both be positive or both be negative. Since \(c\) can be any positive number, \(ac\) is any multiple of \(a\), and so we are looking for two numbers of the same sign which add to \(b\) and multiply to give a multiple of \(a\).  There doesn’t seem to be an obvious way of finding the exact number of such pairs, but we can at least say that there can only be finitely many of them, since they still have to add to \(b\).   Now let’s generalise question 3. First the case \(a=1\):  If \(b\) is a fixed integer, how many quadratics of the form \(x^2+bx+c\) factorise with integer coefficients? Here, \(c\) is allowed to be any negative integer.  Again, we write \(x^2+bx+c=(x+r)(x+s)=x^2+(r+s)x+rs\), and we need \(b=r+s\), with every different pair of numbers \(r\), \(s\) giving a different value of \(c=rs\). (Swapping \(r\) and \(s\) doesn’t give a different value of \(b\), though.)  This time, since \(c\) is negative, the two numbers which add to \(b\) must have different signs, and there are infinitely many possibilities. If \(b\) is positive, we can take \(r=b+1\), \(s=-1\), or \(r=b+2\), \(s=-2\), and so on (in general, \(r=b+n\), \(s=-n\), where \(n\) is a positive integer). If \(b\) is negative, the argument is similar: we can take \(r=1\), \(s=b-1\), or \(r=2\), \(s=b-2\), and so on (in general \(r=n\), \(s=b-n\), where \(n\) is a positive integer).  So there are infinitely many possibilities for \(c\).   And finally, question 3 in the case that \(a\) is positive:  If \(a\) and \(b\) are fixed integers, with \(a\) positive, how many quadratics of the form \(ax^2+bx+c\) factorise with integer coefficients? Here, \(c\) is allowed to be any negative integer.  As before in the generalisation of question 2, we require two numbers which add to \(b\) and multiply to \(ac\). But this time, since \(a\) is positive and \(c\) is negative, \(ac\) is negative. Since \(c\) is arbitrary (we can choose it), \(ac\) is any negative multiple of \(a\).  So we could take the two numbers to be \(ka\) and \(b-ka\) for any positive integer \(k\) where \(b-ka<0\). For all large enough \(k\), this will be the case. (How large does \(k\) have to be?) The product of the two numbers is \(ka(b-ka)<0\), which is clearly a negative multiple of \(a\), so we can take \(c=k(b-ka)\).  Therefore each such \(k\) gives a possible value for \(c\), and so there are infinitely many possible values of \(c\) in this case.  We may well not have found all possible values of \(c\) using this method. But we have shown that there are infinitely many of them. Finding a rule for all possible values of \(c\) seems as though it will be a lot harder in general, so we will stop here.
