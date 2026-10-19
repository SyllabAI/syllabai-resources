---
note_id: "rn_c2m93xXbwc8GhmJb"
title: "Logarithms"
source: https://www.savemyexams.com/igcse/maths/cie/international-maths/23/extended/revision-notes/algebra-and-sequences/exponentials-and-logarithms/logarithms
path: algebra-and-sequences/exponentials-and-logarithms/logarithms
updated_at: "2025-06-06T07:22:43.690Z"
spec_point_ids: ["spcpt_6RvsM8sgsQBvtjGP"]
spec_point_codes: []
guided_study: true
---

# Logarithms

## Logarithms

> **Spec point** — `spcpt_6RvsM8sgsQBvtjGP`

## Logarithms

### What are logarithms?

- A **logarithm** is the** inverse function** of an** exponential function**

  - Making $x$ the subject of $a^{x}=b$ gives `x equals log subscript a open parentheses b close parentheses`
  
    - This is pronounced "log base* a* of *b*"
    - This is the **definition** of a logarithm
    - The number $a$ is called the **base** of the logarithm
- If** no base** is given, it means the** base number is 10**

  - `log open parentheses... close parentheses` means `log subscript 10 open parentheses... close parentheses`
  
    - In the past, this was a common base to use
    - The **log button **on a calculator is always base 10

### How do I interpret logarithms?

- **log base *****a***** of *****b****, *$\mathrm{log}_{a}(b)$,*** ***is the **power** that you raise $a$ to, to get $b$

  - This is the power required to take the small number, $a$, to the big number,* *$b$
  - For example, $\mathrm{log}_{5}125$ is the power needed to get 5 to 125
  
    - The power needed is 3 (because 5<sup>3</sup> = 125)
    - So $\mathrm{log}_{5}125=3$
  - Similarly
  
    - $\mathrm{log}_{5}25=2$
    - $\mathrm{log}_{5}5=1$
    - $\mathrm{log}_{5}1=0$ (as $5^{0}=1$)
  - It works for **negative powers** (reciprocals)
  
    - `log subscript 5 open parentheses 1 fifth close parentheses equals negative 1` (as $\frac{1}{5}=5^{-1}$)
    - `log subscript 5 open parentheses 1 over 25 close parentheses equals log subscript 5 open parentheses 1 over 5 squared close parentheses equals negative 2`
  - It works for **fractional powers** (roots)
  
    - `log subscript 5 open parentheses square root of 5 close parentheses equals 1 half` (as $\sqrt{5}=5^{\frac{1}{2}}$)
    - `log subscript 5 open parentheses cube root of 5 close parentheses equals 1 third`
- Where possible, use a **calculator **to check

  - Use the `log subscript... end subscript open parentheses... close parentheses` button which allows you to **change the base number**
  
    - This is a different button to the log button (base 10)

### How do I convert between logarithms and exponentials?

- `log subscript a open parentheses b close parentheses equals x` and $a^{x}=b$ are mathematically** identical** statements

  - You can convert between the two
- Learn to read `log subscript a open parentheses b close parentheses equals x` as "$x$ is the **power** that you raise $a$ to, to get $b$"

  - This allows you to convert logs to **exponentials **
  
    - $a^{x}=b$
- This also works the other way

  - $a^{x}=b$ means `x equals log subscript a open parentheses b close parentheses`
  
    - Though it is often easier to think of making $x$the **subject**
    - To make $x$ the subject, **take log base *****a*** **of** **both sides**, $\mathrm{log}_{a}$
- This means you can relate logarithms to **exponential graphs**

  - e.g. the graph of $y=3^{x}$ passes through the point `open parentheses x comma space 81 close parentheses`
  
    - $3^{x}=81$ so $x=\mathrm{log}_{3}81=4$

![two exponential graphs; y=3^x and y=2^x](../../../assets/6a9b897d6ece-6-1-1-exponential-functions-fig3.png)

> **Exam Hint**
> In the exam, you can rewrite a logarithm question as an exponential question if you prefer.

### How do I solve equations with logarithms?

- Equations where $x$ is in the power are called **exponential equations**

  - Some can be solved easily **by inspection** (seeing the answer)
  
    - For example, $2^{x}=8$ is solved by $x=3$
  - Others cannot
  
    - For example, $2^{x}=10$
  - These must be solved using logarithms by making $x$ the **subject**
  
    - $2^{x}=10$ means $x=\mathrm{log}_{2}10$
    - Type this into your **calculator **to get $x=3.321928...$
