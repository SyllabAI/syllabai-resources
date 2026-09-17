---
note_id: "rn_7fWhhgGKrQxqPTyw"
title: "Scheduling Activities"
source: https://www.savemyexams.com/international-a-level/maths/edexcel/20/decision-1/revision-notes/critical-path-analysis/critical-path-analysis/scheduling-activities
path: critical-path-analysis/critical-path-analysis/scheduling-activities
updated_at: "2026-07-02T08:19:38.467Z"
spec_point_ids: ["spcpt_vg4jSpg46ks8kcrD"]
spec_point_codes: []
guided_study: false
---

# Scheduling Activities

## Scheduling Activities

> **Spec point** — `spcpt_vg4jSpg46ks8kcrD`

## Scheduling Activities

### What is meant by scheduling (activities)?

- **Scheduling activities** is the process of **assigning workers** to **activities** within a **project**
- The **two** types of problem that arise involve

  - Finding the **minimum number of workers** such that a project can be completed in its **minimum project duration**
  
    - The **minimum project duration** is also called the **critical time** of the project
  - Finding the (new) **minimum project duration** given that there are **constraints**
  
    - E.g. There may be a **maximum number** of **workers **available at any given time
- In harder problems, certain workers may only be capable of carrying out particular activities

### What assumptions are made in scheduling?

- In **scheduling** activities the following assumptions are made

  - Each **activity** requires only **one worker**
  
    - Or one team of workers, i.e. one resource
  - An activity is assigned the first available worker
  - If there is a choice of activities, assign a worker the activity with the **lower late end time**
  
    - This is the **lower late event time** at the **activity end node**
  - A worker can only work on one activity at a time
  - Once a worker has started an activity, that activity needs to be completed

### How do I schedule activities for a project that requires the minimum number of workers?

- For this type of problem, the **critical time** of the project* ***cannot **change

  - The **critical activities** cannot be delayed
  - **One worker** (resource) will complete all the **critical activities**
- Using a **Gantt chart** and considering the **non-critical activities**

  - **Non-critical activities** can be delayed, but only **within** their (total) **float** times
  
    - **Early start times** can be delayed but **late end times** cannot
  - **Visualise** each activity as its bar being able to 'slide' within its box (solid and dotted)
  
    - Aim for as few **overlaps** between activities as possible
  - Activities can then be combined into as few rows as possible
  
    - Place them 'back-to-back'
    - Where possible activities should start **immediately** after others end
  - Each **row** on the (reduced) Gantt chart will then be completed by **one worker**
  
    - The number of rows is the number of workers

- Remember that the **precedence** of **activities** needs to be maintained

  - E.g.  Activity H, say, cannot move so it starts after activity I, as activity I depends on H being completed first
  
    - H is an **immediate predecessor** of I

### What is the lower bound for the (minimum) number of workers?

- The **theoretical lower bound** for the number of workers to complete a project in its **minimum project duration **is

  - the **smallest integer** value that satisfies

$\mathrm{Lower} \mathrm{bound}\geq\frac{\mathrm{Total} \mathrm{time} \mathrm{of} \mathrm{all} \mathrm{activities}}{\mathrm{Minimum} \mathrm{project} \mathrm{duration}}$

- To find a **practical lower bound** for the number of workers

  - Imagine vertical lines drawn in between each unit
  
    - e.g. vertical lines at 0.5, 1.5, 2.5, etc
  - For each line, consider which **activities **can use their float to **move **so that the **line does not touch them**
  - Count the number of activities which **cannot **be **moved **and **must happen **at that time
  - The **biggest number **found is a **lower bound **
- It is **not always possible** to schedule activities such that the lower bound can be met

### How do I schedule activities for a project that has a maximum number of workers?

- For a problem, where there is a **maximum number of workers** available at any point in time

  - The maximum number of workers **cannot** be exceeded,
  - It may require activities to be delayed and the project's **critical time** to be increased
- Using a **Gantt chart**

  - Find the **minimum number** of workers required to complete the project in its **critical time**
  
    - The Gantt chart would have already been largely reduced
    - Do this using the process above
  - Consider how **any** activity (critical or non-critical) can be **delayed**
  
    - The Gantt chart must use no more rows than the (maximum) number of workers available at any time
