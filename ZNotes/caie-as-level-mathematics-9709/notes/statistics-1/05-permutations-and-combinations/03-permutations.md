## Permutations

* A Permutation can be defined as the number of arrangements of $n$ distinct objects where **order matters**.

  The number of arrangements of $r$ objects from $n$ total distinct objects can be found using

$$

{}^nP_r = \frac{n!}{(n - r)!} \quad [\text{Where} ~ r \leq n]
$$

<center>Furthermore</center>

$$

{}^nP_n =  n!
$$


---

**<center>Example</center>**

In how many different ways can five boys be arranged in a row?

**<center>Answer</center>**

First, we begin by drawing our dashes

$$

\_ ~ \_ ~ \_ ~ \_ ~ \_
$$

* We have 5 possible boys to choose from to place in the first dash
  * After we place the first boy in the first dash, we have 4 possible boys to choose from to place in the second dash.
  * The same process is repeated until all the boys are arranged.

<center>This gives us the answer as</center>

$$

5 \times 4 \times 3 \times 2 \times 1 = {}^5P_{5} = 5! = 120
$$

**<center>Example 2</center>**

In how many different ways can 3 apples be arranged in a row, from a total of 6 apples.

**<center>Answer</center>**

First, we being by drawing our dashes

$$

\_ ~ \_  ~\_
$$

* We have 6 possible apples to choose from to place in the first dash
  * After we place the first apple in the first dash, we have 5 apples to choose from to place in the second dash.
  * After we place the second apple in the second dash, we have 4 apples to choose from to place in the third and final dash.

<center>This gives us the answer as</center>

$$

6 \times 5 \times 4 = {}^6P_3 = 120
$$