- **Alternatively**, you can also solve equations using** logs of base 10 only**

  - The **rule **for base 10 is if $a^{x}=b$ then $x=\frac{\mathrm{log}b}{\mathrm{log}a}$ where $\mathrm{log}$ means base 10
  - For example, $2^{x}=10$ means $x=\frac{\mathrm{log}10}{\mathrm{log}2}=3.321928...$

> **Exam Hint**
> Whilst you still need to know both methods, mark schemes will accept different correct answers with logarithms, depending on whether you have used logs of base 10 or logs of a different base.

### How do I use logarithms in compound interest questions?

- You can use** logarithms** to work out the power, $n$, in **compound interest** questions

  - e.g.you put £500 into a bank account with 5% interest per year; after how many whole years does it exceed £900?
  
    - $500\times1.05^{n}=900$
    - Make $n$ the subject: $1.05^{n}=\frac{900}{500}=1.8$ so `n equals log subscript 1.05 end subscript open parentheses 1.8 close parentheses` (or $n=\frac{\mathrm{log}1.8}{\mathrm{log}1.05}$)
    - This gives $n=12.047236...$ so $n=13$ years
    - (it has not **exceeded** 900 after 12 years)

### How do I find inverse functions using logarithms?

- For **exponential functions**, you can use** logarithms** to find their **inverse functions**

  - Use the standard process for finding inverse functions
  - e.g. `straight f open parentheses x close parentheses equals 2 to the power of 4 x end exponent`
  
    - $y=2^{4x}$ then swap $x$ and $y$ to get $x=2^{4y}$
    - Make $4y$ the subject using logarithms: $4y=\mathrm{log}_{2}x$
    - Finally make $y$ the subject to give `straight f to the power of negative 1 end exponent open parentheses x close parentheses equals 1 fourth log subscript 2 x`

> **Worked Example**
> (a) Solve the equation $4^{x}=20$, giving your answer correct to 3 significant figures.
> 
> > *Method 1*
> 
> > *To make *$x$* the subject, take log base 4 of both sides*
> 
> `x equals log subscript 4 open parentheses 20 close parentheses`
> 
> > *Use the *`log subscript... end subscript open parentheses... close parentheses`* button on your calculator to find *$x$
> 
> $x=2.1609640...$
> 
> > *Round to 3 significant figures*
> 
> **Final answer:** $x=2.16$** to 3 s.f.**
> 
> > *Method 2*
> 
> > *Using logs of base 10, solve *$a^{x}=b$* by using  *$x=\frac{\mathrm{log}b}{\mathrm{log}a}$* *
> 
> $x=\frac{\mathrm{log}20}{\mathrm{log}4}$
> 
> > *Use the log button on your calculator to find *$x$
> 
> $x=2.1609640...$
> 
> > *Round to 3 significant figures*
> 
> **Final answer:** $x=2.16$** to 3 s.f.**
> 
> (b) Without using a calculator, solve the equation `log open parentheses 8 x close parentheses equals 4`
> 
> > *log with no base means log base 10*
> 
> `log subscript 10 open parentheses 8 x close parentheses equals 4`
> 
> > *Rewrite this statement as a exponential relationship*
> *4 is the power that you raise 10 to, to get *$8x$
> 
> $10^{4}=8x$
> 
> > *Simplify and make *$x$* the subject*
> 
> $10000=8x\,\frac{10000}{8}=x$
> 
> $x=1250$
> 
> (c) Make $t$ the subject of `7 to the power of p open parentheses t minus 1 close parentheses end exponent equals 2 q`
> 
> > *Take log base 7 of both sides*
> 
> `p open parentheses t minus 1 close parentheses equals log subscript 7 open parentheses 2 q close parentheses`
> 
> > *Rearrange to make *$t$* the subject*
> *Start by dividing both sides by *$p$
> 
> `t minus 1 equals 1 over p log subscript 7 open parentheses 2 q close parentheses`
> 
> > *Then add 1 to both sides*
> 
> `t equals 1 plus 1 over p log subscript 7 open parentheses 2 q close parentheses`
> 
> > `t equals 1 plus fraction numerator log space open parentheses 2 q close parentheses over denominator p log space 7 end fraction`* in base 10 is also accepted*
