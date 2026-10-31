# Logarithmic & Exponential Functions

## Introduction

### **Definition**

* for $a > 0$ and $a ≠ 1$

$$
y = a^{x} \Leftrightarrow x = \log_ay
$$

* For $\log_ay$ to be defined

* $y > 0$ and $a > 0$, $a$ ≠ $1$

When the logarithms are defined

$$
\log_a1 = 0\ \ \ \ \ \ \ \ \ \ \ \ \log_ab + \log_ac \equiv \log_a\text{bc}
$$

$$
\log_aa = 1\ \ \ \ \ \ \ \ \ \ \ \ \ \log_ab - \log_ac \equiv \log_a\frac{b}{c}
$$

$$
\log_a{b \equiv \frac{\log b}{\log a}}\ \ \ \ \ \ \ \ \ \ \ \ \ \log_a{b^{n} \equiv n\log_ab}
$$

When solving logarithmic equations, check solution with original
equation and discard any solutions that cause the logarithm to be undefined.

Solution of $a^{x} = b$ where $a$ ≠ $- 1,\ 0,\ 1$

If $b$ can be easily written as $a^{n},$ then

$$
a^{x} = a^{n} \Rightarrow x = n
$$

Otherwise take logarithms on both sides, i.e.

$$
\log a^{x} = \log b\ \text{and so}\ x = \frac{\log b}{\log a}
$$

$\log{\Rightarrow \log_{10}\ }$

$\ln\  \Rightarrow \log_e\ $ (also known as natural log)

**Change of base rule:**

$$
\log_a\left( x \right) = \frac{\log_b(x)}{\log_b(a)}
$$

Sometimes equations involve logs of awkward bases. Converting to a common base makes it easier to solve.

Most calculators only have $\log$ (base 10) and $\ln$ (base $e$). To compute something like $\log_2 8$, you use the base change rule: $\log_2 8 = \frac{\log 8}{\log 2}$.

**Example**:

Solve for $ x $ in the equation:
$$
\log_3(2x + 5) + \log_3(x - 1) = 2
$$

**Step 1**: Use the product law of logarithms:

$\log_3(2x + 5) + \log_3(x - 1) = \log_3\big((2x + 5)(x - 1)\big)$

So the equation becomes:\
$
\log_3\big((2x + 5)(x - 1)\big) = 2
$

**Step 2**: Remove the logarithm by converting to exponential form

$(2x + 5)(x - 1) = 3^2 = 9$

**Step 3**: Expand and solve the quadratic\
$(2x + 5)(x - 1) = 9$

$2x^2 - 2x + 5x - 5 = 9$

$2x^2 + 3x - 5 = 9$

$2x^2 + 3x - 14 = 0$

**Step 4**: Solve the quadratic using the quadratic formula\
$
x = \frac{-3 \pm \sqrt{3^2 - 4(2)(-14)}}{2(2)} = \frac{-3 \pm \sqrt{9 + 112}}{4} = \frac{-3 \pm \sqrt{121}}{4}
$

$x = \frac{-3 \pm 11}{4} \Rightarrow x = 2,\quad x = -3.5$

**Step 5**: Check for invalid solutions

We must have:
$
2x + 5 > 0 \Rightarrow x > -2.5
$
$
x - 1 > 0 \Rightarrow x > 1
$

Only $ x = 2 $ satisfies both conditions.

**Final Answer**:
$
x = 2
$