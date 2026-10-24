---
note_id: "rn_qHfcfhXx2Bg3HQkQ"
title: "Techniques of Differentiation"
source: https://www.savemyexams.com/igcse/further-maths/edexcel/19/revision-notes/calculus/differentiation/techniques-of-differentiation
path: calculus/differentiation/techniques-of-differentiation
updated_at: "2024-10-20T15:17:27.425Z"
spec_point_ids: ["spcpt_73PM55Cdbc4wmMbw", "spcpt_8CPCjzFPC6TwMWnx", "spcpt_r7zgkvS5WHxQnK3Q"]
spec_point_codes: []
guided_study: false
---

# Techniques of Differentiation

## Product Rule

> **Spec point** — `spcpt_73PM55Cdbc4wmMbw`

## Product Rule

### What is the product rule?

- The **product** **rule** states that if  $y = \mathrm{f} ( x ) \mathrm{g} ( x )$  is the product of two functions $f(x)$ and $g(x)$ then

  - $\frac{ \mathrm{d} y}{ \mathrm{d} x} = \mathrm{f} ' ( x ) \mathrm{g} ( x ) + \mathrm{f} ( x ) \mathrm{g} ' ( x )$

- This is **not** given on the exam formula sheet, so you need to remember it
- This is sometimes written as  $y=uv$  where $u$ and $v$ are both functions of $x$

  - Then $y'=u'v+uv'$
  
    - where  $y'=\frac{dy}{dx}$,  $u'=\frac{du}{dx}$  and  $v'=\frac{dv}{dx}$

- For your **final answer **make sure you match the notation used in the question

### How do I know when to use the product rule?

- The **product rule** is used to **differentiate** a **product** of two functions

  - This can easily be confused with a 'function of a function' (see the **Chain** **Rule** note)
  
    - $\mathrm{sin}(\mathrm{cos}x)$ is a function of a function, “sin of cos of $x$”
    - $\mathrm{sin}x\mathrm{cos}x$ is a product of two functions, “sin *x* times cos $x$”

### How do I use the product rule?

