---
note_id: "rn_CT4n4tyXRmZXkrKn"
title: "Derivation of the Kinetic Theory of Gases Equation"
source: https://www.savemyexams.com/a-level/physics/cie/25/revision-notes/15-ideal-gases/15-3-kinetic-theory-of-gases/derivation-of-the-kinetic-theory-of-gases-equation
path: 15-ideal-gases/15-3-kinetic-theory-of-gases/derivation-of-the-kinetic-theory-of-gases-equation
updated_at: "2026-10-08T14:17:03.484Z"
spec_point_ids: ["spcpt_XrS6py9275ZQvvDf", "spcpt_kNySbncfcZKPxpKJ"]
spec_point_codes: []
guided_study: true
---

# Derivation of the Kinetic Theory of Gases Equation

## Derivation of the Kinetic Theory of Gases Equation

> **Spec point** — `spcpt_XrS6py9275ZQvvDf`

## Derivation of the kinetic theory of gases equation

- **Molecular movement** causes the **pressure** exerted by a gas

  - When molecules rebound from their container wall, the **change in momentum** gives rise to a **force** exerted by the particles on the wall
  - Many molecules moving in random motion exert forces on the walls, which creates an average overall **pressure** (since pressure is the force per unit area)

### Setting up the model

- Take a **single molecule** in a cube-shaped box with **sides** of equal **length **$L$
- The molecule has **mass **$m$ and moves with **speed **$c$ parallel to one side of the box
- It collides at regular intervals with the sides of the box, exerting a force and contributing to the pressure of the gas
- By calculating the pressure this **one molecule** exerts on **one end** of the box, the total pressure produced by a total of $N$ molecules can be deduced

#### Modelling a gas molecule in a container

![Single molecule in box, downloadable AS & A Level Physics revision notes](../../../assets/38c01cc46ed1-15-2-single-molecule-in-box.png)

***A single molecule in a box collides with the walls and exerts a pressure***

### Deriving the equation step-by-step

**     1. Find the change in momentum as a single molecule hits a wall perpendicularly**

- One assumption of the kinetic theory is that molecules **rebound elastically**

  - This means there is no kinetic energy lost in the collision
- If a molecule rebounds in the opposite direction to its initial velocity $c$, its final velocity will be $-c$
- The change in momentum is therefore:

$\Deltap=p_{f}-p_{i}$

$\Delta p = - m c - ( + m c ) = - m c - m c = - 2 m c$

**     2. Calculate the number of collisions per second by the molecule on a wall**

- The time between collisions of the molecule travelling to one wall and back is calculated by travelling a distance of $2l$ with speed $c$:

Time between collisions = $\frac{\mathrm{distance}}{\mathrm{speed}}=\frac{2l}{c}$

- **Note:** $c$ is **not **taken as the speed of light in this scenario

**     3. Find the change in momentum per second**

- The average force the molecule exerts on one wall is found using Newton’s second law of motion:

$F=\frac{\Deltap}{\Deltat}$

$F=\frac{2mc}{\frac{2l}{c}}=\frac{mc^{2}}{l}$

- The change in momentum is $+2mc$ since the force on the molecule from the wall is in the opposite direction to its change in momentum

**     4. Calculate the total pressure from N molecules**

- The area $A$ of one wall is $l^{2}$
- The pressure $p$ is defined as the force per unit area:

$p=\frac{F}{A}$

$p=\frac{\frac{mc^{2}}{l}}{l^{2}}=\frac{mc^{2}}{l^{3}}$

- This is the pressure exerted on the container wall by **one molecule**
- To account for the large number of *N* molecules, the pressure can now be written as:

$p=\frac{Nmc^{2}}{l^{3}}$

- Each molecule has a different velocity and they all contribute to the pressure
- The mean square speed $c^{2}$ is written with left and right-angled brackets `< c ^2 >`
- The pressure is now defined as:

$p = \frac{N m ( \text{angle} \text{brackets} c^{2} ) \text{angle} \text{brackets} }{l^{3}}$

**     5. Consider the effect of the molecule moving in 3D space**

- The pressure equation still assumes all the molecules are travelling in the **same direction** and colliding with the same pair of opposite faces of the cube
- In reality, all molecules will be moving in three dimensions equally and randomly, with different velocities $c$:

$c^{2}=c_{x}^{2}+c_{y}^{2}+c_{z}^{2}$

- Where $c_{x}$, $c_{y}$, and $c_{z}$ are the $x$-, $y$-, and $z$- components of the velocity

  - This equation is a result of Pythagoras' theorem in 3D
