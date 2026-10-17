---
note_id: "rn_vDqdrDSHKhN3mhYs"
title: "Floating-Point Conversions"
source: https://www.savemyexams.com/a-level/computer-science/cie/19/revision-notes/13-data-representation-/floating-point-numbers-representation-and-manipulation/floating-point-conversions
path: 13-data-representation-/floating-point-numbers-representation-and-manipulation/floating-point-conversions
updated_at: "2026-07-02T09:29:40.957Z"
spec_point_ids: ["spcpt_NPkTzcxyQqKqymwn", "spcpt_VCY2SgXbSzFg7VCw"]
spec_point_codes: []
guided_study: false
---

# Floating-Point Conversions

## Denary to floating-point binary

> **Spec point** — `spcpt_NPkTzcxyQqKqymwn`

## Denary to floating-point binary

### How do you convert denary to floating-point binary?

- These examples assume:

  - 12-bit **mantissa** (two's complement, binary point after the leftmost bit)
  - 4-bit **exponent** (two's complement)

1. **Convert the magnitude to binary** (integer part + fractional part)

  1. e.g. `5 = 101₂`, `0.25 = 0.01₂`, so `5.25 = 101.01₂`
2. **Normalise** into the form `0.xxxxx × 2ⁿ`

  1. move the binary point until the first two bits differ; the number of places moved is the **exponent**
3. **Build the positive mantissa**: write `0`, then the fraction bits, then pad with zeros on the right
4. **If the number is negative**, take the **two's complement of the whole positive mantissa** (flip the bits and add 1)
5. **Convert the exponent** to two's complement in the required number of bits
6. **Write the final answer** as Mantissa and Exponent

#### Example: +5.25

- **Convert to binary**: `5.25 = 101.01₂`
- **Normalise**: `101.01 = 0.10101 × 2³`
- **Mantissa**: `0` + fraction `10101`, padded = `010101000000`
- **Exponent**: `+3 = 0011`
- **Result**: Mantissa `010101000000`, Exponent `0011`

#### Example: −5.25

- Work out the **positive** version first (as above): positive mantissa = `010101000000`
- Take the **two's complement** of the whole mantissa:

| Step | Bits |
|---|---|
| Positive mantissa | `010101000000` |
| Flip the bits | `101010111111` |
| Add 1 | `101011000000` |

- The exponent is **unchanged**: `+3 = 0011`
- **Result**: Mantissa `101011000000`, Exponent `0011`
- The mantissa begins `10`, confirming it is a normalised negative number

| Value | Binary | Normalised | Mantissa (12-bit) | Exponent (4-bit) |
|---|---|---|---|---|
| +5.25 | `101.01` | `0.10101 × 2³` | `010101000000` | `0011` |
| -5.25 | `-101.01` | `0.10101 × 2³` | `101011000000` | `0011` |

## Floating-point binary to denary

> **Spec point** — `spcpt_VCY2SgXbSzFg7VCw`

## Floating-point binary to denary

### How do you convert floating-point binary to denary?

- These examples assume a 12-bit two's complement mantissa and a 4-bit two's complement exponent

1. **Read the exponent** and convert it from two's complement to denary
2. **Check the first bit of the mantissa****: `0` = positive, `1` = negative
3. **If the mantissa is negative**, take its **two's complement** (flip the bits and add 1) to find the **magnitude** of the fraction
4. **Write the fraction** as `0`.`<fraction bits>`  and **apply the exponent** by moving the binary point (right if positive, left if negative)
5. **Apply the sign**: if the first mantissa bit was `1`, make the final result negative

#### Example (positive)

- Mantissa: 010101000000
- Exponent: 0011

- **Exponent**: `0011 = +3`
- **First bit**: `0` → positive
- **Fraction**: `0.10101`
- **Apply exponent**: `0.10101 × 2³ = 101.01₂ = 5.25`
- **Result**: `+5.25`

#### Example (negative)

- Mantissa: 101011000000
- Exponent: 0011

- **Exponent**: `0011 = +3`
- **First bit**: `1` → negative
- **Two's complement of the mantissa** to find the magnitude:

| Step | Bits |
|---|---|
| Mantissa | `101011000000` |
| Flip the bits | `010100111111` |
| Add 1 | `010101000000` |

- **Fraction (magnitude)**: `0.10101`
- **Apply exponent**: `0.10101 × 2³ = 101.01₂ = 5.25`
- **Apply sign**: negative → `−5.25`
- **Result**: `−5.25`

### Summary

| Mantissa | Exponent | Result |
|---|---|---|
| `010101000000` | `0011` | +5.25 |
| `101011000000` | `0011` | -5.25 |

> **Exam Hint**
> - The **whole mantissa is two's complement**. For a negative number (mantissa starts with `1`), take the two's complement of the mantissa to find the magnitude, then make the final answer negative.
> - **Both** the mantissa and the exponent are two's complement.
> - Quicker check: the leftmost mantissa bit carries a **negative place value**, so `1.01011 = −1 + 0.34375 = −0.65625`, then `× 2³ = −5.25`.
> - Show the working the mark scheme expects: the binary conversion, the **two's complement step for negatives**, and the exponent (the number of places the point moves).

> **Worked Example**
> Numbers are stored in two different computer systems using floating-point representation.
> 
> **System 1 uses:**
> 
> - 10 bits for the mantissa
> - 6 bits for the exponent
> - two's complement form for both the mantissa and the exponent
> 
> **System 2 uses:**
> 
> - 8 bits for the mantissa
> - 8 bits for the exponent
> - two's complement form for both the mantissa and the exponent
> 
> **Calculate **the normalised floating-point representation of 113.75 in each system. Show your working.
> 
> **[4]**
> 
> **Answer**
> 
> - Convert 113.75 to binary: `1110001.11` *(1 mark)*
> - Normalise and find the exponent: `0.111000111 × 2⁷`, so the point moves 7 places, exponent = 7 *(1 mark for evidence of exponent 7)*
> - **System 1**: exponent `7 = 000111`
> 
> | Mantissa | Exponent |
> |---|---|
> | `0111000111` | `000111` |
> 
> - **System 2**: exponent `7 = 00000111` (the mantissa is truncated to 8 bits, losing precision)
> 
> | Mantissa | Exponent |
> |---|---|
> | `01110001` | `00000111` |
