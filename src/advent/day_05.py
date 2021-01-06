def read_input(file):
    return [line.strip() for line in file.readlines()]


def row(boarding_pass):
    return search(boarding_pass[:7], lambda c: c == "F")


def col(boarding_pass):
    return search(boarding_pass[7:], lambda c: c == "L")


def search(sequence, lower_half):
    lower, upper = 0, 2 ** len(sequence) - 1

    for c in sequence:
        if lower_half(c):
            upper = lower + (upper - lower) // 2
        else:
            lower = lower + (upper - lower) // 2 + 1

    return lower


def seat_id(boarding_pass):
    return row(boarding_pass) * 8 + col(boarding_pass)


def part_one(boarding_passes):
    return max(seat_id(p) for p in boarding_passes)


def part_two(boarding_passes):
    seats = {seat_id(p) for p in boarding_passes}

    for seat in range(min(seats) + 1, max(seats)):
        if all([seat not in seats, seat - 1 in seats, seat + 1 in seats]):
            return seat