- Since pressure is due to the force exerted on one face of the cube, only the component of velocity **perpendicular **to that face (e.g. the $x$-direction) matters
- For a gas with molecules moving randomly in all directions, the mean square speed is evenly distributed among all three directions:

`< c _ x ^ 2 > = < c _ y ^ 2 > = < c _ z ^ 2 >`

- Therefore, the mean square speed in the $x$-direction `open angle brackets c subscript x superscript 2 close angle brackets` accounts for a third of the total mean square speed `< c ^2 >`

$( \text{angle} \text{brackets} c_{x}^{2} ) \text{angle} \text{brackets} = 1 \frac{1}{3} ( \text{angle} \text{brackets} c^{2} ) \text{angle} \text{brackets}$

- This is why only one-third of the total mean square speed contributes to the pressure on one wall

**     6. Re-write the pressure equation**

- The box is a cube, and all the sides are of length $l$

  - This means the volume $V$ of the cube is equal to $l^{3}$
- Substituting the new values for `< c ^2 >`  and $l^{3}$ back into the pressure equation obtains the final equation:

$p V = 1 \frac{1}{3} N m ( \text{angle} \text{brackets} c^{2} ) \text{angle} \text{brackets}$

- Where:

  - $p$ = pressure (Pa)
  - $V$ = volume (m<sup>3</sup>)
  - $N$ = number of molecules
  - $m$ = mass of one molecule (kg)
  - `< c ^2 >` = mean square speed of the molecules (m<sup>2</sup> s<sup>–2</sup>)

- This can also be written using the density *ρ* of the gas:

$ρ=\frac{\mathrm{mass}}{\mathrm{volume}}=\frac{Nm}{V}$

- Rearranging the pressure equation for $p$ and substituting the density $ρ$:

$p = 1 \frac{1}{3} \\rho ( \text{angle} \text{brackets} c^{2} ) \text{angle} \text{brackets}$

> **Worked Example**
> An ideal gas has a density of 4.5 kg m<sup>-3</sup> at a pressure of 9.3 × 10<sup>5</sup> Pa and a temperature of 504 K.
> 
> Determine the root-mean-square (r.m.s.) speed of the gas atoms at 504 K.
> 
> **Answer:**
> 
> **Step 1: Write out the equation for the pressure of an ideal gas with density**
> 
> $p=\frac{1}{3}ρ<c^{2}>$
> 
> **Step 2: Rearrange for mean square speed**
> 
> $<c^{2}>=\frac{3p}{ρ}$
> 
> **Step 3: Substitute in values**
> 
> $< c^{2} > = \frac{3 \times ( 9.3 \times 10^{5 ) }{4.5} = 6.2 \times 10^{5} \mathrm{m}^{2} \mathrm{s}^{-2} }$
> 
> **Step 4: To find the r.m.s value, take the square root of the mean square speed**
> 
> $c_{r. m. s} = \sqrt{< c^{2} >} = \sqrt{6.2 \times 10^{5} = 787.4 = 790 \mathrm{m} \mathrm{s}^{-1} } ( 2 \mathrm{s} . \mathrm{f} . )$

## Root-Mean-Square Speed

> **Spec point** — `spcpt_kNySbncfcZKPxpKJ`

## Root-mean-square speed

- The equation for the kinetic theory of ideal gases contains the **mean square speed** of the molecules:

`< c ^2 >`

- Where

  - $c$ = velocity of **one **gas molecule (m s<sup>-1</sup>)
  - `open angle brackets c close angle brackets` = **average **velocity of the molecules in a gas (m s<sup>-1</sup>)
  - `< c ^2 >` = **average **of the **square **of the** **speeds of the molecules in a gas (m<sup>2</sup> s<sup>-2</sup>)
- Since there are a large number of molecules in a gas, travelling in all directions in 3D space, this results in a large range of values of $c$
- The average velocity `open angle brackets c close angle brackets` of all the molecules in a gas gives a net zero value overall

  - This is because velocity is a vector, so some molecules will have a negative direction and others a positive direction
- Squaring the velocities gives positive values only
- Averaging the values of $c^{2}$ gives `< c ^2 >`, the **mean square speed**
- Then, taking the square root of the mean square speed gives:

$c_{r. m. s} = \sqrt{( \text{angle} \text{brackets} c^{2} ) \text{angle} brackets}$

- $c_{r.m.s}$ is known as the** root-mean-square** speed and has units of **m s**<sup>**-1**</sup>

  - The root-mean-square speed $c_{r.m.s}$ is **not** the same as the mean speed `open angle brackets c close angle brackets`
