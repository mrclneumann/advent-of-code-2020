import pytest

from aoc.day_02 import parse_line, part_01, part_02, PasswordRecord, read_puzzle


@pytest.fixture()
def puzzle():
    return read_puzzle("../input/input_02.txt")


def test_parse_line():
    assert parse_line("1-3 a: abcde") == (1, 3, "a", "abcde")


def test_part_01():
    assert (
        part_01(
            [
                PasswordRecord(1, 3, "a", "abcde"),
                PasswordRecord(1, 3, "b", "cdefg"),
                PasswordRecord(2, 9, "c", "ccccccccc"),
            ]
        )
        == 2
    )


def test_part_02():
    assert (
        part_02(
            [
                PasswordRecord(1, 3, "a", "abcde"),
                PasswordRecord(1, 3, "b", "cdefg"),
                PasswordRecord(2, 9, "c", "ccccccccc"),
            ]
        )
        == 1
    )


def test_solution(puzzle):
    assert part_01(puzzle) == 582
    assert part_02(puzzle) == 729
