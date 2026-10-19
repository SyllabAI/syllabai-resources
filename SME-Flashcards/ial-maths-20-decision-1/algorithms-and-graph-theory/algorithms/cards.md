# Algorithms

Course: ial-maths-20-decision-1 · Section: Algorithms & Graph Theory

Source: https://www.savemyexams.com/international-a-level/maths/edexcel/20/decision-1/flashcards/algorithms-and-graph-theory/algorithms/


## Card 1 — keyword_definition (`fl_P3QG9VNbRwRXSXcX`)

**FRONT**

Define an **algorithm**.


**BACK**

An algorithm is a set of **precise** instructions which, if followed exactly, produces the solution to a problem.

Because the instructions leave nothing to judgement, a computer or a person can carry them out without needing to understand the problem itself.


Spec links: `spcpt_8gBcbKsMFqBsThd6`


## Card 2 — question_and_answer (`fl_6cKgRqJmjcTczq5s`)

**FRONT**

In what two ways can an algorithm be presented?


**BACK**

As a **text-based algorithm**, which is a list of instructions written out in sentences and usually numbered, or as a **flow chart**, which sets the same instructions out diagrammatically.

A flow chart makes the order of the instructions visible, along with any part that has to be repeated.


Spec links: `spcpt_zhGH23vdhhw5pDX2` `spcpt_8gBcbKsMFqBsThd6`


## Card 3 — fill_in_the_blanks (`fl_NPn27j4V6w7csJwz`)

**FRONT**

Complete the meanings of the three box shapes used in a flow chart:

An **oval** marks the `\_\_\_\_\_\_` or end of the algorithm, a **rectangle** holds an `\_\_\_\_\_\_` to carry out, and a **diamond** holds a `\_\_\_\_\_\_` to answer.


**BACK**

The completed sentence is:

An **oval** marks the **start** or end of the algorithm, a **rectangle** holds an **instruction** to carry out, and a **diamond** holds a **question** to answer.

The shape tells you what kind of command you are looking at before you have read a word of it.


*Blanks: 0 — answers: ['oval', 'start', 'rectangle', 'instruction', 'diamond', 'question']*

Spec links: `spcpt_gRHgyFgW2bf6vQrK`

Flags: blank_answer_mismatch


## Card 4 — question_and_answer (`fl_vjBRfrKjH3FHbdqZ`)

**FRONT**

What kinds of instruction make a flow chart a better way to present an algorithm than a list of sentences?


**BACK**

**Conditional** instructions, such as 'is $a > b$?', where a yes sends you to one instruction and a no sends you to a different one.

Also **repetitive** parts, since a flow chart can loop an arrow back to an earlier box instead of writing the same instructions out again.


Spec links: `spcpt_gRHgyFgW2bf6vQrK`


## Card 5 — true_or_false (`fl_K9wNRT2nCvY7cwRz`)

**FRONT**

**True or False?**

An algorithm always produces the best possible solution to the problem it is applied to.


**BACK**

**False.**

Many algorithms are built to give a solution that is good enough rather than the very best one, because a real problem can be far too complex to solve exactly.

A route-finding algorithm might return a route $200$ miles longer than the shortest, and on a very long journey finding it quickly can matter more than that inaccuracy.


Spec links: `spcpt_8gBcbKsMFqBsThd6`


## Card 6 — question_and_answer (`fl_HPGCk4fR8V9bqMs7`)

**FRONT**

What do the flow chart commands 'Input', 'Let' and 'Output' each tell you to do?


**BACK**

**Input** supplies the algorithm with its starting data, **Let** assigns or updates the value of a variable, and **Output** (or Print) tells you to write the answer down.

The output has to be read off the instruction that names it, and is not simply whatever number happens to be last in your working.


Spec links: `spcpt_gRHgyFgW2bf6vQrK`


## Card 7 — question_and_answer (`fl_jb7YGNxWHTWMcvHQ`)

**FRONT**

You are asked to describe what an algorithm shown as a flow chart achieves. Where should you look first?


**BACK**

