# grade-8-9-8-4-completing-the-square — lesson

_Lane: `gcse-maths-edexcel` · grade 8 · 6 content steps · 4 check questions (source: MathsGenie lessons)_

## What completing the square does

Completing the square means rewriting a quadratic so that it contains a squared bracket. Instead of a form like $x^2+px+q$, we aim for something like $a(x+h)^2+k$, which is easier to read from a graph.

The logic is based on the expansion of a perfect square: $$(x+r)^2=x^2+2rx+r^2$$ Running this backwards shows that the constant inside the bracket is exactly half the coefficient of the $x$ term.

To complete the square for $x^2+px+q$, you halve the coefficient $p$ and subtract the square of that value to keep the expression balanced. This results in the standard form: $$x^2+px+q=(x+\frac{p}{2})^2+q-\left(\frac{p}{2}\right)^2$$

## Worked example with coefficient 1

Rewrite $x^2-8x+9$ by halving $-8$ to get $-4$. Put $-4$ in the bracket, then correct the extra 16.

$$$x^2-8x+9=(x-4)^2-16+9=(x-4)^2-7$$

![Graph comparing y = x^2 and y = (x-4)^2-7 on coordinate axes, with vertex (4,-7) marked and line of symmetry x = 4](../assets/001-4b6997d1-6676-47b1-9e84-209e616e45f7.jpeg)

The graph shows that the parabola has moved 4 units right and 7 units down from $y=x^2$. The dashed line shows the line of symmetry $x=4$, where the bracket becomes zero.

That means the turning point is $(4,-7)$. Because the coefficient of the square is positive, this turning point is a minimum.

## Odd coefficients give fractions

If the coefficient of $x$ is odd, halving it gives a fraction, and that is completely normal. For $x^2-3x+2$, half of $-3$ is $-\frac{3}{2}$. Now complete the square carefully.

$$$x^2-3x+2=\left(x-\frac{3}{2}\right)^2-\frac{9}{4}+2=\left(x-\frac{3}{2}\right)^2-\frac{1}{4}$$

So the turning point is $\left(\frac{3}{2},-\frac{1}{4}\right)$. The common mistake is subtracting $\frac{3}{2}$ instead of subtracting its square, $\frac{9}{4}$.

## When the coefficient of $x^2$ is not 1

If the leading coefficient is not 1, factor it out of the $x^2$ and $x$ terms first. For $2x^2+16x+35$, we begin by grouping the terms containing $x$ and factoring out the 2.

$$$2x^2+16x+35=2(x^2+8x)+35$$

Now complete the square inside the bracket using the standard method: $x^2+8x=(x+4)^2-16$. Substitute this back into the expression and remember that the leading coefficient multiplies everything inside the brackets.

$$$2(x^2+8x)+35=2((x+4)^2-16)+35=2(x+4)^2+3$$

The turning point is $(-4,3)$. A common mistake is forgetting that the constant correction must be multiplied by the factor outside: $2 \times 16 = 32$, so $35 - 32 = 3$.

## Solving exactly by completing the square

To solve a quadratic exactly, complete the square, isolate the squared bracket, and then square root both sides. For $x^2+7x+6.25=0$, it helps to rewrite $6.25$ as $\frac{25}{4}$.

First, complete the square for the expression on the left:
$$x^2+7x+\frac{25}{4}=\left(x+\frac{7}{2}\right)^2-\frac{49}{4}+\frac{25}{4}=\left(x+\frac{7}{2}\right)^2-6$$
By substituting this back into the original equation and rearranging, we get $(x+\frac{7}{2})^2=6$.

Now square root both sides and remember the $\pm$ sign. This gives $x+\frac{7}{2}=\pm\sqrt{6}$, which results in the exact solution $x=-\frac{7}{2}\pm\sqrt{6}$.

## Reading minimums and maximums

In the vertex form $y=a(x+h)^2+k$, the turning point is always $(-h,k)$. This occurs because the squared term is zero when the expression inside the bracket is zero, making $k$ the extreme value.

The sign of $a$ determines the nature of this point. If $a > 0$, the parabola opens upwards and the turning point is a minimum. If $a < 0$, it opens downwards, meaning the turning point is a maximum.

For example, in the equation $y = -3(x+2)^2+5$, the turning point is $(-2, 5)$. Since the coefficient $a = -3$ is negative, the parabola opens downwards and the maximum value of the function is 5.

## Check yourself

1. Which expression is equivalent to $x^2+10x$?

   - $$(x+5)^2-25$ ✔

   - $$(x+10)^2-100$

   - $$(x+5)^2-5$

   - $$(x-5)^2-25$

   _Explanation:_ $$A$ is correct because half of 10 is 5, and $(x+5)^2=x^2+10x+25$, so you must subtract 25 to keep the expression the same. The most common wrong answer is $C$, which subtracts the half-coefficient instead of subtracting its square.

2. Which is the correct completed square form of $x^2-3x+2$?

   - $$\left(x-\frac{3}{2}\right)^2-\frac{1}{4}$ ✔

   - $$\left(x-\frac{3}{2}\right)^2-\frac{3}{2}$

   - $$\left(x+\frac{3}{2}\right)^2-\frac{1}{4}$

   - $$\left(x-\frac{3}{4}\right)^2+2$

   _Explanation:_ Option a is correct because half of the coefficient $-3$ is $-\frac{3}{2}$, and squaring this gives $\frac{9}{4}$. Subtracting this from the constant term gives $2-\frac{9}{4}=-\frac{1}{4}$. A common error is subtracting the linear coefficient's half ($-\frac{3}{2}$) instead of its square.

3. What is the completed square form of $2x^2+16x+35$?

   - $$2(x+4)^2+3$ ✔

   - $$2(x+4)^2+19$

   - $$2(x-4)^2+3$

   - $$(2x+4)^2+19$

   _Explanation:_ $$A$ is correct because you factor out 2, complete the square inside, and then multiply the $-16$ correction by 2. The most common wrong answer is $B$, which forgets the outside multiplier and only subtracts 16 instead of 32.

4. Solve $x^2+7x+6.25=0$ exactly.

   - $$x=-\frac{7}{2}\pm\sqrt{6}$ ✔

   - $$x=\frac{7}{2}\pm\sqrt{6}$

   - $$x=-\frac{7}{2}+\sqrt{6}$

   - $$x=\pm\sqrt{6}$

   _Explanation:_ $$A$ is correct because completing the square gives $(x+\frac{7}{2})^2=6$, and square rooting then subtracting $\frac{7}{2}$ gives two solutions. The most common wrong answer is $C$, which forgets the $\pm$ sign and loses one of the roots.
