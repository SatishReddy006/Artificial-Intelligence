def rotated_array_search(input_list, number):
    """
    Find the index by searching in a rotated sorted array

    Args:
       input_list(array), number(int): Input array to search and the target
    Returns:
       int: Index or -1
    """
    if len(input_list)>=1 and number != None:
        mid = (len(input_list)-1)//2
        if (input_list[mid]>=number):
            for index in range(mid,len(input_list)):
                if input_list[index] == number:
                    return index
        for index in range(0,mid):
            if input_list[index] == number:
                return index
    return -1

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


test_function([[6, 7, 8, 9, 10, 1, 2, 3, 4], 6]) #return 0
test_function([[6, 7, 8, 9, 10, 1, 2, 3, 4], 1]) #return 5
test_function([[6, 7, 8, 1, 2, 3, 4], 8])    #return 2
test_function([[6, 7, 8, 1, 2, 3, 4], 1])    #return 3
test_function([[6, 7, 8, 1, 2, 3, 4], 10])   #return -1
test_function([[], 6])   #return -1
test_function([[], None])  #return -1