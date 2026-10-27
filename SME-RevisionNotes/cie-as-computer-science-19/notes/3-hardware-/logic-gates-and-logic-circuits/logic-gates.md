---
note_id: "rn_vwtTjfrrfQFFKFNB"
title: "Logic gates"
source: https://www.savemyexams.com/as/computer-science/cie/19/revision-notes/3-hardware-/logic-gates-and-logic-circuits/logic-gates
path: 3-hardware-/logic-gates-and-logic-circuits/logic-gates
updated_at: "2026-10-01T09:23:51.614Z"
spec_point_ids: ["spcpt_qw7kMMx47FmDJjgs", "spcpt_4Dn6vThMXRCq8x22"]
spec_point_codes: []
guided_study: false
---

# Logic gates

## Logic gates

> **Spec point** — `spcpt_qw7kMMx47FmDJjgs`

## Logic gates

### What is a logic gate?

- A logic gate is a **visual way** of representing a **Boolean expression**
- The logic gates covered in this course are:

  - **AND**
  - **OR**
  - **NOT**
  - **XOR**
  - **NAND**
  - **NOR**

#### AND

| **Expression operator** | **Circuit symbol** | **Function** |
|---|---|---|
| (A **AND **B) | ![and-gate](assets/e8e6485b0912-and-gate.png) | Returns TRUE only if** both** inputs are TRUE<br><br>**TRUE **AND **TRUE **= **TRUE**<br><br>Otherwise = FALSE |

#### OR

| **Expression operator** | **Circuit symbol** | **Function** |
|---|---|---|
| (A **OR **B) | ![or-gate](assets/5b7eee70ea7c-or-gate.png) | Returns TRUE if **either** input is TRUE<br><br>**TRUE **OR **FALSE **= **TRUE**<br><br>**FALSE **OR **FALSE **= **FALSE** |

#### NOT

| **Expression operator** | **Circuit symbol** | **Function** |
|---|---|---|
| (**NOT **A) | ![not-gate](assets/7ed9b463218d-not-gate.png) | **Reverses **the input value<br><br>NOT **TRUE **= **FALSE**<br><br>NOT **FALSE **= **TRUE** |

#### XOR (exclusive OR)

| **Expression operator** | **Circuit symbol** | **Function** |
|---|---|---|
| (A **XOR** B) | ![xor](assets/9e0424c74965-screenshot-2023-05-30-at-08-25-28.png) | Returns TRUE if **either** input is TRUE but **NOT** both<br><br>**TRUE**  XOR **FALSE** = **TRUE**<br><br>**FALSE** XOR **FALSE** = **FALSE**<br><br>**TRUE** XOR **TRUE** = **FALSE** |

#### NAND (not and)

| **Expression operator** | **Circuit symbol** | **Function** |
|---|---|---|
| (A **NAND **B) | ![screenshot-2023-05-30-at-08-25-01](assets/88cbded23e3f-screenshot-2023-05-30-at-08-25-01.png) | Returns TRUE if **either or both** inputs are FALSE<br><br>**TRUE** NAND **FALSE** = **TRUE**<br><br>**FALSE** NAND **FALSE** = **TRUE**<br><br>**TRUE** NAND **TRUE** = **FALSE** |

#### NOR (not OR)

| **Expression operator** | **Circuit symbol** | **Function** |
|---|---|---|
| (A **NOR **B) | ![screenshot-2023-05-30-at-08-25-22](assets/dea8458c864e-screenshot-2023-05-30-at-08-25-22.png) | Returns TRUE if **both** inputs are FALSE<br><br>**TRUE** NOR **FALSE** = **FALSE**<br><br>**FALSE** NOR **FALSE** = **TRUE**<br><br>**TRUE** NOR **TRUE** = **FALSE** |

## Truth tables

> **Spec point** — `spcpt_4Dn6vThMXRCq8x22`

## Truth tables

### What is a truth table?

- A truth table is a **tool **used in logic and computer science to **visualise **the **results **of **Boolean expressions**
- They represent **all possible inputs** and the **associated outputs** for a **given Boolean expression**

#### AND

| **Circuit symbol** | **Truth Table** |
|---|---|
| ![screenshot-2023-05-30-at-08-24-36](assets/28bda956492e-screenshot-2023-05-30-at-08-24-36.png) | \| **A** \| **B** \| **A AND B** \|<br>\|---\|---\|---\|<br>\| 0 \| 0 \| 0 \|<br>\| 0 \| 1 \| 0 \|<br>\| 1 \| 0 \| 0 \|<br>\| 1 \| 1 \| 1 \| |

#### OR

| **Circuit symbol** | **Truth Table** |
|---|---|
| ![screenshot-2023-05-30-at-08-24-49](assets/46087ced0a82-screenshot-2023-05-30-at-08-24-49.png) | \| **A** \| **B** \| **A OR B** \|<br>\|---\|---\|---\|<br>\| 0 \| 0 \| 0 \|<br>\| 0 \| 1 \| 1 \|<br>\| 1 \| 0 \| 1 \|<br>\| 1 \| 1 \| 1 \| |

#### NOT

| **Circuit symbol** | **Truth Table** |
|---|---|
| ![screenshot-2023-05-30-at-08-24-28](assets/a35d1c8ac2f8-screenshot-2023-05-30-at-08-24-28.png) | \| **A** \| **NOT A** \|<br>\|---\|---\|<br>\| 0 \| 1 \|<br>\| 1 \| 0 \| |

#### XOR (exclusive)

| **Circuit symbol** | **Truth Table** |
|---|---|
| ![screenshot-2023-05-30-at-08-25-28](assets/9e0424c74965-screenshot-2023-05-30-at-08-25-28.png) | \| **A** \| **B** \| **A XOR B** \|<br>\|---\|---\|---\|<br>\| 0 \| 0 \| 0 \|<br>\| 0 \| 1 \| 1 \|<br>\| 1 \| 0 \| 1 \|<br>\| 1 \| 1 \| 0 \| |

#### NAND (not and)

| **Circuit symbol** | **Truth Table** |
|---|---|
| ![screenshot-2023-05-30-at-08-25-01](assets/88cbded23e3f-screenshot-2023-05-30-at-08-25-01.png) | \| **A** \| **B** \| **NOT (A AND B)** \|<br>\|---\|---\|---\|<br>\| 0 \| 0 \| 1 \|<br>\| 0 \| 1 \| 1 \|<br>\| 1 \| 0 \| 1 \|<br>\| 1 \| 1 \| 0 \| |

#### NOR (not or)

| **Circuit symbol** | **Truth Table** |
|---|---|
| ![Logic gate diagram showing a NOR gate with two input lines on the left and one output line on the right with a small circle.](assets/dea8458c864e-screenshot-2023-05-30-at-08-25-22.png) | \| **A** \| **B** \| **NOT (A OR B)** \|<br>\|---\|---\|---\|<br>\| 0 \| 0 \| 1 \|<br>\| 0 \| 1 \| 0 \|<br>\| 1 \| 0 \| 0 \|<br>\| 1 \| 1 \| 0 \| |
