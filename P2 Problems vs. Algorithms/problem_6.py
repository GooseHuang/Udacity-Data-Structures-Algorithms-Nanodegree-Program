def get_min_max(ints):
    """
    Return a tuple(min, max) out of list of unsorted integers.

    Args:
       ints(list): list of integers containing one or more integers
    """
    if not ints:
        return (None,None)
    min_number = ints[0]
    max_number = ints[0]
    for x in ints[1:]:
        if x > max_number:
            max_number = x
        if x < min_number:
            min_number = x
    
    return (min_number,max_number)

## Example Test Case of Ten Integers
import random


l = [i for i in range(0, 10)]  # a list containing 0 - 9
random.shuffle(l)

print ("Pass" if ((0, 9) == get_min_max(l)) else "Fail")
print ("Pass" if ((None, None) == get_min_max([])) else "Fail")
print ("Pass" if ((0,0) == get_min_max([0,0,0,0,0,0,0,0,0,0,0,0])) else "Fail")