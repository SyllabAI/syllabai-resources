# Critical Path Analysis

Course: ial-maths-20-decision-1 · Section: Critical Path Analysis

Source: https://www.savemyexams.com/international-a-level/maths/edexcel/20/decision-1/flashcards/critical-path-analysis/critical-path-analysis/


## Card 1 — keyword_definition (`fl_Zwq2h9nmhM8WXygR`)

**FRONT**

Define an **activity network**.


**BACK**

An activity network is a graph showing the **activities** needed to complete a project and the **order** in which they must be carried out.

Some activities cannot begin until others are finished, while others can happen at the same time.


Spec links: `spcpt_7bBdB5ZtfBRKrDtX`


## Card 2 — question_and_answer (`fl_kBHjjBvNd3kqFKYF`)

**FRONT**

In an activity network, what do the arcs represent, and what do the nodes represent?


**BACK**

The **arcs** represent the activities, which is why this is called an **activity-on-arc** network.

The **nodes** represent events, and nothing beyond an event can begin until every activity leading into it has been completed.


Spec links: `spcpt_7bBdB5ZtfBRKrDtX`


## Card 3 — fill_in_the_blanks (`fl_W6S9S8z9Z6D9Nxhg`)

**FRONT**

Complete the names of the two special events of an activity network:

The event at the start of the project is the `\_\_\_\_\_\_` node, and the event at the end of the project is the `\_\_\_\_\_\_` node.


**BACK**

The completed sentence is:

The event at the start of the project is the **source** node, and the event at the end of the project is the **sink** node.

The source node is labelled $0$ or $S$, and the sink node is either the highest-numbered node or is labelled $T$.


*Blanks: 0 — answers: ['source', 'sink']*

Spec links: `spcpt_7bBdB5ZtfBRKrDtX`

Flags: blank_answer_mismatch


## Card 4 — question_and_answer (`fl_f8n9ZMJg3XStqbPv`)

**FRONT**

What must be true of the start and end nodes of every activity in an activity network?


**BACK**

Every activity must have a **unique pair** of start and end nodes, so no two activities may run between the same two events.

Writing an activity as an ordered pair makes the check easy: if one activity is `\left(1 , 2\right)` then no other activity may be `\left(1 , 2\right)` as well.


Spec links: `spcpt_BRTBn4PHdYjxcYdy`


## Card 5 — keyword_definition (`fl_yyvsVB8zwmtJHxVQ`)

**FRONT**

Define a **precedence table**.


**BACK**

A precedence table lists every activity in a project alongside the activities it depends on, and it usually gives each activity's **duration** as well.

A dash in the dependency column shows that an activity has no predecessors at all, so it can start at the very beginning of the project.


Spec links: `spcpt_7bBdB5ZtfBRKrDtX`


## Card 6 — true_or_false (`fl_5H9Zwb7rZ4P2Qqcz`)

**FRONT**

**True or False?**

In a precedence table, an activity that depends on A, where A itself depends on B, should have both A and B listed against it.


**BACK**

**False.**

Only the **immediately** preceding activities are listed, so the entry is just A.

The dependence on B is already carried by A's own row, and repeating it would clutter the table without adding anything.


Spec links: `spcpt_7bBdB5ZtfBRKrDtX`


## Card 7 — question_and_answer (`fl_YZxmb6RSDbfgj6nX`)

**FRONT**

When drawing an activity network, which activities are attached to the source node, and which run to the sink node?


**BACK**

Activities with **no preceding activities** start at the source node, since nothing has to happen before them.

Activities that are not a predecessor of anything else run to the sink node, because the project is finished once they are done.


Spec links: `spcpt_BRTBn4PHdYjxcYdy`


## Card 8 — question_and_answer (`fl_CVMSMKkVsgJhWqjW`)

**FRONT**

You are reading a precedence table off an activity network. How do you find the immediate predecessors of an activity?


**BACK**

Look at the node the activity **starts** at, and list every activity that **ends** at that same node.

An activity starting at the source node has no predecessors at all, which is shown in the table by a dash.


Spec links: `spcpt_zVhvgrfbmXNfnpXT`


