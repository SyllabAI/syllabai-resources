# Inference using normal and t-distributions

## t-distribution

![Screenshot 2024-11-27 at 4.36.06 PM.png](../../../assets/42afd87fc2a2-667c162c3112117423e6e03d3ce3878d60c3996bf7e7cd4c.36)

* t-Distributions are used for small sample sizes in hypothesis tests’
  critical values.
* Given $n$ data points, the unbiased estimator of the variance,
  $s^{2}$, is calculated using:

$
s^2 = \frac{1}{n - 1} \sum_{i=1}^{n} (x_i - \overline{x})^2
$

<center>Or</center>

$$
s^{2} = \frac{1}{n - 1}\left( \sum_{}^{}x^ - \frac{\left( \sum_{}^{}x \right)^{2}}{n} \right)
$$

$$
= \frac{1}{n - 1}\left( \sum_{}^{}x^ - n{\overline{x}}^{2} \right)
$$

* For an underlying population that is normally distributed, with
  unknown variance, $H_{0}$ and $H_{1}$ will be:
  $$
  H_{0}:\ \mu = k
  $$

$$H_1 = \begin{cases} \mu > k \ \mu < k \ \mu ~\cancel{=}~ k \end{cases}$$.

* Test statistic
  $= \frac{\overline{x} - \mu}{\frac{s}{\sqrt{n}}}$ , where
  $\overline{x}$ is sample mean, $s$ is the unbiased estimator
  of the standard deviation.

* The critical value for a significance level is:

  One tailed: $t_{\alpha,n - 1}$

  Two tailed: $t_{\frac{\alpha}{2},n - 1}$

**<span class="underline">Example:</span>**

A random sample of 12 workers from a mobile phone assembly line is
selected from a large number of workers to assemble a phone at their
normal working speed. The times taken, in minutes, to complete these
tasks are recorded below:

43\.2, 41.6, 49.3, 48.2, 44.2, 40.6, 39.7, 43.4, 44.9, 45.1, 46.2, 43.2

Assuming that this sample comes from an underlying normal population,
investigate that the population mean is 45 minutes. Use 5% significance
level

**<span class="underline">Solution:</span>**

* Assumed underlying normal dist.
* Unknown variance
* Small sample size
* Test if population is different from 45, which means that it’s a two
  tailed test.
* Significance level is 5%

$$
H_{0}:\mu = 45
$$

$$
H_{1}:\mu \neq 45
$$

Test statistic:

We will have to calculate $\sum_{}^{}x$ and $\sum x^2$
manually

$$
\sum_{}^{}x = 529.6
$$

$$
\sum_{}^{}x^ = 23462.88
$$

$$
s = \sqrt{\frac{1}{12 - 1}\left( 23462.88 - \frac{{529.6}^{2}}{12} \right)}\  \approx 2.86
$$

$$
\overline{x} = \frac{\sum_{}^{}x}{n} = \frac{529.6}{12} \approx 44.1
$$

Test statistic:

$$
\frac{\overline{x} - \mu}{\frac{s}{\sqrt{n}}} = \frac{44.1 - 45}{\frac{2.86}{\sqrt{12}}} = - 1.05
$$

* Ignore the negative sign, we will only take $1.05$
* Check the critical value for this test, which is $t_{0.975,11}$

$$
t_{0.975,11} = 2.201
$$

Since $1.05 < 2.201$, the test statistic is not in the critical region
and hence we do not reject $H_{0}$. There is insufficient evidence to
claim that the population mean is not 45 minutes

Note: if we were to take the negative value, $- 1.05$, then we would
the critical value be negative too, $- 2.201$, we would then conclude
by saying

$- 1.05\  > \  - 2.201$. The magnitude is what is important here, if the magnitude of our test statistic is **not** higher than the magnitude of the critical value, we do not reject $H_{0}$. Otherwise, reject
$H_{0}.$