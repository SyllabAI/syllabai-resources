## Permutations with Repetitions

* As permutations only deals with the number of arrangements of **distinct** where **order matters,** we **overcount** the number of arrangements if we try to use the regular formula.

$$

\text{Number of arrangements} = \frac{n!}{p! \times q! \times \cdots}
$$

Where:

* $n$ is the **total** number of objects
  * $n = p + q + \cdots$
* $p$ is the number of $p$ **repeated** **alike**, non distinct, objects
* $q$ is the number of $q$ **repeated** **alike**, non distinct, objects


---

**<center>Example</center>**

Find the number of permutations of the 11 letter word MISSISSIPPI.

**<center>Answer</center>**

First we note down the number of times each letter occurs in the word.

$1 = M, 4 = I, 4 = S, 2 = P$

Using the formula we get

$$

\text{Number of arrangements} = \frac{11!}{4! \times 4! \times 2!} = 34,650
$$



