# The Magnitude of a Vector Flashcards

_Lane: `igcse-maths-edexcel` · grade 7 · 21 cards (source: MathsGenie flashcards)_

## Card 1 — `basic`

**Front:** What does the notation $|\vec{v}|$ represent?

**Back:** The magnitude (or length) of vector $\vec{v}$.

**Choices:**

- The magnitude (or length) of vector $\vec{v}$. ✔
  - _why:_ The modulus bars around a vector denote its magnitude, found from its components using Pythagoras. This gives the vector’s non-negative geometric length.
- The direction (or angle) of vector $\vec{v}$.
  - _why:_ A vector’s direction describes the angle in which it points, not the meaning of the modulus notation. $|\vec{v}|$ represents the vector’s magnitude or length.
- The unit vector in the direction of vector $\vec{v}$.
  - _why:_ A unit vector is obtained by dividing a non-zero vector by its magnitude. The notation $|\vec{v}|$ gives the magnitude or length itself.
- The horizontal component (or width) of vector $\vec{v}$.
  - _why:_ The horizontal component is only one coordinate of the vector and does not account for vertical displacement. $|\vec{v}|$ represents the vector’s overall magnitude or length.

## Card 2 — `basic`

**Front:** In the column vector $\begin{pmatrix} x \\ y \end{pmatrix}$, what do the numbers represent?

**Back:** $x$: horizontal component$y$: vertical component

**Choices:**

- $x$: horizontal component$y$: vertical component ✔
  - _why:_ In a two-dimensional column vector, the top number measures horizontal displacement and the bottom number measures vertical displacement, with their signs indicating direction.
- $x$: vertical component$y$: horizontal component
  - _why:_ This reverses the standard coordinate order. The top entry $x$ is the horizontal component, while the bottom entry $y$ is the vertical component.
- $x$: magnitude component$y$: direction component
  - _why:_ The entries are perpendicular displacement components, not magnitude and direction. The $x$ entry is horizontal and the $y$ entry is vertical.
- $x$: starting component$y$: finishing component
  - _why:_ A column vector does not list the starting and finishing coordinates of a journey. Its $x$ and $y$ entries represent horizontal and vertical components respectively.

## Card 3 — `basic`

**Front:** If $\vec{AB} = \begin{pmatrix} 5 \\ -2 \end{pmatrix}$, what is $\vec{BA}$?

**Back:** $$\begin{pmatrix} -5 \\ 2 \end{pmatrix}$

**Choices:**

- $$\begin{pmatrix} -5 \\ 2 \end{pmatrix}$ ✔
  - _why:_ Reversing a vector negates every component because the displacement has the same length but the opposite direction. Thus $5$ becomes $-5$ and $-2$ becomes $2$.
- $$\begin{pmatrix} 5 \\ -2 \end{pmatrix}$
  - _why:_ Keeping both components unchanged gives $\vec{AB}$ again rather than the reverse journey. For $\vec{BA}$, both component signs must change, giving $\begin{pmatrix}-5\\2\end{pmatrix}$.
- $$\begin{pmatrix} -5 \\ -2 \end{pmatrix}$
  - _why:_ Only negating the horizontal component does not reverse the vector completely. Both components must change sign, so the vertical component should be $2$.
- $$\begin{pmatrix} 5 \\ 2 \end{pmatrix}$
  - _why:_ Only negating the vertical component leaves the horizontal direction unchanged. Reversing the entire vector also changes $5$ to $-5$, producing $\begin{pmatrix}-5\\2\end{pmatrix}$.

## Card 4 — `cloze`

**Front:** The magnitude of a vector $\vec{v} = \begin{pmatrix} x \\ y \end{pmatrix}$ is calculated using the formula $|\vec{v}| = \text{[...]}$.

**Back:** The magnitude of a vector $\vec{v} = \begin{pmatrix} x \\ y \end{pmatrix}$ is calculated using the formula $|\vec{v}| = \boxed{\sqrt{x^2+y^2}}$.

