# as-pure-mathematics-10-4-solving-trigonometric-equations — lesson

_Lane: `a-level-maths-edexcel` · grade — · 6 content steps · 3 check questions (source: MathsGenie lessons)_

## Why one trig equation can have several answers

![Graph of y = sin(x - 30°) and y = 0.3 showing two intersections between 0° and 360°](../assets/001-a51e57d6-20b7-4fdd-89ea-3312f1daacb3.jpeg)

A trigonometric equation can have several answers because sine, cosine, and tangent repeat. In this topic, angles are in degrees, so put your calculator in degree mode and always watch the stated solution interval.

Your calculator usually gives a principal value, but that is only a starting point. You then use the graph, quadrant symmetry, or the period of the function to find every other angle in the interval.

For example, solving $\sin(x - 30^{\circ}) = 0.3$ means finding where a horizontal line meets the shifted sine curve. Between $0^{\circ}$ and $360^{\circ}$, that intersection can happen more than once.

## Solve the inside angle first

![Unit circle with quadrants I to IV labelled and the positive quadrants for sine, cosine and tangent marked](../assets/002-4d8a8647-d3b1-4f60-a686-74a6535e7fb8.jpeg)

For equations like $\cos(2x + 10^\circ) = 0.4$, treat the whole inside angle as one object. Let $u = 2x + 10^\circ$, solve the trig equation in $u$, and only then convert back to $x$; the same method works for $2x$ or $3\theta - 20^\circ$.

You must convert the interval as well. If $0 \le x < 180^\circ$, then $u$ runs from $10^\circ$ up to but not including $370^\circ$.

Use the period and the correct quadrants to find all values of $u$. Sine and cosine repeat every $360^\circ$, while tangent repeats every $180^\circ$, and you should not divide by $2$ or $3$ until the end.

## Worked example: shifted cosine

Solve $\cos(2x + 10^\circ) = 0.4$ for $0 \le x < 180^\circ$. Let $u = 2x + 10^\circ$, so the interval becomes $10^\circ \le u < 370^\circ$.

$$u = 2x + 10^\circ$$

$$10^\circ \le u < 370^\circ$$

The principal value is $u \approx 66.4218^\circ$, since $u = \arccos(0.4)$. Cosine is positive in quadrants I and IV, so the other value in this interval is $u \approx 360^\circ - 66.4218^\circ = 293.5782^\circ$.

$$u = 66.4218^\circ \quad \text{or} \quad u = 293.5782^\circ$$

Now solve the two linear equations in $x$. This gives $x \approx 28.2109^\circ$ or $x \approx 141.7891^\circ$, so to one decimal place $x = 28.2^\circ$ or $x = 141.8^\circ$.

$$2x + 10^\circ = 66.4218^\circ \quad \text{or} \quad 2x + 10^\circ = 293.5782^\circ$$

$$x = 28.2^\circ \quad \text{or} \quad x = 141.8^\circ$$

## Tangent and squared trig

For tangent, the inside-angle method is the same, but the period is shorter. If $\tan u = -1.8$ and $-140^\circ \le u < 220^\circ$, the calculator gives $u \approx -60.9^\circ$, and adding $180^\circ$ gives the second value $u \approx 119.1^\circ$.

Squared trig functions need a positive and a negative branch after square-rooting. From $\tan^2 x = 5$ you must write $\tan x = \pm \sqrt{5}$, or you will miss half the solutions.

A quick check is to ask which quadrants match the sign. Positive tangent lives in quadrants I and III, while negative tangent lives in quadrants II and IV.

## Worked example: using an identity

Solve $3\sin^2 x = 5\cos x + 1$ for $0 \le x < 360^\circ$. Because the equation already contains $\cos x$, rewrite $\sin^2 x$ as $1 - \cos^2 x$ and make a quadratic in $\cos x$.

$$$3(1 - \cos^2 x) = 5\cos x + 1$$ $$3\cos^2 x + 5\cos x - 2 = 0$$

Factorise the quadratic before touching the trig part. You get $(3\cos x - 1)(\cos x + 2) = 0$, so $\cos x = \frac{1}{3}$ or $\cos x = -2$. $$\cos x = \frac{1}{3} \quad \text{or} \quad \cos x = -2$$

Now reject any impossible trig value. Since cosine must lie between $-1$ and $1$, $\cos x = -2$ is invalid, and $\cos x = \frac{1}{3}$ gives $x \approx 70.5^\circ$ or $x \approx 289.5^\circ$. $$x = 70.5^\circ \quad \text{or} \quad x = 289.5^\circ$$

## Factorise, do not divide away answers

Solve $2\tan x = 3\sin x$ for $0 \le x < 360^\circ$. Rewrite tangent as $\frac{\sin x}{\cos x}$ so that you can factorise instead of dividing by a trig expression.

$$$\frac{2\sin x}{\cos x} = 3\sin x$$ Multiply by $\cos x$ to clear the denominator. The original equation is undefined when $\cos x = 0$, so $90^\circ$ and $270^\circ$ are never answers.

Rearranging gives the factorised form below: $$2\sin x = 3\sin x \cos x$$ $$\sin x(2 - 3\cos x) = 0$$ Now solve both factors, not just one branch.

This gives $x = 0^\circ$, $48.2^\circ$, $180^\circ$, and $311.8^\circ$. Dividing by $\sin x$ at the start would have lost the two answers where $\sin x = 0$.

## Check yourself

1. Why can $\sin(x - 30^\circ) = 0.3$ have more than one solution in $0^\circ \le x < 360^\circ$?

   - Because sine repeats, so the graph of $\sin(x - 30^\circ)$ can meet $y = 0.3$ more than once ✔

   - Because sine has period $180^\circ$

   - Because the calculator gives two answers automatically

   - Because every sine equation has exactly four solutions

   _Explanation:_ A is correct because sine repeats every $360^\circ$, so the shifted sine curve can cross the horizontal line more than once in one full turn. A common wrong answer is B: $180^\circ$ is the period of tangent, not sine.

2. If $\tan u = -1.8$ and $-140^\circ \le u < 220^\circ$, which are all the solutions for $u$?

   - $$u = -60.9^\circ$ and $u = 119.1^\circ$ ✔

   - $$u = -60.9^\circ$ and $u = 299.1^\circ$

   - $$u = 60.9^\circ$ and $u = 119.1^\circ$

   - $$u = -60.9^\circ$ only

   _Explanation:_ A is correct because tangent repeats every $180^\circ$, so starting from $-60.9^\circ$ you add $180^\circ$ to get $119.1^\circ$. A common wrong answer is B: adding $360^\circ$ uses the period of sine or cosine, not tangent.

3. Why is dividing both sides of $2\tan x = 3\sin x$ by $\sin x$ dangerous?

   - It changes degrees to radians

   - It removes the solutions where $\sin x = 0$ ✔

   - It makes tangent undefined for all $x$

   - It forces cosine to be positive

   _Explanation:_ Dividing by $\sin x$ assumes $\sin x \ne 0$, so you lose the solutions where $\sin x = 0$. A common wrong answer is C: tangent is only undefined when $\cos x = 0$, not for every angle. Hint: Ask yourself what happens if the thing you divide by could be zero.
