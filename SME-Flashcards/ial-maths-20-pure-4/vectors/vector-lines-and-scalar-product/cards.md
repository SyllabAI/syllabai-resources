# Vector Equations of Lines & The Scalar Product

Course: ial-maths-20-pure-4 · Section: Vectors

Source: https://www.savemyexams.com/international-a-level/maths/edexcel/20/pure-4/flashcards/vectors/vector-lines-and-scalar-product/


## Card 1 — fill_in_the_blanks (`fl_mvVkR4NddM65zzgQ`)

**FRONT**

Complete the vector equation of the line through the points with position vectors $a$ and $b$:

`\mathbf{r} = \mathbf{a} + t \left(\_\_\_\_\_\_\right)`


**BACK**

The completed equation is:

`\mathbf{r} = \mathbf{a} + t \left(\mathbf{b} - \mathbf{a}\right)`

The bracket is a **direction vector**: the step that takes you from one of the points to the other.


*Blanks: 0 — answers: ['direction vector']*

Spec links: `spcpt_hXC48dpxjzYC42CR`

Flags: blank_answer_mismatch


## Card 2 — question_and_answer (`fl_vPvxzZckFtzpKt9k`)

**FRONT**

What two pieces of information fix a line in vector form?


**BACK**

The position vector of **one point** on it, and a **direction vector** along it.

Those give $r = a + t d$, where $t$ runs through every real value as you move along the line.


Spec links: `spcpt_hXC48dpxjzYC42CR`


## Card 3 — question_and_answer (`fl_5zzdm2Sv24m89Q2z`)

**FRONT**

How does $r = a + t d$ compare with $y = m x + c$?


**BACK**

$a$ plays the part of the $+ c$, fixing where the line sits.

$d$ plays the part of the $m$, fixing which way it goes, and unlike a gradient it works just as well in three dimensions.


Spec links: `spcpt_hXC48dpxjzYC42CR`


## Card 4 — question_and_answer (`fl_D3hSh7fhfktdxXPN`)

**FRONT**

Is the point `\left(2 , 0 , - 1\right)` on the line `\mathbf{r} = 3 \mathbf{i} + 2 \mathbf{j} - \mathbf{k} + t \left(\mathbf{i} + 2 \mathbf{j}\right)`, and how can you tell?


**BACK**

Yes, it is, because $t = - 1$ makes all three components match at once.

A point lies on the line only if a **single** value of $t$ works for every component; if no one value does, it does not.


Spec links: `spcpt_hXC48dpxjzYC42CR`


## Card 5 — true_or_false (`fl_kkbTQ4ZzWVNnJKnk`)

**FRONT**

**True or False?**

Two vector equations that look different must represent different lines.


**BACK**

**False.**

Any point on the line will serve as $a$, and any multiple of the direction will serve as $d$, so a single line has infinitely many equations.

That is unlike a Cartesian equation, where two equations describe the same line only if one is a multiple of the other.


Spec links: `spcpt_hXC48dpxjzYC42CR`


## Card 6 — question_and_answer (`fl_TNnNzrxXrjXJ8CWC`)

**FRONT**

Can a vector equation use column vectors instead of $i$, $j$ and $k$?


**BACK**

Yes, and the two forms say exactly the same thing.

So `\mathbf{r} = 3 \mathbf{i} + \mathbf{j} - 7 \mathbf{k} + t \left(\mathbf{i} - 2 \mathbf{j}\right)` and `\mathbf{r} = \begin{pmatrix} 3 \\ 1 \\ - 7 \end{pmatrix} + t \begin{pmatrix} 1 \\ - 2 \\ 0 \end{pmatrix}` are one and the same equation.


Spec links: `spcpt_hXC48dpxjzYC42CR`


## Card 7 — keyword_definition (`fl_8SPgvbwqN8hCjXzj`)

**FRONT**

Define **skew lines**.


**BACK**

Two lines that are **not parallel** and which **do not intersect**.

They can only occur in three dimensions; in two dimensions, lines that are not parallel always meet somewhere.


Spec links: `spcpt_k868kHQFjJdH2rtC`


## Card 8 — question_and_answer (`fl_mC4sYnvRJpB6FXZD`)

**FRONT**

How do you tell whether two lines in 3D are parallel?


**BACK**

Check whether their **direction vectors** are scalar multiples of each other.

The points the lines happen to pass through are irrelevant to this; only the directions count.


Spec links: `spcpt_k868kHQFjJdH2rtC`


