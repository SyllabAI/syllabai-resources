# Mark Schemes — Calculus for Kinematics
**Calculus** · Cambridge (CIE) IGCSE further-maths (0606)


## Exam Questions (14 questions)


### Q1
> *Differentiate velocity to find acceleration*

**Method 1**

> *Expand and simplify the velocity first*

$\begin{gathered} v = 6 ( t^{2} - 1 \frac{1}{2} t - 1 \frac{1}{2} t + 1 \frac{1}{4} ) + \frac{5}{2} \\ v = 6 ( t^{2} - t + 1 \frac{1}{4} ) + \frac{5}{2} \\ v = 6 t^{2} - 6 t + \frac{3}{2} + \frac{5}{2} \\ v = 6 t^{2} - 6 t + 4 \end{gathered}$

**[M1]**

> *Then differentiate *$v$* to find *$a$

$a=12t-6$

**[M1 A1]**

> *Substitute in *$t=2$

$a=12\times2-6$

**Final answer:** **18 ms**<sup>**-2**</sup>

**[A1]**

**Method 2**

> *Use the chain rule, *$a=\frac{dv}{dt}=\frac{dv}{du}\frac{du}{dt}$* where *$u=t-\frac{1}{2}$

$\begin{gathered} v = 6 u^{2} + \frac{5}{2} u = t - 1 \frac{1}{2} \\ \frac{ \mathrm{d} v}{ \mathrm{d} u} & = 12 u \frac{ \mathrm{d} u}{ \mathrm{d} t} = 1 \end{gathered}$

**[M1]**

> *This gives*

$\begin{gathered} a = 12 u \times 1 \\ a = 12 ( t - 1 \frac{1}{2} ) \end{gathered}$

**[A1 A1]**

> **[mark-scheme]**
> **A1:** For an answer at least in the form $k ( t - 1 \frac{1}{2} )$.
> 
> **A1:** For $12 ( t - 1 \frac{1}{2} )$ or $12t-6$.

> *Substitute in *$t=2$

$a = 12 ( 2 - 1 \frac{1}{2} )$

**Final answer:** **18 ms**<sup>**-2**</sup>

**[A1]**
**Method 1**

> *Integrate *$v=6t^{2}-6t+4$* to get displacement *$s$* and add a constant of integration*

$s=\frac{6t^{3}}{3}-\frac{6t^{2}}{2}+4t+c$

**[M1]**

> **[mark-scheme]**
> This mark is for at least two correct terms in $t$ (can be unsimplified).

> *Simplify*

$s=2t^{3}-3t^{2}+4t+c$

**[A1]**

> *The initial displacement is *$-1$* so substitute in *$s=-1$* when *$t=0$* to find *$c$

$\begin{gathered} - 1 & = 0 - 0 + 0 + c \\ c = - 1 \end{gathered}$

> *Substitute this value of *$c$* back into the expression for *$s$

$s=2t^{3}-3t^{2}+4t-1$

**[A1]**

> *Substitute in *$t=2$

$s = 2 ( 2 )^{3} - 3 ( 2 )^{2} + 4 ( 2 ) - 1$

**Final answer:** **11  m**

**[A1]**

**Method 2**

> *Integrate *$v = 6 ( t - 1 \frac{1}{2} )^{2} + \frac{5}{2}$* using *$\int ( a x + b )^{n \mathrm{d} x = \frac{1}{a} \times \frac{1}{n + 1} ( a x + b )^{n} + 1} + c$* to get displacement *$s$* *

> *Add a constant of integration*

$s = 6 \times \frac{1}{1} \times 1 \frac{1}{3} ( t - 1 \frac{1}{2} )^{3} + \frac{5}{2} t + c$

**[M1 A1]**

> *Simplify*

$s = 2 ( t - 1 \frac{1}{2} )^{3} + \frac{5}{2} t + c$

> *The initial displacement is *$-1$* so substitute in *$s=-1$* when *$t=0$* to find *$c$

