# grade-7-7-4-quadratic-formula — lesson

_Lane: `gcse-maths-edexcel` · grade 7 · 6 content steps · 4 check questions (source: MathsGenie lessons)_

## Standard form and the formula

Some quadratics factorise, but many do not. The quadratic formula works for any quadratic equation, even when the answers are awkward decimals or surds.

Before using it, rearrange into standard form $$ax^2+bx+c=0$$ where $a$, $b$, and $c$ are the coefficients and $a \ne 0$. The biggest trap is signs, so only identify $a$, $b$, and $c$ after rearranging.

The formula is $$x=\frac{-b\pm\sqrt{b^2-4ac}}{2a}$$ The $\pm$ means you should check a plus answer and a minus answer.

## The discriminant and the graph

![Three side-by-side quadratic graphs showing a parabola cutting the x-axis twice, touching it once, and not meeting it, labelled with positive, zero, and negative discriminant cases](../assets/001-919b3d04-db31-47db-b572-a1b581ba8957.jpeg)

The part under the square root, $b^2-4ac$, is called the discriminant. It tells you what kind of answers the formula will give before you even solve.

If $b^2-4ac>0$, the graph cuts the x-axis twice, so there are two different real roots. If $b^2-4ac=0$, the graph just touches the x-axis once, so the two formula answers are actually the same.

If $b^2-4ac<0$, the square root is not real, so there are no real solutions. At GCSE, this usually means the graph does not meet the x-axis.

## Worked example: rearrange first

Suppose you need to solve $5x^2=4x+7$ to 3 significant figures. First move everything to one side so the right-hand side is 0:
$$
5x^2-4x-7=0
$$
This is now in standard form.

Read off the coefficients with their signs: 
$$
a=5,\quad b=-4,\quad c=-7
$$
Notice that $b$ is negative, so $-b$ becomes positive when you substitute:
$$
x=\frac{-(-4)\pm\sqrt{(-4)^2-4(5)(-7)}}{2(5)}
$$

Simplify in stages, not all at once:
$$
x=\frac{4\pm\sqrt{16+140}}{10}=\frac{4\pm\sqrt{156}}{10}
$$
Then do the plus case and the minus case separately on your calculator.

This gives $x=1.648\ldots$ or $x=-0.848\ldots$. To 3 significant figures, the solutions are $x=1.65$ or $x=-0.848$. Keep full calculator accuracy until this final line.

## Worked example: decimal answers

Solve $2x^2+9x+3=0$ correct to 2 decimal places. Identifying the coefficients, we have $a=2$, $b=9$, and $c=3$.

$$$
 x=\frac{-9\pm\sqrt{9^2-4(2)(3)}}{2(2)}=\frac{-9\pm\sqrt{57}}{4}
 $$

Now evaluate the plus case first: $$x=\frac{-9+\sqrt{57}}{4}=-0.362\ldots$$ Then evaluate the minus case: $$x=\frac{-9-\sqrt{57}}{4}=-4.137\ldots$$

Round only at the end, not halfway through. So the solutions are $x=-0.36$ or $x=-4.14$ to 2 decimal places. If you round $\sqrt{57}$ too early, both answers can drift.

## Worked example: exact surd answers

Sometimes the question wants an exact answer, so do not turn the square root into a decimal. For $x^2+10x-2=0$, substitute the coefficients into the quadratic formula to get: $$x=\frac{-10\pm\sqrt{10^2-4(1)(-2)}}{2(1)}=\frac{-10\pm\sqrt{108}}{2}$$

Simplify the surd before dividing. Since $108=36\times3$, it follows that $\sqrt{108}=6\sqrt{3}$. Now, divide both parts of the numerator by the denominator:

$$$x=\frac{-10\pm6\sqrt{3}}{2}=-5\pm3\sqrt{3}$$ This result is in exact surd form, so no further rounding or decimal approximation is needed.

## Quadratics from geometry

In geometry questions, you often build the quadratic first and then solve it. For a right-angled triangle with sides $x+1$ and $x+4$, and hypotenuse $x+6$, Pythagoras gives:
$$
(x+1)^2+(x+4)^2=(x+6)^2
$$

Expand and collect terms to find the standard form: $x^2+2x+1+x^2+8x+16=x^2+12x+36$. This rearranges to the simplified equation:
$$
x^2-2x-19=0
$$

Using the quadratic formula, we solve for $x$:
$$
x=\frac{-(-2)\pm\sqrt{(-2)^2-4(1)(-19)}}{2(1)}=\frac{2\pm\sqrt{80}}{2}
$$
Since $\sqrt{80}=4\sqrt{5}$, this becomes $x=1\pm2\sqrt{5}$. Only $x=1+2\sqrt{5}$ is valid because lengths must be positive.

## Check yourself

1. If a quadratic has $b^2-4ac=0$, which statement is correct?

   - It has two different real roots

   - It has one repeated real root ✔

   - It has no real roots

   - The quadratic formula cannot be used

   _Explanation:_ When the discriminant is 0, the square-root term is 0, so the plus and minus cases give the same value. The common wrong choice is A, but $\pm 0$ does not make two different answers.

2. The calculator gives $x=1.380\ldots$ and $x=-1.630\ldots$ for $4x^2+x-9=0$. What are the answers to 3 significant figures?

   - $$1.38$ and $-1.63$ ✔

   - $$1.380$ and $-1.630$

   - $$1.4$ and $-1.6$

   - $$1.39$ and $-1.64$

   _Explanation:_ To 3 significant figures, keep 3 meaningful digits from the first non-zero digit, so the answers are $1.38$ and $-1.63$. The common wrong choice is C because it rounds to only 2 significant figures.

3. Solve $x^2+4x+1=0$ in simplest exact form.

   - $$x=-2\pm\sqrt{3}$ ✔

   - $$x=2\pm\sqrt{3}$

   - $$x=-4\pm\sqrt{12}$

   - $$x=-2\pm2\sqrt{3}$

   _Explanation:_ Using the formula gives $x=\frac{-4\pm\sqrt{16-4}}{2}=\frac{-4\pm\sqrt{12}}{2}=\frac{-4\pm2\sqrt{3}}{2}=-2\pm\sqrt{3}$. The common wrong choice is D because $\sqrt{12}=2\sqrt{3}$ is correct, but you must still divide the whole numerator by 2.

4. A geometry problem leads to $x=1\pm2\sqrt{5}$. Which value of $x$ should you keep for side lengths?

   - $$1+2\sqrt{5}$ ✔

   - $$1-2\sqrt{5}$

   - Both values

   - Neither value

   _Explanation:_ Side lengths must be positive, and $1-2\sqrt{5}$ is negative, so it would make some lengths impossible. The common wrong choice is C because algebraically both roots solve the equation, but the context rules one out.
