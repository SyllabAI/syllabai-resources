# grade-8-9-8-6-quadratic-inequalities — lesson

_Lane: `igcse-maths-edexcel` · grade 8 · 6 content steps · 3 check questions (source: MathsGenie lessons)_

## What quadratic inequalities mean

![Upward-opening parabola crossing the x-axis at -5 and -2, with positive regions outside the roots and a negative region between them](../assets/001-77dc506a-b3ae-4f05-a653-1e47cce5d95c.jpeg)
A quadratic inequality asks for all the values of $x$ that make a quadratic expression positive or negative, such as $x^2+4x+3>0$. The roots are the key starting points because they are the values where the expression equals zero.

For an upward-opening quadratic, the expression is positive outside the roots and negative between them. If you rearrange first so the coefficient of $x^2$ is positive, this pattern becomes very reliable.

If the inequality is strict, like $<$ or $>$, the roots are not included in the answer. If the inequality is inclusive, like $\le$ or $\ge$, the roots are included.

## A first worked example

Start by solving the related equation $(x-2)(x-6)=0$. Set each factor equal to zero to get the roots.

$$$x=2 \quad \text{and} \quad x=6$$

Because the quadratic opens upward and the question asks for $(x-2)(x-6)<0$, we want the negative region between the roots. You can check this by testing $x=3$, which gives $(1)(-3)=-3$.

The inequality is strict, so the endpoints are not included. The solution is $$2<x<6$$

## Between or outside?

Factorise the quadratic first. This turns the expression into two simpler factors.
$$x^2+7x+10=(x+5)(x+2)$$

The roots are $-5$ and $-2$, and the coefficient of $x^2$ is positive. That means the graph is above the x-axis outside the roots.

So the solution to $x^2+7x+10>0$ is two separate regions. Write
$$x<-5 \quad \text{or} \quad x>-2$$
Use "or", not "and", because a number can lie in either outside region.

## Rearrange before solving

Always move everything to one side before you decide where the quadratic is positive or negative. Adding or subtracting terms does not change the inequality sign.

For $8x+20>x^2$, we must rearrange the inequality so that one side is zero: $$8x+20>x^2$$ $$0>x^2-8x-20$$ $$x^2-8x-20<0$$

Now factorise the quadratic expression to find the roots of the equation: $$x^2-8x-20=(x-10)(x+2)$$ $$x=-2 \quad \text{and} \quad x=10$$

The coefficient of $x^2$ is positive, so a $<0$ inequality indicates the region between the roots. The final solution is $$-2<x<10$$

## When the coefficient is not 1

The same method works even when the coefficient of $x^2$ is not $1$. Consider solving $4x^2-4x-15<0$ by first factorising the expression into the following form:

$$$(2x-5)(2x+3)<0$$ The roots come from setting each bracket equal to zero, which provides the critical values: $$x=\frac{5}{2} \quad \text{and} \quad x=-\frac{3}{2}$$

Put the roots in numerical order as $-\frac{3}{2}$ and then $\frac{5}{2}$. Because the quadratic opens upward and we want values less than zero, the solution is the region between the roots: $$-\frac{3}{2}<x<\frac{5}{2}$$

This same between-the-roots pattern also explains why $x^2\le 64$ gives values from $-8$ to $8$. Since the inequality includes the 'equal to' component, we include both endpoints in the final result.

## When factorising does not work nicely

If the quadratic does not factorise neatly, use the quadratic formula on the related equation. For the equation $x^2-6x+7=0$, the formula provides the roots as follows:

$$$x=\frac{-(-6)\pm\sqrt{(-6)^2-4(1)(7)}}{2(1)}$$
$$x=3\pm\sqrt{2}$$

These roots are approximately $1.59$ and $4.41$. Since the quadratic opens upward, $x^2-6x+7<0$ is true between these roots, which gives the integer solutions $2, 3, 4$.

Sometimes there are no real roots, meaning the graph never crosses the x-axis. In that case, test one easy value, often $x=0$, to decide whether the inequality is true for all real values or for none.

## Check yourself

1. For an upward-opening quadratic with roots $1$ and $5$, where is the quadratic negative?

   - $$1<x<5$ ✔

   - $$x<1$ or $x>5$

   - $$1\le x\le 5$

   - all real values of $x$

   _Explanation:_ An upward-opening quadratic is below the x-axis between its roots, so the negative region is $1<x<5$. The most common wrong answer is B because students remember the "outside" pattern, but outside the roots the quadratic is positive, not negative.

2. Which is the correct solution to $x^2+7x+10>0$?

   - $$-5<x<-2$

   - $$x<-5$ or $x>-2$ ✔

   - $$x<-5$ and $x>-2$

   - $$-5\le x\le -2$

   _Explanation:_ Factorising gives roots $-5$ and $-2$, and an upward-opening quadratic is positive outside its roots, so B is correct. The most common wrong answer is A because that is the region where the quadratic is negative, and D also wrongly includes the roots even though the inequality is strict.

3. Which list gives all the integer values satisfying $x^2-6x+7<0$?

   - $$1,2,3,4$

   - $$2,3,4$ ✔

   - $$2,3,4,5$

   - $$1,2,3,4,5$

   _Explanation:_ Solving $x^2-6x+7=0$ gives roots $3\pm\sqrt{2}\approx1.59$ and $4.41$, so the integers strictly between them are $2,3,4$. The most common wrong answer is A because students round the lower root down to $1$, but $1$ lies outside the solution interval.
