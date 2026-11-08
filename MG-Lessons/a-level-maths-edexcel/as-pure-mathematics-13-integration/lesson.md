# as-pure-mathematics-13-integration — lesson

_Lane: `a-level-maths-edexcel` · grade — · 6 content steps · 4 check questions (source: MathsGenie lessons)_

## Integration as reverse differentiation

Integration works backwards from a gradient function to a function itself. If $F'(x)=f(x)$, then $F(x)$ is an antiderivative of $f(x)$ and $\int f(x)\,dx$ means integrate with respect to $x$.

For powers of $x$, add 1 to the power and divide by the new power. This is known as the reverse power rule:

$$$\int ax^n\,dx=\frac{a}{n+1}x^{n+1}+C,\qquad n\neq -1$$

The $+C$ is the constant of integration, because differentiating any constant gives 0. A quick check is to differentiate your answer and see if you recover the original integrand.

## Worked example with a polynomial

For a polynomial, integrate each term separately. Constants integrate to a multiple of $x$, so $\int -9\,dx=-9x$.

Here are the four terms integrated one by one. Doing them separately makes the structure clear.

$$\int 4x^3\,dx=x^4,\qquad \int -6x^2\,dx=-2x^3$$

$$\int 5x\,dx=\frac{5}{2}x^2,\qquad \int -9\,dx=-9x$$

So the full antiderivative is

$$\int \left(4x^3-6x^2+5x-9\right)\,dx=x^4-2x^3+\frac{5}{2}x^2-9x+C$$

Differentiating this answer gives back the original expression, which is a quick self-check.

## Expand brackets and rewrite powers first

The reverse power rule works best on a sum of powers of $x$. If brackets are multiplied, expand first: $(x+5)(x-2)=x^2+3x-10$.

$$$
\int (x+5)(x-2)\,dx=\int \left(x^2+3x-10\right)\,dx=\frac{1}{3}x^3+\frac{3}{2}x^2-10x+C
$$

Roots and reciprocal powers should also be rewritten before integrating. For example, $\sqrt{x}=x^{\frac{1}{2}}$, $\frac{1}{x^2}=x^{-2}$, and $\frac{1}{\sqrt{x}}=x^{-\frac{1}{2}}$.

After rewriting, apply the same rule as before. For example,
$$
\int \left(6\sqrt{x}+\frac{4}{x^2}+3\right)\,dx=4x^{\frac{3}{2}}-\frac{4}{x}+3x+C
$$
Be careful with $x^{-1}$, because the reverse power rule would divide by 0.

## Using a point to find the constant

If you know a point on the curve, first integrate to get the whole family of curves. Then substitute the coordinates of the point to find the single correct value of $C$.

Given that $\frac{dy}{dx}=6x^2-4x+7$ and the curve passes through $(1,10)$, first integrate the derivative. This gives
$$y=2x^3-2x^2+7x+C$$

Now substitute $x=1$ and $y=10$ to find the constant. This gives
$$10=2(1)^3-2(1)^2+7(1)+C=7+C,\qquad C=3$$

So the curve is
$$y=2x^3-2x^2+7x+3$$
Always include $+C$ before using the point, or you cannot determine the correct curve.

## Definite integrals and area under a curve

![Area under a curve y = f(x) between x = a and x = b with the region shaded](../assets/001-733ee454-defe-464a-a30d-7903c1012c74.jpeg)
A definite integral has limits, so it gives a number rather than a family of functions. If the curve stays above the $x$-axis, $\int_a^b f(x)\,dx$ represents the area under $y=f(x)$ from $x=a$ to $x=b$.

Example: evaluate $\int_1^4 \left(6+\frac{2}{\sqrt{x}}\right)\,dx$. First rewrite the fraction as a power:
$$6+\frac{2}{\sqrt{x}}=6+2x^{-\frac{1}{2}}$$
Now find an antiderivative. This gives:
$$\int \left(6+2x^{-\frac{1}{2}}\right)\,dx=6x+4x^{\frac{1}{2}}$$

