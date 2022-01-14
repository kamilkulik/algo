import pytest
from src.DYNAMIC_PROGRAMMING.can_construct.can_construct import (
    can_construct,
    can_construct_tabularised,
)
from tests.conftest import reset_defaults

test_cases = [
    ("skateboard", ["ska", "t", "board", "eboar", "teb"], False),
    ("abcdef", ["abc", "cde", "def", "bcd", "ef", "a"], True),
    ("enterapotentpot", ["a", "p", "ent", "enter", "ot", "o", "t"], True),
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
        False,
    ),
]

ids = ["word: {}".format(case[0]) for case in test_cases]


@pytest.mark.parametrize("word, wordbank, constructable", test_cases, ids=ids)
def test_can_construct(word, wordbank, constructable):
    reset_defaults(can_construct)
    assert can_construct(word, wordbank) == constructable


@pytest.mark.parametrize("word, wordbank, constructable", test_cases, ids=ids)
def test_can_construct_tabularised(word, wordbank, constructable):
    assert can_construct(word, wordbank) == constructable
