## Combinations

- A combination is a way of **selecting**, or **choosing**, $r$ objects, in **no particular order**, from $n$ objects.


The number of ways of selecting, or choosing, $r$ objects from $n$ objects is:
$$
{}^nC_r = \frac{n!}{(n - r)! \times r!}
$$
This can also be thought of as
$$
{}^nC_r = \frac{\text{Total number we select from}!}{\text{Number selected}! ~ \times ~\text{Number not selected}!}
$$



---
**<center>Example 1</center>**
In how many ways can 5 books and 3 magazines be selected from 8 books and 6 magazines?
**<center>Answer</center>**
- The word "and" indicates the use of the multiplication principle.

We can choose 5 books from 8 books in ${}^8C_5$ or 56 ways.

We can choose 3 magazines from 6 magazines in ${}^6C_3$ or 20 ways.

As we are trying to find the total number of selections, we multiply both results. This is the multiplication principle

Total number of ways of selection = $56 \times 20 = 1120$.

$$
\phantom{invis}
$$

**<center>Example 2</center>**
A team of five is to be chosen from six women and five men. Find the number of possible teams in which there will be more women than men.
**<center>Answer</center>**
We can have 3 cases in which there are more women than men on the team.
$$
\text{Case 1}~ - ~ \underline{w} ~ \underline{w} ~\underline{w} ~ \underline{m} ~ \underline{m} = {}^6C_3 \times {}^5C_2 = 200
$$
$$
\text{Case 2}~ - ~ \underline{w} ~ \underline{w} ~\underline{w} ~ \underline{w} ~ \underline{m} = {}^6C_4 \times {}^5C_1 = 75
$$
$$
\text{Case 3}~ - ~ \underline{w} ~ \underline{w} ~\underline{w} ~ \underline{w} ~ \underline{w} = {}^6C_5 \times {}^5C_0 = 6
$$
As we cannot have all of these cases happening at the same time, due to a constraint on the number of people, we will have a choice between case 1 **OR** case 2 **OR** case 3. This is an application of the addition principle, thus we add all our cases to find the total number of selections.

$$
200 + 75 + 6 = 281 ~\text{ways}
$$