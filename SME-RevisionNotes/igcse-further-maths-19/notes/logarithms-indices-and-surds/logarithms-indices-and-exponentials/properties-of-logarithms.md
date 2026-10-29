---
note_id: "rn_6BPd2sq7cYs7mvXv"
title: "Properties of Logarithms"
source: https://www.savemyexams.com/igcse/further-maths/edexcel/19/revision-notes/logarithms-indices-and-surds/logarithms-indices-and-exponentials/properties-of-logarithms
path: logarithms-indices-and-surds/logarithms-indices-and-exponentials/properties-of-logarithms
updated_at: "2024-10-16T15:04:45.696Z"
spec_point_ids: ["spcpt_kcmqw6MvM9Yf43W8", "spcpt_rY2z2249fyCsQx3n"]
spec_point_codes: []
guided_study: false
---

# Properties of Logarithms

## Laws of Logarithms

> **Spec point** — `spcpt_kcmqw6MvM9Yf43W8`

## Laws of Logarithms

### What are the laws of logarithms?

- **Laws of logarithms** allow you to **simplify** and **manipulate** expressions involving logarithms

  - They can help with **solving** exponential and logarithmic **equations**
  - The laws of logarithms are closely related to the **laws of indices**
- You **need to know** the following laws, which are valid for $a,x,y>0$*,* $a\neq1$:

  - $\mathrm{log}_{a}xy=\mathrm{log}_{a}x+\mathrm{log}_{a}y$
  
    - "log of a product is equal to the sum of the logs"
    - This relates to $a^{m}\timesa^{n}=a^{m+n}$
  - $\mathrm{log}_{a}\frac{x}{y}=\mathrm{log}_{a}x-\mathrm{log}_{a}y$
  
    - "log of a division is equal to the difference of the logs"
    - This relates to $a^{m}\diva^{n}=a^{m-n}$
  - $\mathrm{log}_{a}x^{k}=k\mathrm{log}_{a}x$
  
    - "power in a log may be brought down as a multiplier in front of the log"
    - note that  $log_{a} x^{k} = log_{a} ( x^{k} )$
    - This relates to $(a^{m})^{n}=a^{mn}$
  - $\mathrm{log}_{a}a=1$
  
    - This relates to  $a^{1}=a$
  - $\mathrm{log}_{a}1=0$
  
    - This relates to  $a^{0=1}$
- **Be careful**

  - With the **first two laws** the logs on the right-hand side must have the **same base**
  
    - Logs with **different bases** cannot be combined using those laws
  - Also **note the following** (students often make these mistakes on the exam):
  
    - $log_{a} ( x + y )$** **is **not equal** to $\mathrm{log}_{a}x+\mathrm{log}_{a}y$
    - $log_{a} ( x - y )$ is **not equal** to $\mathrm{log}_{a}x-\mathrm{log}_{a}y$

### What are some other useful properties of logarithms?

- You should also **be familiar** with the following **properties** of logarithms

  - $\mathrm{log}_{a}a^{k}=k$
  
    - This can be derived from the third and fourth laws above
  - $\mathrm{log}_{a}\frac{1}{x}=-\mathrm{log}_{a}x$
  
    - Because $log_{a} \frac{1}{x} = log_{a} ( x^{- 1} )$
    - Then use the third law above
  - $log_{a} ( a^{x ) = a^{\log }_{a} x} = x$
  
    - Because $\mathrm{log}_{a}x$ and $a^{x}$ are inverse functions
    - "log cancels exponential and exponential cancels log"
- Also remember that $\mathrm{ln}x$ is another way of writing $\mathrm{log}_{e}x$

  - All the laws and properties apply to $\mathrm{ln}x$ as well
  - This includes  $\ln ( \mathrm{e}^{x ) = \mathrm{e}^{\ln } x} = x$

> **Exam Hint**
> - Make sure you know the laws and properties of logarithms
> 
>   - They are not included on the exam formula sheet

