from aoc.day_01 import part_01, part_02


def test_part_01():
    assert part_01([1721, 979, 366, 299, 675, 1456]) == 514579


def test_part_02():
    assert part_02([1721, 979, 366, 299, 675, 1456]) == 241861950
