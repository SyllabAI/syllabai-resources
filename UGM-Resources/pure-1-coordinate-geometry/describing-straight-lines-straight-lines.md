---
created: 2026-10-23T02:04:16 (UTC +06:00)
source: https://undergroundmathematics.org/geometry-of-equations/describing-straight-lines
author: Underground Mathematics (University of Cambridge)
rights: © University of Cambridge (Underground Mathematics). Use inside SyllabAI is authorised by the operator attestation of 2026-10-23 — see LICENSE-DATA.md (Amendment 2026-10-23) in this repository. 
  Takedown / correction handling as stated in LICENSE-DATA.md.
tags:
- underground-mathematics
- geometry-of-equations
- type/building-blocks
- level/introducing
resource_identity:
  ugm_id: describing-straight-lines
  station: geometry-of-equations
  station_title: Geometry of Equations
  resource_type_id: 1
  resource_type_label: Building blocks
  level: Introducing
  ref: 5341
  old_site_id: G2_RT2_1
spec_map:
  curriculum_code: CIE-9709-P1-2023
  lane: cie-a-level-maths-20-pure-1
  board: Cambridge CIE
  syllabus_version: 2023-2025
  subsection: geometry-of-equations
  subsection_provenance:
    tier: PROVIDER
    signal: source-url-slug
    slug: geometry-of-equations
    validation_status: SUGGESTED
  spec_points:
  - code: 1.3.2
    provenance:
      tier: AI_SUGGESTED
      confidence: high
      model_version: GLM (Super Z agent, z.ai) — P3c lane-3 cross-map (cross-map-coordinate-geometry.json (P3c lane 3) @
        syllabai-experimental cb947595)
      evidence: 'y=mx+c, y-y1=m(x-x1), ax+by+c=0, x=k, point+gradient, two points; degenerate cases (y^2=x^2, xy=1, repeated line) sharpen the graph-equation reading. Card-sort '
      rationale: 'Canonical UGM title: “Straight lines”'
      validation_status: SUGGESTED
    title: interpret and use any of the forms y = mx + c , y – y = m ( x – x ) , ax + by + c = 0 in solving
  - code: 1.3.1
    provenance:
      tier: AI_SUGGESTED
      confidence: high
      model_version: GLM (Super Z agent, z.ai) — P3c lane-3 cross-map (cross-map-coordinate-geometry.json (P3c lane 3) @
        syllabai-experimental cb947595)
      evidence: 'y=mx+c, y-y1=m(x-x1), ax+by+c=0, x=k, point+gradient, two points; degenerate cases (y^2=x^2, xy=1, repeated line) sharpen the graph-equation reading. Card-sort '
      rationale: 'Canonical UGM title: “Straight lines”'
      validation_status: SUGGESTED
    title: find the equation of a straight line given e.g. given two points, or one point and the gradient. sufficient information
  mapped_date: '2026-10-23'
  mapper: cross-map-coordinate-geometry.json (P3c lane 3) @ syllabai-experimental cb947595
provenance:
  capture_date: '2026-10-22'
  capture_tool: P2 full-site crawl (ugm-crawl) → ugm-clean extraction; text-only import
  content_language: en
task: T-UGM-IMPORT-3
assets:
- path: https://undergroundmathematics.org/geometry-of-equations/describing-straight-lines/download/teacher-notes.pdf
  kind: printable
---

# Straight lines

> Excerpt: Students are given a list of equations and geometrical conditions and are asked to decide which ones describe a straight line.

## Problem

