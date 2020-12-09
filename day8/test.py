import pytest
from solver import parse, solve1, solve2

TESTDATA = """
nop +0
acc +1
jmp +4
acc +3
jmp -3
acc -99
acc +1
jmp -4
acc +6
"""

data = None


def test_parse():
    global data
    data = parse(TESTDATA)
    assert data == [
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


# PART 1
def test_solve1():
    solution = solve1(data)
    assert solution == 5


# PART 2
def test_solve2():
    solution = solve2(data)
    assert solution == 8
