def get_min_max_by_sorting(ints):
    """
    Return a tuple(min, max) out of list of unsorted integers.

    Args:
       ints(list): list of integers containing one or more integers
    """
    if ints is None or len(ints)<1:
        return (-1,-1)
    return getMinMax(0,len(ints)-1,ints)

def getMinMax(low, high, arr):
    arr_max = arr[low]
    arr_min = arr[low]
     
    # If there is only one element
    if low == high:
        arr_max = arr[low]
        arr_min = arr[low]
        return (arr_min,arr_max)
         
    # If there is only two element
    elif high == low + 1:
        if arr[low] > arr[high]:
            arr_max = arr[low]
            arr_min = arr[high]
        else:
            arr_max = arr[high]
            arr_min = arr[low]
        return (arr_min,arr_max)
    else:
         
        # If there are more than 2 elements
        mid = int((low + high) / 2)
        arr_min1,arr_max1 = getMinMax(low, mid, arr)
        arr_min2,arr_max2 = getMinMax(mid + 1, high, arr)
 
    return (min(arr_min1, arr_min2),max(arr_max1, arr_max2))

## Example Test Case of Ten Integers
import random

l = [i for i in range(0, 10)]  # a list containing 0 - 9
random.shuffle(l)

print ("Pass" if ((0, 9) == get_min_max_by_sorting(l)) else "Fail")  #return (0, 9)
print ("Pass" if ((-1,-1) == get_min_max_by_sorting(None)) else "Fail") #return (-1,-1)
print ("Pass" if ((-1, -1) == get_min_max_by_sorting([])) else "Fail") #return (-1,-1)
print ("Pass" if ((6, 6) == get_min_max_by_sorting([6])) else "Fail")  #return (6, 6)
print ("Pass" if ((6, 9) == get_min_max_by_sorting([6,9])) else "Fail")  #return (6, 9)