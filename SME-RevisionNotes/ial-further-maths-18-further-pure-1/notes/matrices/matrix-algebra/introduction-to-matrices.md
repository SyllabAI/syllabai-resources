---
note_id: "rn_wSCqmqgVJsDYbCc8"
title: "Introduction to Matrices"
source: https://www.savemyexams.com/international-a-level/further-maths/edexcel/18/further-pure-1/revision-notes/matrices/matrix-algebra/introduction-to-matrices
path: matrices/matrix-algebra/introduction-to-matrices
updated_at: "2024-04-10T09:27:00.609Z"
spec_point_ids: ["spcpt_CRFsjrVKdnBVB9Qg", "spcpt_JDWV8bD7tNcdGzCF"]
spec_point_codes: []
guided_study: false
---

# Introduction to Matrices

## Introduction to Matrices

> **Spec point** — `spcpt_CRFsjrVKdnBVB9Qg`

## Introduction to Matrices

### What is a matrix?

- A **matrix** is a rectangular grid (array) of **elements** (numbers or letters) arranged in **rows** and **columns**

  - The plural of matrix is **matrices**
- The **order **(**dimensions**)** **of a matrix is its **number of rows × number of columns**

  - a 2 × 1 matrix is `open parentheses table row a row b end table close parentheses`
  
    - this is also called a **column matrix** or a **column** **vector**
  - a 2 × 2 matrix is `open parentheses table row a b row c d end table close parentheses`
  
    - this is called a **square **matrix
- A **bold capital **letter is often used to represent a matrix

  - `bold A equals open parentheses table row 5 2 row 0 4 end table close parentheses`, `bold B equals open parentheses table row 4 row 3 end table close parentheses`
- **2D coordinates **can be written as a column matrix

  - The point `open parentheses 3 comma space 5 close parentheses` is `open parentheses table row 3 row 5 end table close parentheses`

- You can use **subscript **notation to refer to **elements** in a matrix

  - Matrix $A$ is $A=(a_{i,j})$ where $i=1,2,3,...,m$ and $j=1,2,3,...,n$
  
    - $a_{i,j}$ refers to the element in row $i$, column $j$
    - The **order** of $A$ is $m\timesn$ (rows × columns)

![A matrix written in subscript notation](../../../assets/4a5122f5fe39-u0splroy-1-7-1-ib-ai-hl-introduction-to-matrices.png)

### What type of matrices do I need to know?

- A **column matrix** (or column vector) is a matrix with a **single column**

  - Order $m\times1$
- A **row matrix** is a matrix with a **single row**

  - Order $1\timesn$
- A **square matrix** is one in which the number of rows is **equal** to the number of columns

  - Order $n\timesn$
- Two matrices are **equal** when they are of the **same order** and their **corresponding elements **are **equal**

  - $a_{i,j}=b_{i,j}$ for all elements
- A **zero matrix**,** **$0$, is a matrix in which all the elements are zero

  - For example, the 2 × 2 zero matrix is `bold 0 equals open parentheses table row 0 0 row 0 0 end table close parentheses`
- An** identity matrix**, $I$, is a **square** matrix in which all elements along the **leading diagonal** (top-left to bottom right) are 1

  - The rest of the elements are zero
  - For example, the 2 × 2 identity matrix is  `bold I equals open parentheses table row 1 0 row 0 1 end table close parentheses`
  - The notation $I_{n}$ can be used to specify the $n\timesn$ identity matrix

## Basic Operations with Matrices

> **Spec point** — `spcpt_JDWV8bD7tNcdGzCF`

## Basic Operations with Matrices

### How do I multiply a matrix by a scalar?

- To multiply any matrix by a **scalar** (a number), **multiply each element **by that scalar

  - If `bold A equals open parentheses table row 5 2 row 0 4 end table close parentheses` then `2 bold A equals 2 open parentheses table row 5 2 row 0 4 end table close parentheses equals open parentheses table row cell 2 cross times 5 end cell cell 2 cross times 2 end cell row cell 2 cross times 0 end cell cell 2 cross times 4 end cell end table close parentheses equals open parentheses table row 10 4 row 0 8 end table close parentheses`
