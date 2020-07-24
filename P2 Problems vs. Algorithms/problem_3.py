def mergesort(items):

    if len(items) <= 1:
        return items
    
    mid = len(items) // 2
    left = items[:mid]
    right = items[mid:]
    
    left = mergesort(left)
    right = mergesort(right)
    
    return merge(left, right)
    
def merge(left, right):
    
    merged = []
    left_index = 0
    right_index = 0
    
    while left_index < len(left) and right_index < len(right):
        if left[left_index] > right[right_index]:
            merged.append(right[right_index])
            right_index += 1
        else:
            merged.append(left[left_index])
            left_index += 1

    merged += left[left_index:]
    merged += right[right_index:]
        
    return merged

def rearrange_digits(input_list):
    """
    Rearrange Array Elements so as to form two number such that their sum is maximum.

    Args:
       input_list(list): Input List
    Returns:
       (int),(int): Two maximum sums
    """
    if not input_list:
        return []
    if len(input_list)==1:
        return input_list
    
    len_smaller = len(input_list) // 2
    len_bigger = len(input_list) - len_smaller
    
    sorted_list = mergesort(input_list)
    
    smaller = ''
    bigger = ''
    
    give_bigger = True
    for x in sorted_list[::-1]:
        if give_bigger:
            bigger += str(x)
            give_bigger = False
        else:
            smaller += str(x)
            give_bigger = True
    return [int(bigger),int(smaller)]
        
    
    
    
def test_function(test_case):
    output = rearrange_digits(test_case[0])
    solution = test_case[1]
    if sum(output) == sum(solution):
        print("Pass")
    else:
        print("Fail")


# Test cases
test_function([[4, 6, 2, 1, 9, 1, 6, 7, 5, 9, 8], [986521, 97641]])
# Return: pass
test_function([[], []])
# Return: pass
test_function([[3], [3]])
# Return: pass
test_function([[1, 2, 3, 4, 5], [542, 31]])
# Return: pass
test_function([[4, 6, 2, 5, 9, 8], [964, 852]])
# Return: pass
