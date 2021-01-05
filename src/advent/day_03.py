from itertools import takewhile, count
import math

TREE = "#"


class Grid:
    def __init__(self, locations) -> None:
        self.locations = locations

    def __getitem__(self, pos):
        row, col = pos
        return self.locations[row][col % self.width]

    @property
    def height(self):
        return len(self.locations)

    @property
    def width(self):
        return len(self.locations[0])


def read_input(file):
    return Grid([line.strip() for line in file])


def path_generator(dx, dy, limit):
    return takewhile(lambda p: p[0] < limit, zip(count(0, dy), count(0, dx)))


def num_trees(grid, path):
    return sum(grid[row, col] == TREE for row, col in path)


def part_one(grid):
    return num_trees(grid, path_generator(3, 1, grid.height))


def part_two(grid):
    slopes = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]
    return math.prod(
        num_trees(grid, path_generator(dx, dy, grid.height)) for dx, dy in slopes
    )
