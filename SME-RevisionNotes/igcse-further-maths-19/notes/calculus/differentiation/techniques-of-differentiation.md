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

- The **product** **rule** states that if  `y equals straight f open parentheses x close parentheses straight g open parentheses x close parentheses`  is the product of two functions $f(x)$ and $g(x)$ then

  - `fraction numerator straight d y over denominator straight d x end fraction equals straight f apostrophe open parentheses x close parentheses straight g open parentheses x close parentheses plus straight f open parentheses x close parentheses straight g apostrophe open parentheses x close parentheses`

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

- To **differentiate**  `y equals straight f open parentheses x close parentheses straight g open parentheses x close parentheses`

  - you'll need to make it clear what `straight f open parentheses x close parentheses comma space straight g open parentheses x close parentheses comma space straight f to the power of apostrophe open parentheses x close parentheses` and `straight g to the power of apostrophe open parentheses x close parentheses` are
  
    - Arranging them in a square can help
- **STEP 1**
**Identify** the two functions, `straight f open parentheses x close parentheses` and `straight g open parentheses x close parentheses`

  - Then **differentiate** each one with respect to$x$ to find `straight f to the power of apostrophe open parentheses x close parentheses` and `straight g to the power of apostrophe open parentheses x close parentheses`
- **STEP 2**
Obtain $\frac{dy}{dx}$ by applying the product rule **formula**

  - If  `y equals straight f open parentheses x close parentheses straight g open parentheses x close parentheses`,  then  $\frac{dy}{dx}=f^{'}(x)g(x)+f(x)g^{'}(x)$
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
> `fraction numerator straight d y over denominator straight d x end fraction equals open parentheses 10 x close parentheses open parentheses cos 3 x close parentheses plus open parentheses 5 x squared close parentheses open parentheses negative 3 sin 3 x close parentheses`
> 
> > *Expand the brackets*
> 
> $\frac{dy}{dx}=10x\mathrm{cos}3x-15x^{2}\mathrm{sin}3x$

## Quotient Rule

> **Spec point** — `spcpt_8CPCjzFPC6TwMWnx`

## Quotient Rule

### What is the quotient rule?

- The **quotient** **rule** states if  `y equals fraction numerator straight f open parentheses x close parentheses over denominator straight g open parentheses x close parentheses end fraction`  is the quotient of two functions `straight f open parentheses x close parentheses` and `straight g open parentheses x close parentheses` then

  - `fraction numerator straight d y over denominator straight d x end fraction equals fraction numerator straight f to the power of apostrophe open parentheses x close parentheses straight g open parentheses x close parentheses minus straight f open parentheses x close parentheses straight g to the power of apostrophe open parentheses x close parentheses over denominator open square brackets straight g open parentheses x close parentheses close square brackets squared end fraction`
  
    - This is given on the **exam formula sheet**, so you don't need to remember it
- This is sometimes written as  $y=\frac{u}{v}$  where $u$ and $v$ are both functions of $x$

  - Then  $y'=\frac{u'v-uv'}{v^{2}}$
  
    - where  $y'=\frac{dy}{dx}$,  $u'=\frac{du}{dx}$  and  $v'=\frac{dv}{dx}$

- For your **final answer** make sure you match the notation used in the question

### How do I know when to use the quotient rule?

- The **quotient** **rule** is used to **differentiate** a **quotient** of two functions

  - If the **numerator** is a **constant**, **negative** **powers** can be used
  
    - e.g  `fraction numerator k over denominator straight g open parentheses x close parentheses end fraction equals k open parentheses straight g open parentheses x close parentheses close parentheses to the power of negative 1 end exponent`
    - The **chain rule** can be used here
    - Note that `open parentheses straight g open parentheses x close parentheses close parentheses to the power of negative 1 end exponent` is different from the **inverse function** `straight g to the power of negative 1 end exponent open parentheses x close parentheses`
  - If the **denominator** is a **constant**, treat it as a **factor** of the expression
  
    - `fraction numerator straight f open parentheses x close parentheses over denominator k end fraction equals 1 over k straight f open parentheses x close parentheses`
  - The quotient rule **will still work** for both those cases
  
    - But it might not be the quickest method

### How do I use the quotient rule?

- To **differentiate**  `y equals fraction numerator straight f open parentheses x close parentheses over denominator straight g open parentheses x close parentheses end fraction`

  - you'll need to make it clear what `straight f open parentheses x close parentheses comma space straight g open parentheses x close parentheses comma space straight f to the power of apostrophe open parentheses x close parentheses` and `straight g to the power of apostrophe open parentheses x close parentheses` are
  
    - Arranging them in a square can help
