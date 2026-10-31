## Goodness of Fit to Prescribed Distribution Type

* This is the case where the null hypothesis states that the data has
  a ‘particular named distribution’ but does not specify all the
  parameters of the distribution
* You must then calculate the parameter in order to carry out the test
  e.g.
  * Normal: mean and estimated sample variance
  * Poisson: mean
  * Binomial: probability of success
* For $k$ parameters calculated from the observed data, you must
  subtract $k$ from the degrees of freedom $v$
* Hence, with $m$ different outcomes,

$$v = m - 1 - k$$

Or in words

Deg. Of freedom = No. of $E_{i}$ – 1 $–$ Parameters estimated

**<span class="underline">Question 2</span>
<span class="underline">9231/04/SP/20</span>**

Each of 200 identically biased dice is thrown repeatedly until an even
number is obtained. The number of throws needed is recorded and the
results are summarized in the following table.

| No. of throws | 1 | 2 | 3 | 4 | 5 | 6 | $\geq 7$ |
|----|----|----|----|----|----|----|----|
| Frequency | 126 | 43 | 22 | 3 | 5 | 1 | 0 |

Carry out a goodness of fit test, at the 5% significance level, to test
whether Geo(0.6) is a satisfactory model for the data.

**<span class="underline">Solution:</span>**

Hypotheses:

$H_{0}:$ Geo(0.6) is a suitable model

$H_{1}:$ Geo(0.6) is **not** a suitable model

Calculate expected values using
$200 \times \left( 0.6 \right)\left( 0.4 \right)^{r - 1}$

| $r$ | 1 | 2 | 3 | 4 | 5 | 6 | $\geq 7$ |
|----|----|----|----|----|----|----|----|
| $O_{i}$ | 126 | 43 | 22 | 3 | 5 | 1 | 0 |
| $E_{i}$ | 120 | 48 | 19.2 | 7.68 | 3.072 | 1.2288 | 0.8192 |

Combine the last 3 cells since we want to ensure that all $E_{i}$ are
greater than 5, $E_{i} \geq 5$.

| $r$ | 1 | 2 | 3 | 4 | $\geq 5$ |
|----|----|----|----|----|----|
| $O_{i}$ | 126 | 43 | 22 | 3 | 6 |
| $E_{i}$ | 120 | 48 | 19.2 | 7.68 | 5.12 |

Calculate test statistic, $\chi^{2}$:

$$\chi^{2} = \sum_{}^{}\left( \frac{O_{i}^{2}}{E_{i}} \right) - N$$

$$= \frac{126^{2}}{120} + \frac{43^{2}}{48} + \frac{22^{2}}{19.2} + \frac{3^{2}}{7.68} + \frac{6^{2}}{5.12} - 200$$

$$= \frac{4063}{960} \approx 4.2323$$

Find the critical value:

* Degree of freedom = No. of cells – 1 $–$ parameter estimated =
  $5 - 1\  = 4$
* 5% significance level
  $\rightarrow ,\chi_{4}^{2}\left( 0.95 \right)$

From tables:

$$\chi_{4}^{2}\left( 0.95 \right) = 9.488$$

Compare test statistic with crit. Value

$$4.2323 < 9.488$$

Since Test Stat. < Crit. Value, $\therefore$ Accept $H_{0}$,
Geo(0.6) is a suitable model.

Note: You can use

$$\chi^{2} = \sum_{}^{}\frac{\left( O_{i} - E_{i} \right)^{2}}{E_{i}}$$

To calculate the test statistic, but the method shown is more convenient
to use.