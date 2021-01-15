class InfiniteLoopDetected(Exception):
    pass


class Interpreter:
    def __init__(self) -> None:
        self.counter = 0
        self.accumulator = 0
        self.seen = set()

    def interpret(self, program):
        program = list(program)

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
    for p in alternatives(program):
        interpreter = Interpreter()
        try:
            interpreter.interpret(p)
        except InfiniteLoopDetected:
            continue
        else:
            return interpreter.accumulator


def alternatives(program):
    for index, (instruction, arg) in enumerate(program):
        if instruction in ("nop", "jmp"):
            yield program[:index] + [(other(instruction), arg)] + program[index + 1 :]


def other(instruction):
    return "nop" if instruction == "jmp" else "jmp"
