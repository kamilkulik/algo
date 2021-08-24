# the idea is to iterate over an array
# at each iteration compare two adjacent numbers and put them in ascending order if necessary
# algorithm will have completed after no sorting was done in last iteration

# Worst case complexity: O(n^2) time and O(1) space
# Average case complexity: O(n^2) time and O(1) space
# Best case complexity: O(n) time and O(1) space - when the array is sorted

def bubble_sort(array):
    is_sorted = False
    while not is_sorted:
        is_sorted = True
        for i in range(len(array) - 1):
            if array[i] > array[i + 1]:
                swap(array, i)
                is_sorted = False
    return array

def swap(array, i):
    array[i], array[i + 1] = array[i + 1], array[i]

print(bubble_sort([5, 2, 1, -6, 10, 123, -432, 78, 44]))

# slight optimisation that doesn't affect space-time complexity:

def bubble_sort_optimised(array):
    is_sorted = False
    counter = 0 # introduce a counter which will increase by 1 at each iteration
    while not is_sorted:
        is_sorted = True
        for i in range(len(array) - 1 - counter): # because at each iteration the maximum number will be pushed to the end of array we don't have to iterate over it in the next iteration
            if array[i] > array[i + 1]:
                swap(array, i)
                is_sorted = False
        counter += 1 # increment at the end of each full iteration (outside for loop)
    return array

def swap(array, i):
    array[i], array[i + 1] = array[i + 1], array[i]

print(bubble_sort_optimised([5, 2, 1, -6, 10, 123, -432, 78, 44]))