**Choices:**

- $$\sqrt{x^2+y^2}$ ✔
  - _why:_ The horizontal and vertical components form perpendicular sides of a right-angled triangle. Pythagoras therefore gives the vector’s length as the square root of the sum of their squares.
- $$\sqrt{x+y}$
  - _why:_ Adding the components before taking a square root does not apply Pythagoras and can even produce a negative radicand. The components must first be squared and then added.
- $$x^2+y^2$
  - _why:_ The sum of the squares is the magnitude squared, not the magnitude. Taking its square root gives the required length, $\sqrt{x^2+y^2}$.
- $$\sqrt{x^2-y^2}$
  - _why:_ Pythagoras adds the squares of perpendicular components; it does not subtract them. Subtraction can also make the radicand negative, whereas a real vector’s magnitude is non-negative.

## Card 5 — `basic`

**Front:** Why is the magnitude of a vector always positive, even if components are negative?

**Back:** Negative components square to positives: $(-x)^2 = x^2$.

**Choices:**

- Negative components square to positives: $(-x)^2 = x^2$. ✔
  - _why:_ Squaring removes the signs of the components, so each squared value is non-negative. Their sum and its principal square root are therefore also non-negative.
- Negative components cancel with positives: $-x+x=0$.
  - _why:_ Components are not cancelled against one another when calculating magnitude. Each component is squared, the squares are added, and the non-negative square root is taken.
- Negative components are simply ignored: only positive components are used.
  - _why:_ Negative components still affect the vector’s length and cannot be discarded. Their signs disappear because squaring makes their contributions non-negative before the square root is taken.
- Negative components become positive when added: $-x+(-y)=x+y$.
  - _why:_ Adding negative components does not automatically make them positive, and the stated equality is generally false. Magnitude is non-negative because each component is squared before addition.

## Card 6 — `cloze`

**Front:** To reverse a vector, you must change the [ ___ ] of both components.

**Back:** To reverse a vector, you must change the signs of both components.

**Choices:**

- signs ✔
  - _why:_ A reversed vector has the same magnitude but points in the opposite direction. Multiplying by $-1$ changes the signs of both components without changing their absolute sizes.
- magnitudes
  - _why:_ Changing component magnitudes would generally alter the vector’s length rather than merely reverse it. Reversal requires changing both signs while keeping the absolute values unchanged.
- positions
  - _why:_ Swapping the positions of the components exchanges the horizontal and vertical displacements and does not produce the opposite vector. Both component signs must instead be changed.
- squares
  - _why:_ The squares of opposite components are identical, so changing or considering squares cannot distinguish a vector from its reverse. The signs of both original components must change.

## Card 7 — `basic`

**Front:** State a vector path to find $\vec{AC}$ using the point $B$.

**Back:** $$\vec{AC} = \vec{AB} + \vec{BC}$

**Choices:**

- $$\vec{AC} = \vec{AB} + \vec{BC}$ ✔
  - _why:_ Travelling from $A$ to $B$ and then from $B$ to $C$ gives the same overall displacement as travelling directly from $A$ to $C$.
- $$\vec{AC} = \vec{AB} - \vec{BC}$
  - _why:_ The path from $A$ through $B$ to $C$ combines the two consecutive displacements by addition, not subtraction. Therefore $\vec{AC}=\vec{AB}+\vec{BC}$.
- $$\vec{AC} = \vec{BA} + \vec{BC}$
  - _why:_ The first leg must travel from $A$ to $B$, but $\vec{BA}$ points in the opposite direction. The valid path is $\vec{AB}+\vec{BC}$.
- $$\vec{AC} = \vec{AB} + \vec{CB}$
  - _why:_ The second leg must travel from $B$ to $C$, whereas $\vec{CB}$ points backwards. The correct route is $\vec{AB}+\vec{BC}$.

## Card 8 — `basic`

