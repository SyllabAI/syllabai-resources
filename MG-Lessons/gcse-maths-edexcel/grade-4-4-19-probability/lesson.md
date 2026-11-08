# grade-4-4-19-probability — lesson

_Lane: `gcse-maths-edexcel` · grade 4 · 7 content steps · 4 check questions (source: MathsGenie lessons)_

## What probability means

![Probability scale from 0 to 1 marked impossible, even chance and certain, with example events rolling a 7 on a die, landing on heads, and rolling less than 7 on a die](../assets/001-81d6a4d1-a70c-4902-8814-d40cbec7281d.jpeg)

Probability describes how likely an event is when the result is random. It is always a number from 0 to 1, where 0 means impossible and 1 means certain.

An outcome is one possible result, such as landing on blue. An event is the result you care about, and we write its probability as $P(\text{blue})$.

If a question lists every possible outcome, their probabilities must add to 1. In symbols, $P(\text{all outcomes}) = 1$, and this helps you find missing values and check your answers.

## Completing a probability table

When the listed outcomes are the only possibilities, add the known probabilities and subtract from 1. Do not stop after the addition, because the missing outcome gets whatever is left.

Example: a bag contains only red, blue and white counters, with $P(\text{red}) = 0.46$ and $P(\text{blue}) = 0.37$. First add the known probabilities: $0.46 + 0.37 = 0.83$.

Now subtract from 1 to find white: $P(\text{white}) = 1 - 0.83 = 0.17$. A quick check is $0.46 + 0.37 + 0.17 = 1$.

## Estimating frequency from probability

A trial is one go of an experiment, such as one roll or one spin. To estimate how many times an event happens, use $\text{estimated number} = \text{probability} \times \text{number of trials}$.

Example: the probability that a seed grows is $0.88$, and a gardener plants 50 seeds. Multiply the probability by the number of trials: $0.88 \times 50 = 44$.

So the estimate is 44 seeds. Because this is an estimate, the actual number might be a little higher or lower.

## Probability of this or that

If two outcomes cannot happen at the same time on one trial, they are mutually exclusive. For mutually exclusive outcomes, you simply add the probabilities of the individual events occurring.

Consider a biased die where $P(1)=0.12$, $P(2)=0.24$, $P(3)=0.09$, $P(5)=0.16$ and $P(6)=0.20$. To find the missing probability for 4, sum the known values: $0.12 + 0.24 + 0.09 + 0.16 + 0.20 = 0.81$, which means $P(4) = 1 - 0.81 = 0.19$.

Now add the probabilities for 2 or 4, then estimate the number of occurrences in 200 rolls. Since $P(2 \text{ or } 4) = 0.24 + 0.19 = 0.43$, the estimate is $0.43 \times 200 = 86$.

## Turning ratios into probabilities

A ratio compares counts in parts, so you first add the parts to find the whole. Each probability is then its part divided by the total number of parts.

Example: red, blue and white counters are in the ratio $4 : 3 : 5$. The total number of parts is $4 + 3 + 5 = 12$.

So $P(\text{red}) = \frac{4}{12} = \frac{1}{3}$, $P(\text{blue}) = \frac{3}{12} = \frac{1}{4}$ and $P(\text{white}) = \frac{5}{12}$. These add to 1, which is a good check.

## Sharing the leftover probability

Sometimes two probabilities are missing, but you are told they are the same, or that one is twice or three times the other. First find the leftover probability, then split it in the matching ratio, such as $1:1$, $2:1$, or $3:1$.

Example: on a spinner, $P(2)=0.32$ and $P(4)=0.17$, and $P(1)$ is twice $P(3)$. The leftover probability for outcomes 1 and 3 is calculated as $1 - 0.32 - 0.17 = 0.51$.

Because "twice" implies a $2:1$ split, there are 3 equal parts in total. One part is $0.51 \div 3 = 0.17$. Therefore, $P(3)=0.17$ and $P(1)=0.34$.

## Using probabilities to find actual numbers

You can work backwards from a probability to an actual total. If 30 pens are green and $P(\text{green}) = 0.15$, then 30 is $0.15$ of the whole box.

Suppose $P(\text{red}) = 0.37$, $P(\text{green}) = 0.15$, and black pens are three times as likely as blue pens. The leftover for blue and black is $1 - 0.37 - 0.15 = 0.48$.

A $3 : 1$ split has 4 equal parts, so one part is $0.48 \div 4 = 0.12$ and $P(\text{black}) = 0.36$. The total number of pens is $30 \div 0.15 = 200$.

Finally, the number of black pens is $0.36 \times 200 = 72$. This problem is more challenging because it combines leftover probability, ratios and actual counts.

## Check yourself

1. Which of these cannot be a probability?

   - $$0.25$

   - $$1.2$ ✔

   - $$0$

   - $$1$

   _Explanation:_ Probabilities must be between 0 and 1 inclusive, so $1.2$ is too large. A common wrong choice is $1$, but $1$ is valid because it means the event is certain.

2. The probability that a bus is on time is $0.3$. Over 80 days, about how many days should you expect it to be on time?

   - $$24$ ✔

   - $$0.24$

   - $$80$

   - $$110$

   _Explanation:_ Use $\text{probability} \times \text{number of trials}$, so $0.3 \times 80 = 24$. A common wrong choice is $80$, but that is the total number of days, not the estimated number of successful days.

3. Two missing probabilities add to $0.24$, and one is three times the other. What is the larger probability?

   - $$0.06$

   - $$0.08$

   - $$0.12$

   - $$0.18$ ✔

   _Explanation:_ A $3 : 1$ split has 4 equal parts, so one part is $0.24 \div 4 = 0.06$ and the larger probability is $3 \times 0.06 = 0.18$. A common wrong answer is $0.12$, which comes from splitting the leftover equally instead of in a $3 : 1$ ratio.

4. A box has red, blue, green and yellow beads. $P(\text{yellow}) = 0.2$ and there are 24 yellow beads. Also $P(\text{red}) = 0.35$ and $P(\text{blue}) = 0.15$. How many green beads are in the box?

   - $$30$

   - $$36$ ✔

   - $$48$

   - $$120$

   _Explanation:_ First find $P(\text{green}) = 1 - 0.35 - 0.15 - 0.2 = 0.3$. Since 24 is $0.2$ of the total, the total is $24 \div 0.2 = 120$, so green beads $= 0.3 \times 120 = 36$; a common wrong answer is $48$, which comes from forgetting to subtract all the known probabilities.
