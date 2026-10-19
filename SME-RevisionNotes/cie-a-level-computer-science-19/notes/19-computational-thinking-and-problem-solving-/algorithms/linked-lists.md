---
note_id: "rn_YgH6RTm5QZ8HN85W"
title: "Linked Lists"
source: https://www.savemyexams.com/a-level/computer-science/cie/19/revision-notes/19-computational-thinking-and-problem-solving-/algorithms/linked-lists
path: 19-computational-thinking-and-problem-solving-/algorithms/linked-lists
updated_at: "2025-06-03T13:29:16.951Z"
spec_point_ids: ["spcpt_HvnjNStCybDJDHFz"]
spec_point_codes: []
guided_study: false
---

# Linked Lists

## Linked lists

> **Spec point** — `spcpt_HvnjNStCybDJDHFz`

## Linked lists

## How do you program a linked list?

- To recap the main operations of linked lists and how they work, read our [ADT Overview](https://www.savemyexams.com/a-level/computer-science/cie/19/revision-notes/10-data-types-and-structures-/introduction-to-abstract-data-types-adt/adt-overview/) page
- To program a Linked List you must be able to perform the following operations:

  - **Create a linked list**
  - **Traverse a linked list**
  - **Add data to a linked list**
  - **Remove data from a linked list**

### Create a linked list

- Define the class called ‘Node’ that represents a node in the linked list.
- Each node has 2 fields ‘fruit’ (this stores the fruit value) and ‘next’ (this stores a reference to the next node in the list)
- We create 3 nodes and assign fruit values to each node
- To establish a connection between the nodes we set the ‘next’ field of each node to the appropriate next node

| **Pseudocode** |
|---|
|   |

| **Python** |
|---|
|   |

| **Java** |
|---|
|   |

## Algorithm to traverse a linked list

- We traverse the linked list starting from ‘node1’. We output the fruit value of each node and update the ‘current’ reference to the next node until we reach the end of the list

| **Pseudocode** |
|---|
|   |

| **Python** |
|---|
| `# Traverse the linked list`<br><br>`current = node1`<br><br>`while current is not None:`<br><br>`    print(current.fruit)`<br><br>`    current = current.next` |

| **Java** |
|---|
| `// Traverse the linked list`<br><br>`current = node1;`<br><br>`while (current != null) {`<br><br>`System.out.println(current.fruit);`<br><br>`      current = current.next;` |

## Algorithm to add data to a linked list

- We create a new node with the new data and check if the list is empty
- If it isn’t, we find the last node and add the new node to the end

| **Pseudocode** |
|---|
|   |

| **Python** |
|---|
| `# Add "orange" to the end of the linked list`<br>`new_node = Node("orange")`<br><br>`if node1 is None:`<br>`    # If the list was empty, make "orange" the head`<br>`    node1 = new_node`<br>`else:`<br>`    # Find the last node and append "orange" to it`<br>`    current = node1`<br>`    while current.next is not None:`<br>`        current = current.next`<br>`    current.next = new_node` |

| **Java** |
|---|
| `// Add "orange" to the end of the linked list`<br>`Node new_node = new Node("orange");`<br><br>`if (node1 == null) {`<br>`// If the list was empty, make "orange" the head`<br>`node1 = new_node;`<br>`} else {`<br>`// Find the last node and append "orange" to it`<br>`      current = node1;`<br>`      while (current.next != null) {`<br>`      current = current.next;`<br>`      }`<br>`      current.next = new_node;`<br><br>`}` |

## Algorithm to remove data from a linked list

- We traverse the list until we find the data to be removed
- If the data to be removed is the first node, we update the head, else we update the node before to bypass the data to be removed

| **Pseudocode** |
|---|
|   |

| **Python** |
|---|
| `# Find and remove "apple"`<br><br>`while current is not None:`<br><br>`    if current.fruit == "apple":`<br><br>`        if previous is None:`<br><br>`            # If "apple" is the first node, update the head`<br><br>`            node1 = current.next`<br><br>`        else:`<br><br>`            # Remove the node by updating the previous node's next pointer`<br><br>`            previous.next = current.next`<br><br>`        break`<br><br>`    previous = current`<br><br>`    current = current.next` |

| **Java** |
|---|
| `// Find and remove "apple"`<br><br>` while (current != null) {`<br><br>`  if (current.fruit.equals("apple")) {`<br><br>`if (previous == null) {`<br><br>`              // If "apple" is the first node, update the head`<br><br>`              node1 = current.next;`<br><br>`             } else {`<br><br>`              // Remove the node by updating the previous node's next pointer`<br><br>`              previous.next = current.next;`<br><br>`              }`<br><br>`              break;`<br><br>`           }`<br><br>`previous = current;`<br><br>`      current = current.next;`<br><br>`    }` |

> **Worked Example**
> The following diagram represents an Abstract Data Type (ADT) for a linked list.
> 
> ![Flowchart of rectangular boxes connected by arrows showing sequence: A to C to D to E, ending in Ø. Each box represents a step in a process.](assets/fa03c3ac227b-43855-2025-06-03-0o3-kleki.png)
> 
> The free list is as follows:
> 
> ![Flowchart showing a series of connected boxes with arrows. The last box contains the symbol Ø, indicating an end or null operation.](assets/8611e23676b6-50240-2025-06-03-0o3-kleki-1.png)
> 
> Explain how a node containing data value B is added to the list in alphabetic sequence.**[4]**
> 
> **Final answer:** **Answer**
> 
> **One mark per point**
> 
> 1. Check for a free node **[1 mark]**
> 2. Search for correct insertion point **[1 mark]**
> 3. Assign data value B to first node in free list / node pointed to by start pointer of free list **[1 mark]**
> 4. Pointer from A will be changed to point to node containing B (instead of C) **[1 mark]**
> 5. Pointer from B will be changed to point to node containing C **[1 mark]**
> 6. Start pointer in free list moved to point to next free node  **[1 mark]**
