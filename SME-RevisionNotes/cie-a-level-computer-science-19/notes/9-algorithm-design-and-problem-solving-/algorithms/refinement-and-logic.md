---
note_id: "rn_crR5yWTHNbcdQPHn"
title: "Refinement & Logic"
source: https://www.savemyexams.com/a-level/computer-science/cie/19/revision-notes/9-algorithm-design-and-problem-solving-/algorithms/refinement-and-logic
path: 9-algorithm-design-and-problem-solving-/algorithms/refinement-and-logic
updated_at: "2025-04-21T09:28:20.499Z"
spec_point_ids: ["spcpt_WNyy3hqQgGcqb3Nm"]
spec_point_codes: []
guided_study: false
---

# Refinement & Logic

## Stepwise refinement

> **Spec point** — `spcpt_WNyy3hqQgGcqb3Nm`

## Stepwise refinement

### What is stepwise refinement?

- Stepwise refinement is the process of **breaking down a complex problem** into smaller, more manageable sub-problems in a logical order
- Each sub-problem is **refined step by step** until it is simple enough to be solved with a single subroutine or module
- This method ensures that the overall problem can be solved by addressing each part individually, in a **structured and efficient** way

#### Relationship to decomposition and top-down design

- **Decomposition** is the general concept of breaking a problem down into smaller parts
- **Top-down design** is the strategy used to perform decomposition
- **Stepwise refinement** is the process used in top-down design to **gradually refine** each major task into simpler sub-tasks
- In other words, **stepwise refinement is how top-down design is implemented**

#### Benefits of stepwise refinement

- Helps developers **understand and organise** the structure of a program
- Makes **testing and debugging easier** through **unit testing** of individual subroutines
- Encourages **code reuse** by breaking tasks into reusable components
- Supports **collaborative development**, as tasks can be divided between team members
- Each subroutine should:

  - **Be clear and focused **on a single task
  - **Be simple** enough to implement directly
  - **Not need **further breakdown

### Example: Calculating student grades

- Here’s how stepwise refinement could be applied to a program designed to calculate student grades for a teacher’s classes:

#### Top-level task:

- Calculate grades for all students in all classes

#### Stepwise refinement:

- **Step 1 – Calculate the grade for each assessment**

  - For each question:
  
    - Mark the question
    - Store the mark
  - Sum the marks for all questions in the assessment
- **Step 2 – Calculate the average grade for each student**

  - Add together grades from all assessments
  - Divide by the number of assessments
  - Store the average
- **Step 3 – Repeat for each class**

  - For every student in the class:
  
    - Perform Steps 1 and 2
- This structured breakdown allows each task to be turned into a subroutine, simplifying the design, implementation, and testing of the overall program
