---
note_id: "rn_P25gRyqM9cYTtyrY"
title: "Calculating Probabilities & Events"
source: https://www.savemyexams.com/international-a-level/maths/edexcel/20/statistics-1/revision-notes/probability/basic-probability/calculating-probabilities-and-events
path: probability/basic-probability/calculating-probabilities-and-events
updated_at: "2026-07-02T08:19:38.244Z"
spec_point_ids: ["spcpt_bxWFJwqxDSR3cBsC", "spcpt_xPq8dPj856nqvFQ3"]
spec_point_codes: []
guided_study: true
---

# Calculating Probabilities & Events

## Probability Basics

> **Spec point** — `spcpt_bxWFJwqxDSR3cBsC`

## Calculating probabilities & events

### What language is used in probability?

- The language used in probability can be confusing so here are some definitions of commonly misunderstood terms

  - An **experiment** is a repeatable activity that has a result that can be observed or recorded; it is what is happening in a question
  - An **outcome** is the result of an experiment
  - All possible outcomes can be shown in a **sample** **space** – this may be a list or a table and is particularly useful when it is difficult to envisage all possible outcomes in your head
- e.g.  The sample space below is for two ***fair***** **four-sided spinners whose outcomes are the product of the sides showing when spun.

![3-1-1-fig1-sample-space](../../../assets/8335c0714882-3-1-1-fig1-sample-space.png)

- An **event** is an outcome or a collection of outcomes; it is what we are interested in happening

  - Do note how this could be more than one outcome e.g. For the spinners above,        the event “the product is -2” has one outcome but        the event “the product is negative” has 6 outcomes
