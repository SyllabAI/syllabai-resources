---
note_id: "rn_2nBj2FwhckVKnxfY"
title: "Standard Proofs by Induction"
source: https://www.savemyexams.com/international-a-level/further-maths/edexcel/18/further-pure-1/revision-notes/proof/proof-by-induction/standard-proofs-by-induction
path: proof/proof-by-induction/standard-proofs-by-induction
updated_at: "2025-06-12T07:55:48.800Z"
spec_point_ids: ["spcpt_b54Tg8rD74DyCckg", "spcpt_Zdhf85vx7x4Jdd54", "spcpt_P6PMYkhvyYkCXM2d", "spcpt_6NkRppSFKD89hB3j"]
spec_point_codes: []
guided_study: false
---

# Standard Proofs by Induction

## Proof by Induction with Series

> **Spec point** — `spcpt_b54Tg8rD74DyCckg`

## Proof by Induction with Series

### What are the steps for proof by induction with series?

- For example: prove that $\sum_{r = 1}^{n} r^{2} = \frac{1}{6} n ( n + 1 ) ( 2 n + 1 )$* *

  - It has a** left-hand** side, $L H S = \sum_{r = 1}^{n} r^{2}$
  - and a **right-hand** side, $RHS=\frac{1}{6}n(n+1)(2n+1)$

- **STEP 1** **The basic step:** Show result is true for** **$n=1$

  - **Substitute*** *$n=1$ into both sides **individually** $L H S = \sum_{r = 1}^{1} r^{2} = 1^{2} = 1
 R H S = \frac{1}{6} \times 1 \times ( 1 + 1 ) ( 2 \times 1 + 1 ) = \frac{1}{6} \times 2 \times 3 = 1$

- **STEP 2** **The assumption step: **Assume the *LHS* and *RHS*  are equal for some $n=k$* *where $k$* *is some integer

  - Replace $n$ with $k$ in the statement
  - Write: "Assume $\sum_{r = 1}^{k} r^{2} = \frac{1}{6} k ( k + 1 ) ( 2 k + 1 )$ is true"

- **STEP 3** **The inductive step: **You need to **prove **that the *LHS* and *RHS*  are equal for $n=k+1$

  - **Start** with the ***LHS**** * for $n=k+1$
  
    - Take the** last** term out: $\sum_{r = 1}^{k + 1} r^{2 } = \sum_{r = 1}^{k} r^{2} + ( k + 1 )^{2}$
    - **Substitute** in the **assumption **(STEP 2) :
    - $\sum_{r = 1}^{k + 1} r^{2 } = \frac{1}{6} k ( k + 1 ) ( 2 k + 1 ) + ( k + 1 )^{2}$
    - **Factorise**: 
    $\frac{1}{6} ( k + 1 ) [ k ( 2 k + 1 ) + 6 ( k + 1 ) ] = \frac{1}{6} ( k + 1 ) [ 2 k ^{2} + 7 k + 6 ] = \frac{1}{6} ( k + 1 ) ( k + 2 ) ( 2 k + 3 )$
  - **Check** if it is the **same** as the** *****RHS***** ** for $n=k+1$ $\begin{gathered} R H S & = \frac{1}{6} ( k + 1 ) ( ( k + 1 ) + 1 ) ( 2 ( k + 1 ) + 1 ) \\ = \frac{1}{6} ( k + 1 ) ( k + 2 ) ( 2 k + 3 ) \end{gathered}$
  - So** *****LHS*****  = *****RHS*****  **for $n=k+1$, as long as the **assumption** is true

- **STEP 4** **The conclusion step: **Explain in** words** how the above steps make the result** true** for **all** integers, using the following **two **sentences:

  - "**If** it is true for $n=k$,* ***then** it is true for $n=k+1$."
  - "**As** it is true for $n=1$, the** **statement** **is true **for all** $n\inℤ^{+}$."

