---
note_id: "rn_jps3NptRBvtk8FQc"
title: "Exponential Discharge in a Capacitor"
source: https://www.savemyexams.com/international-a-level/physics/edexcel/19/revision-notes/4-further-mechanics-fields-and-particles/capacitance/4-24-exponential-discharge-in-a-capacitor
path: 4-further-mechanics-fields-and-particles/capacitance/4-24-exponential-discharge-in-a-capacitor
updated_at: "2026-07-02T08:19:39.481Z"
spec_point_ids: ["spcpt_tqZ9jBYpXQCFjZ5p"]
spec_point_codes: []
guided_study: false
---

# Exponential Discharge in a Capacitor

## Exponential Discharge in a Capacitor

> **Spec point** — `spcpt_tqZ9jBYpXQCFjZ5p`

## Exponential Discharge in a Capacitor

#### The Discharge Equation

- When a capacitor discharges through a resistor, the charge stored on it decreases **exponentially**
- The amount of charge remaining on the capacitor *Q* after some elapsed time *t* is governed by the **exponential decay equation**:

$Q=Q_{0}e^{-(t/RC)}$

- Where:

  - *Q* = charge remaining (C)
  - *Q*<sub>0</sub> = initial charge stored (C)
  - *e* = exponential function
  - *t* = elapsed time (s)
  - *R = *circuit* *resistance (Ω)
  - *C* = capacitance (F)

#### Discharge Equation for Potential Difference

- The exponential decay equation for **charge** can be used to derive a decay equation for potential difference

- Recall the equation for charge *Q* = *CV*

  - It also follows that the initial charge *Q*<sub>0</sub>* *= *CV*<sub>0</sub>* *(where *V*<sub>0</sub> is the initial potential difference)

- Therefore, substituting *CV* for *Q *into the original exponential decay equation gives:

$CV=CV_{0}e^{-(t/RC)}$

- Cancelling *C *from both sides gives the exponential decay equation for **potential difference *****V*****:**

$V=V_{0}e^{-(t/RC)}$

- Where:

  - *V* = potential difference after some time *t* (V)
  - *V*<sub>0</sub> = initial potential difference (V)
  - *t* = elapsed time (s)
  - *R* = resistance (Ω)
  - *C* = capacitance (F)

- This equation shows that the potential difference also decreases **exponentially, **from some initial value *V*<sub>0</sub>

#### Discharge Equation for Current

- The exponential decay equation for **potential difference** can be used to derive a decay equation for current

- Recall Ohm's law ***V***** = *****IR***

  - It follows that the initial potential difference *V*<sub>0</sub>* *= *I*<sub>0</sub>*R *(where *I*<sub>0</sub> is the initial current)

- Therefore, substituting *IR* for *V *into the decay equation for potential difference gives:

$IR=I_{0}Re^{-(t/RC)}$

- Cancelling *R *from both sides gives the exponential decay equation for **current *****I*****:**

$I=I_{0}e^{-(t/RC)}$

- Where:

  - *I* = current after some time *t* (A)
  - *I*<sub>0</sub> = initial current (A)
  - *t* = elapsed time (s)
  - *R* = resistance (Ω)
  - *C* = capacitance (F)

- This equation shows that the current also decreases **exponentially, **from some initial value *I*<sub>0</sub>

