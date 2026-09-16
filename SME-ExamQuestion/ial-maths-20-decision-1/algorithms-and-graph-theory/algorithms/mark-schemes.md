# Mark Schemes — Algorithms
**Algorithms & Graph Theory** · Edexcel International A Level (IAL) Maths (YMA01) — Decision 1


## Q1 — medium — 15 marks · exam-questions

### 3((a)) — 3 marks
First-fit takes the numbers in the order given and puts each one into the first bin with room for it

A bin only ever holds a total of 33, so keep a running total for each bin as you go

12.1 opens Bin 1, and 9.3 fits alongside it, but 15.7 would take Bin 1 to 37.1 and so opens Bin 2

10.9 goes back into Bin 1, which reaches 32.3, and 17.4 fits in neither of the first two bins, so it opens Bin 3

6.4 returns to Bin 2, 20.1 opens Bin 4, and 7.9 completes Bin 2 at exactly 30.0

8.1 joins 17.4 in Bin 3, and 14.0 fits nowhere, since Bin 4 would reach 34.1, so it opens Bin 5

**Final answer:** **Bin 1: 12.1, 9.3, 10.9**

**Final answer:** **Bin 2: 15.7, 6.4, 7.9**

**Final answer:** **Bin 3: 17.4, 8.1**

**Final answer:** **Bin 4: 20.1**

**Final answer:** **Bin 5: 14.0**

**[M1 A1 A1]**

> **[mark-scheme]**
> **M1**: Places the first four numbers correctly, so Bin 1 is correct and 15.7 is in Bin 2, and puts at least seven of the numbers into bins.
> 
> **A1**: Places the first eight numbers correctly, so Bins 1 and 2 are correct, 17.4 is in Bin 3 and 20.1 is in Bin 4.
> 
> **A1**: All ten numbers placed correctly.
> 
> Writing cumulative totals beside each bin instead of the numbers themselves is condoned for the method mark, but not for either accuracy mark.
> 
> The three marks are staged, so a slip partway through the list still earns whatever was correct before it.

> **[exam-tip]**
> First-fit never revisits a decision, so always start again at Bin 1 for each new number rather than carrying on from the bin you have just filled. Numbers 10.9, 6.4, 7.9 and 8.1 all go back into earlier bins here.
> 
> - Write the running total beside each bin and update it as you add, so checking whether the next number fits is one subtraction rather than a re-addition
> - Five bins is not a failure: first-fit is quick rather than efficient, and part (d) shows what a little sorting saves

### 3() — 4 marks
**(i)**

A bubble sort compares each neighbouring pair in turn, swapping them whenever they are in the wrong order

The list is being sorted into descending order, so a pair is swapped whenever the left number is the smaller

The first pass makes nine comparisons and carries the smallest number, 6.4, all the way to the right-hand end

*12.1, 15.7, 10.9, 17.4, 9.3, 20.1, 7.9, 8.1, 14.0, 6.4*

**[M1]**

The second pass needs only eight comparisons, because the last number is already in its final place

**Final answer:** **15.7, 12.1, 17.4, 10.9, 20.1, 9.3, 8.1, 14.0, 7.9, 6.4**

**[A1]**

**(ii)**

Count the comparisons first: nine on the first pass and eight on the second

$9 + 8$

$\text{total number of comparisons} = 17$

**[B1]**

Now count the swaps, which are the pairs that actually changed places: seven on the first pass and five on the second

$7 + 5$

$\text{total number of swaps} = 12$

**[B1]**

> **[mark-scheme]**
> **M1**: A correct first pass of a bubble sort.
> 
> **A1**: Both passes correct. Any additional passes written down are ignored.
> 
> **B1**: The total number of comparisons, 17.
> 
> **B1**: The total number of swaps, 12.
> 
> Both totals must be the correct answers, with no follow through.
> 
> If neither B mark is earned, one mark for each is still available where the correct numbers, 9 and 8 for the comparisons and 7 and 5 for the swaps, are referred to but not summed.

> **[exam-tip]**
> The number of comparisons on a pass never depends on the numbers, only on how much of the list is still unsorted: with ten numbers a first pass is always nine comparisons and a second always eight.
> 
> - Swaps have to be counted as you make them, so put a tick above each pair you exchange rather than trying to recover the count afterwards
> - Descending order reverses the test, so you swap when the left number is smaller, which is the opposite of the ascending sort most students practise first

### 3((c)) — 4 marks
A quick sort picks a pivot, then splits the list into the numbers that belong before it and the numbers that belong after it

The specification fixes the pivot as the middle item, which is at position $\frac{1}{2} ( N + 1 )$ when $N$ is odd and $\frac{1}{2} ( N + 2 )$ when $N$ is even

The list is being sorted into descending order, so the larger numbers go to the left of the pivot

Pivots are shown in brackets, and every pivot already placed stays fixed for the rest of the sort

Ten numbers gives a first pivot at position 6, which is 6.4

*12.1, 9.3, 15.7, 10.9, 17.4, (6.4), 20.1, 7.9, 8.1, 14.0*

Nothing is smaller than 6.4, so the whole list moves to its left; the next sublist has nine numbers and a pivot at position 5

*12.1, 9.3, 15.7, 10.9, (17.4), 20.1, 7.9, 8.1, 14.0, 6.4*

**[M1]**

Only 20.1 is larger than 17.4; the sublist to the right has seven numbers, so its pivot is at position 4

*(20.1), 17.4, 12.1, 9.3, 15.7, (10.9), 7.9, 8.1, 14.0, 6.4*

**[A1]**

20.1 is alone and so needs no further sorting, and 10.9 splits the rest into two sublists of three, each with its pivot at position 2

*20.1, 17.4, 12.1, (15.7), 14.0, 10.9, 9.3, (7.9), 8.1, 6.4*

Each of those pivots leaves a sublist of two, whose pivot is the second number

*20.1, 17.4, 15.7, 12.1, (14.0), 10.9, 9.3, (8.1), 7.9, 6.4*

**[A1]**

No sublist now holds more than one number, so the sort is complete

**Final answer:** **20.1, 17.4, 15.7, 14.0, 12.1, 10.9, 9.3, 8.1, 7.9, 6.4**

**[A1]**

> **[mark-scheme]**
> **M1**: Chooses a pivot and produces a first pass giving the numbers above the pivot, then the pivot, then the numbers below it. The pivot must be the middle left or the middle right item; choosing the first or the last item scores nothing.
> 
> **A1**: First and second passes correct, and the pivots for the third pass chosen correctly. The third pass does not itself have to be correct for this mark.
> 
> **A1**: Third and fourth passes correct, and the pivots for the fifth pass chosen correctly. Allow follow through from your own second pass and choice of pivots.
> 
> **A1**: A fully correct solution, with every earlier mark in this part also earned, and the sort shown to be complete.
> 
> Choosing only one pivot per iteration, rather than one in each sublist, limits this part to the method mark.
> 
> Completion can be shown by rewriting the final list, by stating that the list is sorted, or by every number having actually been used as a pivot rather than merely being in the right place.
> 
> This specification defines the middle item as position one half of $N + 1$ for an odd number of items and one half of $N + 2$ for an even number, which gives the middle right item. This scheme also accepts the middle left item, provided the choice is made consistently.

> **[exam-tip]**
> After the first pass every sublist is sorted independently, and each one chooses its own pivot, so from the third pass onwards you are usually picking two or three pivots at a time. Picking only one is the commonest way to lose three of these four marks.
> 
> - Recount the length of each sublist before picking its pivot, because the position rule is applied to the sublist and not to the original ten numbers
> - Underline or bracket a pivot as soon as it is placed, so you can see at a glance which numbers are still in play
> - The sort is not finished when the list merely looks sorted; it is finished when no sublist holds more than one number, and the final mark depends on saying so

### 3((d)) — 3 marks
First-fit decreasing runs exactly the same procedure as part (a), but on the sorted list rather than the original one

Working from the largest number down means the big awkward numbers are placed while the bins are still empty

20.1 opens Bin 1, 17.4 opens Bin 2 and 15.7 opens Bin 3, since no two of them fit together in a bin of 33

14.0 joins 17.4 in Bin 2, reaching 31.4, and 12.1 joins 20.1 in Bin 1, reaching 32.2

10.9 goes into Bin 3, and 9.3 fits in none of the first three bins, so it opens Bin 4

8.1 and 7.9 follow it into Bin 4, and 6.4 fills Bin 3 to exactly 33

**Final answer:** **Bin 1: 20.1, 12.1**

**Final answer:** **Bin 2: 17.4, 14.0**

**Final answer:** **Bin 3: 15.7, 10.9, 6.4**

**Final answer:** **Bin 4: 9.3, 8.1, 7.9**

**[M1 A1 A1]**

> **[mark-scheme]**
> **M1**: Uses a list sorted into decreasing order, places the first four numbers correctly and puts at least seven of them into bins.
> 
> **A1**: Places the first eight numbers correctly.
> 
> **A1**: All ten numbers placed correctly.
> 
> Applying first-fit to an increasing list earns nothing here. The sorted list is judged independently of part (c), so full marks are available even if your part (c) ended with an incorrect list.
> 
> Where the list you carry forward contains one error, such as a missing number, an extra number or one number out of place, only the method mark is available. More than one error earns nothing.
> 
> Writing cumulative totals beside each bin instead of the numbers is condoned for the method mark only.

> **[exam-tip]**
> Sorting first saves a whole bin here, five down to four, which is the point the pairing of parts (a) and (d) is making.
> 
> - Copy the sorted list out again before you start packing, because a single transcription slip costs two of the three marks

### 3((e)) — 1 marks
Dividing the total of all ten numbers by the bin size gives a lower bound for how many bins could possibly be enough

Add the ten numbers first

$12 . 1 + 9 . 3 + 15 . 7 + 10 . 9 + 17 . 4 + 6 . 4 + 20 . 1 + 7 . 9 + 8 . 1 + 14 . 0 = 121 . 9$

Now divide by the bin size of 33

$\frac{121.9}{33} \approx 3 . 694$

Bins come whole, so this rounds up to a lower bound of 4 bins

**Final answer:** **Part (d) used 4 bins, which is the lower bound, so it does use the minimum possible number of bins**

**[B1]**

> **[mark-scheme]**
> **B1**: The calculation, together with the value 4 and a correct conclusion. Accept the division written as 121.9 over 33, or an answer rounding to 3.7, or 3.6 where the correct calculation is shown alongside it.
> 
> Both halves are needed. A correct calculation reaching 4 with no conclusion at all earns nothing, and as a minimum the conclusion must say yes.
> 
> Allow follow through, so the conclusion is judged against your own answer to part (d) rather than against four bins.

> **[exam-tip]**
> A lower bound only tells you that fewer bins is impossible. It cannot promise that the bound is achievable, so it settles the question only when your packing has already matched it, as it does here.
> 
> - Always round the division up, never to the nearest whole number: 3.694 bins means 4
> - The single mark covers both the arithmetic and the conclusion, so answering with a bare 3.694, or a bare yes, scores nothing

## Q2 — medium — 13 marks · exam-questions

### 3((a)) — 3 marks
First-fit works along the list in the order given, putting each number into the first bin that still has room for it

Each bin holds at most 5, so keep a running total beside each one

1.8 and 1.4 open Bin 1, and 2.6 will not fit alongside them, so it opens Bin 2

1.6 goes back into Bin 1, bringing it to 4.8, and 2.8 fits in neither of the first two bins, so it opens Bin 3

0.9 joins Bin 2 at 3.5, then 3.1 opens Bin 4 and 0.8 returns to Bin 2 at 4.3

1.2 goes into Bin 3, 2.4 fits nowhere and opens Bin 5, and 0.6 finishes Bin 2 at 4.9

**Final answer:** **Bin 1: 1.8, 1.4, 1.6**

**Final answer:** **Bin 2: 2.6, 0.9, 0.8, 0.6**

**Final answer:** **Bin 3: 2.8, 1.2**

