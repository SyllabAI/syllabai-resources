## Method of differences

The method of differences is a cancellation technique used to find the sum of the differences of two consecutive terms of a sequence, commonly known as the telescoping series.

* For a telescoping series:

$$

\sum_{r  \ = \ 1}^{n} f(r) - f(r - 1) = -f(0) + \cancel{f(1) - f(1)} + \cancel{f(2) - f(2)} \ + \cdots \ \cancel{-f(n - 1)} + f(n)
$$

$$

 \sum_{r \ = \ 1}^{n} f(r) - f(r - 1) = -f(0) + f(n)
$$




### **Convergence**

* A telescoping series approaches a finite limit as $n$ approaches infinity
  * For this to be possible, $f(n)$ must approach 0 ($f(n) \rightarrow 0$).

$$

\sum_{r \ = \ 1}^{\infty} f(r) - f(r - 1) = -f(0)
$$

This can also be written as:

$$

\lim_{N \ \rightarrow \ \infty} \ \sum_{r \ = \ 1}^{N} f(r) - f(r - 1) = -f(0)
$$

### The values a series is convergent for

If a series resembles a geometric series, $ar^{n - 1}$, then it will converge for

$$

-1 < r < 1 \quad \text{[Where r is the common ratio]}
$$



