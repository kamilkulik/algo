def monotonic_array(array):
    is_non_decreasing = True
    is_non_increasing = True

    for i in range(1, len(array)):
        direction = array[i -1] - array[i]
        if direction > 0:
            is_non_increasing = False
        elif direction < 0:
            is_non_decreasing = False

    return is_non_decreasing or is_non_increasing
