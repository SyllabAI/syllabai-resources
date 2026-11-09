# The Normal Distribution Flashcards

_Lane: `a-level-maths-edexcel` · grade — · 21 cards (source: MathsGenie flashcards)_

## Card 1 — `basic`

**Front:** In the notation $X \sim N(\mu, \sigma^2)$, what do the two parameters represent?

**Back:** $\mu$: the mean$\sigma^2$: the variance

**Choices:**

- $\mu$: the mean$\sigma^2$: the variance ✔
  - _why:_ In $X \sim N(\mu, \sigma^2)$, $\mu$ gives the centre of the distribution, while $\sigma^2$ measures its spread as the variance.
- $\mu$: the variance$\sigma^2$: the mean
  - _why:_ The parameters have been swapped: $\mu$ always denotes the mean, while $\sigma^2$ denotes the variance. Confusing variance with standard deviation is a common notation error.
- $\mu$: the standard deviation$\sigma^2$: the mean
  - _why:_ The mean is represented by $\mu$, not $\sigma^2$. The symbol $\sigma$ represents standard deviation, so $\sigma^2$ represents variance.
- $\mu$: the median$\sigma^2$: the standard deviation
  - _why:_ For a normal distribution, $\mu$ represents the mean, which is also the median, but it is not labelled the median here. The squared parameter $\sigma^2$ is variance, not standard deviation.

## Card 2 — `basic`

**Front:** How does an increase in the standard deviation $\sigma$ affect the shape of the normal curve?

**Back:** The curve becomes wider and flatter.

**Choices:**

- The curve becomes wider and flatter. ✔
  - _why:_ A larger standard deviation spreads values further from the mean. To keep the total area equal to 1, the normal curve becomes wider and its peak becomes flatter.
- The curve becomes narrower and taller.
  - _why:_ This is the effect of decreasing, not increasing, $\sigma$. A larger standard deviation spreads the distribution out, making it wider and flatter while preserving total area.
- The curve shifts to the right and becomes flatter.
  - _why:_ Changing $\sigma$ alters the spread but not the centre. The mean controls horizontal position; increasing $\sigma$ makes the curve wider and flatter without shifting it.
- The curve becomes wider and taller.
  - _why:_ Although increasing $\sigma$ makes the curve wider, its maximum height must decrease because the total area remains 1. Therefore it becomes wider and flatter.

## Card 3 — `cloze`

**Front:** For any continuous normal variable, the probability of the variable taking exactly one specific value is [ ___ ].

**Back:** For any continuous normal variable, the probability of the variable taking exactly one specific value is 0.

**Choices:**

- 0 ✔
  - _why:_ A normal variable is continuous, so the probability at one exact point has zero area under the curve. Probabilities come from intervals, not individual values.
- 1
  - _why:_ A probability of 1 would mean the variable is certain to equal that one value. For a continuous normal variable, one point has zero width and therefore probability 0.
- 0.5
  - _why:_ The value 0.5 might describe an interval probability, but not the probability of one exact point in a continuous distribution. The correct point probability is 0.
- $$\frac{1}{2}$
  - _why:_ An exact value has no interval width, so its probability is zero, not $\frac{1}{2}$. A non-zero probability applies to a range of values.

## Card 4 — `basic`

**Front:** Why is $P(X < a)$ equal to $P(X \le a)$ in a normal distribution?

**Back:** The probability of $X$ being exactly $a$ is zero.

**Choices:**

- The probability of $X$ being exactly $a$ is zero. ✔
  - _why:_ A normal distribution is continuous, so $P(X=a)=0$. Consequently, including or excluding the single endpoint does not change the probability, giving $P(X<a)=P(X\le a)$.
- The probability of $X$ being less than $a$ is zero.
  - _why:_ The probability below $a$ is generally a positive area under the curve. Equality holds because the probability of the single endpoint $X=a$ is zero.
- The probability of $X$ being greater than $a$ is zero.
  - _why:_ Values greater than $a$ usually have positive probability in a normal distribution. The relevant fact is that the probability of exactly $a$ is zero.
- The probability of $X$ being exactly the mean is one.
  - _why:_ Even the mean is only one point on a continuous distribution, so its probability is zero, not one. The endpoint equality follows from $P(X=a)=0$ for any $a$.

## Card 5 — `basic`

**Front:** Identify the mean and standard deviation of $X \sim N(100, 25)$.

**Back:** Mean: 100Standard deviation: 5 ($\sqrt{25}$)

**Choices:**