$\begin{gathered} - 1 & = 2 ( 0 - 1 \frac{1}{2} )^{3} + 0 + c \\ - 1 & = - 1 \frac{1}{4} + c \\ c = - \frac{3}{4} \end{gathered}$

> *Substitute this value of *$c$* back into the expression for *$s$

$s = 2 ( t - 1 \frac{1}{2} )^{3} + \frac{5}{2} t - \frac{3}{4}$

**[A1]**

> *Substitute in *$t=2$

$s = 2 ( 2 - 1 \frac{1}{2} )^{3} + \frac{5}{2} ( 2 ) - \frac{3}{4}$

**Final answer:** **11  m**

**[A1]**
> *Speed is the positive part of the velocity, *$\vert v \vert$

**Method 1**

> *Use algebra to show that *$v = 6 ( t - 1 \frac{1}{2} )^{2} + \frac{5}{2}$* is always positive*

> *Start by noting that *$( t - 1 \frac{1}{2} )^{2} \text{greater} \text{or} \text{equal} \text{than} 0$* as it is a squared expression*

$\begin{gathered} ( t - 1 \frac{1}{2} )^{2} & \text{greater} \text{or} \text{equal} \text{than} 0 \\ 6 ( t - 1 \frac{1}{2} )^{2} & \text{greater} \text{or} \text{equal} \text{than} 0 \\ 6 ( t - 1 \frac{1}{2} )^{2} + \frac{5}{2} & > 0 \end{gathered}$

> *This expression is actually positive for all *$t$* values, but you need just *$t\geq0$

**Final answer:** $v = 6 ( t - 1 \frac{1}{2} )^{2} + \frac{5}{2}$** is always positive for **$t\geq0$** so the velocity-time graph and speed-time graph are the same**

**[B1]**

> **[mark-scheme]**
> Your answer must refer to the fact that $v = 6 ( t - 1 \frac{1}{2} )^{2} + \frac{5}{2}$ is always positive for $t\geq0$ (or all $t$) to score the mark.

**Method 2**

> *The velocity-time graph of *$v = 6 ( t - 1 \frac{1}{2} )^{2} + \frac{5}{2}$* is a U-shaped quadratic with a minimum point of *$( 1 \frac{1}{2} , \frac{5}{2} )$* above the *$t$*-axis*

![Graph of a quadratic curve on v-t axes with a minimum point at (1/2, 5/2). The graph is U-shaped and fully above the x-axis.](assets/001-graph-of-a-quadratic-curve-on-v-t-axes-with-a-mi.png)

**Final answer:** $v = 6 ( t - 1 \frac{1}{2} )^{2} + \frac{5}{2}$** is always positive for **$t\geq0$** so the velocity-time graph and speed-time graph are the same**

**[B1]**

> **[mark-scheme]**
> Your answer must refer to $v = 6 ( t - 1 \frac{1}{2} )^{2} + \frac{5}{2}$ always being positive for $t\geq0$ (or all $t$)  to score the mark.
> 
> The graph sketch is not necessary for the mark.

> **[exam-tip]**
> Even though the graph sketch is not awarded any marks here, it is still a good idea to include it.

### Q2
> *The particle moves in a straight line so we have a linear relationship between the initial and final velocity, which is dependent upon the acceleration*

> *Form a linear equation*

$v=-6t+c$

**[1]**

> *The constant is the initial velocity which is 18*

$v=-6t+18$

**[1]**

> *Substitute the final velocity, because we know the particle is at rest*

$0=-6t+18$

$0 = ( - 6 ) t + 18$

> *Solve to find *$t$

$t=\frac{18}{6}=3$

$t=3$ **[1]**
> *Displacement (*$s$*) is the integral of velocity.  From part (a), *$v=18-6t$*.*
* The third second is between *$t=2$* and *$t=3$*.*

$s = \int_{2}^{3} ( 18 - 6 t ) \mathrm{d} t = [ 18 t - 3 t^{2} ]_{2}^{3}$

**[1]**

> *Apply the limits.*

$\begin{gathered} s = [ 18 \times 3 - 3 \times 3^{2} ] - [ 18 \times 2 - 3 \times 2^{2} ] \\ s = 27 - 24 \end{gathered}$

