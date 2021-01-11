import pytest

from advent.day_08 import Interpreter, InfiniteLoopDetected


@pytest.fixture()
def interpreter():
    return Interpreter()


def test_interpret_nop(interpreter):
    interpreter.interpret([("nop", 0)])

    assert interpreter.counter == 1
    assert interpreter.accumulator == 0
    assert interpreter.seen == {0}


def test_interpret_acc(interpreter):
    interpreter.interpret([("acc", 5)])

    assert interpreter.counter == 1
    assert interpreter.accumulator == 5
    assert interpreter.seen == {0}


def test_interpret_jmp(interpreter):
    interpreter.interpret([("jmp", 2)])

    assert interpreter.counter == 2
    assert interpreter.accumulator == 0
    assert interpreter.seen == {0}


def test_interpret_program_with_infinite_loop(interpreter):
    with pytest.raises(InfiniteLoopDetected):
        interpreter.interpret(
            [
                ("nop", +0),
                ("acc", +1),
                ("jmp", +4),
                ("acc", +3),
                ("jmp", -3),
                ("acc", -99),
                ("acc", +1),
                ("jmp", -4),
                ("acc", +6),
            ]
        )

        assert interpreter.accumulator == 5