- **Terminology** - be careful with the words **'not'**, **'and'** and **'or'**

  - ***A***** and *****B*** means both the events *A* and *B* happen at the same time
  
    - (You will have seen this written as $A\capB$ at GCSE)
  - ***A***** or *****B***  means event *A* happens, or event *B* happens, **or both** happen
  
    - (You will have seen this written as $A\cupB$ at GCSE)
  - **not *****A*** means the event *A* does not happen
  
    - (You will have seen this written as *A*' at GCSE)
- **Notation** – the way probabilities are written is formal and consistent at A-level

  - $P(A)=0.6$           “the probability of **event **$A$  happening is 0.6”
  - $P(A')=0.4$          “the probability of **event** ** **$A$ **not** happening equals 0.4”
  - (This is sometimes written as $P(\overline{A})$)

- $P(X\leq4)=0.4$      “the probability of $X$ being less than four is 0.4”

### How do I find probabilities?

- The big difference with probability at A level is the language and the notation used
- Recall basic results of probability

  - $P("\mathrm{success}")=\frac{\mathrm{number} \mathrm{of} \mathrm{ways} \mathrm{to} \mathrm{get}"\mathrm{success}"}{\mathrm{total} \mathrm{number} \mathrm{of} \mathrm{outcomes}}$
  
    - It is important to understand that the above only applies if all outcomes are ***equally**** ****likely***
  - $P(\mathrm{not}A)=1-P(A)$
  
    - The probability of “$notA$” is the ***complement*** of the probability of “*A*”
    - One of the easiest results in probability to understand, one of the hardest results to spot!
- Be aware of whether you are using ***theoretical**** ****probabilities*** or probabilities based on the results of several experiments (***relative**** ****frequency***). You may have to compare the two and make a judgement as to whether there is *bias* in the experiment.
- e.g.        The outcomes from rolling a fair dice have theoretical probabilities but the outcomes from a football match would be based on previous results between the two teams

- Ensure you can interpret common ways of displaying data – from frequency tables, histograms, box plots and other ways to illustrate data

  - See Revision Notes
  - 2.1.2 Frequency Tables
  - 2.2.1 Data Presentation
  - 2.2.2 Box Plots & Cumulative Frequency
  - 2.2.3 Histograms
  - Be particularly careful when using **histograms**
  
    - These use **frequency** **density**, not frequency
    - Using *parts* of bars may be required due to where class boundaries fall so values will be **estimates **(using the proportion of the bar needed, sometimes called **interpolation**)

> **Worked Example**
> 100 skydivers took part in an all-day charity event, with the altitude of the aeroplane at which they jumped from summarised in the histogram below.
> 
> ![3-1-1-fig2-we-diagram](assets/d01f0be25223-3-1-1-fig2-we-diagram.png)
> 
> (a) Use the histogram to find the probability that a randomly chosen skydiver jumped from the aeroplane at an altitude
> 
> (i) between 14 000 and 16 000 feet,
> 
> (ii) between 16 000 and 20 000 feet.
> 
> (b) Estimate the probability that a randomly chosen skydiver jumped from the aeroplane at an altitude between 13 000 and 15 000 feet.
> 
> **Answer:**
> 
> ![1x0Cpl4~_3-1-1-fig2-we-solution-part-1](assets/a45c77609405-1x0cpl4-3-1-1-fig2-we-solution-part-1.png)
> 
> ![3-1-1-fig2-we-solution-part-2](assets/f1d3027c1643-image.bin)

> **Exam Hint**
> - Most probability questions are in context so can be long and wordy; go back and re-read the question, several times, whenever you need to
> - Try to get immersed in the context of the question to help understand a problem

## Independent & Mutually Exclusive Events

> **Spec point** — `spcpt_xPq8dPj856nqvFQ3`

## Independent & mutually exclusive events

### What are independent events?

- **Independent** ***events***** **do not affect each other
- For two independent events, the probability of one event happening is unaffected by the *outcome* of the other event
- e.g.    The events “rolling a 6 on a dice” and “flipping heads on a coin” are    independent - the outcome “rolling a 6” does not affect the probability of the outcome “heads” (and vice versa)

- For two **independent** events, *A* and *B*

$P(A\mathrm{AND}B)=P(A)\timesP(B)$

- e.g.     $P("6\mathrm{on}a\mathrm{dice}"\mathrm{AND}"\mathrm{heads} \mathrm{on}a\mathrm{coin}")=\frac{1}{6}\times\frac{1}{2}=\frac{1}{12}$

- Independent events could refer to events from different *experiments*

### What are mutually exclusive events?

- **Mutually** **exclusive** **events** cannot occur simultaneously

  - $P(A\mathrm{AND}B)=0$
- For two mutually exclusive events, the outcome of one event means the other event cannot occur e.g.      The events “rolling a 5 on a die” and “rolling a 6 on a die” are mutually exclusive
- For two **mutually** **exclusive** events, *A* and *B*

$P(A\mathrm{OR}B)=P(A)+P(B)$

- e.g.  `straight P left parenthesis " 6 space on space straight a space dice " space bold OR bold space " 5 space on space straight a space dice " right parenthesis equals 1 over 6 plus 1 over 6 equals 2 over 6 space space space space open parentheses 1 third close parentheses`

- **Mutually** **exclusive** events generally refer to events from the same (single trial of an) experiment
- Mutually exclusive events cannot be independent; the outcome of one event means the probability of the other event is zero

### How do I solve problems involving independent and mutually exclusive events?

- Make sure you know the statistical terms – **independent** and **mutually** **exclusive**
- Remember

  - **independence** is **AND** and is $\times$
  - **mutual** **exclusivity** is **OR** and is $+$
- Solving problems will require interpreting the information given and the application of the appropriate formula

  - Information may be explained in words or by diagram(s)
  - (including Venn diagrams – see Revision Note 3.1.2 Venn Diagrams)

- **Showing** or **determining** whether two events are independent or mutually exclusive are also common

  - To do this you would show the relevant formula is true
- **Just for fun …**

- A well-known sports TV broadcaster used to advertise their football matches as either “Live and exclusive” or “Exclusively live” – can you tell the difference?

- “Live and exclusive” meant that the broadcaster was airing the football match live and was the only broadcaster allowed to air any of the match at any time. “Exclusively live” meant that the broadcaster was the only one airing the football match live, but other broadcasters would be able to air any of the match afterwards.

> **Worked Example**
> (a) Two events, $Q$ and $R$ are such that $P(Q)=0.8$ and $P(QandR)=0.1$. Given that $Q$ and $R$ are independent, find $P(R)$
> 
> (b) Two events, $S$ and $T$ are such that $P(S)=2P(T)$ . Given that $S$ and $T$ are mutually exclusive and that $P(SorT)=0.6$ find $P(S)$ and $P(T)$.
> 
> (c) A fair five-sided spinner has sides labelled 2, 3, 5, 7, 11. Find the probability that the spinner lands on a number greater than 5.
> 
> **Answer:**
> 
> ![3-1-1-fig3-we2-solution](assets/9198d10c5764-image.bin)

> **Exam Hint**
> - Try to rephrase questions in your head in terms of **AND** and/or **OR** ! e.g.      A fair six-sided die is rolled and a fair coin is flipped.            “Find the probability of obtaining a prime number with heads.”
> 
> would be
> 
> “Find the probability of rolling a 2 **OR** a 3 **OR** a 5 **AND** heads.”
