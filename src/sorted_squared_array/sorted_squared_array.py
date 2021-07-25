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

    return reverse(result)

def reverse(array):
    if len(array) == 1: return [array[0]]
    return [array[-1]] + reverse(array[:-1])
