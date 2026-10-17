---
note_id: "rn_KqvdT23Ffh4cqX9d"
title: "Precision Issues"
source: https://www.savemyexams.com/a-level/computer-science/cie/19/revision-notes/13-data-representation-/floating-point-numbers-representation-and-manipulation/precision-issues
path: 13-data-representation-/floating-point-numbers-representation-and-manipulation/precision-issues
updated_at: "2025-05-13T15:00:04.913Z"
spec_point_ids: ["spcpt_CBTy9sh2hqRFjqVq"]
spec_point_codes: []
guided_study: false
---

# Precision Issues

## Approximation & rounding

> **Spec point** — `spcpt_CBTy9sh2hqRFjqVq`

## Approximation & rounding

- In computing, **real numbers** are often stored using **floating-point binary**, which has a **limited number of bits** for the mantissa and exponent
- This means not all real numbers can be represented **exactly**, only **approximated**

#### Rounding errors

- Some decimal values cannot be **precisely represented** in binary
- **Example**:

- Because memory is limited (e.g. 32 or 64 bits), the binary value must be **truncated or rounded**, which introduces **small errors**
- **Consequence**:

  - Calculations using approximated values may **accumulate errors**
  - Final results may be **slightly inaccurate**

#### Underflow

- Underflow occurs when a number is **too close to zero** to be stored in the available number of bits
- **Example**:

  - A very small number like `1.2 × 10⁻⁴⁰`
  - The exponent is too negative to be stored
  - Result: **Stored as 0**
- **Consequence:**

  - Loss of precision
  - Can affect accuracy in scientific or financial calculations

#### Overflow

- **Overflow** occurs when a number is **too large** to fit in the allocated bits for the exponent or mantissa
- **Example:**

  - A calculation produces `1.2 × 10⁵⁰`, but the maximum representable number is `1.2 × 10³⁸`
- **Consequence:**

  - Program may crash or return an **infinity**, **error**, or **wraparound value**
  - Can be especially dangerous in loops or financial applications

### Summary table

| **Issue** | **Cause** | **Effect** |
|---|---|---|
| **Rounding error** | Real number can’t be exactly represented in binary | Slight inaccuracies in results |
| **Underflow** | Number too small to be stored (exponent too negative) | Value becomes 0 |
| **Overflow** | Number too large to be stored (exponent too positive) | Incorrect result or program error |
