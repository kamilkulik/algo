# the idea is work on two subarrays
# THE FIRST is going to be created at the beginning of the input array
# into it, we'll INSERT the smallest element from the other sub array at index 0
# THE SECOND subarray will contain the unsorted elements
# it will decrease in length proportionally to how the first subarray will increase in length
# it will be iterated over for smallest elements

# O(n^2) time and O(1) space

def selection_sort(array):
    for i in range(len(array) -1):
        j = i
        for j in range(j, len(array)):
            if array[i] > array[j]:
                swap(array, i, j)
            j += 1
    return array

def swap(array, i, j):
    array[i], array[j] = array[j], array[i]

print(selection_sort([5, 2, 1, -6, 10, 123, -432, 78, 44]))