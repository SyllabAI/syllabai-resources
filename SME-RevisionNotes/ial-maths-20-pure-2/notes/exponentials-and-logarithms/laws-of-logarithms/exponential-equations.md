---
note_id: "rn_Yh9WSHHxFkT6YGpk"
title: "Exponential Equations"
source: https://www.savemyexams.com/international-a-level/maths/edexcel/20/pure-2/revision-notes/exponentials-and-logarithms/laws-of-logarithms/exponential-equations
path: exponentials-and-logarithms/laws-of-logarithms/exponential-equations
updated_at: "2026-07-02T08:19:38.538Z"
spec_point_ids: ["spcpt_9kbfchzHcdwh6WZN"]
spec_point_codes: []
guided_study: false
---

# Exponential Equations

## Exponential Equations

> **Spec point** — `spcpt_9kbfchzHcdwh6WZN`

## Exponential equations

### What are exponential equations?

- An equation where the unknown is a power
- In simple cases the solutions can be “spotted”

![Exponential Equations Notes fig2, A Level & AS Maths: Pure revision notes](../../../assets/ac77cc343ae4-6-2-2-exponential-equations-notes-fig2.png)

- See Exponential Functions

### How do I solve exponential equations in the form a<sup>f(x)</sup> = b?

- If the value of *b* can be written as a power of *a* (*b* = *a*<sup>*k* </sup>)

  - Write $a^{f(x)}=a^{k}$
  - Solve $f(x)=k$
- If the value of *b* can not be written as a power of *a*

  - Apply logs of base *a* to both sides to get:
  
    - $f(x)=\mathrm{log}_{a}b$
  - Solve for *x*

### How do I solve exponential equations in the form a<sup>f(x)</sup> = b<sup>g(x)</sup>?

- If the value of *b* can be written as a power of *a* (*b* = *a*<sup>*k* </sup>)

  - Use the index law to rewrite $b^{g(x)}$
  
    - $b^{ \mathrm{g} ( x )} = ( a^{k )^{g} ( x )} = a^{k \mathrm{g} ( x ) }$
  - Write $a^{ \mathrm{f} ( x )} = a^{k \mathrm{g} ( x ) }$
  - Solve $f(x)=kg(x)$
- If the value of *b* can not be written as a power of *a*

  - Apply logs of the same base (any base will work) to both sides to get:
  
    - $\log ( a^{ \mathrm{f} ( x )} ) = \log ( b^{ \mathrm{g} ( x )} )$
  - Use the laws of logarithms to bring the power to the front:
  
    - $\mathrm{f} ( x ) \log a = \mathrm{g} ( x ) \log b$
  - log *a* and log *b* are just numbers so rearrange and solve for *x*
- If either side is multiplied by a constant ($pa^{f(x)}$ )

  - Do **not** write as $(pa)^{f(x)}$ – this is **incorrect**
  - Still take logs of both sides but you will need to use another law of logs
  
    - $\log ( p a^{ \mathrm{f} ( x )} ) = \log p + \log p a^{ \mathrm{f} ( x )}$
  - log *p* is just a constant so can be solved in the same way as above

### How do I solve exponential equations with three terms?

- If the equation has three terms such as $a^{ \mathrm{f} ( x )} + a^{ \mathrm{g} ( x )} + c = 0$

  - Use the index laws in reverse to split up the powers
  
    - $a^{Ax+B}=a^{Ax}\timesa^{B}$
  - Try and use a substitution to transform the equation into a quadratic
  
    - See Further Solving Quadratics (Hidden Quadratics)
    - Look out for terms where one power is double another power
  - Solve the quadratic
  - For each solution find the corresponding value(s) of *x*

> **Worked Example**
> ![5-1-4-exp-equations-we-solution](assets/2d8877bcae16-5-1-4-exp-equations-we-solution.png)

> **Exam Hint**
> - Pay attention to how the question asks you to write your answer
> 
>   - it could ask for exact form, a specific form or rounded to a specified degree of accuracy
