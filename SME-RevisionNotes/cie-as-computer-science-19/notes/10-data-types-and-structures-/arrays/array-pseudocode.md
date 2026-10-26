---
note_id: "rn_f6BwFHRj2mt3GbDj"
title: "Array pseudocode"
source: https://www.savemyexams.com/as/computer-science/cie/19/revision-notes/10-data-types-and-structures-/arrays/array-pseudocode
path: 10-data-types-and-structures-/arrays/array-pseudocode
updated_at: "2026-10-01T11:21:56.814Z"
spec_point_ids: ["spcpt_DTB8jjHzTdHVpnC2", "spcpt_SZCsB8JMfyN8zsRR"]
spec_point_codes: []
guided_study: false
---

# Array pseudocode

## Searching arrays

> **Spec point** — `spcpt_DTB8jjHzTdHVpnC2`

## Searching arrays

### What is a linear search?

- A linear search **starts with the first value** in a dataset and** checks every value one at a time** until all values have been checked
- A linear search can be performed **even if the values are not in order**

#### How do you perform a linear search?

| **Step** | **Instruction** |
|---|---|
| **1** | Check the first value |
| **2** | **IF **it is the value you are looking for<br><br>- STOP! |
| **3** | **ELSE **move to the next value and check |
| **4** | **REPEAT UNTIL **you have checked all values and not found the value you are looking for |

- A linear search can be used to **find elements in an array**
- Each element in the array is **checked in order**, from the **lower bound** to the **upper bound**, until the item is found or the upper bound is reached
- An example pseudocode algorithm to perform a linear search on a **1D array** could be:

- Works on a fixed-size array `List[0:4]`
- Uses a `WHILE` loop for flexibility (early exit if found)
- Clearly separates **input**, **processing**, and **output**

#### Identifier table

| **Identifier** | **Data type** | **Description** |
|---|---|---|
| `List` | ARRAY[0:4] OF INTEGER | Stores the list of numbers to search through |
| `Target` | INTEGER | The number the user wants to search for |
| `Found` | BOOLEAN | Tracks whether the target value has been found |
| `Index` | INTEGER | The current position being checked in the array |

## Sorting arrays

> **Spec point** — `spcpt_SZCsB8JMfyN8zsRR`

## Sorting arrays

### What is a bubble sort?

- A bubble sort is a simple sorting algorithm that starts at the beginning of a dataset and **checks values **in **'pairs'** and **swaps them **if they are** not in the correct order**
- One full run of comparisons from beginning to end is called a '**pass**', a bubble sort may require **multiple **'**passes**' to sort the dataset
- The algorithm is finished when there are **no more swaps to make**

### How do you perform a bubble sort?

| **Step** | **Instruction** |
|---|---|
| **1** | Compare the first two values in the dataset |
| **2** | **IF **they are in the wrong order...<br><br>- Swap them |
| **3** | Compare the next two values |
| **4** | **REPEAT **step 2 & 3 until you reach the end of the dataset (**pass 1**) |
| **5** | **IF **you have made any swaps...<br><br>- **REPEAT **from the start (pass 2,3,4...) |
| **6** | **ELSE **you have not made any swaps...<br><br>- STOP! the list is in the correct order |

#### Example

- Perform a bubble sort on the following dataset

| `5` | `2` | `4` | `1` | `6` | `3` |
|---|---|---|---|---|---|

| **Step** | **Instruction** |
|---|---|
| **1** | Compare the first two values in the dataset<br><br>\| `5` \| `2` \| `4` \| `1` \| `6` \| `3` \|<br>\|---\|---\|---\|---\|---\|---\| |
| **2** | **IF **they are in the wrong order...<br><br>- Swap them<br><br>\| `2` \| `5` \| `4` \| `1` \| `6` \| `3` \|<br>\|---\|---\|---\|---\|---\|---\| |
| **3** | Compare the next two values<br><br>\| `2` \| `5` \| `4` \| `1` \| `6` \| `3` \|<br>\|---\|---\|---\|---\|---\|---\| |
| **4** | **REPEAT **step 2 & 3 until you reach the end of the dataset<br><br>- 5 & 4 SWAP!<br><br>\| `2` \| `4` \| `5` \| `1` \| `6` \| `3` \|<br>\|---\|---\|---\|---\|---\|---\|<br><br>- 5 & 1 SWAP!<br><br>\| `2` \| `4` \| `1` \| `5` \| `6` \| `3` \|<br>\|---\|---\|---\|---\|---\|---\|<br><br>- 5 & 6 NO SWAP!<br><br>\| `2` \| `4` \| `1` \| `5` \| `6` \| `3` \|<br>\|---\|---\|---\|---\|---\|---\|<br><br>- 6 & 3 SWAP!<br><br>\| `2` \| `4` \| `1` \| `5` \| `3` \| `6` \|<br>\|---\|---\|---\|---\|---\|---\|<br><br>- End of pass 1 |
| **5** | **IF **you have made any swaps...<br><br>- **REPEAT **from the start<br>- End of pass 2 (swaps made)<br><br>\| `2` \| `1` \| `4` \| `3` \| `5` \| `6` \|<br>\|---\|---\|---\|---\|---\|---\|<br><br>- End of pass 3 (swaps made)<br><br>\| `1` \| `2` \| `3` \| `4` \| `5` \| `6` \|<br>\|---\|---\|---\|---\|---\|---\|<br><br>- End of pass 4 (no swaps)<br><br>\| `1` \| `2` \| `3` \| `4` \| `5` \| `6` \|<br>\|---\|---\|---\|---\|---\|---\| |
| **6** | **ELSE **you have not made any swaps...<br><br>- STOP! the list is in the correct order |

- A bubble sort can be used to **put elements in an array in order**
- A **pseudocode algorithm** for a bubble sort on a 1D array could be:

- Uses a **flag**, `Swapped`, in a `REPEAT ... UNTIL` loop so the sort stops after the first pass with no swaps
- Includes an **optimisation** to exit early if no swaps were made on a pass

#### Identifier table

| **Identifier** | **Data type** | **Description** |
|---|---|---|
| `Numbers` | ARRAY[0:5] OF INTEGER | Stores the list of numbers to be sorted |
| `Temp` | INTEGER | Temporary variable used for swapping two elements in the array |
| `Pass` | INTEGER | Tracks the number of passes through the array |
| `Index` | INTEGER | Tracks the current position being compared in the array |
| `Swapped` | BOOLEAN | Indicates whether a swap occurred during a pass (used to optimise sorting) |
