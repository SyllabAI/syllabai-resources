---
note_id: "rn_p5HCc4mQthDm6Z6w"
title: "Multiplying Matrices"
source: https://www.savemyexams.com/igcse/maths/edexcel/b/16/revision-notes/matrices/properties-of-matrices/multiplying-matrices
path: matrices/properties-of-matrices/multiplying-matrices
updated_at: "2026-01-14T10:53:48.747Z"
spec_point_ids: ["spcpt_gWpj9n8N6CP4TnDv"]
spec_point_codes: []
guided_study: false
---

# Multiplying Matrices

## Multiplying matrices

> **Spec point** — `spcpt_gWpj9n8N6CP4TnDv`

## Multiplying matrices

### How do I multiply two matrices?

- To **multiply** two matrices

  - the number of **columns** in the first matrix
  - must be **equal** to the number of **rows** in the second matrix
- For example, consider `bold A equals open parentheses table row 1 3 row 7 4 end table close parentheses` and `bold B equals open parentheses table row 1 0 5 row 8 2 9 end table close parentheses`

  - You can multiply $A\timesB$
  
    - because the number of columns in $A$ (2) matches the number of rows in $B$ (2)
  - But you cannot multiply $B\timesA$
  
    - because the number of columns in $B$ (3) does not match the number of rows in $A$ (2)
- Multiplying matrices involves

  - multiplying the corresponding elements in a **row **of the **first** matrix
  
    - with the corresponding elements in a **column** of the **second **matrix
    - and writing the **sum** of the products in the answer matrix
  - It is easiest to see this through some examples
  - The process becomes more natural the more times you do it!

#### How do I multiply a 2×2 matrix by a 2×1 matrix?

- The answer will be a 2 x 1 matrix
- Multiply the corresponding elements in the **row **of the **first** matrix with the corresponding elements in the **column** of the **second **matrix, writing their **sum** in the answer matrix

  - `open parentheses table row a b row c d end table close parentheses open parentheses table row x row y end table close parentheses equals open parentheses table row cell a x plus b y end cell row cell c x plus d y end cell end table close parentheses`
- `open parentheses table row 1 2 row 3 4 end table close parentheses open parentheses table row 10 row 20 end table close parentheses equals open parentheses table row cell 1 cross times 10 plus 2 cross times 20 end cell row cell 3 cross times 10 plus 4 cross times 20 end cell end table close parentheses equals open parentheses table row cell 10 plus 40 end cell row cell 30 plus 80 end cell end table close parentheses equals open parentheses table row 50 row 110 end table close parentheses`

#### How do I multiply a 2×2 matrix by another 2×2 matrix?

- The answer will be a 2 x 2 matrix
- Multiply the corresponding elements in the **row **of the **first** matrix with the corresponding elements in the **column** of the **second **matrix, writing their **sum** in the answer matrix

  - `open parentheses table row a b row c d end table close parentheses open parentheses table row A B row C D end table close parentheses equals open parentheses table row cell a A plus b C end cell cell a B plus b D end cell row cell c A plus d C end cell cell c B plus d D end cell end table close parentheses`
- `open parentheses table row 1 2 row 3 4 end table close parentheses open parentheses table row 5 10 row 20 25 end table close parentheses equals open parentheses table row cell 1 cross times 5 plus 2 cross times 20 end cell cell 1 cross times 10 plus 2 cross times 25 end cell row cell 3 cross times 5 plus 4 cross times 20 end cell cell 3 cross times 10 plus 4 cross times 25 end cell end table close parentheses equals open parentheses table row cell 5 plus 40 end cell cell 10 plus 50 end cell row cell 15 plus 80 end cell cell 30 plus 100 end cell end table close parentheses equals open parentheses table row 45 60 row 95 130 end table close parentheses`

#### How do I multiply a 2×2 matrix by a 2×3 matrix?

- The answer will be a 2 x 3 matrix
- Multiply the corresponding elements in the **row **of the **first** matrix with the corresponding elements in the **column** of the **second **matrix, writing their **sum** in the answer matrix

  - `open parentheses table row a b row c d end table close parentheses open parentheses table row A B C row D E F end table close parentheses equals open parentheses table row cell a A plus b D end cell cell a B plus b E end cell row cell c A plus d D end cell cell c B plus d E end cell end table table row cell a C plus b F end cell row cell c C plus d F end cell end table close parentheses`
