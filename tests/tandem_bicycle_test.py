import pytest
from src.tandem_bicycle.tandem_bicycle import tandem_bicycle, tandem_bicycle_with_reverse

test_cases = [
    ([], [], True, 0),
    ([1, 2, 3, 4, 5], [5, 4, 3, 2, 1], True, 21),
    ([1, 2, 3, 4, 5], [5, 4, 3, 2, 1], False, 15),
    ([3, 4, 4, 1, 1, 8, 9], [9, 8, 2, 2, 3, 5, 6], False, 35),
    ([3, 4, 4, 1, 1, 8, 9], [9, 8, 2, 2, 3, 5, 6], True, 49)
]

ids = ['blue_shirt_speeds: {}, red_shirt_speeds: {}, fastest: {}, tandem_speed: {}'
.format(case[0], case[1], case[2], case[3]) for case in test_cases]

@pytest.mark.parametrize('blue_shirt_speeds, red_shirt_speeds, fastest, tandem_speed', test_cases, ids = ids)
def test_tandem_bicycle(blue_shirt_speeds, red_shirt_speeds, fastest, tandem_speed):
    assert tandem_bicycle(blue_shirt_speeds, red_shirt_speeds, fastest) == tandem_speed

@pytest.mark.parametrize('blue_shirt_speeds, red_shirt_speeds, fastest, tandem_speed', test_cases, ids = ids)
def test_tandem_bicycle_with_reverse(blue_shirt_speeds, red_shirt_speeds, fastest, tandem_speed):
    assert tandem_bicycle_with_reverse(blue_shirt_speeds, red_shirt_speeds, fastest) == tandem_speed
