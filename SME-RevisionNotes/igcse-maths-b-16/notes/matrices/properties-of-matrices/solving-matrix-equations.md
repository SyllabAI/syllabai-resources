---
note_id: "rn_7HCGBNPXM8Mnj2t7"
title: "Solving Matrix Equations"
source: https://www.savemyexams.com/igcse/maths/edexcel/b/16/revision-notes/matrices/properties-of-matrices/solving-matrix-equations
path: matrices/properties-of-matrices/solving-matrix-equations
updated_at: "2026-01-14T11:42:53.189Z"
spec_point_ids: ["spcpt_JGrDCdnmTzs2Z9Cb"]
spec_point_codes: []
guided_study: false
---

# Solving Matrix Equations

## Solving matrix equations with inverses

> **Spec point** — `spcpt_JGrDCdnmTzs2Z9Cb`

## Solving matrix equations with inverses

- Inverses can be used to **rearrange** and **solve** equations with matrices
- This relies on the essential properties of inverses and of the identity matrix:

  - $\mathrm{AA}^{-1}=A^{-1}A=I$
  - $\mathrm{AI}=\mathrm{IA}=A$
- For example, to solve the matrix equation $\mathrm{AB}=C$** **for $B$

  - First multiply both sides of the equation 'from the left' by $A^{-1}$
  
    - $A^{-1}\mathrm{AB}=A^{-1}C$
  - But $A^{-1}A=I$, so
  
    - $\mathrm{IB}=A^{-1}C$
  - And $\mathrm{IB}=B$, so
  
    - $B=A^{-1}C$
  - Then multiply together the two matrices on the right-hand side to find $B$ explicitly
- Similarly, you can solve the matrix equation $\mathrm{BA}=C$** **for $B$

  - Though here you will need to multiply 'from the right' by $A^{-1}$

`table row cell bold BAA to the power of negative 1 end exponent end cell equals cell bold CA to the power of negative 1 end exponent end cell row bold BI equals cell bold CA to the power of negative 1 end exponent end cell row bold B equals cell bold CA to the power of negative 1 end exponent end cell end table`

- This is similar to solving a regular equation by 'doing the same thing to both sides'

  - Except that **order of multiplication** matters with matrices
  
    - Multiplying 'from the left' is **not** the same as multiplying 'from the right'
  - For example, if you tried to solve $\mathrm{BA}=C$** **for $B$ by multiplying 'from the left' by $A^{-1}$
  
    - you would get $A^{-1}\mathrm{BA}=A^{-1}C$
    - which does not simplify any further

> **Exam Hint**
> Remember that a matrix and its inverse only 'collapse' to the identity matrix $I$ when they are next to each other in a multiplication.
> 
> - So $A^{-1}\mathrm{AB}=\mathrm{IB}=B$
> - and $\mathrm{BAA}^{-1}=\mathrm{BI}=B$
> - but $A^{-1}\mathrm{BA}$ does not simplify any further

> **Worked Example**
> `bold P equals open parentheses table row 4 cell negative 2 end cell row cell negative 2 end cell 2 end table close parentheses space space space space space space space bold Q equals open parentheses table row k 1 row 3 0 end table close parentheses space space space space space space space bold R equals open parentheses table row 10 4 row cell negative 2 end cell cell negative 2 end cell end table close parentheses`
> 
> where $k$ is a constant.
> 
> (a) Find $P^{-1}$.
> 
> **Answer:**
> 
> > *Use the inverse formula for a *$2\times2$* matrix*
> 
> - *The inverse of *`space open parentheses table row a b row c d end table close parentheses space`* is *`space fraction numerator 1 over denominator a d minus b c end fraction open parentheses table row d cell negative b end cell row cell negative c end cell a end table close parentheses`
> 
> `table row cell bold P to the power of bold minus bold 1 end exponent end cell equals cell fraction numerator 1 over denominator 4 cross times 2 minus open parentheses negative 2 close parentheses cross times open parentheses negative 2 close parentheses end fraction open parentheses table row 2 2 row 2 4 end table close parentheses end cell row blank equals cell fraction numerator 1 over denominator 8 minus 4 end fraction open parentheses table row 2 2 row 2 4 end table close parentheses end cell row blank equals cell 1 fourth open parentheses table row 2 2 row 2 4 end table close parentheses end cell row blank equals cell open parentheses table row cell 1 fourth cross times 2 end cell cell 1 fourth cross times 2 end cell row cell 1 fourth cross times 2 end cell cell 1 fourth cross times 4 end cell end table close parentheses end cell row blank equals cell open parentheses table row cell 1 half end cell cell 1 half end cell row cell 1 half end cell 1 end table close parentheses end cell end table`
> 
> `table row cell bold P to the power of bold minus bold 1 end exponent end cell equals cell open parentheses table row cell 1 half end cell cell 1 half end cell row cell 1 half end cell 1 end table close parentheses end cell end table`
> 
> (b) Given that $\mathrm{PQ}=R$ find the value of $k$.
> 
> **Answer:**
> 
> > *Use matrix algebra to solve the equation for *$Q$
> 
> - *Multiply both sides of the equation 'from the left' by *$P^{-1}$
> 
> $P^{-1}\mathrm{PQ}=P^{-1}R$
> 
> - *By the definition of the inverse, *$P^{-1}P=I$
> 
> $\mathrm{IQ}=P^{-1}R$
> 
> - *By the properties of the identity matrix, *$\mathrm{IQ}=Q$
> 
> $Q=P^{-1}R$
> 
> > *That gives you a matrix 'formula' for *$Q$
> 
> - *Substitute in matrices *$P^{-1}$* and *$R$
> 
> `bold Q equals open parentheses table row cell 1 half end cell cell 1 half end cell row cell 1 half end cell 1 end table close parentheses open parentheses table row 10 4 row cell negative 2 end cell cell negative 2 end cell end table close parentheses`
> 
> - *Carry out the multiplication*
> 
> `table row bold Q equals cell open parentheses table row cell 1 half cross times 10 plus 1 half cross times open parentheses negative 2 close parentheses end cell cell 1 half cross times 4 plus 1 half cross times open parentheses negative 2 close parentheses end cell row cell 1 half cross times 10 plus 1 cross times open parentheses negative 2 close parentheses end cell cell 1 half cross times 4 plus 1 cross times negative 2 end cell end table close parentheses end cell row blank equals cell open parentheses table row cell 5 minus 1 end cell cell 2 minus 1 end cell row cell 5 minus 2 end cell cell 2 minus 2 end cell end table close parentheses end cell row blank equals cell open parentheses table row 4 1 row 3 0 end table close parentheses end cell end table`
> 
> $k=4$
