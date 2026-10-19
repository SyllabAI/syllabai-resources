---
note_id: "rn_tzms3MNjz7zvPSRK"
title: "Rates of Change"
source: https://www.savemyexams.com/igcse/further-maths/edexcel/19/revision-notes/calculus/applications-of-differentiation/rates-of-change
path: calculus/applications-of-differentiation/rates-of-change
updated_at: "2024-10-20T15:31:52.246Z"
spec_point_ids: ["spcpt_ZZrY5rw5sBbWbbZy", "spcpt_8jcwyqx46F7WVjRS"]
spec_point_codes: []
guided_study: false
---

# Rates of Change

## Approximations Using Rates of Change

> **Spec point** — `spcpt_ZZrY5rw5sBbWbbZy`

## Approximations Using Rates of Change

### How can I use rates of change to approximate changes in value?

- Remember that a **derivative** in maths represents a **rate of change**
- e.g. if  $y=x^{3}$  then  $\frac{dy}{dx}=3x^{2}$

  - When  $x=2$,  `fraction numerator straight d y over denominator straight d x end fraction equals 3 open parentheses 2 close parentheses squared equals 12`
  
    - That's the **rate of change **of $y$ with respect to $x$ when $x=2$
  - As soon as $x$ **changes** away from 2, $\frac{dy}{dx}$ is no longer equal to 12
  
    - But it will still be **close to** 12 so long as $x$ is still close to 2
- We can use this to **approximate** the change in one variable based on a change in the other variable:

  - $dy\approx\frac{dy}{dx}dx$
  - That is, when $x$ changes by a **small amount** $dx$
  
    - the **change** in the value of $y$,  $dy$,
    - will be **approximately** equal to $\frac{dy}{dx}$ times $dx$
- This approximation is only **valid** when the change in $x$ is **small**

  - The **smaller** the change in $x$ is,
  
    - the **more accurate** the approximation will be
- You may need to **derive** rates of change starting from standard **geometric formulae**

  - e.g.  the volume of a sphere is  $V=\frac{4}{3}πr^{3}$
  - Take the **derivative** with respect to $r$,  $\frac{dV}{dr}=4πr^{2}$
  
    - That's the **rate of change **of volume with respect to radius
- You may also need to use the relation  `fraction numerator straight d x over denominator straight d y end fraction equals 1 divided by fraction numerator straight d y over denominator straight d x end fraction equals fraction numerator 1 over denominator open parentheses fraction numerator straight d y over denominator straight d x end fraction close parentheses end fraction`

  - e.g. you may need $\frac{dr}{dV}$ to answer a question
  
    - Then  `fraction numerator straight d r over denominator straight d V end fraction equals fraction numerator 1 over denominator open parentheses fraction numerator straight d V over denominator straight d r end fraction close parentheses end fraction equals fraction numerator 1 over denominator 4 pi r squared end fraction`

> **Exam Hint**
> - Look out for calculus questions asking you to 'estimate' or 'approximate' the change in a quantity
> 
>   - The  $dy\approx\frac{dy}{dx}dx$ approximation is likely to be required
>   - Remember that's only valid when $dx$ is small

> **Worked Example**
> A sphere has a radius of $5\mathrm{cm}$.
> 
> The surface area of the sphere is increased by $15\mathrm{cm}^{2}$.
> 
> Using calculus, find an estimate for the increase in the radius of the sphere.  Give your answer in $\mathrm{cm}$, correct to 2 significant figures.
> 
> > *'Using calculus' and 'find an estimate for the increase' are hints that we should use  *$dy\approx\frac{dy}{dx}dx$
> 
> > *Here we know the change in the surface area, *$dA$
> 
> > *We want to estimate the change in the radius, *$dr$
> 
> $dr\approx\frac{dr}{dA}dA$
> 
> > *Write down the formula for the surface area of a sphere from the exam formula sheet*
> 
> $A=4πr^{2}$
> 
> > *Differentiate that with respect to *$r$* to find *$\frac{dA}{dr}$* *
> 
> $\frac{dA}{dr}=8πr$
> 
> > *But we need *$\frac{dr}{dA}$* for our approximation formula, so use  *`fraction numerator straight d x over denominator straight d y end fraction equals fraction numerator 1 over denominator open parentheses fraction numerator straight d y over denominator straight d x end fraction close parentheses end fraction`
> 
> `fraction numerator straight d r over denominator straight d A end fraction equals fraction numerator 1 over denominator open parentheses fraction numerator straight d A over denominator straight d r end fraction close parentheses end fraction equals fraction numerator 1 over denominator 8 pi r end fraction`
> 
> > *Substitute that into the approximation formula*
> 
> $dr\approx\frac{1}{8πr}dA$
> 
> > *We want to know the value of that when *$r=5$* and *$dA=15$
> 
> > *(Note that that is a 'small' change, *$dA$*, compared to the total surface area of *$100π=314.15...\mathrm{cm}^{2}$* when *$r=5$*) *
> 
> `straight d r almost equal to fraction numerator 1 over denominator 8 pi open parentheses 5 close parentheses end fraction open parentheses 15 close parentheses equals fraction numerator 3 over denominator 8 pi end fraction equals 0.119366...`
> 
> > *Round to 2 significant figures, as required*
> 
> $0.12\mathrm{cm}(2s.f.)$

