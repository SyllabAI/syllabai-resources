## Equation of a plane

Consider the image below 
![Screenshot 2024-10-29 at 11.23.17 AM.png](../../../assets/6cb172945f57-6710a942e9cbc15cbbb48525b3696f59472c76280ca716ac.23)


The equation of the plane can be written as
$$
r = a + \lambda b + \mu c
$$

Where:
- **r** is a position vector to any general point on the plane
- **a** is any position vector to the plane
- **b** and **c** are any non-parallel vectors in the plane
- $\lambda$ and $\mu$ can take the value of any real number to give all the positions on the plane


### **Equation of a plane using the dot product**

- The vectors $a$, $b$, $c$ lie on the same plane **if and only if** the dot product of vector $a$ and the perpendicular to vectors $b$ and $c$ equal $0$.

![Screenshot 2024-10-31 at 3.58.39 PM.png](../../../assets/137a7ac33b85-6710a942e9cbc15cbbb48525aaf534b77961634044ba07d8.58)

The three vectors lie on the same plane as
$$
(b \times c) \cdot a = 0
$$

Consider the image:

![Screenshot 2024-10-31 at 3.45.42 PM.png](../../../assets/e34bbf2ce776-6710a942e9cbc15cbbb48525df6720094273f518011b869f.45)


- The unit vector perpendicular to the plane, $\hat{n}$, is also perpendicular to the vector $r - a$. Thus, the dot product of these two vectors must equal 0. 

This implies that the vectors lie on the same plane, and as such, must meet the requirement above
$$
(r - a) \cdot \hat{n} = 0
$$

We can further expand the equation above to get
$$
r \cdot \hat{n} = a \cdot \hat{n}
$$
As $r$ represents a position vector to a **general point** on the plane, we can re-write it as column vector and find its dot product with $\hat{n}$
$$
\begin{pmatrix}
   x \\
   y \\
z
\end{pmatrix}
\cdot \hat{n} = n_1x + n_2y + n_3z
$$
As $a$ represents a position vector to a **known point** on the plane, we can find its dot product with $\hat{n}$ and get a constant, $d$, as its result
$$
a \cdot \hat{n} = d
$$

Now, we can write the equation of a vector plane as
$$
n_1x + n_2y + n_3z = d
$$
This is the **cartesian equation** for a vector plane
- The vector $(n_1, n_2, n_3)$ is the **perpendicular vector**, $\hat{n}$, to the plane
- $x$, $y$, $z$ determine the **direction** of the plane
- $d$ is the **location** of the plane, or its distance from the origin