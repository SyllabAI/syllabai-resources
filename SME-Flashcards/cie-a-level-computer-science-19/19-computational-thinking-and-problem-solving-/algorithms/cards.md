# Algorithms

Course: cie-a-level-computer-science-19 · Section: 19. Computational thinking & Problem-solving

Source: https://www.savemyexams.com/a-level/computer-science/cie/19/flashcards/19-computational-thinking-and-problem-solving-/algorithms/


## Card 1 — keyword_definition (`fl_VptQjj2285kgRrdH`)

**FRONT**

Define **linear search**.


**BACK**

A standard algorithm used to find elements in an **unordered list**, searching **sequentially and systematically from the start to the end**, one element at a time.


Spec links: `spcpt_Dmcr2fSnqYKTJzgH`


## Card 2 — fill_in_the_blanks (`fl_Yxjbg7dFxGvSb9Tk`)

**FRONT**

In a linear search the list is searched <u>**                        **</u> and systematically from the start to the end.


**BACK**

In a linear search the list is searched **sequentially** and systematically from the start to the end.


*Blanks: 1 — answers: []*

Spec links: `spcpt_Dmcr2fSnqYKTJzgH`

Flags: blank_answer_mismatch


## Card 3 — question_and_answer (`fl_wwkw2BhvkCsM9n69`)

**FRONT**

Does a linear search need a sorted list?


**BACK**

**No.** It works on an **unordered list**.


Spec links: `spcpt_Dmcr2fSnqYKTJzgH`


## Card 4 — true_or_false (`fl_GWv856vfKHSytcmC`)

**FRONT**

**True or False?**

A linear search requires the list to be sorted.


**BACK**

**False.**

A linear search works on an **unordered list**.


Spec links: `spcpt_Dmcr2fSnqYKTJzgH`


## Card 5 — question_and_answer (`fl_bKfdtHgVnrDs4csF`)

**FRONT**

What does a linear search do with each element?


**BACK**

It **compares each element** to the value being searched for.


Spec links: `spcpt_Dmcr2fSnqYKTJzgH`


## Card 6 — question_and_answer (`fl_vwjbgKnZgDKTVF55`)

**FRONT**

What happens if the value is found?


**BACK**

The algorithm **outputs where it was found in the list**.


Spec links: `spcpt_Dmcr2fSnqYKTJzgH`


## Card 7 — question_and_answer (`fl_tcqWXGxk8Wd75bFX`)

**FRONT**

What happens if the value is not found?


**BACK**

It **outputs a message stating that the value is not in the list**.


Spec links: `spcpt_Dmcr2fSnqYKTJzgH`


## Card 8 — question_and_answer (`fl_SKszYbwKFwtgq5JM`)

**FRONT**

Give an example use of a linear search.


**BACK**

Looking for a **specific student name in a list**, or searching for an item in a shopping list.


Spec links: `spcpt_Dmcr2fSnqYKTJzgH`


## Card 9 — question_and_answer (`fl_942Xx9rnStKQfBp2`)

**FRONT**

What is the worst case time complexity of a linear search?


**BACK**

**O(n)**


Spec links: `spcpt_Dmcr2fSnqYKTJzgH`


## Card 10 — question_and_answer (`fl_Ss5nXspPNp3PgpMn`)

**FRONT**

What is the best case time complexity of a linear search, and when does it occur?


**BACK**

**O(1)**, when the item is found on the **first comparison**.


Spec links: `spcpt_Dmcr2fSnqYKTJzgH`


## Card 11 — true_or_false (`fl_SrzYxSgtJ26zfBt6`)

**FRONT**

**True or False?**

The best case for a linear search is O(n).


**BACK**

**False.**

The **best case is O(1)**, where the item is found on the first comparison. **O(n) is the worst case**.


Spec links: `spcpt_Dmcr2fSnqYKTJzgH`


## Card 12 — question_and_answer (`fl_z5jRksb5VmPxS7qP`)

**FRONT**

What is the average case time complexity of a linear search?


**BACK**

**O(n/2)**, which after removing coefficients is still **O(n)**.


Spec links: `spcpt_Dmcr2fSnqYKTJzgH`


## Card 13 — question_and_answer (`fl_JmmpFMRxwrStYY6K`)

**FRONT**

Why does the linear term dominate the constant term in Big-O?


**BACK**

**Linear time dominates constant time.** The constant term and coefficients contribute significantly less as the input size n grows larger.


Spec links: `spcpt_Dmcr2fSnqYKTJzgH`


## Card 14 — question_and_answer (`fl_BHwtCtWXbBspPkVN`)

**FRONT**

What does the `linearSearch` function return?


**BACK**

The **index** of the item if it is found, or **-1** if it is not.


Spec links: `spcpt_Dmcr2fSnqYKTJzgH`


## Card 15 — fill_in_the_blanks (`fl_GKnxcxQDYwBgKs49`)

**FRONT**

If the item is not found, the linear search returns <u>**        **</u>.


**BACK**

If the item is not found, the linear search returns **-1**.


*Blanks: 1 — answers: []*

Spec links: `spcpt_Dmcr2fSnqYKTJzgH`

Flags: blank_answer_mismatch


## Card 16 — question_and_answer (`fl_4Z2D9mpDn4tVfXsd`)

**FRONT**

In the linear search pseudocode, which three variables are initialised, and to what?


**BACK**

`index` to **-1**, `i` to **0**, and `found` to **FALSE**.


Spec links: `spcpt_Dmcr2fSnqYKTJzgH`


## Card 17 — question_and_answer (`fl_nhqWRCdR4rK2ySCt`)

**FRONT**

Write the loop condition used in the linear search.


**BACK**

`WHILE i < LENGTH(list) AND found = FALSE`


Spec links: `spcpt_Dmcr2fSnqYKTJzgH`


## Card 18 — question_and_answer (`fl_mtWkbrZXP4Vf5sYs`)

**FRONT**

What happens when a match is found?


**BACK**

`index ← i` saves the current index, and `found ← TRUE` stops the search.


Spec links: `spcpt_Dmcr2fSnqYKTJzgH`


## Card 19 — question_and_answer (`fl_XqdtnvdPTJkG9KBV`)

**FRONT**

Why is the `found` flag used?


**BACK**

To **stop the search** once the item has been found, rather than checking the rest of the list.


Spec links: `spcpt_Dmcr2fSnqYKTJzgH`


## Card 20 — keyword_definition (`fl_wj63RpNXVC5Z9y2Y`)

**FRONT**

Define **binary search**.


**BACK**

A binary search **compares the middle item to the target item**, halving the search space with each step. It is more efficient than a linear search.


Spec links: `spcpt_k4NdKwZVJ4bP3VDK`


## Card 21 — question_and_answer (`fl_qQjGHdWwjbYZYxYN`)

**FRONT**

What must be true of the list for a binary search to work?


**BACK**

The **list must be sorted**.


Spec links: `spcpt_k4NdKwZVJ4bP3VDK`


## Card 22 — true_or_false (`fl_vnHJcpw7R6yfDhXF`)

**FRONT**

**True or False?**

A binary search works on an unsorted list.


**BACK**

**False.**

The **list must be sorted** for a binary search to work correctly.


Spec links: `spcpt_k4NdKwZVJ4bP3VDK`


## Card 23 — question_and_answer (`fl_gf4dxnTGjpwVvWqd`)

**FRONT**

What happens if the middle value matches the target?


**BACK**

The **index is returned**.


Spec links: `spcpt_k4NdKwZVJ4bP3VDK`


## Card 24 — question_and_answer (`fl_dvdRKBksx9yDvXd2`)

**FRONT**

What happens if the target is less than the middle value?


**BACK**

The **top half is ignored**.


Spec links: `spcpt_k4NdKwZVJ4bP3VDK`


## Card 25 — question_and_answer (`fl_yGwCSrRxF7S628zC`)

**FRONT**

What happens if the target is larger than the middle value?


**BACK**

The **bottom half is ignored**.


Spec links: `spcpt_k4NdKwZVJ4bP3VDK`


## Card 26 — true_or_false (`fl_jrgC55zTZTNVFTkp`)

**FRONT**

**True or False?**

A binary search deletes the half of the list it discards.


**BACK**

**False.**

It **does not discard, delete or remove** parts of the list. It only **adjusts the start, end and mid pointers**, which gives the appearance that items have been removed.


Spec links: `spcpt_k4NdKwZVJ4bP3VDK`


## Card 27 — fill_in_the_blanks (`fl_7J3fd9PyrHQBcJyp`)

**FRONT**

A binary search only adjusts the start, end and <u>**        **</u> pointers.


**BACK**

A binary search only adjusts the start, end and **mid** pointers.


*Blanks: 1 — answers: []*

Spec links: `spcpt_k4NdKwZVJ4bP3VDK`

Flags: blank_answer_mismatch


## Card 28 — question_and_answer (`fl_YVwzVGCVdCHsZZz3`)

**FRONT**

When does the binary search stop searching?


**BACK**

When the **item is found**, or when the item is shown **not to be in the list**.


Spec links: `spcpt_k4NdKwZVJ4bP3VDK`


## Card 29 — question_and_answer (`fl_5F8DH3d6VPSprkyg`)

**FRONT**

What is the time complexity of a binary search?


**BACK**

**O(log n)**, because it **halves the search space** with each iteration of the loop.


Spec links: `spcpt_k4NdKwZVJ4bP3VDK`


## Card 30 — fill_in_the_blanks (`fl_cDkvGbfqb59JfKct`)

**FRONT**

A binary search is an example of <u>**                      **</u> time complexity.


**BACK**

A binary search is an example of **logarithmic** time complexity.


*Blanks: 1 — answers: []*

Spec links: `spcpt_k4NdKwZVJ4bP3VDK`

Flags: blank_answer_mismatch


## Card 31 — keyword_definition (`fl_F2Kw5X57qTMPdy7V`)

**FRONT**

Define **divide and conquer**.


**BACK**

An approach where a problem is **progressively reduced in size**, so that when each problem is at its smallest it is easiest to solve.


