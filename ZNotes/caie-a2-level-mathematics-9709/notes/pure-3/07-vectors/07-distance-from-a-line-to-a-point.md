## $\mathbf{\bot}$ Distance from a Line to a Point

  - **AKA:** shortest distance from a point to the line

  - Find vector for the point,$\text{ B}$, on the line

Vector equation of the line:

$$
\widetilde{\mathbf{r}} = \ \begin{pmatrix}
1 \\
3 \\
 - 2 \\
\end{pmatrix} + \ t\begin{pmatrix}
1 \\
1 \\
3 \\
\end{pmatrix}
$$

$$
\therefore\overrightarrow{\text{OB}} = \ \begin{pmatrix}
1 + t \\
3 + t \\
3t - 2 \\
\end{pmatrix}
$$

- $A$ is the point given

$$
\overrightarrow{\text{OA}} = \ \begin{pmatrix}
2 \\
3 \\
4 \\
\end{pmatrix}
$$

$$
\therefore\overrightarrow{\text{AB}} = \ \begin{pmatrix}
1 + t - 2 \\
3 + t - 3 \\
3t - 2 - 4 \\
\end{pmatrix} = \begin{pmatrix}
t - 1 \\
t \\
3t - 6 \\
\end{pmatrix}
$$

- Use Dot product of $\text{AB}$ and the direction vector

$$
\overrightarrow{\text{AB}}.\mathbf{d} = \ \cos 90
$$

$$
\begin{pmatrix}
t - 1 \\
t \\
3t - 6 \\
\end{pmatrix}\text{. }\begin{pmatrix}
1 \\
1 \\
3 \\
\end{pmatrix} = 0
$$

$$
1\left( t - 1 \right) + 1\left( t \right) + 3\left( 3t - 6 \right) = 0
$$

$$
11t - 19 = 0
$$

$$
t = \frac{19}{11}
$$

- Substitute $t$ into equation to get foot

- Use Pythagoras’ Theorem to find distance

&nbsp;

**<span class="underline">{S08-P3} Question:</span>**

The points $A$ and $B$ have position vectors, relative to the origin
$O$, given by

$OA = \mathbf{i} + 2\mathbf{j} + 3\mathbf{k}$ and
$OB = 2\mathbf{i} + \mathbf{j} + 3\mathbf{k}$

The line $l$ has vector equation

$$
\mathbf{r}\mathbf{=}\left( 1 - 2t \right)\mathbf{i} + \left( 5 + t \right)\mathbf{j} + \left( 2 - t \right)\mathbf{k}
$$

i)  Show that $l$ does not intersect the line passing through $A$
    and $B$.

ii)  The point $\text{P }$lies on $l$ and is such that angle
    $\text{PAB}$ is equal to $60{^\circ}$. Given that the position
    vector of $P$ is
    $\left( 1 - 2t \right)\mathbf{i} + \left( 5 + t \right)\mathbf{j} + \left( 2 - t \right)\mathbf{k,}$
    show that $3t^{2} + 7t + 2 = 0$. Hence find the only possible
    position vector of $P$

**<center>Solution:</center>**

**<span class="underline">Part (i)</span>**

*Firstly, we must find the equation of line* $\text{AB}$

$$
AB = OB - OA
$$

$$
= \begin{pmatrix}
2 \\
1 \\
3 \\
\end{pmatrix} - \begin{pmatrix}
1 \\
2 \\
3 \\
\end{pmatrix} = \begin{pmatrix}
1 \\
 - 1 \\
0 \\
\end{pmatrix}
$$

$$
\mathbf{AB = \ }\begin{pmatrix}
1 \\
2 \\
3 \\
\end{pmatrix} + s\begin{pmatrix}
1 \\
 - 1 \\
0 \\
\end{pmatrix}
$$

and 

$$
\mathbf{L =}\begin{pmatrix}
1 \\
5 \\
2 \\
\end{pmatrix} + t\begin{pmatrix}
 - 2 \\
1 \\
 - 1 \\
\end{pmatrix}
$$

*Equating the two lines*

$$
\begin{pmatrix}
1 + s \\
2 - s \\
3 \\
\end{pmatrix} = \begin{pmatrix}
1 - 2t \\
5 + t \\
2 - t \\
\end{pmatrix}
$$

*Equation 1:* $1 + s = 1 - 2t$ so $s = - 2t$

*Equation 2:* $2 - s = 5 + t$

*Substitute 1 into 2:*

$$
2 + 2t = 5 + t
$$

$\therefore t = 3$ and then $s = - 6$

*Equation 3:*

$$3 = 2 - t$$

*Substitute the value of* $t$

$3 = 2 - 3$ so $3 = - 1$

*This is incorrect therefore lines don’t intersect*

**<span class="underline">Part (ii)</span>**

