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


def all_construct_tabularised(target, wordbank):
    table = [[] for _ in range(len(target) + 1)]
    table[0] = [[]]

    for i in range(len(table)):
        if len(table[i]):
            current_substring = target[i:]
            for word in wordbank:
                if i + len(word) <= len(target) and current_substring.startswith(word):

                    combination = map(lambda substring: substring + [word], table[i])
                    combination_final = [element for element in combination]

                    table[i + len(word)] += combination_final

    return table[-1]
