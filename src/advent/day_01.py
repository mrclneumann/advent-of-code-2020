from typing import List

import math
from itertools import combinations


def read_input(file) -> List[int]:
    return [parse_line(line) for line in file.readlines()]


def parse_line(line) -> int:
    return int(line.strip())


def part_one(expense_report: List[int]) -> int:
    seen = set()

    for x in expense_report:
        y = 2020 - x

        if y in seen:
            return x * y

        seen.add(x)


def part_two(expense_report: List[int]) -> int:
    for comb in combinations(expense_report, 3):
        if sum(comb) == 2020:
            return math.prod(comb)