**Front:** How is $\vec{BC}$ expressed in terms of $\vec{AC}$ and $\vec{AB}$?

**Back:** $$\vec{BC} = \vec{AC} - \vec{AB}$

**Choices:**

- $$\vec{BC} = \vec{AC} - \vec{AB}$ ✔
  - _why:_ Starting from $\vec{AC}=\vec{AB}+\vec{BC}$, subtracting $\vec{AB}$ from both sides isolates the required vector and gives $\vec{BC}=\vec{AC}-\vec{AB}$.
- $$\vec{BC} = \vec{AC} + \vec{AB}$
  - _why:_ Adding $\vec{AB}$ fails to rearrange the path equation correctly. From $\vec{AC}=\vec{AB}+\vec{BC}$, subtracting $\vec{AB}$ gives $\vec{BC}=\vec{AC}-\vec{AB}$.
- $$\vec{BC} = \vec{AB} - \vec{AC}$
  - _why:_ Reversing the subtraction gives $\vec{CB}$ rather than $\vec{BC}$. The required displacement is found by subtracting $\vec{AB}$ from $\vec{AC}$.
- $$\vec{BC} = \vec{AB} + \vec{CA}$
  - _why:_ Since $\vec{CA}=-\vec{AC}$, this expression equals $\vec{AB}-\vec{AC}$ and points from $C$ to $B$. The required vector is $\vec{AC}-\vec{AB}$.

## Card 9 — `basic`

**Front:** Calculate the magnitude of $\vec{v} = \begin{pmatrix} -8 \\ 15 \end{pmatrix}$.

**Back:** 17

**Choices:**

- 17 ✔
  - _why:_ The magnitude is $\sqrt{(-8)^2+15^2}=\sqrt{64+225}=\sqrt{289}=17$, using Pythagoras on the horizontal and vertical components.
- 23
  - _why:_ This comes from adding the absolute component values, $8+15$, rather than using Pythagoras. The correct magnitude is $\sqrt{(-8)^2+15^2}=17$.
- 7
  - _why:_ This comes from combining the components by subtraction instead of squaring and adding them. Using $\sqrt{(-8)^2+15^2}$ gives the correct magnitude of $17$.
- 289
  - _why:_ This is the squared magnitude, $(-8)^2+15^2$, but the required magnitude is its square root. Therefore, the correct answer is $\sqrt{289}=17$.

## Card 10 — `basic`

**Front:** What defines an exact magnitude in vector geometry?

**Back:** An answer that has not been rounded, typically written as a surd.

**Choices:**

- An answer that has not been rounded, typically written as a surd. ✔
  - _why:_ An exact magnitude preserves the complete value without decimal approximation. When the square root is irrational, it is normally left in simplified surd form.
- An answer that has been rounded, typically written as a decimal.
  - _why:_ Rounding produces an approximate magnitude because some precision is lost. An exact magnitude has not been rounded and is typically retained as a simplified surd.
- An answer that has been estimated, typically written as an integer.
  - _why:_ Estimating to an integer gives an approximation rather than an exact value. The exact magnitude remains unrounded, usually in simplified surd form when necessary.
- An answer that has been truncated, typically written as a decimal.
  - _why:_ Truncation removes digits and therefore changes the value into an approximation. An exact magnitude is unrounded and is commonly expressed as a simplified surd.

## Card 11 — `cloze`

**Front:** To simplify a magnitude like $\sqrt{116}$, you should identify and factor out [ ___ ] (e.g., 4, 9, 16).

**Back:** To simplify a magnitude like $\sqrt{116}$, you should identify and factor out square factors (e.g., 4, 9, 16).

**Choices:**

- square factors ✔
  - _why:_ A square factor has an integer square root, so it can be taken outside the radical. For example, $\sqrt{116}=\sqrt{4\times29}=2\sqrt{29}$.
