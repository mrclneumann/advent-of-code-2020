import numpy as np
from itertools import product
from scipy.signal import convolve2d

empty = "L"
occupied = "#"
floor = "."


def read_input(file):
    return np.array([list(line.strip()) for line in file.readlines()])


def part_one(grid):
    return run(grid, next_generation_1)


def part_two(grid):
    return run(grid, next_generation_2)


def run(grid, f):
    while True:
        next_grid = f(grid)

        if np.array_equal(grid, next_grid):
            return count(grid, occupied)

        grid = next_grid


def count(grid, seat):
    return np.sum(grid == seat)


def next_generation_1(grid):
    occupied_seats = convolve2d(
        grid == occupied, np.array([[1, 1, 1], [1, 0, 1], [1, 1, 1]]), mode="same"
    )

    return rule_1(grid, occupied_seats)


def next_generation_2(grid):
    occupied_seats = np.zeros(grid.shape)

    for y in range(len(grid)):
        for x in range(len(grid[0])):
            occupied_seats[y, x] = sum(
                visible(grid, x, y, dx, dy)
                for dx, dy in product([-1, 0, 1], repeat=2)
                if dx or dy
            )
    return rule_2(grid, occupied_seats)


def visible(grid, x, y, dx, dy):
    while True:
        x += dx
        y += dy

        if not ((0 <= x < len(grid[0])) and (0 <= y < len(grid))):
            return 0
        if grid[y, x] == floor:
            continue
        if grid[y, x] == empty:
            return 0
        else:
            return 1


@np.vectorize
def rule_1(seat, occupied_seats):
    return (
        occupied
        if seat == empty and occupied_seats == 0
        else empty
        if seat == occupied and occupied_seats >= 4
        else seat
    )


@np.vectorize
def rule_2(seat, occupied_seats):
    return (
        occupied
        if seat == empty and occupied_seats == 0
        else empty
        if seat == occupied and occupied_seats >= 5
        else seat
    )
