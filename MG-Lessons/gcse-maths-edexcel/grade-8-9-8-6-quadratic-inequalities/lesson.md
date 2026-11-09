# grade-8-9-8-6-quadratic-inequalities — lesson

_Lane: `gcse-maths-edexcel` · grade 8 · 6 content steps · 3 check questions (source: MathsGenie lessons)_

## What a quadratic inequality means

![Upward-opening parabola crossing the x-axis at x = -3 and x = 2, with positive regions outside the roots and a negative region between them labelled](../assets/001-57b0df04-53bf-4369-b476-9aa8acb7abbc.jpeg)

A quadratic inequality asks when a quadratic expression is greater than, less than, or equal to zero. To solve one, first find the boundary values by solving the related quadratic equation where the expression equals zero.

The roots split the number line into regions. For an upward-opening parabola, the expression is positive outside the roots and negative between them.

Strict signs $<$ and $>$ do not include the roots. Inclusive signs $\le$ and $\ge$ do include them.

## Worked example with $>0$

To solve $x^2+5x+6>0$, start with the related equation. We swap the inequality for an equals sign to find the boundary values: $$x^2+5x+6=0$$

Factorising the equation gives $(x+2)(x+3)=0$, showing the boundary values are $x=-2$ and $x=-3$. Put them in order as $-3$ then $-2$ so it is easy to read the intervals.

The coefficient of $x^2$ is positive, so the parabola opens upwards and the expression is positive outside the roots. The solution is $$x<-3 \quad \text{or} \quad x>-2$$

## Strict or inclusive

When the sign is inclusive, the endpoints stay in the answer. On a number line, use closed circles for $\le$ or $\ge$ and open circles for $<$ or $>$.

To solve $x^2-8x+15\le 0$, we first determine the roots of the related quadratic equation: $$x^2-8x+15=0$$

This factorises to $(x-3)(x-5)=0$, giving roots of $3$ and $5$. Since the parabola opens upwards, the expression is negative between these roots.

Because the inequality is inclusive, we include the boundary points in our final solution: $$3\le x\le 5$$

## Rearrange before factorising

Some inequalities are not already equal to zero on one side. Solve $5x+14>x^2$ by subtracting $5x+14$ from both sides to set one side of the inequality to zero:

$$$0>x^2-5x-14$$

We rewrite this as $x^2-5x-14<0$. Factorising then gives $(x-7)(x+2)<0$, which reveals the boundary values of $x=7$ and $x=-2$.

Since the coefficient of $x^2$ is positive, the less-than-zero region is found between the two roots. Therefore, the solution is: $$-2<x<7$$

## Special cases and non-monic quadratics

If there is no $x$ term, it is still a quadratic inequality. To solve $x^2 \le 64$, we rearrange the terms into standard form and factorise the expression into its linear components.

$$$x^2-64\le 0 \implies (x-8)(x+8)\le 0$$

The roots are $-8$ and $8$, so the solution is $-8\le x\le 8$. Do not forget the negative root, because squaring a negative number can still give a value less than or equal to $64$.

Non-monic quadratics use the same method. For example, given $6x^2+7x-3=(3x-1)(2x+3)$, the inequality $6x^2+7x-3<0$ is satisfied between the roots $x=-\frac{3}{2}$ and $x=\frac{1}{3}$.

## Stretch: listing integer solutions

Sometimes the boundary values are not integers, so factorising is not convenient. For $x^2-6x+7<0$, use the quadratic formula on the related equation: $$x=\frac{6\pm\sqrt{6^2-4\cdot 1\cdot 7}}{2}$$

This simplifies to $x=3\pm\sqrt{2}$. Since the quadratic opens upwards and the inequality is less than zero, the full solution is $$3-\sqrt{2}<x<3+\sqrt{2}$$

Now approximate the roots: $3-\sqrt{2}\approx 1.59$ and $3+\sqrt{2}\approx 4.41$. The integer values in that interval are $2$, $3$, and $4$.

## Check yourself

1. For $x^2+7x+12>0$, what are the boundary values?

   - $$x=-4$ and $x=-3$ ✔

   - $$x=4$ and $x=3$

   - $$x=-4$ and $x=3$

   - $$x=4$ and $x=-3$

   _Explanation:_ Replace $>$ with $=$, factorise $x^2+7x+12=(x+4)(x+3)$, and set each bracket equal to zero. The common wrong answer is $3$ and $4$, which comes from forgetting that $(x+4)=0$ gives $x=-4$, not $4$.

2. Which solution set is correct for $x^2-8x+15\le 0$?

   - $$3\le x\le 5$ ✔

   - $$x<3$ or $x>5$

   - $$3<x<5$

   - $$x\le 3$ or $x\ge 5$

   _Explanation:_ The quadratic is zero at $3$ and $5$ and, because it opens upwards, it is less than zero between the roots. The common wrong answer is $3<x<5$, which forgets that $\le 0$ includes the boundary values.

3. Solve $x^2\le 64$.

   - $$-8\le x\le 8$ ✔

   - $$x\le 8$

   - $$x\ge -8$

   - $$x<-8$ or $x>8$

   _Explanation:_ Rewrite as $x^2-64\le 0$ and use the roots $-8$ and $8$; an upward-opening quadratic is less than or equal to zero between the roots. The common wrong answer is $x\le 8$, which forgets that negative values like $x=-5$ also satisfy the inequality.
