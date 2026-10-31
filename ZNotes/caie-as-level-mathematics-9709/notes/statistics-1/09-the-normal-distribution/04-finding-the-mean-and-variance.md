## Finding the mean and variance

**<center>Example</center>**

The lengths of body feathers of a particular species of bird are
modelled by a normal distribution. A researcher measures the lengths of
a random sample of 600 feathers and finds that 63 are less than 6 cm
long and 155 are more than 12 cm long.

i.  Find estimates of the mean and standard deviation of the lengths of
    body feathers of birds of this species.

ii.  In a random sample of 1000 body feathers from birds of this species,
    how many would the researcher expect to find with lengths more than
    1 standard deviation from the mean?

**<center>Answer</center>**

**Part (i):**

Interpreting the question and finding probabilities:

$P\left( X < 6 \right) = 0.105$ $P\left( X > 12 \right) = 0.258$

For $X < 6$, the probability cannot be found on the tables which
means it is behind the mean and therefore we must find $1 -$ and
assume probability is negative

$$- P\left( X < 6 \right) = 0.895$$

Using the standardization formula and working back from the table as we
are given probability

$$\frac{6 - \mu}{\sigma} = - 1.253$$

Convert the greater than sign to less than

$$P\left( X > 12 \right) = 1 - P\left( X < 12 \right)$$

$$P\left( X < 12 \right) = 1 - 0.258 = 0.742$$

Work back from table and use standardization formula

$$\frac{\left( 12 - \mu \right)}{\sigma} = 0.650$$

Solve the simultaneous equations

$\sigma = 3.15$ and $\mu = 9.9$

**Part (ii):**

Greater than 1 standard deviance from $\mu$ means both sides of the graph however
area symmetrical therefore find the greater area & double it

Using values calculated from (i):

$$P(X > \left( 9.9 + 3.15 \right) = P(X > 13.05)$$

Standardise this value

$$\frac{13.05 - 9.9}{3.15} = 1$$

We re-write the inequality as such

$$P\left( Z > 1 \right) = 1 - P\left( Z < 1 \right)$$

Find probability of 1 and find $P\left( Z > 1 \right)$

$$P\left( Z > 1 \right) = 1 - 0.841 = 0.1587$$

Multiply the probability by 2 to take into account the other side.

$$0.1587 \times 2 = 0.3174$$

Multiply the probability with the sample size

$0.3174 \times 1000 = 317$ birds