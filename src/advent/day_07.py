import re
from collections import defaultdict


def read_input(file):
    rules = defaultdict(dict)

    for line in file.readlines():
        if "no other bag" in line:
            continue

        matches = re.findall(r"(\d+)? ?(\S+ \S+) bag", line.strip())

        for num, color in matches[1:]:
            rules[matches[0][1]][color] = int(num)

    return rules


def root(color, rules):
    result = set()

    if color not in rules:
        return result

    result.update(rules[color])

    for parent in rules[color]:
        if parent in rules:
            result.update(root(parent, rules))

    return result


def invert(rules):
    d = defaultdict(set)

    for parent, children in rules.items():
        for child in children.keys():
            d[child].add(parent)

    return d


def count(color, rules):
    if color not in rules:
        return 0

    return sum(num + num * count(color, rules) for color, num in rules[color].items())


def part_one(rules):
    return len(root("shiny gold", invert(rules)))


def part_two(rules):
    return count("shiny gold", rules)
