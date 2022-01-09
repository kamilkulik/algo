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
