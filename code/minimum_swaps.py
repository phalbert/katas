def minimum_swaps(ratings):
    swaps = 0
    if sorted(ratings, reverse=True) == ratings:
       return swaps

    array = ratings
    for i in range(len(ratings)):
        if i + 1 < len(ratings):
            swapped, x, y = swap(ratings[i], ratings[i + 1])
            array[i] = x
            array[i + 1] = y
            
            if swapped:
                swaps =+ 1
        
        
    return swaps

def swap(x,y):
    if x < y:
        return True, y, x
    return False, x, y

value = minimum_swaps([3,1,2,4])
print(value)