**Final answer:** **Bin 4: 3.1**

**Final answer:** **Bin 5: 2.4**

**[M1 A1 A1]**

> **[mark-scheme]**
> **M1**: Places the first four values correctly, so Bin 1 is correct and 2.6 is in Bin 2, and puts at least eight of the values into bins.
> 
> **A1**: Places the first eight values correctly, with all eleven values placed and none of them repeated or incorrect.
> 
> **A1**: A fully correct solution, with no extra or repeated values. This mark depends on both previous marks.
> 
> Writing cumulative totals beside each bin instead of the values themselves is condoned for the method mark only.
> 
> A repeated or incorrect value anywhere costs the first accuracy mark even when the first eight values are placed correctly.

> **[exam-tip]**
> Every number must appear exactly once across the bins. Copying a value twice is the single commonest way to lose both accuracy marks here, and it costs them even when the packing itself is right.
> 
> - Tick each number off the printed list as you place it, which catches a repeat at the moment you make it
> - Go back to Bin 1 for every new number: 1.6, 0.9, 0.8, 1.2 and 0.6 all return to earlier bins

### 3() — 3 marks
**(i)**

A bubble sort compares each neighbouring pair along the list and swaps the pair whenever it is the wrong way round

The list is being sorted into descending order, so a pair is swapped whenever the left number is the smaller

With eleven numbers the first pass makes ten comparisons and carries the smallest number, 0.6, to the right-hand end

**Final answer:** **1.8, 2.6, 1.6, 2.8, 1.4, 3.1, 0.9, 1.2, 2.4, 0.8, 0.6**

**[B1]**

**(ii)**

Every neighbouring pair is compared once, and with eleven numbers there are ten such pairs

$\text{number of comparisons} = 10$

**[B1]**

A swap only happens where the pair was the wrong way round, which here is six of those ten comparisons

$\text{number of swaps} = 6$

**[B1]**

> **[mark-scheme]**
> **B1**: The correct list at the end of one complete pass. Anything written after that is ignored.
> 
> **B1**: The number of comparisons, 10.
> 
> **B1**: The number of swaps, 6.
> 
> Show the state of the list only after the pass is finished. Writing out every individual swap, or carrying on into a second pass, makes it unclear where the first pass ended. The position of 0.8, second from the right-hand end, is the quickest check that exactly one pass has been completed.
> 
> Where the two numbers are given without labels, the first is taken as the comparisons and the second as the swaps. Writing 6 then 10 therefore earns only the first of these two marks.

> **[exam-tip]**
> Label the two numbers. The order is what is marked when they are unlabelled, so an unlabelled 6, 10 loses a mark that a labelled one keeps.
> 
> - The comparison count never depends on the numbers themselves: a first pass through a list of eleven is always ten comparisons
> - Write only the finished list, not the list part-way through, because a pass shown mid-swap cannot earn the first mark

### 3((c)) — 4 marks
A quick sort chooses a pivot, then splits the list into the numbers that belong before it and the numbers that belong after it

The specification fixes the pivot as the middle item, at position $\frac{1}{2} ( N + 1 )$ when $N$ is odd and $\frac{1}{2} ( N + 2 )$ when $N$ is even

The list is being sorted into descending order, so the larger numbers go to the left of the pivot

Pivots are shown in brackets, and each one stays fixed once placed

Eleven numbers gives a first pivot at position 6, which is 1.4

*2.6, 1.8, 2.8, 1.6, 3.1, (1.4), 1.2, 2.4, 0.9, 0.8, 0.6*

That leaves a sublist of six on the left, with its pivot at position 4, and a sublist of four on the right, with its pivot at position 3

*2.6, 1.8, 2.8, (1.6), 3.1, 2.4, 1.4, 1.2, 0.9, (0.8), 0.6*

**[M1 A1]**

Nothing in the left sublist is smaller than 1.6, so it moves across whole; on the right, 0.6 is left alone and needs no sorting

*2.6, 1.8, (2.8), 3.1, 2.4, 1.6, 1.4, 1.2, (0.9), 0.8, (0.6)*

3.1 and 1.2 are now alone as well, and 1.8 is the pivot of the three numbers left in the middle

*(3.1), 2.8, 2.6, (1.8), 2.4, 1.6, 1.4, (1.2), 0.9, 0.8, 0.6*

**[A1]**

Only 2.6 and 2.4 are still unsorted, and their pivot is the second of the two

*3.1, 2.8, 2.6, (2.4), 1.8, 1.6, 1.4, 1.2, 0.9, 0.8, 0.6*

No sublist now holds more than one number, so the sort is complete

**Final answer:** **3.1, 2.8, 2.6, 2.4, 1.8, 1.6, 1.4, 1.2, 0.9, 0.8, 0.6**

**[A1]**

> **[mark-scheme]**
> **M1**: Chooses a pivot and produces a first pass reading the values greater than the pivot, then the pivot, then the values less than it. The pivot must be the middle left or the middle right item; choosing the first or the last item scores nothing.
> 
> **A1**: First pass correct, with consistent pivots chosen for the second pass.
> 
> **A1**: Second and third passes correct. Allow follow through from your own first pass and choice of pivots, provided the second-pass pivots are consistent, either both middle left or both middle right.
> 
> **A1**: A fully correct solution with every earlier mark in this part also earned. Taking the middle right item, a fifth pass must actually be shown; stating that the sort is complete after the fourth pass is not enough. Taking the middle left item throughout, a fourth pass is what must be shown.
> 
> Choosing only one pivot per iteration, rather than one in each sublist, limits this part to the method mark.
> 
> Sorting into ascending order instead earns at most two marks, and reversing the list at the end does not recover the others.
> 
> Where the list you start from carries a single error, such as one missing, extra, transposed or incorrect number, at most the method mark and the follow-through accuracy mark are available.

> **[exam-tip]**
> Consistency is marked as heavily as correctness here: having taken the middle right item once, take it every time, in every sublist. A solution that alternates cannot earn the second accuracy mark even where each individual pass is right.
> 
> - Recount each sublist before choosing its pivot, since the position rule applies to the sublist and not to the eleven original numbers
> - A sublist of one needs no pivot and no sorting, but writing it in brackets, as with 0.6, 3.1 and 1.2 here, keeps the bookkeeping visible
> - Taking the middle right item needs five passes, so do not stop at the fourth: the final mark depends on the fifth pass appearing

### 3((d)) — 3 marks
First-fit decreasing is the same procedure as part (a), applied to the sorted list from part (c)

3.1 opens Bin 1, 2.8 opens Bin 2 and 2.6 opens Bin 3, since no two of them fit together in a bin of 5

2.4 joins 2.6 in Bin 3, filling it to exactly 5, and 1.8 joins 3.1 in Bin 1 at 4.9

1.6 goes into Bin 2 at 4.4, and 1.4 fits in none of the first three bins, so it opens Bin 4

1.2 and 0.9 follow it into Bin 4, then 0.8 brings Bin 4 to 4.3, and 0.6 completes Bin 2 at exactly 5

**Final answer:** **Bin 1: 3.1, 1.8**

**Final answer:** **Bin 2: 2.8, 1.6, 0.6**

**Final answer:** **Bin 3: 2.6, 2.4**

**Final answer:** **Bin 4: 1.4, 1.2, 0.9, 0.8**

**[M1 A1 A1]**

> **[mark-scheme]**
> **M1**: Places the five largest values correctly and puts at least eight of the values into bins. Remember a bin holds at most 5.
> 
> **A1**: Places the first eight values correctly, with none of them repeated or incorrect.
> 
> **A1**: A fully correct solution, with no extra or repeated values. This mark depends on both previous marks.
> 
> Applying first-fit to an increasing list earns nothing. Where no sort appears in part (c) at all, this part is marked assuming the correct sorted list has been used.
> 
> Writing cumulative totals beside each bin instead of the values is condoned for the method mark only.

> **[exam-tip]**
> Sorting first saves a bin here, five down to four, and it also fills two of them exactly: Bin 2 and Bin 3 both reach 5 with nothing to spare.
> 
> - Check the five largest values first, because the method mark turns on those alone

## Q3 — medium — 9 marks · exam-questions

### 1((a)) — 2 marks
A lower bound comes from the total weight: even if every truck were filled exactly to its limit, this many trucks would still be needed

Add the ten crate weights

$175 + 135 + 210 + 105 + 100 + 150 + 60 + 20 + 70 + 125 = 1150$

Divide the total by the capacity of one truck

$\frac{1150}{300} = 3 . 83 \dots$

Trucks come whole, so round up rather than to the nearest whole number

$\text{lower bound} = 4  \text{trucks}$

**[M1 A1]**

> **[mark-scheme]**
> **M1**: Attempts the total weight divided by 300. A value of 3.83 or better seen with no working can imply this mark.
> 
> **A1**: The correct calculation, or 3.83 or better, followed by a lower bound of 4.
> 
> An answer of 4 with no working at all scores nothing. Writing only 3.8 followed by 4 earns the method mark but not the accuracy mark, so the second decimal place is worth having.

> **[exam-tip]**
> The division almost never comes out whole, and the answer is always the value rounded up, never rounded to the nearest whole number. Here 3.83 gives 4, and it would still give 4 at 3.1.
> 
> - Quote at least two decimal places, since 3.8 costs the accuracy mark where 3.83 keeps it
> - A lower bound says only that fewer trucks is impossible; it does not promise that four trucks can actually be loaded, which is what part (c) goes on to show

### 1((b)) — 4 marks
A bubble sort compares each neighbouring pair along the list and swaps any pair that is the wrong way round

The weights are wanted in descending order, so a pair is swapped whenever the left weight is the smaller

Each pass carries the smallest weight still loose to the right-hand end, so after each pass one more weight is fixed there

*175, 210, 135, 105, 150, 100, 60, 70, 125, 20*

**[M1]**

20 is now fixed, so the second pass stops one place earlier

*210, 175, 135, 150, 105, 100, 70, 125, 60, 20*

*210, 175, 150, 135, 105, 100, 125, 70, 60, 20*

**[A1]**

Only two swaps happen across the next two passes, since most of the list is already in order

*210, 175, 150, 135, 105, 125, 100, 70, 60, 20*

*210, 175, 150, 135, 125, 105, 100, 70, 60, 20*

**[A1]**

The list now looks sorted, but that has to be demonstrated: a further pass makes no swaps at all, which is what ends the algorithm

**Final answer:** **210, 175, 150, 135, 125, 105, 100, 70, 60, 20**

**[A1]**

> **[mark-scheme]**
> **M1**: A bubble sort in a consistent direction, with 20 finishing in place and the list beginning with the correct first five numbers, 175, 210, 135, 105, 150.
> 
> **A1**: First, second and third passes correct, so three numbers finish in place.
> 
> **A1**: Fourth and fifth passes correct. Allow follow through from your own third pass.
> 
> **A1**: A fully correct solution, with a sixth pass shown making no swaps.
> 
> Passes are judged by the numbers rather than by any labels you write. The first time 20 appears at the end of the list is taken as the end of your first pass.
> 
> The sixth pass must be a genuine pass. Simply writing the list out again after the fifth pass does not earn the final mark, although you are given the benefit of the doubt where the passes are unlabelled. Continuing as far as a ninth pass is condoned, provided nothing changes in it.
> 
> Sorting into ascending order earns at most two marks, and reversing the list at the end does not recover the others.

> **[exam-tip]**
> A bubble sort does not stop when the list looks right; it stops when a whole pass passes without a swap. That final unchanged pass is worth a mark of its own here, and it is the one most often left out.
> 
> - Show only the state at the end of each pass, as the question asks, not every individual swap along the way
> - After the fifth pass five numbers are guaranteed fixed at the right-hand end, so a quick check is that each pass should leave one more of them settled

### 1((c)) — 3 marks
First-fit decreasing works down the sorted list from part (b), putting each crate into the first truck that can still take it

Each truck carries at most 300 kg