## Card 9 — question_and_answer (`fl_msPSrdvNMFZJKFvp`)

**FRONT**

Two lines have been shown to be parallel. What are the only two possibilities?


**BACK**

They either never meet at all, or they are the **same line** written two different ways.

Which of the two it is still has to be checked, since two very different-looking equations can describe one line.


Spec links: `spcpt_k868kHQFjJdH2rtC`


## Card 10 — question_and_answer (`fl_z37MxwPGQVvPbC3W`)

**FRONT**

How do you check whether two parallel lines are actually identical?


**BACK**

Take any point on one line and test whether it also lies on the other.

A single point in common is enough, because parallel lines cannot cross and then separate again.


Spec links: `spcpt_k868kHQFjJdH2rtC`


## Card 11 — question_and_answer (`fl_3MMYVN5q8ZdVVWR4`)

**FRONT**

Two lines are known not to be parallel. How do you find out whether they intersect?


**BACK**

Equate the two general points and write down **three equations**, one for each component.

Solve any two of them for the two parameters, then test whether those values also satisfy the third.


Spec links: `spcpt_k868kHQFjJdH2rtC`


## Card 12 — question_and_answer (`fl_kGk5kz73j238gmn7`)

**FRONT**

What does the third component equation tell you?


**BACK**

Whether the two lines actually meet.

If the parameter values satisfy it as well, the lines **intersect**; if they do not, the lines are **skew**.


Spec links: `spcpt_k868kHQFjJdH2rtC`


## Card 13 — true_or_false (`fl_vrWXywdC6s55PFR4`)

**FRONT**

**True or False?**

The same letter can be used for the parameter in both lines' equations.


**BACK**

**False.**

The two lines reach any common point at different parameter values in general, so one letter cannot stand for both at once.

Using $s$ for one line and $t$ for the other keeps them properly apart.


Spec links: `spcpt_k868kHQFjJdH2rtC`


## Card 14 — fill_in_the_blanks (`fl_WqjmM8YBVvypt6WQ`)

**FRONT**

Complete the scalar product of $a = a_{1} i + a_{2} j + a_{3} k$ and $b = b_{1} i + b_{2} j + b_{3} k$:

`\mathbf{a} \cdot \mathbf{b} = a_{1} b_{1} + \_\_\_\_\_\_ + \_\_\_\_\_\_`


**BACK**

The completed definition is:

`\mathbf{a} \cdot \mathbf{b} = a_{1} b_{1} + a_{2} b_{2} + a_{3} b_{3}`

Corresponding components are multiplied together and the results are then **added**.


*Blanks: 0 — answers: ['added']*

Spec links: `spcpt_GnvjF6Qpb6TTNvnd`

Flags: blank_answer_mismatch


## Card 15 — true_or_false (`fl_GdwzHB5z5qYJkbwf`)

**FRONT**

**True or False?**

The scalar product of two vectors is another vector.


**BACK**

**False.**

The result is a **real number**, which is exactly why it is called the *scalar* product.

That is worth holding on to, since most other operations on vectors hand you back a vector.


Spec links: `spcpt_GnvjF6Qpb6TTNvnd`


## Card 16 — question_and_answer (`fl_CdvYCTDDrCy94BBz`)

**FRONT**

What is the scalar product in terms of the angle between the vectors?


**BACK**

`\mathbf{a} \cdot \mathbf{b} = \left| \mathbf{a} \right| \left| \mathbf{b} \right| \cos \theta`.

Here $θ$ is the angle between them when they are placed **base to base**, that is starting from the same point.


Spec links: `spcpt_GnvjF6Qpb6TTNvnd`


## Card 17 — question_and_answer (`fl_JxjKMQymdRyQrqtZ`)

**FRONT**

What is `\mathbf{a} \cdot \mathbf{a}` equal to?


**BACK**

`\left| \mathbf{a} \right|^{2}`, the square of the vector's own magnitude.

It follows from the angle formula, since a vector makes an angle of zero with itself and $\mathrm{cos} 0 ^{\circ} = 1$.


Spec links: `spcpt_GnvjF6Qpb6TTNvnd`


## Card 18 — question_and_answer (`fl_5BJpxtDDFH2q4G4S`)

**FRONT**

Which two familiar algebraic rules does the scalar product obey?


**BACK**

The order does not matter, `\mathbf{a} \cdot \mathbf{b} = \mathbf{b} \cdot \mathbf{a}`, and brackets multiply out, `\mathbf{a} \cdot \left(\mathbf{b} + \mathbf{c}\right) = \mathbf{a} \cdot \mathbf{b} + \mathbf{a} \cdot \mathbf{c}`.

