def first_duplicate(array):
    duplicates = set()
    for value in array:
        if value in duplicates:
            return value
        duplicates.add(value)
    return -1


# time O(n^2), space O(1)
def first_duplicate_brute(array):
    minimum_second_idx = len(array)
    for i in range(len(array)):
        current_element = array[i]
        for j in range(i + 1, len(array)):
            second_duplicate = array[j]
            if second_duplicate == current_element:
                minimum_second_idx = min(minimum_second_idx, j)
    return array[minimum_second_idx] if minimum_second_idx < len(array) else -1