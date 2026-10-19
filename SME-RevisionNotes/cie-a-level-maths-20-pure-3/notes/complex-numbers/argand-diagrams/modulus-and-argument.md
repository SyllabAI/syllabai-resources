---
note_id: "rn_2x9gDBS9kgChvkfV"
title: "Modulus & Argument"
source: https://www.savemyexams.com/a-level/maths/cie/20/pure-3/revision-notes/complex-numbers/argand-diagrams/modulus-and-argument
path: complex-numbers/argand-diagrams/modulus-and-argument
updated_at: "2026-07-02T08:19:38.129Z"
spec_point_ids: ["spcpt_CTzdQvyV74XgQhWs", "spcpt_zp6rDS7x7nWFJG2K"]
spec_point_codes: []
guided_study: true
---

# Modulus & Argument

## Modulus & Argument

> **Spec point** — `spcpt_CTzdQvyV74XgQhWs`

## Modulus & argument

### How do I find the modulus of a complex number?

- The modulus of a complex number is its **distance **from the origin when plotted on an Argand diagram
- The modulus of $z$ is written `open vertical bar z close vertical bar`
- If $z=x+iy$, then we can use **Pythagoras** to show…

  - `open vertical bar z close vertical bar equals square root of x squared plus y squared end root`
- A modulus is always **positive**
- the modulus is related to the complex **conjugate** by…

  - `z z to the power of asterisk times equals z to the power of asterisk times z equals open vertical bar z close vertical bar squared`
  - This is because `z z to the power of asterisk times equals open parentheses x plus straight i y close parentheses open parentheses x minus straight i y close parentheses equals x squared plus y squared`
- In general, `open vertical bar z subscript 1 plus z subscript 2 close vertical bar not equal to open vertical bar z subscript 1 close vertical bar plus vertical line z subscript 2 vertical line`

  - e.g. both $z_{1}=3+4i$ and $z_{2}=-3+4i$ have a modulus of 5, but $z_{1}+z_{2}$ simplifies to $8i$ which has a modulus of 8

![8-2-3_notes_fig1](../../../assets/aa88241b9f44-8-2-3-notes-fig1.png)

### How do I find the argument of a complex number?

- The argument of a complex number is the anti-clockwise **angle** that it makes when starting at the positive real axis on an Argand diagram
- Arguments are measured in **radians**

  - Sometimes these can be given exact in terms of $π$
- The argument of $z$ is written $\mathrm{arg}z$
- Arguments can be calculated using right-angled **trigonometry**

  - This involves using the tan ratio plus a sketch to decide whether it is positive/negative and acute/obtuse
- Arguments are usually given in the range $-π<\mathrm{arg}z\leqπ$

  - Negative arguments are for complex numbers in the third and fourth quadrants
  - Occasionally you could be asked to give arguments in the range $0\leq\mathrm{arg}z<2π$
- The argument of zero, $\mathrm{arg}0$ is undefined (no angle can be drawn)

![8-2-3_notes_fig2](../../../assets/aeda3338f274-8-2-3-notes-fig2.png)

> **Worked Example**
> ![8-2-3_example_fig1-part-1](assets/7982bdddd1aa-8-2-3-example-fig1-part-1.png)
> 
> ![8-2-3_example_fig1-part-2](assets/4f189e455127-8-2-3-example-fig1-part-2.png)

> **Exam Hint**
> - Give non-exact arguments in radians to 3 significant figures.

## Modulus-Argument (Polar) Form

> **Spec point** — `spcpt_zp6rDS7x7nWFJG2K`

## Modulus-argument (polar) form

The complex number $z=x+iy$ is said to be in Cartesian form. There are, however, other ways to write a complex number, such as in modulus-argument (polar) form.

### How do I write a complex number in modulus-argument (polar) form?

- The **Cartesian form **of a complex number, $z=x+iy$, is written in terms of its real part, $x$, and its imaginary part, $y$
- If we let `r equals vertical line z vertical line` and $θ=\mathrm{arg}z$, then it is possible to write a complex number in terms of its modulus, $r$, and its argument, $θ$, called the **modulus-argument (polar) form**, given by...

  - `z equals r open parentheses cos space theta plus isin space theta close parentheses`
