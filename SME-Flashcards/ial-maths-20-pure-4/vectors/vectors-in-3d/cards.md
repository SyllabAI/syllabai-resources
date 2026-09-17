# Vectors in 3D

Course: ial-maths-20-pure-4 · Section: Vectors

Source: https://www.savemyexams.com/international-a-level/maths/edexcel/20/pure-4/flashcards/vectors/vectors-in-3d/


## Card 1 — keyword_definition (`fl_5jZdXV76t6dmbMGN`)

**FRONT**

Define **unit vector**.


**BACK**

A vector with a **magnitude of 1**.

$i$, $j$ and $k$ are the unit vectors in the directions of the $x$, $y$ and $z$ axes, and they are mutually **perpendicular**.


Spec links: `spcpt_XrvxCtZwqGx2bXZq`


## Card 2 — question_and_answer (`fl_t2yZX8MpJm3fhpx3`)

**FRONT**

What are the two ways of writing a 3D vector?


**BACK**

As a **column vector**, or in $i$, $j$, $k$ form. The three components are the same numbers either way:

`\begin{pmatrix} 3 \\ 7 \\ -2 \end{pmatrix} = 3\mathbf{i} + 7\mathbf{j} - 2\mathbf{k}`

Each component is the distance moved in the direction of one axis.


Spec links: `spcpt_XrvxCtZwqGx2bXZq`


## Card 3 — fill_in_the_blanks (`fl_8vc7qrPQJGTBKMpD`)

**FRONT**

Complete the formula for the magnitude of a 3D vector:

`|x\mathbf{i} + y\mathbf{j} + z\mathbf{k}| = \sqrt{\_\_\_\_\_\_}`


**BACK**

The completed formula is:

`|x\mathbf{i} + y\mathbf{j} + z\mathbf{k}| = \sqrt{x^{2} + y^{2} + z^{2}}`

It is Pythagoras' theorem carried into three dimensions. This one is on the list of formulae you are expected to **know**, so it is not given in the formulae booklet.

The magnitude is also called the **modulus** of the vector.


*Blanks: 0 — answers: ['know', 'modulus']*

Spec links: `spcpt_XrvxCtZwqGx2bXZq`

Flags: blank_answer_mismatch


## Card 4 — true_or_false (`fl_JSFhb6w7XxnSRDh4`)

**FRONT**

**True or False?**

The magnitude of $- 2 i + 3 j - 6 k$ is negative, because two of its components are negative.


**BACK**

**False.**

A magnitude is a **length**, so it is never negative. Squaring the components removes the signs:

`|-2\mathbf{i} + 3\mathbf{j} - 6\mathbf{k}| = \sqrt{4 + 9 + 36} = \sqrt{49} = 7`


Spec links: `spcpt_XrvxCtZwqGx2bXZq`


## Card 5 — question_and_answer (`fl_45ZdjXWdDwjV4bqw`)

**FRONT**

How do you find the unit vector in the direction of a vector $a$?


**BACK**

Divide the vector by its own magnitude, giving `\frac{\mathbf{a}}{|\mathbf{a}|}`. It is written `\hat{\mathbf{a}}`.

So, **for example**, if $a = 3 i - 4 j + 5 k$ then `|\mathbf{a}| = \sqrt{50} = 5\sqrt{2}`, so:

`\hat{\mathbf{a}} = \frac{1}{5\sqrt{2}}\left(3\mathbf{i} - 4\mathbf{j} + 5\mathbf{k}\right)`


Spec links: `spcpt_XrvxCtZwqGx2bXZq`


## Card 6 — question_and_answer (`fl_Sr4T29qqfb7ctqKS`)

**FRONT**

How can you tell whether two vectors are parallel?


**BACK**

One is a **scalar multiple** of the other, so every component is multiplied by the same number.

So, **for example**:

`\begin{pmatrix} 6 \\ -4 \\ 2 \end{pmatrix} = \frac{2}{3}\begin{pmatrix} 9 \\ -6 \\ 3 \end{pmatrix}`

so those two vectors are parallel.


Spec links: `spcpt_XrvxCtZwqGx2bXZq`


## Card 7 — question_and_answer (`fl_CVtDQmH6KzDrJCBf`)

**FRONT**

Two points are given by their position vectors. How do you find the distance between them?


**BACK**

Subtract one position vector from the other to get the vector joining the points, then find that vector's **magnitude**.