Spec links: `spcpt_k4NdKwZVJ4bP3VDK`


## Card 32 — question_and_answer (`fl_n7TTzJTmsSG3Wq6Z`)

**FRONT**

How many items remain after i iterations of a binary search?


**BACK**

**n divided by 2 to the power i**. The algorithm starts with n items, then n/2, then n/4, then n/8, and so on.


Spec links: `spcpt_k4NdKwZVJ4bP3VDK`


## Card 33 — question_and_answer (`fl_Gmc9cvY9PRgSgjbh`)

**FRONT**

What is the best case time complexity of a binary search, and when?


**BACK**

**O(1)**, where the item is found on the **first comparison**.


Spec links: `spcpt_k4NdKwZVJ4bP3VDK`


## Card 34 — question_and_answer (`fl_HPcTK6XzG4YmxzNG`)

**FRONT**

What is the average case time complexity of a binary search?


**BACK**

**O(log n / 2)**, which after removing coefficients is still **O(log n)**.


Spec links: `spcpt_k4NdKwZVJ4bP3VDK`


## Card 35 — question_and_answer (`fl_cxtz2rBWSQR5YHgS`)

**FRONT**

Why is the rounding of the midpoint flexible?


**BACK**

**Rounding up or down are both valid**, provided the **same rounding is used consistently** throughout the algorithm.


Spec links: `spcpt_k4NdKwZVJ4bP3VDK`


## Card 36 — question_and_answer (`fl_Pxp8V3n2Gb5SKY9T`)

**FRONT**

What does the `binarySearch` function return?


**BACK**

The **index** of the item if it is found, or **-1** if it is not found.


Spec links: `spcpt_k4NdKwZVJ4bP3VDK`


## Card 37 — question_and_answer (`fl_mRWRtsYrkRssrmXC`)

**FRONT**

In the binary search pseudocode, what are `start` and `end` initialised to?


**BACK**

`start` to **0**, and `end` to `**LENGTH(list) - 1**`.


Spec links: `spcpt_k4NdKwZVJ4bP3VDK`


## Card 38 — question_and_answer (`fl_gk8z5P353tPd8BP3`)

**FRONT**

Write the loop condition used in the binary search.


**BACK**

`WHILE start <= end AND found = FALSE`


Spec links: `spcpt_k4NdKwZVJ4bP3VDK`


## Card 39 — question_and_answer (`fl_ZcBW4VvGDgpH7CcY`)

**FRONT**

How is the middle index calculated in the binary search pseudocode?


**BACK**

`mid ← (start + end) DIV 2`


Spec links: `spcpt_k4NdKwZVJ4bP3VDK`


## Card 40 — question_and_answer (`fl_WrrpCmqSCzKfyj6N`)

**FRONT**

What happens if `list[mid]` is less than the item?


**BACK**

`start ← mid + 1`, which searches the **right half**.


Spec links: `spcpt_k4NdKwZVJ4bP3VDK`


## Card 41 — question_and_answer (`fl_KsRyrpZ7hNqFr8P6`)

**FRONT**

What happens if `list[mid]` is greater than the item?


**BACK**

`end ← mid - 1`, which searches the **left half**.


Spec links: `spcpt_k4NdKwZVJ4bP3VDK`


## Card 42 — question_and_answer (`fl_5dhv7DxyKCGtkYjc`)

**FRONT**

When does the binary search loop end?


**BACK**

When the item is **found**, or when the **search range becomes invalid**.


Spec links: `spcpt_k4NdKwZVJ4bP3VDK`


## Card 43 — keyword_definition (`fl_CV4TTmjNphNrzXwj`)

**FRONT**

Define **bubble sort**.


**BACK**

A bubble sort puts items into order **smallest to largest**, by **comparing pairs of elements and swapping them if they are out of order**.


Spec links: `spcpt_GKFVVHVJpwRgY6XY`


## Card 44 — question_and_answer (`fl_qBNnsDXFd8WdKQ6f`)

**FRONT**

Which pairs are compared during a pass?


**BACK**

The first to the second, the second to the third, and so on, until the **second to last is compared to the last**.


Spec links: `spcpt_GKFVVHVJpwRgY6XY`


## Card 45 — keyword_definition (`fl_vWsGBXkjFn9j7SwK`)

**FRONT**

Define **pass** in a bubble sort.


**BACK**

A pass is one complete run of comparisons **through the list**.


Spec links: `spcpt_GKFVVHVJpwRgY6XY`


## Card 46 — question_and_answer (`fl_ks7N8ZpR2GkwQRPw`)

**FRONT**

What is true at the end of a pass?


**BACK**

The **value at the top of the list is now in order**, and the sort **resets back to the start of the list** to sort the next largest value.


Spec links: `spcpt_GKFVVHVJpwRgY6XY`


## Card 47 — question_and_answer (`fl_VG6NC6pqWfzxxS3n`)

**FRONT**

Why does each pass get shorter?


**BACK**

Because after each pass the **previously sorted final value is in order** and does not need to be rechecked.


Spec links: `spcpt_GKFVVHVJpwRgY6XY`


## Card 48 — question_and_answer (`fl_6sBKtwy7k8SbTbRD`)

**FRONT**

How does a bubble sort know it has finished?


**BACK**

A **final pass checks all elements**, and if **no swaps are made** the sort is complete.


Spec links: `spcpt_GKFVVHVJpwRgY6XY`


## Card 49 — fill_in_the_blanks (`fl_7yWffSvWBqXZVXkC`)

**FRONT**

A bubble sort is complete when a final pass makes <u>**        **</u> swaps.


**BACK**

A bubble sort is complete when a final pass makes **no** swaps.


*Blanks: 1 — answers: []*

Spec links: `spcpt_GKFVVHVJpwRgY6XY`

Flags: blank_answer_mismatch


## Card 50 — question_and_answer (`fl_CgxJkDmW6MqHqZMX`)

**FRONT**

Give an example use of a bubble sort.


**BACK**

Sorting an array of **names into alphabetical order**, or sorting an array of **student marks** from a test.


Spec links: `spcpt_GKFVVHVJpwRgY6XY`


## Card 51 — question_and_answer (`fl_NWpHcqwRGhw9WX6S`)

**FRONT**

What is the worst case time complexity of a bubble sort?


**BACK**

**O(n squared)**


Spec links: `spcpt_GKFVVHVJpwRgY6XY`


## Card 52 — question_and_answer (`fl_YXyXvnHNMpDVQCPc`)

**FRONT**

What is the best case for a bubble sort, and when does it occur?


**BACK**

**O(n)**, for an **already sorted list**, since each item must still be compared to check it is in order.


Spec links: `spcpt_GKFVVHVJpwRgY6XY`


## Card 53 — true_or_false (`fl_B5GXvVmmhmYp9gj5`)

**FRONT**

**True or False?**

The best case for a bubble sort is O(n squared).


**BACK**

**False.**

The **best case is O(n)** for an already sorted list. **O(n squared) is the worst case**.


Spec links: `spcpt_GKFVVHVJpwRgY6XY`


## Card 54 — question_and_answer (`fl_tb5NK7fr445t92Ph`)

**FRONT**

What is the average case for a bubble sort?


**BACK**

**O(n squared / 2)** for an almost sorted list, which after removing coefficients is still **O(n squared)**.


Spec links: `spcpt_GKFVVHVJpwRgY6XY`


## Card 55 — question_and_answer (`fl_m6ct5zT8xTpwbJ7d`)

**FRONT**

What is the space complexity of a bubble sort, and why?


**BACK**

**O(1)**, because it operates **in-place**, requiring only a fixed amount of memory for loop counters and a temporary swap variable.


Spec links: `spcpt_GKFVVHVJpwRgY6XY`


## Card 56 — fill_in_the_blanks (`fl_7F79CGQvTv53VFsc`)

**FRONT**

A bubble sort operates <u>**                **</u>, requiring only a fixed amount of memory.


**BACK**

A bubble sort operates **in-place**, requiring only a fixed amount of memory.


*Blanks: 1 — answers: []*

Spec links: `spcpt_GKFVVHVJpwRgY6XY`

Flags: blank_answer_mismatch


## Card 57 — true_or_false (`fl_xZjH3ZyXJzyfNGFx`)

**FRONT**

**True or False?**

A bubble sort needs extra memory proportional to the size of the list.


**BACK**

**False.**

It has space complexity **O(1)**, because it sorts **in-place**.


Spec links: `spcpt_GKFVVHVJpwRgY6XY`


## Card 58 — question_and_answer (`fl_VJdyChKPHS5M7q9W`)

**FRONT**

In the bubble sort pseudocode, what does `last` store?


**BACK**

The **length of the list**.


Spec links: `spcpt_GKFVVHVJpwRgY6XY`


## Card 59 — question_and_answer (`fl_qmQRCWm39bMwdJkM`)

**FRONT**

In the bubble sort pseudocode, what does `i` track?


**BACK**

The **number of completed passes**.


Spec links: `spcpt_GKFVVHVJpwRgY6XY`


## Card 60 — question_and_answer (`fl_5zByFRCzkcwyW42D`)

**FRONT**

What is the `swap` variable used for?


**BACK**

It is a **boolean flag** used to check whether any swaps occurred during a pass.


Spec links: `spcpt_GKFVVHVJpwRgY6XY`


## Card 61 — question_and_answer (`fl_FyxRmfYYGRFnRsmz`)

**FRONT**

Why is `swap` set to TRUE before the main loop begins?


**BACK**

To **assume a swap will happen**, so that the loop is entered at least once.


Spec links: `spcpt_GKFVVHVJpwRgY6XY`


## Card 62 — question_and_answer (`fl_dKGSDxB7pmSFmSNM`)

**FRONT**

Write the main WHILE condition of the bubble sort.


**BACK**

`WHILE i < (last - 1) AND swap = TRUE`


Spec links: `spcpt_GKFVVHVJpwRgY6XY`


## Card 63 — question_and_answer (`fl_6ds4vFvkkcCVSQ47`)

**FRONT**

