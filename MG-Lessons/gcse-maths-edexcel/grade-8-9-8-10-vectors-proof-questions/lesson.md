# grade-8-9-8-10-vectors-proof-questions — lesson

_Lane: `gcse-maths-edexcel` · grade 8 · 6 content steps · 3 check questions (source: MathsGenie lessons)_

## Routes and position vectors

![Triangle with origin O, position vectors OA equals 4a and OB equals 3b, with AB and BA labelled](../assets/001-8e9fab70-eb9e-43f5-8985-e3ecbc1a1f09.jpeg)

Vectors proof questions turn a diagram into algebra. The first job is to write important position vectors from the origin, usually in terms of $a$ and $b$.

A side vector is found by subtracting position vectors in the correct order. The key route fact is
$$\vec{AB}=\vec{OB}-\vec{OA}$$

So if $\vec{OA}=4a$ and $\vec{OB}=3b$, then
$$\vec{AB}=3b-4a,\qquad \vec{BA}=4a-3b$$
Reversing the direction changes the sign, so order always matters.

## Points dividing a line in a ratio

![Line segment AB with point P between them, AP:PB equals 2:1, and position vectors OA, OB and OP shown](../assets/002-cd0b6485-8a19-4a3d-bd2e-08ecde0cca3c.jpeg)

If P lies on AB with $\text{AP}:\text{PB}=m:n$, then P is $\frac{m}{m+n}$ of the way from A to B. This lets you turn a ratio statement into a vector step along the line.

Starting from A gives
$$\vec{OP}=\vec{OA}+\frac{m}{m+n}\vec{AB}$$
This is usually the safest method because you can see how far you travel from A.

You can also use the weighted form
$$\vec{OP}=\frac{n}{m+n}\vec{OA}+\frac{m}{m+n}\vec{OB}$$
The opposite weights are easy to mix up, so check which part of the ratio is attached to which end.

## Worked example: finding $k$

In triangle OAB, $\vec{OA}=3a$ and $\vec{OB}=2b$. Point P lies on AB with the ratio $\text{AP}:\text{PB}=2:1$, and we are given that $\vec{OP}=k(3a+4b)$. Our goal is to determine the value of the scalar $k$.

Because P is $\frac{2}{3}$ of the way from A to B, we use the vector addition $\vec{OP}=\vec{OA}+\frac{2}{3}\vec{AB}$. We first find the vector for the side $\vec{AB} = \vec{OB} - \vec{OA} = 2b-3a$.

Substitute and simplify the expression for $\vec{OP}$ carefully:
$$
\begin{aligned}
\vec{OP}&=3a+\frac{2}{3}(2b-3a)\\
&=3a+\frac{4}{3}b-2a\\
&=a+\frac{4}{3}b
\end{aligned}
$$
This gives us the vector in its simplest linear form.

Now factor to match the given form $k(3a+4b)$:
$$
\vec{OP}=\frac{1}{3}(3a+4b)
$$
Comparing terms, we find $k=\frac{1}{3}$. A common mistake is using $\frac{1}{3}\vec{AB}$ instead of $\frac{2}{3}\vec{AB}$ when setting up the initial path.

## Worked example: proving points are collinear

In triangle $OAB$, $\vec{OA}=6a$ and $\vec{OB}=4b$. Point $C$ lies on $OA$ with $\text{OC}:\text{CA}=2:1$, $M$ is the midpoint of $AB$, and $D$ lies on $OB$ extended with $\text{OB}:\text{OD}=1:2$. We want to show that $C$, $M$ and $D$ are collinear.

First find the position vectors:
$$\vec{OC}=4a,\qquad \vec{OM}=\frac{1}{2}(6a+4b)=3a+2b,\qquad \vec{OD}=8b$$
Writing these first makes the rest of the proof much cleaner.

Use $C$ as the common starting point. Then:
$$\vec{CM}=\vec{OM}-\vec{OC}=(3a+2b)-4a=-a+2b$$
and
$$\vec{CD}=\vec{OD}-\vec{OC}=8b-4a=-4a+8b$$

