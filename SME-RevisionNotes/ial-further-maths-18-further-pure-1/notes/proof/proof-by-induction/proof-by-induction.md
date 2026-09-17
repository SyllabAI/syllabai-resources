---
note_id: "rn_m9N8zpSqc7gFZcR3"
title: "Proof by Induction"
source: https://www.savemyexams.com/international-a-level/further-maths/edexcel/18/further-pure-1/revision-notes/proof/proof-by-induction/proof-by-induction
path: proof/proof-by-induction/proof-by-induction
updated_at: "2024-04-02T10:05:35.079Z"
spec_point_ids: ["spcpt_SMzk6CSSYWkfQPd8"]
spec_point_codes: []
guided_study: false
---

# Proof by Induction

## Introduction to Proof by Induction

> **Spec point** — `spcpt_SMzk6CSSYWkfQPd8`

## Introduction to Proof by Induction

### What is proof by induction?

- **Proof by induction** is a way of proving a **result is true for a set of integers** by showing that if it is **true for one integer then it is true for the next integer**
- It can be thought of as falling dominoes:

  - Assume one domino falls
  
    - The **assumption** step
  - Show that if this domino falls, the next domino falls
  
    - The** inductive** step
- If you want all dominoes to fall (from the beginning) then

  - Show also that the** first** domino falls
  
    - The** basic** step

### What are the steps for proof by induction?

- **STEP 1** **The basic step: **Show the result is **true** for the **base case**

  - This is normally** **$n=1$** or **$n=0$

- **STEP 2**
**The assumption step: Assume** the result is true for $n=k$ where $k$* *is some integer

  - There is nothing to do for this step apart from writing down the assumption

- **STEP 3**
**The inductive step: **Use the** assumption **to show the result is true for $n=k+1$

  - This involves investigating* *$n=k+1$ and bringing in the $n=k$ assumption

- **STEP 4**
**The conclusion step: **Explain in** words** how the above steps make the result** true** for **all** integers, using the following **two **sentences:

  - "**If** it is true for $n=k$,* ***then** it is true for $n=k+1$."
  - "**As** it is true for $n=1$, the** **statement** **is true **for all** $n\inℤ^{+}$."

> **Exam Hint**
> Learn the exact wording from the conclusion above! You can lose the final mark  if your conclusion does not make sense.
