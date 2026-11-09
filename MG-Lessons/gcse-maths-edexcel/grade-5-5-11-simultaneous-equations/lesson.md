# grade-5-5-11-simultaneous-equations — lesson

_Lane: `gcse-maths-edexcel` · grade 5 · 6 content steps · 3 check questions (source: MathsGenie lessons)_

## What a solution means

![Graph of the lines 3x+2y=18 and 5x-2y=14 intersecting at (4,3) with axes labelled](../assets/001-67d126d4-a25c-44f0-8b32-1309a471aae3.jpeg)

On a graph, each equation is represented as a line. The solution to simultaneous equations is the point where the two lines intersect, because that point lies on both lines.

A pair of simultaneous equations usually has two unknowns, such as $x$ and $y$. A solution is one pair of values that makes both equations true at the same time.

You can check a proposed solution by substituting it into each equation. If it works in only one equation, it is not the solution to the system.

## Elimination by adding or subtracting

Elimination removes one variable so you can solve a simpler equation with one unknown. Look at the coefficients, which are the numbers in front of the same variable in each equation.

If the coefficients are the same size and opposite signs, add the equations. If the coefficients are the same size and the same sign, subtract one equation from the other.

For example,
$$
\begin{aligned}
3x+2y&=18 \\
5x-2y&=14
\end{aligned}
$$
has $+2y$ and $-2y$, so adding will cancel the $y$ terms. That is exactly what we want.

## Worked example: add to eliminate

Solve this pair of simultaneous equations.
$$
\begin{aligned}
3x+2y&=18 \\
5x-2y&=14
\end{aligned}
$$
The $y$ coefficients are opposites, so add the equations to eliminate $y$.

Add left sides and right sides carefully. This leaves a one-variable equation.
$$
\begin{aligned}
3x+2y+5x-2y&=18+14 \\
8x&=32 \\
x&=4
\end{aligned}
$$

Now substitute $x=4$ into one original equation. Solve the result to find $y$.
$$
\begin{aligned}
3(4)+2y&=18 \\
12+2y&=18 \\
2y&=6 \\
y&=3
\end{aligned}
$$

So the solution is $x=4,\ y=3$. A quick check in the second equation gives $5(4)-2(3)=14$, so the pair works in both equations.

## If nothing cancels yet, multiply first

Sometimes no coefficients match, so make a match before eliminating. In
$$
\begin{aligned}
2x+y&=11 \\
5x+2y&=26
\end{aligned}
$$
the $y$ coefficients are 1 and 2, so multiply the first equation by 2.

Multiplying the whole equation by 2 gives
$$
\begin{aligned}
4x+2y&=22 \\
5x+2y&=26
\end{aligned}
$$
Now the $y$ terms have the same sign, so subtract the first new equation from the second.

Subtract to solve for $x$, then substitute back. This removes $y$ completely.
$$
\begin{aligned}
(5x+2y)-(4x+2y)&=26-22 \\
x&=4
\end{aligned}
$$

Using $2x+y=11$ gives
$$
\begin{aligned}
2(4)+y&=11 \\
8+y&=11 \\
y&=3
\end{aligned}
$$
Always multiply every term, including the number on the right-hand side.

## Rearrange first if needed

Not every pair starts in standard form. For example, consider this system:
$$
\begin{aligned}
3x&=12+y \\
x+4y&=19
\end{aligned}
$$
First, rearrange the top equation to $3x-y=12$.

After rearranging, the system is ready for the elimination method:
$$
\begin{aligned}
3x-y&=12 \\
x+4y&=19
\end{aligned}
$$
Multiply the first equation by 4 so the $y$ terms become opposites.

Then add the equations to eliminate the $y$ variable.
$$
\begin{aligned}
12x-4y&=48 \\
x+4y&=19 \\
13x&=67
\end{aligned}
$$
Solving this equation gives $x=\frac{67}{13}$.

Substitute into $x+4y=19$ to find $y$.
$$
\begin{aligned}
\frac{67}{13}+4y&=19 \\
4y&=\frac{180}{13} \\
y&=\frac{45}{13}
\end{aligned}
$$
Fractions can be perfectly correct answers in simultaneous equations; do not assume you made a mistake just because the result is not an integer.

## Turning words into equations

In a word problem, choose letters first and keep their meaning fixed. Let $s$ be the price of one sandwich and $d$ be the price of one drink. If two sandwiches and three drinks cost £14.70, and one sandwich and two drinks cost £8.70, we can represent the situation with these equations:

$$$
\begin{aligned}
2s+3d&=14.70 \\
s+2d&=8.70
\end{aligned}
$$
Now solve the pair just like any other simultaneous equations question. Start by multiplying the second equation by 2 so that the coefficients of $s$ match.

$$$
\begin{aligned}
2s+4d&=17.40 \\
(2s+4d)-(2s+3d)&=17.40-14.70 \\
d&=2.70
\end{aligned}
$$
Once you have found $d=2.70$, substitute this value back into the equation $s+2d=8.70$ to find the price of a sandwich.

$$$
\begin{aligned}
s+2(2.70)&=8.70 \\
s+5.40&=8.70 \\
s&=3.30
\end{aligned}
$$
Final results show that one sandwich costs £3.30 and one drink costs £2.70. Always ensure your final answer relates back to the original context of the problem.

## Check yourself

1. Which statement best describes a correct solution to simultaneous equations?

   - It makes both equations true ✔

   - It makes at least one equation true

   - It makes the left sides of the equations equal to each other

   - It always gives whole numbers

   _Explanation:_ A solution must satisfy every equation in the pair, so both equations become true with the same values. The common wrong answer "at least one equation" is not enough, because many pairs work for one equation only.

2. When you multiply $2x+y=11$ by 2, which new equation is correct?

   - $$4x+2y=22$ ✔

   - $$4x+2y=11$

   - $$2x+2y=22$

   - $$4x+y=22$

   _Explanation:_ Doubling an equation means every term on both sides is doubled, so the correct result is $4x+2y=22$. The common wrong answer $4x+2y=11$ forgets to double the right-hand side.

3. Let $a$ be adult ticket price and $c$ be child ticket price. Which equation matches "3 adults and 2 children cost £28"?

   - $$3a+2c=28$ ✔

   - $$2a+3c=28$

   - $$a+c=28$

   - $$3ac=28$

   _Explanation:_ $$3a$ means 3 adult tickets and $2c$ means 2 child tickets, so together they total 28. The common wrong answer $2a+3c=28$ swaps the coefficients, which changes the meaning of the sentence.
