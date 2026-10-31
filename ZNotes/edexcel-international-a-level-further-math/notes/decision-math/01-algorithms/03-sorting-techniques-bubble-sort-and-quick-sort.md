## Sorting techniques: Bubble Sort and Quick Sort

## Bubble Sort

Bubble sort are algorithms that help to sort an unsorted set of data into ascending or descending order.

STEPS FOR BUBBLE SORT - Ascending Order:

1. For ascending order, start comparing items from the left side moving to the end of the list

2. Each item of the list must be compared to the next item

3. If item compared is larger than the next item then both values must be SWAPPED.

4. If value compared is smaller than the next value then no swaps take place and it remains the same

5. Count number of swaps taken place.

Example 1-

Item list- 22, 10, 42, 67, 89

Using bubble sort technique 22 is larger than 10, therefore 10 and 22 will be swapped

After swapping the numbers, 22 is compared to 42, since 42 is larger no swaps will take place.

If no swaps occur after a pass the list is sorted Count the number of swaps taken place.

## Quick Sort-

1. Choose an element from the list as your pivot

2. Compare each element of the list with the pivot

3. All elements smaller than the pivot must be moved to the left, larger elements must be shifted to the right, for ascending order. Opposite must be carried out if question mentions descending order

4. The pivot element is now in it’s correct position

5. Repeat same steps for left and right sub lists, until sublist only contains one element

6. List is now sorted

Quick Sort example: Ascending

Item list-

22, 10, 42, 67, 89

Step 1 : Choosing pivot

Starting at the middle, 42 cannot be assigned as a pivot, since everything after 42 is placed correctly. Therefore we can either 22 or 10, Choosing 22 as our pivot.

Step 2: Shifting

10 moves to the left since it’s smaller than the pivot

Updated list :

10 22 42 67 89

List sorted.

## Bin packing Algorithms

First Fit Decreasing Algorithm

1. Sort all items in decreasing order

2. Take the first item place into the first bin

3. Take the next item and place into the first bin that must have enough space remaining

4. If the item does not fit in the existing bin, open a new bin

5. Repeat until all items are placed

Example:

Bin capacity - 10

Item list- 8,6,2,3,5

Step 1 : Arrange in descending order

8,6,5,3,2

Step 2: Assign each item to a corresponding Bin.

Bin 1 : 8,2

Bin 2 : 6,3

Bin 3 : 5

Full Bin packing

1. Take items into the original order

2. Place each item into the first bin that has enough space

3. If the item doesn’t fit in the previous bin, move to the next one

4. Continue until all items are packed

Example -

Bin capacity- 10

Item list - 8,6,2,3,5

Bin 1: 8,2

Bin 2: 6,3

Bin 3: 5