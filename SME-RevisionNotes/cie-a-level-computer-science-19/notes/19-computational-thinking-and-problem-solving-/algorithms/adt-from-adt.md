---
note_id: "rn_sQxzjzfRDHGSwHtB"
title: "ADT from ADT"
source: https://www.savemyexams.com/a-level/computer-science/cie/19/revision-notes/19-computational-thinking-and-problem-solving-/algorithms/adt-from-adt
path: 19-computational-thinking-and-problem-solving-/algorithms/adt-from-adt
updated_at: "2025-05-19T13:38:20.561Z"
spec_point_ids: ["spcpt_vct4zxppSDRnwt9H"]
spec_point_codes: []
guided_study: false
---

# ADT from ADT

## ADT from ADT

> **Spec point** — `spcpt_vct4zxppSDRnwt9H`

## ADT from ADT

## What does it mean?

- You should be able to **explain or demonstrate** how you can build one abstract data type **on top of another**
- For example:

  - A **stack** can be implemented using a **linked list**
  - A **queue** can be implemented using two **stacks**
  - A **dictionary** can be implemented using a **binary search tree**
- You’re not just limited to built-in types like arrays, you can **compose ADTs out of each other**

### What is an ADT?

- If you are unsure what an ADT is, read our[ ADT overview](https://www.savemyexams.com/a-level/computer-science/cie/19/revision-notes/10-data-types-and-structures-/introduction-to-abstract-data-types-adt/adt-overview/) page

### How are ADTs implemented?

#### Using built-in types (e.g. arrays, lists)

| ADT | Built-in type used | Example |
|---|---|---|
| Stack | List/array | Use `.append()` and `.pop()` in Python |
| Queue | List/array or circular buffer | Use `.append()` and `.pop(0)` |
| Linked list | Class with `next` fields | Implement nodes manually |
| Dictionary | Hash table (built-in `dict`) | Key-value mapping |
| Binary tree | Class with `left` and `right` | Each node links to children |

#### Using other ADTs

| ADT being built | Uses this ADT | Example |
|---|---|---|
| Queue | Two stacks | Enqueue in one stack, dequeue using a second stack |
| Stack | Linked list | Push/pop from head of list |
| Binary tree | Linked list or array | Nodes link to each other like a graph |
| Dictionary | Binary search tree | Store keys and values in BST for ordered lookup |

### Example: Implementing a Queue using Two Stacks

#### Idea:

- Use **two stacks** (let’s say `inStack` and `outStack`) to simulate a queue

#### How it works:

- `enqueue(x)` → push `x` onto `inStack`
- `dequeue()` → if `outStack` is empty, pop all items from `inStack` and push onto `outStack`, then pop from `outStack`
- This simulates **FIFO behaviour** using **LIFO operations** from stacks
