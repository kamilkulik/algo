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

# COMPLEXITY
# O(n) time
# O(1) time

def validate_subsequence_for_loop(array, sequence):
    seq_pointer = 0
    for value in array:
        if seq_pointer == len(sequence):
            return True
        if value == sequence[seq_pointer]:
            seq_pointer += 1
    return seq_pointer == len(sequence)