**[1]**

> *As positive, distance will be the same as displacement.*

**P**** travels a distance of 3 metres in the third second** **[1]**

### Q3
> *To find the expression for velocity, *$v$*, integrate the expression for acceleration.*

> *Integrate using reverse chain rule.*

$\int ( 2 t + 1 )^{- 1 \frac{1}{2}} \mathrm{d} t = \frac{( 2 t + 1 )^{1 \frac{1}{2}} }{1 \frac{1}{2}} \times 1 \frac{1}{2} + C$

$v = ( 2 t + 1 )^{1 \frac{1}{2}} + C$

$[ 1 ]$

> *To find C, substitute *$t=0$* and *$v=8$* into the equation.*

> $8 = ( 2 ( 0 ) + 1 )^{1 \frac{1}{2}} + C$*  *

> *Simplify, then rearrange, to find C.*

$8=\sqrt{1}+C$

$C=7$

$[ 1 ]$

> *Substitute *$C=7$* into the equation for velocity.*

> $v=(2t+1)^{\frac{1}{2}}+7$* *$[ 1 ]$
> *To find the expression for displacement, *$s$*, integrate the expression for velocity.  *

$\int ( ( 2 t + 1 )^{1 \frac{1}{2}} + 7 ) \mathrm{d} t$

> *Break up the integral.*

$\int ( 2 t + 1 )^{1 \frac{1}{2}} \mathrm{d} t + \int 7 \mathrm{d} t$

> *Integrate *$( 2 t + 1 )^{1 \frac{1}{2}}$* with respect to *$t$* using reverse chain rule.*

$\text{integral} ( 2 t + 1 ) ^{1} \text{half} \mathrm{d} t = \frac{ ( 2 t + 1 ) ^{\frac{3}{2}}}{\frac{3}{2}} \times 1 \text{half} + d$

$= 1 \frac{1}{3} ( 2 t + 1 )^{ \frac{3}{2} } + d$

> *Hence,*

$s = 1 \frac{1}{3} ( 2 t + 1 )^{ \frac{3}{2} } + 7 t + d$

**for an attempt to integrate answer to part **$a$$[ 1 ]$

**for correct result **$[ 1 ]$

> *To find *$d$*, substitute *$s=4$* and *$t=0$* into the equation.*

`4 = ( 2 ( 0 ) + 1 ) ^ 3 / 2 / 3 + 7 ( 0 ) + d`

> *Simplify, then rearrange, to find *$d$*.*

$4=\frac{1}{3}+d$

$d=\frac{11}{3}$

$[ 1 ]$

> *Substitute *$d=\frac{11}{3}$*into the equation for displacement.*

$s=\frac{1}{3}(2t+1)^{\frac{3}{2}}+7t+\frac{11}{3}$ $[ 1 ]$** **

### Q4
> *To find an expression for velocity, **v**, integrate the acceleration function *
*We can use *$\int ( a x + b )^{n \mathrm{d} x = \frac{ 1}{a} \times \frac{1}{n + 1} ( a x + b )^{n} + 1} + c$

$v = \int ( 3 t + 2 )^{- 1 \frac{1}{3}} \mathrm{d} t = \frac{ 1}{3} \times \frac{3}{2} ( 3 t + 2 )^{ \frac{2}{3} } + c$

**[1]**

> *                         *$= 1 \frac{1}{2} ( 3 t + 2 )^{ \frac{2}{3} } + c$

> *To find the constant of integration, substitute *$t=2$* and *$v=8$*the limits of integration*

$8 = 1 \frac{1}{2} ( 3 \times 2 + 2 )^{ \frac{2}{3} } + c$

**[1]**

> *Solve*

$8 = 1 \frac{1}{2} ( 8 )^{ \frac{2}{3} } + c
8 = 1 \frac{1}{2} \times 4 + c
8 = 2 + c
c = 6$

> *Don't forget to write out the full expression at the end for the final mark*

