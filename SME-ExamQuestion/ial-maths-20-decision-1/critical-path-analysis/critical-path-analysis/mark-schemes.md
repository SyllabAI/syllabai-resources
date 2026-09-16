# Mark Schemes — Critical Path Analysis
**Critical Path Analysis** · Edexcel International A Level (IAL) Maths (YMA01) — Decision 1


## Q1 — medium — 16 marks · exam-questions

### 6((a)) — 2 marks
A dummy takes no time and does no work, so the only thing it can be there for is to fix the logic of the network

**(i)**

$F$ ends at event 5 and $J$ starts there, so $J$ needs only $F$ to be finished

$D$ and $E$ both end at event 6, and $I$ starts there, so $I$ needs $D$ and $E$ as well

The dummy carries the finish of $F$ forward into event 6 without letting $D$ or $E$ reach back into event 5

**Final answer:** **The dummy from event 5 to event 6 is there because I depends on D, E and F, while J depends on F alone**

**[B1]**

**(ii)**

$G$ runs from event 4 to event 9 and $H$ runs from event 4 to event 7

Without the dummy, $H$ would have to run from event 4 to event 9 as well, and the two activities would then share both of their events

**Final answer:** **The dummy from event 7 to event 9 is there so that G and H can each be described uniquely by the events at its two ends**

**[B1]**

> **[mark-scheme]**
> **B1**: The dependency reason. Every activity involved must be named: I, J, F and at least one of D and E.
> 
> **B1**: The uniqueness reason. Saying only that the activities can be defined uniquely is not enough on its own: the answer must mention describing an activity by the events at each of its ends.
> 
> The words activity and event must be used correctly for either mark. Give the benefit of the doubt to an answer which implies that two activities would otherwise begin and end at the same pair of events.

> **[exam-tip]**
> There are only two reasons a dummy is ever drawn, and naming which one applies is most of the answer.
> 
> - A dummy for dependency splits a group of activities so that a later one needs some of them and not all
> - A dummy for uniqueness keeps two activities from sharing the same pair of events, so that each can still be named by its start and finish

### 6((b)) — 4 marks
The early event time is the earliest that everything arriving at an event can be finished, so the forward pass takes the LARGEST total along any route into it

Work left to right from event 1, which is 0

Where more than one activity arrives, take the largest: at event 6 the routes give $D$ finishing at 9, $E$ finishing at 11 and the dummy carrying 13 across from event 5, so the early event time is 13

The late event time is the latest an event can happen without pushing the project out, so the backward pass takes the SMALLEST difference along any route leaving it

Work right to left from event 9, which is 21, because the project may not overrun

Where more than one activity leaves, take the smallest: at event 4, $G$ gives $21 - 7 = 14$ and $H$ gives $21 - 6 = 15$, so the late event time is 14

![The completed Diagram 3, with the early event time in the top half of each box and the late event time in the bottom half: event 1 is 0 and 0, event 2 is 5 and 10, event 3 is 4 and 4, event 4 is 7 and 14, event 5 is 13 and 13, event 6 is 13 and 14, event 7 is 13 and 21, event 8 is 15 and 16, and event 9 is 21 and 21.](assets/052-the-completed-diagram-3-with-the-early-event-tim.png)

**[M1 A1 M1 A1]**

> **[mark-scheme]**
> **M1**: All the top boxes complete, with the values generally increasing in the direction of the arrows. One rogue value is condoned.
> 
> **A1**: A correct answer only for all nine top boxes.
> 
> **M1**: All the bottom boxes complete, with the values generally decreasing against the direction of the arrows, so read right to left. One rogue value is condoned.
> 
> **A1**: A correct answer only for all nine bottom boxes.
> 
> The four marks are earned by the one completed diagram, which is why they are shown together beneath it: the two method marks are for the shape of each pass and the two accuracy marks for its values.

> **[exam-tip]**
> Both passes are decided at the events where more than one arc meets, and everywhere else the number simply carries through. There are only three of those events here.
> 
> - A dummy is treated exactly like an activity of duration zero, so it carries a value straight across
> - Check the finish before going on: the early and late times at event 9 must agree, and so must those at event 1

### 6((c)) — 1 marks
The project cannot finish until every activity is done, so the minimum completion time is the early event time at the final event

$\text{minimum project completion time} = 21  \text{hours}$

**[B1]**

> **[mark-scheme]**
> **B1**: 21. The unit is not required for the mark.

> **[exam-tip]**
> This is a read-off from part (b) rather than a fresh calculation, and it is also the check that the two passes agree, since the early and late times at the final event must match.

### 6((d)) — 2 marks
A lower bound shares all of the work out over the shortest time the project can take, and assumes nobody is ever idle

Add up the durations of all eleven activities

$5 + 4 + 7 + 4 + 7 + 9 + 7 + 6 + 2 + 8 + 5 = 64$

Divide by the minimum completion time from part (c)

$\frac{64}{21} \approx 3 . 05$

**[M1]**

Workers come in whole numbers, and three of them could not get through 64 hours of work in 21 hours, so round the answer up

$\text{lower bound} = 4  \text{workers}$

**[A1]**

> **[mark-scheme]**
> **M1**: The total of the activity durations divided by the finishing time, or any total in the range 55 to 73 divided by the finishing time. As a minimum, a value rounding to 3.05, or the truncated 3.04, earns it.
> 
> **A1**: A correct solution only. Either a correct calculation is seen, or a value rounding to 3.05, and then the answer 4.
> 
> An answer of 4 with no working at all scores nothing, so the division has to appear.

> **[exam-tip]**
> Always round a lower bound UP, never to the nearest whole number: 3.05 workers means 4.
> 
> - The bound only says that three workers are impossible; whether four are enough is a separate question, and part (f) shows that even three can finish if the project is allowed one extra hour

### 6((e)) — 4 marks
A cascade chart shows every activity starting as early as it can, with its float drawn on afterwards as the amount it could slip by without delaying the project

Put the critical activities along the top, end to end: they have no float, so together they fill the whole 21 hours

Give each of the other eight activities its own row, starting at its earliest start time, and shade its total float immediately after it

$A$ starts at 0 and lasts 5 hours, and its float is 5, so it is drawn from 0 to 5 with shading from 5 to 10

![A cascade chart on a grid numbered 0 to 26. The top row holds the critical activities end to end: B from 0 to 4, F from 4 to 13 and J from 13 to 21. Below, each activity has its own row with its float shaded: A from 0 to 5 with float to 10, C from 0 to 7 with float to 14, D from 5 to 9 with float to 14, E from 4 to 11 with float to 14, G from 7 to 14 with float to 21, H from 7 to 13 with float to 21, I from 13 to 15 with float to 16, and K from 15 to 20 with float to 21.](assets/054-a-cascade-chart-on-a-grid-numbered-0-to-26-the-t.png)

**[M1 A1 M1 A1]**

> **[mark-scheme]**
> **M1**: At least 8 activities placed, including 5 floats. A scheduling diagram drawn instead of a cascade chart scores nothing here.
> 
> **A1**: The critical activities dealt with correctly, together with four non-critical activities.
> 
> **M1**: All 11 activities placed, including all eight floats, each on the correct non-critical activity.
> 
> **A1**: A correct answer only, with every activity present exactly once.
> 
> The four marks are staged over the one chart, which is why they are shown together beneath it.

> **[exam-tip]**
> Count before you draw: eleven activities and three of them critical means eight rows carrying a float, and that count is exactly what the third mark is checking.
> 
> - Each activity goes at its EARLIEST start, so the chart is read down the left-hand edge rather than across
> - The float on a row is the total float from the network, not the gap to the next activity along

### 6((f)) — 3 marks
A scheduling diagram gives each worker a row and fills it with activities that do not overlap, and no activity may start until everything it depends on is finished

Part (d) shows four workers are needed to finish in 21 hours, but one extra hour is allowed here, so try three

Twenty-two hours with three workers gives 66 worker hours for 64 hours of work, so at most 2 hours can be left idle across the whole schedule

Keep the critical activities on one row, since they run back to back and cannot be moved

Then fill the other two rows in an order that respects the network: $D$ cannot start until $A$ is done, $G$ and $H$ cannot start until $C$ is done, and $K$ cannot start until $I$ is done

![A scheduling diagram on a grid numbered 0 to 26, with three worker rows. The first row is B from 0 to 4, F from 4 to 13 and J from 13 to 21. The second is A from 0 to 5, D from 5 to 9, G from 9 to 16 and H from 16 to 22. The third is C from 0 to 7, E from 7 to 14, I from 14 to 16 and K from 16 to 21.](assets/056-a-scheduling-diagram-on-a-grid-numbered-0-to-26-.png)

**[M1 A1 A1]**

> **[mark-scheme]**
> **M1**: Not a cascade chart. Three workers used, at least 9 activities placed, and a completion time no greater than one hour more than the minimum found in part (c).
> 
> **A1**: Three workers, all 11 activities present exactly once, and a completion time of exactly one hour more than the minimum. One error of either precedence or activity length is condoned.
> 
> **A1**: Three workers, all 11 activities present exactly once, no errors, and a completion time of 22.
> 
> Many different schedules earn full marks. The three marks are staged over the one diagram, which is why they are shown together beneath it.

> **[exam-tip]**
> The worker hours are the quickest way to see whether a schedule can exist at all: three workers for 22 hours is 66 worker hours against 64 hours of work, so there is almost no slack to waste.
> 
> - Place the critical activities first and along one row, because they are the only ones with no freedom at all
> - Check each row across, then check each activity against the network, since the two ways of going wrong are an overlap and a broken precedence

## Q2 — medium — 13 marks · exam-questions

### 4((a)) — 2 marks
The activities immediately preceding an activity are the ones that finish at the event it starts from

Take each blank activity in turn, find the event its arc leaves, and list everything arriving there

A dummy is not an activity, so where a dummy arrives at that event, carry on back through it to the event the dummy comes from

$G$, $H$ and $I$ all leave the event that $B$ and $E$ arrive at, and a dummy brings $A$ across to it as well, so all three follow $A$, $B$ and $E$

$J$ leaves the event that $F$ arrives at, and a dummy brings that same group across, so $J$ follows $A$, $B$, $E$ and $F$

$N$ and $P$ leave the event that $H$ and $K$ arrive at

$Q$ leaves the event that $I$ and $J$ arrive at, with a dummy carrying $H$ and $K$ across, and $R$ leaves the event that $P$ and $Q$ arrive at

Fill those eight entries into the table

| Activity | Immediately preceded by |
|---|---|
| A | – |
| B | – |
| C | – |
| D | A |
| E | C |
| F | C |
| G | **Final answer:** **A, B, E** |
| H | **Final answer:** **A, B, E** |
| I | **Final answer:** **A, B, E** |
| J | **Final answer:** **A, B, E, F** |
| K | D, G |
| L | D, G |
| M | D, G |
| N | **Final answer:** **H, K** |
| P | **Final answer:** **H, K** |
| Q | **Final answer:** **H, I, J, K** |
| R | **Final answer:** **P, Q** |

**[B1 B1]**

> **[mark-scheme]**
> **B1**: Any four of the eight blank rows correct.
> 
> **B1**: All eight blank rows correct.
> 
> The official scheme awards these two marks together, as two marks for the whole table with one mark if at least four of the eight blank rows are right. The nine rows the question already fills in are not part of the award.

> **[exam-tip]**
> List only the IMMEDIATE predecessors. $G$ follows $E$, and $C$ comes before $E$, but $C$ does not go in $G$'s row.
> 
> - The rows the question has already filled in are worth reading first, because they tell you how it wants a dummy handled
> - Where two activities leave the same event they always have the same row, which is a quick check on four of these eight

### 4((b)) — 4 marks
The early event time is the earliest that everything arriving at an event can be finished, so the forward pass takes the LARGEST total along any route into it

Work left to right from the start event, which is 0

Where more than one activity arrives, take the largest: at the event $K$ and $H$ arrive at, $K$ finishes at 30 and $H$ finishes at 20, so the early event time is 30

The late event time is the latest an event can happen without pushing the project out, so the backward pass takes the SMALLEST difference along any route leaving it

Work right to left from the finish event, which is 43, because the project may not overrun

Where more than one activity leaves, take the smallest: at the event $D$ arrives at, $K$ gives $30 - 7 = 23$, $L$ gives $43 - 6 = 37$ and $M$ gives $43 - 6 = 37$, so the late event time is 23

![Diagram 1 completed, with the early event time in the top half of each box and the late event time in the bottom half. Reading left to right, the start event is 0 and 0, the event at the end of A is 9 and 11, the event at the end of C is 9 and 9, the event at the end of B is 12 and 12, the event at the end of D is 23 and 23, the event at the end of F is 22 and 30, the event at the end of L is 29 and 43, the event at the end of H is 30 and 30, the event at the end of J is 30 and 35, the event at the end of P is 37 and 40, and the finish event is 43 and 43.](assets/042-diagram-1-completed-with-the-early-event-time-in.png)