- `table row cell open parentheses table row 1 3 row 7 4 end table close parentheses open parentheses table row 1 0 5 row 8 2 9 end table close parentheses end cell equals cell open parentheses table row cell 1 cross times 1 plus 3 cross times 8 end cell cell 1 cross times 0 plus 3 cross times 2 end cell row cell 7 cross times 1 plus 4 cross times 8 end cell cell 7 cross times 0 plus 4 cross times 2 end cell end table table row cell 1 cross times 5 plus 3 cross times 9 end cell row cell 7 cross times 5 plus 4 cross times 9 end cell end table close parentheses end cell row blank equals cell open parentheses table row cell 1 plus 24 end cell cell 0 plus 6 end cell row cell 7 plus 32 end cell cell 0 plus 8 end cell end table table row cell 5 plus 27 end cell row cell 35 plus 36 end cell end table close parentheses end cell row blank equals cell open parentheses table row 25 6 row 39 8 end table table row 32 row 71 end table close parentheses end cell end table`

#### How do I multiply a 3×3 matrix by another 3×3 matrix?

- The answer will be a 3 x 3 matrix
- Multiply the corresponding elements in the **row **of the **first** matrix with the corresponding elements in the **column** of the **second **matrix, writing their **sum** in the answer matrix

  - `open parentheses table row a b c row d e f row g h i end table close parentheses open parentheses table row A B C row D E F row G H I end table close parentheses equals open parentheses table row cell a A plus b D plus c G end cell cell a B plus b E plus c H end cell cell a C plus b F plus c I end cell row cell d A plus e D plus f G end cell cell d B plus e E plus f H end cell cell d C plus e F plus f I end cell row cell g A plus h D plus i G end cell cell g B plus h E plus i H end cell cell g C plus h F plus i I end cell end table close parentheses`
- `table row cell open parentheses table row 1 0 3 row 0 cell negative 5 end cell 0 row 2 7 1 end table close parentheses open parentheses table row 0 2 3 row cell negative 1 end cell 0 cell negative 2 end cell row 4 0 6 end table close parentheses end cell equals cell open parentheses table row cell 1 cross times 0 plus 0 cross times open parentheses negative 1 close parentheses plus 3 cross times 4 end cell cell 1 cross times 2 plus 0 cross times 0 plus 3 cross times 0 end cell cell 1 cross times 3 plus 0 cross times open parentheses negative 2 close parentheses plus 3 cross times 6 end cell row cell 0 cross times 0 plus open parentheses negative 5 close parentheses cross times open parentheses negative 1 close parentheses plus 0 cross times 4 end cell cell 0 cross times 2 plus open parentheses negative 5 close parentheses cross times 0 plus 0 cross times 0 end cell cell 0 cross times 3 plus open parentheses negative 5 close parentheses cross times open parentheses negative 2 close parentheses plus 0 cross times 6 end cell row cell 2 cross times 0 plus 7 cross times open parentheses negative 1 close parentheses plus 1 cross times 4 end cell cell 2 cross times 2 plus 7 cross times 0 plus 1 cross times 0 end cell cell 2 cross times 3 plus 7 cross times open parentheses negative 2 close parentheses plus 1 cross times 6 end cell end table close parentheses end cell row blank equals cell open parentheses table row cell 0 plus 0 plus 12 end cell cell 2 plus 0 plus 0 end cell cell 3 plus 0 plus 18 end cell row cell 0 plus 5 plus 0 end cell cell 0 plus 0 plus 0 end cell cell 0 plus 10 plus 0 end cell row cell 0 minus 7 plus 4 end cell cell 4 plus 0 plus 0 end cell cell 6 minus 14 plus 6 end cell end table close parentheses end cell row blank equals cell open parentheses table row 12 2 21 row 5 0 10 row cell negative 3 end cell 4 cell negative 2 end cell end table close parentheses end cell end table`

### How do I square a matrix?

