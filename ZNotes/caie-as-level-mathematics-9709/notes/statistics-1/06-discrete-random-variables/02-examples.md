## Examples

### **<center> Example 1</center>**
A fair 6-sided dice has the numbers 1, 2, 2, 3, 3, 3 on its 6 sides. The die is rolled twice. The random variable $X$ denotes the sum of of the two numbers obtained. Draw the probability distribution table for $X$, and find the mean and variance of $X$.
### **<center>Answer</center>**
The random variable $X$ is the sum of two numbers obtained after rolling the die. Using this, we know that the values $X$ can take are:
$$
1 + 1 = 2, ~ 1 + 2 = 3, ~ 1 + 3 = 4, ~ 2 + 3 = 5, ~ 3 + 3 = 6
$$
- Note that other combinations exist to obtain the same values listed above.

Now we can find the probability of the random variable $X$ taking up each value using a probability space diagram. Each row and column, apart from the first one, represents the sum of the two faces obtained.

|  | 1 | 2 | 2     | 3     | 3     | 3     |
| -------- | -------- | -------- | -------- | -------- | -------- | -------- |
| 1    | 2     | 3     | 3     | 4     | 4     | 4     |
| 2     | 3     | 4     | 4     | 5     | 5     | 5     |
| 2     | 3     | 4     | 4     | 5     | 5     | 5     |
| 3     | 4     | 5     | 5     | 6     | 6     | 6     |
| 3     | 4     | 5     | 5     | 6     | 6     | 6     |
| 3     | 4     | 5     | 5     | 6     | 6     | 6     |

Using 
$$
\text{Probability} = \frac{\text{Favourable outcomes}}{\text{Total outcomes}}
$$
We can draw the probability distribution table for $X$ as:
![Screenshot 2024-09-12 at 4.08.44 PM.png](../../../assets/c49e1f3e8a2a-66e2c0d786c2d165d1f97d9f2f5ac0b48437bbb3506b1431.08)

- We also note that all the probabilities in the table add upto 1.
$$
\phantom{invis}
$$
To find the mean and variance, we use the probability distribution table.
$$
E(X) = \frac{2 \times 1}{36} + \frac{3 \times 4}{36} + \frac{4 \times 10}{36} + \frac{5 \times 12}{36} + \frac{6 \times 9}{36} = \frac{14}{3}
$$
To find the variance, we first find $\sum x^2_ip_i$.
$$
\sum x^2_ip_i = \frac{(2)^2 \times 1}{36} + \frac{(3)^2 \times 4}{36} + \frac{(4)^2 \times 10}{36} + \frac{(5)^2 \times 12}{36} + \frac{(6)^2 \times 9}{36} = \frac{206}{9}
$$
We subtract this value from the mean squared to find the variance
$$
Var(X) = \frac{206}{9} - \left( \frac{14}{3} \right)^2 = \frac{10}{9}
$$



---

### **<center> Example 2</center>**
The random variable $X$ takes the values -1, 1, 2, 3 only. The probability that $X$ takes the value $x$ is
$$
P(X = x) = kx^2 \quad [\text{Where} ~ k ~ \text{is a constant}]
$$
Draw the probability distribution table for $X$, in terms of $k$, and find the value of $k$.
### **<center>Answer</center>**
We can draw the probability distribution table by inputting the values which $X$ can take.
$$
P(X = -1) = k(-1)^2 = k, ~ P(X = 1) = k(1)^2 = k
$$
$$
P(X = 2) = k(2)^2 = 4k, ~ P(X = 3) = k(3)^2 = 9k
$$

So the probability distribution table is:
![Screenshot 2024-09-12 at 4.22.16 PM.png](../../../assets/04379f08f322-66e2c0d786c2d165d1f97d9f53cfc2e24d0475b0e62fa5ef.22)

To find the value of $k$, we make use of the fact that the sum of probabilities in a probability distribution table must add upto 1.
$$
k + k + 4k + 9k = 1 \implies 15k = 1
$$
Solving for $k$:
$$
k = \frac{1}{15}
$$