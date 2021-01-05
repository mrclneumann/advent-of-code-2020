from advent.day_03 import Grid, path_generator


def test_grid():
    grid = Grid([".#.", "..#"])

    assert grid[0, 0] == "."
    assert grid[0, 1] == "#"
    assert grid[0, 2] == "."
    assert grid[0, 3] == "."
    assert grid[1, 0] == "."
    assert grid[1, 1] == "."
    assert grid[1, 2] == "#"
    assert grid[1, 3] == "."


def test_path():
    p = path_generator(dx=3, dy=1, limit=3)

    assert next(p) == (0, 0)
    assert next(p) == (1, 3)
    assert next(p) == (2, 6)


def test_path_length():
    p = path_generator(dx=3, dy=1, limit=30)

    assert len(list(p)) == 30
