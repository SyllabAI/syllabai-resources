---
created: 2026-10-23T02:04:16 (UTC +06:00)
source: https://undergroundmathematics.org/circles/finding-circles
author: Underground Mathematics (University of Cambridge)
rights: © University of Cambridge (Underground Mathematics). Use inside SyllabAI is authorised by the operator attestation of 2026-10-23 — see LICENSE-DATA.md (Amendment 2026-10-23) in this repository. 
  Takedown / correction handling as stated in LICENSE-DATA.md.
tags:
- underground-mathematics
- circles
- type/many-ways-problem
- level/developing
resource_identity:
  ugm_id: finding-circles
  station: circles
  station_title: Circles
  resource_type_id: 4
  resource_type_label: Many ways problem
  level: Developing
  ref: 6917
  old_site_id: G2_RT6_2
spec_map:
  curriculum_code: CIE-9709-P1-2023
  lane: cie-a-level-maths-20-pure-1
  board: Cambridge CIE
  syllabus_version: 2023-2025
  subsection: circles
  subsection_provenance:
    tier: PROVIDER
    signal: source-url-slug
    slug: circles
    validation_status: SUGGESTED
  spec_points:
  - code: 1.3.2
    provenance:
      tier: AI_SUGGESTED
      confidence: high
      model_version: GLM (Super Z agent, z.ai) — P3c lane-3 cross-map (cross-map-coordinate-geometry.json (P3c lane 3) @
        syllabai-experimental cb947595)
      evidence: 'How many points define a circle; equations from diameter ends and point sets — the folded circle statement as an investigation. Pattern exemplar.'
      rationale: 'Canonical UGM title: “Finding circles”'
      validation_status: SUGGESTED
    title: interpret and use any of the forms y = mx + c , y – y = m ( x – x ) , ax + by + c = 0 in solving
  mapped_date: '2026-10-23'
  mapper: cross-map-coordinate-geometry.json (P3c lane 3) @ syllabai-experimental cb947595
provenance:
  capture_date: '2026-10-22'
  capture_tool: P2 full-site crawl (ugm-crawl) → ugm-clean extraction; text-only import
  content_language: en
task: T-UGM-IMPORT-3
assets:
- path: https://undergroundmathematics.org/circles/finding-circles/download/teacher-notes.pdf
  kind: printable
---

# Finding circles

> Excerpt: This resource encourages students to consider how many points are required to define a circle. They will work with the graphical and algebraic representations of circles.

## Warm-up

The points \((3,8)\) and \((5,2)\) lie at the ends of a diameter of a circle. What is the equation of the circle?

**Some more points…**

In the previous question, two points were enough to specify a circle. But is that always the case? For each of the following three statements, is the answer ALWAYS, SOMETIMES or NEVER? Do justify your answers!

