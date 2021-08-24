import pytest
from src.bubble_sort.bubble_sort import bubble_sort, bubble_sort_optimised
from src.sorting_test_cases.sorting_test_cases import sorting_test_cases

@pytest.mark.parametrize('input_array, sorted_array', sorting_test_cases)
def test_bubble_sort(input_array, sorted_array):
  assert bubble_sort(input_array) == sorted_array

@pytest.mark.parametrize('input_array, sorted_array', sorting_test_cases)
def test_bubble_sort_optimised(input_array, sorted_array):
  assert bubble_sort_optimised(input_array) == sorted_array