- **STEP 1**
**Identify** the two functions, `straight f open parentheses x close parentheses` and `straight g open parentheses x close parentheses`

  - Then **differentiate** each one with respect to$x$ to find `straight f to the power of apostrophe open parentheses x close parentheses` and `straight g to the power of apostrophe open parentheses x close parentheses`
- **STEP 2**
Obtain $\frac{dy}{dx}$ by applying the quotient rule **formula**

  - If  `y equals fraction numerator straight f open parentheses x close parentheses over denominator straight g open parentheses x close parentheses end fraction`,  then  `fraction numerator straight d y over denominator straight d x end fraction equals fraction numerator straight f to the power of apostrophe stretchy left parenthesis x stretchy right parenthesis straight g stretchy left parenthesis x stretchy right parenthesis minus straight f stretchy left parenthesis x stretchy right parenthesis straight g to the power of apostrophe open parentheses x close parentheses over denominator open square brackets straight g open parentheses x close parentheses close square brackets squared end fraction`
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
>   - But it's probably easier to use laws of indices to rewrite as `y equals fraction numerator straight f open parentheses x close parentheses over denominator straight g open parentheses x close parentheses end fraction`
>   
>     - and then use the quotient rule

> **Worked Example**
> Given the function $f(x)=\frac{\mathrm{cos}2x}{3x+2}$,  find `straight f to the power of apostrophe open parentheses x close parentheses`.
> 
> > *We'll use *`y equals fraction numerator straight f open parentheses x close parentheses over denominator straight g open parentheses x close parentheses end fraction`* form*
> 
> > *Identify the functions *`straight f open parentheses x close parentheses`* and *`straight g open parentheses x close parentheses`
> 
> `straight f open parentheses x close parentheses equals cos 2 x space space space space space space space space space space space straight g open parentheses x close parentheses equals 3 x plus 2`
> 
> > *Differentiate those to find *`straight f apostrophe open parentheses x close parentheses`* and *`straight g to the power of apostrophe open parentheses x close parentheses`
> 
> `straight f to the power of apostrophe open parentheses x close parentheses equals negative 2 sin 2 x space space space space space space space space space space space straight g to the power of apostrophe open parentheses x close parentheses equals 3`
> 
> > *Put the pieces together using  *`fraction numerator straight d over denominator straight d x end fraction open parentheses fraction numerator straight f open parentheses x close parentheses over denominator straight g open parentheses x close parentheses end fraction close parentheses equals fraction numerator straight f to the power of apostrophe open parentheses x close parentheses straight g open parentheses x close parentheses minus straight f open parentheses x close parentheses straight g to the power of apostrophe open parentheses x close parentheses over denominator open square brackets straight g open parentheses x close parentheses close square brackets squared end fraction`* from the exam formula sheet*
> 
> `straight f apostrophe open parentheses x close parentheses equals fraction numerator open parentheses negative 2 sin 2 x close parentheses open parentheses 3 x plus 2 close parentheses minus open parentheses cos 2 x close parentheses open parentheses 3 close parentheses over denominator open parentheses 3 x plus 2 close parentheses squared end fraction`
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

  - For example  `y equals open parentheses 5 x to the power of 4 minus 2 x close parentheses to the power of 7`
  
    - $y=u^{7}$
    - $u=5x^{4}-2x$
  - Or  `y equals cos open parentheses 3 x squared minus 1 close parentheses`
  
    - $y=\mathrm{cos}u$
    - $u=3x^{2}-1$

### How can I use the chain rule to differentiate the power of a function?

- ** **The **chain rule** can be used to **differentiate** a **'power of a function'**

  - This can **save you a lot of work**
  
    - e.g. finding the derivative of `y equals open parentheses x squared minus 5 x plus 7 close parentheses to the power of 7`
    - The other option would require trying to expand `open parentheses x squared minus 5 x plus 7 close parentheses to the power of 7` first!
  - You may need to use **laws of indices**
  
    - e.g. finding the derivative of  $y=\frac{1}{\sqrt{2x-3}}$
    - Rewrite first as `y equals open parentheses 2 x minus 3 close parentheses to the power of negative 1 half end exponent`

- A power of a function can be differentiated using this **special case** of the chain rule:

  - If `y equals open square brackets straight f open parentheses x close parentheses close square brackets to the power of n`
  
    - i.e. if $y$ is the function `straight f open parentheses x close parentheses` raised to the power $n$
  - then  `space fraction numerator straight d y over denominator straight d x end fraction equals n straight f to the power of apostrophe stretchy left parenthesis x stretchy right parenthesis stretchy left square bracket straight f open parentheses x close parentheses stretchy right square bracket to the power of n minus 1 end exponent`
  
    - i.e. $n$ times the derivative of `straight f open parentheses x close parentheses`, times `straight f open parentheses x close parentheses` to the power of $n-1$
    - compare `fraction numerator straight d over denominator straight d x end fraction open parentheses x to the power of n close parentheses equals n x to the power of n minus 1 end exponent`
  - $n$ can be **any power** (including fractional and negative powers)
  - This formula is **not** on the exam formula sheet, so you need to remember it