- To **differentiate**  $y = \mathrm{f} ( x ) \mathrm{g} ( x )$

  - you'll need to make it clear what $\mathrm{f} ( x ) , \mathrm{g} ( x ) , \mathrm{f}^{'} ( x )$ and $\mathrm{g}^{'} ( x )$ are
  
    - Arranging them in a square can help
- **STEP 1**
**Identify** the two functions, $\mathrm{f} ( x )$ and $\mathrm{g} ( x )$

  - Then **differentiate** each one with respect to$x$ to find $\mathrm{f}^{'} ( x )$ and $\mathrm{g}^{'} ( x )$
- **STEP 2**
Obtain $\frac{dy}{dx}$ by applying the product rule **formula**

  - If  $y = \mathrm{f} ( x ) \mathrm{g} ( x )$,  then  $\frac{dy}{dx}=f^{'}(x)g(x)+f(x)g^{'}(x)$
  - **Simplify** the answer if
  
    - it is straightforward to do so
    - or if the question requires a particular form

- In trickier problems **chain** **rule** may have to be used when finding $u'$ and $v'$

> **Exam Hint**
> - Using $u,v,u'$ and $v'$ can save time writing
> 
>   - lay them out in a 2x2 'square' to help keep which is which straight
> - For trickier functions chain rule may be required along with product rule
> 
>   - i.e.  either $u$ and/or $v$ could be a 'function of a function'
>   - So chain rule needed to find $u'$ and $v'$

> **Worked Example**
> Find the derivative of $y=5x^{2}\mathrm{cos}3x$.
> 
> > *We'll use  *$y=uv$*  form*
> 
> > *Identify the functions *$u$* and *$v$
> 
> $u=5x^{2}v=\mathrm{cos}3x$
> 
> > *Differentiate those to find *$u'$* and *$v'$
> 
> $u'=10xv'=-3\mathrm{sin}3x$
> 
> > *Put the pieces together using  *$y'=u'v+uv'$
> 
> $\frac{ \mathrm{d} y}{ \mathrm{d} x} = ( 10 x ) ( \cos 3 x ) + ( 5 x^{2} ) ( - 3 \sin 3 x )$
> 
> > *Expand the brackets*
> 
> $\frac{dy}{dx}=10x\mathrm{cos}3x-15x^{2}\mathrm{sin}3x$

## Quotient Rule

> **Spec point** — `spcpt_8CPCjzFPC6TwMWnx`

## Quotient Rule

### What is the quotient rule?

- The **quotient** **rule** states if  $y = \frac{ \mathrm{f} ( x )}{ \mathrm{g} ( x )}$  is the quotient of two functions $\mathrm{f} ( x )$ and $\mathrm{g} ( x )$ then

  - $\frac{ \mathrm{d} y}{ \mathrm{d} x} = \frac{ \mathrm{f}^{'} ( x ) \mathrm{g} ( x ) - \mathrm{f} ( x ) \mathrm{g}^{'} ( x )}{[ \mathrm{g} ( x ) ]^{2}}$
  
    - This is given on the **exam formula sheet**, so you don't need to remember it
- This is sometimes written as  $y=\frac{u}{v}$  where $u$ and $v$ are both functions of $x$

  - Then  $y'=\frac{u'v-uv'}{v^{2}}$
  
    - where  $y'=\frac{dy}{dx}$,  $u'=\frac{du}{dx}$  and  $v'=\frac{dv}{dx}$

- For your **final answer** make sure you match the notation used in the question

### How do I know when to use the quotient rule?

- The **quotient** **rule** is used to **differentiate** a **quotient** of two functions

  - If the **numerator** is a **constant**, **negative** **powers** can be used
  
    - e.g  $\frac{k}{ \mathrm{g} ( x )} = k ( \mathrm{g} ( x ) )^{- 1}$
    - The **chain rule** can be used here
    - Note that $( \mathrm{g} ( x ) )^{- 1}$ is different from the **inverse function** $\mathrm{g}^{- 1} ( x )$
  - If the **denominator** is a **constant**, treat it as a **factor** of the expression
  
    - $\frac{ \mathrm{f} ( x )}{k} = \frac{1}{k} \mathrm{f} ( x )$
  - The quotient rule **will still work** for both those cases
  
    - But it might not be the quickest method

### How do I use the quotient rule?

- To **differentiate**  $y = \frac{ \mathrm{f} ( x )}{ \mathrm{g} ( x )}$

  - you'll need to make it clear what $\mathrm{f} ( x ) , \mathrm{g} ( x ) , \mathrm{f}^{'} ( x )$ and $\mathrm{g}^{'} ( x )$ are
  
    - Arranging them in a square can help
- **STEP 1**
**Identify** the two functions, $\mathrm{f} ( x )$ and $\mathrm{g} ( x )$

  - Then **differentiate** each one with respect to$x$ to find $\mathrm{f}^{'} ( x )$ and $\mathrm{g}^{'} ( x )$
- **STEP 2**
Obtain $\frac{dy}{dx}$ by applying the quotient rule **formula**

  - If  $y = \frac{ \mathrm{f} ( x )}{ \mathrm{g} ( x )}$,  then  $\frac{ \mathrm{d} y}{ \mathrm{d} x} = \frac{ \mathrm{f}^{'} ( x ) \mathrm{g} ( x ) - \mathrm{f} ( x ) \mathrm{g}^{'} ( x )}{[ \mathrm{g} ( x ) ]^{2}}$
  - **Simplify** the answer if
  
    - it is straightforward to do so
    - or if the question requires a particular form

- In trickier problems **chain** **rule** may have to be used when finding $u'$ and $v'$

> **Exam Hint**
> - For trickier functions chain rule may be required along with product rule
> 
>   - i.e.  either $u$ and/or $v$ could be a 'function of a function'
>   - So chain rule needed to find $u'$ and $v'$
> - Look out for functions of the form $y=f(x)(g(x))^{-1}$
> 
>   - These can be differentiated using a combination of chain rule and product rule
>   
>     - It would be good practice to try this sometime!
>   - But it's probably easier to use laws of indices to rewrite as $y = \frac{ \mathrm{f} ( x )}{ \mathrm{g} ( x )}$
>   
>     - and then use the quotient rule

> **Worked Example**
> Given the function $f(x)=\frac{\mathrm{cos}2x}{3x+2}$,  find $\mathrm{f}^{'} ( x )$.
> 
> > *We'll use *$y = \frac{ \mathrm{f} ( x )}{ \mathrm{g} ( x )}$* form*
> 
> > *Identify the functions *$\mathrm{f} ( x )$* and *$\mathrm{g} ( x )$
> 
> $\mathrm{f} ( x ) = \cos 2 x \mathrm{g} ( x ) = 3 x + 2$
> 
> > *Differentiate those to find *$\mathrm{f} ' ( x )$* and *$\mathrm{g}^{'} ( x )$
> 
> $\mathrm{f}^{'} ( x ) = - 2 \sin 2 x \mathrm{g}^{'} ( x ) = 3$
> 
> > *Put the pieces together using  *$\frac{ \mathrm{d} }{ \mathrm{d} x} ( \frac{ \mathrm{f} ( x )}{ \mathrm{g} ( x )} ) = \frac{ \mathrm{f}^{'} ( x ) \mathrm{g} ( x ) - \mathrm{f} ( x ) \mathrm{g}^{'} ( x )}{[ \mathrm{g} ( x ) ]^{2}}$* from the exam formula sheet*
> 
> $\mathrm{f} ' ( x ) = \frac{( - 2 \sin 2 x ) ( 3 x + 2 ) - ( \cos 2 x ) ( 3 )}{( 3 x + 2 )^{2}}$
> 
> > *Simplify the numerator*
> *(The denominator is simplest left as it is)*
> 
> $f^{'}(x)=\frac{-2(3x+2)\mathrm{sin}2x-3\mathrm{cos}2x}{(3x+2)^{2}}$

## Chain Rule

> **Spec point** — `spcpt_r7zgkvS5WHxQnK3Q`

## Chain Rule

### What is the chain rule?

- The **chain rule** is used to **differentiate** a **composite function**

  - A function of a function
- The **chain** **rule** is given by the **formula**

  - $\frac{dy}{dx}=\frac{dy}{du}\times\frac{du}{dx}$
  
    - where $y$ is a function of $u$
    - and $u$ is a function of $x$
    - (Of course this ultimately makes $y$ a function of $x$ as well!)

- It can also be written in **function** **notation** as

  - If  $y=f(g(x))$,  then  $\frac{dy}{dx}=f'(g(x))g'(x)$
- The chain rule makes it possible to differentiate a **function of a function**

  - For example  $y = ( 5 x^{4} - 2 x )^{7}$
  
    - $y=u^{7}$
    - $u=5x^{4}-2x$
  - Or  $y = \cos ( 3 x^{2} - 1 )$
  
    - $y=\mathrm{cos}u$
    - $u=3x^{2}-1$

### How can I use the chain rule to differentiate the power of a function?

- ** **The **chain rule** can be used to **differentiate** a **'power of a function'**

  - This can **save you a lot of work**
  
    - e.g. finding the derivative of $y = ( x^{2} - 5 x + 7 )^{7}$
    - The other option would require trying to expand $( x^{2} - 5 x + 7 )^{7}$ first!
  - You may need to use **laws of indices**
  
    - e.g. finding the derivative of  $y=\frac{1}{\sqrt{2x-3}}$
    - Rewrite first as $y = ( 2 x - 3 )^{- 1 \frac{1}{2}}$

- A power of a function can be differentiated using this **special case** of the chain rule:

  - If $y = [ \mathrm{f} ( x ) ]^{n}$
  
    - i.e. if $y$ is the function $\mathrm{f} ( x )$ raised to the power $n$
  - then  $\frac{ \mathrm{d} y}{ \mathrm{d} x} = n \mathrm{f}^{' ( x ) [ \mathrm{f} ( x ) ]^{n} - 1}$
  
    - i.e. $n$ times the derivative of $\mathrm{f} ( x )$, times $\mathrm{f} ( x )$ to the power of $n-1$
    - compare $\frac{ \mathrm{d} }{ \mathrm{d} x} ( x^{n ) = n x^{n} - 1}$
  - $n$ can be **any power** (including fractional and negative powers)
  - This formula is **not** on the exam formula sheet, so you need to remember it
- The power of a function may also be differentiated using the general chain rule method in the **next section**

  - But remembering the 'special case' **formula** is a lot **quicker**

### How can I use the general chain rule to differentiate a function?

- **STEP 1**
Identify $y$ and $u$

  - e.g.  $y = \cos ( 3 x^{2} - 1 )$
  
    - $y=\mathrm{cos}u$
    - $u=3x^{2}-1$
- **STEP 2**
Find  $\frac{dy}{du}$ and $\frac{du}{dx}$

  - $\frac{dy}{du}=-\mathrm{sin}u$
  - $\frac{du}{dx}=6x$
- **STEP 3**
Substitute into  $\frac{dy}{dx}=\frac{dy}{du}\times\frac{du}{dx}$

  - $\frac{ \mathrm{d} y}{ \mathrm{d} x} = ( - \sin u ) \times ( 6 x )$
- **STEP 4**
Substitute the expression for $u$ back in

  - This gets $\frac{dy}{dx}$ entirely in terms of $x$
  
    - $\frac{ \mathrm{d} y}{ \mathrm{d} x} = ( - \sin ( 3 x^{2} - 1 ) ) \times ( 6 x ) = - 6 x \sin ( 3 x^{2} - 1 )$

> **Exam Hint**
> - When asked to differentiate a 'power of a function', the chain rule is usually your best option
> 
>   - Look out for 'hidden powers'
>   
>     - e.g. square roots (fractional powers)
>     - or functions in a denominator (negative powers)
> - To integrate a general 'function of a function' the chain rule is your only option!

> **Worked Example**
> (a) Find the derivative of$y=(x^{2}-5x+7)^{7}$.
> 
> > *This is *$y = [ \mathrm{f} ( x ) ]^{n}$* with *$n=7$* and *$\mathrm{f} ( x ) = x^{2} - 5 x + 7$
> 
> > *Start by finding the derivative of *$\mathrm{f} ( x )$
> 
> $\frac{ \mathrm{d} }{ \mathrm{d} x} ( x^{2} - 5 x + 7 ) = 2 x - 5$
> 
> > *Now use  *$\frac{ \mathrm{d} y}{ \mathrm{d} x} = n \mathrm{f}^{' ( x ) [ \mathrm{f} ( x ) ]^{n} - 1}$
> 
> $\frac{ \mathrm{d} y}{ \mathrm{d} x} = 7 ( 2 x - 5 ) ( x^{2} - 5 x + 7 )^{7 - 1}$
> 
> $\frac{dy}{dx}=7(2x-5)(x^{2}-5x+7)^{6}$
> 
> (b) Find the derivative of  $y=\sqrt{\mathrm{sin}x}$.
> 
> > *First use laws of indices to write as a power*
> 
> $y = ( \sin x )^{1 \frac{1}{2}}$
> 
> > *This is *$y = [ \mathrm{f} ( x ) ]^{n}$* with *$n=\frac{1}{2}$* and *$\mathrm{f} ( x ) = \sin x$
> 
> > *Find the derivative of *$\mathrm{f} ( x )$
> 
> $\frac{ \mathrm{d} }{ \mathrm{d} x} ( \sin x ) = \cos x$
> 
> > *Now use  *$\frac{ \mathrm{d} y}{ \mathrm{d} x} = n \mathrm{f}^{' ( x ) [ \mathrm{f} ( x ) ]^{n} - 1}$
> 
> $\begin{gathered} \frac{ \mathrm{d} y}{ \mathrm{d} x} & = ( 1 \frac{1}{2} ) ( \cos x ) ( \sin x )^{1 \frac{1}{2} - 1} \\ = \frac{\cos x}{2} ( \sin x )^{- 1 \frac{1}{2}} \end{gathered}$
> 
> > *And by laws of indices  *$( \sin x )^{- 1 \frac{1}{2}} = \frac{1}{( \sin x )^{1 \frac{1}{2}}} = \frac{1}{ \sqrt{\sin x} }$
> 
> $\frac{dy}{dx}=\frac{\mathrm{cos}x}{2\sqrt{\mathrm{sin}x}}$
> 
> (c) Find the derivative of $y=e^{\mathrm{cos}x}$.
> 
> > *This is not a 'power of a function', so we need to use the general chain rule method*
> 
> > *Start by identifying *$y$* and *$u$
> 
> $y=e^{u}\,\,u=\mathrm{cos}x$
> 
> > *Differentiate*
> 
> $\frac{dy}{du}=e^{u}\,\,\frac{du}{dx}=-\mathrm{sin}x$
> 
> > *Substitute into  *$\frac{dy}{dx}=\frac{dy}{du}\times\frac{du}{dx}$
> 
> $\frac{ \mathrm{d} y}{ \mathrm{d} x} = ( \mathrm{e}^{u} ) \times ( - \sin x )$
> 
> > *Substitute the expression for *$u$* back in*
> 
> $\frac{ \mathrm{d} y}{ \mathrm{d} x} = ( \mathrm{e}^{\cos x} ) \times ( - \sin x )$
> 
> $\frac{dy}{dx}=-(\mathrm{sin}x)e^{\mathrm{cos}x}$