> **Worked Example**
> Prove by induction that $\sum_{r = 1}^{n} r ( r - 3 ) = 1 \frac{1}{3} n ( n - 4 ) ( n + 1 )$ for $n\inℤ^{+}$.
> 
> > *STE P 1: The basic step*
> *Find the LHS when* $n=1$
> 
> $\sum_{r = 1}^{1} r ( r - 3 ) = 1 ( 1 - 3 ) = - 2$* *
> 
> > *Find the RHS when** *$n=1$
> 
> $1 \frac{1}{3} \times 1 \times ( 1 - 4 ) ( 1 + 1 ) = 1 \frac{1}{3} \times ( - 6 ) = - 2$* *
> 
> > *The LHS and RHS are equal, which shows the statement is true for* $n=1$
> *State this*
> 
> *LHS = RHS, so it is true for* $n=1$
> 
> > *  *
> 
> > *STEP 2: The assumption step*
> *Assume the statement is true for some* $n=k$ *where* $k$* **is a positive integer*
> 
> *Assume that* $\sum_{r = 1}^{k} r ( r - 3 ) = 1 \frac{1}{3} k ( k - 4 ) ( k + 1 )$
> 
> > * *
> 
> > *STEP 3: The inductive step*
> *Find the RHS when* $n=k+1$
> 
> > $1 \frac{1}{3} ( k + 1 ) ( k + 1 - 4 ) ( k + 1 + 1 ) = 1 \frac{1}{3} ( k + 1 ) ( k - 3 ) ( k + 2 )$* *
> 
> > *Find the LHS when* $n=k+1$
> 
> $\sum_{r = 1}^{k + 1} r ( r - 3 )$
> 
> > *Prove that the LHS when* $n=k+1$ *equals the RHS when* $n=k+1$
> *Start by pulling out the final term in the sum*
> 
> $\begin{gathered} \sum_{r = 1}^{k + 1} r ( r - 3 ) & = \sum_{r = 1}^{k} r ( r - 3 ) + ( k + 1 ) ( k + 1 - 3 ) \\ = \sum_{r = 1}^{k} r ( r - 3 ) + ( k + 1 ) ( k - 2 ) \end{gathered}$
> 
> > *Now use the assumption in STEP 2 to replace the sum from 1 to* $k$ *with its answer*
> 
> $\begin{gathered} \sum_{r = 1}^{k + 1} r ( r - 3 ) & = 1 \frac{1}{3} k ( k - 4 ) ( k + 1 ) + ( k + 1 ) ( k - 2 ) \end{gathered}$
> 
> > *Now factorise the right-hand side*
> 
> $\begin{gathered} \sum_{r = 1}^{k + 1} r ( r - 3 ) & = ( k + 1 ) [ 1 \frac{1}{3} k ( k - 4 ) + ( k - 2 ) ] \\ = 1 \frac{1}{3} ( k + 1 ) [ k ( k - 4 ) + 3 ( k - 2 ) ] \end{gathered}$
> 
> > *Expand inside the square brackets then continue to factorise*
> 
> $\begin{gathered} \sum_{r = 1}^{k + 1} r ( r - 3 ) & = 1 \frac{1}{3} ( k + 1 ) [ k^{2} - 4 k + 3 k - 6 ] \\ = 1 \frac{1}{3} ( k + 1 ) [ k^{2} - k - 6 ] \\ = 1 \frac{1}{3} ( k + 1 ) ( k - 3 ) ( k + 2 ) \end{gathered}$
> 
> > *This is the same as the RHS when* $n=k+1$
> *The LHS and RHS are equal, which shows that the statement is true for* $n=k+1$
> *State this*
> 
> *LHS = RHS, so it is true for* $n=k+1$
> 
> > * *
> 
> > *STEP 4: The conclusion*
> *We have just proved that if the case when* $n=k$ *is true, then the case when* $n=k+1$ *is true*
> *We have also shown that the case when* $n=1$ *is true*
> *Those two parts come together to mean that* $n=1$* is true, so** *$n=2$ *is true, so* $n=3$ *is true, ... and so on*
> 
> **Final answer:** **If it is true for **$n=k$**, then it is true for **$n=k+1$**.**
> **As it is true for **$n=1$**, the statement is true for all **$n\inℤ^{+}$**.**

## Proof by Induction with Divisibility

