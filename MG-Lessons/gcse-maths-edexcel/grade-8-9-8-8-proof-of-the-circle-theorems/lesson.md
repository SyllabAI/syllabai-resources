# grade-8-9-8-8-proof-of-the-circle-theorems — lesson

_Lane: `gcse-maths-edexcel` · grade 8 · 6 content steps · 3 check questions (source: MathsGenie lessons)_

## The proof engine

Most circle theorem proofs start the same way: draw the centre $O$ and join it to points on the circumference. Equal radii create isosceles triangles, and isosceles triangles create equal base angles.

From there, use angle facts you already know: angles in a triangle add to $180^\circ$, angles on a straight line add to $180^\circ$, and angles around a point add to $360^\circ$. This is enough to build the main circle theorems from scratch.

The key chain is: angle at the centre is twice the angle at the circumference, then same segment, then cyclic quadrilateral and tangent-chord results. Always identify the chord or arc an angle stands on, and give a reason for each step.

## Proving the angle at the centre theorem

![Circle with centre O, chord PR, radii OP, OQ and OR, and angle at Q split into x and y compared with central angle POR](../assets/001-fb1383fc-2235-4a26-8aa8-d3cc4623a1a7.jpeg)

Let $\angle PQO = x$ and $\angle OQR = y$. Because $OP=OQ$ and $OQ=OR$, triangles $OPQ$ and $OQR$ are isosceles.

So $\angle OPQ = x$ and $\angle ORQ = y$. Then $\angle POQ = 180^\circ - 2x$ and $\angle QOR = 180^\circ - 2y$.

Angles around $O$ add to $360^\circ$, so $\angle POR = 360^\circ - (180^\circ - 2x) - (180^\circ - 2y) = 2x + 2y$. Since $\angle PQR = x+y$, we get $\angle POR = 2\angle PQR$.

## Proving the angle in a semicircle

![Circle with diameter AC through centre O and point B on the circumference, showing angle ABC split into x and y and central angles AOB and BOC](../assets/002-95af3e54-90ae-494f-a9be-14fb9cf3420c.jpeg)

If $AC$ is a diameter, then $A$, $O$, and $C$ lie on one straight line. Let $\angle ABO = x$ and $\angle OBC = y$, so that the total angle $\angle ABC = x+y$.

Because $OA=OB$ and $OB=OC$ (as they are all radii), triangles $AOB$ and $BOC$ are isosceles. Consequently, the central angles can be expressed as $\angle AOB = 180^\circ - 2x$ and $\angle BOC = 180^\circ - 2y$.

These central angles lie on the straight line diameter, so their sum must be $180^\circ$:
$$(180^\circ - 2x) + (180^\circ - 2y) = 180^\circ$$

Simplifying the equation gives $x+y=90^\circ$. Therefore $\angle ABC = 90^\circ$, proving the theorem. Note that while this is a special case of the angle at the centre theorem, this radii-based proof is required if the exam specifies not to use other circle theorems.

## Two quick consequences

Suppose $\angle ABD$ and $\angle ACD$ both stand on chord $AD$. Each is half of the same central angle $\angle AOD$, so $\angle ABD = \angle ACD$.

Now take a cyclic quadrilateral $ABCD$. Angles $\angle ABC$ and $\angle ADC$ stand on the two arcs from $A$ to $C$, and the matching central angles make a full $360^\circ$ around the centre.

Each circumference angle is half its central angle, so $\angle ABC + \angle ADC = 180^\circ$. Only opposite angles must add to $180^\circ$; adjacent angles do not have to.

## Proving the tangent-chord theorem

![Circle with tangent at C, chord BC, angle BAC in the opposite segment, and radii OB and OC](../assets/003-69ae899d-d701-42fc-bc87-296ce0b8f318.jpeg)

Draw radius $OC$ to the point of contact. Since a radius is perpendicular to a tangent, the angle between $OC$ and the tangent is $90^\circ$.

Let $\angle OCB = y$. Then the angle between the tangent and chord $BC$ is $90^\circ - y$. Because $OB=OC$ (both are radii), triangle $OBC$ is isosceles, so $\angle OBC = y$.

This gives $\angle BOC = 180^\circ - 2y$. By the circle theorem relating the center and circumference, $\angle BAC = \frac{1}{2}(180^\circ - 2y) = 90^\circ - y$. Therefore, the angle between the tangent and chord equals the angle in the opposite segment.

This theorem is also called the alternate segment theorem. The key construction for this proof is always drawing the radius to the point of contact.

## Model proof writing

Example: prove $\angle ABD = \angle ACD$ when both angles stand on chord $AD$. First draw $OA$ and $OD$, because these create the central angle on the same chord.

Both circumference angles are half of $\angle AOD$. So $\angle AOD = 2\angle ABD$ and $\angle AOD = 2\angle ACD$.

Therefore $2\angle ABD = 2\angle ACD$, so $\angle ABD = \angle ACD$. This is neat because every line points back to the same chord $AD$.

If an exam question bans circle theorems, replace the quoted theorem with the radii proof from earlier in the lesson. Never jump from the diagram to the final answer with no reasons.

## Check yourself

1. When points $A$ and $B$ lie on a circle with centre $O$, why is triangle $AOB$ isosceles?

   - Because $OA$ and $OB$ are radii of the same circle ✔

   - Because $AB$ is always a diameter

   - Because opposite angles in a cyclic quadrilateral are equal

   - Because a tangent meets a chord at $90^\circ$

   _Explanation:_ $$OA$ and $OB$ are both radii, so they are equal and triangle $AOB$ is isosceles. The common wrong answer is B, but a chord is only a diameter if it passes through the centre.

2. In cyclic quadrilateral $ABCD$, $\angle BAD = 73^\circ$. What is $\angle BCD$?

   - $$73^\circ$

   - $$107^\circ$ ✔

   - $$146^\circ$

   - $$287^\circ$

   _Explanation:_ Opposite angles in a cyclic quadrilateral add to $180^\circ$, so $\angle BCD = 180^\circ - 73^\circ = 107^\circ$. The common wrong answer is A because students sometimes mix this up with angles in the same segment, but these two angles are opposite, not on the same chord.

3. A student writes, "Triangle $OBC$ is isosceles because $OB$ and $BC$ are radii." What is the flaw in the proof?

   - $$BC$ is a chord, not a radius ✔

   - Isosceles triangles cannot be used in circle proofs

   - Two equal sides are not enough to show a triangle is isosceles

   - The centre must lie on the circumference

   _Explanation:_ A radius must run from the centre to the circumference, so $OB$ is a radius but $BC$ is a chord. The common wrong answer is C, but two equal sides are exactly what make a triangle isosceles.
