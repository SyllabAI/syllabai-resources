# grade-5-5-8-simultaneous-equations — lesson

_Lane: `igcse-maths-edexcel` · grade 5 · 6 content steps · 4 check questions (source: MathsGenie lessons)_

## What a simultaneous solution means

![Graph of the lines 2x + y = 7 and x - y = -1 crossing at the solution point (2, 3)](../assets/001-1794111f-10e7-4b2c-a4ce-238347aad9fb.jpeg)

Each linear equation is a straight line, and the simultaneous solution is the point where the lines cross. A solution pair must make both equations true at the same time.

For the graph shown, the lines $2x + y = 7$ and $x - y = -1$ meet at $(2, 3)$. That means $x = 2$ and $y = 3$ satisfy both equations together.

You can also check a claimed solution by substitution. If the left side equals the right side in both equations, the pair is correct.

## Elimination by adding

If the coefficients match and the signs are opposite, add the equations to eliminate that variable. In this example, the $y$ terms are $+3y$ and $-3y$.
$$
\begin{aligned}
4x+3y&=26 \quad \text{(1)}\\
x-3y&=-1 \quad \text{(2)}
\end{aligned}
$$

Add equation (1) and equation (2) term by term. The $y$ terms cancel, leaving one equation in $x$.
$$
\begin{aligned}
5x&=25\\
x&=5
\end{aligned}
$$

Substitute $x=5$ into equation (2) to find $y$. Then solve and write the answer as an ordered pair.
$$
\begin{aligned}
5-3y&=-1\\
-3y&=-6\\
y&=2
\end{aligned}
$$
So the solution is $(5,2)$.

## Elimination by subtracting

If the matching terms have the same sign, subtract one equation from the other. Here both equations contain $2x$, so subtracting removes $x$.

$$
\begin{aligned}
2x+5y&=28 \quad \text{(1)}\\
2x-y&=4 \quad \text{(2)}
\end{aligned}
$$

Be careful with negatives when you subtract. Since $5y-(-y)=6y$, we get the following simplified equation:

$$
\begin{aligned}
(2x+5y)-(2x-y)&=28-4\\
6y&=24\\
y&=4
\end{aligned}
$$

Now substitute $y=4$ into the original equation $2x-y=4$. This calculation gives $2x-4=4$, so $2x=8$ and $x=4$, resulting in the solution $(4,4)$.

## Making coefficients match first

Sometimes no variable cancels straight away, so you first scale an entire equation. For $2x-3y=4$ and $4x-y=18$, doubling the first equation makes the $x$ coefficients equal, and every term must be doubled.

$$$
\begin{aligned}
2x-3y&=4\\
4x-y&=18\\
4x-6y&=8
\end{aligned}
$$

Now subtract $4x-y=18$ from $4x-6y=8$. This gives $-5y=-10$, so $y=2$.
$$
\begin{aligned}
(4x-6y)-(4x-y)&=8-18\\
-5y&=-10
\end{aligned}
$$

Substitute $y=2$ into $4x-y=18$. Then $4x-2=18$, so $4x=20$, $x=5$, and the solution is $(5,2)$.

## Rearranged equations and decimals

Not every question starts in standard form. For example, $3x=10+y$ becomes $3x-y=10$ after subtracting $y$ from both sides.
$$
3x-y=10
$$

Decimals do not change the method. If it helps, multiply a whole equation by $10$ to clear one decimal place and make the numbers easier to handle.

In $6x+5y=6.5$ and $3x-2y=5.5$, doubling the second equation gives $6x-4y=11$. Subtracting then gives $9y=-4.5$, so $y=-0.5$, and substituting back gives $x=1.5$.
$$
\begin{aligned}
6x-4y&=11\\
9y&=-4.5
\end{aligned}
$$

## Turning words into equations

In word problems, define the variables before you do any algebra. Let $d$ be the price of one drink in pence and $b$ be the price of one biscuit in pence.

Two drinks and five biscuits cost £8.90, and one drink and three biscuits cost £4.95. Converting the totals to pence gives the following system of equations:

$$$
\begin{aligned}
2d+5b&=890\\
d+3b&=495
\end{aligned}
$$

Double the second equation to get $2d+6b=990$, then subtract the first equation to find $b=100$. Next, substitute back to get $d=195$. Because the equations used pence, convert the final answers back to £1.95 and £1.00.

## Check yourself

1. What does the solution to a pair of simultaneous equations represent?

   - the pair of values that makes both equations true ✔

   - any pair of values that works in one equation only

   - the $x$-intercept of either line

   - the coefficient of the larger variable

   _Explanation:_ A solution must satisfy both equations at once. The common wrong answer is B, but a pair that works in only one equation lies on just one line, not at the intersection of both.

2. When you simplify $(2x+5y)-(2x-y)$, what is the result?

   - $$6y$ ✔

   - $$4y$

   - $$0$

   - $$2y$

   _Explanation:_ Subtracting the second bracket changes its signs, so $5y-(-y)=5y+y=6y$. The common wrong answer is B, which comes from forgetting that subtracting a negative is the same as adding.

3. For the equations $6x+5y=6.5$ and $3x-2y=5.5$, which first step makes elimination easiest?

   - multiply the second equation by $2$ ✔

   - add the equations immediately

   - multiply only the $3x$ term by $2$

   - change $6.5$ to $65$ but leave the rest unchanged

   _Explanation:_ Doubling the whole second equation gives matching $x$ coefficients, $6x$ and $6x$, so elimination is straightforward. The common wrong answer is C, but you must multiply every term in an equation, not just one term.

4. Solve $2x+y=7$ and $3x=1+y$. Which ordered pair is correct?

   - $$(1.6,3.8)$ ✔

   - $$(3.8,1.6)$

   - $$(2,3)$

   - $$(1.6,2.2)$

   _Explanation:_ Rearrange $3x=1+y$ to $3x-y=1$, then add it to $2x+y=7$ to get $5x=8$, so $x=1.6$. Substituting back gives $y=3.8$, so the answer is $(1.6,3.8)$. The common wrong answer is B, which simply swaps the order; ordered pairs are written as $(x,y)$, not $(y,x)$.
