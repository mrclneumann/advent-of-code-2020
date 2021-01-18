import pytest

from advent.day_12 import (
    Ship,
    interpret,
    Instruction,
    read_input,
    part_one,
    Waypoint,
    part_two,
)


@pytest.fixture
def ship():
    return Ship()


@pytest.fixture()
def input_path(tmp_path):
    p = tmp_path / "input.txt"

    p.write_text(
        """
F10
N3
F7
R90
F11
    """.strip()
    )

    return p


@pytest.fixture()
def instructions():
    return [
        Instruction("forward", 10),
        Instruction("north", 3),
        Instruction("forward", 7),
        Instruction("right", 90),
        Instruction("forward", 11),
    ]


def test_move_north(ship):
    ship.north(3)
    assert ship.position == (0, 3)


def test_move_south(ship):
    ship.south(4)
    assert ship.position == (0, -4)


def test_move_east(ship):
    ship.east(5)
    assert ship.position == (5, 0)


def test_move_west(ship):
    ship.west(6)
    assert ship.position == (-6, 0)


def test_turn_forward(ship):
    ship.forward(2)
    assert ship.position == (2, 0)


def test_turn_left(ship):
    ship.left(90)
    assert ship.dx == 0
    assert ship.dy == 1


def test_turn_right(ship):
    ship.right(180)
    assert ship.dx == -1
    assert ship.dy == 0


def test_interpret(instructions, ship):
    assert interpret(instructions, ship) == 25


def test_read_input(input_path, instructions):
    with input_path.open("r") as f:
        assert list(read_input(f)) == instructions


def test_part_one(instructions):
    assert part_one(instructions) == 25


@pytest.fixture()
def waypoint():
    return Waypoint()


def test_waypoint_north(waypoint):
    waypoint.north(3)
    assert waypoint.position == (10, 4)


def test_waypoint_south(waypoint):
    waypoint.south(5)
    assert waypoint.position == (10, -4)


def test_waypoint_east(waypoint):
    waypoint.east(1)
    assert waypoint.position == (11, 1)


def test_waypoint_west(waypoint):
    waypoint.west(8)
    assert waypoint.position == (2, 1)


def test_waypoint_left(waypoint):
    waypoint.left(90)
    assert waypoint.position == (-1, 10)


def test_waypoint_right(waypoint):
    waypoint.right(270)
    assert waypoint.position == (-1, 10)


def test_waypoint_forward(waypoint):
    waypoint.forward(10)
    assert waypoint.position == (10, 1)
    assert waypoint.ship.position == (100, 10)


def test_part_two(instructions):
    assert part_two(instructions) == 286
