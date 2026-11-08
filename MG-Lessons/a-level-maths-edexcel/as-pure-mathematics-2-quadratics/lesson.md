# as-pure-mathematics-2-quadratics — lesson

_Lane: `a-level-maths-edexcel` · grade — · 6 content steps · 3 check questions (source: MathsGenie lessons)_

## Quadratic form and graphs

A quadratic expression has the form $ax^2+bx+c$, where $a$, $b$, and $c$ are constants and $a\neq0$. A quadratic equation is formed by setting this equal to zero, usually as $ax^2+bx+c=0$.

The graph of $y=ax^2+bx+c$ is a parabola. If $a>0$ it opens upwards, and if $a<0$ it opens downwards; its roots are the $x$-values where the graph meets the $x$-axis.

To put an equation into standard form, move every term to one side. For example, $3x^2+7=2x$ becomes $3x^2-2x+7=0$, so $a=3$, $b=-2$, and $c=7$.

## Using the discriminant

![Three parabolas showing a curve crossing the x-axis twice, a curve touching it at the vertex, and a curve staying above it, labelled with the three discriminant cases](../assets/001-cc2c17eb-c431-421c-8293-97a4632a1484.jpeg)

The discriminant of $ax^2+bx+c=0$ is $\Delta=b^2-4ac$. It tells you how many real roots a quadratic has, but only after the equation is written in standard form.

If $\Delta>0$, there are two distinct real roots; if $\Delta=0$, there is one repeated root; if $\Delta<0$, there are no real roots. On the graph, that means the parabola crosses the $x$-axis twice, just touches it once, or misses it completely.

A repeated root happens at the turning point, where the curve only touches the axis. Always identify $a$, $b$, and $c$ carefully before substituting, especially the sign of $b$.

## Completing the square

![Graph of y = 3(x+2)^2 - 7 with the turning point labelled at (-2,-7) and a dashed vertical axis of symmetry x = -2](../assets/002-a1a64cd6-eeb2-43b9-accd-3d0ccd43850b.jpeg)

Completing the square rewrites a quadratic as $a(x-h)^2+k$. In this form, the turning point is $(h,k)$, and the sign of $a$ tells you whether it is a minimum or maximum.

To rewrite $3x^2+12x+5$, first factor 3 from the first two terms:

$$3x^2+12x+5=3(x^2+4x)+5$$

Then complete the square inside the bracket:

$$x^2+4x=(x+2)^2-4$$

Substitute back and simplify:

$$3\left((x+2)^2-4\right)+5=3(x+2)^2-7$$

So the turning point is $(-2,-7)$ and, because $a=3>0$, it is a minimum. The axis of symmetry is $x=-2$.

## Parameters and edge cases

When a parameter appears in the coefficient of $x^2$, first check that the equation is still quadratic. If that coefficient becomes 0, the discriminant rules for quadratics no longer apply.

For $(k+1)x^2+2x+k=0$ to have two distinct real roots, first require $k\neq-1$ so the equation stays quadratic. Then use $\Delta>0$:
$$2^2-4(k+1)k>0$$
This simplifies to the quadratic inequality $k^2+k-1<0$.

Solve the boundary equation $k^2+k-1=0$ to find the critical values:
$$k=\frac{-1\pm\sqrt{5}}{2}$$
The quadratic in $k$ is negative between these roots, meaning $k$ must lie within that range.

The final solution is:
$$\frac{-1-\sqrt{5}}{2}<k<-1 \quad \text{or} \quad -1<k<\frac{-1+\sqrt{5}}{2}$$
The interval splits at $k=-1$ because that specific value makes the equation linear, not quadratic.

## Tangency and repeated roots

When a line is tangent to a curve, the two graphs meet at one point. After rearranging, the resulting equation in $x$ has a repeated root, so its discriminant is zero.

For the curve $y=\frac{3}{x}+k$ and the line $y=-x+4$, set them equal and multiply by $x$ to clear the denominator:
$$\frac{3}{x}+k=-x+4 \Rightarrow 3+kx=-x^2+4x$$

Rearranging the equation into a standard quadratic form gives:
$$x^2+(k-4)x+3=0$$
Now we can apply the condition for tangency by setting the discriminant $\Delta = 0$.

$$$(k-4)^2-4(1)(3)=0$$
Solving for $k$, we get $(k-4)^2=12$, which simplifies to $k=4\pm2\sqrt{3}$. These are the two values of $k$ for which the line just touches the curve.

## Quadratic models

In modelling questions, completed-square form makes the maximum or minimum easy to spot. For $P=50-2(x-12)^2$, the square term is always non-negative, so the largest possible value occurs when $(x-12)^2=0$.

That gives a maximum profit of £50,000 when $x=12$, because $P$ is measured in thousands of pounds. To find when profit is more than £32,000, solve

$$50-2(x-12)^2>32$$

Rearranging gives

$$(x-12)^2<9$$

so

$$-3<x-12<3 \Rightarrow 9<x<15$$

The endpoints are excluded because the profit must be more than £32,000, not equal to it. In context, $x$ should also be a sensible positive ticket price.

## Check yourself

1. After rearranging $3x^2+7=2x$ into the form $ax^2+bx+c=0$, what are $a$, $b$, and $c$?

   - $$a=3$, $b=-2$, $c=7$ ✔

   - $$a=3$, $b=2$, $c=7$

   - $$a=3$, $b=-2$, $c=-7$

   - $$a=2$, $b=3$, $c=7$

   _Explanation:_ A is correct because subtracting $2x$ from both sides gives $3x^2-2x+7=0$. B is the most common wrong answer because the sign of the middle term was not changed when moving $2x$ to the left.

2. Which set of values of $k$ gives two distinct real roots for $(k+1)x^2+2x+k=0$?

   - $$\frac{-1-\sqrt{5}}{2}<k<\frac{-1+\sqrt{5}}{2}$

   - $$k<\frac{-1-\sqrt{5}}{2}$ or $k>\frac{-1+\sqrt{5}}{2}$

   - $$\frac{-1-\sqrt{5}}{2}<k<-1$ or $-1<k<\frac{-1+\sqrt{5}}{2}$ ✔

   - $$k=-1$

   _Explanation:_ C is correct because $\Delta>0$ gives the interval between the two roots of $k^2+k-1$, but $k=-1$ must be excluded since the equation would no longer be quadratic. A is the most common wrong answer because it forgets to remove that excluded value.

3. For $P=50-2(x-12)^2$, which ticket prices give profit more than £32,000?

   - $$9<x<15$ ✔

   - $$x\le9$ or $x\ge15$

   - $$9\le x\le15$

   - $$x=12$ only

   _Explanation:_ A is correct because solving $50-2(x-12)^2>32$ gives $(x-12)^2<9$, so $9<x<15$. C is the most common wrong answer because it includes $x=9$ and $x=15$, where the profit is exactly £32,000 rather than more than £32,000. Hint: Treat it as an inequality in completed-square form.
