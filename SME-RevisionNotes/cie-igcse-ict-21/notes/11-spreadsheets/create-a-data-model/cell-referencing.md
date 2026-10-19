---
note_id: "rn_DqjzY9PXhjjJQ8Km"
title: "Cell Referencing"
source: https://www.savemyexams.com/igcse/ict/cie/21/revision-notes/11-spreadsheets/create-a-data-model/cell-referencing
path: 11-spreadsheets/create-a-data-model/cell-referencing
updated_at: "2024-05-16T14:08:29.060Z"
spec_point_ids: ["spcpt_CcDDQ67qdqwpvVpW", "spcpt_mG3CvrFX2DwjmnD5"]
spec_point_codes: []
guided_study: false
---

# Cell Referencing

## Relative

> **Spec point** — `spcpt_CcDDQ67qdqwpvVpW`

## Relative

### What is an relative cell reference?

- A relative cell reference means that when a formula is copied** the cell reference can change**
- The reference is** relative to the cell** containing the formula
- It is the **default cell referencing** used in spreadsheets

**Example**

- Consider the following example spreadsheet:

|   | **A** | **B** | **C** |
|---|---|---|---|
| **1** | 10 | 20 |   |
| **2** | 5 | 15 |   |

- When you copy a formula that includes a relative cell reference, spreadsheet software **adjusts the reference** relative to the new location
- For example, if you copy the formula **"=A1+B1**" from cell **C1** to **C2**, the formula will adjust to "**=A2+B2**"

#### What are the benefits of relative cell references?

- Relative cell references** saves time** by automatically adjusting references when being copied, **improving efficiency**
- Relative cell references are **flexible **and allow users to create formulas that can be **used on a range of data**

## Absolute

> **Spec point** — `spcpt_mG3CvrFX2DwjmnD5`

## Absolute

### What is an absolute cell reference?

- An absolute cell reference means that when a formula is copied **the cell reference does not change**
- Absolute cell references are fixed **using the \$ symbol**

**Example**

- Consider the following example spreadsheet:

|   | **A** | **B** | **C** |
|---|---|---|---|
| **1** | 10 | 20 |   |
| **2** | 5 | 15 |   |

- If you input the formula "**=A1+B1**" in cell **C1** and drag the fill handle down to copy the formula to cell **C2**, the formula in **C2 **will change to "**=A2+B2**"
- But if you input the formula "**=\$A\$1+B1**" in cell **C1** and drag the fill handle down, the formula in C2 will still refer to cell A1: "**=\$A\$1+B2**"

#### What are the benefits of absolute cell references?

- Absolute cell reference **provide consistency** in a spreadsheet, for example:

  - **Calculations using a tax rate (fixed) that you want consistently applied across the spreadsheet**
- Absolute cell references **provide clarity **in formulas, they become **easier to understand**
