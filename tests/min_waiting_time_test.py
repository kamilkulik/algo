import pytest
from src.min_waiting_time.min_waiting_time import min_waiting_time, min_waiting_time_smart

test_cases = [
    ([1, 1, 1, 4, 5, 6, 8, 1, 1, 2, 1], 81),
    ([17, 4, 3], 10),
    ([2], 0),
    ([4, 3, 1, 1, 3, 2, 1, 8], 45),
    ([1, 9], 1)
]

ids = ['queries: {}, min_wait_time: {}'.format(case[0], case[1]) for case in test_cases]

@pytest.mark.parametrize('queries, min_wait_time', test_cases, ids = ids)
def test_min_waiting_time(queries, min_wait_time):
    assert min_waiting_time(queries) == min_wait_time

@pytest.mark.parametrize('queries, min_wait_time', test_cases, ids = ids)
def test_min_waiting_time_smart(queries, min_wait_time):
    assert min_waiting_time_smart(queries) == min_wait_time