**[M1 A1 M1 A1]**

> **[mark-scheme]**
> **M1**: All the top boxes complete, with the values generally increasing in the direction of the arrows, so generally left to right across the network. One rogue value is condoned, meaning that if ignoring a single value leaves the rest increasing in the direction of the arrows then that counts as one rogue. Every value in the top boxes may be incorrect and this mark is still earned, provided they increase in that way.
> 
> **A1**: A correct answer only for all nine top boxes.
> 
> **M1**: All the bottom boxes complete, with the values generally decreasing against the direction of the arrows, so generally right to left across the network. One rogue value is condoned in the same way. A blank bottom box at the end event is condoned, for the method mark only.
> 
> **A1**: A correct answer only for all nine bottom boxes.
> 
> The four marks are earned by the one completed diagram, which is why they are shown together beneath it: the two method marks are for the shape of each pass and the two accuracy marks for its values.

> **[exam-tip]**
> Only the events where more than one arc meets need a decision; everywhere else the number simply carries through.
> 
> - A dummy behaves exactly like an activity of duration zero, so it carries a value straight across
> - Check the ends before going on: the two numbers must agree at the start event and again at the finish event

### 4((c)) — 1 marks
A critical activity is one with no float at all, so any delay to it delays the whole project

That happens exactly when the early and late event times agree at both ends of its arc and its duration fills the gap between them

Reading the completed diagram, the events where the two numbers agree are the start, the end of $C$, the end of $B$, the end of $D$, the end of $H$ and the finish

Take the activities joining consecutive events in that list where the duration accounts for the whole gap

**Final answer:** **The critical activities are C, E, G, K and N**

**[B1]**

> **[mark-scheme]**
> **B1**: A correct answer only, C, E, G, K and N, with nothing else listed as critical.

> **[exam-tip]**
> Equal numbers in a box are not enough on their own. Both ends of the arc need equal numbers AND the duration has to fill the gap exactly.
> 
> - $M$ runs between two such events here, from 23 to 43, but takes only 6 days, so it is not critical
> - The critical activities always form an unbroken chain from start to finish, which is the quickest check that you have them all

### 4((d)) — 1 marks
The total float of an activity is how long it could be delayed without pushing the project out

Take the LATEST time its finishing event can happen, subtract the EARLIEST time its starting event can happen, then subtract how long the activity itself takes

$J$ starts at the event with early time 22 and finishes at the event with late time 35, and takes 5 days

$35 - 22 - 5 = 8$

$\text{total float for J} = 8  \text{days}$

**[B1]**

> **[mark-scheme]**
> **B1**: A correct calculation. Allow follow-through from your own event times for J, provided the float that results is not negative.
> 
> The answer with no working at all scores nothing: all three numbers must appear in the calculation, which is what the question means by making them clear.

> **[exam-tip]**
> The late time comes from the box at the END of the arc and the early time from the box at the START of it, so the two numbers are read from different boxes.
> 
> - Taking both numbers from the starting box gives the slack at that event instead, which is often the same and is sometimes not
> - A negative answer means the two numbers have been swapped, so it is worth a glance before moving on

### 4((e)) — 1 marks
A lower bound shares all of the work out over the shortest time the project can take, and assumes nobody is ever idle

Figure 2 states the total of all seventeen activity times underneath it, so there is nothing to add up

Divide that total by the minimum completion time of 43 days

$\frac{133}{43} \approx 3 . 09$

Workers come in whole numbers, and three of them could not get through 133 days of work in 43 days, so round up

$\text{lower bound} = 4  \text{workers}$

**[B1]**

> **[mark-scheme]**
> **B1**: A correct solution only. The answer 4, together with either a correct calculation or a value rounding to 3.1.
> 
> An answer of 4 with no working scores nothing, and if any working is shown it must be correct.

> **[exam-tip]**
> Always round a lower bound UP, never to the nearest whole number.
> 
> - The 133 is printed under Figure 2, so this part is one division and a rounding rather than a long addition
> - The bound only rules three workers out; whether four are actually enough is what part (f) settles

### 4((f)) — 4 marks
Part (e) rules out three workers, so try to build a schedule for four

Each row is one worker, working straight through with no float shading, and every activity must sit inside its own time window

Give one worker the critical activities: they have no float, so they run end to end and fill the whole 43 days

Diagram 2 already places $C$ and $A$ on the first two rows and $B$ on the third, so leave those where the question puts them

Fill the rest in one at a time, always checking that everything an activity depends on has already finished

$F$ needs $C$, which finishes at 9, so the third worker waits from 4 until 9

![The completed Diagram 2, a scheduling diagram on a grid numbered 0 to 44 with four worker rows. The first row is C from 0 to 9, E from 9 to 12, G from 12 to 23, K from 23 to 30 and N from 30 to 43. The second row is A from 0 to 9, D from 9 to 21, I from 21 to 33 and L from 33 to 39. The third row is B from 0 to 4, then a gap, F from 9 to 22, H from 22 to 30, J from 30 to 35, Q from 35 to 40 and R from 40 to 43. The fourth row is M from 23 to 29 and P from 30 to 37.](assets/044-the-completed-diagram-2-a-scheduling-diagram-on-.png)

**[M1 A1 A1 A1]**

> **[mark-scheme]**
> **M1**: A scheduling diagram rather than a cascade chart, using at most 5 worker rows, with at least 8 of the new activities placed.
> 
> **A1**: 4 workers, with all 14 new activities present exactly once, 17 in total. Condone at most three errors.
> 
> **A1**: The same, condoning at most one error, which may be a precedence, a time interval or an activity length.
> 
> **A1**: The same again with no errors at all.
> 
> One activity can give rise to at most three errors: one on its duration, one on its time interval and only one on its immediately preceding activities.
> 
> The four marks are staged over the one diagram, which is why they are shown together beneath it.

> **[exam-tip]**
> Put the critical activities on a row to themselves first. They fix the length of the whole diagram and leave a much smaller problem behind.
> 
> - A row may contain gaps, and the third worker here has one from 4 to 9
> - Read each activity's window off the completed Diagram 1 before placing it, rather than checking afterwards

## Q3 — medium — 11 marks · exam-questions

### 2((a)) — 2 marks
The critical path is the longest route through the network, and its length is the minimum completion time of 26 days

$C$, $H$ and $N$ are given as that path, so their three durations must add to 26

$7 + 9 + x = 26$

$x = 10$

**[B1]**

The total float on an activity is the LATE event time where it finishes, minus the EARLY event time where it starts, minus its duration

$B$ leaves the start event, whose early time is 0, and arrives at the event whose late time is 9

$9 - 0 - 5 = 4$

$I$ leaves the event whose early time is 13 and arrives at the event whose late time is 22, so its total float is $22 - 13 - y$, which simplifies to $9 - y$

The float on $B$ is twice the float on $I$

$4 = 2 ( 9 - y )$

$2 = 9 - y$

$y = 7$

**[B1]**

> **[mark-scheme]**
> **B1**: A correct answer only for x, 10. Any working is ignored for this mark.
> 
> **B1**: A correct answer only for y, 7, reached with sufficient working, since the value of y is given in the question. As a minimum, accept $4 = 2 ( 9 - y )$ or any equivalent form; writing $4 = 18 - 2 y$ on its own is not enough.

> **[exam-tip]**
> The second half is a "show that", so the working is what earns the mark and the answer 7 on its own earns nothing.
> 
> - Both floats come from boxes the question already prints, so neither needs the rest of the diagram to be completed first
> - Simplify $22 - 13 - y$ to $9 - y$ before doubling it, since that is the line the scheme names as the minimum acceptable working

### 2((b)) — 3 marks
The early event time is the earliest that everything arriving at an event can be finished, so the forward pass takes the LARGEST total along any route into it

Work left to right from the start event, which is 0

Where more than one arc arrives, take the largest: at the event where $G$, $J$ and the dummy meet, $G$ brings 13, $J$ brings 15 and the dummy carries 16 across, so the early event time is 16

The late event time is the latest an event can happen without pushing the project out, so the backward pass takes the SMALLEST difference along any route leaving it

Work right to left from the final event, which is 26, because the project may not overrun

Where more than one arc leaves, take the smallest: at that same event, $K$ gives $22 - 5 = 17$ and $M$ gives $26 - 3 = 23$, so the late event time is 17

![The completed Diagram 1, with the early event time in the top half of each box and the late event time in the bottom half. The start event is 0 and 0. The event after A is 4 and 7. The event after B is 7 and 9. The event after C is 7 and 7. The event where D and F meet is 13 and 15. The event where G, J and the dummy meet is 16 and 17. The event after H is 16 and 16. The event where I and K meet is 21 and 22. The final event is 26 and 26.](assets/047-the-completed-diagram-1-with-the-early-event-tim.png)

**[M1 M1 A1]**

> **[mark-scheme]**
> **M1**: All the top boxes complete, with the values generally increasing in the direction of the arrows, so read left to right. One rogue value is condoned. All the values may be incorrect and still earn this mark, provided they increase in the way described.
> 
> **M1**: All the bottom boxes complete, with the values generally decreasing against the direction of the arrows, so read right to left. One rogue value is condoned in the same way.
> 
> **A1**: A correct answer only, with every value correct.
> 
> The three marks are earned by the one completed diagram, which is why they are shown together beneath it: a method mark for the shape of each pass and a single accuracy mark for all eighteen values.

> **[exam-tip]**
> Only one accuracy mark is available here for all eighteen numbers, so the two method marks are worth protecting by completing both passes fully even if you are unsure of a value.
> 
> - The two dummies each carry a value straight across, unchanged, in both directions
> - Finish by checking that the early and late times agree at the start event and at the final event

### 2((c)) — 6 marks
A cascade chart puts every activity at its EARLIEST start, with its total float shaded straight afterwards to show how far it could slip without delaying the project

The three critical activities have no float, so they go along the top row end to end and fill the whole 26 days

Give each of the other eleven activities its own row, starting at its earliest start time

$M$ starts at 16 and lasts 3 days, and its float is $26 - 16 - 3 = 7$, so it is drawn from 16 to 19 with shading from 19 to 26

![A cascade chart on a grid numbered 0 to 26. The top row holds the critical activities end to end: C from 0 to 7, H from 7 to 16 and N from 16 to 26. Below, each remaining activity has its own row with its float shaded: A from 0 to 4 with float to 7, B from 0 to 5 with float to 9, D from 4 to 12 with float to 15, E from 4 to 5 with float to 9, F from 7 to 13 with float to 15, G from 7 to 13 with float to 17, I from 13 to 20 with float to 22, J from 13 to 15 with float to 17, K from 16 to 21 with float to 22, L from 21 to 25 with float to 26, and M from 16 to 19 with float to 26.](assets/049-a-cascade-chart-on-a-grid-numbered-0-to-26-the-t.png)

**[M1 A1 A1 A1]**

A lower bound read off the chart is the busiest moment that cannot be avoided, so look for a time when several activities must ALL be under way

An activity is unavoidable at a given time only between its latest start and its earliest finish, so one with plenty of float can always be slid out of the way

Reading down the chart at a time just after 11 days, four activities are running and none of them can be moved clear of that moment

**Final answer:** **At any time strictly between 11 and 12 days, activities D, F, G and H must all be in progress, so the minimum number of workers is 4**

**[M1 A1]**

> **[mark-scheme]**
> **M1**: At least ten different activities labelled, including at least seven floats. A scheduling diagram, or any diagram in which no floats are evident, scores nothing here.
> 
> **A1**: The critical activities C, H and N dealt with correctly and each appearing just once, together with three non-critical activities whose duration and total float are both correct.
> 
> **A1**: Any six non-critical activities correct. This mark does not depend on the previous accuracy mark.
> 
> **A1**: A completely correct chart, with exactly fourteen activities each appearing just once.
> 
> **M1**: Either a statement with the correct number of workers, 4, and the correct activities D, F, G and H together with any numerical time, or the correct number of workers with a time anywhere in the interval 11 to 12 inclusive. Mark the numerical value only and not the way the time is described. In either case the correct number of workers must be stated. This mark is dependent on the first method mark of this part.
> 
> **A1**: A completely correct statement giving both the time and the activities. The time must lie strictly inside 11 to 12.
> 
> An answer given as an interval of time is accepted only if it is correct throughout, so "11 to 12" and "between 11 and 12" both score nothing, while a time of 11.5, or "on day 12", is correct. A completely correct statement spoiled by an extra incorrect statement scores nothing, so nothing is ignored.

> **[exam-tip]**
> Eleven of the fourteen activities carry a float here, and the method mark asks for at least seven of them, so a chart with the floats left off scores nothing at all.
> 
> - $H$ is one of the four activities running at that moment, and it is the critical one, so name it alongside the other three
> - Quote a time strictly inside the interval, such as 11.5 days, because at 11 itself $G$ is only just able to start

## Q4 — medium — 9 marks · exam-questions