210, 175 and 150 each open a truck of its own, since no two of them fit together

135 joins 150 in Truck 3 at 285 kg, and 125 completes Truck 2 at exactly 300 kg

105 fits in none of the first three trucks, so it opens Truck 4, and 100 follows it there

70 goes back into Truck 1 at 280 kg, 60 joins Truck 4 at 265 kg, and 20 fills Truck 1 to exactly 300 kg

**Final answer:** **Truck 1: 210, 70, 20**

**Final answer:** **Truck 2: 175, 125**

**Final answer:** **Truck 3: 150, 135**

**Final answer:** **Truck 4: 105, 100, 60**

**[M1 A1 A1]**

> **[mark-scheme]**
> **M1**: Places the first four items correctly and puts at least eight of the values into trucks. Remember the maximum weight of a truck is 300 kg.
> 
> **A1**: Places the first eight items correctly, with no additional or repeated values.
> 
> **A1**: A fully correct solution, with no additional or repeated values.
> 
> Applying first-fit to an increasing list earns nothing here. Where no sort appears in part (b), this part is marked assuming the correct descending list has been used.
> 
> Writing cumulative totals beside each truck instead of the weights is condoned for the method mark only.
> 
> There is no follow through and no allowance for a misread on either accuracy mark. You must be working with the correct ten weights, so any wrong value anywhere in the trucks costs both of them.

> **[exam-tip]**
> Four trucks matches the lower bound from part (a), so this loading is provably the best possible and nothing would be gained by trying to improve it.
> 
> - Two trucks here fill to exactly 300 kg, which is a useful check: if a truck of yours exceeds 300 the packing has gone wrong rather than merely being inefficient
> - The accuracy marks allow no follow through at all, so copy the sorted list carefully before you start placing crates

## Q4 — medium — 11 marks · exam-questions

### 1((a)) — 2 marks
A lower bound comes from the total weight: even if every container were filled exactly to its limit, this many containers would still be needed

Add the ten box weights

$17 + 9 + 15 + 8 + 20 + 13 + 28 + 4 + 12 + 5 = 131$

Divide the total by the capacity of one container

$\frac{131}{40} = 3 . 275$

Containers come whole, so round up rather than to the nearest whole number

$\text{lower bound} = 4  \text{containers}$

**[M1 A1]**

> **[mark-scheme]**
> **M1**: Attempts the total weight divided by 40. A value of 3.275 seen with no accompanying calculation can imply this mark, and so can a clear intention to add all ten weights and divide by 40.
> 
> **A1**: The correct calculation, or the value 3.275, followed by 4.
> 
> An answer of 4 with no working at all scores nothing in this part, so the division has to be visible.

> **[exam-tip]**
> The division almost never comes out whole, and the lower bound is always that value rounded up, never rounded to the nearest whole number. Here 3.275 gives 4, and 3.05 would give 4 as well.
> 
> - Write the division down even if you can do it on a calculator in one step, because the answer alone earns nothing here
> - A lower bound only rules out fewer containers; it does not promise that four can actually be loaded, which is what part (b) goes on to test

### 1((b)) — 3 marks
First-fit works along the list in its original order, putting each box into the first container that still has room for it

Each container holds at most 40 kg

17 opens Container 1, and 9 joins it at 26 kg

15 does not fit alongside them, so it opens Container 2, and 8 goes back into Container 1 at 34 kg

20 fits in neither of the open containers, so it joins 15 in Container 2 at 35 kg

13 fits nowhere either and opens Container 3, and 28 then opens Container 4

4 returns to Container 1 at 38 kg, 12 joins 13 in Container 3 at 25 kg, and 5 fills Container 2 to exactly 40 kg

**Final answer:** **Container 1: 17, 9, 8, 4**

**Final answer:** **Container 2: 15, 20, 5**

**Final answer:** **Container 3: 13, 12**

**Final answer:** **Container 4: 28**

**[M1 A1 A1]**

> **[mark-scheme]**
> **M1**: Places the first four values, 17, 9, 15 and 8, correctly and puts at least eight values into containers.
> 
> **A1**: Places the first eight values, so as far as the 4, correctly.
> 
> **A1**: A fully correct solution.
> 
> The official scheme stages these three marks over one allocation, so all three depend on the same diagram: the method mark on the first four values, the first accuracy mark on the first eight, and the last on all ten.
> 
> Writing cumulative running totals beside each container instead of the weights is condoned for the method mark only.
> 
> Neither accuracy mark is available if any value is repeated, or if more than ten values appear in the containers, even where the first eight are correct. The final mark is also dependent on both of the previous marks being earned.

> **[exam-tip]**
> First-fit means first container with room, not emptiest container, so you always start scanning again from Container 1 for every new box. That is why 8, 4 and 5 all travel backwards into containers opened much earlier.
> 
> - Keep a running total beside each container as you go, but write the weights themselves in the answer, since totals alone cost the accuracy marks
> - Two containers here finish at exactly 40 kg, which is a useful check that nothing has overflowed

### 1((c)) — 3 marks
A quick sort picks a pivot, then splits the list into the numbers that belong before it and the numbers that belong after it

The specification fixes the pivot as the middle item, at position $\frac{1}{2} ( N + 1 )$ when $N$ is odd and $\frac{1}{2} ( N + 2 )$ when $N$ is even

The list is being sorted into ascending order, so the smaller numbers go to the left of the pivot

Pivots are shown in brackets, and every pivot already placed stays fixed for the rest of the sort

Ten numbers gives a first pivot at position 6, which is 13

*17, 9, 15, 8, 20, (13), 28, 4, 12, 5*

Five numbers fall below 13 and four above it, so the next two sublists have five and four numbers, with pivots at positions 3 and 3

*9, 8, (4), 12, 5, 13, 17, 15, (20), 28*

**[M1]**

Nothing is smaller than 4, so its sublist of four passes to its right; 28 is left alone above 20

*4, 9, 8, (12), 5, 13, 17, (15), 20, (28)*

**[A1]**

12 splits its sublist into three numbers below and none above, and 15 leaves only 17 above it

*4, 9, (8), 5, 12, 13, 15, (17), 20, 28*

No sublist now holds more than one number, so the sort is complete

**Final answer:** **4, 5, 8, 9, 12, 13, 15, 17, 20, 28**

**[A1]**

> **[mark-scheme]**
> **M1**: Chooses a pivot and produces a first pass giving the numbers below the pivot, then the pivot, then the numbers above it. The pivot must be the middle left or the middle right item; choosing the first or the last item scores nothing.
> 
> **A1**: The first two passes correct, and the pivots for the third pass chosen correctly. The third pass does not itself have to be correct for this mark.
> 
> **A1**: A fully correct solution.
> 
> Sorting into descending order limits this part to the method mark, even where the list is reversed at the end.
> 
> The method mark can still be earned where exactly one number is missing, incorrect or added to the list; it is lost if more than one number is wrong.
> 
> Choosing only one pivot per iteration, rather than one in each sublist, also limits this part to the method mark.
> 
> The final mark requires the sort to be shown to be complete after the fourth pass, either by writing the sorted list out again or by stating that it is sorted. Underlining the fourth pass is not enough on its own.

> **[exam-tip]**
> Ascending order reverses the split, so the numbers smaller than the pivot go to its left. Everything else about the algorithm is identical to the descending version, and mixing the two up is the commonest way to lose every mark after the first.
> 
> - Recount the length of each sublist before picking its pivot, because the position rule applies to the sublist and not to the original ten numbers
> - From the second pass onwards you choose a pivot in every sublist at once, not one pivot for the whole list
> - Say in words that the sort is complete, or write the finished list out one more time, because the last mark depends on it

### 1((d)) — 3 marks
A binary search repeatedly halves the list, each time throwing away the half that cannot contain the number

It only works on a sorted list, so the ascending list from part (c) is the one to search

The specification fixes the middle item at position $\frac{1}{2} ( N + 1 )$ when $N$ is odd and $\frac{1}{2} ( N + 2 )$ when $N$ is even, so with an even number of items you take the right-hand one of the middle pair

Number the weights 1 to 10 in ascending order, so item 1 is 4 and item 10 is 28

Ten items gives a pivot at position 6, which is 13, and 9 is smaller than 13, so 13 and everything above it goes

*Pivot item 6 (13): reject items 6 to 10*

**[M1]**

Items 1 to 5 are left, which is five items, so the pivot is the third of them, item 3, which is 8

9 is larger than 8, so 8 and everything below it goes

*Pivot item 3 (8): reject items 1 to 3*

**[A1]**

Items 4 and 5 are left, and with two items the pivot is the second of them, item 5, which is 12

*Pivot  item 5 (12): reject item 5*

Only item 4 remains, so it becomes the pivot, and it is the weight being searched for

**Final answer:** **Pivot item 4 (9): the weight 9 has been found**

**[A1]**

> **[mark-scheme]**
> **M1**: Chooses the middle right pivot and makes an attempt at discarding or retaining half the list. Choosing the middle left item, the 12, scores nothing.
> 
> **A1**: The first two passes correct, selecting the 6th item and then working on items 1 to 5 and selecting the 3rd of them, the 8, and rejecting items 1 to 3. The second pass must not still include item 6.
> 
> **A1**: The search completed, rejecting the 12 in the third pass, together with the 9 being found.
> 
> You must be searching a correctly sorted list, 4, 5, 8, 9, 12, 13, 15, 17, 20, 28. If it is clear that some other list is being used, nothing is earned here, and the sixth value of the original unsorted list is 13 too, so the next pivot is usually what shows which list you are working from.
> 
> For the method mark, retaining the wrong half of the list is condoned.
> 
> A list sorted into descending order earns full marks in exactly the same way, but the first pivot is then the 12 and not the 13, since the middle right item must still be chosen.
> 
> It must be clear that the 9 has been found, not just stated as the final value. Saying that once the 12 has been rejected the only value left is the 9, so it has been found, is accepted.

> **[exam-tip]**
> Work in item numbers rather than in weights. Each pivot is then a single short calculation on the first and last positions still in play, and it is much harder to lose track of which part of the list has already gone.
> 
> - Apply the position rule to the sublist you are actually searching, not to the original ten: items 1 to 5 is a list of five, so its middle is the third of those five
> - Rejecting the pivot itself matters as much as rejecting the half, because a pivot that has been used must never reappear in a later pass
> - Finish by saying the number has been found; stopping at the last rejection leaves the final mark on the table

## Q5 — medium — 10 marks · exam-questions

### 7((a)) — 3 marks
The lower bound for the number of bins is the total of the numbers divided by the bin size, rounded up

Add the eleven numbers

$14 + 20 + 23 + 17 + 15 + 22 + 19 + 25 + 13 + 28 + 32 = 228$

Rounding up gives 4 exactly when the quotient is greater than 3 and no greater than 4

$3 < \frac{228}{n} \leq 4$

**[M1]**

The right-hand inequality gives the smallest bin size that could work

$\frac{228}{4} = 57$

The left-hand inequality gives the value the bin size has to stay below

$\frac{228}{3} = 76$

**[A1]**

A bin size of 57 is allowed, since the quotient is then exactly 4, but 76 is not, since the quotient would be exactly 3 and the lower bound would drop to 3

$57 \leq n < 76$

**[A1]**

> **[mark-scheme]**
> **M1**: An equation or inequality linking the expression 228 over $n$ with either 3 or 4.
> 
> **A1**: The correct critical values of 57 and 76, or of 57 and 75.
> 
> **A1**: The completed range, written as 57 is less than or equal to $n$, which is less than 76.
> 
> Because $n$ is a whole number the upper end may equally be written as 75 with a weak inequality, so both forms of the range are accepted, and both forms earn the final mark.

> **[exam-tip]**
> The two ends of the range behave differently, and it is worth thinking about why rather than guessing which inequality is strict. Dividing by exactly 57 gives 4 and rounds up to 4, while dividing by exactly 76 gives 3, which is already a whole number and so stays at 3.
> 
> - Work out both critical values first and decide about the inequality signs afterwards, since that is where the marks separate
> - A lower bound of 4 rules out 3 bins as well as 5, so the condition traps the quotient between two values rather than just below one

