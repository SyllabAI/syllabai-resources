# grade-4-4-18-probability — lesson

_Lane: `igcse-maths-edexcel` · grade 4 · 6 content steps · 3 check questions (source: MathsGenie lessons)_

## Probability on a scale

![Probability scale from 0 impossible to 1 certain with even chance at 0.5 and a point marked 0.82 for seed grows](../assets/001-7cff17ec-be39-4ca6-b483-2bd8ffabfd50.jpeg)
Probability measures how likely an event is to happen. It is written as a number from $0$ to $1$, where $0$ means impossible and $1$ means certain.

An outcome is one possible result, such as rolling a $6$. An event is the result we care about, such as "rolling an even number".

A probability of $0.82$ means the event is likely because it is above $0.5$. It is not guaranteed, because only probability $1$ means certain.

## Complete sets add to 1

If a list contains every possible outcome and exactly one outcome happens each time, the probabilities add to $1$. This is why a complete probability table must total $1$.

For example, if a bag contains only red, blue, and white counters with $P(\text{red}) = 0.46$ and $P(\text{blue}) = 0.27$, add the known probabilities first to find the used total:
$$0.46 + 0.27 = 0.73$$

Then subtract from $1$ to find what is left for white. So the missing probability is calculated as:
$$1 - 0.73 = 0.27$$

The same idea works with fractions as well. You still find the total part already used, then subtract that sum from the whole to find the remainder.

## Ratio clues and equal shares

Ratios tell you how many equal parts each outcome has. If red:blue:white = $4:3:5$, there are $12$ parts in total, so the probabilities are $\frac{4}{12}$, $\frac{3}{12}$, and $\frac{5}{12}$.

The same parts idea works for phrases like "twice as likely". If a spinner has $P(2) = 0.30$, $P(4) = 0.25$, and landing on $1$ is twice as likely as landing on $3$, the leftover probability is

$$$1 - 0.30 - 0.25 = 0.45$$

"Twice as likely" means the ratio for $1:3$ is $2:1$, so there are $3$ equal parts altogether. One part is $0.45 \div 3 = 0.15$, so $P(3) = 0.15$ and $P(1) = 0.30$.

## Expected frequency

Expected frequency estimates how many times an event will happen in repeated trials. To calculate it, use the following formula: $$\text{expected frequency} = \text{probability} \times \text{number of trials}$$

For a biased die with $P(6) = 0.31$ rolled $200$ times, multiply the probability by the number of rolls. This gives the estimate directly: $$0.31 \times 200 = 62$$

So the expected number of sixes is $62$. You might not get exactly $62$ in practice, but it is the best estimate from the information given.

## Working backwards from a probability

When provided with a probability and the specific count of an event, you can work backwards to find the total size of the set. This allows you to solve for the denominator in the standard probability formula:

$$$P(\text{event}) = \frac{\text{number in event}}{\text{total number}}$$

If a bag has $14$ red counters and $P(\text{red}) = 0.2$, we can define the total number of counters as $T$. Substituting these values into the equation gives $0.2 = \frac{14}{T}$, and solving for the total results in $T = 14 \div 0.2 = 70$.

This calculation shows there are $70$ counters altogether. If the other groups, like blue and white, were present in equal amounts, the remaining $56$ counters would split into two groups of $28$ each.

## Using "or" for probabilities

When two outcomes cannot happen at the same time, "or" means add their probabilities. In symbols, $P(A \text{ or } B) = P(A) + P(B)$ for mutually exclusive outcomes.

Suppose a biased die has probabilities $0.10, 0.24, 0.16, 0.12,$ and $0.18$ for the outcomes $1, 2, 3, 5,$ and $6$. We first find the missing probability $P(4)$ by subtracting the sum of the known values from $1$.

$$$1 - (0.10 + 0.24 + 0.16 + 0.12 + 0.18) = 0.20$$

Now add the probabilities for rolling $2$ or $4$, then estimate the results over $150$ rolls. $$P(2 \text{ or } 4) = 0.24 + 0.20 = 0.44$$ $$0.44 \times 150 = 66$$ The die is expected to land on $2$ or $4$ about $66$ times, demonstrating that we add probabilities first and then multiply by the number of trials.

## Check yourself

1. A seed has probability $0.82$ of growing. Which statement is correct?

   - Growing is likely but not certain, so about 82 out of 100 similar seeds would be expected to grow ✔

   - The seed will definitely grow

   - The seed is more likely not to grow than to grow

   - $$0.82$ is not a valid probability

   _Explanation:_ $$0.82$ is between $0$ and $1$, so it is a valid probability, and it is greater than $0.5$, so growing is more likely than not. The common wrong answer is B, but a high probability is not the same as certainty; only probability $1$ means guaranteed.

2. A spinner can land only on A, B, C, or D. If $P(A) = 0.20$, $P(B) = 0.35$, and $P(C) = P(D)$, what is $P(C)$?

   - $$0.45$

   - $$0.225$ ✔

   - $$0.325$

   - $$0.15$

   _Explanation:_ The known probabilities total $0.55$, so $0.45$ is left for C and D together. Because C and D are equal, each gets $0.45 \div 2 = 0.225$. The common wrong answer is A, which forgets that the remainder must be shared by both missing outcomes.

3. A bag contains only red, blue, green, and yellow counters. $P(\text{green}) = 0.20$, $P(\text{yellow}) = 0.35$, and red is twice as likely as blue. There are 16 green counters. How many red counters are in the bag?

   - 24 ✔

   - 12

   - 36

   - 80

   _Explanation:_ Green and yellow use $0.20 + 0.35 = 0.55$, so red and blue share $0.45$. Since red:blue = $2:1$, one part is $0.45 \div 3 = 0.15$, so $P(\text{red}) = 0.30$. If $0.20$ of the bag is 16 counters, the total is $16 \div 0.20 = 80$, and the number of red counters is $0.30 \times 80 = 24$. The common wrong answer is C, which comes from dividing $0.45$ by $2$ instead of $3$ and forgetting that $2:1$ means 3 parts altogether.
