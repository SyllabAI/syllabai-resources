# grade-8-9-8-9-vectors-proof-questions — lesson

_Lane: `igcse-maths-edexcel` · grade 8 · 5 content steps · 3 check questions (source: MathsGenie lessons)_

## Core setup: position vectors and ratios

![Triangle with origin O, vectors OA and OB, and point P dividing AB in the ratio 2:3](../assets/001-vectors-proof-op-6ec28c1f33e18ed3.png)

In vector proof questions, every important point is usually described from a fixed origin $O$. Most answers are then written using base vectors such as $a$ and $b$.

The rule you use all the time is end minus start. That gives
$$\vec{AB}=\vec{OB}-\vec{OA}$$
and it prevents the common mistake of reversing the direction.

If P divides AB in the ratio $AP:PB=m:n$, then P is $\frac{m}{m+n}$ of the way from A to B. So
$$\vec{OP}=\vec{OA}+\frac{m}{m+n}\vec{AB}$$
using the part measured from the starting end A.

## Worked example: finding a ratio point

Suppose $\vec{OA}=2a$ and $\vec{OB}=5b$, and point $P$ divides $AB$ so that $AP:PB=2:3$. We begin the process by calculating the vector for the whole segment:
$$\vec{AB}=\vec{OB}-\vec{OA}=5b-2a$$

Point $P$ is $\frac{2}{5}$ of the way from $A$ to $B$ because the line is split into $2+3=5$ equal parts. Using the starting point $A$, we can find the position vector $\vec{OP}$:
$$\vec{OP}=\vec{OA}+\frac{2}{5}\vec{AB}=2a+\frac{2}{5}(5b-2a)=\frac{6}{5}a+2b$$

Many exam questions require the final answer to be in a factored form. In this example, we factor out the common scalar to find $k = \frac{2}{5}$:
$$\frac{6}{5}a+2b=\frac{2}{5}(3a+5b)$$

## The straight-line proof test

![Parallelogram OABC with D on OC, E midpoint of BC, and A D E on one straight line](../assets/002-5402cd07-39cb-477e-a01c-fbcbf159262b.jpeg)
When a question says "show that three points are on one straight line", your target is collinearity. The cleanest proof is to show two vectors with the same starting point are scalar multiples of each other.

For example, to prove $A, D$ and $E$ are collinear, compare vectors from $A$. You want a result like:

$$$\vec{AD}=\lambda \vec{AE}$$

for some number $\lambda$. Do not compare $\vec{OD}$ and $\vec{OE}$ unless the line is supposed to pass through $O$. That common mistake only tells you about a line through the origin, not about the line through $A$.

## Worked example: proving collinearity in a parallelogram

In parallelogram $OABC$, let $\vec{OA}=3a$ and $\vec{OB}=3b$. We start by finding the vector for the diagonal $OC$ and the position of point $D$ on that diagonal.
$$\vec{OC}=3a+3b,\qquad \vec{OD}=\frac{2}{3}\vec{OC}=2a+2b$$

Point $E$ is the midpoint of $BC$. To find its position vector, we calculate the average of vectors $\vec{OB}$ and $\vec{OC}$ as shown below:
$$\vec{OE}=\frac{1}{2}(\vec{OB}+\vec{OC})=\frac{1}{2}(3b+3a+3b)=\frac{3}{2}a+3b$$

Now we switch to vectors starting from point $A$. We calculate $\vec{AD}=\vec{OD}-\vec{OA}=(2a+2b)-3a=-a+2b$, as straight-line proofs require a common starting point for comparison.

Next, we calculate the vector for $E$ relative to $A$ and compare it to our result for $D$:
$$\vec{AE}=\vec{OE}-\vec{OA}=\left(\frac{3}{2}a+3b\right)-3a=\frac{3}{2}(-a+2b)=\frac{3}{2}\vec{AD}$$
Since $\vec{AE}$ is a scalar multiple of $\vec{AD}$, the points $A, D$, and $E$ are collinear.

## Unknown point on an extension

When a point is on an extension, introduce an unknown scalar on that line. For example, if $E$ is on $OB$ extended, we can write $\vec{BE}=xb$, which leads to $\vec{OE}=(3+x)b$.

Consider a case where $\vec{OA}=8a$ and $\vec{OB}=3b$. Point $C$ satisfies $OC:CA=3:1$ and $D$ satisfies $AD:DB=1:2$, placing $C$ on $OA$ and $D$ one third of the way from $A$ to $B$. $$\vec{OC}=6a,\qquad \vec{OD}=8a+\frac{1}{3}(3b-8a)=\frac{16}{3}a+b$$

Because $C, D$, and $E$ are collinear, we compare vectors starting from $C$. We first form these two vectors to establish a relationship: $$\vec{CD}=\vec{OD}-\vec{OC}=-\frac{2}{3}a+b,\qquad \vec{CE}=\vec{OE}-\vec{OC}=-6a+(3+x)b$$

Set $\vec{CD}=\lambda \vec{CE}$ and compare coefficients of $a$ and $b$. From $-\frac{2}{3}=-6\lambda$ we get $\lambda=\frac{1}{9}$; then solving $1=\frac{1}{9}(3+x)$ gives $x=6$ and $\vec{BE}=6b$.

## Check yourself

1. If $\vec{OA}=4a$ and $\vec{OB}=7b$, what is $\vec{AB}$?

   - $$7b-4a$ ✔

   - $$4a-7b$

   - $$4a+7b$

   - $$\frac{1}{2}(7b-4a)$

   _Explanation:_ $$\vec{AB}$ means from A to B, so use end minus start: $\vec{OB}-\vec{OA}=7b-4a$. The common wrong answer $4a-7b$ is actually $\vec{BA}$, which points in the opposite direction.

2. To prove that A, D and E are collinear, which pair of vectors is usually the most useful to compare?

   - $$\vec{AD}$ and $\vec{AE}$ ✔

   - $$\vec{OD}$ and $\vec{OE}$

   - $$\vec{OA}$ and $\vec{OB}$

   - The lengths $AD$ and $AE$

   _Explanation:_ You need two vectors that start at the same point on the line you are testing, so comparing $\vec{AD}$ and $\vec{AE}$ is the right method. The common wrong choice is $\vec{OD}$ and $\vec{OE}$, but that only gives information about directions from O.

3. Stretch: In the extension example, what is the value of $x$ in $\vec{BE}=xb$?

   - 6 ✔

   - 3

   - 9

   - 12

   _Explanation:_ Hint: Find $\lambda$ from the $a$ coefficients first. Compare coefficients after setting $\vec{CD}=\lambda \vec{CE}$. From $-\frac{2}{3}=-6\lambda$ you get $\lambda=\frac{1}{9}$, then $1=\frac{1}{9}(3+x)$ gives $3+x=9$ and so $x=6$. The common wrong answer $9$ comes from forgetting the final subtraction of $3$.
