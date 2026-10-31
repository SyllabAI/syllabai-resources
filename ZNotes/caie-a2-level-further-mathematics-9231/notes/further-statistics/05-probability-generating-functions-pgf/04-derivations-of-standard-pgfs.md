## Derivations of standard PGFs

These derivations of standard PGFs are **required** to be known.

### **Binomial distribution**

Let $X \sim Bin(n, p)$, such that $P(X = x) = {n \choose r}p^rq^{n - r}$

$$

G_{X}(t) = \sum_{r ~ = ~ 0}^{n} t^x {n \choose r}p^rq^{n ~ - ~ r}
$$

$$

G_{X}(t) = \sum_{r ~ = ~ 0}^{n} {n \choose r} (pt)^rq^{n ~ - ~ r} \implies (pt + q)^n
$$

Thus, for all $t \in \mathbb{R}$,

$$

G_{X}(t) = (pt + q)^n
$$

To find the expectation and variance:

$$

G\prime_{X}(t) = np(pt + q)^{n - 1} ~ \text{and} ~ G\prime\prime_{X}(t) = (np^2)(n - 1)(pt + q)^{n - 2}
$$

So we get the following results:

$$

E(X) = G\prime_{X}(1) = np(p + q)^{n - 1} \implies np(1)^{n - 1} = np
$$

$$

Var(X) = G\prime\prime_{X}(1) + G\prime_{X}(t)(1) - (G\prime_{X}(1))^2 \implies (np^2)(n - 1)(1)^{n - 2} + np - (np)^2 = n(n - 1)p^2
$$




### **Poisson distribution**

Let $X \sim Po(\lambda)$, such that $P(X = x) = e^{-\lambda}\frac{\lambda^x}{x!}$

$$

G_{X}(t) = \sum_{x ~ = ~0}^{\infty} t^x e^{-\lambda}\frac{\lambda^x}{x!}
$$

$$

G_{X}(t) = e^{-\lambda} \sum_{x ~ = ~ 0}^{\infty} \frac{(t\lambda)^x}{x!}
$$

Notice that the summation is Maclaurin’s series expansion for $e^{t\lambda}$

$$

e^{t\lambda} = \sum_{x ~ = ~ 0}^{\infty} \frac{(t\lambda)^x}{x!}
$$

Thus, for all $t \in \mathbb{R}$,

$$

G_{X}(t) = e^{-\lambda}e^{t\lambda} = e^{\lambda(t ~ - ~ 1)}
$$

To find the expectation and variance:

$$

G\prime_{X}(t) = \lambda e^{\lambda(t ~ - ~ 1)} ~ \text{and} ~ G\prime\prime_{X}(t) = \lambda^2e^{\lambda(t ~ - ~ 1)}
$$

So we get the following results:

$$

E(X) = G\prime_{X}(1) \implies \lambda e^{\lambda(1 - 1)} = \lambda
$$

$$

Var(X) = \lambda^2 e^{\lambda(1 ~ - ~ 1)} + \lambda e^{\lambda(1 ~ - ~ 1)} - (\lambda e^{\lambda(1~ - ~ 1)})^2 \implies \lambda^2 + \lambda - \lambda^2 = \lambda
$$




### **Geometric distribution**

Let $X \sim Geo(p)$, such that $P(X = x) = p(1 - p)^{x} = pq^{x}$ (Representing the probability of $x$ failures before the first successful attempt)

$$

G_{X}(t) = \sum_{x ~ = ~ 0}^{\infty} t^xpq^{x}
$$

$$

G_{X}(t) = p \sum_{x ~ = ~ 0}^{\infty} (qt)^x
$$

Notice that the summation can be expressed as the sum of an infinite geometric series, with the first term $1$ and $qt$ as the common ratio.

$$

\sum_{x ~ = ~ 0}^{\infty} (qt)^x = \frac{1}{1 - qt}
$$

Thus, for all $t \in \mathbb{R}$,

$$

G_{X}(t) = \frac{p}{1 - qt}
$$

To find the expectation and variance:

$$

G\prime_{X}(t) = pq(1 - qt)^{-2} ~ \text{and} ~ G\prime\prime_{X}(t) = 2pq^2(1 - qt)^{-3}
$$

So we get the following results:

$$

E(X) = G\prime_{X}(1) = pq(1 - q)^{-2} \implies \frac{pq}{p^2} = \frac{q}{p}
$$

$$

Var(X) = 2pq^2\left(1 - q \right)^{-3} + \frac{q}{p} - \left(\frac{q}{p} \right)^2 \implies \frac{q}{p} \left(\frac{q + p}{p} \right) = \frac{q}{p^2}
$$



### **Discrete Uniform distribution**

Let $X$ be a discrete random variable, such that $P(X = x) = \frac{1}{n}$

$$

G_{X}(t) = \sum_{x ~ = ~ 1}^{n} \frac{t^x}{n}
$$

$$

G_{X}(t) = \frac{t}{n} \sum_{x ~ = ~ 1}^{n - 1} t^x
$$

Notice that the summation can be expressed as the sum of an infinite geometric series, with first term $1$ and $t^x$ as the common ratio.

$$

\sum_{x ~ = ~ 1}^{n - 1} t^x = \frac{1 - t^n}{1 - t}
$$

Thus, for all $t \in \mathbb{R}$,

$$

G_{X}(t) = \frac{t(1 - t^n)}{n(1 - t)}
$$

To find the expectation and variance of a discrete uniform distribution:

* Use the standard $E(X)$ and $Var(X)$ formulae for PGFs.



