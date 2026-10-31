# Measures of Spread

## Variance of Discrete Data

- The variance is a measure of spread.
  - It is denoted by $\sigma^2$.
    It can be found using the formulas below:
    $$
    \sum \frac{\left( x_i - \overline{x} \right)^{2}}{n}
    $$

$$
\sum_{i=1}^{n} \frac{x_i^2 - \overline{x}^2}{n}
$$

### **Coded Variance**

- Coded data does not affect the variance.
  - This is because the actual spread of the values does not change when they are transformed.

$$
\text{Variance} = \frac{\sum (x - b)^2}{n} - \left( \frac{\sum (x - b)}{n} \right)^2
$$

### **Grouped Variance**

- The variance of 2 sets of data, or grouped variance, can be found by adding the mean of squares and subtracting it using the mean squared.

Suppose a data set $x$ exists where the sum of the data is $\sum x$ and the number of values is $n_x$, and another data set $y$ exists where the sum of the data is $\sum y$ and the number of values is $n_y$.

$$
\text{Grouped Variance} = \frac{\sum x^2 + \sum y^2}{n_x + n_y} - \left( \frac{\sum x + \sum y}{n_x + n_y} \right)^2
$$

---

**<center>Example</center>**
The Znotes Archery club has 12 Junior members and 20 Senior members. For the Junior members, the mean age is 15.5 years and the standard deviation of the ages is 1.2 years. The ages of the Senior members are summarised by $\sum y = 910$ and $\sum y^2 = 42850$, where y is the age of a Senior member in years.
Find the mean and variance of all 32 members of the club.
**<center>Answer</center>**
Let $x$ denote the data of the junior members, such that $n_x = 12$ and $\frac{ \sum x}{12} = 15.5 \implies \sum x = 12 \times 15.5 = 186$.

The combined mean of both data sets is:
$$
\frac{186 + 910}{12 + 20} = 34.25
$$

The standard deviation of the juniors is $1.2$, meaning the variance is $1.2^2$.
$$
1\.2^2 = \frac{ \sum x^2}{12} - (15.5)^2 \implies \sum x^2 = 2900.28
$$

Now we can find the combined variance:
$$
\sigma^2 = \frac{ 2900.28 + 42850}{12 + 20} - (34.25)^2 = 256.63
$$