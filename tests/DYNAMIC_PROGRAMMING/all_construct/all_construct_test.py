import pytest
from src.DYNAMIC_PROGRAMMING.all_construct.all_construct import (
    all_construct,
    all_construct_tabularised,
)
from tests.conftest import reset_defaults

test_cases = [
    ("skateboard", ["ska", "t", "board", "eboar", "teb"], []),
    (
        "abcdef",
        ["abc", "ab", "cde", "def", "bcd", "ef", "a", "f"],
        [["abc", "def"], ["ab", "cde", "f"], ["a", "bcd", "ef"]],
    ),
    (
        "enterapotentpot",
        ["a", "p", "ent", "enter", "ot", "o", "t"],
        [
            ["enter", "a", "p", "ot", "ent", "p", "ot"],
            ["enter", "a", "p", "ot", "ent", "p", "o", "t"],
            ["enter", "a", "p", "o", "t", "ent", "p", "ot"],
            ["enter", "a", "p", "o", "t", "ent", "p", "o", "t"],
        ],
    ),
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
        [],
    ),
]

ids = ["word: {}".format(case[0]) for case in test_cases]


@pytest.mark.parametrize("word, wordbank, constructable", test_cases, ids=ids)
def test_count_construct(word, wordbank, constructable):
    reset_defaults(all_construct)
    assert all_construct(word, wordbank) == constructable


@pytest.mark.parametrize("word, wordbank, constructable", test_cases, ids=ids)
def test_count_construct_tabularised(word, wordbank, constructable):
    assert all_construct_tabularised(word, wordbank) == constructable