## Card 9 — question_and_answer (`fl_vdxb8j6drd6TXq84`)

**FRONT**

In an activity network, activity F starts at node 4, and activities D and E are the only activities ending at node 4. What is F's entry in the precedence table?


**BACK**

Its immediately preceding activities are **D and E**, so the entry in the table reads 'D, E'.


Spec links: `spcpt_zVhvgrfbmXNfnpXT`


## Card 10 — keyword_definition (`fl_6DVQcfXtSGYcvbjf`)

**FRONT**

Define a **dummy activity**.


**BACK**

A dummy activity is an activity with a duration of **zero**.

It is drawn as a **dotted** arc and is not given an activity letter, because it represents no actual work: it exists only to show how activities depend on one another.


Spec links: `spcpt_JcFRspDf7gjktJNn`


## Card 11 — question_and_answer (`fl_XjgRgs6zRPnZFBVw`)

**FRONT**

Activities B and C would both run from event 1 to event 2. Why is a dummy needed here, and what does it do?


**BACK**

A dummy is needed because every activity must have a unique pair of start and end nodes, and B and C would both be the pair `\left(1 , 2\right)`.

Inserting a dummy moves one of them to a new event, so that B becomes `\left(1 , 3\right)` while C stays as `\left(1 , 2\right)`.


Spec links: `spcpt_JcFRspDf7gjktJNn`


## Card 12 — question_and_answer (`fl_NskytFchVz7p4Qty`)

**FRONT**

Activity D depends on both B and C, but activity E depends on B alone. Why does this need a dummy?


**BACK**

Because B has to lead into both D and E, while C has to lead into D only, and no single event can do both jobs.

A dummy runs from the end of B to the event where C ends, so that D picks up B and C together while E still depends on B alone.


Spec links: `spcpt_JcFRspDf7gjktJNn`


## Card 13 — true_or_false (`fl_YJzdNpMXwG7Y72jh`)

**FRONT**

**True or False?**

When a dummy is needed to give two activities unique start and end nodes, there can be more than one correct place to put it.


**BACK**

**True.**

Where B and C would share the pair `\left(1 , 2\right)`, the dummy can be inserted so that either B or C is the one moved on to a new event.

Both versions show exactly the same precedences, so either is a correct answer.


Spec links: `spcpt_JcFRspDf7gjktJNn`


## Card 14 — question_and_answer (`fl_xzbPq5JkKVPpSrZB`)

**FRONT**

Looking at a precedence table, what pattern tells you that a dummy activity will be needed?


**BACK**

Look for two activities whose lists of predecessors **overlap without matching**, such as one depending on B and C while another depends on B alone.

Also look for two activities with **identical** predecessor lists, since those would otherwise end up sharing the same pair of start and end nodes.


Spec links: `spcpt_JcFRspDf7gjktJNn`


## Card 15 — question_and_answer (`fl_7Wq3DsvXjXrY5q5X`)

**FRONT**

What does critical path analysis of a project find?


**BACK**

It finds the **minimum duration** of the whole project, which activities are critical and the critical path they form, and how much any non-critical activity can be delayed.

In short, it says how quickly the project can be done and where there is slack.


Spec links: `spcpt_HKKqTh4c83HbRhck`


## Card 16 — keyword_definition (`fl_24y39QJnRN8TPTS6`)

**FRONT**

Define a **critical activity**.


**BACK**

A critical activity is one that must start and finish at the **earliest possible time** if the project is to be completed in its minimum duration.

Any delay to a critical activity delays the whole project.


Spec links: `spcpt_HKKqTh4c83HbRhck`


## Card 17 — question_and_answer (`fl_wrttDQbfdbPNdYMs`)

**FRONT**

What is the earliest event time at a node, and where is it written?


**BACK**

The earliest event time is the earliest moment at which any activity leaving that event can start.

It is written in the **top** of the two boxes at the node, and the bottom box is kept for the latest event time.


Spec links: `spcpt_dhRm2dQ87WyZp6J8`


## Card 18 — question_and_answer (`fl_qtxN4RqWH7TXDKS6`)

**FRONT**

