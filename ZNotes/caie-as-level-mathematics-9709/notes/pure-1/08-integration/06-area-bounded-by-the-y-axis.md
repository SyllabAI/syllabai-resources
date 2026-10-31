## Area bounded by the $y$-axis

- To find the area bounded by the $y$-axis, we need to get an equation in terms of $y$, such as $x = F(y)$.
  - The limits must converted to $y$-values, if required.

![Screenshot 2024-09-04 at 3.21.11 PM.png](../../../assets/46b28bf6ca25-66d7e5133bc0c34099338bf50bedee95089eb184946c3c08.21)

- The definite integral below gives us the area bounded by the $y$-axis.
  $$
  \int_{y = c}^{y = d} f(y) , dy = F(d) - F(c) \quad \left[ \text{where} \quad c \leq y \leq d \right]
  $$

### **Area bounded left of the $y$-axis**

- The area bounded below the $y$-axis is negative, but the **positive value ** must be taken as area can never have a negative value

![Screenshot 2024-09-04 at 8.21.43 PM.png](../../../assets/3236d9edfe18-66d7e5133bc0c34099338bf5a80e87d37df359d458ae0d5d.21)

So the area left of the $y$-axis can be written as
$$

- \int_{c}^{d} f(y) \~dy
  $$

---

**<center>Example</center>**

A curve has the equation
$$
y = 2 + \sqrt{x + 3}
$$
![Screenshot 2024-09-07 at 7.16.32 PM.png](../../../assets/293959759686-66d7e5133bc0c34099338bf551c0f1d70c3426874136f2e2.16)
Find the area of the shaded region, bounded by the $y$-axis and the curve.

**<center>Answer</center>**
We start by making $x$ the subject of the formula
$$
x = (y - 2)^2 - 3 = y^2 - 4y + 1
$$

Next, find the corresponding $y$-values for the $x$ limits.
$$
y = 2 + \sqrt{1 + 3} = 4
$$
$$
y = 2 + \sqrt{13 + 3} = 6
$$

We can now begin by integrating, along with the upper and lower limit
$$
\int_{4}^{6} y^2 - 4y + 1 \~dy = \left( \frac{y^3}{3} - \frac{4y^2}{2} + y \right)_{4}^{6}
$$
Substituting in the limits gives us
$$
\left( \frac{(4)^3}{3} - 2(4)^2 + 4 \right) - \left(  \frac{(6)^3}{3} - 2(6)^2 + 6 \right) = \frac{38}{3}
$$
So the area of the shaded region is $\frac{38}{3}$.