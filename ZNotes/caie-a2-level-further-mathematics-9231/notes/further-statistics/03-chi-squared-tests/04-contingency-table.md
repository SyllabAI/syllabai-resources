## Contingency Table

* This is a table which contains the frequencies for two or more
  variables.
* You may then assess whether the variables are associated or
  independent.
* Hypothesis when testing:
  * $H_{0}:$ the variables are independent
  * $H_{1}:$ the variables are associated
* For example:

|    | $\mathbf{A}$ | $\mathbf{B}$ | $\mathbf{C}$ |    |
|----|----|----|----|----|
| $\mathbf{X}$ | $\ $ |    |    | $\sum R_{1}$ |
| $\mathbf{Y}$ |    |    |    | $\sum R_{2}$ |
| $\mathbf{Z}$ |    |    |    | $\sum R_{3}$ |
|    | $\sum C_{1}$ | $\sum C_{2}$ | $\sum C_{3}$ | $\mathbf{T}$ |

* The expectation of each variable is calculated by

$$\frac{row\ total\  \times \ column\ total}{\text{grand\ total}}$$

Or in math symbols

$$E_{\text{ij}} = \frac{\sum_{}^{}R_{i} \times \sum_{}^{}C_{j}}{\mathbf{T}}$$

* List each variable and set up table as before
* The degree of independence for an $r$ by $c$ table is

$$v = \left( r - 1 \right)(c - 1)$$

**<span class="underline">Question 10</span>
<span class="underline">9231/02/QP/12:</span>**

Random samples of employees are taken from two companies, A and B. Each
employee is asked which of three types of coffee (cappuccino, latte, and
ground) they prefer. The results are shown in the following table.

|    | Cappuccino | Latte | Ground |
|----|----|----|----|
| Company A | 60 | 52 | 32 |
| Company B | 35 | 40 | 31 |

a) Test, at the 5% significance level, whether coffee preferences of
employees are independent of their company



**<span class="underline">Solution:</span>**

a) Calculate the totals for each row and column by using
$E_{\text{ij}} = \frac{\sum_{}^{}R_{i} \times \sum_{}^{}C_{j}}{\mathbf{T}}$

| Expected | Cappuccino | Latte | Ground |
|----|----|----|----|
| Company A | $\frac{144 \times 95}{250}$ | $\frac{144 \times 92}{250}$ | $\frac{144 \times 63}{250}$ |
| Company B | $\frac{106 \times 95}{250}$ | $\frac{106 \times 92}{250}$ | $\frac{106 \times 63}{250}$ |

Simplifying the values in the table:

| Expected | Cappuccino | Latte | Ground |
|----|----|----|----|
| Company A | $54.72$ | $52.992$ | $36.288$ |
| Company B | $40.28$ | $39.008$ | $26.712$ |

Hypotheses:

$H_{0}:$ There is **no** association between the company and coffee
preference

$H_{1}:$ There is association between the company and coffee
preference

Calculating the test statistic

<table> <thead> <tr class="header"> <th><br /><span class="math display"><strong>O</strong></span><br /></th> <th><br /><span class="math display"><strong>E</strong></span><br /></th> <th><p><br /><span class="math display">(<strong>O</strong><sub>ij</sub><strong>−</strong><strong>E</strong><sub>ij</sub>)<sup><strong>2</strong></sup></span><br /></p> <p><span class="math inline"><strong>E</strong><sub>ij</sub></span></p></th> </tr> </thead> <tbody> <tr class="odd"> <td>60</td> <td>54.72</td> <td>0.509474</td> </tr> <tr class="even"> <td>52</td> <td>52.992</td> <td>0.01857</td> </tr> <tr class="odd"> <td>32</td> <td>36.288</td> <td>0.506695</td> </tr> <tr class="even"> <td>35</td> <td>40.28</td> <td>0.692115</td> </tr> <tr class="odd"> <td>40</td> <td>39.008</td> <td>0.025227</td> </tr> <tr class="even"> <td>31</td> <td>26.712</td> <td>0.68834</td> </tr> </tbody> </table>

Now we calculate the test statistic
$$
\chi^2 = 2.44
$$
Next, calculate the number of degrees of freedom
$$
v = (2 - 1)(3 - 1) = 2
$$
Finally, find the critical value
$$
\chi^2_2(0.95) = 5.991
$$
Since $2.44 < 5.991$, we do not reject $H_0$. There is insufficient evidence to suggest there is an association between the company and the coffee type.


