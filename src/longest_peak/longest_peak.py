def longest_peak(array):
    longest_peak_length = 0
    i = 1

    while i < len(array) - 1:
        # checking if we have a peak at i
        is_peak = array[i - 1] < array[i] and array[i] > array[i + 1]
        if not is_peak:
            i += 1
            continue

        # we now know we have a peak
        # checking the length of the peak to the left
        left_idx = i - 2
        while left_idx >= 0 and array[left_idx] < array[left_idx + 1]:
            left_idx -= 1
        # checking the length of the peak to the right
        right_idx = i + 2
        while right_idx < len(array) and array[right_idx - 1] > array[right_idx]:
            right_idx += 1

        current_longest_peak = right_idx - left_idx - 1
        longest_peak_length = max(current_longest_peak, longest_peak_length)

        i = right_idx

    return longest_peak_length