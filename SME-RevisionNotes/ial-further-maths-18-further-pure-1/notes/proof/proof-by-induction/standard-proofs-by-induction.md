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

- For example: prove that `sum from r equals 1 to n of r squared equals 1 over 6 n left parenthesis n plus 1 right parenthesis left parenthesis 2 n plus 1 right parenthesis`* *

  - It has a** left-hand** side, `L H S equals sum from r equals 1 to n of r squared`
  - and a **right-hand** side, $RHS=\frac{1}{6}n(n+1)(2n+1)$

- **STEP 1** **The basic step:** Show result is true for** **$n=1$

  - **Substitute*** *$n=1$ into both sides **individually** `L H S equals space sum from r equals 1 to 1 of r squared equals 1 squared equals 1
  R H S equals 1 over 6 cross times 1 cross times left parenthesis 1 plus 1 right parenthesis left parenthesis 2 cross times 1 plus 1 right parenthesis equals 1 over 6 cross times 2 cross times 3 equals 1`

- **STEP 2** **The assumption step: **Assume the *LHS  *and *RHS*  are equal for some $n=k$* *where $k$* *is some integer

  - Replace $n$ with $k$ in the statement
  - Write: "Assume `sum from r equals 1 to k of r squared equals 1 over 6 k left parenthesis k plus 1 right parenthesis left parenthesis 2 k plus 1 right parenthesis` is true"

- **STEP 3** **The inductive step: **You need to **prove **that the* LHS  *and *RHS*  are equal for $n=k+1$

  - **Start** with the ***LHS**** * for $n=k+1$
  
    - Take the** last** term out: `sum from r equals 1 to k plus 1 of r to the power of 2 space end exponent equals sum from r equals 1 to k of r squared space plus open parentheses k plus 1 close parentheses squared`
    - **Substitute** in the **assumption **(STEP 2) :
    - `sum from r equals 1 to k plus 1 of r to the power of 2 space end exponent equals 1 over 6 k left parenthesis k plus 1 right parenthesis left parenthesis 2 k plus 1 right parenthesis space plus open parentheses k plus 1 close parentheses squared`
    - **Factorise**: 
    `1 over 6 open parentheses k plus 1 close parentheses left square bracket k left parenthesis 2 k plus 1 right parenthesis plus 6 open parentheses k plus 1 close parentheses right square bracket
    equals 1 over 6 open parentheses k plus 1 close parentheses left square bracket 2 k squared plus 7 k plus 6 right square bracket
    equals 1 over 6 open parentheses k plus 1 close parentheses open parentheses k plus 2 close parentheses open parentheses 2 k plus 3 close parentheses`
  - **Check** if it is the **same** as the** *****RHS***** ** for $n=k+1$ `table row cell R H S end cell equals cell 1 over 6 open parentheses k plus 1 close parentheses open parentheses open parentheses k plus 1 close parentheses plus 1 close parentheses open parentheses 2 open parentheses k plus 1 close parentheses plus 1 close parentheses end cell row blank equals cell 1 over 6 open parentheses k plus 1 close parentheses open parentheses k plus 2 close parentheses open parentheses 2 k plus 3 close parentheses end cell end table`
  - So** *****LHS*****  = *****RHS*****  **for $n=k+1$, as long as the **assumption** is true

- **STEP 4** **The conclusion step: **Explain in** words** how the above steps make the result** true** for **all** integers, using the following **two **sentences:

  - "**If** it is true for $n=k$,* ***then** it is true for $n=k+1$."
  - "**As** it is true for $n=1$, the** **statement** **is true **for all** $n\inℤ^{+}$."