> **Spec point** — `spcpt_Zdhf85vx7x4Jdd54`

## Proof by Induction with Divisibility

### What are the steps for proof by induction with divisibility?

- For example: prove that $f(n)=4^{n}-1$ is divisible by 3 for all positive integers *n*

  - Being** divisible** by 3 is the same as being a **multiple** of 3

- **STEP 1** **The basic step:** Show result is true for** **$n=1$

  - **Substitute*** *$n=1$ into the function
  - $\mathrm{f} ( 1 ) = 4^{1} - 1 = 3$which is divisible by 3

- **STEP 2** **The assumption step: **Assume $f(k)=4^{k}-1$ is divisible by 3 for some $n=k$* *where $k$* *is some integer

  - Replace $n$ with $k$ in the statement
  - Write "divisible by 3" as "$=3m$" where $m$ is a positive integer
  - So$\mathrm{f} ( k ) = 4^{k} - 1 = 3 m$ where $m\inℤ^{+}$
  - It helps to make $4^{k}$ the **subject**: $4^{k}=1+3m$

- **STEP 3** **The inductive step (method 1): **You need to show that the $n=k+1$ case is divisible by 3

  - Substitute $n=k+1$ into the function
  
    - $f(k+1)=4^{k+1}-1$
  - Use** index laws** to substitute in the **assumption **(STEP 2)  $4^{k}=1+3m$
  
    - $\mathrm{f} ( k + 1 ) = 4 ( 4^{k} ) - 1 = 4 ( 1 + 3 m ) - 1 = 3 ( 4 m + 1 )$which is a multiple of 3
  - So $f(k+1)$is divisible by 3 (as long as the **assumption** is true)

- **STEP 3** **The inductive step (method 2): **An **alternative method ** is to show that the **difference** $f(k+1)-f(k)$  is a multiple of 3

  - i.e.  $f(k+1)-f(k)=3\times...$
  - Making $f(k+1)$the subject gives $\mathrm{f} ( k + 1 ) = \mathrm{f} ( k ) + 3 \times...$
  - So $f(k+1)$ is divisible by 3 (as long as the **assumption** is true, i.e. that  $f(k)$ is divisible by 3)
  - This method does not always work
  
    - When it does, a hint will be given in the question

- **STEP 4** **The conclusion step: **Explain in** words** how the above steps make the result** true** for **all** integers, using the following **two **sentences:

  - "**If** it is true for $n=k$,* ***then** it is true for $n=k+1$."
  - "**As** it is true for $n=1$, the** **statement** **is true **for all** $n\inℤ^{+}$."

