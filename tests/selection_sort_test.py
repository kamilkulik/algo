import pytest
from src.selection_sort.selection_sort import selection_sort
from src.sorting_test_cases.sorting_test_cases import sorting_test_cases

@pytest.mark.parametrize('input_array, sorted_array', sorting_test_cases)
def test_selection_sort(input_array, sorted_array):
  assert selection_sort(input_array) == sorted_array