Look at the **final instructions**, and particularly at whatever the chart outputs, since that is what the whole algorithm was built to produce.

Working backwards from the output usually makes the purpose of the loop above it clear.


Spec links: `spcpt_gRHgyFgW2bf6vQrK`


## Card 8 — question_and_answer (`fl_zJV4Kv3JdxHKWFKB`)

**FRONT**

When following a flow chart, why might a column of the table of values be left mostly empty?


**BACK**

Because a value only gets a new entry on a row when the algorithm actually **changes** it.

An input such as $n$ that is never updated appears once, in the first row, and every later row leaves that column blank.


Spec links: `spcpt_gRHgyFgW2bf6vQrK`


## Card 9 — question_and_answer (`fl_RbY6jv49VsCPQFCF`)

**FRONT**

What does a sorting algorithm do?


**BACK**

A sorting algorithm arranges a list of items into **ascending** or **descending** order.

The items are usually numbers, such as weights, lengths, scores or times, but they can equally be letters or words.


Spec links: `spcpt_GhSjBXgQRgBb843c`


## Card 10 — question_and_answer (`fl_dXtqZcNx3P9rhgXm`)

**FRONT**

What happens during one pass of the bubble sort algorithm?


**BACK**

Each pair of neighbouring items on the working list is compared in turn, working from **left to right**, and the two are swapped whenever they are out of order.

A pair of **equal** items is already in order, so it is not swapped and does not add to the swap count.


Spec links: `spcpt_Vcg4PHTNDThnKgZ2`


## Card 11 — question_and_answer (`fl_8vJSC6rK97d8DqQH`)

**FRONT**

How do you know when the bubble sort algorithm is complete?


**BACK**

It is complete as soon as a **pass produces no swaps**, because that means every neighbouring pair is already in the right order.

It is also complete once only one item would be left on the working list, since a single item cannot be out of order.


Spec links: `spcpt_Vcg4PHTNDThnKgZ2`


## Card 12 — keyword_definition (`fl_RxnM7Rr6xCvxMH4V`)

**FRONT**

Define the **working list** in a bubble sort.


**BACK**

The working list is the part of the list that the next pass is actually applied to, meaning the items not yet known to be in their final place.

It starts as the whole list and loses one item after every pass, because each pass carries the largest remaining item to the end, or the smallest if the sort is descending.


Spec links: `spcpt_Vcg4PHTNDThnKgZ2`


## Card 13 — fill_in_the_blanks (`fl_htW5mG5pW7MF6Y7J`)

**FRONT**

A bubble sort is applied to a list of $n$ items. Complete the two results:

The maximum number of passes needed is `\_\_\_\_\_\_` and the greatest number of swaps possible in a single pass equals the number of `\_\_\_\_\_\_` made in that pass.


**BACK**

The completed results are:

The maximum number of passes needed is $n - 1$ and the greatest number of swaps possible in a single pass equals the number of **comparisons** made in that pass.

The whole algorithm needs the greatest number of swaps when the list starts in exactly reverse order.


*Blanks: 0 — answers: ['comparisons']*

Spec links: `spcpt_Vcg4PHTNDThnKgZ2`

Flags: blank_answer_mismatch


## Card 14 — question_and_answer (`fl_FBY5Dp56hXSN5gZx`)

**FRONT**

A bubble sort is applied to a list of $n$ items. What is the greatest number of comparisons the whole algorithm can involve?


**BACK**

The comparisons total `\left(n - 1\right) + \left(n - 2\right) + \dots + 2 + 1`, which sums to `\frac{1}{2} n \left(n - 1\right)`.

Each pass compares one fewer pair than the pass before, because the working list has just lost an item.


Spec links: `spcpt_Vcg4PHTNDThnKgZ2`


## Card 15 — true_or_false (`fl_fCYBt96nbbSvYZHY`)

**FRONT**

**True or False?**

A bubble sort can need the maximum possible number of passes even when only one item is out of place.


**BACK**

**True.**

An item sitting at the very end of the list that belongs at the very start moves only **one place closer** with each pass.

