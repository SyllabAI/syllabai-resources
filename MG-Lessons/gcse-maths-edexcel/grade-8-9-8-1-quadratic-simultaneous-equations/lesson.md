# grade-8-9-8-1-quadratic-simultaneous-equations — lesson

_Lane: `gcse-maths-edexcel` · grade 8 · 5 content steps · 3 check questions (source: MathsGenie lessons)_

## What are quadratic simultaneous equations?

![Graph of the circle $x^2 + y^2 = 25$ and the line $y = 5 - 3x$ with intersections labelled at $(0,5)$ and $(3,-4)$.](../assets/001-c50b66a0-8349-4fc5-a018-bb6d25dc6499.jpeg)

Quadratic simultaneous equations combine a quadratic equation with another equation, often a line. A solution is an ordered pair $(x, y)$ that makes both equations true at the same time.

On a graph, the solution pairs are the intersection points of the two graphs. That is why there can be $0$, $1$, or $2$ real solutions.

A linear equation such as $3x + y = 5$ has variables only to the first power, so it draws as a straight line. A quadratic equation such as $x^2 + y^2 = 25$ contains a squared term, so its graph is curved.

## Substitution turns two equations into one

Use the linear equation to replace one variable in the quadratic equation. If the line is already written as $x = \dots$ or $y = \dots$, you can substitute straight away.

For $x^2 + y^2 = 25$ and $x = y - 1$, replace every $x$ with $y - 1$. Because the whole expression is being substituted, write brackets to show the substitution:
$$
(y - 1)^2 + y^2 = 25
$$

Expand and collect terms until you have standard form $ax^2 + bx + c = 0$. Here the first stage is to expand the brackets and collect like terms:
$$
y^2 - 2y + 1 + y^2 = 25
$$

Finally, set the expression to zero and divide through by any common factors to simplify. The resulting standard quadratic equations are:
$$
2y^2 - 2y - 24 = 0
$$
$$
y^2 - y - 12 = 0
$$

## Finish the example and pair the answers

Now solve the one-variable quadratic. Factorising the resulting equation gives the following expression:

$$$ (y - 4)(y + 3) = 0 $$

This yields $y = 4$ or $y = -3$. Substitute each value back into the equation $x = y - 1$. If $y = 4$, then $x = 3$; if $y = -3$, then $x = -4$.

So the solutions are $(3, 4)$ and $(-4, -3)$. Always write coordinate pairs, because separate lists of $x$-values and $y$-values do not show the correct matching.

## Worked example: rearrange the line first

Sometimes the line is not ready to substitute. For $x^2 + y^2 = 25$ and $3x + y = 5$, first make $y$ the subject: $$y = 5 - 3x$$

Substitute into the quadratic and simplify carefully. Collect like terms after expanding the square: $$x^2 + (5 - 3x)^2 = 25$$ $$x^2 + 25 - 30x + 9x^2 = 25$$

$$$10x^2 - 30x = 0$$ Factorise to get $$10x(x - 3) = 0$$ so $x = 0$ or $x = 3$. Then $y = 5 - 3x$ gives $y = 5$ or $y = -4$, so the solutions are $(0, 5)$ and $(3, -4)$.

## When factorising is awkward

If the quadratic does not factorise nicely, use the quadratic formula:
$$
x = \frac{-b \pm \sqrt{b^2 - 4ac}}{2a}
$$
This is often necessary when solving simultaneous equations where substitution leads to complex coefficients.

For $x^2 + y^2 = 18$ and $2x + y = 4$, first rearrange the linear equation to $y = 4 - 2x$. Then substitute this into the quadratic to produce a single equation in $x$:
$$
x^2 + (4 - 2x)^2 = 18
$$

Expand the quadratic and collect terms to reach the standard form $ax^2 + bx + c = 0$:
$$
x^2 + 16 - 16x + 4x^2 = 18
$$
$$
5x^2 - 16x - 2 = 0
$$

Using the formula gives $x = \frac{16 \pm \sqrt{296}}{10}$, so $x \approx 3.320$ or $x \approx -0.120$. Using the unrounded values in $y = 4 - 2x$ gives the solutions $(3.32, -2.64)$ and $(-0.120, 4.24)$. Remember to keep full calculator values until the final line.

## Check yourself

1. Which ordered pair is a solution of both $x^2 + y^2 = 25$ and $y = 5 - 3x$?

   - $$(0, 5)$ ✔

   - $$(5, 0)$

   - $$(3, 4)$

   - $$(-4, 3)$

   _Explanation:_ $$(0, 5)$ works because $0^2 + 5^2 = 25$ and $5 = 5 - 3 \times 0$. The common wrong choice is $(3, 4)$ because it lies on the circle, but it does not satisfy the line since $5 - 3 \times 3 = -4$.

2. If $y = 5 - 3x$, which substitution into $x^2 + y^2 = 25$ is correct?

   - $$x^2 + (5 - 3x)^2 = 25$ ✔

   - $$x^2 + 5 - 3x^2 = 25$

   - $$(x^2 + 5 - 3x)^2 = 25$

   - $$x^2 + (5 - 3x) = 25$

   _Explanation:_ You replace $y$ with the whole expression $5 - 3x$, so the square must be written as $(5 - 3x)^2$. The common wrong choice is $x^2 + 5 - 3x^2 = 25$, which incorrectly squares only part of the expression.

3. Stretch: After substituting $x = 5 - 2y$ into $x^2 - 2y^2 = 7$, which quadratic in $y$ is correct?

   - $$y^2 - 10y + 9 = 0$ ✔

   - $$y^2 - 10y - 9 = 0$

   - $$y^2 - 20y + 18 = 0$

   - $$2y^2 - 20y + 9 = 0$

   _Explanation:_ Expanding gives $25 - 20y + 4y^2 - 2y^2 = 7$, so $2y^2 - 20y + 18 = 0$, and dividing by $2$ gives $y^2 - 10y + 9 = 0$. The common wrong choice is $y^2 - 10y - 9 = 0$, which comes from moving the $7$ across with the wrong sign. Hint: Expand $(5 - 2y)^2$ before collecting like terms.
