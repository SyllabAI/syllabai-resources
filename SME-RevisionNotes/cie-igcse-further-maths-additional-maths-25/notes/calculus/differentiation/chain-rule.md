---
note_id: "rn_ckd2rtRGpnfkwzp4"
title: "Chain Rule"
source: https://www.savemyexams.com/igcse/further-maths/cie/additional-maths/25/revision-notes/calculus/differentiation/chain-rule
path: calculus/differentiation/chain-rule
updated_at: "2026-07-02T08:19:38.521Z"
spec_point_ids: ["spcpt_7VHhcbpGm4bQrx3v"]
spec_point_codes: []
guided_study: false
---

# Chain Rule

## Chain Rule

> **Spec point** — `spcpt_7VHhcbpGm4bQrx3v`

## Chain rule

### What is the chain rule?

- The **chain** **rule** states if$y$ is a function of$u$ and$u$ is a function of$x$ then

$y=f(u(x))$

$\frac{dy}{dx}=\frac{dy}{du}\times\frac{du}{dx}$

- In **function** **notation** this could be written

$y=f(g(x))$

$\frac{dy}{dx}=f'(g(x))g'(x)$

### How do I know when to use the chain rule?

- ** **The chain rule is used when we are trying to differentiate **composite** **functions**

  - “function of a function”
  - these can be identified as the variable (usually$x$) does not ‘appear alone’
  
    - $\mathrm{sin}x$ – **not** a composite function, $x$ ‘appears alone’
    - $\mathrm{sin}(3x+2)$ **is** a **composite function;** $x$ is tripled and has 2 added to it before the sine function is applied

### How do I use the chain rule?

**STEP 1**

Identify the two functions

Rewrite $y$ as a function of$u$; $y=f(u)$

Write $u$ as a function of$x$; $u=g(x)$

**STEP 2**

Differentiate $y$ with respect to $u$ to get$\frac{dy}{du}$ Differentiate $u$ with respect to $x$ to get$\frac{du}{dx}$

**STEP 3**

Obtain $\frac{dy}{dx}$ by applying the formula$\frac{dy}{dx}=\frac{dy}{du}\times\frac{du}{dx}$ and substitute$u$ back in for$g(x)$

- In trickier problems **chain** **rule** may have to be applied **more than once**

How do I differentiate (*ax* + *b*)<sup>n</sup>?

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

### How do I differentiate √(ax+b)?

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

### Are there any standard results for using chain rule?

- The following general results are particularly useful

  - If$\text{size} 16px \text{size} 16px y \text{size} 16px = ( \mathrm{f} ( x ) )^{size} 16px n$ then$\frac{dy}{dx}=nf^{'}(x)f(x)^{n-1}$

- If$y=e^{f(x)}$ then$\frac{dy}{dx}=f^{'}(x)e^{f(x)}$

  - If$y = \ln ( \mathrm{f} ( x ) )$ then$\frac{dy}{dx}=\frac{f^{'}(x)}{f(x)}$
  - If$y = \sin ( \mathrm{f} ( x ) )$ then$\frac{ \mathrm{d} y}{ \mathrm{d} x} = \mathrm{f}^{'} ( x ) \cos ( \mathrm{f} ( x ) )$
  - If$y = \cos ( \mathrm{f} ( x ) )$ then$\frac{ \mathrm{d} y}{ \mathrm{d} x} = - \mathrm{f}^{'} ( x ) \sin ( \mathrm{f} ( x ) )$
  - If $\text{size} 16px y \text{size} 16px = \text{size} 16px \tan ( \mathrm{f} ( x ) )$ then `Alternative text not available`

> **Exam Hint**
> - You should aim to be able to spot and carry out the chain rule mentally (rather than use substitution)
> 
>   - every time you use it, say it to yourself in your head *“differentiate the first function ignoring the second, then multiply by the derivative of the second function"*

> **Worked Example**
> a) Find the derivative of$y=(x^{2}-5x+7)^{7}$.
> 
> > *STEP 1   Identify the two functions and rewrite*
> 
> > $y=u^{7}$*           *$u=x^{2}-5x+7$
> 
> > *STEP 2   Find *$\frac{dy}{du}$* and *$\frac{du}{dx}$
> 
> > $\frac{dy}{du}=7u^{6}$*         *$\frac{du}{dx}=2x-5$
> 
> > *STEP 3   Apply the chain rule, *$\frac{dy}{dx}=\frac{dy}{du}\times\frac{du}{dx}$
> 
> $\frac{ \mathrm{d} y}{ \mathrm{d} x} = 7 u^{6} ( 2 x - 5 )$
> 
> > *Substitute *$u$* in terms of *$x$* back in*
> 
> $= 7 ( x^{2} - 5 x + 7 )^{6} ( 2 x - 5 )$
> 
> $\frac{dy}{dx}=7(2x-5)(x^{2}-5x+7)^{6}$
> 
> b) Find the derivative of$y=\mathrm{sin}(e^{2x})$.
> 
> > *(In this solution, we will be applying the mental method discussed in the Exam Tip above)*
> 
> > *"... differentiate *`sin box _`*, ignore *$e^{2x}$*"*
> 
> `( d y)/( d x) = cos ( e ^ 2 x ) x box`
> 
> > *"... multiply by the derivative of *$e^{2x}$*": differentiate *$e^{2x}$* using the result "if *$y=e^{f(x)}$*, then *$\frac{dy}{dx}=f^{'}(x)e^{f(x)}$*"*
> 
> $\frac{ \mathrm{d} y}{ \mathrm{d} x} = \cos ( \mathrm{e}^{2 x} ) \times 2 \mathrm{e}^{2 x}$
> 
> $\frac{dy}{dx}=2e^{2x}\mathrm{cos}(e^{2x})$
