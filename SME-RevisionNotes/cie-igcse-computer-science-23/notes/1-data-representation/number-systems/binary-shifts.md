---
note_id: "rn_kMmghdBykKGWk4Kg"
title: "Binary Shifts"
source: https://www.savemyexams.com/igcse/computer-science/cie/23/revision-notes/1-data-representation/number-systems/binary-shifts
path: 1-data-representation/number-systems/binary-shifts
updated_at: "2025-06-26T10:54:48.642Z"
spec_point_ids: ["spcpt_SGK63hHrknXV2vnB"]
spec_point_codes: []
guided_study: false
---

# Binary Shifts

## Binary Shifts

> **Spec point** — `spcpt_SGK63hHrknXV2vnB` · "5 Perform a logical binary shift on a positive 8-bit binary integer and understand the effect this has
on the positive binary integer"

## Binary Shifts

### What is a logical binary shift?

> **Exam Hint**
> *Cambridge IGCSE 0478 expects you to perform binary shifts ****on 8-bit values**** and explain how the result changes (×2, ÷2). Every example here mirrors the real exam format.*

- A logical binary shift is how a computer system performs **basic multiplication and division **on non-negative values (0 and positive numbers)
- Binary digits are **moved left** or **right **a set number of times
- A left shift **multiplies **a binary number by 2 (x2)
- A right shift **divides **a binary number by 2 (/2)
- A shift can move more than one place at a time, the principle remains the same
- A left shift of 2 places would multiply the original binary number by 4 (x4)

### How do you perform a logical left shift of 1?

- Here is the binary representation of the denary number 40

| **128** | **64** | **32** | **16** | **8** | **4** | **2** | **1** |
|---|---|---|---|---|---|---|---|
| ***0*** | ***0*** | ***1*** | ***0*** | ***1*** | ***0*** | ***0*** | ***0*** |

- To perform a left logical binary shift of 1, we move each bit 1 place to the left
- Since the most significant bit is 0, there is no overflow
- The 1 column becomes empty so is filled with a 0

| **128** | **64** | **32** | **16** | **8** | **4** | **2** | **1** | ** ** |
|---|---|---|---|---|---|---|---|---|
|   | ***0*** | ***1*** | ***0*** | ***1*** | ***0*** | ***0*** | ***0*** | **= 40** |
| ***0*** | ***1*** | ***0*** | ***1*** | ***0*** | ***0*** | ***0*** | ***0*** | **= 80** |

- The original binary representation of denary **40 **(32+8)  was **multiplied by 2** and became **80 **(64+16)

### How do you perform a logical left shift of 2?

- Here is the binary representation of the denary number 28

| **128** | **64** | **32** | **16** | **8** | **4** | **2** | **1** |
|---|---|---|---|---|---|---|---|
| ***0*** | ***0*** | ***0*** | ***1*** | ***1*** | ***1*** | ***0*** | ***0*** |

- To perform a left binary shift of 2, we move each bit 2 places to the left
- Since the two leftmost bits are **0**, nothing important is lost and **no overflow occurs**
- The 1 and 2 column become empty so are filled with a 0

| **128** | **64** | **32** | **16** | **8** | **4** | **2** | **1** | ** ** |
|---|---|---|---|---|---|---|---|---|
|   |   | ***0*** | ***1*** | ***1*** | ***1*** | ***0*** | ***0*** | **= 28** |
| ***0*** | ***1*** | ***1*** | ***1*** | ***0*** | ***0*** | ***0*** | ***0*** | **= 112** |

- The original binary representation of denary **28 **(16+8+4)  was **multiplied by 4** and became **112 **(64+32+16)

> **Exam Hint**
> *Your textbook might show shifts with longer binary values—but in IGCSE exams, you’ll only ever be asked about ****8-bit unsigned integers****. That’s why all our examples are capped at 8 bits.*

### How do you perform a logical right shift of 1?

- Here is the binary representation of the denary number 40

| **128** | **64** | **32** | **16** | **8** | **4** | **2** | **1** |
|---|---|---|---|---|---|---|---|
| ***0*** | ***0*** | ***1*** | ***0*** | ***1*** | ***0*** | ***0*** | ***0*** |

- To perform a right binary shift of 1, we move each bit 1 place to the right
- The bit in the **1 column (LSB)** is shifted out and **lost**
- The 128 column becomes empty so is filled with a 0

| **128** | **64** | **32** | **16** | **8** | **4** | **2** | **1** | ** ** |
|---|---|---|---|---|---|---|---|---|
| ***0*** | ***0*** | ***1*** | ***0*** | ***1*** | ***0*** | ***0*** |   | **= 40** |
| ***0*** | ***0*** | ***0*** | ***1*** | ***0*** | ***1*** | ***0*** | ***0*** | **= 20** |

- The original binary representation of denary **40** (32+8)  was **divided by 2** and became **20** (16+4)

### How do you perform a logical right shift of 2?

- Here is the binary representation of the denary number 200

| **128** | **64** | **32** | **16** | **8** | **4** | **2** | **1** |
|---|---|---|---|---|---|---|---|
| ***1*** | ***1*** | ***0*** | ***0*** | ***1*** | ***0*** | ***0*** | ***0*** |

- To perform a right binary shift of 2, we move each bit 2 places to the right
- The bits in the **1 and 2 columns** are shifted out and **lost**
- The 128 and 64 columns become empty so are filled with a 0

| **128** | **64** | **32** | **16** | **8** | **4** | **2** | **1** | ** ** |
|---|---|---|---|---|---|---|---|---|
| ***1*** | ***1*** | ***0*** | ***0*** | ***1*** | ***0*** |   |   | **= 200** |
| ***0*** | ***0*** | ***1*** | ***1*** | ***0*** | ***0*** | ***1*** | ***0*** | **= 50** |

- The original binary representation of denary **200 **(128+64+8) was **divided by 4** and became **50 **(32+16+2)

### Overflow in binary shifts

- **Overflow happens** when a **1 is shifted out of the most significant bit (MSB)** on the left in a logical left shift
- This means** important data is lost**, which can seriously change the number’s value

> **Exam Hint**
> *In IGCSE Computer Science, you usually only need to spot an overflow when a 1 is shifted out on the left. You don’t need to worry about ****underflow ****in this context!*
