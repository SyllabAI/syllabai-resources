## Chain rule

* The chain rule helps us differentiate a **composite function**.

Consider $f(~g(x)~)$. If we let $u = g(x)$ and $y = f(u)$, and then differentiate $y$, we get

$$

\frac{dy}{dx} = \frac{du}{dx} \times \frac{dy}{du}
$$

So we can define the derivative of $y = f(~g(x)~)$

$$

\frac{d}{dx} ~f(~ g(x) ~) = f\prime(~g(x)~) ~\times~ g\prime(x)
$$

It may also be thought of like this

 ![](../../../assets/dc4ffede8709-66d073b4bbd3ad56b58b99f8499150aba8706fe088b496f8.00)




### **Applications of chain rule**

* The chain rule can be applied to differentiate functions of the type $[f(x)]^n$

Using the chain rule and power rule, we can differentiate $y = [f(x)]^n$ to get

$$

\frac{d}{dx} ~ [f(x)]^n = n  ~ \times ~ [f(x)]^{n ~ - ~ 1} ~ \times ~ f\prime(x)
$$

Another application is seen while differentiating $y = (ax + b)^n$

$$

\frac{d}{dx} ~ (ax + b)^n = n ~ \times ~ (ax + b)^{n ~ - ~ 1} ~ \times ~ \frac{d}{dx} ~ ax + b
$$

$$

\implies \frac{d}{dx} ~ (ax + b)^n = n ~ \times ~ (ax + b)^{n ~ - ~ 1} ~ \times ~ a
$$

- This is valid for all real numbers $n ~ \cancel{=} ~ 0$

---

**<center>Example</center>**

Differentiate $y = (2x + 5)^5$.

**<center>Answer</center>**

Using the chain rule

$$

\frac{d}{dx} ~(2x + 5)^5 = 5 ~\times~ (2x + 5)^{5 ~-~ 1} ~\times~ \frac{d}{dx}~ 2x + 5
$$

$$

\implies \frac{d}{dx}~ (2x + 5)^5 = 5 ~\times~ (2x + 5)^4 ~\times~ 2
$$

$$

\implies \frac{d}{dx} ~(2x + 5)^5 = 10 ~\times~ (2x + 5)^4
$$



