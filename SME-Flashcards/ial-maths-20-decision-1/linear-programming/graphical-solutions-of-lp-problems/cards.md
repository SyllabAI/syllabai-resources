# Graphical Solutions of LP Problems

Course: ial-maths-20-decision-1 · Section: Linear Programming

Source: https://www.savemyexams.com/international-a-level/maths/edexcel/20/decision-1/flashcards/linear-programming/graphical-solutions-of-lp-problems/


## Card 1 — keyword_definition (`fl_7TJsk7g5Vg42KyBk`)

**FRONT**

Define the **feasible region** of a linear programming problem.


**BACK**

The feasible region is the set of all points that satisfy **every** constraint of the problem at the same time, including the non-negativity constraint.

On a graph it appears as an area, and it is usually labelled $R$.


Spec links: `spcpt_mdHSsJWn3V3wQv6v`


## Card 2 — true_or_false (`fl_tt2gz5sFw2hqx95h`)

**FRONT**

**True or False?**

On a completed linear programming graph, the feasible region is the area left unshaded.


**BACK**

**True.**

The convention is to shade the side of each line that **does not** satisfy its inequality, so the unwanted parts of the graph are covered over.

With several constraints this leaves the feasible region as the one area with no shading on it, which is far easier to pick out than an area shaded several times over.


Spec links: `spcpt_mdHSsJWn3V3wQv6v`


## Card 3 — fill_in_the_blanks (`fl_Gh7XZpFznqKV592W`)

**FRONT**

Complete the rule for the type of line used when a constraint is plotted:

A constraint written with $\leq$ or $\geq$ is drawn as a `\_\_\_\_\_\_` line, and one written with $<$ or $>$ is drawn as a `\_\_\_\_\_\_` line.


**BACK**

The completed rule is:

A constraint written with $\leq$ or $\geq$ is drawn as a **solid** line, and one written with $<$ or $>$ is drawn as a **dotted** line.

A solid line shows that the points on the line itself satisfy the constraint, so they belong to the feasible region. Strict inequalities are rare in linear programming.


*Blanks: 0 — answers: ['solid', 'dotted']*

Spec links: `spcpt_mdHSsJWn3V3wQv6v`

Flags: blank_answer_mismatch


## Card 4 — question_and_answer (`fl_7WtgtSBr7JKKYZzj`)

**FRONT**

What is the first thing you must do with a constraint such as $3 x + 2 y \leq 24$ before it can be drawn?


**BACK**

Replace the inequality sign with an equals sign, so that the constraint becomes the straight line $3 x + 2 y = 24$.

The easiest way to plot it is usually to find where it crosses the axes, at $( 0 , 12 )$ and $( 8 , 0 )$, and join those two points; rearranging into the form $y = m x + c$ is an alternative.


Spec links: `spcpt_mdHSsJWn3V3wQv6v`


## Card 5 — question_and_answer (`fl_9sqKHGdJs6nChx2X`)

**FRONT**

A problem has three decision variables $x$, $y$ and $z$, where $z = 2 y$. How can it still be solved graphically?


**BACK**

Use $z = 2 y$ to replace $z$ everywhere, so that every constraint and the objective function are written in terms of $x$ and $y$ only.

A graphical solution needs exactly **two** variables, one for each axis, so a third is workable only when it is tied to the others by a relationship like this.


Spec links: `spcpt_PVmrngMBS34TZSnP`


## Card 6 — question_and_answer (`fl_kq4zqjgYB5JfY27n`)

**FRONT**

A problem has constraints $x + y \leq 10$, $3 x + 2 y \leq 24$ and $x + 2 y \leq 18$. Does the point $( 6 , 4 )$ lie in the feasible region?


**BACK**

The point $( 6 , 4 )$ does **not** lie in the feasible region.

It satisfies $x + y \leq 10$ and $x + 2 y \leq 18$, but `3 \left(6\right) + 2 \left(4\right) = 26`, which is greater than 24.


Spec links: `spcpt_mdHSsJWn3V3wQv6v`


