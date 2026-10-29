---
note_id: "rn_GKTrTFNBqN7R4CMF"
title: "Solving Equations with Complex Roots"
source: https://www.savemyexams.com/international-a-level/further-maths/edexcel/18/further-pure-1/revision-notes/complex-numbers/solving-equations-with-complex-roots/solving-equations-with-complex-roots
path: complex-numbers/solving-equations-with-complex-roots/solving-equations-with-complex-roots
updated_at: "2024-04-05T07:57:52.496Z"
spec_point_ids: ["spcpt_zsSv929BKZ5RjrwZ", "spcpt_Vj2kxp9s4PfSKScf"]
spec_point_codes: []
guided_study: false
---

# Solving Equations with Complex Roots

## Quadratics with Complex Roots

> **Spec point** — `spcpt_zsSv929BKZ5RjrwZ`

## Quadratics with Complex Roots

### How do I solve a quadratic with complex roots?

- **Quadratic equations **with **complex roots** can still be solved using the **quadratic formula **or by **completing the square**

  - They have the **form** $az^{2}+bz+c=0$ where $a$, $b$ and $c$ are **real** numbers
  - For **complex roots**, the** discriminant** is **negative**
  
    - $b^{2}-4ac<0$
  - You must therefore rewrite the **square root** using $i$
  
    - $\sqrt{-16}=4i$,  $\sqrt{-2}=i\sqrt{2}$,  ... and so on
- The** two roots**, $z_{1}$ and $z_{2}$ are **complex conjugates** of each other

  - (provided $a$, $b$ and $c$ from the equation are all **real **numbers)
  - So $z_{1}=x+iy$ and $z_{2}=x-iy$
  
    - $z_{2}=z_{1}\ast$

> **Exam Hint**
> Complex conjugate roots is a key concept that is used in many exam questions.

### How do I solve a quadratic with one known  complex root?

- If you **know **one complex root, the **other** will be its **complex** **conjugate**

  - If $z_{1}=4+5i$ is a root to $z^{2}-8z+41=0$
  
    - then $z_{2}=4-5i$ must be the **other **root
    - No solving is required!

### How do I find a quadratic from its complex root?

- If you are **given** one **complex **root, $z_{1}$, the **other **root** **is its **complex conjugate**, $z_{1}\ast$
- You can then write its** quadratic equation** in **factorised form**

  - $( z - z_{1} ) ( z - z_{1} \text{asterisk} \times ) = 0$
  - **Expand **this to give the equation in **expanded form**  $az^{2}+bz+c=0$
  
    - Any **multiple** of this equation also works
- A good** trick **when expanding is to **group** the **first two terms** in each bracket

  - So $( \mathrm{z} - ( 2 + 3 \mathrm{i} ) ) ( \mathrm{z} - ( 2 - 3 \mathrm{i} ) )$ becomes $( ( z - 2 ) - 3 \mathrm{i} ) ( ( z - 2 ) + 3 \mathrm{i} )$
  - Then use the **difference of two squares**
  
    - $( z - 2 )^{2} - ( 3 \mathrm{i} )^{2} \equiv ( z - 2 )^{2} + 9 \equiv z^{2} - 4 z + 4 + 9$
  - The equation is therefore $z^{2}-4z+13=0$

> **Exam Hint**
> Always check how the question wants the answer, for example asking for integer coefficients.

