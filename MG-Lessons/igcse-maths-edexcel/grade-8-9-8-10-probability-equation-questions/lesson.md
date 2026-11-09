# grade-8-9-8-10-probability-equation-questions — lesson

_Lane: `igcse-maths-edexcel` · grade 8 · 6 content steps · 3 check questions (source: MathsGenie lessons)_

## Working backwards from a probability

![Probability tree for two draws without replacement from $x$ blue and $3$ red counters, highlighting the blue then blue path and the changing fractions on the second draw](../assets/001-aa1fc593-a71c-40aa-a1ed-88ca82a07749.jpeg)

Probability equation questions ask you to work backwards from a known probability to an unknown number of counters. A tree diagram like the one above helps you keep track of what changes after the first draw.

When two selections happen in order, multiply the probabilities along the path.

If the first counter is not put back, there is one fewer counter for the second draw. The denominator is $1$ smaller, and if the first counter was the colour you are following, that numerator is also $1$ smaller.

If the first counter is put back, the bag returns to its original contents before the second draw, so you use the same fraction again.

## Build the algebra first

Start by writing the number of each colour and the total in algebra. For example, 3 red and $x$ blue gives a total of $x + 3$, while a ratio of red to blue of $2:1$ can be written as red $= 2k$, blue $= k$, and total $= 3k$.

Then write the probability of the required path and set it equal to the given value. Two common setups are shown below: $$P(\text{blue then blue}) = \frac{x}{x+3} \times \frac{x-1}{x+2}$$

$$$P(\text{red then red}) = \left(\frac{4}{y+4}\right)^2$$ This setup is the bridge from the words to the algebra you solve.

## Worked example: with replacement

A bag contains 4 red counters and $y$ blue counters, so the total is $y+4$. A counter is chosen, replaced, then another is chosen, and the probability of getting two red counters is $\frac{4}{25}$. Because the counter is replaced, the probability of red is the same on both picks: $\frac{4}{y+4}$.

Set up the equation and take the positive square root:
$$\left(\frac{4}{y+4}\right)^2 = \frac{4}{25}$$
$$\frac{4}{y+4} = \frac{2}{5}$$
We use the positive root because a probability cannot be negative.

Now solve by cross-multiplying:
$$\begin{aligned} 20 &= 2(y+4) \\ 20 &= 2y + 8 \\ 12 &= 2y \\ y &= 6 \end{aligned}$$
So the bag contains 6 blue counters.

## Using ratios to form the equation

In ratio questions, turn the ratio into algebra before you do any probability calculations. If the ratio of red to blue is $2:1$, represent red as $2k$, blue as $k$, and the total count as $3k$.

For selecting two reds without replacement, the probability path is:
$$P(\text{red then red}) = \frac{2k}{3k} \times \frac{2k-1}{3k-1} = \frac{2}{3} \times \frac{2k-1}{3k-1}$$
Simplifying the first fraction early by cancelling the $k$ terms makes the resulting equation significantly easier to solve.

If this probability is given as $\frac{3}{7}$, we can solve for $k$ using cross-multiplication:
$$\begin{aligned} \frac{2}{3} \times \frac{2k-1}{3k-1} &= \frac{3}{7} \\ 14(2k-1) &= 9(3k-1) \\ 28k - 14 &= 27k - 9 \\ k &= 5 \end{aligned}$$
Because blue was represented by $k$, there are 5 blue counters in the set.

## Worked example: when a quadratic appears

A bag contains 3 red counters and $x$ blue counters. Two counters are chosen without replacement, and the probability of getting two blue counters is $\frac{5}{14}$. This gives the initial probability equation:
$$\frac{x}{x+3} \times \frac{x-1}{x+2} = \frac{5}{14}$$

To solve, multiply the algebraic fractions first, then cross-multiply to eliminate denominators.
$$\frac{x(x-1)}{(x+3)(x+2)} = \frac{5}{14}$$
$$14x(x-1) = 5(x+3)(x+2)$$
Now expand both sides of the equation to prepare for a quadratic setup.

After collecting terms on one side, the quadratic equation becomes simpler to solve.
$$\begin{aligned} 14x^2 - 14x &= 5x^2 + 25x + 30 \\ 9x^2 - 39x - 30 &= 0 \\ 3x^2 - 13x - 10 &= 0 \end{aligned}$$
Factoring gives $(3x + 2)(x - 5) = 0$, which yields $x = -\frac{2}{3}$ or $x = 5$.

Only one of these solutions is valid in the context of the problem. A number of counters cannot be negative or fractional, so the valid answer is $x = 5$.

## Exam technique and common checks

In a "show that" question, the method is still the same: write the probability path, form the equation, and then expand until the required quadratic appears. You usually earn method marks for this setup, so do not skip straight to the final line.

Before you finish, check that your answer is positive, sensible, and large enough for the bag described. If the question is about numbers of counters, a negative answer or a non-integer answer must be rejected.

## Check yourself

1. A bag has 5 red counters and $x$ blue counters. Two counters are chosen without replacement. Which expression gives $P(\text{blue then blue})$?

   - $$\frac{x}{x+5} \times \frac{x-1}{x+4}$ ✔

   - $$\frac{x}{x+5} \times \frac{x}{x+5}$

   - $$\frac{x}{x+5} \times \frac{x-1}{x+5}$

   - $$\frac{x}{x+4} \times \frac{x-1}{x+4}$

   _Explanation:_ A is correct because the first blue has probability $\frac{x}{x+5}$, then one blue is gone so the second blue has probability $\frac{x-1}{x+4}$. B is the most common wrong answer because it treats the question as with replacement and forgets that the bag has changed.

2. In the worked example, why do we keep $\frac{2}{5}$ and not $-\frac{2}{5}$ after taking square roots?

   - Because probabilities must be non-negative ✔

   - Because replacement makes the denominator stay the same

   - Because cross-multiplying removes negative answers

   - Because squared fractions only have one square root

   _Explanation:_ A is correct because $\frac{4}{y+4}$ represents a probability, so it cannot be negative. B is the most common wrong idea: replacement affects whether the fraction repeats, but it does not decide the sign of the square root.

3. Stretch: A bag has $n$ counters in total, 6 of them red and the rest blue. Solving the probability equation for two blue counters without replacement gives $n = 21$ or $n = 4$. Which value is valid?

   - $$n = 21$ ✔

   - $$n = 4$

   - Both values are valid

   - Neither value is valid

   _Explanation:_ $$n = 21$ is correct because the total number of counters must be at least 6 if there are already 6 red counters. The most common wrong answer is $n = 4$, but a bag cannot contain 6 red counters and only 4 counters altogether.
