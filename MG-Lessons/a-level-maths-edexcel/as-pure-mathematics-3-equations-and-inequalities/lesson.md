# as-pure-mathematics-3-equations-and-inequalities — lesson

_Lane: `a-level-maths-edexcel` · grade — · 7 content steps · 3 check questions (source: MathsGenie lessons)_

## The basic language

An equation says two expressions are equal, so you usually look for exact value or values that make both sides match. An inequality compares size using $<$, $>$, $\le$, or $\ge$, so the answer is often a range of values.

A solution is any value that makes the statement true. The solution set is the full collection of such values, and set notation writes this compactly as $\{x:x>3\}$, meaning all values of $x$ greater than 3.

## Solving linear inequalities safely

To solve a linear inequality, collect like terms and isolate the variable just as you would in a linear equation. The one extra rule is that if you multiply or divide both sides by a negative number, the inequality sign must reverse.

For example, solve $20-x < 4x+5$ by moving the constants first and then the $x$ terms. Because the final division is by positive 5, the sign stays the same.

$$$15-x < 4x$$
$$15 < 5x$$
$$x > 3$$

If you had $-2x > 6$, dividing by $-2$ would give $x < -3$. This sign change is one of the easiest exam slips to make, so always check the sign of the number you divide by.

## Quadratic inequalities and sign intervals

![Graph of the parabola y=(x+8)(x-2) crossing the x-axis at -8 and 2, with positive sign outside the roots and negative sign between them](../assets/001-76412970-4a59-47d8-b10a-4486c8629b7e.jpeg)

For a quadratic inequality, first rearrange so one side is zero. The roots of the matching quadratic equation are the boundary values that split the number line into intervals.

If the coefficient of $x^2$ is positive, the parabola opens upwards, so the quadratic is positive outside the roots and negative between them. If the coefficient is negative, that pattern reverses.

If you are unsure which interval to choose, test an easy value such as $x=0$. A quick sign check confirms whether you want the middle interval or the outside intervals.

## Worked example with a quadratic inequality

Start by comparing the quadratic with zero, then factorise. For $x^2+6x>16$, this gives

$$$x^2+6x-16>0$$
$$(x+8)(x-2)>0$$

The roots are $x=-8$ and $x=2$, so these values split the number line into three intervals. Because the quadratic opens upwards, it is greater than zero outside the roots.

$$$\{x:x<-8 \text{ or } x>2\}$$

For a non-strict inequality, include the boundary values if equality is allowed. So $x(x+2)\le15$ becomes $(x+5)(x-3)\le0$, giving $-5\le x\le3$.

## Combining inequalities

When two inequalities must both be true, solve them separately first. Then keep only the overlap, not every value from either set.

For $x^2+3x-18<0$, factorising gives $(x+6)(x-3)<0$, so $-6<x<3$. For $15+3x\le17+x$, rearranging gives $2x\le2$, so $x\le1$.

The shared solution is the part common to both results. So the final answer is $$\lbrace x:-6<x\le1 \rbrace$$

## Simultaneous equations as intersections

![Coordinate graph showing the parabola y=x^2-4x+6 and the line y=6-x crossing at the points (0,6) and (3,3)](../assets/002-63cc0952-a00b-4606-838f-ee4d3d607246.jpeg)

A simultaneous solution must satisfy both equations at the same time. On a graph, that means the coordinates of the intersection points.

For the curve $y=x^2-4x+6$ and the line $x+y=6$, first rearrange the line to $y=6-x$ and substitute into the curve equation. This gives:

$$$6-x=x^2-4x+6$$
$$x^2-3x=0$$
$$x(x-3)=0$$

So $x=0$ or $x=3$. Substituting these values into $y=6-x$ gives the intersection points $(0,6)$ and $(3,3)$.

## Using the discriminant

After substitution, a line and a curve often lead to a quadratic equation in one variable. The discriminant $b^2-4ac$ tells you how many real intersections there are: positive gives two, zero gives one repeated point, and negative gives none.

For $y=px^2-2px-2p$ and $y=x-3$, substitution gives $$px^2-(2p+1)x+(3-2p)=0$$

No real intersections means the discriminant is negative, so $$(2p+1)^2-4p(3-2p)<0$$

Simplifying gives $12p^2-8p+1<0$, which factorises to $(6p-1)(2p-1)<0$. Because this quadratic in $p$ opens upwards, it is negative between the roots, so $\frac{1}{6}<p<\frac{1}{2}$.

## Check yourself

1. What does the set notation $\{x:x>3\}$ mean?

   - The set of all values of $x$ greater than 3 ✔

   - Only the value $x=3$

   - The set of all values of $x$ less than 3

   - No values of $x$

   _Explanation:_ A is correct because the colon means "such that", so the set contains every value satisfying $x>3$. B is the most common wrong answer because students confuse the boundary with the whole solution set.

2. Solve $x(x+2)\le15$.

   - $$-5\le x\le3$ ✔

   - $$x\le-5$ or $x\ge3$

   - $$-3\le x\le5$

   - $$x<-5$ or $x>3$

   _Explanation:_ Hint: Move everything to one side before deciding which interval works. Rearranging the expression gives $x^2+2x-15\le0$, which factors to $(x+5)(x-3)\le0$. This quadratic is negative or zero between the roots $-5$ and $3$, including the roots themselves. B is a common wrong answer because it describes the region where the upward-opening parabola is positive, rather than less than or equal to zero.

3. For the line $y=x-3$ and the curve $y=px^2-2px-2p$, which values of $p$ give no real intersections?

   - $$p<\frac{1}{6}$ or $p>\frac{1}{2}$

   - $$\frac{1}{6}<p<\frac{1}{2}$ ✔

   - $$p=\frac{1}{6}$ or $p=\frac{1}{2}$

   - All real values of $p$

   _Explanation:_ B is correct because no real intersections means the discriminant is less than zero, which simplifies to $(6p-1)(2p-1)<0$ and therefore values between the roots. A is the most common wrong answer because students remember that an upward quadratic is positive outside the roots, but here we need the quadratic in $p$ to be negative.
