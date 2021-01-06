import pytest
from advent.day_05 import read_input, seat_id, row, col


@pytest.fixture()
def input_path(tmp_path):
    p = tmp_path / "input.txt"

    p.write_text("\n".join(["BFFFBBFRRR", "FFFBBBFRRR", "BBFFBBFRLL"]))

    return p


def test_read_input(input_path):
    with input_path.open("r") as f:
        assert read_input(f) == ["BFFFBBFRRR", "FFFBBBFRRR", "BBFFBBFRLL"]


@pytest.mark.parametrize(
    "boarding_pass,expected",
    [
        ("BFFFBBFRRR", 567),
        ("FFFBBBFRRR", 119),
        ("BBFFBBFRLL", 820),
    ],
)
def test_seat_id(boarding_pass, expected):
    assert seat_id(boarding_pass) == expected


@pytest.mark.parametrize(
    "boarding_pass,expected",
    [
        ("BFFFBBFRRR", 70),
        ("FFFBBBFRRR", 14),
        ("BBFFBBFRLL", 102),
    ],
)
def test_row(boarding_pass, expected):
    assert row(boarding_pass) == expected


@pytest.mark.parametrize(
    "boarding_pass,expected",
    [
        ("BFFFBBFRRR", 7),
        ("FFFBBBFRRR", 7),
        ("BBFFBBFRLL", 4),
    ],
)
def test_col(boarding_pass, expected):
    assert col(boarding_pass) == expected