### 7((b)) — 4 marks
A quick sort picks a pivot, then splits the list into the numbers that belong before it and the numbers that belong after it

The specification fixes the pivot as the middle item, at position $\frac{1}{2} ( N + 1 )$ when $N$ is odd and $\frac{1}{2} ( N + 2 )$ when $N$ is even

The list is being sorted into descending order, so the larger numbers go to the left of the pivot

Pivots are shown in brackets, and every pivot already placed stays fixed for the rest of the sort

Eleven numbers gives a first pivot at position 6, which is 22

*14, 20, 23, 17, 15, (22), 19, 25, 13, 28, 32*

Four numbers are larger than 22 and six are smaller, so the next two sublists have four and six numbers, with pivots at positions 3 and 4

*23, 25, (28), 32, 22, 14, 20, 17, (15), 19, 13*

**[M1 A1]**

32 is left alone above 28, and 15 splits the lower sublist into three above it and two below

*(32), 28, 23, (25), 22, 20, (17), 19, 15, 14, (13)*

Each of 25, 17 and 13 leaves at most two numbers to sort beside it

*32, 28, 25, (23), 22, 20, (19), 17, 15, (14), 13*

**[A1]**

No sublist now holds more than one number, so the sort is complete

**Final answer:** **32, 28, 25, 23, 22, 20, 19, 17, 15, 14, 13**

**[A1]**

> **[mark-scheme]**
> **M1**: Chooses a pivot and produces a first pass giving the numbers above the pivot, then the pivot, then the numbers below it. The pivot must be the middle left or the middle right item.
> 
> **A1**: The first pass correct, with the pivots for the second pass chosen correctly, or at least consistently with the first choice.
> 
> **A1**: The second and third passes correct. Allow follow through from your own first pass and choice of pivots.
> 
> **A1**: A fully correct solution, including a fourth pass in which 19 is used as a pivot, or 14 if you are choosing the middle left item throughout.
> 
> Choosing only one pivot per iteration, rather than one in each sublist, limits this part to the method mark.
> 
> Sorting the list into ascending order is treated as a misread rather than as a wrong method.

> **[exam-tip]**
> The fourth pass changes nothing at all here, and it is still needed: 19 has to be used as a pivot before the sort can be declared finished. A list that already looks sorted is not evidence that the algorithm has terminated.
> 
> - Recount the length of each sublist before picking its pivot, because the position rule applies to the sublist and not to the original eleven numbers
> - From the second pass onwards you choose a pivot in every sublist at once, not one pivot for the whole list
> - Eleven numbers is an odd length, so the very first pivot is the true middle, at position 6 with five numbers on each side

### 7((c)) — 3 marks
Each allocation is evidence about $n$: a number that went into a bin fits, and a number that skipped a bin does not

Start with the first-fit allocation

14, 20 and 23 fill Bin 1 to 57, and the next number, 17, went into Bin 2 instead, so 17 could not be added

Later in the same allocation the 15 did go into Bin 1, taking it to 72, which is the largest total in any bin

*From first-fit, 57 plus 15 fits but 57 plus 17 does not, so n is at least 72 and at most 73*

**[B1]**

Now use the first-fit decreasing allocation, which fills Bin 1 with 32 and 28, reaching 60

The next number is 25, which opened Bin 2, and further down the list the 13 did not go into Bin 1 either

*From first-fit decreasing, 60 plus 13 does not fit, so n is at most 72*

**[B1]**

Only one value satisfies both allocations

$n = 72$

**[B1]**

> **[mark-scheme]**
> **B1**: A correct deduction from the first-fit allocation that $n$ is at least 72 or at most 73. As a minimum, accept the statement that $n$ is less than 74, or at most 73, or at least 72.
> 
> **B1**: A correct deduction from the first-fit decreasing allocation that the 13 did not fit into Bin 1. As a minimum, accept the statement that $n$ is less than 73, or at most 72, or simply that the 13 did not fit into Bin 1; give the benefit of the doubt if it is not clear which Bin 1 is meant.
> 
> **B1**: The correct answer, dependent on both of the previous marks. You must state or show that the largest total in any bin is 72, and it must be clear that the deduction about the 13 concerns the first-fit decreasing allocation and not the first-fit one.
> 
> Nothing is earned in this part for stating that $n$ is 72 with no working, or for doing no more than summing the numbers in each bin.
> 
> The first mark can be implied if you consider the first-fit decreasing packing before the first-fit one and argue from that direction, so long as both deductions are present.

> **[exam-tip]**
> Both allocations are needed, and they do different jobs: the first-fit packing pins the bin size down to 72 or 73, and only the first-fit decreasing packing rules out 73. Quoting one of them alone can never determine a single value.
> 
> - Look for a number that skipped a bin, since that is what gives you an upper limit, while a number that was accepted gives you a lower one
> - Name which packing each deduction comes from, because the last mark depends on the 13 being discussed as part of the first-fit decreasing allocation
> - The largest bin total in either packing is a value $n$ is allowed to take, so it is always worth writing the bin totals down before reasoning

## Q6 — medium — 12 marks · exam-questions

### 1((a)) — 2 marks
A lower bound comes from the total weight: even if every container were filled exactly to its limit, this many containers would still be needed

Add the twelve parcel weights

$16 + 23 + 18 + 9 + 4 + 20 + 35 + 5 + 17 + 13 + 6 + 11 = 177$

Divide the total by the capacity of one container

$\frac{177}{45} = 3 . 933 \dots$

Containers come whole, so round up rather than to the nearest whole number

$\text{lower bound} = 4  \text{containers}$

**[M1 A1]**

> **[mark-scheme]**
> **M1**: Attempts the total weight divided by 45. A value of 3.9 or better seen with no accompanying calculation can imply this mark, and so can a clear intention to add all twelve weights and divide by 45.
> 
> **A1**: The correct calculation, or a value of 3.9 or better, followed by 4.
> 
> An answer of 4 with no working at all scores nothing in this part, so the division has to be visible.
> 
> The fraction 59 over 15 is accepted in place of the decimal.

> **[exam-tip]**
> The lower bound is the quotient rounded up, never rounded to the nearest whole number, so 3.9 and 3.1 would both give 4. Only an exact whole number leaves the value unchanged.
> 
> - Write the division down even if your calculator does it in one step, because the answer alone earns nothing here
> - Four containers is only a target at this stage; part (b) then finds out whether first-fit actually achieves it, and it does not

### 1((b)) — 3 marks
First-fit works along the list in its original order, putting each parcel into the first container that still has room for it

Each container holds at most 45 kg

16 opens Container 1, and 23 joins it at 39 kg

18 does not fit alongside them, so it opens Container 2, and 9 joins it at 27 kg

4 goes back into Container 1 at 43 kg, and 20 fits in neither open container, so it opens Container 3

35 fits nowhere and opens Container 4, then 5 joins Container 2 at 32 kg

17 joins 20 in Container 3 at 37 kg, and 13 fills Container 2 to exactly 45 kg

6 goes into Container 3 at 43 kg, and 11 fits in none of the four, so it opens Container 5

**Final answer:** **Container 1: 16, 23, 4**

**Final answer:** **Container 2: 18, 9, 5, 13**

**Final answer:** **Container 3: 20, 17, 6**

**Final answer:** **Container 4: 35**

**Final answer:** **Container 5: 11**

**[M1 A1 A1]**

> **[mark-scheme]**
> **M1**: Places the first five items, 16, 23, 18, 9 and 4, correctly and puts at least eight values into containers.
> 
> **A1**: Places the first eight items, so as far as the 5, correctly.
> 
> **A1**: A fully correct solution, with no additional or repeated values.
> 
> The official scheme stages these three marks over one allocation, so all three depend on the same diagram: the method mark on the first five items, the first accuracy mark on the first eight, and the last on all twelve.
> 
> Writing cumulative running totals beside each container instead of the weights is condoned for the method mark only.
> 
> The first accuracy mark is not available if any value is repeated, or if more than twelve items appear in the containers, even where the first eight are correct.

> **[exam-tip]**
> First-fit needs five containers here, one more than the lower bound of four from part (a). That is not a mistake: a lower bound says only that fewer is impossible, and first-fit makes no attempt to be efficient.
> 
> - Always rescan from Container 1 for each new parcel, which is why 4, 5, 13 and 6 all travel backwards into containers opened earlier
> - Keep a running total beside each container as you work, but write the weights themselves in the answer, since totals alone cost the accuracy marks

### 1((c)) — 4 marks
A bubble sort compares each neighbouring pair along the list and swaps any pair that is the wrong way round

The weights are wanted in descending order, so a pair is swapped whenever the left weight is the smaller

Each pass carries the smallest weight still loose to the right-hand end, so after each pass one more weight is fixed there

*23, 18, 16, 9, 20, 35, 5, 17, 13, 6, 11, 4*

**[M1]**

4 is now fixed, so the second pass stops one place earlier, and the third stops one earlier again

*23, 18, 16, 20, 35, 9, 17, 13, 6, 11, 5, 4*

*23, 18, 20, 35, 16, 17, 13, 9, 11, 6, 5, 4*

**[A1]**

The next two passes settle the middle of the list, leaving 11, 9, 6, 5 and 4 in place

*23, 20, 35, 18, 17, 16, 13, 11, 9, 6, 5, 4*

*23, 35, 20, 18, 17, 16, 13, 11, 9, 6, 5, 4*

**[A1]**

35 is still travelling left, one place per pass, and the sixth pass finally puts it at the front

*35, 23, 20, 18, 17, 16, 13, 11, 9, 6, 5, 4*

The list now looks sorted, but that has to be demonstrated: a further pass makes no swaps at all, which is what ends the algorithm

**Final answer:** **35, 23, 20, 18, 17, 16, 13, 11, 9, 6, 5, 4**

**[A1]**

> **[mark-scheme]**
> **M1**: A bubble sort in a consistent direction throughout, with the first pass correct.
> 
> **A1**: Second and third passes correct, so three numbers finish in place.
> 
> **A1**: Fourth and fifth passes correct, so five numbers finish in place. Allow follow through from your own third pass.
> 
> **A1**: A fully correct solution, with a seventh pass shown making no swaps.
> 
> Check the first pass carefully if you are in the habit of writing out the result of every individual comparison, because the question asks only for the state of the list after each complete pass.
> 
> Continuing as far as an eleventh pass is condoned, provided nothing changes in any pass after the sixth.
> 
> Sorting into ascending order and then reversing the list at the end can still score full marks. If the list is not reversed, the last two accuracy marks are lost, and saying that it needs reversing without actually showing the reversed list costs the final mark.
> 
> A single number misread before the sort begins, whether missing, extra or simply wrong, is treated as a misread in this part only. Misreading more than one number loses the method mark, and miscopying one of your own numbers during the sort is an accuracy error rather than a misread.

> **[exam-tip]**
> Watch the 35 rather than the whole list. A bubble sort moves a large value left by only one place per pass, so a value near the wrong end takes a pass each time, and here the 35 alone is what forces the sort out to six passes.
> 
> - Show only the state at the end of each pass, as the question asks, not every individual swap along the way
> - After the fifth pass five numbers are guaranteed fixed at the right-hand end, so a quick check is that each pass should settle one more of them
> - The seventh pass is identical to the sixth and is still worth a mark, because an unchanged pass is the only thing that proves the algorithm has stopped

### 1((d)) — 3 marks
First-fit decreasing works down the sorted list from part (c), putting each parcel into the first container that can still take it

Each container holds at most 45 kg

35 opens Container 1, and 23 will not fit beside it, so it opens Container 2

20 joins 23 in Container 2 at 43 kg, and 18 fits in neither, so it opens Container 3

17 joins 18 in Container 3 at 35 kg, and 16 fits nowhere, so it opens Container 4

