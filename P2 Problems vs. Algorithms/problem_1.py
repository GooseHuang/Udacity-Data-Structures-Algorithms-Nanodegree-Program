def sqrt(number=None):
    """
    Calculate the floored square root of a number

    Args:
       number(int): Number to find the floored squared root
    Returns:
       int: Floored Square Root
    """
    if number == None:
        return None
    
    if number <= 1:
        if number <0:
            return None
        else:
            return number
    
    upper = number
    lower = 0
    while upper - lower > 1:
        mid = (upper + lower) // 2
        
        mid_squre = mid * mid
        if mid_squre == number:
            return mid
        elif mid * mid > number:
            upper = mid
        else:
            lower = mid
    
    return lower
        
        
    
# Test cases
print ("Pass" if  (None == sqrt()) else "Fail")
print ("Pass" if  (None == sqrt(-27)) else "Fail")
print ("Pass" if  (3 == sqrt(9)) else "Fail")
print ("Pass" if  (0 == sqrt(0)) else "Fail")
print ("Pass" if  (4 == sqrt(16)) else "Fail")
print ("Pass" if  (1 == sqrt(1)) else "Fail")
print ("Pass" if  (5 == sqrt(27)) else "Fail")