$v=\frac{1}{2}(3t+2)^{\frac{2}{3}}+6$  **[1]**
**Because the formula for the velocity is **$v=\frac{1}{2}(3t+2)^{\frac{2}{3}}+6$** and we are told that **$t\geq0$**, so the velocity will always be positive** **[1]**

**In actual fact the velocity will always be greater than 6**
> *To find an expression for displacement, **s**, integrate the velocity function Again, we can use *$\int ( a x + b )^{n \mathrm{d} x = \frac{ 1}{a} \times \frac{1}{n + 1} ( a x + b )^{n} + 1} + c$

$s = \int ( 1 \frac{1}{2} ( 3 t + 2 )^{1 \frac{1}{3}} + 6 ) \mathrm{d} t = \frac{ 1}{2} ( 1 \frac{1}{3} \times \frac{3}{5} ( 3 t + 2 )^{ \frac{5}{3} } ) + 6 t + c$

**[1]**

> *                         *$= \frac{1}{10} ( 3 t + 2 )^{ \frac{5}{3} } + 6 t + c$

> *To find the constant of integration, substitute *$t=2$* and *$s=-4.8$

$- 4.8 = \frac{1}{10} ( 3 \times 2 + 2 )^{ \frac{5}{3} } + 6 \times 2 + c$

**[1]**

> *Solve*

$\begin{gathered} - 4.8 & = \frac{1}{10} ( 8 )^{ \frac{5}{3} } + 12 + c \\ - 4.8 & = \frac{ 1}{10} \times 32 + 12 + c \\ - 4.8 & = 3.2 + 12 + c \\ - 4.8 & = 15.2 + c \\ - 20 & = c \end{gathered}$

> *Therefore *

$s = \frac{1}{10} ( 3 t + 2 )^{ \frac{5}{3} } + 6 t - 20$

**[1]**

> *Substitute *$t=\frac{25}{3}$* into *$s$

$t = \frac{25}{3} , s = \frac{1}{10} ( 3 ( \frac{25}{3} ) + 2 )^{ \frac{5}{3} } + 6 ( \frac{25}{3} ) - 20$

$= \frac{1}{10} ( 27 )^{ \frac{5}{3} } + \frac{150}{3} + 20
= \frac{1}{10} \times 243 + 50 + 20
= 24.3 + 50 - 20$

**54.3**  **[1]**

### Q5
(i) *To find velocity, *$v$*, divide displacement, *$x$*, by time, *$t$*.*

> *For *$0\leqt\leq50$

$100\div50=2$

> *For *$50\leqt\leq65$

$0\div15=0$

> *  *

> *For *$65\leqt\leq85$

$50\div20=2.5$

> *  *

> *For *$85\leqt\leq125$

$-150\div40=-3.75$

> * *

> *Draw the lines on the given axes.*

**for correct line at **$v=2$** **$[ 1 ]$

**for correct line at **$v=2.5$** **$[ 1 ]$

**for correct line at  **$v=3.75$** and **$v=0$** **$[ 1 ]$

(ii) $0\leqt\leq50$*, the distance covered is 100m.*

> $50\leqt\leq65$*, the distance covered is 0m.*

> $65\leqt\leq85$*, the distance covered is 50m.*

> $85\leqt\leq125$*, the distance covered is 150m.*

$100+0+50+150=300$

$300m$ $[ 1 ]$

### Q6
(i) *To find the expression for velocity, **v,** integrate the expression for acceleration.   *

$\int ( 6 \cos 2 t ) \mathrm{d} t = 3 \sin 2 t + C$

$v=3\mathrm{sin}2t+C$

$[ 1 ]$

> *To find C, substitute *$t=0$* and *$v=10$* into the equation.*

> *  *

> $10 = 3 \sin ( 2 \times 0 ) + C$*  *

> *Simplify, then rearrange, to find C.*

$C=10$

$[ 1 ]$

> *Substitute *$C=10$* into the equation for velocity.*

> $v=3\mathrm{sin}2t+10$* *$[ 1 ]$

