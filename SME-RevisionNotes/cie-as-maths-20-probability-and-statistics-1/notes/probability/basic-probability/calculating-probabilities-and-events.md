---
note_id: "rn_z2wwpznhDd5W4g7B"
title: "Calculating Probabilities & Events"
source: https://www.savemyexams.com/as/maths/cie/20/probability-and-statistics-1/revision-notes/probability/basic-probability/calculating-probabilities-and-events
path: probability/basic-probability/calculating-probabilities-and-events
updated_at: "2026-07-02T08:19:38.463Z"
spec_point_ids: ["spcpt_B8jpsFGFMWZ2ywS5", "spcpt_7GngfWnfm7YxqRWm"]
spec_point_codes: []
guided_study: true
---

# Calculating Probabilities & Events

## Probability Basics

> **Spec point** — `spcpt_B8jpsFGFMWZ2ywS5`

## Probability Basics

#### What do I need to know about probability for AS and A level Mathematics?

- The language used in probability can be confusing so here are some definitions of commonly misunderstood terms

  - An **experiment** is a repeatable activity that has a result that can be observed or recorded; it is what is happening in a question
  - An **outcome** is the result of an experiment
  - All possible outcomes can be shown in a **sample** **space** – this may be a list or a table and is particularly useful when it is difficult to envisage all possible outcomes in your head

e.g.  The sample space below is for two ***fair***** **four-sided spinners whose outcomes are the product of the sides showing when spun.

![3-1-1-fig1-sample-space](../../../assets/8335c0714882-3-1-1-fig1-sample-space.png)

- An **event** is an outcome or a collection of outcomes; it is what we are interested in happening

  - Do note how this could be more than one outcome
  e.g. For the spinners above,
         the event “the product is -2” has one outcome but
         the event “the product is negative” has 6 outcomes
- **Terminology** - be careful with the words **'not'**, **'and'** and **'or'**

  - ***A***** and *****B*** means both the events *A* and *B* happen at the same time
  
    - *A*  **and ***B*  is formally written as  $A\capB$ (∩ is called **intersection**)
  - ***A***** or *****B***  means event *A* happens, or event *B* happens, **or both** happen
  
    - *A*  **or ***B*  is formally written as  $A\cupB$(∪ is called **union**)
  - **not *****A*** means the event *A* does not happen
  
    - **not *****A is formally*** written as ***A*****'** (pronounced "*A* prime*"*)
