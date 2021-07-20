# COMPLEXITY
# O(n) time
# O(1) space
# The constant space is because the input string only has lowercase
# English-alphabet letters; thus, our hash table will never have more
# than 26 character frequencies.

def first_non_repeating_char(string):
    char_count = {}
    for char in string:
        if char not in char_count:
            char_count[char] = 0
        char_count[char] += 1

    for idx in range(len(string)):
        if char_count[string[idx]] == 1:
            return idx
    
    return -1