1. Which of the following describe or determine a single straight line? \(4x - 2y = 6\) \(y = 2\) The points \((1,2)\) and \((0,-1)\) \(y = \frac{3}{2}x\) The points \((-1, -4)\), \((3, 7)\), and \((8, 8)\) \(y = 3 - 2x\) The point \((0,-1)\) and the constant gradient \(3\) \(x=-2\) \(y = x^2 + 2\) \(x = 7y + 5\) \(y - 8 = 3(x - 3)\) The points \(\left(\frac{1}{2},2\right)\), \((1,1)\), and \(\left(\frac{3}{2}, 0\right)\) \(y^2 = x^2\) The point \((3,3)\) and the direction specified by the vector \(\big( \begin{smallmatrix}1\\2\end{smallmatrix}\big)\) \(\frac{1}{3}y - x + \frac{1}{3} = 0\) \(xy = 1\) \(y^2 - 4xy + 4x^2 = 0\) How did you decide? You might find it helpful to try sketching some of these. You could use graphing software such as [Desmos](http://www.desmos.com/calculator/).

1. Which of the descriptions in question 1 represent the same straight line?

---

1. What ways of describing straight lines have been used in question 1? Can you give any other ways to describe a unique straight line?

---

1. Now consider the equation \(y=4x+1\), which describes a straight line. Use some of the ways of describing straight lines you have identified to give alternative descriptions of this straight line.

---

1. Why might one description be more useful than another? Can you identify any advantages or disadvantages of any of these representations?

## Solution

1. There are many ways of tackling this problem. Here is just one of those ways. The equation of a straight line can (usually) be written as \(y=mx+c\), where \(m\) is the gradient and \(c\) is the \(y\)-intercept. Therefore, any equation involving \(x\) and \(y\) which can be rearranged into that form describes a straight line. The equation \(4x-2y=6\) can be rearranged to give \(y=2x-3\), so it describes a unique straight line. We note that \(y=2\) is of the form \(y=mx+c\) with \(m=0\) and \(c=2\), so it also describes a straight line. The idea here is that for any two (distinct) points there is always a unique straight line going through both points. Can you see why this should be the case? The straight line going through the two points \((1,2)\) and \((0,-1)\) must have gradient \[m = \frac{2-(-1)}{1-0}=3.\] By substituting \(x=0\) and \(y=-1\) into \(y=3x+c\) we obtain \(c=-1\). Hence, the unique straight line passing through \((1,2)\) and \((0,-1)\) has equation \(y=3x-1\). You might also have spotted a quicker way in this case: since the line passes through \((0,-1)\), this tells us that the \(y\)-intercept is \(-1\), so \(c=-1\). An alternative way to find the equation is to substitute the coordinates of *both* pairs of points into the equation \(y=mx+c\) to get a pair of simultaneous equations: \[\begin{align*} 2 &= m\times 1 + c\\ -1 &= m\times 0 + c \end{align*}\] These simplify to give \[\begin{align*} 2 &= m + c\\ -1 &= c \end{align*}\] so \(c=-1\) and \(m=3\), giving \(y=3x-1\) as before. This might seem a little bit strange in this case; the effectiveness of this technique in more difficult cases is explored in [this exposition](https://undergroundmathematics.org/geometry-of-equations/the-equation-of-a-straight-line). The equation \(y=\frac{3}{2}x\) is of the form \(y=mx+c\) with \(c=0\) and so describes a straight line which passes through the origin. As we said in part c, for any two distinct points there is a unique straight line passing through both points. Therefore, three points will describe a straight line only if the third point lies on the straight line passing through the first two points. The equation of the straight line through \((-1,-4)\) and \((3,7)\) is \(y=\frac{11}{4}x - \frac{5}{4}\). However, \(x=y=8\) does not satisfy this equation. Thus, the three points do not lie on the same straight line. In fact, the three points given describe three different straight lines: the one through \((-1,-4)\) and \((3,7)\), the one through \((-1,-4)\) and \((8,8)\), and the one through \((3,7)\) and \((8,8)\). Another way of working out that these three points do not lie on the same straight line is to work out the gradient of the lines between two pairs: if they are equal, then we have a straight line, but if not, we do not. In this case, the gradient of the line between \((-1,-4)\) and \((3,7)\) is \(\frac{11}{4}\), whereas that between \((3,7)\) and \((8,8)\) is \(\frac{1}{5}\), which is clearly different. This also describes a straight line as it is in the form \(y=mx+c\) with \(m=-2\) and \(c=3\). A straight line has a constant gradient. In this case it is \(3\), and the intersection with the \(y\)-axis is at \(-1\), so this describes the straight line \(y=3x-1\). This is a vertical straight line through the point \((-2,0)\), parallel to the \(y\)-axis. This type of straight line is the only one which cannot be written in the form \(y=mx+c\). You might argue that \(y=x^2+2\) is the equation of a parabola and so it cannot describe a straight line. But are you really convinced by this? Or could you really convince someone who is sceptical? We’ll give an argument that *proves* it cannot be a straight line. The parabola described by \(y=x^2+2\) passes through the points \((-1,3)\), \((0,2)\) and \((1,3)\). However, whereas the first and third points lie on the straight line with equation \(y=3\) the second one does not. So, the equation \(y=x^2+2\) cannot describe a straight line. This can be rearranged to give \(y=\frac{1}{7}x - \frac{5}{7}\), so it describes a straight line. This can be rearranged to give \(y=3x - 1\) and so it also describes a straight line. We repeat what we did in part e, but this time all three points lie on the straight line with equation \(y=3 - 2x\). The obvious thing to do is to take the square root of both sides, to get the equation \(y=x\). So this describes a straight line. Or does it? Answer When we take square roots of equations, we must always remember that there are **two** possible square roots: a positive one and a negative one. So actually, we can take square roots to get \[y=\pm x,\] so there are actually **two** straight lines here: \(y=x\) and \(y=-x\). Another way to go about doing this is to rewrite the original equation as \(y^2-x^2=0\). The left hand side is a difference of two squares, so we can factorise it to get \((y+x)(y-x)=0\). So either \(y+x=0\) or \(y-x=0\), which are the two straight lines \(y=-x\) and \(y=x\). If this seems strange, remember that the graph of an equation is all those points whose coordinates satisfy the equation. In this case, points such as \((1,1)\), \((1,-1)\), \((-1,1)\) and \((-1,-1)\) all work in the equation \(y^2=x^2\), so we get *both* lines. The point \((3,3)\) and the direction specified by the vector \(\binom{1}{2}\) An alternative way to describe a straight line is using vectors: by specifying a fixed point and a direction vector we are uniquely describing the straight line that passes through the given fixed point in the direction of the vector. The vector given says “go \(1\) in the \(x\)-direction and \(2\) in the \(y\)-direction, so the gradient must be \(m=2/1=2\). Then the equation of the straight line described by the point and the direction vector given must be \(y=2x+c\); substituting \(x=y=3\) into this then gives \(c=3\), so \(y=2x+3\). This can be rearranged to give \(y=3x-1\), so this is a straight line. We can rearrange this to get \(y=\frac{1}{x}\). You may remember the shape of this graph; if not, you should have a go at drawing it! To *prove* that it is not a straight line, we can use the same approach as in part i. We pick three points that satisfy \(xy = 1\) and discover that they do not lie on the same straight line (for example, \((1,1)\), \(\left(2,\frac{1}{2}\right)\), \(\left(\frac{1}{2},2\right)\)), showing that \(xy = 1\) is not a straight line. This is tricky. We have a quadratic equal to zero, so what might be a sensible thing to do to it? Answer We can attempt to factorise the quadratic. In this case, we can do so (with some thinking) to get \(y^2-4xy+4x^2=(y-2x)^2\), so the equation given becomes \[(y-2x)^2=0,\] so we must have \(y-2x=0\), and so we do indeed have a straight line—the straight line with equation \(y=2x\). A key observation about the equations is that if a polynomial equation involving \(x\) and \(y\) only has linear terms, meaning that no \(x^2\) or \(y^2\) or \(xy\) or higher power appears, then the equation represents a straight line. (The converse is not true: part q shows that straight lines can sometimes be written in other ways.) The two forms \(y=mx+c\) and \(ax+by+c=0\) are very useful, because they allow us to quickly and easily compare lines, as we will explore further in [The equation of a straight line](https://undergroundmathematics.org/geometry-of-equations/the-equation-of-a-straight-line).

---

1. Do any of the descriptions in question 1 represent the same straight line? In question 1, we rearranged all the equations that described a straight line into the form \(y=mx+c\). This now makes it a lot easier to decide which equations describe the same straight line. Going back to our results from question 1, we see that parts a and n both describe \(y=2x-3\), parts c, g, k and o describe \(y=3x-1\) and parts f and l describe \(y=3-2x\). In each case, the different parts offer different descriptions of the same straight line.

---

1. In question 1, we encountered several different descriptions of a straight line. The equation \(y=mx+c\) describes a straight line for any numbers \(m\) and \(c\). This equation can also be rearranged in lots of ways. The equation \(x=c\) describes a vertical straight line for any real number \(c\). Putting these two together, it turns out that we can rearrange the equation of *any* straight line in the \(x\)-\(y\) plane into the form \(ax+by=c\) for some numbers \(a\), \(b\) and \(c\), including those which are vertical and horizontal. A straight line can be described uniquely by specifying two distinct points through which the line passes. A straight line can be specified by giving its gradient and one point through which it passes. Alternatively, one point and a direction vector also describes a straight line as in part 1(n). There are other ways to describe a unique straight line. For instance, we could consider the locus of all points equidistant from two given points. You may know that this also gives a straight line. Are there still further ways?

---

1. Now consider the equation \(y=4x+1\), which describes a straight line. Use some of the ways of describing straight lines you have identified to give alternative descriptions of this straight line. We can easily rearrange this into the form \(ax+by=c\): we get \(4x-y=-1\). We can also easily find two points on the line: just pick two distinct values for \(x\) and compute the corresponding \(y\)-values, for example \((0,1)\) and \((1,5)\). Following question 1(g), we can describe the line by giving its gradient (which is \(4\)) and some point it passes through, for example \((2,9)\). To give the vector formulation, we can turn the gradient \(4\) into the vector \(\binom{1}{4}\) (why?) and then give a point on the line such as \((-1,-3)\). It’s a bit harder to describe this line as the locus of points equidistant from two specified points—can you see how to do this?

---

1. Whether one of the above descriptions is more useful than another always depends on the context you are working in. For instance, as remarked earlier, one disadvantage of the description \(y=mx+c\) is that it does not include straight lines parallel to the \(y\)-axis. On the other hand, contrary to the description by the equation \(ax+by=c\) or by just specifying two points, you can easily read off the gradient and the \(y\)-intercept of the corresponding straight line from \(y=mx+c\).
