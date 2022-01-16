def count_construct(word, wordbank, memo={}):
    if word in memo:
        return memo[word]
    if word == "":
        return 1
    combinations = 0
    for prefix in wordbank:
        if word.startswith(prefix):
            suffix = word[len(prefix) :]
            combinations += count_construct(suffix, wordbank, memo)
    memo[word] = combinations
    return combinations


def count_construct_tabularised(target, wordbank):
    table = [0 for _ in range(len(target) + 1)]
    table[0] = 1

    for i in range(len(target)):
        if table[i]:
            current_substring = target[i:]
            for word in wordbank:
                if i + len(word) <= len(target) and current_substring.startswith(word):
                    # at this point we have a root that is true
                    # and we have a word that is found in the current substring
                    table[i + len(word)] += table[i]
    return table[-1]
