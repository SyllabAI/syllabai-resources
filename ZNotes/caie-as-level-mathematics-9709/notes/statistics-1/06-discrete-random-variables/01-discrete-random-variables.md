# Discrete Random Variables

## Probability Distribution Tables

* The probability distribution of a discrete random variable lists the values that a random variable can take and shows the corresponding probabilities.

- The sum of all the probabilities in a probability distribution table always adds upto 1.
    -  This is useful when finding the values of unknown probabilities in the table.
 
Let $X$ represent a discrete random variable.
![Screenshot 2024-09-12 at 3.39.16 PM.png](../../../assets/ce7a58f095b2-66c3f770edfdad19c845f4d4d6a7c15f1b463a53b72fa333.39)

- In this example, $P(X = 1)$ would represent the probability when the random variable $X$ takes a value of 1. Looking at the probability distribution table, $P(X = 1) = \frac{2}{40}$.





### **Mean and Variance**

- The mean of a random variable is also called its expectation, or expected value.
    - $E(X)$ represents the expected value of the random variable $X$.

To find $E(X)$:
- Multiply the values that the random variable $X$ can take with the corresponding probability, sum up all the results to get the expectation.
$$
\mu = E\left( x \right)  = \sum x_ip_i \quad [\text{Given in MF19}]
$$

$$
\phantom{invis}
$$

- The variance of a random variable $X$ is denoted by Var(X).

To find $Var(X)$:
- Find the sum of the product of the squared values of the values the random variable $X$ can take with the corresponding probability. Subtract this value with the mean squared.

$$
\sigma^{2} = \sum x^2_ip_i - \left( E(X) \right)^2 \quad [\text{Given in MF19}]
$$



