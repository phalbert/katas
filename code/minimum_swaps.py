"""
Question:
Mary can perform the following minimal sequence of swap operations to 
successfully sort all 3 items by decreasing popularity rating: [3, 1, 2] → [3, 2, 1].

rearrange the items on the shelf by  decreasing popularity rating such that the rating for the i item
is always greater than the popularity rating of the (i + 1) item.

Solution:
1. The swap always compares the last element in the array with
 the least element in the remaining list e.g.  
 in the case  of [3, 1, 2, 4]...we compare 4 with the minimum value in [3,1,2]
  and swap the two if the minimum value is less
2. Repeat 1 until the the list is sorted in descending order
3. Do the above while counting the swaps"""

def minimum_swaps(ratings):
    if sorted(ratings, reverse=True) == ratings:
       return 0
    swaps = 1
    while sorted(ratings, reverse=True) != sorter(ratings):
        swaps += 1
    return swaps

def sorter(array):

    for i in sorted(range(len(array)), reverse=True):    
        comp = array[:i]
        if len(comp) > 0:
            mini = min(comp)

        if mini < array[i]:
            index = array.index(mini)

            array[i], array[index] = array[index], array[i]
            return array

    return array

print(minimum_swaps([3,1,2,4]))

print(minimum_swaps([3,1,2]))

print(minimum_swaps([3,2,1]))