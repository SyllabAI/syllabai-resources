# 3d Pythagoras and Trigonometry Flashcards

_Lane: `igcse-maths-edexcel` · grade 7 · 22 cards (source: MathsGenie flashcards)_

## Card 1 — `basic`

**Front:** In the Pythagoras theorem $a^2 + b^2 = c^2$, which side must be $c$?

**Back:** The hypotenuse (the longest side opposite the right angle).

**Choices:**

- The hypotenuse (the longest side opposite the right angle). ✔
  - _why:_ In a right-angled triangle, $c$ is the hypotenuse because it lies opposite the right angle and is always the triangle’s longest side.
- The adjacent side (the side next to the right angle).
  - _why:_ The adjacent side depends on which acute angle is being considered, so it is not necessarily $c$. In Pythagoras, $c$ must be the hypotenuse opposite the right angle.
- The shortest side (the side next to the right angle).
  - _why:_ Choosing the shortest side confuses the fixed role of $c$ with relative side lengths. The correct side is the hypotenuse, which is opposite the right angle and longest.
- The opposite side (the side opposite an acute angle).
  - _why:_ The opposite side in trigonometry changes according to the chosen acute angle. In Pythagoras, $c$ specifically represents the hypotenuse opposite the right angle.

## Card 2 — `cloze`

**Front:** A [ ___ ] joins two opposite corners of a 3D shape, passing through the inside of the solid.

**Back:** A space diagonal joins two opposite corners of a 3D shape, passing through the inside of the solid.

**Choices:**

- space diagonal ✔
  - _why:_ A space diagonal connects opposite vertices while travelling through the interior of a three-dimensional solid, rather than remaining on one of its faces.
- face diagonal
  - _why:_ A face diagonal joins opposite corners of one two-dimensional face and stays on the solid’s surface. A diagonal passing through the interior is a space diagonal.
- slant height
  - _why:_ A slant height measures a sloping surface length, commonly on a cone or pyramid; it does not generally connect opposite vertices. The required term is space diagonal.
- base edge
  - _why:_ A base edge joins two neighbouring vertices and lies along the boundary of the base. A line joining opposite corners through the solid is a space diagonal.

## Card 3 — `basic`

**Front:** What is the 2-step strategy for finding a cuboid's space diagonal without using the shortcut formula?

**Back:** Find the face/base diagonal using Pythagoras.Use that diagonal and the height in a second Pythagoras calculation.

**Choices:**

- Find the face/base diagonal using Pythagoras.Use that diagonal and the height in a second Pythagoras calculation. ✔
  - _why:_ The base diagonal forms the first right-angled triangle. It then becomes one perpendicular side of a second right-angled triangle whose hypotenuse is the cuboid’s space diagonal.
- Find the face/base diagonal by adding length and width.Use that diagonal and the height in a Pythagoras calculation.
  - _why:_ Adding length and width does not give the base diagonal; that mistake ignores the first right-angled triangle. Use Pythagoras for the base diagonal, then use Pythagoras again with the height.
- Find the face/base perimeter using the side lengths.Use half that perimeter and the height in Pythagoras.
  - _why:_ Half the base perimeter is not a straight-line distance across the base. First calculate the base diagonal using Pythagoras, then combine it with the height using Pythagoras again.
- Choose one base edge as the horizontal distance.Use that edge and the height in a Pythagoras calculation.
  - _why:_ One base edge omits the cuboid’s other horizontal dimension, so the result is only a face diagonal. Use the base diagonal with the height to obtain the space diagonal.

## Card 4 — `basic`

**Front:** What is the shortcut formula for the space diagonal $d$ of a cuboid with length $l$, width $w$, and height $h$?

**Back:** $$d^2 = l^2 + w^2 + h^2$

**Choices:**

- $$d^2 = l^2 + w^2 + h^2$ ✔
  - _why:_ Applying Pythagoras across the base and then through the cuboid gives the sum of all three squared perpendicular dimensions, so $d^2=l^2+w^2+h^2$.
