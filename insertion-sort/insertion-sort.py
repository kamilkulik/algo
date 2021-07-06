# the idea of insertion sort is to divide conceptually input array into two subarrays
# FIRST subarray will contain sorted elements
# SECOND subarray will contain unsorted elements
# current position is going to be an analysed number
# we'll then keep comparing that number to elements to its left
# until we find the right spot for that number
# and we can continue with the iteration

# O(n^2) time and O(1) space

def insertion_sort(array):
    for i in range(len(array)):
        j = i
        while j > 0 and array[j] < array[j - 1]:
            array[j -1], array [j] = array[j], array[j -1]
            j -= 1
    return array

print(insertion_sort([5, 2, 1, -6, 10, 123, -432, 78, 44]))
