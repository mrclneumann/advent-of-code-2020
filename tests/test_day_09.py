import pytest

from advent.day_09 import xmas, contiguous_set


@pytest.mark.parametrize(
    "numbers,n,expected", [([1, 2, 3], 42, False), ([2, 3, 4, 1], 7, True)]
)
def test_xmas(numbers, n, expected):
    assert xmas(numbers, n) == expected


def test_contiguous_set():
    assert (
        contiguous_set(
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
