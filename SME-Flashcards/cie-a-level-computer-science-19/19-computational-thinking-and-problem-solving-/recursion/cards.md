# Recursion

Course: cie-a-level-computer-science-19 · Section: 19. Computational thinking & Problem-solving

Source: https://www.savemyexams.com/a-level/computer-science/cie/19/flashcards/19-computational-thinking-and-problem-solving-/recursion/


## Card 1 — keyword_definition (`fl_JNGVRqk2rS7by8Wm`)

**FRONT**

Define **recursion**.


**BACK**

Recursion is a programming technique where a **function calls itself** to solve a problem or execute a task.


Spec links: `spcpt_qM6kDbGBJYcn4ZnP`


## Card 2 — question_and_answer (`fl_MHbrHcPqvhyVRWxx`)

**FRONT**

What does recursion use instead of iterative loops?


**BACK**

The idea of **self-reference**, to **break down complicated problems** into more manageable subproblems.


Spec links: `spcpt_qM6kDbGBJYcn4ZnP`


## Card 3 — question_and_answer (`fl_Xbp7pG67yPXYWvGt`)

**FRONT**

Name the three features of a recursive algorithm.


**BACK**

The function must **call itself**, there must be a **base case**, and there must be a **stopping base** that is reachable after a finite number of times.


Spec links: `spcpt_qM6kDbGBJYcn4ZnP`


## Card 4 — keyword_definition (`fl_BR45KCZkjwQY5mzZ`)

**FRONT**

Define **base case**.


**BACK**

A condition where the function can **return a value without further recursive calls**.


Spec links: `spcpt_qM6kDbGBJYcn4ZnP`


## Card 5 — fill_in_the_blanks (`fl_JSWNnCpvQm5ZMWYb`)

**FRONT**

Recursive programs must reach the base case in a <u>**            **</u> number of steps.


**BACK**

Recursive programs must reach the base case in a **finite** number of steps.


*Blanks: 1 — answers: []*

Spec links: `spcpt_qM6kDbGBJYcn4ZnP`

Flags: blank_answer_mismatch


## Card 6 — question_and_answer (`fl_H9Q7nvb4dHZV6Vpf`)

**FRONT**

How does a recursive function progress towards the base case?


**BACK**

It **calls itself with a modified input parameter**, breaking the problem into smaller instances each time.


Spec links: `spcpt_qM6kDbGBJYcn4ZnP`


## Card 7 — question_and_answer (`fl_rK44bFcs3N8vNQ6j`)

**FRONT**

What is the base case for `factorial(n)`?


**BACK**

When **n is 0 or 1**, the function returns **1**.


Spec links: `spcpt_qM6kDbGBJYcn4ZnP`


## Card 8 — question_and_answer (`fl_Nq9s9w7SmrYFqpr9`)

**FRONT**

What does `factorial(5)` return?


**BACK**

**120**, since 5! = 5 x 4 x 3 x 2 x 1.


Spec links: `spcpt_qM6kDbGBJYcn4ZnP`


## Card 9 — question_and_answer (`fl_TFdChBMWV2CCtPD7`)

**FRONT**

What happens without a proper stopping condition?


**BACK**

The function **calls itself indefinitely**, using up excessive memory and causing **stack overflow errors** and program crashes.


Spec links: `spcpt_qM6kDbGBJYcn4ZnP`


## Card 10 — question_and_answer (`fl_GwVmKHXzCQJjHR7m`)

**FRONT**

How do you design a stopping condition?


**BACK**

**Identify the simplest scenario** where the function can give a **direct result**, and define that as the base case.


Spec links: `spcpt_qM6kDbGBJYcn4ZnP`


## Card 11 — question_and_answer (`fl_MwhyJ2j6sYnDWzK8`)

**FRONT**

Name two benefits of recursion.


**BACK**

It is **concise**, especially for structures like trees or fractals, and **simple** to read and maintain because it states what needs doing rather than how.


Spec links: `spcpt_qM6kDbGBJYcn4ZnP`


## Card 12 — question_and_answer (`fl_xHkQjZZwprPY8JbF`)

**FRONT**

Name three drawbacks of recursion.


**BACK**

**Performance**, because repeated function calls are CPU and memory intensive; **debugging**, because the program state is harder to track; and **limited application**, because not all problems suit recursion.


Spec links: `spcpt_qM6kDbGBJYcn4ZnP`


## Card 13 — true_or_false (`fl_3mNz4G43NstQ4TpS`)

**FRONT**

**True or False?**

Recursion always performs better than iteration.


**BACK**

**False.**

Iteration is **more efficient** and uses **less memory**. Repeated recursive calls are CPU and memory intensive, leading to slower execution.


Spec links: `spcpt_qM6kDbGBJYcn4ZnP`


## Card 14 — question_and_answer (`fl_vcYHZFXdDDNxxdJS`)

**FRONT**

Name three benefits of iteration.


**BACK**

Better **performance** with less memory usage, easier to **understand and debug**, and **wider application** to a range of problems.


