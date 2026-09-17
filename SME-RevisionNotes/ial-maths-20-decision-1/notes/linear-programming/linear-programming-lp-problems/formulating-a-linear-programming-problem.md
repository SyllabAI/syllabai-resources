---
note_id: "rn_cwNTzx84k6Dk6Wy8"
title: "Formulating a Linear Programming Problem"
source: https://www.savemyexams.com/international-a-level/maths/edexcel/20/decision-1/revision-notes/linear-programming/linear-programming-lp-problems/formulating-a-linear-programming-problem
path: linear-programming/linear-programming-lp-problems/formulating-a-linear-programming-problem
updated_at: "2026-07-02T08:19:38.468Z"
spec_point_ids: ["spcpt_54K9jGM5NpNxkjnW", "spcpt_b3g5Xvr72HJrHwrr", "spcpt_5M4cNk3PtSgwyT9F"]
spec_point_codes: []
guided_study: false
---

# Formulating a Linear Programming Problem

## Introduction to Linear Programming

> **Spec point** — `spcpt_54K9jGM5NpNxkjnW`

## Introduction to Linear Programming

### What is linear programming?

- **Linear programming,** often abbreviated to **LP,** is a means of solving problems that

  - involve working with a set of **constraints**
  - require a quantity to be **maximised** or **minimised**
- Typical uses of linear programming problems including finance and manufacturing

  - For example, a furniture manufacturer may make a mixture of chairs and tables
  
    - They would want to **minimise** their **costs** (of raw materials, manufacturing time)
    - They would want to **maximise** their **profit** (chairs may make more profit than tables)
    - They may have restrictions **(constraints)** such as build time and the amount of raw materials available

## Decision Variables in Linear Programming

> **Spec point** — `spcpt_b3g5Xvr72HJrHwrr`

## Decision Variables in Linear Programming

### What are decision variables?

- In a linear programming problem, **decision variables** are the quantities that can be **varied**

  - $x,y,z$ are usually used as the decision variables
  - E.g. A furniture manufacturer could produce $x$ chairs and $y$ tables per week
- Varying the **decision variables** will vary the quantity that is to be maximised or minimised

  - E.g. 12 chairs and 3 tables may lead to a profit of £200
  - or 3 chairs and 12 tables may lead to a profit of £160
- The values that the **decision variable** may take will depend upon the **constraints**

  - A furniture manufacturer can't make endless chairs and tables to gain unlimited profit!

### What is the objective function in a linear programming problem?

- The **objective function** is the quantity in a linear programming problem that requires **optimising**

  - The objective of a furniture manufacturer may be to **maximise** its **profits**
  - They may also wish to **minimise** their **costs**
- The objective function is the **aim** of a linear programming problem

  - It is a function of the **decision variables**
  - $P$ is usually used for **maximising** problems ($P$, profit)
  - $C$ is usually used for **minimising** problems ($C$, costs)

## Constraints & Inequalities in Linear Programming

> **Spec point** — `spcpt_5M4cNk3PtSgwyT9F`

## Constraints & Inequalities in Linear Programming

### What are constraints in linear programming?

- The **constraints** in a linear programming problem are the **restrictions** the problem is contained within

  - Mathematically, constraints are represented by **inequalities** involving the** decision variables**
  - E.g. Constraints for a furniture manufacturer could include glue drying time or the amount of paint available
- Decision variables are usually zero or positive as they represent a 'number of things'

  - The constraint $x,y\geq0$ is usually included
  - This is called the **non-negativity** constraint

### How do I formulate a linear programming problem?

- Formulating a linear programming problems involves

  - Defining the **decision variables**
  - Deducing the **constraints** as inequalities
  - Determining the **objective function**
  - Writing the problem out formally

- **STEP 1**
**Define** the **decision variables**

  - Read the question carefully to gather what quantities can be varied
  - Typically these will be a 'number of things'

- **STEP 2**
Write each **constraint** (given in words) as a mathematical **inequality**

  - Where possible, inequalities should be simplified, e.g.  $2x+4y\leq8$ simplifies to $x+2y\leq4$
  - Each inequality will be in terms of the decision variables

- **STEP 3**
Determine the **objective function**

  - This will be the quantity that is required to be maximised or minimised
  - Typically this would be maximising profit or minimising costs

- **STEP 4**
Formulate the** linear programming problem** by writing it in a formal manner

  - This is of the form
  Maximise
       <objective function>
  subject to
       <constraints>
  - Include the non-negativity constraint, e.g.  $x,y\geq0$

> **Exam Hint**
> - When writing a formal linear programming problem
> 
>   - whether specified or not, and where appropriate, always include the **non-negativity constraint**
>   - $x,y\geq0$

> **Worked Example**
> A furniture manufacturer makes chairs and tables.
> 
> Due to the availability of quality timber, on any particular day the manufacturer cannot make more than a total of 10 chairs and tables.
> 
> A chair takes an hour to produce whilst a table takes 2 hours to produce.  The manufacturer's factory can produce items for a maximum of 18 hours per day.
> 
> The varnish on a chair takes 3 hours to dry whilst the varnish on a table takes 2 hours to dry.  There are four drying zones within the factory, each able to provide 6 hours of drying time per day.
> 
> The manufacturer makes £30 profit on each chair it produces in a day, and £40 profit on each table.  The manufacturer wants to maximise its daily profit.
> 
> Formulate the above as a linear programming problem, defining the decision variables, stating the objective function and listing the constraints.
> 
> **Answer:**
> 
> - *STEP 1*
> *Define the decision variables*
> *The 'things' that can be varied here are the number of chairs and the number of tables that are made per day*
> 
> *Let *$x$* be the number of chairs made by the furniture manufacturer per day*
> *Let *$y$* be the number of tables made by the furniture manufacturer per day*
> 
> - *STEP 2*
> *Write each constraint (given in words) as an inequality*
> *The first constraint is the total amount of chairs and tables able to be made in a day*
> 
> $x+y\leq10$
> 
> > *The second constraint is the production time*
> *Chairs take one hour, tables take two with a maximum of 18 hours available per day*
> 
> $x+2y\leq18$
> 
> > *The third constraint is the varnish drying time*
> *This is 3 hours for a chair, 2 hours for a table*
> *The maximum drying time per day available is 4 x 6 = 24 hours*
> 
> $3x+2y\leq24$
> 
> - *STEP 3*
> *Determine the objective function*
> *Profit is to be maximised*
> 
> $P=30x+40y$
> 
> - *STEP 4*
> *Formulate the linear programming problem by writing it in a formal manner, including the non-negativity constraint*
> 
> **Final answer:** **Maximise                              **
> 
> $P=30x+40y$
> 
> **Final answer:** **subject to                              **
> 
> `table row cell bold italic x bold plus bold italic y end cell bold less or equal than bold 10 row cell bold italic x bold plus bold 2 bold italic y end cell bold less or equal than bold 18 row cell bold 3 bold italic x bold plus bold 2 bold italic y end cell bold less or equal than bold 24 row cell bold italic x bold comma bold space bold italic y end cell bold greater or equal than bold 0 end table`