> **Worked Example**
> Prove by induction that `sum from r equals 1 to n of r open parentheses r minus 3 close parentheses equals 1 third n open parentheses n minus 4 close parentheses open parentheses n plus 1 close parentheses` for $n\inℤ^{+}$.
> 
> > *STE P 1: The basic step*
> *Find the LHS when *$n=1$
> 
> `sum from r equals 1 to 1 of r open parentheses r minus 3 close parentheses equals 1 open parentheses 1 minus 3 close parentheses equals negative 2`* *
> 
> > *Find the RHS when** *$n=1$
> 
> `1 third cross times 1 cross times open parentheses 1 minus 4 close parentheses open parentheses 1 plus 1 close parentheses equals 1 third cross times open parentheses negative 6 close parentheses equals negative 2`* *
> 
> > *The LHS and RHS are equal, which shows the statement is true for *$n=1$
> *State this*
> 
> *LHS = RHS, so it is true for *$n=1$
> 
> > *  *
> 
> > *STEP 2: The assumption step*
> *Assume the statement is true for some *$n=k$* where *$k$* **is a positive integer*
> 
> *Assume that *`sum from r equals 1 to k of r open parentheses r minus 3 close parentheses equals 1 third k open parentheses k minus 4 close parentheses open parentheses k plus 1 close parentheses`
> 
> > * *
> 
> > *STEP 3: The inductive step*
> *Find the RHS when *$n=k+1$
> 
> > `1 third open parentheses k plus 1 close parentheses open parentheses k plus 1 minus 4 close parentheses open parentheses k plus 1 plus 1 close parentheses equals 1 third open parentheses k plus 1 close parentheses open parentheses k minus 3 close parentheses open parentheses k plus 2 close parentheses`* *
> 
> > *Find the LHS when *$n=k+1$
> 
> `sum from r equals 1 to k plus 1 of r open parentheses r minus 3 close parentheses`
> 
> > *Prove that the LHS when *$n=k+1$* equals the RHS when *$n=k+1$
> *Start by pulling out the final term in the sum*
> 
> `table row cell sum from r equals 1 to k plus 1 of r open parentheses r minus 3 close parentheses end cell equals cell sum from r equals 1 to k of r open parentheses r minus 3 close parentheses plus open parentheses k plus 1 close parentheses open parentheses k plus 1 minus 3 close parentheses end cell row blank equals cell sum from r equals 1 to k of r open parentheses r minus 3 close parentheses plus open parentheses k plus 1 close parentheses open parentheses k minus 2 close parentheses end cell end table`
> 
> > *Now use the assumption in STEP 2 to replace the sum from 1 to *$k$* with its answer *
> 
> `table row cell sum from r equals 1 to k plus 1 of r open parentheses r minus 3 close parentheses end cell equals cell 1 third k open parentheses k minus 4 close parentheses open parentheses k plus 1 close parentheses plus open parentheses k plus 1 close parentheses open parentheses k minus 2 close parentheses end cell end table`
> 
> > *Now factorise the right-hand side*
> 
> `table row cell sum from r equals 1 to k plus 1 of r open parentheses r minus 3 close parentheses end cell equals cell open parentheses k plus 1 close parentheses open square brackets 1 third k open parentheses k minus 4 close parentheses plus open parentheses k minus 2 close parentheses close square brackets end cell row blank equals cell 1 third open parentheses k plus 1 close parentheses open square brackets k open parentheses k minus 4 close parentheses plus 3 open parentheses k minus 2 close parentheses close square brackets end cell end table`
> 
> > *Expand inside the square brackets then continue to factorise*
> 
> `table row cell sum from r equals 1 to k plus 1 of r open parentheses r minus 3 close parentheses end cell equals cell 1 third open parentheses k plus 1 close parentheses open square brackets k squared minus 4 k plus 3 k minus 6 close square brackets end cell row blank equals cell 1 third open parentheses k plus 1 close parentheses open square brackets k squared minus k minus 6 close square brackets end cell row blank equals cell 1 third open parentheses k plus 1 close parentheses open parentheses k minus 3 close parentheses open parentheses k plus 2 close parentheses end cell end table`
> 
> > *This is the same as the RHS when *$n=k+1$
> *The LHS and RHS are equal, which shows that the statement is true for *$n=k+1$
> *State this*
> 
> *LHS = RHS, so it is true for *$n=k+1$
> 
> > * *
> 
> > *STEP 4: The conclusion*
> *We have just proved that if the case when *$n=k$* is true, then the case when *$n=k+1$* is true*
> *We have also shown that the case when *$n=1$* is true*
> *Those two parts come together to mean that *$n=1$* is true, so** *$n=2$* is true, so *$n=3$* is true, ... and so on*
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
  - `straight f open parentheses 1 close parentheses equals 4 to the power of 1 minus 1 equals 3`which is divisible by 3