What is `swap` set to at the start of each pass?


**BACK**

**FALSE**


Spec links: `spcpt_GKFVVHVJpwRgY6XY`


## Card 64 — question_and_answer (`fl_CPT8FZz2txTHTh5y`)

**FRONT**

What range does the inner FOR loop cover?


**BACK**

From index **0 to **`**last - i - 2**`, which is the unsorted part of the list.


Spec links: `spcpt_GKFVVHVJpwRgY6XY`


## Card 65 — question_and_answer (`fl_V8SPbghkpDVjWkHQ`)

**FRONT**

Write the three lines that perform the swap in a bubble sort.


**BACK**

`temp ← list[j]`, then `list[j] ← list[j + 1]`, then `list[j + 1] ← temp`


Spec links: `spcpt_GKFVVHVJpwRgY6XY`


## Card 66 — question_and_answer (`fl_PG5tVdvyq5KXpgCj`)

**FRONT**

What happens after the inner loop completes?


**BACK**

`i` is **incremented**, which shortens the range checked on the next pass.


Spec links: `spcpt_GKFVVHVJpwRgY6XY`


## Card 67 — question_and_answer (`fl_3YHYb7NBQ39Cbydf`)

**FRONT**

In an efficient bubble sort, what does reducing the Boundary each pass achieve?


**BACK**

It **shortens the range checked** on each subsequent pass, because the end of the list is already sorted.


Spec links: `spcpt_GKFVVHVJpwRgY6XY`


## Card 68 — keyword_definition (`fl_hq75crzj2mS4bnGN`)

**FRONT**

Define **insertion sort**.


**BACK**

An insertion sort **sorts one item at a time** by **placing it in the correct position** of an unsorted list, repeating until all items are in the correct position.


Spec links: `spcpt_wMSzdkRTKsHsZcZ6`


## Card 69 — fill_in_the_blanks (`fl_Yrykr3pjx95Fw9NB`)

**FRONT**

The insertion sort places each item in the correct position of an <u>**                **</u> list.


**BACK**

The insertion sort places each item in the correct position of an **unsorted** list.


*Blanks: 1 — answers: []*

Spec links: `spcpt_wMSzdkRTKsHsZcZ6`

Flags: blank_answer_mismatch


## Card 70 — question_and_answer (`fl_GZvnRwZNVNCNcktn`)

**FRONT**

What is the current item compared to?


**BACK**

**Each previous item** in the list.


Spec links: `spcpt_wMSzdkRTKsHsZcZ6`


## Card 71 — question_and_answer (`fl_9WTXRFJbstP586d6`)

**FRONT**

What happens if the current item is smaller than the previous item?


**BACK**

The **previous item is moved to the right** and the **current item takes its place**.


Spec links: `spcpt_wMSzdkRTKsHsZcZ6`


## Card 72 — question_and_answer (`fl_fWyc8k3H3fMN4DVn`)

**FRONT**

What happens if the current item is larger than the previous item?


**BACK**

It is already in the **correct position**, and the next item is then sorted.


Spec links: `spcpt_wMSzdkRTKsHsZcZ6`


## Card 73 — question_and_answer (`fl_sr9C9R7KgXGm6XHy`)

**FRONT**

When does the insertion sort process stop?


**BACK**

When **all items are in the correct position**.


Spec links: `spcpt_wMSzdkRTKsHsZcZ6`


## Card 74 — question_and_answer (`fl_DVzkvZvR4FX9FhM2`)

**FRONT**

What is the worst case time complexity of an insertion sort?


**BACK**

**O(n squared)**


Spec links: `spcpt_wMSzdkRTKsHsZcZ6`


## Card 75 — question_and_answer (`fl_G6yvYzhsYNDPyNTd`)

**FRONT**

What is the best case for an insertion sort, and when?


**BACK**

**O(n)**, for an **already sorted list**, where each item is checked one at a time.


Spec links: `spcpt_wMSzdkRTKsHsZcZ6`


## Card 76 — question_and_answer (`fl_MHqP47q7rj9xkvTY`)

**FRONT**

What is the average case for an insertion sort?


**BACK**

**O(n squared / 2)** for a half sorted list, which after removing coefficients is still **O(n squared)**.


Spec links: `spcpt_wMSzdkRTKsHsZcZ6`


## Card 77 — question_and_answer (`fl_qPV3GVpXybhtqvzT`)

**FRONT**

What is the space complexity of an insertion sort, and why?


**BACK**

**O(1)**, because the insertion sort **requires no additional space**.


Spec links: `spcpt_wMSzdkRTKsHsZcZ6`


## Card 78 — true_or_false (`fl_6qjqtsyKp55D8mkb`)

**FRONT**

**True or False?**

An insertion sort needs a second array to hold the sorted items.


**BACK**

**False.**

It **requires no additional space**, so its space complexity is **O(1)**.


Spec links: `spcpt_wMSzdkRTKsHsZcZ6`


## Card 79 — question_and_answer (`fl_ZmXTqX74RdfPtCqD`)

**FRONT**

At which index does an insertion sort start, and why?


**BACK**

Index **1**, not 0, because the **first item is considered already sorted**.


Spec links: `spcpt_wMSzdkRTKsHsZcZ6`


## Card 80 — true_or_false (`fl_9FXmJ8qhtPPxBN5b`)

**FRONT**

**True or False?**

An insertion sort starts at index 0.


**BACK**

**False.**

It starts at index **1**, because the item at index 0 is considered already sorted.


Spec links: `spcpt_wMSzdkRTKsHsZcZ6`


## Card 81 — question_and_answer (`fl_XY9xf63kZ3W8Tz7D`)

**FRONT**

In the insertion sort pseudocode, what does `item` store?


**BACK**

The **current value to be positioned**.


Spec links: `spcpt_wMSzdkRTKsHsZcZ6`


## Card 82 — question_and_answer (`fl_VwkZWJCT4ctVcB5H`)

**FRONT**

In the insertion sort pseudocode, what does `position` track?


**BACK**

**Where **`**item**`** should go** in the sorted portion of the list.


Spec links: `spcpt_wMSzdkRTKsHsZcZ6`


## Card 83 — question_and_answer (`fl_cSTsQ9QRkCcrwnsT`)

**FRONT**

Write the outer FOR loop of the insertion sort.


**BACK**

`FOR i ← 1 TO n - 1`


Spec links: `spcpt_wMSzdkRTKsHsZcZ6`


## Card 84 — question_and_answer (`fl_Syy6WnkM5mvD7m3D`)

**FRONT**

Write the inner WHILE condition of the insertion sort.


**BACK**

`WHILE position > 0 AND list[position - 1] > item`


Spec links: `spcpt_wMSzdkRTKsHsZcZ6`


## Card 85 — question_and_answer (`fl_8nxmq8649CGXf5BZ`)

**FRONT**

What does the inner WHILE loop do?


**BACK**

It **shifts elements in the sorted portion to the right** while they are greater than `item`.


Spec links: `spcpt_wMSzdkRTKsHsZcZ6`


## Card 86 — fill_in_the_blanks (`fl_bjtdWwbvmz2G2WzX`)

**FRONT**

In an insertion sort, elements greater than the item are <u>**              **</u> to the right.


**BACK**

In an insertion sort, elements greater than the item are **shifted** to the right.


*Blanks: 1 — answers: []*

Spec links: `spcpt_wMSzdkRTKsHsZcZ6`

Flags: blank_answer_mismatch


## Card 87 — question_and_answer (`fl_Cj3NvDTZ6G69PPK4`)

**FRONT**

Name the two conditions that stop the inner loop.


**BACK**

The **start of the list is reached** (`position = 0`), or the **correct spot is found** (`list[position - 1] <= item`).


Spec links: `spcpt_wMSzdkRTKsHsZcZ6`


## Card 88 — question_and_answer (`fl_Gks2Mwjv4vjnxVvq`)

**FRONT**

What happens after the inner loop finishes?


**BACK**

`list[position] ← item` **inserts the value in its correct position**.


Spec links: `spcpt_wMSzdkRTKsHsZcZ6`


## Card 89 — question_and_answer (`fl_ck7HPrC2Bpsrrd4p`)

**FRONT**

An insertion sort runs on [5, 9, 4, 2, ...].

What is the list after the pass at i = 2?


**BACK**

**[4, 5, 9, 2, ...]**. The value 4 is shifted in front of both 9 and 5.


Spec links: `spcpt_wMSzdkRTKsHsZcZ6`


## Card 90 — question_and_answer (`fl_r77B3kVxbDRD3k6W`)

**FRONT**

Name the six main stack operations.


**BACK**

`isEmpty()`, `isFull()`, `push(value)`, `pop()`, `peek()` and `size()`.


Spec links: `spcpt_v76wFF6YjGffmg7S`


## Card 91 — question_and_answer (`fl_7SJdGRrPMsqTKJyP`)

**FRONT**

What three fields does a record-based stack have?


**BACK**

`items`, `top` and `capacity`.


Spec links: `spcpt_v76wFF6YjGffmg7S`


## Card 92 — fill_in_the_blanks (`fl_3HVbQhTKCVRVywVv`)

**FRONT**

In pseudocode, a stack is assumed to be <u>**            **</u>-based, with items, top and capacity fields.


**BACK**

In pseudocode, a stack is assumed to be **record**-based, with items, top and capacity fields.


*Blanks: 1 — answers: []*

Spec links: `spcpt_v76wFF6YjGffmg7S`

Flags: blank_answer_mismatch


## Card 93 — question_and_answer (`fl_cNzzknSs6Sm8vRkB`)

**FRONT**

What is `top` set to for an empty stack?


**BACK**

**-1**


Spec links: `spcpt_v76wFF6YjGffmg7S`


## Card 94 — true_or_false (`fl_SjBrr2xx847jtGDP`)

**FRONT**

**True or False?**

A stack's top pointer is 0 when the stack is empty.


**BACK**

**False.**

It is **-1** when empty, which is why `size` is calculated as `top + 1`.


Spec links: `spcpt_v76wFF6YjGffmg7S`