- $$d^2 = l + w + h$
  - _why:_ This adds unsquared lengths, which is incompatible with Pythagoras and even gives mismatched units on the two sides. The correct formula is $d^2=l^2+w^2+h^2$.
- $$d = l^2 + w^2 + h^2$
  - _why:_ This forgets that the sum of the squares equals $d^2$, not $d$, producing a dimensional mismatch. The correct relationship is $d^2=l^2+w^2+h^2$.
- $$d^2 = (l + w + h)^2$
  - _why:_ Squaring the total introduces extra cross-terms such as $2lw$, which Pythagoras does not include. The three dimensions must be squared separately: $d^2=l^2+w^2+h^2$.

## Card 5 — `cloze`

**Front:** To find a missing depth $x$ in a cuboid where the space diagonal $d$, width $w$, and height $h$ are known, the formula is $x^2 = \text{[...]}$.

**Back:** To find a missing depth $x$ in a cuboid where the space diagonal $d$, width $w$, and height $h$ are known, the formula is $x^2 = \boxed{d^2 - w^2 - h^2}$.

**Choices:**

- $$d^2 - w^2 - h^2$ ✔
  - _why:_ Starting from $d^2=x^2+w^2+h^2$, subtracting both known squared dimensions isolates the missing depth: $x^2=d^2-w^2-h^2$.
- $$d^2 + w^2 + h^2$
  - _why:_ Adding the known squares again makes the missing depth larger than the space diagonal. Rearranging requires subtraction, giving $x^2=d^2-w^2-h^2$.
- $$d^2 - w^2 + h^2$
  - _why:_ This changes the sign of only one known dimension, so the height remains on the wrong side of the equation. Both known squares must be subtracted from $d^2$.
- $$d^2 - (w + h)^2$
  - _why:_ Adding width and height before squaring creates an unwanted $2wh$ term. Pythagoras uses separate squares, so the correct expression is $d^2-w^2-h^2$.

## Card 6 — `cloze`

**Front:** Common mistake: calculating $d = l + w + h$ for a cuboid is wrong because Pythagoras works with squares of lengths, not [ ___ ].

**Back:** Common mistake: calculating $d = l + w + h$ for a cuboid is wrong because Pythagoras works with squares of lengths, not lengths added directly.

**Choices:**

- lengths added directly ✔
  - _why:_ Pythagoras adds squared perpendicular lengths, as in $d^2=l^2+w^2+h^2$. Simply adding the original lengths measures a route along edges rather than the straight diagonal.
- lengths multiplied directly
  - _why:_ Multiplication is not the specific mistake in $d=l+w+h$; that expression adds unsquared lengths. Pythagoras instead adds their squares, so the missing phrase is lengths added directly.
- lengths subtracted directly
  - _why:_ Subtraction is not being performed in $d=l+w+h$; the misconception is adding the three unsquared dimensions. The correct contrast is with lengths added directly.
- angles added directly
  - _why:_ The formula $d=l+w+h$ contains lengths rather than angles, so angle addition is unrelated. Its error is treating the diagonal as lengths added directly instead of using squared lengths.

## Card 7 — `basic`

**Front:** When finding the angle between a cuboid's diagonal and its base, what must be used as the adjacent side?

**Back:** The base diagonal (not just one edge of the base).

**Choices:**

- The base diagonal (not just one edge of the base). ✔
  - _why:_ The space diagonal’s projection onto the horizontal base runs between opposite base corners, so the adjacent side of the relevant right-angled triangle is the base diagonal.
- The length edge (not the diagonal across the base).
  - _why:_ Using only the length ignores the base’s width and forms the wrong triangle. The adjacent side must be the base diagonal, which is the space diagonal’s horizontal projection.
- The vertical height (not a side across the base).
  - _why:_ For an angle measured from the base, the vertical height is the opposite side, not the adjacent side. The adjacent side is the diagonal across the base.
- The space diagonal (not a side lying on the base).
  - _why:_ The space diagonal is the hypotenuse of the right-angled triangle, so it cannot also be the adjacent side. The adjacent side is its projection, the base diagonal.

