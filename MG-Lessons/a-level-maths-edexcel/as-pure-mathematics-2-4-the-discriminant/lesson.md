# as-pure-mathematics-2-4-the-discriminant — lesson

_Lane: `a-level-maths-edexcel` · grade — · 6 content steps · 3 check questions (source: MathsGenie lessons)_

## What the discriminant tells you

![Three side-by-side parabolas showing two roots, one repeated root, and no real roots](../assets/001-6c4bf37b-314c-4e06-8c25-caeda6e6f512.jpeg)
The quadratic formula is shown below:

$$$x=\frac{-b\pm\sqrt{b^{2}-4ac}}{2a}$$

The expression under the square root is called the discriminant. For a quadratic written as $ax^{2}+bx+c=0$, the discriminant is $\Delta=b^{2}-4ac$. Its sign tells you the number of real roots without solving the equation fully.

If $\Delta>0$ there are two distinct real roots, if $\Delta=0$ there is one repeated root, and if $\Delta<0$ there are no real roots. On a graph, that means the parabola crosses the x-axis twice, touches it once, or misses it completely.

## Reading off $a$, $b$, and $c$

A discriminant question only works once the equation is written in standard form $ax^2+bx+c=0$. Then you can read off $a$, $b$, and $c$ carefully, including any minus signs.

For $5x^2+(k-3)x-2=0$, the coefficients are $a=5$, $b=k-3$, and $c=-2$. The minus sign belongs to the constant term, so $c$ is not $2$.

## Worked example: number of real roots

You do not need to solve a quadratic fully if the question only asks for the number of real roots. For $2x^2-5x+7=0$, identify the coefficients $a=2$, $b=-5$, and $c=7$.

Then calculate the discriminant: $$\Delta=(-5)^2-4(2)(7)=25-56=-31$$ This resulting value is negative.

Since $\Delta < 0$, the equation has no real roots. A common slip is to treat $(-5)^2$ as $-25$, but the correct value is $25$.

## Worked example: equal roots

Equal roots occur when the discriminant is exactly zero. For the equation $kx^2+7x+k=0$, we identify the coefficients as $a=k$, $b=7$, and $c=k$.

$$$49-4k^2=0$$

Solving this equation gives $4k^2=49$, so $k=\pm\frac{7}{2}$. Since the problem specifies that $k>0$, the only valid value is $k=\frac{7}{2}$.

## When the equation might stop being quadratic

If the coefficient of $x^2$ contains a parameter, you must first ensure the equation remains quadratic by checking that the coefficient is not zero. In the case of $(r+2)x^2+5x+r=0$, the equation is quadratic only when $r+2\neq 0$, meaning $r\neq -2$.

To find the values for two distinct real roots, we set the discriminant $\Delta > 0$. By substituting the coefficients into the formula $b^2 - 4ac$, we arrive at an inequality that must be solved for the parameter $r$.

$$$25-4(r+2)r>0\quad\Rightarrow\quad 4r^2+8r-25<0$$

The boundary values are $r=\frac{-2\pm\sqrt{29}}{2}$. Because the quadratic in $r$ is negative between its roots and we must exclude the value where the equation ceases to be quadratic ($r=-2$), the final range is $\frac{-2-\sqrt{29}}{2}<r<-2$ or $-2<r<\frac{-2+\sqrt{29}}{2}$.

## Intersections and tangents

![Circle centred at the origin with two symmetric tangent lines touching it and crossing the y-axis at 3](../assets/002-a0e2ca27-815e-45d8-95a9-57c2a89756d7.jpeg)

When a curve and a line intersect, they have the same $y$-value, so you set their equations equal. After rearranging to a quadratic in $x$, the discriminant tells you whether there are two intersections, one tangent point, or no intersection.

A tangent means the graphs meet at exactly one point, so the quadratic in $x$ has a repeated root and $\Delta=0$. For $y=mx+3$ and $x^2+y^2=5$, substitute the line into the circle:

$$x^2+(mx+3)^2=5$$

Expanding and rearranging gives $(1+m^2)x^2+6mx+4=0$. Using $\Delta=0$ gives $(6m)^2-4(1+m^2)(4)=0$, so $20m^2=16$ and $m=\pm\frac{2\sqrt{5}}{5}$.

## Check yourself

1. For a quadratic equation, what does $\Delta<0$ tell you?

   - It has two distinct real roots

   - It has one repeated real root

   - It has no real roots ✔

   - It is not quadratic

   _Explanation:_ A negative discriminant means the square root part of the quadratic formula would be the square root of a negative number, so there are no real solutions. The common wrong answer B is wrong because one repeated root happens when $\Delta=0$, not when $\Delta<0$.

2. The equation $x^2+kx+6=0$ has no real roots. Which condition on $k$ is correct?

   - $$-2\sqrt{6}<k<2\sqrt{6}$ ✔

   - $$k<-2\sqrt{6}$ or $k>2\sqrt{6}$

   - $$k=\pm 2\sqrt{6}$

   - $$k>24$

   _Explanation:_ No real roots means $\Delta<0$, so $k^2-4(1)(6)<0$, which gives $k^2<24$ and therefore $-2\sqrt{6}<k<2\sqrt{6}$. The common wrong answer B comes from solving $k^2>24$, but that would give two distinct real roots, not no real roots.

3. The equation $(r+2)x^2+5x+r=0$ has two distinct real roots. Which set of values of $r$ is correct?

   - $$\frac{-2-\sqrt{29}}{2}<r<\frac{-2+\sqrt{29}}{2}$

   - $$\frac{-2-\sqrt{29}}{2}<r<-2$ or $-2<r<\frac{-2+\sqrt{29}}{2}$ ✔

   - $$r<\frac{-2-\sqrt{29}}{2}$ or $r>\frac{-2+\sqrt{29}}{2}$

   - All real $r$ except $-2$

   _Explanation:_ Solving $4r^2+8r-25<0$ gives values between the two boundary roots. The common wrong answer A forgets that $r=-2$ makes the coefficient of $x^2$ zero, so the equation becomes linear and must be excluded.
