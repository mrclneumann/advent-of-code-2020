from collections import namedtuple

from itertools import count

Schedule = namedtuple("Schedule", ["departure", "bus_lines"])


def read_input(file):
    departure = int(file.readline().strip())
    bus_lines = [
        int(x) if x.isnumeric() else None for x in file.readline().strip().split(",")
    ]
    return Schedule(departure, bus_lines)


def part_one(schedule: Schedule):
    bus_lines = set(filter(lambda x: x is not None, schedule.bus_lines))

    for t in count(schedule.departure):
        try:
            bus_line = next(filter(lambda bus: t % bus == 0, bus_lines))
        except StopIteration:
            continue
        else:
            return bus_line * (t - schedule.departure)


def part_two(schedule):
    bus_lines = filter(lambda x: x[1] is not None, enumerate(schedule.bus_lines))

    t, step = 0, 1
    for offset, bus_line in bus_lines:
        t = find(t, offset, step, bus_line)
        step *= bus_line
    return t


def find(start, offset, step, mod):
    for x in count(start, step):
        if (x + offset) % mod == 0:
            return x
