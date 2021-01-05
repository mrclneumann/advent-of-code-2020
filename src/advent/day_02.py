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


def read_input(file) -> List[PasswordRecord]:
    return [parse_line(line) for line in file.readlines()]


def parse_line(line) -> PasswordRecord:
    m = re.match(r"(\d+)-(\d+) (\w): (.*)", line.strip())
    return PasswordRecord(int(m.group(1)), int(m.group(2)), m.group(3), m.group(4))


def part_one(records: List[PasswordRecord]) -> int:
    return num_valid_passwords(records, SledRentalPolicy())


def part_two(records: List[PasswordRecord]) -> int:
    return num_valid_passwords(records, TobogganCorporatePolicy())


def num_valid_passwords(records: List[PasswordRecord], policy: PasswordPolicy) -> int:
    return sum(policy.is_valid(record) for record in records)