- Mean: 100Standard deviation: 5 ($\sqrt{25}$) ✔
  - _why:_ In $N(100,25)$, the first parameter is the mean and the second is the variance. The standard deviation is $\sqrt{25}=5$.
- Mean: 100Standard deviation: 25 ($\sqrt{625}$)
  - _why:_ The second parameter, 25, is the variance rather than the standard deviation. Taking its square root gives the standard deviation, $\sqrt{25}=5$.
- Mean: 25Standard deviation: 10 ($\sqrt{100}$)
  - _why:_ The parameters have been reversed and the spread has then been calculated from the wrong value. The mean is 100, and $\sqrt{25}=5$ is the standard deviation.
- Mean: 100Standard deviation: 625 ($25^2$)
  - _why:_ Squaring the variance increases the spread instead of converting it to standard deviation. The required operation is $\sqrt{25}$, giving a standard deviation of 5.

## Card 6 — `cloze`

**Front:** The standard normal distribution is denoted by $\text{[...]}$.

**Back:** The standard normal distribution is denoted by $\boxed{Z \sim N(0, 1)}$.

**Choices:**

- $$Z \sim N(0, 1)$ ✔
  - _why:_ The standard normal distribution has mean 0 and variance 1, so it is written as $Z \sim N(0,1)$. Its standard deviation is also 1.
- $$Z \sim N(1, 0)$
  - _why:_ The standard normal has mean 0 and variance 1, not mean 1 and variance 0. A variance of 0 would describe a constant rather than a normal curve.
- $$Z \sim N(0, 0)$
  - _why:_ The mean is correctly shown as 0, but the variance must be 1. Variance 0 gives no spread, so it cannot represent the standard normal distribution.
- $$Z \sim N(1, 1)$
  - _why:_ Although the variance is correctly 1, the standard normal mean is 0, not 1. The notation must therefore be $Z \sim N(0,1)$.

## Card 7 — `cloze`

**Front:** The formula to standardise a value $X$ is $\text{[...]}$.

**Back:** The formula to standardise a value $X$ is $\boxed{Z = \frac{X - \mu}{\sigma}}$.

**Choices:**

- $$Z = \frac{X - \mu}{\sigma}$ ✔
  - _why:_ Subtracting $\mu$ centres the value relative to the mean, and dividing by $\sigma$ measures that distance in standard deviations. The result is the standardised value $Z$.
- $$Z = \frac{X + \mu}{\sigma}$
  - _why:_ Adding the mean does not centre $X$; it moves the value further from the reference point. Standardisation requires subtracting $\mu$ before dividing by $\sigma$.
- $$Z = \frac{X - \sigma}{\mu}$
  - _why:_ The mean must be subtracted to centre the observation, and the standard deviation must divide to measure standard-deviation units. These roles have been incorrectly exchanged.
- $$Z = \frac{X}{\mu - \sigma}$
  - _why:_ Standardisation is based on the distance from the mean, $X-\mu$, scaled by the standard deviation $\sigma$. Combining the parameters as $\mu-\sigma$ does not produce a z-value.

## Card 8 — `basic`

**Front:** What does a $z$-value represent in the context of the normal distribution?

**Back:** The number of standard deviations a value is from the mean.

**Choices:**

- The number of standard deviations a value is from the mean. ✔
  - _why:_ A z-value measures the signed distance from the mean in standard-deviation units. Positive values lie above the mean and negative values lie below it.
- The number of variances a value is from the mean.
  - _why:_ A z-value uses standard deviation, not variance, as the unit of spread. Dividing by $\sigma^2$ would give the wrong scale and would not represent standard-deviation units.
- The probability of a value being from the mean.
  - _why:_ A z-value is a standardised distance, not a probability. Probabilities are found from areas under the normal curve after using the z-value.
- The number of units a value is above the mean.
  - _why:_ A z-value can be positive or negative and measures distance in standard deviations, not ordinary units or only upward distance. Values below the mean have negative z-values.

## Card 9 — `basic`

**Front:** State the symmetry property of $P(X < \mu)$ for any normal distribution.

**Back:** $$P(X < \mu) = 0.5$

**Choices:**

- $$P(X < \mu) = 0.5$ ✔
  - _why:_ A normal distribution is symmetric about its mean, so exactly half of the probability lies below $\mu$ and half lies above it.
- $$P(X < \mu) = 0.25$
  - _why:_ This confuses the mean with a quartile. Symmetry divides the total probability equally at the mean, so $P(X < \mu) = 0.5$.
- $$P(X < \mu) = 0$
  - _why:_ The mean is not the distribution’s lower boundary. Half of the probability lies below the mean, giving $P(X < \mu) = 0.5$.
