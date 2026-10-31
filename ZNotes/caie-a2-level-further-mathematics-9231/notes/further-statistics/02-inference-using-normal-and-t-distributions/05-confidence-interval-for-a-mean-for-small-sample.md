## Confidence interval for a mean for small sample

* If $\overline{x}$ is the mean of a random sample of size $n$
  from a normal distribution with population mean $\mu$, a
  $100\left( \alpha - 1 \right)%$ confidence interval for $\mu$
  is given by:

$$
\overline{x} \pm t_{\frac{\alpha}{2},, n - 1}\frac{s}{\sqrt{n}}
$$

* Interval is written as:

$$
\left( \overline{x} - t_{\frac{\alpha}{2},n - 1}\frac{s}{\sqrt{n}},,\overline{x} + t_{\frac{\alpha}{2},n - 1}\frac{s}{\sqrt{n}} \right)
$$

**<span class="underline">Example:</span>**

A random sample of people queueing for a train ticket are asked how long
they have been waiting in the queue before buying their ticket, their
replies, in minutes, are 12, 17, 21, 9, 14, 9.

Assuming a normal distribution, calculate a 90% confidence interval for
the mean stated waiting time.

**<span class="underline">Solution:</span>**

Since we have a small sample, and the population variance is unknown, we
must consider a t-distribution.

Calculate the unbiased estimators of the mean and variance

* $\sum_{}^{}x = 92$
* $\sum_{}^{}x^{2} = 1512$

$$
\overline{x} = \frac{\sum_{}^{}x}{n} = \frac{92}{6} \approx 15.333
$$

$$
s^{2} = \frac{1}{n - 1}\left( \sum_{}^{}x^{2} - \frac{\left( \sum_{}^{}x \right)^{2}}{n} \right) = \frac{1512 - \frac{92^{2}}{6}}{5}
$$

$$
\approx 20.267
$$

We are creating 90% conf. interval so:

$$
100\left( \alpha - 1 \right)% = 90%
$$

$$
\therefore\frac{\alpha}{2} = 0.95
$$

The conf. interval required is:

$$
\overline{x} \pm t_{0.95,5}\frac{s}{\sqrt{n}}
$$

From tables, $t_{0.95,5} = 2.015$

So, conf. interval is:

$$
15.33 \pm 2.015\frac{\sqrt{20.267}}{\sqrt{6}}
$$

And the 90% conf. interval is (11.627, 19.033)