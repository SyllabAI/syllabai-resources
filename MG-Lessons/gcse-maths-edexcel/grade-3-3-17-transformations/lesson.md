# grade-3-3-17-transformations — lesson

_Lane: `gcse-maths-edexcel` · grade 3 · 5 content steps · 3 check questions (source: MathsGenie lessons)_

## What transformations do

![Four coordinate grids showing the same triangle translated, reflected in the line x = 1, rotated 90 degrees anticlockwise about O, and enlarged by scale factor 2 from O](../assets/001-5db078b2-b732-4e1b-9f46-32b7a6160258.jpeg)

A transformation moves or changes a shape on a coordinate grid. The original shape is called the object, the new one is the image, and matching corners are corresponding vertices.

A point is written as $(x,y)$, where $x$ tells you how far across and $y$ tells you how far up or down. The origin is specifically the point $O=(0,0)$.

There are four main transformations: translation, reflection, rotation, and enlargement. To describe one fully, you must name the type and provide its specific extra detail.

## Translations and vectors

![Coordinate grid showing a triangle translated from A(-2,-1), B(0,-1), C(-1,1) to A'(4,2), B'(6,2), C'(5,4) with a movement arrow labelled vector 6 over 3](../assets/002-4c6f94c7-10b2-4b73-8dc3-79cbbe9aa822.jpeg)

A translation slides a shape without turning or flipping it. Every vertex moves the same distance, so the image has the same size and orientation as the object.

In the diagram, $A(-2,-1)$ moves to $A'(4,2)$. The $x$-coordinate increases by $6$, so the movement is 6 right, and the $y$-coordinate increases by $3$, so the movement is 3 up.

We write this as
$$
\begin{pmatrix} 6 \\ 3 \end{pmatrix}
$$
The top number is the horizontal movement and the bottom number is the vertical movement. That vector is the full description of the translation.

## Reflections and rotations

![Coordinate grid comparing a shape reflected in the line y = x, a shape rotated 90 degrees anticlockwise about O, and a triangle enlarged by scale factor 3 from O](../assets/003-b4090e9d-4a72-467c-9a48-3e1bad6bc1cc.jpeg)

The diagram compares three non-translation transformations. A reflection flips a shape in a mirror line, a rotation turns it about a centre, and an enlargement changes its size from a centre.

For reflections, corresponding vertices stay the same distance from the mirror line on opposite sides. In the $x$-axis, $(x,y)\to(x,-y)$, in the $y$-axis, $(x,y)\to(-x,y)$, and in the line $y=x$, $(x,y)\to(y,x)$.

For rotations about $O$, a $90^\circ$ anticlockwise turn uses $(x,y)\to(-y,x)$ and a $180^\circ$ turn uses $(x,y)\to(-x,-y)$. A full description of a rotation must include the angle, direction, and centre.

## Enlargements from the origin

An enlargement changes size but keeps shape. The scale factor tells you how many times each distance from the centre changes, and the centre of enlargement is the fixed point it grows from.

If the centre is $O$, multiply each coordinate by the scale factor. With scale factor $3$, $(1,0)\to(3,0)$, $(2,0)\to(6,0)$, and $(2,2)\to(6,6)$.

So the triangle with vertices $(1,0)$, $(2,0)$, and $(2,2)$ becomes a triangle with vertices $(3,0)$, $(6,0)$, and $(6,6)$. This quick multiplication rule only works when the centre of enlargement is $O$.

## Combined transformations

When a question gives two transformations, do them in the order written. 'Reflect then translate' can give a different result from 'translate then reflect.'

Example: start with the point $(2,3)$ and reflect it in the $x$-axis to get $(2,-3)$. Now compare $(2,-3)$ with the final point $(-1,-4)$.

The movement is 3 left and 1 down, so the translation vector is
$$\begin{pmatrix} -3 \\ -1 \end{pmatrix}$$

Working one step at a time is the safest method. It also helps you spot if you have used the wrong pair of points.

## Check yourself

1. Which transformation can change the size of a shape?

   - Translation

   - Reflection

   - Enlargement ✔

   - Rotation

   _Explanation:_ Enlargement is correct because it changes the size of the shape. Rotation is the most common wrong answer because the shape turns, but it stays the same size.

2. A point at $(4,-2)$ is reflected in the line $y=x$. What are the coordinates of the image?

   - $$(-2,4)$ ✔

   - $$(4,2)$

   - $$(2,-4)$

   - $$(-4,2)$

   _Explanation:_ Reflecting in $y=x$ swaps the coordinates, so $(4,-2)$ becomes $(-2,4)$. Option B is the common wrong answer because it only changes the sign of $y$, which is reflection in the $x$-axis, not in $y=x$.

3. A point starts at $(2,1)$. It is translated by the vector $\begin{pmatrix} 3 \\ -2 \end{pmatrix}$ and then reflected in the $x$-axis. Where is the final point?

   - $$(5,1)$ ✔

   - $$(5,-1)$

   - $$(5,-3)$

   - $$(-5,1)$

   _Explanation:_ First translate: $(2,1)\to(5,-1)$. Then reflect in the $x$-axis, which changes the sign of the $y$-coordinate, so $(5,-1)\to(5,1)$. Option B is the common wrong answer because it stops after the translation, and option C is a common wrong answer because it does the reflection first.
