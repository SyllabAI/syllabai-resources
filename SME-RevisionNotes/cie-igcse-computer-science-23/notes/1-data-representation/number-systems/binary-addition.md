---
note_id: "rn_mw6smcmBK3StMgDV"
title: "Binary Addition"
source: https://www.savemyexams.com/igcse/computer-science/cie/23/revision-notes/1-data-representation/number-systems/binary-addition
path: 1-data-representation/number-systems/binary-addition
updated_at: "2025-05-06T13:48:06.862Z"
spec_point_ids: ["spcpt_6DxWpcrHw9kFd3Hn", "spcpt_z9jBrF6zHBtMZm3S"]
spec_point_codes: []
guided_study: false
---

# Binary Addition

## Adding Positive 8-bit Binary Integers

> **Spec point** — `spcpt_6DxWpcrHw9kFd3Hn` · 4 (a) Add two positive 8-bit binary integers 

## Adding Positive 8-bit Binary Integers

> **Exam Hint**
> *Cambridge IGCSE 0478 expects you to add 8-bit binary values using clear working, with carries shown. These examples match the style and format used in the real exam.*

### What is binary addition?

- Binary addition is the process of **adding together two binary integers** (up to and including 8 bits)
- To be successful there are **5 golden rules** to apply:

| **Binary Addition** | **Binary Answer** | **Working** |
|---|---|---|
| 0 + 0 = | ***0*** | \| **1s** \| ** ** \|<br>\|---\|---\|<br>\| ***0*** \| **= 0** \| |
| 0 + 1 = | ***1*** | \| **1s** \| ** ** \|<br>\|---\|---\|<br>\| ***1*** \| **= 1** \| |
| 1 + 0 = | ***1*** | \| **1s** \| ** ** \|<br>\|---\|---\|<br>\| ***1*** \| **= 1** \| |
| 1 + 1 = | ***10*** | \| **2s** \| **1s** \| ** ** \|<br>\|---\|---\|---\|<br>\| ***1*** \| ***0*** \| **= 2** \| |
| 1 + 1 + 1 = | ***11*** | \| **2s** \| **1s** \| ** ** \|<br>\|---\|---\|---\|<br>\| ***1*** \| ***1*** \| **= 3** \| |

- Like denary addition, start from the rightmost digit and move left
- Carrying over occurs when the **sum of a column is greater than 1**, passing the excess to the next left column

#### Example 1

- Add together the binary values ***1001 ***and ***0100***

| **8** | **4** | **2** | **1** | **+** |
|---|---|---|---|---|
| ***1*** | ***0*** | ***0*** | ***1*** |   |
| ***0*** | ***1*** | ***0*** | ***0*** |   |
|   |   |   |   | **C** |
|   |   |   |   |   |

- Starting from right to left, add the two binary values together **applying the 5 golden rules**
- If your answer has **2 digits**, place the rightmost digit in the column and **carry the remaining digit** to the next column on the left
- In this example, start with 1+0, 1+0 = 1, so place a 1 in the column

| **8** | **4** | **2** | **1** | **+** |
|---|---|---|---|---|
| ***1*** | ***0*** | ***0*** | ***1*** |   |
| ***0*** | ***1*** | ***0*** | ***0*** |   |
|   |   |   |   | **C** |
|   |   |   | ***1*** |   |

- Repeat until **all columns have a value**

| **8** | **4** | **2** | **1** | **+** |
|---|---|---|---|---|
| ***1*** | ***0*** | ***0*** | ***1*** |   |
| ***0*** | ***1*** | ***0*** | ***0*** |   |
|   |   |   |   | **C** |
| ***1*** | ***1*** | ***0*** | ***1*** |   |

- The sum of adding together binary ***1001 ***(9) and ***0100 ***(4) is ***1101 ***(13)

> **Exam Hint**
> *You can earn marks ****just for showing carries correctly****, even if your final answer is wrong. Always show your carry bits clearly above or below your sum—examiner reports say it matters.*

#### Example 2

- Add together the binary values ***00011001 ***and ***10001001***

| **128** | **64** | **32** | **16** | **8** | **4** | **2** | **1** | **+** |
|---|---|---|---|---|---|---|---|---|
| ***0*** | ***0*** | ***0*** | ***1*** | ***1*** | ***0*** | ***0*** | ***1*** |   |
| ***1*** | ***0*** | ***0*** | ***0*** | ***1*** | ***0*** | ***0*** | ***1*** |   |
|   |   |   |   |   |   |   |   | **C** |
|   |   |   |   |   |   |   |   |   |

- Starting from right to left, add the two binary values together **applying the 5 golden rules**
- If your answer has **2 digits**, place the rightmost digit in the column and **carry the remaining digit** to the next column on the left
- In this example, start with 1+1, 1+1 = 10, so place a 0 in the column and carry the 1 to the next column

| **128** | **64** | **32** | **16** | **8** | **4** | **2** | **1** | **+** |
|---|---|---|---|---|---|---|---|---|
| ***0*** | ***0*** | ***0*** | ***1*** | ***1*** | ***0*** | ***0*** | ***1*** |   |
| ***1*** | ***0*** | ***0*** | ***0*** | ***1*** | ***0*** | ***0*** | ***1*** |   |
|   |   |   |   |   |   | ***1*** | *** *** | **C** |
|   |   |   |   |   |   | *** *** | ***0*** |   |

- Repeat until **all columns have a value**

| **128** | **64** | **32** | **16** | **8** | **4** | **2** | **1** | **+** |
|---|---|---|---|---|---|---|---|---|
| ***0*** | ***0*** | ***0*** | ***1*** | ***1*** | ***0*** | ***0*** | ***1*** |   |
| ***1*** | ***0*** | ***0*** | ***0*** | ***1*** | ***0*** | ***0*** | ***1*** |   |
| *** *** | *** *** | ***1*** | ***1*** | *** *** | *** *** | ***1*** | *** *** | **C** |
| ***1*** | ***0*** | ***1*** | ***0*** | ***0*** | ***0*** | ***1*** | ***0*** |   |

- The sum of adding together binary ***00011001 ***(25) and ***10001001 ***(137) is ***10100010 ***(162)

## Overflow & Binary Addition

> **Spec point** — `spcpt_z9jBrF6zHBtMZm3S` · 4 (b) Understand the concept of overflow and why it occurs in binary addition

## Overflow & Binary Addition

### What is an overflow error?

- An overflow error occurs when the result of a binary addition** exceeds the available bits**
- For example, if you took binary ***11111111 ***(255) and tried to add ***00000001 ***(1) this would cause an overflow error as the result would need a **9th** bit to represent the answer (256)

| **256** | **128** | **64** | **32** | **16** | **8** | **4** | **2** | **1** | **+** |
|---|---|---|---|---|---|---|---|---|---|
|   | ***1*** | ***1*** | ***1*** | ***1*** | ***1*** | ***1*** | ***1*** | ***1*** |   |
|   | ***0*** | ***0*** | ***0*** | ***0*** | ***0*** | ***0*** | ***0*** | ***1*** |   |
| ***1*** | ***1*** | ***1*** | ***1*** | ***1*** | ***1*** | ***1*** | ***1*** | *** *** | **C** |
| *** *** | ***0*** | ***0*** | ***0*** | ***0*** | ***0*** | ***0*** | ***0*** | ***0*** |   |

> **Exam Hint**
> *If the next question asks what error has occurred, it's probably testing ****overflow****. Look for sums that go over 255—Cambridge loves this trick.*