## Card 95 — question_and_answer (`fl_47Ftxsdm2Zzfjxms`)

**FRONT**

Write the body of the `isEmpty` function for a stack.


**BACK**

`RETURN s.top = -1`


Spec links: `spcpt_v76wFF6YjGffmg7S`


## Card 96 — question_and_answer (`fl_P38m8JxBpg6FjJ7X`)

**FRONT**

Write the body of the `isFull` function for a stack.


**BACK**

`RETURN s.top = s.capacity - 1`


Spec links: `spcpt_v76wFF6YjGffmg7S`


## Card 97 — question_and_answer (`fl_wJ6gQQJ4QH2NKhBJ`)

**FRONT**

What are the two steps of a push?


**BACK**

**Increment **`**top**`, then **assign the value** to `s.items[s.top]`.


Spec links: `spcpt_v76wFF6YjGffmg7S`


## Card 98 — fill_in_the_blanks (`fl_wbyBTrPp9ksvXDfQ`)

**FRONT**

A push must check the stack is not <u>**        **</u> before adding a value.


**BACK**

A push must check the stack is not **full** before adding a value.


*Blanks: 1 — answers: []*

Spec links: `spcpt_v76wFF6YjGffmg7S`

Flags: blank_answer_mismatch


## Card 99 — question_and_answer (`fl_znJRJWmwGZwpMT3p`)

**FRONT**

What happens if you push onto a full stack?


**BACK**

It outputs **"Stack is full"**.


Spec links: `spcpt_v76wFF6YjGffmg7S`


## Card 100 — question_and_answer (`fl_yZcGK56xd7X6yscb`)

**FRONT**

What are the steps of a pop?


**BACK**

**Read **`**s.items[s.top]**` into a value, then **decrement **`**top**`, then **return the value**.


Spec links: `spcpt_v76wFF6YjGffmg7S`


## Card 101 — question_and_answer (`fl_pQfmbqFPj7frkhFf`)

**FRONT**

What does `pop()` return if the stack is empty?


**BACK**

**-1**


Spec links: `spcpt_v76wFF6YjGffmg7S`


## Card 102 — question_and_answer (`fl_kkpDDDQCtCW2f5Zc`)

**FRONT**

What does `peek()` do?


**BACK**

It **returns **`**s.items[s.top]**`** without removing it**, provided the stack is not empty.


Spec links: `spcpt_v76wFF6YjGffmg7S`


## Card 103 — true_or_false (`fl_FdXgKvWtsgPbCQrh`)

**FRONT**

**True or False?**

`peek()` removes the top value from the stack.


**BACK**

**False.**

`peek()` **returns the top value without removing it**. It is `pop()` that removes.


Spec links: `spcpt_v76wFF6YjGffmg7S`


## Card 104 — question_and_answer (`fl_GsKmM2v56r7drxWp`)

**FRONT**

How is the size of a stack calculated?


**BACK**

`RETURN s.top + 1`


Spec links: `spcpt_v76wFF6YjGffmg7S`


## Card 105 — question_and_answer (`fl_RYzth2ggyBGTQZhQ`)

**FRONT**

Why is the size `top + 1`?


**BACK**

Because `top` is a **zero-based index**, and it is **-1** when the stack is empty.


Spec links: `spcpt_v76wFF6YjGffmg7S`


## Card 106 — question_and_answer (`fl_HkGVDzR86pQTQbbV`)

**FRONT**

10, 20 and 30 are pushed onto an empty stack.

What does `peek()` return?


**BACK**

**30**, the value at the top of the stack.


Spec links: `spcpt_v76wFF6YjGffmg7S`


## Card 107 — question_and_answer (`fl_hYSG6vVhpZvsHcBt`)

**FRONT**

10, 20 and 30 are pushed, then two values are popped.

What is the size of the stack?


**BACK**

**1**. The pops return 30 then 20, leaving only 10.


Spec links: `spcpt_v76wFF6YjGffmg7S`


## Card 108 — question_and_answer (`fl_gz9zQWWC4Rk8YhQm`)

**FRONT**

In the `PushAnimal()` example, what is checked first?


**BACK**

Whether the stack is **full**, using `IF AnimalTopPointer = 20`.


Spec links: `spcpt_v76wFF6YjGffmg7S`


## Card 109 — question_and_answer (`fl_mgj7GtrXW8WnfhqF`)

**FRONT**

What does `PushAnimal()` return if the stack is full?


**BACK**

**FALSE**


Spec links: `spcpt_v76wFF6YjGffmg7S`


## Card 110 — question_and_answer (`fl_WqmPpFsqc3tDwPjZ`)

**FRONT**

What three things does `PushAnimal()` do if there is room?


**BACK**

**Inserts the value** at `Animal[AnimalTopPointer]`, **increments the pointer**, and **returns TRUE**.


Spec links: `spcpt_v76wFF6YjGffmg7S`


## Card 111 — keyword_definition (`fl_TJByXCj9y9vrdhkd`)

**FRONT**

Define **queue** as an ADT.


**BACK**

A queue is a **linear ADT** that follows the **First In, First Out (FIFO)** principle.


Spec links: `spcpt_qK9fpwfrvpwWk2r8`


## Card 112 — fill_in_the_blanks (`fl_Z7hVZN45fHczJSc4`)

**FRONT**

A queue is a <u>**            **</u> ADT that follows the First In, First Out principle.


**BACK**

A queue is a **linear** ADT that follows the First In, First Out principle.


*Blanks: 1 — answers: []*

Spec links: `spcpt_qK9fpwfrvpwWk2r8`

Flags: blank_answer_mismatch


## Card 113 — true_or_false (`fl_4K7mkFgpXvW7cBbn`)

**FRONT**

**True or False?**

A queue follows the Last In, First Out principle.


**BACK**

**False.**

A queue is **First In, First Out (FIFO)**. It is a **stack** that is Last In, First Out.


Spec links: `spcpt_qK9fpwfrvpwWk2r8`


## Card 114 — question_and_answer (`fl_9KB9RCJ22W3CG487`)

**FRONT**

Name the five main queue operations.


**BACK**

**Enqueue**, **dequeue**, **peek or front**, **isEmpty** and **isFull**.


Spec links: `spcpt_qK9fpwfrvpwWk2r8`


## Card 115 — question_and_answer (`fl_RmfN5qdWj66fXvsn`)

**FRONT**

What does enqueue do?


**BACK**

**Adds an item to the back** of the queue.


Spec links: `spcpt_qK9fpwfrvpwWk2r8`


## Card 116 — question_and_answer (`fl_PPs8CqgZ5q75995f`)

**FRONT**

What does dequeue do?


**BACK**

**Removes an item from the front** of the queue.


Spec links: `spcpt_qK9fpwfrvpwWk2r8`


## Card 117 — question_and_answer (`fl_hdvSSJrwqzcZ5QfX`)

**FRONT**

What does peek do on a queue?


**BACK**

**Looks at the front item without removing it**.


Spec links: `spcpt_qK9fpwfrvpwWk2r8`


## Card 118 — question_and_answer (`fl_JQS7G7GGnK9nnKn7`)

**FRONT**

Which fields does the circular queue record use?


**BACK**

`items`, `front`, `rear`, `size` and `capacity`.


Spec links: `spcpt_qK9fpwfrvpwWk2r8`


## Card 119 — question_and_answer (`fl_XjNNnhWwRCsv8VKX`)

**FRONT**

Write the line that advances the rear pointer on enqueue.


**BACK**

`q.rear ← (q.rear + 1) MOD q.capacity`


Spec links: `spcpt_qK9fpwfrvpwWk2r8`


## Card 120 — question_and_answer (`fl_8Y7h6Pw4Qk275VVw`)

**FRONT**

Why is MOD used on the queue pointers?


**BACK**

So the pointer **wraps around** to the start of the array, which is what makes the queue circular.


Spec links: `spcpt_qK9fpwfrvpwWk2r8`


## Card 121 — fill_in_the_blanks (`fl_nX8nynVxyk6DKjqn`)

**FRONT**

The MOD operator makes the pointer <u>**        **</u> around to the start of the array.


**BACK**

The MOD operator makes the pointer **wrap** around to the start of the array.


*Blanks: 1 — answers: []*

Spec links: `spcpt_qK9fpwfrvpwWk2r8`

Flags: blank_answer_mismatch


## Card 122 — question_and_answer (`fl_WFvpyGrPf5zFWnpy`)

**FRONT**

What three things does enqueue do when the queue is not full?


**BACK**

**Advances **`**rear**`, **stores the item** at `q.items[q.rear]`, and **increments **`**size**`.


Spec links: `spcpt_qK9fpwfrvpwWk2r8`


## Card 123 — question_and_answer (`fl_KMsRxchHDywJzfGB`)

**FRONT**

What does enqueue output if the queue is full?


**BACK**

**"Queue is full"**


Spec links: `spcpt_qK9fpwfrvpwWk2r8`


## Card 124 — question_and_answer (`fl_GggW7z6XVmh2y5RS`)

**FRONT**

What does dequeue do when the queue is not empty?


**BACK**

Reads `q.items[q.front]` into a value, **advances **`**front**` using MOD, **decrements **`**size**`, and **returns the value**.


Spec links: `spcpt_qK9fpwfrvpwWk2r8`


## Card 125 — true_or_false (`fl_Jn4NQcmW4GfrQQFM`)

**FRONT**

**True or False?**

In a circular queue, dequeue physically shifts every remaining item forward.


**BACK**

**False.**

It only **advances the front pointer**, using MOD to wrap around the array.


Spec links: `spcpt_qK9fpwfrvpwWk2r8`


## Card 126 — question_and_answer (`fl_Nj75Z6Bt88jwHk6Z`)

**FRONT**

What does dequeue return if the queue is empty?


**BACK**

**"Queue is empty"**


Spec links: `spcpt_qK9fpwfrvpwWk2r8`


## Card 127 — question_and_answer (`fl_KGDBytqgcZZ46fpb`)

**FRONT**

Write the body of the `isEmpty` function for a queue.


