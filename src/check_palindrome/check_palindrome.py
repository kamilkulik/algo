def check_palindrome_string_concat(string):
    new_string = ''
    for i in reversed(range(len(string))):
        new_string += string[i]
    return new_string == string