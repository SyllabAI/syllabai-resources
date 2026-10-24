---
note_id: "rn_JTYRqf9MZSrGbnFj"
title: "Transforming Relationships to Linear Form"
source: https://www.savemyexams.com/igcse/further-maths/cie/additional-maths/25/revision-notes/algebra-and-functions/logarithmic-and-exponential-functions/transfoming-relationships-to-linear-form
path: algebra-and-functions/logarithmic-and-exponential-functions/transfoming-relationships-to-linear-form
updated_at: "2026-07-02T08:19:38.509Z"
spec_point_ids: ["spcpt_kQPdXBwRV3szcFmZ", "spcpt_tHJZ5mFPV6tSzr2w"]
spec_point_codes: []
guided_study: false
---

# Transforming Relationships to Linear Form

## Transforming Relationships in the Form y=ax^n

> **Spec point** — `spcpt_kQPdXBwRV3szcFmZ`

## Transforming relationships in the form y=ax^n

### How do I use logarithms to linearise a graph in the form y = ax<sup>n</sup>?

- Logarithms can be used to linearise graphs of **power functions**
- Suppose $y=ax^{n}$

  - You can take logarithms of both sides
  
    - $\mathrm{ln}y=\mathrm{ln}(ax^{n})$
  - You can split the right hand side into the sum of two logarithms
  
    - $\mathrm{ln}y=\mathrm{ln}a+\mathrm{ln}(x^{n})$
  - You can bring down the power in the final term
  
    - $\mathrm{ln}y=\mathrm{ln}a+n\mathrm{ln}x$
- $\mathrm{ln}y=\mathrm{ln}a+n\mathrm{ln}x$ is in linear form $Y=mX+c$

  - $Y=\mathrm{ln}y$
  - $X=\mathrm{ln}x$
  - $m=n$
  - $c=\mathrm{ln}a$

### How can I use linearised form to find the unknown constants?

- After linearising the function it will be in the form $\mathrm{ln}y=\mathrm{ln}a+n\mathrm{ln}x$

  - $n$ is the gradient of the straight line graph
  - $\mathrm{ln}a$ is the $y$-intercept of the straight line graph
- Once you know the value of the gradient of the straight line graph this is the value of $n$
- You will need to find the value of $a$ by solving the equation $\mathrm{ln}a=c$

> **Exam Hint**
> - You may need to leave your answer in exact form, especially in the non-calculator paper
> 
>   - e.g. to solve ln *a *= 2 the answer will be *a *= e<sup>2</sup>

> **Worked Example**
> The heights, $h$ metres, and the amount of time spent sleeping, $t$ hours, of a group of young giraffes can be modelled using $t=ah^{b}$, where $a$ and $b$ are constants.
> 
> The graph of $\mathrm{ln}t$ against $\mathrm{ln}h$ is a straight line passing through the points (1, -0.9) and (4, -4.5).
> 
> Find the values of $a$ and $b$, giving your answers in exact form.
> 
> > *Find the gradient of the straight line between the two coordinates.*
> 
> $m=\frac{-4.5--0.9}{4-1}=-\frac{3.6}{3}=-1.2$
> 
> > *Substitute *$m=-1.2$*, *$x=\mathrm{ln}h$* and *$y=\mathrm{ln}t$* into the equation of a straight line (*$y=mx+c$*).*
> 
> > $\mathrm{ln}t=-1.2\mathrm{ln}h+c$* *
> 
> > *Substitute either coordinate in and rearrange to find *$c$*.*
> 
> $\begin{gathered} - 0.9 & = - 1.2 ( 1 ) + c \\ c & = - 0.9 + 1.2 \\ c & = 0.3 \end{gathered}$
> 
> > *Compare this to the linearised form of *$t=ah^{b}$*. Take logarithms of both sides first and rearrange if you can't remember the correct form. *
> 
> > $\ln t = \ln ( a h^{b} )
> \ln t = \ln a + b \ln h$* *
> 
> > *So *$b$* is the value in front of *$\mathrm{ln}h$* and *$\mathrm{ln}a=0.3$*. Solve *$\mathrm{ln}a=0.3$* by taking *$e$* of both sides.*
> 
> $\begin{gathered} \ln a & = 0.3 \\ \mathrm{e}^{\ln a } & = \mathrm{e}^{0.3} \\ a & = \mathrm{e}^{0.3} \end{gathered}$
> 
> $a=e^{0.3},b=-1.2$

