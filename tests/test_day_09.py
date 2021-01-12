import pytest

from advent.day_09 import is_valid, find_range_summing_to


@pytest.mark.parametrize(
    "numbers,n,expected", [([1, 2, 3], 42, False), ([2, 3, 4, 1], 7, True)]
)
def test_xmas(numbers, n, expected):
    assert is_valid(numbers, n) == expected


def test_contiguous_set():
    assert (
        find_range_summing_to(
            [
                5,
                1,
                2,
                4,
            ],
            3,
        )
        == [1, 2]
    )
