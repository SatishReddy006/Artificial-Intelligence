def sqrt(number):
    """
    Calculate the floored square root of a number

    Args:
       number(int): Number to find the floored squared root
    Returns:
       int: Floored Square Root
    """
    if number is None or number <0:
        return None
    if (number == 0 or number == 1) :
        return number
  
    start = 1
    end = number
    while (start <= end) :
        mid = (start + end) // 2
         
        if (mid*mid == number) :
            return mid

        if (mid * mid < number) :
            start = mid + 1
            answer = mid     
        else :
            end = mid-1
             
    return answer

print ("Pass" if  (3 == sqrt(9)) else "Fail") #return 3
print ("Pass" if  (0 == sqrt(0)) else "Fail") #return 0
print ("Pass" if  (4 == sqrt(16)) else "Fail") #return 4
print ("Pass" if  (None == sqrt(-1)) else "Fail") #return None
print ("Pass" if  (None == sqrt(None)) else "Fail") #return None