---
note_id: "rn_scDmfMTdqPpjQsW3"
title: "Calculus for Kinematics"
source: https://www.savemyexams.com/igcse/further-maths/edexcel/19/revision-notes/calculus/calculus-for-kinematics/calculus-for-kinematics
path: calculus/calculus-for-kinematics/calculus-for-kinematics
updated_at: "2024-10-20T15:52:44.111Z"
spec_point_ids: ["spcpt_VSCsG2N5Dv92vpKZ", "spcpt_zXdKYDbwn48sk8Fm"]
spec_point_codes: []
guided_study: false
---

# Calculus for Kinematics

## Differentiation for Kinematics

> **Spec point** — `spcpt_VSCsG2N5Dv92vpKZ`

## Differentiation for Kinematics

### How is differentiation used in kinematics?

- **Displacement**, **velocity** and **acceleration** are related by calculus
- In terms of differentiation and derivatives

  - **velocity** is the **rate** of **change** of **displacement**
  
    - $v=\frac{ds}{dt}$  (differentiate displacement to get velocity)
  - **acceleration** is the **rate** of **change** of **velocity**
  
    - $a=\frac{dv}{dt}$  (differentiate velocity to get acceleration)
  - so **acceleration** is also the **second** **derivative** of **displacement**
  
    - $a=\frac{d^{2}s}{dt^{2}}$  (differentiate displacement twice to get acceleration)
- On a **graph** this means that

  - **velocity** is the **gradient** on a **displacement-time** graph
  - **acceleration** is the **gradient** on a **velocity-time)** graph
- You can also use this to find **(local) minimum** **and maximum** values

  - Exactly the **same** as using **calculus** to find other minimum and maximum values
  - e.g. to find any local minimum or maximum values for **velocity**
  
    - look for times $t$ at which  $\frac{dv}{dt}=0$