Together they let you expand something like `\left(\mathbf{a} - \mathbf{b}\right) \cdot \left(\mathbf{a} - \mathbf{b}\right)` exactly as you would in ordinary algebra.


Spec links: `spcpt_GnvjF6Qpb6TTNvnd`


## Card 19 — question_and_answer (`fl_4HTKGntNhkz76XNd`)

**FRONT**

Work out `\left(3 \mathbf{i} - \mathbf{k}\right) \cdot \left(2 \mathbf{i} + 9 \mathbf{j} + \mathbf{k}\right)`.


**BACK**

The answer is $5$.

The absent $j$ in the first vector counts as $0$, so the sum is `3 \times 2 + 0 \times 9 + \left(- 1\right) \times 1 = 5`.


Spec links: `spcpt_GnvjF6Qpb6TTNvnd`


## Card 20 — fill_in_the_blanks (`fl_s5GwnHhJMDmdGkqQ`)

**FRONT**

Complete the angle between two vectors:

`\theta = \_\_\_\_\_\_ \left(\frac{\mathbf{a} \cdot \mathbf{b}}{\left| \mathbf{a} \right| \left| \mathbf{b} \right|}\right)`


**BACK**

The completed formula is:

`\theta = \cos^{- 1} \left(\frac{\mathbf{a} \cdot \mathbf{b}}{\left| \mathbf{a} \right| \left| \mathbf{b} \right|}\right)`

The scalar product divided by the two magnitudes gives $\mathrm{cos} θ$, so an inverse cosine is what finally produces the angle itself.


*Blanks: 0 — answers: []*

Spec links: `spcpt_GjkGPBQxw5qX3wHd`


## Card 21 — question_and_answer (`fl_gsDPr2qsdkV7BMWg`)

**FRONT**

How do you find the angle between two lines in 3D?


**BACK**

Find the angle between their **direction vectors**.

Where the lines happen to sit makes no difference to the angle between them, so the position vectors play no part at all.


Spec links: `spcpt_GjkGPBQxw5qX3wHd`


## Card 22 — true_or_false (`fl_VsyD2s2ZZWMsCmPj`)

**FRONT**

**True or False?**

Two non-zero vectors are perpendicular exactly when their scalar product is zero.


**BACK**

**True.**

If they are perpendicular then $\mathrm{cos} 90 ^{\circ} = 0$ makes the product zero; and if the product is zero then neither magnitude can be, so $\mathrm{cos} θ$ must be.

The condition holds in both directions, which is what makes it such a quick test.


Spec links: `spcpt_GjkGPBQxw5qX3wHd`


## Card 23 — question_and_answer (`fl_7zqGpqjYVTtKY5Mh`)

**FRONT**

Are $2 i - 3 j + 5 k$ and $- 4 i - j + k$ perpendicular?


**BACK**

Yes, they are perpendicular.

Their scalar product works out as `2 \times \left(- 4\right) + \left(- 3\right) \times \left(- 1\right) + 5 \times 1 = - 8 + 3 + 5 = 0`.


Spec links: `spcpt_GjkGPBQxw5qX3wHd`


## Card 24 — keyword_definition (`fl_NKcWQSjwbVNBwm7q`)

**FRONT**

Define the **foot of the perpendicular** from a point to a line.


**BACK**

The point on the line that is **closest** to the given point.

The segment joining the two is perpendicular to the line, which is where the name comes from.


Spec links: `spcpt_GjkGPBQxw5qX3wHd`


## Card 25 — question_and_answer (`fl_VcWRNGVqJjryszSn`)

**FRONT**

A point $P$ does not lie on the line $r = a + t d$. How do you locate the closest point on the line?


**BACK**

Write that point as $a + t_{0} d$, form the vector running from it to $P$, and set the scalar product of that vector with $d$ equal to zero.

Solving the resulting equation gives $t_{0}$, and substituting it back gives the point itself.


Spec links: `spcpt_GjkGPBQxw5qX3wHd`


## Card 26 — question_and_answer (`fl_4CTkRfjhbdpj7Wz2`)

**FRONT**

Once you have found the closest point on the line, how do you get the shortest distance?


**BACK**

Take the **magnitude** of the vector joining that point to $P$.

That length is sometimes called the length of the perpendicular, and it is smaller than the distance to any other point of the line.


Spec links: `spcpt_GjkGPBQxw5qX3wHd`