## Card 7 — fill_in_the_blanks (`fl_MfG5RYMMTV4QX4DF`)

**FRONT**

Complete the fact that the objective line method and the vertex method both rely on:

The optimal solution of a linear programming problem always lies at a `\_\_\_\_\_\_` of the feasible region.


**BACK**

The completed fact is:

The optimal solution of a linear programming problem always lies at a **vertex** (corner) of the feasible region.

Because the objective function is linear, its value improves steadily in one direction across the region, so the best value is reached at a corner rather than at a point inside.


*Blanks: 0 — answers: ['vertex']*

Spec links: `spcpt_r9mzkqH5CfKCjppT` `spcpt_QNpRGQHvyfTQgDXj`

Flags: blank_answer_mismatch


## Card 8 — keyword_definition (`fl_2xtYWdCwdpP7TnF5`)

**FRONT**

Define the **objective line** of a linear programming problem.


**BACK**

The objective line is the straight line obtained by fixing the objective function $P = a x + b y$ at one chosen value of $P$.

Rearranged, $P = a x + b y$ takes the form $y = m x + c$, so each value of $P$ gives one straight line that can be drawn on the graph.


Spec links: `spcpt_r9mzkqH5CfKCjppT`


## Card 9 — question_and_answer (`fl_WJCKpqfZPDDt8Hpk`)

**FRONT**

The objective function is $P = 30 x + 40 y$. What kind of value of $P$ should you pick in order to plot the first objective line easily?


**BACK**

Pick a value that is a **multiple of both 30 and 40**, such as $120$.

The line $120 = 30 x + 40 y$ then passes through $( 0 , 3 )$ and $( 4 , 0 )$, two points with whole-number coordinates that can be plotted and joined straight away.


Spec links: `spcpt_r9mzkqH5CfKCjppT`


## Card 10 — question_and_answer (`fl_vJhVsQ3bXDHrF3rs`)

**FRONT**

In a maximising problem, which way do you slide the ruler, and which vertex gives the optimal solution?


**BACK**

Slide the ruler **away from the origin**, keeping it parallel to the objective line already drawn.

The **last** vertex of the feasible region the ruler passes through is the optimal solution.

In a minimising problem you slide it **towards** the origin instead.


Spec links: `spcpt_r9mzkqH5CfKCjppT`


## Card 11 — true_or_false (`fl_5wk3YGXQsCpYP6cr`)

**FRONT**

**True or False?**

Objective lines drawn for two different values of $P$ have different gradients.


**BACK**

**False.**

Rearranging $P = a x + b y$ gives $y = - \frac{a}{b} x + \frac{P}{b}$, so the value of $P$ affects only the **intercept**.

Every objective line for the same problem therefore has the same gradient, which is exactly why the ruler can be slid across the graph while being kept parallel.


Spec links: `spcpt_r9mzkqH5CfKCjppT`


## Card 12 — question_and_answer (`fl_GXCKYzCtJXSXZgNf`)

**FRONT**

What is the first thing the vertex method requires you to do?


**BACK**

Find the **coordinates of every vertex** of the feasible region.

Some can be read straight off an accurate graph, and obvious ones, such as the origin or a point sitting on an axis, can be written down directly.


Spec links: `spcpt_QNpRGQHvyfTQgDXj`


## Card 13 — question_and_answer (`fl_4pDnHR533KJN59Ck`)

**FRONT**

Two constraints of a problem are $x + y \leq 8$ and $x + 4 y \leq 17$. How do you find the coordinates of the vertex where they meet?


**BACK**

Solve them as **simultaneous equations**, with each inequality sign replaced by an equals sign: $x + y = 8$ and $x + 4 y = 17$.

This gives $x = 5$ and $y = 3$, so the vertex is at $( 5 , 3 )$.


Spec links: `spcpt_QNpRGQHvyfTQgDXj`


## Card 14 — question_and_answer (`fl_B839DQzcG3wrnBCg`)

**FRONT**

Once you have the coordinates of every vertex, how does the vertex method finish?


**BACK**

Substitute each vertex's coordinates into the **objective function** and work out its value there.

