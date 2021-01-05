import re
from schema import Schema, And, Use, Regex, Or


def read_input(file):
    return [parse_passport(p) for p in file.read().split("\n\n")]


def parse_passport(passport):
    return {m.group(1): m.group(2) for m in re.finditer(r"([^\s]+):([^\s]+)", passport)}


def part_one(passports):
    return sum(has_all_required_fields(p) for p in passports)


def has_all_required_fields(passport):
    return all(
        x in passport.keys() for x in ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]
    )


def part_two(passports):
    schema = Schema(
        {
            "byr": And(Use(int), lambda n: 1920 <= n <= 2002),
            "iyr": And(Use(int), lambda n: 2010 <= n <= 2020),
            "eyr": And(Use(int), lambda n: 2020 <= n <= 2030),
            "hgt": valid_height,
            "hcl": Regex(r"^#[0-9a-f]{6}$"),
            "ecl": Or("amb", "blu", "brn", "gry", "grn", "hzl", "oth"),
            "pid": Regex(r"^\d{9}$"),
        },
        ignore_extra_keys=True,
    )

    return sum(schema.is_valid(p) for p in passports)


def valid_height(hgt):
    match = re.match(r"(\d+)(cm|in)", hgt)

    if match:
        height, unit = int(match.group(1)), match.group(2)

        if unit == "cm":
            return 150 <= height <= 193

        if unit == "in":
            return 59 <= height <= 76

    return False