- $$P(X < \mu) = 1$
  - _why:_ The mean is not an upper boundary containing the entire distribution. Symmetry places half the probability below it, so $P(X < \mu) = 0.5$.

## Card 10 — `cloze`

**Front:** To find a value $x$ from a standard normal $z$-value, use the formula $\text{[...]}$.

**Back:** To find a value $x$ from a standard normal $z$-value, use the formula $\boxed{x = \mu + \sigma z}$.

**Choices:**

- $$x = \mu + \sigma z$ ✔
  - _why:_ Rearranging $z = \frac{x-\mu}{\sigma}$ gives $x-\mu=\sigma z$, and then adding $\mu$ gives $x=\mu+\sigma z$.
- $$x = \frac{z-\mu}{\sigma}$
  - _why:_ This incorrectly applies the standardisation formula to $z$ rather than rearranging it. Solving $z=\frac{x-\mu}{\sigma}$ for $x$ gives $x=\mu+\sigma z$.
- $$x = \mu - \sigma z$
  - _why:_ The sign has been reversed when rearranging the standardisation formula. Since $x-\mu=\sigma z$, the correct result is $x=\mu+\sigma z$.
- $$x = \mu + \frac{z}{\sigma}$
  - _why:_ This divides the standard normal value by the standard deviation instead of multiplying it. Rescaling requires $\sigma z$, so $x=\mu+\sigma z$.

## Card 11 — `basic`

**Front:** What is the first step required to find a missing $\mu$ or $\sigma$ when given a probability?

**Back:** Use inverse normal to find the corresponding $z$-value.

**Choices:**

- Use inverse normal to find the corresponding $z$-value. ✔
  - _why:_ A cumulative probability identifies a percentile of the standard normal distribution. Applying inverse normal converts that probability into the corresponding standardised $z$-value.
- Use normal cumulative distribution to find the corresponding $z$-value.
  - _why:_ The cumulative distribution function finds a probability from a known value, reversing the required direction. Use inverse normal to obtain the $z$-value from the probability.
- Use linear interpolation to find the corresponding $z$-value.
  - _why:_ Linear interpolation is not the initial method for converting a normal probability into a standard score. Use inverse normal to find the corresponding $z$-value.
- Use standardisation to find the corresponding $z$-value.
  - _why:_ Standardisation requires the mean and standard deviation already to be known, so it cannot initially resolve a missing parameter. First use inverse normal to find the $z$-value.

## Card 12 — `basic`

**Front:** How many probability statements are needed to calculate both a missing mean and a missing standard deviation?

**Back:** Two (to form two simultaneous equations).

**Choices:**

- Two (to form two simultaneous equations). ✔
  - _why:_ The unknown mean and standard deviation are two separate parameters. Each probability statement provides one equation, so two statements produce two simultaneous equations.
- One (to form one simultaneous equation).
  - _why:_ One probability statement supplies only one equation, which cannot uniquely determine two unknown parameters. Two statements are needed to form two simultaneous equations.
- Three (to form three simultaneous equations).
  - _why:_ A third independent statement is unnecessary because there are only two unknowns, $\mu$ and $\sigma$. Two probability statements provide the required simultaneous equations.
- Four (to form four simultaneous equations).
  - _why:_ This incorrectly assumes each parameter needs two separate conditions. There are two unknown parameters, so two probability statements are sufficient to form two simultaneous equations.

## Card 13 — `basic`

**Front:** In race times, how should the phrase "faster than 10 seconds" be written in probability notation?

**Back:** $$P(T < 10)$

**Choices:**

- $$P(T < 10)$ ✔
  - _why:_ A faster race time is numerically smaller, so finishing faster than 10 seconds means the recorded time $T$ is less than 10.
- $$P(T > 10)$
  - _why:_ This treats a larger time as faster, reversing the relationship. Faster performances take fewer seconds, so the correct notation is $P(T < 10)$.
- $$P(T \leq 10)$
  - _why:_ The word “faster” indicates a strict inequality and excludes a time of exactly 10 seconds. The correct notation is therefore $P(T < 10)$.
- $$P(T \geq 10)$
  - _why:_ This both reverses the direction and includes exactly 10 seconds. Faster times are below 10 seconds, so the correct expression is $P(T < 10)$.

## Card 14 — `cloze`

**Front:** The general formula for conditional probability is $P(A|B) = \frac{\text{[...]}}{P(B)}$.