13 and 11 follow 16 into Container 4, taking it to 40 kg, and 9 goes back into Container 1 at 44 kg

6 joins Container 3 at 41 kg, 5 fills Container 4 to exactly 45 kg, and 4 fills Container 3 to exactly 45 kg as well

**Final answer:** **Container 1: 35, 9**

**Final answer:** **Container 2: 23, 20**

**Final answer:** **Container 3: 18, 17, 6, 4**

**Final answer:** **Container 4: 16, 13, 11, 5**

**[M1 A1 A1]**

> **[mark-scheme]**
> **M1**: Places the first six items, 35, 23, 20, 18, 17 and 16, correctly and puts at least eight values into containers.
> 
> **A1**: Places the first nine items, so as far as the 9, correctly, with no additional or repeated values.
> 
> **A1**: A fully correct solution, with no additional or repeated values.
> 
> You must be working from a correct sorted list in descending order. There is no follow through and no allowance for a misread from part (c), so a wrong value carried in from the sort costs the marks here as well. Applying first-fit to an increasing list earns nothing.
> 
> Writing cumulative running totals beside each container instead of the weights is condoned for the method mark only.

> **[exam-tip]**
> First-fit decreasing gets the parcels into four containers where plain first-fit needed five, and four is the lower bound from part (a), so this loading is provably the best possible.
> 
> - Two containers finish at exactly 45 kg, which is a useful check that nothing has overflowed
> - Sorting first is what makes the difference: the large parcels are placed while the containers are still empty, and the small ones then fill the gaps they leave

## Q7 — medium — 6 marks · exam-questions

### 3((a)) — 4 marks
The flow chart takes the value of $a$, works out a new value $b$ from it, and then asks whether the two are close enough

Rearranging $8 x^{4} + 5 x - 12 = 0$ gives the rule the chart applies

`b = \left[\frac{12 - 5 a}{8}\right]^{\frac{1}{4}}`

The test asks whether $a - b$ lies between $- 10^{-5}$ and $10^{-5}$

While the answer is no, the new value $b$ becomes the next $a$ and the chart loops round again

Starting from $a = 1$, the values settle after six passes

| a | b | Test satisfied? |
|---|---|---|
| **Final answer:** **1** | **Final answer:** **0.96716821** | **Final answer:** **N** |
| **Final answer:** **0.96716821** | **Final answer:** **0.97278935** | **Final answer:** **N** |
| **Final answer:** **0.97278935** | **Final answer:** **0.97183385** | **Final answer:** **N** |
| **Final answer:** **0.97183385** | **Final answer:** **0.97199647** | **Final answer:** **N** |
| **Final answer:** **0.97199647** | **Final answer:** **0.97196880** | **Final answer:** **N** |
| **Final answer:** **0.97196880** | **Final answer:** **0.97197351** | **Final answer:** **Y** |

**[M1 A1 A1]**

On the sixth pass $a - b$ is about $- 0 . 0000047$, which is inside the interval, so the chart outputs the current value of $b$

$\text{final output} = 0 . 97197$

**[A1]**

> **[mark-scheme]**
> **M1**: At least three rows of the $a$ and $b$ columns completed, with a correct first row of 1 for $a$ and 0.967168 for $b$.
> 
> **A1**: The first three rows correct, judging the $a$ and $b$ columns only.
> 
> **A1**: The fourth and fifth rows correct, again judging the $a$ and $b$ columns only.
> 
> **A1**: The output correct and written in the Final Output box. It must be given as 0.97197 and no other value, and the third column of the table must also have been completed correctly.
> 
> Values in the first three marks must be given to at least 6 decimal places, and may be either rounded or truncated.
> 
> Each row begins and ends when a value is changed, so one row carries one value of $a$ and the value of $b$ produced from it.

> **[exam-tip]**
> Six decimal places is a requirement, not a suggestion, and the values only separate from one another in the fifth and sixth places. Rounding to three or four would make consecutive rows look identical and lose the accuracy marks.
> 
> - Keep the full calculator value between rows rather than retyping a rounded one, since the last row turns on a difference of about five millionths
> - The final output is the value of $b$, not of $a$, and it is rounded to 5 decimal places while the table is not
> - The last mark also depends on the yes and no column, so complete it as you go rather than leaving it until the end

### 3((b)) — 2 marks
The chart works out a fourth root, and a fourth root of a negative number is not a real number

So the algorithm breaks down as soon as the quantity inside the root turns negative

$12 - 5 a < 0$

**[M1]**

Solve that inequality for $a$

$a > 2 . 4$

**[A1]**

> **[mark-scheme]**
> **M1**: Considers that $12 - 5 a$ cannot be negative, because the fourth root of a negative number does not exist. Simply stating the critical value of 2.4 is enough for this mark, as is stating or implying that the expression is less than or equal to zero, or equal to zero.
> 
> **A1**: The answer $a > 2 . 4$, and no other. It must be a strict inequality and must be written in terms of $a$.
> 
> The expression may be written in any of its equivalent forms, whether as $12 - 5 a$, as that divided by 8, or as the whole fourth-root expression.
> 
> Any letter may be used in place of $a$ for the method mark.

> **[exam-tip]**
> The inequality is strict because $a = 2 . 4$ is perfectly usable: it makes the quantity zero, the fourth root of zero is zero, and the algorithm carries on quite happily from there.
> 
> - Read the question's restriction as well: $a$ is given as non-negative, so there is no lower end to worry about and the whole answer is the single inequality

## Q8 — medium — 4 marks · exam-questions

### 1() — 4 marks
A binary search repeatedly halves the list, each time throwing away the half that cannot contain the word

The specification fixes the middle item at position $\frac{1}{2} ( N + 1 )$ when $N$ is odd and $\frac{1}{2} ( N + 2 )$ when $N$ is even, so with an even number of items you take the right-hand one of the middle pair

Number the words 1 to 10 in the order given, and compare each pivot with Parallelogram alphabetically

Ten words gives a pivot at position 6, which is Diameter, and Parallelogram comes after Diameter, so everything from Diameter back to Arc goes

*Pivot 6, Diameter: reject items 1 to 6*

**[M1]**

Items 7 to 10 are left, which is four words, so the pivot is the third of them, item 9, Segment

Parallelogram comes before Segment, so Segment and everything after it goes

*Pivot 9, Segment: reject items 9 and 10*

**[A1]**

Items 7 and 8 are left, and with two words the pivot is the second of them, item 8, Sector

Parallelogram comes before Sector, so Sector goes

*Pivot 8, Sector: reject item 8*

**[A1]**

Only item 7, Radius, remains, so it becomes the pivot; it is not Parallelogram, so it is rejected too and nothing is left to search

*Pivot 7, Radius: reject item 7*

**Final answer:** **The list is now empty, so Parallelogram is not in the list**

**[A1]**

> **[mark-scheme]**
> **M1**: Chooses the middle right pivot and makes an attempt at discarding or retaining half the list.
> 
> **A1**: The first pass correct, choosing item 6, and the second pass worked on items 7 to 10. The second pass must not still include item 6.
> 
> **A1**: Second and third passes correct, choosing item 9, Segment, and then item 8, Sector.
> 
> **A1**: The search completed, rejecting items 8 and 7, together with a statement that Parallelogram is not in the list.
> 
> Choosing the middle left item, Circumference, earns nothing at all, so the position rule has to be applied exactly.
> 
> For the method mark, retaining the wrong half of the list, or rejecting only items 1 to 5, is condoned.
> 
> For the first accuracy mark you are not required to choose the 9th item or to reject items 9 and 10; those belong to the next mark.
> 
> A pivot that has been used must not reappear in a later pass.
> 
> Radius has to be dealt with by name, or as the seventh item, after Sector has been rejected. Rejecting Radius on the same line as Sector is condoned provided it comes after it, and so is stating that Radius is not Parallelogram without formally rejecting it.
> 
> Abbreviations are accepted where they are clear and unambiguous, and you may rewrite the shortened list after each pass, with or without the accompanying calculations.

> **[exam-tip]**
> The search is not finished when one word is left. Radius still has to be looked at and rejected, and the final mark depends on that step and on the sentence saying the word is not there.
> 
> - Number the words 1 to 10 before you start, then work in item numbers rather than in words, which makes each pivot a single short calculation
> - Apply the position rule to the sublist you are actually searching, not to the original ten: items 7 to 10 is a list of four, so its middle is the third of those four
> - With an even number of items the pivot is the right-hand one of the middle pair, and taking the left-hand one here loses every mark in the question

## Q9 — medium — 13 marks · exam-questions

### 3((a)) — 3 marks
First-fit works along the list in its original order, putting each number into the first bin that still has room for it

Each bin holds a total of at most 5

2.6 opens Bin 1, and 0.8 joins it at 3.4

2.1 does not fit alongside them, so it opens Bin 2, and 1.2 goes back into Bin 1 at 4.6

0.9 will not fit in Bin 1, so it joins 2.1 in Bin 2 at 3.0, and 1.7 follows it there at 4.7

2.3 fits in neither open bin and opens Bin 3, then 0.3 returns to Bin 1 at 4.9

1.8 joins 2.3 in Bin 3 at 4.1, and 2.7 fits nowhere, so it opens Bin 4

**Final answer:** **Bin 1: 2.6, 0.8, 1.2, 0.3**

**Final answer:** **Bin 2: 2.1, 0.9, 1.7**

**Final answer:** **Bin 3: 2.3, 1.8**

**Final answer:** **Bin 4: 2.7**

**[M1 A1 A1]**

> **[mark-scheme]**
> **M1**: Places the first four items, 2.6, 0.8, 2.1 and 1.2, correctly and puts at least seven values into bins.
> 
> **A1**: Places the first seven items, so as far as the 2.3, correctly.
> 
> **A1**: A fully correct solution, with no additional or repeated values.
> 
> The official scheme stages these three marks over one allocation, so all three depend on the same diagram: the method mark on the first four items, the first accuracy mark on the first seven, and the last on all ten.
> 
> Writing cumulative running totals beside each bin instead of the values is condoned for the method mark only.
> 
> The first accuracy mark is not available if any value is repeated or if an extra value appears, even where the first seven are correct.

> **[exam-tip]**
> No bin here fills to exactly 5, so there is no neat arithmetic check at the end. What you can check instead is that every number appears exactly once and that no bin total exceeds 5.
> 
> - Always rescan from Bin 1 for each new number, which is why 1.2 and 0.3 travel backwards into a bin opened much earlier
> - Keep a running total beside each bin as you work, but write the values themselves in the answer, since totals alone cost the accuracy marks

### 3() — 4 marks
**(i)**

A bubble sort compares each neighbouring pair along the list and swaps any pair that is the wrong way round

The list is being sorted into descending order, so a pair is swapped whenever the left number is the smaller

The first pass makes nine comparisons and carries the smallest number, 0.3, all the way to the right-hand end

*2.6, 2.1, 1.2, 0.9, 1.7, 2.3, 0.8, 1.8, 2.7, 0.3*

**[B1]**

The second pass needs only eight comparisons, because the last number is already in its final place, and it settles 0.8 next to it

**Final answer:** **2.6, 2.1, 1.2, 1.7, 2.3, 0.9, 1.8, 2.7, 0.8, 0.3**

**[B1]**

**(ii)**

Count the comparisons from the length of the list, and the swaps from the pairs that actually changed places

|   | Number of comparisons | Number of swaps |
|---|---|---|
| **Final answer:** **First pass** | **Final answer:** **9** | **Final answer:** **7** |
| **Final answer:** **Second pass** | **Final answer:** **8** | **Final answer:** **4** |

**[B1] [B1]**

> **[mark-scheme]**
> **B1**: The first pass correct, as a correct answer only.
> 
> **B1**: The second pass correct, as a correct answer only.
> 
> **B1**: Any two of the four values in the table correct.
> 
> **B1**: All four values in the table correct.
> 
> If you show the result of every individual comparison and swap rather than only the state after each pass, the first pass is taken to be the list at the point where 0.3 has reached its correct position, and the second pass the list at the point where 0.8 and 0.3 are both in position.
> 
> Any further passes written beyond the two asked for are ignored.

