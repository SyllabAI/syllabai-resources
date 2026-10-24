# Mark Schemes — Binomial Theorem
**Sequences & Series** · Cambridge (CIE) IGCSE further-maths (0606)


## Exam Questions (12 questions)


### Q1
> *Substitute *$a=2$*, *$b=\frac{k}{2}$* and *$n=8$* into the first three terms of the binomial expansion*

$( a + b )^{n = a^{n} + ( \begin{gathered} n \\ 1 \end{gathered} ) a^{n} - 1} b + ( \begin{gathered} n \\ 2 \end{gathered} ) a^{n - 2} b^{2} +... + ( \begin{gathered} n \\ r \end{gathered} ) a^{n - r} b^{r} +... + b^{n}$

$( 2 + \frac{k}{2} )^{8} = 2^{8} + ( \begin{gathered} 8 \\ 1 \end{gathered} ) 2^{7} ( \frac{k}{2} ) + ( \begin{gathered} 8 \\ 2 \end{gathered} ) 2^{6} ( \frac{k}{2} )^{2} +...$

> *Simplify each term*

$( 2 + \frac{k}{2} )^{8} = 256 + 8 \times 128 ( \frac{k}{2} ) + 28 \times 64 ( \frac{k^{2}}{4} ) +...$

$256+512k+448k^{2}$

**[B1 B1]**

> **[mark-scheme]**
> **B1: **For at least two terms correct.
> 
> **B1:** For the fully correct final answer.
> *Substitute *$k=p-p^{2}$* into the answer in part (a)*

$256 + 512 ( p - p^{2} ) + 448 ( p - p^{2} )^{2}$

> *Expand*

$256 + 512 p - 512 p^{2} + 448 ( p^{2} - 2 p^{3} + p^{4} )$

> *Ignore any terms in *$p^{3}$* or higher*

$256+512p-512p^{2}+448p^{2}$

> *Collect like terms*

$256+512p-64p^{2}$

**[B1 B1]**

> **[mark-scheme]**
> **B1: **For at least two terms correct.
> 
> **B1:** For the fully correct final answer.
> *Substitute *$a=ax^{2}$*, *$b = ( - \frac{1}{x^{2}} )$* and *$n=6$* into the formula for a general term *$( \begin{gathered} n \\ r \end{gathered} ) a^{n - r} b^{r}$

$( \begin{gathered} 6 \\ r \end{gathered} ) ( a x^{2} )^{6 - r} ( - \frac{1}{x^{2}} )^{r}$

**[M1]**

> *Rewrite this expression using index laws, noting that *$( - \frac{1}{x^{2}} ) = ( - 1 ) x^{- 2}$

$( \begin{gathered} 6 \\ r \end{gathered} ) a^{6 - r} x^{2 ( 6 - r )} ( - 1 )^{r x^{-2} r}$

> *Collect the terms in *$x$* using index laws*

$( \begin{gathered} 6 \\ r \end{gathered} ) a^{6 - r} ( - 1 )^{r x^{2} ( 6 - r ) - 2 r}$

> *The term 'independent of *$x$*' is the term without an *$x$*, i.e. *$x^{0}=1$

> *Set the power of *$x$* equal to zero and solve*

$\begin{gathered} 2 ( 6 - r ) - 2 r & = 0 \\ 12 - 2 r - 2 r & = 0 \\ 12 = 4 r \\ r = 3 \end{gathered}$

**[A1]**

> *Substitute *$r=3$* back into the general term*

$\begin{gathered} = ( \begin{gathered} 6 \\ 3 \end{gathered} ) a^{6 - 3} ( - 1 )^{3} x^{2 ( 6 - 3 ) - 2 \times 3} \\ = ( \begin{gathered} 6 \\ 3 \end{gathered} ) a^{3} ( - 1 )^{3} x^{0} \\ = - ( \begin{gathered} 6 \\ 3 \end{gathered} ) a^{3} \end{gathered}$

> *Work out *$( \begin{gathered} 6 \\ 3 \end{gathered} )$*, e.g. on your calculator*

$( \begin{gathered} 6 \\ 3 \end{gathered} ) = 20$

> *Substitute this back into the term to get the final answer*

$-20a^{3}$

**[A1]**

### Q2
> *Expand both the brackets up to their *$x^{2}$* terms using the Binomial Expansion. This will lead us to form *$27+bx+cx^{2}$*.*

$( a + x )^{3} = ( 1 ) ( a )^{3} + ( C pre^{3}_{1} ) ( a )^{2} ( x ) + ( C pre^{3}_{2} ) ( a ) ( x )^{2} + ...$

