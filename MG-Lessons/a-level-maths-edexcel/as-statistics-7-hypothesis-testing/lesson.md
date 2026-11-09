# as-statistics-7-hypothesis-testing — lesson

_Lane: `a-level-maths-edexcel` · grade — · 5 content steps · 4 check questions (source: MathsGenie lessons)_

## The big idea

![Three discrete binomial bar charts showing lower-tail, upper-tail, and two-tailed tests with rejection regions shaded in the tails.](../assets/001-4979c081-2a01-4e9e-b01f-655948385626.jpeg)
A binomial hypothesis test starts with a binomial model: a fixed number of trials, two outcomes, independent trials, and a constant success probability $p$. The number of successes is written $X \sim B(n,p)$.

The null hypothesis $H_0$ is the starting claim, usually $p=p_0$. The alternative hypothesis $H_1$ gives the direction of the challenge: decreased means $p<p_0$, increased means $p>p_0$, and changed means $p\ne p_0$.

The p-value is the probability, assuming $H_0$ is true, of the observed result or something more extreme in the direction of $H_1$. If the p-value is less than or equal to the significance level, reject $H_0$; otherwise, do not reject $H_0$.

## Worked example: lower-tail p-value

Let $p$ be the true probability that a customer buys a drink. In a sample of 40 customers, only 7 buy a drink, so we test $H_0: p = 0.30$ against $H_1: p < 0.30$ and use $X \sim B(40, 0.30)$ under $H_0$.

Because the claim is that the proportion has decreased, this is a lower-tail test. The p-value is $P(X \le 7) = 0.0553$, not $P(X=7)$, because a hypothesis test includes the observed result and anything more extreme in the same direction.

Compare $0.0553$ with $0.05$. Since $0.0553 > 0.05$, do not reject $H_0$ and conclude that there is not sufficient evidence at the 5% level that the proportion buying a drink has decreased.

## Worked example: upper-tail p-value

Let $p$ be the true probability that a lunch customer orders tea. If 19 out of 40 customers order tea, we test $H_0:p=0.30$ against $H_1:p>0.30$ and use $X \sim B(40,0.30)$ under $H_0$.

Because the claim is "increased", the p-value is in the upper tail: $$P(X\ge19)=1-P(X\le18)=0.0148$$ Using $1-P(X\le19)$ would be wrong because it would miss the observed value 19.

At the 1% level, $0.0148>0.01$, so do not reject $H_0$. At the 5% level, $0.0148<0.05$, so the same sample would be significant and you would reject $H_0$.

## Worked example: two-tailed critical region

For a spinner claimed to land on red with probability $0.4$, let $X$ be the number of reds in 20 spins. We test $H_0: p = 0.4$ against $H_1: p \neq 0.4$, so under $H_0$ we use $X \sim B(20, 0.4)$.

A 10% two-tailed test splits the allowance across both tails, so each tail must have probability less than $0.05$. Because the binomial distribution is discrete, the tails usually total less than 10% rather than exactly 10%.

For the lower tail, $P(X \le 3) = 0.0160$ but $P(X \le 4) = 0.0510$. Therefore, to remain within the $0.05$ probability allowance, the lower critical region is defined as $X \le 3$.

For the upper tail, $P(X \ge 13) = 0.0210$ but $P(X \ge 12) = 0.0565$. So the full critical region is $X \le 3$ or $X \ge 13$, with an actual significance level of $0.0160 + 0.0210 = 0.0370$.

## Writing the conclusion properly

Good conclusions are cautious. You are not proving $H_0$ true or false; you are deciding whether the sample gives enough evidence against it.

If the p-value is larger than the significance level, write "do not reject $H_0$" and explain this in context. For example, with p-value $0.073$ at the 5% level in an upper-tail test, there is not sufficient evidence that the probability has increased.

If the p-value is at or below the significance level, reject $H_0$ and support $H_1$. Avoid phrases like "accept $H_0$" or "the probability definitely has not changed".

## Check yourself

1. A company claims that 8% of its batteries are faulty. An inspector believes the fault rate is higher. Which pair of hypotheses is correct?

   - $$H_0:p=0.08,\ H_1:p>0.08$ ✔

   - $$H_0:X=0.08,\ H_1:X>0.08$

   - $$H_0:p=0.08,\ H_1:p\ne0.08$

   - $$H_0:p>0.08,\ H_1:p=0.08$

   _Explanation:_ A is correct because hypotheses are about the true probability $p$, and the word "higher" makes this an upper-tail test. The most common wrong answer is C, but $p\ne0.08$ would mean "has changed", not specifically "is higher".

2. In the tea example, which probability should be used as the p-value?

   - $$P(X=19)$

   - $$P(X\ge19)$ ✔

   - $$P(X\le19)$

   - $$1-P(X\le19)$

   _Explanation:_ B is correct because an upper-tail test includes the observed value 19 and any more extreme larger values. The most common wrong answer is D, but $1-P(X\le19)$ equals $P(X\ge20)$, so it leaves out the observed result.

3. A test gives p-value $0.073$ at the 5% significance level, and $H_1:p>p_0$. Which is the best conclusion?

   - Accept $H_0$ because $0.073>0.05$

   - Reject $H_0$ because $0.073$ is close to $0.05$

   - There is not sufficient evidence at the 5% level that the probability has increased ✔

   - The probability has definitely not increased

   _Explanation:_ C is correct because the p-value is larger than $0.05$, so we do not reject $H_0$ and report insufficient evidence for an increase. The most common wrong answer is A, but in hypothesis testing we say "do not reject $H_0$" rather than "accept $H_0$".

4. Stretch: A test gives p-value $0.0148$. Which statement is correct?

   - Reject $H_0$ at both 5% and 1%

   - Reject $H_0$ at 5% but not at 1% ✔

   - Do not reject $H_0$ at either 5% or 1%

   - The result is only significant if the sample size was greater than 40

   _Explanation:_ B is correct because $0.0148 < 0.05$ but $0.0148 > 0.01$. The most common wrong answer is A, but a 1% test is stricter than a 5% test, so evidence that is enough for 5% may still be too weak for 1%.