> **Worked Example**
> (a) Write the expression  $2\mathrm{log}_{3}4-\mathrm{log}_{3}2$  in the form  $\mathrm{log}_{3}p$,  where $p$ is an integer.
> 
> > *First use* $\mathrm{log}_{a}x^{k}=k\mathrm{log}_{a}x$ *to rewrite* $2\mathrm{log}_{3}4$
> 
> $\begin{gathered} 2 log_{3} 4 & = log_{3} 4^{2} \\ = log_{3} 16 \end{gathered}$
> 
> > *Substitute that into the original expression*
> *Then use* $\mathrm{log}_{a}\frac{x}{y}=\mathrm{log}_{a}x-\mathrm{log}_{a}y$ *to simplify*
> 
> > $\begin{gathered} 2 log_{3} 4 - log_{3} 2 & = log_{3} 16 - log_{3} 2 \\ = log_{3} \frac{16}{2} \\ = log_{3} 8 \end{gathered}$
> *That's in the required form with* $p=8$
> 
> $\mathrm{log}_{3}8$
> 
> (b) Hence solve  $2\mathrm{log}_{3}4-\mathrm{log}_{3}2=-\mathrm{log}_{3}\frac{1}{x}$.
> 
> > *First use* $\mathrm{log}_{a}x^{k}=k\mathrm{log}_{a}x$ *to rewrite* $-\mathrm{log}_{3}\frac{1}{x}$
> 
> > *Note that* $( \frac{1}{x} ) ^{ - } 1 = \frac{1}{ ( \frac{1}{x} ) } = x$
> 
> $\begin{array}{rcl} - log_{3} \frac{1}{x} & = log_{3} ( \frac{1}{x} )^{- 1} \\ = log_{3} x \end{array}$
> 
> > *Substitute that, and your answer from part (a), into the equation and solve for* $x$
> 
> $\begin{gathered} 2 log_{3 } 4 - log_{3} 2 & = - log_{3} \frac{1}{x} \\ \\ log_{3} 8 & = log_{3} x \end{gathered}$
> 
> $x=8$

## Change of Base

> **Spec point** — `spcpt_rY2z2249fyCsQx3n`

## Change of Base

### Why change the base of a logarithm?

- The **laws of logarithms** can only be used if the logs have the same** base**

  - If a problem involves logarithms with **different bases**
  
    - you can **change the base(s)** of the logarithm(s)
    - and then **apply** the logarithm laws
- **Changing the base **can also allow a log problem to be solved **without a calculator**

  - **Choose** a base that allows you to solve the problem using the equivalent **exponent**

### How do I change the base of a logarithm?

- The **formula** for **changing the base** of a logarithm is

  - $\mathrm{log}_{a}x=\frac{\mathrm{log}_{b}x}{\mathrm{log}_{b}a}$

- This is on the **formula sheet** in the exam paper

  - So you don't need to remember it
  - But you do need to be able to use it
- The change of base formula also leads to the following **useful result:**

  - $\mathrm{log}_{a}b=\frac{1}{\mathrm{log}_{b}a}$
  
    - This is not on the formula sheet
    - But it can be derived from the change of base formula:

$\mathrm{log}_{a}b=\frac{\mathrm{log}_{b}b}{\mathrm{log}_{b}a}=\frac{1}{\mathrm{log}_{b}a}$

> **Exam Hint**
> - Changing the base is a key skill
> 
>   - Make sure you are confident with using it!
> - If you get stuck on a logarithm question, stop and think whether change of base would help
> 
>   - And don't forget that the formula is on the exam formula sheet!

> **Worked Example**
> Solve the equation
> 
> $\mathrm{log}_{4}x+\mathrm{log}_{32}x+\mathrm{log}_{2}x=\frac{34}{5}$
> 
> Show your working clearly.
> 
> > $4$ *and* $32$ *are both powers of 2*
> 
> > *So use* $\mathrm{log}_{a}x=\frac{\mathrm{log}_{b}x}{\mathrm{log}_{b}a}$ *with* $b=2$
> 
> > *This will make ALL the logarithms have a base of* $2$
> 
> $\mathrm{log}_{4}x=\frac{\mathrm{log}_{2}x}{\mathrm{log}_{2}4}$
> 
> $\mathrm{log}_{32}x=\frac{\mathrm{log}_{2}x}{\mathrm{log}_{2}32}$
> 
> > *Substitute into the equation*
> 
> $\frac{\mathrm{log}_{2}x}{\mathrm{log}_{2}4}+\frac{\mathrm{log}_{2}x}{\mathrm{log}_{2}32}+\mathrm{log}_{2}x=\frac{34}{5}$
> 
> > $\mathrm{log}_{2}4=2$ *because* $2^{2}=4$ *(by the definition of a logarithm)*
> 
> > $\mathrm{log}_{2}32=5$ *because* $2^{5}=32$
> 
> > *Substitute into the equation and collect terms on the left-hand side*
> 
> $\begin{gathered} \frac{log_{2} x}{2} + \frac{log_{2} x}{5} + log_{2} x & = \frac{34}{5} \\ ( 1 \frac{1}{2} + 1 \frac{1}{5} + 1 ) log_{2} x & = \frac{34}{5} \\ \frac{17}{10} log_{2} x & = \frac{34}{5} \end{gathered}$
> 
> > *Multiply both sides by* $\frac{10}{17}$ *to find the value of* $\mathrm{log}_{2}x$
> 
> $\begin{gathered} log_{2} x & = \frac{10}{17} \times \frac{34}{5} = 4 \end{gathered}$
> 
> > *By the definition of a logarithm,* $\mathrm{log}_{2}x=4$ *is equivalent to* $x=2^{4}$*   *
> 
> $x=2^{4}$
> 
> $x=16$
