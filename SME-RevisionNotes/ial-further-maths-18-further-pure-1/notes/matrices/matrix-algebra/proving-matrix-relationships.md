---
note_id: "rn_TCf54CMjTMyCHpPj"
title: "Proving Matrix Relationships"
source: https://www.savemyexams.com/international-a-level/further-maths/edexcel/18/further-pure-1/revision-notes/matrices/matrix-algebra/proving-matrix-relationships
path: matrices/matrix-algebra/proving-matrix-relationships
updated_at: "2024-04-10T09:30:57.449Z"
spec_point_ids: ["spcpt_BhD7jyg3SMt38vvJ"]
spec_point_codes: []
guided_study: false
---

# Proving Matrix Relationships

## Proving Matrix Relationships

> **Spec point** — `spcpt_BhD7jyg3SMt38vvJ`

## Proving Matrix Relationships

### What is a matrix relationship?

- A matrix **relationship** is an equation that connects different matrices

  - For example, if **A**, **B** and **C** are matrices then possible relationships are
  
    - **AB** = **C**
    - **A** + 2**B** = **C**
- Remember that in general matrix multiplication is **not commutative**

  - **AB **≠** BA**
  - **ABC **≠ **ACB** ≠ **BAC** ≠ …
  - **CBC** does not simplify to **C**<sup>2</sup>**B**
  
    - Since **C**(**BC**) ≠ **C**(**CB**)

### What matrix relationships do I need to know?

- If **A** and **B** are matrices and **I** is the **identity matrix**, you need to know the following:

  - **AA**<sup>-1</sup> =** I**
  - **A**<sup>-1</sup>**A** = **I**
  - **IA** = **AI **= **A**
  - (**AB**)<sup>-1</sup> = **B**<sup>-1</sup>**A**<sup>-1</sup>
  
    - The **order reverses**

### How do I prove matrix relationships?

- You need to carefully **pre-multiply** (on the left) or** post-multiply** (on the right) **both sides** by matrices or their inverses

  - To make **B** the subject of **AB** = **C**
  
    - **A**<sup>-1</sup>**AB** = **A**<sup>-1</sup>**C** (pre-multiply by **A**<sup>-1</sup>)
    - **IB** = **A**<sup>-1</sup>**C** (form the identity)
    - **B **= **A**<sup>-1</sup>**C** (simplify)
  - To make **A** the subject of **AB** = **C**
  
    - **ABB**<sup>-1</sup> = **CB**<sup>-1</sup> (post-multiply by **B**<sup>-1</sup>)
    - **AI **= **CB**<sup>-1</sup> (form the identity)
    - **A** =** CB**<sup>-1</sup> (simplify)

### How do I prove that (AB)<sup>-1</sup> = B<sup>-1</sup>A<sup>-1</sup>?

- Start by **multiplying AB** by its **inverse** to form the** identity**

  - **AB**(**AB**)<sup>-1</sup> = **I**
- Then make **(AB)**<sup>**-1**</sup> the **subject**

  - Pre-multiply by **A**<sup>-1</sup> and simplify
  
    - **A**<sup>-1</sup>**AB**(**AB**)<sup>-1</sup> = **A**<sup>-1</sup>**I**
    - **IB**(**AB**)<sup>-1</sup>=**A**<sup>-1</sup>
    - **B**(**AB**)<sup>-1</sup>=**A**<sup>-1</sup>
  - Then pre-multiply by **B**<sup>-1</sup> and simplify
  
    - **B**<sup>-1</sup>**B**(**AB**)<sup>-1</sup>=**B**<sup>-1</sup>**A**<sup>-1</sup>
    - **I**(**AB**)<sup>-1</sup>=**B**<sup>-1</sup>**A**<sup>-1</sup>
    - (**AB**)<sup>-1</sup>=**B**<sup>-1</sup>**A**<sup>-1</sup>

> **Exam Hint**
> - Learn the formula (**AB**)<sup>-1 </sup>=**B**<sup>-1</sup>**A**<sup>-1</sup> as you are not given it in the Formulae Booklet.
> 
> - Show lots of steps when doing matrix algebra.
> 
>   - Examiners want to see pre- or post-multiplying clearly.

> **Worked Example**
> Let $P$, $Q$ and $R$ be three matrices such that $\mathrm{PQR}^{-1}=I$ where $I$ is the identity matrix.
> 
> Prove that $Q=P^{-1}R$.
> 
> > *You need to use matrix algebra to make *$Q$* the subject*
> *One possible way is to remove *$P$* from the left by pre-multiplying both  sides by *$P^{-1}$
> 
> $P^{-1}\mathrm{PQR}^{-1}=P^{-1}I$
> 
> > *The *$P^{-1}P$* forms the identity matrix, *$I$*, on the left*
> *The *$P^{-1}I$* simplifies to just *$P^{-1}$* on the right*
> 
> $\mathrm{IQR}^{-1}=P^{-1}$
> 
> > *The *$\mathrm{IQR}^{-1}$* on the left simplifies to just *$\mathrm{QR}^{-1}$
> 
> $\mathrm{QR}^{-1}=P^{-1}$
> 
> > *Now post-multiply both sides by *$R$
> 
> $\mathrm{QR}^{-1}R=P^{-1}R$
> 
> > *The *$R^{-1}R$* on the left forms the identity matrix*
> 
> $\mathrm{QI}=P^{-1}R$
> 
> > *The *$\mathrm{QI}$* on the left simplifies to *$Q$
> 
> $Q=P^{-1}R$
