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
