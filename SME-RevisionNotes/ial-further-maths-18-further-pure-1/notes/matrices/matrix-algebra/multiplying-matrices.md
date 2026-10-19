---
note_id: "rn_ZHbHKcJHGNhPdqzh"
title: "Multiplying Matrices"
source: https://www.savemyexams.com/international-a-level/further-maths/edexcel/18/further-pure-1/revision-notes/matrices/matrix-algebra/multiplying-matrices
path: matrices/matrix-algebra/multiplying-matrices
updated_at: "2024-04-10T13:17:14.799Z"
spec_point_ids: ["spcpt_DFnsnvP295B5FmbK", "spcpt_zBy7BQ9swFbWk3ZJ"]
spec_point_codes: []
guided_study: false
---

# Multiplying Matrices

## Multiplying Matrices

> **Spec point** — `spcpt_DFnsnvP295B5FmbK`

## Multiplying Matrices

### How do I multiply a 2x2 matrix by a 2x1 matrix?

- Multiply the corresponding elements in the **row **of the **first** matrix with the corresponding elements in the **column** of the **second **matrix, writing their **sum** in the answer matrix
- The answer will be a **2 × 1 matrix**

  - `open parentheses table row a b row c d end table close parentheses open parentheses table row x row y end table close parentheses equals open parentheses table row cell a x plus b y end cell row cell c x plus d y end cell end table close parentheses`
- `open parentheses table row 1 2 row 3 4 end table close parentheses open parentheses table row 10 row 20 end table close parentheses equals open parentheses table row cell 1 cross times 10 plus 2 cross times 20 end cell row cell 3 cross times 10 plus 4 cross times 20 end cell end table close parentheses equals open parentheses table row cell 10 plus 40 end cell row cell 30 plus 80 end cell end table close parentheses equals open parentheses table row 50 row 110 end table close parentheses`

### How do I multiply a 2x2 matrix by another 2x2 matrix?

- Multiply the corresponding elements in the **row **of the **first** matrix with the corresponding elements in the **column** of the **second **matrix, writing their **sum** in the answer matrix
- The answer will be a **2 × 2** **matrix**

  - `open parentheses table row a b row c d end table close parentheses open parentheses table row A B row C D end table close parentheses equals open parentheses table row cell a A plus b C end cell cell a B plus b D end cell row cell c A plus d C end cell cell c B plus d D end cell end table close parentheses`
- `open parentheses table row 1 2 row 3 4 end table close parentheses open parentheses table row 5 10 row 20 25 end table close parentheses equals open parentheses table row cell 1 cross times 5 plus 2 cross times 20 end cell cell 1 cross times 10 plus 2 cross times 25 end cell row cell 3 cross times 5 plus 4 cross times 20 end cell cell 3 cross times 10 plus 4 cross times 25 end cell end table close parentheses equals open parentheses table row cell 5 plus 40 end cell cell 10 plus 50 end cell row cell 15 plus 80 end cell cell 30 plus 100 end cell end table close parentheses equals open parentheses table row 45 60 row 95 130 end table close parentheses`
- This process becomes more natural the more times you do it!

### How do I square a matrix?

- **Do not** square each individual element inside the matrix
- Write out a **matrix multiplication**

  - If `bold P equals open parentheses table row 2 4 row 1 cell negative 3 end cell end table close parentheses` then `bold P squared equals bold P cross times bold P equals open parentheses table row 2 4 row 1 cell negative 3 end cell end table close parentheses open parentheses table row 2 4 row 1 cell negative 3 end cell end table close parentheses equals open parentheses table row cell 2 cross times 2 plus 4 cross times 1 end cell cell 2 cross times 4 plus 4 cross times open parentheses negative 3 close parentheses end cell row cell 1 cross times 2 plus open parentheses negative 3 close parentheses cross times 1 end cell cell 1 cross times 4 plus open parentheses negative 3 close parentheses cross times open parentheses negative 3 close parentheses end cell end table close parentheses equals open parentheses table row 8 cell negative 4 end cell row cell negative 1 end cell 13 end table close parentheses`
- It is possible to have **negative** elements in a squared matrix

### How do I multiply matrices of any dimensions?

- To multiply a matrix by another matrix:

  - The **number of columns** in the **first **matrix must be **equal** to the **number of rows** in the **second **matrix
  - For example, the **first** matrix is $m\timesn$ and the **second** matrix is $n\timesp$
  - The **order **of the r**esultant** matrix will be $m\timesp$
