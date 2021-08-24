import pytest
from src.insertion_sort.insertion_sort import insertion_sort
from src.sorting_test_cases.sorting_test_cases import sorting_test_cases

@pytest.mark.parametrize('input_array, sorted_array', sorting_test_cases)
def test_insertion_sort(input_array, sorted_array):
  assert insertion_sort(input_array) == sorted_array