> **Worked Example**
> Prove by induction that $f(n)=6^{n}+13^{n+1}$ is divisible by 7 for all integers satisfying $n\geq0$.
> 
> > *STE P 1: The basic step*
> *Prove that it is true for* $n=0$
> 
> $\begin{gathered} \mathrm{f} ( 0 ) & = 6^{0 + 13^{0} + 1} \\ = 1 + 13 \\ = 14 \\ = 7 \times 2 \end{gathered}$
> 
> > *State that it is true for* $n=0$
> 
> *14 is divisible by 7, so it is true for* $n=0$
> 
> > * *
> 
> > *STEP 2: The assumption step*
> *Assume the statement is true for some* $n=k$ *where* $k$ *is a positive integer*
> 
> *Assume that* $f(k)=6^{k}+13^{k+1}$ *is divisible by 7*
> 
> > *Replace "being divisible by 7" with being equal to* $7m$*, where* $m$ *is a positive integer*
> 
> $6^{k}+13^{k+1}=7m$
> 
> > * *
> 
> > *STEP 3: The inductive step*
> *Substitute* $n=k+1$ *into the function*
> 
> $\begin{gathered} \mathrm{f} ( k + 1 ) & = 6^{k + 1} + 13^{( k + 1 ) + 1} \\ = 6^{k + 1} + 13^{k + 2} \end{gathered}$
> 
> > *Now make either* $6^{k}$ *or* $13^{k+1}$ *the subject of STEP 2 and substitute it in*
> *It helps to use index laws first*
> 
> $\begin{gathered} \mathrm{f} ( k + 1 ) & = 6^{k \times 6 + 13^{k} + 2} \\ = ( 7 m - 13^{k + 1} ) \times 6 + 13^{k + 2} \end{gathered}$
> 
> > *Simplify the terms, using index laws to group the* $13^{k+1}$ *terms*
> 
> $\begin{gathered} \mathrm{f} ( k + 1 ) & = 42 m - 6 \times 13^{k + 1} + 13^{k + 2} \\ = 42 m - 6 \times 13^{k + 1} + 13 \times 13^{k + 1} \\ = 42 m + ( - 6 + 13 ) \times 13^{k + 1} \\ = 42 m + 7 \times 13^{k + 1} \end{gathered}$
> 
> > *The goal is to show that this result is divisible by 7*
> *Factorise out a 7 to show this*
> 
> $\begin{gathered} \mathrm{f} ( k + 1 ) & = 7 \times ( 6 m + 13^{k + 1} ) \end{gathered}$
> 
> > *State that it is true for* $n=k+1$
> 
> $\mathrm{f} ( k + 1 )$ *is divisible by 7, so it is true for* $n=k+1$
> 
> > * *
> 
> > *STEP 4: The conclusion*
> *We have just proved that if the case when* $n=k$ *is true, then the case when* $n=k+1$ *is true*
> *We have also shown that the case when* $n=0$ *is true*
> *Those two parts come together to mean that* $n=0$* is true, so** *$n=1$ *is true, so* $n=2$ *is true, ... and so on*
> 
> **Final answer:** **If it is true for **$n=k$**, then it is true for **$n=k+1$**.**
> **As it is true for **$n=0$**, the statement is true for all integers **$n\geq0$**.**

## Proof by Induction with Sequences

> **Spec point** — `spcpt_P6PMYkhvyYkCXM2d`

## Proof by Induction with Sequences

### What are the steps for proof by induction with sequences?

- For example: prove that the sequence given** recursively** by $u_{n+1}=3u_{n}+4$ where $u_{1}=1$ has the** *****n***<sup>**th**</sup>** term formula** $u_{n}=3^{n}-2$ for $n\geq1$

- **STEP 1** **The basic step:** Show result is true for** **$n=1$

  - **Substitute*** *$n=1$ into the formulae** separately**
  - $u_{1}=1$ from the recursive formula
  - $u_{1}=3^{1}-2=1$ from the *n*<sup>th</sup> term formula

- **STEP 2** **The assumption step: **Assume that the term $u_{k}$ satisfies* *$u_{k}=3^{k}-2$ for some $n=k$* *where $k$* *is some integer

  - Replace $n$ with $k$ in the statement
  - The assumption is on the *n*<sup>th</sup> term formula
  
    - (not on the recursive formula)

- **STEP 3** **The inductive step: **Show that the *n*<sup>th</sup> term formula is true for $n=k+1$

  - Use the recursive formula to write $u_{k+1}=3u_{k}+4$
  - Substitute in the **assumption** (STEP 2) and simplify
  
    - $u_{k + 1} = 3 ( 3^{k - 2 ) + 4 = 3^{k} + 1} - 2$
  - **Check** this is the same as the* n*th term formula when $n=k+1$
  
    - $u_{k+1}=3^{k+1}-2$
    - It is the same

- **STEP 4** **The conclusion step: **Explain in** words** how the above steps make the result** true** for **all** integers, using the following **two **sentences:

  - "**If** it is true for $n=k$,* ***then** it is true for $n=k+1$."
  - "**As** it is true for $n=1$, the** **statement** **is true **for all** $n\inℤ^{+}$."

> **Exam Hint**
> - If the recursive formula involves the previous **two **terms, then the basic step must be done for both $n=1$ and $n=2$.

