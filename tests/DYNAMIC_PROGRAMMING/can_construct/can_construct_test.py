import pytest
from src.DYNAMIC_PROGRAMMING.can_construct.can_construct import can_construct

test_cases = [
    ("skateboard", ["ska", "t", "board", "eboar", "teb"], False),
    ("abcdef", ["abc", "cde", "def", "bcd", "ef", "a"], True),
]

ids = ["word: {}".format(case[0]) for case in test_cases]


@pytest.mark.parametrize("word, wordbank, constructable", test_cases, ids=ids)
def test_can_construct(word, wordbank, constructable):
    assert can_construct(word, wordbank) == constructable
