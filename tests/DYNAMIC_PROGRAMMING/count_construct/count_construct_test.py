import pytest
from src.DYNAMIC_PROGRAMMING.count_construct.count_construct import (
    count_construct,
    count_construct_tabularised,
)
from tests.conftest import reset_defaults

test_cases = [
    ("skateboard", ["ska", "t", "board", "eboar", "teb"], 0),
    ("abcdef", ["abc", "ab", "cde", "def", "bcd", "ef", "a", "f"], 3),
    ("enterapotentpot", ["a", "p", "ent", "enter", "ot", "o", "t"], 4),
    (
        "eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeef",
        [
            "e",
            "ee",
            "eee",
            "eeee",
            "eeeee",
            "eeeeee",
        ],
        0,
    ),
]

ids = ["word: {}".format(case[0]) for case in test_cases]


@pytest.mark.parametrize("word, wordbank, constructable", test_cases, ids=ids)
def test_count_construct(word, wordbank, constructable):
    reset_defaults(count_construct)
    assert count_construct(word, wordbank) == constructable


@pytest.mark.parametrize("word, wordbank, constructable", test_cases, ids=ids)
def test_count_construct_tabularised(word, wordbank, constructable):
    assert count_construct_tabularised(word, wordbank) == constructable
