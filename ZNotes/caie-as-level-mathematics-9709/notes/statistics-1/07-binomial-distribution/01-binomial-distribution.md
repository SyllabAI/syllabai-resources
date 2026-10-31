# Binomial Distribution

* A binomial distribution is a **discrete distribution** that is modelled using two parameters
  * The number of **finite trials** $n$
  * The **constant** probability of success $p$
* The conditions for a model to follow a Binomial distribution:
  * **Finite** number of trials, denoted by $n$
  * Only **2 possible outcomes**, success and failure
  * Probability of success, $p$, is **constant** in each trial
  * Outcomes of each trial are **independent** of each other




### **Finding probability using the distribution**

* We say a continuous random variable, $X$, follows a binomial distribution $B(n, p)$. This is written as

$$

X \sim B(n, p)
$$

The probability of the random variable $X$ having $x$ success in $n$ trials can be found using:

$$
P(X=x)=\binom{n}{x} \times p^x \times (1-p)^{n-x} \quad[\text{Given in MF19}]
$$

Here:

* $x$ is a positive integer.
  * $x$ = 0, 1, 2, $\cdots$, n
* $(1 - p)$ denotes the probability of a failure
  * It is also denoted by $q$




### **Mean and Variance**

* To calculate the **expected value**, or the mean, of a random variable following a binomial distribution, we can use the formula

$$
E(X)=\mu=np
$$

* To calculate the **variance** of a random variable following a binomial distribution, we can use the formula

$$
Var(X) = \sigma^{2} = np(1 - p)
$$



