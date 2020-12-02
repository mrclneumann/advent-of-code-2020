from typing import List

import math
from itertools import combinations


def read_puzzle(filename) -> List[int]:
    with open(filename) as f:
        return [parse_line(line) for line in f.readlines()]


def parse_line(line) -> int:
    return int(line.strip())


def part_01(expense_report: List[int]) -> int:
    seen = set()

    for x in expense_report:
        y = 2020 - x

        if y in seen:
            return x * y

        seen.add(x)


def part_02(expense_report: List[int]) -> int:
    for comb in combinations(expense_report, 3):
        if sum(comb) == 2020:
            return math.prod(comb)


def main():
    puzzle = read_puzzle("../input/input_01.txt")

    print(f"Part 01: {part_01(puzzle)}")
    print(f"Part 02: {part_02(puzzle)}")


if __name__ == "__main__":
    main()