ii) *To find the expression for displacement, *$s$*, integrate the expression for velocity.  *

$\int ( 3 \sin 2 t + 10 ) \mathrm{d} t$

> *Break up the integral.*

$\int ( 3 \sin 2 t ) \mathrm{d} t + \int 10 \mathrm{d} t$

> *Integrate *$3\mathrm{sin}2t$* with respect to *$t$*.*

$\int ( 3 \sin 2 t ) \mathrm{d} t = \frac{ - 3 \cos 2 t}{2} + d$

$= - \frac{3}{2} ( \cos 2 t ) + d$

> *Combine with the integral of 10.*

$s = - \frac{3}{2} ( \cos 2 t ) + 10 t + d$

$[ 1 ]$

> *To find *$d$*, substitute *$s=0$* and *$t=0$* into the equation.*

> *  *

$\begin{gathered} 0 = - \frac{3}{2} ( \cos 0 ) + 10 ( 0 ) + d \\ d = \frac{3}{2} \end{gathered}$

$[ 1 ]$

> *Substitute *$d=\frac{3}{2}$*into the equation for displacement.*

**Final answer:** $s=-\frac{3}{2}(cos2t)+10t+\frac{3}{2}$** **$[ 1 ]$

### Q7
i) $0-10$ *seconds, the runner travels *$50$*m.*
* *$10-40$* seconds, the runner travels *$60$*m.  *

$50+60$

> $110$*m *$[ 1 ]$

ii) *Work out the gradient for each line to find velocity. *
*For *$0-10$* seconds*

$\frac{50}{10}=5$* **m/s*

> *For *$10-40$* seconds*

$\frac{-60}{30}=-2$ *m/s*

> *Draw on the axes provided.*

> *   *

![olevelciemay21paper1q7a](assets/005-olevelciemay21paper1q7a.jpg)

**for a line joining **$( 0 , 5 )$** and **$( 10 , 5 )$** **$[ 1 ]$

**for a line joining **$( 10 , - 2 )$** and **$( 40 , - 2 )$** **$[ 1 ]$

### Q8
> *Velocity is the change in speed with respect to time, therefore differentiate to get*

$v=\frac{ds}{dt}=2e^{2t}-10e^{t}-12$

$2e^{2t}$** [1]**

** fully correct expression**** [1]**

> *Acceleration is the change in velocity with respect to time, therefore we differentiate to get*

$a=\frac{dv}{dt}=4e^{2t}-10e^{t}$ **[1]**
> *If the particle is at rest, this means that the velocity is 0.*

$0=2e^{2t}-10e^{t}-12$

> *This is a hidden quadratic which is easier to solve if we let *$e^{t}=x$

$0=2x^{2}-10x-12$

> *Dividing through by 2 gives*

$0=x^{2}-5x-6$

> *We can factorise this by looking for a factor pair of -6 that has a sum of -5. This would be -6 and +1.*

$0 = ( x - 6 ) ( x + 1 )$

**[1]**

> *This means that the solutions are*

$x=6\Rightarrowe^{t}=6$

**[1]**

$x=-1\Rightarrowe^{t}=-1$* **which has no solutions*

> *Taking natural log of both sides of the first solution gives*

$t=\mathrm{ln}6(\mathrm{seconds})$  **[1]**
> *Substituting *$t=\mathrm{ln}6$* into the equation for *$a$* gives*

$a=4e^{2\mathrm{ln}6}-10e^{\mathrm{ln}6}$

** ****correct substitution ****[1]**

$a=84(\mathrm{ms}^{-2})$ **[1]**

### Q9
(i) *The area under the line on a velocity-time graph is equal to the displacement of the object.*

> *Since we are given the displacement, 2775m, we can find the final velocity, **V**, by finding the area under the graph. equating it to 2775 and then solving to find **V**.*

> *  *

> *Split the area under the graph into two trapeziums, find their areas, add them together and equate to 2775.*

$1 \frac{1}{2} ( 60 + 40 ) ( 30 ) + 1 \frac{1}{2} ( 30 + V ) ( 30 ) = 2775$