## Connected Rates of Change

> **Spec point** — `spcpt_8jcwyqx46F7WVjRS`

## Connected Rates of Change

### What is meant by rates of change?

- A **rate** **of** **change** is a measure of

  - how a quantity is changing
  - with respect to another quantity
- Mathematically rates of change are **derivatives**

  - $\frac{dV}{dr}$ could be
  
    - the rate at which the **volume** $V$ of a sphere changes
    - with respect to how its **radius **$r$ is changing
- **Context** is important when interpreting positive and negative rates of change

  - A **positive** rate of change indicates an increase
  
    - e.g. the change in volume of water as a bathtub fills
  - A **negative** rate of change indicates a decrease
  
    - e.g. the change in volume of water in a leaking bucket
  - If a question talks about **rate of** **increase** or **decrease**
  
    - make sure you use the appropriate sign (+/-)

### What is meant by connected rates of change?

- **Connected** **rates** **of** **change** are **connected** by a linking variable or parameter

  - They are also called '**related rates of change**'
  - Often the linking parameter is **time**, represented by$t$
  
    - **seconds** is the standard unit for time
    - but a question may use other units
- e.g.  Water running into a large bowl

  - both the **height** and **volume** of water in the bowl change with time
  - **time** is the linking parameter

### What are the key ideas involved with connected rates of change?

- These questions usually involve the **chain rule **

  - $\frac{dy}{dx}=\frac{dy}{du}\times\frac{du}{dx}$

- **Different letters** may be used relative to the context

  - e.g. $V$ for **volume, **$A$ for **area, **$h$ for **height, **$r$ for **radius**
  - For **time** problems you will often use the form  $\frac{dy}{dt}=\frac{dy}{du}\times\frac{du}{dt}$
  
    - where $y$ and $u$ represent other quantities in the question
- Note that  `fraction numerator straight d x over denominator straight d y end fraction equals 1 divided by fraction numerator straight d y over denominator straight d x end fraction equals fraction numerator 1 over denominator open parentheses fraction numerator straight d y over denominator straight d x end fraction close parentheses end fraction`

  - Use this if you **know** a derivative $\frac{dy}{dx}$
  
    - but you **need to know** the derivative $\frac{dx}{dy}$ instead
- Also note that the chain rule can be **extended** to more than two terms on the right-hand side

  - e.g.  $\frac{dy}{dx}=\frac{dy}{du}\times\frac{du}{dv}\times\frac{dv}{dx}$
  - This lets you **connect more variables** using the chain rule
- Remember, a **derivative** is **not** a **fraction**

  - But if you treat the derivatives on the **right-hand side** of the chain rule as fractions
  
    - then their common terms should '**cancel out**'
    - to give you the derivative on the **left-hand side**
  - This is a way to **check** a chain rule formula
  
    - It can also help you **write** the formula in the first place

### How do I solve problems involving connected rates of change?

Most **connected rates of change** questions will involve the following steps

- **STEP 1**
Write down the rate of change **given** and the rate of change **required**

  - Write these down as **derivatives**
  - If **unsure** of the rates of change involved, use the **units** given as a clue
  
    - e.g.  $m/s$ (or $\mathrm{ms}^{-1}$, metres per second)
    - This would be the rate of change of length with respect to time
    - The precise 'length of what' would depend on the question
