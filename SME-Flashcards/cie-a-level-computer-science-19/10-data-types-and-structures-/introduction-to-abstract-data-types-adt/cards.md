# Introduction to Abstract Data Types (ADT)

Course: cie-a-level-computer-science-19 · Section: 10. Data Types & Structures

Source: https://www.savemyexams.com/a-level/computer-science/cie/19/flashcards/10-data-types-and-structures-/introduction-to-abstract-data-types-adt/


## Card 1 — keyword_definition (`fl_vn7fDDyGXf9JKmrN`)

**FRONT**

Define **abstract data type (ADT)**.


**BACK**

An abstract data type is a **collection of data and a set of operations on that data**.


Spec links: `spcpt_ywfgTSkKDNwWtyth`


## Card 2 — question_and_answer (`fl_mTCRnwxF2M2xhWym`)

**FRONT**

Name three common abstract data types.


**BACK**

**Stacks**, **queues** and **linked lists**.


Spec links: `spcpt_ywfgTSkKDNwWtyth`


## Card 3 — keyword_definition (`fl_mrNJ6TJVxc2ZB5x6`)

**FRONT**

Define **stack**.


**BACK**

A stack is an abstract data type that stores data using the **Last In, First Out (LIFO)** principle.


Spec links: `spcpt_ywfgTSkKDNwWtyth`


## Card 4 — question_and_answer (`fl_G4MBvbDfr55N22g9`)

**FRONT**

What everyday object is a stack like?


**BACK**

**A pile of plates**: the last item you put on is the first one you take off.


Spec links: `spcpt_ywfgTSkKDNwWtyth`


## Card 5 — question_and_answer (`fl_gJ45PVn6qBGhsVKn`)

**FRONT**

What do PUSH and POP do?


**BACK**

**PUSH** adds an item to the **top** of the stack. **POP** removes the item from the **top**.


Spec links: `spcpt_ywfgTSkKDNwWtyth`


## Card 6 — question_and_answer (`fl_69xRpbkhgGzx5Vqn`)

**FRONT**

Name the two pointers that a stack uses.


**BACK**

A **base pointer**, which points to the first item in the stack, and a **top pointer**, which points to the last item.


Spec links: `spcpt_ywfgTSkKDNwWtyth`


## Card 7 — question_and_answer (`fl_gMRWWR8Tjgvscn32`)

**FRONT**

What happens to the pointer when data is pushed onto a stack?


**BACK**

The pointer **increments by 1**, signifying the new top of the stack.


Spec links: `spcpt_ywfgTSkKDNwWtyth`


## Card 8 — question_and_answer (`fl_zHr6TyPpCRFFpQ4n`)

**FRONT**

What happens to the pointer when data is popped from a stack?


**BACK**

The pointer **decrements by 1**, to point at the new top of the stack.


Spec links: `spcpt_ywfgTSkKDNwWtyth`


## Card 9 — keyword_definition (`fl_fd4XZHYRzp3HXt4F`)

**FRONT**

Define **stack overflow**.


**BACK**

A stack overflow is an attempt to **push an item onto a full stack**.


Spec links: `spcpt_ywfgTSkKDNwWtyth`


## Card 10 — keyword_definition (`fl_x4tXk52RdTg39sXX`)

**FRONT**

Define **stack underflow**.


**BACK**

A stack underflow is an attempt to **pop an item from an empty stack**.


Spec links: `spcpt_ywfgTSkKDNwWtyth`


## Card 11 — question_and_answer (`fl_drCRsXjx7WcXR3ht`)

**FRONT**

What does `peek()` do on a stack?


**BACK**

It **returns the top value** of the stack without removing it, after first checking that the stack is not empty.


Spec links: `spcpt_ywfgTSkKDNwWtyth`


## Card 12 — true_or_false (`fl_WydC5mDDBtPyf25d`)

**FRONT**

**True or False?**

Data that is popped is always erased from the stack.


**BACK**

**False.**

The data is **not necessarily erased**. The top pointer moves, and depending on the implementation the value may be deleted, replaced with a null value, or left to be overwritten.


Spec links: `spcpt_ywfgTSkKDNwWtyth`


## Card 13 — keyword_definition (`fl_3Bb99DRNcgSyCGM6`)

**FRONT**

Define **queue**.


**BACK**

A queue is an abstract data type that stores data **in the order it arrives**, using the **First In, First Out (FIFO)** principle.


Spec links: `spcpt_RgSwb9JrytxxJ6Cv`


## Card 14 — question_and_answer (`fl_QTvV8RrFcSNdrBCN`)

**FRONT**

What do ENQUEUE and DEQUEUE do?


**BACK**

**ENQUEUE** adds an item to the **back** of the queue. **DEQUEUE** removes the item from the **front**.


Spec links: `spcpt_RgSwb9JrytxxJ6Cv`


## Card 15 — question_and_answer (`fl_CvRtv2XbbBtt83C6`)

**FRONT**

What does `peek()` do on a queue?


**BACK**

It returns the value of the item at the **front** of the queue **without removing it** from the queue.


Spec links: `spcpt_RgSwb9JrytxxJ6Cv`


## Card 16 — keyword_definition (`fl_YnqrkF78yGSZDFx6`)

**FRONT**

Define **linear queue**.


**BACK**

A linear queue is a data structure that **consists of an array**, where items are added to the next available space and removed from the front.


Spec links: `spcpt_RgSwb9JrytxxJ6Cv`


## Card 17 — question_and_answer (`fl_54cbDkFpNQnc5SKC`)

**FRONT**

What must be checked before adding an item to a linear queue?


**BACK**

That the **queue is not full**.