## Card 8 — `cloze`

**Front:** The [ ___ ] of a line onto a plane is like its shadow on that plane.

**Back:** The projection of a line onto a plane is like its shadow on that plane.

**Choices:**

- projection ✔
  - _why:_ A projection represents where a line would fall on a plane, like a shadow cast onto that surface. It is used to form the appropriate two-dimensional triangle.
- intersection
  - _why:_ An intersection is the point or set of points where objects meet, not the line’s shadow on a plane. The shadow-like representation is called a projection.
- inclination
  - _why:_ Inclination describes the angle a line makes with a reference line or plane. The shadow-like line formed on the plane is instead called its projection.
- reflection
  - _why:_ A reflection produces a mirror image across a line or plane rather than a shadow onto it. The line’s shadow-like image on the plane is its projection.

## Card 9 — `cloze`

**Front:** The projection of a line onto a plane is like its [ ___ ] on that plane.

**Back:** The projection of a line onto a plane is like its shadow on that plane.

**Choices:**

- shadow ✔
  - _why:_ A projection shows where the line would appear on the plane when mapped directly onto it, like the shadow cast by the line onto that surface.
- reflection
  - _why:_ A reflection is a mirror image produced across a line or plane. The correct term is shadow because a projection represents the line’s mapped position on the plane.
- rotation
  - _why:_ A rotation turns an object about a fixed point or axis. The correct term is shadow because a projection shows the line mapped onto the plane.
- intersection
  - _why:_ An intersection is where geometric objects meet, which may be only one point. The correct term is shadow because the whole line is projected onto the plane.

## Card 10 — `basic`

**Front:** How is the angle between a line and a plane defined?

**Back:** The angle between the line and its projection on the plane.

**Choices:**

- The angle between the line and its projection on the plane. ✔
  - _why:_ The projection represents the line’s direction along the plane, so the angle between the original line and this projection is defined as the line-plane angle.
- The angle between the line and the normal to the plane.
  - _why:_ The angle with the normal is complementary to the angle with the plane. The required angle is between the line and its projection on the plane.
- The angle between the projection and a perpendicular to the line.
  - _why:_ Using an arbitrary perpendicular to the line does not define the line-plane angle. It is measured between the line and its projection on the plane.
- The angle between the plane and a vertical line through the plane.
  - _why:_ A vertical line is not necessarily related to the given line and may depend on the diagram’s orientation. The angle uses the line and its projection.

## Card 11 — `basic`

**Front:** How do you find the projection of a point onto a plane?

**Back:** Drop a perpendicular line from the point down to the plane.

**Choices:**

- Drop a perpendicular line from the point down to the plane. ✔
  - _why:_ The perpendicular gives the shortest route from the point to the plane. Where it meets the plane is the point’s orthogonal projection.
- Draw a parallel line from the point across to the plane.
  - _why:_ A line parallel to the plane will not meet it, so it cannot locate the projection. A perpendicular must be dropped from the point to the plane.
- Draw a horizontal line from the point across to the plane.
  - _why:_ Horizontal depends on the diagram’s orientation and does not guarantee a 90-degree angle with the plane. The projection is found using a perpendicular line.
- Join a diagonal line from the point to a corner of the plane.
  - _why:_ Joining the point to a chosen corner gives a sloping segment, not its projection. The correct construction drops a perpendicular line to the plane.

## Card 12 — `cloze`

**Front:** In a symmetrical square-based pyramid, the vertical height meets the base at the [ ___ ] of the square.

**Back:** In a symmetrical square-based pyramid, the vertical height meets the base at the centre of the square.

**Choices:**

- centre ✔
  - _why:_ Symmetry places the apex directly above the centre of the square base, so the perpendicular vertical height meets the base at that central point.
- corner
  - _why:_ A line from the apex to a corner is a sloping edge, not the vertical height. In a symmetrical pyramid, the vertical height meets the centre.
- perimeter
  - _why:_ The perimeter is the boundary of the square rather than the point directly below the apex. The vertical height meets the base at its centre.
