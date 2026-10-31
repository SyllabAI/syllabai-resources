## Solving Cubic Inequalities

Consider inequalities of the form:

$$
f(x) \geq d, \quad f(x) > d, \quad f(x) \leq d, \quad f(x) < d
$$

where $ f(x) $ is a product of three linear factors, for example:

$$
f(x) = (x - a)(x - b)(x - c)
$$

and $ d $ is a constant.

**Steps to solve:**

1. **Rewrite the inequality**:\
   Move all terms to one side to analyze the sign:
   $$
   f(x) - d
   $$

2. **Find the roots by solving**:
   $$
   f(x) = d
   $$

   Which means:
   $$
   (x - a)(x - b)(x - c) = d
   $$

   $$
   (x - a)(x - b)(x - c) - d = 0
   $$

3. **Find the roots**:
   Solve for the values of $ x $ where:
   $$
   f(x) = d \quad \Rightarrow \quad x_1, x_2, x_3
   $$

4. **Draw or analyze the graph**:

   - The function crosses the line $ y = d $ at the points $ x_1, x_2, x_3 $.
   - Between the roots, the value of $ f(x) $ changes sign (positive/negative).
   - Since it's a cubic function, the sign alternates across the roots.

5. **Determine where the inequality holds**:

   - Check each interval between the roots.
   - Identify where the expression is greater than, less than, or equal to $ d $, depending on the inequality.

6. **Write the solution set**:

   - Based on your sign analysis, write the intervals where the inequality is true.
   - Use open or closed intervals depending on whether the inequality is strict $(<, >)$ or inclusive $( \leq, \geq )$

**Example:**

Solve the inequality:

$$
(x - 1)(x + 2)(x - 4) \leq 0
$$

**Step 1: Find the roots**

Set the expression equal to zero:

$$
(x - 1)(x + 2)(x - 4) = 0
$$

So the roots are:

$$
x = -2,\quad x = 1,\quad x = 4
$$

**Step 2: Split the number line into intervals**

The critical points divide the number line into four intervals:

- $x < -2$
- $-2 < x < 1$
- $1 < x < 4$
- $x > 4$

**Step 3: Test the sign of the expression in each interval**

Let:

$$
f(x) = (x - 1)(x + 2)(x - 4)
$$


|Interval|Test value|Sign of each factor|Sign of (f(x))|
|:---|:---|:---|:---|
|$x < -2$|$x = -3$|$(-)(-)(-)$|Negative|
|$-2 < x < 1$|$x = 0$|$(-)(+)(-)$|Positive|
|$1 < x < 4$|$x = 2$|$(+)(+)(-)$|Negative|
|$x > 4$|$x = 5$|$(+)(+)(+)$|Positive|

**Step 4: Select intervals where the expression is $\leq 0$**

We want:

$$
(x - 1)(x + 2)(x - 4) \leq 0
$$

This means $f(x)$ is either negative or zero.

- Negative in: $(-\infty, -2)$ and $(1, 4)$
- Zero at: $x = -2, 1, 4$

**Final Answer:**

$$
x \leq -2 \quad \text{or} \quad 1 \leq x \leq 4
$$