**[1]**

`( 1 - x / 3 ) ^ 5 = ( 1 ) ( 1 ) ^ 5 + ( C _ 1 ^ 5 ) ( 1 ) ^ 4 ( - x / 3 ) + ( C _ 2 ^ 5 ) ( 1 ) ^3 ( - x / 3 ) ^2 + ...`

$= 1 + ( 5 ) ( - \frac{x}{3} ) + ( 10 ) ( \frac{x^{2}}{9} ) + ...$

$=1-\frac{5}{3}x+\frac{10}{9}x^{2}+...$

**[2]**

> *Multiply together.*

$( a^{3} + 3 a^{2} x + 3 a x^{2} +... ) ( 1 - \frac{5}{3} x + \frac{10}{9} x^{2} +... )$

> *Find the constant term and equate to 27.*

$a^{3}=27$

$a=3$  **[1]**

> *Substitute *$a=3$* into the expression.*

$= ( ( 3 )^{3} + ( 3 ) ( 3 )^{2} x + ( 3 ) ( 3 ) x^{2} +... ) ( 1 - \frac{5}{3} x + \frac{10}{9} x^{2} +... )$

$= ( 27 + 27 x + 9 x^{2} +... ) ( 1 - \frac{5}{3} x + \frac{10}{9} x^{2} +... )$

> *Find the coefficient of *$x$* and equate to *$b$*.*

$b = 27 - \frac{5}{3} ( 27 )$

**[1]**

$b=-18$ **[1]**

> *Find the coefficient of *$x^{2}$* and equate to *$c$*.*

$c = 9 + ( 27 ) ( \frac{10}{9} ) + ( 27 ) ( - \frac{5}{3} )$

**[1]**

$c=-6$ **[1]**

### Q3
> *Using the formula for the binomial expansion, finding the first three terms gives*

$( a^{5 + ( \begin{gathered} 5 \\ 1 \end{gathered} ) a^{4} b x + ( \begin{gathered} 5 \\ 2 \end{gathered} ) a^{3} } ( b x )^{2} ) ( 1 + x )$

**[1]**

> *Simplifying gives*

$( a^{5 + 5 a^{4} b x + 10 a^{3} } b^{2} x^{2} ) ( 1 + x )$

**[1]**

> *Expanding the brackets*

$a^{5}+5a^{4}bx+10a^{3}b^{2}x^{2}+a^{5}x+5a^{4}bx^{2}+10a^{3}b^{2}x^{3}$

**multiplying out brackets**** [1]**

**all terms correct**** [1]**

> *Comparing to *$32-208x+cx^{2}$* by comparing the constants we have*

$a^{5}=32$

$a=2$**  [1]**

> *Equating the coefficients of *$x$* we have*

$5a^{4}b+a^{5}=-208$

> *Substituting in *$a=2$

$80b+32=-208$

$80b=-240$

$b=-3$**  [1]**

> *Equating the coefficients of *$x^{2}$* we have*

$10a^{3}b^{2}+5a^{4}b=c$

> *Substituting in *$a=2$* and *$b=-3$* we have*

$720-240=c$

$c=480$** ****[1]**

### Q4
> *Expand *$( 1 - \frac{x}{2} )^{n}$* using the binomial expansion up to the *$x^{2}$* term. *

$( 1 )^{n + ( \begin{gathered} n \\ 1 \end{gathered} ) ( 1 )^{n} - 1} ( - \frac{x}{2} ) + ( \begin{gathered} n \\ 2 \end{gathered} ) ( 1 )^{n - 2} ( - \frac{x}{2} )^{2} + ...

1 + ( \frac{n factorial}{( n - 1 ) \text{factorial} 1 factorial} ) ( - \frac{x}{2} ) + ( \frac{n factorial}{( n - 2 ) \text{factorial} 2 factorial} ) ( - \frac{x}{2} )^{2} +...

1 + ( n ) ( - \frac{x}{2} ) + ( \frac{n ( n - 1 )}{2} ) ( \frac{x^{2}}{4} ) +...$

> * *

> *Multiplied by *$( 1 + x )$*, this is:*

$( 1 + x ) ( 1 + ( n ) ( - \frac{x}{2} ) + ( \frac{n ( n - 1 )}{2} ) ( \frac{x^{2}}{4} ) +... )$

**for the correct **$x$** term **$[ 1 ]$

**for the correct **$x^{2}$** term **$[ 1 ]$

> *When expanded, the *$x^{2}$* terms will be*

