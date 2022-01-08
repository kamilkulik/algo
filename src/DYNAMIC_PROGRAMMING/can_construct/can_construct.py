def can_construct(word, wordbank):
    if word == "":
        return True
    for current_word in wordbank:
        if word.startswith(current_word):
            word_copy = word[len(current_word) :]
            if can_construct(word_copy, wordbank):
                return True
    return False
