## Newton’s Sums

* Newton’s sums can help us find the sum of roots for a polynomial.

We represent the recurrence model as

$$

S_n = \alpha^n + \beta^n + \gamma^n + \delta^n
$$

For example a quadratic equation, $ax^2 + bx + c = 0$, with roots $\alpha$ and $\beta$ can be represented using Newton’s sums:

$$
a(\alpha)^2 + b(\alpha) + c 
$$

$$
+
$$

$$
a(\beta)^2 + b(\beta) + c
$$

$$
=
$$

$$
aS_2 + bS_1 + 2c = 0
$$

This makes it easier to find higher powers of $S_n$, as in this example $S_2 = \frac{-bS_1 - 2c}{a}$.

### **Newton's sums for polynomials**


* Quadratic $(ax^2 + bx + c = 0)$
  * $S_n = \alpha^n + \beta^n$
  * $aS_2 + bS_1 + 2c = 0$
* Cubic $(ax^3 + bx^2 + cx + d = 0)$
  * $S_n = \alpha^n + \beta^n + \gamma^n$
  * $aS_3 + bS_2 + cS_1 + 3d = 0$
* Quartic $(ax^4 + bx^3 + cx^2 + dx + e = 0)$
  * $S_n = \alpha^n + \beta^n + \gamma^n + \delta^n$
  * $aS_4 + bS_3 + cS_2 + dS_1 + 4e = 0$


### **Newton's sums after transformations**

* It is also important to note how an **exponential transformation** can change the results obtained by using **Newton’s sums**:

| Transformation | Substitution | Original sum | New sum |
|----|----|----|----|
| $\alpha^m$ | $x = \sqrt[m]{y}$ | $S_n$ | $S_{\frac{n}{m}}$ |
| $\sqrt[m]{\alpha}$ | $x = y^m$ | $S_n$ | $S_{nm}$ |





---

---


<span class="underline">Question:</span>

**The Cubic Equation** $z^{3} - z^{2} - z - 5 = 0$ **has roots**
$\alpha$**,** $\beta$ **and**$\gamma$

1)  **Show that** $\alpha^{3} + \beta^{3} + \gamma^{3} = 19$

2)  **Find the value of**
    $\mathbf{\alpha}^{\mathbf{4}} + \mathbf{\beta}^{\mathbf{4}} + \mathbf{\gamma}^{\mathbf{4}}$

<center>Solution:</center>

We can use Recurrence Notation since:

$$S_{3} = \alpha^{3} + \beta^{3} + \gamma^{3}$$

Find $S_{1}$and $S_{2}$ from the polynomial:

$$S_{1} = 1$$

Using
$S_{2} = \left( \sum_{}^{}\alpha \right)^{2} - 2\sum_{}^{}\alpha\beta$

$$S_{2} = \left( 1 \right)^{2} - 2\left( - 1 \right) = 3$$

From our polynomial, we know that:

$$S_{3} - S_{2} - S_{1} - 15 = 0$$

Substitute in values and find $S_{3}$

$$S_{3} - \left( 3 \right) - \left( 1 \right) - 15 = 0$$

$$\rightarrow S_{3} = 15 + 3 + 1$$

$$\rightarrow S_{3} = 19\mathbf{\quad}\mathrm{(Ans\ for\ a)}$$

In order to find $S_{4}$, we will need to use a substitution, we
will be letting $y = z^{2} \rightarrow z = \sqrt{y}$

Rearrange the terms:

$$z^{3} - z = z^{2} + 5$$

Square both sides:

$$z^{6} - 2z^{4} + z^{2} = z^{4} + 10z^{2} + 25$$

Rearrange the terms back and substitute in $z = \sqrt{y}$

$$z^{6} - 3z^{4} - 9z^{2} - 25 = 0$$

$$\rightarrow y^{3} - 3y^{2} - 9y - 25 = 0$$

$S_{2}$ in the new equation is $S_{4}$ in the old
equation

$$\mathbf{S}_{\mathbf{2}} = \left( \mathbf{3} \right)^{\mathbf{2}} - \mathbf{2}\left( - \mathbf{9} \right) = \mathbf{27}\mathbf{\quad}\mathrm{(Ans\ for\ b)}$$