- Only **square matrices** (2 x 2 or 3 x 3) can be squared
- **Do not** square each individual element
- Write out a matrix multiplication

  - E.g. if `bold P equals open parentheses table row 2 4 row 1 cell negative 3 end cell end table close parentheses` then `bold P squared equals bold P cross times bold P equals open parentheses table row 2 4 row 1 cell negative 3 end cell end table close parentheses open parentheses table row 2 4 row 1 cell negative 3 end cell end table close parentheses equals open parentheses table row cell 2 cross times 2 plus 4 cross times 1 end cell cell 2 cross times 4 plus 4 cross times open parentheses negative 3 close parentheses end cell row cell 1 cross times 2 plus open parentheses negative 3 close parentheses cross times 1 end cell cell 1 cross times 4 plus open parentheses negative 3 close parentheses cross times open parentheses negative 3 close parentheses end cell end table close parentheses equals open parentheses table row 8 cell negative 4 end cell row cell negative 1 end cell 13 end table close parentheses`
- It is possible to have **negative** elements after squaring a matrix

### When multiplying, does it matter which matrix is on the left and which is on the right?

- When **multiplying numbers** "swapping the order doesn't change the result"

  - E.g. 5 × 4 = 4 × 5
- This is **not true** for **matrix multiplication**

  - In general, **AB** ≠ **BA**
- For example, `open parentheses table row 1 2 row 3 4 end table close parentheses open parentheses table row 0 1 row 5 1 end table close parentheses equals open parentheses table row 10 3 row 20 7 end table close parentheses` but `open parentheses table row 0 1 row 5 1 end table close parentheses open parentheses table row 1 2 row 3 4 end table close parentheses equals open parentheses table row 3 4 row 8 14 end table close parentheses`

### How can I multiply more than two matrices together?

- When **multiplying numbers** "it doesn't matter which order you group operations into"

  - E.g. to do 8 x 9 x 10, either (8 x 9) x 10 or 8 x (9 x 10) works
- This is **also true** for **matrix multiplication**

  - **(AB)C** ≡ **A(BC)**
- To multiply** three** matrices together

  - it's fine to start by multiplying the first two together
  
    - then multiplying the answer with the third matrix
  - or to start by multiplying the second two together
  
    - then multiplying the answer with the first matrix
- Just don't switch the order

  - **A(BC) **is not the same as **(BC)A**

### What is special about the identity matrix?

- **Multiplying **any 2×2 or 3×3 matrix by the corresponding ***identity matrix*** leaves it **unchanged**

  - $\mathrm{AI}=A$ and $\mathrm{IA}=A$
- For example, in the 2×2 case

  - `open parentheses table row a b row c d end table close parentheses open parentheses table row 1 0 row 0 1 end table close parentheses equals open parentheses table row a b row c d end table close parentheses`** **and `open parentheses table row 1 0 row 0 1 end table close parentheses open parentheses table row a b row c d end table close parentheses equals open parentheses table row a b row c d end table close parentheses`
  - This result can be proved by multiplying together the two matrices on the left side of each equation
