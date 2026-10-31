## Confidence Interval for a Population Mean 

**Sample taken from a normal population distribution with known
population variance**

$$\left( \overline{x} - z\frac{\sigma}{\sqrt{n}},\ \overline{x} + z\frac{\sigma}{\sqrt{n}} \right)$$

  - $z$ is the value corresponding to the confidence level required
    and $n$ is the sample size

  - The confidence interval calculated is exact

**Large sample taken from an unknown population distribution with known
population variance**

  - By the Central Limit Theorem, the distribution of $\overline{X}$
    will be approximately normal so same method as above

$$\left( \overline{x} - z\frac{\sigma}{\sqrt{n}},\ \overline{x} + z\frac{\sigma}{\sqrt{n}} \right)$$

  - The confidence interval calculated is an approximate

**Large sample taken from an unknown population distribution with
unknown population variance**

  - As the population variance is unknown, you must first estimate the
    population variance, $s$, using sample data

$$\left( \overline{x} - z\frac{s}{\sqrt{n}},\ \overline{x} + z\frac{s}{\sqrt{n}} \right)$$

  - The confidence interval calculated is an approximate

**<span class="underline">{W13-P71} Question 2:</span>**

Heights of a certain species of animal are normally distributed with
$\sigma = \ $0.17m. Obtain a 99% confidence interval for the
population mean, with total width less than 0.2m. Find the smallest
sample size required.

**<span class="underline">Solution:</span>**

*For a 99% confidence interval, find* $z$ *where*

$\Phi\left( z \right) =$ *0.995 (think of the 1% cut from both sides)*

$$z = 2.576$$

*Subtract the limits of the interval and equate to 0.2*

$$\left( \overline{x} + z\frac{\sigma}{\sqrt{n}} \right) - \left( \overline{x} - z\frac{\sigma}{\sqrt{n}} \right) = 0.2$$

$$2\left( z\frac{\sigma}{\sqrt{n}} \right) = 0.2$$

*Substitute information given and find* $n$

$$\sqrt{n} = \frac{2 \times 2.576}{0.2} \times 0.17$$

$$n = 19.2 \approx 20$$
