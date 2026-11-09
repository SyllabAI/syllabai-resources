# as-pure-mathematics-3-5-quadratic-inequalities — lesson

_Lane: `a-level-maths-edexcel` · grade — · 6 content steps · 3 check questions (source: MathsGenie lessons)_

## From quadratic expression to solution set

A quadratic inequality asks for the values of $x$ that make a quadratic expression positive or negative. For example, solving $x^2 + 4x \gt 12$ is equivalent to deciding where the graph $y = x^2 + 4x - 12 = (x+6)(x-2)$ is above the x-axis. The final answer is a solution set, usually written using interval notation or as separate regions on a number line.

Start by rearranging so that one side is zero: $x^2 + 4x \gt 12$ becomes $x^2 + 4x - 12 \gt 0$. Then factorise: $x^2 + 4x - 12 = (x+6)(x-2)$. The roots are $x = -6$ and $x = 2$, and these split the number line into intervals.

For this upward-opening quadratic, the expression is positive outside the roots and negative between them. So $x^2 + 4x \gt 12$ when $x \lt -6$ or $x \gt 2$. If the inequality is $\geq$ or $\leq$, include the roots because the rearranged quadratic equals $0$ there.

## Worked example with a strict inequality

Solve $x^2+7x>18$ by moving everything to the left. This gives
$$
x^2+7x-18>0
$$
and factorising gives
$$
(x+9)(x-2)>0.
$$

Now replace the inequality with an equation to find the critical values. From
$$
(x+9)(x-2)=0
$$
we get $x=-9$ and $x=2$.

The coefficient of $x^2$ is positive, so the parabola opens upwards and is above the $x$-axis outside the roots. Therefore the solution is
$$
x<-9 \quad \text{or} \quad x>2.
$$

## Strict versus non-strict inequalities

A strict inequality such as $<0$ or $>0$ does not include the roots. A non-strict inequality such as $\le 0$ or $\ge 0$ does include the roots because the quadratic may equal zero.

For $x(x+2)\le 15$, first expand and rearrange so one side is zero. This gives
$$
x^2+2x-15\le 0
$$
and factorising gives
$$
(x+5)(x-3)\le 0.
$$

The roots are $x=-5$ and $x=3$, and an upward-opening quadratic is negative between the roots. Because the sign is $\le$, the final answer is
$$
-5\le x\le 3.
$$

## When the quadratic opens downwards

If the coefficient of $x^2$ is negative, the parabola opens downwards. A quick method is to multiply the whole inequality by $-1$, but then you must reverse the inequality sign.

For example, to solve $-x^2+5x+6>0$, we multiply the expression by $-1$ and flip the inequality sign: $$x^2-5x-6<0$$

Next, factorise the quadratic to find the critical values: $$x^2-5x-6=(x-6)(x+1)$$ This shows that the roots are $x=-1$ and $x=6$.

Since an upward-opening quadratic is less than zero between its roots, the solution to $x^2-5x-6<0$ (and thus the original problem) is $-1<x<6$.

## Solving two inequalities at the same time

When a question says both inequalities, solve each one separately first. Then keep only the overlap, which is called the intersection.

Consider the system $$x^2+4x-12<0$$ and $$8+3x\le 10+x.$$

Factorising the quadratic gives $(x+6)(x-2)<0$, so $-6<x<2$. That is only the solution to the quadratic part.

Now solve the linear inequality: $8+3x\le 10+x \Rightarrow 2x\le 2 \Rightarrow x\le 1$. The overlap of $-6<x<2$ and $x\le 1$ is $$-6<x\le 1.$$

## Quick checks and common mistakes

Do not stop at the roots unless the question explicitly asks for them. The roots only mark the boundaries that split the number line into intervals.

If you are unsure which interval works, test a simple value. For $(x+9)(x-3) < 0$, testing $x=0$ gives $9 \times (-3) = -27$, so the middle interval $-9 < x < 3$ is correct.

Check the inequality sign one last time before you write your answer. A strict sign excludes the roots, while a non-strict sign includes them.

## Check yourself

1. What is the best first step when solving $x^2+7x>18$?

   - Rearrange to $x^2+7x-18>0$ ✔

   - Write $x^2+7x=18$

   - Factorise as $(x+9)(x+2)>0$

   - Solve $x^2+7x-18=0$ and stop

   _Explanation:_ A is correct because putting everything on one side lets you study the sign of a single quadratic expression. D is the most common wrong choice because the roots are only boundary values; you still have to decide which intervals make the inequality true.

2. Which solution set is correct for $x(x+2)\le 15$?

   - $$-5<x<3$

   - $$-5\le x\le 3$ ✔

   - $$x\le -5$ or $x\ge 3$

   - $$x=-5$ or $x=3$

   _Explanation:_ B is correct because the rearranged quadratic is upward-opening and $\le 0$ means between the roots with the endpoints included. A is the most common wrong answer because students find the right interval but forget that $\le$ includes the roots.

3. What is the final solution to the system $x^2+4x-12<0$ and $8+3x\le 10+x$?

   - $$-6<x<2$

   - $$x\le 1$

   - $$-6<x\le 1$ ✔

   - $$x<-6$ or $x>1$

   _Explanation:_ C is correct because you need the intersection of the quadratic solution $-6<x<2$ and the linear solution $x\le 1$. B is the most common wrong answer because it uses only the linear inequality and ignores the word both. Hint: Keep only the overlap.