The rest of the list already being in order does nothing to speed that item up, so the sort runs to the full number of passes.


Spec links: `spcpt_Vcg4PHTNDThnKgZ2`


## Card 16 — question_and_answer (`fl_rspjbh8BxqCsd3nX`)

**FRONT**

What happens during one pass of the quick sort algorithm?


**BACK**

Every sub-list is split into two halves around a **pivot**, with the items smaller than the pivot on one side and the larger ones on the other.

For an ascending sort the smaller items go before the pivot, and within each half the items keep the order they were already in.


Spec links: `spcpt_4KvCvTtSnQnbmCpW`


## Card 17 — fill_in_the_blanks (`fl_63sP7b7rYXyvRyfx`)

**FRONT**

Complete the rule for finding the pivot in a quick sort, for a sub-list of $n$ items:

`\text{position of pivot} = \frac{\_\_\_\_\_\_}{2} \text{, rounded up}`


**BACK**

The completed rule is:

$\text{position of pivot} = \frac{n+1}{2} \text{, rounded up}$

So a sub-list of $8$ items takes its $5$th item as the pivot, since $\frac{9}{2} = 4 . 5$ rounds up to $5$.


*Blanks: 0 — answers: []*

Spec links: `spcpt_4KvCvTtSnQnbmCpW`


## Card 18 — true_or_false (`fl_4tPjcCh3nJgbZffy`)

**FRONT**

**True or False?**

In a quick sort, the pivot is found by putting the sub-list into order and then taking the middle value.


**BACK**

**False.**

The pivot is whichever item sits in the middle **position** of the sub-list as it currently stands, with no reordering at all.

Sorting the sub-list first would defeat the purpose, since sorting it is exactly what the algorithm is trying to achieve.


Spec links: `spcpt_4KvCvTtSnQnbmCpW`


## Card 19 — question_and_answer (`fl_M6YWBZ4RDYhb6xnP`)

**FRONT**

In a quick sort, where should an item equal to the pivot be placed?


**BACK**

Either side is valid, but for **consistency** always put it in the half holding the items greater than or equal to the pivot.

Keeping to one convention means your sub-lists match the expected working at every later pass.


Spec links: `spcpt_4KvCvTtSnQnbmCpW`


## Card 20 — question_and_answer (`fl_58B7SHWHbt5MbS7q`)

**FRONT**

How do you know when the quick sort algorithm is complete?


**BACK**

It is complete once **every item on the original list has been a pivot**, because an item that has served as a pivot is already in its final position.

At that point no sub-list has more than one item left in it.


Spec links: `spcpt_4KvCvTtSnQnbmCpW`


## Card 21 — question_and_answer (`fl_cQtFSSMwW754MkP3`)

**FRONT**

A pivot turns out to be the lowest item in its sub-list. What happens on that side of the pivot?


**BACK**

No new sub-list is created there, because there are no items smaller than the pivot to form one.

The next pass simply has one fewer sub-list to work on, which is why the number of pivots does not always double from one pass to the next.


Spec links: `spcpt_4KvCvTtSnQnbmCpW`


## Card 22 — keyword_definition (`fl_p4K8RvRXR59b9FVQ`)

**FRONT**

Define the **binary search algorithm**.


**BACK**

The binary search algorithm inspects an **ordered** list to decide whether a specified item is in it, and if it is, to find where it is.

The list must already be sorted for the algorithm to be used at all.


Spec links: `spcpt_Zmf4G8ptrjJTyQzz`


## Card 23 — question_and_answer (`fl_6prMRVy4yYVNyGH3`)

**FRONT**

Why must a list be in order before a binary search can be run on it?


**BACK**

Because the method works by comparing the target with a middle item and then **discarding one whole half** of the list.

That step is only valid if everything on one side of the middle item comes before it and everything on the other side comes after it, which is exactly what being ordered guarantees.


Spec links: `spcpt_Zmf4G8ptrjJTyQzz`


## Card 24 — question_and_answer (`fl_8VpzFQxMzdRT29Mf`)

**FRONT**

