---
note_id: "rn_cBHtdJdvwfRJYfHN"
title: "Linear Combinations of Random Variables"
source: https://www.savemyexams.com/a-level/maths/cie/20/probability-and-statistics-2/revision-notes/statistical-distributions/linear-combinations-of-random-variables/linear-combinations-of-random-variables
path: statistical-distributions/linear-combinations-of-random-variables/linear-combinations-of-random-variables
updated_at: "2026-07-02T08:19:38.730Z"
spec_point_ids: ["spcpt_ZKTsy2RrhrRGDxnH", "spcpt_Bjg5yWKMV4mBYjrW", "spcpt_44sx7ZCBmc2kxvPj"]
spec_point_codes: []
guided_study: true
---

# Linear Combinations of Random Variables

## aX+b

> **Spec point** — `spcpt_ZKTsy2RrhrRGDxnH`

## aX+b

#### How are the mean and variance of X related to the mean and variance of aX + b?

- If *a* and *b* are **constants** then the following results are true

  - **E*****(aX + b) = a*****E*****(X) + b***
  - **Var*****(aX + b) = a² *****Var*****(X)***
- Note that the mean is affected by multiplication and addition whereas **addition does not** **change the variance**
- The factor of *a²*  includes the squared because the values of X are squared in the calculation

  - You could try and use the first result and the formula for variance to verify the second result
- Remember a subtraction can be written as an addition

  - *X – b* can be written as *X + (-b)*
- And division can be written as a multiplication

  - $\frac{x}{a}$can be written as $\frac{1}{a}X$

#### What does the distribution of aX + b look like?

- A linear function is applied to each value of *X*
- The graphical representation of ***aX + b ***is a linear transformation (a translation and a stretch) of the graphical representation of ***X***
- If ***X*** follows a **normal **distribution then ***aX + b ***will also follow a **normal** distribution

  - If *X *~ N(*μ, σ²*) then *aX + b *~ N(*aμ + b, a²σ²*)
- If *X* follows a binomial, geometric or Poisson distribution then *aX + b* will no longer follow the same type of distribution

> **Worked Example**
> $X$ is a random variable such that $E(X)=5$ and $\mathrm{Var}(X)=4$.
> 
> Find the value of:
> 
> (i) $E(3X+5)$
> 
> (ii) $\mathrm{Var}(3X+5)$
> 
> (iii) $\mathrm{Var}(2-X)$
> 
> **Answer:**
> 
> ![2-2-1-ax--b-we-solution-1-2](assets/b26060dbaea0-image.bin)

## aX + bY

> **Spec point** — `spcpt_Bjg5yWKMV4mBYjrW`

## aX + bY

#### How are the means and variances of X and Y related to the mean and variance of X + Y ?

- If *X* and *Y* are two **random variables** then *X *+* Y *is the random variable whose values are the sums of each pair containing one value of *X* and one value of *Y*
- **E(*****X *****+***** Y*****) = E(*****X*****) + E(*****Y*****)**

  - this is true for **any** random variables *X* and *Y*
  - Note that **E(*****X *****– *****Y*****) = E(*****X*****) - E(*****Y*****)** (see below for more information)
- **Var(*****X *****+***** Y*****) = Var(*****X*****) + Var(*****Y*****)**

  - this is true if *X* and *Y *are **independent**
  - Note that **Var(*****X *****-***** Y*****) = Var(*****X*****) + Var(*****Y*****)** (see below for more information)

#### What does the distribution of X + Y  look like?

- If ***X*** and ***Y*** are **two independent Poisson** distributions then ***X *****+***** Y*** is also a **Poisson** distribution

  - If $X^{\sim } P o ( \\lambda )$ and $\text{size} 16px Y^{size} 16px \sim \text{size} 16px P \text{size} 16px o \text{size} 16px ( \text{size} 16px \\mu \text{size} 16px )$ then $X + Y^{\sim } P o ( \\lambda + \\mu )$
- If ***X*** and ***Y*** are **two independent normal** distributions then ***X *****+***** Y*** is also a **normal** distribution

  - If $X^{\sim } N ( \mu_{1} , \sigma_{1}^{2} )$ and $Y^{size} 16px \sim \text{size} 16px N ( \mu_{2} , \sigma_{2}^{2} )$ then $X + Y^{\sim } N ( \mu_{1} + \mu_{2} \text{size} 16px , \text{size} 16px \sigma_{size} 16px 1^{size} 16px 2 \text{size} 16px + \text{size} 16px \sigma_{size} 16px 2^{size} 16px 2 \text{size} 16px )$

#### What does the distribution of aX + bY look like?

- If *X* and *Y* are random variables and *a* and *b* are two constants we can combine the results for *aX* + *b* and *X* + *Y*
- **E(*****aX***** + *****bY*****) = *****a*****E(*****X*****) + *****b*****E(*****Y*****)**

  - this is true for **any** random variables *X* and *Y*
- **Var(*****aX***** + *****bY*****) = *****a*****²Var(*****X*****) + *****b*****²Var(*****Y*****)**

  - this is true if *X* and *Y *are **independent**
- Note that b is squared for the variance so we have

  - **E(*****aX***** - *****bY*****) = *****a*****E(*****X*****) - *****b*****E(*****Y*****)**
  - **Var(*****aX***** - *****bY*****) = *****a*****²Var(*****X*****) + *****b*****²Var(*****Y*****)**
  
    - Notice that the variances of ***aX***** + *****bY ***and ***aX***** – *****bY ***are the same
