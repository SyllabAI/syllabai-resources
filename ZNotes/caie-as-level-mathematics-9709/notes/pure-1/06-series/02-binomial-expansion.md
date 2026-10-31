## Binomial expansion

* The binomial expansion helps us expand the sum of two terms raised to an exponent.
  * It makes use of pascal’s triangle, as shown below, to obtain the binomial coefficient.

 ![](../../../assets/737e69ff66ae-66b8ffbcfbf8af206516dcf3a689c07a1825eac9d32c7252.41)The expansion is given in MF19 for $n > 0$, and can be generalised to

$$

(a + b)^n = {n \choose 0} a^n + {n \choose 1}a^{n ~ - ~ 1}b+ {n\choose2}a^{n ~ - ~2}b^2 + \cdots + {n \choose n - 1} ab^{n ~ - ~ 1} + {n \choose n} b^n
$$

* Observations:
  * The exponents for $a$ and $b$ sum up to the value of $n$
  * The ${n \choose r}$ notation can be thought of as **choosing** $r$ number of terms to be the second term, $b$.

**<center>We can find the rth term of a binomial expansion using</center>**

$$

T_{r ~ + ~ 1} = {}^nC_r \times a^{n ~ - ~ r} \times b^r
$$




### **Binomial expansion with 3 terms**

* We can also use binomial expansion to expand a trinomial, or the sum of three terms raised to an exponent.

Consider the expansion of  $(a + b)^n$

$$

(a + b)^n = {n \choose 0} a^n + {n \choose 1}a^{n ~ - ~ 1}b + \cdots + {n \choose n - 1} ab^{n ~ - ~ 1} + {n \choose n} b^n
$$

<center>We can write the trinomial as</center>

$$

(x + y + z)^n \implies (a + [y + z])^n
$$

Now we can substitute $b = y + z$ in the expansion of $(a + b)^n$

$$

(a + b)^n = {n \choose 0} x^n + {n \choose 1}x^{n ~ - ~ 1}(y + z) + \cdots + {n \choose n - 1} x(y + z)^{n ~ - ~ 1} + {n \choose n} (y + z)^n
$$


---

**<center> Example </center>**

Find the expansion of $(3x+2)^4$.

**<center>Answer </center>**

$$

(3x + 2)^4 = (3x)^4 + {4\choose1}(3x)^{4-1}(2)+ {4\choose2}(3x)^{4-2}(2)^2 + {4\choose3}(3x)^{4-3}(2)^3+ {4\choose4}(2)^4
$$

$$

(3x + 2)^4 = 81x^4 + (4)(3x)^3(2)+(6)(3x)^2(4) + (4)(3x)(8)+16
$$

$$

(3x + 2)^4 = 81x^4 + 216x^3 + 216x^2 + 96x + 16
$$



