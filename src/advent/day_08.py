from dataclasses import dataclass, field


class InfiniteLoopDetected(Exception):
    pass


@dataclass
class Interpreter:
    counter: int = 0
    accumulator: int = 0
    seen: set = field(default_factory=set)

    def interpret(self, program):
        while True:
            if self.counter >= len(program):
                return self.accumulator

            if self.counter in self.seen:
                raise InfiniteLoopDetected()

            instruction, arg = program[self.counter]

            if instruction == "nop":
                self.nop()
            elif instruction == "acc":
                self.acc(arg)
            elif instruction == "jmp":
                self.jmp(arg)

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
    instruction, arg = line.strip().split()
    return instruction, int(arg)


def part_one(program):
    interpreter = Interpreter()

    try:
        interpreter.interpret(program)
    except InfiniteLoopDetected:
        return interpreter.accumulator


def part_two(program):
    for index, (instruction, arg) in enumerate(program):
        if instruction in ("nop", "jmp"):
            p = list(swap_instruction(program, index))
            interpreter = Interpreter()
            try:
                interpreter.interpret(p)
            except InfiniteLoopDetected:
                continue
            else:
                return interpreter.accumulator


def swap_instruction(program, counter):
    for index, (instruction, arg) in enumerate(program):
        if index == counter:
            instruction = "nop" if instruction == "jmp" else "jmp"
        yield instruction, arg