So, **for example**, for $A ( 5 , 3 , - 7 )$ and $B ( 3 , - 6 , 5 )$:

$\sqrt{(5-3)^{2}+(3-(-6))^{2}+(-7-5)^{2}} = \sqrt{229} = 15 . 1$

It does not matter which way round you subtract, because each difference is squared.


Spec links: `spcpt_XrvxCtZwqGx2bXZq`


## Card 8 — keyword_definition (`fl_V9xFW4J6cj2Zy756`)

**FRONT**

Define **collinear** points.


**BACK**

Points that all lie on the **same straight line**.

Showing it needs two vectors that are parallel **and** share a common point, since parallel vectors on their own only give parallel lines.


Spec links: `spcpt_2PGdnfT8zrW4HcHn`


## Card 9 — question_and_answer (`fl_672Gw8QXfR8MH6qn`)

**FRONT**

How do you show that three points are collinear?


**BACK**

Use their position vectors to find two vectors that start at the **same** point, such as $\overset{\rightarrow}{AB}$ and $\overset{\rightarrow}{AC}$, then show one is a multiple of the other.

So, **for example**, for $A ( 1 , 2 , 3 )$, $B ( 3 , 8 , 1 )$ and $C ( 7 , 20 , - 3 )$, $\overset{\rightarrow}{AB}=2i+6j-2k$ and $\overset{\rightarrow}{AC}=6i+18j-6k=3\overset{\rightarrow}{AB}$, and both start at $A$.


Spec links: `spcpt_2PGdnfT8zrW4HcHn`


## Card 10 — fill_in_the_blanks (`fl_b7j25HzssCfF2F8B`)

**FRONT**

The vector $a = x i + y j + z k$ makes an angle $θ_{x}$ with the $x$-axis. Complete the formula:

`\cos\theta_{x} = \frac{\_\_\_\_\_\_}{\_\_\_\_\_\_}`


**BACK**

The completed formula is:

`\cos\theta_{x} = \frac{x}{|\mathbf{a}|}`

It is just cosine = adjacent divided by hypotenuse, in the right-angled triangle formed by the vector and the axis: the side along the axis has length $x$, and the vector itself has length `|\mathbf{a}|`.

The $y$ and $z$ versions work the same way, and none of them is in the formulae booklet.


*Blanks: 0 — answers: []*

Spec links: `spcpt_2PGdnfT8zrW4HcHn`


## Card 11 — question_and_answer (`fl_922xnhPjvJmfDNMZ`)

**FRONT**

How do you find the angle between two vectors in three dimensions?


**BACK**

Make them two sides of a **triangle** and find the vector for the third side, then find the length of all three sides using the magnitude formula.

The angle then comes from the **cosine rule**:

$\mathrm{cos} θ = \frac{b^{2}+c^{2}-a^{2}}{2bc}$


Spec links: `spcpt_2PGdnfT8zrW4HcHn`


## Card 12 — true_or_false (`fl_YVn5fCfdb4vQHSr3`)

**FRONT**

**True or False?**

To show that a triangle with sides given as vectors is isosceles, you show that two of those vectors are equal.


**BACK**

**False.**

You compare their **magnitudes**. Two side vectors of a triangle can never be equal, since equal vectors point the same way and the sides of a triangle do not.

So, **for example**, sides $5 i + 6 j - 2 k$ and $7 i + 4 k$ are different vectors, but both have magnitude $\sqrt{65}$.


Spec links: `spcpt_2PGdnfT8zrW4HcHn`


## Card 13 — question_and_answer (`fl_nK2Fr7vRV5yJQ7NY`)

**FRONT**

Why must you find an angle before you can find the area of a triangle whose sides are given as vectors?


**BACK**

Because the area formula $\text{Area} = \frac{1}{2} a b \mathrm{sin} θ$ needs the angle **between** the two sides, and the vectors do not give it to you directly.

That is why an area question of this kind always begins by finding all three side lengths: the angle has to be worked out from those first.


Spec links: `spcpt_2PGdnfT8zrW4HcHn`


## Card 14 — question_and_answer (`fl_FhZT9GHRMmwV6pdB`)

**FRONT**

In a shape such as a cuboid or a parallelogram, what is true of the vectors along opposite sides?


**BACK**

They are **equal**: the same magnitude and the same direction.

That is what lets you find a missing vertex. Travel to the unknown corner along a route made of vectors you already know, adding them as you go.


Spec links: `spcpt_2PGdnfT8zrW4HcHn`

