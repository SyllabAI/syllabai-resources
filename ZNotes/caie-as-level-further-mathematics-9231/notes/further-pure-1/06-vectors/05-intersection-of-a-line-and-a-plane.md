## Intersection of a line and a plane
There are 3 cases for the intersection of a line and a plane

### **No points of intersection**

![Screenshot 2024-11-03 at 3.58.38 PM.png](../../../assets/3529f0a4b6f9-67274100880fbf3c79d48d00dd2e5cf3fb40fefc25c0b8fb.58)

- The line and the plane are **parallel** and have no points of intersection.
  - The direction vector of the line is perpendicular to the plane's normal vector

Given a line $r = a_1i + a_2j + a_3k + \lambda(b_1i + b_2j + b_3k)$ and a plane $c_1x + c_2y + c_3z = d$
$$
\begin{pmatrix}
   b_1 \\
   b_2 \\
b_3 \\
\end{pmatrix}
\cdot
\begin{pmatrix}
   c_1 \\
   c_2 \\
c_3
\end{pmatrix}
= b_1c_1 + b_2c_2 + b_3c_3 = 0
$$
### **One point of intersection**

![Screenshot 2024-11-03 at 3.57.24 PM.png](../../../assets/b8def5d2ba52-67274100880fbf3c79d48d0024ac402d37c80909b1b0d071.57)

- The line and the plane have **one** point of intersection

To find the coordinates of the point of intersection
- Find the general coordinate of the line
- Substitute this into the equation of the plane, and solve for the unknown variable
- Substitute in the value of the unknown variable back into the general coordinate of the line to get the coordinates


### **Line lies in the plane**

![Screenshot 2024-11-03 at 4.12.21 PM.png](../../../assets/9d8ca8963f69-67274100880fbf3c79d48d00834da7bb434645b28546e9fa.12)

- The line lies inside the plane
  - The line is parallel and all the points on the line also lie on the plane
 
- To show that a line and a plane are parallel, the dot product of the direction vector of the line and the perpendicular vector to the plane must equal 0.
  - You must also show a point that lies on the plane by substituting in a coordinate from the line into the plane.



---

**<center>Example 1</center>**
Find the point of intersection of the line $r = 2i + 3j + 4k + \lambda(i + 2j - k)$ and the plane $5x + y - z = 1$.
**<center>Answer</center>**
First we find the general coordinates of any point on the line
$$
r = (2 + \lambda)i + (3 + 2\lambda)j + (4 - \lambda)k
$$
Next we substitute in these values into the plane
$$
5(2 + \lambda) + (3 + 2\lambda) - (4 - \lambda) = 1
$$
Solving for $\lambda$, we get
$$
8\lambda = -8 \implies \lambda = -1
$$
Now we substitute in this value of $\lambda$ into the equation of the line
$$
r = (2 + (-1))i + (3 + 2(-1))j + (4 - (-1))k = i + j + 5k
$$
So the point of intersection is $(1, 1, 5)$. We can verify this value by substituting it into the plane and see if it satisfies the equation
$$
5(1) + 1 - 5 = 1
$$

**<center>Example 2</center>**
Show that the line $r = 2i + j + \mu(3i + j - 2k)$ lies in the plane $2x  + 4y + 5z = 8$.
**<center>Answer</center>**
We first show that the line and plane are parallel.
$$
\begin{pmatrix}
   3 \\
   1 \\
-2 \\
\end{pmatrix}
\cdot
\begin{pmatrix}
   2 \\
   4 \\
5
\end{pmatrix}
= 3(2) + 1(4) + -2(5) = 0
$$
As they are parallel, we can now show a point that lies on the plane. 
We can do this by letting $\mu = 1$
$$
r = 2i + j + 1(3i + j - 2k) = 5i + 2j - 2k
$$
Next we will substitute in this point into the equation of the plane, and see if its satisfies the equation
$$
2(5) + 4(2) + 5(-2) = 8
$$
As the line and plane are parallel, and the point $(5, 2, -2)$ lie on the plane, the line lies in the plane.