> **Worked Example**
> A sequence is defined by $u_{n+1}=5u_{n}-4$ where $u_{1}=2$ and $n\geq1$.
> 
> Prove by mathematical induction that $u_{n}=5^{n-1}+1$, where $n\geq1$.
> 
> > *STE P 1: The basic step*
> *Find* $u_{1}$ *from the recursive sequence*
> 
> $u_{1}=2$
> 
> > *Find* $u_{1}$* from the **n*<sup>*th*</sup> *term formula*
> 
> $\begin{gathered} u_{1} & = 5^{1 - 1} + 1 \\ = 5^{0} + 1 \\ = 1 + 1 \\ = 2 \end{gathered}$
> 
> > *These two terms are equal*
> *State that it is true for* $n=1$
> 
> *It is true for* $n=1$
> 
> > * *
> 
> > *STEP 2: The assumption step*
> *Assume the formula is true for some* $n=k$ *where* $k$ *is a positive integer*
> 
> *Assume that* $u_{k}=5^{k-1}+1$
> 
> > * *
> 
> > *STEP 3: The inductive step*
> *Use the recursive sequence to write* $u_{k+1}$ *in terms of* $u_{k}$
> 
> $\begin{gathered} u_{k + 1} & = 5 u_{k} - 4 \end{gathered}$
> 
> > *Replace* $u_{k}$ *with the assumption in STEP 2 and simplify*
> 
> $\begin{gathered} u_{k + 1} & = 5 ( 5^{k - 1} + 1 ) - 4 \\ = 5^{k} + 5 - 4 \\ = 5^{k} + 1 \end{gathered}$
> 
> > *Check that this is the same as substituting* $n=k+1$* into the **n*<sup>*th*</sup> *term formula*
> 
> $\begin{gathered} u_{k + 1} & = 5^{( k + 1 ) - 1} + 1 \\ = 5^{k} + 1 \end{gathered}$
> 
> > *State that the result is true for* $n=k+1$
> 
> *It is true for* $n=k+1$
> 
> > * *
> 
> > *STEP 4: The conclusion*
> *We have just proved that if the case when* $n=k$ *is true, then the case when* $n=k+1$ *is true*
> *We have also shown that the case when* $n=1$ *is true*
> *Those two parts come together to mean that* $n=1$* is true, so** *$n=2$ *is true, so* $n=3$ *is true, ... and so on*
> 
> **Final answer:** **If it is true for **$n=k$**, then it is true for **$n=k+1$**.**
> **As it is true for **$n=1$**, the statement is true for all **$n\inℤ^{+}$**.**

## Proof by Induction with Matrices

> **Spec point** — `spcpt_6NkRppSFKD89hB3j`

## Proof by Induction with Matrices

### What are the steps for proof by induction with matrices?

- For example: prove that $M^{n} = ( \begin{gathered} 2^{n} & 0 \\ 1 - 2^{n} & 1 \end{gathered} )$ where $M = ( \begin{gathered} 2 0 \\ - 1 & 1 \end{gathered} )$ for all integers $n\geq1$.

- **STEP 1** **The basic step:** Show result is true for** **$n=1$

  - **Substitute*** *$n=1$ into formula
  - $M^{1 =} ( \begin{gathered} 2^{1} & 0 \\ 1 - 2^{1} & 1 \end{gathered} ) = ( \begin{gathered} 2 0 \\ - 1 & 1 \end{gathered} ) = M$

- **STEP 2** **The assumption step: **Assume $M^{k} = ( \begin{gathered} 2^{k} & 0 \\ 1 - 2^{k} & 1 \end{gathered} )$ is true for some $n=k$* *where $k$* *is some integer

  - Replace $n$ with $k$ in the statement

- **STEP 3** **The inductive step: **You need to show that the $n=k+1$ case is true

  - Use **index laws** to write $M^{k+1}=\mathrm{MM}^{k}$
  - Substitute in the** assumption**: $M^{k + 1} = M ( \begin{gathered} 2^{k} & 0 \\ 1 - 2^{k} & 1 \end{gathered} ) = ( \begin{gathered} 2 0 \\ - 1 & 1 \end{gathered} ) ( \begin{gathered} 2^{k} & 0 \\ 1 - 2^{k} & 1 \end{gathered} )$
  - **Multiply** the matrices
  
    - $M^{k + 1} = ( \begin{gathered} 2^{k + 1} & 0 \\ 1 - 2 \times 2^{k & 1 \end{gathered} ) = ( \begin{gathered} 2^{k} + 1} & 0 \\ 1 - 2^{k + 1} & 1 \end{gathered} )$
  - **Check** if it is the same as the formula with $n=k+1$
  
    - $M^{k + 1} = ( \begin{gathered} 2^{k + 1} & 0 \\ 1 - 2^{k + 1} & 1 \end{gathered} )$
    - It is the same