- **STEP 2** **The assumption step: **Assume $f(k)=4^{k}-1$ is divisible by 3 for some $n=k$* *where $k$* *is some integer

  - Replace $n$ with $k$ in the statement
  - Write "divisible by 3" as "$=3m$" where $m$ is a positive integer
  - So`straight f open parentheses k close parentheses equals 4 to the power of k minus 1 equals 3 m` where $m\inℤ^{+}$
  - It helps to make $4^{k}$ the **subject**: $4^{k}=1+3m$

- **STEP 3** **The inductive step (method 1): **You need to show that the $n=k+1$ case is divisible by 3

  - Substitute $n=k+1$ into the function
  
    - $f(k+1)=4^{k+1}-1$
  - Use** index laws** to substitute in the **assumption **(STEP 2)  $4^{k}=1+3m$
  
    - `straight f left parenthesis k plus 1 right parenthesis equals 4 open parentheses 4 to the power of k close parentheses minus 1 equals 4 open parentheses 1 plus 3 m close parentheses minus 1 equals 3 open parentheses 4 m plus 1 close parentheses`which is a multiple of 3
  - So $f(k+1)$is divisible by 3 (as long as the **assumption** is true)

- **STEP 3** **The inductive step (method 2): **An **alternative method ** is to show that the **difference** $f(k+1)-f(k)$  is a multiple of 3

  - i.e.  $f(k+1)-f(k)=3\times...$
  - Making $f(k+1)$the subject gives `straight f left parenthesis k plus 1 right parenthesis equals straight f open parentheses k close parentheses plus 3 cross times...`
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
> *Prove that it is true for *$n=0$
> 
> `table row cell straight f open parentheses 0 close parentheses end cell equals cell 6 to the power of 0 plus 13 to the power of 0 plus 1 end exponent end cell row blank equals cell 1 plus 13 end cell row blank equals 14 row blank equals cell 7 cross times 2 end cell end table`
> 
> > *State that it is true for *$n=0$
> 
> *14 is divisible by 7, so it is true for *$n=0$
> 
> > * *
> 
> > *STEP 2: The assumption step*
> *Assume the statement is true for some *$n=k$* where *$k$* is a positive integer*
> 
> *Assume that *$f(k)=6^{k}+13^{k+1}$* is divisible by 7*
> 
> > *Replace "being divisible by 7" with being equal to *$7m$*, where *$m$* is a positive integer*
> 
> $6^{k}+13^{k+1}=7m$
> 
> > * *
> 
> > *STEP 3: The inductive step*
> *Substitute *$n=k+1$* into the function*
> 
> `table row cell straight f left parenthesis k plus 1 right parenthesis end cell equals cell 6 to the power of k plus 1 end exponent plus 13 to the power of open parentheses k plus 1 close parentheses plus 1 end exponent end cell row blank equals cell 6 to the power of k plus 1 end exponent plus 13 to the power of k plus 2 end exponent end cell end table`
> 
> > *Now make either *$6^{k}$* or *$13^{k+1}$* the subject of STEP 2 and substitute it in*
> *It helps to use index laws first*
> 
> `table row cell straight f left parenthesis k plus 1 right parenthesis end cell equals cell 6 to the power of k cross times 6 plus 13 to the power of k plus 2 end exponent end cell row blank equals cell open parentheses 7 m minus 13 to the power of k plus 1 end exponent close parentheses cross times 6 plus 13 to the power of k plus 2 end exponent end cell end table`
> 
> > *Simplify the terms, using index laws to group the *$13^{k+1}$* terms*
> 
> `table row cell straight f left parenthesis k plus 1 right parenthesis end cell equals cell 42 m minus 6 cross times 13 to the power of k plus 1 end exponent plus 13 to the power of k plus 2 end exponent end cell row blank equals cell 42 m minus 6 cross times 13 to the power of k plus 1 end exponent plus 13 cross times 13 to the power of k plus 1 end exponent end cell row blank equals cell 42 m plus left parenthesis negative 6 plus 13 right parenthesis cross times 13 to the power of k plus 1 end exponent end cell row blank equals cell 42 m plus 7 cross times 13 to the power of k plus 1 end exponent end cell end table`
> 
> > *The goal is to show that this result is divisible by 7*
> *Factorise out a 7 to show this*
> 
> `table row cell straight f left parenthesis k plus 1 right parenthesis end cell equals cell 7 cross times open parentheses 6 m plus 13 to the power of k plus 1 end exponent close parentheses end cell end table`
> 
> > *State that it is true for *$n=k+1$
> 
> `straight f open parentheses k plus 1 close parentheses`* is divisible by 7, so it is true for *$n=k+1$
> 
> > * *
> 
> > *STEP 4: The conclusion*
> *We have just proved that if the case when *$n=k$* is true, then the case when *$n=k+1$* is true*
> *We have also shown that the case when *$n=0$* is true*
> *Those two parts come together to mean that *$n=0$* is true, so** *$n=1$* is true, so *$n=2$* is true, ... and so on*
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
  
    - `u subscript k plus 1 end subscript equals 3 open parentheses 3 to the power of k minus 2 close parentheses plus 4 equals 3 to the power of k plus 1 end exponent minus 2`
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
> *Find *$u_{1}$* from the recursive sequence*
> 
> $u_{1}=2$
> 
> > *Find *$u_{1}$* from the **n*<sup>*th*</sup>* term formula*
> 
> `table row cell u subscript 1 end cell equals cell 5 to the power of 1 minus 1 end exponent plus 1 end cell row blank equals cell 5 to the power of 0 plus 1 end cell row blank equals cell 1 plus 1 end cell row blank equals 2 end table`
> 
> > *These two terms are equal*
> *State that it is true for *$n=1$
> 
> *It is true for *$n=1$
> 
> > * *
> 
> > *STEP 2: The assumption step*
> *Assume the formula is true for some *$n=k$* where *$k$* is a positive integer*
> 
> *Assume that *$u_{k}=5^{k-1}+1$
> 
> > * *
> 
> > *STEP 3: The inductive step*
> *Use the recursive sequence to write *$u_{k+1}$* in terms of *$u_{k}$
> 
> `table row cell u subscript k plus 1 end subscript end cell equals cell 5 u subscript k minus 4 end cell end table`
> 
> > *Replace *$u_{k}$* with the assumption in STEP 2 and simplify*
> 
> `table row cell u subscript k plus 1 end subscript end cell equals cell 5 open parentheses 5 to the power of k minus 1 end exponent plus 1 close parentheses minus 4 end cell row blank equals cell 5 to the power of k plus 5 minus 4 end cell row blank equals cell 5 to the power of k plus 1 end cell end table`
> 
> > *Check that this is the same as substituting *$n=k+1$* into the **n*<sup>*th*</sup>* term formula *
> 
> `table row cell u subscript k plus 1 end subscript end cell equals cell 5 to the power of open parentheses k plus 1 close parentheses minus 1 end exponent plus 1 end cell row blank equals cell 5 to the power of k plus 1 end cell end table`
> 
> > *State that the result is true for *$n=k+1$
> 
> *It is true for *$n=k+1$
> 
> > * *
> 
> > *STEP 4: The conclusion*
> *We have just proved that if the case when *$n=k$* is true, then the case when *$n=k+1$* is true*
> *We have also shown that the case when *$n=1$* is true*
> *Those two parts come together to mean that *$n=1$* is true, so** *$n=2$* is true, so *$n=3$* is true, ... and so on*
> 
> **Final answer:** **If it is true for **$n=k$**, then it is true for **$n=k+1$**.**
> **As it is true for **$n=1$**, the statement is true for all **$n\inℤ^{+}$**.**