> **Worked Example**
> (a)  Solve $z^{2}-2z+37=0$.
> 
> > *Use the quadratic formula with* $a=1$*,* $b=-2$ *and* $c=37$
> *Find the discriminant* $b^{2}-4ac$
> 
> $\begin{gathered} b^{2} - 4 a c & = ( - 2 )^{2} - 4 \times 1 \times 37 \\ = 4 - 148 \\ = - 144 \end{gathered}$
> 
> > *Substitute these values into the quadratic formula* $\frac{-b\pm\sqrt{b^{2}-4ac}}{2a}$
> 
> $\begin{gathered} z = \frac{- ( - 2 ) \pm \sqrt{- 144} }{2 \times 1} \\ = \frac{2 \pm \sqrt{- 144} }{2} \end{gathered}$
> 
> > *Use that* $\sqrt{-144}=\sqrt{144i^{2}}=12i$
> 
> $z=\frac{2\pm12i}{2}$
> 
> > *Simplify the answers*
> *Check that they are complex conjugates of each other*
> 
> $z=1\pm6i$
> 
> (b)  If $-\frac{1}{2}+\frac{3i}{2}$ is one root of the equation $az^{2}+bz+c=0$ where $a$, $b$ and $c$ are positive integers, find $a$, $b$ and $c$ .
> 
> > *Write down the other root (the complex conjugate)*
> 
> $-\frac{1}{2}-\frac{3i}{2}$
> 
> > *Write down the quadratic equation in factorised form,* $( z - z_{1} ) ( z - z_{1} \text{asterisk} \times ) = 0$
> 
> $( z - ( - 1 \frac{1}{2} + \frac{3 \mathrm{i} }{2} ) ) ( z - ( - 1 \frac{1}{2} - \frac{3 \mathrm{i} }{2} ) ) = 0$
> 
> > *Expand inside each bracket*
> 
> $( z + 1 \frac{1}{2} - \frac{3 \mathrm{i} }{2} ) ( z + 1 \frac{1}{2} + \frac{3 \mathrm{i} }{2} ) = 0$
> 
> > *Group the first two terms in each bracket*
> 
> $( ( z + 1 \frac{1}{2} ) - \frac{3 \mathrm{i} }{2} ) ( ( z + 1 \frac{1}{2} ) + \frac{3 \mathrm{i} }{2} ) = 0$
> 
> > *Use the difference of two squares to expand*
> 
> $( z + 1 \frac{1}{2} )^{2} - ( \frac{3 \mathrm{i} }{2} )^{2} = 0$
> 
> > *Expand and collect, using* $i^{2}=-1$
> 
> $\begin{gathered} z^{2} + z + 1 \frac{1}{4} + \frac{9}{4} & = 0 \\ z^{2} + z + \frac{5}{2} & = 0 \end{gathered}$
> 
> > *The question wants the final answer to have positive integer coefficients*
> *Multiply both sides of the equation by 2*
> 
> $2z^{2}+2z+5=0$
> 
> > *Write down the values of* $a$*,* $b$ *and* $c$
> 
> **Final answer:** $a=2$**, **$b=2$** and **$c=5$
> 
> **Positive integer multiples of these answers are also accepted**

## Cubics & Quartics with Complex Roots

> **Spec point** — `spcpt_Vj2kxp9s4PfSKScf`

## Cubics & Quartics with Complex Roots

### How do I solve a cubic with complex roots?

- **Cubic equations** have either

  - **3 real **roots
  - or **1 real** root and one **complex conjugate pair** of roots
- Solve $az^{3}+bz^{2}+cz+d=0$, given that $m+ni$ is a root

  - Another root is** **$m-ni$
  
    - Its complex conjugate
  - So $( z - ( m + n \mathrm{i} ) )$ and $(z-(m-ni))$ are **factors**
  - **Multiply** the factors together to get a **quadratic factor **
  
    - $(Az^{2}+Bz+C)$
  - You need to find the remaining **linear** factor $(Pz+Q)$
  - Either use **equating coefficients** to find $α$
  
    - $( A z^{2} + B z + C ) ( P z + Q ) \equiv a x^{3} + b x^{2} + c x + d$
    - Expand** **and simplify the left-hand side
    - Match each coefficient with the right-hand side
  - Or use **polynomial division** to find $( P z + Q )$
  
    - $( a z^{3} + b z^{2} + c z + d ) \div ( A z^{2} + B z + C )$
  - Write out your **three roots** clearly

### How do I solve a quartic with complex roots?

- **Quartic equations** have either

  - **4 real **roots
  - or **2 real** roots and **1 pair** of **complex conjugate **roots
  - or **2 pairs** of **complex conjugate **roots
