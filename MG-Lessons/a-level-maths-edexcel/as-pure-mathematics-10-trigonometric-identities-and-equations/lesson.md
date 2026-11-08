# as-pure-mathematics-10-trigonometric-identities-and-equations — lesson

_Lane: `a-level-maths-edexcel` · grade — · 7 content steps · 3 check questions (source: MathsGenie lessons)_

## Angles, periods and reference angles

![Unit circle on x-y axes with quadrants labelled by CAST, a reference angle in Quadrant I, and signs for sine, cosine and tangent](../assets/001-9e7ccf7c-a31b-4d53-8d9c-221a50817764.jpeg)

In AS questions, trigonometric equations are usually solved in degrees, so check your calculator is in degree mode first. The unit circle shows why one trig value can match more than one angle in a full turn.

Sine and cosine repeat every $360^{\circ}$, while tangent repeats every $180^{\circ}$. This repeating length is called the period, and it tells you how many solutions can appear in an interval.

A reference angle is the acute angle between the terminal side and the x-axis. Use CAST to decide which quadrants have the correct sign: all in I, sine in II, tangent in III, cosine in IV.

## Composite angles and transformed intervals

![Graph of y equals sin x and y equals sin(x minus 30 degrees) from 0 to 360 degrees, showing the second curve shifted right](../assets/002-a4c3f39f-3acc-44c6-838c-43f8c7ccb6c8.jpeg)

The graph of $y = \sin(x - 30)$ is the graph of $y = \sin x$ shifted $30^\circ$ to the right. This is a useful check that changing the argument changes where solutions appear, not the shape of the curve.

When the angle inside the trig function is something like $3\theta - 20$, solve it by setting a new variable such as $u = 3\theta - 20$. This turns the problem into a standard equation in $u$, but only after you change the interval as well.

For $0^\circ \leq \theta < 180^\circ$, the substitution $u = 3\theta - 20$ gives $-20^\circ \leq u < 520^\circ$. Inverse sine, cosine, or tangent gives only one principal angle, so you must then use symmetry and periodicity to find the rest.

## Worked example: solving a composite-angle equation

To solve $\sin(3\theta - 20) = 0.7$, let $u = 3\theta - 20$. Because $0^\circ \leq \theta < 180^\circ$, the new interval is $-20^\circ \leq u < 520^\circ$.

Now find the reference angle:
$$\alpha = \sin^{-1}(0.7) = 44.43^\circ$$
Sine is positive in Quadrants I and II, so $u = 44.43^\circ$ or $135.57^\circ$, and adding $360^\circ$ gives the extra values $404.43^\circ$ and $495.57^\circ$ that also lie in the interval.

Undo the substitution using $\theta = \frac{u + 20}{3}$. This gives
$$\theta = 21.48^\circ,\ 51.86^\circ,\ 141.48^\circ,\ 171.86^\circ$$

A quick check shows all four answers lie in $0^\circ \leq \theta < 180^\circ$. The stretched interval explains why there are four solutions rather than two.

## Using identities to make a quadratic

If an equation mixes $\sin^2 x$ with $\cos x$, use $\sin^2 x \equiv 1 - \cos^2 x$ to write everything in one trig function. That often turns the problem into an ordinary quadratic.

For $3\sin^2 x = 4\cos x + 2$, substitute: $$3(1 - \cos^2 x) = 4\cos x + 2$$ After simplifying and multiplying by $-1$, this becomes $$3\cos^2 x + 4\cos x - 1 = 0$$.

This quadratic does not factor nicely, so use the quadratic formula. Let $u = \cos x$. Then $$3u^2 + 4u - 1 = 0$$ and $$u = \frac{-4 \pm \sqrt{4^2 - 4(3)(-1)}}{2\cdot 3} = \frac{-2 \pm \sqrt{7}}{3}$$.

So $\cos x = \frac{-2 + \sqrt{7}}{3}$ or $\cos x = \frac{-2 - \sqrt{7}}{3}$. The second value is outside $[-1,1]$, so it is rejected because cosine must lie between $-1$ and $1$. Hence, for $0^\circ \le x < 360^\circ$, $$x \approx 77.6^\circ,\ 282.4^\circ$$.

## Tangent equations and lost solutions

When tangent appears, rewrite it as $\tan x \equiv \frac{\sin x}{\cos x}$. Remember that $\tan x$ is undefined when $\cos x = 0$, so those angles can never be solutions of the original equation.

For $3\tan x = 5\sin x$, write $$3\cdot \frac{\sin x}{\cos x} = 5\sin x$$ and multiply by $\cos x$ to get $$3\sin x = 5\sin x\cos x$$

