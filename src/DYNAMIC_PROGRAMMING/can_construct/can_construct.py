def can_construct(word, wordbank, memo={}):
    if word in memo:
        return memo[word]
    if word == "":
        return True
    for current_word in wordbank:
        if word.startswith(current_word):
            word_copy = word[len(current_word) :]
            if can_construct(word_copy, wordbank, memo):
                memo[word] = True
                return True
    memo[word] = False
    return False


def can_construct_tabularised(word, wordbank):
    table = [False for _ in range(len(word) + 1)]
    table[0] = True

    for i in range(len(table)):
        if table[i]:
            for prefix in wordbank:
                current_word = word[i:]
                if current_word.startswith(prefix) and i + len(prefix) <= len(table):
                    table[i + len(prefix)] = True
    return table[-1]