- Solve $az^{4}+bz^{3}+cz^{2}+dz+e=0$, given that $m+ni$ is a root

  - Another root is** **$m-ni$
  
    - Its complex conjugate
  - So $( z - ( m + n \mathrm{i} ) )$ and $(z-(m-ni))$ are **factors**
  - **Multiply** the factors together to get a **quadratic factor **
  
    - $(Az^{2}+Bz+C)$
  - You need to find the remaining **quadratic **factor $( P z^{2} + Q z + R )$
  - Either use **equating coefficients** to find $P$, $Q$ and $R$
  
    - $( A z^{2} + B z + C ) ( P z^{2} + Q z + R ) \equiv a z^{4} + b z^{3} + c z^{2} + d z + e$
    - Expand** **and simplify the left-hand side
    - Match each coefficient with the right-hand side
  - Or use **polynomial division** to find $( P z^{2} + Q z + R )$
  
    - $( a z^{4} + b z^{3} + c z^{2} + d z + e ) \div ( A z^{2} + B z + C )$
  - Solve $Pz^{2}+Qz+R=0$
  - Write out your **four roots** clearly

### How do I find unknown coefficients of equations?

- Find as many **factors** as possible from **given** roots

  - **Real **roots give **linear** factors
  
    - $z=α$ gives $( z - \\alpha )$
  - **Complex **roots give **quadratic** factors (from **conjugate** pairs)
  - $z=m+ni$ gives $( z - ( m + n \mathrm{i} ) ) ( z - ( m - n \mathrm{i} ) ) \equiv A z^{2} + B z + C$
- Then write out the rest **algebraically **and use **equating coefficients**

  - Start by matching coefficients of the **highest powers** and of the **constants**
  
    - These can often been seen** *****by inspection***

> **Exam Hint**
> Whilst polynomial division can be used instead of equating coefficients, it is not recommended when exam questions have algebraic coefficients!

