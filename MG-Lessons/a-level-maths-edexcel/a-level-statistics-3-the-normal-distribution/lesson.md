# a-level-statistics-3-the-normal-distribution — lesson

_Lane: `a-level-maths-edexcel` · grade — · 6 content steps · 3 check questions (source: MathsGenie lessons)_

## Bell curves and normal notation

![Bell curve with mean mu at the centre, mu minus sigma and mu plus sigma marked, and equal left and right areas showing symmetry](../assets/001-e1c5c87a-5ba8-46ee-9cc1-dd4df49c7066.jpeg)

A normal distribution is a continuous model with a symmetric bell-shaped curve. Probabilities are areas under the curve, so the total area is 1 and the curve is balanced about its centre.

We write $X \sim N(\mu,\sigma^2)$. Here $\mu$ is the mean, $\sigma$ is the standard deviation, and $\sigma^2$ is the variance, so a larger $\sigma$ gives a wider, flatter curve.

For example, if $W \sim N(120,16)$, then $\mu=120$ and $\sigma=\sqrt{16}=4$. By symmetry, $P(W<120)=0.5$.

## Standardising to the standard normal

The standard normal distribution is $Z \sim N(0,1)$. To convert a value of $X$ to a z-score, use $Z=\frac{X-\mu}{\sigma}$, which tells you how many standard deviations the value is from the mean.

Once you standardise, normal probabilities become standard normal probabilities. For a continuous variable, $P(X<a)=P(X\le a)$ because the probability of one exact value is 0.

If $X \sim N(250,5^2)$ and $x=257$, then $z=\frac{257-250}{5}=1.4$. So $P(X>257)=P(Z>1.4)$, and values below the mean give negative z-scores.

## Worked example: finding probabilities

![Normal distribution for cereal box mass with 243, 246, 250, 255 and 257 marked, the right tail beyond 257 shaded, and the interval 246 to 255 shaded](../assets/002-1d03ae9b-a5f6-47b2-a6e7-a392baad758a.jpeg)
Let $X \sim N(250,5^2)$ represent the mass of a cereal box in grams. A good first step is to mark the mean 250 and decide which region of the curve you need.

For the right tail beyond 257 g, standardise the boundary:
$$
z=\frac{257-250}{5}=1.4
$$
So $P(X>257)=P(Z>1.4)\approx 0.0808$.

For the left tail below 243 g, standardise again:
$$
z=\frac{243-250}{5}=-1.4
$$
So $P(X<243)=P(Z<-1.4)\approx 0.0808$, which matches by symmetry.

For the middle region, standardise both ends:
$$
\frac{246-250}{5}=-0.8,\qquad \frac{255-250}{5}=1
$$
Hence $P(246<X<255)=P(-0.8<Z<1)\approx 0.629$.

## Inverse normal and working backwards

Sometimes the probability is given and the boundary value is unknown. If $P(Z < z_p) = p$, then the matching value on the original scale is $x = \mu + \sigma z_p$.

Suppose $T \sim N(62, 10^2)$ and you want the time by which 90% of people finish. This is a lower-tail probability of 0.90, so $z_{0.90} \approx 1.282$ and $t = 62 + 10(1.282) \approx 74.8$. So the cut-off is about 75 minutes.

The same idea also finds a missing spread. If $P(H < 154) = 0.12$ with mean 168, then $z \approx -1.175$ and $154 = 168 - 1.175\sigma$, so $\sigma \approx 11.9$.

## Normal hypothesis tests for a mean

![Sampling distribution of sample mean under H0 with centre 500, observed mean 497.8 marked to the left, and the lower tail shaded for the p-value](../assets/003-4d4f2d42-548a-4542-8ad9-5429de3db781.jpeg)

When the population standard deviation is known, the sample mean follows $\bar X \sim N\left(\mu,\frac{\sigma^2}{n}\right)$. Its standard deviation is the standard error, $\frac{\sigma}{\sqrt{n}}$, which tells you the typical spread of sample means.

A machine should fill bottles with mean 500 ml, and the manager suspects the mean has decreased. With $\sigma=5.5$, $n=25$, and observed $\bar x=497.8$, the hypotheses are $H_0:\mu=500$ and $H_1:\mu<500$, so under $H_0$ we use $\bar X \sim N\left(500,\frac{5.5^2}{25}\right)$.

Now standardise the sample mean:

$$z=\frac{497.8-500}{5.5/\sqrt{25}}=-2.00$$

So the p-value is $P(Z<-2.00)\approx 0.0228$. Since $0.0228<0.05$, reject $H_0$ and conclude there is evidence that the mean fill has decreased.

## Stretch: finding both parameters

When both $\mu$ and $\sigma$ are unknown, one probability statement is not enough. You need two probabilities, and for race times remember that "faster" means a smaller time.

Suppose a sprinter is faster than 9.8 s on 12% of attempts and slower than 10.9 s on 25% of attempts. That means $P(T<9.8)=0.12$ and $P(T<10.9)=0.75$, so with $z_1\approx -1.175$ and $z_2\approx 0.674$ we get:

$$$9.8=\mu-1.175\sigma,\qquad 10.9=\mu+0.674\sigma$$

Subtracting the first equation from the second removes $\mu$, resulting in $1.1=1.849\sigma$, which gives $\sigma\approx 0.595$. Substituting back, we find $\mu\approx 10.5$. This stretch problem requires translating words correctly to solve two linked equations.

## Check yourself

1. If $X \sim N(20,25)$, which statement is correct?

   - Mean 20 and standard deviation 5 ✔

   - Mean 25 and standard deviation 20

   - Mean 20 and standard deviation 25

   - Mean 5 and variance 20

   _Explanation:_ In $N(\mu,\sigma^2)$, the first number is the mean and the second number is the variance. So $\mu=20$ and $\sigma=\sqrt{25}=5$. The most common wrong answer is C, which treats the variance as if it were the standard deviation.

2. If $X \sim N(250,5^2)$, which is the correct setup for $P(X<243)$?

   - $$P(Z<-1.4)$ ✔

   - $$P(Z<1.4)$

   - $$P(Z>-1.4)$

   - $$P(Z>1.4)$

   _Explanation:_ Since 243 is 7 below the mean, the z-score is $\frac{243-250}{5}=-1.4$. The probability is also a lower-tail probability, so the correct setup is $P(Z<-1.4)$. The most common wrong answer is B, which forgets that values below the mean must have negative z-scores.

3. In the bottle-filling test, the p-value is 0.0228 at the 5% significance level. What is the correct conclusion?

   - Reject $H_0$; there is evidence the mean has decreased. ✔

   - Reject $H_0$; there is evidence the mean is exactly 497.8.

   - Fail to reject $H_0$; 0.0228 is too small to matter.

   - Fail to reject $H_0$; because 0.0228 is greater than 0.05.

   _Explanation:_ You reject $H_0$ when the p-value is less than the significance level, and here $0.0228 < 0.05$. That gives evidence for the alternative hypothesis $H_1: \mu < 500$. The most common wrong answer is D, which reverses the comparison and incorrectly says $0.0228$ is greater than $0.05$.
