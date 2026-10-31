

## Intersections of two planes

To find the equation of the intersection of two planes
- First find the cross product of the the normals of each plane
   - This will be our direction vector for the line
- Then, by equating a variable in the equation of a plane to 0, solve a simultaneous equation 
   - This will give us the position vector of the known point to both planes
  

---

**<center>Example</center>**
Find the vector equation of the line of intersection to the planes $x + 3y - z = 1$ and $2x + 4y + z = 6$.
**<center>Answer</center>**
First we find the direction vector using the cross product
$$
\begin{vmatrix}
   i & j & k \\
   1 & 3 & -1 \\
2 & 4 & 1
\end{vmatrix}
= 7i - 3j - 2k
$$

Next to find the position vector of the known point, we will set $x = 0$ for the plane equations. We can do this as both planes must pass through a point where one of the variables is equal to 0.

$$
3y - z = 1
$$
$$
4y + z = 6
$$
Solving this simultaneous equation gives us
$$
y = 1, z = 2, x = 0
$$

Thus, we get the equation of the line intersecting both planes as
$$
r = j + 2k + \lambda(7i - 3i - 2k)
$$
