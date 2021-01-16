from collections import namedtuple

from sympy import cos, rad, sin

Instruction = namedtuple("Instruction", ["action", "value"])

instruction_table = {
    "N": "north",
    "S": "south",
    "E": "east",
    "W": "west",
    "L": "left",
    "R": "right",
    "F": "forward",
}


def read_input(file):
    return [parse_line(line) for line in file.readlines()]


def parse_line(line):
    action, value = line[0], line[1:]
    return Instruction(instruction_table[action], int(value))


def part_one(instructions):
    return interpret(instructions, Ship())


def part_two(instructions):
    return interpret(instructions, Waypoint())


def interpret(instructions, item):
    for action, value in instructions:
        item.__getattribute__(action)(value)

    return item.manhattan()


class Ship:
    def __init__(self, x=0, y=0) -> None:
        self.x = x
        self.y = y

        self.degrees = 0

    @property
    def dx(self):
        return cos(rad(self.degrees))

    @property
    def dy(self):
        return sin(rad(self.degrees))

    @property
    def position(self):
        return self.x, self.y

    def manhattan(self):
        return sum(abs(x) for x in self.position)

    def north(self, steps):
        self.y += steps

    def south(self, steps):
        self.y -= steps

    def east(self, steps):
        self.x += steps

    def west(self, steps):
        self.x -= steps

    def left(self, degrees):
        self.degrees += degrees

    def right(self, degrees):
        self.degrees -= degrees

    def forward(self, steps):
        self.x += steps * self.dx
        self.y += steps * self.dy


class Waypoint(Ship):
    def __init__(self, x=10, y=1) -> None:
        super().__init__(x, y)
        self.ship = Ship()

    def left(self, degrees):
        self.right(360 - degrees % 360)

    def right(self, degrees):
        if degrees > 0:
            self.x, self.y = self.y, -self.x
            self.right(degrees - 90)

    def forward(self, value):
        self.ship.x = self.ship.x + value * self.x
        self.ship.y = self.ship.y + value * self.y

    def manhattan(self):
        return sum(abs(x) for x in self.ship.position)
