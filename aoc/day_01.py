from typing import List

import math
from itertools import combinations

from aoc.utils import read_list


def part_01(expense_report: List[int]):
    seen = set()

    for x in expense_report:
        y = 2020 - x

        if y in seen:
            return x * y

        seen.add(x)


def part_02(expense_report: List[int]):
    for comb in combinations(expense_report, 3):
        if sum(comb) == 2020:
            return math.prod(comb)


def main():
    with open("../input/input_01.txt") as f:
        puzzle = read_list(f)

    print(f"Part 01: {part_01(puzzle)}")
    print(f"Part 02: {part_02(puzzle)}")


if __name__ == "__main__":
    main()