### 5((a)) — 5 marks
The activities immediately preceding an activity are the ones that finish at the event it starts from, so work through the table one activity at a time

$A$, $B$ and $C$ depend on nothing, so all three leave the start event

$D$ and $E$ depend on $A$ and $B$, while $F$ and $G$ depend on $B$ and $C$, so $B$ is needed at two different events and a dummy carries it into each of them

$K$ depends on $D$, $E$ and $F$, so bring those three together: $E$ and $F$ already finish at one event, and a third dummy carries the finish of $D$ across to it

$I$ depends on $D$, $E$, $F$ and $G$, so a fourth dummy carries that same event across to the end of $G$

$H$ depends on $D$ alone, so it leaves the event at the end of $D$

$J$ depends on $H$ and $I$, so both finish at one event and $J$ leaves it

$J$ and $K$ have nothing depending on them, so both end at the single finish event

![The activity network drawn from the precedence table, using activity on arc and four dummies. A, B and C leave the start event. Dummies run from the end of B to the event where A finishes and to the event where C finishes. D and E leave the event A finishes at, and F and G leave the event C finishes at. E and F both end at one event, a third dummy runs to it from the end of D, and K leaves it. A fourth dummy runs from that event to the end of G, and I leaves there. H leaves the end of D. H and I both finish at one event, from which J leaves, and J and K both reach the single end event.](assets/037-the-activity-network-drawn-from-the-precedence-t.png)

**[M1 A1 A1 A1 A1]**

> **[mark-scheme]**
> **M1**: At least eight activities labelled on their arcs, one start event, and at least two dummies placed. An activity-on-node diagram scores nothing.
> 
> **A1**: A, B, C and two of D, E, F or G dealt with correctly, so at least one dummy with a correct arrow is needed.
> 
> **A1**: D, E, F and G all dealt with correctly, so the first two dummies with correct arrows are needed.
> 
> **A1**: H and I dealt with correctly, so the final two dummies with correct arrows are needed.
> 
> **A1**: A correct solution only, with J and K dealt with correctly, every arrow correctly placed, one finish event and at most four dummies.
> 
> Dealt with correctly means the activity starts from the correct event, even where it does not also finish at the correct one.
> 
> A network drawn non-planar, with arcs crossing one another, is perfectly acceptable. If no dummy carries an arrow at all then only the method mark is earned. An extra dummy which is unnecessary but still keeps the precedence correct costs only the final accuracy mark.

> **[exam-tip]**
> $B$ is the activity that forces the first two dummies, because it is needed at two different events: once with $A$ and once with $C$.
> 
> - Deal with the pairs first, then the longer lists, since $K$ and $I$ differ by only one activity and that difference is the fourth dummy
> - No duration is given anywhere in this part, so nothing here depends on the times that arrive with Figure 3 in part (b)

### 5((b)) — 4 marks
**(i)**

Figure 3 is a schedule, so each of the three rows is one worker rather than one activity, and the shaded blocks are time a worker spends waiting

The project is finished when the last activity on any row is finished, and $J$ ends the top row

$\text{minimum completion time} = 24  \text{hours}$

**[B1]**

**(ii)**

A critical activity has no float, so the critical activities run end to end with no gap between them and fill the whole 24 hours

Read along the top row of Figure 3: it begins at 0, the four activities on it follow straight on from one another with no gap, and the last of them finishes at 24

**Final answer:** **The critical activities are C, F, I and J**

**[B1]**

**(iii)**

The total float of an activity is the latest time its finishing event can happen, minus the earliest time its starting event can happen, minus how long the activity takes

$G$ can start once $B$ and $C$ are done, so its earliest start is 7, and it must finish in time for $I$ to start at 13, so its latest finish is 13

$13 - 7 - 3 = 3$

$\text{total float for G} = 3  \text{hours}$

**[B1]**

$K$ can start once $D$, $E$ and $F$ are done, so its earliest start is 13, and nothing follows it, so its latest finish is 24

$24 - 13 - 10 = 1$

$\text{total float for K} = 1  \text{hour}$

**[B1]**

> **[mark-scheme]**
> **B1**: A correct answer only, 24. The unit is not required.
> 
> **B1**: A correct answer only, C, F, I and J, with no others.
> 
> **B1**: A correct answer only, the total float for G is 3.
> 
> **B1**: A correct answer only, the total float for K is 1.

> **[exam-tip]**
> The shaded blocks in Figure 3 are a worker waiting, not float. The one before $D$ lasts an hour while $A$'s total float is three, so reading a gap as a float gives the wrong answer.
> 
> - Both floats here can be read straight off the schedule: $G$ finishes at 12 and $I$ cannot start until 13, and $K$ finishes at 23 against a project length of 24
> - A critical activity is one with a float of zero, so part (ii) and part (iii) are the same calculation asked two different ways

## Q5 — medium — 5 marks · exam-questions

### 3() — 5 marks
The activities immediately preceding an activity are the ones that finish at the event it starts from, so work through the table one activity at a time

$A$, $B$ and $C$ depend on nothing, so all three leave the start event

$D$ and $E$ both depend on $A$, $B$ and $C$, so they leave an event that all three reach: $B$ finishes there, and a dummy carries each of $A$ and $C$ across to it

$F$ depends on $C$ alone, so $C$ needs an event of its own for $F$ to leave, which is exactly why the dummy from $C$ is needed

$G$ depends on $F$ alone and $H$ depends on $D$ alone, so each leaves the event at the end of the activity it follows

$J$ depends on $D$ and $E$, so a third dummy carries the finish of $D$ across to the end of $E$, and $J$ leaves from there

$I$ depends on $D$, $E$ and $G$, so a fourth dummy carries that same pair across to the end of $G$

$H$, $I$ and $J$ have nothing depending on them, so all three end at the single finish event

![The activity network drawn from the precedence table, using activity on arc and four dummies. A, B and C leave the start event. Dummies run from the end of A and from the end of C to the end of B, and D and E leave that event. F leaves the end of C and G leaves the end of F. H leaves the end of D. A dummy runs from the end of D to the end of E, and J leaves that event. A fourth dummy runs from that same event to the end of G, and I leaves there. H, I and J all finish at the single end event.](assets/005-the-activity-network-drawn-from-the-precedence-t.png)

**[M1 A1 A1 A1 A1]**

> **[mark-scheme]**
> **M1**: Seven activities labelled on their arcs, one start event, and at least two dummies placed. An activity-on-node diagram scores nothing.
> 
> **A1**: A, B, C, the first two dummies with correct arrows on them, and F all dealt with correctly. The first two dummies are the ones at the ends of A and C.
> 
> **A1**: D, E, G and H dealt with correctly. This mark can be given the benefit of the doubt if the arrows are missing from the first two dummies, provided those dummies are in the right place.
> 
> **A1**: I and J dealt with correctly, which requires the third and fourth dummies with correct arrows on them.
> 
> **A1**: A correct solution only, with every arrow correctly placed, one finish event and at most four dummies.
> 
> Dealt with correctly means the activity starts from the correct event, even where it does not also finish at the correct one. Incorrect or missing numbers on the events are condoned throughout.
> 
> An unlabelled solid line is taken to be an unlabelled activity rather than a dummy, even where a dummy is what belongs there. One unlabelled arc loses the first accuracy mark and the last one, though the second may still be given the benefit of the doubt. Arrows missing from the activities themselves are ignored for the first four marks, but if no dummy carries an arrow at all then only the method mark is earned. An extra dummy which is unnecessary but still keeps the precedence correct costs only the final accuracy mark.
> 
> This is not the only correct network: the scheme notes that A and B could be interchanged, so a diagram which gives B its own event and runs the dummy from there is equally right.

> **[exam-tip]**
> A dummy is needed wherever one activity depends on a group and another depends on only part of that group, and all four here come from that one pattern.
> 
> - The first two dummies are there so that $F$ can follow $C$ alone while $D$ and $E$ follow $A$, $B$ and $C$ together
> - Every dummy needs an arrow, because the direction is what carries the dependency, and a dummy with no arrow costs four of the five marks

## Q6 — medium — 10 marks · exam-questions

### 4((a)) — 4 marks
The total float on an activity is the LATE event time where it finishes, minus the EARLY event time where it starts, minus its duration

$F$ leaves the event whose early time is 8 and arrives at the event whose late time is 22, so its total float is $22 - 8 - y$

$D$ leaves the event whose early time is 3 and arrives at the event whose late time is 8, so its total float is $8 - 3 - x$

The first condition says that the float on $F$ is twice the float on $D$

$22 - 8 - y = 2 ( 8 - 3 - x )$

$2 x - y = - 4$

**[B1]**

The critical path takes 26 days, which is the early event time at the final event

The second condition says that $B$, $D$, $F$ and $M$ together take 10 days less than that, so add their four durations

$3 + x + y + 3 = 26 - 10$

$x + y = 10$

**[B1]**

Adding the two equations removes $y$, leaving one equation in $x$

$3 x = 6$

**[M1]**

Divide by 3, then substitute that value back into $x + y = 10$

**Final answer:** $x = 2$** and **$y = 8$

**[A1]**

> **[mark-scheme]**
> **B1**: A correct answer only for the float equation, in any equivalent form. Allow $14 - y = 2 ( 5 - x )$ or $14 - y = 10 - 2 x$.
> 
> **B1**: A correct answer only for the path equation, in any equivalent form. Allow $x + y + 6 = 16$.
> 
> **M1**: Setting up two equations both including x and y, and an attempt to solve them for both letters, leading to a value for each. This mark is dependent on one of the equations being correct, and it may be implied by two equations in x and y with at least one correct, followed by values for x and y.
> 
> **A1**: A correct answer only, $x = 2$ and $y = 8$.
> 
> Both correct values stated with no working or justification at all are sent to review rather than credited, which is what the instruction to make your method and working clear is asking for.

> **[exam-tip]**
> Each condition turns into one equation, and both equations have to carry both letters before they can be solved together.
> 
> - The path condition is about DURATIONS, so add the four activity times rather than reading anything off the event boxes
> - Take each float at the event where the activity FINISHES: using the late time at its starting event gives the event slack instead, which is a different number for both $D$ and $F$

### 4((b)) — 4 marks
A cascade chart puts every activity at its EARLIEST start, with its total float shaded straight afterwards to show how far it could slip without delaying the project

The four critical activities have no float, so they go along the top row end to end and fill the whole 26 days

Give each of the other nine activities its own row, starting at its earliest start time

$F$ starts at 8 and lasts 8 days now that $y$ is known, and its float is $22 - 8 - 8 = 6$, so it is drawn from 8 to 16 with shading from 16 to 22

![A cascade chart on a grid numbered 0 to 28. The top row holds the critical activities end to end: A from 0 to 8, G from 8 to 13, I from 13 to 22 and L from 22 to 26. Below, each remaining activity has its own row with its float shaded: B from 0 to 3 with float to 5, C from 0 to 4 with float to 6, D from 3 to 5 with float to 8, E from 4 to 11 with float to 13, F from 8 to 16 with float to 22, H from 3 to 11 with float to 13, J from 13 to 21 with float to 23, K from 13 to 21 with float to 23, and M from 22 to 25 with float to 26.](assets/004-a-cascade-chart-on-a-grid-numbered-0-to-28-the-t.png)

**[M1 A1 A1 A1]**

> **[mark-scheme]**
> **M1**: At least nine activities labelled, including at least five floats. A scheduling diagram drawn instead scores nothing here.
> 
> **A1**: The critical activities A, G, I and L dealt with correctly and each appearing just once, together with three non-critical activities dealt with correctly.
> 
> **A1**: Any six non-critical activities correct. This mark does not depend on the previous accuracy mark.
> 
> **A1**: A completely correct chart, with exactly thirteen activities each appearing just once.
> 
> The four marks are staged over the one chart, which is why they are shown together beneath it.

> **[exam-tip]**
> Part (a) has to be finished before this chart can be drawn at all, since $D$ and $F$ have no lengths until $x$ and $y$ are known.
> 
> - $J$ and $K$ have the same start, the same length and the same float, so their two rows are identical and it is worth checking you have drawn both
> - The float shaded after an activity is its TOTAL float from the network, not the gap to whatever comes next along the row

### 4((c)) — 2 marks
A lower bound read off the cascade chart is the busiest moment that cannot be avoided, so look for a time when several activities must ALL be under way

An activity is unavoidable at a given time only between its latest start and its earliest finish, so one with plenty of float can always be slid out of the way

Reading down the chart at a time just after 15 days, four activities are running and none of them can be moved clear of that moment

**Final answer:** **At any time strictly between 15 and 16 days, activities F, I, J and K must all be in progress, so the minimum number of workers is 4**

**[M1 A1]**