- prime factors
  - _why:_ Prime factorisation may help reveal a square factor, but individual prime factors cannot automatically be taken outside a square root. The required factors are square factors.
- cube factors
  - _why:_ Cube factors are relevant when simplifying cube roots, not square roots. To simplify $\sqrt{116}$, identify and factor out square factors such as $4$.
- common factors
  - _why:_ A common factor need not have an integer square root, so it may not simplify the radical. The useful factors are square factors, such as $4$ in $116$.

## Card 12 — `basic`

**Front:** Simplify the magnitude $\sqrt{116}$ into a simplified surd.

**Back:** $$2\sqrt{29}$

**Choices:**

- $$2\sqrt{29}$ ✔
  - _why:_ Since $116=4\times29$, the square factor $4$ can be removed from the radical: $\sqrt{116}=\sqrt{4}\sqrt{29}=2\sqrt{29}$.
- $$4\sqrt{29}$
  - _why:_ This takes $4$ outside the square root without first finding its square root. Since $\sqrt{4}=2$, the correct simplified surd is $2\sqrt{29}$.
- $$2\sqrt{58}$
  - _why:_ This does not preserve the original value, since squaring $2\sqrt{58}$ gives $232$. Factoring $116$ as $4\times29$ gives $2\sqrt{29}$.
- $$4\sqrt{7}$
  - _why:_ This corresponds to $\sqrt{112}$ because $(4\sqrt{7})^2=112$, not $116$. Using the square factor $4$ gives the correct result $2\sqrt{29}$.

## Card 13 — `basic`

**Front:** If $\vec{AB} = \begin{pmatrix} 3 \\ 4 \end{pmatrix}$ and $\vec{DC} = 3\vec{AB}$, find the column vector for $\vec{DC}$.

**Back:** $$\begin{pmatrix} 9 \\ 12 \end{pmatrix}$

**Choices:**

- $$\begin{pmatrix} 9 \\ 12 \end{pmatrix}$ ✔
  - _why:_ Multiplying a vector by $3$ means multiplying both components by $3$. Thus $3\begin{pmatrix}3\\4\end{pmatrix}=\begin{pmatrix}9\\12\end{pmatrix}$.
- $$\begin{pmatrix} 6 \\ 7 \end{pmatrix}$
  - _why:_ This adds $3$ to each component instead of multiplying each component by $3$. Scalar multiplication gives $\begin{pmatrix}3\times3\\3\times4\end{pmatrix}=\begin{pmatrix}9\\12\end{pmatrix}$.
- $$\begin{pmatrix} 9 \\ 4 \end{pmatrix}$
  - _why:_ This multiplies only the first component by $3$. A scalar must multiply every component, so the correct vector is $\begin{pmatrix}9\\12\end{pmatrix}$.
- $$\begin{pmatrix} 3 \\ 12 \end{pmatrix}$
  - _why:_ This multiplies only the second component by $3$. Both components must be scaled, giving $\begin{pmatrix}3\times3\\4\times3\end{pmatrix}=\begin{pmatrix}9\\12\end{pmatrix}$.

## Card 14 — `basic`

**Front:** In a parallelogram $ABCD$, describe the vector path for the diagonal $\vec{AC}$.

**Back:** $$\vec{AC} = \vec{AB} + \vec{BC}$

**Choices:**

- $$\vec{AC} = \vec{AB} + \vec{BC}$ ✔
  - _why:_ Travelling from $A$ to $C$ via $B$ consists of the consecutive vectors $\vec{AB}$ and $\vec{BC}$. Therefore, vector addition gives $\vec{AC}=\vec{AB}+\vec{BC}$.
- $$\vec{AC} = \vec{AB} + \vec{DC}$
  - _why:_ In a parallelogram, $\vec{DC}$ equals $\vec{AB}$, so this sum does not follow a connected path from $A$ to $C$. The path is $\vec{AB}+\vec{BC}$.
