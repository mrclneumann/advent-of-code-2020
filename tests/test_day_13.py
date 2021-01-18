import pytest

from advent.day_13 import part_one, Schedule, read_input, part_two


@pytest.fixture()
def schedule():
    return Schedule(939, [7, 13, None, None, 59, None, 31, 19])


def test_solution(schedule):
    assert part_one(schedule) == 295
    assert part_two(schedule) == 1068781


@pytest.fixture()
def input_path(tmp_path):
    p = tmp_path / "input.txt"

    p.write_text(
        """
939
7,13,x,x,59,x,31,19
    """.strip()
    )

    return p


def test_read_input(input_path, schedule):
    with input_path.open("r") as f:
        assert read_input(f) == schedule
