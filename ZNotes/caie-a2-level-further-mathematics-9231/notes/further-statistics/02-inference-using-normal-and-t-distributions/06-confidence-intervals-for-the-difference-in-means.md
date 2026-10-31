## Confidence intervals for the difference in means

* Conf. interval for the difference in means for small samples is given as:

$$
\left( \overline{x} - \overline{y} \right) \pm t_{\frac{\alpha}{2},n_{x} + n_{y} - 2} \times s_{p}\sqrt{\frac{1}{n_{x}} + \frac{1}{n_{y}}}
$$

* $X$ and $Y$ are independent populations
* The population variance of the two populations is the same but may be unknown
* $n$ is small ($n < 30$)

<!-- end list -->

* Conf. interval for the difference in means for large $n$ is given as:

$$
\left( \overline{x} - \overline{y} \right) \pm z_{\frac{\alpha}{2}} \times \sqrt{\frac{s_{x}^{2}}{n_{x}} + \frac{s_{y}^{2}}{n_{y}}}
$$

* $X$ and $Y$ are independent populations
* The population variance of the two populations is the same but may be unknown
* $n$ is large

<!-- end list -->

* Conf. interval for the difference in means for matched pairs is given as:

$$
\overline{d} \pm t_{\frac{\alpha}{2},n - 1} \times \frac{s_{d}}{\sqrt{n}}
$$

**<span class="underline">Question 3</span> <span class="underline">9231/04/SP/20:</span>**

Employees at a particular company have been working seven hours each day, from 9 am to 4 pm. To

try to reduce absence, the company decides to introduce ‘flexi-time’ and allow employees to work their seven hours each day at any time between 7 am and 9 pm.

For a random sample of 10 employees, the

numbers of hours of absence in the year before and the year after the introduction of flexi-time are

given in the following table.

| Employee | A | B | C | D | E | F | G | H | I | J |
|----|----|----|----|----|----|----|----|----|----|----|
| Before | 42 | 35 | 96 | 74 | 20 | 5 | 78 | 45 | 146 | 0 |
| After | 34 | 32 | 100 | 72 | 31 | 2 | 61 | 35 | 140 | 0 |

Test, at the 10% significance level, whether the population mean number of hours of absence has

decreased following the introduction of flexi-time, stating any assumption that you make.

**<span class="underline">Solution:</span>**

Assume:

* Population differences are normally distributed

Hypothesis:

$$
H_{0}:\mu_{d} = 0
$$

$$
H_{1}:\mu_{d} < 0
$$

Take their differences

| Employee | A | B | C | D | E | F | G | H | I | J |
|----|----|----|----|----|----|----|----|----|----|----|
| Difference | -8 | -3 | 4 | -2 | 11 | -3 | -17 | -10 | -6 | 0 |

Gather information:

* $n = 10$
* $\sum_{}^{}d = - 34$
* $\sum_{}^{}d^{2} = 648$

$$
\overline{d} = \frac{- 34}{10}
$$

$$
s_{d}^{2} = \frac{1}{9}\left( 648 - \frac{34^{2}}{10} \right) = \frac{2662}{45}
$$

Test statistic:

$$
t = \frac{\overline{d} - \mu_{d}}{\frac{s_{d}}{\sqrt{n}}} = \frac{- 3.4}{\frac{\sqrt{\frac{2662}{45}}}{\sqrt{10}}}\  \approx - 1.39792
$$

Critical value:

* One-tailed test
* 10% significance level

Which means:

$$
t_{0.9,9} = - 1.383
$$

$$
1.39792 > 1.383
$$

Since test statistic > critical value

$\therefore$ Reject $H_{0}$, hours of absence have decreased.