Working forwards through an activity network, how do you find the earliest event time at a node?


**BACK**

For each activity leading into the node, add its duration to the earliest event time at its own start node, then take the **maximum** of those totals.

The maximum is right because the event is not reached until **every** activity leading into it has finished; the source node starts at $0$.


Spec links: `spcpt_dhRm2dQ87WyZp6J8`


## Card 19 — true_or_false (`fl_HsB8z4ynyDfVQxJZ`)

**FRONT**

**True or False?**

A dummy activity can be ignored when working out earliest event times, because it takes no time.


**BACK**

**False.**

A dummy is still an arc leading into a node, so it must go into the comparison like any other activity.

What it contributes is the earliest event time at its start node plus $0$, and that value can turn out to be the largest of them all.


Spec links: `spcpt_dhRm2dQ87WyZp6J8`


## Card 20 — question_and_answer (`fl_r58Q3q9W2Z2xMcPT`)

**FRONT**

Where does the backward pass start, and with what value?


**BACK**

It starts at the **sink node**, whose latest event time is set equal to its earliest event time.

That value is the **minimum project duration**, so the backward pass is asking how late each event can be while still meeting it.


Spec links: `spcpt_Xhz9tPKq3b3J9HWM`


## Card 21 — question_and_answer (`fl_rRyk6RWxqrmdbcQP`)

**FRONT**

Working backwards through an activity network, how do you find the latest event time at a node?


**BACK**

For each activity leaving the node, subtract its duration from the latest event time at its **end** node, then take the **minimum** of those results.

The minimum is right because the event has to be left early enough for **every** following activity to still finish on time.


Spec links: `spcpt_Xhz9tPKq3b3J9HWM`


## Card 22 — fill_in_the_blanks (`fl_mK25QS2DG8qtvYzp`)

**FRONT**

Complete the formula for the total float of the activity running from event $i$ to event $j$:

`F \left(i , j\right) = \_\_\_\_\_\_ - \_\_\_\_\_\_ - \text{duration} \left(i , j\right)`


**BACK**

The completed formula is:

`F \left(i , j\right) = l_{j} - e_{i} - \text{duration} \left(i , j\right)`

Here $e_{i}$ is the **earliest** event time at event $i$, and $l_{j}$ is the **latest** event time at event $j$.


*Blanks: 0 — answers: ['earliest', 'latest']*

Spec links: `spcpt_fN2rrfqvt7NDGwsB`

Flags: blank_answer_mismatch


## Card 23 — question_and_answer (`fl_RRdtjddNmbPNcnHz`)

**FRONT**

What does the total float of an activity tell you?


**BACK**

It is the amount of time the start of the activity can be **delayed** without pushing back the minimum project duration.

A critical activity therefore has a total float of **zero**, and despite its name the total float is a single value for a single activity rather than a total of anything.


Spec links: `spcpt_fN2rrfqvt7NDGwsB`


## Card 24 — keyword_definition (`fl_T9H9F5RwW9JT7rsG`)

**FRONT**

Define a **critical path** through an activity network.


**BACK**

A critical path is a path from the **source node** to the **sink node** made up entirely of critical activities.

It is written as a sequence with dashes, such as $A - C - G - I$, and a network can have more than one.


Spec links: `spcpt_kdsfyGCHBSPwhMQK`


## Card 25 — question_and_answer (`fl_nWwYyvvjpkhyRfsH`)

**FRONT**

What makes an event critical, and why is that useful?


**BACK**

An event is critical when its **earliest and latest event times are equal**, so the two boxes at that node hold the same number.

A critical activity can only run between critical events, so scanning for nodes with equal boxes narrows the search down quickly.


Spec links: `spcpt_kdsfyGCHBSPwhMQK`


## Card 26 — true_or_false (`fl_5WFWv8SFncFbn57f`)

**FRONT**

**True or False?**

If an activity runs between two critical events, then that activity must itself be critical.


**BACK**

**False.**

A critical activity must have critical events at both ends, but the reverse does not follow.

An activity can join two critical events and still have a **positive total float**, if its duration is shorter than the gap between those two event times, so the float has to be checked rather than assumed.


