# Geometric Distribution

* A geometric distribution is a discrete probability distribution that is modelled using a single parameter, $p$, which represents the probability of success.




### **Finding the probability using the distribution**

* We say a continuous random variable, $X$, follows a geometric distribution $Geo(p)$. This is written as

$$

X \sim Geo(p)‎
$$

The probability of getting a success on the $x^{th}$ trial is found using

$$

P(X = x) = p \times (1 - p)^{x - 1} \quad[\text{Given in MF19}]
$$

Here

* $x$ is a positive integer
  * $x \geq 1$
* $(1 - p)$ denotes the probability of a failure
  * Also represented by $q$




### **Useful results**

<center>Read as "The probability of the first success after the xth trial" </center>
$$
P(X > x)= (1 - p)^x
$$

- This can also be interpreted as the "probability of failure on the first $x$ trials"


$$
\phantom{invis}
$$

<center>Read as "The probability of the first success on one of the first x trials" </center>
$$
P(X \le x)=1-(1-p)^x
$$

- This can also be interpreted as "1 - probability of failure on $x$ trials" 



### **Measures of central tendency**

* Mean of a Geometric Distribution:

$$
E(x)=\mu=\frac{1}{p}
$$

* The mode of all geometric distributions is 1



