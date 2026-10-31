## Finding the equation of a plane
### **Finding the equation of the plane when given three position vectors**

Given three position vectors, a, b, and c, we can find the equation of the plane which passes through all three points. 

- First identify a known point to the plane, $\overrightarrow{OA}$
- Next find two vectors which are on the plane
  - These two vectors are $\overrightarrow{AB}$ and $\overrightarrow{AC}$
- Put them in the form of the plane equation

$$
r = \overrightarrow{OA} + \lambda \left(\overrightarrow{OB} - \overrightarrow{OA} \right) + \mu \left(\overrightarrow{OC} - \overrightarrow{OA}\right)
$$
$$
r = \overrightarrow{OA} + \lambda\overrightarrow{AB} + \mu\overrightarrow{AC}
$$

### **Finding the cartesian equation of a plane**

Given a plane equation
$$
r = \begin{pmatrix}
   a_1 \\
   a_2 \\
a_3
\end{pmatrix} + \lambda\begin{pmatrix}
   b_1 \\
   b_2 \\
b_3
\end{pmatrix} + \mu\begin{pmatrix}
   c_1 \\
c_2 \\
c_3
\end{pmatrix}
$$

We can find the common perpendicular to the plane by finding the cross product of the two direction vectors.

$$
\begin{vmatrix}
   i & j & k \\
b_1 & b_2 & b_3 \\
c_1 & c_2 & c_3
\end{vmatrix}

= 
\begin{pmatrix}
   e \\
   f \\
g
\end{pmatrix}
$$

We can use the values obtained to write the cartesian equation of the plane
$$
ex + fy + gz = d
$$

To find the value of $d$, we can input the position vector of a known point as it must satisfy the vector equation.
$$
e(a_1) + f(a_2) + g(a_3) = d
$$
After finding the value of $d$, we re-write the equation of the plane.



---


**<center> Example </center>**

The points $A$, $B$, $C$ are three position vectors
$$
-i + j + 2k, ~ -2i - j, ~ 2i + 2k
$$

Find the equation of the plane $ABC$, giving your answer as a cartesian equation.

**<center> Answer </center>**
- First we identify a known position vector to the plane, lets say $A$.
- Next we need to find two non parallel vectors to the plane

$$
\overrightarrow{AB} = \overrightarrow{OB} - \overrightarrow{OA} = -2i - j - (-1 + j + 2k) = -i - 2j - 2k
$$

$$
\overrightarrow{AC} = \overrightarrow{OC} - \overrightarrow{OA} = 2i + 2k - (-1 + j + 2k) = 3i - j 
$$

This gives us the plane
$$
r = -i + j + 2k + \lambda(-i - 2j - 2k) + \mu(3i - j)
$$

Now we can find the vector perpendicular to the plane by finding the cross product of the direction vectors


$$
\begin{vmatrix}
   i & j & k \\
1 & 2 & 2 \\
3 & -1 & 0
\end{vmatrix}

= 
\begin{pmatrix}
   -2 \\
   -6 \\
7
\end{pmatrix}
$$

$$
-2x - 6y + 7z = d
$$
Next, we input the position vector of the known point to find the value of $d$
$$
-2(-1) - 6(1) + 7(2) = 10
$$
$$
-2x - 6y + 7z = 10
$$