> **[exam-tip]**
> The number of comparisons never depends on the numbers, only on how much of the list is still unsorted: ten numbers always give nine comparisons on the first pass and eight on the second.
> 
> - Count the swaps as you make them, by ticking each pair you exchange, since the count cannot be recovered from the finished list
> - Two of the four table values are worth a mark on their own, so fill in the comparisons even if you are unsure of the swaps
> - Descending order reverses the test, so you swap when the left number is smaller, which is the opposite of the ascending sort most students practise first

### 3((c)) — 3 marks
A quick sort picks a pivot, then splits the list into the numbers that belong before it and the numbers that belong after it

The specification fixes the pivot as the middle item, at position $\frac{1}{2} ( N + 1 )$ when $N$ is odd and $\frac{1}{2} ( N + 2 )$ when $N$ is even

The list is being sorted into descending order, so the larger numbers go to the left of the pivot

Pivots are shown in brackets, and every pivot already placed stays fixed for the rest of the sort

The updated list has ten numbers, so the first pivot is at position 6, which is 1.8

*2.6, 2.1, 1.7, 2.3, 1.2, (1.8), 2.7, 0.9, 0.8, 0.3*

Four numbers are larger than 1.8 and five are smaller, so the next two sublists have four and five numbers, with pivots at positions 3 and 3

*2.6, 2.1, (2.3), 2.7, 1.8, 1.7, 1.2, (0.9), 0.8, 0.3*

**[M1]**

2.1 is left alone below 2.3, and 0.9 leaves a pair on each side of it

*2.6, (2.7), 2.3, (2.1), 1.8, 1.7, (1.2), 0.9, 0.8, (0.3)*

**[A1]**

No sublist now holds more than one number, so the sort is complete

**Final answer:** **2.7, 2.6, 2.3, 2.1, 1.8, 1.7, 1.2, 0.9, 0.8, 0.3**

**[A1]**

> **[mark-scheme]**
> **M1**: Chooses a pivot and produces a first pass giving the numbers above the pivot, then the pivot, then the numbers below it. The pivot must be the middle left or the middle right item; choosing the first or the last item scores nothing.
> 
> **A1**: The first two passes correct, with the second-pass pivot consistent with your choice of pivot in the first pass. Choosing the pivots for the third pass is not required for this mark.
> 
> **A1**: A fully correct solution, with every earlier mark in this part also earned, and a statement that the sort is complete.
> 
> Completion can be shown by rewriting the final list, by stating that the list is sorted, or by every number having been used as a pivot, which would mean writing the final list out twice.
> 
> Choosing only one pivot per iteration, rather than one in each sublist, limits this part to the method mark, and so does sorting into ascending order.
> 
> Two special cases are recognised. Carrying out the quick sort on the original list from part (a) rather than on the updated list scores the method mark only. Carrying it out on just the first seven numbers of the updated list, so leaving out the last three, scores the method mark and the first accuracy mark.

> **[exam-tip]**
> Start from the updated list printed in this part, not from the original one. Sorting the wrong list is the single most expensive mistake available here, and it caps the part at one mark however well the algorithm is carried out.
> 
> - Recount the length of each sublist before picking its pivot, because the position rule applies to the sublist and not to the original ten numbers
> - Three passes are enough here because the updated list is already close to sorted, but you still have to say so rather than simply stopping

### 3((d)) — 3 marks
First-fit decreasing works down the fully sorted list from part (c), putting each number into the first bin that can still take it

Each bin holds a total of at most 5

2.7 opens Bin 1, and 2.6 will not fit beside it, so it opens Bin 2

2.3 joins 2.7 in Bin 1, filling it to exactly 5, and 2.1 joins 2.6 in Bin 2 at 4.7

1.8 fits in neither, so it opens Bin 3, and 1.7 joins it at 3.5

1.2 follows them into Bin 3 at 4.7, and 0.9 fits nowhere, so it opens Bin 4

0.8 joins 0.9 in Bin 4 at 1.7, and 0.3 fills Bin 2 to exactly 5

**Final answer:** **Bin 1: 2.7, 2.3**

**Final answer:** **Bin 2: 2.6, 2.1, 0.3**

**Final answer:** **Bin 3: 1.8, 1.7, 1.2**

**Final answer:** **Bin 4: 0.9, 0.8**

**[M1 A1 A1]**

> **[mark-scheme]**
> **M1**: Places the first four items, 2.7, 2.6, 2.3 and 2.1, correctly and puts at least seven values into bins.
> 
> **A1**: Places the first seven items, so as far as the 1.2, correctly.
> 
> **A1**: A fully correct solution, with no additional or repeated values.
> 
> The official scheme stages these three marks over one allocation, so all three depend on the same diagram: the method mark on the first four items, the first accuracy mark on the first seven, and the last on all ten.
> 
> Writing cumulative running totals beside each bin instead of the values is condoned for the method mark only.
> 
> There is no allowance for a misread anywhere in this part, so the values must be the ten from the original list.

> **[exam-tip]**
> Two bins fill to exactly 5 here, and the total of all ten numbers is 16.4, so four bins is the smallest number that could possibly work. This packing therefore cannot be improved on.
> 
> - Sorting first is what makes the difference: the large numbers are placed while the bins are still empty, and the small ones then fill the gaps they leave
> - Work down the sorted list one number at a time rather than trying to see the whole packing at once, since first-fit decreasing never looks ahead

## Q10 — medium — 13 marks · exam-questions

### 2() — 4 marks
**(i)**

A bubble sort works along the list comparing neighbouring pairs, and one pass is one journey from the left-hand end to the right-hand end

Ascending order means each value should be no larger than the one after it, so a pair is swapped whenever the left value is the larger

**Final answer:** **Compare the first value with the second, and swap them if the first is larger**

**[M1]**

The comparison then moves along one place at a time, and each comparison uses whatever value has just been left in that position

**Final answer:** **Then compare the second value with the third and swap them if the second is larger, continuing in this way until the last pair in the list has been compared**

**[A1]**

**(ii)**

A bubble sort has two possible stopping points, and either one ends the algorithm

**Final answer:** **The sort stops when there is only one item left to sort**

**[B1]**

**Final answer:** **The sort also stops when a whole pass is completed in which no swaps are made**

**[B1]**

> **[mark-scheme]**
> **M1**: Compares the first value with the second and swaps them if the first is larger. Comparing them in the wrong order is condoned for the method mark only.
> 
> **A1**: Compares the second value with the third, and continues in the same way to the end of the list. It must be clear that the whole list has been considered, so "and so on until the end of the list" or "all", "last" or similar is needed rather than just the next two.
> 
> **B1**: Either one of the two stopping conditions, stated correctly.
> 
> **B1**: Both reasons stated correctly.
> 
> For the first stopping condition, saying that the sort stops after one fewer pass than there are numbers is equivalent and is accepted, but saying that it stops once all the required passes have been done is not. For the second, saying that one pass gives the same result as the next is equivalent and is accepted.
> 
> Stating only that the sort stops when the list is in order earns nothing, because that is what the algorithm has to detect rather than something it is told.

> **[exam-tip]**
> Both stopping conditions are needed for the second mark, and they are genuinely different. One counts passes and will always finish; the other watches for a pass with no swaps and can finish much sooner on a list that is already nearly sorted.
> 
> - Describe the comparisons in terms of positions rather than particular numbers, since the question is about a list of any length
> - Say explicitly that the pass carries on to the end of the list, because stopping your description after the second comparison costs the accuracy mark

### 2((b)) — 2 marks
Each pass of a bubble sort settles one more value permanently at the right-hand end, so after $k$ passes the $k$ largest values are guaranteed to be in place

Sort the list mentally and compare it with the one given: 1.7, 2.2 and 3.2 occupy the last three positions correctly, but the fourth from the end should be 1.5 and it is 0.7

So three values are settled and a fourth is not, which puts a ceiling on how many passes can have happened

$\text{maximum number of passes} = 3$

**[B1]**

**Final answer:** **Only the three largest numbers are in their correct positions, and a fourth pass would have settled a fourth**

**[B1]**

> **[mark-scheme]**
> **B1**: The value 3, as a correct answer only.
> 
> **B1**: Correct reasoning, dependent on the first mark.
> 
> The reasoning must mention that the three largest numbers are in the correct position. Naming 1.7, 2.2 and 3.2 as being in the correct position is not enough on its own, because it does not say that they are the three largest and so does not explain why no further pass can have taken place.

> **[exam-tip]**
> The question asks for the maximum, not the exact number, because a bubble sort can settle extra values by luck. Three is the largest number of passes consistent with the list shown, and fewer passes could in principle have produced it.
> 
> - Count from the right-hand end, since that is where a bubble sort deposits values it has finished with
> - The word largest is what earns the second mark, so make sure your reason says which numbers are settled and why that is the ceiling

### 2((c)) — 4 marks
The list is being sorted into ascending order, so a pair is swapped whenever the left number is the larger

Each pass carries the largest number still loose to the right-hand end, so after each pass one more number is fixed there

The first pass moves 1.5 past three smaller numbers and leaves it in seventh place

*0.9, 1.2, 0.5, 1.4, 1.1, 0.7, 1.5, 1.7, 2.2, 3.2*

**[M1]**

1.5 is now fixed, so each following pass stops one place earlier than the one before

*0.9, 0.5, 1.2, 1.1, 0.7, 1.4, 1.5, 1.7, 2.2, 3.2*

*0.5, 0.9, 1.1, 0.7, 1.2, 1.4, 1.5, 1.7, 2.2, 3.2*

**[A1]**

Only the 0.7 is still out of place, and the next two passes each move it one position to the left

*0.5, 0.9, 0.7, 1.1, 1.2, 1.4, 1.5, 1.7, 2.2, 3.2*

*0.5, 0.7, 0.9, 1.1, 1.2, 1.4, 1.5, 1.7, 2.2, 3.2*

**[A1]**

The list now looks sorted, but that has to be demonstrated: a further pass makes no swaps at all, which is what ends the algorithm

**Final answer:** **0.5, 0.7, 0.9, 1.1, 1.2, 1.4, 1.5, 1.7, 2.2, 3.2**

**[A1]**

> **[mark-scheme]**
> **M1**: A bubble sort in a consistent direction throughout, with the first pass correct.
> 
> **A1**: Second and third passes correct, so six numbers finish in place after the third pass.
> 
> **A1**: Fourth and fifth passes correct, so eight numbers finish in place after the fifth pass. Allow follow through from your own third pass.
> 
> **A1**: A fully correct solution, with a sixth pass shown making no swaps.
> 
> Check the first pass carefully if you are in the habit of writing out the result of every individual comparison, because the question asks only for the state of the list after each complete pass.
> 
> A quick sort earns nothing here, and neither does a sort into descending order.
> 
> A statement that the list is in order after the fifth pass does not replace the sixth pass, which has to be written out.

> **[exam-tip]**
> This list was already three passes into a sort when part (b) looked at it, so the remaining work is small: only 0.5 and 0.7 are seriously out of position. That does not shorten the answer, because the unchanged sixth pass is still required.
> 
> - Show only the state at the end of each pass, as the question asks, not every individual swap along the way
> - After the third pass six numbers are guaranteed fixed at the right-hand end, so a quick check is that each pass should settle one more of them
> - The sixth pass is identical to the fifth and is still worth a mark, because an unchanged pass is the only thing that proves the algorithm has stopped

### 2((d)) — 3 marks
First-fit decreasing sorts the numbers into descending order first, then puts each one into the first bin that can still take it

Each bin holds a total of at most 4

*3.2, 2.2, 1.7, 1.5, 1.4, 1.2, 1.1, 0.9, 0.7, 0.5*

3.2 opens Bin 1, and 2.2 will not fit beside it, so it opens Bin 2

