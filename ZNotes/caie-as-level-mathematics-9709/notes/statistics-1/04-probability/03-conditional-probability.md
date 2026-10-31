## Conditional Probability

* Calculation of probability of one event given that another,
  connected event, had occurred.
* **Conditional Probability formula:**

$$
P\left( B \middle| A \right) = \frac{P\left( \text{A and B} \right)}{P\left( A \right)}
$$

Or, in another form:

$$
P\left( A\,\text{and}\, B \right)\, = \, P\left( A \right)\, P\left( B \middle| A \right)
$$

"Probability of event A and event B equals the probability of event A
times the probability of event B given event A has occurred"

*Example:*

$$
P\left( Get\ 2\ kings \right) = \frac{4}{52} \times \frac{3}{51}
$$

*Both events are “Get a king” but since one king has been picked up, the
next probability has changed. In other words,* $\frac{3}{51}$ *is*
$P(Get\ a\ king\ |\ Get\ a\ king)$*, the probability that you get a
king given that you’ve already gotten one.*

**<span class="underline">{S07-P06} Question 2:</span>**

Jamie is equally likely to attend or not to attend a training session
before a football match. If he attends, he is certain to be chosen for
the team which plays in the match. If he does not attend, there is a
probability of 0.6 that he is chosen for the team.


1. Find the probability that Jamie is chosen for team.
2. Find the probability that Jamie attended the training session, given that he was chosen for the team.

**<center>Solution:</center>**

**<span class="underline">Part (i)</span>**

*Probability attends training and chosen*

$$
0.5 \times 1 = 0.5
$$

*Probability does not attend and is chosen*

$$
0.5 \times 0.6 = 0.3
$$

*Total probability*

$$
P\left( \text{Chosen} \right) = 0.3 + 0.5 = 0.8
$$

*Since we are looking for* $P\left( \text{Chosen} \right)$*, we have
to find every possible way (every possible probability) that Jamie is
chosen, then sum them up.*

**<span class="underline">Part (ii)</span>**

*This is a conditional probability question, and we have to look for*
$P\left( \text{Attends } \middle| \text{ Chosen} \right)$*.*

$$
P\left( \text{Attends} \middle| \text{Chosen} \right) = \frac{P\left( \text{Attends and Chosen} \right)}{P\left( \text{Chosen} \right)}
$$

$$
P\left( \text{Attends} \middle| \text{Chosen} \right) = \frac{0.5}{0.8} = 0.625
$$

**<span class="underline">Old Question Question 7:</span>**

Events $A$ and $B$ are such that
$P\left( A \right) = 0.3,\ P\left( B \right) = 0.8$ and
$P\left( \text{A and B} \right) = 0.4$. State, giving a reason in
each case, whether $A$ and $B$ are


1. Independent
2. mutually exclusive

**<center>Solution:</center>**

**<span class="underline">Part (i)</span>**

$A$ and $B$ are not mutually exclusive because:

$P(A\ and\ B)$ does not equal 0

**<span class="underline">Part (ii)</span>**

$A$ and $B$ are not independent because:

$P\left( A \right) \times P\left( B \right)$ does not equal 0.4

Instead of using $P\left( \text{A and B} \right) = 0$ or
$P\left( \text{A and B} \right) = P\left( A \right) \times P\left( B \right)$
as a formula, we can also use it as a test to see if such events satisfy
the conditions to be a Mutually Exclusive Event or Independent Event.

**<span class="underline">{S11-P63} Question 4:</span>**

Tim throws a fair die twice and notes the number on each throw. Events
A, B, C are defined as follows.

*A: the number on the second throw is 5*

*B: the sum of the numbers is 6*

*C: the product of the numbers is even*

By calculation find which pairs, if any, of the events A, B and C are
independent.

**<span class="underline">Solution:</span>**

*Probability of Event A* $=$ *P(Any Number)* $\times$ *P(5)*

$$
\therefore P\left( A \right) = 1 \times \frac{1}{6} = \frac{1}{6}
$$

*Finding the probability of Event B*

*Number of ways of getting a sum of 6:*

5 and 1 1 and 5 4 and 2 2 and 4 3 and 3

$$
\therefore P\left( B \right) = \left( \frac{1}{6} \times \frac{1}{6} \right) \times 5 = \frac{5}{36}
$$

*Finding the probability of Event C*

*One minus method; you get an odd only when odd multiplies by another
odd number:*

$$
1 - P\left( C \right) = \frac{3}{6} \times \frac{3}{6}
$$

$1 - P\left( C \right)$ *represents the probability of getting an odd
when doing the product of the two numbers, which can only occur when an
odd number is multiplied by another odd number which is*
$\frac{3}{6} \times \frac{3}{6}$*. This method is much easier because
if one does a direct method, they will have to count Even* $\times$
*Even and Even* $\times$ *Odd.*

*Making* $P\left( C \right)$ *the subject gives us:*

$$
\therefore P\left( C \right) = \frac{3}{4}
$$

*For an independent event,*
$P\left( \text{A and B} \right) = P(A) \times P(B)$

$$
P\left( \text{A and B} \right) = \ P\left( 1\ and\ 5 \right) = \frac{1}{36}
$$

$$
\neq \ P(A)\  \times \ P(B)
$$

$$
P\left( \text{A and C} \right) = \ P\left\lbrack \left( 2,5 \right) + \ \left( 4,5 \right) + \ \left( 6,5 \right) \right\rbrack = \frac{3}{36}
$$

$$
\neq \ P(A)\  \times \ P(C)
$$

$$
P\left( \text{B\ and\ C} \right) = \ P\left\lbrack \left( 2,4 \right) + \ \left( 4,2 \right) \right\rbrack = \frac{2}{36}
$$

$$
\neq \ P(B)\  \times \ P(C)
$$

$\therefore$ none are independent.

*As said from the previous worked question, we use the
equation*$\text{ P}\left( \text{A and B} \right) = P(A) \times P(B)$
*not as a formula but as a test to see whether two events are
independent or not.*