- Multiplying by a **negative** scalar changes the **sign** of each element in the matrix
- **Lower case** letters often refer to scalar multiples

  - $kA$ is the matrix $A$ multiplied by the scalar $k$

### How do I add and subtract matrices?

- Two matrices of the **same order** can be added (or subtracted) by adding (or subtracting) **corresponding elements**

  - The answer is a matrix of the **same order**
  - For example, `open parentheses table row 1 2 row cell negative 3 end cell 0 row 2 1 end table close parentheses plus open parentheses table row 3 0 row 3 cell negative 1 end cell row 4 1 end table close parentheses equals open parentheses table row cell 1 plus 3 end cell cell 2 plus 0 end cell row cell negative 3 plus 3 end cell cell 0 minus 1 end cell row cell 2 plus 4 end cell cell 1 plus 1 end cell end table close parentheses equals open parentheses table row 4 2 row 0 cell negative 1 end cell row 6 2 end table close parentheses`

### What properties of matrix addition do I need to know?

- $A+B=B+A$

  - Matrix **addition** is **commutative**
  
    - You can swap the order
  - Matrix **subtraction** is **not** commutative
  
    - $A-B\neqB-A$
- $A-B=A+(-B)$

  - **Subtraction** is the same as **adding **a **negative**
- $A+(B+C)=(A+B)+C$

  - Matrix **addition** is **associative **
  
    - To add three matrices, you can start with the first two, or the last two
  - Matrix **subtraction** is **not **associative
  
    - $A-(B-C)\neq(A-B)-C$
    - Try expanding the brackets to see
- $A+0=A$

  - Adding the** zero **matrix has no effect
- $0-A=-A$

> **Worked Example**
> Consider the matrices `bold A equals open parentheses table row cell negative 4 end cell 2 row 7 3 row 1 cell negative 5 end cell end table close parentheses`, `bold B equals open parentheses table row 2 6 row 5 cell negative 9 end cell row cell negative 2 end cell cell negative 3 end cell end table close parentheses`.
> 
> (a)  Find $A+B$.
> 
> > *The matrices have the same order (dimensions) *
> *Corresponding elements can be added*
> 
> `bold A plus bold B equals open parentheses table row cell negative 4 plus 2 end cell cell 2 plus 6 end cell row cell 7 plus 5 end cell cell 3 plus open parentheses negative 9 close parentheses end cell row cell 1 plus open parentheses negative 2 close parentheses end cell cell negative 5 plus open parentheses negative 3 close parentheses end cell end table close parentheses`
> 
> `bold A plus bold B equals open parentheses table row cell negative 2 end cell 8 row 12 cell negative 6 end cell row cell negative 1 end cell cell negative 8 end cell end table close parentheses`
> 
> (b)  Find $-10B$.
> 
> > *Multiply each element by -10*
> 
> * *`table row cell negative 10 bold B end cell equals cell negative 10 open parentheses table row 2 6 row 5 cell negative 9 end cell row cell negative 2 end cell cell negative 3 end cell end table close parentheses end cell row blank equals cell open parentheses table row cell negative 10 cross times 2 end cell cell negative 10 cross times 6 end cell row cell negative 10 cross times 5 end cell cell negative 10 cross times open parentheses negative 9 close parentheses end cell row cell negative 10 cross times open parentheses negative 2 close parentheses end cell cell negative 10 cross times open parentheses negative 3 close parentheses end cell end table close parentheses end cell end table`
> 
> `table row cell negative 10 bold B end cell equals cell open parentheses table row cell negative 20 end cell cell negative 60 end cell row cell negative 50 end cell 90 row 20 30 end table close parentheses end cell end table`
