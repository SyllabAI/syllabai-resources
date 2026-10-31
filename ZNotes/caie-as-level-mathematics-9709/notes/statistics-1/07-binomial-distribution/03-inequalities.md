## Logarithmic inequalities

* Logarithms are a type of function that help us solve exponential equations

Given an equation

$$

a^x = b
$$

We can solve for $x$ by using the logarithmic function

$$

log_{a}(b) = x
$$

* Most calculators have an inbuilt function which can solve logarithmic equations for you.
* If a logarithm is taken with a base, $a$, less than 1 then the **inequality is flipped**.
* To solve inequalities in binomial distribution questions, its important to know that ${n \choose 0} = {n \choose n} = 1$.


---

**<center>Example</center>**

A factory makes water pistols, 8% of which do not work properly.

In a random sample of $n$ water pistols, the probability that **at least one** does not work properly is greater than 0.9. Find the smallest value of $n$.

**<center>Answer</center>**

We can model the distribution as such

$$

X \sim B\left(n, 0.08 \right)
$$

From the question

$$

P(X \geq 1) > 0.9
$$

We can re-write this as

$$

1 - P(X = 0) > 0.9 \implies P(X = 0) < 0.1
$$

Using the distribution $X \sim B(n, 0.08)$

$$

{n \choose 0} \times (0.08)^0 \times (0.92)^n < 0.1
$$

$$

(0.92)^n < 0.1
$$

As $0.92 < 1$, the inequality is flipped when we apply the logarithmic function

$$

n  > log_{0.92}(0.1)
$$

$$

 n > 27.6
$$

So the smallest value of $n$ is 28.