> **[mark-scheme]**
> **M1**: Either a statement with the correct number of workers, 4, and the correct activities F, I, J and K together with any numerical time, or the correct number of workers with a time anywhere in the interval 15 to 16 inclusive. Mark the numerical value only and not the way the time is described. In either case the correct number of workers must be stated. The critical activity has to be named explicitly, so listing F, J, K and "the critical activity" scores nothing.
> 
> **A1**: A completely correct statement giving both the time and the activities. The time must lie strictly inside 15 to 16.
> 
> An answer given as an interval of time is accepted only if it is correct throughout, so a time of 15 to 16 scores nothing here, while "on day 16" is correct and "on day 15" is not. A completely correct statement spoiled by an extra incorrect statement scores nothing, so nothing is ignored.

> **[exam-tip]**
> Read the command word before deciding what to work out. "Use your cascade chart" and "specific reference to time and activities" ask for the busiest unavoidable moment, whereas "calculate a lower bound, showing your working" would ask for the total work divided by the project length, which here gives 3 rather than 4.
> 
> - $I$ is one of the four, and it is the critical activity running at that moment, so name it rather than describing it
> - Quote a time strictly inside the interval, such as 15.5 days, because at 15 itself $J$ and $K$ are only just able to start

## Q7 — medium — 11 marks · exam-questions

### 4((a)) — 2 marks
The activities immediately preceding an activity are the ones that finish at the event it starts from, so take each activity in turn and look at what arrives where its arc begins

A dummy is not an activity, so where a dummy arrives at that event, carry on back through it to the event the dummy comes from

$A$ and $B$ both leave the start event, so neither has anything before it

$C$ and $D$ leave the event $A$ arrives at, and $E$, $I$ and $J$ leave the event $B$ arrives at, which a dummy also reaches from the end of $A$

$H$ leaves the event $D$ and $E$ arrive at, and a dummy brings $C$ across to it as well

$K$ leaves the event $F$ arrives at, while $L$ leaves the event $G$, $H$ and $I$ arrive at, with a dummy bringing $F$ across

$M$ leaves the event $J$ arrives at, and a second dummy brings that whole group forward, so $M$ follows five activities

| Activity | Immediately preceding activities |
|---|---|
| A | **Final answer:** **–** |
| B | **Final answer:** **–** |
| C | **Final answer:** **A** |
| D | **Final answer:** **A** |
| E | **Final answer:** **A, B** |
| F | **Final answer:** **C** |
| G | **Final answer:** **C** |
| H | **Final answer:** **C, D, E** |
| I | **Final answer:** **A, B** |
| J | **Final answer:** **A, B** |
| K | **Final answer:** **F** |
| L | **Final answer:** **F, G, H, I** |
| M | **Final answer:** **F, G, H, I, J** |

**[B1] [B1]**

> **[mark-scheme]**
> **B1**: Any six rows correct, not counting the rows for A and B.
> 
> **B1**: A correct answer only, condoning blank rows for A and B.
> 
> The official scheme awards these two marks together, as two marks for the whole table with one mark if any six of the rows other than A and B are right. A and B have nothing before them, so a dash and a blank are both accepted there.

> **[exam-tip]**
> List only the IMMEDIATE predecessors. $K$ follows $F$, and $C$ comes before $F$, but $C$ does not go in $K$'s row.
> 
> - Activities leaving the same event always have the same row, which fixes C and D together, E, I and J together, and L and M almost together
> - $M$ is the one to check last, because the second dummy gives it a longer list than $L$ even though the two look alike on the diagram

### 4((b)) — 3 marks
$v$ is the duration of $C$, and the event $C$ arrives at has an early time of 12 while the event it leaves has an early time of 5

$12 - 5 = 7$

$x$ is a LATE event time, so take the smallest difference along the three arcs leaving that event: $D$ gives $13 - 4 = 9$, while $C$ and the dummy both give 6

$13 - 7 = 6$

$z$ is a LATE event time too, and of the two arcs leaving that event the dummy carries 20 across while $K$ gives the smaller value

$25 - 6 = 19$

$w$ and $y$ cannot be found from Figure 2 alone, so read them off Grid 1: $F$ runs from 12 to 16, and $K$ begins at 16

**Final answer:** $v = 7$**, **$w=4$**, **$x = 6$**, **$y = 16$** and **$z = 19$

**[B1] [B1] [B1]**

> **[mark-scheme]**
> **B1**: Any two correct values.
> 
> **B1**: Any three correct values.
> 
> **B1**: All five values correct.
> 
> The official scheme awards these three marks together, staged by how many of the five values are right rather than by which ones, so no single value carries a mark of its own.

> **[exam-tip]**
> The stem says to use Figure 2 AND Grid 1, and that is a real instruction: $w$ and $y$ are not recoverable from the network alone, because $F$ is the only arc into its event and so nothing there pins its length.
> 
> - Read $w$ as the length of $F$'s white bar, from 12 to 16, and $y$ as the time $K$'s bar begins
> - Check the two against each other: $y$ must equal $12 + w$, since $K$ starts as soon as $F$ is finished

### 4((c)) — 1 marks
A lower bound shares all of the work out over the shortest time the project can take, and assumes nobody is ever idle

Add up the durations of all thirteen activities, then divide by the completion time of 25 days

$5 + 6 + 7 + 4 + 7 + 4 + 5 + 7 + 10 + 4 + 6 + 5 + 4 = 74$

$\frac{74}{25} = 2 . 96$

Workers come in whole numbers, so round up

$\text{lower bound} = 3  \text{workers}$

**[B1]**

> **[mark-scheme]**
> **B1**: A correct answer only, 3, from correct working. As a minimum for correct working, accept either the value 2.96 or the sum of the thirteen durations written over 25.

> **[exam-tip]**
> This is only ONE mark, but the working still has to appear: a bare 3 scores nothing.
> 
> - The bound says three workers might be enough; it does not say they are, and part (d) is where that gets settled

### 4((d)) — 3 marks
A scheduling diagram gives each worker a row and fills it with activities that do not overlap, and no activity may start until everything it depends on is finished

Try three workers first, since that is the bound from part (c)

Three workers cannot do it. Three workers over 25 days is 75 worker days for 74 days of work, so at most one worker day can be left idle in the whole schedule, but at time 0 only $A$ and $B$ can start, so a third worker would have nothing to do for the first five days

So four workers are needed, and the project still finishes in 25 days

Keep the critical activities on one row, then fill the others in an order that respects the table

![A scheduling diagram on a grid numbered 0 to 26, with four worker rows. The first row is B from 0 to 6, E from 6 to 13, H from 13 to 20 and L from 20 to 25. The second is A from 0 to 5, C from 5 to 12, F from 12 to 16, J from 16 to 20 and M from 20 to 24. The third is D from 5 to 9, G from 12 to 17 and K from 17 to 23. The fourth is I from 6 to 16.](assets/036-a-scheduling-diagram-on-a-grid-numbered-0-to-26-.png)

**[M1 A1 A1]**

> **[mark-scheme]**
> **M1**: Not a cascade chart. At most four workers used, and at least nine activities placed.
> 
> **A1**: Four workers, all thirteen activities present exactly once. At most two errors are condoned, and one activity can give rise to at most three errors: one on its duration, one on its time interval and only one on its preceding activities.
> 
> **A1**: Four workers, all thirteen activities present exactly once, with no errors.
> 
> Many different schedules earn full marks, but all of them use four workers. The three marks are staged over the one diagram, which is why they are shown together beneath it.

> **[exam-tip]**
> A lower bound is a bound, not a promise. Part (c) gives three and this part needs four, which happens whenever the precedence forces workers to wait.
> 
> - $I$ lasts 10 days and cannot start before day 6, so it ties up one worker for most of the project
> - Draw the critical row first, because those four activities fill all 25 days and nothing about them can move

### 4((e)) — 2 marks
Adding 5 to the duration of $F$ lengthens every route that uses $F$, and leaves every other route alone

$F$ now takes 9, so the route $A$, $C$, $F$, $K$ takes $5 + 7 + 9 + 6$

$5 + 7 + 9 + 6 = 27$

Every other route is shorter than this, so the project now takes 27 days and that route is the critical one

$\text{new minimum completion time} = 27  \text{days}$

**[B1]**

**Final answer:** **The new critical path is A C F K**

**[B1]**

> **[mark-scheme]**
> **B1**: A correct answer only, 27.
> 
> **B1**: A correct answer only, A C F K, or the same path written backwards as K F C A.

> **[exam-tip]**
> Five extra days on $F$ lengthen the project by only two, because $F$ had three days of float to absorb first.
> 
> - The old critical path was $B$, $E$, $H$, $L$ and it still takes 25 days, so the change is entirely about the route through $F$ overtaking it
> - Check by recomputing the forward pass: the event $F$ arrives at moves from 16 to 21, and $K$ then finishes at 27

## Q8 — medium — 10 marks · exam-questions

### 2((a)) — 4 marks
The early event time is the earliest that everything arriving at an event can be finished, so the forward pass takes the LARGEST total along any route into it

Work left to right from the start event, which is 0

Where more than one activity arrives, take the largest: at the event $D$ and $F$ arrive at, $D$ finishes at 8 and $F$ finishes at 9, and the dummy brings 14 across from the end of $G$, so the early event time is 14

The late event time is the latest an event can happen without pushing the project out, so the backward pass takes the SMALLEST difference along any route leaving it

Work right to left from the finish event, which is 28, because the project may not overrun

Where more than one activity leaves, take the smallest: at the event $H$ and $I$ arrive at, $M$ gives $24 - 7 = 17$ and $Q$ gives $28 - 8 = 20$, so the late event time is 17

![The completed Diagram 1, with the early event time in the top half of each box and the late event time in the bottom half. The start event is 0 and 0. The event at the end of A is 3 and 7. The event where A, B and E meet is 7 and 7. The event at the end of C is 2 and 2. The event where D, F and the dummy meet is 14 and 14. The event at the end of G is 14 and 14. The event where H, I and the dummy meet is 14 and 17. The event at the end of J is 20 and 20. The event where K, L, M and N meet is 24 and 24. The finish event is 28 and 28.](assets/029-the-completed-diagram-1-with-the-early-event-tim.png)

**[M1 A1 M1 A1]**

> **[mark-scheme]**
> **M1**: All the top boxes complete, with the values generally increasing in the direction of the arrows, so generally left to right across the network. A missing 0 at the start event is condoned for this mark. One rogue value is condoned, meaning that if ignoring a single value leaves the rest increasing in the direction of the arrows then that counts as one rogue. Every value in the top boxes may be incorrect and this mark is still earned, provided they increase in that way.
> 
> **A1**: A correct answer only for all ten top boxes.
> 
> **M1**: All the bottom boxes complete, with the values generally decreasing against the direction of the arrows, so generally right to left across the network. A blank bottom box at the end of P or Q, or at the start node, is condoned for this method mark only. One rogue value is condoned in the same way.
> 
> **A1**: A correct answer only for all ten bottom boxes.
> 
> The four marks are earned by the one completed diagram, which is why they are shown together beneath it: the two method marks are for the shape of each pass and the two accuracy marks for its values.

> **[exam-tip]**
> Two of the three dummies leave the same event, the one at the end of $G$, so the value 14 is carried into two places at once.
> 
> - A dummy behaves exactly like an activity of duration zero, so it moves a value sideways without changing it
> - Only the events where more than one arc meets need a decision; everywhere else the number simply carries through

### 2((b)) — 4 marks
A cascade chart shows every activity starting as early as it can, with its float drawn on afterwards as the amount it could slip by without delaying the project

Put the critical activities along the top, end to end: they have no float, so together they fill the whole 28 hours

Give each of the other ten activities its own row, starting at its earliest start time, and shade its total float immediately after it

$A$ starts at 0 and lasts 3 hours, and its float is 4, so it is drawn from 0 to 3 with shading from 3 to 7

![A cascade chart on a grid numbered 0 to 32. The top row holds the critical activities end to end: C from 0 to 2, E from 2 to 7, G from 7 to 14, J from 14 to 20, N from 20 to 24 and P from 24 to 28. Below, each activity has its own row with its float shaded: A from 0 to 3 with float to 7, B from 0 to 4 with float to 7, D from 3 to 8 with float to 14, F from 7 to 9 with float to 14, H from 7 to 13 with float to 17, I from 2 to 6 with float to 17, K from 14 to 22 with float to 24, L from 14 to 18 with float to 24, M from 14 to 21 with float to 24, and Q from 14 to 22 with float to 28.](assets/031-a-cascade-chart-on-a-grid-numbered-0-to-32-the-t.png)

**[M1 A1 A1 A1]**

> **[mark-scheme]**
> **M1**: At least ten different activities labelled, including at least six floats. A scheduling diagram, meaning one in which no floats are evident, scores nothing here.
> 
> **A1**: The six critical activities dealt with correctly and appearing just once, together with three non-critical activities correct in both duration and total float.
> 
> **A1**: Any six non-critical activities correct. This mark does not depend on the previous one.
> 
> **A1**: A completely correct chart, with exactly sixteen activities appearing just once.
> 
> The critical activities may share one line, as here, or take separate lines, provided the durations and floats are clear and do not overlap. The floats need not be shaded, provided they are clearly distinguishable from the duration of the activity.