1.7 joins 2.2 in Bin 2 at 3.9, and 1.5 fits in neither, so it opens Bin 3

1.4 joins 1.5 in Bin 3 at 2.9, and 1.2 fits nowhere, so it opens Bin 4

1.1 fills Bin 3 to exactly 4, and 0.9 joins 1.2 in Bin 4 at 2.1

0.7 goes back into Bin 1 at 3.9, and 0.5 joins Bin 4 at 2.6

**Final answer:** **Bin 1: 3.2, 0.7**

**Final answer:** **Bin 2: 2.2, 1.7**

**Final answer:** **Bin 3: 1.5, 1.4, 1.1**

**Final answer:** **Bin 4: 1.2, 0.9, 0.5**

**[M1 A1 A1]**

> **[mark-scheme]**
> **M1**: Places the first four items, 3.2, 2.2, 1.7 and 1.5, correctly.
> 
> **A1**: Places the first eight items, so as far as the 0.9, correctly.
> 
> **A1**: A fully correct solution.
> 
> The official scheme stages these three marks over one allocation, so all three depend on the same diagram: the method mark on the first four items, the first accuracy mark on the first eight, and the last on all ten.
> 
> Writing cumulative running totals beside each bin instead of the values is condoned for the method mark only.
> 
> Any additional or repeated value caps this part at the method mark, even where the first eight items are placed correctly.

> **[exam-tip]**
> The sorted list you need here is the one from part (c), but read down rather than up, because first-fit decreasing starts from the largest number. Working up the ascending list instead is first-fit increasing and earns nothing.
> 
> - Only Bin 3 fills to exactly 4, so the useful check is that no bin total exceeds 4 and all ten numbers appear once
> - The 0.7 travels back into Bin 1 late in the process, which is a reminder that first-fit decreasing still rescans from the first bin every time

## Q11 — medium — 13 marks · exam-questions

### 4((a)) — 3 marks
First-fit works along the list in its original order, putting each number into the first bin that still has room for it

Each bin holds a total of at most 60

35 opens Bin 1, and 17 joins it at 52

10 will not fit in Bin 1, so it opens Bin 2, and 7 goes back into Bin 1, filling it to exactly 59

28 joins 10 in Bin 2 at 38, and 23 fits in neither bin, so it opens Bin 3

41 fits nowhere and opens Bin 4, then 15 completes Bin 2 at exactly 53

20 joins 23 in Bin 3 at 43, and 29 fits in none of the four, so it opens Bin 5

**Final answer:** **Bin 1: 35, 17, 7**

**Final answer:** **Bin 2: 10, 28, 15**

**Final answer:** **Bin 3: 23, 20**

**Final answer:** **Bin 4: 41**

**Final answer:** **Bin 5: 29**

**[M1 A1 A1]**

> **[mark-scheme]**
> **M1**: Places the first four items, 35, 17, 10 and 7, correctly and puts at least seven values into bins.
> 
> **A1**: Places the first eight items, so as far as the 15, correctly.
> 
> **A1**: A fully correct solution, with no additional or repeated values.
> 
> The official scheme stages these three marks over one allocation, so all three depend on the same diagram: the method mark on the first four items, the first accuracy mark on the first eight, and the last on all ten.
> 
> Writing cumulative running totals beside each bin instead of the values is condoned for the method mark only.
> 
> If one of the first four values appears in more than one bin the method mark is lost, and if one of the next four appears in two different bins the first accuracy mark is lost.

> **[exam-tip]**
> Five bins looks wasteful, and it is: Bin 4 holds only 41 and Bin 5 only 29, leaving 19 and 31 of their capacity unused. Part (c) sorts first and pairs each of them with a smaller number instead, which saves a whole bin.
> 
> - Always rescan from Bin 1 for each new number, which is why 7 and 15 travel backwards into bins opened earlier
> - Keep a running total beside each bin as you work, but write the values themselves in the answer, since totals alone cost the accuracy marks

### 4((b)) — 4 marks
A quick sort picks a pivot, then splits the list into the numbers that belong before it and the numbers that belong after it

The specification fixes the pivot as the middle item, at position $\frac{1}{2} ( N + 1 )$ when $N$ is odd and $\frac{1}{2} ( N + 2 )$ when $N$ is even

The list is being sorted into descending order, so the larger numbers go to the left of the pivot

Pivots are shown in brackets, and every pivot already placed stays fixed for the rest of the sort

Ten numbers gives a first pivot at position 6, which is 23

*35, 17, 10, 7, 28, (23), 41, 15, 20, 29*

Four numbers are larger than 23 and five are smaller, so the next two sublists have four and five numbers, with pivots at positions 3 and 3

*35, 28, (41), 29, 23, 17, 10, (7), 15, 20*

**[M1]**

Nothing is larger than 41, so its sublist of three passes to its right, and nothing is smaller than 7, so its sublist of four passes to its left

*41, 35, (28), 29, 23, 17, 10, (15), 20, 7*

**[A1]**

28 leaves 35 and 29 above it, and 15 splits the remaining three into two above and one below

*41, 35, (29), 28, 23, 17, (20), 15, (10), 7*

**[A1]**

No sublist now holds more than one number, so the sort is complete

**Final answer:** **41, 35, 29, 28, 23, 20, 17, 15, 10, 7**

**[A1]**

> **[mark-scheme]**
> **M1**: Chooses a pivot and produces a first pass giving the numbers above the pivot, then the pivot, then the numbers below it. The pivot must be the middle left or the middle right item; choosing the first or the last item scores nothing.
> 
> **A1**: The first two passes correct.
> 
> **A1**: The third pass correct. Allow follow through from your own second pass and from your choice of pivots for the third pass, which must still be middle left or middle right items.
> 
> **A1**: A fully correct solution, with every earlier mark in this part also earned, and a statement that the sort is complete.
> 
> Completion can be shown by rewriting the final list, by stating that the list is sorted, or by every number having been used as a pivot, which would mean writing the final list out twice.
> 
> Choosing only one pivot per iteration, rather than one in each sublist, limits this part to the method mark.
> 
> Starting from a list with a single error, meaning one number missing, one extra, two numbers transposed or one number wrong, caps this part at the method mark and the first accuracy mark.
> 
> Sorting into ascending order and then reversing the list can still score full marks. If the list is not reversed, the last two accuracy marks are lost, and saying that it needs reversing without actually showing the reversed list costs the final mark.

> **[exam-tip]**
> Choosing the middle left item instead needs six passes here rather than four, and both are accepted, so long as you stay with one choice throughout. Switching between them mid-sort is what loses marks.
> 
> - Recount the length of each sublist before picking its pivot, because the position rule applies to the sublist and not to the original ten numbers
> - From the second pass onwards you choose a pivot in every sublist at once, not one pivot for the whole list
> - Bracket a pivot as soon as it is placed, so you can see at a glance which numbers are still in play

### 4((c)) — 3 marks
First-fit decreasing works down the sorted list from part (b), putting each number into the first bin that can still take it

Each bin holds a total of at most 60

41 opens Bin 1, and 35 will not fit beside it, so it opens Bin 2

29 fits in neither, so it opens Bin 3, and 28 joins it there at exactly 57

23 joins 35 in Bin 2 at 58, and 20 fits in none of the three, so it opens Bin 4

17 goes back into Bin 1 at 58, and 15 joins 20 in Bin 4 at 35

10 and 7 follow them into Bin 4, taking it to 52

**Final answer:** **Bin 1: 41, 17**

**Final answer:** **Bin 2: 35, 23**

**Final answer:** **Bin 3: 29, 28**

**Final answer:** **Bin 4: 20, 15, 10, 7**

**[M1 A1 A1]**

> **[mark-scheme]**
> **M1**: Places the first five items, 41, 35, 29, 28 and 23, correctly and puts at least eight values into bins.
> 
> **A1**: Places the first seven items, so as far as the 17, correctly.
> 
> **A1**: A fully correct solution, with no additional or repeated values.
> 
> You must be working from a list in strictly descending order. Applying first-fit to an increasing list earns nothing.
> 
> A sorted list carried in from part (b) containing a single error, meaning one number missing, one extra or one number wrong, still allows the method mark, provided the list is in descending order.
> 
> Writing cumulative running totals beside each bin instead of the values is condoned for the method mark only. If one of the first seven values appears in two different bins the first accuracy mark is lost.

> **[exam-tip]**
> Sorting first saves a whole bin: first-fit needed five and first-fit decreasing needs four. The reason is visible in the answer, since 41 and 29 each end up sharing with a smaller number rather than sitting alone.
> 
> - No bin fills to exactly 60, so the check to make is that every number appears once and no total exceeds 60
> - Work down the sorted list one number at a time rather than trying to see the whole packing at once, since first-fit decreasing never looks ahead

### 4((d)) — 3 marks
A bubble sort in descending order swaps a neighbouring pair whenever the left number is the smaller, so each comparison that did or did not happen is a piece of information about $x$ and $y$

Work through the second pass, comparing what it must have done with the list given

The second pass starts 24, 20, 26, 17, 15 and reaches the pair 15 and $x$; the given list still has 15 in fifth place, so no swap happened there

It then compares $x$ with $y$, and the given list has $y$ in sixth place, so that pair did swap

$x$ is then compared with 19 and with 12, both of which moved left past it, and finally with 8, which did not

So $x$ swapped with 12 but not with 8, which makes 8 the smaller of the two limits and 12 the larger

The first pass gives the same lower limit, since 8 travelled all the way to the right-hand end and so had to be smaller than $x$

$x > 8$

**[B1]**

$x < 12$

**[B1]**

$y > x$

**[B1]**

Nothing in either pass compares $y$ with a larger number, so there is no upper limit on $y$, and $y > 8$ follows from the three constraints above rather than being a fourth one

> **[mark-scheme]**
> **B1**: $x > 8$.
> 
> **B1**: $x < 12$.
> 
> **B1**: $x < y$, or equivalently $y > x$.
> 
> If both of the first two marks are lost, one mark is still available for the answer given with weak inequalities, as 8 less than or equal to $x$ less than or equal to 12, or any equivalent form.
> 
> Stating only that $y > 8$ is not enough on its own for the third mark, because it does not say how $y$ compares with $x$.
> 
> For full marks there must be no additional incorrect constraint. An extra condition such as $y > 15$ costs the third mark, although extra conditions are not penalised further once all three correct constraints have been given.

> **[exam-tip]**
> Read the swaps backwards. Every adjacent pair in the printed list is evidence: a pair that changed places tells you which of the two is larger, and a pair that did not tells you the same thing the other way round.
> 
> - The second pass is the more useful one here, because $x$ is compared with four known numbers in it
> - Check whether each constraint is genuinely new before writing it down, since $y > 8$ already follows from $y > x$ and $x > 8$
> - An extra constraint that is not justified costs a mark, so do not add plausible-looking limits on $y$

## Q12 — medium — 18 marks · exam-questions

### 3((a)) — 2 marks
A lower bound comes from the total number of pupils: even if every tour group were filled exactly to its limit, this many groups would still be needed

Add the ten school sizes

$8 + 17 + 9 + 14 + 18 + 12 + 22 + 10 + 15 + 7 = 132$

Divide the total by the maximum size of one tour group

$\frac{132}{42} = 3 . 14 \dots$

Tour groups come whole, so round up rather than to the nearest whole number

$\text{lower bound} = 4  \text{tour groups}$

**[M1 A1]**

> **[mark-scheme]**
> **M1**: Attempts the total number of pupils divided by 42. A value of 3.14 or better seen with no working can imply this mark.
> 
> **A1**: A correct solution only, meaning the correct calculation, or 3.14 followed by 4. A value of 3.1 is accepted provided the correct calculation is also seen.
> 
> An answer of 4 with no working at all scores nothing in this part, so the division has to be visible.

> **[exam-tip]**
> The lower bound is the quotient rounded up, never rounded to the nearest whole number, so 3.14 gives 4 even though it is much closer to 3.
> 
> - Write the division down even if your calculator does it in one step, because the answer alone earns nothing here
> - A lower bound only rules out fewer groups, but it is worth knowing the target before you start: part (b) turns out to reach it

