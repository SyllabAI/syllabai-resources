# grade-8-9-8-4-completing-the-square — lesson

_Lane: `igcse-maths-edexcel` · grade 8 · 6 content steps · 3 check questions (source: MathsGenie lessons)_

## Building a perfect square

Completing the square rewrites a quadratic into a form where the square is obvious. The aim is to write it as $(x + a)^2 + b$, which makes the structure much easier to read.

The pattern comes from expansion:
$$
(x + p)^2 = x^2 + 2px + p^2
$$
The middle term is always twice the number inside the bracket.

So if the expression begins $x^2 + bx$, the square part starts as $\left(x + \frac{b}{2}\right)^2$. After that, you correct the constant outside the bracket because the square has created a hidden $+\left(\frac{b}{2}\right)^2$.

## Worked example with coefficient 1

To rewrite $x^2 - 8x + 6$, focus on the first two terms. Half of $-8$ is $-4$, so the square bracket must be $(x - 4)^2$.

Now check what that bracket really expands to:
$$
(x - 4)^2 = x^2 - 8x + 16
$$
This is close, but it has $+16$ instead of the original constant.

Correct the extra 16 outside the bracket:
$$
x^2 - 8x + 6 = (x - 4)^2 - 16 + 6 = (x - 4)^2 - 10
$$
That outside number is what makes the expression exactly equal to the original quadratic.

## Turning points from completed square form

![Graph of $y=(x-2)^2+1$ with turning point $(2,1)$ and axis of symmetry $x=2$ labelled](../assets/001-b807f30a-f977-4b62-9d1a-a0a0a42d6604.jpeg)

When a quadratic is written as $y = (x - h)^2 + k$, its turning point is $(h, k)$. The axis of symmetry is the vertical line $x = h$.

In $y = x^2 + 10x + 4$, half of 10 is 5, so we can complete the square:

$$y = (x + 5)^2 - 25 + 4 = (x + 5)^2 - 21$$

This puts the quadratic into completed square form. The square part is smallest when it equals 0, so $x + 5 = 0$ and $x = -5$. Therefore the turning point is $(-5, -21)$, not $(5, -21)$.

## Fractions are allowed

If the coefficient of $x$ is odd, halving it gives a fraction and that is completely fine. You use exactly the same method as you would with even integers.

For $y = x^2 + 5x - 2$, half of 5 is $\frac{5}{2}$, so start with $\left(x + \frac{5}{2}\right)^2$. Expanding this bracket shows that the hidden constant being added is $\frac{25}{4}$.

Subtracting this constant gives: $$y = \left(x + \frac{5}{2}\right)^2 - \frac{25}{4} - 2 = \left(x + \frac{5}{2}\right)^2 - \frac{33}{4}$$ From this form, we can see the turning point is $\left(-\frac{5}{2}, -\frac{33}{4}\right)$.

## When the leading coefficient is not 1

If the quadratic starts with a coefficient other than 1, such as $2x^2$ or $3x^2$, first factor that number out of the $x^2$ and $x$ terms. You can then complete the square for the simplified expression inside the bracket.

For $2x^2 - 20x + 41$, we begin by factoring out the 2:
$$2x^2 - 20x + 41 = 2(x^2 - 10x) + 41$$
Inside the bracket, $x^2 - 10x$ is completed to $(x - 5)^2 - 25$.

Substitute this back and multiply the correction term by the coefficient:
$$2((x - 5)^2 - 25) + 41 = 2(x - 5)^2 - 50 + 41 = 2(x - 5)^2 - 9$$
The turning point is $(5, -9)$. A common error is forgetting to multiply the $-25$ by the leading 2.

## Solving by completing the square

To solve a quadratic exactly, rewrite it in completed square form, move the constant, then square root both sides. This is especially useful when the answers are not whole numbers.

For $x^2 + 6x - 5 = 0$, complete the square first: $$x^2 + 6x - 5 = (x + 3)^2 - 9 - 5 = (x + 3)^2 - 14$$ So the equation becomes $(x + 3)^2 - 14 = 0$.

Now isolate the square to prepare for rooting: $$(x + 3)^2 = 14$$ Taking square roots gives $x + 3 = \pm \sqrt{14}$.

Finally, rearrange the equation to solve for $x$: $$x = -3 \pm \sqrt{14}$$ The $\pm$ matters because both $+\sqrt{14}$ and $-\sqrt{14}$ square to 14.

## Check yourself

1. Which square bracket should you write first when completing the square for $x^2 + 10x - 3$?

   - $$(x + 5)^2$ ✔

   - $$(x + 10)^2$

   - $$(x + 3)^2$

   - $$(x + 25)^2$

   _Explanation:_ A is right because half of 10 is 5, so the square must start as $(x + 5)^2$. The common wrong answer B uses the full coefficient of $x$ instead of halving it.

2. What is the turning point of $y = (x - 6)^2 - 11$?

   - $$(6, -11)$ ✔

   - $$(-6, -11)$

   - $$(6, 11)$

   - $$(-6, 11)$

   _Explanation:_ A is right because the square is zero when $x - 6 = 0$, so $x = 6$ and then $y = -11$. The common wrong answer B flips the sign even though the bracket is already $x - 6$.

3. Which is equivalent to $3x^2 + 12x + 1$?

   - $$3(x + 2)^2 - 11$ ✔

   - $$3(x + 2)^2 - 3$

   - $$3(x + 4)^2 + 1$

   - $$(3x + 2)^2 - 11$

   _Explanation:_ A is right because $3x^2 + 12x + 1 = 3(x^2 + 4x) + 1 = 3((x + 2)^2 - 4) + 1 = 3(x + 2)^2 - 11$. The common wrong answer B forgets that the correction $-4$ inside the bracket must also be multiplied by 3.