> **[exam-tip]**
> Count before you draw: sixteen activities and six of them critical means ten rows carrying a float, and that count is what the last mark is checking.
> 
> - Each activity goes at its EARLIEST start, so the chart is read down the left-hand edge rather than across
> - The float on a row is the total float from the network, not the gap to the next activity along

### 2((c)) — 2 marks
One worker can only do one activity at a time, so the number needed is at least the number of activities that have to be in progress at the same moment

An activity with float can be slid later, so it does not have to be running at any particular time

An activity is unavoidable at a given moment only when that moment falls after the latest it could start and before the earliest it could finish

Read down the chart looking for the moment where the most activities are unavoidable

Just after 20 hours, $J$ has finished but $K$, $M$, $N$ and $Q$ are all still running and none of them can be moved clear

**Final answer:** **A minimum of 4 workers is needed, because at time 20.5 hours activities K, M, N and Q must all be in progress**

**[M1 A1]**

> **[mark-scheme]**
> **M1**: Either 4 workers together with the correct activities K, M, N and Q and any numerical time, or 4 workers together with a time in the interval 20 to 21 inclusive.
> 
> **A1**: A completely correct statement, giving both a time strictly inside 20 to 21, such as 20.5, and the activities K, M, N and Q.
> 
> A time of 20 itself is wrong, and an answer given as the interval 20 to 21 scores nothing, because it is not correct for all the values in it. A completely correct statement accompanied by an incorrect one earns no accuracy mark, so subsequent working is not ignored here.

> **[exam-tip]**
> Quote a time that is strictly between two whole numbers, such as 20.5. At 20 exactly one activity is finishing as others begin, and the scheme treats that as wrong.
> 
> - This is not the same question as a lower bound from the total work: that division gives 3 here, and the chart gives 4
> - Counting the boxes a vertical line crosses is not the test either, since an activity with float can simply be moved out of the way

## Q9 — medium — 9 marks · exam-questions

### 6((a)) — 5 marks
The activities immediately preceding an activity are the ones that finish at the event it starts from, so work through the table one activity at a time

$A$, $B$ and $C$ depend on nothing, so all three leave the start event

$F$ depends on $A$, $B$ and $C$, so it leaves an event that all three reach: $B$ finishes there, and a dummy carries each of $A$ and $C$ across to it

$D$ and $E$ depend on $A$ alone and $G$ depends on $C$ alone, so $A$ and $C$ each need a separate event, which is exactly why those two dummies are needed

$H$ depends on $G$ alone, so it leaves the event at the end of $G$

$I$ depends on $D$, $E$, $F$ and $H$, so bring all four into one event: $E$, $F$ and $H$ finish there and a third dummy carries the finish of $D$ across

$J$, $K$ and $L$ all depend on $I$ alone, so all three leave the event at the end of $I$

$M$ depends on $L$ alone, so it leaves the event at the end of $L$

$J$, $K$ and $M$ have nothing depending on them, so all three end at the finish event, and a fourth dummy separates $J$ from $K$, because two activities may not join the same pair of events

![The activity network drawn from the precedence table, using activity on arc and four dummies. A, B and C leave the start event. Dummies run from the end of A and from the end of C to the end of B, and F leaves that event. D and E leave the end of A, and G leaves the end of C. H leaves the end of G. E, F and H all finish at one event, a third dummy runs to it from the end of D, and I leaves it. J, K and L leave the end of I. M leaves the end of L. K and M reach the finish event directly, and a fourth dummy runs from the end of J to the finish.](assets/026-the-activity-network-drawn-from-the-precedence-t.png)

**[M1 A1 A1 A1 A1]**

> **[mark-scheme]**
> **M1**: Eight activities labelled on their arcs, one start event, and at least two dummies placed. An activity-on-node diagram scores nothing.
> 
> **A1**: A, B, C, the first two dummies, D, E and G all dealt with correctly. The first two dummies are the ones at the ends of A and C, and both must carry arrows in the correct direction.
> 
> **A1**: F, H and the third dummy dealt with correctly. The third dummy is the one at the end of D, and it must carry an arrow in the correct direction.
> 
> **A1**: I, J, K, L and M dealt with correctly.
> 
> **A1**: A correct solution only, with every arrow correctly placed, one finish event, and a fourth dummy carrying a correct arrow at the end of J.
> 
> Dealt with correctly means the activity starts from the correct event, even where it does not also finish at the correct one. For I this means D, E, F and H all lead into the same event, with the help of a dummy if needed, and that I starts from it. Incorrect or missing numbers on the events are condoned throughout.
> 
> An unlabelled solid line is taken to be an unlabelled activity rather than a dummy, even where a dummy is what belongs there. One unlabelled arc loses the first accuracy mark and the last one, though the second may still be given the benefit of the doubt. Arrows missing from the activities themselves are ignored for the first four marks, but if no dummy carries an arrow at all then only the method mark is earned. An extra dummy which is unnecessary but still keeps the precedence correct costs only the final accuracy mark.
> 
> This is not the only correct network. D and E may be interchanged, and so may J and K. The dummy at the end of D may instead be drawn before D, and the same for the dummy at the end of J, whose arrow may also point the other way.

> **[exam-tip]**
> The last dummy is doing a different job from the first three. Those three carry a dependency; this one carries nothing and is there only because $J$ and $K$ would otherwise be two arcs joining the same pair of events.
> 
> - The tell is that its direction does not matter, which the scheme says outright: reversing it still keeps $J$ and $K$ apart
> - $I$ has the longest list, so settling where it starts fixes most of the diagram before you draw anything after it

### 6((b)) — 2 marks
A critical activity lies on a critical path, and every critical path runs from the start event to the finish event

So an activity that lies on EVERY route through the network must lie on the critical path, whichever route that turns out to be

Follow the table: $D$, $E$ and $F$ all lead into $I$, and so does $H$ by way of $G$, while $J$, $K$, $L$ and $M$ all follow it

That accounts for every activity, so no route can avoid $I$

**Final answer:** **Activity I is guaranteed to be critical**

**[M1]**

**Final answer:** **This is because every path through the network contains activity I**

**[A1]**

> **[mark-scheme]**
> **M1**: Activity I only. Naming more than one activity as critical scores nothing.
> 
> **A1**: A correct reason. It must say that every path, or every route, through the network contains I. Wording such as "there is no route that does not contain I" is fine.
> 
> The word matters here: "everything passes through I" earns the first mark only, because it does not name a path or a route, while "every route passes through I" earns both.

> **[exam-tip]**
> An activity is guaranteed critical when the network has a pinch point, and you can find one without any durations at all.
> 
> - Look for the activity that every other activity is either before or after, which here is $I$
> - Say "every path" or "every route" in the reason, since the scheme refuses a vaguer version of the same idea

### 6((c)) — 2 marks
When every activity takes the same time, the longest route is simply the one through the most activities

Dummies take no time, so they add nothing to the count

The longest route runs through six activities, and every other route runs through five or fewer

Each activity takes 2 hours, so multiply the count by 2

$6 \times 2 = 12$

$\text{minimum completion time} = 12  \text{hours}$

**[B1]**

**Final answer:** **The critical path is C – G – H – I – L – M**

**[B1]**

> **[mark-scheme]**
> **B1**: A correct answer only, 12.
> 
> **B1**: A correct answer only, C, G, H, I, L and M.

> **[exam-tip]**
> Part (b) told you $I$ is on the critical path, so you only have to find the longest way into it and the longest way out of it.
> 
> - Into $I$ the longest run is $C$, $G$, $H$ at three activities, and every other way in takes exactly two
> - Out of $I$ the longest run is $L$ then $M$, at two, against one each for $J$ and $K$

## Q10 — medium — 13 marks · exam-questions

### 6((a)) — 3 marks
The activities immediately preceding an activity are the ones that finish at the event it starts from, so each new activity leaves the event that everything in its list arrives at

$G$, $H$ and $I$ all follow $B$, $C$ and $E$, and so does $K$, which is already drawn

So all three leave the same event that $K$ leaves: $B$ and $E$ already arrive there, and a dummy carries $C$ across to it

$L$ and $M$ follow $F$, $G$ and $K$, while $N$ follows $F$ and $G$ alone, so $G$ must end where $F$ ends and a second dummy carries that pair forward into the event $L$ and $M$ leave

$H$ ends where $D$ ends, because $J$ follows $D$ and $H$, and $I$ has nothing following it, so it runs straight to the finish event

![The completed activity network. G runs from the event B and E arrive at to the event F arrives at. H runs from that same event to the event D arrives at. I runs from it to the finish event. A dummy runs from the end of C into the event B and E arrive at, and a second dummy runs from the event F and G arrive at into the event K arrives at.](assets/022-the-completed-activity-network-g-runs-from-the-e.png)

**[B1] [B1] [B1]**

> **[mark-scheme]**
> **B1**: Any two of the five new arcs drawn correctly. An activity must be labelled with the correct letter, and a dummy must be dashed, or labelled as a dummy, and carry no weight.
> 
> **B1**: Four of the five new arcs drawn correctly, judged the same way.
> 
> **B1**: A correct solution only: all three activities and both dummies, with no extras, every letter and weight correct and every arrow correct.
> 
> Missing or wrong arrows are condoned for the first two marks but not for the third. An activity drawn as a dashed line is condoned for full marks provided it carries the correct letter.

> **[exam-tip]**
> Read down the "immediately preceding" column looking for repeats. $G$, $H$, $I$ and $K$ share the same list, so all four leave the same event, and $K$ is already drawn for you.
> 
> - The second dummy is needed because $N$ follows $F$ and $G$ only, while $L$ and $M$ also need $K$
> - Check your answer by reading the precedence back off the drawing rather than by comparing pictures, since several correct networks look different

### 6((b)) — 4 marks
The early event time is the earliest that everything arriving at an event can be finished, so the forward pass takes the LARGEST total along any route into it

Work left to right from the start event, which is 0

Where more than one arc arrives, take the largest: at the event $G$, $H$, $I$ and $K$ leave, $B$ finishes at 7, $E$ finishes at 9 and the dummy carries 6 across from the end of $C$, so the early event time is 9

The late event time is the latest an event can happen without pushing the project out, so the backward pass takes the SMALLEST difference along any route leaving it

Work right to left from the finish event, which is 28, because the project may not overrun

Where more than one arc leaves, take the smallest: at that same event, $G$ gives $16 - 6 = 10$, $H$ gives $19 - 6 = 13$, $I$ gives $28 - 7 = 21$ and $K$ gives $17 - 8 = 9$, so the late event time is 9

![The completed Diagram 1, with the early event time in the top half of each box and the late event time in the bottom half. The start event is 0 and 0. The event after A is 4 and 4. The event where B, E and the first dummy meet is 9 and 9. The event after C is 6 and 9. The event where D and H meet is 15 and 19. The event where F and G meet is 15 and 16. The event where K and the second dummy meet is 17 and 17. The event where M and N meet is 23 and 23. The finish event is 28 and 28.](assets/023-the-completed-diagram-1-with-the-early-event-tim.png)

**[M1 A1 M1 A1]**

> **[mark-scheme]**
> **M1**: All the top boxes complete, with the values generally increasing in the direction of the arrows, so read left to right. One rogue value is condoned, and all the values may be incorrect and still earn this mark provided they increase in the way described. This mark is dependent on the first mark of part (a) having been awarded.
> 
> **A1**: A correct answer only for the top boxes.
> 
> **M1**: All the bottom boxes complete, with the values generally decreasing against the direction of the arrows, so read right to left. One rogue value is condoned, and a missing 28 or a missing 0 at the end events is condoned for this mark. It carries the same dependency on part (a).
> 
> **A1**: A correct answer only for the bottom boxes.
> 
> For full marks here, all three activities and both dummies must have been added correctly in part (a), condoning missing arrows only.

> **[exam-tip]**
> The event $G$, $H$, $I$ and $K$ leave is the busiest one in the diagram, with three arcs arriving and four leaving, so it is where both passes are decided.
> 
> - A dummy is treated as an activity of duration zero, so it carries a value straight across in both directions
> - $I$ runs from that event all the way to the finish, which is why its late time comes out so much larger than the others and does not affect the answer

### 6((c)) — 1 marks
An activity is critical when it has no total float, so any delay to it delays the whole project

Those are the activities whose start and finish events both have equal early and late times, and which fill the whole gap between them

**Final answer:** **The critical activities are A, E, K, M and P**

**[B1]**

> **[mark-scheme]**
> **B1**: A correct answer only, A, E, K, M and P.

> **[exam-tip]**
> The critical activities always form a complete path from the start event to the finish event, so reading them off as a route is the quickest check that none has been missed.
> 
> - Here that route is $A$, then $E$, then $K$, then $M$, then $P$, and $4 + 5 + 8 + 6 + 5$ comes to the 28 days the project takes

