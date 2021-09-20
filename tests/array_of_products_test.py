import pytest
from src.array_of_products.array_of_products import array_of_products, array_of_products_brute

test_cases = [
    ([0, 0, 0, 0], [0, 0, 0, 0]),
    ([1, 1, 1, 1], [1, 1, 1, 1]),
    ([-1, -1, -1], [1, 1, 1]),
    ([0, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]),
    ([1, 8, 6, 2, 4], [384, 48, 64, 192, 96]),
    ([-5, 2, -4, 14, -6], [672, -1680, 840, -240, 560])
]

ids = ['input array: {}'.format(case[0]) for case in test_cases]


@pytest.mark.parametrize('input_array, output_array', test_cases, ids=ids)
def test_array_of_products_brute(input_array, output_array):
    assert array_of_products_brute(input_array) == output_array

@pytest.mark.parametrize('input_array, output_array', test_cases, ids=ids)
def test_array_of_products(input_array, output_array):
    assert array_of_products(input_array) == output_array