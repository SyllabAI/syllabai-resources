# as-pure-mathematics-2-2-completing-the-square — lesson

_Lane: `a-level-maths-edexcel` · grade — · 7 content steps · 4 check questions (source: MathsGenie lessons)_

## The halfway idea

Completing the square rewrites a quadratic so the first part is a perfect square. The key algebraic expansion used for this process is:

$$$ (x+a)^2=x^2+2ax+a^2 $$

The middle coefficient is always twice the number inside the bracket. For a monic quadratic $x^2+bx+c$, halve the coefficient of $x$ first. That half-value goes inside the bracket, so the expression becomes $(x+\frac{b}{2})^2+k$ for some constant $k$.

## A first worked example

For $x^2+10x+7$, half of 10 is 5, so the matching square is $(x+5)^2$. Expanding that square gives $x^2+10x+25$.

The square result of 25 is 18 too large because the original constant is 7. To adjust the expression, we subtract 18 from the perfect square:

$$$x^2+10x+7=(x+5)^2-18$$

Always do a quick mental check by expanding the result. A common mistake is to write $(x+5)^2+7$, which would create $x^2+10x+32$ instead of the original quadratic.

## Fractions are normal

If the coefficient of $x$ is odd, the half-value is a fraction, and that is normal. For $x^2-7x+4$, half of $-7$ is $-\frac{7}{2}$.

Start with the matching square:
$$
\left(x-\frac{7}{2}\right)^2=x^2-7x+\frac{49}{4}
$$
Now compare the constant $\frac{49}{4}$ with the original constant 4.

To reduce $\frac{49}{4}$ down to 4, subtract $\frac{33}{4}$ outside the square. Therefore
$$
x^2-7x+4=\left(x-\frac{7}{2}\right)^2-\frac{33}{4}
$$
and the fractions are exactly what we expect.

## Non-monic quadratics

When the coefficient of $x^2$ is not 1, factor it out from the $x^2$ and $x$ terms first. Do not pull it out of the constant unless it is a common factor of the whole expression.

For $3x^2-12x+5$, factor the first two terms to get $$3x^2-12x+5=3(x^2-4x)+5$$ Inside the bracket, complete the square using $x^2-4x=(x-2)^2-4$.

Substitute back and simplify: $$3\left((x-2)^2-4\right)+5=3(x-2)^2-7$$ So the completed-square form is $3(x-2)^2-7$.

## Reading the minimum point from the graph

![Graph of the parabola y = (x - 4)^2 - 5 with vertex at (4, -5) and dashed axis of symmetry x = 4](../assets/001-3896128a-6f36-4d43-9389-ab43f9cf061c.jpeg)

Completed-square form shows the turning point straight away.

$$
y=(x-4)^2-5
$$

Because a square is always at least $0$, the square part can never be negative, so the lowest possible value of $y$ is $-5$.

Rewrite $y=x^2-8x+11$ as

$$
y=(x-4)^2-5
$$

The minimum point is $(4,-5)$, and the axis of symmetry is $x=4$.

In general, if $y=(x-a)^2+b$ and the coefficient of the square is positive, then the minimum point is $(a,b)$. The common sign trap is writing $(-a,b)$, but the bracket is zero when $x=a$.

## Using completed squares in inequalities

Completed-square form is powerful for inequalities because any real square is at least zero. If a quadratic can be written as $(x+a)^2+c$ with $c>0$, then it is always positive.

$$$x^2-10x+28=(x-5)^2+3$$

Since $(x-5)^2 \ge 0$, the smallest possible value for this expression is 3. Therefore, the expression is greater than 0 for all real $x$.

If you are comparing two expressions, move everything to one side first to form a single quadratic. For instance, $x^2+3x+9 > x+1$ becomes $x^2+2x+8 = (x+1)^2+7 > 0$.

## Solving with a parameter

To solve by completing the square, rewrite the quadratic so a squared bracket stands on one side. For $x^2+px+5=0$, the first step is $$\left(x+\frac{p}{2}\right)^2-\frac{p^2}{4}+5=0$$ and then the constants can be moved across.

Now isolate the square: $$\left(x+\frac{p}{2}\right)^2=\frac{p^2-20}{4}$$ Taking square roots gives $x+\frac{p}{2}=\pm \frac{1}{2}\sqrt{p^2-20}$.

So the roots are $$x=-\frac{p}{2}\pm \frac{1}{2}\sqrt{p^2-20}$$ Real roots need $p^2-20 \ge 0$, while no real roots occur when $-2\sqrt{5}<p<2\sqrt{5}$.

## Check yourself

1. Which perfect square has the same $x^2$ and $x$ terms as $x^2-8x+11$?

   - $$(x-4)^2$ ✔

   - $$(x-8)^2$

   - $$(x+4)^2$

   - $$(x-4)^2+11$

   _Explanation:_ $$(x-4)^2=x^2-8x+16$, so it matches the $x^2$ term and the $x$ term exactly. The common wrong answer $(x-8)^2$ uses the full coefficient instead of half, giving $x^2-16x+64$. Hint: In $(x+a)^2$, the coefficient of $x$ is $2a$.

2. Which is the correct completed-square form of $x^2-7x+4$?

   - $$\left(x-\frac{7}{2}\right)^2-\frac{33}{4}$ ✔

   - $$(x-7)^2-45$

   - $$\left(x-\frac{7}{2}\right)^2+\frac{33}{4}$

   - $$\left(x+\frac{7}{2}\right)^2-\frac{33}{4}$

   _Explanation:_ Half of $-7$ is $-\frac{7}{2}$, and the correction is $4-\frac{49}{4}=-\frac{33}{4}$. The common wrong answer $(x-7)^2-45$ forgets that the number inside the bracket must be half the coefficient of $x$, not the whole coefficient. Hint: Expand your chosen bracket mentally and compare the middle term.

3. What is the minimum point of $y=x^2+6x-2$?

   - $$(3,-11)$

   - $$(-3,-11)$ ✔

   - $$(-6,-2)$

   - $$(-3,-2)$

   _Explanation:_ Hint: Rewrite the quadratic in the form $(x-a)^2+b$. Completing the square gives $y=(x+3)^2-11$, so the minimum occurs when the square is 0, at $x=-3$, and the minimum value is $-11$. The common wrong answer $(3,-11)$ comes from flipping the sign incorrectly; $(x+3)^2$ is zero when $x=-3$.

4. Which statement is enough to prove $x^2-10x+28>0$ for all real $x$?

   - $$x^2-10x+28=(x-5)^2+3$ ✔

   - $$x^2-10x+28=(x-5)^2+28$

   - $$x^2-10x+28=(x-5)^2-3$

   - $$x^2-10x+28=(x+5)^2+3$

   _Explanation:_ Writing it as $(x-5)^2+3$ works because a square is always at least 0, so the whole expression is at least 3. The common wrong answer $(x-5)^2-3$ gets the constant adjustment the wrong way round and would expand to $x^2-10x+22$, not the original quadratic.