### 6((d)) — 2 marks
A lower bound shares all of the work out over the shortest time the project can take, and assumes nobody is ever idle

Add up the durations of all fifteen activities

$4 + 7 + 6 + 10 + 5 + 7 + 6 + 6 + 7 + 9 + 8 + 4 + 6 + 7 + 5 = 97$

Divide by the minimum completion time of 28 days

$\frac{97}{28} \approx 3 . 46$

**[M1]**

Workers come in whole numbers, and three of them could not get through 97 days of work in 28 days, so round the answer up

$\text{lower bound} = 4  \text{workers}$

**[A1]**

> **[mark-scheme]**
> **M1**: The total of the activity durations divided by the minimum completion time.
> 
> **A1**: A correct solution only, so the division has to be seen and the answer rounded up to 4. An answer of 4 with no working at all scores nothing.

> **[exam-tip]**
> Always round a lower bound UP, never to the nearest whole number: 3.46 workers means 4.
> 
> - The bound only says that three workers are impossible; whether four are enough is a separate question, and part (e) is what settles it

### 6((e)) — 3 marks
A scheduling diagram gives each worker a row and fills it with activities that do not overlap, and no activity may start until everything it depends on is finished

Part (d) shows that at least four workers are needed, so try four

Four workers over 28 days gives 112 worker days for 97 days of work, so 15 days can be left idle in total

Keep the critical activities on one row, since they run back to back and cannot be moved

Then fill the other rows in an order that respects the table: $D$ cannot start until $A$ is done, $G$, $H$ and $I$ cannot start until $B$, $C$ and $E$ are all done, and $P$ cannot start until both $M$ and $N$ are done

![A scheduling diagram on a grid numbered 0 to 32, with four worker rows. The first row is A from 0 to 4, E from 4 to 9, K from 9 to 17, M from 17 to 23 and P from 23 to 28. The second is B from 0 to 7, D from 7 to 17, I from 17 to 24 and L from 24 to 28. The third is C from 0 to 6, F from 6 to 13, H from 13 to 19 and J from 19 to 28. The fourth is G from 9 to 15 and N from 15 to 22.](assets/025-a-scheduling-diagram-on-a-grid-numbered-0-to-32-.png)

**[M1 A1 A1]**

> **[mark-scheme]**
> **M1**: Not a cascade chart. At most five workers used, and at least eleven activities placed.
> 
> **A1**: Four workers, all fifteen activities present exactly once. At most two errors are condoned, and one activity can give rise to at most three errors: one on its duration, one on its time interval and only one on its preceding activities.
> 
> **A1**: Four workers, all fifteen activities present exactly once, with no errors.
> 
> Many different schedules earn full marks. The three marks are staged over the one diagram, which is why they are shown together beneath it.

> **[exam-tip]**
> Place the critical activities first and along one row, because they are the only ones with no freedom at all, and then everything else has to fit around them.
> 
> - $I$ is the loosest activity here, with twelve days of float, so leave it until last and use it to fill a gap
> - Check each row across for an overlap, then check each activity against the precedence table, since those are the two ways a schedule goes wrong

## Q11 — medium — 7 marks · exam-questions

### 4((a)) — 5 marks
Work through the table one activity at a time, drawing each as an arc from the event where everything it depends on has finished

$A$ and $B$ depend on nothing, so both leave the start event

$C$ depends on $A$ alone, so it leaves the event at the end of $A$

$D$ depends on $A$ and $B$, so it cannot leave that same event: a dummy carries the finish of $A$ across to the end of $B$, and $D$ leaves from there

$G$ depends on $C$ alone and $F$ depends on $D$ alone, so each leaves its own event, and $E$ depends on both $C$ and $D$, so two more dummies bring those two finishes together at a new event for $E$ to leave

$H$ and $I$ both depend on $G$ alone, so both leave the event at the end of $G$

$K$ depends on $F$ alone, while $J$ depends on $E$, $F$ and $I$, so a fourth dummy carries the finish of $F$ across to the event where $E$ and $I$ arrive

$H$, $J$ and $K$ have nothing depending on them, so all three end at the single finish event

![The activity network drawn from the precedence table, using activity on arc. A and B leave the start event. A dummy runs from the end of A to the end of B. C leaves the end of A and D leaves the end of B. Dummies run from the end of C and from the end of D to a new event, from which E leaves. G leaves the end of C and F leaves the end of D. H and I leave the end of G. A dummy runs from the end of F to the event where E and I arrive, and J leaves that event. H, J and K all finish at the single end event.](assets/019-the-activity-network-drawn-from-the-precedence-t.png)

**[M1 A1 A1 A1 A1]**

> **[mark-scheme]**
> **M1**: Eight activities labelled on the arcs, one start event, and at least two dummies placed. An activity-on-node diagram scores nothing.
> 
> **A1**: A, B, C, the first dummy with a correct arrow on it, and D all dealt with correctly. The first dummy is the one at the end of A.
> 
> **A1**: The second and third dummies with correct arrows on them, and E, F and G dealt with correctly. Those are the dummies at the ends of C and D.
> 
> **A1**: The fourth dummy with a correct arrow on it, and H, I, J and K dealt with correctly. The fourth dummy is the one at the end of F.
> 
> **A1**: A correct solution only, with every arrow present and correctly placed and exactly one finish event.
> 
> Dealt with correctly means the activity starts from the correct event, even where it does not also finish at the correct one.
> 
> An unlabelled solid line is taken to be an unlabelled activity rather than a dummy, even where a dummy is what belongs there. Incorrect or missing arrows on the activities themselves are ignored for the first four marks. If no dummy carries an arrow at all, that caps this part at the method mark. An extra dummy which is unnecessary but still keeps the precedence correct costs only the final accuracy mark.

> **[exam-tip]**
> A dummy is needed exactly where one activity depends on a group and another depends on only part of that group, and every dummy in this network comes from that same pattern.
> 
> - Draw the arcs in table order and add a dummy only when the next activity would otherwise pick up a dependency it does not have
> - Every dummy needs an arrow, because the direction is what carries the dependency: without it the network says nothing

### 4((b)) — 1 marks
A critical activity has no float, so if $K$ is critical then everything $K$ waits for is critical too

Follow the table back from $K$

$K$ depends on $F$ alone, and $F$ depends on $D$ alone, so both must be critical

$D$ depends on $A$ and $B$ together, so the critical route through $D$ may come through either one of them, and neither is forced

**Final answer:** **D and F must also be critical**

**[B1]**

> **[mark-scheme]**
> **B1**: A correct answer only, D and F, with no other activity stated as critical. Repeating K itself is ignored.

> **[exam-tip]**
> Trace back only through activities with a SINGLE predecessor. As soon as an activity depends on two things at once the chain branches, and neither branch is forced to be critical.
> 
> - $A$ and $B$ are the trap here: $D$ needs both of them, but only the longer of the two lies on the critical path

### 4((c)) — 1 marks
When every activity takes the same time, the longest path is simply the one through the most activities

Dummies take no time, so they do not add to the count

Follow each route from the start event to the finish and count the activities on it: the longest runs through five, and every other route through four or fewer

**Final answer:** **The critical path is A – C – G – I – J**

**[B1]**

> **[mark-scheme]**
> **B1**: A correct answer only, A to C to G to I to J.

> **[exam-tip]**
> Counting activities is only equivalent to adding durations because the durations here are equal, so do not carry the shortcut into a question that gives you times.
> 
> - Count the arcs on each route rather than the events, and skip the dummies: a route with four activities and two dummies is still four

## Q12 — medium — 12 marks · exam-questions

### 5((a)) — 4 marks
The early event time is the earliest that everything arriving at an event can be finished, so the forward pass takes the LARGEST total along any route into it

Work left to right from the start event, which is 0

Where more than one arc arrives, take the largest: at the event $H$ and $G$ arrive at, $G$ brings 8 and $H$ brings 14, so the early event time is 14

The late event time is the latest an event can happen without pushing the project out, so the backward pass takes the SMALLEST difference along any route leaving it

Work right to left from the finish event, which is 33, because the project may not overrun

Where more than one arc leaves, take the smallest: at the event $B$, $E$ and $F$ arrive at, $H$ gives $16 - 4 = 12$ and the dummy carries 19 across unchanged, so the late event time is 12

![The completed Diagram 1, with the early event time in the top half of each box and the late event time in the bottom half. The start event is 0 and 0. The event after A is 7 and 7. The event where B, E and F meet is 10 and 12. The event after C is 5 and 10. The event where D, I and the first dummy meet is 19 and 19. The event where G and H meet is 14 and 16. The event where J and L meet is 24 and 24. The event where K and the second dummy meet is 19 and 19. The event after M is 31 and 33. The finish event is 33 and 33.](assets/016-the-completed-diagram-1-with-the-early-event-tim.png)

**[M1 A1 M1 A1]**

> **[mark-scheme]**
> **M1**: All the top boxes complete, with the values generally increasing in the direction of the arrows, so read left to right. One rogue value is condoned.
> 
> **A1**: A correct answer only for all ten top boxes.
> 
> **M1**: All the bottom boxes complete, with the values generally decreasing against the direction of the arrows, so read right to left. One rogue value is condoned.
> 
> **A1**: A correct answer only for all ten bottom boxes.
> 
> The four marks are earned by the one completed diagram, which is why they are shown together beneath it: the two method marks are for the shape of each pass and the two accuracy marks for its values.

> **[exam-tip]**
> There are three dummies here and each simply carries a value across unchanged, in both directions, because a dummy takes no time.
> 
> - The event after $M$ is the one to watch: its early time is 31 but its late time is 33, because the dummy leaving it needs no time at all
> - Check the ends before going on, since the early and late times must agree at the start event and at the finish event

### 5((b)) — 2 marks
A lower bound shares all of the work out over the shortest time the project can take, and assumes nobody is ever idle

Add up the durations of all fifteen activities

$7 + 8 + 5 + 12 + 3 + 2 + 3 + 4 + 3 + 5 + 2 + 3 + 7 + 9 + 14 = 87$

Divide by the minimum completion time of 33 days

$\frac{87}{33} \approx 2 . 64$

**[M1]**

Workers come in whole numbers, and two of them could not get through 87 days of work in 33 days, so round the answer up

$\text{lower bound} = 3  \text{workers}$

**[A1]**

> **[mark-scheme]**
> **M1**: The total of the activity durations divided by the minimum completion time.
> 
> **A1**: A correct solution only, so the division has to be seen and the answer rounded up to 3. An answer of 3 with no working at all scores nothing.

> **[exam-tip]**
> Always round a lower bound UP, never to the nearest whole number: 2.64 workers means 3, and so would 2.1.
> 
> - The bound says two workers are impossible; part (c) is what shows that three really are enough, and the two questions are separate

### 5((c)) — 4 marks
A scheduling diagram gives each worker a row and fills it with activities that do not overlap, and no activity may start until everything it depends on is finished

Part (b) shows that at least three workers are needed, so try three

Three workers over 33 days gives 99 worker days for 87 days of work, so only 12 days can be left idle in total

Keep the critical activities on one row, since they run back to back and cannot be moved

Then fill the other two rows in an order that respects the network: $E$ cannot start until $A$ is done, $H$ needs $B$, $E$ and $F$, and $P$ needs everything that reaches the event it leaves

![A scheduling diagram on a grid numbered 0 to 36, with three worker rows. The first row is A from 0 to 7, D from 7 to 19, J from 19 to 24 and N from 24 to 33. The second is B from 0 to 8, E from 8 to 11, H from 11 to 15, I from 15 to 18 and P from 19 to 33. The third is C from 0 to 5, F from 5 to 7, G from 7 to 10, K from 16 to 18, L from 19 to 22 and M from 24 to 31.](assets/018-a-scheduling-diagram-on-a-grid-numbered-0-to-36-.png)

**[M1 A1 A1 A1]**

> **[mark-scheme]**
> **M1**: Not a cascade chart. At most four workers used, and at least ten activities placed.
> 
> **A1**: Three workers, all fifteen activities present exactly once. At most two errors are condoned, and one activity can give rise to at most three errors: one on its duration, one on its time interval and only one on its preceding activities.
> 
> **A1**: Three workers, all fifteen activities present exactly once, with at most one error condoned, judged the same way.
> 
> **A1**: A correct answer only.
> 
> Many different schedules earn full marks. The four marks are staged over the one diagram, which is why they are shown together beneath it.

> **[exam-tip]**
> The worker days are the quickest way to see how little slack there is: three workers for 33 days is 99 worker days against 87 days of work, so no more than 12 can be wasted.
> 
> - $P$ is 14 days long and cannot start before day 19, so it fills one worker completely from there to the end and has to be placed early in your planning
> - Check each row across for an overlap, then check each activity against the network, since those are the two ways a schedule goes wrong

### 5((d)) — 2 marks
Shortening an activity only shortens the project if the activity lies on EVERY critical path, and if it is critical in the first place