> **Worked Example**
> The displacement, $s$ metres, of a particle at time $t$ seconds, is modelled by  $s(t)=2t^{3}-18t^{2}+48t$,  $t\geq0$.
> 
> (a) Find expressions in terms of $t$ for the velocity and acceleration of the particle.
> 
> > *Differentiate the displacement to find the velocity*
> 
> > *Note that this 'powers of* $t$*' derivative works exactly the same way as a 'powers of* $x$*' derivative!*
> 
> $\begin{gathered} v = \frac{ \mathrm{d} s}{ \mathrm{d} t} \\ = 2 ( 3 t^{3 - 1} ) - 18 ( 2 t^{2 - 1} ) + 48 \end{gathered}$
> 
> $v(t)=6t^{2}-36t+48$
> 
> > *Now differentiate the velocity to find the acceleration.*
> 
> $\begin{array}{rcl} a = \frac{ \mathrm{d} v}{ \mathrm{d} t} \\ = 6 ( 2 t^{2 - 1} ) - 36 \end{array}$
> 
> $a(t)=12t-36$
> 
> (b) Find the time(s) at which the particle is instantaneously at rest.
> 
> > *'Instantaneously at rest' means that the velocity is zero*
> 
> > *So solve* $v ( t ) = 0$ *for* $t$
> 
> $\begin{array}{rcl} 6 t^{2} - 36 t + 48 & = 0 \\ 6 ( t^{2} - 6 t + 8 ) & = 0 \\ t^{2} - 6 t + 8 & = 0 \\ ( t - 2 ) ( t - 4 ) & = 0 \end{array}$
> $t=2\mathrm{or}t=4$
> 
> **Final answer:** **The particle is at rest at **$t=2$** ****seconds and at **$t=4$** seconds**
> 
> (c) Find the minimum velocity of the particle.
> 
> > *First of all note that this is a different question from 'find the minimum **speed **of the particle'*
> *The answer to that would be zero, at the times found in part (b)!*
> 
> > *The graph of* $v ( t ) = 6 t^{2} - 36 t + 48$ *is a 'u-shaped' parabola*
> 
> > *So we know there is going to be a single minimum point*
> 
> > *That minimum point will occur when* $\frac{dv}{dt}=0$
> 
> > *So start by solving* $a=\frac{dv}{dt}=0$ *for* $t$
> 
> $\begin{gathered} 12 t - 36 & = 0 \\ 12 t & = 36 \\ t = 3 \end{gathered}$
> 
> > *So the minimum velocity occurs when* $t=3$
> 
> > *(Note that, by the symmetry of quadratic graphs, that's halfway between the* $t$ *values found in part (b)!)*
> 
> > *Substitute* $t=3$ *into* $v ( t )$ *to find the velocity at that time*
> 
> > $\begin{gathered} v ( 3 ) & = 6 ( 3 )^{2} - 36 ( 3 ) + 48 \\ = 54 - 108 + 48 \\ = - 6 \end{gathered}$* *
> 
> **Final answer:** **Minimum velocity **$=-6m/s$** **

## Integration for Kinematics

> **Spec point** — `spcpt_zXdKYDbwn48sk8Fm`

## Integration for Kinematics

### How is integration used in kinematics?

- Since **velocity** is the **derivative** of **displacement** ($v=\frac{ds}{dt}$) it follows that

  - $s = \int v \mathrm{d} t$
  
    - Integrate velocity to find displacement

- Similarly, since **acceleration** is the **derivative** of **velocity **($a=\frac{dv}{dt}$)

  - $v = \int a \mathrm{d} t$
  
    - Integrate acceleration to find velocity

### How can I find the constant of integration in kinematics problems?

- Without further information **integration** can only find $s$ or $v$ 'up to a **constant of integration**'

  - i.e.  $\int v ( t ) \mathrm{d} t = s ( t ) + c$
  - and  $\int a ( t ) \mathrm{d} t = v ( t ) + c$
- To find the value of $c$ we need **additional information**

  - Usually this will be the **value** of $s$ or $v$ at a **particular time** $t$
- Look out for the words **“initial”** or **“initially”**

  - This refers to time  $t=0$
- **Substitute** the known values into your integration answers for $s ( t )$ or $v ( t )$

  - and solve for $c$

> **Exam Hint**
> - Read the question closely to spot any given values at particular times
> 
>   - These allow you to find the constant of integration
>   - Remember that 'initially' means $t=0$

> **Worked Example**
> A particle $P$ is moving along the $x$-axis.
> 
> At time $t$ seconds ($t\geq0$) the velocity, $vm/s$, of $P$ is given by  $v ( t ) = 6 t^{2} - t + 3$.
> 
> When $t=0$, the displacement of $P$ from the origin is  $-5m$.
> 
> Find the displacement of $P$ from the origin when  $t=4$.
> 
> > *Start by integrating the velocity to find an expression for the displacement*
> 
> > *Note that this 'powers of* $t$*' integral works exactly the same as a 'powers of* $x$*' integral*
> 
> > *Don't forget the constant of integration!*
> 
> $\begin{gathered} s ( t ) & = \int ( 6 t^{2} - t + 3 ) \mathrm{d} t \\ = 6 ( \frac{t^{2 + 1} }{2 + 1} ) - ( \frac{t^{1 + 1} }{1 + 1} ) + 3 t + c \\ = 2 t^{3} - 1 \frac{1}{2} t^{2} + 3 t + c \end{gathered}$
> 
> > *We know that when* $t=0$*,  the displacement is* $-5$
> 
> > *Substitute these values in and solve for* $c$
> 
> $\begin{gathered} s ( 0 ) & = - 5 \\ 2 ( 0 )^{3} - 1 \frac{1}{2} ( 0 )^{2} + 3 ( 0 ) + c & = - 5 \\ 0 + c & = - 5 \\ c = - 5 \end{gathered}$
> 
> > *Now we have a precise expression for* $s ( t )$
> 
> $s ( t ) = 2 t^{3} - 1 \frac{1}{2} t^{2} + 3 t - 5$
> 
> > *Substitute in* $t=4$ *to find the displacement at that time*
> 
> $\begin{array}{rcl} s ( 4 ) & = 2 ( 4 )^{3} - 1 \frac{1}{2} ( 4 )^{2} + 3 ( 4 ) - 5 \\ = 128 - 8 + 12 - 5 \\ = 127 \end{array}$
> 
> **Final answer:** **Displacement **$=127m$
