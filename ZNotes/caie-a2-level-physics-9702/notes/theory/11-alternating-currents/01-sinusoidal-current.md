# Alternating Currents

## Sinusoidal Current

* **Period,** $\mathbf{T}$**:** ***the time for one complete cycle
  of the a.c. (alternating current)***
* **Frequency,** $\mathbf{f}$**:** number of oscillations per unit
  time

$$
f = \frac{1}{T}
$$

* **Peak value,**
  $$I_0$$ and $$V_0$$**:**
  highest point on the graph, max current/voltage
* **Instantaneous current/voltage,** $\mathbf{I/V}$**:** the
  current/voltage at a particular instant of time $(t)$

$$
I = I_{0}\sin\text{ωt }/V = V_{0}\sin\text{ωt}
$$

where $\omega = 2\pi f = \frac{2\pi}{T}$

Note that the above equation only applies if the starting current/voltage at time=0 is zero; if the starting current/voltage is maxium, replace sin with cos

![](https://images.znotes.org/allimages/ebbdeafdf933189522853337.webp =545x)

* The **root-mean-squared (r.m.s.) value,**

  $$
  I_{\text{rms}}/V_{\text{rms}}
  $$

  is the value of steady current/voltage that produces same power in a resistor as the alternating current/voltage

$$
I_{\text{rms}} = \frac{I_{0}}{\sqrt{2}}
$$

$$
V_{\text{rms}} = \frac{V_{0}}{\sqrt{2}}
$$
Where:

* $$I_0$$ is the peak I value
* $$V_0$$ is the peak V value

**Question:**

An electronic device in Mr Jenning’s house is an alternating current supply which is represented by the equation:

$$I = 6.0 \sin(100\pi t)$$

where $I$ is the current in amperes ($\text{A}$) and $t$ is the time in seconds ($\text{s}$).

1. State the peak current $I_0$ and calculate the root-mean-square current $I_{\text{rms}}$.

2. Determine the frequency $f$ of the alternating current.

3. Calculate the average power dissipated when this current passes through a $12\ \Omega$ resistor.

**Solution:**

1. **Peak and r.m.s. Current:**

   From the equation $I = I_0 \sin(\omega t)$, the peak current is $I_0 = 6.0\text{ A}$.

   $$I_{\text{rms}} = \frac{I_0}{\sqrt{2}} = \frac{6.0}{\sqrt{2}} \approx 4.24\text{ A}$$

2. **Frequency:**

   Angular frequency $\omega = 100\pi\text{ rad s}^{-1}$.

   $$f = \frac{\omega}{2\pi} = \frac{100\pi}{2\pi} = 50\text{ Hz}$$

3. **Average Power:**

   $$P_{\text{avg}} = I_{\text{rms}}^2 R = (4.24)^2 \times 12 = 216\text{ W}$$