- Multiply corresponding elements in the **row** of the **first** matrix with the corresponding elements in the **column** of the **second **matrix

  - Place their **sums** in the resultant matrix
  
    - For example, if `bold A equals open parentheses table row a b c row d e f end table close parentheses`, `bold B equals open parentheses table row g h row i j row k l end table close parentheses`
    - then `Error converting from MathML to accessible text.`
    - whereas  `bold BA equals open parentheses table row cell left parenthesis g a plus h d right parenthesis end cell cell left parenthesis g b plus h e right parenthesis end cell cell left parenthesis g c plus h f right parenthesis end cell row cell left parenthesis i a plus j d right parenthesis end cell cell left parenthesis i b plus j e right parenthesis end cell cell left parenthesis i c plus j f right parenthesis end cell row cell left parenthesis k a plus l d right parenthesis end cell cell left parenthesis k b plus l e right parenthesis end cell cell left parenthesis k c plus l f right parenthesis end cell end table close parentheses`
- It is possible for **AB **to exist but **BA***** ***not to exist

  - For **square matrices** of the same order, **AB***** ***and* ***BA***** ***will both exist

### What does commutative mean?

- **Commutative** means "swapping the order doesn't change the result"

  - 5 × 4 = 4 × 5 and 3 + 2 = 2 + 3
  
    - Multiplication and addition of **numbers** are commutative
  - 4 ÷ 2 ≠ 2 ÷ 4 and 5 - 3 ≠ 3 - 5
  
    - Division and subtraction of **numbers** are not commutative
- However,** matrix multiplication** is **not commutative**

  - In general **AB** ≠ **BA**
- For example, `open parentheses table row 1 2 row 3 4 end table close parentheses open parentheses table row 0 1 row 5 1 end table close parentheses equals open parentheses table row 10 3 row 20 7 end table close parentheses` but `open parentheses table row 0 1 row 5 1 end table close parentheses open parentheses table row 1 2 row 3 4 end table close parentheses equals open parentheses table row 3 4 row 8 14 end table close parentheses`

### What does associative mean?

- **Associative** means "it doesn't matter which order you group operations into"

  - To do 5 + 4 + 3, either (5 + 4) + 3 or 5 + (4 + 3) works
  - To do 8 × 9 × 10, either (8 × 9) × 10 or 8 × (9 × 10) works
  
    - Multiplication and addition of **numbers** are associative
  - (8 ÷ 4) ÷ 2 ≠ 8 ÷ (4 ÷ 2) and (5 - 4) - 3 ≠ 5 - (4 - 3)
  
    - Division and subtraction of **numbers** are not associative
- **Matrix multiplication** is** associative**

  - **(AB)C** ≡ **A(BC)**
- To multiply** three** matrices together, it is fine to either:

  - start by multiplying the first two together,
  - or start by multiplying the second two together
  
    - Just don't switch the order
    - **A(BC) **is not the same as **(BC)A**

> **Worked Example**
> If `bold P equals open parentheses table row 3 1 row cell negative 2 end cell 0 end table close parentheses`, `bold Q equals open parentheses table row 5 cell negative 5 end cell row 4 2 end table close parentheses` and `bold R equals open parentheses table row 10 cell negative 1 end cell 4 row 8 0 5 end table close parentheses`, find the following:
> 
> (a)  $\mathrm{PQ}$
> 
> > *Write out *$\mathrm{PQ}$* in full*
> 
> `open parentheses table row 3 1 row cell negative 2 end cell 0 end table close parentheses cross times open parentheses table row 5 cell negative 5 end cell row 4 2 end table close parentheses`
> 
> > *Multiply the matrices*
> 
> `open parentheses table row cell open parentheses 3 cross times 5 space plus space 1 cross times 4 close parentheses end cell cell open parentheses 3 cross times negative 5 space plus space 1 cross times 2 close parentheses end cell row cell open parentheses negative 2 cross times 5 space plus space 0 cross times 4 close parentheses end cell cell open parentheses negative 2 cross times negative 5 space plus space 0 cross times 2 close parentheses end cell end table close parentheses equals open parentheses table row cell open parentheses 15 space plus space 4 close parentheses end cell cell open parentheses negative 15 space plus space 2 close parentheses end cell row cell open parentheses negative 10 space plus space 0 close parentheses end cell cell open parentheses 10 space plus space 0 close parentheses end cell end table close parentheses`
> 
> > *Simplify*
> 
> `bold PQ equals open parentheses table row 19 cell negative 13 end cell row cell negative 10 end cell 10 end table close parentheses`
> 
> (b)  $\mathrm{PR}$
> 
> > *Write out *$\mathrm{PR}$* in full*
> 
> `open parentheses table row 3 1 row cell negative 2 end cell 0 end table close parentheses cross times open parentheses table row 10 cell negative 1 end cell 4 row 8 0 5 end table close parentheses`
> 
> > *The order (dimensions) agree, as *$P$* has 2 columns and *$R$* has 2 rows*
> *Multiply the matrices*
> 
> `open parentheses table row cell open parentheses 3 cross times 10 space plus space 1 cross times 8 close parentheses end cell cell open parentheses 3 cross times negative 1 space plus space 1 cross times 0 close parentheses end cell cell open parentheses 3 cross times 4 space plus space 1 cross times 5 close parentheses end cell row cell open parentheses negative 2 cross times 10 space plus space 0 cross times 8 close parentheses end cell cell open parentheses negative 2 cross times negative 1 space plus space 0 cross times 0 close parentheses end cell cell open parentheses negative 2 cross times 4 space plus space 0 cross times 5 close parentheses end cell end table close parentheses`
> 
> > *Simplify*
> 
> `bold PR equals open parentheses table row 38 cell negative 3 end cell 17 row cell negative 20 end cell 2 cell negative 8 end cell end table close parentheses`
> 
> (c)  $Q^{2}$
> 
> > *Write out *$Q^{2}$* as *$Q\timesQ$
> 
> `open parentheses table row 5 cell negative 5 end cell row 4 2 end table close parentheses cross times open parentheses table row 5 cell negative 5 end cell row 4 2 end table close parentheses`
> 
> > *Multiply the matrices*
> 
> `open parentheses table row cell open parentheses 5 cross times 5 space plus space minus 5 cross times 4 close parentheses end cell cell open parentheses 5 cross times negative 5 space plus space minus 5 cross times 2 close parentheses end cell row cell open parentheses 4 cross times 5 space plus space 2 cross times 4 close parentheses end cell cell open parentheses 4 cross times negative 5 space plus space 2 cross times 2 close parentheses end cell end table close parentheses equals open parentheses table row cell open parentheses 25 space plus space minus 20 close parentheses end cell cell open parentheses negative 25 space plus space minus 10 close parentheses end cell row cell open parentheses 20 space plus space 8 close parentheses end cell cell open parentheses negative 20 space plus space 4 close parentheses end cell end table close parentheses`
> 
> > *Simplify*
> 
> `bold Q squared equals open parentheses table row 5 cell negative 35 end cell row 28 cell negative 16 end cell end table close parentheses`
> 
> (d)  Explain why the matrix $\mathrm{RP}$ does not exist.
> 
> > *An *$m\timesn$*  matrix can only be multiplied by an *$n\timesp$*  matrix*
> 
> **Final answer:** **The order (dimensions) do not agree, as **$R$** has 3 columns but **$P$** has 2 rows**

