## Addition of Poisson Distributions

* If $X$ and $Y$ are independent Poisson random variables, with
  parameters $\lambda$ and $\mu$ respectively, then $X + Y$ has
  a Poisson distribution with parameter $\lambda + \mu$

 

**<span class="underline">{IS Ex 8d} Question 1:</span>**

The numbers of emissions per minute from two radioactive objects $A$
and $B$ are independent Poisson variables with mean $0.65$ and
$0.45$ respectively. Find the probabilities that:


1. In a period of three minutes there are at least three emissions from
   $A$.
2. In a period of two minutes there is a total of less than four
   emissions from $A$ and $B$ together.

**<center>Solution:</center>**

**Part (i):**

*Write the distribution using the correct notation*

$$
A\sim Po\left( 0.65 \times 3 \right) = \ A\sim Po\left( 1.95 \right)
$$

*Use the limits given in the question to find probability*

$$
P\left( A \geq 3 \right) = 1 - P\left( A < 3 \right)
$$

$$
= 1 - \left( \frac{{1.95}^{2}e^{- 1.95}}{2!} + \frac{{1.95}^{1}e^{- 1.95}}{1!} + \frac{{1.95}^{0}e^{- 1.95}}{0!} \right)
$$

$$
= 1 - 0.690 = 0.310
$$

**Part (ii):**

*Write the distribution using the correct notation*

$$
\left( A + B \right)\sim Po\left( 2\left( 0.65 + 0.45 \right) \right) = \left( A + B \right)\sim Po\left( 2.2 \right)
$$

*Use the limits given in the question to find probability*

$$
P\left( A < 4 \right) = e^{- 2.2}\left( \frac{\left( 2.2 \right)^{3}}{3!} + \frac{\left( 2.2 \right)^{2}}{2!} + \frac{\left( 2.2 \right)^{1}}{1!} + \frac{\left( 2.2 \right)^{0}}{0!} \right)
$$

$$
= 0.819
$$



