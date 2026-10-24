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

  - a 2 × 1 matrix is $( \begin{gathered} a \\ b \end{gathered} )$
  
    - this is also called a **column matrix** or a **column** **vector**
  - a 2 × 2 matrix is $( \begin{gathered} a b \\ c d \end{gathered} )$
  
    - this is called a **square **matrix
- A **bold capital **letter is often used to represent a matrix

  - $A = ( \begin{gathered} 5 2 \\ 0 4 \end{gathered} )$, $B = ( \begin{gathered} 4 \\ 3 \end{gathered} )$
- **2D coordinates **can be written as a column matrix

  - The point $( 3 , 5 )$ is $( \begin{gathered} 3 \\ 5 \end{gathered} )$

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

  - For example, the 2 × 2 zero matrix is $0 = ( \begin{gathered} 0 0 \\ 0 0 \end{gathered} )$
- An** identity matrix**, $I$, is a **square** matrix in which all elements along the **leading diagonal** (top-left to bottom right) are 1

  - The rest of the elements are zero
  - For example, the 2 × 2 identity matrix is  $I = ( \begin{gathered} 1 0 \\ 0 1 \end{gathered} )$
  - The notation $I_{n}$ can be used to specify the $n\timesn$ identity matrix

## Basic Operations with Matrices

> **Spec point** — `spcpt_JDWV8bD7tNcdGzCF`

## Basic Operations with Matrices

### How do I multiply a matrix by a scalar?

- To multiply any matrix by a **scalar** (a number), **multiply each element **by that scalar

  - If $A = ( \begin{gathered} 5 2 \\ 0 4 \end{gathered} )$ then $2 A = 2 ( \begin{gathered} 5 2 \\ 0 4 \end{gathered} ) = ( \begin{gathered} 2 \times 5 & 2 \times 2 \\ 2 \times 0 & 2 \times 4 \end{gathered} ) = ( \begin{gathered} 10 4 \\ 0 8 \end{gathered} )$
- Multiplying by a **negative** scalar changes the **sign** of each element in the matrix
- **Lower case** letters often refer to scalar multiples

  - $kA$ is the matrix $A$ multiplied by the scalar $k$

### How do I add and subtract matrices?

- Two matrices of the **same order** can be added (or subtracted) by adding (or subtracting) **corresponding elements**

  - The answer is a matrix of the **same order**
  - For example, $( \begin{gathered} 1 2 \\ - 3 & 0 \\ 2 1 \end{gathered} ) + ( \begin{gathered} 3 0 \\ 3 - 1 \\ 4 1 \end{gathered} ) = ( \begin{gathered} 1 + 3 & 2 + 0 \\ - 3 + 3 & 0 - 1 \\ 2 + 4 & 1 + 1 \end{gathered} ) = ( \begin{gathered} 4 2 \\ 0 - 1 \\ 6 2 \end{gathered} )$

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
> Consider the matrices $A = ( \begin{gathered} - 4 & 2 \\ 7 3 \\ 1 - 5 \end{gathered} )$, $B = ( \begin{gathered} 2 6 \\ 5 - 9 \\ - 2 & - 3 \end{gathered} )$.
> 
> (a)  Find $A+B$.
> 
> > *The matrices have the same order (dimensions) *
> *Corresponding elements can be added*
> 
> $A + B = ( \begin{gathered} - 4 + 2 & 2 + 6 \\ 7 + 5 & 3 + ( - 9 ) \\ 1 + ( - 2 ) & - 5 + ( - 3 ) \end{gathered} )$
> 
> $A + B = ( \begin{gathered} - 2 & 8 \\ 12 - 6 \\ - 1 & - 8 \end{gathered} )$
> 
> (b)  Find $-10B$.
> 
> > *Multiply each element by -10*
> 
> * *$\begin{gathered} - 10 B & = - 10 ( \begin{gathered} 2 6 \\ 5 - 9 \\ - 2 & - 3 \end{gathered} ) \\ = ( \begin{gathered} - 10 \times 2 & - 10 \times 6 \\ - 10 \times 5 & - 10 \times ( - 9 ) \\ - 10 \times ( - 2 ) & - 10 \times ( - 3 ) \end{gathered} ) \end{gathered}$
> 
> $\begin{gathered} - 10 B & = ( \begin{gathered} - 20 & - 60 \\ - 50 & 90 \\ 20 30 \end{gathered} ) \end{gathered}$
