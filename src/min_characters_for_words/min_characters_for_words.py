def min_characters_for_words(words):
    maximum_frequencies = {}

    for word in words:
        character_frequencies = count_character_frequencies(word)
        update_maximum_frequencies(maximum_frequencies, character_frequencies)

    return make_frequencies_into_characters(maximum_frequencies)
