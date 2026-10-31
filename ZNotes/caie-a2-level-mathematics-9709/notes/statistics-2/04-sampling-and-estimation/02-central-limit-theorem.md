## Central Limit Theorem

* If $\left( X_{1},\ X_{2},\ \ldots,\ X_{n} \right)$ is a random
  sample of size $n$ drawn from any population with mean $\mu$ and
  variance $\sigma^{2}$ then the sample has:

Expected mean, $\mu$

Expected variance, $\frac{\sigma^{2}}{n}$

It forms a normal distribution:

$$
\widetilde{X}\sim N\left( \mu,\frac{\sigma^{2}}{n} \right)
$$

**<span class="underline">{IS Ex 10f} Question 12:</span>**

The weights of the trout at a trout farm are normally distributed with
mean 1kg & standard deviation 0.25kg


1. Find, to 4 decimal places, the probability that a trout chosen at
   random weighs more than 1.25kg.
2. If $\overline{Y}$kg represents mean weight of a sample of 10 trout
   chosen at random, state the distribution of $\overline{Y}$:
   evaluate the mean and variance. Find the probability that the mean
   weight of a sample of 10 trout will be less than 0.9kg

**<span class="underline">Solution:</span>**

**Part (a):**

*Write down distribution*

$$
X\sim N\left( 1,\ {0.25}^{2} \right)
$$

*Write down the probability they want*

$$
P\left( X > 1.25 \right) = 1 - P\left( X < 1.25 \right)
$$

*Standardize and evaluate*

$$
1 - P\left( Z < \frac{1.25 - 1}{0.25} \right) = 0.1587
$$

**Part (b):**

*Write down initial distribution*

$$
X\sim N\left( 1,\ {0.25}^{2} \right)
$$

For sample, mean remains equal but variance changes

*Find new variance*

Variance of
sample$\  = \frac{\sigma^{2}}{n} = \frac{{0.25}^{2}}{10} = 0.00625$

*Write down distribution of sample*

$$
\overline{Y}\sim N\left( 1,\ 0.00625 \right)
$$

*Write down the probability they want*

$$
P\left( \overline{Y} < 0.9 \right)
$$

*Standardize and evaluate*

*Standardized probability is negative so do 1 minus*

$$
P\left( Z < \frac{0.9 - 1}{\sqrt{0.00625}} \right) = 1 - P\left( Z < \frac{0.1}{\sqrt{0.00625}} \right) = 0.103
$$



