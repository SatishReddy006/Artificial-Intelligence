def rearrange_digits(input_list):
    """
    Rearrange Array Elements so as to form two number such that their sum is maximum.

    Args:
       input_list(list): Input List
    Returns:
       (int),(int): Two maximum sums
    """
    if input_list is None or len(input_list) <= 1:
        return [-1, -1]

    input_freq = [0] * 10
    for num in input_list:
        input_freq[num] += 1

    array_one, array_two = [], []
    first = 1
    if len(input_list) % 2 != 0:
        first = 2
    for i in range(9, -1, -1):
        while input_freq[i]:
            if first:
                array_one.append(str(i))
                first -= 1
            else:
                first += 1
                array_two.append(str(i))
            input_freq[i] -= 1
    return [int(''.join(array_one)), int(''.join(array_two))]

def test_function(test_case):
    output = rearrange_digits(test_case[0])
    solution = test_case[1]
    if sum(output) == sum(solution):
        print("Pass")
    else:
        print("Fail")

test_function([[1, 2, 3, 4, 5], [542, 31]])   #return [542, 31]
test_function([[4, 6, 2, 5, 9, 8], [964, 852]])  #return [964, 852]
test_function([[], [-1,-1]])    #return [-1,-1]
test_function([None, [-1,-1]])  #return [-1,-1]
