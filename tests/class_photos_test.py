from src.class_photos.class_photos import class_photos
import pytest

test_cases = [
    ([6], [6], False),
    ([6, 9, 2, 4, 5, 1], [5, 8, 1, 3, 4, 9], False),
    ([1, 2, 3, 4, 5], [2, 3, 4, 5, 6], True),
    ([1, 1, 1, 1, 1, 1, 1, 1], [2, 2, 2, 2, 2, 2, 2, 2], True),
    ([19, 2, 4, 6, 2, 3, 1, 1, 4], [21, 5, 4, 4, 4, 4, 4, 4, 4], False)
]

ids = ['red_shirts: {}, blue_shirt: {}, photo_possible: {}'.format(case[0], case[1], case[2]) for case in test_cases]

@pytest.mark.parametrize('red_shirt_heights, blue_shirt_heights, photo_possible', test_cases, ids=ids)
def test_class_photos(red_shirt_heights, blue_shirt_heights, photo_possible):
    
    assert class_photos(red_shirt_heights, blue_shirt_heights) == photo_possible