*G has a total float of 8 days, so it is not critical and shortening it would change nothing*

*D and P are both critical, so either one is worth considering*

**[M1]**

There are two critical paths here, A – D – J – N and A – D – P, and both take 33 days

$P$ lies on only the second of them, so shortening $P$ would leave the first still taking 33 days

**Final answer:** **Activity D should be shortened, because D lies on both critical paths while P lies on only one of them**

**[A1]**

> **[mark-scheme]**
> **M1**: Either D and P stated as being critical, or that G is not critical.
> 
> **A1**: The correct answer of D, with a fully correct reason. That means saying that G is not critical, that D and P are both critical, and that D appears on all of the critical paths, or equivalently that P appears on only one of them.

> **[exam-tip]**
> A critical activity is not automatically the right one to shorten. What matters is whether every critical path passes through it, and that is why this question is worth checking for a second critical path before answering.
> 
> - $G$'s total float is $16 - 5 - 3 = 8$ days, which is far longer than $G$ itself, so it is nowhere near critical
> - Shortening $D$ by one day takes the project to 32 days, while shortening $P$ by one day leaves it at 33

## Q13 — medium — 9 marks · exam-questions

### 3((a)) — 3 marks
The total float on an activity is the LATE event time where it finishes, minus the EARLY event time where it starts, minus its duration

$D$ and $E$ both leave the event whose early time is 4

$E$ arrives at the event whose late time is 17, so subtract 4 and then its duration of 7

$17 - 4 - 7 = 6$

$D$ arrives at the event whose late time is 24, so its total float is $24 - 4 - x$

The float on $D$ is twice the float on $E$, which gives an equation in $x$ alone

$24 - 4 - x = 2 \times 6$

$20 - x = 12$

$x = 8$

**[B1]**

$y$ is a LATE event time, so it comes from the backward pass, which takes the smallest difference along any route leaving that event

Only $F$ leaves it, running to the event whose late time is 17, so subtract the 5 that $F$ takes

$17 - 5 = 12$

$y = 12$

**[B1]**

$z$ is an EARLY event time, so it comes from the forward pass, which takes the largest total along any route into that event

Four arcs arrive there: $E$ brings $4 + 7 = 11$, $F$ brings $7 + 5 = 12$, $G$ brings $7 + 9 = 16$, and the dummy carries 17 straight across from the event below

$z = 17$

**[B1]**

> **[mark-scheme]**
> **B1**: A correct answer only for the value of x, 8.
> 
> **B1**: A correct answer only for the value of y, 12.
> 
> **B1**: A correct answer only for the value of z, 17.
> 
> The three marks are independent of one another, so two correct values out of three still earn two marks.

> **[exam-tip]**
> Take the float from the event where the activity FINISHES. For $D$ that is the 24 at its head, not the 10 in the box it leaves, and reading the 10 instead gives $10 - 4 - 8 = - 2$, which is a negative float and so cannot be right.
> 
> - Both floats in the condition come from boxes the figure already prints, so $x$ can be found before $y$ and $z$
> - The dummy arriving at the $z$ event carries a value across unchanged, and here it is the largest of the four, so it decides the answer

### 3((b)) — 4 marks
A cascade chart puts every activity at its EARLIEST start, with its total float shaded straight afterwards to show how far it could slip without delaying the project

The four critical activities have no float, so they go along the top row end to end and fill the whole 33 days

Give each of the other nine activities its own row, starting at its earliest start time

$A$ starts at 0 and lasts 4 days, and its float is $10 - 0 - 4 = 6$, so it is drawn from 0 to 4 with shading from 4 to 10

![A cascade chart on a grid numbered 0 to 34. The top row holds the critical activities end to end: C from 0 to 7, H from 7 to 17, I from 17 to 24 and J from 24 to 33. Below, each remaining activity has its own row with its float shaded: A from 0 to 4 with float to 10, B from 0 to 5 with float to 12, D from 4 to 12 with float to 24, E from 4 to 11 with float to 17, F from 7 to 12 with float to 17, G from 7 to 16 with float to 17, K from 17 to 27 with float to 33, L from 17 to 28 with float to 33, and M from 17 to 26 with float to 33.](assets/013-a-cascade-chart-on-a-grid-numbered-0-to-34-the-t.png)

**[M1 A1 A1 A1]**

> **[mark-scheme]**
> **M1**: At least ten activities labelled, including at least three floats. A scheduling diagram drawn instead scores nothing here.
> 
> **A1**: The critical activities C, H, I and J dealt with correctly and each appearing just once, together with three non-critical activities dealt with correctly.
> 
> **A1**: Any six non-critical activities correct. This mark does not depend on the previous accuracy mark.
> 
> **A1**: A completely correct chart, with exactly thirteen activities each appearing just once.
> 
> The four marks are staged over the one chart, which is why they are shown together beneath it.

> **[exam-tip]**
> The float drawn after an activity is its TOTAL float from the network, not the gap to whatever is drawn next along the row.
> 
> - Nine of the thirteen activities carry a float here, and the last mark is checking that every one of them is present exactly once
> - $D$ has the largest float at 12 days, which is longer than $D$ itself, so its shading is wider than its bar

### 3((c)) — 2 marks
A lower bound read off the cascade chart is the busiest moment that cannot be avoided, so look for a time when several activities must ALL be under way

An activity is unavoidable at a given time only between its latest start and its earliest finish, so one with plenty of float can always be slid out of the way

Reading down the chart at a time just after 24 days, four activities are running and none of them can be moved clear of that moment

**Final answer:** **At any time strictly between 24 and 26 days, activities J, K, L and M must all be in progress, so a lower bound is 4 workers**

**[M1 A1]**

> **[mark-scheme]**
> **M1**: Either a statement with the correct number of workers, 4, and the correct activities J, K, L and M together with any numerical time, or the correct number of workers with a time anywhere in the interval 24 to 26 inclusive. Mark the numerical value only and not the way the time is described. In either case the correct number of workers must be stated.
> 
> **A1**: A completely correct statement giving both the time and the activities. The time must lie strictly inside 24 to 26, so 24 itself is incorrect.
> 
> An answer given as an interval of time is accepted only if the whole interval is correct, so a time of 25 to 26 scores nothing here, while "on day 25" and "on day 26" are both correct. A completely correct statement spoiled by an extra incorrect statement scores nothing, so nothing is ignored.

> **[exam-tip]**
> Read the command word before deciding what to work out. "Use your cascade chart" and "specific reference to time and activities" ask for the busiest unavoidable moment, whereas "calculate a lower bound, showing your working" would ask for the total work divided by the project length.
> 
> - Quote a time strictly inside the interval, such as 25 days, because at 24 itself $J$ is only just starting and the answer cannot be told apart from one that has counted a finishing activity
> - The peak of the chart as you have drawn it is 5 activities, but that counts ones which could simply be moved later, so it is not the answer here

## Q14 — medium — 7 marks · exam-questions

### 5((a)) — 5 marks
The activities immediately preceding an activity are the ones that finish at the event it starts from, so work through the table one activity at a time

$A$, $B$ and $C$ depend on nothing, so all three leave the start event

$F$, $G$ and $I$ all depend on $A$, $B$ and $C$, so they leave an event that all three reach: $B$ finishes there, and a dummy carries each of $A$ and $C$ across to it

$D$ depends on $A$ alone and $E$ depends on $C$ alone, so $A$ and $C$ each need a separate event, which is exactly why those two dummies are needed

$H$ and $J$ depend on $D$, $F$ and $G$, so bring $D$ and $F$ together at one event and run a third dummy from there into the end of $G$

$L$ depends on $D$, $E$, $F$, $G$ and $I$, so run a fourth dummy from that same event into the event where $E$ and $I$ finish

$K$ depends on $H$ alone, so it leaves the event at the end of $H$

$J$, $K$ and $L$ have nothing depending on them, so all three end at the single finish event

![The activity network drawn from the precedence table, using activity on arc and four dummies. A, B and C leave the start event. Dummies run from the end of A and from the end of C to the end of B, and F, G and I leave that event. D leaves the end of A and E leaves the end of C. D and F both finish at one event, and a third dummy runs from there to the end of G, which is where H and J leave. A fourth dummy runs from that same event to the event where E and I finish, and L leaves there. K leaves the end of H. J, K and L all finish at the single end event.](assets/010-the-activity-network-drawn-from-the-precedence-t.png)

**[M1 A1 A1 A1 A1]**

> **[mark-scheme]**
> **M1**: Seven activities labelled on their arcs, one start event, and at least two dummies placed. An activity-on-node diagram scores nothing.
> 
> **A1**: A, B, C, the first two dummies with correct arrows on them, D and E all dealt with correctly. The first two dummies are the ones at the ends of A and C.
> 
> **A1**: A dummy linking D, F and G into one event and a dummy linking D, F, G, I and E into one event, together with F, G and I dealt with correctly. Both dummies must have arrows.
> 
> **A1**: H, J, K and L dealt with correctly.
> 
> **A1**: A correct solution only, with every arrow correctly placed, one finish event and at most four dummies.
> 
> Dealt with correctly means the activity starts from the correct event, even where it does not also finish at the correct one. Incorrect or missing numbers on the events are condoned throughout.
> 
> An unlabelled solid line is taken to be an unlabelled activity rather than a dummy, even where a dummy is what belongs there. One unlabelled arc loses the first accuracy mark and the last one, though the second may still be given the benefit of the doubt. Arrows missing from the activities themselves are ignored for the first four marks, but if no dummy carries an arrow at all then only the method mark is earned. An extra dummy which is unnecessary but still keeps the precedence correct costs only the final accuracy mark.
> 
> This is not the only correct network. The scheme says so of the third and fourth dummies in particular, so a diagram which brings the same activities together in a different order is equally right.

> **[exam-tip]**
> The activities with the longest predecessor lists are the ones that force the dummies, so look at $L$ and $H$ before you start drawing rather than after.
> 
> - Count as you go: three activities share the list $A$, $B$, $C$ but $D$ and $E$ each follow just one of them, and that mismatch is what the first two dummies are for
> - A dummy with no arrow on it costs four of the five marks here, so put the arrows in as you draw each one

### 5((b)) — 2 marks
A critical activity has no float, so it lies on a critical path

Every critical path goes through $H$, so any critical activity has to lie on a route that passes through $H$: it must be something $H$ waits for, or something that waits for $H$

Follow the table back from $H$: it waits for $D$, $F$ and $G$, and those wait for $A$, $B$ and $C$

Follow the table forward from $H$: only $K$ waits for it

Everything else lies on a route that avoids $H$ altogether, so none of it can be critical

**Final answer:** **E, I, J and L cannot be critical**

**[M1 A1]**

> **[mark-scheme]**
> **M1**: At least two of the four correct, with no more than five activities stated altogether.
> 
> **A1**: All four of E, I, J and L, and no others.

> **[exam-tip]**
> Work outwards from $H$ in both directions and list what you reach. Whatever is left over is the answer, and that is quicker than testing each activity in turn.
> 
> - $E$ and $I$ feed only $L$, so once $L$ is ruled out they go with it
> - $J$ and $L$ both end the project, and a path finishing on either of them never touches $H$

## Q15 — medium — 12 marks · exam-questions

### 4() — 2 marks
A dummy takes no time and does no work, so the only reason to draw one is to fix the logic of the network

**(i)**

$D$ and $E$ leave event 2, which only $A$ arrives at, so those two need $A$ alone to be finished

$F$ and $G$ leave event 3, which $B$ arrives at and which the dummy reaches from event 2, so those two need $B$ and $A$

Without the dummy there would be no way to let $F$ and $G$ wait for $A$ while $D$ and $E$ do not wait for $B$

**Final answer:** **The dummy from event 2 to event 3 is there because F and G depend on both A and B, while D and E depend on A alone**

**[B1]**

**(ii)**

$J$ and $K$ both leave event 4, and $J$ arrives at event 7

Without the dummy, $K$ would arrive at event 7 as well, so the two activities would begin and end at the same pair of events

**Final answer:** **The dummy from event 6 to event 7 is there so that J and K can each be described uniquely by the events at its two ends**

**[B1]**

> **[mark-scheme]**
> **B1**: The dependency reason. Every relevant activity must be named: A and B, one of D or E, and one of F or G, so four activities in all.
> 
> **B1**: The uniqueness reason. Saying only that the activities can be defined uniquely is not enough on its own; there must be some mention of describing an activity by the event at each of its ends. Give the benefit of the doubt to an answer which implies that two activities would otherwise begin and end at the same events, and J and K need not be named for this mark.
> 
> Throughout part (a) the words activity and event must be used correctly.

> **[exam-tip]**
> A dummy is drawn for one of exactly two reasons, and naming which one applies is most of the answer.
> 
> - A dependency dummy splits a group so that some later activities need all of the earlier ones and others need only some
> - A uniqueness dummy separates two activities that would otherwise run between the same pair of events, so that each can still be named by its two ends

