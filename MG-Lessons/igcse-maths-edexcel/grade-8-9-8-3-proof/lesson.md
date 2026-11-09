# grade-8-9-8-3-proof — lesson

_Lane: `igcse-maths-edexcel` · grade 8 · 6 content steps · 3 check questions (source: MathsGenie lessons)_

## What proof means

![Flowchart of algebraic proof forms showing integer n, even 2n, odd 2n+1, consecutive numbers, and target forms like 2k+1, mk, and p^2](../assets/001-9d68c947-19e8-4fb3-b800-5e557d3d555e.jpeg)

A proof is a logical argument that shows a statement is true for every allowed value. Testing a few numbers can suggest a pattern, but it cannot guarantee the pattern always continues.

In algebraic proof, you choose useful forms for the numbers and simplify until the result matches a target form. Typical targets are $2k+1$ for odd, $mk$ for a multiple of $m$, and $p^2$ for a square number.

A strong proof ends with a sentence that links the algebra to the claim. For example, since $k$ is an integer, $6k$ is a multiple of 6.

## Representing numbers algebraically

Use a letter such as $n$ to represent any integer. Then build the number type you need from that starting point.

An even integer can be written as $2n$, and an odd integer as $2n+1$. Consecutive integers are $n$, $n+1$, $n+2$.

Consecutive even or odd integers go up by 2, not 1. So $2n$, $2n+2$, $2n+4$ are consecutive evens, while $2n+1$, $2n+3$, $2n+5$ are consecutive odds. That is why $2n$, $2n+1$, $2n+2$ are not three consecutive even numbers.

## Worked example: odd sum

To prove the sum of any two consecutive integers is always odd, let the integers be $n$ and $n+1$, where $n$ is an integer. This covers every possible pair of consecutive integers.

Add them and simplify. The result is
$$
n+(n+1)=2n+1
$$

The expression $2n+1$ is the standard form of an odd number. Since $n$ is an integer, $2n$ is even, so $2n+1$ is odd. Therefore, the sum of any two consecutive integers is always odd.

## Worked example: multiple of 6

To prove the sum of any three consecutive even integers is always a multiple of 6, let them be $2n$, $2n+2$ and $2n+4$, where $n$ is an integer. This uses the correct gap of 2 between consecutive even numbers.

Add and simplify these values. The result is:

$$2n+(2n+2)+(2n+4)=6n+6$$

Now factorise the common factor of 6 to show the sum in the form $6k$:

$$6n+6=6(n+1)$$

Since $n+1$ is an integer, $6(n+1)$ is a multiple of 6. Therefore the sum is always a multiple of 6.

## Worked example: square number

Suppose $n$ is an integer. If the goal is a square number, try to end with a bracket squared. In many algebraic proofs, factorising is significantly quicker than expanding.

Start with the expression and factorise out the common factor $n+3$. This keeps the square structure visible throughout the process:
$$
(n+3)(n+2)+(n+3)=(n+3)((n+2)+1)
$$

Now that the two brackets match, you can write the final result as a square:
$$
(n+3)((n+2)+1)=(n+3)(n+3)=(n+3)^2
$$

The final form is a square, so the expression is always a square number. Including that concluding sentence is essential because it turns mathematical working into a formal proof.

## Stretch example: 2 more than a multiple of 8

We want to prove the statement: the sum of the squares of two consecutive odd integers is $2$ more than a multiple of $8$. So the goal is to write the final expression in the form $8k+2$ for some integer $k$. Let the consecutive odd integers be $2n+1$ and $2n+3$, where $n$ is an integer.

Expanding both squares and collecting like terms gives: $$(2n+1)^2+(2n+3)^2=(4n^2+4n+1)+(4n^2+12n+9)=8n^2+16n+10$$

Now rewrite the expression to show the target form $8k+2$. First rewrite $10$ as $8+2$, then factor out $8$: $$8n^2+16n+10=8n^2+16n+8+2=8(n^2+2n+1)+2$$

Since $n^2+2n+1$ is an integer, let $k=n^2+2n+1$. Then the expression is $8k+2$, so the sum of the squares is $2$ more than a multiple of $8$.

## Check yourself

1. Why is testing $n=1$, $n=2$ and $n=3$ not enough to prove a statement?

   - It only checks a few cases, not every allowed value ✔

   - Small numbers cannot be used in algebra

   - A statement is proved once the first three values work

   - Proof questions only apply to positive integers

   _Explanation:_ A is right because a proof must cover all allowed values, not just a sample. The common wrong answer C is wrong because a pattern can work for the first few numbers and still fail later.

2. Which final sentence correctly completes the proof after showing $n+(n+1)=2n+1$?

   - Since $2n+1$ is one more than an even number, it is odd. ✔

   - Since $2n+1$ is divisible by 2, it is odd.

   - Since $n$ must be odd, the sum is odd.

   - Since $2n+1$ is greater than $2n$, it is odd.

   _Explanation:_ A is right because any integer of the form $2k+1$ is odd. The common wrong answer B is wrong because numbers divisible by 2 are even, not odd.

3. To show $(n+3)(n+2)+(n+3)$ is a square number, what is the best first move?

   - Factorise out $n+3$ ✔

   - Replace $n$ with 2 to test it

   - Expand everything first and stop at a quadratic

   - Divide both terms by $n+3$

   _Explanation:_ A is right because the common factor $n+3$ creates two equal brackets and reveals a square. The common wrong answer C is not the best method because a quadratic expression does not immediately show a square number and needs extra work.
