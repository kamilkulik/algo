import pytest
from src.overlapping_intervals.overlapping_intervals import overlapping_intervals

test_cases = [
    ([
         [0, 0],
         [0, 0],
         [0, 0],
         [0, 0],
         [0, 0],
         [0, 0],
         [0, 0]], [
         [0, 0]
     ]),
    ([
         [1, 2],
         [3, 5],
         [4, 7],
         [6, 8],
         [9, 10]
     ], [
         [1, 2],
         [3, 8],
         [9, 10]
     ]),
    ([
         [1, 10],
         [11, 20],
         [21, 30],
         [31, 40],
         [41, 50],
         [51, 60],
         [61, 70],
         [71, 80],
         [81, 90],
         [91, 100]
     ], [
         [1, 105]
     ]),
    ([
         [89, 90],
         [-10, 20],
         [-50, 0],
         [70, 90],
         [90, 91],
         [90, 95]
     ], [
         [-50, 20],
         [70, 95]
     ])
]

ids = ['test set: {}'.format(test_cases.index(case) + 1) for case in test_cases]


@pytest.mark.parametrize('intervals, merged_intervals', test_cases, ids=ids)
def test_overlapping_intervals(intervals, merged_intervals):
    assert overlapping_intervals(intervals) == merged_intervals
