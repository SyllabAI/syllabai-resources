## Shortest distance from a point to a line

![Screenshot 2024-11-02 at 10.13.59 PM.png](../../../assets/05851080ec9e-672656ed853a987edb0ba5845c80632d2b2e93c9523e9eca.13)

- Consider a point $P$ and a line $L$, which is represented by $r = a + \lambda b$.
  - Vector $\overrightarrow{AP}$ is $p - a$

Clearly, we see that $d$ is the shortest distance, and geometrically we infer:
$$
d = \text{|}p - a \text{|}sin(\theta)
$$
Therefore, using the formula for the cross product, $d$ is the magnitude of the vector product of $\overrightarrow{AP}$ and the **unit vector** $\hat{b}$
$$
d = \text{|}(p - a) \times \frac{b}{\text{|}b\text{|}} \text{|} = \text{|}(p - a) \times \hat{b}\text{|}
$$
We also see that
$$
(p - a) ~\times~ \hat{b}~ = ~\text{|}(p - a)\text{|}\text{|}\hat{b}\text{|}sin(\theta) ~=~ \text{|}(p - a)\text{|}sin(\theta)
$$