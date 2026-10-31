# Non-Parametric Tests

## Single-sample sign test

* Given $n$ data points, a single-sample sign test is created using
  $X$ $\sim$ Bin($n,\ 0.5$)
* The test statistic can be the number of + signs, that is the number
  of data points greater than the median.
* We can calculate the probability that $X$ is above this test
  statistic, below this test statistic, or either in the case of a
  two-tailed test.
* This can be expressed as
  $P\left( X \leq \text{ts} \middle| X\sim\mathrm{\text{Bin}}\left( n,0.5 \right) \right)$
  or
  $P\left( X \geq \text{ts} \middle| X\sim\mathrm{\text{Bin}}\left( n,0.5 \right) \right)$
  where $\text{ts}$ stands for test statistic.
* Only in this chapter where if the test statistic is less than the
  critical value is when you reject $H_{0}$.

**<span class="underline">Example:</span>**

It is believed that the following dataset comes from a population with
median 135

| 150 | 130 | 125 | 140 | 170 |
|----|----|----|----|----|
| 140 | 190 | 180 | 175 | 165 |
| 160 | 130 | 140 | 140 | 145 |

Perform a single-sample sign test, at the 5% significance level, to test
this claim.

**<span class="underline">Solution:</span>**

Hypotheses:

$H_{0}:$ The population median is 135

$H_{1}:$ The population median is **not** 135

This is a two-tailed test

| Value | Sign | Value | Sign |
|----|----|----|----|
| 150 | + | 140 | + |
| 140 | + | 140 | + |
| 160 | + | 175 | + |
| 130 | - | 140 | + |
| 190 | + | 170 | + |
| 130 | - | 165 | + |
| 125 | - | 145 | + |
| 180 | + |    | + |

Here, the test statistic is 12, as there are 12 values above the stated
median.

Since 12 is greater than $\frac{n}{2}$, which is 7.5, we need consider
only the top tail.

Consider $X\sim\mathrm{\text{Bin}}\left( 15,0.5 \right)$:

$$P\left( X \geq 12 \right) = \left( \frac{15}{12} \right)\left( 0.5 \right)^{15} + \left( \frac{15}{13} \right)\left( 0.5 \right)^{15} +$$

$$ \left( \frac{15}{14} \right)\left( 0.5 \right)^{15} + \left( \frac{15}{15} \right)\left( 0.5 \right)^{15}$$

$$P\left( X \geq 12 \right) \approx 0.017578$$

Since $0.017578 < 0.025$, the test statistic of 12 is in the critical
region and, therefore, we reject $H_{0}$.

There is sufficient evidence to suggest the population is not 135.

* We can approximate the simple-sample sign test with the normal
  distribution
  * $n$ has to be large ($n > 10$)
  * Let $S = \mathrm{min(No.\  + \ signs,\ No.\ of\  - \ signs)}$
  * $E\left( S \right) = \frac{n}{2}$
  * $\text{Var}\left( S \right) = \frac{n}{4}$
  * Then $T\sim N\left( \frac{n}{2},\frac{n}{4} \right)$
  * Applying continuity correction, our z-value is:

$$z = \frac{S^{+} - \mu + 0.5}{\sigma}$$