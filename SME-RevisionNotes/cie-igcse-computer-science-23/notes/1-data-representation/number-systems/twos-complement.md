---
note_id: "rn_pvsW9s6PjJ4vbFzW"
title: "Two's Complement"
source: https://www.savemyexams.com/igcse/computer-science/cie/23/revision-notes/1-data-representation/number-systems/twos-complement
path: 1-data-representation/number-systems/twos-complement
updated_at: "2025-09-16T09:30:04.910Z"
spec_point_ids: ["spcpt_PqcxDCzbS2vr8sZR"]
spec_point_codes: []
guided_study: false
---

# Two's Complement

## Two's Complement

> **Spec point** — `spcpt_PqcxDCzbS2vr8sZR` · "6 Use two’s complement to represent positive and
negative 8-bit binary integers"

## Two's Complement

### What is two's complement?

> **Exam Hint**
> *Cambridge IGCSE 0478 requires you to represent signed binary values using ****8-bit two’s complement**** only. This page follows the exact bit structure and method examiners expect to see.*

- In IGCSE Computer Science, two's complement is a method of using ***signed binary values*** to **represent negative numbers**
- Using two's complement the** left most bit** is designated the most significant bit (**MSB**)
- In two’s complement, **if the MSB is 1**, it represents** a negative number**
- **In 8-bit**, the MSB column has a weight of **-128**, while the remaining columns keep their positive values

| **-128** | **64** | **32** | **16** | **8** | **4** | **2** | **1** |   |
|---|---|---|---|---|---|---|---|---|
| *1* | 1 | 1 | 1 | 1 | 1 | 1 | 1 | **= -1** |

- In the example above, to find the value, **add together the column values where there is a 1**
- Here, all columns are 1, so the sum is **-128 + 64 + 32 + 16 + 8 + 4 + 2 + 1 = -1**
- The two's complement representation of *-1* is *11111111*

#### Quick two's complement conversion

- To represent -76
- Write out the **positive version of the number**

| **128** | **64** | **32** | **16** | **8** | **4** | **2** | **1** |   |
|---|---|---|---|---|---|---|---|---|
| 0 | 1 | 0 | 0 | 1 | 1 | 0 | 0 | ** = 76** |

- Starting from the **least significant bit **(right most column), copy out the binary values **up to and including the first 1**

| **-128** | **64** | **32** | **16** | **8** | **4** | **2** | **1** |
|---|---|---|---|---|---|---|---|
|   |   |   |   |   | ***1*** | ***0*** | ***0*** |

- For the remaining digits,** invert them** (0s to 1s/1s to 0s)

| **-128** | **64** | **32** | **16** | **8** | **4** | **2** | **1** |
|---|---|---|---|---|---|---|---|
| *1* | *0* | *1* | *1* | *0* | 1 | 0 | 0 |

- -128 + 32 + 16 + 4 = **-76**
- The two's complement representation of *-76 *is *10110100*

> **Exam Hint**
> *The “flip and add 1” trick isn’t shown here, but the method above is what examiners prefer: copy from the right, then invert. It’s reliable, repeatable, and rewarded in papers.*
