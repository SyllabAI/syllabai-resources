## Integrating $\cos^mx \ \sin^nx$

**If** $\mathbf{m}$ **or** $\mathbf{n}$ **are odd and even, then:**

* Factor out one power from **odd trig function**
* Use Pythagorean identities to transform remaining **even trig
  function** into the **odd trig function**
* Let u equal to **odd trig function** and integrate

**If** $\mathbf{m}$ **and** $\mathbf{n}$ **are both even, then:**

* Replace all even powers using the double angle identities and
  integrate

**If** $\mathbf{m}$ **and** $\mathbf{n}$ **are both odd, then:**

* Choose one of the trig. functions & factor out one power
* Use Pythagorean identity to transform remaining even power of chosen
  trig function into other trig. function

**If either** $\mathbf{m}$ **or** $\mathbf{n}$ **or both = 1,
then:**

* Let $u$ equal to the trig function whose power doesn’t equal 1
  then integrate
* If both are 1, then let $u$ equal either

 

**<span class="underline">{W09-P31} Question 5:</span>**

i)  Prove the identity

$$
\cos{4\theta} - 4\cos{2\theta} + 3 \equiv 8\sin^{4}\theta
$$

ii)  Using this result find, in simplified form, the exact value of

$$
\int_{\frac{1}{6}\pi}^{\frac{1}{3}\pi}{\sin^{4}{\theta\text{dθ}}}
$$

**<center>Solution:</center>**

**<span class="underline">Part (i)</span>**

*Use double angle identities*

$$
\cos{4\theta} - 4\cos{2\theta} + 3 
$$

$$
\equiv 1 - 2\sin^{2}{2\theta} - 4\left( 1 - 2\sin^{2}\theta \right) + 3
$$

*Open everything and clean*

$$
\equiv 1 - 2\sin^{2}{2\theta} - 4 + 8\sin^{2}\theta + 3
$$

$$
\equiv 1 - 2{(\sin{2\theta)}}^{2} - 4 + 8\sin^{2}\theta + 3
$$

$$
\equiv 1 - 2{(2\sin{\theta\cos{\theta)}}}^{2} - 4 + 8\sin^{2}\theta + 3
$$

$$
\equiv 1 - 2\left( 4\sin^{2}\theta\cos^{2}\theta \right) - 4 + 8\sin^{2}\theta + 3
$$

$$
\equiv 1 - 2(4\sin^{2}\theta(1 - \sin^{2}{\theta)}) - 4 + 8\sin^{2}\theta + 3
$$

$$
\equiv 1 - 8\sin^{2}\theta + 8\sin^{4}\theta - 4 + 8\sin^{2}\theta + 3
$$

$$
\equiv 8\sin^{4}\theta
$$

**<span class="underline">Part (ii)</span>**

*Use identity from (part i):*

$$
\frac{1}{8}\int_{\frac{1}{6}\pi}^{\frac{1}{3}\pi}{\cos{4\theta} - 4\cos{2\theta} + 3}
$$

$$
\equiv \frac{1}{8}\left\lbrack \frac{1}{4}\sin{4\theta} - 2\sin\theta + 3\theta \right\rbrack_{\frac{1}{6}\pi}^{\frac{1}{3}\pi}
$$

*Substitute limits*

$$
\equiv \frac{1}{32}\left( 2\pi - \sqrt{3} \right)
$$

 

**<span class="underline">{W12-P32} Question 5:‎</span>**

i.  By differentiating $\frac{1}{\cos x}$, show that if
$y\  = \ \sec x$ then
$\frac{\text{dy}}{\text{dx}} = \sec x\tan x$

ii.  Show that $\frac{1}{\sec{x - \tan x}} \equiv \sec x + \tan x$

iii.  Deduce that:

$$\frac{1}{{(sec}x - {\tan{x)}}^{2}} \equiv 2\sec^{2}x - 1 + 2\sec x\tan x$$

iv.  Hence show that:

$$\int_{0}^{\frac{1}{4}\pi}\frac{1}{{(sec}x - {\tan{x)}}^{2}}dx = \frac{1}{4}\left( 8\sqrt{2} - \pi \right)$$

**<center>Solution:</center>**

**<span class="underline">Part (i)</span>**

*Change to index form:*

$$\frac{1}{\cos x} = \cos^{- 1}x$$

*Differentiate by chain rule:*

$$\frac{\text{dy}}{\text{dx}} = - 1\left( \cos x \right)^{- 2} \times \left( - \sin x \right)$$

$$- 1\left( \cos x \right)^{- 2} \times \left( - \sin x \right) \equiv \frac{\sin x}{\cos^{2}x} \equiv \frac{\sin x}{\cos x} \times \frac{1}{\cos x}$$

$$\frac{\sin x}{\cos x} \times \frac{1}{\cos x} \equiv \sec x\tan x$$

**<span class="underline">Part (ii)</span>**

*Multiply numerator and denominator by* $\sec x + \tan x$

$$\frac{\sec{x + \tan x}}{{(sec}{x - \tan{x)}}\left( \sec{x + \tan x} \right)} \equiv \frac{\sec{x + \tan x}}{\sec^{2}x - \tan^{2}x}$$

$$\frac{\sec{x + \tan x}}{\sec^{2}x - \tan^{2}x} \equiv \frac{\sec{x + \tan x}}{1} \equiv \sec{x + \tan x}$$

**<span class="underline">Part (iii)</span>**

*Substitute identity from (part ii)*

$$\frac{1}{{(sec}x - {\tan{x)}}^{2}} \equiv {(sec}x + {\tan{x)}}^{2}$$

*Open out brackets*

$${(sec}x + {\tan{x)}}^{2}$$

$$\equiv \sec^{2}x + 2\sec x\tan x + \tan^{2}x$$

$$\equiv \sec^{2}x + 2\sec x\tan x + \sec^{2}x - 1$$

$$\equiv {2sec}^{2}x + 2\sec x\tan x - 1$$

$$\equiv 2\sec^{2}x - 1 + 2\sec x\tan x$$

**<span class="underline">Part (iv)</span>**

$$\int_{}^{}{\frac{1}{{(sec}x - {\tan{x)}}^{2}}\text{dx}}$$

$$\equiv \int_{}^{}{2\sec^{2}x - 1 + 2\sec x\tan x}\text{dx}$$

$$\equiv 2\int_{}^{}{\sec^{2}x} - \int_{}^{}1 + 2\int_{}^{}{\sec^{2}{x\tan^{2}x}}$$

*Using differential from part i:*

$$\equiv 2\tan x - x + 2\sec x$$

*Substitute boundaries:*

$$= \frac{1}{4}\left( 8\sqrt{2} - \pi \right)$$