## Proof by Induction with Matrices

> **Spec point** — `spcpt_6NkRppSFKD89hB3j`

## Proof by Induction with Matrices

### What are the steps for proof by induction with matrices?

- For example: prove that `bold M to the power of n equals open parentheses table row cell 2 to the power of n end cell 0 row cell 1 minus 2 to the power of n end cell 1 end table close parentheses` where `bold M equals open parentheses table row 2 0 row cell negative 1 end cell 1 end table close parentheses` for all integers $n\geq1$.

- **STEP 1** **The basic step:** Show result is true for** **$n=1$

  - **Substitute*** *$n=1$ into formula
  - `bold M to the power of 1 equals end exponent open parentheses table row cell 2 to the power of 1 end cell 0 row cell 1 minus 2 to the power of 1 end cell 1 end table close parentheses equals open parentheses table row 2 0 row cell negative 1 end cell 1 end table close parentheses equals bold M`

- **STEP 2** **The assumption step: **Assume `bold M to the power of k equals open parentheses table row cell 2 to the power of k end cell 0 row cell 1 minus 2 to the power of k end cell 1 end table close parentheses` is true for some $n=k$* *where $k$* *is some integer

  - Replace $n$ with $k$ in the statement

- **STEP 3** **The inductive step: **You need to show that the $n=k+1$ case is true

  - Use **index laws** to write $M^{k+1}=\mathrm{MM}^{k}$
  - Substitute in the** assumption**: `bold M to the power of k plus 1 end exponent equals bold M open parentheses table row cell 2 to the power of k end cell 0 row cell 1 minus 2 to the power of k end cell 1 end table close parentheses equals open parentheses table row 2 0 row cell negative 1 end cell 1 end table close parentheses open parentheses table row cell 2 to the power of k end cell 0 row cell 1 minus 2 to the power of k end cell 1 end table close parentheses`
  - **Multiply** the matrices
  
    - `bold M to the power of k plus 1 end exponent equals open parentheses table row cell 2 to the power of k plus 1 end exponent end cell 0 row cell 1 minus 2 cross times 2 to the power of k end cell 1 end table close parentheses equals open parentheses table row cell 2 to the power of k plus 1 end exponent end cell 0 row cell 1 minus 2 to the power of k plus 1 end exponent end cell 1 end table close parentheses`
  - **Check** if it is the same as the formula with $n=k+1$
  
    - `bold M to the power of k plus 1 end exponent equals open parentheses table row cell 2 to the power of k plus 1 end exponent end cell 0 row cell 1 minus 2 to the power of k plus 1 end exponent end cell 1 end table close parentheses`
    - It is the same

