def move_element_to_end(array, to_move):
    left_pointer = 0
    right_pointer = len(array) - 1

    while left_pointer < right_pointer:

        while array[right_pointer] == to_move and left_pointer < right_pointer:

            right_pointer -= 1

        if array[left_pointer] == to_move:
            array[left_pointer], array[right_pointer] = array[right_pointer], array[left_pointer]

        left_pointer += 1

    return array