- **Notation** – the way probabilities are written is formal and consistent at A-level

  - $P(A)=0.6$           “the probability of **event *****A*** happening is 0.6”
  - $P(A')=0.4$          “the probability of **event *****A*** **not** happening equals 0.4”

(This is sometimes written as $P(\overline{A})$)

- $P(X\leq4)=0.4$      “the probability of being less than four is 0.4”

#### How do I solve A level probability questions?

- Recall basic results of probability

  - $P("\mathrm{success}")=\frac{\mathrm{number} \mathrm{of} \mathrm{ways} \mathrm{to} \mathrm{get}"\mathrm{success}"}{\mathrm{total} \mathrm{number} \mathrm{of} \mathrm{outcomes}}$
  
    - It is important to understand that the above only applies if all outcomes are ***equally likely***
  - $P(A')=1-P(A)$
  
    - The probability of “$notA$” is the ***complement***** **of the probability of “*A*”
    - One of the easiest results in probability to understand,
    one of the hardest results to spot!
- Be aware of whether you are using ***theoretical probabilities*** or probabilities based on the results of several experiments (***relative frequency***). You may have to compare the two and make a judgement as to whether there is ***bias*** in the experiment.

e.g.        The outcomes from rolling a fair dice have theoretical probabilities but the outcomes from a football match would be based on previous results between the two teams

- For probabilities based on relative frequency, a large number of experiments usually provides a better estimate of the probability of an event happening
- **Frequencies** or **probabilities** may have to be read from basic statistical **diagrams** such as **bar** **charts**, **box**-**and**-**whisker** diagrams, **stem** **and** **leaf** diagrams, etc

> **Worked Example**
> A fair, five-sided spinner has its sides labelled 2, 5, 8, 10 and 11.
> 
> Find, from one spin, the probability that the spinner shows
> 
> (i) 8
> 
> (ii) a prime number
> 
> (iii) an odd prime number
> 
> (iv) a number other than 5.
> 
> **Answer:**
> 
> ![2-1-1-cie-fig2-we-solution](assets/664d7693ccaf-image.bin)

> **Exam Hint**
> - Most probability questions are in context so can be long and wordy; go back and re-read the question, several times, whenever you need to
> - Try to get immersed in the context of the question to help understand a problem

## Independent & Mutually Exclusive Events

> **Spec point** — `spcpt_7GngfWnfm7YxqRWm`

## Independent & Mutually Exclusive Events

#### What are independent events?

- **Independent** **events** do not affect each other
- For two independent events, the probability of one event happening is unaffected by the outcome of the other event

  - e.g.    The events “rolling a 6 on a dice” and “flipping heads on a coin” are    independent
  
    - the outcome “rolling a 6” does not affect the probability of the outcome “heads” (and vice versa)
- For two **independent** events, *A* and *B*

$P(A\mathrm{AND}B)=P(A)\timesP(B)$

e.g.     $P("6\mathrm{on}a\mathrm{dice}"\mathrm{AND}"\mathrm{heads} \mathrm{on}a\mathrm{coin}")=\frac{1}{6}\times\frac{1}{2}=\frac{1}{12}$

- Independent events could refer to events from different experiments

#### What are mutually exclusive events?

- **Mutually** **exclusive** ***events***** **cannot occur simultaneously

  - $P(A\mathrm{AND}B)=P(A\capB)=0$
- For two mutually exclusive events, the ***outcome*** of one event means the other event cannot occur

  - e.g.      The events “rolling a 5 on a die” and “rolling a 6 on a die” are mutually exclusive
- For two **mutually** **exclusive** events, *A* and *B*

$P(A\mathrm{OR}B)=P(A\cupB)=P(A)+P(B)$

e.g.  $\mathrm{P} ( " 6 \text{on} \mathrm{a} \text{dice} " \text{OR} " \text{heads} \text{on} \mathrm{a} \text{coin} " ) = \frac{1}{6} + 1 \frac{1}{2} = \frac{4}{6} = ( \frac{2}{3} )$

- **Mutually** **exclusive** events generally refer to events from the same (single trial of an) ***experiment***
- Mutually exclusive events cannot be independent; the outcome of one event means the probability of the other event is zero

#### How do I solve problems involving independent and mutually exclusive events?

- Make sure you know the statistical terms – **independent** and **mutually** **exclusive**
- Remember

  - **independence** is **AND(∩)** and is $\times$
  - **mutual** **exclusivity** is **OR (∪)** and is $+$
- Solving problems will require interpreting the information given and the application of the appropriate formula

  - Information may be explained in words or by diagram(s)

(including Venn diagrams – see Revision Note Venn Diagrams)

- **Showing** or **determining** whether two events are independent or mutually exclusive are also common

  - To do this you would show the relevant formula is true

> **Worked Example**
> (a) Two events, $Q$ and $R$ are such that $P(Q)=0.8$ and $\text{P}(Q\mathrm{and}R)=0.1$.
> Given that $Q$ and $R$ are independent, find $P(R)$
> 
> (b) Two events, $S$ and $T$ are such that $P(S)=2P(T)$.
> Given that $S$ and $T$ are mutually exclusive and that $P(SorT)=0.6$ find $P(S)$ and $P(T)$.
> 
> (c) A fair five-sided spinner has sides labelled 2, 3, 5, 7, 11.
> Find the probability that the spinner lands on a number greater than 5.
> 
> **Answer:**
> 
> ![2-1-1-cie-fig3-we-solution_a](assets/b2bc8c1cb5de-image.bin)
> 
> ![2-1-1-cie-fig3-we-solution_b](assets/296651c8e62f-image.bin)
> 
> ![2-1-1-cie-fig3-we-solution_c](assets/7cd7714d6b5b-image.bin)

> **Exam Hint**
> - Try to rephrase questions in your head in terms of **AND** and/or **OR** !
> e.g.      A fair six-sided die is rolled and a fair coin is flipped.
>            “Find the probability of obtaining a prime number with heads.”
> 
> would be
> 
> “Find the probability of rolling a 2 **OR** a 3 **OR** a 5 **AND** heads.”