- As in the first type of problem, the **precedence** of **activities** needs to be maintained

  - You may want to use the activity network to check this
  - E.g.  Activity H, say, cannot move so it starts after activity I, as activity I depends on H being completed first
  
    - H is an **immediate predecessor** of I

> **Exam Hint**
> - Practise scheduling questions as exam preparation
> 
>   - Experience is the best way to become familiar with what to look for as there is no specific algorithm to follow
> - If you are asked to state a lower bound for the minimum number of workers then:
> 
>   - Show the calculation if you use the formula
>   - State the time at which the maximum number of activities must happen and state those activities
>   
>     - E.g. A lower bound is 3 because at time 10.5 the activities A, B and F must happen

> **Worked Example**
> A precedence table and Gantt chart for a project are shown below.
> Each activity requires one worker and times are given in days.
> 
> | **Activity** | **Immediately preceding activities** |
> |---|---|
> | A | - |
> | B | - |
> | C | A |
> | D | B |
> | E | A, D |
> | F | B |
> | G | C |
> | H | C |
> | I | G, H |
> | J | E, F |
> 
> ![reslev-sched-gantt-we-qu](assets/4c72739ccc37-reslev-sched-gantt-we-qu.png)
> 
> a) Find the lower bound for the minimum number of workers required to complete the project within its critical time.
> 
> **Answer:**
> 
> `table row cell fraction numerator Total space time space of space all space activities over denominator Minimum space project space duration end fraction end cell equals cell fraction numerator 23 plus 4 plus 3 plus 7 plus 6 plus 4 plus 4 over denominator 23 end fraction end cell row blank equals cell 51 over 23 end cell row blank equals cell 2.217 space... end cell end table`
> 
> > *The lower bound is the smallest integer greater than or equal to 2.217 ...*
> 
> **Final answer:** **The lower bound for the number of workers is 3**
> 
> b) Find the minimum number of workers required such that the project can be completed within its critical time.
> 
> **Answer:**
> 
> > *Worker 1 ('row 1') will be assigned to all the critical activities ('back-to-back')*
> 
> > *Worker 2 can start activity B at time zero, with activity D following immediately (at its early start time) and activity E immediately after that*
> 
> ![sched-we-ans-b1](assets/52f82ca11e8c-sched-we-ans-b1.png)
> 
> > *By 'sliding' activities F and H it can be seen that there will be (at least) one day where either E and F or F and H will need to happen simultaneously - therefore a third worker is needed*
> 
> > *There is some flexibility in assigning worker 3 but activity H is dependent on activity C*
> 
> > *Activity J is dependent on E and F but as long as F finishes by its late end time that will look after itself*
> 
> > *The adjusted Gantt chart is*
> 
> ![sched-gantt-we-ans-a](assets/5ad7c594bbde-sched-gantt-we-ans-a.png)
> 
> > *The (minimum) number of workers is the number of rows in the adjusted Gantt chart, of which there are 3*
> 
> **Final answer:** **To complete the project within its critical time (23 days) a minimum of three workers will be required**
> 
> c) Find the minimum project duration given that a maximum of two workers are available at any time.
> 
> **Answer:**
> 
> > *Using the solution to part b) we can see that activities A, C, B, D and E efficiently occupy two workers*
> 
> > *Delaying activity F so it starts immediately after E will delay the whole project by one day (24 days)*
> *(Be careful describing this, activity F would be starting **after** day 14, so starts **on** day 15)*
> 
> > *This leaves activity H - I is dependent on it (and G) and H itself is dependent on C*
> 
> > *Assigning H to worker 2 would delay the project by longer than necessary (at least 28 days) but by assigning H to worker 1 (either between C and G or between G and I) means precedences are maintained*
> 
> > *The adjusted Gantt chart is*
> 
> ![sched-gantt-we-ans-b](assets/bb0b14d9e499-sched-gantt-we-ans-b.png)
> 
> > *Activity I is the last to finish at a time of 27 days*
> 
> **Final answer:** **The minimum project time for a maximum of two workers is 27 days**
