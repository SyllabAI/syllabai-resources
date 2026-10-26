---
note_id: "rn_9PkwbNQgDdTy4Nyh"
title: "Chain Rule"
source: https://www.savemyexams.com/as/maths/cie/20/pure-1/revision-notes/differentiation/differentiation/chain-rule
path: differentiation/differentiation/chain-rule
updated_at: "2026-07-02T08:19:38.538Z"
spec_point_ids: ["spcpt_pPPkKgggBhJzKnDq"]
spec_point_codes: []
guided_study: true
---

# Chain Rule

## Chain Rule

> **Spec point** — `spcpt_pPPkKgggBhJzKnDq`

## Chain Rule

#### What is the chain rule?

- If ***y*** is a function of ***u***, and ***u*** is a function of ***x***, then the **chain rule** tells us that

$\frac{dy}{dx}=\frac{dy}{du}\times\frac{du}{dx}$

- The chain rule allows us to differentiate more complicated expressions and **composite functions**
- You will often see and use the **chain rule** with different variables

  - This is particularly useful for **connected rates of change**

#### How do I differentiate (ax + b)<sup>n</sup>?

- For *n = 2* you will most likely **expand the brackets** and differentiate each term separately
- If *n > 2* this becomes **time-consuming** and if *n* is not a positive integer we need a different method completely
- The chain rule allows us to use **substitution** to differentiate any function in the form *y* = (*ax* + *b*)<sup>n</sup>

  - Let *u = ax + b, *then *y = u*<sup>*n*</sup>
  - **Differentiate** both parts **separately**
  
    - $\frac{du}{dx}=a$ and $\frac{dy}{du}=nu^{n-1}$
  - Put both parts into the **chain rule**
  
    - $\frac{dy}{dx}=\frac{dy}{du}\times\frac{du}{dx}=a\timesnu^{n-1}=anu^{n-1}$
  - **Substitute** *u = ax + b *back into your answer
  
    - $\frac{dy}{dx}=an(ax+b)^{n-1}$

#### How do I differentiate √(ax+b)?

- The chain rule allows us to use **substitution** to differentiate any function in the form $y=\sqrt{ax+b}$
- Rewrite $\sqrt{ax+b}=(ax+b)^{\frac{1}{2}}$

  - Let *u = ax + b, *then *y = u*<sup>*½*</sup>
  - **Differentiate** both parts **separately**
  
    - $\frac{du}{dx}=a$ and $\frac{dy}{du}=\frac{1}{2}u^{-\frac{1}{2}}$
  - Put both parts into the **chain rule**
  
    - $\frac{dy}{dx}=\frac{dy}{du}\times\frac{du}{dx}=a\times\frac{1}{2}u^{-\frac{1}{2}}=\frac{a}{2}u^{-\frac{1}{2}}$
  - **Substitute** *u = ax + b *back into your answer
  
    - $\frac{ \mathrm{d} y}{ \mathrm{d} x} = \frac{a}{2} ( a x + b )^{- 1 \frac{1}{2}} = \frac{a}{2 \sqrt{a x + b} }$
- This method can be used for any **fractional power** of any linear or non-linear expression

  - Provided you know how to differentiate the non-linear expression

#### How do I differentiate (f(x))<sup>n</sup>?

- This method can be used for any linear or non – linear expression

  - Let *u *= f(*x*) and follow the method above
  - In general if $y=(f(x))^{n}$ then $\frac{ \mathrm{d} y}{ \mathrm{d} x} = n \mathrm{f}^{ \mathrm{'} ( x ) ( \mathrm{f} ( x ) )^{n} - 1}$
- With practice you will be able to carry out this method **without the need for *****u***

  - This is essential for learning the **reverse chain rule** later in the course

> **Worked Example**
> ![5-1-4-chain-rule-we-solution-part-1](assets/b147bdde07a6-5-1-4-chain-rule-we-solution-part-1.png)
> 
> ![5-1-4-chain-rule-we-solution-part-2](assets/e56028298894-5-1-4-chain-rule-we-solution-part-2.png)

> **Exam Hint**
> If using *u *as a substitution don't forget to substitute *x *back into your final answer.
