from functools import reduce


def read_input(file):
    return [parse_group(group) for group in file.read().strip().split("\n\n")]


def parse_group(group):
    return group.strip().split("\n")


def union(group):
    return len(reduce(lambda a, b: a | b, map(set, group)))


def intersection(group):
    return len(reduce(lambda a, b: a & b, map(set, group)))


def part_one(groups):
    return sum(union(group) for group in groups)


def part_two(groups):
    return sum(intersection(group) for group in groups)