- edge
  - _why:_ An edge lies on the boundary of the base, so meeting it would place the apex off-centre. Symmetry requires the height to meet the centre.

## Card 13 — `basic`

**Front:** In a pyramid, what is the difference between vertical height and a sloping edge?

**Back:** Vertical height goes straight from apex to base at 90 degrees.Sloping edge connects the apex to a corner of the base.

**Choices:**

- Vertical height goes straight from apex to base at 90 degrees.Sloping edge connects the apex to a corner of the base. ✔
  - _why:_ Vertical height is perpendicular to the base and measures the pyramid’s true height. A sloping edge instead joins the apex to a base vertex.
- Vertical height connects the apex to a corner of the base.Sloping edge goes straight from apex to base at 90 degrees.
  - _why:_ This reverses the two definitions. The vertical height is perpendicular to the base, while a sloping edge joins the apex to a corner of the base.
- Vertical height runs along the base from corner to corner.Sloping edge connects two corners of the base.
  - _why:_ Both descriptions refer to lines within the base rather than lines from the apex. The height is perpendicular to the base, while a sloping edge reaches a base corner.
- Vertical height follows a triangular face down to its base.Sloping edge connects the apex to the centre of the base.
  - _why:_ This confuses face height, vertical height and sloping edge. Vertical height reaches the base perpendicularly, while a sloping edge joins the apex to a base corner.

## Card 14 — `basic`

**Front:** In a square-based pyramid, what is the relationship between the distance from corner to centre ($AO$) and the base diagonal ($AC$)?

**Back:** $$AO = \frac{1}{2} AC$

**Choices:**

- $$AO = \frac{1}{2} AC$ ✔
  - _why:_ The diagonals of a square bisect each other at the centre. Therefore, the distance from a corner to the centre is half the full diagonal.
- $$AO = AC$
  - _why:_ This treats the corner-to-centre distance as the whole diagonal. Since the centre bisects the diagonal, the correct relationship is $AO = \frac{1}{2}AC$.
- $$AO = 2AC$
  - _why:_ This reverses and doubles the relationship, making a segment larger than the full diagonal containing it. In fact, $AO = \frac{1}{2}AC$.
- $$AO = \frac{1}{\sqrt{2}} AC$
  - _why:_ The factor $\frac{1}{\sqrt{2}}$ relates a square’s side to its diagonal, not half a diagonal. Since $O$ is the midpoint, $AO = \frac{1}{2}AC$.

## Card 15 — `basic`

**Front:** If a square base has side length $s$, what is the formula for the full base diagonal $d$?

**Back:** $$d = \sqrt{s^2 + s^2}$ or $d = s\sqrt{2}$

**Choices:**

- $$d = \sqrt{s^2 + s^2}$ or $d = s\sqrt{2}$ ✔
  - _why:_ The diagonal is the hypotenuse of a right-angled triangle with two sides of length $s$. Pythagoras gives $d^2=s^2+s^2$, so $d=s\sqrt{2}$.
- $$d = s + s$ or $d = 2s$
  - _why:_ Adding the side lengths calculates a two-side path around the square, not the direct diagonal. Pythagoras gives $d=\sqrt{s^2+s^2}=s\sqrt{2}$.
- $$d = \sqrt{s^2 - s^2}$ or $d = 0$
  - _why:_ This subtracts the squares instead of adding them, giving an impossible zero diagonal. Pythagoras requires $d=\sqrt{s^2+s^2}=s\sqrt{2}$.
- $$d = \frac{s}{\sqrt{2}}$ or $d = \frac{\sqrt{2}}{2}s$
  - _why:_ This gives half the square’s diagonal, which is the corner-to-centre distance. The full diagonal is $d=\sqrt{s^2+s^2}=s\sqrt{2}$.

## Card 16 — `cloze`

**Front:** The volume of a pyramid is found using the formula $V = \text{[...]} \times \text{base area} \times \text{vertical height}$.

