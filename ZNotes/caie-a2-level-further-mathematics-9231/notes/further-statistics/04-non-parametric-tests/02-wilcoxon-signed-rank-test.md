## Wilcoxon signed-rank test

A Wilcoxon signed-rank test can be performed when:
- The underlying data are symmetric
- The underlying data are continuous.
- The data are independent
- Where:
  - $P$ is the sum of the ranks corresponding to the positive
    differences from the stated median.
  - $N$ is the sum of the rank corresponding to the negative
    differences from the stated median.
  - $T = \mathrm{\min}\left( P,N \right)$ is the test statistic
- **If the test statistic is below the critical value, we reject**
  $\mathbf{H}_{\mathbf{0}}$. This is because the closer our test
  statistic is to 0, the more extreme the data; that is, more likely
  data are to be above or below stated population median, which is why
  our test statistic needs to be below the critical value from the
  tables.

$$
\text{Example}
$$

The weights (in kg) of ten randomly selected Spanish mackerel are
recorded:

|    |    |    |    |    |    |    |    |    |    |
|----|----|----|----|----|----|----|----|----|----|
| 1.6 | 1.1 | 2.1 | 2.4 | 2.2 | 2.9 | 2.6 | 2.3 | 2.7 | 1.9 |

Test, at the 5% significance level, whether the median weight is greater
than 1.8 kg.


$$
\text{Sample}
$$

Hypotheses:

$H_{0}:$ The population median weight of Spanish mackerel is 1.8 kg.

$H_{1}:$ The population median weight of Spanish mackerel is **greater
than** 1.8 kg.

Note: To perform this test, we first need to rank the magnitude of
differences of each data point from the stated population median.
Ignoring signs, start with the smallest difference and give this rank 1,
the next smallest difference is given rank 2 and so on.

| **Weight,** $\mathbf{W}_{\mathbf{i}}$ | $\mathbf{W}_{\mathbf{i}}\mathbf{-}$**Median** | **P** | **N** |
|----|----|----|----|
| 1.6 | -0.2 |    | 2 |
| 1.1 | -0.7 |    | 7 |
| 2.1 | 0.3 | 3 |    |
| 2.4 | 0.6 | 6 |    |
| 2.2 | 0.4 | 4 |    |
| 2.9 | 1.1 | 10 |    |
| 2.6 | 0.8 | 8 |    |
| 2.3 | 0.5 | 5 |    |
| 2.7 | 0.9 | 9 |    |
| 1.9 | 0.1 | 1 |    |
|    | **Sums:** | 46 | 9 |

So, the test statistic here is
$T = \mathrm{\min}\left( P,N \right) = 9$

We look up the critical value in the statistical tables:

- One-tailed test
- 5% significance level

Since $9 < 10$, (Test statistic < critical value), there is
sufficient evidence to reject. $\therefore$ There is sufficient
evidence to suggest that the population median is not 1.8kg.

Note: Once again, in this case we require the test statistic to be lower
than the crit. value to reject $H_{0}$.

* Given the statistic $T = \mathrm{\min}\left( P,N \right)$
  * $E\left( T \right) = \frac{n\left( n + 1 \right)}{4}$
  * $\text{Var}\left( T \right) = \frac{n\left( n + 1 \right)\left( 2n + 1 \right)}{24}$
  * For large $n$:

$$
T\sim N\left( \frac{n\left( n + 1 \right)}{4},\frac{n\left( n + 1 \right)\left( 2n + 1 \right)}{24} \right)
$$

* Allowing for an approximate z-test to be done using:

$$
z = \frac{T - \mu + 0.5}{\sigma}
$$

* **After approximating it to the normal distribution, this is where
  you reject the** $\mathbf{H}_{\mathbf{0}}$ **if the test statistic
  is bigger than the crit. value, exactly like in the last chapters.**

**<span class="underline">Example:</span>**

Managers at a busy international airport are studying the time arriving passengers take to pass immigration, collect their luggage, and then pass through customs. It is known that in the past this was 50 minutes. Some changes have been made to the queueing system to reduce this time. **A random sample of 45 arriving passengers is taken, and the rank sums are calculated as P=55, N=410. Using a suitable approximation test with a 1% significance level, whether the median waiting time has reduced**

**<span class="underline">Solution:</span>**

Hypotheses:

$H_{0}$: Median waiting time is 50 minutes

$H_{1}$: Median waiting time is lower than 50 minutes.

This is a One-tailed test

We will use normal dist. to approximate our data because our $n$ is
large

Gather information:

* $n = 45$
* $E\left( T \right) = \frac{1}{4}n\left( n + 1 \right) = \frac{1035}{2}$
* $\text{Var}\left( T \right) = \frac{1}{24}n\left( n + 1 \right)\left( 2n + 1 \right) = \frac{31395}{4}$
* $T = \mathrm{\min}\left( 55,\ 410 \right) = 55$

Standardizing our $T$ value

$$
z = \frac{T - \mu + 0.5}{\sigma}
$$

$$
= \frac{55.5 - \frac{1035}{2}}{\sqrt{\frac{31395}{4}}}
$$

$$
\approx - 5.21485
$$

Crit. value from the normal dist. table:

$$
z_{0.99} = - 2.326
$$

$$
\therefore 5.21485 > 2.326
$$

Since our Test statistic > Crit. value. We reject $H_{0}$, we can
conclude that the median waiting time is lower than 50 minutes

Note: as shown, once we have used normal dist. to approximate the signed-rank test, we stick back to the old rule of rejecting $H_{0}$ when the Test stat. > Crit. val.