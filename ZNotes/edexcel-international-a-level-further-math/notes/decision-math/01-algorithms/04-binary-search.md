# Binary Search Algorithm

Binary search algorithm helps finding whether the item wanted is in the list of not

KEY POINT - Binary search algorithm can only take place when the list is ordered

Steps for binary search algorithm

* Find midpoint using the formula (n+1)/2 (Round up if necessary)

  * If pivot is the item wanted then search is complete

  * If pivot > target search the item in the first half of the list and cancel other items to make search easier

  * If pivot < target search the item in the second half of the list

* Steps One and three must be repeated in order to find item, if item isn’t found than it’s not in the list

## Example question :

Find 21 in the list

3 4 7 9 10 13 15 17 18 20 21 24

12 numbers so middle most number is 6th number which is 13

21 being larger than 13 reduces list to 15 17 18 20 21 24

Middle most number of list is 3rd number

Updated list :

20 21 24

Middle number = 21

Item found binary search complete.