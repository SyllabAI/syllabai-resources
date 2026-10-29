---
note_id: "rn_wJMXgDHv6sYnbCzS"
title: "Solving Equations Graphically"
source: https://www.savemyexams.com/igcse/further-maths/edexcel/19/revision-notes/coordinate-geometry-and-graphs/graphs/solving-equations-graphically
path: coordinate-geometry-and-graphs/graphs/solving-equations-graphically
updated_at: "2024-10-20T07:46:43.029Z"
spec_point_ids: ["spcpt_GrBVPqh2RRq5kQGY"]
spec_point_codes: []
guided_study: false
---

# Solving Equations Graphically

## Solving Equations Graphically

> **Spec point** — `spcpt_GrBVPqh2RRq5kQGY`

## Solving Equations Graphically

### How can I solve equations graphically?

- A **graph** can be used to to help solve an equation like $f(x)=g(x)$

  - **Draw the graphs** of $y=f(x)$ and $y=g(x)$
  - The **solutions** are the ***x*****-coordinates** of the points of **intersection**
- This can be used when an equation is difficult or impossible to solve **algebraically**

  - The solutions found will usually be **approximations** rather than exact answers
  - The more **accurate** the graph, the more accurate the approximation

### How can I estimate a solution by drawing a line on a graph?

- An exam question my ask you to **estimate a solution** by drawing a 'suitable' (or 'appropriate') **straight line** on a graph
- Often this will be a **horizontal** line

  - For example solving $\mathrm{f} ( x ) = k$ for some constant $k$
  
    - On a graph of $y = \mathrm{f} ( x )$, draw the line $y=k$
    - The solutions are the ***x-*****coordinates** of any points of intersection
  - Finding **roots** by seeing where a graph crosses the *x*-axis is a special case of this
  
    - The *x-*axis is the horizontal line with equation  $y=0$
- Sometimes it will be the line  $y=x$

  - Draw this on the graph of $y = \mathrm{f} ( x )$ to find the solution(s) of $\mathrm{f} ( x ) = x$
- But sometimes determining the line to draw will be **more challenging**

  - For example, 'By drawing an appropriate straight line on the graph of $y=3+2e^{-2x}$, estimate the root of the equation  $\ln ( x - 3 )^{3} = - 6 x$'
  - We need to **rewrite** the equation in the form  $\mathrm{g} ( x ) = 3 + 2 \mathrm{e}^{- 2 x}$, where $y = \mathrm{g} ( x )$ is the equation of a straight line
  - Take the **exponential** of both sides ('exp cancels log')
  
    - $( x - 3 )^{3} = \mathrm{e}^{- 6 x}$
  - Take the **cube root** of both sides
  
    - $x-3=e^{-2x}$
  - **Multiply** both sides by 2
  
    - $2x-6=2e^{-2x}$
  - **Add** 3 to both sides
  
    - $2x-3=3+2e^{-2x}$
  - That equation is **equivalent** to  $\ln ( x - 3 )^{3} = - 6 x$
  
    - it will have the same solutions
  - So we need to **draw the line**  $y=2x-3$  on the graph of  $y=3+2e^{-2x}$
  
    - the* ****x-*****coordinates** of the points of intersection will give the solution(s) for  $2x-3=3+2e^{-2x}$
    - But those are the **same** as the solution(s) for  $\ln ( x - 3 )^{3} = - 6 x$

> **Exam Hint**
> - Be extra careful when drawing graphs on 'estimate solutions by using a graph' questions
> 
>   - The accuracy of your answer will depend on the accuracy of your drawing
>   - Use a ruler for straight lines

> **Worked Example**
> A graph of  $y = 2^{( \frac{x}{3} + 1 )} - 1$  in the interval  $0\leqx\leq6$  is shown in the following diagram
> 
> ![Graph of exponential function](assets/2d75892b9aeb-qb9hr5gw-picture1.png)
> 
> By drawing a suitable straight line on the grid, show that the equation  $log_{2} ( 3 x - 1 )^{2} - \frac{2}{3} x = 2$  has a root in the interval  $0\leqx\leq6$, and obtain an estimate for the value of that root.
> 
> > *Be careful here – we cannot just draw the horizontal line* $y=2$
> *That would only work if we had the graph of* $y = log_{2} ( 3 x - 1 )^{2} - \frac{2}{3} x$
> 
> > *Instead we must work on rearranging the equation*
> *Start by getting the logarithm alone on the left-hand side*
> 
> $log_{2} ( 3 x - 1 )^{2} = \frac{2}{3} x + 2$
> 
> > *Use laws of logarithms to bring the power down in front of the logarithm*
> *Then divide both sides of the equation by 2*
> 
> $\begin{gathered} 2 log_{2} ( 3 x - 1 ) & = \frac{2}{3} x + 2 \\ log_{2} ( 3 x - 1 ) & = \frac{x}{3} + 1 \end{gathered}$
> 
> > *Now take both sides to the power of 2*
> *This will cancel the logarithm on the left-hand side ('exp cancels log')*
> 
> $3 x - 1 = 2^{( \frac{x}{3} + 1 )}$
> 
> > *Finally subtract 1 from both sides*
> 
> $3 x - 2 = 2^{( \frac{x}{3} + 1 )} - 1$
> 
> > *Now the right-hand side is the function that is graphed on the diagram*
> *So we need to draw the straight line* $y=3x-2$
> *We can estimate the root by considering the **x-**coordinate of the point of intersection*
> 
> ![Solution graph for question](assets/276d6f8c5dc3-rvnd1ehm-picture2.png)
> 
> **Final answer:** **root:  **$x\approx1.2$