**for an attempt to find the area under the graph **$[ 1 ]$

**for equating to 2775 **$[ 1 ]$

> *Rearrange and solve for **V**.*

$\begin{gathered} 1500 + 15 ( 30 + V ) & = 2775 \\ 15 ( 30 + V ) & = 1275 \\ 30 + V & = 85 \\ V = 55 \end{gathered}$

> *   *

> $V=55\mathrm{ms}^{-1}$* *$[ 1 ]$

(ii) *Examine the graph.*

> *When *$t=40$*, the graph is a horizontal line with a gradient of 0. Therefore, the acceleration at this time is 0.*

> *   *

$0$** **$[ 1 ]$

### Q10
i) *The differential of displacement is velocity*

$( v = ) \frac{ \mathrm{d} x}{ \mathrm{d} t} = 20 \cos 2 t$

> *At time *$t=π$

$v = 20 \cos ( 2 \mathrm{\pi } ) = 20 \times 1 = 20$

> *As this is positive, speed will be the same*

**Speed of particle ****P**** at time **$π$** seconds is **$20ms^{-1}$ **[1]**

ii) *When **P** is at rest, *$v=0$

> *Use the equation from part (i)*

$20\mathrm{cos}2t=0$

**[1]**

$\mathrm{cos}2t=0$

`2 t = cos ^ - 1 ( 0 ) = pi / 2`

> *Divide by 2 to find **t*

$t=\frac{π}{4}$

$\frac{π}{4}s$* ***[1]**

iii) *To find the acceleration, differentiate the velocity*

$v=20\mathrm{cos}2t$

$\frac{dv}{dt}=-40\mathrm{sin}2t$

**[1]**

> *Calculate the acceleration when *$t=\frac{π}{4}$

`( d v)/( d t) = - 40 sin ( 2 x pi / 4 ) = - 40`

$-40\mathrm{ms}^{-2}$ **[1]**

### Q11
i) *Use the first section of the graph when the particle is accelerating*

> *The acceleration is the gradient of the graph*

$\mathrm{acceleration}=\frac{\mathrm{final} \mathrm{speed}-\mathrm{initial} \mathrm{speed}}{\mathrm{time}}$

$3.5=\frac{V-0}{10}$

$V=35\mathrm{ms}^{-1}$

$35$ **[1]**

ii) *Use the area of the trapezium to find the unknown velocity*

> *The area of the trapezium = distance travelled = 112.5 m*

$Area of \text{trapezium} = 1 \text{half} ( a + b ) h$

$112.5 = 1 \frac{1}{2} ( 35 + b ) 5$

$225 = ( 35 + b ) 5$

$45=35+b$

$b=10\mathrm{ms}^{-1}$

$10$ **[1]**

iii) *Find the deceleration of the particle *

> *Initial velocity = 35*

> *Final velocity = 10*

> *Time = 5*

$\mathrm{deceleration}=\frac{\mathrm{final} \mathrm{speed}-\mathrm{initial} \mathrm{speed}}{\mathrm{time}}$

$\mathrm{deceleration}=\frac{35-10}{5}=5\mathrm{ms}^{-2}$

**[1]**

> *Use the gradient of the last section of the graph*

$5=\frac{35}{t-20}$

**[1]**

$t-20=\frac{35}{5}$

$t-20=7$

$t=27s$

$27$ **[1]**

### Q12
i) *To find the expression for velocity, integrate the expression for acceleration. Integrate using reverse chain rule.*

$\int ( 2 t + 4 )^{- 1 \frac{1}{2}} \mathrm{d} t = \frac{( 2 t + 4 )^{1 \frac{1}{2}} }{1 \frac{1}{2}} \times 1 \frac{1}{2} + C$

$V = ( 2 t + 4 )^{1 \frac{1}{2}} + C$

$[ 1 ]$

> *To find C, substitute *$t=6$* and *$V=9$* into the equation.*

> $9 = ( 2 ( 6 ) + 4 )^{1 \frac{1}{2}} + C$*  *

> *Simplify, then rearrange, to find C.*

