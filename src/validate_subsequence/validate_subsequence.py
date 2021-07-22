# COMPLEXITY
# O(n) time
# O(1) time

def validate_subsequence(array, sequence):
    seq_pointer = 0
    arr_pointer = 0
    while arr_pointer < len(array) and seq_pointer < len(sequence):
        if array[arr_pointer] == sequence[seq_pointer]:
            seq_pointer += 1
        arr_pointer += 1
    return seq_pointer == len(sequence)

