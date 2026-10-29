---
note_id: "rn_Srzjn8c2CyJmfpHZ"
title: "Standard Normal Distribution"
source: https://www.savemyexams.com/a-level/maths/cie/20/probability-and-statistics-1/revision-notes/statistical-distributions/normal-distribution/standard-normal-distribution
path: statistical-distributions/normal-distribution/standard-normal-distribution
updated_at: "2026-08-03T09:52:35.442Z"
spec_point_ids: ["spcpt_khQ8s7M7XpHHbF5t"]
spec_point_codes: []
guided_study: true
---

# Standard Normal Distribution

## Standard Normal Distribution

> **Spec point** — `spcpt_khQ8s7M7XpHHbF5t`

## Standard Normal Distribution

#### What is the standard normal distribution?

- The **standard normal distribution** is a normal distribution where the **mean is 0** and the **standard deviation is 1**

  - It is denoted by *Z*
  - $Z \sim \mathrm{N} ( 0 , 1^{2} )$

#### Why is the standard normal distribution important?

- Calculating probabilities for the normal distribution can be difficult and lengthy due to its complicated probability density function
- The probabilities for the **standard normal distribution** have been calculated and laid out in the **table of the normal distribution** which can be found in your formula booklet

  - Nowadays, many calculators can calculate probabilities for any normal distribution, if yours does it is a good idea to learn how to use it to check your answers but you must still use the tables of the normal distribution and show all your working clearly
- It is possible to map any normal distribution onto the standard normal distribution curve
- Mapping different normal distributions to the standard normal distribution allows distributions with different means and standard deviations to be compared with each other

#### How is any normal distribution mapped to the standard normal distribution?

- Any **normal distribution curve** can be transformed to the standard normal distribution curve by a **horizontal translation** and a **horizontal stretch**

  - Therefore, for $X \sim \mathrm{N} ( \\mu , \\sigma ^{2} )$  and `Error converting from MathML to accessible text.`, we have the relationship:

$Z=\frac{X-μ}{σ}$

- Probabilities are related by:

  - $\mathrm{P} ( X < a ) = \mathrm{P} ( Z < \frac{a - \\mu }{\\sigma } )$
  - This is a very useful relationship for calculating probabilities for any normal distribution
  - As it is a normal distribution $P(z_{1}\leqZ\leqz_{2})=P(z_{1}<Z<z_{2})$ so you do not need to worry about whether the inequality is strict (< or >) or weak (≤ or ≥)
- A value of z = 1 corresponds with the *x*-value that is 1 standard deviation above the mean and a value of z = -1 corresponds with the *x*-value that is 1 standard deviation below the mean
- If a value of** *****x***** **is** less than the mean** then the *z* **-value will be negative**
- The function $Φ(z)$ is used to represent $P(Z<z)$

#### How is the table of the normal distribution function used?

- In your formula booklet you have the table of the normal distribution which provides probabilities for the standard normal distribution

  - The probabilities are provided for $Φ(z)=P(Z\leqz)=P(Z<z)$
  - To find other probabilities you should use the symmetry property of the normal distribution curve
- The table gives probabilities for values of *z* between 0 and 3

  - For negative values of *z*, the symmetry property of the normal distribution is used
  - For values greater than *z* = 3 the probabilities are small enough to be considered negligible
- The tables give the probabilities to 4 decimal places
- To read probabilities from the normal distribution table for a *z* value of up to 2 decimal places:

  - The very first column lists all *z* values to 1 decimal place from *z* = 0.0 to *z* = 2.9
  - The top row gives the second decimal place for each of these *z* values
  - So the value of $Φ(1.23)=P(Z\leq1.23)$ would be found at the point where the ‘1.2’ row meets the ‘3’ column
  
    - $P(Z\leq1.23)=0.8907$
