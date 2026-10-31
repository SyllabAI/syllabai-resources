## Difference in means: two-sample t-test

* The pooled estimate of the population variance $s_{p}^{2}$ can be
  found from:

$$
s_{p}^{2} = \frac{\sum_{}^{}\left( x - \overline{x} \right)^{2} + \sum_{}^{}\left( y - \overline{y} \right)^{2}}{n_{x} + n_{y} - 2}
$$

**Or**

$$
s_{p}^{2} = \frac{\left( n_{x} - 1 \right)s_{x}^{2} + \left( n_{y} - 1 \right)s_{y}^{2}}{n_{x} + n_{y} - 2}
$$

Note: The second formula is more commonly used.

* Difference in means: two-sample t-test
  * Underlying distributions are normal
  * Populations are independent
  * Population variance of the two populations is the same (but may by unknown)
* The test statistic is:

$$
T = \frac{\left( \overline{X} - \overline{Y} \right) - \left( \mu_{x} - \mu_{y} \right)}{\sqrt{s_{p}^{2}\left( \frac{1}{n_{x}} + \frac{1}{n_{y}} \right)}}
$$

And critical value will be $t_{n_{x} + n_{y} - 2}$

**<span class="underline">Example:</span>**

A shopkeeper believes that playing music in his shop encourages customers to spend more money. To test this belief, he records how much money is collected for ten days while music is playing and then for eight days without music. The sales, in thousands of dollars, are summarized as follows.

| With music | $\sum_{}^{}x = 960.1$ | $\sum_{}^{}x^{2} = 92274.44$ |
|----|----|----|
| Without music | $\sum_{}^{}y = 748.2$ | $\sum_{}^{}y^{2} = 70041.16$ |

Assuming these data are randomly sampled from normal distributions with the same variance, test the shopkeeper’s claim using a 5% significance level.

**<span class="underline">Solution:</span>**

* $n$ is small for both populations
* Both have an underlying mean
* The variances are equal but unknown

Let $X$ be the sales with music, and $Y$ be the sales without music.

If the sales “with music” are greater than “without”, then
$\mu_{x} > \mu_{y}$. Rewrite this as:

$$
H_{0}:\mu_{x} - \mu_{y} = 0
$$

$$
H_{1}:\mu_{x} - \mu_{y} > 0
$$

*This is a one-tailed test.*

*The test statistic is:*

$$
\frac{\left( \overline{X} - \overline{Y} \right) - \left( \mu_{x} - \mu_{y} \right)}{\sqrt{s_{p}^{2}\left( \frac{1}{n_{x}} + \frac{1}{n_{y}} \right)}}
$$

Next, we need to find what $s_{p}^{2}$ is:

$$
\left( n_{x} - 1 \right)s_{x}^{2} = \sum_{}^{}x^{2} - \frac{\left( \sum_{}^{}x \right)^{2}}{n_{x}}
$$

$$
= 92274.44 - \frac{{960.1}^{2}}{10} \approx 95.239
$$

$$
\left( n_{y} - 1 \right)s_{y}^{2} = \sum_{}^{}y^{2} - \frac{\left( \sum_{}^{}y \right)^{2}}{n_{y}}
$$

$$
= 70041.16 - \frac{{748.2}^{2}}{8} \approx 65.755
$$

*Using the formula for pooled variance:*

$$
s_{p}^{2} = \frac{\left( n_{x} - 1 \right)s_{x}^{2} + \left( n_{y} - 1 \right)s_{y}^{2}}{n_{x} + n_{y} - 2} = \frac{95.239 + 65.755}{10 + 8 - 2} 
$$

$$
\approx 10.062125
$$

*Finding their means:*

$$
\overline{x} = \frac{960.1}{10} = 96.01
$$

$$
\overline{y} = \frac{748.2}{8} = 93.525
$$

*Test statistic:*

$$
\frac{\left( 96.01 - 93.525 \right) - \left( 0 \right)}{\sqrt{10.062125\left( \frac{1}{10} + \frac{1}{8} \right)}} \approx 1.65154
$$

Critical value is $t_{0.95,16} = 1.746$

We used $t_{\alpha,n_{x} + n_{y} - 2}$ here.

Since $1.65154\  < \ 1.746$, the test statistic is not in the critical region, we do not reject $H_{0}$.

There is insufficient evidence to suggest that playing music increases
the sales in the shop.