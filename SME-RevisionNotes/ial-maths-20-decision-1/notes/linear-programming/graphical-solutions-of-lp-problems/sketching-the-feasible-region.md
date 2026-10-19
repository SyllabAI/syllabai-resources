---
note_id: "rn_BKy4QZDvr5H3dfcY"
title: "Sketching the Feasible Region"
source: https://www.savemyexams.com/international-a-level/maths/edexcel/20/decision-1/revision-notes/linear-programming/graphical-solutions-of-lp-problems/sketching-the-feasible-region
path: linear-programming/graphical-solutions-of-lp-problems/sketching-the-feasible-region
updated_at: "2026-07-02T08:19:38.480Z"
spec_point_ids: ["spcpt_PVmrngMBS34TZSnP", "spcpt_mdHSsJWn3V3wQv6v"]
spec_point_codes: []
guided_study: false
---

# Sketching the Feasible Region

## Introduction to Solving an LP Problem Graphically

> **Spec point** — `spcpt_PVmrngMBS34TZSnP`

## Introduction to Solving an LP Problem Graphically

### How do I solve a linear programming problem graphically?

- For problems with two decision variables

  - Plot the **constraints** (inequalities) accurately on a graph
  - This leads to the **feasible region**
  - The **optimal solution** will be one of the vertices of the feasible region
- In harder problems

  - There may be a **third** decision variable
  
    - There will be a connection to one (or both) of the other decision variables
    - **All** constraints can be rewritten in terms of just two of the decision variables
    - E.g. $x,y,z$ are the numbers of chairs, tables and desks made by a furniture manufacturer
    The number of desks produced is twice the number of tables, i.e. $z=2y$
  - The optimal solution may not give **integer** values for the decision variables but the **context** demands they are
  
    - E.g. Is it possible to make 3.65 chairs and 4.2 tables per day?

## Feasible Region

> **Spec point** — `spcpt_mdHSsJWn3V3wQv6v`

## Feasible Region

### What is the feasible region?

- The **feasible region** is the set of all values that satisfy **all** the **constraints** in a linear programming problem

  - In practice, this is the **area** on a **graph** that **satisfies** all of the **inequalities**
  
    - This includes the **non-negativity** inequality

### How do I find the feasible region?

- To find the **feasible region**

  - **Accurately** plot each **inequality** (constraint) on a **graph**
  
    - Plot each inequality as a **straight line**
    - Rearranging to the form $y\leqmx+c$ or $y\geqmx+c$ may help
    - It can be easier to determine two points that lie on each line, plot and join them up
    - Draw the line **solid** for inequalities involving ≤ or ≥, or **dotted** for inequalities involving > or <
    - < and > are rare in linear programming problems
  - **Shade** the part of the graph **not satisfied** by each inequality
  
    - It is easier to see a 'blank' area rather than an area shaded several times
  - The **feasible region** is the **area** on the **graph** left **unshaded**
  
    - It is the area that **satisfies all** of the **inequalities**
    - It is usually labelled with the capital letter $R$
- Label the line of each inequality around the edge of the graph

> **Exam Hint**
> - Exam questions will provide a graph for you to accurately plot the inequalities
> 
>   - Alternatively they may provide an accurate graph with some or all of the inequalities already plotted
> - It is helpful to complete the shading for each inequality as you add it to the graph
> 
>   - If you leave the shading to the end it can become confusing

> **Worked Example**
> A linear programming problem is formulated as
> 
> Maximise
> 
> $P=30x+40y$
> 
> subject to
> 
> `table row cell x plus y end cell less or equal than 10 row cell 3 x plus 2 y end cell less or equal than 24 row cell x plus 2 y end cell less or equal than 18 row cell x comma space y end cell greater or equal than 0 end table`
> 
> Show graphically the feasible region, $R$, of the linear programming problem.
> 
> **Answer:**
> 
> > *The objective function is not needed to plot the feasible region*
> 
> > *Plot each inequality as a straight line graph with the 'unwanted' side shaded*
> *For this problem, all lines will be solid lines*
> *The first constraint will be the line *$y=-x+10$* (gradient -1 and *$y$*-axis intercept 10)*
> *(You may find it easier to 'see' that points like (0, 10) and (10, 0) lie on the line, which you can plot and join up)*
> 
> ![feasible-1](assets/b3cfb7a125bc-feasible-1.png)
> 
> > *Plot and label the rest of the inequalities in the same way*
> 
> ![feasible-2](assets/e0194ce30b77-feasible-2.png)
> 
> > *Label the feasible region with *$R$
> 
> ![feasible-3-green](assets/c5726b3ac50b-feasible-3-green.png)