- It is usual to give arguments in the range $-π<θ\leqπ$

  - Negative arguments should be shown clearly, e.g. `z equals 2 open parentheses cos space open parentheses negative pi over 3 close parentheses plus isin space open parentheses negative pi over 3 close parentheses close parentheses`without simplifying `cos invisible function application left parenthesis negative pi over 3 right parenthesis`  to either `cos invisible function application open parentheses pi over 3 close parentheses` or $\frac{1}{2}$
  - Occasionally you could be asked to give arguments in the range $0\leqθ<2π$
- If a complex number is given in the form `z equals r open parentheses cos space theta minus isin space theta close parentheses`, then it is not currently in modulus-argument (polar) form due to the minus sign, but can be converted as follows…

  - By considering transformations of trigonometric functions, we see that `negative sin invisible function application theta identical to sin invisible function application left parenthesis negative theta right parenthesis` and `cos invisible function application theta identical to cos invisible function application left parenthesis negative theta right parenthesis`
  - Therefore `z equals r open parentheses cos invisible function application theta minus isin invisible function application theta close parentheses` can be written as `z equals r open parentheses cos invisible function application open parentheses negative theta close parentheses plus isin invisible function application open parentheses negative theta close parentheses close parentheses`, now in the correct form and indicating an argument of $-θ$
- To convert from modulus-argument (polar) form back to Cartesian form, evaluate the real and imaginary parts

  - E.g. `z equals 2 open parentheses cos invisible function application open parentheses negative pi over 3 close parentheses plus isin invisible function application open parentheses negative pi over 3 close parentheses close parentheses` becomes `z equals 2 open parentheses 1 half plus straight i open parentheses negative fraction numerator square root of 3 over denominator 2 end fraction close parentheses close parentheses equals 1 minus square root of 3 blank straight i`

![8-2-3_notes_fig3](../../../assets/bcb7d3943b0c-8-2-3-notes-fig3.png)

### What are the rules for moduli and arguments under multiplication and division?

- When two complex numbers, $z_{1}$ and $z_{2}$, are **multiplied** to give $z_{1}z_{2}$, their **moduli** are also **multiplied**

  - `open vertical bar z subscript 1 z subscript 2 close vertical bar equals open vertical bar z subscript 1 close vertical bar vertical line z subscript 2 vertical line`
- When two complex numbers, $z_{1}$ and $z_{2}$, are **divided** to give $\frac{z_{1}}{z_{2}}$, their **moduli** are also **divided**

  - `open vertical bar z subscript 1 over z subscript 2 close vertical bar equals fraction numerator open vertical bar z subscript 1 close vertical bar over denominator open vertical bar z subscript 2 close vertical bar end fraction`
- When two complex numbers, $z_{1}$ and $z_{2}$, are **multiplied** to give $z_{1}z_{2}$, their **arguments** are **added**

  - `arg space open parentheses z subscript 1 z subscript 2 close parentheses equals arg space z subscript 1 plus arg space z subscript 2`
- When two complex numbers, $z_{1}$and $z_{2}$, are **divided** to give $\frac{z_{1}}{z_{2}}$, their **arguments** are **subtracted**

  - `arg space open parentheses z subscript 1 over z subscript 2 close parentheses equals arg space z subscript 1 minus arg space z subscript 2`

### How do I multiply complex numbers in modulus-argument (polar) form?

- The main benefit of writing complex numbers in modulus-argument (polar) form is that they multiply and divide very easily (often quicker than when in Cartesian form)
- To **multiply** two complex numbers, $z_{1}$ and $z_{2}$, in modulus-argument (polar) form we use the rules from above to **multiply their moduli** and **add their arguments**

  - `open vertical bar z subscript 1 z subscript 2 close vertical bar equals open vertical bar z subscript 1 close vertical bar open vertical bar z subscript 2 close vertical bar`
  - $\mathrm{arg}(z_{1}z_{2})=\mathrm{arg}z_{1}+\mathrm{arg}z_{2}$