### 4((b)) — 4 marks
The early event time is the earliest that everything arriving at an event can be finished, so the forward pass takes the LARGEST total along any route into it

Work left to right from event 1, which is 0

Where more than one arc arrives, take the largest: at event 7 the routes give $E$ finishing at 12, $F$ at 11, $H$ at 13 and $J$ at 11, and the dummy carries 12 across from event 6, so the early event time is 13

The late event time is the latest an event can happen without pushing the project out, so the backward pass takes the SMALLEST difference along any route leaving it

Work right to left from event 9, which is 26, because the project may not overrun

Where more than one arc leaves, take the smallest: at event 5, $H$ gives $15 - 4 = 11$ and $I$ gives $20 - 11 = 9$, so the late event time is 9

![The completed Diagram 1, with the early event time in the top half of each box and the late event time in the bottom half: event 1 is 0 and 0, event 2 is 5 and 5, event 3 is 5 and 9, event 4 is 10 and 13, event 5 is 9 and 9, event 6 is 12 and 15, event 7 is 13 and 15, event 8 is 20 and 20, and event 9 is 26 and 26.](assets/009-the-completed-diagram-1-with-the-early-event-tim.png)

**[M1 A1 M1 A1]**

> **[mark-scheme]**
> **M1**: All the top boxes complete, with the values generally increasing in the direction of the arrows, so read left to right. One rogue value is condoned.
> 
> **A1**: A correct answer only for all nine top boxes.
> 
> **M1**: All the bottom boxes complete, with the values generally decreasing against the direction of the arrows, so read right to left. One rogue value is condoned, and a missing 0 at event 1 or a missing 26 at event 9 is condoned for this mark only.
> 
> **A1**: A correct answer only for all nine bottom boxes.
> 
> The four marks are earned by the one completed diagram, which is why they are shown together beneath it: the two method marks are for the shape of each pass and the two accuracy marks for its values.

> **[exam-tip]**
> A dummy is treated as an activity of duration zero, so it carries a value straight across in both passes.
> 
> - Event 5 is worth extra care on the backward pass, because $I$ is much longer than $H$ and so gives the smaller difference
> - Check the ends before going on: the early and late times must agree at event 1 and at event 9

### 4((c)) — 2 marks
The project cannot finish until every activity is done, so the minimum completion time is the early event time at the final event

$\text{minimum project completion time} = 26  \text{hours}$

**[B1]**

An activity is critical when it has no total float, so any delay to it delays the whole project

Those are the activities running between events where the early and late times are equal, and which use up the whole gap between them

**Final answer:** **The critical activities are A, D, I and M**

**[B1]**

> **[mark-scheme]**
> **B1**: A correct answer only, 26. The unit is not required for the mark.
> 
> **B1**: A correct answer only, A, D, I and M only. Naming any further activity loses the mark.

> **[exam-tip]**
> Equal early and late times at an event are not enough on their own to make an activity critical: event 5 and event 8 both qualify, and so does event 2, but $H$ and $L$ are not critical because they do not fill the gap between their two events.
> 
> - Check each candidate with the float: the late time where it finishes, minus the early time where it starts, minus its duration
> - The four critical activities here form a single path from event 1 to event 9, which is the usual check that none has been missed

### 4() — 3 marks
**(i)**

The early event time at event 7 is the largest total along any route into it, and only the route through $H$ has changed

$E$ still brings 12, $F$ and $J$ still bring 11, and the dummy still carries 12 across from event 6, so the largest of the unchanged routes is 12

$H$ leaves event 5, whose early time is 9, so it now brings $9 + x$

The new early event time is whichever of those two is larger

**Final answer:** $12$** or **$9 + x$

**[M1 A1]**

**(ii)**

If the project still finishes in 26 hours, the backward pass is unchanged and the late event time at event 7 stays at 15

If $H$ is long enough to push the project out, then event 7 lies on the new critical path, so its late event time equals its early event time

**Final answer:** $15$** or **$9 + x$

**[A1]**

> **[mark-scheme]**
> **M1**: One of the two possible early event times for event 7, either $12$ or $9 + x$.
> 
> **A1**: Both correct answers, $12$ and $9 + x$.
> 
> **A1**: Both correct answers for the late event time, $15$ and $9 + x$.
> 
> Give the two possibilities on their own. An answer which LINKS them, for example by writing that 12 is greater than $9 + x$, loses the accuracy mark, although the method mark may still be given the benefit of the doubt.

> **[exam-tip]**
> State the two possibilities and stop there. Adding the condition under which each one holds is the natural instinct and it costs the accuracy mark on this scheme.
> 
> - Only the arc carrying $x$ can change either answer, so every other route into event 7 can be worked out once and left alone
> - The two answers to (ii) are 15 and $9 + x$, not 15 and $12 + x$: when event 7 becomes critical its late time equals its EARLY time, which is the answer to (i)

### 4((e)) — 1 marks
The new minimum completion time is four hours more than the 26 found in part (c)

$26 + 4 = 30$

The project can only have got longer through $H$, so event 7 now lies on the critical path and its early event time is $9 + x$

From event 7 the longest route to the finish is $L$ then $M$, taking $5 + 6 = 11$ hours, which beats $N$ on its own at 10

$9 + x + 11 = 30$

$x = 10$

**[B1]**

> **[mark-scheme]**
> **B1**: A correct answer only, 10.

> **[exam-tip]**
> The extra four hours all have to appear on the route through $H$, so the answer is not simply four more than $H$'s original duration of 4.
> 
> - Check it by putting $x = 10$ back in: event 7 becomes 19, event 8 becomes 24, and the project finishes at 30

## Q16 — medium — 8 marks · exam-questions

### 6((a)) — 5 marks
The activities immediately preceding an activity are the ones that finish at the event it starts from, so work through the table one activity at a time

$A$, $B$, $C$ and $D$ depend on nothing, so all four leave the start event

$F$ depends on $A$, $B$ and $C$, so it leaves an event that all three reach: $B$ finishes there, and a dummy carries each of $A$ and $C$ across to it

$E$ depends on $A$ alone, and $G$ and $H$ depend on $C$ alone, so $A$ and $C$ each need a separate event, which is exactly why those two dummies are needed

$I$ depends on $D$ and $H$, so let $H$ finish at the event $D$ already ends at, and $I$ leaves from there

$M$ depends on $G$ and $I$, so let both finish at one event, and $M$ leaves it

$L$ depends on $F$, $G$ and $I$, so a third dummy carries that event across to the end of $F$

$J$ and $K$ both depend on $E$ alone, so both leave the event at the end of $E$: a fourth dummy keeps them apart, because two activities may not join the same pair of events

$J$, $K$, $L$ and $M$ have nothing depending on them, so all four end at the single finish event

![The activity network drawn from the precedence table, using activity on arc and four dummies. A, B, C and D leave the start event. Dummies run from the end of A and from the end of C to the end of B, and F leaves that event. E leaves the end of A, and G and H leave the end of C. H finishes at the event D ends at, and I leaves there. G and I both finish at one event, from which M leaves, and a third dummy runs from there to the end of F, where L leaves. J and K leave the end of E, and a fourth dummy runs from the end of J to the finish. J, K, L and M all reach the single end event.](assets/006-the-activity-network-drawn-from-the-precedence-t.png)

**[M1 A1 A1 A1 A1]**

> **[mark-scheme]**
> **M1**: At least eight activities labelled on their arcs, one start event, and at least two dummies placed. An activity-on-node diagram scores nothing.
> 
> **A1**: A, B, C, the first two dummies with correct arrows on them, and D all dealt with correctly. The first two dummies are the ones meeting at the end of activity B.
> 
> **A1**: E, F, G, H and I dealt with correctly.
> 
> **A1**: J, K, L and M dealt with correctly, together with the third dummy and its arrow. The third dummy is the one beginning at the end of activity G.
> 
> **A1**: A correct solution only, with the final dummy and its arrow, every arrow correctly placed, one finish event and no additional dummies.
> 
> Dealt with correctly means the activity starts from the correct event, even where it does not also finish at the correct one. Incorrect or missing numbers on the events are condoned throughout.
> 
> An unlabelled solid line is taken to be an unlabelled activity rather than a dummy, even where a dummy is what belongs there. One unlabelled arc loses the second accuracy mark and the last one, though the third may still be given the benefit of the doubt. Arrows missing from the activities themselves are ignored for the first four marks, but if no dummy carries an arrow at all then only the method mark is earned. An extra dummy which is unnecessary but still keeps the precedence correct costs only the final accuracy mark.
> 
> This is not the only correct network: J and K may be interchanged, and the fourth dummy may instead be placed immediately after E.

> **[exam-tip]**
> Three of these dummies are there for precedence and one is there only to keep two activities apart, so do not expect every dummy to be doing the same job.
> 
> - $J$ and $K$ follow exactly the same thing and lead to nothing, so the only reason they cannot share both ends is that an activity has to be named by the pair of events it joins
> - $M$ follows $G$ and $I$ while $L$ follows those two and $F$ as well, which is the mismatch the third dummy exists for

### 6((b)) — 1 marks
A critical path runs from the start event to the finish event through critical activities only, and here there is just one

$K$ is critical, so the critical path must pass through $K$

$K$ follows $E$ alone, and $E$ follows $A$ alone, so the route back from $K$ is forced

$K$ has nothing depending on it, so the path ends there

**Final answer:** **The critical path is A – E – K**

**[B1]**

> **[mark-scheme]**
> **B1**: A correct answer only, A, E and K and nothing else.

> **[exam-tip]**
> Naming one critical activity is enough to fix the whole path whenever the route through it is forced, and here every step back from $K$ has a single predecessor.
> 
> - Check both directions: nothing follows $K$, so the path finishes on it rather than carrying on

### 6((c)) — 2 marks
When every activity takes the same time, the longest route is simply the one through the most activities

Dummies take no time, so they add nothing to the count

Follow each route from the start event to the finish and count the activities on it

The longest routes run through four activities, and every other route runs through three or fewer

Two different routes achieve four, because $L$ and $M$ both follow $G$ and $I$

**Final answer:** **First critical path: C – H – I – M**

**Final answer:** **Second critical path: C – H – I – L**

**[B1] [B1]**

> **[mark-scheme]**
> **B1**: One correct path, provided at most three paths are stated altogether.
> 
> **B1**: Both correct, with no others.

> **[exam-tip]**
> Where two activities share the same predecessors and both end the project, either can finish a critical path, so a question like this rarely has just one answer.
> 
> - The route through $K$ from part (b) carries only three activities, so equal durations move the critical path somewhere else entirely
> - Count the arcs on each route rather than the events, and skip the dummies: a route with four activities and one dummy is still four

## Q17 — medium — 6 marks · exam-questions

### 1() — 5 marks
![Activity-on-arc network for the precedence table. A single start node leads to activities A, B and C. Five dashed dummy arcs enforce the shared dependencies: from the end of A into the start of E, from the ends of C and E into the start of G, from the end of E into the start of H, and one from the end of J into the start of K so that I and J are uniquely defined by their start and end nodes. Activities I, J and F converge on the node from which K leaves, and K ends at a single finish node. Node numbers and activity durations are not shown.](assets/001-activity-on-arc-network-for-the-precedence-table.png)

**[M1 A1 A1 A1 A1]**

> **[mark-scheme]**
> **M1:** For including all 11 activities, with one start node, and for placing at least two dummies.
> 
> **A1: **For correctly dealing with activities A to E, and for the dummy from the end of A to the start of E.
> 
> **A1:** For correctly dealing with activities F and G, and for the dummy from the end of C as well as the dummy from the end of E into the start of G, including the arrowhead.
> 
> **A1:** For correctly dealing with activities H, I, J and K, as well as the dummy from the end of E into the start of H and the dummy from the end of J into the start of K, both including the arrowhead.
> 
> **A1:** For a completely correct solution, including all arrows correctly placed for each activity, with a single start node and a single end node, and exactly 5 dummies correctly placed.

> **[exam-tip]**
> Note that the way that you have drawn your diagram does not need to match the model answer exactly, but it should satisfy every row of the given precedence table. Remember that activities must be uniquely defined by their start and end nodes, so you cannot have two arrows between the same pair of nodes.
> 
> You do not need to include numbers on your nodes nor to include the weights of the activities on your diagram.

### 2() — 1 marks
Deduce the possible critical paths

Using the diagram you created in part (a), as the question states that D and F are critical activities, you can deduce that there are two critical paths:

- CFK
- and either one of the possibilities ADHJK or ADHIK

Consider the lengths of these critical paths

- The length of the critical path CFK = 1 + 6 + 1 = 8, and so the other critical path must have an equal length
- Deduce that the other critical path must therefore be ADHIK which is also of length 8, not ADHJK which is of length 7

List the critical activities

**Final answer:** **Activities A, C, H, I and K are critical**

**[B1]**

> **[mark-scheme]**
> **B1: **For the correct set of critical activities: A, C, H, I and K.