**BACK**

`RETURN q.size = 0`


Spec links: `spcpt_qK9fpwfrvpwWk2r8`


## Card 128 — question_and_answer (`fl_bwyYQrdF8dpFwr4M`)

**FRONT**

Write the body of the `isFull` function for a queue.


**BACK**

`RETURN q.size = q.capacity`


Spec links: `spcpt_qK9fpwfrvpwWk2r8`


## Card 129 — question_and_answer (`fl_NZzGwFTyYwdvCj3h`)

**FRONT**

How does the find function search a circular queue?


**BACK**

It performs a **linear search**, starting at `q.front` and stepping forward with `pos ← (pos + 1) MOD q.capacity` for `q.size` items.


Spec links: `spcpt_qK9fpwfrvpwWk2r8`


## Card 130 — question_and_answer (`fl_q3FhM9PdKDPnwJMc`)

**FRONT**

What does the find function return?


**BACK**

**TRUE** if the target is found, otherwise **FALSE**.


Spec links: `spcpt_qK9fpwfrvpwWk2r8`


## Card 131 — question_and_answer (`fl_cfYBn7RSBc5XWh8v`)

**FRONT**

Why does find loop only `q.size` times rather than `q.capacity`?


**BACK**

Because only `**size**`** items are actually in the queue**, even though the array has `capacity` slots.


Spec links: `spcpt_qK9fpwfrvpwWk2r8`


## Card 132 — question_and_answer (`fl_Kx44C7MDpCgBY6gK`)

**FRONT**

Name the four operations you must be able to program on a linked list.


**BACK**

**Create** a linked list, **traverse** it, **add data** to it, and **remove data** from it.


Spec links: `spcpt_HvnjNStCybDJDHFz`


## Card 133 — question_and_answer (`fl_h2z3bNzTMrQ8JQVp`)

**FRONT**

What two fields does a linked list Node class have?


**BACK**

A **data field**, for example `fruit`, and a `**next**`** field** storing a reference to the next node in the list.


Spec links: `spcpt_HvnjNStCybDJDHFz`


## Card 134 — fill_in_the_blanks (`fl_MQwnG8GZxFNRDqdM`)

**FRONT**

In a linked list, the `next` field stores a <u>**                  **</u> to the next node.


**BACK**

In a linked list, the `next` field stores a **reference** to the next node.


*Blanks: 1 — answers: []*

Spec links: `spcpt_HvnjNStCybDJDHFz`

Flags: blank_answer_mismatch


## Card 135 — question_and_answer (`fl_rZRs2Wy2DgxR29Ss`)

**FRONT**

How is a connection between nodes established?


**BACK**

By setting the `**next**`** field of each node to the appropriate next node**.


Spec links: `spcpt_HvnjNStCybDJDHFz`


## Card 136 — question_and_answer (`fl_2qvCfGW89tbppwf2`)

**FRONT**

What is the `next` field of the last node set to?


**BACK**

**NULL**


Spec links: `spcpt_HvnjNStCybDJDHFz`


## Card 137 — question_and_answer (`fl_vV5km27n28Ym3STD`)

**FRONT**

How do you traverse a linked list?


**BACK**

Start at the **head**, **output the current node's value**, then **set **`**current**`** to **`**current.next**`, repeating until `current` is NULL.


Spec links: `spcpt_HvnjNStCybDJDHFz`


## Card 138 — question_and_answer (`fl_2VB3BgkfKfRGPKZJ`)

**FRONT**

Write the traversal loop condition for a linked list.


**BACK**

`WHILE current != NULL`


Spec links: `spcpt_HvnjNStCybDJDHFz`


## Card 139 — fill_in_the_blanks (`fl_tpBzhRkYzHRh8Zj9`)

**FRONT**

Traversal of a linked list stops when `current` becomes <u>**        **</u>.


**BACK**

Traversal of a linked list stops when `current` becomes **NULL**.


*Blanks: 1 — answers: []*

Spec links: `spcpt_HvnjNStCybDJDHFz`

Flags: blank_answer_mismatch


## Card 140 — question_and_answer (`fl_Qx9whck25vZ8qJjy`)

**FRONT**

What is the first step in adding a node to the end of a linked list?


**BACK**

**Create a new node** with the new data, and set its `next` field to NULL.


Spec links: `spcpt_HvnjNStCybDJDHFz`


## Card 141 — question_and_answer (`fl_kCc8rXTSkbKCdg5x`)

**FRONT**

What is checked before appending a node?


**BACK**

Whether the **list is empty**, that is `IF node1 = NULL`.


Spec links: `spcpt_HvnjNStCybDJDHFz`


## Card 142 — question_and_answer (`fl_H8csxnfcb5sqzCGS`)

**FRONT**

What happens if the list is empty when adding a node?


**BACK**

The **new node becomes the head** of the list.


Spec links: `spcpt_HvnjNStCybDJDHFz`


## Card 143 — question_and_answer (`fl_QV9msRMqmDgGwRwn`)

**FRONT**

How do you find the end of a linked list?


**BACK**

Traverse with `WHILE current.next != NULL`, then set `current.next` to the new node.


Spec links: `spcpt_HvnjNStCybDJDHFz`


## Card 144 — question_and_answer (`fl_JygWCJYYnPjVKjjv`)

**FRONT**

Which two pointers does the removal algorithm track?


**BACK**

`current` and `previous`.


Spec links: `spcpt_HvnjNStCybDJDHFz`


## Card 145 — question_and_answer (`fl_qcHVt2n8rKNjjZnK`)

**FRONT**

What happens when the node to remove is at the head?


**BACK**

`previous` is NULL, so the **head is updated** to `current.next`.


Spec links: `spcpt_HvnjNStCybDJDHFz`


## Card 146 — true_or_false (`fl_Whv82P7CzVc8MJVF`)

**FRONT**

**True or False?**

The head of a linked list never changes.


**BACK**

**False.**

If the node being removed is **at the head**, the head is updated to `current.next`.


Spec links: `spcpt_HvnjNStCybDJDHFz`


## Card 147 — question_and_answer (`fl_WTm43vmbbvCyRC6c`)

**FRONT**

What happens when the node to remove is not at the head?


**BACK**

`previous.next` is set to `current.next`, which **bypasses the node**.


Spec links: `spcpt_HvnjNStCybDJDHFz`


## Card 148 — true_or_false (`fl_BWX4RHc4VwZPFr7w`)

**FRONT**

**True or False?**

Removing a node from a linked list requires shifting the remaining nodes.


**BACK**

**False.**

It only **updates the previous node's pointer to bypass** the removed node.


Spec links: `spcpt_HvnjNStCybDJDHFz`


## Card 149 — question_and_answer (`fl_FNhyFGKdrNWTYtkN`)

**FRONT**

What happens immediately after a node is removed?


**BACK**

The loop **breaks**, so no further nodes are checked.


Spec links: `spcpt_HvnjNStCybDJDHFz`


## Card 150 — question_and_answer (`fl_p8HRPqbsgyWDMZvv`)

**FRONT**

How do the pointers advance if no match is found?


**BACK**

`previous ← current`, then `current ← current.next`.


Spec links: `spcpt_HvnjNStCybDJDHFz`


## Card 151 — question_and_answer (`fl_dtXps4k3yK4CF2Bb`)

**FRONT**

A node containing B is inserted into a linked list in alphabetic order.

What is the first step?


**BACK**

**Check for a free node**.


Spec links: `spcpt_HvnjNStCybDJDHFz`


## Card 152 — question_and_answer (`fl_F2h2YFQjJffFcgkV`)

**FRONT**

A node containing B is inserted in alphabetic order.

What is the second step?


**BACK**

**Search for the correct insertion point**.


Spec links: `spcpt_HvnjNStCybDJDHFz`


## Card 153 — question_and_answer (`fl_cvmhnF2m7BXxBsGD`)

**FRONT**

When inserting a new value, where is the data value assigned?


**BACK**

To the **first node in the free list**, that is the node pointed to by the free list's start pointer.


Spec links: `spcpt_HvnjNStCybDJDHFz`


## Card 154 — question_and_answer (`fl_6N8jJwCYQT7Vbfp4`)

**FRONT**

B is inserted between A and C.

Which two pointers change?


**BACK**

The pointer from **A is changed to point to B** instead of C, and the pointer from **B points to C**.


Spec links: `spcpt_HvnjNStCybDJDHFz`


## Card 155 — question_and_answer (`fl_RXPQ49WGtdDdN7dV`)

**FRONT**

What happens to the free list after an insertion?


**BACK**

Its **start pointer moves to point to the next free node**.


Spec links: `spcpt_HvnjNStCybDJDHFz`


## Card 156 — keyword_definition (`fl_k9JFjwvWdc7vKSJ4`)

**FRONT**

Define **binary tree**.


**BACK**

A binary tree is a **rooted tree** where every node has a **maximum of 2 nodes**.


Spec links: `spcpt_hRhHmbZxSpFB7chR`


## Card 157 — true_or_false (`fl_HdrJp3PWCcCndb3C`)

**FRONT**

**True or False?**

A node in a binary tree can have three children.


**BACK**

**False.**

Every node in a binary tree has a **maximum of 2**.


Spec links: `spcpt_hRhHmbZxSpFB7chR`


## Card 158 — question_and_answer (`fl_JXtcCGPzgmScnVzH`)

**FRONT**

What is a binary tree essentially?


**BACK**

A **graph**, and it can therefore be implemented in the same way.


Spec links: `spcpt_hRhHmbZxSpFB7chR`


## Card 159 — question_and_answer (`fl_K6v4TGrGBhNgVgSr`)

**FRONT**

What is the most common way to represent a binary tree?


**BACK**

By storing each node with a **left and right pointer**.


Spec links: `spcpt_hRhHmbZxSpFB7chR`


## Card 160 — question_and_answer (`fl_Y4rMWHYQKWbbqnZJ`)

**FRONT**

Name the three things you must be able to do with a tree.


**BACK**

**Traverse** the tree data structure, **add new data** to a tree, and **remove data** from a tree.


