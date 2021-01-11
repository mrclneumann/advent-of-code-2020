PREAMBLE = 25


def read_input(file):
    return [int(line.strip()) for line in file.readlines()]


def part_one(numbers):
    for index, n in enumerate(numbers[PREAMBLE:], PREAMBLE):
        if not xmas(numbers[index - PREAMBLE : index], n):
            return n


def part_two(numbers):
    n = part_one(numbers)
    s = contiguous_set(numbers, n)

    return min(s) + max(s)


def xmas(numbers, n):
    return any(n - x in set(numbers).difference([n]) for x in numbers)


def contiguous_set(numbers, n):
    i, j = 0, 1

    while True:
        if sum(numbers[i:j]) == n:
            return numbers[i:j]

        while sum(numbers[i:j]) < n:
            j += 1

        while sum(numbers[i:j]) > n:
            i += 1
