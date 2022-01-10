def all_construct(word, wordbank, memo={}):
    if word in memo:
        return memo[word]
    if word == "":
        return [[]]
    combinations = []
    for prefix in wordbank:
        if word.startswith(prefix):
            suffix = word[len(prefix) :]
            suffix_ways = all_construct(suffix, wordbank, memo)
            word_ways = map(lambda suffix_way: [prefix] + suffix_way, suffix_ways)
            combinations = combinations + [word_way for word_way in word_ways]
    memo[word] = combinations
    return combinations