You might like to explore your ideas with [GeoGebra](https://www.geogebra.org/graphing).

1. If we specify two (distinct) points in the plane, there is a unique circle that passes through them.

---

1. If we specify three (distinct) points in the plane, there is a unique circle that passes through them.

---

1. If we specify four (distinct) points in the plane, there is a unique circle that passes through them.

Once you have answered these, you will be ready to move to the [main problem](https://undergroundmathematics.org/circles/finding-circles/main-problem).

## Warm-up solutions

The points \((3,8)\) and \((5,2)\) lie at the ends of a diameter of a circle. What is the equation of the circle?

The equation of a circle can always be written as \[(x-a)^2+(y-b)^2=r^2,\] where the centre is \((a,b)\) and the radius is \(r\). So if we can find the centre and the radius, we can just write down the equation.

The centre of the circle is the midpoint of a diameter, so the centre is at \((\frac{3+5}{2},\frac{8+2}{2})=(4,5)\).

The radius is the distance from the centre to any point on the circumference, so using Pythagoras, it is \[r=\sqrt{(4-3)^2+(5-8)^2}=\sqrt{1^2+(-3)^2}=\sqrt{10}.\] As a check, if we use the other point on the circumference, we get \[r=\sqrt{(4-5)^2+(5-2)^2}=\sqrt{(-1)^2+3^2}=\sqrt{10}.\]

Alternatively, we could find the (length of the) diameter and halve it to get the radius: the diameter is \[d=\sqrt{(3-5)^2+(8-2)^2}=\sqrt{(-2)^2+6^2}=\sqrt{40}=2\sqrt{10},\] so \(r=\sqrt{10}\).

Therefore the circle has equation \[(x-4)^2+(y-5)^2=10\] using the general formula \((x-a)^2+(y-b)^2=r^2\) for a circle with centre \((a,b)\) and radius \(r\).

In fact, we can save ourselves some effort by realising that we don’t need to take square roots in this problem: we only need \(r^2\) for the formula.

So we could have used Pythagoras to write \[r^2=(4-3)^2+(5-8)^2=1^2+(-3)^2=10\] instead, and then the circle’s equation is just \((x-4)^2+(y-5)^2=10\).

If you use this approach, you just have to be careful to remember that you already have \(r^2\) and that you don’t need to square it again. Writing \((x-4)^2+(y-5)^2=100\) would be unfortunate!

**Some more points…**

1. Never true: there are infinitely many circles passing through any two distinct points. All of their centres lie on a straight line, which is the perpendicular bisector of the line joining the two given points.

---

1. Sometimes true: If the three points lie on a straight line, then there is no circle through them. In all other cases, there is a unique circle through the three points.

---

1. Sometimes true: Three of the points (as long as they are not on a straight line) will have a unique circle through them. The fourth point might lie on that circle or might not. Points which all lie on a single circle are called *concyclic*. (You might also recall coming across cyclic quadrilaterals; a quadrilateral is cyclic if all of its vertices lie on the circumference of a circle.)

## Main problem

We now know that given three distinct points in the plane, there is (usually) a unique circle passing through them.

So if we are given three points, we would like to find the equation of the circle that passes through them. How many ways can you find to do this? There are suggestions available in the [“Suggestion” section](https://undergroundmathematics.org/circles/finding-circles/suggestion).

Here are some examples for you to try your ideas out on. For each set of three points, find the equation of the circle passing through them.

It is certainly worth sketching a graph to help you understand what is going on in each case!

Which of your approaches is the most effective?

1. \(A(3,2)\), \(B(3,6)\), \(C(5,8)\)

---

1. \(A(0,4)\), \(B(4,0)\), \(C(-6,0)\)

---

1. \(A(-1,-5)\), \(B(-2,2)\), \(C(2,-1)\)

---

1. \(A(3,3)\), \(B(1,-2)\), \(C(4,1)\)

If you want more practice, there is a [Mathmo](http://nrich.maths.org/mathmoApp/#/mathmo) exercise for this.

If we join the three points up to form a triangle, then the circle which passes through the three points – the three vertices of the triangle – is known as the *circumcircle* of the triangle. The centre of this circle is known as the *circumcentre* of the triangle.

## Suggestion

We now know that given three distinct points in the plane, there is (usually) a unique circle passing through them.

So if we are given three points, we would like to find the equation of the circle that passes through them. How many ways can you find to do this?

**An algebraic approach**

Might the general equation of a circle be of use here?

Further suggestion

We want to find an equation of the form \((x-a)^2 + (y-b)^2 = r^2\), where \((a,b)\) is the (unknown) centre of the circle and \(r\) is the (unknown) radius. We have \(3\) points that lie on the circle, so we can use these to get some simultaneous equations…

A slightly more geometric way to think about this approach is that we know that the centre, say \((a,b)\), is at an equal distance from all points. So we could write down the distances from \((a,b)\) to our known points, and then equate those…

**A geometric approach**

If we have two (distinct) points, then there are many circles that pass through both points. Can you say anything about the centres of these circles? Might that help us when we know a third point on the circle?

This GeoGebra applet might be helpful to explore this. The two points \(A\) and \(B\) (in red) are fixed, while the third point \(C\) (in blue) can be moved. The centre of the circle through these three points, labelled \(O\), can be seen, and leaves a trace as you move \(C\).

[Download GeoGebra file](https://www.geogebratube.org/material/download/format/file/id/vv9G8Fj9)

Can you explain the behaviour you have observed? And how can this help us to find the equation of the circle when we know a third point on the circumference?

Further suggestion

Let’s call the three given points \(A\), \(B\) and \(C\).

The centre of the circle must be the same distance from \(A\), \(B\) and \(C\). Those points which are the same distance from \(A\) and \(B\) lie on the …

What about those points which are the same distance from \(A\) and \(C\)?

Is that enough to find the centre?

## Main solutions

Here are some examples for you to try your ideas out on. For each set of three points, find the equation of the circle passing through them.

It is certainly worth sketching a graph to help you understand what is going on in each case!

Which of your approaches is the most effective?

1. \(A(3,2)\), \(B(3,6)\), \(C(5,8)\)

---

1. \(A(0,4)\), \(B(4,0)\), \(C(-6,0)\)

---

1. \(A(-1,-5)\), \(B(-2,2)\), \(C(2,-1)\)

---

1. \(A(3,3)\), \(B(1,-2)\), \(C(4,1)\)

**Brief answers**

1. \((x-7)^2+(y-4)^2=20\)

---

1. \((x+1)^2+(y+1)^2=26\)

---

1. \(\left(x+\frac{3}{2}\right)^2+\left(y+\frac{3}{2}\right)^2= \frac{25}{2}\)

---

1. \(\left(x-\frac{7}{6}\right)^2+\left(y-\frac{5}{6}\right)^2= \frac{145}{18}\)

**Full solutions**

1. \(A(3,2)\), \(B(3,6)\), \(C(5,8)\)

**A geometric approach**

In the suggestion, we saw that the centre of the circle must be the same distant from \(A\) and \(B\), and it turns out that those points which are lie on the *perpendicular bisector* of the line segment \(AB\).

Detailed justification of this

If we draw a diagram with a point \(P\) that is equidistant from \(A\) and \(B\), and mark on the midpoint \(M\) of \(AB\), we get the following:

The triangles

\(AMP\)

and

\(BMP\)

are congruent by side-side-side (SSS):

\[\begin{align*} AM&=BM&&\text{$M$ is midpoint of $AB$}\\ PA&=PB&&\text{$P$ is equidistant from $A$ and $B$ (given)}\\ MP&=MP&&\text{common side} \end{align*}\]

Therefore the angles \(\angle AMP\) and \(\angle BMP\) are equal. But together they form a straight line (\(180^\circ\)), so each angle is a right angle. Thus \(\angle AMP=90^\circ\) and the point \(P\) lies on the perpendicular bisector of \(AB\).

So if we draw the perpendicular bisector of \(AB\), the circle’s centre must lie on it.

Likewise, if we draw the perpendicular bisector of \(AC\) or of \(BC\), the circle’s centre must lie on that, too.

The point where these perpendicular bisectors meet must therefore be the centre of the circle through the points \(A\), \(B\) and \(C\).

This GeoGebra applet shows how this works for this question; you can move the points \(A\), \(B\) and \(C\) if you wish.

[Download GeoGebra file](https://www.geogebratube.org/material/download/format/file/id/tQP28g3x)

We can now see that the perpendicular bisector of \(AB\) is going to be the line \(y=4\) since \(A\) and \(B\) have the same \(x\)-coordinate.

The perpendicular bisector of the chord \(BC\) passes through the midpoint of \(BC\), which is \((4,7)\). (The midpoint of a line between two points can be found by averaging the coordinates of the two points: its coordinates are half way between the coordinates of \(B\) and \(C\).)

The gradient of line through the points \(B\) and \(C\) is \[m=\frac{8-6}{5-3}=\frac{2}{2}=1,\] so the gradient of the line perpendicular to that is \[m'=-\frac{1}{m}=-\frac{1}{1}=-1\] (the negative reciprocal of \(m\)).

The equation of this second perpendicular bisector is therefore

\[\begin{align*} &&y-7&=-(x-4)&&\quad \\ \implies&& y&=11-x. \end{align*}\]

We now need to find the point of intersection of these two lines as this is the centre of our circle. Solving the equations \(y=4\) and \(y=11-x\) simultaneously gives the coordinates of their intersection, which is \(O(7,4)\). Finally, we want the radius of our circle so we work out the length \(|OA|\): \[r=|OA|=\sqrt{(3-7)^2+(2-4)^2}=\sqrt{20}.\] Therefore the equation of the circle is \[(x-7)^2+(y-4)^2=20.\]

Incidentally, note that as the equation for the circle only needs \(r^2\) and not \(r\) itself, we could have found \(r^2=|OA|^2\) and dispensed with all square roots. We will do this from now on in this question.

**An algebraic approach**

Following the suggestion, we substitute for

\(x\)

and

\(y\)

in the equation

\((x-a)^2+(y-b)^2=r^2\)

for our three coordinates to find

\(a\)

,

\(b\)

and

\(r\)

. This gives us the following three

simultaneous equations

:

\[\begin{align} (3-a)^2+(2-b)^2&=r^2 \label{eq:1}\\ (3-a)^2+(6-b)^2&=r^2 \label{eq:2}\\ (5-a)^2+(8-b)^2&=r^2 \label{eq:3} \end{align}\]

In this form, they are not that easy to solve, so we expand the brackets:

\[\begin{align} \eqref{eq:1} \implies && a^2-6a+b^2-4b+13&=r^2&&\quad \label{eq:4}\\ \eqref{eq:2} \implies && a^2-6a+b^2-12b+45&=r^2 \label{eq:5}\\ \eqref{eq:3} \implies && a^2-10a+b^2-16b+89&=r^2 \label{eq:6} \end{align}\]

Now subtracting any pair of these eliminates all of the square terms, as follows:

\[\begin{align*} \eqref{eq:5}-\eqref{eq:4}& \implies -8b+32=0 \implies b=4\\ \eqref{eq:6}-\eqref{eq:5}& \implies -4a+44-4\times 4 \implies a=7 \end{align*}\]

Substituting our values for

\(a\)

and

\(b\)

into

\(\eqref{eq:1}\)

we find the value of

\(r^2\)

:

\[\begin{align*} r^2&=(3-7)^2+(2-4)^2 \\ &=16+4=20. \end{align*}\]

Therefore the equation of the circle is \[(x-7)^2+(y-4)^2=20.\]

*Which method is quicker/easier here?*

By virtue of the fact we can write down one of the perpendicular bisectors by inspection, probably the geometric method here.

1. \(A(0,4)\), \(B(4,0)\), \(C(-6,0)\)

**Geometric, perpendicular bisector method**

The midpoint of \(AB\) is \((2,2)\), so the perpendicular bisector passes through this point. The gradient of \(AB\) is \(-1\), so the perpendicular bisector has gradient \(-1/-1=1\) and thus the equation of the perpendicular bisector is \[y-2=1(x-2) \implies y=x,\] as is apparent from the sketch. Similarly, the perpendicular bisector of the chord \(BC\) is the line \(x=-1\). Thus the point of intersection, and the centre of the circle, is \(O(-1,-1)\). We work out the length \(|OA|\) to find the (square of the) radius: \[r^2 = |OA|^2 = (-1-0)^2+(-1-4)^2=26\] so the equation of our circle through the points \(A\), \(B\) and \(C\) is \[(x+1)^2+(y+1)^2=26.\]

**Algebraic, simultaneous equations method**

Substituting the coordinates

\(A\)

,

\(B\)

and

\(C\)

into the general equation for a circle and expanding the brackets as in part (a), we find

\[\begin{align} a^2+b^2-8b+16 &=r^2 \label{eq:7}\\ a^2-8a+b^2+16 &=r^2 \label{eq:8}\\ a^2+12a+b^2+36 &=r^2 \label{eq:9} \end{align}\]

Then subtracting the equations gives

\[\begin{align*} \eqref{eq:9}-\eqref{eq:8}& \implies& -20a+20&=0&\implies& a=-1\\ \eqref{eq:8}-\eqref{eq:7}& \implies& 8b+8&=0 &\implies& b=-1. \end{align*}\]

From equation \(\eqref{eq:7}\), we find that the radius of our circle is given by \[r^2=(-1)^2 + (-1)^2-8(-1)+16=26\] so the equation of the circle through \(A\), \(B\) and \(C\) is \[(x+1)^2+(y+1)^2=26.\]

*Which method is quicker/easier here?*

Again, probably the geometric method as the perpendicular bisectors weren’t algebraically fiddly to find.

1. \(A(-1,-5)\), \(B(-2,2)\), \(C(2,-1)\)

**Geometric, perpendicular bisector method**

The midpoint of \(AB\) is \(\left(-\dfrac{3}{2},-\dfrac{3}{2}\right)\) and the gradient of \(AB\) is \(\dfrac{-5-2}{-1-(-2)}=-7\). Thus the equation of the perpendicular bisector of \(AB\) is \[y-\left(-\frac{3}{2}\right)= \frac{1}{7}\left(x-\left(-\frac{3}{2}\right)\right)\] which we can rearrange to \[y=\frac{1}{7}x-\frac{9}{7}.\] Similarly, the midpoint of \(BC\) is \(\left(0,\dfrac{1}{2}\right)\) and its gradient is \(\dfrac{2-(-1)}{-2-2}=-\dfrac{3}{4}\). The equation of the second perpendicular bisector is therefore \[y-\frac{1}{2}=\frac{4}{3}x\] or \(y=\frac{4}{3}x+\frac{1}{2}\).

The two lines intersect when

\[\frac{1}{7}x-\frac{9}{7}=\frac{4}{3}x+\frac{1}{2}\]

which we can rearrange to get

\[\begin{align*} &&\left(\frac{28}{21}-\frac{3}{21}\right)x&=-\frac{9}{7}-\frac{1}{2}&&\quad\\ \implies&& \frac{25}{21}x&=-\frac{25}{14}\\ \implies&& x&=-\frac{3}{2}. \end{align*}\]

Substituting into the equation of the second perpendicular bisector (which has a simpler-looking equation), we find \[y=\frac{4}{3}\left(-\frac{3}{2}\right)+\frac{1}{2}=-\frac{3}{2}.\] Thus the centre of the circle is \(O\left(-\dfrac{3}{2},-\dfrac{3}{2}\right)\) and the radius is given by \[r^2=|OA|^2=\left(-1+\frac{3}{2}\right)^2+\left(-5+\frac{3}{2}\right)^2 =\frac{1}{4}+\frac{49}{4}=\frac{25}{2}.\] The final equation of the circle is therefore \[\left(x+\frac{3}{2}\right)^2+\left(y+\frac{3}{2}\right)^2=\frac{25}{2}.\]

**Algebraic, simultaneous equations method**

This time, our three simultaneous equations are:

\[\begin{align} a^2+2a+b^2+10b+26&=r^2 \label{eq:10}\\ a^2+4a+b^2-4b+8&=r^2 \label{eq:11}\\ a^2-4a+b^2+2b+5&=r^2 \label{eq:12} \end{align}\]

Then eliminating the squared terms, we find

\[\begin{align} \eqref{eq:11}-\eqref{eq:10}& \implies& 2a-14b-18&=0&&\quad \label{eq:13}\\ \eqref{eq:12}-\eqref{eq:11}& \implies& -8a+6b-3&=0. \label{eq:14} \end{align}\]

Eliminating \(a\): \[4\times\eqref{eq:13}+\eqref{eq:14} \implies -50b-75=0 \implies b=-\frac{3}{2}.\] Substitute this value for into equation \(\eqref{eq:14}\) to find \[-8a+6\times\left(-\frac{3}{2}\right)+3=0 \implies 8a=-12 \implies a=-\frac{3}{2}.\] (Alternatively, halving equation \(\eqref{eq:13}\) gives \(a-7b-9=0\), so \(a=7b+9=-\frac{3}{2}\).)

The radius is then given by \[r^2=\left(-1+\frac{3}{2}\right)^2+\left(-5+\frac{3}{2}\right)^2=\frac{1}{4}+\frac{49}{4}=\frac{25}{2}\] and the final equation of the circle is \[\left(x+\frac{3}{2}\right)^2+\left(y+\frac{3}{2}\right)^2=\frac{25}{2}.\]

Note that we can save ourselves a lot of effort by converting all fractions from mixed fractions like \(4\frac{1}{2}\) to \(\frac{9}{2}\) straightaway - this trick saves time when we are manipulating a lot of fractions.

*Which method is quicker/easier here?*

Tough call - which do you prefer?

It is interesting to notice that in the diagram for this part, the centre of the circle appears to lie on the chord \(AB\). Is this really the case?

Answer

If the centre does lie on \(AB\), then \(AB\) is a diameter, and therefore the angle \(\angle ACB\) would have to be a right angle, as angles in semicircles are right angles. And the converse is true, too: if \(\angle ACB\) is a right angle, then \(AB\) is a diameter. So we need only check whether \(AC\) and \(CB\) are perpendicular, and we can do this by calculating their gradients.

The gradient of \(AC\) is \(\dfrac{-1-(-5)}{2-(-1)}=\dfrac{4}{3}\), and we have already calculated that the gradient of \(CB\) is \(-\dfrac{3}{4}\). These multiply to \(-1\) and so they are perpendicular.

It follows that the centre of the circle is the midpoint of \(AB\), which is \((-\frac{3}{2},-\frac{3}{2})\), as we found earlier.

1. \(A(3,3)\), \(B(1,-2)\), \(C(4,1)\)

**Geometric, perpendicular bisector method**

The midpoint of \(AB\) is \(\left(2,\dfrac{1}{2}\right)\) and the gradient of \(AB\) is \(\dfrac{3-(-2)}{3-1}=\dfrac{5}{2}\). Thus the equation of the first perpendicular bisector is \[y-\frac{1}{2}=-\frac{2}{5}(x-2)\] which can be rearranged to give \(y=-\frac{2}{5}x+\frac{13}{10}.\)

Likewise, the midpoint of \(BC\) is \(\left(\dfrac{5}{2},-\dfrac{1}{2}\right)\) and its gradient is \(\dfrac{-2-1}{1-4}=1\). The equation of the second perpendicular bisector is therefore \[y+\frac{1}{2}=-1\left(x-\frac{5}{2}\right)\] which gives \(y=2-x\).

The two lines intersect when

\[\begin{align*} &&-\frac{2}{5}x+\frac{13}{10}&=2-x&&\quad\\ \implies&& \frac{3}{5}x&=\frac{7}{10}\\ \implies&& x&=\frac{7}{6}. \end{align*}\]

Substituting into the equation of the second perpendicular bisector we find

\[y=2-\frac{7}{6}=\frac{5}{6}.\]

Thus the centre of the circle is

\(O\left(\dfrac{7}{6},\dfrac{5}{6}\right)\)

and the radius is given by

\[\begin{align*} r^2=\vert OA \vert^2 &= \left(3-\frac{7}{6}\right)^2+\left(3-\frac{5}{6}\right)^2\\ &= \left(\frac{11}{6}\right)^2+\left(\frac{13}{6}\right)^2\\ &= \frac{121+169}{36}\\ &=\frac{145}{18}. \end{align*}\]

The final equation of the circle is therefore \[\left(x-\frac{7}{6}\right)^2+\left(y-\frac{5}{6}\right)^2= \frac{145}{18}.\]

**Algebraic, simultaneous equations method**

Our three simultaneous equations are:

\[\begin{align} a^2-6a+b^2-6b+18 &=r^2 \label{eq:15}\\ a^2-2a+b^2+4b+5 &=r^2 \label{eq:16}\\ a^2-8a+b^2-2b+17 &=r^2 \label{eq:17} \end{align}\]

Eliminating the squared terms gives

\[\begin{align} \eqref{eq:16}-\eqref{eq:15}& \implies& 4a+10b-13&=0&&\quad \label{eq:18}\\ \eqref{eq:17}-\eqref{eq:16}& \implies& -6a-6b+12&=0 \notag \\ \div (-6)& \implies& a+b-2&=0.\label{eq:19} \end{align}\]

Eliminating

\(a\)

:

\[\eqref{eq:18}-4\times\eqref{eq:19} \implies 6b-5=0 \implies b=\frac{5}{6}.\]

Substituting this value for

\(b\)

into equation

\(\eqref{eq:19}\)

gives

\[a+\frac{5}{6}-2=0 \implies a=\frac{7}{6}.\]

The radius is then given by

\[\begin{align*} r^2&= \left(3-\frac{7}{6}\right)^2+\left(3-\frac{5}{6}\right)^2\\ &= \left(\frac{11}{6}\right)^2+\left(\frac{13}{6}\right)^2\\ &= \frac{121+169}{36}\\ &=\frac{145}{18} \end{align*}\]

and thus the equation of the circle is \[\left(x-\frac{7}{6}\right)^2+\left(y-\frac{5}{6}\right)^2= \frac{145}{18}.\]

*Which method is quicker/easier here?*

Again, it’s a tough call - do you have a preference?
