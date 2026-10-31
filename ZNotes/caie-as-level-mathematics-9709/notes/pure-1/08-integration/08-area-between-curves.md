## Area between curves

- The area between two curves can be found by finding the difference of the areas of the top curve and bottom curve.

![Screenshot 2024-09-08 at 7.00.42 PM.png](../../../assets/579c438ec0a6-66dd98382d782f76461bd874137386bef0c36c3cd24de4e4.00)

We can find the area between two curves as such
$$
\int_{a}^{b} f(x) - g(x) ~dx \quad [\text{Where} ~a \leq x \leq b]
$$


- While finding the area between two curves, it is important to identify which function is on top and on the bottom.
    - You may also need to find their points of intersection, and use them as the upper and lower limit in questions.



---

**<center>Example</center>**

The curve $y = 3\sqrt{x}$ and the line $y = x$ intersect at the origin $O$ and the point $P$. 

![Screenshot 2024-09-08 at 7.41.26 PM.png](../../../assets/e9594d63d868-66dd98382d782f76461bd87408ff9eaa4d922ff2e9ac6b71.41)

Find the area of the shaded region.


**<center>Answer</center>**
We must first find the points of intersection, to use them as our limits. The point $O$ has coordinates $(0, 0)$. To find the $x$-coordinate of the point $P$, we must equate both curves.
$$
3\sqrt{x} = x \implies x = 9
$$
The point $P$ has coordinates $(9, 9)$.
**<center>Method 1</center>**
Next we notice that curve $y = 3\sqrt{x}$ is above the line $y = x$. So we subtract the area of the line from the curve.

$$
\int_{0}^{9} 3\sqrt{x} ~dx - \int_{0}^{9} x ~dx = \int_{0}^{9} 3\sqrt{x} - x ~dx
$$
$$
\left( 2x^{\frac{3}{2}} - \frac{x^2}{2} \right)_{0}^{9}
$$
$$
0 - \left( 2(9)^{\frac{3}{2}} - \frac{9^2}{2} \right) = 13.5
$$
The area between the two curves is 13.5.

**<center>Method 2</center>**
Next we notice that curve $y = 3\sqrt{x}$ is above the line $y = x$. So we subtract the area of the line from the curve. The line is a triangle with base length $9$ and height $9$.

$$
\int_{0}^{9} 3\sqrt{x} ~dx ~ - ~ \left( \frac{1}{2} \times 9 \times 9 \right)
$$

$$
(2x^{\frac{3}{2}})_{0}^{9} - \left( \frac{81}{2} \right) = 2(9)^{\frac{3}{2}} - \frac{81}{2} = 13.5
$$
The area between the two curves is 13.5.