## The Identity Matrix

> **Spec point** — `spcpt_zBy7BQ9swFbWk3ZJ`

## The Identity Matrix

### What is the Identity Matrix?

- The **identity** **matrix**, $I$, is a **square** matrix with:

  - **Ones** along the **leading diagonal** (from top-left to bottom-right)
  - and **zeros** everywhere else
  
    - The **2 × 2** identity matrix is `bold I equals open parentheses table row 1 0 row 0 1 end table close parentheses`
    - The **3 × 3** identity matrix is `bold I equals open parentheses table row 1 0 0 row 0 1 0 row 0 0 1 end table close parentheses`
  - The notation $I_{n}$ can be used to specify the $n\timesn$ identity matrix
- **Multiplying** any **square** matrix by the same-sized** identity** matrix leaves it **unchanged**

  - Both $\mathrm{AI}=A$ and $\mathrm{IA}=A$
  - `open parentheses table row a b row c d end table close parentheses open parentheses table row 1 0 row 0 1 end table close parentheses equals open parentheses table row a b row c d end table close parentheses`** **and `open parentheses table row 1 0 row 0 1 end table close parentheses open parentheses table row a b row c d end table close parentheses equals open parentheses table row a b row c d end table close parentheses`
  
    - This result can be proved by multiplying together the matrices

> **Exam Hint**
> The identity matrix is an important matrix which you should know or recognise as $I$ in a question.

> **Worked Example**
> If `bold A equals open parentheses table row 0 2 row 2 0 end table close parentheses` show that $A^{2}=4I$.
> 
> > *Write out *$A^{2}$* as *$A\timesA$
> 
> `open parentheses table row 0 2 row 2 0 end table close parentheses cross times open parentheses table row 0 2 row 2 0 end table close parentheses`
> 
> > *Multiply the matrices*
> 
> `table row cell open parentheses table row 0 2 row 2 0 end table close parentheses cross times open parentheses table row 0 2 row 2 0 end table close parentheses end cell equals cell open parentheses table row cell open parentheses 0 cross times 0 space plus space 2 cross times 2 close parentheses end cell cell open parentheses 0 cross times 2 space plus space 2 cross times 0 close parentheses end cell row cell open parentheses 2 cross times 0 space plus space 0 cross times 2 close parentheses end cell cell open parentheses 2 cross times 2 space plus space 0 cross times 0 close parentheses end cell end table close parentheses end cell row blank equals cell open parentheses table row 4 0 row 0 4 end table close parentheses end cell end table`
> 
> > *Write in terms of the identity matrix, *`bold I equals open parentheses table row 1 0 row 0 1 end table close parentheses`* **by factorising out 4*
> 
> `stretchy left parenthesis table row 4 0 row 0 4 end table stretchy right parenthesis equals 4 stretchy left parenthesis table row 1 0 row 0 1 end table stretchy right parenthesis equals 4 bold I`
