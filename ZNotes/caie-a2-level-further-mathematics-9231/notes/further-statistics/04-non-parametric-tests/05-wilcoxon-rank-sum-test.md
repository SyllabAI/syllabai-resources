## Wilcoxon rank-sum test:

  - A Wilcoxon rank-sum test can be performed when the two samples are
    independent, where:
    
      - The two samples have sizes $m$ and $n$, where $m \leq n$
    
      - $R_{m}$ is the sum of the ranks of the items in the sample
        size $m$
    
      - The test statistic is:

$$W = \mathrm{\min}\left( R_{m},m\left( n + m + 1 \right) - R_{m} \right)$$

**<span class="underline">Example:</span>**

Researchers are investigating the effect of vitamin B12 on the size of
the brain. A sample of males aged between 25 & 40 years is selected.
Nine of them are known to have low B12 levels and seven are known to
have high B12 levels. After a brain scan, the ratio of brain volume to
skull capacity is recorded.

| **Low B12 Levels** | **High B12 Levels** |
| ------------------ | ------------------- |
| 0.795              | 0.786               |
| 0.798              | 0.789               |
| 0.802              | 0.792               |
| 0.805              | 0.796               |
| 0.806              | 0.799               |
| 0.807              | 0.8                 |
| 0.808              | 0.803               |
| 0.81               |                     |
| 0.812              |                     |

Carry out a Wilcoxon rank-sum test, at the 5% significance level, to see
whether the level of vitamin B12 affects the size of the brain.

**<span class="underline">Solution:</span>**

Hypotheses:

$H_{0}:$ Level of B12 **has no** effect on brain size

$H_{1}:$ Level of B12 **has an** effect on brain size

First, rank the whole dataset. Note which group each value comes from.
Then add up the ranks for each category. Use the value of the sums of
the group with the smaller sample size.

|       |         | Low B12 | High B12 |
| ----- | ------- | ------- | -------- |
| 0.812 | 1       | 1       |          |
| 0.810 | 2       | 2       |          |
| 0.808 | 3       | 3       |          |
| 0.807 | 4       | 4       |          |
| 0.806 | 5       | 5       |          |
| 0.805 | 6       | 6       |          |
| 0.803 | 7       |         | 7        |
| 0.802 | 8       | 8       |          |
| 0.800 | 9       |         | 9        |
| 0.799 | 10      |         | 10       |
| 0.798 | 11      | 11      |          |
| 0.796 | 12      |         | 12       |
| 0.795 | 13      | 13      |          |
| 0.792 | 14      |         | 14       |
| 0.789 | 15      |         | 15       |
| 0.786 | 16      |         | 16       |
|       | **Sum** | 53      | 83       |

Calculate the test statistic:

$R_{m} = 83$ since this is the rank sum from the smaller-sized sample.

$$m\left( n + m + 1 \right) - R_{m} = 7\left( 9 + 7 + 1 \right) - 83 = 36$$

The test statistic is the minimum of 83 & 36, which is $W = 36$

Since 36 \< 40, there is sufficient evidence to reject $H_{0}$. There
is evidence to suggest that level of vitamin B12 affects brain size.

Note: The following table shows what we would get if we ranked them the
other way around.

|       |         | Low B12 | High B12 |
| ----- | ------- | ------- | -------- |
| 0.812 | 1       | 16      |          |
| 0.810 | 2       | 15      |          |
| 0.808 | 3       | 14      |          |
| 0.807 | 4       | 13      |          |
| 0.806 | 5       | 12      |          |
| 0.805 | 6       | 11      |          |
| 0.803 | 7       |         | 10       |
| 0.802 | 8       | 9       |          |
| 0.800 | 9       |         | 8        |
| 0.799 | 10      |         | 7        |
| 0.798 | 11      | 6       |          |
| 0.796 | 12      |         | 5        |
| 0.795 | 13      | 4       |          |
| 0.792 | 14      |         | 3        |
| 0.789 | 15      |         | 2        |
| 0.786 | 16      |         | 1        |
|       | **Sum** | 100     | 36       |

- Given the test statistic $W$, then:
  - $E\left( W \right) = \frac{1}{2}m\left( n + m + 1 \right)$
  - $\text{Var}\left( W \right) = \frac{1}{12}\text{mn}\left( n + m + 1 \right)$
  - For large $n$ and $m$, it is possible to approximate $W$
        as a normal dist.

$$
W\sim N\left( \frac{1}{2}m\left( n + m + 1 \right),\frac{1}{12}\text{mn}\left( n + m + 1 \right) \right)
$$

- Allowing for an approximate z-test with:

$$
z = \frac{W - \mu + 0.5}{\sigma}
$$