- The 2×2 identity matrix also leaves a 2×1 matrix unchanged

  - `open parentheses table row 1 0 row 0 1 end table close parentheses open parentheses table row a row b end table close parentheses equals open parentheses table row a row b end table close parentheses`
  - This can be relevant to [matrix transformations](https://www.savemyexams.com/igcse/maths/edexcel/b/16/revision-notes/matrices/transformations-using-matrices/transforming-a-point/)
- The identity matrix is an important matrix which you should know (or recognise as $I$ in a question)

> **Worked Example**
> If `bold P equals open parentheses table row 3 1 row cell negative 2 end cell 0 end table close parentheses`, `bold Q equals open parentheses table row 5 cell negative 5 end cell row 4 2 end table close parentheses` and `bold R equals open parentheses table row 10 row 8 end table close parentheses`, find the following:
> 
> (i)  $\mathrm{PR}$
> 
> (ii)  $\mathrm{PQ}$
> 
> (iii)  $Q^{2}$
> 
> **Answer:**
> 
> (i)*  **Write out *$\mathrm{PR}$* in full*
> 
> `open parentheses table row 3 1 row cell negative 2 end cell 0 end table close parentheses cross times open parentheses table row 10 row 8 end table close parentheses`
> 
> > *Multiply the matrices*
> 
> `open parentheses table row cell open parentheses 3 cross times 10 close parentheses plus open parentheses 1 cross times 8 close parentheses end cell row cell open parentheses negative 2 cross times 10 close parentheses plus open parentheses 0 cross times 8 close parentheses end cell end table close parentheses`
> 
> > *Simplify*
> 
> `Error converting from MathML to accessible text.`
> 
> (ii)*  **Write out *$\mathrm{PQ}$* in full*
> 
> `open parentheses table row 3 1 row cell negative 2 end cell 0 end table close parentheses cross times open parentheses table row 5 cell negative 5 end cell row 4 2 end table close parentheses`
> 
> > *Multiply the matrices*
> 
> `open parentheses table row cell open parentheses 3 cross times 5 space plus space 1 cross times 4 close parentheses end cell cell open parentheses 3 cross times negative 5 space plus space 1 cross times 2 close parentheses end cell row cell open parentheses negative 2 cross times 5 space plus space 0 cross times 4 close parentheses end cell cell open parentheses negative 2 cross times negative 5 space plus space 0 cross times 2 close parentheses end cell end table close parentheses equals open parentheses table row cell open parentheses 15 space plus space 4 close parentheses end cell cell open parentheses negative 15 space plus space 2 close parentheses end cell row cell open parentheses negative 10 space plus space 0 close parentheses end cell cell open parentheses 10 space plus space 0 close parentheses end cell end table close parentheses`
> 
> > *Simplify*
> 
> `Error converting from MathML to accessible text.`
> 
> (iii)*  **Write out *$Q^{2}$* as *$Q\timesQ$
> 
> `open parentheses table row 5 cell negative 5 end cell row 4 2 end table close parentheses cross times open parentheses table row 5 cell negative 5 end cell row 4 2 end table close parentheses`
> 
> > *Multiply the matrices*
> 
> `open parentheses table row cell open parentheses 5 cross times 5 space plus space minus 5 cross times 4 close parentheses end cell cell open parentheses 5 cross times negative 5 space plus space minus 5 cross times 2 close parentheses end cell row cell open parentheses 4 cross times 5 space plus space 2 cross times 4 close parentheses end cell cell open parentheses 4 cross times negative 5 space plus space 2 cross times 2 close parentheses end cell end table close parentheses equals open parentheses table row cell open parentheses 25 space plus space minus 20 close parentheses end cell cell open parentheses negative 25 space plus space minus 10 close parentheses end cell row cell open parentheses 20 space plus space 8 close parentheses end cell cell open parentheses negative 20 space plus space 4 close parentheses end cell end table close parentheses`
> 
> > *Simplify*
> 
> `Error converting from MathML to accessible text.`

> **Worked Example**
> If `bold A equals open parentheses table row 0 2 row 2 0 end table close parentheses` show that $A^{2}=4I$.
> 
> **Answer:**
> 
> > *Write out *$A^{2}$* as *$A\timesA$
> 
> `open parentheses table row 0 2 row 2 0 end table close parentheses cross times open parentheses table row 0 2 row 2 0 end table close parentheses`
> 
> > *Multiply the matrices*
> 
> `open parentheses table row 0 2 row 2 0 end table close parentheses cross times open parentheses table row 0 2 row 2 0 end table close parentheses equals open parentheses table row cell open parentheses 0 cross times 0 space plus space 2 cross times 2 close parentheses end cell cell open parentheses 0 cross times 2 space plus space 2 cross times 0 close parentheses end cell row cell open parentheses 2 cross times 0 space plus space 0 cross times 2 close parentheses end cell cell open parentheses 2 cross times 2 space plus space 0 cross times 0 close parentheses end cell end table close parentheses`
> 
> `equals open parentheses table row 4 0 row 0 4 end table close parentheses`
> 
> > *Write in terms of the identity matrix,  *`bold I equals open parentheses table row 1 0 row 0 1 end table close parentheses`* by factoring out 4*
> 
> `stretchy left parenthesis table row 4 0 row 0 4 end table stretchy right parenthesis equals 4 stretchy left parenthesis table row 1 0 row 0 1 end table stretchy right parenthesis equals 4 bold I`
