# the idea is work on two subarrays
# THE FIRST is going to be created at the beginning of the input array
# into it, we'll INSERT the smallest element from the other sub array at index 0
# THE SECOND subarray will contain the unsorted elements
# it will decrease in length proportionally to how the first subarray will increase in length
# it will be iterated over for smallest elements

# O(n^2) time and O(1) space

def selection_sort(array):
    current_idx = 0
    while current_idx < len(array) -1:
        smallest_idx = current_idx
        for i in range(current_idx + 1, len(array)):
            if array[smallest_idx] > array[i]:
                smallest_idx = i
        swap(current_idx, smallest_idx, array)
        current_idx += 1
    return array

def swap(i, j, array):
    array[i], array[j] = array[j], array[i]