---
note_id: "rn_smNP7xpYBRzcDfMY"
title: "Converting Between Hexadecimal & Binary"
source: https://www.savemyexams.com/igcse/computer-science/cie/23/revision-notes/1-data-representation/number-systems/converting-between-hexadecimal-and-binary
path: 1-data-representation/number-systems/converting-between-hexadecimal-and-binary
updated_at: "2025-05-06T13:45:13.182Z"
spec_point_ids: ["spcpt_tTFNDhXyrJ3xFxQb", "spcpt_35mBJJzHpr7dxtxW"]
spec_point_codes: []
guided_study: false
---

# Converting Between Hexadecimal & Binary

## Binary to Hexadecimal Conversion

> **Spec point** — `spcpt_tTFNDhXyrJ3xFxQb` · b(iii) Convert between positive hexadecimal and positive binary

## Binary to Hexadecimal Conversion

### How do you convert from binary to hexadecimal?

> **Exam Hint**
> *Cambridge IGCSE 0478 expects all conversions to use 8-bit binary and 2-digit hex where possible. These examples follow the exam format exactly—so you’re revising the right way.*

- It is important before revising how to convert from binary to hexadecimal and vice versa that you fully understand the [binary](https://www.savemyexams.com/gcse/computer-science/ocr/22/revision-notes/2-memory-and-storage/data-storage-and-compression/converting-between-denary-and-binary/) and [hexadecimal](https://www.savemyexams.com/gcse/computer-science/ocr/22/revision-notes/2-memory-and-storage/data-storage-and-compression/converting-between-denary-and-hexadecimal/) number systems.

| **0** | **1** | **2** | **3** | **4** | **5** | **6** | **7** | **8** | **9** | **10** | **11** | **12** | **13** | **14** | **15** |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| **0** | **1** | **2** | **3** | **4** | **5** | **6** | **7** | **8** | **9** | **A** | **B** | **C** | **D** | **E** | **F** |

#### Example 1

- To convert the binary number *10110111 *to **hexadecimal**, first split the 8 bit number into 2 binary** *****nibbles***

| **8** | **4** | **2** | **1** | ** ** | **8** | **4** | **2** | **1** |
|---|---|---|---|---|---|---|---|---|
| *1* | *0* | *1* | *1* | *0* | *1* | *1* | *1* |   |

- For each nibble, convert the binary to it’s denary value
- (1 x 8) + (1 x 2) + (1 x 1) = 11 (B)
- (1 x 4) + (1 x 2) + (1 x 1) = 7
- Join them together to make a 2 digit hexadecimal number
- Binary *10110111 *is **B7 **in hexadecimal

#### Example 2

- To convert the binary number *00111001 *to **hexadecimal**, first split the 8 bit number into 2 binary nibbles

| **8** | **4** | **2** | **1** | ** ** | **8** | **4** | **2** | **1** |
|---|---|---|---|---|---|---|---|---|
| *0* | *0* | *1* | *1* | *1* | *0* | *0* | *1* |   |

- For each nibble, convert the binary to it’s denary value
- (1 x 2) + (1 x 1) = 3
- (1 x 8) + (1 x 1) = 9
- Join them together to make a 2 digit hexadecimal number
- Binary *00111001 *is **39 **in hexadecimal

## Hexadecimal to Binary Conversion

> **Spec point** — `spcpt_35mBJJzHpr7dxtxW` · b(iii) Convert between positive hexadecimal and positive binary

## Hexadecimal to Binary Conversion

### How do you convert from hexadecimal to binary?

#### Example 1

- To convert the hexadecimal number **5F **to binary, first **split the digits apart** and convert each to a binary **nibble**

| **8** | **4** | **2** | **1** |   |
|---|---|---|---|---|
| *0* | *1* | *0* | *1* | **= 5** |

| **8** | **4** | **2** | **1** |   |
|---|---|---|---|---|
| *1* | *1* | *1* | *1* | **= 15 (F)** |

- Join the 2 binary nibbles together to create an 8 bit binary number

| **128** | **64** | **32** | **16** | **8** | **4** | **2** | **1** |
|---|---|---|---|---|---|---|---|
| *0* | *1* | *0* | *1* | *1* | *1* | *1* | *1* |

- Hexadecimal **5F **is ***01011111 ***in binary

> **Exam Hint**
> *You might see methods that skip writing out the full 8-bit binary number—especially in textbooks. In this course, we stick to ****examiner-approved formatting****, so your answers never fall short.*

#### Example 2

- To convert the hexadecimal number **26 **to binary, first **split the digits apart **and convert each to a binary **nibble**

| **8** | **4** | **2** | **1** |   |
|---|---|---|---|---|
| *0* | *0* | *1* | *0* | **= 2** |

| **8** | **4** | **2** | **1** |   |
|---|---|---|---|---|
| *0* | *1* | *1* | *0* | **= 6** |

- Join the 2 binary nibbles together to create an 8 bit binary number

| **128** | **64** | **32** | **16** | **8** | **4** | **2** | **1** |
|---|---|---|---|---|---|---|---|
| *0* | *0* | *1* | *0* | *0* | *1* | *1* | *0* |

- Hexadecimal **26 **is ***00100110 ***in binary
