# Permutations and Combinations

## Factorial

The factorial for a positive integer $n$ can be expanded as

$$

n! = n \times (n - 1) \times (n - 2) \times \cdots \times 3 \times 2 \times 1
$$

An interesting result obtained from factorials is

$$

0! = 1
$$

* A calculator can also be used to compute the value of a factorial.


---

**<center>Example 1</center>**

Compute the value of $5!$

**<center>Answer</center>**

$$

5! = 5 \times 4 \times 3 \times 2 \times 1 = 120
$$

**<center>Example 2</center>**

Compute the value of $\frac{100!}{98!}$

**<center>Answer</center>**

We can re-write the numerator as

$$

100 \times 99 \times 98 \times 97 \times \cdots \times 3 \times 2 \times 1 \implies 100 \times 99 \times 98!
$$

So the fraction is

$$

\frac{100 \times 99 \times 98!}{98!}
$$

Clearly $98!$ cancels out in the numerator and denominator, leaving us with

$$

\frac{100 \times 99 \times \cancel{98!}}{\cancel{98!}} = 100 \times 99
$$

So the value we get is

$$

\frac{100!}{98!} = 100 \times 99 = 9900
$$