Now compare the two vectors:
$$\vec{CD}=4\vec{CM}$$
Since they are scalar multiples and both start from $C$, the points $C$, $M$ and $D$ lie on the same straight line.

## Shape facts and extension tricks

Harder proofs often hide extra vector facts inside shapes. In a parallelogram, if $O$ is one corner and $A$ and $B$ are adjacent corners, then the opposite corner $C$ satisfies the following relation:

$$$\vec{OC}=\vec{OA}+\vec{OB}$$

Regular hexagons also give useful shortcuts. Opposite vertices have opposite position vectors, and adjacent vertex relations can often be written using $p$ and $q$, such as $\vec{OT}=-q$.

If a point lies on an extension, put the unknown in the known direction. For example, if $E$ lies on $OB$ extended, write $\vec{BE}=tb$ so $\vec{OE}=(3+t)b$, then use collinearity and compare coefficients of $a$ and $b$.

## Worked example: finding an unknown extension vector

In triangle OAB, $\vec{OA}=6a$ and $\vec{OB}=3b$. Point C lies on OA with $\text{OC}:\text{CA}=5:1$, point D lies on AB with $\text{AD}:\text{DB}=1:2$, and OB is extended to E. Given that C, D and E are collinear, find $\vec{BE}$.

First find the position vectors for points C and D. Using the given ratios, we calculate:
$$\vec{OC}=5a,\qquad \vec{OD}=\frac{2}{3}(6a)+\frac{1}{3}(3b)=4a+b$$
Now let $\vec{BE}=tb$, which implies $\vec{OE}=(3+t)b$.

Form two vectors starting from point C to represent segments of the line CDE:
$$\vec{CD}=\vec{OD}-\vec{OC}=(4a+b)-5a=-a+b$$
$$\vec{CE}=\vec{OE}-\vec{OC}=(3+t)b-5a=-5a+(3+t)b$$

Because C, D and E are collinear, we write $\vec{CE}=\lambda\vec{CD}$. Comparing coefficients of $a$ gives $-5=-\lambda$, so $\lambda=5$. Comparing coefficients of $b$ gives $3+t=5$, so $t=2$ and therefore $\vec{BE}=2b$.

## Check yourself

1. In triangle OAB, $\vec{OA}=6a$ and $\vec{OB}=2b$. What is $\vec{AB}$?

   - $$2b-6a$ ✔

   - $$6a-2b$

   - $$6a+2b$

   - $$4b$

   _Explanation:_ $$\vec{AB}$ means from A to B, so you subtract $\vec{OA}$ from $\vec{OB}$. The common wrong answer is $6a-2b$ because that is actually $\vec{BA}$, the vector in the opposite direction.

2. A student writes $\vec{OP}=\vec{OA}+\frac{1}{3}\vec{AB}$ when $\text{AP}:\text{PB}=2:1$. What is the mistake?

   - They used the fraction from B instead of the fraction from A ✔

   - They should have used $\vec{OP}=\vec{OA}+\frac{3}{2}\vec{AB}$

   - They should have added $\vec{OA}$ and $\vec{OB}$ directly

   - There is no mistake

   _Explanation:_ $$2:1$ means P is two out of three equal parts from A, so the step along AB should be $\frac{2}{3}\vec{AB}$. The common wrong answer is $\frac{3}{2}\vec{AB}$ because that would place P beyond B, not between A and B.

3. In triangle OAB, $\vec{OB}=3b$ and E lies on OB extended beyond B. Which is the best way to represent E?

   - $$\vec{BE}=tb$ ✔

   - $$\vec{BE}=ta$

   - $$\vec{OE}=ta+tb$

   - $$\vec{AE}=tb$

   _Explanation:_ E stays on the same line and in the same direction as OB, so the unknown vector must be a scalar multiple of $b$. The common wrong answer is $\vec{OE}=ta+tb$ because that is a general vector and may not lie on line OB at all.
