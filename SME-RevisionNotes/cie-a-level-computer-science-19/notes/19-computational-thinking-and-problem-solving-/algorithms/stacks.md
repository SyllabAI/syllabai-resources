---
note_id: "rn_fBfydSFTp9VpR3WJ"
title: "Stacks"
source: https://www.savemyexams.com/a-level/computer-science/cie/19/revision-notes/19-computational-thinking-and-problem-solving-/algorithms/stacks
path: 19-computational-thinking-and-problem-solving-/algorithms/stacks
updated_at: "2025-06-03T09:45:19.002Z"
spec_point_ids: ["spcpt_v76wFF6YjGffmg7S"]
spec_point_codes: []
guided_study: false
---

# Stacks

## Implementing a stack

> **Spec point** — `spcpt_v76wFF6YjGffmg7S`

## Implementing a stack

## How do you program a stack?

- To recap the main operations of stacks and how they work, read the [ADT overview](https://www.savemyexams.com/a-level/computer-science/cie/19/revision-notes/10-data-types-and-structures-/introduction-to-abstract-data-types-adt/adt-overview/)
- When programming a stack, the main operations listed below must be included in your program.
- The main operations for stacks are:

#### Main operations

| **Operation** | **Pseudocode** | **Python** | **Java** |
|---|---|---|---|
| **isEmpty()** | `FUNCTION isEmpty(s : Stack) RETURNS BOOLEAN RETURN s.top = -1 ENDFUNCTION` | `def isEmpty(self): return len(self.stack) == 0` | `stack.isEmpty();` |
| **isFull()** | `FUNCTION isFull(s : Stack) RETURNS BOOLEAN RETURN s.top = s.capacity - 1 ENDFUNCTION` | `def isFull(self): return len(self.stack) == self.capacity` | `public boolean isFull() { return top == capacity - 1; }` |
| **push(value)** | `PROCEDURE push(s : REF Stack, value : INTEGER) IF NOT isFull(s) THEN s.top ← s.top + 1 s.items[s.top] ← value ELSE OUTPUT "Stack is full" ENDIF ENDPROCEDURE` | `stack.push(1)` | `stack.push(1);` |
| **pop()** | `FUNCTION pop(s : REF Stack) RETURNS INTEGER IF NOT isEmpty(s) THEN DECLARE value : INTEGER value ← s.items[s.top] s.top ← s.top - 1 RETURN value ELSE RETURN -1 ENDIF ENDFUNCTION` | `popped_item = stack.pop()` | `int poppedItem = stack.pop();` |
| **peek()** | `FUNCTION peek(s : Stack) RETURNS INTEGER IF NOT isEmpty(s) THEN RETURN s.items[s.top] ELSE RETURN -1 ENDIF ENDFUNCTION` | `def peek(self): if not self.isEmpty(): return self.stack[-1] else: return None` | `int topItem = stack.peek();` |
| **size()** | `FUNCTION size(s : Stack) RETURNS INTEGER RETURN s.top + 1 ENDFUNCTION` | `size = len(stack)` | `int size = stack.size();` |

- In **pseudocode**, we assume a record-based stack with fields like `items`, `top`, and `capacity`
- Python uses built-in lists or a class with `.push()` and `.pop()` methods
- Java uses `Stack<E>` from `java.util.Stack`

#### Stack in operation (Pseudocode)

- **Defines a Stack structure** with a fixed-size array of 5 items, a `top` pointer, and a `capacity`
- **Initialises the stack** with `top ← -1` to indicate it is empty
- **Pushes 3 values** (`10`, `20`, `30`) onto the stack one by one:

  - Each `push` increases `top` and adds the value to the `items` array
- **Peeks** at the current top of the stack:

  - Returns `30` without removing it
- **Pops two values** off the stack:

  - First pop returns `30`, second returns `20`
  - Each `pop` decreases `top` by 1
- **Outputs the current size** of the stack:

  - After popping twice, only one value (`10`) remains → size is `1`

#### Python

#### Java

> **Worked Example**
> Study the pseudocode function `PushAnimal()`:
> 
> Write program code for the function `PushAnimal()`**[3]**
> 
> **Final answer:** **Answer**
> 
> - Function header (and close where appropriate) with parameter, checking if full (`AnimalTopPointer = 20`) **and **returning false **[1 mark]**
> - If not full, inserting parameter value into `AnimalTopPointer` **[1 mark]**
> - …incrementing pointer and returning true **[1 mark]**
> 
> Example program code:
> 
> **Java**
> 
> **VB.NET**
> 
> **Python**
