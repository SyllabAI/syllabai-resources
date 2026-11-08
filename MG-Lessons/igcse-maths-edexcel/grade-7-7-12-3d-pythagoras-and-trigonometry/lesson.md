# grade-7-7-12-3d-pythagoras-and-trigonometry — lesson

_Lane: `igcse-maths-edexcel` · grade 7 · 5 content steps · 3 check questions (source: MathsGenie lessons)_

## Make a 2D triangle first

![Cuboid with base diagonal AC and space diagonal AG labelled, dimensions 9 cm, 5 cm and 6 cm](../assets/001-722c4485-bce0-4132-aab0-6ecb635c6780.jpeg)

In 3D questions, the formulas are the same as in 2D right-angled triangles. The main skill is spotting which flat triangle you need inside the solid.

For lengths, use Pythagoras: $a^2+b^2=c^2$. For angles or missing sides, use SOH CAH TOA:

$$\sin\theta=\frac{\text{opposite}}{\text{hypotenuse}}, \cos\theta=\frac{\text{adjacent}}{\text{hypotenuse}}, \tan\theta=\frac{\text{opposite}}{\text{adjacent}}$$

In a cuboid, it is often easiest to find a face diagonal first and then combine it with the height. The long line joining opposite corners through the inside is called a space diagonal.

## Worked example: cuboid space diagonal

A cuboid has length 9 cm, depth 5 cm and height 6 cm. First find the diagonal across the base, because the space diagonal belongs to a second right-angled triangle.

Start with the base. The diagonal across the base is the hypotenuse of a right-angled triangle:
$$AC^2=9^2+5^2=106,\qquad AC=\sqrt{106}$$
So the base diagonal is $\sqrt{106}$ cm.

Now use that base diagonal with the height 6 cm. This gives a new right-angled triangle inside the cuboid:
$$AG^2=AC^2+6^2=106+36=142,\qquad AG=\sqrt{142}\approx 11.9$$
So the space diagonal is 11.9 cm to 3 significant figures.

Once you understand the two-step method, you can remember the shortcut $d^2=l^2+w^2+h^2$. The shortcut works because you are really applying Pythagoras twice.

## Work backwards and choose the correct side

If a space diagonal is given and one edge is missing, rearrange the squared relationship instead of adding lengths directly. For a cuboid with space diagonal 12 cm, width 5 cm and height 6 cm, write:

$$$12^2=5^2+x^2+6^2$$ Then $x^2=83$, so $x=\sqrt{83}\approx 9.11$ cm.

For angles, first decide which 2D triangle actually contains the angle. In a cuboid with base 8 cm by 6 cm and height 4 cm, the angle between the space diagonal and the base uses the base diagonal as the adjacent side.

Find the base diagonal first. Then use tangent. $$AC=\sqrt{8^2+6^2}=10,\qquad \tan\theta=\frac{4}{10}$$ So $\theta\approx 21.8^\circ$. A common mistake is to use 8 cm as the adjacent side, but that edge is not the projection of the space diagonal onto the base.

## Angles between a line and a plane

![Line AF above base plane ABCD with projection AC and vertical height FC marked](../assets/002-7b561f22-edd8-49a7-bb48-4cff6f8d1a08.jpeg)

The angle between a line and a plane is measured using the line's projection on the plane. In the diagram, the angle between $AF$ and the base plane is defined as the angle between $AF$ and its projection $AC$.

Suppose the base $ABCD$ is a rectangle with $AD=30$ cm and $CD=16$ cm, and $\angle FDC=35^{\circ}$. First find the diagonal $AC$ of the base, which is the projection of $AF$, and the vertical height $FC$:

$$AC=\sqrt{30^2+16^2}=34,\qquad FC=16\tan 35^{\circ}\approx 11.2$$

So the projection on the base is 34 cm long and the rise is about 11.2 cm.

Now work in right-angled triangle $AFC$ to find $\theta=\angle FAC$. Use the tangent ratio because you know the opposite side ($FC$) and adjacent side ($AC$):

$$\tan\theta=\frac{FC}{AC}=\frac{11.2}{34},\qquad \theta\approx 18.2^{\circ}$$

So the angle between $AF$ and the plane is about $18.2^{\circ}$. If you skip the step of finding the projection, you are likely to choose the wrong adjacent side.

## Square-based pyramids and volume

![Square-based pyramid with apex P above centre O, base diagonal AC, sloping edge PA, and angle PAC marked 65 degrees](../assets/003-ef15719b-2872-4f58-87cb-d5f6e73638d8.jpeg)

In a symmetrical square-based pyramid, the vertical height goes from the apex straight down to the centre of the square base. This helpful triangle usually includes a corner of the base, the centre $O$, and the apex $P$.

Suppose the base side is 15 cm and $\angle PAC = 65^\circ$. Since the diagonal of the square base is $15\sqrt{2}$, we can find the distance from the corner to the centre $O$:
$$AO = \frac{15\sqrt{2}}{2} \approx 10.6$$
Because $A$, $O$, and $C$ are on one straight line, the angle $\angle PAC$ is equivalent to $\angle PAO$.

We can now use the tangent ratio to find the vertical height $PO$:
$$PO = AO \tan 65^\circ \approx 22.7$$
So the perpendicular height is approximately 22.7 cm. Finding this vertical height is a necessary step before calculating the volume.

Finally, we apply the pyramid volume formula using the base area and vertical height:
$$V = \frac{1}{3} \times 15^2 \times 22.7 \approx 1710$$
So the volume is about 1710 cm^3. A common mistake in these problems is using the sloping edge length instead of the vertical height.

## Check yourself

1. In a 3D solid, what is a space diagonal?

   - A line joining opposite vertices through the inside of the solid ✔

   - Any diagonal drawn on one face

   - A vertical edge

   - The line from the centre of the solid to one corner

   _Explanation:_ A space diagonal joins one vertex to the opposite vertex through the interior of the solid. The common wrong answer B describes a face diagonal, which lies on a surface rather than through the solid.

2. A cuboid has base 8 cm by 6 cm and height 4 cm. What is the angle between its space diagonal and the base plane?

   - $$21.8^\circ$ ✔

   - $$26.6^\circ$

   - $$36.9^\circ$

   - $$68.2^\circ$

   _Explanation:_ The projection on the base is the base diagonal, $AC=\sqrt{8^2+6^2}=10$. Then $\tan\theta=\frac{4}{10}$, so $\theta=21.8^\circ$. The common wrong answer $26.6^\circ$ comes from using 8 cm as the adjacent side instead of the base diagonal. Hint: The angle with a plane uses the projection on that plane.

3. A square-based pyramid has base side 8 cm. Its apex E is vertically above the centre of the base, 12 cm high. What is $\angle EAC$?

   - $$64.8^\circ$ ✔

   - $$56.3^\circ$

   - $$46.7^\circ$

   - $$25.2^\circ$

   _Explanation:_ The base diagonal is $AC=8\sqrt{2}$, so $AO=\frac{AC}{2}=4\sqrt{2}$. Since $O$ lies on $AC$, $\angle EAC=\angle EAO$, and $\tan\theta=\frac{12}{4\sqrt{2}}$. The common wrong answer $56.3^\circ$ comes from using the side length 8 cm as the adjacent side instead of half the diagonal.