**Back:** The volume of a pyramid is found using the formula $V = \boxed{\frac{1}{3}} \times \text{base area} \times \text{vertical height}$.

**Choices:**

- $$\frac{1}{3}$ ✔
  - _why:_ A pyramid with a given base area and perpendicular height has one-third the volume of the corresponding prism, so the required multiplier is $\frac{1}{3}$.
- $$\frac{1}{2}$
  - _why:_ The factor $\frac{1}{2}$ is used for triangular area, not pyramid volume. A pyramid occupies one-third of the corresponding prism, so the multiplier is $\frac{1}{3}$.
- $$1$
  - _why:_ Using a multiplier of $1$ calculates the volume of a prism with the same base and height. A pyramid has one-third that volume, requiring $\frac{1}{3}$.
- $$\frac{1}{4}$
  - _why:_ Dividing by four is not the pyramid volume relationship and usually comes from confusing the number of triangular faces with volume. The correct multiplier is $\frac{1}{3}$.

## Card 17 — `basic`

**Front:** What trigonometry ratio is typically used to find the height ($O$pposite) of a pyramid when given the angle and the base projection ($A$djacent)?

**Back:** Tangent ($\tan\theta = \frac{\text{opp}}{\text{adj}}$)

**Choices:**

- Tangent ($\tan\theta = \frac{\text{opp}}{\text{adj}}$) ✔
  - _why:_ Tangent directly relates the opposite and adjacent sides. The pyramid’s perpendicular height is opposite the angle, while the relevant base projection is adjacent to it.
- Sine ($\sin\theta = \frac{\text{opp}}{\text{hyp}}$)
  - _why:_ Sine relates the opposite side to the hypotenuse, not to the adjacent side. With the height and base projection involved, tangent is required because $\tan\theta=\frac{\text{opp}}{\text{adj}}$.
- Cosine ($\cos\theta = \frac{\text{adj}}{\text{hyp}}$)
  - _why:_ Cosine relates the adjacent side to the hypotenuse, so it does not directly connect the given base projection to the required height. Tangent links opposite and adjacent.
- Cotangent ($\cot\theta = \frac{\text{adj}}{\text{opp}}$)
  - _why:_ Cotangent uses the required sides in the reversed order, which can lead to solving the relationship incorrectly. The standard ratio here is tangent, $\tan\theta=\frac{\text{opp}}{\text{adj}}$.

## Card 18 — `basic`

**Front:** State the formula for $\cos\theta$ in a right-angled triangle.

**Back:** $$\cos\theta = \frac{\text{adjacent}}{\text{hypotenuse}}$

**Choices:**

- $$\cos\theta = \frac{\text{adjacent}}{\text{hypotenuse}}$ ✔
  - _why:_ Cosine is the ratio of the side adjacent to the chosen angle to the hypotenuse. This is the CAH part of the mnemonic SOHCAHTOA.
- $$\cos\theta = \frac{\text{hypotenuse}}{\text{adjacent}}$
  - _why:_ Reversing the fraction gives the reciprocal of cosine, called secant. Cosine itself is adjacent divided by hypotenuse, following the CAH part of SOHCAHTOA.
- $$\cos\theta = \frac{\text{opposite}}{\text{hypotenuse}}$
  - _why:_ Using the opposite side confuses cosine with sine. Cosine compares the adjacent side with the hypotenuse, so the correct formula is $\cos\theta=\frac{\text{adjacent}}{\text{hypotenuse}}$.
- $$\cos\theta = \frac{\text{adjacent}}{\text{opposite}}$
  - _why:_ Dividing adjacent by opposite is the reciprocal of tangent, not cosine. Cosine must use the hypotenuse as the denominator: $\cos\theta=\frac{\text{adjacent}}{\text{hypotenuse}}$.

## Card 19 — `basic`

**Front:** State the formula for $\sin\theta$ in a right-angled triangle.

**Back:** $$\sin\theta = \frac{\text{opposite}}{\text{hypotenuse}}$

**Choices:**

