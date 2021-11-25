import pytest
from src.min_characters_for_words.min_characters_for_words import (
    min_characters_for_words,
)

test_cases = [
    (
        ["this", "that", "did", "deed", "them!", "a"],
        ["t", "t", "h", "i", "s", "a", "d", "d", "e", "e", "m", "!"],
    ),
    (["a"], ["a"]),
    (["!!!2", "234", "222", "432"], ["!", "!", "!", "2", "2", "2", "3", "4"]),
]

labels = [f"words: {words}, chars: {outputs}" for words, outputs in test_cases]


@pytest.mark.parametrize("words, characters", test_cases, labels)
def test_min_characters_for_words(words, characters):
    assert min_characters_for_words(words) == characters