- If ***X*** and ***Y*** are **two independent normal** distributions then ***aX *****+***** bY*** is also a **normal** distribution

  - If *X* ~ N(*μ*<sub>*1*</sub>*, σ*<sub>*1*</sub>²) and *Y* ~ N(*μ*<sub>*2*</sub>*, σ*<sub>*2*</sub>²) then *aX* ± *bY* ~ N(*aμ*<sub>*1*</sub>* *± *bμ*<sub>*2*</sub>*, a*²*σ*<sub>*1*</sub>²* *+ *b*²*σ*<sub>*2*</sub>²)
- Note that *aX *+* bY *is **no longer Poisson** even if *X* and *Y* are Poisson

  - This holds provided *a *and *b *are not 0 or 1

> **Worked Example**
> $X$ and $Y$ are independent random variable such that
> 
> $E(X)=5\mathrm{and} \mathrm{Var}(X)=3$
> 
> $E(Y)=-2\mathrm{and} \mathrm{Var}(Y)=4.$
> 
> Find the value of:
> 
> (i) $E(2X+5Y)$
> 
> (ii) $\mathrm{Var}(2X+5Y)$
> 
> (iii) $\mathrm{Var}(4X-Y)$
> 
> **Answer:**
> 
> ![2-2-1-ax--by-we-solution-1](assets/f88f01632a26-image.bin)

## Linear Combinations

> **Spec point** — `spcpt_44sx7ZCBmc2kxvPj`

## Linear Combinations

#### For a given random variable X, what is the difference between 2X and X<sub>1</sub> + X<sub>2</sub>?

- **2*****X ***means **one observation** of *X *is taken and **then doubled**
- ***X***<sub>**1**</sub>** + *****X***<sub>**2 **</sub>means **two observations** of *X *are taken and **added together**
- **2*****X ***and ***X***<sub>**1**</sub>** + *****X***<sub>**2 **</sub>both have the **same expected value** of **2E(*****X*****)**
- **2*****X ***and ***X***<sub>**1**</sub>** + *****X***<sub>**2 **</sub>have **different variances**

  - **Var(2*****X*****) = 2²Var(X) = 4Var(*****X*****)**
  - **Var(*****X***<sub>**1**</sub>** + *****X***<sub>**2**</sub>**) = 2Var(*****X*****)**
- Imagine *X *could take the values 0 and 1

  - 2*X *could then take the values 0 and 2 (2 × 0 = 0 and 2 × 1 = 2)
  - *X*<sub>1</sub> + *X*<sub>2 </sub>could then take the values 0, 1 and 2 (0 + 0 = 0, 0 +1 = 1, 1 + 1 = 2)
- Sometimes questions may describe the variables in context

  - The mass of a carton of half a dozen eggs is the mass of the carton plus the mass of the 6 **individual** eggs and can be modelled using the random variable
  - *C *+ *E*<sub>*1*</sub> + *E*<sub>*2 *</sub>+ *E*<sub>*3 *</sub>+ *E*<sub>*4 *</sub>+ *E*<sub>*5 *</sub>+ *E*<sub>*6 *</sub>where
  
    - *C *is the mass of a carton
    - *E *is the mass of an egg
  - It is **not** *C *+ 6*E *because the masses of the 6 eggs could be different

#### How do I use linear combinations of normal random variables to find probabilities?

- If the random variables are **normally distributed** and **independent** you might be asked to find probabilities such as

  - P(*X*<sub>1 </sub>+ *X*<sub>2 </sub>+ *X*<sub>3</sub>* *> 2*Y *+ 5)
  - This could be given in words
  
    - Find the probability that the mass of three chickens (*X*) is more than 5 kg heavier than double the mass of a turkey (*Y*)
- To solve these problems:

  - **STEP 1**: **Rearrange** the inequality to get all the **random variables on one side**
  
    - P(*X*<sub>1 </sub>+ *X*<sub>2 </sub>+ *X*<sub>3</sub>* *– 2*Y *> 5)
  - **STEP 2**: Find the **mean and variance** of the **combined normal random** **variable**
  
    - *μ* = E(*X*<sub>1 </sub>+ *X*<sub>2 </sub>+ *X*<sub>3</sub>* *– 2*Y*) = E(*X*<sub>1</sub>) + E(*X*<sub>2</sub>) + E(*X*<sub>3</sub>) - 2E(*Y*)
    - *σ*² = Var(*X*<sub>1 </sub>+ *X*<sub>2 </sub>+ *X*<sub>3</sub>* *– 2*Y*) = Var(*X*<sub>1</sub>) + Var(*X*<sub>2</sub>) + Var(*X*<sub>3</sub>) + 2² Var(*X*<sub>1</sub>)
  - **STEP 3**: Find the **required probability** using the **combined normal distribution**
  
    - *X*<sub>1 </sub>+ *X*<sub>2 </sub>+ *X*<sub>3</sub>* *– 2*Y* ~ N(*μ*, *σ*²)
    - Use z-values and the table of values

> **Worked Example**
> `X tilde N ( 10 , 4 ^2 ) and Y tilde N ( - 5 , 8 ^2 )`
> 
> Find $P(3X>2Y+50)$
> 
> **Answer:**
> 
> ![2-2-1-linear-combs-we-solution-1](assets/f7e9f4382e50-image.bin)

> **Exam Hint**
> - Be careful with negatives!
