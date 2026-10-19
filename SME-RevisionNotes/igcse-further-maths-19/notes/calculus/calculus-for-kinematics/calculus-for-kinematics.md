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
> > *Note that this 'powers of *$t$*' derivative works exactly the same way as a 'powers of *$x$*' derivative! *
> 
> `table row v equals cell fraction numerator straight d s over denominator straight d t end fraction end cell row blank equals cell 2 open parentheses 3 t to the power of 3 minus 1 end exponent close parentheses minus 18 open parentheses 2 t to the power of 2 minus 1 end exponent close parentheses plus 48 end cell end table`
> 
> $v(t)=6t^{2}-36t+48$
> 
> > *Now differentiate the velocity to find the acceleration.*
> 
> `table attributes columnalign right center left columnspacing 0px end attributes row a equals cell fraction numerator straight d v over denominator straight d t end fraction end cell row blank equals cell 6 open parentheses 2 t to the power of 2 minus 1 end exponent close parentheses minus 36 end cell end table`
> 
> $a(t)=12t-36$
> 
> (b) Find the time(s) at which the particle is instantaneously at rest.
> 
> > *'Instantaneously at rest' means that the velocity is zero*
> 
> > *So solve *`v open parentheses t close parentheses equals 0`* for *$t$
> 
> `table attributes columnalign right center left columnspacing 0px end attributes row cell 6 t squared minus 36 t plus 48 end cell equals 0 row cell 6 open parentheses t squared minus 6 t plus 8 close parentheses end cell equals 0 row cell t squared minus 6 t plus 8 end cell equals 0 row cell open parentheses t minus 2 close parentheses open parentheses t minus 4 close parentheses end cell equals 0 end table`
> $t=2\mathrm{or}t=4$
> 
> **Final answer:** **The particle is at rest at **$t=2$** ****seconds and at **$t=4$** seconds**
> 
> (c) Find the minimum velocity of the particle.
> 
> > *First of all note that this is a different question from 'find the minimum **speed **of the particle'*
> *The answer to that would be zero, at the times found in part (b)!*
> 
> > *The graph of  *`v open parentheses t close parentheses equals 6 t squared minus 36 t plus 48`*  is a 'u-shaped' parabola*
> 
> > *So we know there is going to be a single minimum point*
> 
> > *That minimum point will occur when *$\frac{dv}{dt}=0$
> 
> > *So start by solving  *$a=\frac{dv}{dt}=0$*  for *$t$
> 
> `table row cell 12 t minus 36 end cell equals 0 row cell 12 t end cell equals 36 row t equals 3 end table`
> 
> > *So the minimum velocity occurs when *$t=3$
> 
> > *(Note that, by the symmetry of quadratic graphs, that's halfway between the *$t$* values found in part (b)!)*
> 
> > *Substitute *$t=3$* into *`v open parentheses t close parentheses`* to find the velocity at that time*
> 
> > `table row cell v open parentheses 3 close parentheses end cell equals cell 6 open parentheses 3 close parentheses squared minus 36 open parentheses 3 close parentheses plus 48 end cell row blank equals cell 54 minus 108 plus 48 end cell row blank equals cell negative 6 end cell end table`* *
> 
> **Final answer:** **Minimum velocity **$=-6m/s$** **

## Integration for Kinematics

> **Spec point** — `spcpt_zXdKYDbwn48sk8Fm`

## Integration for Kinematics

### How is integration used in kinematics?

- Since **velocity** is the **derivative** of **displacement** ($v=\frac{ds}{dt}$) it follows that

  - `space s equals integral v space straight d t`
  
    - Integrate velocity to find displacement

- Similarly, since **acceleration** is the **derivative** of **velocity **($a=\frac{dv}{dt}$)

  - `space v equals integral a space straight d t`
  
    - Integrate acceleration to find velocity

### How can I find the constant of integration in kinematics problems?

- Without further information **integration** can only find $s$ or $v$ 'up to a **constant of integration**'

  - i.e.  `integral v open parentheses t close parentheses space straight d t equals s open parentheses t close parentheses plus c`
  - and  `integral a open parentheses t close parentheses space straight d t equals v open parentheses t close parentheses plus c`
- To find the value of $c$ we need **additional information**

  - Usually this will be the **value** of $s$ or $v$ at a **particular time** $t$
- Look out for the words **“initial”** or **“initially”**

  - This refers to time  $t=0$
- **Substitute** the known values into your integration answers for `s open parentheses t close parentheses` or `v open parentheses t close parentheses`

  - and solve for $c$

> **Exam Hint**
> - Read the question closely to spot any given values at particular times
> 
>   - These allow you to find the constant of integration
>   - Remember that 'initially' means $t=0$

> **Worked Example**
> A particle $P$ is moving along the $x$-axis.
> 
> At time $t$ seconds ($t\geq0$) the velocity, $vm/s$, of $P$ is given by  `v open parentheses t close parentheses equals 6 t squared minus t plus 3`.
> 
> When $t=0$, the displacement of $P$ from the origin is  $-5m$.
> 
> Find the displacement of $P$ from the origin when  $t=4$.
> 
> > *Start by integrating the velocity to find an expression for the displacement*
> 
> > *Note that this 'powers of *$t$*' integral works exactly the same as a 'powers of *$x$*' integral*
> 
> > *Don't forget the constant of integration!*
> 
> `table row cell s open parentheses t close parentheses end cell equals cell integral open parentheses 6 t squared minus t plus 3 close parentheses space straight d t end cell row blank equals cell 6 open parentheses fraction numerator t to the power of 2 plus 1 end exponent over denominator 2 plus 1 end fraction close parentheses minus open parentheses fraction numerator t to the power of 1 plus 1 end exponent over denominator 1 plus 1 end fraction close parentheses plus 3 t plus c end cell row blank equals cell 2 t cubed minus 1 half t squared plus 3 t plus c end cell end table`
> 
> > *We know that when *$t=0$*,  the displacement is  *$-5$
> 
> > *Substitute these values in and solve for *$c$
> 
> `table row cell s open parentheses 0 close parentheses end cell equals cell negative 5 end cell row cell 2 open parentheses 0 close parentheses cubed minus 1 half open parentheses 0 close parentheses squared plus 3 open parentheses 0 close parentheses plus c end cell equals cell negative 5 end cell row cell 0 plus c end cell equals cell negative 5 end cell row c equals cell negative 5 end cell end table`
> 
> > *Now we have a precise expression for *`s open parentheses t close parentheses`
> 
> `s open parentheses t close parentheses equals 2 t cubed minus 1 half t squared plus 3 t minus 5`
> 
> > *Substitute in  *$t=4$*  to find the displacement at that time*
> 
> `table attributes columnalign right center left columnspacing 0px end attributes row cell s open parentheses 4 close parentheses end cell equals cell 2 open parentheses 4 close parentheses cubed minus 1 half open parentheses 4 close parentheses squared plus 3 open parentheses 4 close parentheses minus 5 end cell row blank equals cell 128 minus 8 plus 12 minus 5 end cell row blank equals 127 end table`
> 
> **Final answer:** **Displacement **$=127m$