- **STEP 4** **The conclusion step: **Explain in** words** how the above steps make the result** true** for **all** integers, using the following **two **sentences:

  - "**If** it is true for $n=k$,* ***then** it is true for $n=k+1$."
  - "**As** it is true for $n=1$, the** **statement** **is true **for all** $n\inℤ^{+}$."

> **Worked Example**
> The matrix $M$ is given by `bold M equals open parentheses table row 2 2 row 0 1 end table close parentheses`.
> 
> Prove, using mathematical induction, that `bold M to the power of n equals open parentheses table row cell 2 to the power of n end cell cell 2 left parenthesis 2 to the power of n minus 1 right parenthesis end cell row 0 1 end table close parentheses` for all integers satisfying $n\geq1$.
> 
> > *STE P 1: The basic step*
> *Prove that it is true for *$n=1$
> 
> `table row cell bold M to the power of 1 end cell equals cell open parentheses table row cell 2 to the power of 1 end cell cell 2 open parentheses 2 to the power of 1 minus 1 close parentheses end cell row 0 1 end table close parentheses end cell row blank equals cell open parentheses table row 2 2 row 0 1 end table close parentheses end cell row blank equals bold M end table`
> 
> > *State that it is true for *$n=1$
> 
> *It is true for *$n=1$
> 
> > * *
> 
> > *STEP 2: The assumption step*
> *Assume the formula is true for some *$n=k$* where *$k$* is a positive integer*
> 
> *Assume that *`bold M to the power of k equals open parentheses table row cell 2 to the power of k end cell cell 2 left parenthesis 2 to the power of k minus 1 right parenthesis end cell row 0 1 end table close parentheses`* *
> 
> > * *
> 
> > *STEP 3: The inductive step*
> *Look at the power of *$n=k+1$
> 
> `table row blank blank cell bold M to the power of k plus 1 end exponent end cell end table`
> 
> > *Use index laws, then substitute in the assumption from STEP 2*
> 
> `table row cell bold M to the power of k plus 1 end exponent end cell equals cell bold M to the power of k bold M to the power of bold 1 end cell row blank equals cell open parentheses table row cell 2 to the power of k end cell cell 2 left parenthesis 2 to the power of k minus 1 right parenthesis end cell row 0 1 end table close parentheses open parentheses table row 2 2 row 0 1 end table close parentheses end cell end table`
> 
> > *Use matrix multiplication to work out the right-hand side*
> *Simplify the terms*
> 
> * *`table row cell bold M to the power of k plus 1 end exponent end cell equals cell open parentheses table row cell 2 to the power of k cross times 2 plus 0 end cell cell space space 2 to the power of k cross times 2 plus 2 left parenthesis 2 to the power of k plus 1 end exponent minus 1 right parenthesis cross times 1 end cell row cell 0 plus 0 end cell cell 0 plus 1 end cell end table close parentheses end cell row blank equals cell open parentheses table row cell 2 to the power of k plus 1 end exponent end cell cell space space 2 cross times 2 to the power of k plus 1 end exponent minus 2 end cell row 0 1 end table close parentheses end cell end table`
> 
> > *Check that this is the same as substituting *$n=k+1$* into the formula for *$M^{n}$
> 
> * *`table row cell bold M to the power of k plus 1 end exponent end cell equals cell open parentheses table row cell 2 to the power of k plus 1 end exponent end cell cell 2 left parenthesis 2 to the power of k plus 1 end exponent minus 1 right parenthesis end cell row 0 1 end table close parentheses end cell row blank equals cell open parentheses table row cell 2 to the power of k plus 1 end exponent end cell cell 2 cross times 2 to the power of k plus 1 end exponent minus 2 end cell row 0 1 end table close parentheses end cell end table`
> 
> > *State that the result is true for *$n=k+1$
> 
> *It is true for *$n=k+1$
> 
> > * *
> 
> > *STEP 4: The conclusion*
> *We have just proved that if the case when *$n=k$* is true, then the case when *$n=k+1$* is true*
> *We have also shown that the case when *$n=1$* is true*
> *Those two parts come together to mean that *$n=1$* is true, so** *$n=2$* is true, so *$n=3$* is true, ... and so on*
> 
> **Final answer:** **If it is true for **$n=k$**, then it is true for **$n=k+1$**.**
> **As it is true for **$n=1$**, the statement is true for all **$n\inℤ^{+}$**.**