- $$\vec{AC} = \vec{AB} - \vec{BC}$
  - _why:_ Subtracting $\vec{BC}$ reverses its direction, creating $\vec{CB}$ rather than the required journey from $B$ to $C$. The correct path is $\vec{AB}+\vec{BC}$.
- $$\vec{AC} = \vec{BA} + \vec{BC}$
  - _why:_ The vector $\vec{BA}$ points towards $A$, so it does not begin the route from $A$ through $B$. The connected path is $\vec{AB}+\vec{BC}$.

## Card 15 — `basic`

**Front:** Find the magnitude of $\vec{v} = \begin{pmatrix} 3 \\ 2 \end{pmatrix}$.

**Back:** $$\sqrt{13}$

**Choices:**

- $$\sqrt{13}$ ✔
  - _why:_ Using Pythagoras, the magnitude is $\sqrt{3^2+2^2}=\sqrt{9+4}=\sqrt{13}$. This surd is already in its simplest exact form.
- $$5$
  - _why:_ This adds the components directly, but vector magnitude requires the square root of the sum of their squares. Therefore, the answer is $\sqrt{3^2+2^2}=\sqrt{13}$.
- $$13$
  - _why:_ This is the squared magnitude, $3^2+2^2$, rather than the magnitude itself. Taking the square root gives the correct answer, $\sqrt{13}$.
- $$\sqrt{5}$
  - _why:_ This comes from adding the components before taking a square root. The components must first be squared, so the correct magnitude is $\sqrt{9+4}=\sqrt{13}$.

## Card 16 — `basic`

**Front:** Outline the two-stage method for finding the magnitude of a hidden vector in geometry.

**Back:** 1. Find the column vector using a path.2. Apply the Pythagoras formula $\sqrt{x^2+y^2}$.

**Choices:**

- 1. Find the column vector using a path.2. Apply the Pythagoras formula $\sqrt{x^2+y^2}$. ✔
  - _why:_ A vector path first reveals the horizontal and vertical components of the hidden vector. Pythagoras then converts those components into its magnitude using $\sqrt{x^2+y^2}$.
- 1. Find the column vector using a path.2. Apply the addition formula $x+y$.
  - _why:_ Adding the components does not calculate the length of a vector. After finding the column vector from a path, use Pythagoras: $\sqrt{x^2+y^2}$.
- 1. Find the scalar length using a path.2. Apply the Pythagoras formula $\sqrt{x^2+y^2}$.
  - _why:_ A path combines directed vectors to find the hidden column vector, not a scalar length. Once its components are known, apply $\sqrt{x^2+y^2}$ to find the magnitude.
- 1. Find the column vector using a path.2. Apply the Pythagoras formula $x^2+y^2$.
  - _why:_ The expression $x^2+y^2$ gives the squared magnitude because the final square root is missing. The correct magnitude formula is $\sqrt{x^2+y^2}$.

## Card 17 — `cloze`

**Front:** A [ ___ ] is a vector multiplied by a number, which changes its length but keeps its direction (or reverses it if negative).

**Back:** A scalar multiple is a vector multiplied by a number, which changes its length but keeps its direction (or reverses it if negative).

**Choices:**

- scalar multiple ✔
  - _why:_ Multiplying a vector by a scalar changes its magnitude by that factor while preserving its direction for positive scalars and reversing it for negative scalars.
- resultant vector
  - _why:_ A resultant vector is the combined effect of two or more vectors. The correct term is scalar multiple because it describes a vector multiplied by a number.
- unit vector
  - _why:_ A unit vector has magnitude 1 and usually represents direction. The correct term is scalar multiple because multiplying by a number scales a vector’s length.
- position vector
  - _why:_ A position vector describes a point’s displacement from the origin. The correct term is scalar multiple because the definition involves multiplying a vector by a number.

## Card 18 — `cloze`

**Front:** A scalar multiple is a vector multiplied by a number, which changes its [ ___ ] but keeps its direction (or reverses it if negative).

