## Paired-sample sign test

* We can extend the idea of the sign test to work with paired-sample
  data by looking for a positive or negative difference. Nevertheless,
  the principles behind the sign test remain the same
* We still use the Binom. Dist. to calculate our test statistic

**<span class="underline">Example:</span>**

Data are collected on the time, in seconds, it takes nine children to
tie up their left shoelace and their right shoelace.

| **Child** | **Left (s)** | **Right (s)** |
|----|----|----|
| A | 42 | 45 |
| B | 38 | 36 |
| C | 51 | 52 |
| D | 42 | 39 |
| E | 31 | 35 |
| F | 48 | 49 |
| G | 61 | 62 |
| H | 38 | 39 |
| I | 44 | 45 |

Test, at the 10% level of significance, whether there is a difference in
the time it takes for the children to tie each shoelace.

**<span class="underline">Solution:</span>**

Hypotheses:

$H_{0}$: There is no difference in the time taken to tie their left
and right shoelaces.

$H_{1}:$ There is a difference in the time taken to tie their left and
right shoelaces.

Let’s set $L_{i} - R_{i}$ as the difference.

| **Child** | **Left (s)** | **Right (s)** |    |
|----|----|----|----|
| A | 42 | 45 | - |
| B | 38 | 36 | + |
| C | 51 | 52 | - |
| D | 42 | 39 | + |
| E | 31 | 35 | - |
| F | 48 | 49 | - |
| G | 61 | 62 | - |
| H | 38 | 39 | - |
| I | 44 | 45 | - |

We will let the number of + signs be the test statistic

The test statistic is 2

Use: $X\sim\mathrm{\text{Bin}}\left( 9,0.5 \right)$

$$
P\left( X \leq 2 \right) = \left( \frac{9}{0} \right)\left( 0.5 \right)^{9} + 
\left( \frac{9}{1} \right)\left( 0.5 \right)^{9} + \left( \frac{9}{2} \right)\left( 0.5 \right)^{9}
$$

$$
P\left( X \leq 2 \right) \approx 0.089844
$$

Because this is a two-tailed test, our critical value will be
$10% \div 2\  = \ 0.05$

Since 0.089844 > 0.05, the test statistic of 2 is not in the critical
region. Therefore, there is insufficient evidence to reject $H_{0}$.
There is insufficient evidence to say there is a difference in the times
taken for children to tie their left and right shoelaces.

Note: Once again here, we only reject $H_{0}$ if our test statistic is
lower than the critical value.