## Variance of a discrete random variable

* The variance $Var(X)$ measures how spread out the values of X are around the mean $E(X)$

  * *Variance of a Discrete Random Variable:* This is a **theoretical** value based on a known probability model or population. It measures the spread of all possible future outcomes before any data is collected.

  * *Normal (Sample) Variance)***:** This is an **empirical** value calculated from actual observed data. It measures the spread of the specific numbers you have already collected in a sample.

* Formula: $Var(X) = E(X²) − [E(X)]²$

  * where $E(X²) = Σx²P(X = x)$

* The standard deviation is the square root of the variance

Example for $(x = 1,2,3,4, P(X=x) = 0.4, 0.3, 0.2, 0.1, E(X) = 2):$

* $E(X²) = 1²(0.4) + 2²(0.3) + 3²(0.2) + 4²(0.1) = 0.4 + 1.2 + 1.8 + 1.6 = 5$

* $Var(X) = E(X²) − [E(X)]² = 5 − 2² = 5 − 4 = 1$