- $$\sin\theta = \frac{\text{opposite}}{\text{hypotenuse}}$ ✔
  - _why:_ Sine compares the side opposite the chosen angle with the hypotenuse. This is the SOH part of the mnemonic SOHCAHTOA.
- $$\sin\theta = \frac{\text{hypotenuse}}{\text{opposite}}$
  - _why:_ Reversing the fraction gives the reciprocal of sine, called cosecant. Sine itself is opposite divided by hypotenuse, following the SOH part of SOHCAHTOA.
- $$\sin\theta = \frac{\text{adjacent}}{\text{hypotenuse}}$
  - _why:_ Using the adjacent side confuses sine with cosine. Sine compares the opposite side with the hypotenuse, so the correct formula is $\sin\theta=\frac{\text{opposite}}{\text{hypotenuse}}$.
- $$\sin\theta = \frac{\text{opposite}}{\text{adjacent}}$
  - _why:_ Opposite divided by adjacent is tangent, not sine. Sine uses the hypotenuse as its denominator, giving $\sin\theta=\frac{\text{opposite}}{\text{hypotenuse}}$.

## Card 20 — `cloze`

**Front:** To maintain accuracy, you should keep [ ___ ] during working and only round the final answer.

**Back:** To maintain accuracy, you should keep extra decimal places during working and only round the final answer.

**Choices:**

- extra decimal places ✔
  - _why:_ Retaining extra decimal places prevents small rounding errors from accumulating across several calculations. Rounding should be postponed until the final answer is obtained.
- rounded intermediate values
  - _why:_ Keeping rounded intermediate values introduces premature rounding errors, which can affect the final result. Extra decimal places should be retained throughout the working instead.
- whole-number approximations
  - _why:_ Whole-number approximations discard too much precision during working and can substantially alter the final answer. Extra decimal places should be kept until the calculation is complete.
- fewer decimal places
  - _why:_ Using fewer decimal places increases the loss of precision at each stage. Extra decimal places should be retained during working, with rounding performed only at the end.

## Card 21 — `cloze`

**Front:** To maintain accuracy, you should keep extra decimal places during working and only [ ___ ].

**Back:** To maintain accuracy, you should keep extra decimal places during working and only round the final answer.

**Choices:**

- round the final answer ✔
  - _why:_ Rounding only the final answer preserves accuracy throughout the calculation while allowing the result to be presented to the precision requested by the question.
- round every intermediate answer
  - _why:_ Rounding every intermediate answer allows small errors to accumulate, particularly in multi-step 3D calculations. Keep extra decimal places during working and round only the final answer.
- truncate the final answer
  - _why:_ Truncation simply removes later digits rather than rounding according to the next digit, creating a biased result. The final answer should be rounded to the requested accuracy.
- round at each calculation step
  - _why:_ Rounding after each calculation step repeatedly reduces precision and may change the final result. Retain extra digits at every stage and round only the final answer.

## Card 22 — `basic`

**Front:** What is the first step recommended when solving 3D geometry problems in an exam?

**Back:** Mark the right angle and identify the specific 2D triangle being used.

**Choices:**

- Mark the right angle and identify the specific 2D triangle being used. ✔
  - _why:_ Marking the right angle and isolating the relevant 2D cross-section reveals which sides form a right-angled triangle, allowing Pythagoras or trigonometry to be applied correctly.
- Choose a trigonometric ratio and substitute all the values shown in the diagram.
  - _why:_ Choosing a trigonometric ratio before identifying the triangle risks labelling the wrong sides as opposite, adjacent or hypotenuse. First mark the right angle and isolate the relevant 2D triangle.
- Calculate the longest edge and use it as the hypotenuse of the triangle.
  - _why:_ Calculating the longest visible edge first may use an irrelevant triangle and wastes working. The reliable first step is to mark the right angle and identify the required 2D triangle.
- Sketch the whole solid and treat its outer edges as a single triangle.
  - _why:_ Treating the whole solid as one triangle ignores that trigonometric methods apply to a particular 2D cross-section. First mark the right angle and identify that specific triangle.
