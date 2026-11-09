# as-mechanics-modelling-assumptions — lesson

_Lane: `a-level-maths-edexcel` · grade — · 5 content steps · 3 check questions (source: MathsGenie lessons)_

## Why mechanics uses models

![Real ball simplified to a particle with downward acceleration g and air resistance ignored](../assets/001-37ecb77d-be91-4ca0-a87e-91909cfee086.jpeg)
A model is a simplified version of a real situation. Modelling assumptions ignore smaller effects so the mathematics becomes manageable.

If an object is modelled as a particle, its mass is treated as concentrated at one point. Its size, shape and rotation are ignored, but it can still have mass and weight.

These words are not decoration. They tell you which forces and effects are included, so they decide which equations you are allowed to use.

## Constant acceleration and SUVAT

Constant acceleration means the acceleration stays the same throughout the motion. In straight-line motion, that is the key condition for using the SUVAT equations.

The symbols are $s$ for displacement, $u$ for initial velocity, $v$ for final velocity, $a$ for acceleration and $t$ for time. The main equations are
$$
v = u + at,\qquad s = ut + \frac{1}{2}at^2,\qquad v^2 = u^2 + 2as,\qquad s = \frac{1}{2}(u+v)t
$$
Choose the one that matches the information you know.

If an object moves freely under gravity and air resistance is negligible, the only force is weight, so its acceleration is the constant value $g$ downward. Near the Earth's surface, $g = 9.8 \, \text{m s}^{-2}$.

Choose a positive direction before you substitute. Any choice is fine if you stay consistent: if upwards is positive, then $a = -9.8 \, \text{m s}^{-2}$; if downwards is positive, then $a = 9.8 \, \text{m s}^{-2}$.

## Worked example: free fall under gravity

Example: A small stone is dropped from rest from a height of $20 \, \text{m}$ and modelled as a particle falling freely under gravity with air resistance ignored. Choose downwards as positive, so $u = 0$, $a = 9.8 \, \text{m s}^{-2}$ and $s = 20 \, \text{m}$.

Use $v^2 = u^2 + 2as$. 

 $$v^2 = 0^2 + 2(9.8)(20) = 392$$

$$$v = \sqrt{392} \approx 19.8 \, \text{m s}^{-1}$$ 

 The positive square root is taken because the question asks for speed.

This model is reasonable for a small dense stone, because air resistance may be small compared with its weight. In reality there is still some drag, so the actual speed would be slightly less than $19.8 \, \text{m s}^{-1}$.

## Smooth, rough, light and inextensible

![Two blocks connected by a taut inextensible string over a smooth light pulley with equal tensions and equal-magnitude accelerations](../assets/002-783824a0-e4c1-4b54-9200-1cf68cc3c806.jpeg)
A smooth surface has no friction, while a rough surface does include friction. A light object has zero mass in the model, so light does not mean small.

If a string is taut and inextensible, connected particles have the same magnitude of acceleration. If a pulley is smooth and light, the tension is the same on both sides.

Be careful with the word taut. If the string goes slack, the same-acceleration conclusion no longer follows.

## Writing exam-style comments on suitability

When you judge a model, do not just say it is unrealistic. Name the assumption and explain what real effect has been ignored.

A strong sentence uses the word because. For example, ignoring air resistance may be unsuitable because the object has a large surface area, so drag could noticeably reduce its acceleration. This links the assumption to a physical consequence.

The same idea works for the particle model. A bus may be treated as a particle for a long straight journey, but not if turning, tipping or size clearance matters.

## Check yourself

1. A car travelling $200\,\text{m}$ along a straight road is modelled as a particle. What does this mean?

   - Its mass is treated as concentrated at one point, so size and turning effects are ignored. ✔

   - It has zero mass.

   - No forces act on it.

   - It must be moving very slowly.

   _Explanation:_ A particle model keeps the object's mass and weight, but ignores its size, shape and rotation when these do not matter to the calculation. The common wrong answer is B: zero mass does not describe a particle.

2. A table tennis ball is modelled as moving freely under gravity with negligible air resistance. Why might this model be unsuitable?

   - Because a table tennis ball has a relatively large surface area for its mass, so air resistance may significantly change its acceleration. ✔

   - Because particles cannot move vertically.

   - Because modelling it as a particle removes its weight.

   - Because gravity near the Earth is not about $9.8 \, \text{m s}^{-2}$.

   _Explanation:_ The free-fall model assumes air resistance is small enough to ignore, so acceleration remains $g$ downward. The common wrong answer is C: a particle can still have mass and weight, so modelling it as a particle does not remove gravity.

3. Two particles are connected by a taut inextensible string over a pulley. Which change could make the tensions different on the two sides while the particles still have the same magnitude of acceleration?

   - The pulley is rough or has mass. ✔

   - The string becomes extensible.

   - One particle is described as a particle.

   - Air resistance is ignored.

   _Explanation:_ Equal tension comes from a smooth light pulley, while same acceleration magnitude comes from a taut inextensible string. The common wrong answer is B: if the string becomes extensible, the same-acceleration conclusion is no longer guaranteed.
