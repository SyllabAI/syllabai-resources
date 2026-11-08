# grade-8-9-8-11-probability-equation-questions — lesson

_Lane: `gcse-maths-edexcel` · grade 8 · 5 content steps · 3 check questions (source: MathsGenie lessons)_

## Turning words into equations

![Probability trees comparing blue then blue with replacement and without replacement from a bag with 3 red and x blue counters](../assets/001-69233fea-04e4-485a-9e20-986060ea2b74.jpeg)
Probability equation questions turn words about counters into algebra. The challenge is usually not the multiplying, but writing the correct fractions before you solve.

Each fraction is "favourable over total". If a question says "both blue", treat it as two events in a row and multiply using the following multiplication rule:

$$$P(A \text{ and } B)=P(A)\times P(B \text{ after } A)$$

With replacement, the bag resets before the second pick, so the two fractions can be the same. Without replacement, the total drops by 1, and the colour count may also drop by 1.

## Worked example: with replacement

A bag contains 6 red counters and $y$ blue counters. A counter is chosen, replaced, and then another counter is chosen, and the probability of two reds is $\frac{9}{64}$.

Because the counter is replaced, the total number of counters is still $6+y$ on the second pick. That means the probability of picking a red counter is the same both times.
$$\left(\frac{6}{6+y}\right)^2=\frac{9}{64}$$

Take the positive square root of both sides, as a probability and a number of counters cannot be negative. This gives the following simplified equation:
$$\frac{6}{6+y}=\frac{3}{8}$$

Now solve the linear equation by cross-multiplying and isolating the variable. This shows that there are 10 blue counters in total.
$$48=18+3y$$
$$30=3y$$
$$y=10$$

## Worked example: without replacement

A bag contains 3 red counters and $x$ blue counters. Two counters are taken without replacement, and the probability that both are blue is $\frac{5}{14}$. The first blue probability is $\frac{x}{x+3}$. If the first counter was blue, the second blue probability is $\frac{x-1}{x+2}$.

Set up the equation and clear the fractions to eliminate the denominators:
$$\frac{x}{x+3}\times \frac{x-1}{x+2}=\frac{5}{14}$$
$$14x(x-1)=5(x+3)(x+2)$$

Expand and simplify the resulting terms to form a quadratic equation equal to zero:
$$14x^2-14x=5x^2+25x+30$$
$$9x^2-39x-30=0$$
$$3x^2-13x-10=0$$

Factorise the quadratic as $(3x+2)(x-5)=0$. This gives roots $x=5$ or $x=-\frac{2}{3}$. We reject $x=-\frac{2}{3}$ because the number of counters must be a positive whole number.

## Using a ratio

A ratio gives relative sizes, not exact numbers. If red:blue = $3:2$, write the numbers as $3k$ and $2k$, so the total is $5k$.

Suppose two counters are taken without replacement and $P(\text{both blue})=\frac{14}{95}$. The first blue probability is $\frac{2k}{5k}=\frac{2}{5}$, and the second is $\frac{2k-1}{5k-1}$.

$$$\frac{2}{5}\times \frac{2k-1}{5k-1}=\frac{14}{95}$$

Cross-multiplying gives $190(2k-1)=70(5k-1)$, so $380k-190=350k-70$ and $k=4$. The total number of counters is $5k=20$. The ratio only gave the pattern, and $k$ turned it into actual numbers.

## Show that, then solve

Some exam questions ask you to show a quadratic before solving it. Start from the probability statement and simplify step by step, rather than trying to guess the equation.

If there are $n$ counters in total, 6 are red and the rest are blue, then the number of blue counters is $n-6$. Based on this, we set up the probability equation:
$$\frac{n-6}{n}\times \frac{n-7}{n-1}=\frac{1}{2}$$

Clear the fractions and expand the brackets to simplify the expression into a standard quadratic form:
$$2(n-6)(n-7)=n(n-1)$$
$$2n^2-26n+84=n^2-n$$
$$n^2-25n+84=0$$

Factorise the quadratic equation to find the solutions: $$(n-21)(n-4)=0$$ Only $n=21$ is valid, because $n=4$ would mean fewer total counters than the 6 red counters already in the bag. This final check turns an algebra answer into a sensible probability answer.

## Check yourself

1. A bag has 3 red counters and $x$ blue counters. Two counters are taken without replacement. What is the probability that both are blue?

   - $$\frac{x}{x+3}\times \frac{x-1}{x+2}$ ✔

   - $$\frac{x}{x+3}\times \frac{x}{x+3}$

   - $$\frac{x}{x+3}\times \frac{x-1}{x+3}$

   - $$\frac{x-1}{x+2}$

   _Explanation:_ After one blue counter is removed, there are $x-1$ blue counters left out of a total of $x+2$ counters remaining in the bag. The probability of picking the first blue counter is $\frac{x}{x+3}$. The probability of picking a second blue counter is $\frac{x-1}{x+2}$. Multiplying these gives the total probability for both being blue.

2. After writing $\frac{x}{x+3}\times \frac{x-1}{x+2}=\frac{5}{14}$, which equation comes next when you clear the fractions?

   - $$14x(x-1)=5(x+3)(x+2)$ ✔

   - $$14x(x+3)=5(x-1)(x+2)$

   - $$14(x-1)=5(x+3)(x+2)$

   - $$14x(x-1)=5(x+2)$

   _Explanation:_ A is correct because multiplying both sides by $14(x+3)(x+2)$ removes every denominator. The most common wrong answer is B, which cross-multiplies diagonally instead of clearing all the fractions in the whole equation.

3. The equation $n^2-25n+84=0$ gives $n=21$ or $n=4$. Which statement is correct in the bag problem with 6 red counters?

   - Both are valid because they solve the quadratic.

   - Only $n=21$ is valid because $n=4$ gives fewer total counters than the 6 red counters. ✔

   - Only $n=4$ is valid because smaller numbers are more likely in probability.

   - Neither is valid because probability equations cannot lead to quadratics.

   _Explanation:_ B is correct because a solution must fit the context as well as the algebra. The most common wrong answer is A, which forgets that probability questions need sensible counting answers, not just roots of an equation.