The vertex giving the largest value is the optimal solution in a maximising problem, and the one giving the smallest value is the optimal solution in a minimising problem.


Spec links: `spcpt_QNpRGQHvyfTQgDXj`


## Card 15 — keyword_definition (`fl_4ZgFQj2vd5H3xm9R`)

**FRONT**

Define what is meant by an **integer solution** to a linear programming problem.


**BACK**

An integer solution is one in which the decision variables all take **whole-number** values.

It is needed when the variables count things that cannot exist in parts, so a manufacturer cannot act on an answer of $3 . 65$ chairs a day.


Spec links: `spcpt_jCNdmDdvzTfzSCF8`


## Card 16 — question_and_answer (`fl_57zsfHHGnwZzbb9J`)

**FRONT**

The optimal solution of a linear programming problem lies at a vertex of the feasible region. Why does that so often mean non-integer coordinates?


**BACK**

Because a vertex is the point where two constraint lines cross, and the crossing point of two lines with awkward coefficients rarely lands on whole-number coordinates.

The graph can therefore give a perfectly correct answer that the context cannot use.


Spec links: `spcpt_jCNdmDdvzTfzSCF8`


## Card 17 — question_and_answer (`fl_mbQWX2FjW78H8k6w`)

**FRONT**

An integer solution can never give a better value of the objective function than the optimal solution read from the graph. Why not?


**BACK**

Because the optimal solution is the best value the objective function takes **anywhere** in the feasible region.

An integer point is simply another point of that region, so it can only match that value or fall short of it.


Spec links: `spcpt_jCNdmDdvzTfzSCF8`


## Card 18 — fill_in_the_blanks (`fl_tRMS7tgkrsNvqZds`)

**FRONT**

The optimal solution of a problem is $x = 3 . 2$, $y = 4 . 7$, but only whole numbers are usable. Complete the four integer points that must be tested:

`\left(3 , 4\right) , \left(3 , 5\right) , \left(\_\_\_\_\_\_ , 4\right) , \left(4 , \_\_\_\_\_\_\right)`


**BACK**

The completed set of points is:

`\left(3 , 4\right) , \left(3 , 5\right) , \left(4 , 4\right) , \left(4 , 5\right)`

They are the **four** points found by rounding each coordinate both down and up, in every combination.


*Blanks: 0 — answers: ['four']*

Spec links: `spcpt_jCNdmDdvzTfzSCF8`

Flags: blank_answer_mismatch


## Card 19 — question_and_answer (`fl_vYsMT67BBhqgR38Y`)

**FRONT**

You have written down the four integer points around an optimal solution. What must you check before going any further?


**BACK**

Check that each point satisfies **every constraint**, since a point close to the optimal vertex can easily fall outside the feasible region.

Any point that fails even one constraint is rejected straight away.


Spec links: `spcpt_jCNdmDdvzTfzSCF8`


## Card 20 — question_and_answer (`fl_2JtmpBpQvfgnQMZP`)

**FRONT**

Two integer points survive the constraint check, and $P = 5 x + 10 y$ is to be maximised. Which of $( 3 , 4 )$ and $( 4 , 4 )$ is the integer solution?


**BACK**

The point $( 4 , 4 )$ is the integer solution, because `P = 5 \left(4\right) + 10 \left(4\right) = 60` there.

At $( 3 , 4 )$ the objective function gives only `5 \left(3\right) + 10 \left(4\right) = 55`.


Spec links: `spcpt_jCNdmDdvzTfzSCF8`


## Card 21 — true_or_false (`fl_jNSyVRYq7KqGZS8q`)

**FRONT**

**True or False?**

The integer solution found by testing the four points around the optimal solution is always the best possible integer solution.


**BACK**

**False.**

Depending on the gradient of the objective line, an integer point further away from the optimal vertex can give a better value of the objective function.

You are not expected to hunt for it, only to recognise that this method finds the integer point **closest to the optimal solution**, which is not necessarily the very best one.


Spec links: `spcpt_jCNdmDdvzTfzSCF8`