Spec links: `spcpt_kdsfyGCHBSPwhMQK`


## Card 27 — question_and_answer (`fl_6bKPJvkrxCfkbmmg`)

**FRONT**

An activity network has two critical paths, $A - C - D - G$ and $A - C - E - F - G$. What are the critical activities?


**BACK**

The critical activities are **A, C, D, E, F and G**, since every activity lying on any critical path is itself critical.

They are written as a list rather than as a sequence, because taken together they do not form a single path.


Spec links: `spcpt_kdsfyGCHBSPwhMQK`


## Card 28 — keyword_definition (`fl_DynncmffJ3XW5wGF`)

**FRONT**

Define a **Gantt (cascade) chart**.


**BACK**

A Gantt chart is a display of a project's activities as horizontal bars against a time axis.

It shows the critical activities, the total float of every non-critical activity, and the minimum project duration, all in one picture.


Spec links: `spcpt_d6KFycyQksKQ2HGD`


## Card 29 — question_and_answer (`fl_6CCYBspZvXFvfBTb`)

**FRONT**

On a Gantt chart, at what time is each activity's bar drawn to start?


**BACK**

Every activity is drawn starting at its **earliest event time**, which is the early event time at its start node.

So an activity of duration $5$ whose start node has an early event time of $4$ is drawn from $4$ to $9$.


Spec links: `spcpt_d6KFycyQksKQ2HGD`


## Card 30 — question_and_answer (`fl_s4kcQkSdSKnbjpZj`)

**FRONT**

How are the critical activities drawn on a Gantt chart, and why can they share a single line?


**BACK**

They are drawn **back-to-back on one horizontal line**, each starting the moment the previous one ends.

That works because every critical activity has a total float of zero, so none of them can move, and together they fill the whole minimum project duration.


Spec links: `spcpt_d6KFycyQksKQ2HGD`


## Card 31 — question_and_answer (`fl_CnPgrb4WbF9DgBN5`)

**FRONT**

How is a non-critical activity drawn on a Gantt chart?


**BACK**

Each non-critical activity gets a **line of its own**, with a solid bar for its duration followed by a **dotted** bar for its total float.

Bars are labelled with the activity's name and its duration, while the dotted float bars are left unlabelled.


Spec links: `spcpt_d6KFycyQksKQ2HGD`


## Card 32 — fill_in_the_blanks (`fl_ppkkBNff7cXzRt79`)

**FRONT**

Complete the rule for where the dotted bar of a non-critical activity ends on a Gantt chart:

`\text{end of dotted bar} = \text{earliest start} + \text{duration} + \_\_\_\_\_\_`


**BACK**

The completed rule is:

$\text{end of dotted bar} = \text{earliest start} + \text{duration} + \text{total float}$

So an activity with earliest start $7$, duration $4$ and total float $3$ has a solid bar from $7$ to $11$ and a dotted bar running on to $14$.


*Blanks: 0 — answers: []*

Spec links: `spcpt_d6KFycyQksKQ2HGD`


## Card 33 — true_or_false (`fl_BrhtvkDJjXVvDwcN`)

**FRONT**

**True or False?**

Every activity on a Gantt chart is drawn as a single unbroken bar.


**BACK**

**True.**

An activity is assumed to run in one continuous block, so once it has started it runs through to completion without a break.

The float of a non-critical activity lets its bar **slide** to a later start, but it never lets the bar be cut in two.


Spec links: `spcpt_d6KFycyQksKQ2HGD`


## Card 34 — question_and_answer (`fl_z9nYKS6qSptfsDHT`)

**FRONT**

What assumption about workers does a Gantt chart make?


**BACK**

It assumes **one worker per activity**, or one team acting as a single resource.

That is what allows each bar to be read as one person's stretch of work, and it is the assumption the whole chart rests on.


Spec links: `spcpt_d6KFycyQksKQ2HGD`


## Card 35 — keyword_definition (`fl_8ZP6vY5pZ5rD97jP`)

**FRONT**

What is meant by **scheduling** the activities of a project?


**BACK**

Scheduling is the process of **assigning workers** to the activities of a project.