Then factorise: $$\sin x(3 - 5\cos x) = 0$$ Now solve each factor: $\sin x = 0$ or $\cos x = \frac{3}{5}$. In $0^\circ \leq x < 360^\circ$, the solutions are $0^\circ,\ 53.1^\circ,\ 180^\circ,\ 306.9^\circ$, and they all satisfy the original equation.

Do not divide both sides by $\sin x$ at the start. That shortcut would lose the valid solutions $x = 0^\circ$ and $x = 180^\circ$.

## Squared equations in tangent

If you see a squared trig equation such as $\tan^2(2x) = 3$, take the square root carefully. This means you must consider both the positive and negative roots: $\tan(2x) = \sqrt{3}$ or $\tan(2x) = -\sqrt{3}$.

Let $u = 2x$, so the interval $0^\circ \leq x < 180^\circ$ becomes $0^\circ \leq u < 360^\circ$. Evaluating both cases, tangent equals $\pm\sqrt{3}$ at the reference angles $u = 60^\circ, 120^\circ, 240^\circ, 300^\circ$ within that range.

Divide each value of $u$ by 2 to return to the original variable $x$. The resulting solutions for the equation are $30^\circ, 60^\circ, 120^\circ, 150^\circ$.

## Proving an identity by simplifying one side

To prove an identity, start with the more complicated side and simplify it until it matches the other side. Do not work from both sides at once, and do not assume the result you want.

For the expression $$\frac{3\sin x - \cos^2 x + 1}{3 + \sin x}$$ replace $\cos^2 x$ with $1 - \sin^2 x$ to rewrite the numerator. This substitution allows the expression to be simplified as follows: $$\frac{3\sin x - (1 - \sin^2 x) + 1}{3 + \sin x} = \frac{3\sin x + \sin^2 x}{3 + \sin x}$$

Now factor the numerator to reveal common terms: $$\frac{\sin x(3 + \sin x)}{3 + \sin x}$$ Since $\sin x$ lies between $-1$ and $1$, the denominator $3 + \sin x$ can never be zero. The cancellation is valid, so the expression simplifies to $\sin x$.

## Check yourself

1. Why does $\cos x = 0.4$ have two solutions in $0^\circ \leq x < 360^\circ$?

   - Cosine is positive in Quadrants I and IV ✔

   - Cosine is positive in Quadrants II and III

   - Cosine has period $180^\circ$

   - $$\cos^{-1}(0.4)$ automatically gives both answers

   _Explanation:_ Cosine is positive in Quadrants I and IV, so the same reference angle appears twice between $0^\circ$ and $360^\circ$. The common wrong answer is C, but $180^\circ$ is the period of tangent, not cosine, so cosine does not repeat halfway round the circle.

2. After using $\sin^2 x \equiv 1 - \cos^2 x$, which quadratic is equivalent to $3\sin^2 x = 4\cos x + 2$?

   - $$3\cos^2 x + 4\cos x - 1 = 0$ ✔

   - $$3\cos^2 x - 4\cos x - 1 = 0$

   - $$3\cos^2 x + 4\cos x + 1 = 0$

   - $$3\sin^2 x - 4\cos x - 2 = 0$

   _Explanation:_ Substituting $\sin^2 x = 1 - \cos^2 x$ gives $3(1 - \cos^2 x) = 4\cos x + 2$, which simplifies to $3 - 3\cos^2 x = 4\cos x + 2$. Rearranging all terms to one side gives $-3\cos^2 x - 4\cos x + 1 = 0$, or $3\cos^2 x + 4\cos x - 1 = 0$ after multiplying by $-1$.

3. Solve $\tan^2(2x) = 3$ for $0^\circ \leq x < 180^\circ$.

   - $$x = 30^\circ,\ 60^\circ,\ 120^\circ,\ 150^\circ$ ✔

   - $$x = 30^\circ,\ 60^\circ$

   - $$x = 60^\circ,\ 120^\circ,\ 240^\circ,\ 300^\circ$

   - $$x = 15^\circ,\ 45^\circ,\ 75^\circ,\ 105^\circ$

   _Explanation:_ Because $\tan^2(2x) = 3$ means $\tan(2x) = \pm\sqrt{3}$, there are four angles for $2x$ in $0^\circ \leq 2x < 360^\circ$: $60^\circ,\ 120^\circ,\ 240^\circ,\ 300^\circ$. The common wrong answer is C, which forgets the final step of dividing by 2 to return from $2x$ to $x$.
