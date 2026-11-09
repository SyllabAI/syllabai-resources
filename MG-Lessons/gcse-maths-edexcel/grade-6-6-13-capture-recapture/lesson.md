# grade-6-6-13-capture-recapture — lesson

_Lane: `gcse-maths-edexcel` · grade 6 · 5 content steps · 4 check questions (source: MathsGenie lessons)_

## What is capture recapture?

![Capture-recapture process showing first sample of 50 fish tagged and released, mixed in a pond, then second sample of 40 fish with 5 tagged, labelled M, S and R.](../assets/001-c309117c-4cc1-4322-9f59-9ee84bf295d7.jpeg)

Capture recapture is used when a population is too large or hidden to count directly. You take a first sample, mark it, release it, then later take a second sample and see how many marked individuals are found again.

The population is the whole group you want to estimate, and a sample is a smaller group taken from it. The key idea is that the proportion marked in the second sample should reflect the proportion marked in the whole population.

If only a few of the second sample are marked, the total population is probably large. If many are marked, the total population is probably smaller.

## The formula and the three numbers

Once the marked individuals have mixed back in, the fraction marked in the second sample should be about the same as the fraction marked in the whole population. That is why this method uses a proportion.

Use $M$ for the number marked in the first sample, $S$ for the size of the second sample, and $R$ for the number of marked individuals found in the second sample. This gives the formula shown below.

$$$\text{Estimated population} = \frac{M \times S}{R}$$

The bottom number is the recaptured marked amount. If $R$ is small, the estimate becomes large because only a small fraction of the second sample was marked. If $R$ is large, the estimate becomes smaller.

## Worked example step by step

A ranger tags 70 birds and releases them. Later, she catches 50 birds, and 10 of them are tagged.

First identify the three numbers: $M=70$, $S=50$, $R=10$. Now substitute into the formula shown below. This sets up the estimate correctly.

$$$ \text{Estimated population} = \frac{70 \times 50}{10} $$ Calculate the numerator first: $70 \times 50 = 3500$. Then divide by 10 to get $350$, so the estimate is 350 birds.

As a quick check, $10$ out of $50$ is $\frac{1}{5}$. So the 70 tagged birds are about one fifth of the population, giving about $70 \times 5 = 350$ birds in total.

## Different sample sizes, rounding, and zero recaptures

The first sample and second sample do not need to be the same size. You just need to use the correct roles for $M$, $S$, and $R$. For example, if $M=35$, $S=25$, and $R=4$, the calculation is shown below.

$$$\text{Estimated population} = \frac{35 \times 25}{4} = 218.75$$

Because you cannot have part of a lizard, round to a sensible whole number and say about 219 lizards. If $R=0$, the formula cannot be used because that would mean dividing by zero. In real life, you would need a larger second sample or a repeat trial.

## Assumptions you should write in exams

Capture recapture only gives a sensible estimate if the method is fair. In exam questions, you are often asked to write one assumption for full marks.

Good assumptions include that the marked individuals mix evenly back into the population and that the marks do not fall off. Another valid idea is that the marks do not change the chance of being caught again.

You can also say that the population size stays roughly the same between the two samples and that the second sample is random. Avoid vague answers like "the estimate is accurate" because that is not an assumption of the method.

## Check yourself

1. In a study, 50 fish are tagged first. Later 40 fish are caught and 5 are tagged. What is $R$?

   - 50

   - 40

   - 5 ✔

   - 90

   _Explanation:_ $$R$ is the number of marked individuals found in the second sample, so $R=5$. The common wrong answer is 40, but that is $S$, the size of the second sample.

2. A student marks 45 squirrels. Later she catches 30 squirrels and 6 are tagged. Which calculation gives the estimate?

   - $$\frac{45 \times 30}{6}$ ✔

   - $$45 + 30 + 6$

   - $$\frac{45 + 30}{6}$

   - $$\frac{45 \times 6}{30}$

   _Explanation:_ The correct method is $\frac{M \times S}{R}$, so $\frac{45 \times 30}{6}$ is right. The common wrong answer is D, where the second sample size is put on the bottom, but the bottom must be the number recaptured and marked.

3. Which statement is a valid capture recapture assumption?

   - The marked individuals mix evenly back into the population ✔

   - The first and second samples must be the same size

   - You add both sample sizes to get the population

   - Every individual must be caught at least once

   _Explanation:_ A is a standard assumption because the second sample should be representative of the whole population. The common wrong answer is B, but the two sample sizes can be different and the formula still works.

4. Two ponds are sampled in the same way. In each pond, 40 fish are tagged first and a second sample of 20 fish is taken. Pond A has 2 tagged fish in the second sample, while Pond B has 8 tagged fish. Which statement is correct?

   - Pond A has the larger estimated population ✔

   - Pond B has the larger estimated population

   - Both ponds have the same estimated population

   - There is not enough information

   _Explanation:_ Pond A gives $\frac{40 \times 20}{2} = 400$, while Pond B gives $\frac{40 \times 20}{8} = 100$, so Pond A is larger. The common wrong answer is B, but more tagged fish in the second sample means the marked fish are a bigger fraction of the population, so the total population is smaller.