It answers one of two questions: how few workers can finish the project in its minimum duration, or how long the project takes when only a fixed number of workers is available.


Spec links: `spcpt_vg4jSpg46ks8kcrD`


## Card 36 — question_and_answer (`fl_Mznjk3xPS2KX7dyC`)

**FRONT**

What is the critical time of a project?


**BACK**

The critical time is another name for the **minimum project duration**, the shortest time in which every activity can be completed.

Scheduling problems use the term when asking whether that time can still be met with a limited workforce.


Spec links: `spcpt_vg4jSpg46ks8kcrD`


## Card 37 — question_and_answer (`fl_ShYrzqHvtRg6WXhY`)

**FRONT**

When scheduling for the fewest workers, which activities are assigned first, and why?


**BACK**

The **critical activities** are assigned first, all of them to a single worker.

They have no float, so their timings are fixed and there is no choice to be made about them; everything else then has to be fitted around that one settled row.


Spec links: `spcpt_vg4jSpg46ks8kcrD`


## Card 38 — question_and_answer (`fl_fxntFs92Mck6n3dV`)

**FRONT**

A worker becomes free and two activities are both available to start. Which one should be given to them?


**BACK**

Give them the activity with the **lower late end time**, meaning the smaller latest event time at the activity's end node.

That activity has the least room to be delayed, so starting it first is what keeps the rest of the schedule workable.


Spec links: `spcpt_vg4jSpg46ks8kcrD`


## Card 39 — question_and_answer (`fl_fV2VMnBcNZV8Y3TS`)

**FRONT**

On a reduced Gantt chart, what does the number of rows tell you?


**BACK**

Each row is one worker's continuous run of activities, so the number of rows is the number of workers needed.

Reducing the chart means sliding the non-critical activities within their float so that activities sit back-to-back and as few rows as possible are used.


Spec links: `spcpt_vg4jSpg46ks8kcrD`


## Card 40 — fill_in_the_blanks (`fl_tbT5MDpRwpw9Dp4H`)

**FRONT**

Complete the formula for the theoretical lower bound on the number of workers needed to finish a project in its minimum duration:

`\text{lower bound} \ge \frac{\_\_\_\_\_\_}{\text{minimum project duration}}`


**BACK**

The completed formula is:

$\text{lower bound} \geq \frac{\text{total time of all activities}}{\text{minimum project duration}}$

The lower bound is the **smallest integer** that satisfies it, so a value of $2 . 217 \dots$ gives a lower bound of $3$.


*Blanks: 0 — answers: ['smallest integer']*

Spec links: `spcpt_vg4jSpg46ks8kcrD`

Flags: blank_answer_mismatch


## Card 41 — question_and_answer (`fl_ZrBQ7qbfqTzxZGDq`)

**FRONT**

The lower bound for the number of workers is $3$. Does that guarantee three workers can finish the project on time?


**BACK**

Three workers may still not be enough.

A lower bound only rules out finishing with **fewer** than three; whether three will actually do depends on whether the activities can be arranged without breaking a precedence, which has to be tried out.


Spec links: `spcpt_vg4jSpg46ks8kcrD`


## Card 42 — question_and_answer (`fl_pRq9nk5WhD2DWYJ9`)

**FRONT**

How can a lower bound for the number of workers be found by looking at a Gantt chart rather than by calculation?


**BACK**

Pick a moment in time and count the activities that **cannot** be moved off it, even using the whole of their float.

That many workers must be busy at once, so the largest such count found anywhere along the chart is a lower bound.


Spec links: `spcpt_vg4jSpg46ks8kcrD`


## Card 43 — true_or_false (`fl_M6RfN2jQBSkGDbkB`)

**FRONT**

**True or False?**

When the number of workers available is capped, the project can always still be finished in its minimum duration.


**BACK**

**False.**

If the cap is below the number of workers the minimum duration requires, activities have to be delayed and the project takes longer.

In that situation even **critical** activities may have to be pushed back, which is exactly what the other kind of scheduling problem does not allow.


Spec links: `spcpt_vg4jSpg46ks8kcrD`

