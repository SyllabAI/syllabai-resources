## Iteration 

  - To solve equation $f\left( x \right) = 0$, you can rearrange
    $f(x)$ into a form $x = \ldots$

  - This function represents a sequence that starts at $x₀$, moving to
    $x_{r}$

  - Substitute a value for $x₀$ and put back into function getting
    $x_{1}$ and so on.

  - As you increase $r,$ value becomes more accurate

  - Sometimes iteration don’t work, these functions are called
    divergent, and you must rearrange the formula for $\text{x\ }$in
    another way.

  - For a successful iterative function, you need a convergent sequence.

  - Ensure to use the full value and not the rounded off value when
    carrying out the iteration.

&nbsp;

**<span class="underline">{M16-P32} Question 3:</span>**

The equation $x^{5} - 3x^{3} + x^{2} - 4 = 0$ has one positive root.

(i)  Verify by calculation that this root lies between 1 and 2.

(ii)  Show that the equation can be rearranged in the form

$x = \sqrt[3]{\left( 3x + \frac{4}{x^{2}} - 1 \right)}$

(iii)  Use an iterative formula based on this rearrangement to determine
the positive root correct to 2 decimal places. Give the result of each
iteration to 4 decimal places.

**<center>Solution:</center>**

**<span class="underline">Part (i)</span>**

*Show a sign change and state it:*

${(1)}^{5} - 3\left( 1 \right)^{3} + \left( 1 \right)^{2} - 4 = \  - 5\ $

${(2)}^{5} - 3\left( 2 \right)^{3} + \left( 2 \right)^{2} - 4 = \ 8\ $

There is a sign change between the results obtained when the values 1
and 2 are substituted into the equation, therefore the root lies between
the values 1 and 2.

**<span class="underline">Part (ii)</span>**

*Rearrange the equation:*

$$
x = \sqrt[3]{\left( 3x + \frac{4}{x^{2}} - 1 \right)}
$$

$$
x^{3} = \ 3x + \frac{4}{x^{2}} - 1
$$

$$
x^{5} = 3x^{3} + 4 - x^{2}
$$

$$
x^{5} - 3x^{3} + x^{2} - 4 = 0
$$

**<span class="underline">Part (iii)</span>**

*Carry out the iteration using either one of the values that the root
lies in between as the starting point:*

$$
x_{n + 1} = \sqrt[3]{\left( 3x_{n} + \frac{4}{{x_{n}}^{2}} - 1 \right)}
$$

$$
x_{0} = 1
$$

$$
x_{1} = \sqrt[3]{\left( 3x_{0} + \frac{4}{{x_{0}}^{2}} - 1 \right)} = 1.8171
$$

$$
x_{2} = \sqrt[3]{\left( 3x_{1} + \frac{4}{{x_{1}}^{2}} - 1 \right)} = 1.7824
$$

$$
x_{3} = \sqrt[3]{\left( 3x_{2} + \frac{4}{{x_{2}}^{2}} - 1 \right)} = 1.7765
$$

$$
x_{4} = \sqrt[3]{\left( 3x_{3} + \frac{4}{{x_{3}}^{2}} - 1 \right)} = 1.7755
$$

<center>The positive root = <b>1.78</b></center>