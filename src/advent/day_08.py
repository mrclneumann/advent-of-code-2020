from collections import namedtuple
from typing import Iterable


class InfiniteLoopDetected(Exception):
    pass


Instruction = namedtuple("Instruction", ["opcode", "argument"])


class Interpreter:
    def __init__(self) -> None:
        self.counter = 0
        self.accumulator = 0
        self.seen = set()

    def interpret(self, program: Iterable[Instruction]):
        program = list(program)

        while True:
            if self.counter >= len(program):
                return self.accumulator

            if self.counter in self.seen:
                raise InfiniteLoopDetected()

            opcode, argument = program[self.counter]

            if opcode == "nop":
                self.nop()
            elif opcode == "acc":
                self.acc(argument)
            elif opcode == "jmp":
                self.jmp(argument)

    def nop(self):
        self.seen.add(self.counter)
        self.counter += 1

    def acc(self, n):
        self.seen.add(self.counter)
        self.accumulator += n
        self.counter += 1

    def jmp(self, n):
        self.seen.add(self.counter)
        self.counter += n


def read_input(file):
    return [parse_line(line) for line in file.readlines()]


def parse_line(line):
    name, argument = line.strip().split()
    return Instruction(name, int(argument))


def part_one(program):
    interpreter = Interpreter()

    try:
        interpreter.interpret(program)
    except InfiniteLoopDetected:
        return interpreter.accumulator


def part_two(program):
    for p in alternatives(program):
        interpreter = Interpreter()
        try:
            interpreter.interpret(p)
        except InfiniteLoopDetected:
            continue
        else:
            return interpreter.accumulator


def alternatives(program):
    for index, instruction in enumerate(program):
        if instruction.opcode in ("nop", "jmp"):
            yield program[:index] + [other(instruction)] + program[index + 1 :]


def other(instruction: Instruction):
    opcode = "nop" if instruction.opcode == "jmp" else "jmp"
    return Instruction(opcode, instruction.argument)
