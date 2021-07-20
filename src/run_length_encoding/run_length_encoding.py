def run_length_encoding(string):
    result = []
    run_length = 1
    
    for idx in range(1, len(string)): # we want to start from 2nd character to have access to current and previous character
        prev = string[idx -1]
        curr = string[idx]

        if prev is not curr or run_length == 9:
            result.append(str(run_length))
            result.append(prev)
            run_length = 0

        run_length += 1

    # because we're appending prev values, we need to take care of the last character in sequence separately
    result.append(str(run_length))
    result.append(string[-1])

    return ''.join(result)