Finally apply upper minus lower.
$$\left[6x+4x^{\frac{1}{2}}\right]_1^4=(24+8)-(6+4)=22$$
No $+C$ is needed once limits are attached, because constants cancel.

## Area between two curves

![Parabola y = 6x - x^2 and line y = 2x with the enclosed region shaded between their intersections](../assets/002-7fe6df3f-906d-485b-b6e7-09dc39a5c351.jpeg)

To find the area between two curves, first determine where they meet because those points give the limits of integration. You should subtract the bottom curve from the top curve so the resulting area is positive.

For the functions $y=6x-x^2$ and $y=2x$, set them equal to each other to find the intersection points. This gives the following quadratic equation:

$$
6x-x^2=2x \Rightarrow -x^2+4x=0 \Rightarrow x(4-x)=0
$$

Consequently, the curves meet at $x=0$ and $x=4$, corresponding to the points $(0,0)$ and $(4,8)$.

At a test point like $x=2$, the parabola gives $y=8$ while the line gives $y=4$, confirming that $y=6x-x^2$ is on top. The area calculation is set up as the integral of the difference between the curves:

$$
\text{Area}=\int_0^4 \left((6x-x^2)-2x\right)\,dx=\int_0^4 \left(4x-x^2\right)\,dx
$$

Evaluating the definite integral at the boundaries $x=0$ and $x=4$ provides the final value for the shaded region. The calculation is performed as follows:

$$
\left[2x^2-\frac{1}{3}x^3\right]_0^4=\left(32-\frac{64}{3}\right)-0=\frac{32}{3}
$$

## Check yourself

1. Which statement is correct?

   - $$\int 5x^4\,dx = x^5 + C$ ✔

   - $$\int 5x^4\,dx = 5x^5 + C$

   - $$\int 5x^4\,dx = x^4 + C$

   - $$\int 5x^4\,dx = 20x^3 + C$

   _Explanation:_ The power 4 becomes 5, then the coefficient 5 is divided by 5, so the answer is $x^5 + C$. The most common wrong answer is B, which forgets to divide by the new power after increasing the exponent.

2. What is the best first step when evaluating $\int (x+3)(x-1)\,dx$?

   - Expand the brackets to get $x^2+2x-3$ ✔

   - Integrate each bracket separately, then multiply the answers

   - Expand the brackets to get $x^2+3x-1$

   - Substitute $x=0$ before integrating

   _Explanation:_ You should expand first so the integrand becomes a sum of powers of $x$, which can then be integrated term by term. The most common wrong answer is B, but there is no rule that lets you integrate a product by integrating each factor separately.

3. What is $\int_1^4 2x\,dx$?

   - $$8$

   - $$15$ ✔

   - $$16$

   - $$x^2+C$

   _Explanation:_ An antiderivative of $2x$ is $x^2$, so the value is $4^2-1^2=15$. The most common wrong answer is C, which uses the upper limit only and forgets to subtract the value at the lower limit.

4. Stretch: The curves $y=x+2$ and $y=x^2$ enclose a region. Which integral gives its area?

   - $$\int_{-1}^{2} \left((x+2)-x^2\right)\,dx$ ✔

   - $$\int_{-1}^{2} \left(x^2-(x+2)\right)\,dx$

   - $$\int_{0}^{2} \left((x+2)-x^2\right)\,dx$

   - $$\int_{-1}^{2} \left(x^2+x+2\right)\,dx$

   _Explanation:_ The curves meet where $x^2=x+2$, so $x=-1$ and $x=2$. On this interval the line is above the parabola, so the area is $\int_{-1}^{2} (\text{top}-\text{bottom})\,dx = \int_{-1}^{2} \left((x+2)-x^2\right)\,dx$. The most common wrong answer is B, which reverses the order and gives a negative value instead of an area.