**Back:** A scalar multiple is a vector multiplied by a number, which changes its length but keeps its direction (or reverses it if negative).

**Choices:**

- length ✔
  - _why:_ A scalar changes a vector’s length by multiplying its magnitude by the scalar’s absolute value. A negative scalar additionally reverses the vector’s direction.
- gradient
  - _why:_ Gradient describes slope rather than vector size. The correct word is length because scalar multiplication scales the vector’s magnitude while preserving or reversing its direction.
- origin
  - _why:_ The origin is a fixed point in a coordinate system and is not altered by scalar multiplication. The correct word is length, meaning the vector’s magnitude.
- dimension
  - _why:_ Scalar multiplication does not change whether a vector is two-dimensional or three-dimensional. It changes the vector’s length and may reverse its direction.

## Card 19 — `basic`

**Front:** Given $\vec{AC} = \begin{pmatrix} 6 \\ -9 \end{pmatrix}$, find the exact magnitude $|\vec{AC}|$.

**Back:** $$\sqrt{117}$

**Choices:**

- $$\sqrt{117}$ ✔
  - _why:_ Using Pythagoras, the magnitude is $\sqrt{6^2+(-9)^2}=\sqrt{36+81}=\sqrt{117}$. Squaring makes both component contributions positive.
- $$\sqrt{45}$
  - _why:_ This comes from treating $(-9)^2$ as $-81$ and calculating $36-81$ incorrectly. Both squared components are positive, giving $\sqrt{117}$.
- $$\sqrt{27}$
  - _why:_ This results from subtracting the component squares in the wrong order: $81-36=45$, not 27. Magnitude requires addition, giving $\sqrt{117}$.
- $$\sqrt{90}$
  - _why:_ This adds the absolute component values before applying a square root, rather than adding their squares. The correct calculation is $\sqrt{36+81}=\sqrt{117}$.

## Card 20 — `basic`

**Front:** If $\vec{CB} = \begin{pmatrix} -1 \\ 4 \end{pmatrix}$, what is $\vec{BC}$?

**Back:** $$\begin{pmatrix} 1 \\ -4 \end{pmatrix}$

**Choices:**

- $$\begin{pmatrix} 1 \\ -4 \end{pmatrix}$ ✔
  - _why:_ Reversing a vector negates every component. Since $\vec{BC}=-\vec{CB}$, negating $(-1,4)$ gives $(1,-4)$.
- $$\begin{pmatrix} -1 \\ 4 \end{pmatrix}$
  - _why:_ This leaves the vector unchanged, but reversing its endpoints reverses its direction. Both components must be negated, so $\vec{BC}=(1,-4)$.
- $$\begin{pmatrix} 1 \\ 4 \end{pmatrix}$
  - _why:_ Only the first component has been negated. Reversing a vector requires changing the sign of every component, so $\vec{BC}=(1,-4)$.
- $$\begin{pmatrix} -1 \\ -4 \end{pmatrix}$
  - _why:_ Only the second component has been negated. Both signs must change when reversing the vector, giving $\vec{BC}=(1,-4)$.

## Card 21 — `basic`

**Front:** Calculate the magnitude of a vector with components $x=8$ and $y=-6$.

**Back:** 10

**Choices:**

- 10 ✔
  - _why:_ The magnitude is found using Pythagoras: $\sqrt{8^2+(-6)^2}=\sqrt{64+36}=\sqrt{100}=10$.
- 14
  - _why:_ This adds the absolute component values, $8+6$, which gives Manhattan distance rather than vector magnitude. Pythagoras gives $\sqrt{64+36}=10$.
- 2
  - _why:_ This subtracts the absolute component values, $8-6$, instead of using Pythagoras. The magnitude is $\sqrt{8^2+(-6)^2}=10$.
- 100
  - _why:_ This is the squared magnitude, found from $8^2+(-6)^2$. Taking the square root is still required, so the vector’s magnitude is 10.