Spec links: `spcpt_RgSwb9JrytxxJ6Cv`


## Card 18 — fill_in_the_blanks (`fl_pXQp5GKCmtNmyb24`)

**FRONT**

Before removing an item from a queue you must make sure that the queue is not <u>**          **</u>.


**BACK**

Before removing an item from a queue you must make sure that the queue is not **empty**.


*Blanks: 1 — answers: []*

Spec links: `spcpt_RgSwb9JrytxxJ6Cv`

Flags: blank_answer_mismatch


## Card 19 — question_and_answer (`fl_vwQYSGjQ9mDB8B8q`)

**FRONT**

What happens to the rear index pointer when an item is enqueued?


**BACK**

If the end of the array has not been reached, the **rear index pointer is incremented** and the new item is added to the queue.


Spec links: `spcpt_RgSwb9JrytxxJ6Cv`


## Card 20 — question_and_answer (`fl_yvPfkbRJhtKs9pRg`)

**FRONT**

What happens to the front pointer when an item is dequeued?


**BACK**

The item at the front of the queue is returned and the **front is incremented by 1**.


Spec links: `spcpt_RgSwb9JrytxxJ6Cv`


## Card 21 — keyword_definition (`fl_5KH6kkj7jYkGPF8c`)

**FRONT**

Define **circular queue**.


**BACK**

A circular queue is a **static array with a fixed capacity** that **reuses the empty slots** at the front of the array which are freed when items are dequeued.


Spec links: `spcpt_RgSwb9JrytxxJ6Cv`


## Card 22 — question_and_answer (`fl_8zpjQCkW84S8FRc9`)

**FRONT**

Why is a circular queue used instead of a linear queue?


**BACK**

In a linear queue it would **take time to move items up to the start** of the array to free space at the end, so a circular queue **reuses the empty slots** instead.


Spec links: `spcpt_RgSwb9JrytxxJ6Cv`


## Card 23 — question_and_answer (`fl_CJ23kqnYkcQq6sgK`)

**FRONT**

When is a circular queue full?


**BACK**

When the **next position to be used is already occupied** by the item at the front of the queue.


Spec links: `spcpt_RgSwb9JrytxxJ6Cv`


## Card 24 — question_and_answer (`fl_3qF5NHPR2vKMkSmT`)

**FRONT**

What happens when the only item in a circular queue is dequeued?


**BACK**

The **rear and front pointers are reset**.


Spec links: `spcpt_RgSwb9JrytxxJ6Cv`


## Card 25 — keyword_definition (`fl_z6H9CwtmN7fy2NPK`)

**FRONT**

Define **linked list**.


**BACK**

A linked list is an abstract data type where each item, or **node**, contains a **data field** and a **pointer to the next node** in the sequence.


Spec links: `spcpt_Y338wwMbry4QFs9p`


## Card 26 — question_and_answer (`fl_WCwHVbpnXRPDWfvX`)

**FRONT**

What two things does each node in a linked list store?


**BACK**

The **actual data**, and a **pointer to the next item** in the list.


Spec links: `spcpt_Y338wwMbry4QFs9p`


## Card 27 — fill_in_the_blanks (`fl_2DjjKsvksmvHcBs3`)

**FRONT**

In a linked list, the <u>**              **</u> field contains the address of the next item in the list.


**BACK**

In a linked list, the **pointer** field contains the address of the next item in the list.


*Blanks: 1 — answers: []*

Spec links: `spcpt_Y338wwMbry4QFs9p`

Flags: blank_answer_mismatch


## Card 28 — question_and_answer (`fl_wZygNcsvGZkh7cnt`)

**FRONT**

Where are new items usually added in a linked list?


**BACK**

To the **start** of the list.


Spec links: `spcpt_Y338wwMbry4QFs9p`


## Card 29 — question_and_answer (`fl_SBH4bh3sPnFYpvRb`)

**FRONT**

What signals that the end of a linked list has been reached?


**BACK**

The **pointer field is empty or null**.


Spec links: `spcpt_Y338wwMbry4QFs9p`


## Card 30 — question_and_answer (`fl_5MbJHDGx8PPgvMZ5`)

**FRONT**

How is a linked list traversed?


**BACK**

Check the list is not empty, start at the node the Start pointer points to, output the item at that node, then **follow the pointer to the next node**, repeating until the pointer field is empty.


Spec links: `spcpt_Y338wwMbry4QFs9p`


## Card 31 — question_and_answer (`fl_7rgv7vTM93gQyq8h`)

**FRONT**

When a node is added to a linked list, what happens to the node it follows?


**BACK**

The pointer field of that node is **updated to point to the new node**.


Spec links: `spcpt_Y338wwMbry4QFs9p`


## Card 32 — question_and_answer (`fl_vxkdS4cn9kwrCZyG`)

**FRONT**

How is a node removed from a linked list?


**BACK**

The pointer field of the **previous node is updated to bypass** the deleted node.


Spec links: `spcpt_Y338wwMbry4QFs9p`


## Card 33 — true_or_false (`fl_N82qbK5DjCMqrKCm`)

**FRONT**

**True or False?**

A removed node is erased from the linked list.


**BACK**

**False.**

The node is **not truly removed**, it is only **ignored**. This is easier, but it wastes memory.


Spec links: `spcpt_Y338wwMbry4QFs9p`


## Card 34 — question_and_answer (`fl_cG822n9Jr4bgcXkr`)

**FRONT**

Give two disadvantages of a linked list compared with an array.


**BACK**

Storing pointers means **more memory is required**, and items can **only be traversed in sequence**, so an item **cannot be directly accessed** as it can in an array.


Spec links: `spcpt_Y338wwMbry4QFs9p`

