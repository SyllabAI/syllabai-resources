# grade-7-7-4-quadratic-formula — lesson

_Lane: `igcse-maths-edexcel` · grade 7 · 5 content steps · 4 check questions (source: MathsGenie lessons)_

## Recognising a quadratic

![Parabola on coordinate axes crossing the x-axis at two roots](../assets/001-79bd9315-d08a-44a3-9c6c-707cb47b7078.jpeg)

A quadratic equation has highest power 2, such as $x^2$. Before using the formula, write it in standard form $ax^2+bx+c=0$ with $a \ne 0$.

The numbers $a$, $b$, and $c$ are the coefficients, and their signs matter. The roots are the values of $x$ that make the equation true, which are also the points where the parabola crosses the x-axis.

## The quadratic formula and the discriminant

For any quadratic in standard form, the solutions are given by the quadratic formula.
$$
x=\frac{-b\pm\sqrt{b^2-4ac}}{2a}
$$
The symbol $\pm$ means you usually get two answers.

The expression $b^2-4ac$ is called the discriminant. If it is positive, there are two real roots; if it is zero, one repeated root; if it is negative, no real roots.

Always identify $a$, $b$, and $c$ after rearranging the equation. If $a=0$, the equation is not quadratic, so the formula does not apply. If $b=-4$, then $-b=4$, so brackets help you keep the signs correct.

## Worked example to 2 decimal places

To solve $3x^2+4x-5=0$ to 2 decimal places, we first identify the coefficients. Match them carefully: $a=3$, $b=4$, and $c=-5$.
$$
x=\frac{-4\pm\sqrt{4^2-4(3)(-5)}}{2(3)}
$$

Now simplify the discriminant by calculating the values under the square root. The negative value of $c$ turns the subtraction into addition, so $-4(3)(-5)$ becomes $+60$.
$$
4^2-4(3)(-5)=16+60=76,\qquad x=\frac{-4\pm\sqrt{76}}{6}
$$

Working out both cases gives the two decimal roots. Keep full calculator accuracy until you perform the final rounding to 2 decimal places.
$$
x=\frac{-4+\sqrt{76}}{6}\approx 0.786,\qquad x=\frac{-4-\sqrt{76}}{6}\approx -2.120
$$
So to 2 decimal places, $x=0.79$ or $x=-2.12$.

## Exact answers in surd form

Sometimes the question wants exact answers instead of decimals. For the equation $x^2+10x+7=0$, identify the coefficients $a=1$, $b=10$, and $c=7$ to substitute into the quadratic formula.
$$x=\frac{-10\pm\sqrt{10^2-4(1)(7)}}{2}$$

Next, simplify the discriminant and the surd. You must look for a square factor inside the root to express the value in its simplest form.
$$10^2-4(1)(7)=100-28=72,\qquad \sqrt{72}=\sqrt{36\cdot 2}=6\sqrt{2}$$

Substitute the simplified surd back into the formula and divide through. This result is in exact form, so do not convert it into decimals unless the question specifically asks.
$$x=\frac{-10\pm 6\sqrt{2}}{2}=-5\pm 3\sqrt{2}$$

## Forming a quadratic from geometry

![Right-angled triangle with sides labeled x + 3, x + 4, and x + 6](../assets/002-f6a128bc-438d-4fcc-9cdd-506057bd79c8.jpeg)

In geometry questions, the main job is often to create the quadratic first. For the triangle shown, where $x+6$ is the hypotenuse, Pythagoras gives:

$$ (x+3)^2+(x+4)^2=(x+6)^2 $$

Expand both sides and rearrange to standard form. This process leads us to a quadratic equation that can be solved using the standard formula:

$$ x^2+6x+9+x^2+8x+16=x^2+12x+36 \Rightarrow x^2+2x-11=0 $$

Now the quadratic formula can be used exactly as before. Note that only $x=-1+2\sqrt{3}$ is valid, because the other root would make side lengths negative.

$$ x=\frac{-2\pm\sqrt{2^2-4(1)(-11)}}{2}=\frac{-2\pm\sqrt{48}}{2}=-1\pm 2\sqrt{3} $$

## Check yourself

1. After writing $4x^2=7x+2$ in standard form, which coefficients are correct?

   - $$a=4$, $b=-7$, $c=-2$ ✔

   - $$a=4$, $b=7$, $c=2$

   - $$a=-4$, $b=7$, $c=2$

   - $$a=7$, $b=2$, $c=4$

   _Explanation:_ Move everything to the left to get $4x^2-7x-2=0$, so $a=4$, $b=-7$, and $c=-2$. Option B is the common mistake of reading the coefficients before rearranging, so the signs of $b$ and $c$ are lost.

2. For $3x^2+4x-5=0$, what is the discriminant?

   - 76 ✔

   - -44

   - 44

   - 60

   _Explanation:_ The discriminant is $b^2-4ac=4^2-4(3)(-5)=16+60=76$. Option B comes from treating $c$ as $5$ instead of $-5$.

3. In the triangle example, why is one of the roots rejected?

   - Because it makes one or more side lengths negative ✔

   - Because the quadratic formula only gives one answer

   - Because the discriminant is negative

   - Because $x$ must be an integer

   _Explanation:_ The quadratic formula can give algebraic roots that are not sensible in context. Option A is correct because a negative root would make a side length negative, while option B is wrong because the formula still correctly produces two algebraic solutions.

4. Stretch: After expanding and rearranging $(x-2)(2x+3)+5(2x-4)=46$, which quadratic should you solve?

   - $$2x^2+9x-72=0$ ✔

   - $$2x^2+9x+72=0$

   - $$2x^2-x-72=0$

   - $$2x^2+9x-26=0$

   _Explanation:_ Expanding gives $2x^2-x-6+10x-20=46$, which simplifies to $2x^2+9x-26=46$. Subtract 46 from both sides to get $2x^2+9x-72=0$, so option D is the common mistake of stopping one step too early.
