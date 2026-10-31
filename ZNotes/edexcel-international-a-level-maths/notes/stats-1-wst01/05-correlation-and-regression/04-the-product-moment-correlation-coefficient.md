## The product-moment correlation coefficient (PMCC)

* The PMCC, denoted r, is a number that measures the strength and direction of the linear correlation between two variables

* Formula: r = $\frac{S_{xy} }{\sqrt {S_{xx} × S_{yy}}}$

  * $S_{yy} = \sum y^2-\frac{\\(\sum y)^2}{n} $
  * r lies between -1 and 1
    * r = 1: perfect positive linear correlation

    * r = -1: perfect negative linear correlation

    * r = 0: no linear correlation

    * r close to 1 or −1: strong correlation

    * r close to 0: weak correlation

**Limitations**

1. Only detects linear relationships: A non-linear/ quadratic relationship (like a U-shaped curve) can have a PMCC value of  r=0, falsely suggesting no relationship exists

2. Highly sensitive to outliers: A single extreme data point or outlier can drastically change the value of r

3. Does not imply causation: A high PMCC value r = 1 or r = -1 proves a mathematical link exists, but it does *not* prove that one variable causes the change in the other. A third hidden variable (confounding factor) could be driving both.

**Example question:**

Interpret r = 0.978 in a pmcc model

**Answer:**

Since r is very close to 1, this indicates a strong, positive linear correlation between x and y

**Example question 2:**

A researcher wants to investigate if there is a linear relationship between the number of hours a student spends revising (x) and the test score they achieve (y)

**Summary Statistics:**

$\sum x = 30$

$\sum y = 320$

$\sum x^2 = 238$

$\sum y^2 = 22,450$

$\sum xy = 2,210$

**Answer:**

* $S_{xx} = \sum x^2 - \frac{(\sum x)^2}{n} = 238 - \frac{30^2}{5} = \mathbf{58}$

* $S_{yy} = \sum y^2 - \frac{(\sum y)^2}{n} = 22,450 - \frac{320^2}{5} = \mathbf{1,970}$

* $S_{xy} = \sum xy - \frac{\sum x \sum y}{n} = 2,210 - \frac{30 \times 320}{5} = \mathbf{290}$

$r=\frac{S_{xy}}{\sqrt{S_{xx}\times S_{yy}}}$

$r=\frac{290}{\sqrt{58\times 1,970}}=\frac{290}{\sqrt{114,260}}\approx \mathbf{0.858}$