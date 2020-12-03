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


def read_puzzle(filename):
    with open(filename) as f:
        return Grid([line.strip() for line in f])


def path_generator(dx, dy, limit):
    return takewhile(lambda p: p[0] < limit, zip(count(0, dy), count(0, dx)))


def num_trees(grid, path):
    return sum(grid[row, col] == TREE for row, col in path)


def part_01(puzzle):
    return num_trees(puzzle, path_generator(3, 1, puzzle.height))


def part_02(puzzle):
    slopes = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]
    return math.prod(
        num_trees(puzzle, path_generator(dx, dy, puzzle.height)) for dx, dy in slopes
    )


def main():
    puzzle = read_puzzle("../input/input_03.txt")

    print(f"Part 01: {part_01(puzzle)}")
    print(f"Part 02: {part_02(puzzle)}")


if __name__ == "__main__":
    main()
