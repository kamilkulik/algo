# Write a function that takes in a non-empty array of integers that are sorted
# in ascending order and returns a new array of the same length with the squares
# of the original integers also sorted in ascending order.

def sorted_squared_array_naive(array):
    
    result = []
    for value in array:
        new_value = value ** 2
        result.append(new_value)

    result.sort()
    return result

def sorted_squared_array(array):
    if len(array) <= 1:
        return array

    result = []
    left = 0
    right = len(array) - 1

    while left < right:
        if abs(array[right]) > abs(array[left]):
            result.append(array[right] ** 2)
            right -= 1
        else:
            result.append(array[left] ** 2)
            left += 1
    result.append(array[left] ** 2)

    return reverse_iteratively(result)

def reverse(array):
    if len(array) == 1: return [array[0]]
    return [array[-1]] + reverse(array[:-1])

def reverse_iteratively(array):
    start = 0
    end = len(array) - 1

    while start < end:
        array[start], array[end] = array[end], array[start]
        start += 1
        end -= 1
    return array


def sorted_squared_array_no_reversal(array):
    output = [0 for _ in array]
    largestIdx = len(array) - 1
    smallestIdx = 0
    
    for idx in reversed(range(len(array))):
        smallest = array[smallestIdx]
        largest = array[largestIdx]
        
        if (abs(largest) > abs(smallest)):
            output[idx] = largest ** 2
            largestIdx -= 1
        else:
            output[idx] = smallest ** 2
            smallestIdx += 1
    return output