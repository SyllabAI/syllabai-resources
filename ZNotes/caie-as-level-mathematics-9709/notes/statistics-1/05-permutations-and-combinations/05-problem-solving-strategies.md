## Problem Solving Strategies
### **Gap Method**
Let’s say there are 4 girls and 4 boys. How many ways can they be seated, such that no girl is sitting next to another girl?
**<center>Answer</center>**

Let the girls be $G_1, G_2, G_3, G_4$ and let the boys be $B_1, B_2, B_3, B_4$. People are distinct, so we do not need to take in consideration any repetitions. 

We can first arrange the boys in such a way that there is a gap between them, to seat the girls.
$$
\_ ~~ \underline{B_1} ~~ \_ ~~ \underline{B_2} ~~ \_ ~~ \underline{B_3} ~~ \_ ~~ \underline{B_4} ~~ \_
$$

Observe that we have made 5 dashes, while there are only 4 girls. This is because the arrangement can be such that a girl is placed in the first dash. If a girl is not in the first dash, then the dash is empty and the boy would be considered the first in line. The same logic is used for the last dash.

We can now select the girls, that are going to be seated, using combinations. There are 5 dashes, but we only need to seat 4 girls. So out of 5 seats, we choose 4 seats to gain the total number of selections possible.
$$
{}^5C_4
$$
Now that we have selected 4 out of 5 seats, we can find the total number of arrangements. We will end up with $4!$ ways of arranging the 4 boys **AND** $4!$ ways of arranging the girls who will be seated. We end up with
$$
{}^5C_4 \times 4! \times 4! = 2880 ~\text{ways}
$$



---

### **String Method**

There are 3 boys and 4 girls. In how many ways can they be seated, such that all the boys are sitting in a row.
**<center>Answer</center>**
First lets "string" together all the boy students. This string of students will be considered as **one dash**.
$$
\boxed{B_1 ~ B_2 ~ B_3} ~ G_1 ~ G_2 ~ G_3 ~ G_4
$$


We can now say there will be 3! ways of arranging the boys **inside** the string amongst each other, and 5! ways of arranging the 5 total dashes. We have considered the string to be 1 dash, so there are 5! ways of arranging the 4 girl students and the string.

In total there are:
$$
5! \times 3! = 720 ~ \text{ways of arrangement} 
$$
