import pytest

from aoc.day_01 import part_01, part_02, read_puzzle


@pytest.fixture()
def puzzle():
    return read_puzzle("../input/input_01.txt")


def test_part_01():
    assert part_01([1721, 979, 366, 299, 675, 1456]) == 514579


def test_part_02():
    assert part_02([1721, 979, 366, 299, 675, 1456]) == 241861950


def test_solution(puzzle):
    assert part_01(puzzle) == 989824
    assert part_02(puzzle) == 66432240
