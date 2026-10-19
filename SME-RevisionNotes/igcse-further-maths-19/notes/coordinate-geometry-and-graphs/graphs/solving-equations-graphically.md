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

  - For example solving `straight f open parentheses x close parentheses equals k` for some constant $k$
  
    - On a graph of `y equals straight f open parentheses x close parentheses`, draw the line $y=k$
    - The solutions are the ***x-*****coordinates** of any points of intersection
  - Finding **roots** by seeing where a graph crosses the *x*-axis is a special case of this
  
    - The *x-*axis is the horizontal line with equation  $y=0$
- Sometimes it will be the line  $y=x$

  - Draw this on the graph of `y equals straight f open parentheses x close parentheses` to find the solution(s) of `straight f open parentheses x close parentheses equals x`
- But sometimes determining the line to draw will be **more challenging**

  - For example, 'By drawing an appropriate straight line on the graph of $y=3+2e^{-2x}$, estimate the root of the equation  `ln open parentheses x minus 3 close parentheses cubed equals negative 6 x`'
  - We need to **rewrite** the equation in the form  `straight g open parentheses x close parentheses equals 3 plus 2 straight e to the power of negative 2 x end exponent`, where `y equals straight g open parentheses x close parentheses` is the equation of a straight line
  - Take the **exponential** of both sides ('exp cancels log')
  
    - `open parentheses x minus 3 close parentheses cubed equals straight e to the power of negative 6 x end exponent`
  - Take the **cube root** of both sides
  
    - $x-3=e^{-2x}$
  - **Multiply** both sides by 2
  
    - $2x-6=2e^{-2x}$
  - **Add** 3 to both sides
  
    - $2x-3=3+2e^{-2x}$
  - That equation is **equivalent** to  `ln open parentheses x minus 3 close parentheses cubed equals negative 6 x`
  
    - it will have the same solutions
  - So we need to **draw the line**  $y=2x-3$  on the graph of  $y=3+2e^{-2x}$
  
    - the* ****x-*****coordinates** of the points of intersection will give the solution(s) for  $2x-3=3+2e^{-2x}$
    - But those are the **same** as the solution(s) for  `ln open parentheses x minus 3 close parentheses cubed equals negative 6 x`

> **Exam Hint**
> - Be extra careful when drawing graphs on 'estimate solutions by using a graph' questions
> 
>   - The accuracy of your answer will depend on the accuracy of your drawing
>   - Use a ruler for straight lines

> **Worked Example**
> A graph of  `y equals 2 to the power of open parentheses x over 3 plus 1 close parentheses end exponent minus 1`  in the interval  $0\leqx\leq6$  is shown in the following diagram
> 
> ![Graph of exponential function](assets/2d75892b9aeb-qb9hr5gw-picture1.png)
> 
> By drawing a suitable straight line on the grid, show that the equation  `log subscript 2 open parentheses 3 x minus 1 close parentheses squared minus 2 over 3 x equals 2`  has a root in the interval  $0\leqx\leq6$, and obtain an estimate for the value of that root.
> 
> > *Be careful here – we cannot just draw the horizontal line *$y=2$
> *That would only work if we had the graph of  *`y equals log subscript 2 open parentheses 3 x minus 1 close parentheses squared minus 2 over 3 x`
> 
> > *Instead we must work on rearranging the equation*
> *Start by getting the logarithm alone on the left-hand side*
> 
> `log subscript 2 open parentheses 3 x minus 1 close parentheses squared equals 2 over 3 x plus 2`
> 
> > *Use laws of logarithms to bring the power down in front of the logarithm*
> *Then divide both sides of the equation by 2*
> 
> `table row cell 2 log subscript 2 open parentheses 3 x minus 1 close parentheses end cell equals cell 2 over 3 x plus 2 end cell row cell log subscript 2 open parentheses 3 x minus 1 close parentheses end cell equals cell x over 3 plus 1 end cell end table`
> 
> > *Now take both sides to the power of 2*
> *This will cancel the logarithm on the left-hand side ('exp cancels log')*
> 
> `3 x minus 1 equals 2 to the power of open parentheses x over 3 plus 1 close parentheses end exponent`
> 
> > *Finally subtract 1 from both sides*
> 
> `3 x minus 2 equals 2 to the power of open parentheses x over 3 plus 1 close parentheses end exponent minus 1`
> 
> > *Now the right-hand side is the function that is graphed on the diagram*
> *So we need to draw the straight line  *$y=3x-2$
> *We can estimate the root by considering the **x-**coordinate of the point of intersection*
> 
> ![Solution graph for question](assets/276d6f8c5dc3-rvnd1ehm-picture2.png)
> 
> **Final answer:** **root:  **$x\approx1.2$
