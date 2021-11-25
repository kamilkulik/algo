def min_characters_for_words(words):
    maximum_frequencies = {}

    for word in words:
        character_frequencies = count_character_frequencies(word)
        update_maximum_frequencies(maximum_frequencies, character_frequencies)

    return make_frequencies_into_characters(maximum_frequencies)


def count_character_frequencies(word):
    frequency = {}

    for character in word:
        if character not in frequency:
            frequency[character] = 0

        frequency[character] += 1

    return frequency


def update_maximum_frequencies(maximum_frequencies, character_frequencies):
    for character, frequency in character_frequencies.items():

        if character in maximum_frequencies:
            maximum_frequencies[character] = max(
                maximum_frequencies[character], frequency
            )
        else:
            maximum_frequencies[character] = frequency


def make_frequencies_into_characters(maximum_frequencies):
    output = []

    for character, frequency in maximum_frequencies.items():

        for _ in range(frequency):
            output.append(character)

    return output