> **Worked Example**
> (a)  Given that $-4+2i$ is a root of the equation $z^{3}+5z^{2}-4z-60=0$, find the other two roots.
> 
> > *Write down the other complex root by finding the complex conjugate*
> 
> $-4-2i$
> 
> > *Write down a factorised quadratic factor of the cubic*
> *Use the form* $( z - ( - 4 + 2 \mathrm{i} ) ) ( z - ( - 4 - 2 \mathrm{i} ) )$
> 
> $( z - ( - 4 + 2 \mathrm{i} ) ) ( z - ( - 4 - 2 \mathrm{i} ) )$
> 
> > *Expand inside each bracket*
> 
> $= ( z + 4 - 2 \mathrm{i} ) ( z + 4 + 2 \mathrm{i} )$
> 
> > *Group the first pair of terms in each bracket*
> *Then expand using the difference between two squares*
> *Simplify the quadratic factor*
> 
> $\begin{gathered} = ( ( z + 4 ) - 2 \mathrm{i} ) ( ( z + 4 ) + 2 \mathrm{i} ) \\ = ( z + 4 )^{2} - ( 2 \mathrm{i} )^{2} \\ = z^{2} + 8 z + 16 + 4 \\ = z^{2} + 8 z + 20 \end{gathered}$
> 
> > *Write the cubic as the quadratic factor multiplied by a linear factor* $Pz+Q$
> 
> $z^{3} + 5 z^{2} - 4 z - 60 \equiv ( z^{2} + 8 z + 20 ) ( P z + Q )$
> 
> > *Either expand the right-hand side and equate coefficients*
> *Or see that* $P=1$ *to get* $z^{3}$ *on the left, and* $Q=-3$ *to get* $-60$ *on the left*
> 
> $z^{3} + 5 z^{2} - 4 z - 60 \equiv ( z^{2} + 8 z + 20 ) ( z - 3 )$
> 
> > $z^{3}+5z^{2}-4z-60=0$ *so set the factorised cubic equal to zero*
> 
> $( z^{2} + 8 z + 20 ) ( z - 3 ) = 0$
> 
> > *The solutions from the quadratic factor are the complex conjugates*
> *The solution from* $( z - 3 ) = 0$ *is* $z=3$
> *Write down all three solutions*
> 
> **Final answer:** $z=-4+2i$**, **$-4-2i$** or **$3$
> 
> (b)  It is known that the equation $z^{4}-8z^{3}+Az^{2}+Bz+90$ has a complex root $1+3i$ and a repeated real root. Find $A$ and $B$.
> 
> > *Write down the other complex root by finding the complex conjugate*
> 
> $1-3i$
> 
> > *Write down a factorised quadratic factor of the quartic*
> *Use the form* $( z - ( 1 + 3 \mathrm{i} ) ) ( z - ( 1 - 3 \mathrm{i} ) )$
> 
> $( z - ( 1 + 3 \mathrm{i} ) ) ( z - ( 1 - 3 \mathrm{i} ) )$
> 
> > *Expand inside each bracket*
> 
> $= ( z - 1 - 3 \mathrm{i} ) ( z - 1 + 3 \mathrm{i} )$
> 
> > *Group the first pair of terms in each bracket*
> *Then expand using the difference between two squares*
> *Simplify the quadratic factor*
> 
> $\begin{gathered} = ( ( z - 1 ) - 3 \mathrm{i} ) ( ( z - 1 ) + 3 \mathrm{i} ) \\ = ( z - 1 )^{2} - ( 3 \mathrm{i} )^{2} \\ = z^{2} - 2 z + 1 + 9 \\ = z^{2} - 2 z + 10 \end{gathered}$
> 
> > *The other two roots are repeated and real*
> *Write the quartic as the quadratic factor multiplied by the square of a linear factor* $( P z + Q )^{2}$
> 
> $z^{4} - 8 z^{3} + A z^{2} + B z + 90 \equiv ( z^{2} - 2 z + 10 ) ( P z + Q )^{2}$
> 
> *Imagine expanding the right-hand side*
> *To get* $z^{4}$ *on the left, you can let* $P$ *equal 1*
> 
> $\begin{gathered} z^{4} - 8 z^{3} + A z^{2} + B z + 90 & \equiv ( z^{2} - 2 z + 10 ) ( z + Q )^{2} \\ \equiv ( z^{2} - 2 z + 10 ) ( z^{2} + 2 Q z + Q^{2} ) \end{gathered}$
> 
> > *To get 90 on the left, let* $Q^{2}=9$ *so* $Q=\pm3$
> *To find out which value* $Q$ *takes, expand and collect the right-hand side further*
> 
> $\begin{gathered} z^{4} - 8 z^{3} + A z^{2} + B z + 90 & \equiv z^{4} + 2 Q z^{3} + 9 z^{2} - 2 z^{3} - 4 Q z^{2} - 18 z + 10 z^{2} + 20 Q z + 90 \\ \equiv z^{4} + ( 2 Q - 2 ) z^{3} + ( 9 - 4 Q + 10 ) z^{2} + ( - 18 + 20 Q ) z + 90 \end{gathered}$
> 
> > *The* $z^{4}$ *and* $+90$ *are correct*
> *Equate the* $z^{3}$ *coefficients to get an equation in* $Q$ *and solve*
> 
> $\begin{gathered} - 8 & = 2 Q - 2 \\ - 6 & = 2 Q \\ - 3 & = Q \end{gathered}$
> 
> > *Substitute* $Q=-3$ *into the coefficient of* $z^{2}$ *to get* $A$
> 
> $\begin{gathered} A = 9 - 4 ( - 3 ) + 10 \\ = 31 \end{gathered}$
> 
> > *Substitute* $Q=-3$ *into the coefficient of* $z$ *to get* $B$
> 
> $\begin{gathered} B = - 18 + 20 ( - 3 ) \\ = - 78 \end{gathered}$
> 
> > *Write out the answers clearly*
> 
> **Final answer:** $A=31$** and **$B=-78$
> 
> **Polynomial division is not recommended as **$A$** and **$B$** are algebraic**
> $P=-1$** and **$Q=3$** also work, as the bracket **$( P z + Q )^{2}$**  is squared**