> **Worked Example**
> A 10 mF capacitor is fully charged by a 12 V power supply and then discharged through a 1 kΩ resistor.
> 
> What is the discharge current after 15 s?
> 
> **Answer:**
> 
> **Step 1: Write the known quantities**
> 
> - Initial potential difference *V*<sub>0</sub> = 12 V
> - Resistance *R* = 1 kΩ = 1000 Ω
> - Capacitance *C* = 10 mF = 0.01 F
> - Time elapsed = 15 s
> 
> **Step 2: Determine the initial current *****I***<sub>**0**</sub>
> 
> - Since the initial potential difference is 12 V and the resistance is 1000 Ω, then:
> 
> $I_{0}=\frac{V_{0}}{R}=\frac{12}{1000}$= 0.012 A
> 
> **Step 3: Write the decay equation for current**
> 
> - The decay equation for current is:
> 
> $I=I_{0}e^{-(t/RC)}$
> 
> **Step 4: Substitute quantities and calculate the current after 15 s **
> 
> - Substituting quantities gives the following:
> 
> *I* = (0.012) × (*e*<sup>–(15/(1000 × 0.01)</sup>)
> 
> *I* = (0.012) × (*e*<sup>–1.5</sup>)
> 
> *I *= (0.012) × (0.223...)
> 
> *I* = 2.7 × 10<sup>–3</sup> A = 2.7 mA

> **Exam Hint**
> Remember you can work out initial quantities like current or potential difference or charge using the equations:
> 
> - *V*<sub>0</sub> = *I*<sub>0</sub>*R*
> - *Q*<sub>0</sub> = *CV*<sub>0</sub>
> 
> You will then usually have enough information to substitute all necessary values into the decay equations!

#### Natural Logarithms & Discharge Equations

- The exponential decay equations are not **linear**
- They can be turned into linear equations by using the **natural logarithm** function

- Recall the exponential decay equation for charge:

$Q=Q_{0}e^{-(t/RC)}$

- Dividing both sides by *Q*<sub>0</sub> gives:

$\frac{Q}{Q_{0}}=e^{-(t/RC)}$

- Taking the **natural** **logarithm** of both sides 'cancels' the exponential function *e*, giving:

`ln space open parentheses Q over Q subscript 0 close parentheses equals ln space left parenthesis e to the power of negative left parenthesis t divided by R C right parenthesis end exponent right parenthesis equals negative fraction numerator t over denominator R C end fraction`

- This simplifies to:

$\mathrm{ln}Q--\mathrm{ln}Q_{0}=-\frac{t}{RC}$

- Leaving an equation for the natural logarithm of charge *Q* as:

$\mathrm{ln}Q=-\frac{1}{RC}t+\mathrm{ln}Q_{0}$

- This is the equation of a **straight** **line graph**, where:

  - ln *Q* is plotted on the *y*-axis
  - *t* is plotted on the *x*-axis
  - The gradient of the line is therefore equal to –1/*RC*

![7-13-natural-log-graph-charge_edexcel-al-physics-rn](../../../assets/4b1fb0c65d43-7-13-natural-log-graph-charge-edexcel-al-physics.png)

***The natural logarithm of the exponential decay curve line arises it to a straight-line graph with a gradient equal to –1/RC***

- Following similar steps, the linearised versions of the decay equations for **potential** **difference** *V *is:

$\mathrm{ln}V=--\frac{1}{RC}t+\mathrm{ln}V_{0}$

- And for current *I* is:

$\mathrm{ln}I=-\frac{1}{RC}t+\mathrm{ln}I_{0}$

> **Worked Example**
> When a capacitor discharges, the voltage *V* across it varies with time *t. *A graph showing the variation of ln *V* against *t* is shown for a particular discharging capacitor.
> 
> ![7-13-we-natural-log-graph-pd_edexcel-al-physics-rn](assets/8c4c28545919-7-13-we-natural-log-graph-pd-edexcel-al-physics-.png)
> 
> Use the graph to determine the initial voltage across the capacitor.
> 
> **Answer:**
> 
> **Step 1: Write the equation for the linearised decay equation for potential difference**
> 
> - The linearised decay equation for potential difference is given by:
> 
> $\mathrm{ln}V=-\frac{1}{RC}t+\mathrm{ln}V_{0}$
> 
> **Step 2: Interpret the graph given using the linearised equation**
> 
> - The equation says the y-intercept of the straight line is represented by ln *V*<sub>0</sub>
> 
> **Step 3: Use the y-intercept to determine the initial voltage**
> 
> - The y-intercept is equal to 2.1
> - Therefore:
> 
> ln *V*<sub>0</sub> = 2.1
> 
> **Step 4: Cancel the natural logarithm using the exponential function:**
> 
> - Raising both sides using the exponential function *e* 'cancels' the natural logarithm
> - This gives:
> 
> *V*<sub>0</sub> = *e*<sup>(2.1)</sup> = 8.2 V

> **Exam Hint**
> You need to know how to derive decay equations for pd and for current from the decay equation for charge, as well as how to use and interpret natural logarithm equations. If you can understand that these natural log equations are **linear**, because they can plotted as a graph in the form *y* = *mx *+ *c*, then you are well set for exam questions on this topic! Remember:
> 
> - The gradient of the straight line is given by -1/*RC*
> - The y-intercept of the line represents ln *Q*<sub>0</sub> or ln *V*<sub>0</sub> or ln *I*<sub>0</sub>
