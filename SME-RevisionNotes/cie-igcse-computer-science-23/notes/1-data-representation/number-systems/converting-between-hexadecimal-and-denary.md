---
note_id: "rn_384NpCXbr4q38bXJ"
title: "Converting Between Hexadecimal & Denary"
source: https://www.savemyexams.com/igcse/computer-science/cie/23/revision-notes/1-data-representation/number-systems/converting-between-hexadecimal-and-denary
path: 1-data-representation/number-systems/converting-between-hexadecimal-and-denary
updated_at: "2025-05-06T13:43:18.519Z"
spec_point_ids: ["spcpt_wT34gWDgJFZS4TC3", "spcpt_r3PTG5W2NwdpfpRw"]
spec_point_codes: []
guided_study: false
---

# Converting Between Hexadecimal & Denary

## Denary to Hexadecimal Conversion

> **Spec point** — `spcpt_wT34gWDgJFZS4TC3` · b(ii) Convert between positive denary and positive hexadecimal

## Denary to Hexadecimal Conversion

### How do you convert denary to hexadecimal?

> **Exam Hint**
> *Cambridge IGCSE 0478 requires you to convert between denary and hex without a calculator. Every method shown here is designed to match exam conditions exactly.*

#### Method 1 (denary to binary to hexadecimal)

- To convert the denary number **28 **to hexadecimal, start by converting the [denary number to binary](https://www.savemyexams.com/o-level/computer-science/cie/21/revision-notes/1-data-representation/number-systems/converting-between-binary-and-denary/)

| **128** | **64** | **32** | **16** | **8** | **4** | **2** | **1** |
|---|---|---|---|---|---|---|---|
| *0* | *0* | *0* | *1* | *1* | *1* | *0* | *0* |

- **Split **the 8 bit binary number into **two nibbles** as shown below

| **8** | **4** | **2** | **1** | ** ** | **8** | **4** | **2** | **1** |
|---|---|---|---|---|---|---|---|---|
| *0* | *0* | *0* | *1* | *1* | *1* | *0* | *0* |   |

- Convert each nibble to its denary value
- **0001 = 1** and **1100 = 12**
- Using the [comparison table](https://www.savemyexams.com/o-level/computer-science/cie/21/revision-notes/1-data-representation/number-systems/number-systems/), the denary value 1 is also 1 in hexadecimal whereas denary value 12 is represented in hexadecimal as C
- Denary **28 **is **1C **in hexadecimal

#### Method 2 (divide by 16)

- To convert the denary number 163 to hexadecimal, start by **dividing the denary** value by 16 and recording the **whole times** the number goes in and the **remainder**
- 163 ➗16 = 10 remainder 3
- In hexadecimal the **whole number = digit 1** and the **remainder = digit 2**
- Digit 1 = 10 (A)
- Digit 2 = 3
- Denary **163 **is **A3** in hexadecimal

## Hexadecimal to Denary Conversion

> **Spec point** — `spcpt_r3PTG5W2NwdpfpRw` · b(ii) Conver between positive denary and positive hexadecimal

## Hexadecimal to Denary Conversion

### How do you convert hexadecimal to denary?

#### Method 1 (hexadecimal to binary to denary)

> **Exam Hint**
> *If you're not confident multiplying or dividing by 16, always fall back on binary conversion. It’s ****fool proof****, and examiners accept either method.*

- To convert the hexadecimal number **B9 **to denary, take each hexadecimal digit and convert it from its **denary value **to** 4 bit binary **(nibble)

| **B (11)** | ** **<br><br>** ** | **9** |   |   |   |   |   |
|---|---|---|---|---|---|---|---|
| **8** | **4** | **2** | **1** | **8** | **4** | **2** | **1** |
| *1* | *0* | *1* | *1* | *1* | *0* | *0* | *1* |

- **Join **the two nibbles to make an** 8 bit number **(byte)
- Convert from [binary to denary](https://www.savemyexams.com/o-level/computer-science/cie/21/revision-notes/1-data-representation/number-systems/converting-between-binary-and-denary/)

| **128** | **64** | **32** | **16** | **8** | **4** | **2** | **1** |
|---|---|---|---|---|---|---|---|
| *1* | *0* | *1* | *1* | *1* | *0* | *0* | *1* |

- (1 x 128) + (1 x 32) + (1 x 16) + (1 x 8) + (1 x 1) = 185
- Hexadecimal **B9 **is **185 **in denary

#### Method 2 (multiply by 16)

- To convert the hexadecimal number **79 **to denary, start by **multiplying the first hexadecimal digit by 16**
- 7 ✖ 16 = 112
- **Add digit 2** to the result
- 112 + 9 = 121
- Hexadecimal **79 **is **121 **in denary

> **Exam Hint**
> Remember that the exam is non-calculator, if you are not confident multiplying and dividing by 16 then use method 1 on both conversions