Spec links: `spcpt_qM6kDbGBJYcn4ZnP`


## Card 15 — question_and_answer (`fl_PJMh6BZBybfHrpZT`)

**FRONT**

Name two drawbacks of iteration.


**BACK**

It can become **very complex** and use more lines of code than a recursive alternative, and it is **less concise**.


Spec links: `spcpt_qM6kDbGBJYcn4ZnP`


## Card 16 — question_and_answer (`fl_x9NYcyzdmbVvnDm7`)

**FRONT**

In the countdown example, what replaces the recursive call in the iterative version?


**BACK**

A **while loop** that checks `n > 0`.


Spec links: `spcpt_qM6kDbGBJYcn4ZnP`


## Card 17 — question_and_answer (`fl_mZFyB6wtFzrCsT5G`)

**FRONT**

What are the two advantages of the iterative countdown?


**BACK**

**Less memory is used**, giving increased performance, and it is **easier to debug**.


Spec links: `spcpt_qM6kDbGBJYcn4ZnP`


## Card 18 — question_and_answer (`fl_YkXbdJyTjJDbk5Rj`)

**FRONT**

How does the compiler treat a recursive function?


**BACK**

**Not like a loop.** It uses the **call stack** to keep track of each function call.


Spec links: `spcpt_MHH4FH7SP9pPrJqz`


## Card 19 — fill_in_the_blanks (`fl_t8RBY5nnPSJkdMbx`)

**FRONT**

Each time a function calls itself, the system stores a snapshot on the <u>**        **</u> stack.


**BACK**

Each time a function calls itself, the system stores a snapshot on the **call** stack.


*Blanks: 1 — answers: []*

Spec links: `spcpt_MHH4FH7SP9pPrJqz`

Flags: blank_answer_mismatch


## Card 20 — keyword_definition (`fl_HwQTxZF4HCpHWvCz`)

**FRONT**

Define **stack frame**.


**BACK**

The **snapshot of a single function call** stored on the call stack.


Spec links: `spcpt_MHH4FH7SP9pPrJqz`


## Card 21 — question_and_answer (`fl_rpNFpMgXMCPxyfHN`)

**FRONT**

Name the three things a stack frame contains.


**BACK**

The **function name**, the **value of parameters and variables** at that level, and the **place to return to** when the function finishes.


Spec links: `spcpt_MHH4FH7SP9pPrJqz`


## Card 22 — question_and_answer (`fl_Rv7cXtyFN9Xkbsty`)

**FRONT**

When do calls stop being added to the stack?


**BACK**

When the **base case is reached**.


Spec links: `spcpt_MHH4FH7SP9pPrJqz`


## Card 23 — keyword_definition (`fl_3tGj3Ytd3kzjtgWD`)

**FRONT**

Define **stack unwinding**.


**BACK**

The process of **returning values back up the stack** after the base case has been reached.


Spec links: `spcpt_MHH4FH7SP9pPrJqz`


## Card 24 — question_and_answer (`fl_pq3g3d7Dc8HYhhbj`)

**FRONT**

What happens during unwinding?


**BACK**

The **most recent call completes and returns a value**, control goes back to the **previous stack frame**, and this continues until the original call receives the final result.


Spec links: `spcpt_MHH4FH7SP9pPrJqz`


## Card 25 — question_and_answer (`fl_fwJCbZKN4wKZJyVS`)

**FRONT**

Trace `factorial(3)` down the call stack.


**BACK**

`factorial(3)` calls `3 * factorial(2)`; `factorial(2)` calls `2 * factorial(1)`; `factorial(1)` hits the **base case and returns 1**.


Spec links: `spcpt_MHH4FH7SP9pPrJqz`


## Card 26 — question_and_answer (`fl_6frcCFhvnfjwHrwf`)

**FRONT**

What does the unwinding of `factorial(3)` give?


**BACK**

`factorial(2) = 2 x 1 = 2`, then `factorial(3) = 3 x 2 = ``**6**`.


Spec links: `spcpt_MHH4FH7SP9pPrJqz`


## Card 27 — question_and_answer (`fl_qdp96v4hQDrVQrv9`)

**FRONT**

What was on the stack at the deepest point of `factorial(3)`?


**BACK**

**factorial(3)**, **factorial(2)** and **factorial(1)**, each popped off as the return values passed back up.


Spec links: `spcpt_MHH4FH7SP9pPrJqz`


## Card 28 — keyword_definition (`fl_kjvG455xS2YMkZm3`)

**FRONT**

Define **stack overflow**.


**BACK**

What happens when **recursive calls never stop**, exhausting the available memory.


Spec links: `spcpt_MHH4FH7SP9pPrJqz`


## Card 29 — true_or_false (`fl_4bN7xkdXqT4sxCjy`)

**FRONT**

**True or False?**

A recursive function without a base case simply returns nothing.


**BACK**

**False.**

The stack **never stops growing**, which leads to a **stack overflow** and causes the program to crash.


Spec links: `spcpt_MHH4FH7SP9pPrJqz`