$9=\sqrt{16}+C$

$C=5$

$[ 1 ]$

> *Substitute *$C=5$*into the equation for velocity.*

> $V=(2t+4)^{\frac{1}{2}}+5$* *$[ 1 ]$

ii) *To find the expression for displacement, integrate the expression for velocity.  *

$\int ( ( 2 t + 4 )^{1 \frac{1}{2}} + 5 ) \mathrm{d} t$

> *Break up the integral.*

$\int ( 2 t + 4 )^{1 \frac{1}{2}} \mathrm{d} t + \int 5 \mathrm{d} t$

> *Integrate *$5$* with respect to *$t$*.*

$\int 5 \mathrm{d} t = 5 t + d$

> *Integrate *$( 2 t + 4 )^{1 \frac{1}{2}}$* with respect to *$t$* using reverse chain rule.*

$\text{integral} ( 2 t + 4 ) ^{1} \text{half} \mathrm{d} t = \frac{ ( 2 t + 4 ) ^{\frac{3}{2}}}{\frac{3}{2}} \times 1 \text{half} + d$

$= 1 \frac{1}{3} ( 2 t + 4 )^{ \frac{3}{2} } + d$

> *Combine both results.*

$s = 1 \frac{1}{3} ( 2 t + 4 )^{ \frac{3}{2} } + 5 t + d$

$[ 1 ]$

> *To find *$d$*, substitute *$s=\frac{1}{3}$* and *$t=6$* into the equation.*

$1 \frac{1}{3} = 1 \frac{1}{3} ( 2 ( 6 ) + 4 )^{ \frac{3}{2} } + 5 ( 6 ) + d$

> *Simplify, then rearrange, to find d.*

$\frac{1}{3}=\frac{64}{3}+30+d$

$d=-51$

$[ 1 ]$

> *Substitute *$d=-51$*into the equation for displacement.*

$\frac{1}{3}(2t+4)^{\frac{3}{2}}+5t-51$ $[ 1 ]$

### Q13
> *If the graph is travelling at a constant velocity, this would be a horizontal line on the graph. A deceleration would have a negative gradient. The final section of the graph should have a steeper negative gradient as the particle has stopped after 5 seconds.*

![june-2020-paper-21-q9a](assets/009-june-2020-paper-21-q9a.png)

**correct shape with three distinct sections ****[1]**

**3 and 1.6 on vertical axis ****[1]**

** ****60, 75 and 80 on horizontal axis**** [1]**
> *The distance is the area under the graph. *
*Finding the area of the first section of the graph, the rectangle*

$60\times3=180$

> *Finding the area of the second section of the graph, the trapezium*

$1 \frac{1}{2} ( 3 + 1.6 ) \times 15 = 34.5$

> *Finding the area of the third section of the graph, the triangle*

$\frac{1}{2}\times1.6\times5=4$

**attempting at least two areas** **[1]**

**all areas calculated correctly ****[1]**

> *Finding the sum of these three areas*

$218.5m$ **[1]**
> *To find the deceleration, calculate the gradient of the line*

$\frac{1.6}{5}$

$0.32\mathrm{ms}^{-2}$ **[1]**

### Q14
> *We need to differentiate *$6 \cos ( 3 t + \frac{\pi }{3} )$* twice.*

> *Differentiate once to find velocity, **v**.*

$\frac{ \mathrm{d} x}{ \mathrm{d} t} = - 18 \sin ( 3 t + \frac{\pi }{3} )$

$[ 1 ]$

> *Differentiate again to find acceleration, **a**.*

$\frac{ \mathrm{d}^{2} x}{ \mathrm{d} t^{2}} = - 54 \cos ( 3 t + \frac{\pi }{3} )$

$[ 1 ]$

> *Substitute *$t=\frac{2π}{3}$* into the equation.*

$a = - 54 \cos ( 3 ( \frac{2 \pi }{3} ) + \frac{\pi }{3} )

a = - 54 \cos ( \frac{7 \pi }{3} )$

> $a=-27$* *$[ 1 ]$