## Transforming Relationships in the Form y=Ab^x

> **Spec point** — `spcpt_tHJZ5mFPV6tSzr2w`

## Transforming relationships in the form y=Ab^x

### How do I use logarithms to linearise a graph in the form y = A(b<sup>x</sup>)?

- Logarithms can be used to linearise graphs of **exponential functions**
- Suppose $y=Ab^{x}$

  - You can take logarithms of both sides
  
    - $\mathrm{log}y=\mathrm{log}(Ab^{x})$
  - You can split the right hand side into the sum of two logarithms
  
    - $\mathrm{log}y=\mathrm{log}A+\mathrm{log}(b^{x})$
  - You can bring down the power in the final term
  
    - $\mathrm{log}y=\mathrm{log}A+x\mathrm{log}b$
- $\mathrm{log}y=\mathrm{log}A+x\mathrm{log}b$ is in linear form $Y=mX+c$

  - $Y=\mathrm{log}y$
  - $X=x$
  - $m=\mathrm{log}b$
  - $c=\mathrm{log}A$

### How can I use linearised form to find the unknown constants?

- After linearising the function it will be in the form $\mathrm{log}y=\mathrm{log}A+x\mathrm{log}b$

  - $\mathrm{log}b$ is the gradient of the straight line graph $( m )$
  - $\mathrm{log}A$ is the $y$-intercept of the straight line graph $( c )$
- You will need to find the value of $A$ by solving the equation $\mathrm{log}A=c$

  - The value of $c$ will either be given or will need to be found
- You will need to find the value of $b$ by solving the equation $\mathrm{log}b=m$

  - The value of $m$ will either be given or will need to be found

> **Exam Hint**
> - Unless the question specifies, you can choose whether to use ln, lg or log
> - Remember you will need to solve the equation at the end
> 
>   - If using lg, solve by taking 10 to the power of each side
>   - If using ln, solve by taking e to the power of each side

> **Worked Example**
> Variables $x$ and $y$ are such that when $\mathrm{lg}y$ is plotted against $x$, a straight line passing through the points $(2,5)$ and $(5,8)$ is obtained.
> 
> Show that $y=A\timesb^{x}$ where $A$ and $b$are constants to be found.
> 
> > *Find the gradient of the straight line between the two coordinates.*
> 
> $m=\frac{8-5}{5-2}=\frac{3}{3}=1$
> 
> > *Substitute *$m=1$*, *$X=x$* and *$Y=\mathrm{lg}y$* into the equation of a straight line (*$Y=mX+c$*).*
> 
> > $\mathrm{lg}y=x+c$* *
> 
> > *Substitute either coordinate in and rearrange to find *$c$*.*
> 
> $\begin{gathered} 5 & = 2 + c \\ c & = 3 \end{gathered}$
> 
> $\mathrm{lg}y=x+3$
> 
> > *Linearise *$y=A\timesb^{x}$*.*
> * Take logarithms of both sides first and rearrange if you can't remember the correct form.  Take logarithms of both sides. *
> 
> > $lg y = lg ( A b^{x} )$* *
> 
> > *Split the right-hand side into the sum of two logarithms.*
> 
> $\mathrm{lg}y=\mathrm{lg}A+\mathrm{lg}b^{x}$
> 
> > *Bring down the power in the final term. *
> 
> $\mathrm{lg}y=\mathrm{lg}A+x\mathrm{lg}b$
> 
> > *Compare this to the equation of the line.*
> 
> > $\mathrm{lg}b=1$* and *$\mathrm{lg}A=3$* *
> 
> > *Solve *$\mathrm{lg}b=1$* by raising 10 to the power of both sides.*
> 
> $\begin{gathered} \text{lg} b & = 1 \\ 10^{lg b} & = 10^{1} \\ b & = 10 \end{gathered}$
> 
> > *Solve *$\mathrm{lg}A=3$* by raising 10 to the power of both sides.*
> 
> $\begin{gathered} \text{lg} A & = 3 \\ 10^{lg A} & = 10^{3} \\ A & = 1000 \end{gathered}$
> 
> $y=1000\times10^{x}$
