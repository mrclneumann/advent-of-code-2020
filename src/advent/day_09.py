from itertools import islice

LEN_PREAMBLE = 25


def read_input(file):
    return [int(line.strip()) for line in file.readlines()]


def part_one(numbers):
    for window in windows(numbers, LEN_PREAMBLE + 1):
        if not is_valid(window[:-1], window[-1]):
            return window[-1]


def windows(seq, n):
    it = iter(seq)
    result = tuple(islice(it, n))
    if len(result) == n:
        yield result
    for elem in it:
        result = result[1:] + (elem,)
        yield result


def part_two(numbers):
    n = part_one(numbers)
    s = find_range_summing_to(numbers, n)

    return min(s) + max(s)


def is_valid(preamble, next_number):
    return any(next_number - x in set(preamble) - {next_number} for x in preamble)


def find_range_summing_to(numbers, n):
    i, j = 0, 1

    while True:
        if sum(numbers[i:j]) == n:
            return numbers[i:j]

        while sum(numbers[i:j]) < n:
            j += 1

        while sum(numbers[i:j]) > n:
            i += 1
