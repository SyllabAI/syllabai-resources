# grade-6-6-2-fractional-and-negative-indices — lesson

_Lane: `igcse-maths-edexcel` · grade 6 · 4 content steps · 3 check questions (source: MathsGenie lessons)_

## What indices are telling you

One helpful way to calculate $a^{-m/n}$ is:

- Negative sign: take the reciprocal.
- Denominator $n$: take the $n$th root.
- Numerator $m$: raise to the power $m$.

So

$$a^{-m/n}=\frac{1}{(\sqrt[n]{a})^m}=\frac{1}{\sqrt[n]{a^m}}$$

Example:

$$32^{-2/5}=\frac{1}{(\sqrt[5]{32})^2}=\frac{1}{2^2}=\frac{1}{4}$$

In $a^k$, $a$ is the base and $k$ is the index. For a fractional index $a^{m/n}$, the denominator $n$ tells you the root and the numerator $m$ tells you the power. When the root is defined, you can write

$$a^{m/n}=\sqrt[n]{a^m}=(\sqrt[n]{a})^m$$

A negative index means reciprocal, not a negative answer. For any non-zero $a$ and integer $k$, $a^{-k}=\frac{1}{a^k}$, so $4^{-1}=\frac{1}{4}$. The same idea works for fractional indices: $a^{-m/n}=\frac{1}{a^{m/n}}$. This is why $0^{-1}$ is undefined: it would mean dividing by zero.

## Fractional indices mean roots

A fractional index tells you to take a root and then a power. For positive values of $a$, $a^{\frac{1}{2}} = \sqrt{a}$, $a^{\frac{1}{3}} = \sqrt[3]{a}$, and in general $a^{\frac{m}{n}} = \left(\sqrt[n]{a}\right)^m$.

The denominator tells you the root and the numerator tells you the power. For $343^{\frac{2}{3}}$, take the cube root first to get $7$, then square to get $49$. A half power is a square root, so $144^{\frac{1}{2}} = 12$, not $72$.

## Negative fractional indices

Put the two ideas together and read the index in stages. For non-zero $a$, $a^{-\frac{m}{n}} = \frac{1}{a^{\frac{m}{n}}}$, so the negative sign means reciprocal, the denominator means root, and the numerator means power.

Example: $32^{-\frac{2}{5}} = \frac{1}{32^{\frac{2}{5}}}$. The fifth root of $32$ is $2$, then $2^2 = 4$, so the value is $\frac{1}{4}$.

With a fraction base, inverting first is often quickest. $$\left(\frac{16}{25}\right)^{-\frac{3}{2}} = \left(\frac{25}{16}\right)^{\frac{3}{2}} = \left(\frac{5}{4}\right)^3 = \frac{125}{64}$$

## Algebra and the same-base strategy

The same laws work with algebraic terms, especially $(a^p)^q = a^{pq}$. For example, $(27x^6)^{\frac{2}{3}} = (\sqrt[3]{27x^6})^2 = (3x^2)^2 = 9x^4$.

To find an unknown index, rewrite both sides with the same base and compare the powers. Since $32 = 2^5$, $2 \times \sqrt{32} = 2^1 \times (2^5)^{\frac{1}{2}} = 2^1 \times 2^{\frac{5}{2}}$. Add the indices to get $2^{\frac{7}{2}}$, so if $2 \times \sqrt{32} = 2^n$, then $n = \frac{7}{2}$.

## Check yourself

1. What is $7^{-1}$?

   - $$\frac{1}{7}$ ✔

   - $$-7$

   - $$7$

   - $$-\frac{1}{7}$

   _Explanation:_ A negative index means reciprocal, so $7^{-1} = \frac{1}{7}$. The common wrong answer $-7$ treats the negative index like a negative sign, but it changes the position of the power, not the sign of the value.

2. What is $\left(\frac{9}{16}\right)^{-\frac{1}{2}}$?

   - $$\frac{4}{3}$ ✔

   - $$\frac{3}{4}$

   - $$-\frac{4}{3}$

   - $$-\frac{3}{4}$

   _Explanation:_ First take the square root: $\left(\frac{9}{16}\right)^{\frac{1}{2}} = \frac{3}{4}$. The negative index then means take the reciprocal, so the answer is $\frac{4}{3}$. The common wrong answer $\frac{3}{4}$ forgets to deal with the negative sign.

3. Simplify $2^3 \times 2^{-\frac{1}{2}}$.

   - $$2^{\frac{5}{2}}$ ✔

   - $$2^{\frac{7}{2}}$

   - $$2^{-\frac{3}{2}}$

   - $$4^{\frac{5}{2}}$

   _Explanation:_ When multiplying powers with the same base, add the indices: $3 + \left(-\frac{1}{2}\right) = \frac{5}{2}$. The common wrong answer $2^{\frac{7}{2}}$ comes from subtracting the negative index instead of just adding it.