Spec links: `spcpt_hRhHmbZxSpFB7chR`


## Card 161 — keyword_definition (`fl_zBp8RvvbdWJPdV84`)

**FRONT**

Define **node**.


**BACK**

An **item in a tree**.


Spec links: `spcpt_hRhHmbZxSpFB7chR`


## Card 162 — keyword_definition (`fl_NbqNRcCQ43qQBFP9`)

**FRONT**

Define **edge**.


**BACK**

An edge **connects two nodes together**, and is also known as a branch or pointer.


Spec links: `spcpt_hRhHmbZxSpFB7chR`


## Card 163 — keyword_definition (`fl_pMqFfbzfYZDrFqcw`)

**FRONT**

Define **root**.


**BACK**

A **single node which does not have any incoming nodes**.


Spec links: `spcpt_hRhHmbZxSpFB7chR`


## Card 164 — fill_in_the_blanks (`fl_6FWYFZBsNQGg6Xjj`)

**FRONT**

A root is a single node which does not have any <u>**                **</u> nodes.


**BACK**

A root is a single node which does not have any **incoming** nodes.


*Blanks: 1 — answers: []*

Spec links: `spcpt_hRhHmbZxSpFB7chR`

Flags: blank_answer_mismatch


## Card 165 — keyword_definition (`fl_87K2nD8hGD425n2r`)

**FRONT**

Define **child**.


**BACK**

A node **with incoming edges**.


Spec links: `spcpt_hRhHmbZxSpFB7chR`


## Card 166 — keyword_definition (`fl_GzxB2z6yTGtSYJzn`)

**FRONT**

Define **parent**.


**BACK**

A node **with outgoing edges**.


Spec links: `spcpt_hRhHmbZxSpFB7chR`


## Card 167 — question_and_answer (`fl_hBzgqN7whydtrw8Y`)

**FRONT**

What is the difference between a parent and a child, in terms of edges?


**BACK**

A **parent has outgoing edges**. A **child has incoming edges**.


Spec links: `spcpt_hRhHmbZxSpFB7chR`


## Card 168 — keyword_definition (`fl_hTDy24kzYKqYDSWM`)

**FRONT**

Define **leaf**.


**BACK**

A node **with no children**.


Spec links: `spcpt_hRhHmbZxSpFB7chR`


## Card 169 — true_or_false (`fl_dxPPJfNMMSBVqHRh`)

**FRONT**

**True or False?**

A leaf node has outgoing edges.


**BACK**

**False.**

A leaf is a node **with no children**, so it has no outgoing edges.


Spec links: `spcpt_hRhHmbZxSpFB7chR`


## Card 170 — keyword_definition (`fl_tGVbk4X3Vtc7jJDX`)

**FRONT**

Define **subtree**.


**BACK**

A **subsection of a tree**, consisting of a parent and all the children of that parent.


Spec links: `spcpt_hRhHmbZxSpFB7chR`


## Card 171 — keyword_definition (`fl_xZxf6hdyC8gGk9Z3`)

**FRONT**

Define **traversing**.


**BACK**

The process of **visiting each node in a tree data structure, exactly once**.


Spec links: `spcpt_hRhHmbZxSpFB7chR`


## Card 172 — fill_in_the_blanks (`fl_7j8SNKnJMGFrFz5M`)

**FRONT**

Traversing is the process of visiting each node in a tree <u>**              **</u> once.


**BACK**

Traversing is the process of visiting each node in a tree **exactly** once.


*Blanks: 1 — answers: []*

Spec links: `spcpt_hRhHmbZxSpFB7chR`

Flags: blank_answer_mismatch


## Card 173 — question_and_answer (`fl_cBwTMSgdtZhXS3gJ`)

**FRONT**

What does a pre-order traversal output first?


**BACK**

The **value of the current node**, before visiting any of its children.


Spec links: `spcpt_hRhHmbZxSpFB7chR`


## Card 174 — question_and_answer (`fl_ZcCTpMnTTTHM7nZQ`)

**FRONT**

What is the base case of a recursive tree traversal?


**BACK**

`IF node = NULL THEN RETURN`


Spec links: `spcpt_hRhHmbZxSpFB7chR`


## Card 175 — question_and_answer (`fl_5mZQ85PmKnzTbVwj`)

**FRONT**

When removing a child by value, what does the procedure do?


**BACK**

It **searches the parent's children for a matching value**, **removes the first match**, and then returns.


Spec links: `spcpt_hRhHmbZxSpFB7chR`


## Card 176 — question_and_answer (`fl_2NDh6b2QyGSgdkwV`)

**FRONT**

What is the limitation of that removal procedure?


**BACK**

It **only removes the first matching child** from the **direct children** of a node. Removing nodes anywhere in the tree would need a **recursive version**.


Spec links: `spcpt_hRhHmbZxSpFB7chR`


## Card 177 — question_and_answer (`fl_FKVtR4mqsv5CCGsZ`)

**FRONT**

What does 'ADT from ADT' mean?


**BACK**

Being able to **explain or demonstrate how one abstract data type can be built on top of another**.


Spec links: `spcpt_vct4zxppSDRnwt9H`


## Card 178 — question_and_answer (`fl_hzq3JNKrf7snpmz5`)

**FRONT**

Give three examples of an ADT built from another ADT.


**BACK**

A **stack from a linked list**, a **queue from two stacks**, and a **dictionary from a binary search tree**.


Spec links: `spcpt_vct4zxppSDRnwt9H`


## Card 179 — true_or_false (`fl_FBmdzPQTqRN962pJ`)

**FRONT**

**True or False?**

An ADT can only be implemented using built-in types.


**BACK**

**False.**

You are **not limited to built-in types**. ADTs can be **composed out of each other**.


Spec links: `spcpt_vct4zxppSDRnwt9H`


## Card 180 — question_and_answer (`fl_mC5y9gC6yBdC4RVP`)

**FRONT**

Which built-in type implements a stack?


**BACK**

A **list or array**, using push and pop operations.


Spec links: `spcpt_vct4zxppSDRnwt9H`


## Card 181 — question_and_answer (`fl_mFrxQGbzmzgsJchv`)

**FRONT**

Which built-in types implement a queue?


**BACK**

A **list or array**, or a **circular buffer**.


Spec links: `spcpt_vct4zxppSDRnwt9H`


## Card 182 — question_and_answer (`fl_6rfPFRY4bzpHtQrt`)

**FRONT**

How is a linked list implemented from built-in types?


**BACK**

As a **class with **`**next**`** fields**, implementing the nodes manually.


Spec links: `spcpt_vct4zxppSDRnwt9H`


## Card 183 — question_and_answer (`fl_VrCfj5Z8F72VxHX9`)

**FRONT**

Which built-in type implements a dictionary?


**BACK**

A **hash table**, giving key-value mapping.


Spec links: `spcpt_vct4zxppSDRnwt9H`


## Card 184 — question_and_answer (`fl_Djknw9yXnSh4fzWp`)

**FRONT**

How is a binary tree implemented from built-in types?


**BACK**

As a **class with **`**left**`** and **`**right**`** fields**, where each node links to its children.


Spec links: `spcpt_vct4zxppSDRnwt9H`


## Card 185 — question_and_answer (`fl_Xf3bK6crhsDrQdhr`)

**FRONT**

How can a stack be built from a linked list?


**BACK**

**Push and pop from the head of the list**.


Spec links: `spcpt_vct4zxppSDRnwt9H`


## Card 186 — question_and_answer (`fl_465F7vr7tjXzm5Zf`)

**FRONT**

How can a dictionary be built from a binary search tree?


**BACK**

**Store the keys and values in the BST**, which gives ordered lookup.


Spec links: `spcpt_vct4zxppSDRnwt9H`


## Card 187 — question_and_answer (`fl_7T5mr7Bd3Tn5rXPt`)

**FRONT**

How can a binary tree be built from another ADT?


**BACK**

From a **linked list or array**, where the nodes link to each other like a graph.


Spec links: `spcpt_vct4zxppSDRnwt9H`


## Card 188 — fill_in_the_blanks (`fl_PRRT3HYCVvGyd5bR`)

**FRONT**

A queue can be implemented using two <u>**            **</u>.


**BACK**

A queue can be implemented using two **stacks**.


*Blanks: 1 — answers: []*

Spec links: `spcpt_vct4zxppSDRnwt9H`

Flags: blank_answer_mismatch


## Card 189 — question_and_answer (`fl_BvRcGfJYsTt4WdCY`)

**FRONT**

What are the two stacks called in a two-stack queue?


**BACK**

`inStack` and `outStack`.


Spec links: `spcpt_vct4zxppSDRnwt9H`


## Card 190 — question_and_answer (`fl_9grQw5VJjfhdfcBn`)

**FRONT**

How does enqueue work in a two-stack queue?


**BACK**

**Push the item onto **`**inStack**`.


Spec links: `spcpt_vct4zxppSDRnwt9H`


## Card 191 — question_and_answer (`fl_YFH2P4RhhZmvtdy5`)

**FRONT**

How does dequeue work in a two-stack queue?


**BACK**

If `outStack` is empty, **pop all items from **`**inStack**`** and push them onto **`**outStack**`, then **pop from **`**outStack**`.


Spec links: `spcpt_vct4zxppSDRnwt9H`


## Card 192 — true_or_false (`fl_WzVGC2Zb5v6wxwd4`)

**FRONT**

**True or False?**

In a two-stack queue, dequeue always pops directly from `inStack`.


**BACK**

**False.**

If `outStack` is empty, all items are **first moved from **`**inStack**`** to **`**outStack**`, and the pop then happens from `outStack`.


Spec links: `spcpt_vct4zxppSDRnwt9H`


## Card 193 — question_and_answer (`fl_gJZzgZQ7pPXQsCRb`)

**FRONT**

What does the two-stack queue demonstrate?


**BACK**

That you can **simulate FIFO behaviour using LIFO operations**.


Spec links: `spcpt_vct4zxppSDRnwt9H`