$1 \times ( \frac{n ( n - 1 )}{2} ) ( \frac{x^{2}}{4} )$* **and *$x \times ( n ( - \frac{x}{2} ) )$

> *Simplify.*

$( \frac{n ( n - 1 )}{8} ) x^{2}$* **and *$( - \frac{n}{2} ) x^{2}$

> *Sum the coefficients of *$x^{2}$* and equate to *$\frac{25}{4}$

$( \frac{n ( n - 1 )}{8} ) + ( - \frac{n}{2} ) = \frac{25}{4}$

$[ 1 ]$

> *Expand the brackets.*

$\frac{n^{2}-n}{8}-\frac{n}{2}=\frac{25}{4}$

> *Multiply through by 8.*

$n^{2}-n-4n=50$

> *Rearrange and solve.*

$\begin{gathered} n^{2} - 5 n - 50 & = 0 \\ ( n - 10 ) ( n + 5 ) & = 0 \\ \end{gathered}$

$n=10$* **and *$n=-5$

*  *

> *We are told in the question that the value of *$n$* is positive. Therefore:*

> $n=10$* *$[ 1 ]$

### Q5
> *Find an expression for the coefficient of the *$x^{4}$* term of the expansion.*

$\frac{n factorial}{4 \text{factorial} ( n - 4 ) factorial} \times ( 1 )^{n - 4} \times ( 1 \frac{1}{2} )^{4 }$

> *This can be written as*

$\frac{n ( n - 1 ) ( n - 2 ) ( n - 3 ) \times ( n - 4 ) factorial}{4 \text{factorial} \times ( n - 4 ) factorial} \times ( 1 \frac{1}{2} )^{4}$

> *Simplify.*

> *  *

$\frac{n ( n - 1 ) ( n - 2 ) ( n - 3 )}{1 \times 2 \times 3 \times 4} \times ( 1 \frac{1}{2} )^{4}$

$[ 1 ]$

> *Similarly, find an expression for the *$x^{6}$* coefficient of the term of the expansion.*

> *   *

$\frac{n ( n - 1 ) ( n - 2 ) ( n - 3 ) ( n - 4 ) ( n - 5 )}{1 \times 2 \times 3 \times 4 \times 5 \times 6} \times ( 1 \frac{1}{2} )^{6}$

$[ 1 ]$

> *We are told that the coefficient of *$x^{4}$* is half the coefficient of *$x^{6}$*, therefore:*

> *  *

$\frac{n ( n - 1 ) ( n - 2 ) ( n - 3 )}{24 \times 16} = 1 \frac{1}{2} \times ( \frac{n ( n - 1 ) ( n - 2 ) ( n - 3 ) ( n - 4 ) ( n - 5 )}{720 \times 64} )$

$[ 1 ]$

> *Simplify.*

$\begin{gathered} \frac{2 \times 720 \times 64}{24 \times 16} & = \frac{n ( n - 1 ) ( n - 2 ) ( n - 3 ) ( n - 4 ) ( n - 5 )}{n ( n - 1 ) ( n - 2 ) ( n - 3 )} \\ \frac{720}{3} & = ( n - 4 ) ( n - 5 ) \\ 240 = ( n - 4 ) ( n - 5 ) \end{gathered}$

$[ 1 ]$

> *Expand the brackets, rearrange and solve.*

$\begin{gathered} n^{2} - 9 n + 20 & = 240 \\ n^{2} - 9 n - 220 & = 0 \\ ( n - 20 ) ( n + 11 ) & = 0 \end{gathered}$

$[ 1 ]$

$n=20$* **or *$n=-11$

> *The question asks for the positive value.*

$n = 20 [ 1 ]$

### Q6
> *We can deduce that the term containing *$x^{2}$* is*

`C _ 2 ( 2 k ) ^3 ( - x / k ) ^2 ^ 5`

**[1]**

> *Simplify this*

> *                             *$=10\times8k^{3}\times\frac{x^{2}}{k^{2}}\,=80kx^{2}$

> *The coefficient of *$x^{2}$* is equal to 160 therefore*

$80k=160$

**[1]**

> *Divide both sides by 80 to get the final answer*

$k=2$** [1]**

### Q7
> *Expand *$( x + \frac{2}{x} )^{5}$

$( 1 ) ( x )^{5} + ( C pre^{5}_{1} ) ( x )^{4} ( \frac{2}{x} )^{1} + ( C pre^{5}_{2} ) ( x )^{3} ( \frac{2}{x} )^{2} +...$

> *Simplify.*

$x^{5}+10x^{3}+40x+...$

