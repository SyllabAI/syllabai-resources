# grade-7-7-10-iteration — lesson

_Lane: `gcse-maths-edexcel` · grade 7 · 7 content steps · 4 check questions (source: MathsGenie lessons)_

## Reading iteration notation

Iteration means repeatedly applying the same rule. In $x_{n+1}=2+\frac{6}{x_n^2}$, $x_n$ is the current value and $x_{n+1}$ is the next value.

A subscript is not a power, so $x_3$ means the term with subscript $3$, not $x^3$. The first given value is called the starting value, usually $x_0$ or $P_0$.

Each use of the rule moves one step along the sequence: $x_0 \to x_1 \to x_2 \to x_3$. Always substitute the latest value back into the formula.

## Worked example: a changing population

Start with the given value $P_0=180$ and the rule $P_{t+1}=1.10(P_t-12)$. To find $P_1$, substitute $P_0$ into the formula once.

$$$P_1=1.10(180-12)=184.8$$

Now use $P_1$, not $P_0$, to find the next term. Reusing the starting value each time is a very common mistake.

$$$P_2=1.10(184.8-12)=190.08$$

One more substitution gives the third new value. If a whole number is needed, round only at the end.

$$$P_3=1.10(190.08-12)=195.888 \approx 196$$

## Using an algebraic iteration formula

Use $x_{n+1}=2+\frac{6}{x_n^2}$ with $x_0=2$. Each time, type the previous answer back into the same rule. $$x_1=2+\frac{6}{2^2}=3.5$$

For the second step, use $x_1=3.5$. Keep the full calculator value so later answers stay accurate. $$x_2=2+\frac{6}{3.5^2}=2.489795918\ldots$$

Now substitute the full value of $x_2$ to get $x_3$. To $3$ d.p., the third value is $2.968$. $$x_3=2+\frac{6}{2.489795918\ldots^2}=2.967884977\ldots$$

## Convergence and solution estimates

![Graph of y = 2/(x^2 + 4) and y = x with cobweb steps from x0 = 0 to x3, showing convergence to a fixed point](../assets/001-09deec3b-659c-4074-bdc5-a1bdec9abf64.jpeg)

This graph shows the iteration $x_{n+1}=\frac{2}{x_n^2+4}$ starting from $x_0=0$. The arrows move between the curve and the line $y=x$, and the steps settle near one value.

The first two values are easy to calculate from the formula. They are already quite close together.
$$x_1=\frac{2}{0^2+4}=0.5$$
$$x_2=\frac{2}{0.5^2+4}=0.470588235\ldots$$

One more step gives the next estimate. Since the values are getting closer together, the sequence converges and the solution estimate is $x \approx 0.474$.
$$x_3=\frac{2}{0.470588235\ldots^2+4}=0.473770491\ldots$$

## From fixed point to equation

If the sequence converges to a value $a$, then both the current term and the next term are close to $a$. So at the fixed point we set $x_n=a$ and $x_{n+1}=a$.

For $x_{n+1}=\frac{2}{x_n^2+4}$, this gives $$a=\frac{2}{a^2+4}$$

Multiply by $a^2+4$ and rearrange to get $$a^3+4a-2=0$$

So the limiting value of the iteration is a root of $x^3+4x-2=0$. This is the key link between an iteration formula and the equation it solves.

## Showing a root is in an interval

![Graph of y = x^3 + 5x - 2 with points at x = 0 and x = 1 labelled f(0) = -2 and f(1) = 4, showing the curve crossing the x-axis between 0 and 1](../assets/002-fac07a4c-2d59-46fd-83b8-e1dcdc8223d9.jpeg)

To show a root lies in an interval, write the equation as $f(x)=0$ and test the endpoints. For a continuous graph, opposite signs mean the curve crosses the x-axis somewhere in between.

For $f(x)=x^3+5x-2$, we calculate the function values at the boundaries of the interval $[0, 1]$:
$$f(0)=-2$$
$$f(1)=4$$

Because $-2$ and $4$ have opposite signs and this graph is continuous, there is a root between $0$ and $1$. This proves the root is in the interval, even though it does not give the exact value. Iteration can then be used to improve the estimate.

## Rearranging into an iteration formula

Sometimes the equation is given first and you must rearrange it into the form $x=\text{expression in }x$. Then change the left side to $x_{n+1}$ and every $x$ on the right to $x_n$.

From $x^3+5x=2$, rearrange step by step. So the iteration formula follows directly from the rearranged equation.
$$5x=2-x^3$$
$$x=\frac{2}{5}-\frac{x^3}{5}$$
$$x_{n+1}=\frac{2}{5}-\frac{x_n^3}{5}$$

With $x_0=0$, the first two values are found by substitution. Keep $x_{n+1}$ on the left and only $x_n$ terms on the right.
$$x_1=\frac{2}{5}-\frac{0^3}{5}=0.4$$
$$x_2=\frac{2}{5}-\frac{0.4^3}{5}=0.3872$$

## Check yourself

1. What does $x_3$ mean?

   - the term with subscript $3$ ✔

   - $$x$ cubed

   - $$3x$

   - the starting value

   _Explanation:_ A is correct because the $3$ is a subscript that labels which term you mean. The common wrong answer B is wrong because $x^3$ is a power written high up, not a subscript written low down.

2. Using $x_{n+1}=2+\frac{6}{x_n^2}$ with $x_0=2$, what is $x_3$ to $3$ d.p.?

   - $$2.968$ ✔

   - $$2.490$

   - $$3.500$

   - $$2.967$

   _Explanation:_ A is correct because three substitutions from $x_0$ give $x_1=3.5$, $x_2=2.489795918\ldots$ and $x_3=2.967884977\ldots$, which rounds to $2.968$. The common wrong answer B is actually $x_2$, so it comes from stopping one step too early.

3. Stretch: If an iteration is $x_{n+1}=3-\frac{5}{x_n}$ and it converges to $a$, which equation must $a$ satisfy?

   - $$a^2-3a+5=0$ ✔

   - $$a^2-3a-5=0$

   - $$a-3+5=0$

   - $$3a-5=0$

   _Explanation:_ A is correct because at convergence you set $a=3-\frac{5}{a}$, then multiply by $a$ to get $a^2=3a-5$, so $a^2-3a+5=0$. The common wrong answer B comes from changing the sign of the $5$ incorrectly when rearranging.

4. Which statement is enough to show that $x^3+5x-2=0$ has a root between $0$ and $1$?

   - $$f(0)=-2$ and $f(1)=4$ ✔

   - $$f(0)=-2$ and $f(1)=-4$

   - $$f(0)=2$ and $f(1)=4$

   - $$f(0)=0$ and $f(1)=4$

   _Explanation:_ A is correct because the endpoint values have opposite signs, so there is a sign change on a continuous graph. The common wrong answer D only shows a root at the endpoint $x=0$, not strictly between $0$ and $1$.
