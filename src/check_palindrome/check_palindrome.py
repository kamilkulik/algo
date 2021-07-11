
# TIME O(n^2), because since strings are immutable in Python
# string concatination is an O(n^2) operation
# BECAUSE interpreter needs to first allocate space for the new string and then create it
# SPACE O(n)

def check_palindrome_reversed_string_concat(string):
    new_string = ''
    for i in reversed(range(len(string))):
        new_string += string[i]
    return new_string == string

# TIME O(n) because we're now appending to the end of array
# which is an O(n) opearation
# SPACE O(n)

def check_palindrome_reversed_string_array(string):
    new_string = []
    for i in reversed(range(len(string))):
        new_string.append(string[i])
    return ''.join(new_string) == string