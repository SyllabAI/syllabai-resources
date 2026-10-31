## Examples

**<span class="underline">{S11-P63} Question 6:</span>**

The probability that Sue completes a Sudoku puzzle correctly is 0.75. Sue attempts 14 Sudoku puzzles every month. XX denotes the number that she completes successfully. Find the value of  $X$ that has the highest probability. You may assume this value is one of the two values closest to the mean of  $X$.

**<center>Solution:</center>**

**Calculate the mean of**  $X$

$$

E\left( X \right) = 14 \times 0.75 = 10.5
$$

**Successful puzzles completed have to be a whole number so they can either be 10 or 11.**

$$
P\left( 10 \right) = 14C_{10} \times {0.75}^{10} \times {0.25}^{4} = 0.220
$$

$$
P\left( 11 \right) = 14C_{11} \times {0.75}^{11} \times {0.25}^{3} = 0.240
$$

Probability with 11 is higher, therefore, X = 11



---



**<span class="underline">{W11-P62} Question 6:</span>**

In Luttley College, $60%$% of students are boys. Students can choose exactly one of Games, Drama or Music on Friday afternoons. $75%$% of the boys choose Games, $10%$% choose Drama, and remainder choose Music. Of the girls, $30%$% choose Games, $55%$% choose Drama and the remainder choose Music. $5$ drama students are chosen. Find the probability that at least $1$ of them is a boy.

**<center>Solution:</center>**

*First, we calculate the probability of selecting a boy who is a drama student, a conditional probability:*

$$
P\left( S \right) = \frac{P\left( \text{Boy} \middle| \text{Drama} \right)}{P\left( \text{Drama} \right)}
$$

$$
P\left( S \right) = \ \frac{P\left( \text{Boy} \right) \times P\left( \text{Drama} \right)}{\left( P\left( \text{Boy} \right) \times P\left( \text{Drama} \right) \right) + \left( P\left( \text{Girl} \right) \times P\left( \text{Drama} \right) \right)}
$$

$$
P\left( S \right) = \frac{0.6 \times 0.1}{\left( 0.6 \times 0.1 \right) + \left( 0.4 \times 0.55 \right)} = \frac{3}{14}
$$

*We can calculate the probability there is at least 1 boy present from 5 drama students using a binomial distribution with 5 trials and P of success =* $\frac{3}{14}$

*Find the probability of 0 and subtract the answer from 1:*

$$
P\left( X \geq 1 \right) = 1 - P(X = 0)
$$

$$
P\left( X \geq 1 \right) = 1 - 5C_0 \times \left( \frac{3}{14} \right)^{0} \times \left( \frac{11}{14} \right)^{5}
$$

$$
P\left( X \geq 1 \right) = 0.701
$$