## Card 194 — fill_in_the_blanks (`fl_cFPB9KczdYd7z2Vh`)

**FRONT**

Two stacks can simulate <u>**        **</u> behaviour using LIFO operations.


**BACK**

Two stacks can simulate **FIFO** behaviour using LIFO operations.


*Blanks: 1 — answers: []*

Spec links: `spcpt_vct4zxppSDRnwt9H`

Flags: blank_answer_mismatch


## Card 195 — question_and_answer (`fl_wmmKk7dJvt6bmWsJ`)

**FRONT**

Why must algorithms be compared?


**BACK**

To **determine how suitable they are for solving a specific problem** or working with a particular set of data.


Spec links: `spcpt_3zm2hqrBFtvw4ZXm`


## Card 196 — question_and_answer (`fl_ntCcCvXGncjxmTvc`)

**FRONT**

Name the two key factors in comparing algorithms.


**BACK**

**Time complexity** and **space complexity**.


Spec links: `spcpt_3zm2hqrBFtvw4ZXm`


## Card 197 — question_and_answer (`fl_ZcrbqMD9hjsKHmQp`)

**FRONT**

What makes an algorithm most suitable?


**BACK**

It solves the problem in the **shortest time** and using the **least memory**.


Spec links: `spcpt_3zm2hqrBFtvw4ZXm`


## Card 198 — keyword_definition (`fl_C8hSs4Fj4CNr82pw`)

**FRONT**

Define **time complexity**.


**BACK**

The **number of operations or steps** an algorithm takes to complete, **not the actual time in seconds or minutes**.


Spec links: `spcpt_3zm2hqrBFtvw4ZXm`


## Card 199 — true_or_false (`fl_VzmMMXS5rgCzThjS`)

**FRONT**

**True or False?**

Time complexity measures the time in seconds that an algorithm takes.


**BACK**

**False.**

It measures the **number of operations or steps**, not the actual time.


Spec links: `spcpt_3zm2hqrBFtvw4ZXm`


## Card 200 — question_and_answer (`fl_MTwh44d3TmNMVBXJ`)

**FRONT**

Why is time complexity independent of hardware?


**BACK**

A **faster CPU executes instructions more quickly**, but the **number of instructions the algorithm performs stays the same**.


Spec links: `spcpt_3zm2hqrBFtvw4ZXm`


## Card 201 — question_and_answer (`fl_H8Wp75Rb4V2fwqn6`)

**FRONT**

How does the marathon analogy explain time complexity?


**BACK**

The **marathon distance is the algorithm** and the **runners are different CPUs**. Each runner finishes at a different time, but the **distance is the same**.


Spec links: `spcpt_3zm2hqrBFtvw4ZXm`


## Card 202 — keyword_definition (`fl_cvzwWZswNTR4DxBX`)

**FRONT**

Define **space complexity**.


**BACK**

The **amount of memory** an algorithm needs to complete its task.


Spec links: `spcpt_3zm2hqrBFtvw4ZXm`


## Card 203 — question_and_answer (`fl_Gczmkj7pnjYjkk4y`)

**FRONT**

Name three things that memory usage includes.


**BACK**

Space for **input data**, **temporary variables**, and any **additional data structures** such as arrays, stacks or queues.


Spec links: `spcpt_3zm2hqrBFtvw4ZXm`


## Card 204 — question_and_answer (`fl_wDxWpkHTc8tt5hdk`)

**FRONT**

Why might a recursive algorithm use more memory?


**BACK**

Because of the **call stack**.


Spec links: `spcpt_3zm2hqrBFtvw4ZXm`


## Card 205 — keyword_definition (`fl_45rZZVqWgjByFvNS`)

**FRONT**

Define **Big O Notation**.


**BACK**

A **mathematical way to describe the time and space complexity** of an algorithm, showing how well it scales as the size of the input increases.


Spec links: `spcpt_35Sp4YK9qjgFjdPx`


## Card 206 — question_and_answer (`fl_JvxfntH6TrVhrjkG`)

**FRONT**

What does Big O describe?


**BACK**

The **order of growth**, or efficiency, of an algorithm.


Spec links: `spcpt_35Sp4YK9qjgFjdPx`


## Card 207 — fill_in_the_blanks (`fl_s2mW76NFVhx7p7k6`)

**FRONT**

Big O is <u>**                **</u>-independent, measuring steps rather than seconds.


**BACK**

Big O is **hardware**-independent, measuring steps rather than seconds.


*Blanks: 1 — answers: []*

Spec links: `spcpt_35Sp4YK9qjgFjdPx`

Flags: blank_answer_mismatch


## Card 208 — true_or_false (`fl_zzb3vjRYknnZ8rjH`)

**FRONT**

**True or False?**

A faster CPU improves an algorithm's Big O complexity.


**BACK**

**False.**

Big O is **hardware-independent**. It measures steps or operations, not seconds.


Spec links: `spcpt_35Sp4YK9qjgFjdPx`


## Card 209 — question_and_answer (`fl_RKzxtWrgDfJn5Sw6`)

**FRONT**

State the two Big O rules.


**BACK**

**Keep only the dominant term**, and **ignore constants**.


Spec links: `spcpt_35Sp4YK9qjgFjdPx`


## Card 210 — fill_in_the_blanks (`fl_MmH7Vy7JJZV7f3WQ`)

**FRONT**

Only the <u>**                **</u> factor is used when determining an algorithm's Big O.


**BACK**

Only the **dominant** factor is used when determining an algorithm's Big O.


*Blanks: 1 — answers: []*

Spec links: `spcpt_35Sp4YK9qjgFjdPx`

Flags: blank_answer_mismatch


## Card 211 — question_and_answer (`fl_GhNmnFFNZ93JByqQ`)

**FRONT**

Why are constants ignored in Big O?


**BACK**

They **become insignificant as the input size grows**.


Spec links: `spcpt_35Sp4YK9qjgFjdPx`


## Card 212 — question_and_answer (`fl_8d8632d44QQZFHcb`)

**FRONT**

What is O(1)?


**BACK**

**Constant time.** The algorithm always takes the same number of steps, regardless of input size.


Spec links: `spcpt_35Sp4YK9qjgFjdPx`


## Card 213 — question_and_answer (`fl_vCmzgD7fTPTwN2GD`)

**FRONT**

What is O(n)?


**BACK**

**Linear time.** The number of steps **increases proportionally with the input size**.


Spec links: `spcpt_35Sp4YK9qjgFjdPx`


## Card 214 — question_and_answer (`fl_HTXZsVk5vpZj9SBZ`)

**FRONT**

What is O(n squared)?


**BACK**

**Polynomial time.** Performance is **proportional to the square of the input size**, caused by **nested loops**.


Spec links: `spcpt_35Sp4YK9qjgFjdPx`


## Card 215 — question_and_answer (`fl_WnbDm9c6SdDq4JPJ`)

**FRONT**

What is O(log n)?


**BACK**

**Logarithmic time.** The number of steps **grows slowly even as the input size grows rapidly**. Common in binary search.


Spec links: `spcpt_35Sp4YK9qjgFjdPx`


## Card 216 — question_and_answer (`fl_mBMDfVskYSw5vD93`)

**FRONT**

What is O(2 to the power n)?


**BACK**

**Exponential time.** The number of steps **doubles for every additional input value**, so it grows extremely fast.


Spec links: `spcpt_35Sp4YK9qjgFjdPx`


## Card 217 — question_and_answer (`fl_4FwKHn26XKWRYvjp`)

**FRONT**

What is O(n log n)?


**BACK**

**Linear logarithmic time**, for algorithms that **divide data and process each part**. Merge sort is an example.


Spec links: `spcpt_35Sp4YK9qjgFjdPx`


## Card 218 — question_and_answer (`fl_YJZWKFGZyjhmP32W`)

**FRONT**

Order the complexities from most to least inefficient.


**BACK**

**Exponential**, then **polynomial**, then **linear**, then **logarithmic**, then **constant**.


Spec links: `spcpt_35Sp4YK9qjgFjdPx`


## Card 219 — question_and_answer (`fl_Syknz5kqh2ndXQyc`)

**FRONT**

Where does factorial time sit?


**BACK**

It performs **worse than exponential time**.


Spec links: `spcpt_35Sp4YK9qjgFjdPx`


## Card 220 — question_and_answer (`fl_qnh4RNBKrzQxdz2j`)

**FRONT**

Where does linear-logarithmic time sit?


**BACK**

**Between polynomial and linear time**.


Spec links: `spcpt_35Sp4YK9qjgFjdPx`


## Card 221 — question_and_answer (`fl_QyWKm8KBYtZgghgQ`)

**FRONT**

Simplify 3n squared + 4n + 5 to Big O.


**BACK**

**O(n squared)**, because n squared is the dominant factor and coefficients are removed.


Spec links: `spcpt_35Sp4YK9qjgFjdPx`


## Card 222 — question_and_answer (`fl_xMcKjVHDVgpXjQgz`)

**FRONT**

Why is the coefficient 3 dropped from 3x squared?


**BACK**

As the input grows arbitrarily large, **multiplying by 3 contributes very little** to the overall time complexity.


Spec links: `spcpt_35Sp4YK9qjgFjdPx`


## Card 223 — question_and_answer (`fl_htjtzpfFmbvBD6yx`)

**FRONT**

How do you derive Big O by counting loops?


**BACK**

**1 loop is O(n)**, **2 nested loops are O(n squared)**, and **no loops is O(1)**.


Spec links: `spcpt_35Sp4YK9qjgFjdPx`


## Card 224 — question_and_answer (`fl_mzVPtpzKbWXQgb2Y`)

**FRONT**

What is log base 2 of 1,024?


**BACK**

**10**, because 2 to the power 10 is 1,024.


Spec links: `spcpt_35Sp4YK9qjgFjdPx`


## Card 225 — question_and_answer (`fl_p4F84xx7wbG3tmtm`)

**FRONT**

Which case does Big O usually describe, and why?


**BACK**

The **worst case**, in order to **guarantee a minimum standard** of performance.


