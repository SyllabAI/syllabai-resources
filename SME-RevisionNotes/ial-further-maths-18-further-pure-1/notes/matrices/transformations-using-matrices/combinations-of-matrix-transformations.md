---
note_id: "rn_QgchJ42HYg9HdZ2Z"
title: "Combinations of Matrix Transformations"
source: https://www.savemyexams.com/international-a-level/further-maths/edexcel/18/further-pure-1/revision-notes/matrices/transformations-using-matrices/combinations-of-matrix-transformations
path: matrices/transformations-using-matrices/combinations-of-matrix-transformations
updated_at: "2024-04-10T13:34:45.939Z"
spec_point_ids: ["spcpt_kZwP597VC4kn3npw"]
spec_point_codes: []
guided_study: false
---

# Combinations of Matrix Transformations

## Combinations of Matrix Transformations

> **Spec point** — `spcpt_kZwP597VC4kn3npw`

## Combinations of Matrix Transformations

### How do I find a single matrix that represents a combination of transformations?

- A point `open parentheses x comma space y close parentheses` can be transformed **twice**

  - **Firstly** by the matrix $P$, then** secondly** by the matrix $Q$
  - This is called a **combined** (or **composite** or **successive**) transformation
- A** single **matrix, $M$, representing the combined transformation can be found using **matrix multiplication** as follows:

  - $M=\mathrm{QP}$** **
  
    - The **order** matters: the **first** transformation is on the **right** in the multiplication
    - This order is the **reverse** of what you might expect!
  - Be careful: $\mathrm{PQ}$  represents** **$Q$ first, followed by $P$ second

### How do I find the inverse of a combined transformation?

- The inverse of a **product** of matrices is the product of the inverses of the matrices in **reverse order**

  - `open parentheses bold AB close parentheses to the power of negative 1 end exponent equals bold B to the power of negative 1 end exponent bold A to the power of negative 1 end exponent`
- Let $M$ represent the transformation **first** by $P$, then** second** by $Q$

  - That means$M=\mathrm{QP}$ from above
- Algebraically, `bold M to the power of negative 1 end exponent equals open parentheses bold QP close parentheses to the power of negative 1 end exponent` which gives $M^{-1}=P^{-1}Q^{-1}$

  - This shows that the **inverse**, $M^{-1}$**,**  first reverses $Q$** **, then reverses $P$
  
    - That is the order we would expect

> **Worked Example**
> Three transformations in the $x$-$y$ plane are represented by the matrices below.
> 
> `bold A equals open parentheses table row cell negative 1 end cell 0 row 0 cell negative 1 end cell end table close parentheses`**  **represents a rotation of 180° about the origin
> `bold B equals open parentheses table row cell negative 1 end cell 0 row 0 1 end table close parentheses`** **represents a reflection in the *y*-axis
> `bold C equals open parentheses table row 1 0 row 0 cell negative 1 end cell end table close parentheses`** **represents a reflection in the *x*-axis
> 
> (a)  Use matrix multiplication to prove that a reflection in the* y*-axis followed by a reflection in the *x*-axis is equivalent to a rotation of 180° about the origin.
> 
> > *The question requires transformation *$B$* followed by transformation *$C$
> *This is the same as the matrix *$\mathrm{CB}$* in that order (the first transformation appears on the right)*
> 
> $\mathrm{CB}$
> 
> > *Use matrix multiplication to find *$\mathrm{CB}$
> 
> `bold CB space equals space open parentheses table row 1 0 row 0 cell negative 1 end cell end table close parentheses cross times open parentheses table row cell negative 1 end cell 0 row 0 1 end table close parentheses equals open parentheses table row cell open parentheses 1 cross times negative 1 space plus space 0 cross times 0 close parentheses end cell cell open parentheses 1 cross times 0 space plus space 0 cross times 1 close parentheses end cell row cell open parentheses 0 cross times negative 1 space plus space minus 1 cross times 0 close parentheses end cell cell open parentheses 0 cross times 0 space plus space minus 1 cross times 1 close parentheses end cell end table close parentheses`
> 
> > *The question claims that this is equivalent to transformation  *$A$
> *Simplify the working above and show that it is the same as matrix *$A$
> 
> **Final answer:** `bold CB equals stretchy left parenthesis table row cell negative 1 end cell 0 row 0 cell negative 1 end cell end table stretchy right parenthesis equals bold A`
> **Therefore a reflection in the**** y****-axis followed by a reflection in the ****x****-axis is equivalent to a rotation of 180° about the origin**
> 
> **You would not get the marks for multiplying BC (it must be CB)**
> 
> (b)  A different transformation is represented by $\mathrm{CD}$ where `bold D to the power of negative 1 end exponent equals open parentheses table row 2 0 row 0 1 end table close parentheses`.
> 
> Find and simplify the matrix representing the inverse of the transformation.
> 
> > *Y**ou need to find the inverse of *$\mathrm{CD}$
> *You need the rule that *`open parentheses bold CD close parentheses to the power of negative 1 end exponent equals bold D to the power of negative 1 end exponent bold C to the power of negative 1 end exponent`
> *You can substitute in *$D^{-1}$* from the question*
> 
> `table row cell open parentheses bold CD close parentheses to the power of negative 1 end exponent end cell equals cell bold D to the power of negative 1 end exponent bold C to the power of negative 1 end exponent end cell row blank equals cell open parentheses table row 2 0 row 0 1 end table close parentheses bold C to the power of negative 1 end exponent end cell end table`
> 
> > *You need to find *$C^{-1}$
> *Use that *`bold M equals open parentheses table row a b row c d end table close parentheses space space rightwards double arrow space space bold M to the power of bold minus bold 1 end exponent equals fraction numerator 1 over denominator det space bold M end fraction open parentheses table row d cell negative b end cell row cell negative c end cell a end table close parentheses`* where *$\mathrm{det}M=ad-bc$
> 
> `table row cell bold C to the power of negative 1 end exponent end cell equals cell fraction numerator 1 over denominator 1 cross times open parentheses negative 1 close parentheses minus 0 cross times 0 end fraction open parentheses table row cell negative 1 end cell 0 row 0 1 end table close parentheses end cell row blank equals cell open parentheses table row 1 0 row 0 cell negative 1 end cell end table close parentheses end cell end table`
> 
> > *(Note that a reflection in the **x-**axis is its own inverse!)*
> *Substitute this into the working above and multiply the matrices*
> 
> `table row cell open parentheses bold CD close parentheses to the power of negative 1 end exponent end cell equals cell open parentheses table row 2 0 row 0 1 end table close parentheses open parentheses table row 1 0 row 0 cell negative 1 end cell end table close parentheses end cell row blank equals cell open parentheses table row 2 0 row 0 cell negative 1 end cell end table close parentheses end cell end table`
> 
> `table row blank blank cell open parentheses table row 2 0 row 0 cell negative 1 end cell end table close parentheses end cell end table`
> 
> **There are other ways to do this question, for example finding **$D$** first**
> **If you saw that **$C^{-1}=C$** (as it is a reflection in the ****x****-axis), explain why clearly**
