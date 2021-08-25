# the idea is work on two subarrays
# THE FIRST is going to be created at the beginning of the input array
# into it, we'll INSERT the smallest element from the other sub array at index 0
# THE SECOND subarray will contain the unsorted elements
# it will decrease in length proportionally to how the first subarray will increase in length
# it will be iterated over for smallest elements

# O(n^2) time and O(1) space

def selection_sort(array):
    # 1. we need current idx because we'll always be looking forward
    current_idx = 0
    # 2. initiate while loop which will exit after we have looked at the penultimate element
    while current_idx < len(array) -1:
        # 3. initialise new variable declared as smallest_idx - we'll use it to track the index of smallest element
        smallest_idx = current_idx
        # 4. Look ahead loop. For loop that starts at the element after current_idx and loop over to the end of array
        for i in range(current_idx + 1, len(array)):
            # 5. check if the current element is smaller than the next one
            if array[smallest_idx] > array[i]:
                # 6. If not, reassign smallest_idx to i
                smallest_idx = i
                # 7. The for loop repeats this for the rest of the array
                # Finally, we'll have the index of the smallest elements in current tick on the while loop
        # 8. swap the element from current idx (starting at first position, and moving incrementally to the end of array) with the smallest element
        swap(current_idx, smallest_idx, array)
        # 9. increment current_idx for the next tick of the while loop
        current_idx += 1
    return array

def swap(i, j, array):
    array[i], array[j] = array[j], array[i]