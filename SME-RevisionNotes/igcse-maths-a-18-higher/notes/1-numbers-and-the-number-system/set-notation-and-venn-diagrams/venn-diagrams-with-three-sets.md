---
note_id: "rn_MPMnSPQPKtCVhFCd"
title: "Venn Diagrams with Three Sets"
source: https://www.savemyexams.com/igcse/maths/edexcel/a/18/higher/revision-notes/1-numbers-and-the-number-system/set-notation-and-venn-diagrams/venn-diagrams-with-three-sets
path: 1-numbers-and-the-number-system/set-notation-and-venn-diagrams/venn-diagrams-with-three-sets
updated_at: "2026-04-29T15:31:05.309Z"
spec_point_ids: ["spcpt_vfPNw2mzksvxf2JP"]
spec_point_codes: []
guided_study: false
---

# Venn Diagrams with Three Sets

## Venn diagrams with three sets

> **Spec point** — `spcpt_vfPNw2mzksvxf2JP`

## Venn diagrams with three sets

### What does a Venn diagram with three sets look like?

- There is a **rectangle** representing the universal set
- There are **three circles**

  - One for each of the sets
  
    - E.g.  $A$, $B$ and $C$
- The three circles intersect and split the rectangle into **eight regions**

  - A region where all **three circles intersect**
  
    - $A\capB\capC$
  - Three regions where **exactly two circles intersect**
  
    - $A\capB\capC'$, $A\capB'\capC$ and $A'\capB\capC$
  - Three regions where each circle **does not intersect with any other circle**
  
    - $A\capB'\capC'$, $A'\capB\capC'$ and $A'\capB'\capC$
  - A region **outside the three circles**
  
    - $A'\capB'\capC'$
    - This can also be written as `open parentheses A union B union C close parentheses apostrophe`

![Venn diagram with three overlapping circles labelled A, B, C. Regions are marked with formulas like AnBnC and A'nB'nC for set operations.](../../../assets/04a0063db139-3484-intersections.png)

*The intersections of three sets*

![Venn diagram with three overlapping circles labelled A, B, C, showing numbers 1 to 11 in various sections, including intersections and outer areas.](../../../assets/55b5fec5976b-54484-venn-diagram-with-3-sets.png)

*Example of a Venn diagram with three sets*

- It is possible that **two **of the circles do not intersect

  - E.g. if $A\capC=\emptyset$

![Venn diagram with three circles labelled A, B, and C. Numbers inside circles are 4, 11, 7, 5, 8. Outside circles are 9, ε.](../../../assets/61ba3a0504b3-14214-venn-diagram-with-3-sets-a-and-c-do-not-ov.png)

*Example of a Venn diagram where two sets do not have an intersection*

### How do I find the number of elements in a subset?

- Identify the **intersections **which make up the subset

  - E.g. the subset $A\capB$ is made up of $A\capB\capC$ and $A\capB\capC'$
- **Add together** the number of elements in the intersections

![Two Venn diagrams with sets A, B, C. Top highlights A∩B: 11+3=14. Bottom highlights A: 4+1+11+3=19, with shaded areas shown.](../../../assets/52dc038ae8d6-16624-number-of-elements-in-3-sets.png)

*Example of finding number of elements in subsets*

### How do I fill in a Venn diagram with three sets?

- Start with the **intersection **of **all three** circles $A\capB\capC$

  - Fill in the number or label it $x$ if it is unknown
- Fill in regions where **exactly two circles intersect**

  - You might be given the total number of elements in the intersection between those two sets
  
    - E.g. There are 20 elements that are in both set $A$ and set $C$
  - Subtract the number in the intersection of all three circles to find the number of elements that are just in those two sets
  
    - E.g. $20-x$ elements are in set $A$ and set $C$ but not set $B$

![Venn diagram with three circles A, B, C. Overlapping areas marked with numbers and expressions. Notes on the left explaining intersections.](../../../assets/d62b8b2a84b9-24324-fill-in-intersections.png)

- Fill in the parts of the circles which **do not intersect other circles**

  - You might be given the total number of elements in a set
  
    - E.g. There are 60 elements in set $A$
  - Subtract the numbers in the intersections which involve set $A$
  
    - E.g. subtract the number of elements in $A\capB\capC$, $A\capB\capC'$ and $A\capB'\capC$ from the number of elements in $A$

![Venn diagram with three sets A, B, C. Set A is shaded with numbers: 27, 13, x, and 20-x. Equation shown: 60 - x - (20 - x) - 13 = 27.](../../../assets/b8e2c3ec640b-8462-fill-in-circle.png)

- Fill in the number **outside all the circles**

  - This is the total number of elements minus the number of elements in all the intersections

> **Worked Example**
> Some students were asked whether they like studying statistics `open parentheses S close parentheses`, algebra `open parentheses A close parentheses` and geometry `open parentheses G close parentheses`.
> 
> - 5 said they like studying all three of statistics, algebra and geometry
> - 11 said they like studying statistics and algebra
> - 16 said they like studying algebra and geometry
> - 8 said they like studying statistics and geometry
> - 25 said they like studying geometry
> - 4 said they do not like studying any of the three topics
> - the number who said they like studying statistics only is the same as the number who said they like studying algebra only
> 
> Let $x$ be the number of students who said they like studying statistics.
> 
> (a) Show all this information on the Venn diagram, giving the number of students in each appropriate subset, in terms of $x$ where necessary. Simplify all expressions.
> 
> ![Venn diagram with three overlapping circles labelled S, A, G, enclosed in a rectangle labelled ε, representing set relationships.](assets/7aeb29526e88-8707-venn-diagram-worked-example.png)
> 
> **Answer**:
> 
> > *Put 4 outside the circles*
> 
> > *Put 5 in the intersection of all three circles*
> 
> > *Find the number of students who like statistics and algebra only*
> 
> *11 - 5 = 6*
> 
> > *Find the number of students who like algebra and geometry only*
> 
> *16 - 5 = 11*
> 
> > *Find the number of students who like statistics and geometry only*
> 
> *8 - 5 = 3*
> 
> > *Find the number of students who like geometry only*
> 
> *25 - 5 - 11 - 3 = 6*
> 
> > *Find the number of students who like studying statistics only*
> 
> - *Give your answer in terms of *$x$
> 
> $x-5-6-3=x-14$
> 
> > *The number of students who like algebra only is the same as the number of students who like statistics only*
> 
> ![Venn diagram with three overlapping circles labelled S, A, and G, containing numbers and expressions. The area outside the circles has the number 4.](assets/47e577ec68e5-63052-venn-diagram-worked-example-solution.png)
> 
> (b) Given that 30 students said they like studying algebra. Find the number of students who said they like studying statistics.
> 
> **Answer**:
> 
> > *Add together the numbers in the circle for algebra*
> 
> $x-14+6+5+11=x+8$
> 
> > *Set this equal to 30 and solve for *$x$
> 
> `table row cell x plus 8 end cell equals 30 row x equals 22 end table`
> 
> **Final answer:** **22 students said they like studying statistics**
