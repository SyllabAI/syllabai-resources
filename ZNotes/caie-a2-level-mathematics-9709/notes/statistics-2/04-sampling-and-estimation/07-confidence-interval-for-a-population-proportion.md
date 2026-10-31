## Confidence Interval for a Population Proportion

  - Calculating the confidence interval from a random sample of $n$
    observations from a population in which the proportion of successes
    is $p$ and the proportion of failures is $q$

  - The observed proportion of success $\widehat{p}$ is
    $\frac{r}{n}$ where $r$ represents the number of successes

$$\left( \widehat{p} - z\sqrt{\frac{\widehat{p}\widehat{q}}{n}},\ \widehat{p} + z\sqrt{\frac{\widehat{p}\widehat{q}}{n}} \right)$$

**<span class="underline">{S10-P71} Question:</span>**

A random sample of $n$ people were questioned about their internet
use. 87 of them had a high-speed internet connection. A confidence
interval for the population proportion having a high-speed internet
connection is 0.1129 $\  < \ p\  < \ $ 0.1771.

1.  Write down the mid-point of this confidence interval and hence find
    the value of $n$.

2.  This interval is an $\alpha$% confidence interval. Find
    $\alpha$.

**<span class="underline">Solution:</span>**

**Part (i):**

*Find the midpoint of the limits, finding* $p$

$$0.1129 + \frac{0.1771 - 0.1129}{2} = 0.145$$

*The midpoint is equal to the proportion of people with high-speed
internet use so*

$\frac{87}{n} = 0.145$ $\therefore n = 600$

**Part (ii):**

*Using the upper limit, this was calculate by:*

$$0.1771 = 0.145 + z\sqrt{\frac{\text{pq}}{n}}$$

*Substituting values calculated (*$q = 1 - p$*), find* $z$

$$0.0321 = z\sqrt{\frac{\frac{87}{600} \times \frac{513}{600}}{600}}\ \ \ \ \ \ \ \ \ \ \therefore z = 2.233$$

*Use normal tables and find corresponding probability*

$$\Phi\left( z \right) = 0.9872$$

*Think of symmetry, the same area is chopped off from both sides of the
graph so*

$$1 - 2\left( 1 - 09872 \right) = 0.9744$$

Hence the $\alpha$% confidence is $= 97.44\%$