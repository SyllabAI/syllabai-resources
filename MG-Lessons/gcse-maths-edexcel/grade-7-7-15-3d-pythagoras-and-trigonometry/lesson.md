# grade-7-7-15-3d-pythagoras-and-trigonometry — lesson

_Lane: `gcse-maths-edexcel` · grade 7 · 6 content steps · 4 check questions (source: MathsGenie lessons)_

## From 3D to a right triangle

Most 3D questions are really about a hidden 2D right-angled triangle inside a cuboid, prism or pyramid. First decide which flat triangle you can draw and label.

Use Pythagoras when you need a missing side: $a^2 + b^2 = c^2$. Use SOHCAHTOA for angles, and choose the ratio from the sides you actually know.

A space diagonal goes through the inside of a solid, while a plane is just a flat face. The angle between a line and a plane is measured using the line's projection, like its shadow, on that face.

## Worked example: cuboid space diagonal

![Cuboid with edge lengths 6 cm, 8 cm and 4 cm showing base diagonal AC and space diagonal AG](../assets/001-909248b8-5d66-4d76-83fc-354f7e43815e.jpeg)
In a cuboid with edges 6 cm, 8 cm and 4 cm, the space diagonal $AG$ is not on one face. So we first find the base diagonal $AC$, then use that with the height.

Across the base rectangle, triangle $ABC$ is right-angled, so we use Pythagoras' theorem:
$$AC^2 = 6^2 + 8^2 = 100$$
Hence the length of the base diagonal $AC$ is 10 cm.

Now triangle $ACG$ is right-angled, so we apply the theorem again:
$$AG^2 = 10^2 + 4^2 = 116$$
Therefore $AG = \sqrt{116} \approx 10.8$ cm. This is why cuboids often need Pythagoras twice, although the shortcut is $d^2 = l^2 + w^2 + h^2$.

## Working backwards to find a missing edge

If the space diagonal is already given, it acts as the hypotenuse of the 3D right-angled triangle. This means you must rearrange the Pythagorean formula and subtract the known squared edges.

For a cuboid with space diagonal 13 cm and edges 5 cm and 6 cm, let the missing edge be $x$. The relationship is defined as:
$$13^2 = 5^2 + 6^2 + x^2$$

Rearranging gives $x^2 = 169 - 25 - 36 = 108$. Calculating the root results in:
$$x = \sqrt{108} \approx 10.4$$
The common mistake is to add the squares again, even though the diagonal is already the hypotenuse.

## Worked example: angle in a cuboid

Suppose a cuboid has $AE = 5$ cm, $AD = 6$ cm and $DC = 8$ cm, and you want to calculate angle $ECA$. The middle letter shows the angle is at vertex $C$, so the useful triangle for our calculations is $EAC$.

First find the base diagonal length using the dimensions of the bottom face:
$$AC^2 = 6^2 + 8^2 = 100$$
This result gives $AC = 10$ cm. In the vertical triangle $EAC$, the side opposite angle $ECA$ is 5 cm and the adjacent side is 10 cm.

Because we know the opposite and adjacent side lengths, we use the tangent ratio:
$$\tan \theta = \frac{5}{10}$$
Hence, the angle is found using the inverse tangent: $\theta = \tan^{-1}(0.5) \approx 26.6^\circ$.

## Angle between a line and a plane

The angle between a line and a plane is not usually taken with a vertical edge. It is defined as the angle between the line and its projection on the plane, which is essentially the line's shadow on that flat face.

In a prism, suppose $F$ is vertically above $C$, with $CD = 18$ cm, $AD = 25$ cm and angle $FDC = 40^0$. First find the vertical height using triangle $FDC$:
$$CF = 18 \tan 40^\circ \approx 15.1$$

The projection of $AF$ onto the base plane is $AC$, which we calculate using Pythagoras' theorem:
$$AC = \sqrt{25^2 + 18^2} \approx 30.8$$
Finally, use triangle $AFC$ to find the angle $\theta$ via the tangent ratio $\tan \theta = \frac{15.1}{30.8}$, so $\theta \approx 26.1^\circ$.

## Worked example: square-based pyramid

![Square-based pyramid with base ABCD, centre O, apex E, diagonal AC and vertical height EO marked](../assets/002-943292c1-45c8-4645-8da6-9c824c48aa5f.jpeg)

In a square-based pyramid with base side 8 cm, the centre $O$ sits halfway along the base diagonal $AC$. If the apex $E$ is 12 cm vertically above $O$, then angle $EAC$ can be found using triangle $EAO$.

First find the base diagonal using the dimensions of the square base:
$$AC^2 = 8^2 + 8^2 = 128$$
So $AC = 8\sqrt{2}$ and therefore $AO = 4\sqrt{2}$.

In right-angled triangle $EAO$, we apply trigonometry to find the angle:
$$\tan \theta = \frac{12}{4\sqrt{2}}$$
so $\theta = \tan^{-1}\left(\frac{12}{4\sqrt{2}}\right) \approx 64.8^\circ$. If you later need volume, use $V = \frac{1}{3} \times \text{base area} \times \text{vertical height}$.

## Check yourself

1. To find the space diagonal of a cuboid with edges 6 cm, 8 cm and 4 cm, what is usually the best first step?

   - Find the diagonal of the 6 cm by 8 cm face ✔

   - Multiply $6 \times 8 \times 4$

   - Add $6 + 8 + 4$

   - Find the area of the top face

   _Explanation:_ You first need a right-angled triangle on one face, because that face diagonal combines with the height to make a second right-angled triangle. A common wrong idea is C, but diagonals are not found by adding side lengths.

2. A cuboid has space diagonal 17 cm and two edges of 8 cm and 12 cm. Which equation correctly starts the method for finding the missing edge $x$?

   - $$x^2 = 17^2 - 8^2 - 12^2$ ✔

   - $$x^2 = 17^2 + 8^2 + 12^2$

   - $$x^2 = 8^2 + 12^2 - 17^2$

   - $$x = 17 - 8 - 12$

   _Explanation:_ The space diagonal is the hypotenuse, so you subtract the other squared edges to isolate $x^2$. B is the common wrong choice because it treats the question as if you were finding the diagonal from the edges, not working backwards from it.

3. In the prism example, the angle between line $AF$ and plane $ABCD$ is measured between $AF$ and which line on the plane?

   - $$AC$ ✔

   - $$CF$

   - $$DC$

   - $$FD$

   _Explanation:_ $$AC$ is the projection of $AF$ onto the base plane, so the required angle is between $AF$ and $AC$. $CF$ is the common wrong choice because it helps find the height, but it is not the shadow of $AF$ on the plane.

4. Stretch: A square-based pyramid has base side 12 cm and angle $PAC = 62^{\circ}$, where $P$ is vertically above the centre of the base. What is the volume, to 3 significant figures?

   - $$255 \, \text{cm}^3$

   - $$383 \, \text{cm}^3$

   - $$766 \, \text{cm}^3$ ✔

   - $$1530 \, \text{cm}^3$

   _Explanation:_ Hint: Use half the base diagonal to get the distance from a corner to the centre. The base diagonal is $12\sqrt{2}$, so $AO = 6\sqrt{2}$ and the vertical height is $PO = 6\sqrt{2}\tan 62^{\circ} \approx 15.96$. Then $V = \frac{1}{3} \times 12^2 \times 15.96 \approx 766 \, \text{cm}^3$, so C is correct; D is the common wrong answer from forgetting the $\frac{1}{3}$ in the pyramid volume formula.
