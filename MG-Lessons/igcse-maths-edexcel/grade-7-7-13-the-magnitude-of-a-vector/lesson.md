# grade-7-7-13-the-magnitude-of-a-vector — lesson

_Lane: `igcse-maths-edexcel` · grade 7 · 5 content steps · 3 check questions (source: MathsGenie lessons)_

## Magnitude means length

![Vector from the origin to point (x, y) split into horizontal and vertical components, with the full length labelled magnitude](../assets/001-cc20a0f1-15fa-4694-a725-66800dd15c3b.jpeg)
A vector describes both size and direction. In a column vector $\begin{pmatrix} x \\ y \end{pmatrix}$, the top number is the horizontal movement and the bottom number is the vertical movement.

The magnitude of a vector is its length, written as $|\vec{v}|$. The components form a right-angled triangle, so we use Pythagoras' theorem to calculate this distance.

$$$|\vec{v}|=\sqrt{x^2+y^2}$$

For example, $\begin{pmatrix} 5 \\ -2 \end{pmatrix}$ means 5 units right and 2 units down. A negative component changes direction, but the magnitude result is still always positive.

## Worked example with a negative component

Suppose $\vec{v}=\begin{pmatrix} -8 \\ 15 \end{pmatrix}$. The negative sign tells you the horizontal part points left, but it does not make the length negative.

Substitute carefully, keeping the negative in brackets when you square. This is why $(-8)^2=64$, not $-64$. $$ |\vec{v}|=\sqrt{(-8)^2+15^2}=\sqrt{64+225}=\sqrt{289} $$

Now take the square root to finish the calculation. So the magnitude is $17$.

## Exact answers and surds

Sometimes the square root of the magnitude is not a whole number. In these cases, you should provide an exact answer and simplify the surd whenever possible.

For $\vec{p}=\begin{pmatrix} 10 \\ -4 \end{pmatrix}$, start with the magnitude formula and simplify the value inside the root first. This gives the unsimplified exact magnitude:
$$|\vec{p}|=\sqrt{10^2+(-4)^2}=\sqrt{100+16}=\sqrt{116}$$

Now look for a square factor inside $116$ to simplify the expression. Since $116=4\times29$, we can take the square root of 4 to find the simplified exact magnitude:
$$|\vec{p}|=2\sqrt{29}$$

## Find the vector first, then the magnitude

![Triangle with vectors AB, BC, and AC showing that AC equals AB plus BC](../assets/002-0543d82f-09f2-4310-ba34-6f180b4b8934.jpeg)

Many questions do not give you the vector whose magnitude you need straight away. To solve these, you must first build the correct vector using a path such as $\vec{AC}=\vec{AB}+\vec{BC}$.

If you are given $\vec{CB}$ instead of $\vec{BC}$, reverse it by changing both signs. With $\vec{AB}=\begin{pmatrix} 5 \\ -7 \end{pmatrix}$ and $\vec{CB}=\begin{pmatrix} -1 \\ 4 \end{pmatrix}$, we first calculate the necessary components.

$$$\vec{BC}=-\vec{CB}=\begin{pmatrix} 1 \\ -4 \end{pmatrix}$$

$$\vec{AC}=\vec{AB}+\vec{BC}=\begin{pmatrix} 6 \\ -11 \end{pmatrix}$$

Only after finding the resultant vector do you calculate its magnitude. Using the Pythagorean theorem on the components, the final exact answer is: $$|\vec{AC}|=\sqrt{6^2+(-11)^2}=\sqrt{157}$$

## Parallelograms and diagonals

In a parallelogram, the diagonal from $A$ to $C$ can be found by going along $\vec{AB}$ and then $\vec{BC}$. This gives the vector relationship $\vec{AC}=\vec{AB}+\vec{BC}$, which rearranges to $\vec{BC}=\vec{AC}-\vec{AB}$.

If $\vec{AB}=\begin{pmatrix} 3 \\ 2 \end{pmatrix}$ and $\vec{AC}=\begin{pmatrix} 11 \\ -4 \end{pmatrix}$, we subtract component by component to find the side vector. This gives the following result:

$$\vec{BC}=\begin{pmatrix} 11 \\ -4 \end{pmatrix}-\begin{pmatrix} 3 \\ 2 \end{pmatrix}=\begin{pmatrix} 8 \\ -6 \end{pmatrix}$$

Now apply the magnitude formula to the new vector. In harder trapezium questions, you may also need to calculate scalar multiples such as $\vec{DC}=3\vec{AB}$ before performing this final step:

$$|\vec{BC}|=\sqrt{8^2+(-6)^2}=\sqrt{64+36}=\sqrt{100}=10$$

## Check yourself

1. What is the magnitude of $\begin{pmatrix} 3 \\ 4 \end{pmatrix}$?

   - $$5$ ✔

   - $$7$

   - $$25$

   - $$1$

   _Explanation:_ The magnitude is $\sqrt{3^2+4^2}=\sqrt{25}=5$. The common wrong answer $7$ comes from adding the components instead of using Pythagoras.

2. What is the simplified exact magnitude of $\begin{pmatrix} 10 \\ -4 \end{pmatrix}$?

   - $$2\sqrt{29}$ ✔

   - $$\sqrt{116}$

   - $$29$

   - $$2\sqrt{116}$

   _Explanation:_ First find $\sqrt{10^2+(-4)^2}=\sqrt{116}$. The common wrong answer $\sqrt{116}$ is exact but not simplified, while $2\sqrt{29}$ is the simplified exact form.

3. In a parallelogram, $\vec{AB} = \begin{pmatrix} 3 \\ 2 \end{pmatrix}$ and $\vec{AC} = \begin{pmatrix} 11 \\ -4 \end{pmatrix}$. What is $\vec{BC}$?

   - $$\begin{pmatrix} 8 \\ -6 \end{pmatrix}$ ✔

   - $$\begin{pmatrix} 14 \\ -2 \end{pmatrix}$

   - $$\begin{pmatrix} 8 \\ 6 \end{pmatrix}$

   - $$\begin{pmatrix} -8 \\ 6 \end{pmatrix}$

   _Explanation:_ Because $\vec{AC}=\vec{AB}+\vec{BC}$, rearrange to $\vec{BC}=\vec{AC}-\vec{AB}$. The common wrong answer $\begin{pmatrix} 14 \\ -2 \end{pmatrix}$ comes from adding instead of subtracting.
