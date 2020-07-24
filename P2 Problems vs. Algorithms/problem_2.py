def binary_search_recursive(array, target):  
    start_index = 0
    end_index = len(array) - 1  
    
    return binary_search_recursive_func(array, target, start_index, end_index)


def binary_search_recursive_func(array, target, start_index, end_index):
    if start_index > end_index:
        return -1
    
    mid_index = (start_index + end_index)//2
    mid_element = array[mid_index]
    
    if mid_element == target:
        return mid_index
    elif target < mid_element:
        return binary_search_recursive_func(array, target, start_index, mid_index - 1)
    else:
        return binary_search_recursive_func(array, target, mid_index + 1, end_index)
        
        
def find_start_index(input_list):
    
    
    lower = 0
    upper = len(input_list)-1
    if input_list[lower] < input_list[upper]:
        return 0
    
    while upper-lower > 1:
        mid = (upper + lower) // 2
        if input_list[mid] > input_list[upper]:
            lower = mid
        else:
            upper = mid
            
    return upper


def rotated_array_search(input_list, number):
    """
    Find the index by searching in a rotated sorted array

    Args:
       input_list(array), number(int): Input array to search and the target
    Returns:
       int: Index or -1
    """
    if not input_list:
        return -1

    start_index = find_start_index(input_list)
    array = input_list[start_index:] + input_list[:start_index]
    index = binary_search_recursive(array, number)
    if index != -1:
        index = (index + start_index) % len(array)
    return index


def linear_search(input_list, number):
    for index, element in enumerate(input_list):
        if element == number:
            return index
    return -1

def test_function(test_case):
    input_list = test_case[0]
    number = test_case[1]
    if linear_search(input_list, number) == rotated_array_search(input_list, number):
        print("Pass")
    else:
        print("Fail")



# Test cases
test_function([[], -1])
# Return: pass
test_function([[6], 6])
# Return: pass
test_function([[6, 7, 8, 9, 10, 1, 2, 3, 4], 6])
# Return: pass
test_function([[6, 7, 8, 9, 10, 1, 2, 3, 4], 1])
# Return: pass
test_function([[6, 7, 8, 1, 2, 3, 4], 8])
# Return: pass
test_function([[6, 7, 8, 1, 2, 3, 4], 1])
# Return: pass
test_function([[6, 7, 8, 1, 2, 3, 4], 10])
# Return: pass