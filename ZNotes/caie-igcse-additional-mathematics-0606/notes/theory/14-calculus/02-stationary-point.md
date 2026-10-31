## Stationary Point

### Distinguishing Maximum and Minimum Points

* At a stationary point, the first derivative is zero:$$f'(x) = 0$$

* To determine whether the stationary point is a maximum or minimum, use the second derivative test:

  * If
    $
    f''(x) > 0,
    $
    then the point is a local minimum (the curve is concave up).

  * If
    $
    f''(x) < 0,
    $
    then the point is a local maximum (the curve is concave down).

  * If
    $
    f''(x) = 0,
    $
    the point may be a point of inflection (inconclusive)

**Example**

### Classifying Stationary Points of $f(x) = x^3 - 3x^2 + 4 $

1. Find the first derivative:
   $$
   f'(x) = 3x^2 - 6x
   $$

2. Find stationary points by setting $ f'(x) = 0 $:
   $$
   3x^2 - 6x = 0 \implies 3x(x - 2) = 0 \implies x = 0 \text{ or } x = 2
   $$

3. Find the second derivative:
   $$
   f''(x) = 6x - 6
   $$

4. Evaluate $f''(x)$ at each stationary point:

- At $ x = 0 $:
  $
  f''(0) = 6(0) - 6 = -6 < 0
  $
  Since $ f''(0) < 0 $, $ x = 0 $ is a local maximum.

- At $ x = 2 $:
  $
  f''(2) = 6(2) - 6 = 12 - 6 = 6 > 0
  $
  Since $ f''(2) > 0 $, $ x = 2 $ is a local minimum.

### Summary:

$ x = 0 $ is a local maximum.

$ x = 2 $ is a local minimum.