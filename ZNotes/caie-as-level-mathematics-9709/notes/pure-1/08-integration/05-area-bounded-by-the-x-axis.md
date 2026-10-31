## Area bounded by the $x$-axis
Finding the area under a curve is an application of definite integration.

![Screenshot 2024-09-03 at 1.30.36 PM.png](../../../assets/451f5ceb75de-66d6b2551bdf4b27368ba7a474a570d4536f551a5b4cea38.30)

- The definite integral below gives us the area under the graph bounded by the $x$-axis.

$$
\int_{x ~ = ~ a}^{x ~ = ~ b} f(x) ~ dx = F(b) - F(a) \quad [\text{Where}~ a \leq x \leq b]
 
$$

- Here $f(x)$ must be in terms of $x$.

- Integrating a constant, such as $y = c$, with limits $a$ and $b$ will give you the area of a rectangle, bounded by the $x$-axis, with length $c$ and breadth $b - a$.

### **The area bounded below the $x$-axis**

- The area bounded below the $x$-axis is negative, but the **positive value** must be taken as area can never have a negative value.

![Screenshot 2024-09-04 at 8.20.46 AM.png](../../../assets/e7f047c9db4c-66d6b2551bdf4b27368ba7a4f44fd468b51f72980bc65b1a.20)
So the area under the $x$-axis can be written as
$$
- \int_{a}^{b} f(x) ~dx 
$$ 

$$
\phantom{invis}
$$

<center> To find the area under a graph as such: </center>

![Screenshot 2024-09-04 at 8.10.04 AM.png](../../../assets/195e3b47c488-66d6b2551bdf4b27368ba7a4b282b60d34168ce069df79a1.10)

We can use 3 different definite integrals
$$
\int_{a}^{b} f(x) ~dx - \int_{b}^{c} f(x) ~dx + \int_{c}^{d} f(x) ~ dx
$$



---

**<center>Example</center>**

A curve has the equation
$$
f(x) = \frac{4}{\sqrt{x}}
$$

![Screenshot 2024-09-04 at 8.34.40 AM.png](../../../assets/a7f89322301c-66d6b2551bdf4b27368ba7a4515fd634733484df18b031c2.34)

Find the area of the shaded region enclosed by the curve, the $x$-axis and the lines $x = 1$ and $x = 4$.


**<center>Answer</center>**

From the question
- $x = 4$ is the upper limit as it is the greater number.
- $x = 1$ is the lower limit as it is the smaller number.

Now we can integrate the function $f(x)$
$$
\int_{1}^{4} 4x^{-\frac{1}{2}} ~dx
$$
Upon integrating, we get
$$
\frac{4x^{- \frac{1}{2} + 1}}{-\frac{1}{2} + 1} = 8x^{\frac{1}{2}}
$$
Now we can substitute in our limits
$$
[ 8x^{\frac{1}{2}}]_{1}^{4} 
$$

$$
\left( 8(4)^{\frac{1}{2}} \right) - \left( 8(1)^{\frac{1}{2}} \right) = 8
$$

So the area of the shaded region is 8.