**Back:** The general formula for conditional probability is $P(A|B) = \frac{\boxed{P(A \cap B)}}{P(B)}$.

**Choices:**

- $$P(A \cap B)$ ✔
  - _why:_ Conditional probability restricts attention to outcomes in $B$. The favourable outcomes are those in both $A$ and $B$, so the numerator is $P(A \cap B)$.
- $$P(A \cup B)$
  - _why:_ The union includes outcomes occurring in either event, including those outside the condition $B$. The numerator must be the intersection $P(A \cap B)$.
- $$P(A)$
  - _why:_ Using all outcomes in $A$ ignores the requirement that $B$ has occurred. The numerator must count outcomes shared by both events, namely $P(A \cap B)$.
- $$P(B|A)$
  - _why:_ This is a conditional probability in the reverse direction, not the joint probability required in the numerator. The correct numerator is $P(A \cap B)$.

## Card 15 — `cloze`

**Front:** The general formula for conditional probability is $P(A|B) = \frac{P(A \cap B)}{\text{[...]}}$.

**Back:** The general formula for conditional probability is $P(A|B) = \frac{P(A \cap B)}{\boxed{P(B)}}$.

**Choices:**

- $$P(B)$ ✔
  - _why:_ Conditioning on $B$ restricts the sample space to event $B$, so the joint probability $P(A \cap B)$ must be divided by $P(B)$.
- $$P(A)$
  - _why:_ Dividing by $P(A)$ would condition on $A$ and produce $P(B|A)$ instead. Since the stated condition is $B$, the denominator is $P(B)$.
- $$P(A \cap B)$
  - _why:_ Using the intersection as both numerator and denominator would always produce 1 when it is non-zero. Conditional probability instead divides by the conditioning event’s probability, $P(B)$.
- $$1-P(B)$
  - _why:_ This divides by the probability that $B$ does not occur, which contradicts the condition that $B$ has occurred. The correct denominator is $P(B)$.

## Card 16 — `basic`

**Front:** If a battery has already lasted 40 hours, how is the probability that it lasts at least another 10 hours expressed?

**Back:** $$P(X > 50 | X > 40)$

**Choices:**

- $$P(X > 50 | X > 40)$ ✔
  - _why:_ Lasting another 10 hours after already exceeding 40 hours means the total lifetime must exceed 50 hours, conditional on it having exceeded 40 hours.
- $$P(X > 10 | X > 40)$
  - _why:_ This treats “another 10 hours” as a total lifetime of 10 hours. The threshold must be added to 40, giving $P(X > 50 | X > 40)$.
- $$P(X > 50)$
  - _why:_ This ignores the information that the battery has already lasted 40 hours. That information must be included as a condition, giving $P(X > 50 | X > 40)$.
- $$P(X > 40 | X > 50)$
  - _why:_ The condition and target events have been reversed. The known event is survival beyond 40 hours, while the target is survival beyond 50 hours.

## Card 17 — `cloze`

**Front:** For a population $X \sim N(\mu, \sigma^2)$, the distribution of the sample mean is $\text{[...]}$.

**Back:** For a population $X \sim N(\mu, \sigma^2)$, the distribution of the sample mean is $\boxed{\bar{X} \sim N(\mu, \frac{\sigma^2}{n})}$.

**Choices:**

- $$\bar{X} \sim N(\mu, \frac{\sigma^2}{n})$ ✔
  - _why:_ Averaging $n$ independent observations preserves the population mean $mu$ and divides the variance by $n$, so the sample mean has variance $\frac{\sigma^2}{n}$.
- $$\bar{X} \sim N(\mu, \frac{\sigma^2}{\sqrt{n}})$
  - _why:_ Dividing the variance by $\sqrt{n}$ confuses the variance with the standard deviation. The sample mean has variance $\frac{\sigma^2}{n}$, giving $\bar{X} \sim N(\mu, \frac{\sigma^2}{n})$.
- $$\bar{X} \sim N(\mu, n\sigma^2)$
  - _why:_ Multiplying by $n$ incorrectly makes sample means more variable as the sample grows. Averaging reduces variance, so the correct distribution is $\bar{X} \sim N(\mu, \frac{\sigma^2}{n})$.
- $$\bar{X} \sim N(n\mu, \frac{\sigma^2}{n})$
  - _why:_ The mean of $\bar{X}$ remains $\mu$ rather than becoming $n\mu$; only a sample total has mean $n\mu$. Its distribution is $N(\mu, \frac{\sigma^2}{n})$.

## Card 18 — `basic`

**Front:** Define the "standard error" of the sample mean.