- **STEP 4** **The conclusion step: **Explain in** words** how the above steps make the result** true** for **all** integers, using the following **two **sentences:

  - "**If** it is true for $n=k$,* ***then** it is true for $n=k+1$."
  - "**As** it is true for $n=1$, the** **statement** **is true **for all** $n\inℤ^{+}$."

> **Worked Example**
> The matrix $M$ is given by $M = ( \begin{gathered} 2 2 \\ 0 1 \end{gathered} )$.
> 
> Prove, using mathematical induction, that $M^{n} = ( \begin{gathered} 2^{n} & 2 ( 2^{n} - 1 ) \\ 0 1 \end{gathered} )$ for all integers satisfying $n\geq1$.
> 
> > *STE P 1: The basic step*
> *Prove that it is true for* $n=1$
> 
> $\begin{gathered} M^{1} & = ( \begin{gathered} 2^{1} & 2 ( 2^{1} - 1 ) \\ 0 1 \end{gathered} ) \\ = ( \begin{gathered} 2 2 \\ 0 1 \end{gathered} ) \\ = M \end{gathered}$
> 
> > *State that it is true for* $n=1$
> 
> *It is true for* $n=1$
> 
> > * *
> 
> > *STEP 2: The assumption step*
> *Assume the formula is true for some* $n=k$ *where* $k$ *is a positive integer*
> 
> *Assume that* $M^{k} = ( \begin{gathered} 2^{k} & 2 ( 2^{k} - 1 ) \\ 0 1 \end{gathered} )$* *
> 
> > * *
> 
> > *STEP 3: The inductive step*
> *Look at the power of* $n=k+1$
> 
> $\begin{gathered} M^{k + 1} \end{gathered}$
> 
> > *Use index laws, then substitute in the assumption from STEP 2*
> 
> `| M ^ k + 1 | = M ^ k M ^ 1 | | _ = ( | 2 ^ k | 2 ( 2 ^ k - 1 ) | | 0 1 | ) ( | 2 2 | 0 1 | ) | |`
> 
> > *Use matrix multiplication to work out the right-hand side*
> *Simplify the terms*
> 
> * *$\begin{gathered} M^{k + 1} & = ( \begin{gathered} 2^{k \times 2 + 0 & 2^{k} \times 2 + 2 ( 2^{k} + 1} - 1 ) \times 1 \\ 0 + 0 & 0 + 1 \end{gathered} ) \\ = ( \begin{gathered} 2^{k + 1} & 2 \times 2^{k + 1} - 2 \\ 0 1 \end{gathered} ) \end{gathered}$
> 
> > *Check that this is the same as substituting* $n=k+1$ *into the formula for* $M^{n}$
> 
> * *$\begin{gathered} M^{k + 1} & = ( \begin{gathered} 2^{k + 1} & 2 ( 2^{k + 1} - 1 ) \\ 0 1 \end{gathered} ) \\ = ( \begin{gathered} 2^{k + 1} & 2 \times 2^{k + 1} - 2 \\ 0 1 \end{gathered} ) \end{gathered}$
> 
> > *State that the result is true for* $n=k+1$
> 
> *It is true for* $n=k+1$
> 
> > * *
> 
> > *STEP 4: The conclusion*
> *We have just proved that if the case when* $n=k$ *is true, then the case when* $n=k+1$ *is true*
> *We have also shown that the case when* $n=1$ *is true*
> *Those two parts come together to mean that* $n=1$* is true, so** *$n=2$ *is true, so* $n=3$ *is true, ... and so on*
> 
> **Final answer:** **If it is true for **$n=k$**, then it is true for **$n=k+1$**.**
> **As it is true for **$n=1$**, the statement is true for all **$n\inℤ^{+}$**.**
