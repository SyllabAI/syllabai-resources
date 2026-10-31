## Poisson Approximation of a Binomial Distribution

* To approximate a binomial distribution given by:

$$
X\sim B(n,p)
$$

* If $n > 50$ and $np < 5$
* Then we can use a Poisson distribution given by:

$$
X\sim Po(np)
$$

**<span class="underline">{IS Ex 8d} Question 8:</span>**

A randomly chosen doctor in general practice sees, on average, one case
of a broken nose per year and each case is independent of the other
similar cases.


1. Regarding a month as a twelfth part of a year,

   
   1. Show that the probability that, between them, three such doctors
      see no cases of a broken nose in a period of one month is 0.779
   2. Find the variance of the number of cases seen by three such
      doctors in a period of six months
2. Find the probability that, between them, three such doctors see at
   least three cases in one year.
3. Find the probability that, of three such doctors, one sees three
   cases and the other two see no cases in one year.

**<span class="underline">Solution:</span>**

**Part (i)(a):**

*Write down the information we know and need*

$1\ $doctor$\  = 1\ $nose per year$\  = \frac{1}{12}$noses per
month

$3\ $doctors$= \frac{3}{12} = \frac{1}{4}$ noses per month

*Write the distribution using the correct notation*

$$
X\sim Po\left( 0.25 \right)
$$

*Use the limits given in the question to find probability*

$$
P\left( X = 0 \right) = \frac{{0.25}^{0}e^{- 0.25}}{0!} = 0.779
$$

**Part (i)(b):**

*Use the rules of a Poisson distribution*

$$
\text{Var}\left( X \right) = \mu = \lambda
$$

*Calculate* $\lambda$ *in this scenario:*

$$
\lambda = 6 \times \mu\ \left( \text{in\ one\ month} \right) = 6 \times 0.25 = 1.5
$$

$$
\therefore Var\left( X \right) = 1.5
$$

**Part (ii):**

*Calculate* $\lambda$ *in this scenario:*

$$
\lambda = 12 \times \mu\ \left( \text{in\ one\ month} \right) = 12 \times 0.25 = 3
$$

*Use the limits given in the question to find probability*

$$
P\left( X \geq 3 \right) = 1 - P\left( X \leq 2 \right)
$$

$$
= 1 - e^{- 3}\left( \frac{3^{2}}{2!} + \frac{3^{1}}{1!} + \frac{3^{0}}{0!} \right) = 1 - 0.423 = 0.577
$$

**Part (iii):**

$$
\lambda\ for\ one\ doctor\ in\ one\ year = 1
$$

$$
\lambda\ for\ other\ two\ doctors\ in\ one\ year = 2 \times 1 = 2
$$

*For the first doctor:*

$$
P\left( X = 3 \right) = e^{- 1}\left( \frac{1^{3}}{3!} \right)
$$

*For the two other doctors:*

$$
P\left( X = 0 \right) = e^{- 1}\left( \frac{1^{0}}{0!} \right)
$$

*Considering that any of the three could be the first*

$$
P\left( X \right) = e^{- 1}\left( \frac{1^{3}}{3!} \right) \times e^{- 1}\left( \frac{1^{0}}{0!} \right) \times_{\ }^{3}C_{2} = 0.025
$$