**Back:** The standard deviation of the sampling distribution: $\frac{\sigma}{\sqrt{n}}$.

**Choices:**

- The standard deviation of the sampling distribution: $\frac{\sigma}{\sqrt{n}}$. ✔
  - _why:_ The standard error measures the standard deviation of sample means across repeated samples. Since $\operatorname{Var}(\bar{X})=\frac{\sigma^2}{n}$, its standard deviation is $\frac{\sigma}{\sqrt{n}}$.
- The standard deviation of the population distribution: $\sigma$.
  - _why:_ The quantity $\sigma$ is the standard deviation of individual population values, not of sample means. Averaging $n$ observations reduces the standard deviation to $\frac{\sigma}{\sqrt{n}}$.
- The variance of the sampling distribution: $\frac{\sigma^2}{n}$.
  - _why:_ The quantity $\frac{\sigma^2}{n}$ is the variance of the sampling distribution, not its standard deviation. Taking its square root gives the standard error $\frac{\sigma}{\sqrt{n}}$.
- The standard deviation of the sampling distribution: $\frac{\sigma}{n}$.
  - _why:_ Dividing the standard deviation by $n$ rather than $\sqrt{n}$ overstates the effect of averaging. The variance divides by $n$, so the standard error is $\frac{\sigma}{\sqrt{n}}$.

## Card 19 — `basic`

**Front:** State the null and alternative hypotheses for a test where the mean $\mu$ is suspected to have increased from a value $k$.

**Back:** $H_0: \mu = k$$H_1: \mu > k$

**Choices:**

- $H_0: \mu = k$$H_1: \mu > k$ ✔
  - _why:_ The null hypothesis fixes the mean at its original value $k$. Because the suspected change is specifically an increase, the alternative hypothesis is the one-tailed statement $\mu>k$.
- $H_0: \mu = k$$H_1: \mu
  - _why:_ The alternative $\muk$.
- $H_0: \mu = k$$H_1: \mu \ne k$
  - _why:_ The alternative $\mu\ne k$ describes a two-tailed test for any change, not specifically an increase. The correct directional alternative is $H_1: \mu>k$, with $H_0: \mu=k$.
- $H_0: \mu > k$$H_1: \mu = k$
  - _why:_ Equality belongs in the null hypothesis, which represents the original claimed value. The correct hypotheses are $H_0: \mu=k$ and $H_1: \mu>k$ for a suspected increase.

## Card 20 — `basic`

**Front:** When conducting a hypothesis test, what is the condition to reject the null hypothesis $H_0$ using a p-value?

**Back:** Reject $H_0$ if p-value < significance level.

**Choices:**

- Reject $H_0$ if p-value < significance level. ✔
  - _why:_ A small p-value indicates that the observed result would be unlikely if $H_0$ were true. The null hypothesis is rejected when the p-value falls below the chosen significance level.
- Reject $H_0$ if p-value > significance level.
  - _why:_ A p-value greater than the significance level does not provide sufficient evidence against $H_0$. The correct decision rule is to reject $H_0$ when the p-value is below the significance level.
- Fail to reject $H_0$ if p-value < significance level.
  - _why:_ The inequality has been reversed: a p-value below the significance level leads to rejection, whereas a larger p-value means there is insufficient evidence to reject $H_0$.
- Reject $H_0$ if p-value = significance level.
  - _why:_ Equality is not included in the stated strict decision rule. At the significance-level boundary, the usual rule here does not reject $H_0$; rejection requires a smaller p-value.

## Card 21 — `basic`

**Front:** How do you estimate the population standard deviation for a large sample if $\sigma$ is unknown?

**Back:** Use the sample standard deviation ($s$).

**Choices:**

- Use the sample standard deviation ($s$). ✔
  - _why:_ For a large sample, the sample standard deviation $s$ provides a suitable estimate of the unknown population standard deviation $\sigma$, allowing it to be substituted in standard-error calculations.
- Use the sample variance ($s^2$).
  - _why:_ The sample variance $s^2$ estimates the population variance $\sigma^2$, not the population standard deviation $\sigma$. The required estimate of standard deviation is $s$.
- Use the sample standard error ($\frac{s}{\sqrt{n}}$).
  - _why:_ The standard error $\frac{s}{\sqrt{n}}$ estimates the spread of sample means, not the spread of individual population values. The population standard deviation is estimated directly by $s$.
- Use the sample range ($R$).
  - _why:_ The range depends only on the two extreme observations and is not a direct estimate of population standard deviation. For a large sample, use the sample standard deviation $s$.