Spec links: `spcpt_35Sp4YK9qjgFjdPx`


## Card 226 — question_and_answer (`fl_mD3wqMKqghznP7Gk`)

**FRONT**

For a linear search, what are the best, average and worst cases?


**BACK**

**Best O(1)** when the item is first, **average O(n)** when it is in the middle, and **worst O(n)** when it is not found.


Spec links: `spcpt_35Sp4YK9qjgFjdPx`


## Card 227 — keyword_definition (`fl_HJjNCZKMHsc4pCFX`)

**FRONT**

Define **binary tree**.


**BACK**

A binary tree is a **rooted data structure** where each node can have a **maximum of two child nodes**, one on the left and one on the right.


Spec links: `spcpt_YXcz52qmXcBBFJVr`


## Card 228 — fill_in_the_blanks (`fl_97Qh9szd9zDQch3W`)

**FRONT**

Each node in a binary tree can have a maximum of <u>**        **</u> child nodes.


**BACK**

Each node in a binary tree can have a maximum of **two** child nodes.


*Blanks: 1 — answers: []*

Spec links: `spcpt_YXcz52qmXcBBFJVr`

Flags: blank_answer_mismatch


## Card 229 — question_and_answer (`fl_6WsMnFJFVXfj3JPh`)

**FRONT**

What are binary trees used for?


**BACK**

Storing data in a way that allows fast **searching, insertion and deletion**.


Spec links: `spcpt_YXcz52qmXcBBFJVr`


## Card 230 — question_and_answer (`fl_RMwq8jj2W7GgWRDs`)

**FRONT**

How are the nodes of a binary tree linked?


**BACK**

Using **pointers** that reference the **left and right child nodes**.


Spec links: `spcpt_YXcz52qmXcBBFJVr`


## Card 231 — question_and_answer (`fl_MKzf5GqtjsBMHRn2`)

**FRONT**

What does a binary tree node contain?


**BACK**

A **data value**, plus **Left and Right pointers**, which may be `NULL` if no child exists.


Spec links: `spcpt_YXcz52qmXcBBFJVr`


## Card 232 — keyword_definition (`fl_kGSdgT3C3xXW5VBx`)

**FRONT**

Define **root**.


**BACK**

The **topmost node**, which has no parent.


Spec links: `spcpt_YXcz52qmXcBBFJVr`


## Card 233 — keyword_definition (`fl_dJnqvrwwhzrX297V`)

**FRONT**

Define **leaf**.


**BACK**

A node with **no children**.


Spec links: `spcpt_YXcz52qmXcBBFJVr`


## Card 234 — keyword_definition (`fl_DG3cKq63b8XY45sM`)

**FRONT**

Define **edge** in a tree.


**BACK**

A **connection between two nodes**, also called a branch or pointer.


Spec links: `spcpt_YXcz52qmXcBBFJVr`


## Card 235 — keyword_definition (`fl_CqMbbVSmNHV8tf93`)

**FRONT**

Define **subtree**.


**BACK**

A **smaller tree that is part of a larger one**.


Spec links: `spcpt_YXcz52qmXcBBFJVr`


## Card 236 — keyword_definition (`fl_gm9ZfY8bwby2krWY`)

**FRONT**

Define **traversal**.


**BACK**

The process of **visiting every node exactly once**.


Spec links: `spcpt_YXcz52qmXcBBFJVr`


## Card 237 — question_and_answer (`fl_K9Pdf7wSGCRKKcwF`)

**FRONT**

What is the difference between a parent and a child?


**BACK**

A **parent links to one or more children**. A **child is a node linked from a parent**.


Spec links: `spcpt_YXcz52qmXcBBFJVr`


## Card 238 — keyword_definition (`fl_nB45RrYt3PQvdXfc`)

**FRONT**

Define **binary search tree (BST)**.


**BACK**

A type of binary tree that stores data in **sorted order**.


Spec links: `spcpt_YXcz52qmXcBBFJVr`


## Card 239 — question_and_answer (`fl_GfvtfZcjfgFs3BdH`)

**FRONT**

State the two rules of a binary search tree.


**BACK**

All values in the **left subtree are less than** the node's value. All values in the **right subtree are greater than or equal to** the node's value.


Spec links: `spcpt_YXcz52qmXcBBFJVr`


## Card 240 — true_or_false (`fl_h6cwDGHNYZvJyp7d`)

**FRONT**

**True or False?**

In a BST, values equal to the node go in the left subtree.


**BACK**

**False.**

Values **greater than or equal to** the node go in the **right** subtree.


Spec links: `spcpt_YXcz52qmXcBBFJVr`


## Card 241 — question_and_answer (`fl_RzTpqf6Q9CmFnhvv`)

**FRONT**

Why are binary search trees efficient?


**BACK**

They use **comparison to decide which branch to follow**, which makes searching and insertion efficient.


Spec links: `spcpt_YXcz52qmXcBBFJVr`


## Card 242 — question_and_answer (`fl_RwcpG5MyRZY6hGj2`)

**FRONT**

What three fields does a `TreeNode` class have?


**BACK**

A **Value**, a **Left** pointer and a **Right** pointer.


Spec links: `spcpt_YXcz52qmXcBBFJVr`


## Card 243 — question_and_answer (`fl_hRdzX287G5fgSqxx`)

**FRONT**

What does `createNode` do?


**BACK**

It creates a new node, sets its **Value** to the data passed in, and sets both **Left and Right to NULL**.


Spec links: `spcpt_YXcz52qmXcBBFJVr`


## Card 244 — question_and_answer (`fl_TjNFzsxFTrZVh4z3`)

**FRONT**

How do you insert a value into a binary search tree?


**BACK**

Compare it with the current node. If **smaller, move left**; if **greater or equal, move right**. Insert the new node when an **empty pointer is found**.


Spec links: `spcpt_YXcz52qmXcBBFJVr`


## Card 245 — question_and_answer (`fl_JdrhnGrbgGgCvj88`)

**FRONT**

Name the three traversal methods.


**BACK**

**Pre-order**, **in-order** and **post-order**.


Spec links: `spcpt_YXcz52qmXcBBFJVr`


## Card 246 — question_and_answer (`fl_f5zrZHNGvDQvr22f`)

**FRONT**

What is the pre-order sequence?


**BACK**

Visit the **current node**, then **left**, then **right**.


Spec links: `spcpt_YXcz52qmXcBBFJVr`


## Card 247 — question_and_answer (`fl_J8ST7sfC3CNymMqP`)

**FRONT**

What is the in-order sequence?


**BACK**

Visit **left**, then the **current node**, then **right**.


Spec links: `spcpt_YXcz52qmXcBBFJVr`


## Card 248 — question_and_answer (`fl_khtDJkkt3nrhPDst`)

**FRONT**

What is the post-order sequence?


**BACK**

Visit **left**, then **right**, then the **current node**.


Spec links: `spcpt_YXcz52qmXcBBFJVr`


## Card 249 — question_and_answer (`fl_kN5m7RYWS363vHF8`)

**FRONT**

A tree has root 10, children 5 and 15, and 15 has children 12 and 20.

What is the pre-order output?


**BACK**

**10 5 15 12 20**


Spec links: `spcpt_YXcz52qmXcBBFJVr`


## Card 250 — question_and_answer (`fl_3NMwNhXrjzhZNNxm`)

**FRONT**

A tree has root 10, children 5 and 15, and 15 has children 12 and 20.

What is the in-order output?


**BACK**

**5 10 12 15 20**


Spec links: `spcpt_YXcz52qmXcBBFJVr`


## Card 251 — question_and_answer (`fl_6VcxznCGNKxk8Mmf`)

**FRONT**

A tree has root 10, children 5 and 15, and 15 has children 12 and 20.

What is the post-order output?


**BACK**

**5 12 20 15 10**


Spec links: `spcpt_YXcz52qmXcBBFJVr`


## Card 252 — true_or_false (`fl_hPm8T6MyX6hhCQHB`)

**FRONT**

**True or False?**

The base case of a recursive traversal is reaching a leaf node.


**BACK**

**False.**

The base case is `IF Node = NULL THEN RETURN`, that is reaching a **NULL pointer**, not a leaf.


Spec links: `spcpt_YXcz52qmXcBBFJVr`


## Card 253 — question_and_answer (`fl_sSvjSKY2Gt6trWGk`)

**FRONT**

Name the three cases for deleting a node from a BST.


**BACK**

The node has **no children**, **one child**, or **two children**.


Spec links: `spcpt_YXcz52qmXcBBFJVr`


## Card 254 — question_and_answer (`fl_RTVzf7wYpfcBzCr3`)

**FRONT**

How do you delete a node with no children?


**BACK**

**Simply remove the node**.


Spec links: `spcpt_YXcz52qmXcBBFJVr`


## Card 255 — question_and_answer (`fl_CKz3sTmd2ywrqgdc`)

**FRONT**

How do you delete a node with one child?


**BACK**

**Replace the node with its single child**.


Spec links: `spcpt_YXcz52qmXcBBFJVr`


## Card 256 — question_and_answer (`fl_HDCFp56DvdCMFS44`)

**FRONT**

How do you delete a node with two children?


**BACK**

Replace the node's value with its **in-order successor**, the **smallest value in the right subtree**, then delete that successor node.


Spec links: `spcpt_YXcz52qmXcBBFJVr`


## Card 257 — fill_in_the_blanks (`fl_Cd6GK63DmHb6PgjG`)

**FRONT**

To delete a node with two children, replace it with its in-order <u>**                  **</u>.


**BACK**

To delete a node with two children, replace it with its in-order **successor**.


*Blanks: 1 — answers: []*

Spec links: `spcpt_YXcz52qmXcBBFJVr`

Flags: blank_answer_mismatch


## Card 258 — question_and_answer (`fl_5vjV25bQrxtKs372`)

**FRONT**

What does the `findMin` helper function do?


**BACK**

It **walks left** from a node until `Left` is NULL, returning the **smallest value in that subtree**.


Spec links: `spcpt_YXcz52qmXcBBFJVr`

