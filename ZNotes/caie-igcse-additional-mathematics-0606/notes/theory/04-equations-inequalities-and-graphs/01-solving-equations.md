# Equations, Inequalities and Graphs

## **Solving Equations**

### **Solving Equations by Elimination**

**1.Equation of the form:**
$$
\|ax + b\| = c
$$

* Where: $c \geq 0$

* Split into **two** cases:

  * $
    ax + b = c
    $

  * $
    ax + b = -c
    $

**Example:** $\|2x - 3\| = 5$

* Case 1:

  $
  2x - 3 = 5
  $

  $
  2x = 8
  $

  $
  x = 4
  $

* Case 2:

  $
  2x - 3 = -5
  $

  $
  2x = -2
  $

  $
  x = -1
  $

Solution:$x = 4 \quad \text{or} \quad x = -1$

---

**2.Equation of the form:**

$$
\|ax + b\| = cx + d
$$

* Split into **two** cases:

  * $
    ax + b = cx + d
    $

  * $
    -(ax + b) = cx + d
    $

**Example:**$\|x - 2\| = 3x + 1$

* Case 1:

  $
  x - 2 = 3x + 1
  $

  $
  -2 = 2x + 1
  $

  $
  -3 = 2x
  $

  $
  x = -1.5
  $

  However, the right-hand side is negative so -1.5 will be rejected.

* Case 2:

  Check if right-hand side is valid (i.e., non-negative):

  $
  -(x - 2) = 3x + 1
  $

  $
  -x + 2 = 3x + 1
  $

  $
  1 = 4x
  $

  $
  x = 0.25
  $

Solution:$x = 0.25$

---

**3. Equation of the form:**

$$
\|ax + b\| = \|cx + d\|
$$

* Consider **four** cases:

  * $
    ax + b = cx + d
    $

  * $
    ax + b = -(cx + d)
    $

  * $
    -(ax + b) = cx + d
    $

  * $
    -(ax + b) = -(cx + d)
    $

**Example:** $\|2x + 1\| = \|x - 3\|$

* Case 1:

  $
  2x + 1 = x - 3
  $

  $
  x = -4
  $

* Case 2:

  $
  2x + 1 = -(x - 3)
  $

  $
  2x + 1 = -x + 3
  $

  $
  3x = 2
  $

  $
  x = \frac{2}{3}
  $

* Case 3:

  $
  -(2x + 1) = x - 3
  $

  $
  -2x - 1 = x - 3
  $

  $
  -3x = -2
  $

  $
  x = \frac{2}{3}
  $

* Case 4:

  $
  -(2x + 1) = -(x - 3)
  $

  $
  -2x - 1 = -x + 3
  $

  $
  x = -4
  $

Solution: $x = -4 \quad \text{or} \quad x = \frac{2}{3}$

---

**4.Equation of the form:**

$$
\|ax^2 + bx + c\| = d
$$

* Split into **two** cases:

  * $
    ax^2 + bx + c = d
    $

  * $
    ax^2 + bx + c = -d
    $

**Example:** $\|x^2 - 4x + 3\| = 2$

* Case 1:

  $
  x^2 - 4x + 3 = 2
  $

  $
  x^2 - 4x + 1 = 0
  $

  Use the quadratic formula:

  $
  x = \frac{4 \pm \sqrt{(-4)^2 - 4(1)(1)}}{2(1)}
  $

  $
  x = \frac{4 \pm \sqrt{16 - 4}}{2}
  $

  $
  x = \frac{4 \pm \sqrt{12}}{2}
  $

  $
  x = 2 \pm \sqrt{3}
  $

* Case 2:

  $
  x^2 - 4x + 3 = -2
  $

  $
  x^2 - 4x + 5 = 0
  $

  Discriminant:

  $
  (-4)^2 - 4(1)(5) = 16 - 20 = -4
  $

  No real solutions.

Solution:$x = 2 + \sqrt{3} \quad \text{or} \quad x = 2 - \sqrt{3}$

---

### **Solving Equations by Substitution**

**Example:** $x^4 - 5x^2 + 6 = 0$

* Let:$u = x^2$

* Then the equation becomes:

  $$
  u^2 - 5u + 6 = 0
  $$

* Solve the quadratic:

  $
  u^2 - 5u + 6 = 0
  $

  $
  (u - 2)(u - 3) = 0
  $

  So, **$u = 2 \quad \text{or} \quad u = 3$**

* Back-substitute:

  Since $u = x^2$,

  * Case 1:

    $
    x^2 = 2 \Rightarrow x = \pm\sqrt{2}
    $

  * Case 2:

    $
    x^2 = 3 \Rightarrow x = \pm\sqrt{3}
    $

Final solution:$x = \pm\sqrt{2},\ \pm\sqrt{3}$