## The Binomial Expansion

### **Factorial Notation**

* The notation is written as $n!$
* $^nC_r$ is equal to the number of combinations of r objects that can be taken from n objects
* $^nC_r = \frac{n!}{r!(n-r)!}$


---

### **The Binomial Expansion**

* The standard form of the expansion is:

  $$
  (a+b)^n = a^n \ + \ (^nC_1)(a^{n-1})(b) \ + \ (^nC_2)(a^{n-2})(b^2) \ + \ (^nC_3)(a^{n-3})(b^3) \ + \ ... \ + \ b^n
  $$


---

### **Finding The Coefficient of an Individual Term**

* To find the coefficient of an individual term without having to expand the entire expression, use the formula:

  $$
  T_{r+1} = (^nC_r)(a^{n-r})(b^r)
  $$


---

Example Question:

* Find the coefficient of $x^3$ in the binomial expansion of $(3+x)^5$


---

Solution:


1. We know that for the coefficient of $x^3$, the value of r will be 3
2. Therefore, $ T_{3+1} = (^5C_3)(3^{5-3})(x^3)$
3. $T_4 = 90x^3$
4. Therefore, the coefficient is 90.