- To read probabilities from the normal distribution table for a *z* value of 3 decimal places:

  - There is an extra section to the right of the tables that gives the amount to add on to the probabilities for the third decimal place
  - The values given in the columns represent one ten-thousandth
  
    - If the value is 7 we add 0.0007 to the probability
    - If the value is 23 we add 0.0023 to the probability
  - To find the value of $Φ(1.234)$ we would need to find the amount to add on to 0.8907
  - Find the point where the 1.2 row meets the ADD 4 column, this gives us the number 7
  - Add the value 0.0007 to the probability for $Φ(1.23)$
  
    - $P(Z\leq1.234)=0.8914$

#### How is the table used to find probabilities that are not listed?

- The property that the area under the graph is 1 allows probabilities to be found for P( *Z > z*)

  - Use the formula $P(Z>z)=1-Φ(z)$
- The symmetrical property of the normal distribution gives the following results:

  - $P(Z\leqz)=P(Z\geq-z)$
  - $P(Z\geqz)=P(Z\leq-z)$
- This allows probabilities to be found for negative values of *z* or for $P(Z>z)$

  - $Φ(-z)=P(Z\leq-z)=\text{P(Z > z) =}1-Φ(z)$
  - Therefore:
  
    - $Φ(-z)=1-Φ(z)$
    - $P(Z>z)=1-Φ(z)$
  - $P(Z>-z)=P(Z\leqz)=Φ(z)$
- The four cases in terms of $Φ(z)$ are:

  - $P(Z<z)=Φ(z)$
  - $P(Z>z)=1-Φ(z)$
  - $P(Z<-z)=1-Φ(z)$
  - $P(Z>-z)=Φ(z)$
- Drawing a sketch of the normal distribution will help find equivalent probabilities

![3-3-2-standard-normal-distribution-diagram-1](../../../assets/2f4ec58e8828-3-3-2-standard-normal-distribution-diagram-1.png)

#### How are z values found from the table of the normal distribution function?

- To find the value of *z* for which $P(Z\leqz)=p$ look for the value of *p* from within the table and find the corresponding value of *z*

  - If the probability is given to 4 decimal places most of the time the value will exist somewhere in the tables
  - Occasionally you may have to use the ADD columns to find the exact value
  - If the values in the ADD columns don’t exactly match up use the closest value or find the midpoint of the *z* values that are either side of the probability
- If your probability is 0.5 or greater look through the tables to find the corresponding *z* value

  - For $P(Z<z)\geq0.5$  use the z value found in the table
  - For $P(Z>z)\geq0.5$ take the negative of the z value found in the table
- If the probability is less than 0.5 you will need to **subtract it from one** before using the tables to find the corresponding *z* value

  - For $P(Z<z)<0.5$  take the negative of the z value found in the table
  - For $P(Z>z)<0.5$ use the z value found in the table
- **Always draw a sketch **so that you can see these clearly
- The formula booklet also contains a **table of the critical values of *****z***

  - This gives *z* values to 3 decimal places for common probabilities
  - The probabilities in this table are 0.75, 0.9, 0.95, 0.975, 0.99, 0.995, 0.9975, 0.999 and 0.9995

> **Worked Example**
> (a) By sketching a graph and using the table of the normal distribution, find the following:
> 
> (i) $P(Z\leq0.957)$
> 
> (ii) $P(Z>0.957)$
> 
> (iii) $P(Z\leq-0.957)$
> 
> (iv) $P(-0.957<Z\leq0.957)$
> 
> (b) Find the value of $z$ such that $P(Z<z)=0.3$
> 
> **Answer:**
> 
> ![ULe~Cq-4_3-3-2-standard-nd-we-solution-1-part-a](assets/c75ae5a07db9-64158-3-3-2-standard-nd-we-solution-1-part-a.png)
> 
> ![R4Ws5m8G_3-3-2-standard-nd-we-solution-1-part-b](assets/ca77e5c76a51-5978-3-3-2-standard-nd-we-solution-1-part-b.png)

> **Exam Hint**
> - A sketch will always help you to visualise the required probability and can be used to check your answer. Check whether the area shaded is more or less than 50% and compare this with your answer.