- The power of a function may also be differentiated using the general chain rule method in the **next section**

  - But remembering the 'special case' **formula** is a lot **quicker**

### How can I use the general chain rule to differentiate a function?

- **STEP 1**
Identify $y$ and $u$

  - e.g.  `y equals cos open parentheses 3 x squared minus 1 close parentheses`
  
    - $y=\mathrm{cos}u$
    - $u=3x^{2}-1$
- **STEP 2**
Find  $\frac{dy}{du}$ and $\frac{du}{dx}$

  - $\frac{dy}{du}=-\mathrm{sin}u$
  - $\frac{du}{dx}=6x$
- **STEP 3**
Substitute into  $\frac{dy}{dx}=\frac{dy}{du}\times\frac{du}{dx}$

  - `fraction numerator straight d y over denominator straight d x end fraction equals open parentheses negative sin u close parentheses cross times open parentheses 6 x close parentheses`
- **STEP 4**
Substitute the expression for $u$ back in

  - This gets $\frac{dy}{dx}$ entirely in terms of $x$
  
    - `fraction numerator straight d y over denominator straight d x end fraction equals open parentheses negative sin open parentheses 3 x squared minus 1 close parentheses close parentheses cross times open parentheses 6 x close parentheses equals negative 6 x sin open parentheses 3 x squared minus 1 close parentheses`

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
> > *This is *`y equals open square brackets straight f open parentheses x close parentheses close square brackets to the power of n`* with *$n=7$* and *`straight f open parentheses x close parentheses equals x squared minus 5 x plus 7`
> 
> > *Start by finding the derivative of *`straight f open parentheses x close parentheses`
> 
> `fraction numerator straight d over denominator straight d x end fraction open parentheses x squared minus 5 x plus 7 close parentheses equals 2 x minus 5`
> 
> > *Now use  *`space fraction numerator straight d y over denominator straight d x end fraction equals n straight f to the power of apostrophe stretchy left parenthesis x stretchy right parenthesis stretchy left square bracket straight f open parentheses x close parentheses stretchy right square bracket to the power of n minus 1 end exponent`
> 
> `fraction numerator straight d y over denominator straight d x end fraction equals 7 open parentheses 2 x minus 5 close parentheses open parentheses x squared minus 5 x plus 7 close parentheses to the power of 7 minus 1 end exponent`
> 
> $\frac{dy}{dx}=7(2x-5)(x^{2}-5x+7)^{6}$
> 
> (b) Find the derivative of  $y=\sqrt{\mathrm{sin}x}$.
> 
> > *First use laws of indices to write as a power*
> 
> `y equals open parentheses sin x close parentheses to the power of 1 half end exponent`
> 
> > *This is *`y equals open square brackets straight f open parentheses x close parentheses close square brackets to the power of n`* with *$n=\frac{1}{2}$* and *`straight f open parentheses x close parentheses equals sin x`
> 
> > *Find the derivative of *`straight f open parentheses x close parentheses`
> 
> `fraction numerator straight d over denominator straight d x end fraction open parentheses sin x close parentheses equals cos x`
> 
> > *Now use  *`space fraction numerator straight d y over denominator straight d x end fraction equals n straight f to the power of apostrophe stretchy left parenthesis x stretchy right parenthesis stretchy left square bracket straight f open parentheses x close parentheses stretchy right square bracket to the power of n minus 1 end exponent`
> 
> `table row cell fraction numerator straight d y over denominator straight d x end fraction end cell equals cell open parentheses 1 half close parentheses open parentheses cos x close parentheses open parentheses sin x close parentheses to the power of 1 half minus 1 end exponent end cell row blank equals cell fraction numerator cos x over denominator 2 end fraction open parentheses sin x close parentheses to the power of negative 1 half end exponent end cell end table`
> 
> > *And by laws of indices  *`open parentheses sin x close parentheses to the power of negative 1 half end exponent equals 1 over open parentheses sin x close parentheses to the power of 1 half end exponent equals fraction numerator 1 over denominator square root of sin x end root end fraction`
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
> `fraction numerator straight d y over denominator straight d x end fraction equals open parentheses straight e to the power of u close parentheses cross times open parentheses negative sin x close parentheses`
> 
> > *Substitute the expression for *$u$* back in*
> 
> `fraction numerator straight d y over denominator straight d x end fraction equals open parentheses straight e to the power of cos x end exponent close parentheses cross times open parentheses negative sin x close parentheses`
> 
> $\frac{dy}{dx}=-(\mathrm{sin}x)e^{\mathrm{cos}x}$
