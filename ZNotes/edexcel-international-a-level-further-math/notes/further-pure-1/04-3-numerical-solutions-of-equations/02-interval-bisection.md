## Interval Bisection

* if $f(x)$ changes sign within an interval, then the interval could contain a root in $f(x) = 0$

* you take the midpoint of the interval and plug into $f(x)$ to lower the range of the interval by replacing the lower or upper bound depending on the corresponding $f(x)$ sign

* repeat this process to obtain an accurate approximation of the root

### example question

* starting with the interval $[-1,0]$, use interval bisection to find an interval of width 0.1 in $f(x) = x^3 -  5x^2 + 2x + 5$, in where the root lies
  * $f(-1) = -3$ and $f(0) = 5$

  * midpoint $ = \frac{-1+0}{2} = -0.5$

  * $f(-0.5) = 2.63$, therefore new interval: $[-1,-0.5]$

  * midpoint $ = \frac{-1-0.5}{2} = -0.75$

  * $f(-0.75) = 0.27$, therefore new interval: $[-1,-0.75]$

  * midpoint $ = \frac{-1-0.75}{2} = -0.875$

  * $f(-0.875) = -1.25$, therefore new intreval: $[-0.875, -0.75]$

  * midpoint $= \frac{-0.875-0.75}{2} = -0.8125$

  * $f(-0.8125) = -0.46$, therefore new interval: $[-0.8125,-0.75]$

  * range in interval (width) $ = -0.75+0.8125 = 0.0625$

  * therefore since width is $<0.1$, a suitable interval $[-0.81,-0.75]$ has been obtained
* process is long and repetitive, so exam questions usually outline how many times you need to perform interval bisection