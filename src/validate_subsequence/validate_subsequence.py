# pointer based solution
# the idea is to iterate over the entire array and increase sequence pointer each time sequence number is found
# if entire subsequence was found in array then the sequence pointer will have been iterated to the length of sequence array

# COMPLEXITY
# O(n) time
# O(1) space

def validate_subsequence(array, sequence):
    # 1. initialize two pointers - 1 for the array and second for sequence
    seq_pointer = 0
    arr_pointer = 0
    # 2. Loop over both arrays as long as both pointers are less than those arrays' lengths
    while arr_pointer < len(array) and seq_pointer < len(sequence):
        # 3. Check if array contains the number of sequence
        if array[arr_pointer] == sequence[seq_pointer]:
            # 3a. if yes, increase the sequence pointer - in next iteration we want to look for the next number in seuqence array
            seq_pointer += 1
        # 4. At the end of each iteration increase the array pointer:
        # if we also increased the seq pointer, than we'll check if the sequence continues in the array
        # otherwise, we'll continue to check for seuqence further in the array
        arr_pointer += 1
        # 5. at the end, check if sequence pointer is of the length of sequence
        # if yes that means enough times sequence pointer was increased to go over all seuqence numbers
    return seq_pointer == len(sequence)

# for loop based solution
# very similar to pointer-based solution
# uses for loop to iterate over each element of array and increments sequence pointer each time seuqence num is found in array


# COMPLEXITY
# O(n) time
# O(1) space

def validate_subsequence_for_loop(array, sequence):
    seq_pointer = 0
    for value in array:
        # very important exit condition
        # once the subsequence is found we need to exit the loop so we don't check for an index of of bounds
        if seq_pointer == len(sequence):
            return True
        if value == sequence[seq_pointer]:
            seq_pointer += 1
    return seq_pointer == len(sequence)