---
note_id: "rn_DzzVjDCzxdB7r6ky"
title: "Converting Between Binary & Denary"
source: https://www.savemyexams.com/igcse/computer-science/cie/23/revision-notes/1-data-representation/number-systems/converting-between-binary-and-denary
path: 1-data-representation/number-systems/converting-between-binary-and-denary
updated_at: "2025-05-06T13:39:19.187Z"
spec_point_ids: ["spcpt_68zy9XdVTMj5Tfgw", "spcpt_TkyP92G3wkKGzfKg"]
spec_point_codes: []
guided_study: false
---

# Converting Between Binary & Denary

## Denary to Binary Conversion

> **Spec point** — `spcpt_68zy9XdVTMj5Tfgw` · b(i) Convert between positive denary and positive binary

## Denary to Binary Conversion

> **Exam Hint**
> *Every method and number line on this page follows the exact rules and bit limits used in the Cambridge IGCSE 0478 exam. No extras. No guesswork.*

### How do you convert denary to binary?

- It is important to **know the process** of converting from denary to binary to understand how computers interpret and process data
- To convert from denary to binary you must start by **writing out a binary number line**
- Find the first column heading with **a value larger than the denary value **you are converting
- Write down **each column heading to the right (not including the largest heading) **until you reach 1

| 32,768 | 16,384 | 8,192 | 4,096 | 2,048 | 1,024 | 512 | 256 | **128** | **64** | **32** | **16** | **8** | **4** | **2** | **1** |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|

#### Example 1

- To convert the denary number **45 **to binary, start by **writing out the binary number line**
- The **first column heading larger than 45** is **64**, so the number line would be:

| **32** | **16** | **8** | **4** | **2** | **1** |
|---|---|---|---|---|---|
|   |   |   |   |   |   |

- Start at the **leftmost empty column heading** (32)
- Divide **column heading into denary number** (how many times does 32 fit into 45?)

  - 1 time with 13 remaining

| 13 |   |   |   |   |   |
|---|---|---|---|---|---|
| **32** | **16** | **8** | **4** | **2** | **1** |
| * 1* | * * | * * | * * | * * | * * |

- **Repeat with next column heading** (how many times does 16 fit into 13?)

  - 0 times with 13 remaining

| 13 | 13 |   |   |   |   |
|---|---|---|---|---|---|
| **32** | **16** | **8** | **4** | **2** | **1** |
| *1* | *0* |   |   |   |   |

- **Repeat **until all columns have a binary value

| 13 | 13 | 5 | 1 | 1 | 0 |
|---|---|---|---|---|---|
| **32** | **16** | **8** | **4** | **2** | **1** |
| *1 * | *0 * | *1 * | *1 * | *0 * | *1 * |

- Denary **45 **is *101101 *in binary (6 bits)

> **Exam Hint**
> *Cambridge often asks for a ****specific number of bits****—if the question says “8-bit answer,” you must pad your binary result with leading 0s. Always double-check the number of bits or you’ll lose a mark.*

#### Example 2

- To convert the denary number **3059 **to binary, start by **writing out the binary number line**
- The **first column heading larger than 3059** is **4096**, so the number line would be:

| 2,048 | 1,024 | 512 | 256 | **128** | **64** | **32** | **16** | **8** | **4** | **2** | **1** |
|---|---|---|---|---|---|---|---|---|---|---|---|
|   |   |   |   |   |   |   |   |   |   |   |   |

- Start at the **leftmost empty column heading** (2048)
- Divide **column heading into denary number** (how many times does 2048 fit into 3059?)

  - 1 time with 1011 remaining

| 1011 |   |   |   |   |   |   |   |   |   |   |   |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 2,048 | 1,024 | 512 | 256 | **128** | **64** | **32** | **16** | **8** | **4** | **2** | **1** |
| *1* |   |   |   |   |   |   |   |   |   |   |   |

- **Repeat with next column heading** (how many times does 1024 fit into 1011?)

  - 0 times with 1011 remaining

| 1011 | 1011 |   |   |   |   |   |   |   |   |   |   |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 2,048 | 1,024 | 512 | 256 | **128** | **64** | **32** | **16** | **8** | **4** | **2** | **1** |
| *1* | *0* |   |   |   |   |   |   |   |   |   |   |

- **Repeat **until all columns have a binary value

| 1011 | 1011 | 499 | 243 | 115 | 51 | 19 | 3 | 3 | 3 | 1 | 0 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 2,048 | 1,024 | 512 | 256 | **128** | **64** | **32** | **16** | **8** | **4** | **2** | **1** |
| *1* | *0* | *1* | *1* | *1* | *1* | *1* | *1* | *0* | *0* | *1* | *1* |

- Denary **3059 **is *101111110011 *in binary (12 bits)

## Binary to Denary Conversion

> **Spec point** — `spcpt_TkyP92G3wkKGzfKg` · b(i) Convert between positive denary and positive binary

## Binary to Denary Conversion

- To convert from binary to denary, count how many bits make up the value
- Write out the column headings for the number of bits given from right to left
- Add together any column heading with a value of 1 in the column

#### Example 1 (4 bits)

- To convert the binary number *1011 *to denary, start by **writing out the binary headings** from right to left

| **8** | **4** | **2** | **1** |
|---|---|---|---|
|   |   |   |   |

- Write in the binary digits under the headings from left to right

| **8** | **4** | **2** | **1** |
|---|---|---|---|
| *1* | *0* | *1* | *1* |

- Add together **any column heading with a 1 under it**
- (1 x 8) + (1 x 2) + (1 x 1) = 11
- Binary *1011 *is **11 **in denary

> **Exam Hint**
> *If a binary number ends in 1, the denary result ****must**** be odd. Use this as a quick logic check during the exam—examiners love to test basic number sense.*

#### Example 2 (8 bits)

- To convert the binary number *01100011 *to denary, start by **writing out the binary headings** from right to left

| **128** | **64** | **32** | **16** | **8** | **4** | **2** | **1** |
|---|---|---|---|---|---|---|---|
|   |   |   |   |   |   |   |   |

- Write in the binary digits under the headings from left to right

| **128** | **64** | **32** | **16** | **8** | **4** | **2** | **1** |
|---|---|---|---|---|---|---|---|
| *0* | *1* | *1* | *0* | *0* | *0* | *1* | *1* |

- Add together **any column heading with a 1 under it**
- (1 x 64) + (1 x 32) + (1 x 2) + (1 x 1) = 99
- Binary *01100011 *is **99** in denary

#### Example 3 (14 bits)

- To convert the binary number *01110001110100 *to denary, start by **writing out the binary headings** from right to left

| 8,192 | 4,096 | 2,048 | 1,024 | 512 | 256 | **128** | **64** | **32** | **16** | **8** | **4** | **2** | **1** |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| *0* | *1* | *1* | *1* | *0* | *0* | *0* | *1* | *1* | *1* | *0* | *1* | *0* | *0* |

- Add together **any column heading with a 1 under it**
- (1 x 4096) + (1 x 2048) + (1 x 1024) + (1 x 64) + (1 x 32) + (1 x 16) + (1 x 4) = 7284
- Binary *01110001110100 *is **7284 **in denary
