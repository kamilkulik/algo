# Write a function that takes in a non-empty array of integers that are sorted
# in ascending order and returns a new array of the same length with the squares
# of the original integers also sorted in ascending order.

# this first is a naive approach because we're bumping up time complexity of algo by sorting the square array at the end
# Complexity
# O(nlog(n)) time
# O(n) space

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
    # 1. initiate an array of zeros whose length is same as input array's to have a placeholder array to update with squared values
    output = [0 for _ in array]
    # 2. initiate two variables which will represent indexes of smallest and largest numbers in input array
    # we'll move these effectively pointers towards inside of the array
    largestIdx = len(array) - 1
    smallestIdx = 0
    
    # 3. loop over array in reverse
    # in reverse because we want to start with rightmost element which is guaranteed to be the largest positive integer
    for idx in reversed(range(len(array))):
        # 4. initiate two helper variables
        smallest = array[smallestIdx]
        largest = array[largestIdx]
        
        # 5. condition to check if absolute value of smallest and greatest input integers have same relationship
        if (abs(largest) > abs(smallest)):
            # 6. if yes, update placeholder with square of the larger number
            output[idx] = largest ** 2
            # 7. Move largestIdx pointer leftward
            largestIdx -= 1
        else:
            # 8. Handle else case
            output[idx] = smallest ** 2
            smallestIdx += 1
    return output