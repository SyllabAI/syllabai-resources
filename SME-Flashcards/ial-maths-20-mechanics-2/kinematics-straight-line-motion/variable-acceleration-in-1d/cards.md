# Variable Acceleration in 1D

Course: ial-maths-20-mechanics-2 · Section: Kinematics (Straight Line Motion)

Source: https://www.savemyexams.com/international-a-level/maths/edexcel/20/mechanics-2/flashcards/kinematics-straight-line-motion/variable-acceleration-in-1d/


## Card 1 — fill_in_the_blanks (`fl_Bgfh8cQ4nc9KTgDy`)

**FRONT**

A particle's acceleration varies with time, so the suvat formulae cannot be used. Fill in the blanks to complete the calculus links:

Differentiate `\_\_\_\_\_\_` to get velocity, and differentiate velocity to get `\_\_\_\_\_\_`


**BACK**

The completed link is:

Differentiate **displacement** to get velocity, and differentiate velocity to get **acceleration**.

Integrating runs the same chain backwards: integrate acceleration to get velocity, and integrate velocity to get displacement.

Each of the three is a function of time, and differentiating measures a **rate of change** with respect to time.


*Blanks: 0 — answers: ['displacement', 'acceleration', 'rate of change']*

Spec links: `spcpt_JqNkg4qXvkzKyC8N`

Flags: blank_answer_mismatch


## Card 2 — question_and_answer (`fl_fdDMxrgdX3RMZXZB`)

**FRONT**

On a velocity-time graph that is a **curve**, how do you find the acceleration at a particular moment, and the displacement over an interval?


**BACK**

**Differentiate** to find the acceleration at a moment, and **integrate** to find the displacement over an interval.

Because the graph curves, the gradient differs at every point and the region under it is not made of triangles and rectangles whose areas can simply be added.

Calculus does both jobs: the derivative gives the gradient at a point, and the definite integral gives the area under the curve.


Spec links: `spcpt_JqNkg4qXvkzKyC8N`


## Card 3 — question_and_answer (`fl_Q5h4x3dMWczSJRg9`)

**FRONT**

A kinematics question says a particle **starts from rest**. What does that tell you, and what do you use it for?


**BACK**

Starting from rest means the velocity is zero at the start, so $v = 0$ when $t = 0$.

That is a pair of matching values, exactly what is needed to find the **constant of integration**: substitute both into the expression after integrating and solve for the constant.

The word **initially** does the same job on its own: it means $t = 0$.


Spec links: `spcpt_JqNkg4qXvkzKyC8N`


## Card 4 — question_and_answer (`fl_F3YRsv4yQqzB8bnc`)

**FRONT**

A particle's velocity changes sign between $t = 0$ and $t = 3$. Why does `\int_{0}^{3} v \text{ d}t` not give the distance it has travelled?


**BACK**

That integral gives the **displacement**, not the distance.

While the velocity is negative the particle is moving backwards, and the integral counts that motion as negative, so it subtracts from the total instead of adding to it.

To find the distance, first find the times when $v = 0$, the moments the particle turns round, then integrate between each consecutive pair and add the **sizes** of the results, ignoring their signs.


Spec links: `spcpt_JqNkg4qXvkzKyC8N`


## Card 5 — true_or_false (`fl_7X8pbYnndPNDpwhT`)

**FRONT**

**True or False?**

You can assume that integrating a particle's acceleration between two times gives its velocity at the later time.


**BACK**

**False.**

Integrating acceleration between two times gives the **change** in velocity over that interval, not the velocity itself.

To get the velocity at the later time, add that change to the velocity at the earlier time.

The two only happen to agree when the particle was at rest at the earlier time, since then the change and the final velocity are the same number.


Spec links: `spcpt_JqNkg4qXvkzKyC8N`


## Card 6 — question_and_answer (`fl_CwxSDQwJKkSMfbrX`)

**FRONT**

A particle's velocity is given as $v = 3 \text{e}^{0.5t}$ rather than as a polynomial. What changes about the way you find its displacement?


**BACK**

Nothing about the method changes: the displacement is still found by integrating the velocity, and the constant of integration is still found by substituting a known pair of values.

Only the **integration itself** is different, because a different technique is needed for an exponential than for a polynomial.

The links between displacement, velocity and acceleration do not depend on what kind of function of $t$ you have been given.


Spec links: `spcpt_JqNkg4qXvkzKyC8N`

