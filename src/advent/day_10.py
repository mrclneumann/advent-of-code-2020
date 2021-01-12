from collections import Counter


def read_input(file):
    return [int(line.strip()) for line in file.readlines()]


def part_one(adapters):
    diff = count_distances([0] + sorted(adapters) + [max(adapters) + 3])
    return diff[1] * diff[3]


def count_distances(adapters):
    return Counter(distances(adapters))


def distances(adapters):
    return [a - b for a, b in zip(adapters[1:], adapters)]


def part_two(adapters):
    adapters = [0] + sorted(adapters) + [max(adapters) + 3]
    return count_arrangements(adapters)


def count_arrangements(adapters):
    arr = {0: 1}

    for adapter in adapters[1:]:
        arr[adapter] = sum(arr.get(adapter - i, 0) for i in range(1, 4))

    return arr[adapters[-1]]
