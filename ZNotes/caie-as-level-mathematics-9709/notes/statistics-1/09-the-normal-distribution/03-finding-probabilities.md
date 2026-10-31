## Finding Probabilities

- The standard normal distribution can be used to find the probability of an event occurring.
   - The notation for the **area** to the **left** of $z$ is $\phi(z)$.

Consider a standard normal distribution, $X \sim N(0, 1)$, where you want to find $P(z \leq a)$.

![Screenshot 2024-09-09 at 11.41.51 AM.png](../../../assets/29c0b4d80c93-66c3f770edfdad19c845f4ac3fe50b821c55a87eea20a34c.41)

We can use the standard normal table to find the value of $a$, and match it with the corresponding probability.

![Screenshot 2024-09-09 at 11.45.59 AM.png](../../../assets/f8d7fe919058-66c3f770edfdad19c845f4acd1718b6ad3eebf3e6421fae3.45)

- The left side of the table gives us a decimal value, and the right side of the table gives us the value we need to add to the decimal value.
   - The reverse of this process can be used to find the $z$ value from a given area.



Let $a$ be equal to **1.645** in this example. Using the table above, given in MF19, we can find the corresponding probability for $\phi(1.645)$ as such:

![Screenshot 2024-09-09 at 11.50.21 AM.png](../../../assets/7864556c41a0-66c3f770edfdad19c845f4ac8ecceea841474a7de334a417.50)

Using the table:
$$
\phi(1.645) = 0.9495 + 0.0005 = 0.95
$$

- This also represents 95% of the area under the graph.
- The **mean value** can be found by probability $\times$ sample space.


### **Symmetry of the Distribution**
- The mean, $\mu$, acts as a line of symmetry for the normal distribution.

- A $z$ value less than the mean will have a **negative value**.

Given a probability $P(z \geq a)$ or $P(z \leq -a)$



![Screenshot 2024-09-09 at 1.59.14 PM.png](../../../assets/4f3d501bf4bb-66c3f770edfdad19c845f4acc9872c57b036f2eed07c27a6.59)

We can find the value by: 
$$
1 - P(z \leq a)
$$

Some other useful results are listed below

| Probability | Area |  
| -------- | -------- | 
| $P(z < a)$     | $\phi(a)$     |
| $P(z > a) = 1 - P(z < a)$    | $1 - \phi(a)$     |
| $P(z > -a) = P(z < a)$ | $\phi(a)$ |
| $P(z < -a) = 1 - P(z < a)$ | $1 - \phi(a)$ |

- It is also important to know that $P(z = a) = 0$ due to the continuous random variable being continuous.  



### **Area in between two values**

- The area in between two values can be found by subtracting the two areas.

![Screenshot 2024-09-09 at 2.22.26 PM.png](../../../assets/4d0bc15baa83-66c3f770edfdad19c845f4ac9f18248fd4c3897425fb6ee1.22)


Some useful results are listed below

| Probability | Area | 
| -------- | -------- | 
| $P(a \leq z \leq b)$    | $\phi(b) - \phi(a)$    | 
| $P(-a \leq z \leq -b)$     | $\phi(a) - \phi(b)$     |
| $P(-a \leq z \leq b)$ | $\phi(b) + \phi(a) - 1$ |
| $P(-a \leq z \leq a)$ | $2\left(\phi(a) \right) - 1$|





---





**<center><span class="underline">Example</span></center>**

For a random variable $X$ with normal distribution

$$X\ \sim\ N(20,\ 4^{2})$$

1)  Find the probability of $P(X \leq 25)$
2)  Find the probability of $P(X \geq 25)$
3)  Find the probability of $P(X \leq 12)$
4)  Find the probability of $P(10 \leq X \leq 30)$
**<center>Answer</center>**

1.  Find the probability of $P(X \leq 25)$

First we standardize the probability

$$Z = \frac{25 - 20}{4} = 1.25$$

Search for this value in normal tables

$$\Phi\left( 1.25 \right) = 0.8944$$

2)  Find the probability of $P(X \geq 25)$

Change from greater than to less than using:

$$P\left( Z \geq a \right) = 1 - P\left( Z \leq a \right)$$

$P\left( X \geq 25 \right) = 1 - P(X \leq 25$)

Using the probability from above

$$P\left( X \geq 25 \right) = 1 - 0.8944 = 0.1057$$

3)  Find the probability of $P(X \leq 12)$

Standardize the probability

$$Z = \frac{12 - 20}{4} = - 2$$

Change from negative value to positive by:

$$P\left( Z \leq - a \right) = 1 - P(Z \leq a)$$

$$P\left( Z \leq - 2 \right) = 1 - P\left( Z \leq 2 \right)$$

Search for 2 in the normal tables

$$P\left( Z \leq - 2 \right) = 1 - 0.9773 = 0.0228$$

4)  Find the probability of $P(10 \leq X \leq 30)$

Split inequality into two using:

$$P\left( a \leq Z \leq b \right) = P\left( Z \leq b \right) - P\left( Z \leq a \right)$$

$$P\left( 10 \leq X \leq 30 \right) = P\left( X \leq 30 \right) - P\left( X \leq 10 \right)$$

Standardize the values

$$= P\left( Z \leq 2.5 \right) - P\left( Z \leq - 2.5 \right)$$

Convert the negative values to positive values

$$= P\left( Z \leq 2.5 \right) - \left( 1 - P\left( Z \leq 2.5 \right) \right)$$

Search for 2.5 in the normal table

$$= 0.9938 - \left( 1 - 0.9938 \right) = 0.9876$$
