# the idea is to use two pointers
# left and right representing first and last element of the array
# we will sort the two input arrays and use that to determine which pointer needs to move at a given time
# given arrays are sorted, you check which element is greater
# you want to swap out smaller for greater element
# this means is the smaller element is in array one, you move the pointer in array one to the right
# to get a greater number
# which will potentially decrease the difference with element from list two

def smallest_difference(first_list, second_list):
    first_list.sort()
    second_list.sort()

    first_list_idx = 0
    second_list_idx = 0
    result = [0, 0]
    smallest_diff = float('inf')

    while first_list_idx < len(first_list) and second_list_idx < len(second_list):
        first_list_value = first_list[first_list_idx]
        second_list_value = second_list[second_list_idx]
        difference = abs(first_list_value - second_list_value)

        if difference < smallest_diff:
            smallest_diff = difference
            result[0] = first_list_value
            result[1] = second_list_value

        if first_list_value < second_list_value:
            first_list_idx += 1
        elif second_list_value < first_list_value:
            second_list_idx += 1
        else:
            return [first_list_value, second_list_value]

    return result