- **STEP 2**
Use **chain rule** to form an **equation** connecting these rates of change with a third rate

  - The third rate of change will come from a **related** quantity
  
    - e.g. volume, surface area, perimeter
  - More complicated questions may involve **more than three** rates of change
  
    - But those will still be able to be **connected** by the chain rule
- **STEP 3**
Write down the **formula** for a related quantity (volume, etc)

  - This can then be **differentiated**
  
    - which will provide a **formula** for one or more of your rates of change
- **STEP 4**
**Substitute** all the known values into the chain rule equation

  - Then **solve** for the value you need to know

> **Exam Hint**
> - To determine which rate of change to use, look at the units for help
> 
>   - e.g.  A rate of 5 **cm**<sup>**3**</sup> *per* **second** implies **volume** *per* **time**
>   - so the rate would likely be $\frac{dV}{dt}$

> **Worked Example**
> A cuboid has a fixed height of 5 cm, and a square cross-section with side length of$x$ cm in the other two dimensions.
> 
> The volume of the cuboid is increasing at a fixed rate of 20 cm<sup>3</sup> per second.
> 
> Find the rate at which the side length is increasing at the time when the side length is 3 cm.
> 
> > *Write down what is given, and what we need to know*
> 
> $\frac{dV}{dt}=20\mathrm{cm}^{3}/s$
> 
> $\mathrm{What} \mathrm{is}\frac{dx}{dt}\mathrm{when}x=3\mathrm{cm}?$
> 
> > *Note that length and volume are both given in terms of centimetres, so we won't need to convert any units*
> 
> *Write down a chain rule equation connecting *$\frac{dV}{dt}$* and *$\frac{dx}{dt}$
> 
> $\frac{dx}{dt}=\frac{d?}{d?}\times\frac{dV}{dt}$
> 
> > *The right-hand side should 'cancel out' to be equal with the left-hand side*
> *This means the missing derivative must be *$\frac{dx}{dV}$
> 
> $\frac{dx}{dt}=\frac{dx}{dV}\times\frac{dV}{dt}$
> 
> > *Now we need to find *$\frac{dx}{dV}$
> 
> > *Write down the volume of a cuboid formula, *$V=\mathrm{height}\times\mathrm{length}\times\mathrm{width}$
> 
> > *Here the height is 5, and the length and width are both *$x$
> 
> > *This gives a formula connecting *$V$* and *$x$
> 
> `table row V equals cell 5 cross times x cross times x end cell row blank equals cell 5 x squared end cell end table`
> 
> > *Now differentiate that with respect to *$x$
> 
> > *That will give a formula for *$\frac{dV}{dx}$* in terms of *$x$
> 
> $\frac{dV}{dx}=10x$
> 
> > *But our chain rule formula needs  *$\frac{dx}{dV}$
> 
> > *We can find this using  *`fraction numerator straight d x over denominator straight d y end fraction equals fraction numerator 1 over denominator open parentheses begin display style fraction numerator straight d y over denominator straight d x end fraction end style close parentheses end fraction`
> 
> `fraction numerator straight d x over denominator straight d V end fraction equals fraction numerator 1 over denominator open parentheses begin display style fraction numerator straight d V over denominator straight d x end fraction end style close parentheses end fraction equals fraction numerator 1 over denominator 10 x end fraction`
> 
> > *Substitute that into the chain rule formula*
> 
> $\frac{dx}{dt}=\frac{1}{10x}\times\frac{dV}{dt}$
> 
> > *We know *$\frac{dV}{dt}=20$*, and we want to know *$\frac{dx}{dt}$* when *$x=3$
> 
> > *Substitute those values into the chain rule formula*
> 
> $\mathrm{When}x=3,$
> 
> `table attributes columnalign right center left columnspacing 0px end attributes row cell fraction numerator straight d x over denominator straight d t end fraction end cell equals cell fraction numerator 1 over denominator 10 open parentheses 3 close parentheses end fraction cross times 20 end cell row blank equals cell 20 over 30 end cell row blank equals cell 2 over 3 end cell end table`
> 
> > *Don't forget the units when giving your final answer!*
> 
> $\frac{dx}{dt}=\frac{2}{3}\mathrm{cm}/s$
