## Derivation of Pressure formula for Ideal Gas

For a single molecule of mass $m$ and velocity $u_x$ bouncing elastically off a wall of area $A$ in a cube of length $L$:

* Change in momentum per collision: $\Delta p_x = 2m u_x$

* Time between collisions with the same wall: $\Delta t = \frac{2L}{u_x}$

* Average force per molecule: $F_x = \frac{\Delta p_x}{\Delta t} = \frac{m u_x^2}{L}$

![Kinetic Gas Equation Cubic Container](https://images.znotes.org/allimages/df596973c22e1c8fb28a3454.webp =448x)

**For $N$ Molecules:** Total force on the wall from all $N$ molecules is $F =\frac{N m \langle c_x^2 \rangle}{L}$, where $\langle c_x^2 \rangle$ is the mean-square speed in the $x$-direction.

**Extending to 3D:** Motion is isotropic (equal in all dimensions), so:

$$\langle c^2 \rangle = \langle c_x^2 \rangle + \langle c_y^2 \rangle + \langle c_z^2 \rangle = 3 \langle c_x^2 \rangle \implies \langle c_x^2 \rangle = \frac{1}{3} \langle c^2 \rangle$$

**Final Derivation:** Substituting $\langle c_x^2 \rangle$ into pressure $p = \frac{F}{A} = \frac{F}{L^2}$:

$$

p = \frac{N m \left\(\frac{1}{3}\langle c^2 \rangle\right\)}{L^3} = \frac{1}{3} \frac{N m \langle c^2 \rangle}{V} \implies pV = \frac{1}{3} N m \langle c^2 \rangle

$$

$\langle c^2 \rangle$ is the **mean-square speed:** Average of the squared speeds of all particles ($\text{m}^2 \text{s}^{-2}$)

$c_{\text{rms}} = \sqrt{\langle c^2 \rangle}$ which is the **root-mean-square speed:** Square root of the mean-square speed ($\text{m s}^{-1}$)