### 3((b)) — 2 marks
First-fit works along the list in its original order, putting each school into the first tour group that still has room for it

Each tour group holds at most 42 pupils

8 opens Group 1, and 17 joins it at 25

9 also fits in Group 1, taking it to 34, but 14 does not, so it opens Group 2

18 joins 14 in Group 2 at 32, and 12 fits in neither, so it opens Group 3

22 joins 12 in Group 3 at 34, and 10 completes Group 2 at exactly 42

15 fits in none of the three, so it opens Group 4, and 7 fills Group 1 to 41

**Final answer:** **Group 1: 8, 17, 9, 7**

**Final answer:** **Group 2: 14, 18, 10**

**Final answer:** **Group 3: 12, 22**

**Final answer:** **Group 4: 15**

**[M1 A1]**

> **[mark-scheme]**
> **M1**: Places the first six items, 8, 17, 9, 14, 18 and 12, correctly and puts at least eight items into groups.
> 
> **A1**: A fully correct solution, with no additional or repeated values.
> 
> Writing cumulative running totals beside each group instead of the numbers of pupils is condoned for the method mark only.

> **[exam-tip]**
> Four groups matches the lower bound from part (a), so first-fit has already found the best possible allocation here. That is luck rather than a property of the algorithm, and part (d) shows the sorted version doing no better.
> 
> - Always rescan from Group 1 for each new school, which is why the 7 travels back into a group opened at the very start
> - Pupils from one school must stay together, which is what makes this a bin packing question rather than a division

### 3((c)) — 4 marks
A quick sort picks a pivot, then splits the list into the numbers that belong before it and the numbers that belong after it

The specification fixes the pivot as the middle item, at position $\frac{1}{2} ( N + 1 )$ when $N$ is odd and $\frac{1}{2} ( N + 2 )$ when $N$ is even

The list is being sorted into descending order, so the larger numbers go to the left of the pivot

Pivots are shown in brackets, and every pivot already placed stays fixed for the rest of the sort

Ten numbers gives a first pivot at position 6, which is 12

*8, 17, 9, 14, 18, (12), 22, 10, 15, 7*

Five numbers are larger than 12 and four are smaller, so the next two sublists have five and four numbers, with pivots at positions 3 and 3

*17, 14, (18), 22, 15, 12, 8, 9, (10), 7*

**[M1 A1]**

Only 22 lies above 18, and 10 is the largest of its own sublist, so 8, 9 and 7 all fall below it

*(22), 18, 17, (14), 15, 12, 10, 8, (9), 7*

14 leaves 17 and 15 above it and nothing below, and 9 likewise has nothing above it, with 8 and 7 below

*22, 18, 17, (15), 14, 12, 10, 9, 8, (7)*

**[A1]**

No sublist now holds more than one number, so the sort is complete

**Final answer:** **22, 18, 17, 15, 14, 12, 10, 9, 8, 7**

**[A1]**

> **[mark-scheme]**
> **M1**: Chooses a pivot and produces a first pass giving the numbers above the pivot, then the pivot, then the numbers below it. The pivot must be the middle left or the middle right item; choosing the first or the last item scores nothing.
> 
> **A1**: The first pass correct, and the pivots for the second pass chosen correctly, which for the middle right choice are 18 and 10, or 14 for the middle left. The second pass does not itself have to be correct for this mark.
> 
> **A1**: The second and third passes correct. Allow follow through from your own first pass and choice of pivots, and you are not required to choose a pivot for the fourth pass for this mark.
> 
> **A1**: A fully correct solution, including a fourth pass in which 15 and 7 are used as pivots, or a fifth pass using 8 if you are choosing the middle left item throughout.
> 
> Choosing only one pivot per iteration, rather than one in each sublist, limits this part to the method mark.
> 
> Sorting into ascending order and then reversing the list can still score full marks. If the list is not reversed, the last two accuracy marks are lost, and if you say it needs reversing without showing the reversed list, the final mark goes. Where you sort into ascending order, the statement that the sort is complete has to appear before the list is reversed.

> **[exam-tip]**
> The fourth pass changes nothing at all here, and it is still required: 15 and 7 have to be used as pivots before the sort can be declared finished. A list that already looks sorted is not evidence that the algorithm has terminated.
> 
> - Recount the length of each sublist before picking its pivot, because the position rule applies to the sublist and not to the original ten numbers
> - From the second pass onwards you choose a pivot in every sublist at once, not one pivot for the whole list
> - Sorting into ascending order is allowed, but the reversal has to be shown and the completion statement has to come first

### 3((d)) — 2 marks
First-fit decreasing works down the sorted list from part (c), putting each school into the first tour group that can still take it

Each tour group holds at most 42 pupils

22 opens Group 1, and 18 joins it at 40

17 will not fit beside them, so it opens Group 2, and 15 joins it at 32

14 fits in neither, so it opens Group 3, and 12 joins it at 26

10 completes Group 2 at exactly 42, and 9 joins Group 3 at 35

8 fits in none of the three, so it opens Group 4, and 7 fills Group 3 to exactly 42

**Final answer:** **Group 1: 22, 18**

**Final answer:** **Group 2: 17, 15, 10**

**Final answer:** **Group 3: 14, 12, 9, 7**

**Final answer:** **Group 4: 8**

**[M1 A1]**

> **[mark-scheme]**
> **M1**: Places the first six items, 22, 18, 17, 15, 14 and 12, correctly and puts at least eight items into groups.
> 
> **A1**: A fully correct solution, with no additional or repeated values.
> 
> Writing cumulative running totals beside each group instead of the numbers of pupils is condoned for the method mark only.

> **[exam-tip]**
> First-fit decreasing also uses four groups here, so it has not improved on part (b). Sorting first usually helps and is not guaranteed to, and where plain first-fit has already matched the lower bound there is nothing left to gain.
> 
> - Two groups fill to exactly 42 here, which is a useful check that nothing has overflowed
> - The allocation is different from part (b) even though the number of groups is the same, so the two answers are not interchangeable

### 3((e)) — 4 marks
Sally has to travel along every corridor at least once and return to her starting point, so this is a route inspection problem

A closed route repeating nothing exists only when every vertex has even degree, so start by counting the arcs at each vertex

$A$ and $D$ have degree 2, and $E$, $F$, $I$ and $J$ have degree 4, so the odd vertices are $B$, $C$, $G$ and $H$, each of degree 3

Four odd vertices can be paired up in three ways, and each pairing is joined by its shortest path

Pair $B$ to $C$ through $E$, and $G$ to $H$ through $I$

$( 11 . 2 + 14 . 5 ) + ( 8 . 3 + 17 . 2 ) = 51 . 2$

Pair $B$ to $G$ through $F$, and $C$ to $H$ through $E$ and $J$

$( 10 . 3 + 15 . 2 ) + ( 14 . 5 + 7 . 5 + 16 . 2 ) = 63 . 7$

Pair $B$ to $H$ through $E$ and $J$, and $C$ to $G$ through $E$ and $F$

$( 11 . 2 + 7 . 5 + 16 . 2 ) + ( 14 . 5 + 4 . 3 + 15 . 2 ) = 68 . 9$

**[M1 A1 A1]**

The first pairing is the cheapest, so those are the corridors Sally repeats

**Final answer:** **Repeat the corridors BE, CE, GI and HI**

**[A1]**

> **[mark-scheme]**
> **M1**: The correct three pairings of the correct four odd nodes, $B$, $C$, $G$ and $H$.
> 
> **A1**: Any one of the three rows correct, including both its pairing and its total.
> 
> **A1**: All three rows correct, including pairings and totals.
> 
> **A1**: A correct answer only, with the arcs clearly stated as BE, CE, GI and HI.
> 
> The official scheme stages the first three marks over the same table of pairings, so all three depend on it: the method mark on the pairings being the right ones, then a mark for one row complete and a mark for all three.
> 
> The final mark is for the four arcs themselves. Naming paths instead, such as BEC or GIH, does not earn it, and neither does describing an arc indirectly, such as BC through E.

> **[exam-tip]**
> Count the degrees before anything else. With four odd vertices there are exactly three pairings to test, and with two there would be only one, so the number of odd vertices tells you immediately how much work the question holds.
> 
> - Each pairing must use the shortest path between the two vertices, which is not always the direct arc: $G$ to $H$ is 27.3 directly but only 25.5 through $I$
> - Write out all three totals even once you can see which is smallest, since two of the four marks are for the rows rather than for the answer
> - The answer is a list of arcs, so name each one by its two endpoints and do not run them together into a path

### 3((f)) — 2 marks
A shortest route travels every corridor once and the four repeated corridors a second time, and it must start and finish at $A$

Build it by walking the network, taking each repeated corridor twice in succession where that is convenient

**Final answer:** **A possible route is ABEBFECEJIFGIGHIHJDCA**

**[B1]**

The length is the total of every corridor in the museum plus the total of the four repeated ones

$227 . 2 + 51 . 2 = 278 . 4$

$\text{length} = 278 . 4  \text{m}$

**[B1]**

> **[mark-scheme]**
> **B1**: Any correct route.
> 
> **B1**: The correct length. Allow follow through as 227.2 plus your own smallest repeat total from part (e), provided at least two of the three totals were written down there and the method mark in part (e) was earned.
> 
> A route can be checked against four things: it has 21 vertices, it starts and ends at $A$, the arcs BE, CE, GI and HI each appear twice, and the vertices are visited $A$ twice, $B$ twice, $C$ twice, $D$ once, $E$ three times, $F$ twice, $G$ twice, $H$ twice, $I$ three times and $J$ twice.

> **[exam-tip]**
> There are many correct routes and only one correct length, so the length is the safer of the two marks. Work it out from the total network weight rather than by adding up your own route, which is slow and easy to get wrong.
> 
> - The 227.2 is given under Figure 2, so it does not have to be calculated
> - Check your route by counting how many times each vertex appears: a vertex of degree 3 that gains a repeated arc becomes degree 4 and so is passed through twice

### 3((g)) — 2 marks
A route that starts and finishes at different vertices leaves those two vertices odd, so only the other two odd vertices need pairing

$H$ is fixed as the start, so the choice is which of $B$, $C$ and $G$ becomes the finish

Whichever is chosen, the remaining two must be joined by their shortest path, and those three paths are already worked out in part (e)

Finishing at $B$ would repeat $C$ to $G$ at 34.0, finishing at $G$ would repeat $B$ to $C$ at 25.7, and finishing at $C$ would repeat $B$ to $G$ at 25.5, which is the smallest

**Final answer:** **The finishing vertex is C**

**[B1]**

The saving is the repeat total from part (f) less the new repeat total, which is the path from $B$ to $G$ through $F$

$51 . 2 - ( 10 . 3 + 15 . 2 ) = 25 . 7$

$\text{difference in length} = 25 . 7  \text{m}$

**[B1]**

> **[mark-scheme]**
> **B1**: A correct answer only, $C$.
> 
> **B1**: A correct answer only, 25.7.
> 
> The correct method subtracts the new repeated path from the old repeat total, as 51.2 minus the sum of BF and FG.
> 
> Watch this one carefully, because the correct answer can come from incorrect working: adding BE and EC gives 11.2 plus 14.5, which is also 25.7, and that scores nothing. A correct answer of 25.7 with no working at all is given the benefit of the doubt.

> **[exam-tip]**
> The two odd vertices you leave unpaired are exactly the start and the finish, so an open route saves you the cost of joining them. Choose the finish that leaves the cheapest pairing of the two vertices that are left, not the one nearest the start.
> 
> - Every pairing you need is already in the table from part (e), so this part is a comparison rather than a fresh calculation
> - The coincidence here is worth knowing about: 25.5 and 25.7 both appear in part (e), and the two shortest paths BC and BG differ by only 0.2, so check which one you have subtracted