- So if $z_{1}=r_{1}(\mathrm{cos}θ_{1}+\mathrm{isin}θ_{1})$ and $z_{2}=r_{2}(\mathrm{cos}θ_{2}+\mathrm{isin}θ_{2})$ then the rules above give…

  - `z subscript 1 z subscript 2 equals r subscript 1 r subscript 2 open parentheses cos space open parentheses theta subscript 1 plus theta subscript 2 close parentheses plus isin space open parentheses theta subscript 1 plus theta subscript 2 close parentheses close parentheses blank`
- Sometimes the new argument, $θ_{1}+θ_{2}$, does not lie in the range $-π<θ\leqπ$ (or  $0\leqθ<2π$  if this is being used)

  - An out-of-range argument can be adjusted by either **adding or subtracting **$2π$
  - E.g. If $θ_{1}=\frac{2π}{3}$ and $θ_{2}=\frac{π}{2}$  then  $θ_{1}+θ_{2}=\frac{7π}{6}$
  
    - This is currently not in the range , but by subtracting $2π$ from $\frac{7π}{6}$ to give $-\frac{5π}{6}$, a new argument is formed that lies in the correct range and represents the same angle on an Argand diagram
- The rules of **multiplying the moduli** and **adding the arguments **can also be applied when…

  - …multiplying three complex numbers together, $z_{1}z_{2}z_{3}$, or more
  - …finding powers of a complex number (e.g. $z^{2}$ can be written as $zz$)
- Whilst not examinable, the rules for multiplication can be proved algebraically by multiplying $z_{1}=r_{1}(\mathrm{cos}θ_{1}+\mathrm{isin}θ_{1})$ by $z_{2}=r_{2}(\mathrm{cos}θ_{2}+\mathrm{isin}θ_{2})$, expanding the brackets and using compound angle formulae

### How do I divide complex numbers in modulus-argument (polar) form?

- To **divide** two complex numbers, $z_{1}$ and $z_{2}$ in modulus-argument (polar) form, we use the rules from above to **divide their moduli** and **subtract their arguments**

  - `open vertical bar z subscript 1 over z subscript 2 close vertical bar blank equals fraction numerator open vertical bar z subscript 1 close vertical bar over denominator vertical line z subscript 2 vertical line end fraction`
  - `arg space open parentheses z subscript 1 over z subscript 2 close parentheses equals arg space z subscript 1 minus arg space z subscript 2`
- So if $z_{1}=r_{1}(\mathrm{cos}θ_{1}+\mathrm{isin}θ_{1})$ and $z_{2}=r_{2}(\mathrm{cos}θ_{2}+\mathrm{isin}θ_{2})$ then the rules above give…

  - `z subscript 1 over z subscript 2 equals r subscript 1 over r subscript 2 open parentheses cos space open parentheses theta subscript 1 minus theta subscript 2 close parentheses plus isin space open parentheses theta subscript 1 minus theta subscript 2 close parentheses close parentheses blank`
- As with multiplication, sometimes the new argument, $θ_{1}-θ_{2}$, can lie out of the range $-π<θ\leqπ$ (or the range $0\leqθ<2π$ if this is being used)

  - You can **add or subtract **$2π$ to bring out-of-range arguments back in range
- Whilst not examinable, the rules for division can be proved algebraically by dividing $z_{1}=r_{1}(\mathrm{cos}θ_{1}+\mathrm{isin}θ_{1})$ by $z_{2}=r_{2}(\mathrm{cos}θ_{2}+\mathrm{isin}θ_{2})$, using complex division and compound angle formulae

> **Worked Example**
> ![8-2-3_example_fig2-part-1](assets/244144250ac7-8-2-3-example-fig2-part-1.png)
> 
> ![8-2-3_example_fig2-part-2](assets/2456d29ddf87-8-2-3-example-fig2-part-2.png)

> **Exam Hint**
> - The rules for multiplying and dividing in modulus-argument (polar) form must be learnt (they are not given in the formula booklet).
> - Remember to add or subtract $2π$ to any out-of-range arguments to bring them back in range.
> - If a question does not give a clear range for arguments, then both $-π<θ\leqπ$  or  $0<θ\leq2π$  would be accepted.
