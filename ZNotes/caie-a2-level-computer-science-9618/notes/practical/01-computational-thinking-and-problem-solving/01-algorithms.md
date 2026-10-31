# Computational thinking and Problem-solving

## Algorithms

### Linear Search

```py
def linear_search(arr, target):
    # Traverse through all elements in the array
    for index in range(len(arr)):
        # If the element is found, return its index
        if arr[index] == target:
            return index
    # If the element is not found, return -1
    return -1
```

### Binary Search
- Can only be used if the array is already sorted.
- While it is true that as we add more items to the array the time taken increases, but with each iteration of the loop the data set is halved. So, the time increases by smaller and smaller increments until it reaches a constant value.

```py
def binary_search(arr, x):
    low = 0
    high = len(arr) - 1
    mid = 0
 
    while low <= high:
 
        mid = (high + low) // 2
 
        # If x is greater, ignore left half
        if arr[mid] < x:
            low = mid + 1
 
        # If x is smaller, ignore right half
        elif arr[mid] > x:
            high = mid - 1
 
        # means x is present at mid
        else:
            return mid
 
    # If we reach here, then the element was not present
    return -1
```

### Bubble Sort
```py
def bubble_sort(array):

	passes = 1
	swapped = True

	 # If zero swaps occur in a loop, then it's already sorted
	while swapped == True:
    	swapped = False
		 # Iterate through the list n times, ignoring last items as they have already been sorted
    	for i in range(len(array) - passes):
			# Swap elements if they are in the wrong order
        	if array[i+1] > array[i]:
            	temp = array[i+1]
	            array[i+1] = array[i]
    	        array[i] = temp
                # Mark that a swap has occurred
        	    swapped = True
    	passes += 1
  
```
### Insertion Sort
```py
def insertionSort(arr):
    n = len(arr)  # Get the length of the array
      
    if n <= 1:
        return  # If the array has 0 or 1 element, it is already sorted, so return
 
    for i in range(1, n):  # Iterate over the array starting from the second element
        key = arr[i]  # Store the current element as the key to be inserted in the right position
        j = i-1
        while j >= 0 and key < arr[j]:  # Move elements greater than key one position ahead
            arr[j+1] = arr[j]  # Shift elements to the right
            j -= 1
        arr[j+1] = key  # Insert the key in the correct position
```