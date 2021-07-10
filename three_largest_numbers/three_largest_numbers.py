# this algorithm is meant to find the three largest numbers in an array and return them in an ascending order

# input = [ 1, 2, 4, 69, 83, 43, 124, 843, 432, 321, 238 ]
# output = [ 321, 432, 843 ]

# iterative solution

def three_largest_numbers(array):
    output = [None, None, None]
    for num in array:
        update_num(output, num)
        
    return output

def update_num(output, num):
    if output[2] is None or num > output[2]:
        insert_and_shift(output, num, 2)
    elif output[1] is None or num > output[1]:
        insert_and_shift(output, num, 1)
    elif output[0] is None or num > output[0]:
        insert_and_shift(output, num, 0)

def insert_and_shift(array, num, idx):
    for i in range(0, idx + 1):
        if i == idx:
            array[idx] = num
        else:
            array[i] = array[i + 1]


print(three_largest_numbers([ 1, 2, 4, 69, 83, 43, 124, 843, 432, 321, 238 ]))