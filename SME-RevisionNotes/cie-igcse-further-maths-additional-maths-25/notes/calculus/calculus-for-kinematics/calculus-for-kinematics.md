---
note_id: "rn_v9Tp9ZGnRvh6tgXt"
title: "Calculus for Kinematics"
source: https://www.savemyexams.com/igcse/further-maths/cie/additional-maths/25/revision-notes/calculus/calculus-for-kinematics/calculus-for-kinematics
path: calculus/calculus-for-kinematics/calculus-for-kinematics
updated_at: "2026-07-02T08:19:38.113Z"
spec_point_ids: ["spcpt_mvBk4XZgQmTP4bnD", "spcpt_8Nm5QbB6qYDJJtkT"]
spec_point_codes: []
guided_study: false
---

# Calculus for Kinematics

## Differentiation for Kinematics

> **Spec point** — `spcpt_mvBk4XZgQmTP4bnD`

## Differentiation for kinematics

### How is differentiation used in kinematics?

- **Displacement**, **velocity** and **acceleration** are related by calculus
- In terms of differentiation and derivatives

  - **velocity** is the **rate** of **change** of **displacement**
  
    - $v=\frac{ds}{dt}$  or  $v(t)=s'(t)$
  - **acceleration** is the **rate** of **change** of **velocity**
  
    - $a=\frac{dv}{dt}$  or  $a(t)=v'(t)$
  - so **acceleration** is also the **second** **derivative** of **displacement**
  
    - $a=\frac{d^{2}s}{dt^{2}}$  or  $a(t)=s''(t)$

> **Worked Example**
> The displacement, $x$ m, of a particle at $t$ seconds, is modelled by the function $x(t)=2t^{3}-27t^{2}+84t$.
> 
> Find expressions for `x apostrophe (t)` and `x apostrophe apostrophe (t)`, and state what these expressions represent.
> 
> $x=2t^{3}-27t^{2}+84t$
> 
> > `x apostrophe (t)` *means the same as* $\frac{dx}{dt}$
> 
> `x apostrophe open parentheses t close parentheses space equals space 6 t squared minus 54 t plus 84
> x apostrophe open parentheses t close parentheses space equals space 6 open parentheses t squared minus 9 t plus 14 close parentheses`
> 
> $x'(t)=6(t-2)(t-7)$
>  **This expression represents the velocity of the particle.** 
> **Answers may or may not need to be factorised, depending on the question**
> 
> > `x apostrophe apostrophe (t)` *means the same as* $\frac{d^{2}x}{dt^{2}}$
> 
> `x apostrophe apostrophe (t)=12t−54`
> 
> $x''(t)=6(2t-9)$ 
> **This expression represents the acceleration of the particle.**

## Integration for Kinematics

> **Spec point** — `spcpt_8Nm5QbB6qYDJJtkT`

## Integration for kinematics

### How is integration used in kinematics?

- Since **velocity** is the **derivative** of **displacement** ($v=\frac{ds}{dt}$) it follows that

`space s equals integral v space straight d t`

- Similarly, **velocity** will be an **antiderivative** of **acceleration**

`space v equals integral a space straight d t`

### How would I find the constant of integration in kinematics problems?

- A **boundary** or **initial** condition would need to be known

  - phrases involving the word **“initial”,** or **“initially”** are referring to **time** being **zero,** i.e. $t=0$
  - you might also be given information about the object at some other time (this is called a **boundary condition**)
  - **substituting** the values in from the **initial or boundary condition** would allow the **constant** of **integration** to be found

### How are definite integrals used in kinematics?

- Definite integrals can be used to find the displacement of a particle between two points in time

  - `space integral_ t_ 1 end_ superscript t_ 2 end superscript v left parenthesis t right parenthesis straight d t` would give the **displacement** of the particle **between** the times$t=t_{1}$ and$t=t_{2}$
  
    - This can be found using a velocity-time graph by **subtracting** the **total area below** the horizontal axis from the **total area above**
    - You could think of this as the "net area" e.g. 4 m - 1 m = 3 m
  - `space integral_ t_ 1 end_ superscript t_ 2 end superscript open vertical bar v left parenthesis t right parenthesis close vertical bar straight d t` gives the **distance **a particle has **travelled** between the times$t=t_{1}$ and$t=t_{2}$
  
    - This can be found using a velocity velocity-time graph by **adding** the **total area below** the horizontal axis to the **total area above**
    - You could think of this as the "gross area" e.g. 4 m + 1 m = 5 m

> **Exam Hint**
> - Sketching the velocity-time graph can help you visualise the distances travelled using areas between the graph and the horizontal axis

> **Worked Example**
> A particle moving in a straight horizontal line has velocity $v$ ms<sup>-1</sup> at time $t$ seconds modelled by $v(t)=8t^{3}-12t^{2}-2t$.
> 
> a) Given that the initial position of the particle is at the origin, find an expression for its displacement from the origin at time $t$ seconds.
> 
> > *The integral of the velocity gives the displacement*
> 
> `s open parentheses t close parentheses space equals integral v open parentheses t close parentheses space d t space space equals space integral open parentheses 8 t cubed minus 12 t squared minus 2 t close parentheses space d t
> s open parentheses t close parentheses space equals space 2 t to the power of 4 minus 4 t cubed minus t squared plus c`
> 
> > *"Initial" means when* $t=0$ *and "at the origin" means* $s=0$
> 
> > *Substitute these values in to find* $c$
> 
> `0 space equals space 2 open parentheses 0 close parentheses to the power of 4 minus 4 open parentheses 0 close parentheses cubed minus open parentheses 0 close parentheses squared plus c
> c equals 0`
> 
> `bold italic s (t)=2 bold italic t^4−4 bold italic t³−bold italic t²`
> 
> b) Find the displacement of the particle from the origin after the first five seconds of its motion.
> 
> > *To find the displacement after 5 seconds, integrate the velocity between 0 and 5*
> 
> `integral subscript 0 superscript 5 8 t cubed minus 12 t squared minus 2 t space d t
> open square brackets 2 t to the power of 4 minus 4 t cubed minus t squared close square brackets subscript 0 superscript 5 space
> equals space open square brackets 2 open parentheses 5 close parentheses to the power of 4 minus 4 open parentheses 5 close parentheses cubed minus open parentheses 5 close parentheses squared close square brackets minus open square brackets 2 open parentheses 0 close parentheses to the power of 4 minus 4 open parentheses 0 close parentheses cubed minus open parentheses 0 close parentheses squared close square brackets
> equals 725 minus 0`
> 
> $725m$
> 
> c) Explain why this value is not the same as the distance travelled during the first 5 seconds.
> 
> **Final answer:** ** **
> 
> **Final answer:** **When finding the displacement, any negative displacements are taken into account. e.g. 3m - 1m = 2m. When finding the distance, we are looking for the total of all the areas, ignoring their direction/sign. e.g. 3m + 1m = 4m. This function for velocity has some regions underneath the x-axis, and some regions above the x-axis between 0 and 5 seconds, so the displacement and distance covered in this time will be different.**
> 
> **Final answer:** ** **
