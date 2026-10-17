---
note_id: "rn_HVvRmykQp8vkfw2T"
title: "Floating-Point Basics"
source: https://www.savemyexams.com/a-level/computer-science/cie/19/revision-notes/13-data-representation-/floating-point-numbers-representation-and-manipulation/floating-point-basics
path: 13-data-representation-/floating-point-numbers-representation-and-manipulation/floating-point-basics
updated_at: "2026-07-02T09:13:35.228Z"
spec_point_ids: ["spcpt_dMzQRprWM4d9tk5Z", "spcpt_VCDty8T35dnZj3yF"]
spec_point_codes: []
guided_study: false
---

# Floating-Point Basics

## Floating-point binary

> **Spec point** — `spcpt_dMzQRprWM4d9tk5Z`

## Floating-point binary

### What is floating-point binary?

- Floating-point binary represents **real numbers** in binary: numbers with a fractional part, and numbers that are very large or very small
- It works like **scientific notation, but in base 2**
- The number is written as a **mantissa** multiplied by **2 to the power of an exponent**
- In denary, `3140 = 3.14 × 10³`

  - Here `3.14` is the mantissa (the significant digits) and `3` is the exponent (how far to move the decimal point)
- Floating-point binary does exactly this using powers of 2

#### Why use floating-point?

- It represents a **much wider range** of numbers than fixed-point using the same number of bits
- The binary point can "float", giving good **precision** for fractional values

#### The two parts

| Component | Description |
|---|---|
| **Mantissa** | The significant bits of the number. It is a **two's complement** number with the binary point **immediately after the leftmost bit**, so that leftmost bit acts as the sign (`0` = positive, `1` = negative) |
| **Exponent** | How many places to move the binary point (positive = right, negative = left). Also stored in **two's complement** |

- **Both the mantissa and the exponent are stored in two's complement**

#### Positive numbers: example +6.25

- `6.25 = 110.01₂`
- Normalise: `110.01 = 0.11001 × 2³`
- Mantissa (12-bit) = `0` then fraction `11001`, padded = `011001000000`
- Exponent (4-bit) = `+3 = 0011`

#### Negative numbers: example −6.25

- Work out the **positive mantissa first**, then take its **two's complement** (flip the bits and add 1)
- Do **not** just change the sign bit

| Step | Bits |
|---|---|
| Positive mantissa for +6.25 | `011001000000` |
| Flip the bits | `100110111111` |
| Add 1 | `100111000000` |

- So **−6.25**: Mantissa = `100111000000`, Exponent = `0011`
- The mantissa now begins `10`, which is the correct start for a normalised negative number

## Normalising floating-point numbers

> **Spec point** — `spcpt_VCDty8T35dnZj3yF`

## Normalising floating-point numbers

### What is normalisation?

- A floating-point number is **normalised** when the first two bits of the mantissa are **different**:

  - `01…` for a positive number (the form `0.1xxxx`)
  - `10…` for a negative number (the form `1.0xxxx`)

#### Why normalise?

- **Precision**: removing leading zeros means the mantissa uses all of its bits for significant figures, giving the most accurate value possible for that number of bits
- **Uniqueness**: each number has exactly one normalised form, which makes comparison and arithmetic simpler

#### How to normalise

1. Shift the bits until the first two bits differ (`01` for positive, `10` for negative)
2. Adjust the exponent by the number of places the binary point moved:

  1. point moved **left** → **increase** the exponent
  2. point moved **right** → **decrease** the exponent

**Example (positive)**

- Before: mantissa `0.0011`, exponent `+2`
- Move the binary point **2 places right** so the mantissa becomes `0.1100` (first two bits are now `01`)
- **Decrease** the exponent by 2: `+2 → 0`
- Normalised: mantissa `01100`, exponent `0000` (the value is unchanged: `0.0011 × 2² = 0.11 × 2⁰`)

> **Exam Hint**
> - The **whole mantissa is two's complement**. For a negative number, find the **positive** mantissa, then **flip the bits and add 1**. Changing only the sign bit is a common mistake that loses every mark on the conversion.
> - **Both** the mantissa and the exponent are in two's complement.
> - **Check your answer with the first two bits**: a normalised positive number starts `01`, a normalised negative number starts `10`. If a negative number starts `11`, it is not normalised (or you used sign-and-magnitude by mistake).
> - Write the normalised form as `0.xxxxx × 2ⁿ` (CIE), not `1.xxxxx × 2ⁿ` (that is IEEE).