In a binary search, how do you find the position of the pivot in a sub-list?


**BACK**

Add the positions of the **first and last** items of the sub-list, divide by $2$, and round up if the answer is not a whole number.

For a sub-list running from position $6$ to position $8$ the pivot is therefore the $7$th item.


Spec links: `spcpt_Zmf4G8ptrjJTyQzz`


## Card 25 — question_and_answer (`fl_HjxfDrk85rsHbPq4`)

**FRONT**

A binary search begins on a list of $8$ items. Which item is compared with the target first?


**BACK**

The $5$th item, since the pivot position works out as $\frac{1+8}{2} = 4 . 5$, which rounds up to $5$.

Every binary search starts at the middle of the whole list rather than at either end of it.


Spec links: `spcpt_Zmf4G8ptrjJTyQzz`


## Card 26 — question_and_answer (`fl_xGrTHD9RBJPgXDxn`)

**FRONT**

The item being searched for comes before the pivot. What does a binary search do next?


**BACK**

It rejects the pivot and everything after it, and carries on searching only the **sub-list before** the pivot.

Had the item come after the pivot instead, the sub-list before it would have been the part rejected.


Spec links: `spcpt_Zmf4G8ptrjJTyQzz`


## Card 27 — fill_in_the_blanks (`fl_NC3R8vYrK4qjr4T7`)

**FRONT**

Complete the two ways a binary search can finish:

The search ends either when the item has been `\_\_\_\_\_\_` in the list, or when it has been shown that the item is `\_\_\_\_\_\_` there at all.


**BACK**

The completed sentence is:

The search ends either when the item has been **found** in the list, or when it has been shown that the item is **not** there at all.

The second case is reached once the sub-list has been cut down until there is nothing left that could hold the item.


*Blanks: 0 — answers: ['found', 'not']*

Spec links: `spcpt_Zmf4G8ptrjJTyQzz`

Flags: blank_answer_mismatch


## Card 28 — true_or_false (`fl_qQ6Vtjq6NP3WPvZs`)

**FRONT**

**True or False?**

A binary search can only report that an item is missing after it has compared the item with every entry in the list.


**BACK**

**False.**

Each comparison lets the search throw away roughly **half** of the items still in play, so only a handful of comparisons are needed even for a long list.

For example, a list of eight names is settled in three comparisons.


Spec links: `spcpt_Zmf4G8ptrjJTyQzz`


## Card 29 — keyword_definition (`fl_sF4cpwY8z7NK5zSF`)

**FRONT**

Define a **bin packing algorithm**.


**BACK**

A bin packing algorithm organises a collection of objects into as **few bins as possible**, where every bin is the same size.

'Size' can mean length, weight, volume or any other capacity, so the objects might be pallets loaded into lorries or lengths of cable cut from reels.


Spec links: `spcpt_gm4qdfZbrNvkCS3S`


## Card 30 — fill_in_the_blanks (`fl_DzkfSKD4zJFzgZJ7`)

**FRONT**

Complete the names of the three bin packing algorithms:

The `\_\_\_\_\_\_` algorithm, the first-fit `\_\_\_\_\_\_` algorithm, and the `\_\_\_\_\_\_` packing algorithm.


**BACK**

The completed list is:

The **first-fit** algorithm, the first-fit **decreasing** algorithm, and the **full-bin** packing algorithm.

All three pack objects into bins that are every one of them the same size.


*Blanks: 0 — answers: ['first-fit', 'decreasing', 'full-bin']*

Spec links: `spcpt_gm4qdfZbrNvkCS3S`

Flags: blank_answer_mismatch


## Card 31 — question_and_answer (`fl_dtJM4MK4J9HXKMYF`)

**FRONT**

How does the first-fit bin packing algorithm decide where each object goes?


**BACK**

Objects are taken in the **order they are presented**, and each one is put into the **first** bin that still has room for it.

A new bin is opened only when no existing bin has enough capacity left.


Spec links: `spcpt_jFw8QgmRgsYPg89c`


