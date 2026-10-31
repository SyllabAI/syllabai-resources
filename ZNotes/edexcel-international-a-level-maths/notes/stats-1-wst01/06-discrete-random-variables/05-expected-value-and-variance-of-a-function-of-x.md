## Expected Value and Variance of a Function of X

* If a discrete random variable (X) is input into a function called g, then g(X) is also a discrete random variable

* If X is a random variable and a and b are constants, then

  * $\boxed {\text{E(aX + b) = aE(X) +b}}$

  * How this formula works?

    * The constant b (Shifting)**:** If a teacher adds 5 bonus points (b) to every single student's test score, the class average E(X) shifts up by exactly 5 points.

    * The constant a (Scaling)**:** If the teacher doubles a everyone's score instead, the final class average will double as well.

* If X and Y are random variables, then $E(X + Y) = E(X) + E(Y)$

* Similarly, if X is a random variable and a and b are constants

* $\boxed{\text{Var(aX+ b) = a²Var(X)}}$

* Note that Var(aX \+ b) always uses a², so the variance is unaffected by the sign of a, and adding a constant b never changes the variance (shifting all values doesn't change how spread out they are)

* More generally, for any function g(X):

  * $E(g(X)) = Σg(x)P(X = x)$

* normal variance is variance of the original random variable, while *variance of a function* is variance after transforming the random variable.

**Question 6**: using $E(X) = 2, Var(X) = 1,$ find $E(3X + 2) and Var(3X + 2)$

**Answer:**

•     $E(3X + 2) = 3E(X) + 2 = 3(2) + 2 = 8$

•     $Var(3X + 2) = 3²Var(X) = 9(1) = 9$