*Angle* $\text{PAB}$ *is formed by the intersection of the lines*
$\text{AP}$ *and* $\text{AB}$

$$
P = \begin{pmatrix}
1 - 2t \\
5 + t \\
2 - t \\
\end{pmatrix}
$$

$$
AP = OP - OA
$$

$$
AP = \begin{pmatrix}
1 - 2t \\
5 + t \\
2 - t \\
\end{pmatrix} - \begin{pmatrix}
1 \\
2 \\
3 \\
\end{pmatrix} = \begin{pmatrix}
 - 2t \\
3 + t \\
 - 1 - t \\
\end{pmatrix}
$$

$$
AB = \begin{pmatrix}
1 \\
 - 1 \\
0 \\
\end{pmatrix}
$$

*Now use the dot product rule to form an eqn.*

$$
\frac{\left| \text{AP.AB} \right|}{\left| \text{AP} \right|\left| \text{AB} \right|};\ \frac{- 3t - 3}{\sqrt{6t^{2} + 8t + 10} \times \sqrt{2}} = \cos 60
$$

$$
3t - 3 = \frac{1}{2}\sqrt{6t^{2} + 8t + 10} \times \sqrt{2}
$$

$$
36t^{2} + 72t + 36 = 12t^{2} + 16t + 20
$$

$$
24t^{2} + 56t + 16 = 0
$$

$t = - \frac{1}{3}$ or $t = - 2$

&nbsp;

**<span class="underline">{W11-P31} Question:</span>**

With respect to the origin $O$, the position vectors of two points
$A$ and $B$ are given by
$\overrightarrow{\text{OA}} = \mathbf{i} + 2\mathbf{j} + 2\mathbf{k}$
and

$\overrightarrow{\text{OB}} = 3\mathbf{i} + 4\mathbf{j}$**.** The
point $P$ lies on the line through $A$ and $B$, and
$\overrightarrow{\text{AP}} = \lambda\overrightarrow{\text{AB}}$

i)  $\overrightarrow{\text{OP}} = \left( 1 + 2\lambda \right)\mathbf{i} + \left( 2 + 2\lambda \right)\mathbf{j} + \left( 2 - 2\lambda \right)\mathbf{k}$

ii)  By equating expressions for $\cos\text{AOP}$ and
    $\cos\text{BOP}$ in terms of $\lambda$, find the value of
    $\lambda$ for which $\text{OP}$ bisects the angle
    $\text{AOB}$.

**<center>Solution:</center>**

**<span class="underline">Part (i)</span>**

$$
\overrightarrow{\text{AP}} = \lambda\overrightarrow{\text{AB}} = \lambda\left( OB - OA \right)
$$

$$
= \lambda\begin{pmatrix}
3 \\
4 \\
0 \\
\end{pmatrix} - \begin{pmatrix}
1 \\
2 \\
2 \\
\end{pmatrix} = \begin{pmatrix}
2 \\
2 \\
 - 2 \\
\end{pmatrix}
$$

$$
\therefore AP = \ \begin{pmatrix}
2\lambda \\
2\lambda \\
 - 2\lambda \\
\end{pmatrix}
$$

$$
OP = OA + \begin{pmatrix}
2\lambda \\
2\lambda \\
 - 2\lambda \\
\end{pmatrix} = \begin{pmatrix}
1 \\
2 \\
2 \\
\end{pmatrix} + \begin{pmatrix}
2\lambda \\
2\lambda \\
 - 2\lambda \\
\end{pmatrix}
$$

**<span class="underline">Part (ii)</span>**

*Interpreting the question gives the information that* $\text{AOP}$
*is equal to* $BOP\therefore$ $\cos\text{AOP}$ *is equal to*
$\cos\text{BOP}$*. Now you can equate the two dot product equations*

$$
\cos\text{AOP} = \frac{\text{OA.OP}}{\left| \text{OA} \right|\left| \text{OP} \right|} = \frac{9 + 2\lambda}{3\sqrt{9 + 4\lambda + 12\lambda^{2}}}
$$

$$
\cos\text{BOP} = \frac{\text{OB.OP}}{\left| \text{OB} \right|\left| \text{OP} \right|} = \frac{11 + 14\lambda}{5\sqrt{9 + 4\lambda + 12\lambda^{2}}}
$$

$$
\frac{9 + 2\lambda}{3\sqrt{9 + 4\lambda + 12\lambda^{2}}} = \frac{11 + 14\lambda}{5\sqrt{9 + 4\lambda + 12\lambda^{2}}}
$$

*Cancel out the denominator to give you*

$$
\frac{9 + 2\lambda}{3} = \frac{11 + 14\lambda}{5}
$$

$$
45 + 10\lambda = 33 + 42\lambda
$$

$12 = 32\lambda$ and $\therefore\lambda = \frac{3}{8}$
