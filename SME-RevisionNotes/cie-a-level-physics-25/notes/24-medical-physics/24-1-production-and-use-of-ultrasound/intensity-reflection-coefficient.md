---
note_id: "rn_khzrcdBNJkFqtnHg"
title: "Intensity Reflection Coefficient"
source: https://www.savemyexams.com/a-level/physics/cie/25/revision-notes/24-medical-physics/24-1-production-and-use-of-ultrasound/intensity-reflection-coefficient
path: 24-medical-physics/24-1-production-and-use-of-ultrasound/intensity-reflection-coefficient
updated_at: "2026-07-02T08:19:40.574Z"
spec_point_ids: ["spcpt_kbQN6wkHqfK9stqc"]
spec_point_codes: []
guided_study: true
---

# Intensity Reflection Coefficient

## Intensity Reflection Coefficient

> **Spec point** — `spcpt_kbQN6wkHqfK9stqc`

## Intensity reflection coefficient

- The intensity reflection coefficient α is defined as: **The ratio of the intensity of the reflected wave relative to the incident (transmitted) wave**
- This can be calculated using the fraction:

$\\alpha = \frac{I_{R} }{I_{0} } = \frac{( Z_{2} - Z_{1} )^{2} }{( Z_{2} + Z_{1} )^{2}}$

- Where:

  - *α* = intensity reflection coefficient
  - *I*<sub>R</sub> = intensity of the reflected wave (W m<sup>-2</sup>)
  - *I*<sub>0</sub> = intensity of the incident wave (W m<sup>-2</sup>)
  - *Z*<sub>1</sub> = acoustic impedance of one material (kg m<sup>-2</sup> s<sup>-1</sup>)
  - *Z*<sub>2</sub> = acoustic impedance of a second material (kg m<sup>-2</sup> s<sup>-1</sup>)

- This equation will be provided on the datasheet for your exam
- This ratio shows:

  - If there is a large difference between the impedance of the two materials, then most of the energy will be reflected
  - If the impedance is the same, then there will be **no reflection**

### Coupling medium

- When ultrasound is used in medical imaging, a **coupler **is needed between the transducer and the body
- The soft tissues of the body are much denser than air
- If air is present between the transducer and the body, then almost all the ultrasound energy will be reflected
- The coupling gel is placed between the transducer and the body, as skin and the coupling gel have a similar density, so little ultrasound is reflected

  - This is an example of *impedance matching*

> **Worked Example**
> A beam of ultrasound is incident at right angles to a boundary between two materials as shown in the diagram.
> 
> ![WE - Intensity reflection coefficient question image, downloadable AS & A Level Physics revision notes](assets/bca880104f7c-24-1-we-intensity-reflection-coefficient-questio.png)
> 
> The materials have acoustic impedances of *Z*<sub>1</sub> and *Z*<sub>2</sub>. The intensity of the transmitted ultrasound beam is *I*<sub>T</sub>, and the reflected intensity is *I*<sub>R</sub>.
> 
> (a) What is the relationship between *I*, *I*<sub>T</sub> and *I*<sub>R</sub>?
> 
> (b) Use the data from the table to determine the reflection coefficient α for a boundary between
> 
> (i)  gel and soft tissue
> 
> (ii)  air and soft tissue
> 
> (c) Explain why gel is usually put on the skin during medical diagnosis using ultrasound.
> 
> | **medium** | **speed of ultrasound / m s**<sup>**–1**</sup> | **acoustic impedance / kg m**<sup>**–2**</sup>** s**<sup>**–1**</sup> |
> |---|---|---|
> | air | 330 | 4.3 × 10<sup>2</sup> |
> | gel | 1500 | 1.5 × 10<sup>6</sup> |
> | soft tisuse | 1600 | 1.6 × 10<sup>6</sup> |
> | bone | 4100 | 7.0 × 10<sup>6</sup> |
> 
> **Answer:**
> 
> **Part (a)**
> 
> State the relationship between *I*, *I*<sub>T</sub> and *I*<sub>R</sub>:
> 
> Incident intensity = Transmitted intensity + Reflected intensity
> 
> $I=I_{T}+I_{R}$
> 
> **Part (b)(i)**
> 
> **Step 1: Write down the equation for intensity reflection coefficient α**
> 
> $\\alpha = \frac{( Z_{2} - Z_{1} )^{2} }{( Z_{2} + Z_{1} )^{2}}$
> 
> **Step 2: Write down the acoustic impedances for gel and soft tissue**
> 
> - Gel, *Z*<sub>1</sub> = 1.5 × 10<sup>6</sup> kg m<sup>-2</sup> s<sup>-1</sup>
> - Soft tissue, *Z*<sub>2</sub> = 1.6 × 10<sup>6</sup> kg m<sup>-2</sup> s<sup>-1</sup>
> 
> **Step 3: Calculate the intensity reflection coefficient**
> 
> $\\alpha = \frac{( 1.6 \times 10^{6} - 1.5 \times 10^{6} )^{2} }{( 1.6 \times 10^{6} + 1.5 \times 10^{6} )^{2}} = \frac{( 0.1 )^{2} }{( 3.1 )^{2}} = 0.001$
> 
> - This result means that only **0.1%** of the incident intensity will be reflected, with the remaining being transmitted
> 
> **Part (b)(ii)**
> 
> **Step 1: Write down the acoustic impedances for air and soft tissue**
> 
> - Air, *Z*<sub>1</sub> = 4.3 × 10<sup>2</sup> kg m<sup>-2</sup> s<sup>-1</sup>
> - Soft tissue, *Z*<sub>2</sub> = 1.6 × 10<sup>6</sup> kg m<sup>-2</sup> s<sup>-1</sup>
> 
> **Step 2:** **Calculate the intensity reflection coefficient**
> 
> $\\alpha = \frac{( 1.6 \times 10^{6} - 4.3 \times 10^{2} )^{2} }{( 1.6 \times 10^{6} + 4.3 \times 10^{2} )^{2}} \approx \frac{( 1.6 \times 10^{6} )^{2} }{( 1.6 \times 10^{6} )^{2}} \approx 1$
> 
> - This result means that **100%** of the incident intensity will be reflected, with none being transmitted
> 
> **Part (c)**
> 
> - At the air-soft tissue boundary, the intensity reflection coefficient is *α* ≈ 1
> 
>   - Therefore, without gel, there is almost complete reflection, no ultrasound is transmitted through the skin
> 
> - Therefore, the gel enables almost complete transmission of the ultrasound through the skin, with very little reflection
> 
>   - At the gel-soft tissue boundary, the intensity reflection coefficient is *α* = 0.001