## Card 32 — question_and_answer (`fl_b7B538wm7KkZDBT8`)

**FRONT**

What is the main advantage of the first-fit bin packing algorithm?


**BACK**

**Speed**, because the objects do not have to be sorted into any order before the packing begins.

For many business or practical purposes a quick workable answer is worth more than the very best one.


Spec links: `spcpt_jFw8QgmRgsYPg89c`


## Card 33 — question_and_answer (`fl_x6XpQzGGCtwvxH5X`)

**FRONT**

How do you find a lower bound for the number of bins needed?


**BACK**

Divide the **total capacity of all the objects** by the **size of one bin**, then round the answer **up** to the next whole number.

A value of $4 . 85$ therefore gives a lower bound of $5$ bins, since four bins could not possibly hold everything.


Spec links: `spcpt_jFw8QgmRgsYPg89c`


## Card 34 — true_or_false (`fl_KKkKTRg2nZtBJt6v`)

**FRONT**

**True or False?**

Each of the three bin packing algorithms has its own lower bound for the number of bins.


**BACK**

**False.**

There is only one lower bound, and it depends on the objects and the bin size rather than on which method is used.

No algorithm can beat it, because the objects simply will not fit into fewer bins than that however cleverly they are arranged.


Spec links: `spcpt_gm4qdfZbrNvkCS3S`


## Card 35 — question_and_answer (`fl_GgWdqwFvG2QTnTFg`)

**FRONT**

How does the first-fit decreasing algorithm differ from the ordinary first-fit algorithm?


**BACK**

The objects are first arranged into **decreasing order**, largest first, and only then packed by the first-fit rule.

Placing the awkward large objects while every bin is still empty usually gets much closer to the optimal number of bins.


Spec links: `spcpt_sQPhN4n7HWK9DRry`


## Card 36 — question_and_answer (`fl_QvK7Rv2Mb6nt7vqJ`)

**FRONT**

A bin packing algorithm has used $5$ bins, and the lower bound is also $5$. What can you conclude?


**BACK**

The solution is **optimal**, since no arrangement at all can manage fewer than $5$ bins and this one achieves exactly that.

Matching the lower bound is the only way to be certain an answer is the best possible.


Spec links: `spcpt_sQPhN4n7HWK9DRry`


## Card 37 — question_and_answer (`fl_g4GpWqmwMq8RzSJj`)

**FRONT**

First-fit has used $6$ bins but the lower bound is $5$. Does that mean a mistake has been made?


**BACK**

No mistake need have been made, and the packing can be entirely correct.

First-fit is not guaranteed to reach the fewest possible bins, so a gap between its answer and the lower bound is an ordinary outcome rather than a sign of an error.


Spec links: `spcpt_jFw8QgmRgsYPg89c`


## Card 38 — question_and_answer (`fl_KYnp376YBWrNRR9Z`)

**FRONT**

How does the full-bin packing algorithm work?


**BACK**

Combinations of objects that **exactly fill** a bin are identified by inspection and placed together.

Whatever objects are left over are then packed using the **first-fit** algorithm.


Spec links: `spcpt_c2bwJnJzvYhj22vC`


## Card 39 — question_and_answer (`fl_BFn2wnB3cPXJGMCZ`)

**FRONT**

Full-bin packing often reaches the optimal answer. Why is it still not always the algorithm to choose?


**BACK**

Because the full-bin combinations have to be spotted by **inspection**, which becomes slow and easy to get wrong once there are many objects.

Where speed matters more than using the fewest bins, first-fit is the better choice.


Spec links: `spcpt_c2bwJnJzvYhj22vC`


## Card 40 — question_and_answer (`fl_c82cSTQ9yZBVShGf`)

**FRONT**

Two students apply the same bin packing algorithm and produce different arrangements, both using $5$ bins. Can both be right?


**BACK**

Both arrangements can be correct.

These algorithms are **heuristic**, which means they guarantee a workable answer rather than a unique one, and the full-bin method in particular can yield several different valid sets of full bins.


Spec links: `spcpt_c2bwJnJzvYhj22vC`

