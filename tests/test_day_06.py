import pytest
from advent.day_06 import read_input


@pytest.fixture()
def puzzle_path(tmp_path):
    p = tmp_path / "input.txt"

    p.write_text(
        "\n".join(
            [
                "abc",
                "",
                "a",
                "b",
                "c",
                "",
                "ab",
                "ac",
                "",
                "a",
                "a",
                "a",
                "a",
                "",
                "b",
            ]
        )
    )

    return p


def test_read_input(puzzle_path):
    with puzzle_path.open("r") as f:
        assert read_input(f) == [
            ["abc"],
            ["a", "b", "c"],
            ["ab", "ac"],
            ["a", "a", "a", "a"],
            ["b"],
        ]
