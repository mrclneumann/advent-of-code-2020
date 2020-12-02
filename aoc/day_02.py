import re
from abc import ABC, abstractmethod
from collections import namedtuple
from typing import List

PasswordRecord = namedtuple("PasswordRecord", ["lower", "upper", "char", "password"])


class PasswordPolicy(ABC):
    @abstractmethod
    def is_valid(self, record: PasswordRecord) -> bool:
        pass


class SledRentalPolicy(PasswordPolicy):
    def is_valid(self, record: PasswordRecord) -> bool:
        return record.lower <= record.password.count(record.char) <= record.upper


class TobogganCorporatePolicy(PasswordPolicy):
    def is_valid(self, record: PasswordRecord) -> bool:
        lower, upper, char, password = record
        return (password[lower - 1] == char) != (password[upper - 1] == char)


def read_puzzle(filename) -> List[PasswordRecord]:
    with open(filename) as f:
        return [parse_line(line) for line in f.readlines()]


def parse_line(line) -> PasswordRecord:
    m = re.match(r"(\d+)-(\d+) (\w): (.*)", line.strip())
    return PasswordRecord(int(m.group(1)), int(m.group(2)), m.group(3), m.group(4))


def part_01(records: List[PasswordRecord]) -> int:
    return num_valid_passwords(records, SledRentalPolicy())


def part_02(records: List[PasswordRecord]) -> int:
    return num_valid_passwords(records, TobogganCorporatePolicy())


def num_valid_passwords(records: List[PasswordRecord], policy: PasswordPolicy) -> int:
    return sum(policy.is_valid(record) for record in records)


def main():
    puzzle = read_puzzle("../input/input_02.txt")

    print(f"Part 01: {part_01(puzzle)}")
    print(f"Part 02: {part_02(puzzle)}")


if __name__ == "__main__":
    main()
