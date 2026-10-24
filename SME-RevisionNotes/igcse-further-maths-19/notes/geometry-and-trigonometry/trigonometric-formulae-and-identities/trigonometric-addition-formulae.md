---
note_id: "rn_GXqsQGmtrPjgGzST"
title: "Trigonometric Addition Formulae"
source: https://www.savemyexams.com/igcse/further-maths/edexcel/19/revision-notes/geometry-and-trigonometry/trigonometric-formulae-and-identities/trigonometric-addition-formulae
path: geometry-and-trigonometry/trigonometric-formulae-and-identities/trigonometric-addition-formulae
updated_at: "2024-10-20T13:34:48.837Z"
spec_point_ids: ["spcpt_RYybv4csdhgVmvkB"]
spec_point_codes: []
guided_study: false
---

# Trigonometric Addition Formulae

## Trigonometric Addition Formulae

> **Spec point** — `spcpt_RYybv4csdhgVmvkB`

## Trigonometric Addition Formulae

### What are the trigonometric addition formulae?

- There are six **trigonometric addition formulae** (also known as **compound angle formulae**),

  - two each for **sin**, **cos** and **tan**
- The formulae for **sin** are

  - $\sin ( A + B ) = \sin A \cos B + \cos A \sin B$
  - $\sin ( A - B ) = \sin A \cos B - \cos A \sin B$
  
    - Note that the +/- sign on the left-hand side **matches** the one on the right-hand side

- The formulae for **cos** are

  - $\cos ( A + B ) = \cos A \cos B - \sin A \sin B$
  - $\cos ( A - B ) = \cos A \cos B + \sin A \sin B$
  
    - Note that the +/- sign on the left-hand side is **opposite to** the one on the right-hand side

- The formulae for **tan** are

  - $\tan ( A + B ) \equiv \frac{\tan A + \tan B}{1 - \tan A \tan B}$
  - $\tan ( A - B ) \equiv \frac{\tan A - \tan B}{1 + \tan A \tan B}$
  
    - Note that the +/- sign on the left-hand side **matches** the one in the **numerator** on the right-hand side, and is **opposite to** the one in the **denominator**
- These formulae are all on the **exam formula sheet**

  - so you don't need to remember them
  - but you do need to be able to use them

### What are the double angle formulae?

- The **double angle formulae** are special cases of the trigonometric addition formulae

  - They are formed by setting $A=B$ in the '+' versions of the addition formulae
- The **sin** version is

  - $\sin ( 2 A ) = 2 \sin A \cos A$
- The **cos** version is

  - $\cos ( 2 A ) = \cos ^{2} A - \sin ^{2} A = 1 - 2 \sin ^{2} A = 2 \cos ^{2} A - 1$
  
    - The last two forms come from using the $\mathrm{sin}^{2}A+\mathrm{cos}^{2}A=1$ identity
    - i.e. $\mathrm{cos}^{2}A=1-\mathrm{sin}^{2}A$ and $\mathrm{sin}^{2}A=1-\mathrm{cos}^{2}A$
- The **tan** version is

  - $\tan ( 2 A ) = \frac{2 \tan A}{1 - \tan ^{2} A}$
- These formulae are **not** on the exam formula sheet

  - They are used frequently, so you may want to remember them
  - But they are also easy to derive from the addition formulae that are on the sheet

### How are the trigonometric addition formulae used?

- The formulae can be used to find the **values** of trigonometric ratios **without a calculator**

  - For example, to find the value of sin15°
  
    - **rewrite** it as sin(45–30)°
    - apply the **formula** for sin(A –B)
    - use your knowledge of **exact values** to calculate the answer
- The formulae can also be used

  - to **derive** further trigonometric identities (like the double angle formulae)
  - in trigonometric **proof**
  - to **simplify** trigonometric equations before solving

> **Exam Hint**
> - Remember that the trigonometric addition formulae are on the exam formula sheet
> 
>   - But always be careful with the +/- signs when using the formulae

> **Worked Example**
> a) Show that $\tan ( x + \frac{\pi }{4} ) - \tan ( x - \frac{\pi }{4} ) = \frac{2 ( \tan ^{2} x + 1 )}{1 - \tan ^{2} x}$.
> 
> > *Use the trigonometric addition formulae for tan*
> 
> > *Also recall that *$\mathrm{tan}\frac{π}{4}=1$
> 
> $\text{tan} ( x + \frac{pi}{4} ) = \frac{ \text{tan} x + \text{tan} \frac{pi}{4}}{1 - \text{tan} x \text{tan} \frac{pi}{4}} = \frac{ \text{tan} x + 1}{1 - \text{tan} x}$
> 
> $\text{tan} ( x - \frac{pi}{4} ) = \frac{ \text{tan} x - \text{tan} \frac{pi}{4}}{1 + \text{tan} x \text{tan} \frac{pi}{4}} = \frac{ \text{tan} x - 1}{1 + \text{tan} x}$
> 
> > *Substitute those into the left-hand side of the equation and rearrange*
> 
> $\begin{gathered} \tan ( x + \frac{\pi }{4} ) - \tan ( x - \frac{\pi }{4} ) & = \frac{\tan x + 1}{1 - \tan x} - \frac{\tan x - 1}{1 + \tan x} \\ = \frac{( \tan x + 1 ) ( 1 + \tan x ) - ( \tan x - 1 ) ( 1 - \tan x )}{( 1 - \tan x ) ( 1 + \tan x )} \\ = \frac{\tan ^{2} x + 2 \tan x + 1 + \tan ^{2} x - 2 \tan x + 1}{1 - \tan ^{2} x} \\ = \frac{2 \tan ^{2} x + 2}{1 - \tan ^{2} x} \\ = \frac{2 ( \tan ^{2} x + 1 )}{1 - \tan ^{2} x} \end{gathered}$
> 
> `tan stretchy ( x + pi / 4 stretchy ) - _ tan stretchy ( x - pi / 4 stretchy ) = ( 2 ( tan ^ 2 invisible function application x + 1 ))/( 1 - tan ^ 2 invisible function application x)`
> 
> b) Hence solve $\tan ( x + \frac{\pi }{4} ) - \tan ( x - \frac{\pi }{4} ) = - 4$  in the interval  $0\leqx\leq\frac{π}{2}$.
> 
> *Substitute the result from part (a) into the equation*
> 
> > *Then rearrange and solve*
> 
> $\begin{gathered} \frac{2 ( \tan ^{2} x + 1 )}{1 - \tan ^{2} x} & = - 4 \\ \frac{\tan ^{2} x + 1}{1 - \tan ^{2} x} & = - 2 \\ \tan ^{2} x + 1 & = 2 \tan ^{2} x - 2 \\ \tan ^{2} x & = 3 \\ \tan x & = \pm \sqrt{3} \\ x = \frac{\pi }{3} , - \frac{\pi }{3} \end{gathered}$
> 
> > *But only *$\frac{π}{3}$* is in the range *$0\leqx\leq\frac{π}{2}$
> 
> $x=\frac{π}{3}$
