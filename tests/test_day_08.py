import pytest

from advent.day_08 import Interpreter, InfiniteLoopDetected, Instruction


@pytest.fixture()
def interpreter():
    return Interpreter()


def test_interpret_nop(interpreter):
    interpreter.interpret([Instruction("nop", 0)])

    assert interpreter.counter == 1
    assert interpreter.accumulator == 0
    assert interpreter.seen == {0}


def test_interpret_acc(interpreter):
    interpreter.interpret([Instruction("acc", 5)])

    assert interpreter.counter == 1
    assert interpreter.accumulator == 5
    assert interpreter.seen == {0}


def test_interpret_jmp(interpreter):
    interpreter.interpret([Instruction("jmp", 2)])

    assert interpreter.counter == 2
    assert interpreter.accumulator == 0
    assert interpreter.seen == {0}


def test_interpret_program_with_infinite_loop(interpreter):
    with pytest.raises(InfiniteLoopDetected):
        interpreter.interpret(
            [
                Instruction("nop", +0),
                Instruction("acc", +1),
                Instruction("jmp", +4),
                Instruction("acc", +3),
                Instruction("jmp", -3),
                Instruction("acc", -99),
                Instruction("acc", +1),
                Instruction("jmp", -4),
                Instruction("acc", +6),
            ]
        )

    assert interpreter.accumulator == 5
