## Definite Integration

- A definite integral is an integral that is described by an upper and lower limit.

$$
\textbf{Fundamental Theorem of Calculus}
$$

$$
\int_{x=b}^{x=a} f(x),dx = [F(x)]_{b}^{a} = F(a) - F(b) \quad \left\[\text{Where } b \leq x \leq a\right\]
$$

Where:

- $a$ is the upper limit.
- $b$ is the lower limit.
- Note that adding the arbitrary constant is not necessary in definite integration as it will get cancelled out.

### **Basics of Definite Integration**

- The upper and lower limit **must be the same** for this rule to apply

**Sum and Difference rule**

$$
\int_{b}^{a} f(x) \pm g(x),dx = \int_{b}^{a} f(x),dx \pm \int_{b}^{a} g(x),dx
$$

**Scalar multiple rule**

$$
\int_{b}^{a} z f(x),dx = z \times \int_{b}^{a} f(x),dx \quad \left\[\text{Where } z \text{ is a constant number}\right\]
$$

**Change of limits rule**

$$
\int_{b}^{a} f(x),dx = -\int_{a}^{b} f(x),dx
$$

**We also come across some useful results**

$$
\int_{a}^{a} f(x),dx = 0
$$

$$
\int_{a}^{b} f(x),dx + \int_{b}^{c} f(x),dx = \int_{a}^{c} f(x),dx \quad \left\[\text{Where } a < b < c \text{ and } f(x) > 0\right\]
$$

---

**Example**

Compute the value of $\displaystyle\int_{2}^{4} 3x^3 - 4x^2 + 2x + 5,dx$.

**Answer**

We first start by integrating.

$$
\int_{2}^{4} 3x^3 - 4x^2 + 2x + 5,dx = \left\( \frac{3x^{3+1}}{3+1} - \frac{4x^{2+1}}{2+1} + \frac{2x^{1+1}}{1+1} + 5x \right\)\Bigg|_{2}^{4}
$$

This simplifies to

$$
\left\( \frac{3x^4}{4} - \frac{4x^3}{3} + x^2 + 5x \right\)\Bigg|_{2}^{4}
$$

Now we can substitute in the upper and lower limit as such

$$
\left\( \frac{3(4)^4}{4} - \frac{4(4)^3}{3} + (4)^2 + 5(4) \right\) - \left\( \frac{3(2)^4}{4} - \frac{4(2)^3}{3} + (2)^2 + 5(2) \right\)
$$

$$
\left\(\frac{428}{3}\right\) - \left\(\frac{46}{3}\right\) = \frac{382}{3}
$$

$$
\int_{2}^{4} 3x^3 - 4x^2 + 2x + 5,dx = \frac{382}{3}
$$