**for two correct terms **$[ 1 ]$

**for **$10x^{3}$** **$[ 1 ]$

**for **$40x$** **$[ 1 ]$

> *     *

> *When multiplied by *$( x - \frac{3}{x} )$*, the only terms in *$x^{2}$* will be when *$40x$* is multiplied by *$x$* and when *$10x^{3}$* is multiplied by *$-\frac{3}{x}$

> *Therefore, the coefficient of *$x^{2}$* is*

$( 1 \times 40 ) - ( 3 \times 10 )$

$[ 1 ]$

$10 [ 1 ]$

### Q8
i) *Use binomial expansion to obtain the first three terms*

> $( 1 + 3 x )^{6} = 1^{6} + C pre^{6}_{1} \times 1^{5} \times ( 3 x )^{1} + C pre^{6}_{2} \times 1^{4} \times ( 3 x )^{2} +...$*       *

**an unsimplified correct substitution or any two correct final terms from the answer below ****[1]**

> *   Simplify*

$=1+6\times3x+15\times9x^{2}$

** **$1+18x+135x^{2}$ **[1]**

ii) *The expansion of *$( a + x )^{2}$* is *$a^{2}+2ax+x^{2}$*. Multiply the first three terms of *$( 1 + 3 x )^{6}$* found in (i) by *$a^{2}+2ax+x^{2}$*, up to terms in *$x^{2}$* (you don't need to multiply terms that will result with *$x^{3}$* or higher)*

$( 1 + 18 x + 135 x^{2} +... ) ( a^{2} + 2 a x + x^{2} )
 = ( a^{2} ) ( 1 ) + ( a^{2} ) ( 18 x ) + ( a^{2} ) ( 135 x^{2} ) +... + ( 2 a x ) ( 1 ) + ( 2 a x ) ( 18 x ) +... + ( x^{2} ) ( 1 ) +...$

> *(The line above is really just shown for demonstration purposes. In reality we'd probably go straight to the line below)*

$( 1 + 18 x + 135 x^{2} +... ) ( a^{2} + 2 a x + x^{2} ) = a^{2} + 18 a^{2} x + 135 a^{2} x^{2} +... + 2 a x + 36 a x^{2} +... + x^{2} +...$

> *We can equate this to *$4+68x+bx^{2}$

$a^{2}+18a^{2}x+135a^{2}x^{2}+...+2ax+36ax^{2}+...+x^{2}+...=4+68x+bx^{2}$

> *The only constant term on the left hand side is "*$a^{2}$*" therefore equating the constants gives*

$a^{2}=4\,a=\pm2$

**[1]**

> *Only one of these can be correct. Examining the terms in *$x$*:*

$\begin{gathered} a = - 2 , 18 a^{2} x + 2 a x = 18 ( - 2 )^{2} x + 2 ( - 2 ) x = 68 x \\ a = 2 , 18 a^{2} x + 2 a x = 18 ( 2 )^{2} x + 2 ( 2 ) x = 76 x \end{gathered}$

> *But we know that the term in *$x$* is *$68x$* therefore *$a\neq2$* and *

$a=-2$ **[1]**

> *Now substitute *$a=-2$* into the terms in *$x^{2}$

$\begin{array}{rcl} 135 ( - 2 )^{2} x^{2} + 36 ( - 2 ) x^{2} + x^{2} & = b x^{2} \\ 540 x^{2} - 72 x^{2} + x & = b x^{2} \\ 469 x^{2} & = b x^{2} \end{array}$

> *Therefore*

$b=469$ **[1]**

### Q9
> *The only term in the expansion that will include no *$x$* is the *$x^{3}$* one, since this is where the powers of *$x$*cancel each other out.*

> *Find the *$x^{3}$* term.*

$C pre^{6}_{3} \times ( 3 x )^{3} \times ( - \frac{1}{x} )^{3}$

$20 \times ( 3 x )^{3} \times ( - \frac{1}{x} )^{3}$

$[ 1 ]$

> *Simplify.*

$20 \times 27 x^{3} \times ( - \frac{1}{x^{3}} )$

$\frac{-540x^{3}}{x^{3}}$

$- 540 [ 1 ]$

### Q10
> *Using the formula for the binomial theorem with *$a=2,b=-x,n=5$

$2^{5 + C pre^{5}_{1} 2^{4} ( - x ) + C pre^{5}_{2} 2^{3} ( - x )^{2} } + C pre^{5}_{3} 2^{2} ( - x )^{3} + C pre^{5}_{4} 2^{1} ( - x )^{4} + C pre^{5}_{5} ( - x )^{5}$

$32-80x+80x^{2}-40x^{3}+10x^{4}-x^{5}$ **[3]**

**2 marks for any four or five terms correct, or 1 mark for any three terms correct**
> *Multiplying both sides of the equation by the denominator*

$e^{( 2 - x )^{5} } \times e^{80 x} = e^{- x^{5} } ( e^{10 x^{4} + 32} )$

> *Expanding the brackets and applying the laws of indices*

$e^{( 2 - x )^{5} + 80 x} = e^{- x^{5} } + 10 x^{4 + 32}$

> *Taking logs of both sides*

$( 2 - x )^{5} + 80 x = - x^{5} + 10 x^{4} + 32$

**[1]**

$( 2 - x )^{5} = - x^{5} + 10 x^{4} - 80 x + 32$

> *Comparing this to the expansion in part (a) gives*

$\begin{gathered} 32 - 80 x + 80 x^{2} - 40 x^{3 } + 10 x^{4 - x^{5} & = - x^{5} + 10 x^{4} - 80 x + 32 \\ \cancel{32 \cancel{-} 80 x} + 80 x^{2} - 40 x^{3} } \cancel{+ 10 x^{4} } \cancel{- x^{5} } & = \cancel{- x^{5} } \cancel{+ 10 x^{4} } \cancel{- 80} x \cancel{+ 32} \\ 80 x^{2} - 40 x^{3} & = 0 \end{gathered}$

**[1]**

> *Factorising gives*

$40 x^{2} ( 2 - x ) = 0$

**[1]**

> *Finding the solutions to the equation*

$x=0,x=2$ **[1]**

### Q11
> *Use the Binomial Theorem to expand the polynomial*

$( 4 - \frac{x}{16} )^{6 = 4^{6} + ( \begin{gathered} 6 \\ 1 \end{gathered} ) 4^{5} } ( - \frac{x}{16} ) + ( \begin{gathered} 6 \\ 2 \end{gathered} ) 4^{4 } ( - \frac{x}{16} )^{2} +...$

$( 4 - \frac{x}{16} )^{6} = 4096 - 384 x + 15 x^{2} +...$

$4096-384x+15x^{2}$ **[3]**

**1 mark for each correct term**

** **
> *From part (a) we know that *$( 4 - \frac{x}{16} )^{6} = 4096 - 384 x + 15 x^{2} +...$* so*

$( 4 - \frac{x}{16} )^{6} ( x - \frac{1}{x} )^{2} = ( 4096 - 384 x + 15 x^{2} +... ) ( x - \frac{1}{x} )^{2}$

> *Expand the second bracket *

$( x - \frac{1}{x} )^{2} = x^{2} - 2 + \frac{1}{x^{2}}$

> *Therefore*

$( 4 - \frac{x}{16} )^{6} ( x - \frac{1}{x} )^{2} = ( 4096 - 384 x + 15 x^{2} +... ) ( x^{2} - 2 + \frac{1}{x^{2}} )$

**[1]**

> *Look at the term without (independent of) an *$x$

> *The term independent of *$x$* will come from 2 different places*

$4096\times-2=-8192$

*and*

$15x^{2}\times\frac{1}{x^{2}}=15$

**[1]**

> *Add these together*

$-8192+15=-8177$

$-8177$ **[1]**

### Q12
> *Use the binomial theorem *$( a + b )^{n = a^{n} + ( \begin{gathered} n \\ 1 \end{gathered} ) a^{n} - 1} b + ( \begin{gathered} n \\ 2 \end{gathered} ) a^{n - 2} b^{2} +... + b^{n}$

$( 3 - a x )^{5} = 3^{5} + ( \begin{gathered} 5 \\ 1 \end{gathered} ) 3^{4} ( - a x ) + ( \begin{gathered} 5 \\ 2 \end{gathered} ) 3^{3} ( - a x )^{2} +...$

$( 3 - a x )^{5} = 243 - 405 a x + 270 a^{2} x^{2} +...$

**1 mark for second and third term**** [2]**

> *Set the first 3 terms equal to the expression given in the question:*

$b-81x+cx^{2}=243-405ax+270a^{2}x^{2}$

> *Equate coefficients:*

$b=243$

**[1]**

$-81=-405a\mathrm{so}a=\frac{1}{5}$

**[1]**

$c = 270 a^{2} = 270 \times ( 1 \frac{1}{5} )^{2} = \frac{54}{5}$

$a=\frac{1}{5},b=243,c=\frac{54}{5}$**[1]**
