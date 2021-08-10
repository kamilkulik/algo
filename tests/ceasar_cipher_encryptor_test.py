import pytest
from src.ceasar_cipher_encryptor.ceasar_cipher_encryptor import ceasar_cipher_encryptor, ceasar_cipher_encryptor_alt

test_cases = [
    ("kjwmntauvjjnmsagwgawkagfuaugjhawgnawgjhawjgawbfawghesh", 15, "zylbcipjkyycbhpvlvplzpvujpjvywplvcplvywplyvplquplvwthw"),
    ("mvklahvjcnbwqvtutmfafkwiuagjkzmzwgf", 7, "tcrshocqjuidxcabatmhmrdpbhnqrgtgdnm"),
    ("ovmqkwtujqmfkao", 52, "ovmqkwtujqmfkao"),
    ("xyz", 25, "wxy"),
    ("abc", 0, "abc")
]

ids = ['string: {}, key: {}'.format(case[0], case[1]) for case in test_cases]

@pytest.mark.parametrize('string, key, output', test_cases, ids = ids)
def test_ceasar_cipher_encryptor(string, key, output):
    assert ceasar_cipher_encryptor(string, key) == output
    
@pytest.mark.parametrize('string, key, output', test_cases, ids = ids)
def test_ceasar_cipher_encryptor_alt(string, key, output):
    assert ceasar_cipher_encryptor_alt(string, key) == output
